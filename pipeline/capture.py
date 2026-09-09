#!/usr/bin/env python3
"""
Append today's facts to the history store.

Rent Manager keeps no history. The warehouse keeps monthly grain. Neither can
answer "is 60% collections at J Bar J normal for the 3rd of the month", because
nothing anywhere records what the 3rd of the month looked like. This is the step
that starts recording it, and it is the one step where waiting costs something
permanent: every day it does not run is a day of baseline that cannot be
recovered afterwards.

WHAT IT CAPTURES. The LIVE block -- figures through today -- per community, in
six families grouped by the source cube behind them. The closed-month block is
deliberately left out: the warehouse already holds monthly grain and can be
re-derived any time, so storing it here would just be a second copy that can
drift. What has no home anywhere is the intra-month shape.

THE AS-OF PROBLEM, HONESTLY. docs/PLATFORM_SPEC.md rule 1 says every pull
records its own as-of date. It cannot be satisfied from the warehouse as it
stands, and pretending otherwise is how a store like this goes quietly wrong.

Of the eleven models, exactly one -- VW_Aged_Receivables -- carries a dimension
that looks like a snapshot date, `asOfDate`. On inspection it is not one. It is
a per-charge attribute: complete portfolio snapshots appear only at month-end
and at the current live read (1,001 customers on 2026-07-31, 949 on 2026-08-31,
1,328 on 2026-09-05), while every other date in it holds one to sixteen
customers -- individual charges, not a portfolio. Reading it as a snapshot
calendar would have filed a $2,669 portfolio for 2026-07-11.

The other models have no snapshot dimension at all. `reportMonth` and `endDate`
are the period the data DESCRIBES, not when it was captured; they read "2026-09"
all month while the live figures underneath them change daily.

So there is no as-of to read, and this step will not invent one. Two things
stand in, and both are recorded on every row so nothing downstream has to guess
which it got:

  THE STAMPED AS-OF, from data/warehouse_asof.json, written by whoever ran the
  pull. That file is the only thing that can state when the warehouse data was
  actually current. Without it the capture REFUSES to run -- a fact row with a
  guessed date is worse than a missing day, because nothing later can tell it
  from a real one.

  THE CONTENT HASH, a digest of the normalised rows, which decides whether a
  family moved at all. Exact, and unlike a date it catches a restatement inside
  an existing month. An unrefreshed feed appends nothing.

Both together give rule 2: one row per snapshot, never one per run.

AND THE DRIFT IS ITSELF THE ALERT. The stamped as-of minus today is recorded on
every row. As this was written the newest complete AR snapshot was 2026-09-05
and the date was 2026-09-09 -- the receivables feed was four days stale, which
is most of the $513K discrepancy in docs/SOURCE_CONSOLIDATION.md, and it is
visible only because the drift is stored rather than assumed away.

FOOTNOTE WORTH ACTING ON. VW_Aged_Receivables holds COMPLETE month-end
snapshots back to at least 2025-01. That is twenty months of month-end AR
history nobody has been reading, and it means AR is not starting from zero at
month-end grain -- only the intra-month shape is.

    capture.py status                    what each family would do, and why
    capture.py stamp <YYYY-MM-DD>        record when the warehouse data was current
    capture.py run                       append the families that moved
    capture.py run --dry                 same, without writing
"""
import hashlib
import json
import os
import sys
from collections import defaultdict
from datetime import date, datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(REPO, "pipeline", "raw")
DASH = os.path.join(REPO, "data", "dashboard.json")
FACTS = os.path.join(REPO, "data", "daily_facts.json")
ASOF = os.path.join(REPO, "data", "warehouse_asof.json")
SCHEMA = 1
# Drift beyond this many days between the warehouse snapshot and the read is an
# alert, not a footnote. AR is a stock: four days of drift moved it by $513K.
STALE_DAYS = 1

