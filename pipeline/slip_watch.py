#!/usr/bin/env python3
"""
Catch projected dates being pushed back, and keep a record of who pushed them.

Cavco and Champion give us projected dates for delivery and setup, and those
projections get revised. A revision that moves a date later is the thing worth
asking about on the Wednesday rehab call: not "is this home late" but "this date
has now moved three times, always later, and nobody said why".

One snapshot cannot show that. The daily asset archive can, because each file is
the projection as it stood that morning. This diffs consecutive snapshots per
asset per date field and appends every movement to data/date_slips.json, so
cumulative drift per home accumulates over time rather than being recomputed
from whatever two files happen to be on disk.

Deliberately not a new notification stream. The output is shaped for the pack
that the Tuesday 5pm rehab pre-read routine already builds, because a second
email nobody asked for is how a good signal gets ignored.

    slip_watch.py scan       diff every consecutive pair in pipeline/incoming
    slip_watch.py report     what to raise on the call
"""
import csv
import glob
import io
import json
import os
import re
import sys
from collections import defaultdict
from datetime import date, datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INCOMING = os.path.join(REPO, "pipeline", "incoming", "asset_listing")
LEDGER = os.path.join(REPO, "data", "date_slips.json")

# The date fields worth watching. Req Delivery is the commitment and moved on
# zero assets in 34 days, so if it ever moves that is the loudest signal here.
WATCH = {
    "UDF: Req Delivery Date": "requested delivery",
    "UDF: Home Delivery Date": "delivery",
    "UDF: Target Home Set Date": "home set",
    "UDF: Order Date": "order",
    "UDF: Online Date": "online",
    "UDF: Permit Submitted Date": "permit submitted",
    "UDF: Permit Received Date": "permit received",
    "UDF: Demo Date": "demo",
    "UDF: Footers / Pads Date": "footers and pads",
    "UDF: Spot Units Date": "spot units",
    "UDF: Set, Side & Tie Down": "set side and tie down",
    "UDF: Interior Trim Out Date": "interior trim out",
    "UDF: Water Connection Date": "water",
    "UDF: Sewer Connection Date'": "sewer",
    "UDF: Electrical Connection Date": "electrical",
    "UDF: AC Connection Date": "AC",
    "UDF: Skirting / Gutter Date": "skirting and gutter",
    "UDF: Steps/Deck Date": "steps and deck",
    "UDF: Punch Out Date": "punch out",
    "UDF: Cert of Occupancy Date": "cert of occupancy",
}

PLACEHOLDER = {"", "TBD", "N/A", "NA", "-", "--", "TBA", "?"}


def parse_date(v):
    """
    The cells are hand-typed, so accept what people actually enter. A 'WE '
    prefix means week-ending and is a real commitment, just a coarse one.
    """
    v = (v or "").strip()
    if v.upper() in PLACEHOLDER:
        return None
    v = re.sub(r"^(WE|We|wk|Week of|week of)\s+", "", v).strip()
    for f in ("%m/%d/%y", "%m/%d/%Y", "%Y-%m-%d", "%m-%d-%y", "%m-%d-%Y"):
        try:
            return datetime.strptime(v, f).date()
        except ValueError:
            pass
    return None


def as_of(path):
    m = re.search(r"_(\d{2})(\d{2})(\d{2})", os.path.basename(path))
    return "20%s-%s-%s" % m.groups() if m else None


def load(path):
    raw = open(path, encoding="utf-8-sig", errors="replace").read()
    rows = list(csv.DictReader(io.StringIO(raw)))
    out = {}
    for r in rows:
        k = (r.get("Asset Name") or "").strip()
        if k:
            out[k] = r
    return out


def snapshots():
    files = sorted(glob.glob(os.path.join(INCOMING, "*.csv")), key=lambda p: as_of(p) or "")
    return [(as_of(p), p) for p in files if as_of(p)]


