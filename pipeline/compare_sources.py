#!/usr/bin/env python3
"""
Diff a candidate warehouse pull against the Rent Manager report it would
replace, before anything is cut over.

The two sources agree on nothing structurally: the warehouse names a property
"American" where Rent Manager says "American Mobile Home Park", keys a unit by
(propertyName, unitName) where Rent Manager uses (EntitiesShortName,
SubEntitiesName), and returns 106 properties where the RM pull was scoped to
the reportable roster. So the join goes through the same alias map build.py
uses, and the report separates three failure modes that look identical in a
row-count summary:

  * a unit only one source knows about   -> a coverage gap
  * a unit both know, values disagree    -> a definition or as-of gap
  * a unit both know, values agree       -> safe to cut over

Only the third kind is evidence. Run it, read it, and do not swap a source
until the first two are explained rather than merely small.

    compare_sources.py rentroll | ar | moves
"""
import json
import os
import sys
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(path):
    d = json.load(open(os.path.join(REPO, path)))
    return d["rows"] if isinstance(d, dict) and "rows" in d else d


def num(v):
    try:
        return round(float(v or 0), 2)
    except (TypeError, ValueError):
        return 0.0


def build_alias():
    """propertyName / short name / community -> the canonical roster name."""
    look = {}
    for p in load("pipeline/raw/pds_reportable.json"):
        canon = p["property_name"]
        for k in (p.get("short_name"), p.get("property_name"), p.get("community")):
            if k and str(k).strip():
                look[str(k).strip().upper()] = canon
    return look


def resolve(look, *candidates):
    for c in candidates:
        if c is None:
            continue
        s = str(c).strip().upper()
        if s in look:
            return look[s]
    return None


def money(x):
    return ("-$" if x < 0 else "$") + format(abs(round(x)), ",")


def report(name, wh_rows, rm_rows, wh_key, rm_key, fields):
    """fields: [(label, wh_field, rm_field)]"""
    look = build_alias()

    def label_of(r):
        """Whatever this row calls its property, whichever source it came from."""
        for f in ("VW_Summary_Rent_Roll.propertyName", "VW_Aged_Receivables.propertyName",
                  "VW_MoveIns_MoveOuts.propertyName", "propertyName",
                  "EntitiesName", "EntitiesShortName", "PrimaryLeasePropertyShortName"):
            v = r.get(f)
            if v not in (None, ""):
                return str(v)
        return "(no property name on the row)"

    def index(rows, keyfn, tag):
        out, unmapped = {}, defaultdict(int)
        for r in rows:
            k = keyfn(look, r)
            if k is None:
                unmapped[label_of(r)] += 1
                continue
            # a unit can legitimately appear twice (two customers on one lot),
            # so accumulate rather than overwrite -- overwriting would hide it
            out.setdefault(k, []).append(r)
        if unmapped:
            print("  %s rows outside the reportable roster: %d across %d names"
                  % (tag, sum(unmapped.values()), len(unmapped)))
            # Naming them is the point. A property dropped here because it is
            # genuinely not reportable is fine; one dropped because the alias
            # map does not know its warehouse spelling is a silent data loss.
            for n, c in sorted(unmapped.items(), key=lambda x: -x[1])[:12]:
                print("       %-46s %d rows" % (n[:46], c))
        return out

    wh = index(wh_rows, wh_key, "warehouse")
    rm = index(rm_rows, rm_key, "rent manager")

    both = set(wh) & set(rm)
    only_wh = set(wh) - set(rm)
    only_rm = set(rm) - set(wh)

    stats = {"shared": len(both), "only_wh": len(only_wh), "only_rm": len(only_rm)}

    print("\n  keys: %s in warehouse, %s in rent manager, %s in both"
          % (format(len(wh), ","), format(len(rm), ","), format(len(both), ",")))
    print("  only in warehouse: %s     only in rent manager: %s"
          % (format(len(only_wh), ","), format(len(only_rm), ",")))

    for label, sample in (("only in warehouse", only_wh), ("only in rent manager", only_rm)):
        if not sample:
            continue
        by_prop = defaultdict(int)
        for k in sample:
            by_prop[k[0]] += 1
        print("\n  %s, by community (top 8):" % label)
        for p, n in sorted(by_prop.items(), key=lambda x: -x[1])[:8]:
            print("     %-38s %d" % (str(p)[:38], n))

    print("\n  %-14s %14s %14s %12s %8s %s"
          % ("FIELD", "WAREHOUSE", "RENT MANAGER", "DIFF", "MATCH%", "on the shared keys"))
    for label, wf, rf in fields:
        wsum = rsum = 0.0
        agree = compared = 0
        worst = []
        for k in both:
            a = sum(num(r.get(wf)) for r in wh[k])
            b = sum(num(r.get(rf)) for r in rm[k])
            wsum += a
            rsum += b
            compared += 1
            if abs(a - b) < 0.51:
                agree += 1
            else:
                worst.append((abs(a - b), k, a, b))
        pct = (agree / compared * 100) if compared else 0
        print("  %-14s %14s %14s %12s %7.1f%%"
              % (label, money(wsum), money(rsum), money(wsum - rsum), pct))
        worst.sort(reverse=True)
        for d, k, a, b in worst[:3]:
            print("       biggest gap  %-30s wh %10s   rm %10s"
                  % ((str(k[0])[:22] + " / " + str(k[1]))[:30], money(a), money(b)))
        stats.setdefault("fields", {})[label] = {"wh": wsum, "rm": rsum}

    # totals over EVERY resolved key, not just the shared ones -- the shared-key
    # sum is what made this look like a rounding difference the first time.
    stats["wh_all"] = sum(sum(num(r.get(f)) for r in rows)
                          for f in [fields[0][1]] for rows in wh.values())
    stats["rm_all"] = sum(sum(num(r.get(f)) for r in rows)
                          for f in [fields[0][2]] for rows in rm.values())
    stats["only_rm_value"] = sum(sum(num(r.get(fields[0][2])) for r in rm[k])
                                 for k in only_rm)
    print("\n  on EVERY resolved key, not just the shared ones:")
    print("     warehouse %s    rent manager %s    gap %s"
          % (money(stats["wh_all"]), money(stats["rm_all"]),
             money(stats["wh_all"] - stats["rm_all"])))
    print("     the %d rent-manager-only keys carry %s of that"
          % (stats["only_rm"], money(stats["only_rm_value"])))
    return stats


