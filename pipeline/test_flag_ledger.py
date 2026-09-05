#!/usr/bin/env python3
"""
Exercise the flag ledger the way tomorrow will: a note whose figure moved, a
note that cleared, and one that came back.

Backdates and doctors data/flag_history.json, reruns the build, and checks what
the payload says. Restores nothing -- the caller rebuilds afterwards.
"""
import json
import os
import subprocess
import sys

REPO = "/home/user/My-Brain"
LEDGER = os.path.join(REPO, "data/flag_history.json")

book = json.load(open(LEDGER))
flags = book["flags"]

# 1. A note that has been open a while, whose figure has since moved.
aged = "utility-recapture-below-target"
flags[aged]["first_seen"] = "2026-06-01"
flags[aged]["title"] = "Utility recapture is 51% against a 80% target"
flags[aged]["history"] = [
    {"date": "2026-06-01", "event": "opened",
     "title": "Utility recapture is 51% against a 80% target", "severity": "warn"}
]

# 2. A note that fired before and will not fire today -- it should clear.
flags["a-note-that-went-away"] = {
    "first_seen": "2026-07-10", "last_seen": "2026-09-04",
    "severity": "warn", "title": "Something that has since been fixed",
    "history": [{"date": "2026-07-10", "event": "opened",
                 "title": "Something that has since been fixed", "severity": "warn"}],
}

# 3. A note previously marked resolved that fires again -- it should reopen and
#    keep its original first_seen.
back = "no-punch-stage-in-rm"
flags[back]["first_seen"] = "2026-05-02"
flags[back]["resolved_on"] = "2026-08-20"
flags[back]["history"] = [
    {"date": "2026-05-02", "event": "opened",
     "title": "There is no punch stage in Rent Manager", "severity": "info"},
    {"date": "2026-08-20", "event": "resolved",
     "title": "There is no punch stage in Rent Manager", "severity": "info"},
]

json.dump(book, open(LEDGER, "w"), indent=1, sort_keys=True)
print("ledger doctored; rebuilding\n")

r = subprocess.run([sys.executable, os.path.join(REPO, "pipeline/build.py")],
                   capture_output=True, text=True, cwd=REPO)
line = [x for x in r.stdout.splitlines() if x.startswith("[build] flags:")]
print(line[0] if line else r.stdout[-400:])
if r.returncode:
    print(r.stderr[-1500:])
    sys.exit(1)

d = json.load(open(os.path.join(REPO, "data/dashboard.json")))
by = {f["id"]: f for f in d["flags"]}
ok = True


def check(label, got, want):
    global ok
    good = got == want
    ok = ok and good
    print(("  OK   " if good else "  FAIL ") + label + ": " + repr(got)
          + ("" if good else " (expected " + repr(want) + ")"))


print("\n1. figure moved on an aged note")
f = by[aged]
check("first_seen preserved", f["first_seen"], "2026-06-01")
check("days_open accrued", f["days_open"] > 90, True)
check("one change recorded", f["changes"], 1)
check("newest history entry is the change", f["history"][0]["event"], "changed")
check("change carries the new title", "46%" in f["history"][0]["title"], True)

print("\n2. a note that stopped firing")
g = by.get("a-note-that-went-away")
check("still in the payload", bool(g), True)
if g:
    check("marked resolved", g["resolved"], True)
    check("resolved_on set", bool(g["resolved_on"]), True)
    check("history closes with resolved", g["history"][0]["event"], "resolved")

print("\n3. a resolved note that came back")
b = by[back]
check("reopened, not resolved", b["resolved"], False)
check("original first_seen kept", b["first_seen"], "2026-05-02")
check("history records the reopen", b["history"][0]["event"], "reopened")

print("\n" + ("ALL LEDGER CHECKS PASS" if ok else "LEDGER HAS A PROBLEM"))
sys.exit(0 if ok else 1)
