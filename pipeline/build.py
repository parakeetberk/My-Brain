#!/usr/bin/env python3
"""
build.py -- Parakeet ops dashboard data build.

Turns the raw RentViewer warehouse pulls in pipeline/raw/ into a single
versioned payload at data/dashboard.json, plus data/registry_audit.json
so every property name the warehouse handed us has a visible disposition.

    python3 pipeline/build.py [--raw pipeline/raw] [--out data]

The raw files are produced by the warehouse queries declared in
pipeline/queries.json. See docs/ARCHITECTURE.md for the refresh loop.
"""
import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone

SCHEMA_VERSION = 3

# Warehouse model prefixes, and the raw file each one arrives in.
SOURCES = {
    "occupancy": ("occupancy_by_property_month.json", "VW_Rental_Unit_Listing."),
    "unit_types": ("unit_listing_by_type.json", "VW_Rental_Unit_Listing."),
    "ar": ("ar_by_property_month.json", "VW_Aged_Receivables."),
    "rentroll": ("rentroll_by_property_month.json", "VW_Summary_Rent_Roll."),
    "moves": ("moves_by_property_month.json", "VW_MoveIns_MoveOuts."),
    "financials": ("financials_by_property_month.json", "VW_Budget_Comparison."),
}


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
        count = blob.get("rowCount", len(rows))
        # A pull that hit its row limit is silently incomplete; refuse it rather
        # than publish numbers that are quietly short.
        if count and count == blob.get("_limit"):
            die("%s hit its row limit (%d) and is truncated. Re-pull with a higher limit."
                % (fname, count))
        out[key] = (rows, prefix)
        log("loaded %-38s %5d rows" % (fname, len(rows)))
    if missing:
        die("missing raw pulls: %s\nRun the queries in pipeline/queries.json first."
            % ", ".join(missing))
    return out


# ---------------------------------------------------------------- registry ---

class Registry:
    """Decides what each warehouse propertyName is, and records why."""

    def __init__(self, cfg):
        self.cfg = cfg
        self.retired_res = [re.compile(p) for p in cfg["rules"]["retired_prefix"]["patterns"]]
        self.sold = {}
        for entry in cfg["sold"]:
            for name in entry["match"]:
                self.sold[name.lower()] = entry["reason"]
        self.non_community = {e["match"].lower(): e["reason"] for e in cfg["non_community"]}
        self.roll_up = {e["match"].lower(): e for e in cfg["roll_up"]}
        self.aliases = {k.lower(): v for k, v in cfg["aliases"].items()}
        self.segments = cfg["segments"]
        self.thresholds = cfg["thresholds"]

        # Flatten the unit-type taxonomy into lookup tables.
        self.ut_class = {}
        self.ut_rentable = {}
        for group, buckets in cfg["unit_types"].items():
            for bucket, names in buckets.items():
                for n in names:
                    self.ut_class[n] = group
                    self.ut_rentable[n] = bucket
        self.audit = {}

    def unit_type(self, name):
        """(group, bucket) for a unit type; unknown types count as rentable MH."""
        if name in self.ut_class:
            return self.ut_class[name], self.ut_rentable[name]
        return "UNKNOWN", "rentable"

    def classify(self, name, latest_month=None, current_month=None, occupancy=None,
                 stale_threshold=2):
        """
        Return (disposition, canonical_name, detail).

        disposition is one of:
          keep        -- a real community, reports on its own row
          roll_up     -- money attributes to `canonical_name`, no lots of its own
          alias       -- same asset as `canonical_name`, figures merge into it
          drop        -- excluded, `detail` says why
        """
        low = name.lower()

        for rx in self.retired_res:
            if rx.match(name):
                return "drop", None, self.cfg["rules"]["retired_prefix"]["reason"]

        if low in self.sold:
            return "drop", None, "Sold: " + self.sold[low]

        if low in self.non_community:
            return "drop", None, self.non_community[low]

        if low in self.roll_up:
            e = self.roll_up[low]
            return "roll_up", e["parent"], "%s sub-ledger" % e["kind"]

        if low in self.aliases:
            return "alias", self.aliases[low], "Duplicate ledger for the same asset"

        if latest_month and current_month:
            gap = months_between(latest_month, current_month)
            if gap >= stale_threshold:
                return "drop", None, ("No snapshot since %s (%d periods stale); disposed or renamed"
                                      % (latest_month, gap))

        return "keep", name, ""

    def record(self, name, disposition, canonical, detail):
        self.audit[name] = {
            "disposition": disposition,
            "canonical": canonical,
            "reason": detail,
        }


