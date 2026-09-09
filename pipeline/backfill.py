#!/usr/bin/env python3
"""
Fold the SharePoint asset archive into a fact store, one snapshot at a time.

387 dated files sit in SharePoint. Reading all of them is ~800 large tool calls
for value that flattens out fast, so the target is a stratified set: every file
for the last 60 days, where day-of-month resolution is what makes the baselines
work, plus month-end going back a year, where comparing Augusts needs nothing
finer. About 72 files for roughly nine tenths of the analytical value.

Three rules that keep a long run from leaving a mess:

  DELETE AS WE GO. Each CSV is normalised into the store and then removed, so
  the footprint stays flat however far the run gets and a partial run leaves
  nothing behind.

  STATE ON DISK. `_state.json` records every snapshot already folded in, so the
  run resumes rather than restarting, and re-reading a file is a no-op.

  NOTHING IN data/ UNTIL THE END. The ledgers are written once from what
  accumulated, not appended 387 times, so a crash mid-run leaves the committed
  ledgers exactly as they were.

    backfill.py plan                  which snapshots are wanted, and what is missing
    backfill.py fold <csv> [...]      normalise, record, delete
    backfill.py finish                write the fact store, the slip ledger, the archive
"""
import csv
import glob
import gzip
import io
import json
import os
import re
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INCOMING = os.path.join(REPO, "pipeline", "incoming", "asset_listing")
STATE = os.path.join(INCOMING, "_state.json")
FACTS = os.path.join(REPO, "data", "asset_facts.json")
# The folded snapshot store, committed. `pipeline/incoming/` is gitignored and
# this container is ephemeral, so without this the 56 reads it took to build the
# store would have to happen again in the next session. Gzipped it is about a
# megabyte; raw it is eighteen.
ARCHIVE = os.path.join(REPO, "data", "asset_snapshots.json.gz")
SLIPS = os.path.join(REPO, "data", "date_slips.json")

TODAY = date(2026, 9, 9)
DENSE_DAYS = 60          # every snapshot inside this window
SPARSE_MONTHS = 12       # month-end only, before it

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

# A one-day nudge on a projected date is not a slip, it is a weekly re-baseline.
# 40 of the first 93 pushes this archive produced were single-day moves on Online
# Date, all recorded on one day. Surfacing those buries the four-week push that
# actually costs an occupancy month, so a push has to clear MATERIAL_DAYS before
# it counts as something to raise.
MATERIAL_DAYS = 3

# When several assets at one community move the SAME field to the SAME new value
# on the SAME day, that is one edit someone made, not N schedule slips. Ten Lucky
# Clover homes went from February and April order dates to 8/24/2026 in a single
# snapshot: a records correction, and one question on the call, not ten.
BULK_MIN = 3

# How far back the call pack reaches.
CALL_PACK_DAYS = 14


def load_state():
    if os.path.exists(STATE):
        return json.load(open(STATE))
    if os.path.exists(ARCHIVE):
        with gzip.open(ARCHIVE, "rt", encoding="utf-8") as fh:
            st = json.load(fh)
        print("[backfill] restored %d snapshots from %s"
              % (len(st.get("snapshots", {})), os.path.basename(ARCHIVE)))
        return st
    return {"snapshots": {}, "started": TODAY.isoformat()}


def save_archive(st):
    os.makedirs(os.path.dirname(ARCHIVE), exist_ok=True)
    with gzip.open(ARCHIVE, "wt", encoding="utf-8") as fh:
        json.dump(st, fh, separators=(",", ":"), sort_keys=True)
    print("[backfill] snapshot store -> %s (%.1f MB)"
          % (os.path.basename(ARCHIVE), os.path.getsize(ARCHIVE) / 1e6))


def save_state(st):
    os.makedirs(INCOMING, exist_ok=True)
    json.dump(st, open(STATE, "w"), indent=1)


def as_of(path):
    m = re.search(r"_(\d{2})(\d{2})(\d{2})", os.path.basename(path))
    if not m:
        return None
    try:
        return "20%s-%s-%s" % m.groups()
    except Exception:
        return None


def wanted():
    """The stratified target set, as ISO dates."""
    out = set()
    for i in range(DENSE_DAYS + 1):
        out.add((TODAY - timedelta(days=i)).isoformat())
    d = TODAY.replace(day=1)
    for _ in range(SPARSE_MONTHS):
        last = d - timedelta(days=1)          # month-end of the prior month
        out.add(last.isoformat())
        d = last.replace(day=1)
    return out


def parse_date(v):
    v = (v or "").strip()
    if v.upper() in PLACEHOLDER:
        return None
    v = re.sub(r"^(WE|We|wk|Week of|week of)\s+", "", v).strip()
    for f in ("%m/%d/%y", "%m/%d/%Y", "%Y-%m-%d", "%m-%d-%y", "%m-%d-%Y"):
        try:
            return datetime.strptime(v, f).date().isoformat()
        except ValueError:
            pass
    return None


