#!/usr/bin/env python3
"""
build.py -- Parakeet ops dashboard data build.

Turns the raw RentViewer warehouse pulls in pipeline/raw/ into a single
versioned payload at data/dashboard.json, plus data/registry_audit.json
so every property name the warehouse handed us has a visible disposition.

    python3 pipeline/build.py [--raw pipeline/raw] [--out data]

Two rules shape everything below:

  REPORTABLE GATE. A community appears only if the Property Data Sheet
  (`vwr VW_PDS_V2`, exported to pipeline/raw/pds_reportable.json) marks it
  Reportable = Yes. That sheet is Austin's own source of truth, and it settles
  what the warehouse alone cannot: which of ~150 propertyName values are real
  reportable communities rather than funds, sub-ledgers or dead records.

  TWO PERIODS, BOTH REAL. Every period-sensitive figure is emitted twice:
  once for the last CLOSED month and once LIVE through today. Rent bills on
  the 1st and is late after the grace day, so live receivables are the
  actionable number even though live collections are structurally low. The UI
  toggles between them; neither is hidden.

See docs/ARCHITECTURE.md for the refresh loop.
"""
import argparse
import json
import os
import re
import sys
from calendar import monthrange
from collections import Counter, defaultdict
from datetime import date, datetime, timezone

SCHEMA_VERSION = 8

# Warehouse model prefixes, and the raw file each one arrives in.
SOURCES = {
    "occupancy": ("occupancy_by_property_month.json", "VW_Rental_Unit_Listing."),
    "unit_types": ("unit_listing_by_type.json", "VW_Rental_Unit_Listing."),
    "ar": ("ar_by_property_month.json", "VW_Aged_Receivables."),
    "rentroll": ("rentroll_by_property_month.json", "VW_Summary_Rent_Roll."),
    "moves": ("moves_by_property_month.json", "VW_MoveIns_MoveOuts."),
    "financials": ("financials_by_property_month.json", "VW_Budget_Comparison."),
}

REPORTABLE_FILE = "pds_reportable.json"

# Property-level grain is all the warehouse will serve: adding unitName or
# glAccountName as a dimension times out at 60s even scoped to one property.
# Unit-level and account-level detail therefore comes from Rent Manager report
# exports instead, keyed on the property short name.
RM_SOURCES = {
    "rm_rent_roll": "rm_rent_roll.json",
    "rm_ar_detail": "rm_ar_detail.json",
    # Move history carries LeasesMoveOutDate, which is the only true anchor for
    # "how long has this been sitting", and CustomerStatus, which separates a
    # former resident's balance from a current one's.
    "rm_moves_detail": "rm_moves_detail.json",
    # Asset listing carries AssetStatusesName: the home lifecycle from Ordered
    # through Needs Rehab, For Sale and Rental.
    "rm_asset_listing": "rm_asset_listing.json",
}

# Extra warehouse pulls carrying the GL category measures. Same grain as the
# main financials pull, so they merge on (propertyName, endDate).
CATEGORY_SOURCES = {
    "expense_categories": ("expense_categories_by_property_month.json", "VW_Budget_Comparison."),
    "income_categories": ("income_categories_by_property_month.json", "VW_Budget_Comparison."),
}

# Rent is billed on the 1st. After this day of the month, unpaid current-month
# charges are late, which is why the live view exists at all.
DEFAULT_GRACE_DAY = 5


def die(msg):
    print("[build] ERROR: " + msg, file=sys.stderr)
    sys.exit(1)


def log(msg):
    print("[build] " + msg, flush=True)


def num(v):
    """Warehouse returns numerics as float, int, numeric string, or null."""
    if v is None or v == "":
        return 0.0
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def rnd(v, places=1):
    return round(v + 0.0, places)


def month_of(value):
    """Normalize reportMonth ('2026-09') or an ISO timestamp to 'YYYY-MM'."""
    if not value:
        return None
    s = str(value)
    m = re.match(r"^(\d{4})-(\d{2})", s)
    return "%s-%s" % (m.group(1), m.group(2)) if m else None


def months_between(a, b):
    ay, am = int(a[:4]), int(a[5:7])
    by, bm = int(b[:4]), int(b[5:7])
    return (by - ay) * 12 + (bm - am)


def count_str(v):
    return "{:,}".format(int(round(v or 0)))


def money(v):
    v = v or 0
    if abs(v) >= 1_000_000:
        return "$%.2fM" % (v / 1_000_000)
    if abs(v) >= 1_000:
        return "$%.0fK" % (v / 1_000)
    return "$%.0f" % v


def load_raw(raw_dir):
    """Read every source file, returning {key: (rows, prefix)}."""
    out = {}
    missing = []
    for key, (fname, prefix) in SOURCES.items():
        path = os.path.join(raw_dir, fname)
        if not os.path.exists(path):
            missing.append(fname)
            continue
        with open(path) as f:
            blob = json.load(f)
        rows = blob.get("rows", [])
        out[key] = (rows, prefix)
        log("loaded %-38s %5d rows" % (fname, len(rows)))
    if missing:
        die("missing raw pulls: %s\nRun the queries in pipeline/queries.json first."
            % ", ".join(missing))
    return out


