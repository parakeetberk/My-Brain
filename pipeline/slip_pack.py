#!/usr/bin/env python3
"""
Render the pushed-date ledger as a section for the Tuesday 5pm rehab pre-read.

Deliberately not a new notification stream. The Tuesday routine
(trig_01MDcyYXyogo9xgQqWAxkTNq) already builds a pack for the Wednesday 10:00
call; this writes one more section for it to paste in. A second email nobody
asked for is how a good signal gets ignored.

Austin's framing: catch the pushes, flag them, so the question gets asked on the
call rather than discovered afterwards. So the output is questions to ask, not a
chart to admire, and it is deliberately short -- the pack is one page and this is
one item on it.

Three things this does that a straight dump of the ledger does not.

BULK MOVES COLLAPSE. Ten Lucky Clover homes re-dated from February and April to
2026-08-24 in a single day is one decision, not ten delays. Printing it as ten
lines invites ten explanations of a thing that needs one. Any group of three or
more homes landing on the same date on the same day prints as one line.

THE OBSERVATION GAP IS NAMED. A push is dated when we SAW it, not when it
happened. The archive has a month-wide hole between 2026-08-03 and 2026-09-03,
so a move "observed 9/3" could have been keyed any day in that window. Saying
"20 pushes this week" off that ledger would be flatly wrong, so the header
states the real window and flags any gap over three days.

NO VENDOR LEAGUE TABLE. `UDF: Req Delivery Date` is written only by the Cavco
import, so every requested-delivery slip is Cavco by construction and comparing
manufacturers on it measures the import, not the vendor. See MANUFACTURER_NOTE.

    slip_pack.py            write data/pre_read_slips.md and print it
    slip_pack.py --stdout   print only
"""
import json
import os
import sys
from collections import defaultdict
from datetime import date, datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(REPO, "data", "date_slips.json")
OUT = os.path.join(REPO, "data", "pre_read_slips.md")

# Three or more homes landing on one date in one observation is a decision, not
# a coincidence. Two could be either, so two still print individually.
BULK_MIN = 3
# A gap wider than this between snapshots means "observed on" is not "happened
# on", and the pack has to say so rather than imply a date it cannot support.
GAP_DAYS = 3

MANUFACTURER_NOTE = (
    "Do not read this as a vendor scorecard. `Req Delivery Date` is populated "
    "only by the Cavco import, so requested-delivery slips are Cavco by "
    "construction, not because Cavco slips more."
)


def _d(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def load():
    if not os.path.exists(LEDGER):
        raise SystemExit("no ledger at %s -- run `slip_watch.py scan` first" % LEDGER)
    return json.load(open(LEDGER))


def windows(events):
    """Every (prior -> observed) pair the ledger covers, and how wide each is."""
    pairs = sorted({(e.get("prior_snapshot"), e["observed"]) for e in events})
    out = []
    for a, b in pairs:
        da, db = _d(a), _d(b)
        out.append((a, b, (db - da).days if da and db else None))
    return out


def group(pushed):
    """
    Collapse a same-date, same-day bulk move into one row. Returns a list of
    (rows, shared_to_date_or_None) so the writer can phrase each differently.
    """
    buckets = defaultdict(list)
    for e in pushed:
        buckets[(e["observed"], e["to"], e["label"])].append(e)
    singles, bulk = [], []
    for (_obs, to, _lab), rows in buckets.items():
        (bulk if len(rows) >= BULK_MIN else singles).append((rows, to))
    bulk.sort(key=lambda x: -len(x[0]))
    singles.sort(key=lambda x: -(x[0][0].get("days") or 0))
    return bulk, singles


def render(data):
    events = data.get("events", [])
    pushed = [e for e in events if e["kind"] == "pushed"]
    L = []
    w = L.append

    w("## Dates that moved later")
    w("")

    if not events:
        w("Ledger is empty. Nothing to raise.")
        return "\n".join(L)

    wins = windows(events)
    first = min(a for a, _b, _g in wins if a)
    last = max(b for _a, b, _g in wins if b)
    wide = [(a, b, g) for a, b, g in wins if g and g > GAP_DAYS]

    if not pushed:
        w("No projected date moved later in the window scanned "
          "(%s to %s). Nothing to raise on this item." % (first, last))
        w("")
        w("_Ledger is append-only, so this reads \"nothing moved\", "
          "not \"nothing was checked\"._")
        return "\n".join(L)

    total = sum(e.get("days") or 0 for e in pushed)
    homes = len({e["asset"] for e in pushed})
    w("**%d pushes across %d homes, %+d days in total**, seen between %s and %s."
      % (len(pushed), homes, total, first, last))
    w("")

    if wide:
        w("> **The dates are when we noticed, not when it happened.** " +
          "; ".join("%s to %s is a %d-day gap" % (a, b, g) for a, b, g in wide) +
          ". Anything observed on the later date could have been keyed any day "
          "inside that window, so treat these as \"has moved\", not \"moved on\".")
        w("")

    bulk, singles = group(pushed)

    if bulk:
        w("### Moved as a block — one question each, not one per home")
        w("")
        for rows, to in bulk:
            days = [r.get("days") or 0 for r in rows]
            comms = sorted({r["community"] for r in rows if r["community"]})
            w("- **%d homes** re-dated to **%s** (%s) on %s, %+d to %+d days each. %s"
              % (len(rows), to, rows[0]["label"], rows[0]["observed"],
                 min(days), max(days),
                 ", ".join(comms) if comms else "community not set"))
            w("  <br>_Ask: one re-order or a correction? If it is a correction, "
              "the old dates were wrong and the slip is not real._")
        w("")

    if singles:
        w("### Moved on their own")
        w("")
        w("| Home | Community | Stage | From | To | Days |")
        w("|---|---|---|---|---|---:|")
        for rows, _to in singles:
            for e in rows:
                w("| %s | %s | %s | %s | %s | %+d |"
                  % (e["asset"], e["community"] or "_not set_", e["label"],
                     e["from"], e["to"], e.get("days") or 0))
        w("")

    per = defaultdict(list)
    for e in pushed:
        per[e["asset"]].append(e)
    repeat = {k: v for k, v in per.items() if len(v) > 1}
    if repeat:
        w("### Pushed more than once")
        w("")
        w("A home that has moved three times is a different conversation from "
          "one that moved once by the same total.")
        w("")
        for k, v in sorted(repeat.items(),
                           key=lambda x: -sum(e.get("days") or 0 for e in x[1])):
            w("- **%s** — %d pushes, %+d days total (%s)"
              % (k, len(v), sum(e.get("days") or 0 for e in v),
                 ", ".join(sorted({e["label"] for e in v}))))
        w("")

    w("_%s_" % MANUFACTURER_NOTE)
    w("")
    w("_Source: %d movements in `data/date_slips.json`, scanned %s. "
      "Only later moves appear here; first-time projections, pulled-forward "
      "dates and edited placeholders are logged but are not slips._"
      % (len(events), data.get("scanned", "unknown")))
    return "\n".join(L)


if __name__ == "__main__":
    md = render(load())
    if "--stdout" not in sys.argv:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        open(OUT, "w").write(md + "\n")
        print("[slip-pack] -> %s" % os.path.relpath(OUT, REPO), file=sys.stderr)
    print(md)
