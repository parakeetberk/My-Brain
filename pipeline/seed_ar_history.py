#!/usr/bin/env python3
"""
Seed twenty months of month-end receivables into the history store.

The capture step only accumulates forward, which is why it had to start before
the design finished. Receivables are the exception: VW_Aged_Receivables holds
twenty months of month-end balances by property, and nobody had been reading
them. So AR does not start from zero -- month-over-month and year-over-year on
the balance are available today rather than in a year. Only the intra-month
shape has to be earned a day at a time.

WHAT asOfDate ACTUALLY IS, after getting it wrong twice.

  It is NOT a portfolio snapshot calendar. Reading it that way makes most dates
  look like partial loads -- 1 to 16 customers against a 949-customer
  month-end -- and invites the conclusion that `reportMonth` double-counts.

  It is NOT evidence that `reportMonth` is broken either. Every property
  contributes exactly ONE row per month (1,661 rows, 1,661 distinct
  property-months), so summing a month adds nothing to itself. Filtering to a
  single portfolio-wide date instead DROPS properties: 83 properties have an
  August row, only 69 of them dated the 31st, and taking the 31st alone zeroed
  fourteen communities including Central at $31,070 and Harbour at $12,567.

  It is a PER-PROPERTY observation date. Each property is snapshotted about
  once a month, on its own date. Southgate's August balance was observed on the
  31st; Central's on the 2nd. `reportMonth` is the correct grouping, and this
  script uses it.

WHICH MAKES THE REAL FINDING A FRESHNESS ONE. Comparing Central's August AR to
Southgate's August AR compares observations twenty-nine days apart. So every
row here carries `observed_lag_days` -- how stale the oldest contributing
observation was at month-end -- because a receivables comparison across
communities is only as good as the closer of the two reads.

ATTRIBUTION COMES FROM build.py, NOT FROM A SECOND GUESS. data/registry_audit.json
is the resolution map build.py already emits: name -> disposition + canonical
community, including the utility sub-ledgers that roll up into a parent. Reading
it means this store and the dashboard can never disagree about which community a
dollar belongs to.

    seed_ar_history.py                       report what would be seeded
    seed_ar_history.py --write               append it
    seed_ar_history.py --asof <file.json>    add per-property observation dates
"""
import json
import os
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AR = os.path.join(REPO, "pipeline", "raw", "ar_by_property_month.json")
AUDIT = os.path.join(REPO, "data", "registry_audit.json")
DASH = os.path.join(REPO, "data", "dashboard.json")
FACTS = os.path.join(REPO, "data", "daily_facts.json")
FAMILY = "receivables_month_end"

M = "VW_Aged_Receivables."
BUCKETS = {"ar_total": "agedReceivablesTotal", "ar_0_30": "current0to30",
           "ar_31_60": "days31to60", "ar_61_90": "days61to90",
           "ar_90_plus": "over90Days", "ar_accounts": "customersWithBalance"}


def month_end(mo):
    y, m = int(mo[:4]), int(mo[5:7])
    return (date(y + (m == 12), (m % 12) + 1, 1) - timedelta(days=1)).isoformat()


def observation_dates(path):
    """(property, month) -> the date that property was actually observed."""
    if not path or not os.path.exists(path):
        return {}
    out = {}
    for r in json.load(open(path))["rows"]:
        d = r[M + "asOfDate"][:10]
        out[(r[M + "propertyName"], d[:7])] = d
    return out