def plan():
    st = load_state()
    have = set(st["snapshots"])
    want = wanted()
    print("target: %d snapshots (%d dense days + %d month-ends)"
          % (len(want), DENSE_DAYS + 1, SPARSE_MONTHS))
    print("folded in already: %d" % len(have))
    missing = sorted(want - have, reverse=True)
    print("still wanted: %d" % len(missing))
    print("\nnext 20, newest first:")
    for d in missing[:20]:
        print("   %s  ->  Asset Listing_%s.csv" % (d, d[2:].replace("-", "")))
    stray = sorted(glob.glob(os.path.join(INCOMING, "*.csv")))
    if stray:
        print("\n%d CSV(s) staged and not yet folded: %s"
              % (len(stray), ", ".join(os.path.basename(s) for s in stray)))


def fold(paths):
    """Normalise each snapshot into the state file, then delete the CSV."""
    st = load_state()
    for p in paths:
        d = as_of(p)
        if not d:
            print("[backfill] SKIP %s: no date in the filename" % os.path.basename(p),
                  file=sys.stderr)
            continue
        raw = open(p, encoding="utf-8-sig", errors="replace").read()
        rows = list(csv.DictReader(io.StringIO(raw)))
        if not rows:
            print("[backfill] SKIP %s: empty" % os.path.basename(p), file=sys.stderr)
            continue

        # SHAPE GUARD. Some files in this folder are a DIFFERENT REPORT wearing
        # the same name. Asset Listing_260831.csv is a 23-column, 122-row POH
        # for-sale listing keyed "Community","ShortName" with `CurrentStatus`
        # rather than `Current Status`, and no UDF stage columns at all.
        #
        # A header-driven reader will not mis-map its columns, but folding it in
        # as a snapshot would read as 1,600 assets vanishing that day and
        # returning the next -- a fabricated mass transition, which is exactly
        # the failure the whole capture design is built to avoid. So a file that
        # does not look like the asset listing is refused, loudly, rather than
        # normalised into something plausible.
        cols = set(rows[0])
        need = {"Asset Name", "Current Status", "Property", "Unit"}
        missing = need - cols
        if missing or len(rows) < 800:
            print("[backfill] REFUSED %s: %d rows, %d columns%s -- this is not the "
                  "asset listing, it is another report with the same filename"
                  % (os.path.basename(p), len(rows), len(cols),
                     "; missing " + ", ".join(sorted(missing)) if missing else ""),
                  file=sys.stderr)
            st.setdefault("refused", {})[d] = {
                "file": os.path.basename(p), "rows": len(rows),
                "columns": len(cols), "missing": sorted(missing),
            }
            save_state(st)
            os.remove(p)
            continue
        # Header-driven, never positional: the archive changes column layout
        # across dates and a positional read would file the wrong values.
        snap = {}
        for r in rows:
            k = (r.get("Asset Name") or "").strip()
            if not k:
                continue
            rec = {
                "community": (r.get("Property") or "").strip(),
                "unit": (r.get("Unit") or "").strip(),
                "status": (r.get("Current Status") or "").strip(),
                "type": (r.get("Asset Type") or "").strip(),
                "mfg": (r.get("Manufacturer") or "").strip(),
            }
            for field in WATCH:
                v = (r.get(field) or "").strip()
                if v:
                    rec[field] = v
            snap[k] = rec
        st["snapshots"][d] = {"assets": snap, "row_count": len(snap),
                              "columns": len(rows[0]),
                              "source_file": os.path.basename(p)}
        save_state(st)
        os.remove(p)
        print("[backfill] folded %s: %d assets, %d columns, CSV removed"
              % (d, len(snap), len(rows[0])))
    print("[backfill] state holds %d snapshots" % len(st["snapshots"]))


