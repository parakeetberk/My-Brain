# -*- coding: utf-8 -*-
"""Extract the comment history out of a published board page.

    python3 pull_comments.py <board.html> [out.json]

Run this on the LIVE artifact HTML before every rebuild. `build_board.py`
reads `comments.json` from this directory and carries it through untouched,
so a rebuild can never lose a comment Austin has saved.

To mark comments as done after writing them into the registers:
    python3 pull_comments.py <board.html> comments.json --action KP-0010 TD-0004

Writes `edits.json` alongside it - the in-place corrections to priority,
category, community and owner. `build_board.py` reads both automatically.
"""
import io, os, re, sys, json

def extract(path):
    s = io.open(path, encoding="utf-8").read()
    m = re.search(r'<script id="board" type="application/json">(.*?)</script>', s, re.S)
    if not m:
        raise SystemExit("no board data block in %s" % path)
    data = json.loads(m.group(1).replace("\\u003c", "<"))
    return data.get("comments", {}), data

def dump_edits(data, out, ids=None, all_=False):
    edits = data.get("edits", {})
    n = 0
    for rid, fields in edits.items():
        for f, e in fields.items():
            if e.get("state") != "actioned" and (all_ or (ids and rid in ids)):
                e["state"] = "actioned"; n += 1
    if ids or all_:
        print("marked actioned: %d correction(s)" % n)
    json.dump(edits, io.open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    tot = sum(len(v) for v in edits.values())
    op = sum(1 for v in edits.values() for e in v.values() if e.get("state") != "actioned")
    print("corrections: %d across %d row(s), %d still open -> %s" % (tot, len(edits), op, out))
    return edits

def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    src = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else "comments.json"
    comments, _data = extract(src)
    ids = []
    if "--action" in sys.argv:
        ids = sys.argv[sys.argv.index("--action") + 1:]
        ids = [i for i in ids if not i.startswith("--")]
        n = 0
        for rid in ids:
            for c in comments.get(rid, []):
                if c.get("state") != "actioned":
                    c["state"] = "actioned"; n += 1
        print("marked actioned: %d comment(s) across %d id(s)" % (n, len(ids)))
    if "--action-all" in sys.argv:
        n = 0
        for rid in comments:
            for c in comments[rid]:
                if c.get("state") != "actioned":
                    c["state"] = "actioned"; n += 1
        print("marked actioned: %d comment(s)" % n)
    json.dump(comments, io.open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    _flags = _data.get("flags", {})
    fout = os.path.join(os.path.dirname(os.path.abspath(out)) or ".", "flags.json")
    json.dump(_flags, io.open(fout, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    nbw = sum(1 for v in _flags.values() if "budget" in v)
    print("flags: %d row(s) flagged for budget week -> %s" % (nbw, fout))
    dump_edits(_data, os.path.join(os.path.dirname(os.path.abspath(out)) or ".", "edits.json"),
               ids=set(ids) if "--action" in sys.argv else None, all_=("--action-all" in sys.argv))
    tot = sum(len(v) for v in comments.values())
    op = sum(1 for v in comments.values() for c in v if c.get("state") != "actioned")
    print("%s: %d comment(s) across %d row(s), %d still open -> %s" % (src, tot, len(comments), op, out))

if __name__ == "__main__":
    main()
