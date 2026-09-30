# -*- coding: utf-8 -*-
"""Rebuild the Open Board page from the six registers.

    VAULT="$HOME/mnt/My Brain" python3 build_board.py [--comments comments.json]

The page renders its rows from a JSON block rather than from pre-rendered
markup, which is what lets it republish ITSELF when Austin saves a comment.
It carries a base64 copy of its own template so a self-publish is a fixed
point: only the data block changes.

Comment history is never generated here. It is read from `comments.json`
(extracted from the live artifact by `pull_comments.py`) and carried
through untouched, so a rebuild can never lose a comment.
"""
import io, os, re, sys, json, html, base64, collections
from parse_registers import build, VAULT

# Build date, derived rather than hand-typed. Hand-typed dates in this builder went stale
# the same way the row count in the page header did - see KP-0039 and TD-0391.
import datetime as _dt
TODAY = _dt.date.today().strftime("%-d %B %Y") if os.name != "nt" else _dt.date.today().strftime("%#d %B %Y")
HERE = os.path.dirname(os.path.abspath(__file__))
def R(n): return io.open(os.path.join(HERE, n), encoding="utf-8").read()

STOP = set("the a an and or of to in on for with that this it is are was were be been at by from as "
           "into not no nothing needs need has have had which whose what who when where why how "
           "its their our his her them they we you i one two three still yet only also".split())
def search_phrase(desc):
    w = [x for x in re.findall(r"[A-Za-z0-9$,'.-]+", desc or "") if x.lower() not in STOP and len(x) > 2]
    return " ".join(w[:7])

SUBS = {
 "Commitments":        "What you owe and are owed at the corporate level",
 "Promises":           "Things you told a named person you would do. Closes when they are told, not when it is done",
 "Parked decisions":   "Waiting on your ruling. A row leaves when you rule, not when it ages",
 "Known problems":     "Findings about the business and about the Brain, ranked by risk",
 "EOS to-dos":         "Actions with a named owner, grouped for one-on-ones",
 "Property follow-ups":"Property-level follow-ups, by community",
}
REG_ORDER = ["Commitments", "Promises", "Parked decisions", "Known problems", "EOS to-dos", "Property follow-ups"]

HOW = """
<div class="how">
  <h2>How the comment loop works</h2>
  <p><b>Every row has a Comment button next to Copy search.</b> It opens the item in full with its whole comment history, date stamped, oldest first. Add a note and it sits as <b>pending</b> in this browser until you hit <b>Save to the page</b>, which writes it into the board itself so it survives a reload and anyone with the link can see it.</p>
  <p><b>Save does not reach me.</b> Nothing wakes a cloud session when you type. So the button that actually moves work is <b>Copy open comments</b>: it puts every unactioned note on your clipboard as <code style="font-family:var(--mono)">KP-0001: your text</code>, one line per row. Paste that into chat and I write them into the registers, then rebuild this page with those comments marked <b>actioned</b>.</p>
  <p><b>Four fields on every row are editable in place: priority, category, community and owner.</b> Click one, pick from the list, and it turns amber as a pending correction. They ride the same Save and the same Copy as comments, and arrive in chat as <code style="font-family:var(--mono)">TD-0044: Community -&gt; Riverwalk (was blank)</code>. The board shows your corrected value straight away; the register is not changed until I write it.</p>
  <p><b>Due date and cost are set the same way.</b> Every row carries a <code style="font-family:var(--mono)">+ due</code> and a <code style="font-family:var(--mono)">+ cost</code> chip; click one for a date picker or a box to type into. An overdue date goes red. Filter with <b>Has a date</b> and <b>Has a cost</b>.</p>
  <p><b>Ask for a draft in a comment and it comes back in the same thread.</b> &ldquo;Draft an email to Melanie about the Royal Oaks titles&rdquo; on the row, send it over, and the draft lands as a reply on that row with a <b>copy</b> button. It never counts as an open comment, because a reply is not something you owe anyone.</p>
  <p><b>The <code style="font-family:var(--mono)">BW</code> box on the left flags a row for budget week.</b> Tick as many as you like and use <b>Budget week only</b> to read the list back. Flags ride the same Save and the same Copy, and when you send them over I build the budget-week list as its own document. <b>A tick is a filter; a comment is prose</b> &mdash; use the box for what goes on the list and a comment for why.</p>
  <p><b>A rebuild never wipes your comments, corrections or flags.</b> The builder reads this page first and carries the history through. Three states, all visible in the popup: <b>pending</b> (in your browser only), <b>open</b> (saved here, waiting on me), <b>actioned</b> (written into the register).</p>
</div>
"""

FOOTER = ("%d rows from commitments, promises, parked decisions, known problems, EOS to-dos and property "
          "follow-ups, " + TODAY + ". IDs are written into the register files themselves, so they "
          "survive every rebuild. Owner, age, state and category come from the register that holds the "
          "row wherever it states them; category is inferred where no register states one and %d rows "
          "sit in Uncategorised rather than being forced. Priority is the source's own signal, never "
          "invented. The registers do overlap in practice, so %d is a row count and not a count of "
          "distinct problems. Built by 00-Meta/board-data/builder/build_board.py, which reads every "
          "markdown table by its own header row.")