def main(write=False, asof_path=None):
    resolve = json.load(open(AUDIT))["names"]
    short = {c["name"]: c for c in json.load(open(DASH))["communities"]}
    obs = observation_dates(asof_path)

    agg = defaultdict(lambda: defaultdict(float))
    lag = defaultdict(list)
    contributors = defaultdict(set)
    unresolved = defaultdict(int)
    for r in json.load(open(AR))["rows"]:
        name = r.get(M + "propertyName")
        mo = str(r.get(M + "reportMonth") or "")[:7]
        if not name or len(mo) != 7:
            continue
        ent = resolve.get(name)
        if not ent:
            unresolved[name] += 1
            continue
        if ent["disposition"] not in ("keep", "roll_up"):
            continue
        canon = ent["canonical"]
        if not canon or canon not in short:
            unresolved[name] += 1
            continue
        cell = agg[(canon, mo)]
        for metric, member in BUCKETS.items():
            v = r.get(M + member)
            if v is not None:
                cell[metric] += v
        contributors[(canon, mo)].add(name)
        seen = obs.get((name, mo))
        if seen:
            lag[(canon, mo)].append((datetime.fromisoformat(month_end(mo))
                                     - datetime.fromisoformat(seen)).days)

    facts = json.load(open(FACTS)) if os.path.exists(FACTS) else \
        {"schema": 1, "families": {}, "rows": []}
    have = {(r["family"], r["as_of"], r["community"]) for r in facts["rows"]}
    live_month = json.load(open(DASH))["period"]["live"]

    rows = []
    for (canon, mo), cell in sorted(agg.items()):
        if mo >= live_month:
            continue            # the open month is not a month-end; the daily
                                # families carry it, and mixing the two would
                                # put a mid-month spike on a month-end line
        as_of = month_end(mo)
        c = short[canon]
        key = (FAMILY, as_of, c["short_name"])
        if key in have:
            continue
        total = cell.get("ar_total") or 0.0
        row = {"family": FAMILY, "as_of": as_of, "day": int(as_of[8:10]),
               "describes": mo, "community": c["short_name"], "park": canon,
               "vehicle": c.get("vehicle"), "kind": c.get("kind"),
               "ledgers": len(contributors[(canon, mo)])}
        for metric in BUCKETS:
            if metric in cell:
                row[metric] = round(cell[metric], 2)
        if total:
            row["ar_over90_share"] = round((cell.get("ar_90_plus") or 0)
                                           / total * 100, 1)
        if lag[(canon, mo)]:
            row["observed_lag_days"] = max(lag[(canon, mo)])
        rows.append(row)
        have.add(key)

    months = sorted({r["describes"] for r in rows})
    print("%d month-end rows across %d communities, %s to %s"
          % (len(rows), len({r["community"] for r in rows}),
             months[0] if months else "-", months[-1] if months else "-"))
    lags = sorted(r["observed_lag_days"] for r in rows
                  if r.get("observed_lag_days") is not None)
    if lags:
        print("observation lag at month-end: median %dd, p90 %dd, worst %dd "
              "(%d of %d rows carry one)"
              % (lags[len(lags) // 2], lags[int(len(lags) * .9)], lags[-1],
                 len(lags), len(rows)))
    if unresolved:
        print("\n%d warehouse property names resolve to nothing reportable "
              "and are counted nowhere:" % len(unresolved))
        for n, k in sorted(unresolved.items(), key=lambda x: -x[1])[:10]:
            print("   %-44s %d months" % (n[:44], k))
    if not write:
        print("\nreport only. Pass --write to append.")
        return
    facts["rows"].extend(rows)
    facts["families"][FAMILY] = {
        "source": "pipeline/raw/ar_by_property_month.json",
        "cube": "VW_Aged_Receivables",
        "as_of": max((r["as_of"] for r in rows), default=None),
        "as_of_basis": "month-end of reportMonth; each property is observed once "
                       "a month on its own date, see observed_lag_days",
        "row_count": len(rows), "captured_on": date.today().isoformat(),
        "note": "month-end grain, seeded once; the daily families carry the "
                "intra-month shape and must not be plotted on the same line",
    }
    json.dump(facts, open(FACTS, "w"), separators=(",", ":"), sort_keys=True)
    print("\n[seed] +%d rows -> data/daily_facts.json (%d total, %.2f MB)"
          % (len(rows), len(facts["rows"]), os.path.getsize(FACTS) / 1e6))


if __name__ == "__main__":
    a = sys.argv[1:]
    ap = a[a.index("--asof") + 1] if "--asof" in a else None
    main(write="--write" in a, asof_path=ap)
