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

EMAILS = os.path.join(REPO, "pipeline", "community_emails.json")

# Addresses are STORED, not derived. The first version of this file generated
# them from the roster and would have got several wrong: obo@ and pse@ are
# initialisms, triples@ drops a word, vantageoak@ is singular where the roster
# is plural, GreenPointe@ spells what the roster calls Greene Pointe, and one
# mailbox serves both Bay Oaks villages. Wrong address means mail about one park
# arriving at another, so this is reviewed data rather than a rule.


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
    src = json.load(open(EMAILS))
    sold = sold_matchers()
    given, shared = src["communities"], src.get("_shared", {})
    table, skipped, no_mailbox = {}, [], []
    for r in roster:
        code, name = r["short_name"], r["property_name"]
        names = {str(r.get(f) or "").strip().upper()
                 for f in ("short_name", "property_name", "community")}
        if names & sold:
            skipped.append(name)
            continue
        local = given.get(code)
        via = None
        if not local and code in shared and not code.startswith("_"):
            via = shared[code]
            local = given.get(via)
        if not local:
            no_mailbox.append((code, name))
            continue
        table[code] = {
            "community": name,
            "email": "%s@%s" % (local, DOMAIN),
            "shares_with": via,
            "verified": True,
        }
    payload = {
        "_comment": [
            "Derived from pipeline/raw/pds_reportable.json by pipeline/routing.py.",
            "Do not hand-edit: re-run `routing.py build` instead, or the next",
            "roster refresh will silently disagree with this file.",
            "Addresses come from pipeline/community_emails.json, supplied by",
            "Austin from the M365 group list. They follow no derivable rule.",
            "Communities under registry.json `sold` are excluded outright.",
            "`no_mailbox` communities have nowhere to send and must not be",
            "silently skipped -- surface them instead.",
        ],
        "convention": {"source": "pipeline/community_emails.json",
                       "domain": DOMAIN, "supplied": src.get("supplied")},
        "no_mailbox": [{"short_name": c, "community": n} for c, n in no_mailbox],
        "not_a_community": src.get("_not_a_community", {}),
        "unresolved": src.get("_unresolved", {}),
        "communities": table,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(payload, open(OUT, "w"), indent=1)
    live = len([r for r in roster
                if not ({str(r.get(f) or "").strip().upper()
                         for f in ("short_name", "property_name", "community")} & sold)])
    print("[routing] %d of %d live communities routed -> data/routing.json"
          % (len(table), live))
    sh = [c for c in table if table[c]["shares_with"]]
    if sh:
        print("[routing] sharing a mailbox with another park: %s" % ", ".join(sorted(sh)))
    if skipped:
        print("[routing] excluded as sold: %s" % ", ".join(sorted(skipped)))
    if no_mailbox:
        print("[routing] NO MAILBOX for %d: %s"
              % (len(no_mailbox), ", ".join("%s (%s)" % (c, n) for c, n in no_mailbox)))


def show():
    d = json.load(open(OUT))
    print("source: %s   supplied %s"
          % (d["convention"]["source"], d["convention"]["supplied"]))
    print("%-10s %-34s %s" % ("CODE", "COMMUNITY", "EMAIL"))
    for code, v in sorted(d["communities"].items()):
        print("%-10s %-34s %-42s %s"
              % (code, v["community"][:34], v["email"],
                 ("shared with " + v["shares_with"]) if v["shares_with"] else ""))


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