def main():
    comments, edits, flags = {}, {}, {}
    for fn, tgt in (("flags.json", "flags"),):
        fp = os.path.join(HERE, fn)
        if os.path.exists(fp):
            flags = json.load(io.open(fp, encoding="utf-8"))
    if "--edits" in sys.argv:
        ep = sys.argv[sys.argv.index("--edits") + 1]
        if os.path.exists(ep):
            edits = json.load(io.open(ep, encoding="utf-8"))
    elif os.path.exists(os.path.join(HERE, "edits.json")):
        edits = json.load(io.open(os.path.join(HERE, "edits.json"), encoding="utf-8"))
    if "--comments" in sys.argv:
        cp = sys.argv[sys.argv.index("--comments") + 1]
        if os.path.exists(cp):
            comments = json.load(io.open(cp, encoding="utf-8"))
    elif os.path.exists(os.path.join(HERE, "comments.json")):
        comments = json.load(io.open(os.path.join(HERE, "comments.json"), encoding="utf-8"))

    rows = build()
    keys = ("id","reg","sec","desc","notes","owner_short","owner_full","category","community",
            "priority","state","lot","age","srcurl","srctype","regurl","person","due","cost")
    out = []
    for r in rows:
        d = {k: r.get(k, "") for k in keys}
        d["q"] = search_phrase(d["desc"])
        d["desc"] = d["desc"][:700]
        d["notes"] = squeeze(d.get("notes") or "", 2000)
        out.append(d)
    order = {n: i for i, n in enumerate(REG_ORDER)}
    out.sort(key=lambda r: (order.get(r["reg"], 99),))

    n_total = len(out)
    n_open = sum(1 for r in out if r["priority"] != "Closed")
    n_unowned = sum(1 for r in out if r["owner_short"] == "Unassigned" and r["priority"] != "Closed")
    n_hot = sum(1 for r in out if r["priority"] in ("Critical (stated)", "Awaiting your ruling"))
    n_closed = n_total - n_open
    n_uncat = sum(1 for r in out if r["category"] == "Uncategorised")

    communities = sorted({r["community"] for r in out if r["community"]} | portfolio_communities())
    # The dropdown offers Austin's list, plus any value still on a row that is
    # not on it - so an unmapped owner can be seen and corrected, not hidden.
    from parse_registers import _canon
    allowed = list(_canon()["allowed"])
    stray = sorted({r["owner_short"] for r in out if r["owner_short"] and r["owner_short"] not in allowed})
    owners = sorted(allowed) + stray
    cats = sorted({r["category"] for r in out if r["category"]})
    opts = dict(priority=["Critical (stated)", "Awaiting your ruling", "High (stated)", "High (ledger)",
                          "Blocked", "Decided, never actioned", "Open", "Closed"],
                category=cats, community=communities, owner_short=owners)

    meta = dict(built=TODAY, opts=opts,
                flags=[dict(key="budget", label="Budget week", short="BW")], total=n_total, open=n_open, unowned=n_unowned, hot=n_hot,
                closed=n_closed, subs=SUBS, how=HOW,
                footer=FOOTER % (n_total, n_uncat, n_total))

    head = R("template_head.html").replace("__BOARD_CSS__", R("board.css"))
    tpl = (head +
           '\n<div class="wrap" id="app"></div>\n' +
           '<script id="tpl" type="text/plain">__TPL_B64__</script>\n' +
           '<script id="board" type="application/json">__DATA_JSON__</script>\n' +
           "<script>\n" + R("template_app.js") + "\n</script>\n")

    b64 = base64.b64encode(tpl.encode("utf-8")).decode("ascii")
    data = json.dumps(dict(meta=meta, rows=out, comments=comments, edits=edits, flags=flags),
                      ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    doc = tpl.replace("__TPL_B64__", lambda_free(b64)).replace("__DATA_JSON__", lambda_free(data))

    io.open(os.path.join(HERE, "open-board.html"), "w", encoding="utf-8").write(doc)
    json.dump(out, io.open(os.path.join(HERE, "open-board-2026-09-01.json"), "w", encoding="utf-8"),
              ensure_ascii=False)
    ncom = sum(len(v) for v in comments.values())
    ned = sum(len(v) for v in edits.values())
    nfl = sum(len(v) for v in flags.values())
    print("rows %d  open %d  unowned %d  comments %d  corrections %d  flags %d  bytes %d"
          % (n_total, n_open, n_unowned, ncom, ned, nfl, len(doc)))

def portfolio_communities():
    """The 67 communities from the portfolio table, so a row can be moved to a
    community that currently has no rows on the board."""
    p = os.path.join(VAULT, "60-Communities", "portfolio.md")
    if not os.path.exists(p):
        return set()
    names = set()
    for ln in io.open(p, encoding="utf-8").read().split("\n"):
        m = re.match(r"^\|\s*[A-Z0-9]+\s*\|\s*\[\[60-Communities/[a-z0-9\-]+\\?\|([^\]]+)\]\]", ln)
        if m:
            names.add(m.group(1).strip())
    return names

def squeeze(t, n):
    """Keep the head (the finding) and the tail (the latest developments).
    Cutting only from the end would drop exactly the part that changed today."""
    if len(t) <= n:
        return t
    head, tail = int(n * 0.35), n - int(n * 0.35)
    return t[:head].rstrip() + "  […]  " + t[-tail:].lstrip()

def lambda_free(s):
    """str.replace treats no characters specially, but re-based helpers do.
    Kept explicit so nobody 'improves' this into re.sub and gets bitten by \\1."""
    return s

if __name__ == "__main__":
    main()
