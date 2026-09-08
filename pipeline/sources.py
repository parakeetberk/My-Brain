#!/usr/bin/env python3
"""
Resolve each dataset from whichever provider is available, and normalise it.

The point is that not every connector is live yet, and the live ones can be
stale without saying so. So a dataset is defined by its canonical fields, not by
where it came from, and pipeline/sources.json lists providers in priority order.
This walks them, takes the first that yields rows, maps the provider's column
names onto the canonical ones, and records which provider served it.

Turning a connector on is an `enabled` flag in sources.json. No code changes,
and nothing downstream knows the difference -- which is the whole requirement.

Neither path reads SharePoint from here; the container has no credentials. The
routine fetches through the MCP connector and writes into
pipeline/incoming/<dataset>/, and a human refreshing by hand drops the same file
in the same place. Identical downstream, so the fallback cannot drift.

    sources.py status              what each dataset would resolve to
    sources.py build [dataset...]  normalise and write pipeline/raw/<out>
"""
import csv
import glob
import io
import json
import os
import re
import sys
from datetime import date, datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = os.path.join(REPO, "pipeline", "sources.json")
INCOMING = os.path.join(REPO, "pipeline", "incoming")
MANIFEST = os.path.join(REPO, "data", "source_manifest.json")


def load_cfg():
    return json.load(open(CFG))["datasets"]


def resolve_map(prov, dataset):
    """A provider can inherit another's field map rather than repeat it."""
    m = prov.get("map")
    if isinstance(m, str) and m.startswith("same_as:"):
        want = m.split(":", 1)[1]
        for p in dataset["providers"]:
            if p["name"] == want:
                return p["map"]
        raise SystemExit("%s: map inherits from unknown provider %r"
                         % (prov["name"], want))
    return m or {}


DATE_IN_NAME = [
    # Asset Listing_260906.csv  ->  2026-09-06
    (re.compile(r"_(\d{2})(\d{2})(\d{2})\D*$"), lambda m: "20%s-%s-%s" % m.groups()),
    # anything_2026-09-06.csv
    (re.compile(r"(\d{4})-(\d{2})-(\d{2})"), lambda m: "%s-%s-%s" % m.groups()),
    # DW_..._20260528123045297.csv
    (re.compile(r"_(\d{4})(\d{2})(\d{2})\d*\.csv$"), lambda m: "%s-%s-%s" % m.groups()),
]


def as_of_from_name(fname):
    base = os.path.basename(fname)
    for rx, fmt in DATE_IN_NAME:
        m = rx.search(base)
        if m:
            try:
                iso = fmt(m)
                datetime.strptime(iso, "%Y-%m-%d")
                return iso
            except ValueError:
                continue
    return None


def read_csv(path):
    """
    Header-driven, never positional. The asset listing archive changes shape
    across dates -- some files carry 125 columns and others a different layout
    beginning with property name and short code -- so a positional read would
    silently file the wrong values.
    """
    raw = open(path, encoding="utf-8-sig", errors="replace").read()
    rows = list(csv.DictReader(io.StringIO(raw)))
    return rows


def candidates(dataset_name, prov):
    """Files this provider could serve, newest as-of first."""
    pat = prov.get("pattern") or "*.csv"
    # a pattern is a naming convention, not a glob, so loosen the date part
    g = re.sub(r"Y{4}-M{2}-D{2}|YYMMDD|YYYY-MM-DD", "*", pat)
    if "*" not in g:
        g = "*" + g
    here = os.path.join(INCOMING, dataset_name)
    found = glob.glob(os.path.join(here, g)) + glob.glob(os.path.join(here, "*.csv"))
    seen, out = set(), []
    for f in found:
        if f in seen:
            continue
        seen.add(f)
        out.append((as_of_from_name(f) or "0000-00-00", f))
    out.sort(reverse=True)
    return out


def normalise(rows, field_map, dataset):
    """Map provider columns onto canonical ones, and pull the stage dates."""
    stages = dataset.get("stage_dates") or {}
    strip = set(dataset.get("pii_strip") or [])
    out = []
    for r in rows:
        rec = {}
        for canon, src in field_map.items():
            rec[canon] = (r.get(src) or "").strip() if isinstance(r.get(src), str) else r.get(src)
        for label, src in stages.items():
            v = r.get(src)
            rec["stage_" + label] = (v or "").strip() if isinstance(v, str) else v
        # PII never reaches a written file, whichever provider served it.
        for bad in strip:
            rec.pop(bad, None)
        out.append(rec)
    return out


def pick(dataset_name, dataset):
    """First enabled provider that actually has a file. Returns (prov, as_of, path)."""
    tried = []
    for prov in dataset["providers"]:
        if not prov.get("enabled"):
            tried.append((prov["name"], "disabled"))
            continue
        if prov["kind"] == "warehouse":
            tried.append((prov["name"], "warehouse provider, not file-backed"))
            continue
        cands = candidates(dataset_name, prov)
        if not cands:
            tried.append((prov["name"], "no file in pipeline/incoming/%s" % dataset_name))
            continue
        as_of, path = cands[0]
        return prov, as_of, path, tried
    return None, None, None, tried


def status():
    cfg = load_cfg()
    print("%-16s %-22s %-12s %s" % ("DATASET", "SERVED BY", "AS OF", "FILE"))
    for name, ds in cfg.items():
        prov, as_of, path, tried = pick(name, ds)
        if prov:
            print("%-16s %-22s %-12s %s"
                  % (name, prov["name"], as_of, os.path.basename(path)))
        else:
            print("%-16s %-22s %-12s %s" % (name, "— nothing available —", "—", ""))
        for who, why in tried:
            print("%-16s   skipped %-18s %s" % ("", who, why))


def build(which=None):
    cfg = load_cfg()
    manifest = {}
    if os.path.exists(MANIFEST):
        manifest = json.load(open(MANIFEST))
    for name, ds in cfg.items():
        if which and name not in which:
            continue
        prov, as_of, path, _ = pick(name, ds)
        if not prov:
            print("[sources] %s: no provider available, leaving the previous file alone"
                  % name)
            continue
        rows = read_csv(path)
        if not rows:
            print("[sources] %s: %s is empty, refusing to overwrite"
                  % (name, os.path.basename(path)), file=sys.stderr)
            continue
        recs = normalise(rows, resolve_map(prov, ds), ds)
        out = os.path.join(REPO, "pipeline", "raw", "%s.json" % name)
        payload = {"dataset": name, "provider": prov["name"], "as_of": as_of,
                   "source_file": os.path.basename(path),
                   "row_count": len(recs), "rows": recs}
        with open(out, "w") as f:
            json.dump(payload, f)
        prev = (manifest.get(name) or {}).get("as_of")
        moved = "" if prev is None else (" (was %s)" % prev if prev != as_of
                                         else "  AS-OF UNCHANGED, no new day of history")
        print("[sources] %-16s %-20s as of %s  %5d rows -> raw/%s.json%s"
              % (name, prov["name"], as_of, len(recs), name, moved))
        manifest[name] = {"provider": prov["name"], "as_of": as_of,
                          "source_file": os.path.basename(path),
                          "row_count": len(recs),
                          "read_on": date.today().isoformat()}
    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    json.dump(manifest, open(MANIFEST, "w"), indent=1)
    print("[sources] manifest -> data/source_manifest.json")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "status":
        status()
    elif cmd == "build":
        build(sys.argv[2:] or None)
    else:
        raise SystemExit(__doc__)