LEDGER = "data/source_reconciliation.json"

# The as-of date of the warehouse snapshot each candidate pull came from. The
# warehouse does not put it in the rows, and the run_query warning only says
# "restricted to its most recent period", so it is read off the asOfDate
# dimension when the pull is made and recorded here. Update both whenever the
# candidate files are re-pulled -- a stale value here would make a real timing
# drift look like zero.
WH_AR_AS_OF = "2026-09-05"        # VW_Aged_Receivables, latest snapshot
WH_RENTROLL_AS_OF = "2026-08-31"  # VW_Summary_Rent_Roll, latest inside August


def as_of(path):
    """
    The date a raw file actually represents, not the date it was written.

    For the Rent Manager pulls that is the file mtime, since the reports are
    as-of-run. This is the variable the AR question turns on: the two sources
    can be a day apart, and the 5th is the grace day, so a snapshot on either
    side of it sits on the far side of the month's heaviest payment window.
    Recording it means a future run can correlate the gap against the drift
    instead of guessing.
    """
    import datetime
    full = os.path.join(REPO, path)
    if not os.path.exists(full):
        return None
    return datetime.date.fromtimestamp(os.path.getmtime(full)).isoformat()


def log_run(source, wh_total, rm_total, shared, only_wh, only_rm, only_rm_value, note,
            wh_as_of=None, rm_as_of=None):
    """
    Append one dated row per run so the gap can be read as a trend rather than
    a number. Committed to the repo for the same reason the flag ledger is: the
    container is reclaimed between runs, and a single-day reading of a snapshot
    difference tells you nothing about whether it is a timing artefact.

    The whole AR question is whether the gap tracks the billing cycle. Rent
    bills on the 1st and is late after the 5th, so a snapshot taken on the 5th
    sits on the far side of the month's heaviest payment window from one taken
    on the 4th. If that is the cause, the gap collapses when both sources are
    pulled the same day and reopens when they drift apart. One row a day is
    what makes that visible.
    """
    path = os.path.join(REPO, LEDGER)
    rows = []
    if os.path.exists(path):
        rows = json.load(open(path)).get("runs", [])
    today = __import__("datetime").date.today().isoformat()
    row = {
        "date": today, "source": source,
        "warehouse_total": round(wh_total, 2), "rent_manager_total": round(rm_total, 2),
        "gap": round(wh_total - rm_total, 2),
        "shared_keys": shared, "only_warehouse": only_wh, "only_rent_manager": only_rm,
        "only_rent_manager_value": round(only_rm_value, 2),
        # The two as-of dates and the drift between them. A gap that moves with
        # `drift_days` is timing; a gap that holds steady at zero drift is not.
        "warehouse_as_of": wh_as_of,
        "rent_manager_as_of": rm_as_of,
        "drift_days": (
            (__import__("datetime").date.fromisoformat(wh_as_of)
             - __import__("datetime").date.fromisoformat(rm_as_of)).days
            if wh_as_of and rm_as_of else None),
        "note": note,
    }
    # A re-run on the same day replaces that day's row rather than stacking a
    # second one; otherwise a day I happened to check twice reads as a trend.
    rows = [r for r in rows if not (r["date"] == today and r["source"] == source)] + [row]
    rows.sort(key=lambda r: (r["date"], r["source"]))
    json.dump({"runs": rows}, open(path, "w"), indent=1)
    print("\n  logged to %s (%d runs held)" % (LEDGER, len(rows)))
    same = [r for r in rows if r["source"] == source]
    if len(same) > 1:
        print("  %-12s %12s %12s %8s %13s %8s"
              % ("DATE", "WH AS OF", "RM AS OF", "DRIFT", "GAP", "RM-ONLY"))
        for r in same[-10:]:
            print("  %-12s %12s %12s %8s %13s %8d"
                  % (r["date"], r.get("warehouse_as_of") or "?",
                     r.get("rent_manager_as_of") or "?",
                     ("%+d d" % r["drift_days"]) if r.get("drift_days") is not None else "?",
                     money(r["gap"]), r["only_rent_manager"]))
        print("  a gap that tracks DRIFT is timing. a gap that survives zero drift is not.")