# Each family names the source file it depends on, the cube behind it, the row
# key that carries the family's data date, and the metrics it lifts out of the
# community's `live` block. Grouping by SOURCE rather than by subject is what
# lets a stale AR feed sit out a day without blocking occupancy from recording.
FAMILIES = {
    "receivables": {
        "source": "ar_by_property_month.json",
        "cube": "VW_Aged_Receivables",
        "date_key": "VW_Aged_Receivables.reportMonth",
        "has_real_as_of": True,
        "metrics": ["ar_total", "ar_0_30", "ar_31_60", "ar_61_90", "ar_90_plus",
                    "ar_over90_share", "ar_past_due_30plus", "ar_accounts",
                    "ar_per_unit", "ar_needs_action", "ar_needs_action_amount",
                    "evictions_open", "eviction_balance"],
    },
    "collections": {
        "source": "rentroll_by_property_month.json",
        "cube": "VW_Summary_Rent_Roll",
        "date_key": "VW_Summary_Rent_Roll.reportMonth",
        "metrics": ["charged", "paid", "outstanding", "collection_pct",
                    "actual_rent", "market_rent", "loss_to_lease"],
    },
    "occupancy": {
        "source": "occupancy_by_property_month.json",
        "cube": "VW_Rental_Unit_Listing",
        "date_key": "VW_Rental_Unit_Listing.reportMonth",
        "metrics": ["units", "occupied", "occupancy", "vacancy_loss"],
        "hot_metrics": ["rentable_units", "occupancy_rentable", "vacant",
                        "lots_billing", "occupied_not_billing", "poh_total",
                        "poh_occupied", "lot_rent_avg"],
    },
    "financials": {
        "source": "financials_by_property_month.json",
        "cube": "VW_Budget_Comparison",
        "date_key": "VW_Budget_Comparison.endDate",
        "metrics": ["revenue", "revenue_budget", "opex", "opex_budget",
                    "noi", "noi_budget", "noi_margin",
                    "ytd_revenue", "ytd_revenue_budget", "ytd_noi", "ytd_noi_budget"],
    },
    "turnover": {
        "source": "moves_by_property_month.json",
        "cube": "VW_MoveIns_MoveOuts",
        "date_key": "VW_MoveIns_MoveOuts.month",
        "metrics": ["move_ins", "move_outs"],
    },
}


def load_facts():
    if os.path.exists(FACTS):
        return json.load(open(FACTS))
    return {"schema": SCHEMA, "started": date.today().isoformat(),
            "families": {}, "rows": []}


def payload(name):
    p = os.path.join(RAW, name)
    if not os.path.exists(p):
        return None
    return json.load(open(p))


def fingerprint(rows):
    """A digest of the rows as data, insensitive to key order and row order."""
    h = hashlib.sha256()
    for line in sorted(json.dumps(r, sort_keys=True, separators=(",", ":"))
                       for r in rows):
        h.update(line.encode())
    return h.hexdigest()[:16]


def describes(rows, key):
    """The period the data describes. NOT when it was captured -- see the note."""
    best = None
    for r in rows:
        v = r.get(key)
        if not isinstance(v, str) or len(v) < 7:
            continue
        if best is None or v > best:
            best = v
    return best[:10] if best else None


def warehouse_asof():
    """When the warehouse data was actually current, per whoever pulled it."""
    if not os.path.exists(ASOF):
        return None
    return json.load(open(ASOF))


def stamp(as_of):
    try:
        d = datetime.strptime(as_of, "%Y-%m-%d").date()
    except ValueError:
        raise SystemExit("as-of must be YYYY-MM-DD, got %r" % as_of)
    today = date.today()
    if d > today:
        raise SystemExit("as-of %s is in the future -- a snapshot cannot be "
                         "newer than the day it was read" % as_of)
    drift = (today - d).days
    json.dump({"as_of": as_of, "read_on": today.isoformat(), "drift_days": drift},
              open(ASOF, "w"), indent=1)
    print("[capture] warehouse as-of %s, read %s, drift %d day%s%s"
          % (as_of, today, drift, "" if drift == 1 else "s",
             "   STALE" if drift > STALE_DAYS else ""))


def read_family(fam, spec):
    pl = payload(spec["source"])
    if pl is None:
        return None, "source file missing: %s" % spec["source"]
    rows = pl.get("rows") or []
    if not rows:
        return None, "source file has no rows"
    wh = warehouse_asof()
    stated = pl.get("as_of")            # the file-backed sources carry their own
    if stated:
        as_of, basis = stated, "stamped by the pull"
    elif wh:
        as_of, basis = wh["as_of"], "warehouse as-of, stamped %s" % wh["read_on"]
    else:
        as_of, basis = None, "none -- run `capture.py stamp <date>` first"
    return {
        "as_of": as_of, "as_of_basis": basis,
        "describes": describes(rows, spec["date_key"]),
        "read_on": (wh or {}).get("read_on"),
        "drift_days": (wh or {}).get("drift_days"),
        "hash": fingerprint(rows),
        "row_count": len(rows),
    }, None


def collect(d, fam, spec, read):
    """One fact row per community for this family."""
    out = []
    as_of = read["as_of"]
    day = int(as_of[8:10]) if as_of and len(as_of) >= 10 else None
    for c in d["communities"]:
        row = {"family": fam, "as_of": as_of, "day": day,
               "describes": read.get("describes"),
               "drift_days": read.get("drift_days"),
               "community": c["short_name"], "park": c["name"],
               "vehicle": c.get("vehicle"), "kind": c.get("kind")}
        live = c.get("live") or {}
        for m in spec["metrics"]:
            if m in live:
                row[m] = live[m]
        hot = c.get("hot") or {}
        for m in spec.get("hot_metrics", []):
            if m in hot:
                row[m] = hot[m]
        out.append(row)
    return out