def scan():
    snaps = snapshots()
    if len(snaps) < 2:
        raise SystemExit("need at least two snapshots in %s" % INCOMING)
    print("[slip] %d snapshots: %s" % (len(snaps), ", ".join(d for d, _ in snaps)))

    events = []
    if os.path.exists(LEDGER):
        events = json.load(open(LEDGER)).get("events", [])
    seen = {(e["asset"], e["field"], e["observed"]) for e in events}

    prev_d, prev_p = snaps[0]
    prev = load(prev_p)
    for cur_d, cur_p in snaps[1:]:
        cur = load(cur_p)
        for k, r in cur.items():
            old = prev.get(k)
            if not old:
                continue
            for field, label in WATCH.items():
                a, b = old.get(field), r.get(field)
                sa, sb = (a or "").strip(), (b or "").strip()
                if sa == sb:
                    continue
                da, db = parse_date(a), parse_date(b)
                # A projection appearing for the first time is not a slip.
                if da is None and db is not None:
                    kind, days = "set", None
                elif da is not None and db is None:
                    kind, days = "cleared", None
                elif da is not None and db is not None:
                    days = (db - da).days
                    kind = "pushed" if days > 0 else ("pulled" if days < 0 else "restated")
                else:
                    kind, days = "text", None
                key = (k, field, cur_d)
                if key in seen:
                    continue
                seen.add(key)
                events.append({
                    "asset": k, "field": field, "label": label,
                    "community": (r.get("Property") or "").strip(),
                    "manufacturer": (r.get("Manufacturer") or "").strip(),
                    "status": (r.get("Current Status") or "").strip(),
                    "from": sa, "to": sb, "kind": kind, "days": days,
                    "observed": cur_d, "prior_snapshot": prev_d,
                })
        prev_d, prev = cur_d, cur

    events.sort(key=lambda e: (e["observed"], e["asset"], e["field"]))
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    json.dump({"events": events, "scanned": date.today().isoformat()},
              open(LEDGER, "w"), indent=1)
    kinds = defaultdict(int)
    for e in events:
        kinds[e["kind"]] += 1
    print("[slip] %d events in the ledger: %s"
          % (len(events), ", ".join("%s %d" % (k, v) for k, v in sorted(kinds.items()))))


def report():
    if not os.path.exists(LEDGER):
        raise SystemExit("run `slip_watch.py scan` first")
    events = json.load(open(LEDGER))["events"]
    pushed = [e for e in events if e["kind"] == "pushed"]

    print("=" * 78)
    print("DATES PUSHED BACK  --  for the rehab call")
    print("=" * 78)
    if not pushed:
        print("\n  Nothing moved later in the window scanned.")
    else:
        print("\n%-24s %-12s %-20s %6s  %s"
              % ("HOME", "STAGE", "MOVED", "DAYS", "STATUS"))
        for e in sorted(pushed, key=lambda e: -(e["days"] or 0)):
            print("%-24s %-12s %-20s %+6d  %s"
                  % (e["asset"][:24], e["label"][:12],
                     "%s -> %s" % (e["from"], e["to"]), e["days"], e["status"][:18]))

    # A home whose dates keep moving is a different conversation from one that
    # slipped once, so count the moves per home rather than only the days.
    per = defaultdict(list)
    for e in pushed:
        per[e["asset"]].append(e)
    repeat = {k: v for k, v in per.items() if len(v) > 1}
    if repeat:
        print("\nREPEAT OFFENDERS -- more than one push")
        for k, v in sorted(repeat.items(), key=lambda x: -sum(e["days"] or 0 for e in x[1])):
            print("   %-24s %d pushes, %+d days total, %s"
                  % (k[:24], len(v), sum(e["days"] or 0 for e in v),
                     ", ".join(sorted({e["label"] for e in v}))))

    by_mfg = defaultdict(list)
    for e in pushed:
        by_mfg[e["manufacturer"] or "(blank)"].append(e["days"] or 0)
    if by_mfg:
        print("\nBY MANUFACTURER")
        for m, d in sorted(by_mfg.items(), key=lambda x: -sum(x[1])):
            print("   %-18s %3d pushes, %+d days total, worst %+d"
                  % (m[:18], len(d), sum(d), max(d)))

    firsts = [e for e in events if e["kind"] == "set"]
    if firsts:
        print("\nFIRST PROJECTIONS RECORDED (not slips, shown so the pack is complete)")
        seen = defaultdict(int)
        for e in firsts:
            seen[e["label"]] += 1
        for lab, n in sorted(seen.items(), key=lambda x: -x[1])[:8]:
            print("   %-24s %d homes" % (lab, n))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "scan"
    {"scan": scan, "report": report}.get(cmd, lambda: (_ for _ in ()).throw(SystemExit(__doc__)))()