def _median(values):
    """Middle value, or None for an empty list. Used where one very old row
    would drag a mean past anything a manager could act on."""
    vals = sorted(values)
    return vals[len(vals) // 2] if vals else None


def load_envelope(raw_dir, fname):
    """
    Read a raw file whole, without unwrapping it to a row list.

    `load_optional` returns blob["rows"] when it finds one, which is right for
    the warehouse and Rent Manager pulls but wrong for a staged source whose
    manifest matters as much as its rows.
    """
    path = os.path.join(raw_dir, fname)
    if not os.path.exists(path):
        log("NOTE  %s absent; the drill-in it feeds will be empty" % fname)
        return None
    with open(path) as f:
        return json.load(f)


def load_optional(raw_dir, fname):
    """Read a raw file that the build can survive without."""
    path = os.path.join(raw_dir, fname)
    if not os.path.exists(path):
        log("NOTE  %s absent; the drill-in it feeds will be empty" % fname)
        return None
    with open(path) as f:
        blob = json.load(f)
    rows = blob.get("rows", blob) if isinstance(blob, dict) else blob
    log("loaded %-38s %5d rows" % (fname, len(rows)))
    return rows


def load_reportable(raw_dir):
    """
    The Reportable = Yes roster from the Property Data Sheet.

    Returns (lookup, rows) where lookup maps every name variant a PDS row
    publishes -- Property Name, Community, Short Name -- to that row. The
    warehouse keys on Property Name in practice, but the other two are cheap
    insurance against a rename.
    """
    path = os.path.join(raw_dir, REPORTABLE_FILE)
    if not os.path.exists(path):
        die("missing %s.\nExport the `vwr VW_PDS_V2` sheet of the Property Data "
            "Sheet (Reportable = Yes rows) to that path. See docs/ARCHITECTURE.md."
            % path)
    with open(path) as f:
        rows = json.load(f)
    if not rows:
        die("%s is empty; refusing to build a dashboard with no reportable communities"
            % REPORTABLE_FILE)
    lookup = {}
    for r in rows:
        for key in ("property_name", "community", "short_name"):
            v = (r.get(key) or "").strip().lower()
            if v and v not in lookup:
                lookup[v] = r
    log("loaded %-38s %5d reportable communities" % (REPORTABLE_FILE, len(rows)))
    return lookup, rows


# ---------------------------------------------------------------- registry ---

class Registry:
    """Decides what each warehouse propertyName is, and records why."""

    def __init__(self, cfg, reportable):
        self.cfg = cfg
        self.reportable = reportable
        self.sold = {}
        for entry in cfg.get("sold", []):
            for name in entry["match"]:
                self.sold[name.lower()] = entry
        self.roll_up = {e["match"].lower(): e for e in cfg.get("roll_up", [])}
        self.segments = cfg.get("segments", {})
        self.thresholds = cfg["thresholds"]

        self.ut_class = {}
        self.ut_rentable = {}
        for group, buckets in cfg["unit_types"].items():
            for bucket, names in buckets.items():
                for n in names:
                    self.ut_class[n] = group
                    self.ut_rentable[n] = bucket
        # Home lifecycle. `home_pipeline` is in display order; matching picks
        # the most constrained rule that fits rather than the first, so the
        # order here stays a presentation choice and never a correctness one.
        self.rtm_field = cfg.get("_rtm_field", "udf_551")
        self.home_pipeline = cfg.get("home_pipeline", {})
        self.home_stage_order = list(self.home_pipeline.keys())

        # Eviction stage -> funnel phase, keyed lowercase because the tracker's
        # spelling drifts ("Court" and "Court: Complaint" both appear).
        self.evict_phase = {}
        self.evict_order = []
        self.evict_label = {}
        for key, spec in cfg.get("eviction_stages", {}).items():
            self.evict_order.append(key)
            self.evict_label[key] = spec["label"]
            for st in spec.get("stages", []):
                self.evict_phase[st.strip().lower()] = key
        self.evict_label["other"] = "Stage not mapped"
        self.unmapped_stages = set()

        self.audit = {}

    def home_stage(self, status, rtm):
        """
        (key, label) for where a home sits in the pipeline, or (None, None) if
        it is already earning or settled.

        `rtm` is the Ready to Market flag. Only an explicit Yes counts; blank
        is treated as not ready, because a home nobody has marked is a home
        nobody has confirmed.
        """
        status = (status or "").strip()
        best = None
        for key, spec in self.home_pipeline.items():
            constraints = 0
            if "statuses" in spec:
                if status not in spec["statuses"]:
                    continue
                constraints += 1
            if "rtm" in spec:
                if bool(spec["rtm"]) != bool(rtm):
                    continue
                constraints += 1
            if not constraints:
                continue
            if best is None or constraints > best[0]:
                best = (constraints, key, spec["label"])
        if best is None:
            return None, None
        return best[1], best[2]

    def eviction_phase(self, stage):
        """(key, label) for a tracker stage; unmapped stages are recorded."""
        key = self.evict_phase.get((stage or "").strip().lower())
        if key is None:
            if stage:
                self.unmapped_stages.add(stage)
            return "other", self.evict_label["other"]
        return key, self.evict_label[key]

    def unit_type(self, name):
        """(group, bucket) for a unit type; unknown types count as rentable MH."""
        if name in self.ut_class:
            return self.ut_class[name], self.ut_rentable[name]
        return "UNKNOWN", "rentable"

    def classify(self, name):
        """
        Return (disposition, canonical_name, detail).

          keep      -- Reportable = Yes; its own row
          roll_up   -- not reportable itself, but money attributes to a
                       reportable parent (utility and home-sales sub-ledgers)
          drop      -- excluded; detail says why
        """
        low = name.strip().lower()

        # A sold property stays out even while the PDS still says Reportable,
        # because the PDS lags a disposition by design. This is the one place
        # the gate is overridden, and it is deliberate and listed.
        if low in self.sold:
            e = self.sold[low]
            return "drop", None, "Sold: %s" % e["reason"]

        pds = self.reportable.get(low)
        if pds:
            return "keep", (pds.get("property_name") or name), ""

        if low in self.roll_up:
            e = self.roll_up[low]
            parent = e["parent"]
            if parent.strip().lower() in self.reportable:
                return "roll_up", parent, "%s sub-ledger" % e["kind"]
            return "drop", None, ("%s sub-ledger whose parent %s is not Reportable"
                                  % (e["kind"], parent))

        return "drop", None, "Not marked Reportable = Yes in the Property Data Sheet"

    def record(self, name, disposition, canonical, detail):
        self.audit[name] = {
            "disposition": disposition,
            "canonical": canonical,
            "reason": detail,
        }


# ------------------------------------------------------------------- build ---

def build(raw_dir, out_dir, registry_path):
    with open(registry_path) as f:
        cfg = json.load(f)
    reportable, reportable_rows = load_reportable(raw_dir)
    reg = Registry(cfg, reportable)

    raw = load_raw(raw_dir)

    # ---- reporting calendar ----
    occ_rows, OP = raw["occupancy"]
    months = sorted({m for m in (month_of(r.get(OP + "reportMonth")) for r in occ_rows) if m})
    if not months:
        die("no reportMonth values found in the occupancy pull")
    live_month = months[-1]
    closed_month = months[-2] if len(months) > 1 else live_month

    today = date.today()
    live_day = today.day if today.strftime("%Y-%m") == live_month else monthrange(
        int(live_month[:4]), int(live_month[5:7]))[1]
    days_in_live = monthrange(int(live_month[:4]), int(live_month[5:7]))[1]
    grace_day = cfg.get("grace_day", DEFAULT_GRACE_DAY)

    log("periods %s .. %s  (closed: %s, live: %s day %d of %d)"
        % (months[0], live_month, closed_month, live_month, live_day, days_in_live))

    # ---- classify every propertyName the warehouse returned ----
    all_names = set()
    for key in ("occupancy", "ar", "rentroll", "moves", "financials"):
        rows, P = raw[key]
        for r in rows:
            n = r.get(P + "propertyName")
            if n:
                all_names.add(n)
    for r in raw["unit_types"][0]:
        n = r.get(raw["unit_types"][1] + "propertyName")
        if n:
            all_names.add(n)

    resolve = {}
    for name in sorted(all_names):
        disp, canon, why = reg.classify(name)
        reg.record(name, disp, canon, why)
        resolve[name] = (disp, canon)

    # Reportable communities the warehouse never mentions: a real gap worth
    # surfacing, not a silent zero row.
    seen_lower = {n.strip().lower() for n in all_names}
    absent = [r for r in reportable_rows
              if not any((r.get(k) or "").strip().lower() in seen_lower
                         for k in ("property_name", "community", "short_name"))]

    def target(name):
        """Where a row's MONEY lands, or None if excluded."""
        disp, canon = resolve.get(name, ("drop", None))
        return canon if disp in ("keep", "roll_up") else None

    def target_units(name):
        """
        Where a row's LOTS land, or None if they must be ignored.

        Money and lots do not merge the same way. A utility sub-ledger bills
        against lots already counted on its parent, so adding its unit count
        inflates the denominator and halves the occupancy it is meant to
        explain. Only a `keep` record contributes lots.
        """
        disp, canon = resolve.get(name, ("drop", None))
        return canon if disp == "keep" else None

    kept = sorted({c for c in (target_units(n) for n in resolve) if c})
    rolled = [n for n, (d, _) in resolve.items() if d == "roll_up"]
    log("properties: %d names -> %d reportable communities (%d dropped, %d rolled up)"
        % (len(resolve), len(kept),
           sum(1 for d, _ in resolve.values() if d == "drop"), len(rolled)))

    # ---- aggregation passes ------------------------------------------------

    occ = defaultdict(lambda: defaultdict(lambda: {"units": 0.0, "vac_days": 0.0,
                                                   "avail_days": 0.0, "actual_rent": 0.0,
                                                   "market_rent": 0.0}))
    for r in occ_rows:
        t = target_units(r.get(OP + "propertyName"))
        mo = month_of(r.get(OP + "reportMonth"))
        if not t or not mo:
            continue
        d = occ[t][mo]
        d["units"] += num(r.get(OP + "unitCount"))
        d["vac_days"] += num(r.get(OP + "daysVacant"))
        d["avail_days"] += num(r.get(OP + "daysAvailable"))
        d["actual_rent"] += num(r.get(OP + "totalActualRent"))
        d["market_rent"] += num(r.get(OP + "totalMarketRent"))

    def occ_pct(d):
        # From unit-days, not an average of percentages, so a 424-lot park
        # outweighs a 19-lot one.
        return (d["avail_days"] - d["vac_days"]) / d["avail_days"] * 100 if d["avail_days"] else 0.0

    ut_rows, UP = raw["unit_types"]
    vac_comp = defaultdict(lambda: defaultdict(lambda: {"units": 0.0, "vac_days": 0.0,
                                                        "avail_days": 0.0}))
    type_mix = defaultdict(lambda: defaultdict(float))
    unknown_types = set()
    for r in ut_rows:
        t = target_units(r.get(UP + "propertyName"))
        if not t:
            continue
        tname = r.get(UP + "unitTypeName") or "TBD"
        group, bucket = reg.unit_type(tname)
        if group == "UNKNOWN":
            unknown_types.add(tname)
        d = vac_comp[t][tname]
        d["units"] += num(r.get(UP + "unitCount"))
        d["vac_days"] += num(r.get(UP + "daysVacant"))
        d["avail_days"] += num(r.get(UP + "daysAvailable"))
        type_mix[t][group] += num(r.get(UP + "unitCount"))

    ar_rows, AP = raw["ar"]
    ar = defaultdict(lambda: defaultdict(lambda: {"total": 0.0, "b0_30": 0.0, "b31_60": 0.0,
                                                  "b61_90": 0.0, "b90p": 0.0, "accounts": 0.0}))
    rolled_ar = defaultdict(float)
    for r in ar_rows:
        name = r.get(AP + "propertyName")
        t = target(name)
        mo = month_of(r.get(AP + "reportMonth"))
        if not t or not mo:
            continue
        d = ar[t][mo]
        v = num(r.get(AP + "agedReceivablesTotal"))
        d["total"] += v
        d["b0_30"] += num(r.get(AP + "current0to30"))
        d["b31_60"] += num(r.get(AP + "days31to60"))
        d["b61_90"] += num(r.get(AP + "days61to90"))
        d["b90p"] += num(r.get(AP + "over90Days"))
        d["accounts"] += num(r.get(AP + "customersWithBalance"))
        if resolve.get(name, ("drop", None))[0] == "roll_up" and mo == closed_month:
            rolled_ar[name] += v

    rr_rows, RP = raw["rentroll"]
    rr = defaultdict(lambda: defaultdict(lambda: {"charged": 0.0, "paid": 0.0, "rent": 0.0,
                                                  "vac_loss": 0.0, "ltl": 0.0, "debit": 0.0}))
    for r in rr_rows:
        t = target(r.get(RP + "propertyName"))
        mo = month_of(r.get(RP + "reportMonth"))
        if not t or not mo:
            continue
        d = rr[t][mo]
        d["charged"] += num(r.get(RP + "totalCharged"))
        d["paid"] += num(r.get(RP + "totalPaid"))
        d["rent"] += num(r.get(RP + "rentCharges"))
        d["vac_loss"] += num(r.get(RP + "vacancyLoss"))
        d["ltl"] += num(r.get(RP + "lossToLease"))
        d["debit"] += num(r.get(RP + "debitBalances"))

    def coll_pct(d):
        return d["paid"] / d["charged"] * 100 if d["charged"] else 0.0

    mv_rows, MP = raw["moves"]
    mv = defaultdict(lambda: defaultdict(lambda: {"ins": 0.0, "outs": 0.0}))
    for r in mv_rows:
        t = target(r.get(MP + "propertyName"))
        mo = month_of(r.get(MP + "month"))
        if not t or not mo:
            continue
        mv[t][mo]["ins"] += num(r.get(MP + "moveIns"))
        mv[t][mo]["outs"] += num(r.get(MP + "moveOuts"))

    fin_rows, FP = raw["financials"]
    fin = defaultdict(lambda: defaultdict(lambda: {"rev": 0.0, "rev_bud": 0.0, "opex": 0.0,
                                                   "opex_bud": 0.0, "noi": 0.0, "noi_bud": 0.0}))
    for r in fin_rows:
        t = target(r.get(FP + "propertyName"))
        mo = month_of(r.get(FP + "endDate"))
        if not t or not mo:
            continue
        d = fin[t][mo]
        d["rev"] += num(r.get(FP + "totalRevenue"))
        d["rev_bud"] += num(r.get(FP + "totalRevenueBudget"))
        d["opex"] += num(r.get(FP + "totalOperatingExpenses"))
        d["opex_bud"] += num(r.get(FP + "totalOperatingExpensesBudget"))
        d["noi"] += num(r.get(FP + "noi"))
        d["noi_bud"] += num(r.get(FP + "noiBudget"))

    # ---- GL category measures (merge on propertyName + month) --------------
    CAT_MEASURES = {
        "repairs_maintenance": "repairsMaintenanceExpense",
        "repairs_maintenance_budget": "repairsMaintenanceBudget",
        "utilities": "utilitiesExpense",
        "utilities_budget": "utilitiesExpenseBudget",
        "utility_reimbursements": "utilityReimbursements",
        "taxes": "taxesExpense",
        "insurance": "insuranceExpense",
        "payroll_management": "payrollManagementExpense",
        "lot_rent_rental": "lotRentRentalIncome",
        "ancillary_fees": "ancillaryFeeIncome",
        "non_operating_income": "nonOperatingIncome",
        "legal_professional": "legalProfessionalExpense",
        "capex": "capexExpense",
        "debt_service": "debtServiceExpense",
    }
    cats = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
    for key, (fname, CP) in CATEGORY_SOURCES.items():
        rows = load_optional(raw_dir, fname)
        if not rows:
            continue
        for r in rows:
            t = target(r.get(CP + "propertyName"))
            mo = month_of(r.get(CP + "endDate"))
            if not t or not mo:
                continue
            for out_name, measure in CAT_MEASURES.items():
                if CP + measure in r:
                    cats[t][mo][out_name] += num(r.get(CP + measure))

    def expense_split(name, mo):
        """
        Controllable versus not, plus utility recapture.

        Controllable is total opex minus the three non-controllable categories,
        so it reconciles to opex exactly and `other_controllable` absorbs admin,
        travel and bad debt without a measure for each.
        """
        c = cats.get(name, {}).get(mo, {})
        f = fin.get(name, {}).get(mo)
        opex = f["opex"] if f else 0.0
        util = c.get("utilities", 0.0)
        tax = c.get("taxes", 0.0)
        ins = c.get("insurance", 0.0)
        non_ctrl = util + tax + ins
        rm = c.get("repairs_maintenance", 0.0)
        payroll = c.get("payroll_management", 0.0)
        legal = c.get("legal_professional", 0.0)
        ctrl = opex - non_ctrl
        util_income = c.get("utility_reimbursements", 0.0)
        return {
            "opex": rnd(opex, 0),
            "controllable": rnd(ctrl, 0),
            "non_controllable": rnd(non_ctrl, 0),
            "controllable_share": rnd(ctrl / opex * 100) if opex else 0.0,
            "repairs_maintenance": rnd(rm, 0),
            "repairs_maintenance_budget": rnd(c.get("repairs_maintenance_budget", 0.0), 0),
            "payroll_management": rnd(payroll, 0),
            "legal_professional": rnd(legal, 0),
            "other_controllable": rnd(ctrl - rm - payroll - legal, 0),
            "utilities": rnd(util, 0),
            "utilities_budget": rnd(c.get("utilities_budget", 0.0), 0),
            "utility_reimbursements": rnd(util_income, 0),
            "utility_net": rnd(util_income - util, 0),
            "utility_recapture_pct": rnd(util_income / util * 100) if util else None,
            "taxes": rnd(tax, 0),
            "insurance": rnd(ins, 0),
            "lot_rent_rental": rnd(c.get("lot_rent_rental", 0.0), 0),
            "ancillary_fees": rnd(c.get("ancillary_fees", 0.0), 0),
            "non_operating_income": rnd(c.get("non_operating_income", 0.0), 0),
            "capex": rnd(c.get("capex", 0.0), 0),
            "debt_service": rnd(c.get("debt_service", 0.0), 0),
        }

    def expense_split_ytd(name, through):
        """Same split summed across the year to date, through `through`."""
        year = through[:4]
        acc = defaultdict(float)
        for mo in sorted(cats.get(name, {})):
            if mo[:4] == year and mo <= through:
                blk = expense_split(name, mo)
                for k, v in blk.items():
                    if isinstance(v, (int, float)) and v is not None and not k.endswith("_pct") \
                       and not k.endswith("_share"):
                        acc[k] += v
        out = {k: rnd(v, 0) for k, v in acc.items()}
        out["controllable_share"] = rnd(out.get("controllable", 0) / out["opex"] * 100) if out.get("opex") else 0.0
        out["utility_recapture_pct"] = (rnd(out.get("utility_reimbursements", 0) / out["utilities"] * 100)
                                        if out.get("utilities") else None)
        return out

    # ---- per-community rows, one block per period --------------------------

    def community_period(name, mo, prev_mo):
        """Everything period-sensitive for one community in one month."""
        o = occ[name].get(mo)
        a = ar[name].get(mo)
        r = rr[name].get(mo)
        f = fin[name].get(mo)
        m = mv[name].get(mo, {})
        if not any((o, a, r, f)):
            return None

        units = int(o["units"]) if o else 0
        occupancy = occ_pct(o) if o else 0.0
        o_prev = occ[name].get(prev_mo) if prev_mo else None
        ar_total = a["total"] if a else 0.0
        over90 = a["b90p"] if a else 0.0
        charged = r["charged"] if r else 0.0
        paid = r["paid"] if r else 0.0

        ytd = {"rev": 0.0, "rev_bud": 0.0, "noi": 0.0, "noi_bud": 0.0}
        for k, d in fin[name].items():
            if k[:4] == mo[:4] and k <= mo:
                ytd["rev"] += d["rev"]
                ytd["rev_bud"] += d["rev_bud"]
                ytd["noi"] += d["noi"]
                ytd["noi_bud"] += d["noi_bud"]

        return {
            "units": units,
            "occupied": int(round(units * occupancy / 100)) if units else 0,
            "occupancy": rnd(occupancy),
            "occupancy_prev": rnd(occ_pct(o_prev)) if o_prev else None,
            "actual_rent": rnd(o["actual_rent"], 0) if o else 0,
            "market_rent": rnd(o["market_rent"], 0) if o else 0,
            "ar_total": rnd(ar_total, 0),
            "ar_0_30": rnd(a["b0_30"], 0) if a else 0,
            "ar_31_60": rnd(a["b31_60"], 0) if a else 0,
            "ar_61_90": rnd(a["b61_90"], 0) if a else 0,
            "ar_90_plus": rnd(over90, 0),
            "ar_over90_share": rnd(over90 / ar_total * 100) if ar_total else 0.0,
            "ar_past_due_30plus": rnd(ar_total - (a["b0_30"] if a else 0), 0),
            "ar_accounts": int(a["accounts"]) if a else 0,
            "ar_per_unit": rnd(ar_total / units, 0) if units else 0,
            "charged": rnd(charged, 0),
            "paid": rnd(paid, 0),
            "outstanding": rnd(charged - paid, 0),
            "collection_pct": rnd(coll_pct(r)) if r else 0.0,
            "vacancy_loss": rnd(r["vac_loss"], 0) if r else 0,
            "loss_to_lease": rnd(r["ltl"], 0) if r else 0,
            "move_ins": int(m.get("ins", 0)),
            "move_outs": int(m.get("outs", 0)),
            "revenue": rnd(f["rev"], 0) if f else 0,
            "revenue_budget": rnd(f["rev_bud"], 0) if f else 0,
            "opex": rnd(f["opex"], 0) if f else 0,
            "opex_budget": rnd(f["opex_bud"], 0) if f else 0,
            "noi": rnd(f["noi"], 0) if f else 0,
            "noi_budget": rnd(f["noi_bud"], 0) if f else 0,
            "noi_margin": rnd(f["noi"] / f["rev"] * 100) if f and f["rev"] else 0.0,
            "ytd_revenue": rnd(ytd["rev"], 0),
            "ytd_revenue_budget": rnd(ytd["rev_bud"], 0),
            "ytd_noi": rnd(ytd["noi"], 0),
            "ytd_noi_budget": rnd(ytd["noi_bud"], 0),
        }

    # ---- Rent Manager detail, keyed by property short name -----------------
    # These feed the drill-ins the warehouse cannot serve. Everything here is
    # keyed on short name, because that is what both the PDS roster and the RM
    # reports agree on. Resident names come back redacted by the connector, so
    # a unit number plus an account id is the whole identity.
    # The two RM reports do not agree on how they name a property: the rent roll
    # carries EntitiesName plus EntitiesEntityID, while aged receivables carries
    # EntitiesShortName. Resolve on any of the three rather than picking one.
    rm_lookup = {}
    for c_name in kept:
        pds = reportable.get(c_name.strip().lower(), {})
        for k in (pds.get("short_name"), pds.get("property_name"),
                  pds.get("community"), c_name):
            if k and str(k).strip():
                rm_lookup[str(k).strip().upper()] = c_name

    id_map = {}
    ids_path = os.path.join(raw_dir, "rm_property_ids.json")
    if os.path.exists(ids_path):
        with open(ids_path) as f:
            blob = json.load(f)
        for pid, short in (blob.get("id_to_short") or {}).items():
            c_name = rm_lookup.get(str(short).strip().upper())
            if c_name:
                id_map[str(pid)] = c_name

    def rm_community(row):
        """Which reportable community an RM report row belongs to, or None."""
        for field in ("EntitiesEntityID", "ChargesEntityID", "PrimaryLeasePropertyEntityID"):
            v = row.get(field)
            if v is not None and str(v) in id_map:
                return id_map[str(v)]
        for field in ("EntitiesName", "EntitiesShortName", "PrimaryLeasePropertyShortName"):
            v = row.get(field)
            if v and str(v).strip().upper() in rm_lookup:
                return rm_lookup[str(v).strip().upper()]
        return None

    reason_of = {}
    reason_meta = {}
    for rk, spec in cfg.get("vacancy_reasons", {}).items():
        reason_meta[rk] = {"label": spec["label"], "actionable": spec.get("actionable", True)}
        for t in spec["types"]:
            reason_of[t] = rk

    # ---- vacancy aging, from the last move-out on each unit ----------------
    # An asset's service start date says when it entered the fleet, not when it
    # went empty, so aging has to come from the lease history. A unit's most
    # recent move-out is the day it became available.
    today_d = date.today()
    last_out = {}
    cust_status = {}
    moves_rows = load_optional(raw_dir, RM_SOURCES["rm_moves_detail"]) or []
    for r in moves_rows:
        cname = rm_community(r)
        if not cname:
            continue
        acct = r.get("AccountsAccountID")
        if acct is not None and r.get("CustomerStatus"):
            cust_status[acct] = r["CustomerStatus"]
        mo_out = (r.get("LeasesMoveOutDate") or "")[:10]
        unit = str(r.get("SubEntitiesName") or "")
        if not mo_out or not unit:
            continue
        key = (cname, unit)
        if key not in last_out or mo_out > last_out[key]:
            last_out[key] = mo_out

    def days_since(iso):
        try:
            y, m, dd = (int(x) for x in iso.split("-")[:3])
            return (today_d - date(y, m, dd)).days
        except (ValueError, TypeError, AttributeError):
            return None

    AGE_BANDS = [(30, "0-30 days"), (60, "31-60 days"), (90, "61-90 days"),
                 (180, "91-180 days"), (365, "181-365 days"), (10**6, "Over a year")]

    def age_band(days):
        if days is None:
            return "Unknown"
        for limit, label in AGE_BANDS:
            if days <= limit:
                return label
        return "Over a year"

    # ---- home lifecycle status, from the asset listing ---------------------
    asset_rows = load_optional(raw_dir, RM_SOURCES["rm_asset_listing"]) or []
    assets_by_comm = defaultdict(list)
    asset_statuses = Counter()
    for r in asset_rows:
        cname = rm_community(r)
        if not cname:
            continue
        status = (r.get("AssetStatusesName") or "Unknown").strip()
        atype = (r.get("AssetTypesName") or "").strip()
        # Structures are not homes; the pipeline view is about sellable and
        # rentable housing stock.
        if atype in ("Other Perm Structure", "Office", "Laundry Facility",
                     "Commercial Building"):
            continue
        start = (r.get("AssetsServiceStartDate") or "")[:10]
        # Ready to Market lives in a user-defined field, not a status. Only an
        # explicit "Yes" counts; see the registry note on how udf_551 was
        # identified and why udf_325 is not it.
        udf = r.get("AdditionalColumns") or {}
        rtm = str(udf.get(reg.rtm_field) or "").strip().lower() == "yes"
        stage, stage_label = reg.home_stage(status, rtm)
        asset_statuses[status] += 1
        assets_by_comm[cname].append({
            "tag": r.get("AssetsAssetTagID") or "",
            "unit": str(r.get("SubEntitiesName") or ""),
            "type": atype,
            "status": status,
            "rtm": rtm,
            # None for a home already earning or settled, so a caller can
            # filter the pipeline out of the fleet without re-deriving it.
            "stage": stage,
            "stage_label": stage_label,
            "in_service": start,
            "age_days": days_since(start),
            "title": (r.get("AssetTitleStatusesName") or "").strip(),
            "market_rent": rnd(num(r.get("MarketRentAmount")), 0),
            # Somebody is living in it. The asset listing leaves OccupantName
            # blank rather than writing "Vacant", and a status alone will not
            # answer this -- a home can read For Sale with a resident still in
            # it. The name itself is dropped; only the boolean survives.
            "occupied": bool(str(r.get("OccupantName") or "").strip()),
        })
    for cname in assets_by_comm:
        assets_by_comm[cname].sort(key=lambda x: (x["status"], x["unit"]))

    def home_pipeline_rows(homes):
        """
        The rehab-to-listed funnel for one community, in registry order.

        Stages with nothing in them are dropped rather than shown as zero, so
        a small community's panel does not read as eight empty rows. Age is
        the median rather than the mean because one home ordered two years ago
        and forgotten drags an average past anything useful.
        """
        by = defaultdict(list)
        for h in homes:
            if h["stage"]:
                by[h["stage"]].append(h)
        out = []
        for key in reg.home_stage_order:
            group = by.get(key)
            if not group:
                continue
            ages = sorted(h["age_days"] for h in group if h["age_days"] is not None)
            out.append({
                "stage": key,
                "label": reg.home_pipeline[key]["label"],
                "homes": len(group),
                "median_age_days": _median(ages),
                "rtm": sum(1 for h in group if h["rtm"]),
            })
        return out

    rent_roll = defaultdict(list)
    vacancy_detail = defaultdict(list)
    unmapped_types = set()
    rr_rows_rm = load_optional(raw_dir, RM_SOURCES["rm_rent_roll"]) or []
    for r in rr_rows_rm:
        # RM returns parent and sub-ledger entities too; only reportable
        # communities have a home here.
        cname = rm_community(r)
        if not cname:
            continue
        utype = (r.get("UnitTypesName") or "TBD").strip()
        vac_loss = num(r.get("VacancyLoss"))
        # No active lease is a far better "currently empty" signal than vacancy
        # loss alone: RM only computes lost rent where a market rent is set, so
        # an RV resort billing transient stays showed almost nothing vacant.
        # This names ~1,800 units against ~800, though it still will not tie
        # exactly to the counted figure, which is unit-day weighted rather than
        # point in time.
        vacant = (not r.get("LeasesMoveInDate")) or vac_loss > 0
        if utype not in reason_of:
            unmapped_types.add(utype)
        entry = {
            "unit": str(r.get("SubEntitiesName") or ""),
            "type": utype,
            "vacant": vacant,
            # A resident on the ledger. This is the hot sheet's occupancy
            # signal, and it is deliberately not `not vacant`: an RV site
            # billing transient stays has a resident but no move-in date and no
            # vacancy loss, so the `vacant` flag above misses it in both
            # directions. Belle Haven reads 55 occupied lots this way against
            # 37 that bill recurring rent.
            "occupied": bool(r.get("CustomersCustomerDisplayID")),
            "rent": rnd(num(r.get("RentCharges")), 0),
            # RM calls scheduled market rent `Rented100`. Needed to price what
            # an occupied lot billing nothing would be worth at market.
            "market_rent": rnd(num(r.get("Rented100")), 0),
            "misc": rnd(num(r.get("MiscCharges")), 0),
            "charged": rnd(num(r.get("TotalCharged")), 0),
            "paid": rnd(num(r.get("TotalPaid")), 0),
            "balance": rnd(num(r.get("DebitBalances")), 0),
            "deposit": rnd(num(r.get("SecurityDeposit")), 0),
            "ltl": rnd(num(r.get("LossToLease")), 0),
            "move_in": (r.get("LeasesMoveInDate") or "")[:10],
        }
        rent_roll[cname].append(entry)
        if vacant:
            out_date = last_out.get((cname, entry["unit"]))
            dv = days_since(out_date) if out_date else None
            vacancy_detail[cname].append({
                "unit": entry["unit"],
                "type": utype,
                "reason": reason_of.get(utype, "vacant_lot"),
                "rent_lost": rnd(vac_loss, 0),
                "vacant_since": out_date,
                "days_vacant": dv,
                "age_band": age_band(dv),
            })

    for cname in rent_roll:
        rent_roll[cname].sort(key=lambda x: (not x["vacant"], x["unit"]))
        vacancy_detail[cname].sort(key=lambda x: (x["reason"], x["unit"]))

    # ---- eviction tracker -------------------------------------------------
    # A scripted Rent Manager report, exported daily to SharePoint and staged
    # through pipeline/stage_eviction.py with resident names and case numbers
    # removed. This is what turns the 90+ bucket from one number into the four
    # work buckets Natalie asked for: in eviction, former resident, payment
    # plan, and everything still untouched.
    evict_raw = load_envelope(raw_dir, "eviction_tracker.json") or {}
    if isinstance(evict_raw, dict):
        evict_cases_raw = evict_raw.get("cases") or []
        evict_as_of = evict_raw.get("as_of") or ""
    else:
        evict_cases_raw, evict_as_of = evict_raw, ""

    def evict_community(case):
        """
        Which reportable community a tracker row belongs to, or None.

        The tracker's ShortName carries suffixes the PDS roster does not --
        WOLFPO, TCMHCPO, PSEPO -- so a direct hit is tried first, then the
        community name, then the short name with the suffix trimmed. All 57
        properties in the tracker resolve this way; the ones that then fall
        out are the sold and non-reportable ones, which is correct.
        """
        sn = (case.get("short_name") or "").strip().upper()
        cm = (case.get("community") or "").strip().upper()
        for k in (sn, cm):
            if k and k in rm_lookup:
                return rm_lookup[k]
        for suffix in ("MHCPO", "MHC", "PO"):
            if sn.endswith(suffix) and sn[:-len(suffix)] in rm_lookup:
                return rm_lookup[sn[:-len(suffix)]]
        return None

    # Keyed by (community, unit). A unit can carry more than one case over the
    # years, so the open one wins and otherwise the most recent close.
    evict_open = {}
    evict_closed = {}
    evict_by_comm = defaultdict(list)
    evict_unresolved = set()
    for case in evict_cases_raw:
        cname = evict_community(case)
        if not cname:
            if case.get("community"):
                evict_unresolved.add(case["community"])
            continue
        phase, phase_label = reg.eviction_phase(case.get("stage"))
        unit = (case.get("unit") or "").strip()
        row = {
            "unit": unit,
            "stage": case.get("stage") or "",
            "phase": phase,
            "phase_label": phase_label,
            "start": case.get("start") or "",
            "closed": case.get("closed") or "",
            "days_open": days_since(case.get("start")) if not case.get("closed") else None,
            "days_in_stage": days_since(case.get("stage_since")),
            "with_attorney": bool(case.get("sent_to_attorney")),
            "has_case": bool(case.get("has_case")),
            "open_charges": rnd(num(case.get("open_charges")), 0),
        }
        key = (cname, unit)
        if row["closed"]:
            prev = evict_closed.get(key)
            if not prev or row["closed"] > prev["closed"]:
                evict_closed[key] = row
        else:
            evict_open[key] = row
        evict_by_comm[cname].append(row)
    for cname in evict_by_comm:
        evict_by_comm[cname].sort(key=lambda x: (bool(x["closed"]), -(x["days_open"] or 0)))

    # AR detail collapses from charge rows to one row per tenant account, which
    # is the grain someone working collections actually calls.
    ar_accounts = defaultdict(dict)
    ar_rows_rm = load_optional(raw_dir, RM_SOURCES["rm_ar_detail"]) or []
    for r in ar_rows_rm:
        cname = rm_community(r)
        if not cname:
            continue
        acct = r.get("AccountsAccountID")
        if acct is None:
            continue
        a = ar_accounts[cname].setdefault(acct, {
            "account": acct,
            # Carried so ar_segment can key the tracker without a closure over
            # the loop variable.
            "community": cname,
            "unit": str(r.get("PrimaryLeaseUnitName") or r.get("SubEntitiesName") or ""),
            "customer": r.get("CustomersCustomerDisplayID"),
            "b0_30": 0.0, "b31_60": 0.0, "b61_90": 0.0, "b90p": 0.0, "total": 0.0,
            "charges": defaultdict(float),
        })
        a["b0_30"] += num(r.get("LessThan30"))
        a["b31_60"] += num(r.get("LessThan60"))
        a["b61_90"] += num(r.get("LessThan90"))
        a["b90p"] += num(r.get("GreaterThan90"))
        a["total"] += num(r.get("TotalLeft"))
        ct = (r.get("ChargeTypesDescription") or r.get("ChargeTypesName") or "Other").strip()
        a["charges"][ct] += num(r.get("TotalLeft"))

    # Which bucket of work does this balance belong to? These are the four
    # Natalie asked for, and they now come from the eviction tracker rather
    # than from guessing at charge names.
    #
    # Order is deliberate. An open case outranks everything, because a resident
    # in eviction is not a collections call regardless of what else is on the
    # ledger. A payment plan outranks former-resident status, since terms
    # agreed on the way out are still terms. Former resident comes from two
    # signals: a lease the move history shows ended, or a closed eviction case
    # on the unit with money still owed, which is the definition of a
    # post-eviction remainder.
    def ar_segment(a):
        key = (a["community"], a["unit"])
        low = {n.lower() for n in a["charges"].keys()}
        ev = evict_open.get(key)
        if ev:
            return "eviction", "In eviction: %s" % ev["phase_label"].lower()
        if any("payment plan" in n or "pmtpln" in n or "payls" in n for n in low):
            return "payment_plan", "On a payment plan"
        if cust_status.get(a["account"]) == "Past":
            return "former", "Former resident, lease ended"
        if key in evict_closed:
            return "former", "Former resident, eviction closed %s" % evict_closed[key]["closed"]
        # With the tracker in place this residue is a real work queue rather
        # than a leftover: no open case, no plan, and nobody who has moved out.
        # Someone has to call these.
        return "needs_action", "No case, no plan -- needs action"

    ar_accounts_out = {}
    for cname, accts in ar_accounts.items():
        rows_out = []
        for a in accts.values():
            if a["total"] <= 0.005:
                continue
            top = sorted(a["charges"].items(), key=lambda x: -x[1])[:3]
            seg, seg_label = ar_segment(a)
            ev = evict_open.get((cname, a["unit"]))
            rows_out.append({
                "segment": seg,
                "segment_label": seg_label,
                "eviction_phase": ev["phase"] if ev else None,
                "eviction_stage": ev["stage"] if ev else "",
                "eviction_days_open": ev["days_open"] if ev else None,
                "account": a["account"],
                "unit": a["unit"],
                "customer": a["customer"],
                "b0_30": rnd(a["b0_30"], 0),
                "b31_60": rnd(a["b31_60"], 0),
                "b61_90": rnd(a["b61_90"], 0),
                "b90p": rnd(a["b90p"], 0),
                "total": rnd(a["total"], 0),
                "past_due_30plus": rnd(a["total"] - a["b0_30"], 0),
                "charges": ", ".join("%s %s" % (k, money(v)) for k, v in top),
            })
        rows_out.sort(key=lambda x: -x["past_due_30plus"])
        ar_accounts_out[cname] = rows_out

    def vacancy_by_reason(name, comp):
        """
        Vacant units grouped by why, counted from the warehouse composition.

        The Rent Manager rent roll can name each vacant unit but cannot be
        trusted to count them: an RV resort that bills transient stays rather
        than recurring lot rent shows no vacancy loss at all, which understated
        Great Oak by about seventy sites. The warehouse computes vacancy from
        unit-days and reconciles to portfolio occupancy, so it owns the counts
        and RM only supplies the names.
        """
        agg = {}
        rm_lost = defaultdict(float)
        for x in vacancy_detail.get(name, []):
            rm_lost[x["reason"]] += x["rent_lost"]
        for tname, dd in (comp or {}).items():
            vac = dd["vacant"] if isinstance(dd, dict) else 0
            if not vac:
                continue
            rk = reason_of.get(tname)
            if rk is None:
                unmapped_types.add(tname)
                rk = "vacant_lot"
            a = agg.setdefault(rk, {"reason": rk, "label": reason_meta[rk]["label"],
                                    "actionable": reason_meta[rk]["actionable"],
                                    "units": 0, "rent_lost": 0.0})
            a["units"] += int(vac)
        for rk, a in agg.items():
            a["rent_lost"] = rnd(rm_lost.get(rk, 0.0), 0)
        return sorted(agg.values(), key=lambda x: -x["units"])

    prior_closed = months[-3] if len(months) > 2 else None
    # ------------------------------------------------------- the hot sheet ---
    # Every unit type the asset listing calls a home. The rent roll returns
    # lots AND homes as sibling rows -- Belle Haven is 93 lots plus 50 homes in
    # 143 rows -- so a hot sheet that counts rows counts each POH twice. Derive
    # the home vocabulary from the asset file rather than hardcoding it, and
    # never treat a "Lot-" type as a home however it is spelled.
    home_types = {(r.get("AssetTypesName") or "").strip() for r in asset_rows}
    home_types = {t for t in home_types if t and not t.startswith("Lot")}

    def hot_sheet(name, pds, comp):
        """
        The per-community hot sheet: occupied over core units, what is empty,
        what the occupied lots actually pay, and the park-owned home split.

        This deliberately does NOT reuse the warehouse occupancy figure. That
        one is unit-day weighted across a whole month, which is the right
        measure for a trend and the wrong one for "how full is this park right
        now". Both appear on the page, labelled, because they answer different
        questions and will not tie.
        """
        lots = [u for u in rent_roll.get(name, []) if u["type"] not in home_types]
        if not lots:
            return None

        core = int(num(pds.get("core_units")) or len(lots))
        occupied = sum(1 for u in lots if u["occupied"])
        # Lots that cannot be leased are still core units, but they are not a
        # leasing failure -- the rentable denominator drops them so a manager
        # is not measured against a demo permit.
        dead = sum(dd["units"] for t, dd in comp.items()
                   if reg.unit_type(t)[1] == "not_rentable")
        rentable = max(core - dead, 0)

        billing = [u for u in lots if u["occupied"] and u["rent"] > 0]
        silent = [u for u in lots if u["occupied"] and u["rent"] <= 0]
        rents = sorted(u["rent"] for u in billing)

        homes = [hm for hm in assets_by_comm.get(name, []) if hm["type"] in home_types]
        poh_occ = sum(1 for hm in homes if hm["occupied"])

        empty = Counter(u["type"] for u in lots if not u["occupied"])
        ltl = sum(u["ltl"] for u in lots)

        return {
            "core_units": core,
            "rentable_units": rentable,
            "occupied": occupied,
            "occupancy": rnd(occupied / core * 100) if core else None,
            "occupancy_rentable": rnd(occupied / rentable * 100) if rentable else None,
            "vacant": len(lots) - occupied,
            "vacant_by_type": [{"type": t, "units": n}
                               for t, n in empty.most_common()],
            "lot_rent_avg": rnd(sum(rents) / len(rents), 0) if rents else None,
            "lot_rent_median": _median(rents),
            "lots_billing": len(billing),
            # Occupied and paying nothing recurring. Reported BY TYPE and never
            # as a single total, because the single total is a trap: portfolio
            # wide it reads 743 lots and $349K a month, of which 581 lots and
            # $299K are RV sites that bill transient or seasonal stays by
            # design and can never carry a recurring charge. Quoting the gross
            # figure as a billing gap would be wrong by a factor of six. The
            # residual on residential lots is the number that means something.
            "occupied_not_billing": len(silent),
            "not_billing_market": rnd(sum(u["market_rent"] for u in silent
                                          if u.get("market_rent")), 0),
            "not_billing_by_type": [
                {"type": t,
                 "units": n,
                 "market": rnd(sum(u["market_rent"] for u in silent
                                   if u["type"] == t and u.get("market_rent")), 0),
                 # RV and transient stays are billed per night or per season,
                 # so an empty recurring charge is expected rather than missing.
                 "transient": "RV" in t}
                for t, n in Counter(u["type"] for u in silent).most_common()],
            "loss_to_lease": rnd(ltl, 0),
            "loss_to_lease_per_lot": rnd(ltl / occupied, 0) if occupied else None,
            "poh_total": len(homes),
            "poh_occupied": poh_occ,
            "poh_pct": rnd(poh_occ / len(homes) * 100) if homes else None,
            "poh_vacant_by_status": [{"status": s, "homes": n} for s, n in
                                     Counter(hm["status"] for hm in homes
                                             if not hm["occupied"]).most_common()],
            "acquired_date": pds.get("acquired_date") or "",
            "acquired_price": pds.get("acquired_price"),
            # What the PDS asserts by hand, kept beside what we just measured
            # so the two can be reconciled instead of quietly disagreeing.
            "pds_poh": int(num(pds.get("poh_pds")) or 0) or None,
            "pds_lot_rent_mh": pds.get("mh_lot_rent_2026"),
            "pds_lot_rent_rv": pds.get("rv_lot_rent_2026"),
        }

    communities = []
    for name in kept:
        closed = community_period(name, closed_month, prior_closed)
        live = community_period(name, live_month, closed_month)
        if not closed and not live:
            continue

        comp_raw = vac_comp.get(name, {})
        # Per-type vacant counts, derived the same way the composition rows are,
        # so `vacancy_by_reason` and `vacancy_composition` always agree.
        comp = {}
        for tname, dd in comp_raw.items():
            vac_units = (int(round(dd["vac_days"] / (dd["avail_days"] / dd["units"])))
                         if dd["units"] and dd["avail_days"] else 0)
            comp[tname] = {"units": int(dd["units"]), "vacant": vac_units}
        comp = comp
        r_units = r_avail = r_vac = impaired = not_rentable = 0.0
        for tname, dd in comp_raw.items():
            group, bucket = reg.unit_type(tname)
            if group == "NON_REVENUE" or bucket == "not_rentable":
                not_rentable += dd["units"]
                continue
            r_units += dd["units"]
            r_avail += dd["avail_days"]
            r_vac += dd["vac_days"]
            if bucket == "rentable_impaired":
                impaired += dd["units"]
        occ_rentable = ((r_avail - r_vac) / r_avail * 100) if r_avail else None

        mix = type_mix.get(name, {})
        seg = reg.segments.get(name, {})
        pds = reportable.get(name.strip().lower(), {})
        vac_reasons = vacancy_by_reason(name, comp)

        communities.append({
            "name": name,
            "short_name": pds.get("short_name") or "",
            "park": seg.get("park") or (pds.get("community") or name),
            "kind": seg.get("type") or (max(mix, key=lambda k: mix[k]) if mix else "MH"),
            "state": pds.get("state") or "",
            "vehicle": pds.get("vehicle") or "",
            "rentable_units": int(r_units),
            "impaired_units": int(impaired),
            "not_rentable_units": int(not_rentable),
            "occupancy_rentable": rnd(occ_rentable) if occ_rentable is not None else None,
            "vacancy_composition": sorted(
                [{"type": t,
                  "group": reg.unit_type(t)[0],
                  "bucket": reg.unit_type(t)[1],
                  "units": dd["units"],
                  "vacant": dd["vacant"]}
                 for t, dd in comp.items()],
                key=lambda x: -x["units"]),
            "hot": hot_sheet(name, pds, comp),
            "closed": closed or {},
            "live": live or {},
            "expenses": expense_split(name, closed_month),
            "expenses_ytd": expense_split_ytd(name, closed_month),
            "rent_roll": rent_roll.get(name, []),
            "utilities_service": {
                "water_service": pds.get("water_service") or "",
                "water_paid_by": pds.get("water_paid_by") or "",
                "sewer_service": pds.get("sewer_service") or "",
                "sewer_paid_by": pds.get("sewer_paid_by") or "",
                "trash_paid_by": pds.get("trash_paid_by") or "",
                # If the community pays, there is nothing to bill back and a low
                # recapture rate is the design rather than a billing failure.
                "recoverable": any((pds.get(k) or "").strip().lower().startswith("resident")
                                   for k in ("water_paid_by", "sewer_paid_by", "trash_paid_by")),
            },
            "homes": assets_by_comm.get(name, []),
            "home_pipeline": home_pipeline_rows(assets_by_comm.get(name, [])),
            "homes_earning": sum(1 for h in assets_by_comm.get(name, []) if not h["stage"]),
            "evictions": evict_by_comm.get(name, []),
            "eviction_phases": [
                {"phase": ph, "label": reg.evict_label.get(ph, ph), "cases": n,
                 "balance": rnd(sum(x["open_charges"] for x in evict_by_comm.get(name, [])
                                    if not x["closed"] and x["phase"] == ph), 0)}
                for ph, n in sorted(
                    Counter(x["phase"] for x in evict_by_comm.get(name, [])
                            if not x["closed"]).items(),
                    key=lambda x: reg.evict_order.index(x[0])
                    if x[0] in reg.evict_order else 99)
            ],
            "home_status": [
                {"status": st, "homes": n}
                for st, n in sorted(Counter(a["status"] for a in assets_by_comm.get(name, [])).items(),
                                    key=lambda x: -x[1])
            ],
            "vacancy_detail": vacancy_detail.get(name, []),
            "ar_accounts": ar_accounts_out.get(name, []),
            "vacancy_by_reason": vac_reasons,
            "vacancy_aging": [
                {"band": b, "units": n,
                 "rent_lost": rnd(sum(x["rent_lost"] for x in vacancy_detail.get(name, [])
                                      if x["age_band"] == b), 0)}
                for b, n in sorted(
                    Counter(x["age_band"] for x in vacancy_detail.get(name, [])).items(),
                    key=lambda x: [lbl for _, lbl in AGE_BANDS].index(x[0])
                    if x[0] in [lbl for _, lbl in AGE_BANDS] else 99)
            ],
            "ar_segments": [
                {"segment": sg, "accounts": n,
                 "amount": rnd(sum(x["total"] for x in ar_accounts_out.get(name, [])
                                   if x["segment"] == sg), 0),
                 # The queue that matters. Rent bills on the 1st, so on day 4 of
                 # a month every occupied lot carries a balance and a raw
                 # account count reads like a portfolio in crisis. Only the
                 # accounts carrying something 30 days old are actually behind.
                 "accounts_30plus": sum(1 for x in ar_accounts_out.get(name, [])
                                        if x["segment"] == sg and x["past_due_30plus"] > 0.005),
                 "past_due_30plus": rnd(sum(x["past_due_30plus"] for x in ar_accounts_out.get(name, [])
                                            if x["segment"] == sg), 0)}
                for sg, n in Counter(x["segment"] for x in ar_accounts_out.get(name, [])).most_common()
            ],
            # How much of the counted vacancy the RM unit list can actually
            # name. Below 100% means the drill-in list is shorter than the
            # count above it, and the panel says so rather than implying the
            # list is complete.
            "vacancy_detail_coverage": rnd(
                len(vacancy_detail.get(name, [])) /
                max(1, sum(v["units"] for v in vac_reasons)) * 100),
        })
    # Eviction and work-bucket counts are point in time, not period figures,
    # but the Communities and Collections tables read every cell through the
    # closed/live accessor. Mirroring them into both blocks keeps that accessor
    # uniform rather than special-casing two columns in the UI.
    for c in communities:
        ev_open = [x for x in c["evictions"] if not x["closed"]]
        na = [g for g in c["ar_segments"] if g["segment"] == "needs_action"]
        pit = {
            "evictions_open": len(ev_open),
            "eviction_balance": rnd(sum(x["open_charges"] for x in ev_open), 0),
            "ar_needs_action": sum(g["accounts_30plus"] for g in na),
            "ar_needs_action_amount": rnd(sum(g["past_due_30plus"] for g in na), 0),
        }
        for blk in ("closed", "live"):
            if c[blk]:
                c[blk].update(pit)

    communities.sort(key=lambda c: c["name"])

    # ---- portfolio trends (full history, partial month marked) -------------

    def series(store, fn):
        out = []
        for mo in months:
            agg = defaultdict(float)
            hit = False
            for name in kept:
                d = store.get(name, {}).get(mo)
                if not d:
                    continue
                hit = True
                for k, v in d.items():
                    agg[k] += v
            if hit:
                out.append({"month": mo, "partial": mo == live_month, **fn(agg)})
        return out

    occ_series = series(occ, lambda a: {"occupancy": rnd(occ_pct(a)), "units": int(a["units"])})
    ar_series = series(ar, lambda a: {
        "total": rnd(a["total"], 0), "b0_30": rnd(a["b0_30"], 0),
        "b31_60": rnd(a["b31_60"], 0), "b61_90": rnd(a["b61_90"], 0),
        "b90p": rnd(a["b90p"], 0), "accounts": int(a["accounts"]),
        "past_due_30plus": rnd(a["total"] - a["b0_30"], 0),
    })
    coll_series = series(rr, lambda a: {
        "collection_pct": rnd(coll_pct(a)), "charged": rnd(a["charged"], 0),
        "paid": rnd(a["paid"], 0), "outstanding": rnd(a["charged"] - a["paid"], 0),
    })
    move_series = series(mv, lambda a: {
        "ins": int(a["ins"]), "outs": int(a["outs"]), "net": int(a["ins"] - a["outs"])})

    # Onboarding is not leasing. When a property is brought into Rent Manager
    # its whole sitting resident base posts as move-ins that month -- Riverwalk
    # booked 169 in August 2025, The Oaks 145, Windward Knoll 139, against a
    # portfolio that normally runs 120 a month in total. Left unmarked, two such
    # months set the scale on the move chart and flatten the eighteen real ones
    # into a flat line, and a trailing-twelve net reads as growth that never
    # happened.
    #
    # The test is per property, not portfolio-wide: move-ins above a quarter of
    # a community's lots in one month is a load, not a leasing season. Months
    # are marked rather than dropped, and the chart draws them off-scale with
    # their true value labelled.
    ONBOARD_SHARE = 0.25
    for p_ in move_series:
        heavy = []
        for name in kept:
            dd = mv.get(name, {}).get(p_["month"])
            if not dd:
                continue
            lots = (occ.get(name, {}).get(p_["month"], {}) or {}).get("units") or 0
            if lots and dd["ins"] >= lots * ONBOARD_SHARE and dd["ins"] >= 25:
                heavy.append((name, int(dd["ins"]), int(lots)))
        heavy.sort(key=lambda x: -x[1])
        p_["onboarding"] = bool(heavy)
        p_["onboarding_ins"] = sum(x[1] for x in heavy)
        p_["onboarding_detail"] = ", ".join("%s %d of %d lots" % x for x in heavy[:4])
    onboarding_months = [p_ for p_ in move_series if p_["onboarding"]]
    fin_series = series(fin, lambda a: {
        "revenue": rnd(a["rev"], 0), "revenue_budget": rnd(a["rev_bud"], 0),
        "opex": rnd(a["opex"], 0), "opex_budget": rnd(a["opex_bud"], 0),
        "noi": rnd(a["noi"], 0), "noi_budget": rnd(a["noi_bud"], 0)})

    # Budgets are loaded per fiscal year, and 2025 was never loaded for most
    # properties: the portfolio "budget" for those months sits near a third of
    # actual, which drew a budget line that looked like a miss rather than an
    # absent plan. Null those points so the series starts where a real budget
    # does, and record where that is.
    # 2025 sat at 42-65% of actual because only some properties had a budget
    # loaded; 2026 runs 94-107%. So the test is not "is there a number" but
    # "did coverage become complete and stay complete", which is the first month
    # from which every later month clears the bar.
    def _ratio(p_):
        rv = p_.get("revenue") or 0
        rb = p_.get("revenue_budget") or 0
        return (rb / rv) if rv else 0.0

    budget_from = None
    for i, p_ in enumerate(fin_series):
        if all(_ratio(q) >= 0.85 for q in fin_series[i:]):
            budget_from = p_["month"]
            break
    if budget_from:
        for p_ in fin_series:
            if p_["month"] < budget_from:
                p_["revenue_budget"] = None
                p_["noi_budget"] = None
                p_["opex_budget"] = None
        log("budget series starts %s; earlier months had no budget loaded" % budget_from)

    def at(s, mo):
        return next((p for p in s if p["month"] == mo), None)

    def closed_pts(s):
        return [p for p in s if not p["partial"]]

    # ---- portfolio blocks, one per period ----------------------------------

    def portfolio_block(mo, prev_mo):
        rows = [c for c in communities if c.get("closed" if mo == closed_month else "live")]
        key = "closed" if mo == closed_month else "live"
        rows = [c for c in communities if c[key]]
        blk = [c[key] for c in rows]
        mh = [c[key] for c in rows if c["kind"] == "MH"]
        rv = [c[key] for c in rows if c["kind"] == "RV"]

        def s(field, source=None):
            return sum((x.get(field) or 0) for x in (source if source is not None else blk))

        def wavg(source, field, weight="units"):
            wt = sum((x.get(weight) or 0) for x in source)
            return rnd(sum((x.get(field) or 0) * (x.get(weight) or 0) for x in source) / wt) if wt else 0.0

        o_now = at(occ_series, mo) or {}
        o_prev = at(occ_series, prev_mo) or {} if prev_mo else {}
        a_now = at(ar_series, mo) or {}
        a_prev = at(ar_series, prev_mo) or {} if prev_mo else {}
        c_now = at(coll_series, mo) or {}
        f_now = at(fin_series, mo) or {}
        m_now = at(move_series, mo) or {}

        ytd = defaultdict(float)
        for p in fin_series:
            if p["month"][:4] == mo[:4] and p["month"] <= mo:
                for k in ("revenue", "revenue_budget", "opex", "noi", "noi_budget"):
                    ytd[k] += p[k]

        charged = c_now.get("charged", 0)
        return {
            "month": mo,
            "partial": mo == live_month,
            "communities": len(rows),
            "parks": len({c["park"] for c in rows}),
            "total_units": s("units"),
            "total_occupied": s("occupied"),
            "occupancy": o_now.get("occupancy", 0.0),
            "occupancy_prev": o_prev.get("occupancy"),
            "occupancy_rentable": wavg(
                [dict(c[key], occupancy_rentable=c["occupancy_rentable"],
                      rentable_units=c["rentable_units"]) for c in rows
                 if c["occupancy_rentable"] is not None],
                "occupancy_rentable", "rentable_units"),
            "mh_units": s("units", mh),
            "mh_occupancy": wavg(mh, "occupancy"),
            "rv_units": s("units", rv),
            "rv_occupancy": wavg(rv, "occupancy"),
            "impaired_units": sum(c["impaired_units"] for c in rows),
            "not_rentable_units": sum(c["not_rentable_units"] for c in rows),
            "ar_total": a_now.get("total", 0),
            "ar_prev": a_prev.get("total"),
            "ar_0_30": a_now.get("b0_30", 0),
            "ar_90_plus": a_now.get("b90p", 0),
            "ar_past_due_30plus": a_now.get("past_due_30plus", 0),
            "ar_over90_share": rnd(a_now.get("b90p", 0) / a_now["total"] * 100) if a_now.get("total") else 0.0,
            "ar_accounts": a_now.get("accounts", 0),
            "charged": charged,
            "paid": c_now.get("paid", 0),
            "outstanding": c_now.get("outstanding", 0),
            "collection_pct": c_now.get("collection_pct", 0.0),
            "collection_ttm": rnd(sum(p["collection_pct"] for p in closed_pts(coll_series)[-12:]) /
                                  max(1, len(closed_pts(coll_series)[-12:]))),
            "revenue": f_now.get("revenue", 0),
            "revenue_budget": f_now.get("revenue_budget", 0),
            "noi": f_now.get("noi", 0),
            "noi_budget": f_now.get("noi_budget", 0),
            "noi_margin": rnd(f_now.get("noi", 0) / f_now["revenue"] * 100) if f_now.get("revenue") else 0.0,
            "ytd_revenue": rnd(ytd["revenue"], 0),
            "ytd_revenue_budget": rnd(ytd["revenue_budget"], 0),
            "ytd_noi": rnd(ytd["noi"], 0),
            "ytd_noi_budget": rnd(ytd["noi_budget"], 0),
            "move_ins": m_now.get("ins", 0),
            "move_outs": m_now.get("outs", 0),
            "vacancy_loss": s("vacancy_loss"),
            "loss_to_lease": s("loss_to_lease"),
        }

    portfolio = {
        "closed": portfolio_block(closed_month, prior_closed),
        "live": portfolio_block(live_month, closed_month),
    }

    # ---- vehicle rollups ---------------------------------------------------
    # Both the Communities and Collections tabs open collapsed to this level,
    # so these totals are what the team sees first. Rates are weighted by the
    # denominator that belongs to them, never averaged across communities.
    def vehicle_block(rows, key):
        blk = [c[key] for c in rows if c[key]]

        def s_(field):
            return sum((x.get(field) or 0) for x in blk)

        units = s_("units")
        charged = s_("charged")
        ar_total = s_("ar_total")
        rev = sum((c["closed"].get("revenue") or 0) for c in rows)
        noi = sum((c["closed"].get("noi") or 0) for c in rows)
        noi_bud = sum((c["closed"].get("noi_budget") or 0) for c in rows)
        exp = [c["expenses"] for c in rows]
        util = sum(e.get("utilities") or 0 for e in exp)
        util_inc = sum(e.get("utility_reimbursements") or 0 for e in exp)
        # Eviction and work-bucket counts are point-in-time, not period
        # figures, so they are identical in the closed and live blocks. They
        # live here anyway because the Collections table opens collapsed to
        # vehicle level and a column with no vehicle total is a blank row.
        ev_open = [x for c in rows for x in c["evictions"] if not x["closed"]]
        na = [g for c in rows for g in c["ar_segments"] if g["segment"] == "needs_action"]
        return {
            "communities": len(rows),
            "units": units,
            "occupied": s_("occupied"),
            "occupancy": rnd(s_("occupied") / units * 100) if units else 0.0,
            "charged": rnd(charged, 0),
            "paid": rnd(s_("paid"), 0),
            "outstanding": rnd(s_("outstanding"), 0),
            "collection_pct": rnd(s_("paid") / charged * 100) if charged else 0.0,
            "ar_total": rnd(ar_total, 0),
            "ar_0_30": rnd(s_("ar_0_30"), 0),
            "ar_31_60": rnd(s_("ar_31_60"), 0),
            "ar_61_90": rnd(s_("ar_61_90"), 0),
            "ar_90_plus": rnd(s_("ar_90_plus"), 0),
            "ar_past_due_30plus": rnd(s_("ar_past_due_30plus"), 0),
            "ar_over90_share": rnd(s_("ar_90_plus") / ar_total * 100) if ar_total else 0.0,
            "ar_accounts": s_("ar_accounts"),
            "ar_per_unit": rnd(ar_total / units, 0) if units else 0,
            "move_ins": s_("move_ins"),
            "move_outs": s_("move_outs"),
            "evictions_open": len(ev_open),
            "eviction_balance": rnd(sum(x["open_charges"] for x in ev_open), 0),
            "ar_needs_action": sum(g["accounts_30plus"] for g in na),
            "ar_needs_action_amount": rnd(sum(g["past_due_30plus"] for g in na), 0),
            "revenue": rnd(rev, 0),
            "noi": rnd(noi, 0),
            "noi_budget": rnd(noi_bud, 0),
            "noi_margin": rnd(noi / rev * 100) if rev else 0.0,
            "controllable": rnd(sum(e.get("controllable") or 0 for e in exp), 0),
            "non_controllable": rnd(sum(e.get("non_controllable") or 0 for e in exp), 0),
            "utilities": rnd(util, 0),
            "utility_reimbursements": rnd(util_inc, 0),
            "utility_recapture_pct": rnd(util_inc / util * 100) if util else None,
        }

    by_vehicle = defaultdict(list)
    for c in communities:
        by_vehicle[c["vehicle"] or "Unassigned"].append(c)
    vehicles = []
    for vname in sorted(by_vehicle):
        rows = by_vehicle[vname]
        vehicles.append({
            "vehicle": vname,
            "names": [c["name"] for c in rows],
            "closed": vehicle_block(rows, "closed"),
            "live": vehicle_block(rows, "live"),
        })
    vehicles.sort(key=lambda v: -v["closed"]["units"])
    log("vehicles: %s" % ", ".join("%s (%d)" % (v["vehicle"], v["closed"]["communities"])
                                   for v in vehicles))

    # ---- portfolio expense split and vacancy reasons -----------------------
    def sum_blocks(blocks):
        acc = defaultdict(float)
        for b in blocks:
            for k, v in b.items():
                if isinstance(v, (int, float)) and v is not None \
                   and not k.endswith("_pct") and not k.endswith("_share"):
                    acc[k] += v
        out = {k: rnd(v, 0) for k, v in acc.items()}
        out["controllable_share"] = (rnd(out.get("controllable", 0) / out["opex"] * 100)
                                     if out.get("opex") else 0.0)
        out["utility_recapture_pct"] = (rnd(out.get("utility_reimbursements", 0) / out["utilities"] * 100)
                                        if out.get("utilities") else None)
        return out

    portfolio["expenses"] = sum_blocks([c["expenses"] for c in communities])
    portfolio["expenses_ytd"] = sum_blocks([c["expenses_ytd"] for c in communities])

    vac_totals = {}
    for c in communities:
        for row in c["vacancy_by_reason"]:
            t = vac_totals.setdefault(row["reason"], {
                "reason": row["reason"], "label": row["label"],
                "actionable": row["actionable"], "units": 0, "rent_lost": 0.0,
                "communities": 0,
            })
            t["units"] += row["units"]
            t["rent_lost"] += row["rent_lost"]
            t["communities"] += 1
    vacancy_reasons = sorted(vac_totals.values(), key=lambda x: -x["units"])
    for v in vacancy_reasons:
        v["rent_lost"] = rnd(v["rent_lost"], 0)
    log("vacant units by reason: %s"
        % ", ".join("%s %d" % (v["label"], v["units"]) for v in vacancy_reasons))

    # ---- portfolio home pipeline and eviction funnel -----------------------
    # Both are rolled up from the community rows rather than recomputed, so the
    # headline and the drill-in can never disagree.
    pipe_tot = {}
    for c in communities:
        for row in c["home_pipeline"]:
            t = pipe_tot.setdefault(row["stage"], {
                "stage": row["stage"], "label": row["label"],
                "homes": 0, "rtm": 0, "communities": 0,
            })
            t["homes"] += row["homes"]
            t["rtm"] += row["rtm"]
            t["communities"] += 1
    home_pipeline = [pipe_tot[k] for k in reg.home_stage_order if k in pipe_tot]
    # Median across every pipeline home, not a median of medians.
    all_ages = defaultdict(list)
    for c in communities:
        for h in c["homes"]:
            if h["stage"] and h["age_days"] is not None:
                all_ages[h["stage"]].append(h["age_days"])
    for row in home_pipeline:
        row["median_age_days"] = _median(all_ages.get(row["stage"], []))
    portfolio["home_pipeline"] = home_pipeline
    portfolio["homes_earning"] = sum(c["homes_earning"] for c in communities)
    log("home pipeline: %s"
        % ", ".join("%s %d" % (r["label"], r["homes"]) for r in home_pipeline))

    seg_roll = {}
    for c in communities:
        for row in c["ar_segments"]:
            t = seg_roll.setdefault(row["segment"], {
                "segment": row["segment"], "accounts": 0, "accounts_30plus": 0,
                "amount": 0.0, "past_due_30plus": 0.0,
            })
            t["accounts"] += row["accounts"]
            t["accounts_30plus"] += row["accounts_30plus"]
            t["amount"] += row["amount"]
            t["past_due_30plus"] += row["past_due_30plus"]
    SEG_ORDER = ["eviction", "payment_plan", "former", "needs_action"]
    portfolio["ar_segments"] = [
        {**seg_roll[k], "amount": rnd(seg_roll[k]["amount"], 0),
         "past_due_30plus": rnd(seg_roll[k]["past_due_30plus"], 0)}
        for k in SEG_ORDER if k in seg_roll
    ]
    log("AR work buckets: %s"
        % ", ".join("%s %d accts / %d past due 30+ (%s)"
                    % (r["segment"], r["accounts"], r["accounts_30plus"],
                       money(r["past_due_30plus"]))
                    for r in portfolio["ar_segments"]))

    ev_tot = {}
    for c in communities:
        for row in c["eviction_phases"]:
            t = ev_tot.setdefault(row["phase"], {
                "phase": row["phase"], "label": row["label"],
                "cases": 0, "balance": 0.0, "communities": 0,
            })
            t["cases"] += row["cases"]
            t["balance"] += row["balance"]
            t["communities"] += 1
    eviction_phases = [ev_tot[k] for k in reg.evict_order + ["other"] if k in ev_tot]
    for row in eviction_phases:
        row["balance"] = rnd(row["balance"], 0)
    open_cases = [x for c in communities for x in c["evictions"] if not x["closed"]]
    portfolio["evictions"] = {
        "as_of": evict_as_of,
        "open_cases": len(open_cases),
        "communities": sum(1 for c in communities if c["eviction_phases"]),
        "balance": rnd(sum(x["open_charges"] for x in open_cases), 0),
        "with_attorney": sum(1 for x in open_cases if x["with_attorney"]),
        # Index into the filtered list, not the unfiltered one -- a case with
        # no start date drops out and the lengths stop matching.
        "median_days_open": _median([x["days_open"] for x in open_cases
                                     if x["days_open"] is not None]),
        "phases": eviction_phases,
    }
    log("evictions: %d open across %d communities, %s owed"
        % (len(open_cases), portfolio["evictions"]["communities"],
           money(portfolio["evictions"]["balance"])))

    # ---- flags -------------------------------------------------------------

    flags = []

    # ---- hot sheet reconciliation -------------------------------------------
    # The Property Data Sheet is maintained by hand and the Asset Listing is
    # not, so where they disagree the page says so rather than silently
    # preferring one. These raised 43 of 64 communities on the first run, which
    # is a maintenance problem, not a rounding one.
    poh_gap = [(c["short_name"] or c["name"], c["hot"]["pds_poh"], c["hot"]["poh_total"])
               for c in communities
               if c.get("hot") and c["hot"]["pds_poh"] and c["hot"]["poh_total"]
               and c["hot"]["pds_poh"] != c["hot"]["poh_total"]]
    if poh_gap:
        poh_gap.sort(key=lambda x: -abs(x[1] - x[2]))
        flags.append({
            "severity": "warn",
            "title": "%d communities disagree on how many park-owned homes they have"
                     % len(poh_gap),
            "detail": ("The Property Data Sheet's POH column and the Rent Manager asset "
                       "listing return different counts. The listing is the live system "
                       "and the PDS is typed by hand, so the PDS is the one to fix. "
                       "Widest gaps: %s."
                       % ", ".join("%s (PDS %d, listing %d)" % g for g in poh_gap[:6])),
        })

    # A residential lot with a resident and no recurring charge is either a
    # billing gap or an arrangement nobody wrote down. RV and seasonal sites are
    # excluded because they bill per stay by design -- including them turns a
    # $55K question into a $349K one that is six-sevenths wrong.
    silent = []
    for c in communities:
        if not c.get("hot"):
            continue
        real = [x for x in c["hot"]["not_billing_by_type"] if not x["transient"]]
        n = sum(x["units"] for x in real)
        if n:
            silent.append((c["short_name"] or c["name"], n,
                           sum(x["market"] for x in real)))
    if silent:
        silent.sort(key=lambda x: -x[1])
        flags.append({
            "severity": "warn",
            "title": "%d occupied lots across %d communities bill no recurring rent"
                     % (sum(s[1] for s in silent), len(silent)),
            "detail": ("Residential lots with a resident on the ledger and no recurring "
                       "charge, worth %s a month at market rent. RV, seasonal and "
                       "transient sites are excluded, because those bill per stay and "
                       "would otherwise inflate this sixfold. Largest: %s."
                       % (money(sum(s[2] for s in silent)),
                          ", ".join("%s (%d lots)" % (s[0], s[1]) for s in silent[:6]))),
        })

    core_gap = [(c["short_name"] or c["name"], c["hot"]["core_units"],
                 c["hot"]["occupied"] + c["hot"]["vacant"])
                for c in communities if c.get("hot")]
    core_gap = [(s, a, b) for s, a, b in core_gap if abs(b - a) > 2]
    if core_gap:
        flags.append({
            "severity": "info",
            "title": "%d communities carry more lots in Rent Manager than the PDS counts"
                     % len(core_gap),
            "detail": ("Total Core Units on the Property Data Sheet is the occupancy "
                       "denominator, so where the rent roll holds more lots than that, "
                       "occupancy sits on the wrong base: %s."
                       % ", ".join("%s (PDS %d, rent roll %d)" % g for g in core_gap[:6])),
        })


    if unknown_types:
        flags.append({
            "severity": "warn",
            "title": "Unclassified unit types",
            "detail": ("Not in registry.json, counted as rentable MH: %s"
                       % ", ".join(sorted(unknown_types))),
        })

    if absent:
        flags.append({
            "severity": "warn",
            "title": "%d reportable %s no warehouse data"
                     % (len(absent), "community has" if len(absent) == 1 else "communities have"),
            "detail": ("The Property Data Sheet marks these Reportable = Yes but the "
                       "warehouse returned no rows for them, so they are missing from "
                       "every total: %s."
                       % ", ".join("%s (%s)" % (r["property_name"], r["short_name"])
                                   for r in absent)),
        })

    if rolled_ar:
        flags.append({
            "severity": "info",
            "title": "%s of receivables rolled in from sub-ledgers" % money(sum(rolled_ar.values())),
            "detail": ("These ledgers are not reportable communities themselves, so their "
                       "balances are attributed to the parent community rather than shown "
                       "as their own row: %s."
                       % ", ".join("%s %s" % (n, money(v))
                                   for n, v in sorted(rolled_ar.items(), key=lambda x: -x[1]))),
        })

    stale_pds = [e["match"][0] for e in cfg.get("sold", [])
                 if e["match"][0].strip().lower() in reportable]
    if stale_pds:
        flags.append({
            "severity": "info",
            "title": "%d sold %s excluded by override, not by the PDS"
                     % (len(stale_pds), "property is" if len(stale_pds) == 1 else "properties are"),
            "detail": ("%s. Correctly out of every figure, but the Property Data Sheet still "
                       "reads Reportable = Yes with no Sale Date, so the exclusion rests on "
                       "registry.json rather than the roster. Flipping Reportable to No and "
                       "filling the Sale Date lets the override be retired."
                       % ", ".join(stale_pds)),
        })

    cl, lv = portfolio["closed"], portfolio["live"]
    if lv["ar_total"] and cl["ar_total"]:
        flags.append({
            "severity": "info",
            "title": "Live receivables run %s above the closed month by design"
                     % money(lv["ar_total"] - cl["ar_total"]),
            "detail": ("Rent bills on the 1st, so day %d of %s carries a full month of new "
                       "charges against %d days of collection. Past the %dth that money is "
                       "late, which is why the live view exists. Use the Closed toggle to "
                       "compare like with like."
                       % (live_day, live_month, live_day, grace_day)),
        })

    ar_closed = closed_pts(ar_series)
    if len(ar_closed) >= 13 and ar_closed[-13]["total"]:
        yoy = (ar_closed[-1]["total"] - ar_closed[-13]["total"]) / ar_closed[-13]["total"] * 100
        if abs(yoy) > 15:
            flags.append({
                "severity": "warn" if yoy > 0 else "info",
                "title": "Receivables are %.0f%% against a year ago" % yoy,
                "detail": "%s in %s against %s in %s."
                          % (money(ar_closed[-1]["total"]), ar_closed[-1]["month"],
                             money(ar_closed[-13]["total"]), ar_closed[-13]["month"]),
            })
    if len(ar_closed) >= 8 and ar_closed[-8]["b90p"]:
        g = (ar_closed[-1]["b90p"] - ar_closed[-8]["b90p"]) / ar_closed[-8]["b90p"] * 100
        if g > 25:
            flags.append({
                "severity": "warn",
                "title": "The 90+ bucket is up %.0f%% in seven months" % g,
                "detail": ("%s to %s while the monthly collection rate still reads %s. "
                           "Collections is a flow and receivables are a stock, so a few "
                           "points of monthly leakage compounds here."
                           % (money(ar_closed[-8]["b90p"]), money(ar_closed[-1]["b90p"]),
                              "%.1f%%" % cl["collection_pct"])),
            })

    frozen = [c["name"] for c in communities
              if c["closed"].get("ar_total", 0) > 25000
              and c["closed"].get("ar_over90_share", 0) >= 99.5]
    if frozen:
        flags.append({
            "severity": "warn",
            "title": "%d %s all receivables in the 90+ bucket"
                     % (len(frozen), "community holds" if len(frozen) == 1 else "communities hold"),
            "detail": ("Nothing current or mid-aged at all, which usually means a stale or "
                       "migrated ledger rather than live delinquency: %s."
                       % ", ".join(sorted(frozen))),
        })

    def pds_units(row):
        v = (row.get("total_units") or "").replace(",", "").strip()
        try:
            return int(float(v))
        except ValueError:
            return 0

    lot_gaps = []
    for c in communities:
        pds_row = reportable.get(c["name"].strip().lower())
        if not pds_row:
            continue
        expected = pds_units(pds_row)
        actual = c["closed"].get("units", 0)
        if expected and abs(actual - expected) >= max(5, expected * 0.05):
            lot_gaps.append((c["name"], expected, actual))
    if lot_gaps:
        flags.append({
            "severity": "warn",
            "title": ("%d %s lot count disagrees with the Property Data Sheet" % (len(lot_gaps), "community's")
                      if len(lot_gaps) == 1 else
                      "%d communities' lot counts disagree with the Property Data Sheet" % len(lot_gaps)),
            "detail": ("The PDS is the authoritative lot count, so a gap means the Rent "
                       "Manager unit list is out of step: %s. Occupancy is computed on the "
                       "warehouse count, so these percentages sit on the wrong denominator "
                       "until the ledgers agree."
                       % ", ".join("%s (PDS %d, RM %d)" % (n, e, a)
                                   for n, e, a in sorted(lot_gaps, key=lambda x: -abs(x[2] - x[1])))),
        })

    # September GL is not posted on day 4, so revenue and NOI have no live
    # reading. Say so rather than letting a zero look like a collapse.
    if not portfolio["live"].get("revenue") and portfolio["closed"].get("revenue"):
        flags.append({
            "severity": "info",
            "title": "%s financials are not posted yet" % live_month,
            "detail": ("Revenue, expenses and NOI have no live figure this early in the "
                       "month, so the Financials tab and the NOI tile always report closed "
                       "%s regardless of the period toggle." % closed_month),
        })

    # A month whose expense ratio sits well under its own trailing range is not
    # a great month, it is an unfinished one. Saying so stops an inflated NOI
    # being read as performance.
    closed_fin = closed_pts(fin_series)
    if len(closed_fin) >= 7:
        ratios = [(p["opex"] / p["revenue"] * 100) for p in closed_fin[:-1]
                  if p.get("revenue")]
        cur = (closed_fin[-1]["opex"] / closed_fin[-1]["revenue"] * 100
               if closed_fin[-1].get("revenue") else None)
        if ratios and cur is not None:
            ratios_sorted = sorted(ratios[-12:])
            median = ratios_sorted[len(ratios_sorted) // 2]
            if cur < median - 4:
                shortfall = (median - cur) / 100 * closed_fin[-1]["revenue"]
                flags.append({
                    "severity": "warn",
                    "title": "%s expenses look only partly posted" % closed_fin[-1]["month"],
                    "detail": ("Operating expense is %.0f%% of revenue against a %.0f%% median "
                               "for the trailing year, a gap worth about %s. NOI of %s for the "
                               "month is flattered by roughly that much and should not be read "
                               "as performance until the ledger is closed out. %s is the last "
                               "month with a full expense picture."
                               % (cur, median, money(shortfall), money(closed_fin[-1]["noi"]),
                                  closed_fin[-2]["month"] if len(closed_fin) > 1 else "The prior month")),
                })

    if unmapped_types:
        flags.append({
            "severity": "info",
            "title": "%d unit types have no vacancy reason mapped" % len(unmapped_types),
            "detail": ("Counted as a plain vacant lot until classified in registry.json "
                       "under `vacancy_reasons`: %s." % ", ".join(sorted(unmapped_types))),
        })

    counted_vac = sum(sum(r["units"] for r in c["vacancy_by_reason"]) for c in communities)
    named_vac = sum(len(c["vacancy_detail"]) for c in communities)
    if counted_vac and abs(named_vac - counted_vac) / counted_vac > 0.1:
        flags.append({
            "severity": "info",
            "title": "Vacant unit counts and the named unit list use different definitions",
            "detail": ("The headline count of %s vacant is unit-day weighted from the "
                       "warehouse, so a lot empty for half the month counts as half. The "
                       "drill-in list names %s units with no active lease as of today. Both "
                       "are right for what they measure, which is why they do not tie."
                       % (count_str(counted_vac), count_str(named_vac))),
        })

    aged_n = sum(1 for c in communities for v in c["vacancy_detail"]
                 if v.get("days_vacant") is not None)
    named_n = sum(len(c["vacancy_detail"]) for c in communities)
    if named_n and aged_n / named_n < 0.8:
        flags.append({
            "severity": "info",
            "title": "Vacancy aging covers %d of %d vacant units" % (aged_n, named_n),
            "detail": ("Days vacant is measured from the unit's last move-out, and the move "
                       "history pulled starts %s, so a lot that has been empty longer than "
                       "that has no anchor and shows as Unknown. Pulling move history further "
                       "back would close the gap." % months[0]),
        })

    seg_tot = defaultdict(lambda: [0, 0.0])
    for c in communities:
        for sgg in c["ar_segments"]:
            seg_tot[sgg["segment"]][0] += sgg["accounts"]
            seg_tot[sgg["segment"]][1] += sgg["amount"]
    total_accts = sum(v[0] for v in seg_tot.values())

    # The tracker is a daily export. If it stops running, the eviction bucket
    # quietly drains into needs-action and nothing else says so.
    if evict_as_of:
        lag = days_since(evict_as_of)
        if lag is not None and lag > 2:
            flags.append({
                "severity": "warn",
                "title": "The eviction tracker export is %d days old" % lag,
                "detail": ("Case stages and the in-eviction split below are as of %s. The "
                           "scripted report lands daily in Data Analytics / Rent Manager / "
                           "Eviction Tracker.csv, so a gap this size means the job did not "
                           "run. Until it does, cases that have moved show their old stage "
                           "and newly filed ones read as needing action." % evict_as_of),
            })

    # A candlestick makes an incomplete month look like a triumph: August shows
    # 27 in against 1 out, which is not a leasing win, it is move-outs that have
    # not posted. Catch it before someone reads the chart.
    if onboarding_months:
        biggest = max(onboarding_months, key=lambda m: m["onboarding_ins"])
        flags.append({
            "severity": "info",
            "title": "%d %s carry onboarding move-ins, not leasing"
                     % (len(onboarding_months),
                        "month" if len(onboarding_months) == 1 else "months"),
            "detail": ("Bringing a community into Rent Manager posts its whole sitting "
                       "resident base as move-ins that month. %s is the largest: %d of its "
                       "%d move-ins are loads (%s). Those months are drawn off scale on the "
                       "move chart with their true net labelled, and excluded from the "
                       "trailing-twelve net, because %s residents inherited with an "
                       "acquisition would otherwise read as a year of leasing wins. "
                       "Occupancy is measured from unit-days and is unaffected."
                       % (biggest["month"], biggest["onboarding_ins"], biggest["ins"],
                          biggest["onboarding_detail"],
                          "{:,}".format(sum(m["onboarding_ins"] for m in onboarding_months)))),
        })

    closed_mv = [m for m in move_series if not m.get("partial")]
    if len(closed_mv) >= 7:
        last_mv = closed_mv[-1]
        prior_outs = [m["outs"] for m in closed_mv[-13:-1]]
        med_outs = _median(prior_outs)
        if med_outs and last_mv["outs"] < med_outs * 0.35:
            flags.append({
                "severity": "warn",
                "title": "%s move-outs look unposted: %d against a %d-month median of %d"
                         % (last_mv["month"], last_mv["outs"], len(prior_outs), med_outs),
                "detail": ("The move-in / move-out candle for %s shows a large net gain and it "
                           "is almost certainly not real -- move-ins posted and move-outs did "
                           "not. Net movement for that month, and the net column on the move "
                           "table, are both overstated until the rest post. Occupancy itself "
                           "is measured from unit-days rather than from moves, so it is "
                           "unaffected." % last_mv["month"]),
            })

    stale_ev = [x for c in communities for x in c["evictions"]
                if not x["closed"] and (x["days_open"] or 0) > 365]
    if stale_ev:
        settled = [x for x in stale_ev if x["open_charges"] <= 0.005]
        flags.append({
            "severity": "warn",
            "title": "%d eviction %s been open more than a year"
                     % (len(stale_ev), "case has" if len(stale_ev) == 1 else "cases have"),
            "detail": ("The oldest has been open %d days. %d of the %d owe nothing at all, "
                       "which usually means the matter resolved and nobody closed it in the "
                       "tracker rather than a resident sitting in eviction for years. Either "
                       "way they inflate the funnel and the in-eviction bucket until someone "
                       "sets a close date. The %d still owing carry %s."
                       % (max(x["days_open"] for x in stale_ev), len(settled), len(stale_ev),
                          len(stale_ev) - len(settled),
                          money(sum(x["open_charges"] for x in stale_ev
                                    if x["open_charges"] > 0.005)))),
        })

    if evict_unresolved:
        flags.append({
            "severity": "info",
            "title": "%d eviction %s outside the reportable roster"
                     % (len(evict_unresolved),
                        "community is" if len(evict_unresolved) == 1 else "communities are"),
            "detail": ("The tracker carries open cases at these, but they are sold or not "
                       "marked Reportable, so their cases are excluded along with the rest "
                       "of their numbers: %s." % ", ".join(sorted(evict_unresolved))),
        })

    if reg.unmapped_stages:
        flags.append({
            "severity": "warn",
            "title": "%d eviction stage %s not mapped to a phase"
                     % (len(reg.unmapped_stages),
                        "is" if len(reg.unmapped_stages) == 1 else "are"),
            "detail": ("These show as Stage not mapped in the funnel. Add them to "
                       "eviction_stages in registry.json: %s."
                       % ", ".join(sorted(reg.unmapped_stages))),
        })

    # Former-resident status is the one bucket the tracker cannot fully settle.
    if total_accts and cust_status:
        resolved = sum(1 for c in communities for a in c["ar_accounts"]
                       if a["account"] in cust_status)
        if resolved / total_accts < 0.6:
            flags.append({
                "severity": "info",
                "title": "Former-resident status is known for %d of %d balances"
                         % (resolved, total_accts),
                "detail": ("In eviction and payment plan now come from the tracker and are "
                           "solid. Former resident does not: it needs a lease that the move "
                           "history shows ended, and that history only reaches back to %s, "
                           "so an account that moved out earlier reads as needing action. "
                           "A closed eviction case recovers %d of them. Pulling move history "
                           "further back closes the rest."
                           % (months[0], sum(1 for c in communities for a in c["ar_accounts"]
                                             if a["segment_label"].startswith(
                                                 "Former resident, eviction")))),
            })

    plan = next((r for r in portfolio["ar_segments"] if r["segment"] == "payment_plan"), None)
    if not plan or plan["accounts"] < 10:
        flags.append({
            "severity": "info",
            "title": "Payment plans are still detected by charge name, not by a field",
            "detail": ("The tracker settles in-eviction and closed cases, but it carries "
                       "nothing about plans. This looks for a payment plan charge type on "
                       "the ledger and finds %d account%s, which is almost certainly under "
                       "the truth -- most plans are agreed by email and never posted as a "
                       "charge. Any account on a plan without one reads as needing action."
                       % (plan["accounts"] if plan else 0,
                          "" if plan and plan["accounts"] == 1 else "s")),
        })

    # Listed but not actually ready to show is the gap the RTM flag exposes.
    pipe = {r["stage"]: r for r in portfolio.get("home_pipeline", [])}
    not_ready = pipe.get("for_sale_prep", {}).get("homes", 0)
    if not_ready:
        flags.append({
            "severity": "warn",
            "title": "%d %s for sale but not marked Ready to Market"
                     % (not_ready, "home is" if not_ready == 1 else "homes are"),
            "detail": ("Their status says For Sale, so they are counted as sellable stock, "
                       "but the Ready to Market flag on the Asset Listing is not set. Either "
                       "the home is not actually showable yet or nobody flipped the flag. "
                       "%d of the %d homes in the pipeline carry the flag."
                       % (sum(r["rtm"] for r in portfolio.get("home_pipeline", [])),
                          sum(r["homes"] for r in portfolio.get("home_pipeline", [])))),
        })

    flags.append({
        "severity": "info",
        "title": "There is no punch stage in Rent Manager",
        "detail": ("The home pipeline runs rehab straight to Ready to Market because no "
                   "punch status and no punch field exist on the Asset Listing. Ready to "
                   "Market itself is a user-defined field, not a status, which is why a "
                   "home can read For Sale and not-ready at the same time. Adding a punch "
                   "status is the only way that step becomes reportable."),
    })

    rr_missing = [c["name"] for c in communities if not c["rent_roll"]]
    if rr_missing:
        flags.append({
            "severity": "info",
            "title": "%d %s no Rent Manager unit detail"
                     % (len(rr_missing), "community has" if len(rr_missing) == 1 else "communities have"),
            "detail": ("Their rent roll, vacancy and account drill-ins are empty because the "
                       "Rent Manager property list did not return an id for them: %s."
                       % ", ".join(sorted(rr_missing))),
        })

    rec = portfolio["expenses"].get("utility_recapture_pct")
    target = cfg.get("expense_buckets", {}).get("utility_recapture", {}).get("target_pct")
    if rec is not None and target and rec < target:
        e = portfolio["expenses"]
        flags.append({
            "severity": "warn",
            "title": "Utility recapture is %.0f%% against a %d%% target" % (rec, target),
            "detail": ("%s billed back against %s of utility spend in %s, so the portfolio "
                       "absorbed %s. Recapture is a pricing and metering question, not a "
                       "controllable expense, which is why it sits on its own."
                       % (money(e.get("utility_reimbursements", 0)), money(e.get("utilities", 0)),
                          closed_month, money(abs(e.get("utility_net", 0))))),
        })

    no_budget = [c["name"] for c in communities
                 if c["closed"].get("revenue") and not c["closed"].get("revenue_budget")]
    if no_budget:
        flags.append({
            "severity": "info",
            "title": "%d %s revenue with no budget loaded"
                     % (len(no_budget), "community posts" if len(no_budget) == 1 else "communities post"),
            "detail": "Budget variance is blank for: %s." % ", ".join(sorted(no_budget)),
        })

    zero_occ = [(c["name"], c["closed"].get("units", 0)) for c in communities
                if c["closed"].get("units", 0) >= 10 and c["closed"].get("occupancy") == 0.0]
    if zero_occ:
        flags.append({
            "severity": "warn",
            "title": "%d %s 0%% occupancy on %d lots"
                     % (len(zero_occ), "community reports" if len(zero_occ) == 1 else "communities report",
                        sum(u for _, u in zero_occ)),
            "detail": ("Either genuinely empty or the ledger is not tracking occupancy: %s."
                       % ", ".join("%s (%d lots)" % (n, u) for n, u in sorted(zero_occ))),
        })

    payload = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "RentViewer data warehouse (Rent Manager) · roster from Property Data Sheet",
        "period": {
            "closed": closed_month,
            "live": live_month,
            "live_day": live_day,
            "days_in_live": days_in_live,
            "grace_day": grace_day,
            "budget_from": budget_from,
            "first": months[0],
            "months": months,
        },
        "thresholds": reg.thresholds,
        "portfolio": portfolio,
        "vehicles": vehicles,
        "vacancy_reasons": vacancy_reasons,
        "reason_meta": reason_meta,
        "communities": communities,
        "trends": {
            "occupancy": occ_series,
            "ar": ar_series,
            "collections": coll_series,
            "moves": move_series,
            "financials": fin_series,
        },
        "flags": flags,
    }

    os.makedirs(out_dir, exist_ok=True)
    dash = os.path.join(out_dir, "dashboard.json")
    with open(dash, "w") as f:
        json.dump(payload, f, indent=1)
    with open(os.path.join(out_dir, "dashboard.min.json"), "w") as f:
        json.dump(payload, f, separators=(",", ":"))
    with open(os.path.join(out_dir, "registry_audit.json"), "w") as f:
        json.dump({
            "generated_at": payload["generated_at"],
            "reportable_source": REPORTABLE_FILE,
            "counts": {
                "names_seen": len(reg.audit),
                "reportable_in_pds": len(reportable_rows),
                "communities": len(communities),
                "dropped": sum(1 for a in reg.audit.values() if a["disposition"] == "drop"),
                "rolled_up": len(rolled),
                "reportable_without_data": len(absent),
            },
            "reportable_without_warehouse_data": absent,
            "names": dict(sorted(reg.audit.items())),
        }, f, indent=1)

    log("wrote %s (%.0f KB)" % (dash, os.path.getsize(dash) / 1024))
    log("CLOSED %s: %d communities, %s lots, %.1f%% occ, %s AR, %.1f%% collections"
        % (closed_month, cl["communities"], "{:,}".format(cl["total_units"]),
           cl["occupancy"], money(cl["ar_total"]), cl["collection_pct"]))
    log("LIVE   %s (day %d): %.1f%% occ, %s AR, %s past due 30+, %s of %s billed still out"
        % (live_month, live_day, lv["occupancy"], money(lv["ar_total"]),
           money(lv["ar_past_due_30plus"]), money(lv["outstanding"]), money(lv["charged"])))
    for fl in flags:
        log("  [%s] %s" % (fl["severity"].upper(), fl["title"]))
    return payload


def main():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=os.path.join(here, "pipeline", "raw"))
    ap.add_argument("--out", default=os.path.join(here, "data"))
    ap.add_argument("--registry", default=os.path.join(here, "pipeline", "registry.json"))
    args = ap.parse_args()
    build(args.raw, args.out, args.registry)


if __name__ == "__main__":
    main()