def rentroll():
    print("=" * 96)
    print("SUMMARY RENT ROLL  --  VW_Summary_Rent_Roll (unit grain)  vs  RM report 69")
    print("=" * 96)
    wh = load("pipeline/raw/candidate/wh_rentroll_unit.json")
    rm = load("pipeline/raw/rm_rent_roll.json")
    ids = json.load(open(os.path.join(REPO, "pipeline/raw/rm_property_ids.json")))
    id_to_short = ids.get("id_to_short") or {}

    def wh_key(look, r):
        p = resolve(look, r.get("VW_Summary_Rent_Roll.propertyName"))
        u = str(r.get("VW_Summary_Rent_Roll.unitName") or "").strip()
        return (p, u) if p and u else None

    def rm_key(look, r):
        short = id_to_short.get(str(r.get("EntitiesEntityID")))
        p = resolve(look, short, r.get("EntitiesName"), r.get("EntitiesShortName"),
                    r.get("PrimaryLeasePropertyShortName"))
        u = str(r.get("SubEntitiesName") or "").strip()
        return (p, u) if p and u else None

    st = report("rentroll", wh, rm, wh_key, rm_key, [
        ("rent charges", "VW_Summary_Rent_Roll.rentCharges", "RentCharges"),
        ("misc charges", "VW_Summary_Rent_Roll.miscCharges", "MiscCharges"),
        ("total charged", "VW_Summary_Rent_Roll.totalCharged", "TotalCharged"),
        ("total paid", "VW_Summary_Rent_Roll.totalPaid", "TotalPaid"),
    ])
    if "--log" in sys.argv:
        log_run("rentroll", st["wh_all"], st["rm_all"], st["shared"], st["only_wh"],
                st["only_rm"], st["only_rm_value"], "rent charges, the first field",
                wh_as_of=WH_RENTROLL_AS_OF,
                rm_as_of=as_of("pipeline/raw/rm_rent_roll.json"))


def ar():
    print("=" * 96)
    print("AGED RECEIVABLES  --  VW_Aged_Receivables (unit grain)  vs  RM report 78")
    print("=" * 96)
    # The RM report is one row per charge; the warehouse rolls to unit. Compare
    # at unit level, which is the grain the drill-ins actually use, and let the
    # RM side sum its charge rows up to that.
    wh = load("pipeline/raw/candidate/wh_ar_unit.json")
    rm = load("pipeline/raw/rm_ar_detail.json")

    def wh_key(look, r):
        p = resolve(look, r.get("VW_Aged_Receivables.propertyName"))
        u = str(r.get("VW_Aged_Receivables.unitName") or "").strip()
        return (p, u) if p and u else None

    def rm_key(look, r):
        p = resolve(look, r.get("EntitiesShortName"))
        u = str(r.get("SubEntitiesName") or "").strip()
        return (p, u) if p and u else None

    st = report("ar", wh, rm, wh_key, rm_key, [
        ("total AR", "VW_Aged_Receivables.agedReceivablesTotal", "TotalLeft"),
        ("0-30", "VW_Aged_Receivables.current0to30", "LessThan30"),
        ("31-60", "VW_Aged_Receivables.days31to60", "LessThan60"),
        ("61-90", "VW_Aged_Receivables.days61to90", "LessThan90"),
        ("over 90", "VW_Aged_Receivables.over90Days", "GreaterThan90"),
    ])
    if "--log" in sys.argv:
        log_run("ar", st["wh_all"], st["rm_all"], st["shared"], st["only_wh"],
                st["only_rm"], st["only_rm_value"],
                "warehouse snapshot vs the rent manager pull; if the gap is timing "
                "it should collapse when both are pulled the same day",
                wh_as_of=WH_AR_AS_OF, rm_as_of=as_of("pipeline/raw/rm_ar_detail.json"))


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "rentroll"
    {"rentroll": rentroll, "ar": ar}[which]()
