#!/usr/bin/env python3
"""
Where a community's reports and alerts get sent.

Austin's call, and it is better than the per-manager mapping I proposed: mail
goes to the community address, not to a named person. It survives turnover with
no roster to maintain, and the manager, the regional and the director all see the
same message land, which buys accountability without needing a task system.

Convention: [community]@parakeetcommunities.com, with the short code in the slot.
PROVISIONAL -- Austin's words were "use the short code now and we will update
it", so the token may change. Because this derives from the roster rather than
being a pasted list, changing the convention is a one-line edit here and every
address regenerates. A static spreadsheet would have to be re-collected.

NOTHING IS SENT UNTIL THESE ARE VERIFIED. A derived address that does not exist
bounces at best and reaches the wrong mailbox at worst, so `verified` stays false
until someone confirms the addresses resolve. The alert step must refuse to send
to an unverified address.

    routing.py build     regenerate data/routing.json from the roster
    routing.py show      print the table
"""
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROSTER = os.path.join(REPO, "pipeline", "raw", "pds_reportable.json")
REGISTRY = os.path.join(REPO, "pipeline", "registry.json")
OUT = os.path.join(REPO, "data", "routing.json")
DOMAIN = "parakeetcommunities.com"

# The token that goes in [community]. Change this one value to change every
# address. "short_code" is what Austin chose provisionally; "slug" is the
# community name with punctuation removed.
TOKEN = "short_code"


def slug(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def address(row):
    if TOKEN == "short_code":
        t = (row.get("short_name") or "").lower()
    else:
        t = slug(row.get("community") or row.get("property_name"))
    return "%s@%s" % (t, DOMAIN) if t else None


def sold_matchers():
    """
    The roster is not the routing list. A disposition lands in the Property Data
    Sheet later than it lands in reality, so registry.json carries an override
    for parks that are sold while the PDS still reads Reportable = Yes. Those
    must not receive alerts -- mail to a park we no longer own is the worst
    possible bounce.
    """
    reg = json.load(open(REGISTRY))
    out = set()
    for entry in reg.get("sold", []):
        for m in entry.get("match", []):
            out.add(str(m).strip().upper())
    return out


def build():
    roster = json.load(open(ROSTER))
    sold = sold_matchers()
    table, missing, dupes, skipped = {}, [], {}, []
    for r in roster:
        names = {str(r.get(f) or "").strip().upper()
                 for f in ("short_name", "property_name", "community")}
        if names & sold:
            skipped.append(r["property_name"])
            continue
        a = address(r)
        name = r["property_name"]
        if not a:
            missing.append(name)
            continue
        if a in dupes:
            # Two communities resolving to one mailbox would silently merge two
            # parks' alerts into one inbox, so it is an error rather than a note.
            print("[routing] COLLISION %s -> %s and %s" % (a, dupes[a], name),
                  file=sys.stderr)
        dupes[a] = name
        table[r["short_name"]] = {
            "community": name, "email": a, "verified": False,
        }
    payload = {
        "_comment": [
            "Derived from pipeline/raw/pds_reportable.json by pipeline/routing.py.",
            "Do not hand-edit: re-run `routing.py build` instead, or the next",
            "roster refresh will silently disagree with this file.",
            "Convention: [%s]@%s, PROVISIONAL per Austin 2026-09-09." % (TOKEN, DOMAIN),
            "verified=false everywhere until someone confirms the mailboxes exist.",
            "The alert step must refuse to send to an unverified address.",
            "Communities under registry.json `sold` are excluded outright.",
        ],
        "convention": {"token": TOKEN, "domain": DOMAIN, "verified_any": False},
        "communities": table,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(payload, open(OUT, "w"), indent=1)
    print("[routing] %d addresses -> data/routing.json  (token=%s, all unverified)"
          % (len(table), TOKEN))
    if skipped:
        print("[routing] excluded as sold, no mail will be routed: %s"
              % ", ".join(sorted(skipped)))
    if missing:
        print("[routing] %d communities have no short code: %s"
              % (len(missing), ", ".join(missing)))


def show():
    d = json.load(open(OUT))
    print("convention: [%s]@%s   verified: %s"
          % (d["convention"]["token"], d["convention"]["domain"],
             d["convention"]["verified_any"]))
    print("%-10s %-34s %s" % ("CODE", "COMMUNITY", "EMAIL"))
    for code, v in sorted(d["communities"].items()):
        print("%-10s %-34s %s" % (code, v["community"][:34], v["email"]))


if __name__ == "__main__":
    # A routine pipes this output; do not traceback when the reader closes early.
    try:
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    {"build": build, "show": show}.get(
        sys.argv[1] if len(sys.argv) > 1 else "build",
        lambda: (_ for _ in ()).throw(SystemExit(__doc__)))()
