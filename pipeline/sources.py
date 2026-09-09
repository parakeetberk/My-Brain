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
import difflib
import re
import sys
from collections import defaultdict
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


def community_index():
    """short name / property name / community -> the canonical roster name."""
    path = os.path.join(REPO, "pipeline", "raw", "pds_reportable.json")
    if not os.path.exists(path):
        return {}, []
    pds = json.load(open(path))
    look = {}
    for p in pds:
        for k in (p.get("short_name"), p.get("property_name"), p.get("community")):
            if k and str(k).strip():
                look[str(k).strip().upper()] = p["property_name"]
    return look, sorted({p["property_name"] for p in pds})


def _norm_name(x):
    """Strip the retired-record prefix and the interchangeable suffixes."""
    x = re.sub(r"^x", "", x or "", flags=re.I)
    x = re.sub(r"\b(MHC|MHP|Manufactured Housing Community|Homes|Village|Park)\b",
               "", x, flags=re.I)
    return re.sub(r"[^a-z0-9]", "", x.lower())


def classify_community(raw, look, roster, _cache={}):
    """
    Assets carry communities the roster does not, and they are not all the same
    kind of problem. Austin's point: the asset listing deliberately keeps
    disposed and inactive records so sales can still be tracked, so filtering
    them out would erase real history while counting them inflates every
    current-inventory number.

    Three outcomes, never two:

      current       -- a live reportable community. Counts toward the piles and
                       the pace.
      historical    -- an `x`-prefixed retired duplicate of a community that is
                       still live, or a community that has been disposed. Its
                       assets are mostly Sold and they are real sales. Counts
                       toward sales history, never toward current inventory.
      unattributed  -- UNASSIGNED, blank, or a name nothing matches. Counted
                       nowhere and flagged, because 45 homes marked To Be Demoed
                       with no community is a data problem, not a pile.

    The alias pass matters: `Hunter Springs MHC` in the asset file against
    `Hunter Springs MHP` in the roster was silently dropping seven live assets
    over a three-letter suffix.
    """
    key = (raw or "").strip()
    if key in _cache:
        return _cache[key]
    up = key.upper()
    if not key or up == "UNASSIGNED":
        out = ("unattributed", None)
    elif up in look:
        out = ("current", look[up])
    else:
        n = _norm_name(key)
        nr = {_norm_name(r): r for r in roster}
        hit = nr.get(n)
        if not hit:
            m = difflib.get_close_matches(n, list(nr), 1, 0.92)
            hit = nr[m[0]] if m else None
        if hit and key.lower().startswith("x"):
            out = ("historical", hit)          # retired duplicate of a live park
        elif hit:
            out = ("current", hit)             # alias miss, e.g. MHC vs MHP
        else:
            out = ("historical", key)          # disposed or never reportable
    _cache[key] = out
    return out


def normalise(rows, field_map, dataset):
    """Map provider columns onto canonical ones, and pull the stage dates."""
    look, roster = community_index()
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
        if "community" in rec:
            scope, canon = classify_community(rec.get("community"), look, roster)
            rec["community_raw"] = rec.get("community")
            rec["community"] = canon
            rec["scope"] = scope
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
        if recs and "scope" in recs[0]:
            tally = defaultdict(int)
            for r in recs:
                tally[r["scope"]] += 1
            print("[sources]   scope: %s"
                  % ", ".join("%s %d" % (k, tally[k])
                              for k in ("current", "historical", "unattributed")
                              if tally[k]))
            if tally["unattributed"]:
                print("[sources]   WARNING %d rows have no community and are counted "
                      "nowhere" % tally["unattributed"])
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
