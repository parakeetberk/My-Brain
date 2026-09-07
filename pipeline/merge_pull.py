#!/usr/bin/env python3
"""
Merge warehouse pulls that had to be split across calls, and refuse to write a
partial one.

The occupancy query times out at 60s with all six measures, so it goes out as
three calls of two and the parts are joined on their shared dimensions here.
Every part must agree on row count and key set, otherwise a measure would land
against the wrong property-month and nothing downstream would notice.

    merge_pull.py <out-name> <dim1,dim2> <file1> <file2> ...
"""
import json
import os
import sys

REPO = "/home/user/My-Brain"


def load(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    i = raw.find("{")
    if i == -1:
        raise SystemExit("no JSON in %s" % path)
    obj = json.loads(raw[i:])
    rows = obj.get("rows")
    if rows is None:
        raise SystemExit("%s has no rows" % path)
    if obj.get("rowCount") is not None and obj["rowCount"] != len(rows):
        raise SystemExit("%s: rowCount %s but %d rows parsed"
                         % (path, obj["rowCount"], len(rows)))
    return rows


def main():
    out_name = sys.argv[1]
    dims = sys.argv[2].split(",")
    parts = [load(p) for p in sys.argv[3:]]

    counts = {len(p) for p in parts}
    if len(counts) != 1:
        raise SystemExit("parts disagree on row count: %s -- refusing to merge"
                         % sorted(counts))

    merged = {}
    for rows in parts:
        for r in rows:
            key = tuple(str(r.get(d)) for d in dims)
            merged.setdefault(key, {}).update(r)

    if len(merged) != len(parts[0]):
        raise SystemExit("merged to %d rows from %d -- the dimensions do not "
                         "uniquely key a row" % (len(merged), len(parts[0])))

    out = list(merged.values())
    # every row must carry every measure, or a split went wrong
    fields = set()
    for r in out:
        fields |= set(r.keys())
    short = [r for r in out if set(r.keys()) != fields]
    if short:
        raise SystemExit("%d rows are missing a measure after the merge" % len(short))

    dest = os.path.join(REPO, "pipeline", "raw", out_name)
    with open(dest, "w") as f:
        json.dump({"rowCount": len(out), "rows": out}, f)
    print("wrote %s: %d rows, %d fields (%s)"
          % (out_name, len(out), len(fields), ", ".join(sorted(fields))))


if __name__ == "__main__":
    main()