def plan():
    if not os.path.exists(DASH):
        raise SystemExit("no data/dashboard.json -- run build.py first")
    d = json.load(open(DASH))
    facts = load_facts()
    rows_by_fam = defaultdict(list)
    report = []
    for fam, spec in FAMILIES.items():
        read, err = read_family(fam, spec)
        if err:
            report.append((fam, "SKIP", err, None))
            continue
        prev = facts["families"].get(fam) or {}
        if prev.get("hash") == read["hash"]:
            report.append((fam, "unchanged", "source has not moved since %s"
                           % prev.get("captured_on", "?"), read))
            continue
        if not read["as_of"]:
            report.append((fam, "REFUSE", "no as-of -- run `capture.py stamp "
                           "<YYYY-MM-DD>` with the date the warehouse data was "
                           "current", read))
            continue
        rows_by_fam[fam] = collect(d, fam, spec, read)
        note = "new" if not prev else "moved from %s" % prev.get("as_of")
        report.append((fam, "capture", note, read))
    return d, facts, rows_by_fam, report


def status():
    _, facts, rows_by_fam, report = plan()
    print("%-13s %-10s %-12s %-9s %s" % ("family", "action", "as of", "rows", "why"))
    for fam, action, why, read in report:
        print("%-13s %-10s %-12s %-9s %s"
              % (fam, action, (read or {}).get("as_of") or "—",
                 len(rows_by_fam.get(fam, [])) or "—", why))
    for fam, _, _, read in report:
        if read:
            print("  %-11s as-of basis: %s   describes through %s"
                  % (fam, read["as_of_basis"], read.get("describes") or "?"))
    wh = warehouse_asof()
    if wh and wh["drift_days"] > STALE_DAYS:
        print("\n  STALE: the warehouse snapshot is %d days behind the read "
              "(%s vs %s). AR is a stock, so drift moves it -- treat these "
              "receivables figures as of %s, not today."
              % (wh["drift_days"], wh["as_of"], wh["read_on"], wh["as_of"]))
    print("\nstore holds %d rows across %d families"
          % (len(facts["rows"]), len(facts["families"])))


def run(dry=False):
    d, facts, rows_by_fam, report = plan()
    status()
    if not rows_by_fam:
        print("\nnothing moved. No rows appended, which is the correct outcome "
              "for an unrefreshed source.")
        return
    # Belt and braces: never append a row for a (family, as_of, community) the
    # store already holds. The hash check above should make this unreachable,
    # but a re-pull that returns identical data under a NEW as-of would slip
    # past it, and a duplicated key would corrupt every baseline built on it.
    have = {(r["family"], r["as_of"], r["community"]) for r in facts["rows"]}
    added = 0
    for fam, rows in rows_by_fam.items():
        fresh = [r for r in rows
                 if (r["family"], r["as_of"], r["community"]) not in have]
        skipped = len(rows) - len(fresh)
        if skipped:
            print("[capture] %s: %d rows already on file for that as-of, skipped"
                  % (fam, skipped))
        if dry:
            continue
        facts["rows"].extend(fresh)
        added += len(fresh)
        read, _ = read_family(fam, FAMILIES[fam])
        facts["families"][fam] = {
            "source": FAMILIES[fam]["source"], "cube": FAMILIES[fam]["cube"],
            "as_of": read["as_of"], "as_of_basis": read["as_of_basis"],
            "hash": read["hash"], "row_count": read["row_count"],
            "captured_on": date.today().isoformat(),
        }
    if dry:
        print("\n--dry: nothing written")
        return
    facts["schema"] = SCHEMA
    facts["generated_at"] = datetime.now().isoformat(timespec="seconds")
    os.makedirs(os.path.dirname(FACTS), exist_ok=True)
    json.dump(facts, open(FACTS, "w"), separators=(",", ":"), sort_keys=True)
    print("\n[capture] +%d rows -> data/daily_facts.json (%d total, %.2f MB)"
          % (added, len(facts["rows"]), os.path.getsize(FACTS) / 1e6))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "status":
        status()
    elif cmd == "stamp":
        if len(sys.argv) < 3:
            raise SystemExit("capture.py stamp <YYYY-MM-DD>")
        stamp(sys.argv[2])
    elif cmd == "run":
        run(dry="--dry" in sys.argv)
    else:
        raise SystemExit(__doc__)
