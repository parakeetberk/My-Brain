#!/usr/bin/env python3
"""
stage_eviction.py -- turn the Eviction Tracker CSV into a staged, de-identified
JSON source for build.py.

    python3 pipeline/stage_eviction.py <csv-or-mcp-json> [--out pipeline/raw/eviction_tracker.json]

The tracker is a scripted Rent Manager report that lands daily at

    ParakeetBirdcage / Data  Analytics / Rent Manager / Eviction Tracker.csv

with a dated copy archived into `Historical Eviction Tracker/`. Read the
undated file: it is the stable path, and the archive folder runs a day or two
behind, which is what made an earlier look conclude the job had stopped.

Two columns never make it past this script:

  FullName    the resident's name. The standalone build gets emailed around,
              and community plus unit plus a name is a resident's whole
              identity. `Name` is the unit number, not a person, and is kept
              because it is the join key to the receivable.

  CaseNumber  a public court filing, but printed next to a community and unit
              it re-identifies the resident to anyone holding the file. The
              dashboard only ever needs whether a case exists, so that is all
              that survives, as `has_case`.

Accepts either a raw CSV or the JSON envelope the SharePoint resource reader
returns, so a refresh can pipe the MCP output straight in.
"""
import argparse
import csv
import io
import json
import os
import sys
from datetime import date

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DROP = ("FullName", "CaseNumber")


def csv_text(path):
    """Pull the CSV out of either a plain file or an MCP resource envelope."""
    raw = open(path, encoding="utf-8").read()
    i = raw.find('{"contents"')
    if i == -1:
        return raw
    obj = json.loads(raw[i:])
    return obj["contents"][0]["text"]


def iso(us):
    """M/D/YYYY -> YYYY-MM-DD. Blank stays blank."""
    us = (us or "").strip()
    if not us:
        return ""
    try:
        m, d, y = [int(x) for x in us.split("/")]
        return "%04d-%02d-%02d" % (y, m, d)
    except ValueError:
        return ""


def money(s):
    s = (s or "").replace(",", "").replace("$", "").strip()
    try:
        return round(float(s), 2)
    except ValueError:
        return 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--out", default=os.path.join(HERE, "pipeline", "raw", "eviction_tracker.json"))
    ap.add_argument("--as-of", default=None,
                    help="date the export was produced (default: today)")
    args = ap.parse_args()

    rows = list(csv.DictReader(io.StringIO(csv_text(args.src))))
    if not rows:
        print("[stage] ERROR: no rows parsed from " + args.src, file=sys.stderr)
        sys.exit(1)
    missing = [c for c in ("Community", "ShortName", "Name", "CurrentStage") if c not in rows[0]]
    if missing:
        print("[stage] ERROR: tracker is missing %s" % ", ".join(missing), file=sys.stderr)
        sys.exit(1)

    out = []
    for r in rows:
        out.append({
            "community": (r.get("Community") or "").strip(),
            "short_name": (r.get("ShortName") or "").strip().upper(),
            "unit": (r.get("Name") or "").strip(),
            "stage": (r.get("CurrentStage") or "").strip(),
            "start": iso(r.get("StartDate")),
            "closed": iso(r.get("CloseDate")),
            "stage_since": iso(r.get("LastStageChangeDate")),
            "sent_to_attorney": iso(r.get("DateSentToAttorney")),
            "open_charges": money(r.get("OpenChargesAmount")),
            "has_case": bool((r.get("CaseNumber") or "").strip()),
        })

    payload = {
        "source": "Eviction Tracker.csv (Rent Manager scripted report)",
        "as_of": args.as_of or date.today().isoformat(),
        "case_count": len(out),
        "open_cases": sum(1 for x in out if not x["closed"]),
        "dropped_columns": list(DROP),
        "cases": out,
    }

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=1)

    # Scan the case rows, not the whole payload -- `dropped_columns` names the
    # very strings being looked for, and checking the manifest against itself
    # fails every clean run.
    blob = json.dumps(payload["cases"])
    for col in DROP:
        if col in blob:
            print("[stage] ERROR: %s survived into the staged file" % col, file=sys.stderr)
            sys.exit(1)
    print("[stage] wrote %s -- %d cases, %d open, as of %s"
          % (args.out, payload["case_count"], payload["open_cases"], payload["as_of"]))


if __name__ == "__main__":
    main()