def finish():
    """Write the fact store and the slip ledger from everything folded in."""
    st = load_state()
    dates = sorted(st["snapshots"])
    if len(dates) < 2:
        raise SystemExit("need at least two snapshots to derive anything")
    print("[backfill] deriving from %d snapshots, %s to %s"
          % (len(dates), dates[0], dates[-1]))

    slips, transitions = [], []
    for a, b in zip(dates, dates[1:]):
        A = st["snapshots"][a]["assets"]
        B = st["snapshots"][b]["assets"]
        for k, rb in B.items():
            ra = A.get(k)
            if not ra:
                continue
            if ra.get("status") != rb.get("status"):
                transitions.append({
                    "asset": k, "community": rb.get("community"),
                    "manufacturer": rb.get("mfg"),
                    "from": ra.get("status"), "to": rb.get("status"),
                    "observed": b, "prior": a,
                })
            for field, label in WATCH.items():
                x, y = (ra.get(field) or "").strip(), (rb.get(field) or "").strip()
                if x == y:
                    continue
                dx, dy = parse_date(x), parse_date(y)
                if dx and dy:
                    days = (datetime.fromisoformat(dy) - datetime.fromisoformat(dx)).days
                    kind = "pushed" if days > 0 else ("pulled" if days < 0 else "restated")
                elif dy and not dx:
                    kind, days = "set", None
                elif dx and not dy:
                    kind, days = "cleared", None
                else:
                    kind, days = "text", None
                slips.append({
                    "asset": k, "field": field, "label": label,
                    "community": rb.get("community"), "manufacturer": rb.get("mfg"),
                    "status": rb.get("status"), "from": x, "to": y,
                    "kind": kind, "days": days, "observed": b, "prior_snapshot": a,
                })

    # Materiality, basis, and bulk-edit collapse. All three exist so the call
    # pack carries things worth asking about rather than everything that moved.
    #
    # BASIS is the one that changes what a row means. Rent Manager has no
    # separate actual-date fields yet -- that is the FastField and Quickbase
    # build -- so the same column carries a projection until someone overwrites
    # it with what happened. The date itself says which: a new value in the
    # FUTURE of the day it appeared is a revised projection, and worth a "why".
    # A new value already in the PAST is the team recording an actual, and the
    # number worth reading is not the move, it is the LAG -- how many days after
    # the fact it got typed in. Read as slips they look identical; they are
    # opposite findings.
    for s in slips:
        s["material"] = bool(s["kind"] == "pushed" and (s["days"] or 0) >= MATERIAL_DAYS)
        s["basis"] = None
        s["entry_lag"] = None
        dy = parse_date(s["to"])
        if dy:
            lag = (datetime.fromisoformat(s["observed"])
                   - datetime.fromisoformat(dy)).days
            s["basis"] = "projection" if lag < 0 else "actual"
            if lag >= 0:
                s["entry_lag"] = lag

    groups = defaultdict(list)
    for s in slips:
        if s["kind"] in ("pushed", "pulled"):
            groups[(s["observed"], s["community"], s["field"], s["to"])].append(s)
    bulk = []
    for (obs, comm, field, to), members in sorted(groups.items()):
        if len(members) < BULK_MIN:
            continue
        gid = "%s|%s|%s|%s" % (obs, comm, field, to)
        for m in members:
            m["bulk_group"] = gid
        days = [m["days"] for m in members if m["days"] is not None]
        bulk.append({
            "id": gid, "observed": obs, "community": comm,
            "field": field, "label": members[0]["label"], "to": to,
            "assets": sorted(m["asset"] for m in members),
            "count": len(members),
            "median_days": sorted(days)[len(days) // 2] if days else None,
            "direction": "pushed" if (days and days[0] > 0) else "pulled",
            "basis": members[0]["basis"],
            "entry_lag": members[0]["entry_lag"],
        })

    cutoff = (TODAY - timedelta(days=CALL_PACK_DAYS)).isoformat()
    recent = [s for s in slips
              if s["material"] and not s.get("bulk_group") and s["observed"] >= cutoff]
    pack = sorted((s for s in recent if s["basis"] == "projection"),
                  key=lambda s: -(s["days"] or 0))
    late = sorted((s for s in recent if s["basis"] == "actual"),
                  key=lambda s: -(s["entry_lag"] or 0))
    pack_bulk = [b for b in bulk if b["observed"] >= cutoff]

    os.makedirs(os.path.dirname(FACTS), exist_ok=True)
    json.dump({"generated": TODAY.isoformat(), "snapshots": dates,
               "snapshot_count": len(dates),
               "asset_counts": {d: st["snapshots"][d]["row_count"] for d in dates},
               "transitions": transitions},
              open(FACTS, "w"), indent=1)
    json.dump({"events": slips, "scanned": TODAY.isoformat(),
               "from_snapshots": len(dates),
               "material_days": MATERIAL_DAYS, "bulk_min": BULK_MIN,
               "bulk_edits": bulk,
               "call_pack": {"since": cutoff, "pushes": pack,
                             "late_entry": late, "bulk_edits": pack_bulk}},
              open(SLIPS, "w"), indent=1)

    pushed = [s for s in slips if s["kind"] == "pushed"]
    mat = [s for s in pushed if s["material"] and not s.get("bulk_group")]
    print("[backfill] %d status transitions -> data/asset_facts.json" % len(transitions))
    print("[backfill] %d date movements (%d pushed; %d material and not a bulk edit; "
          "%d bulk edits) -> data/date_slips.json"
          % (len(slips), len(pushed), len(mat), len(bulk)))
    save_archive(st)

    lags = sorted(s["entry_lag"] for s in slips if s["entry_lag"] is not None)
    print("[backfill] call pack since %s: %d revised projections, "
          "%d actuals entered late, %d bulk edits"
          % (cutoff, len(pack), len(late), len(pack_bulk)))
    if lags:
        print("[backfill] entry lag across the archive: median %dd, p90 %dd, worst %dd"
              % (lags[len(lags) // 2], lags[int(len(lags) * 0.9)], lags[-1]))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "plan"
    if cmd == "plan":
        plan()
    elif cmd == "fold":
        fold(sys.argv[2:] or sorted(glob.glob(os.path.join(INCOMING, "*.csv"))))
    elif cmd == "finish":
        finish()
    else:
        raise SystemExit(__doc__)