# RM writes the same park under several suffix conventions. Reducing a name to
# its stem is what lets a dead "Cedar Grove MHC" find its live twin
# "Cedar Grove Manufactured Housing Community".
_SUFFIXES = [
    "manufactured housing community", "mobile home park", "trailer park",
    "rv resort", "mhc", "mhp", "mh", "rv", "utility", "water", "homes",
]


def community_key(name):
    s = re.sub(r"[^a-z0-9 ]+", " ", name.lower())
    s = re.sub(r"\s+", " ", s).strip()
    changed = True
    while changed:
        changed = False
        for suf in _SUFFIXES:
            if s.endswith(" " + suf) or s == suf:
                s = s[: -len(suf)].strip()
                changed = True
    return s or name.lower()


def months_between(a, b):
    ay, am = int(a[:4]), int(a[5:7])
    by, bm = int(b[:4]), int(b[5:7])
    return (by - ay) * 12 + (bm - am)


# ------------------------------------------------------------------- build ---

def build(raw_dir, out_dir, registry_path):
    with open(registry_path) as f:
        reg = Registry(json.load(f))

    raw = load_raw(raw_dir)

    # ---- establish the reporting calendar from the occupancy snapshots ----
    occ_rows, OP = raw["occupancy"]
    months = sorted({m for m in (month_of(r.get(OP + "reportMonth")) for r in occ_rows) if m})
    if not months:
        die("no reportMonth values found in the occupancy pull")
    current_month = months[-1]
    closed_month = months[-2] if len(months) > 1 else current_month

    # The live month is a partial snapshot: rent bills on the 1st and collects
    # through the month, so its AR is inflated and its collections understated.
    # Everything headline is quoted on the last CLOSED month; the partial month
    # is carried separately and labelled.
    log("periods %s .. %s  (headline month: %s, live partial: %s)"
        % (months[0], current_month, closed_month, current_month))

    # ---- pass 1: what is each property name, and when did it last report? ----
    latest_seen = {}
    for key in ("occupancy", "ar", "rentroll", "moves", "financials"):
        rows, P = raw[key]
        mkey = "month" if key == "moves" else ("endDate" if key == "financials" else "reportMonth")
        for r in rows:
            name = r.get(P + "propertyName")
            mo = month_of(r.get(P + mkey))
            if not name or not mo:
                continue
            if name not in latest_seen or mo > latest_seen[name]:
                latest_seen[name] = mo

    stale_threshold = reg.cfg["rules"]["drop_stale_months"]["threshold"]
    occupancy_latest = {}
    for r in occ_rows:
        name = r.get(OP + "propertyName")
        mo = month_of(r.get(OP + "reportMonth"))
        if name and mo == current_month:
            occupancy_latest[name] = num(r.get(OP + "occupancyRate"))

    resolve = {}
    for name in sorted(latest_seen):
        disp, canon, why = reg.classify(
            name,
            latest_month=latest_seen.get(name),
            current_month=current_month,
            occupancy=occupancy_latest.get(name),
            stale_threshold=stale_threshold,
        )
        reg.record(name, disp, canon, why)
        resolve[name] = (disp, canon)

    # Drop zero-occupancy twins: a record with 0% occupancy whose community is
    # already covered by a live record. Without this the portfolio denominator
    # double-counts every renamed park.
    twin_rule = reg.cfg["rules"]["drop_zero_occupancy_twin"]
    if twin_rule["enabled"]:
        live_by_key = defaultdict(list)
        for name, (disp, canon) in resolve.items():
            if disp == "keep":
                live_by_key[community_key(name)].append(name)
        for name, (disp, canon) in list(resolve.items()):
            if disp != "keep":
                continue
            if occupancy_latest.get(name, None) != 0.0:
                continue
            # A record declared in `segments` is a known-real MH/RV split. An
            # empty RV section is a leasing fact worth showing, not a duplicate
            # ledger to sweep away, so leave it in and let the flag call it out.
            if twin_rule.get("exempt_declared_segments") and name in reg.segments:
                continue
            siblings = [s for s in live_by_key[community_key(name)]
                        if s != name and occupancy_latest.get(s, 0.0) > 0.0]
            if siblings:
                why = ("%s; live record is %s"
                       % (reg.cfg["rules"]["drop_zero_occupancy_twin"]["reason"], siblings[0]))
                resolve[name] = ("drop", None)
                reg.record(name, "drop", None, why)

    def target(name):
        """Where a row's MONEY lands, or None if the row is excluded."""
        disp, canon = resolve.get(name, ("drop", None))
        if disp == "drop":
            return None
        if disp in ("alias", "roll_up"):
            # Follow one hop; the parent may itself be dropped.
            pdisp, pcanon = resolve.get(canon, ("keep", canon))
            if pdisp == "drop":
                return None
            return pcanon or canon
        return name

    def target_units(name):
        """
        Where a row's LOTS and occupancy land, or None if they must be ignored.

        Money and lots do not merge the same way. A utility sub-ledger carries
        real AR against lots that are counted on its parent, and an alias is a
        stale duplicate of a park that is already counted once. Summing either
        one's unit counts inflates the denominator and halves the occupancy it
        is supposed to explain, so only a `keep` record contributes lots.
        """
        disp, _ = resolve.get(name, ("drop", None))
        return name if disp == "keep" else None

    kept = sorted({t for t in (target(n) for n in resolve) if t})
    log("properties: %d names -> %d communities (%d dropped, %d rolled up/aliased)"
        % (len(resolve), len(kept),
           sum(1 for d, _ in resolve.values() if d == "drop"),
           sum(1 for d, _ in resolve.values() if d in ("alias", "roll_up"))))

    # ---- occupancy by community and month ----
    occ = defaultdict(lambda: defaultdict(lambda: {"units": 0.0, "vac_days": 0.0, "avail_days": 0.0,
                                                   "actual_rent": 0.0, "market_rent": 0.0}))
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
        # Recompute from unit-days rather than averaging percentages, so a
        # 400-lot park does not carry the same weight as a 19-lot park.
        return (d["avail_days"] - d["vac_days"]) / d["avail_days"] * 100 if d["avail_days"] else 0.0

    # ---- vacancy composition from the current unit-type snapshot ----
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

    # ---- AR by community and month ----
    ar_rows, AP = raw["ar"]
    ar = defaultdict(lambda: defaultdict(lambda: {"total": 0.0, "b0_30": 0.0, "b31_60": 0.0,
                                                  "b61_90": 0.0, "b90p": 0.0, "accounts": 0.0}))
    for r in ar_rows:
        t = target(r.get(AP + "propertyName"))
        mo = month_of(r.get(AP + "reportMonth"))
        if not t or not mo:
            continue
        d = ar[t][mo]
        d["total"] += num(r.get(AP + "agedReceivablesTotal"))
        d["b0_30"] += num(r.get(AP + "current0to30"))
        d["b31_60"] += num(r.get(AP + "days31to60"))
        d["b61_90"] += num(r.get(AP + "days61to90"))
        d["b90p"] += num(r.get(AP + "over90Days"))
        d["accounts"] += num(r.get(AP + "customersWithBalance"))

    # ---- collections by community and month ----
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

    # ---- moves by community and month ----
    mv_rows, MP = raw["moves"]
    mv = defaultdict(lambda: defaultdict(lambda: {"ins": 0.0, "outs": 0.0}))
    for r in mv_rows:
        t = target(r.get(MP + "propertyName"))
        mo = month_of(r.get(MP + "month"))
        if not t or not mo:
            continue
        mv[t][mo]["ins"] += num(r.get(MP + "moveIns"))
        mv[t][mo]["outs"] += num(r.get(MP + "moveOuts"))

    # ---- financials by community and month ----
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

    # ---- assemble per-community rows ----
    communities = []
    for name in kept:
        o_cur = occ[name].get(current_month)
        o_hdl = occ[name].get(closed_month) or o_cur
        a_hdl = ar[name].get(closed_month)
        a_cur = ar[name].get(current_month)
        r_hdl = rr[name].get(closed_month)

        if not o_hdl and not a_hdl and not r_hdl:
            continue

        units = int(o_hdl["units"]) if o_hdl else 0
        occ_now = occ_pct(o_hdl) if o_hdl else 0.0

        # Rentable-adjusted occupancy: drop lots that cannot be leased at all
        # (unusable, demo) out of the denominator.
        comp = vac_comp.get(name, {})
        r_units = r_avail = r_vac = 0.0
        impaired = 0.0
        not_rentable = 0.0
        for tname, d in comp.items():
            group, bucket = reg.unit_type(tname)
            if group == "NON_REVENUE" or bucket == "not_rentable":
                not_rentable += d["units"]
                continue
            r_units += d["units"]
            r_avail += d["avail_days"]
            r_vac += d["vac_days"]
            if bucket == "rentable_impaired":
                impaired += d["units"]
        occ_rentable = ((r_avail - r_vac) / r_avail * 100) if r_avail else occ_now

        mix = type_mix.get(name, {})
        if mix:
            kind = max(mix, key=lambda k: mix[k])
        else:
            kind = "MH"
        seg = reg.segments.get(name, {})

        ar_total = a_hdl["total"] if a_hdl else 0.0
        over90 = a_hdl["b90p"] if a_hdl else 0.0

        f_hdl = fin[name].get(closed_month)
        ytd = {"rev": 0.0, "rev_bud": 0.0, "opex": 0.0, "opex_bud": 0.0,
               "noi": 0.0, "noi_bud": 0.0}
        year = current_month[:4]
        for mo, d in fin[name].items():
            if mo[:4] == year and mo <= closed_month:
                for k in ytd:
                    ytd[k] += d[k]

        communities.append({
            "name": name,
            "park": seg.get("park") or name,
            "kind": seg.get("type") or kind,
            "units": units,
            "occupied": int(round(units * occ_now / 100)) if units else 0,
            "occupancy": rnd(occ_now),
            "occupancy_rentable": rnd(occ_rentable),
            "rentable_units": int(r_units),
            "impaired_units": int(impaired),
            "not_rentable_units": int(not_rentable),
            "occupancy_prev": rnd(occ_pct(occ[name][months[-3]])) if len(months) > 2 and months[-3] in occ[name] else None,
            "actual_rent": rnd(o_hdl["actual_rent"], 0) if o_hdl else 0,
            "market_rent": rnd(o_hdl["market_rent"], 0) if o_hdl else 0,
            "ar_total": rnd(ar_total, 0),
            "ar_0_30": rnd(a_hdl["b0_30"], 0) if a_hdl else 0,
            "ar_31_60": rnd(a_hdl["b31_60"], 0) if a_hdl else 0,
            "ar_61_90": rnd(a_hdl["b61_90"], 0) if a_hdl else 0,
            "ar_90_plus": rnd(over90, 0),
            "ar_over90_share": rnd(over90 / ar_total * 100) if ar_total else 0.0,
            "ar_accounts": int(a_hdl["accounts"]) if a_hdl else 0,
            "ar_live": rnd(a_cur["total"], 0) if a_cur else None,
            "ar_per_unit": rnd(ar_total / units, 0) if units else 0,
            "charged": rnd(r_hdl["charged"], 0) if r_hdl else 0,
            "paid": rnd(r_hdl["paid"], 0) if r_hdl else 0,
            "collection_pct": rnd(coll_pct(r_hdl)) if r_hdl else 0.0,
            "vacancy_loss": rnd(r_hdl["vac_loss"], 0) if r_hdl else 0,
            "loss_to_lease": rnd(r_hdl["ltl"], 0) if r_hdl else 0,
            "move_ins": int(mv[name].get(closed_month, {}).get("ins", 0)),
            "move_outs": int(mv[name].get(closed_month, {}).get("outs", 0)),
            "revenue": rnd(f_hdl["rev"], 0) if f_hdl else 0,
            "revenue_budget": rnd(f_hdl["rev_bud"], 0) if f_hdl else 0,
            "opex": rnd(f_hdl["opex"], 0) if f_hdl else 0,
            "opex_budget": rnd(f_hdl["opex_bud"], 0) if f_hdl else 0,
            "noi": rnd(f_hdl["noi"], 0) if f_hdl else 0,
            "noi_budget": rnd(f_hdl["noi_bud"], 0) if f_hdl else 0,
            "noi_margin": rnd(f_hdl["noi"] / f_hdl["rev"] * 100) if f_hdl and f_hdl["rev"] else 0.0,
            "ytd_revenue": rnd(ytd["rev"], 0),
            "ytd_revenue_budget": rnd(ytd["rev_bud"], 0),
            "ytd_noi": rnd(ytd["noi"], 0),
            "ytd_noi_budget": rnd(ytd["noi_bud"], 0),
            "vacancy_composition": sorted(
                [{"type": t,
                  "group": reg.unit_type(t)[0],
                  "bucket": reg.unit_type(t)[1],
                  "units": int(d["units"]),
                  "vacant": int(round(d["vac_days"] / (d["avail_days"] / d["units"]))) if d["units"] and d["avail_days"] else 0}
                 for t, d in comp.items()],
                key=lambda x: -x["units"]),
        })

    communities.sort(key=lambda c: c["name"])

    # ---- portfolio trends ----
    def series(store, fn, label_months=None):
        out = []
        for mo in (label_months or months):
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
                out.append({"month": mo, "partial": mo == current_month, **fn(agg)})
        return out

    occ_series = series(occ, lambda a: {
        "occupancy": rnd(occ_pct(a)),
        "units": int(a["units"]),
        "occupied": int(round((a["avail_days"] - a["vac_days"]) / a["avail_days"] * a["units"] / 100 * 100 / 100)) if a["avail_days"] else 0,
    })
    ar_series = series(ar, lambda a: {
        "total": rnd(a["total"], 0),
        "b0_30": rnd(a["b0_30"], 0),
        "b31_60": rnd(a["b31_60"], 0),
        "b61_90": rnd(a["b61_90"], 0),
        "b90p": rnd(a["b90p"], 0),
        "accounts": int(a["accounts"]),
    })
    coll_series = series(rr, lambda a: {
        "collection_pct": rnd(coll_pct(a)),
        "charged": rnd(a["charged"], 0),
        "paid": rnd(a["paid"], 0),
    })
    move_series = series(mv, lambda a: {
        "ins": int(a["ins"]), "outs": int(a["outs"]), "net": int(a["ins"] - a["outs"]),
    })
    fin_series = series(fin, lambda a: {
        "revenue": rnd(a["rev"], 0), "revenue_budget": rnd(a["rev_bud"], 0),
        "opex": rnd(a["opex"], 0), "opex_budget": rnd(a["opex_bud"], 0),
        "noi": rnd(a["noi"], 0), "noi_budget": rnd(a["noi_bud"], 0),
    })

    def closed(s):
        return [p for p in s if not p["partial"]]

    def at(s, mo):
        return next((p for p in s if p["month"] == mo), None)

    # ---- portfolio headline ----
    mh = [c for c in communities if c["kind"] == "MH"]
    rv = [c for c in communities if c["kind"] == "RV"]
    tot_units = sum(c["units"] for c in communities)
    tot_occ = sum(c["occupied"] for c in communities)
    ar_hdl = at(ar_series, closed_month) or {}
    coll_hdl = at(coll_series, closed_month) or {}
    fin_hdl = at(fin_series, closed_month) or {}
    ar_prev = closed(ar_series)[-2] if len(closed(ar_series)) > 1 else {}
    occ_hdl = at(occ_series, closed_month) or {}
    occ_prev = closed(occ_series)[-2] if len(closed(occ_series)) > 1 else {}

    ytd_fin = defaultdict(float)
    year = current_month[:4]
    for p in closed(fin_series):
        if p["month"][:4] == year:
            for k in ("revenue", "revenue_budget", "opex", "opex_budget", "noi", "noi_budget"):
                ytd_fin[k] += p[k]

    def wavg(rows, value, weight):
        wt = sum(r[weight] for r in rows)
        return rnd(sum(r[value] * r[weight] for r in rows) / wt) if wt else 0.0

    portfolio = {
        "communities": len(communities),
        "parks": len({c["park"] for c in communities}),
        "total_units": tot_units,
        "total_occupied": tot_occ,
        "occupancy": occ_hdl.get("occupancy", 0.0),
        "occupancy_prev": occ_prev.get("occupancy"),
        "occupancy_rentable": wavg(communities, "occupancy_rentable", "rentable_units"),
        "mh_units": sum(c["units"] for c in mh),
        "mh_occupancy": wavg(mh, "occupancy", "units"),
        "rv_units": sum(c["units"] for c in rv),
        "rv_occupancy": wavg(rv, "occupancy", "units"),
        "impaired_units": sum(c["impaired_units"] for c in communities),
        "not_rentable_units": sum(c["not_rentable_units"] for c in communities),
        "ar_total": ar_hdl.get("total", 0),
        "ar_prev": ar_prev.get("total"),
        "ar_90_plus": ar_hdl.get("b90p", 0),
        "ar_over90_share": rnd(ar_hdl.get("b90p", 0) / ar_hdl["total"] * 100) if ar_hdl.get("total") else 0.0,
        "ar_accounts": ar_hdl.get("accounts", 0),
        "ar_live": (at(ar_series, current_month) or {}).get("total"),
        "collection_pct": coll_hdl.get("collection_pct", 0.0),
        "charged": coll_hdl.get("charged", 0),
        "paid": coll_hdl.get("paid", 0),
        "collection_ttm": rnd(sum(p["collection_pct"] for p in closed(coll_series)[-12:]) /
                              max(1, len(closed(coll_series)[-12:]))),
        "revenue": fin_hdl.get("revenue", 0),
        "revenue_budget": fin_hdl.get("revenue_budget", 0),
        "noi": fin_hdl.get("noi", 0),
        "noi_budget": fin_hdl.get("noi_budget", 0),
        "noi_margin": rnd(fin_hdl.get("noi", 0) / fin_hdl["revenue"] * 100) if fin_hdl.get("revenue") else 0.0,
        "ytd_revenue": rnd(ytd_fin["revenue"], 0),
        "ytd_revenue_budget": rnd(ytd_fin["revenue_budget"], 0),
        "ytd_noi": rnd(ytd_fin["noi"], 0),
        "ytd_noi_budget": rnd(ytd_fin["noi_budget"], 0),
        "move_ins": (at(move_series, closed_month) or {}).get("ins", 0),
        "move_outs": (at(move_series, closed_month) or {}).get("outs", 0),
        "vacancy_loss": sum(c["vacancy_loss"] for c in communities),
        "loss_to_lease": sum(c["loss_to_lease"] for c in communities),
    }

    # ---- data-quality flags: say what looks wrong instead of hiding it ----
    flags = []

    if unknown_types:
        flags.append({
            "severity": "warn",
            "title": "Unclassified unit types",
            "detail": ("These unit types are not in registry.json and were counted as rentable MH: %s"
                       % ", ".join(sorted(unknown_types))),
        })

    live_ar = portfolio.get("ar_live")
    if live_ar and portfolio["ar_total"]:
        jump = (live_ar - portfolio["ar_total"]) / portfolio["ar_total"] * 100
        if jump > 20:
            flags.append({
                "severity": "info",
                "title": "Live month AR is a partial snapshot",
                "detail": ("%s AR reads %s against %s for closed %s (+%.0f%%). Rent bills on the 1st "
                           "and collects through the month, so the live figure runs hot. Headline "
                           "numbers use %s."
                           % (current_month, money(live_ar), money(portfolio["ar_total"]),
                              closed_month, jump, closed_month)),
            })

    if portfolio.get("ar_prev") and portfolio["ar_total"]:
        chg = (portfolio["ar_total"] - portfolio["ar_prev"]) / portfolio["ar_prev"] * 100
        if abs(chg) > 10:
            flags.append({
                "severity": "warn" if chg > 0 else "info",
                "title": "AR moved %.0f%% month over month" % chg,
                "detail": "%s -> %s between the last two closed months."
                          % (money(portfolio["ar_prev"]), money(portfolio["ar_total"])),
            })

    all_ar = [p for p in closed(ar_series)]
    if len(all_ar) >= 13:
        yoy = (all_ar[-1]["total"] - all_ar[-13]["total"]) / all_ar[-13]["total"] * 100 if all_ar[-13]["total"] else 0
        if abs(yoy) > 15:
            flags.append({
                "severity": "warn" if yoy > 0 else "info",
                "title": "AR is %.0f%% versus a year ago" % yoy,
                "detail": "%s in %s against %s in %s."
                          % (money(all_ar[-1]["total"]), all_ar[-1]["month"],
                             money(all_ar[-13]["total"]), all_ar[-13]["month"]),
            })

    # Communities whose AR sits entirely in 90+ read like a frozen ledger.
    frozen = [c["name"] for c in communities
              if c["ar_total"] > 25000 and c["ar_over90_share"] >= 99.5]
    if frozen:
        flags.append({
            "severity": "warn",
            "title": "%d communities have 100%% of AR in the 90+ bucket" % len(frozen),
            "detail": ("Nothing current or mid-aged at all, which usually means a stale or "
                       "migrated ledger rather than live delinquency: %s. Worth a Rent Manager "
                       "check before these drive collections decisions." % ", ".join(sorted(frozen))),
        })

    # A community carrying lots at exactly 0% occupancy is either genuinely empty
    # or its ledger stopped tracking occupancy. Either way it is a question, and
    # it drags the portfolio denominator down, so name it.
    zero_occ = [(c["name"], c["units"]) for c in communities
                if c["units"] >= 10 and c["occupancy"] == 0.0]
    if zero_occ:
        flags.append({
            "severity": "warn",
            "title": "%d communities report 0%% occupancy on %d lots"
                     % (len(zero_occ), sum(u for _, u in zero_occ)),
            "detail": ("Either genuinely empty or the ledger is not tracking occupancy. These lots "
                       "stay in the portfolio denominator, so they pull reported occupancy down: %s. "
                       "Confirm in Rent Manager, then either fix the ledger or add the record to "
                       "registry.json."
                       % ", ".join("%s (%d lots)" % (n, u) for n, u in sorted(zero_occ))),
        })

    no_budget = [c["name"] for c in communities if c["revenue"] and not c["revenue_budget"]]
    if no_budget:
        flags.append({
            "severity": "info",
            "title": "%d communities post revenue with no budget loaded" % len(no_budget),
            "detail": "Budget variance is blank for: %s." % ", ".join(sorted(no_budget)[:12]),
        })

    dropped_stale = sorted(n for n, a in reg.audit.items()
                           if a["disposition"] == "drop" and "stale" in a["reason"])
    if dropped_stale:
        flags.append({
            "severity": "info",
            "title": "%d property records dropped as stale" % len(dropped_stale),
            "detail": ("No recent snapshot, treated as disposed or renamed: %s. If any of these "
                       "is still live, it needs a look in Rent Manager."
                       % ", ".join(dropped_stale)),
        })

    unclassified = sorted(n for n, a in reg.audit.items()
                          if a["disposition"] == "keep" and n not in {c["name"] for c in communities})
    if unclassified:
        flags.append({
            "severity": "info",
            "title": "%d kept records produced no rows" % len(unclassified),
            "detail": ", ".join(unclassified),
        })

    payload = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "RentViewer data warehouse (Rent Manager)",
        "period": {
            "headline": closed_month,
            "live_partial": current_month,
            "first": months[0],
            "months": months,
        },
        "thresholds": reg.thresholds,
        "portfolio": portfolio,
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
        json.dump(payload, f, indent=1, sort_keys=False)
    with open(os.path.join(out_dir, "dashboard.min.json"), "w") as f:
        json.dump(payload, f, separators=(",", ":"))
    with open(os.path.join(out_dir, "registry_audit.json"), "w") as f:
        json.dump({
            "generated_at": payload["generated_at"],
            "current_month": current_month,
            "counts": {
                "names_seen": len(reg.audit),
                "communities": len(communities),
                "dropped": sum(1 for a in reg.audit.values() if a["disposition"] == "drop"),
                "rolled_up": sum(1 for a in reg.audit.values() if a["disposition"] == "roll_up"),
                "aliased": sum(1 for a in reg.audit.values() if a["disposition"] == "alias"),
            },
            "names": dict(sorted(reg.audit.items())),
        }, f, indent=1)

    log("wrote %s (%.0f KB)" % (dash, os.path.getsize(dash) / 1024))
    log("portfolio: %d communities, %s lots, %.1f%% occupancy, %s AR, %.1f%% collections (as of %s)"
        % (portfolio["communities"], "{:,}".format(portfolio["total_units"]),
           portfolio["occupancy"], money(portfolio["ar_total"]),
           portfolio["collection_pct"], closed_month))
    for fl in flags:
        log("  [%s] %s" % (fl["severity"].upper(), fl["title"]))
    return payload


def money(v):
    v = v or 0
    if abs(v) >= 1_000_000:
        return "$%.2fM" % (v / 1_000_000)
    if abs(v) >= 1_000:
        return "$%.0fK" % (v / 1_000)
    return "$%.0f" % v


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
