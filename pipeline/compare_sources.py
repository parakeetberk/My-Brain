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

    report("rentroll", wh, rm, wh_key, rm_key, [
        ("rent charges", "VW_Summary_Rent_Roll.rentCharges", "RentCharges"),
        ("misc charges", "VW_Summary_Rent_Roll.miscCharges", "MiscCharges"),
        ("total charged", "VW_Summary_Rent_Roll.totalCharged", "TotalCharged"),
        ("total paid", "VW_Summary_Rent_Roll.totalPaid", "TotalPaid"),
    ])


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

    report("ar", wh, rm, wh_key, rm_key, [
        ("total AR", "VW_Aged_Receivables.agedReceivablesTotal", "TotalLeft"),
        ("0-30", "VW_Aged_Receivables.current0to30", "LessThan30"),
        ("31-60", "VW_Aged_Receivables.days31to60", "LessThan60"),
        ("61-90", "VW_Aged_Receivables.days61to90", "LessThan90"),
        ("over 90", "VW_Aged_Receivables.over90Days", "GreaterThan90"),
    ])


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "rentroll"
    {"rentroll": rentroll, "ar": ar}[which]()
