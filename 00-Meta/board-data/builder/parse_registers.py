# -*- coding: utf-8 -*-
"""Parse the five Parakeet registers into board rows.

Header-driven: every markdown table is read by its own header row, so a table
with six columns and a table with five both map correctly. The 2026-09-01
mapping defect came from assuming a fixed column order.
"""
import io, os, re, json, html, urllib.parse

VAULT = os.environ.get("VAULT", "/mnt/user-data/uploads/My Brain")

ID_RE = re.compile(r"`((?:CM|PD|KP|TD|PF|PR)-\d{2,4})`")
WIKI  = re.compile(r"\[\[([^\]|]+)(?:\\?\|([^\]]+))?\]\]")

CAT_RE = re.compile(r"\[cat:\s*([^\]]+)\]", re.I)
PRI_RE = re.compile(r"\[pri:\s*([^\]]+)\]", re.I)
def overrides(blob):
    """Austin corrects a row's bucket on the board; the fix is written into the
    register as [cat: X] or [pri: X] and stripped before display."""
    c = CAT_RE.search(blob or ""); p = PRI_RE.search(blob or "")
    return (c.group(1).strip() if c else ""), (p.group(1).strip() if p else "")

def clean(t):
    t = WIKI.sub(lambda m: (m.group(2) or m.group(1).split("/")[-1]), t or "")
    t = re.sub(r"~~([^~]*)~~", r"\1", t)
    t = t.replace("**","").replace("*","").replace("`","")
    t = re.sub(r"<[^>]+>", "", t)
    t = CAT_RE.sub("", t); t = PRI_RE.sub("", t)
    return re.sub(r"\s+", " ", t).strip()

NOTE_SPLIT = re.compile(r"\s+(?=(?:~~)?\*\*(?:20\d\d-\d\d-\d\d|CLOSED|FIXED|RESOLVED|CORRECTION|Sharpened|Deferred|Recorded)\b)")
def split_notes(cell):
    """Register cells accumulate dated dispositions after the finding itself.
    The finding is what belongs on a board row; the dispositions belong in the
    popup. Split on the first bolded date or disposition keyword."""
    m = NOTE_SPLIT.search(cell or "")
    if not m:
        return cell, ""
    return cell[:m.start()], cell[m.end():]

def split_row(ln):
    body = ln.strip()
    if not body.startswith("|"): return None
    body = body.strip("|").replace("\\|", "\x00")
    return [c.strip().replace("\x00", "|") for c in body.split("|")]

def is_sep(cells):
    return all(set(c) <= set("-: ") and c for c in cells)

CATS = [
 ("Titles",      r"\btitle|retitle|dmv|mso\b"),
 ("Legal",       r"\blegal|counsel|litigat|lawsuit|eviction|attorney|compliance|statut|lien\b"),
 ("Finance",     r"\baccount|invoice|payabl|receivab|budget|ap\b|ar\b|payroll|gl\b|ledger|ramp|wire|audit|tax|noi|revenue|reserve|capital|lender|floorplan|floor line|escrow|facility\b"),
 ("Systems & data", r"\bsharepoint|rent manager|warehouse|data|report|dashboard|power automate|entra|permission|migrat|system|integrat|api|onedrive|teams\b"),
 ("People",      r"\bhire|hr\b|handbook|onboard|employee|manager|staff|training|turnover|headcount\b"),
 ("Utilities",   r"\butilit|water|sewer|septic|electric|meter|boil|aerator|lift station|propane\b"),
 ("Construction",r"\brehab|construct|permit|set\b|demo|lot prep|skirting|roof|punch|make ready|capex|home order\b"),
 ("Collections", r"\bcollect|delinquen|past due|balance|over 90\b"),
 ("Sales & leasing", r"\bsale|lease|listing|prospect|market rent|infill|occupanc|mhvillage\b"),
 ("Resident",    r"\bresident|tenant|homeowner|renter|complaint\b"),
 ("Regulatory",  r"\bregulat|state filing|division|licen|inspection|esg|jadian\b"),
 ("Amenities",   r"\bamenit|pool|clubhouse|playground|shuffleboard|landscap|signage\b"),
]
def categorise(text):
    t = text.lower()
    for name, pat in CATS:
        if re.search(pat, t): return name
    return "Uncategorised"

CANON = None
def _canon():
    """Austin's owner list lives in owner-canon.json so it can be edited without
    touching code. A value that matches nothing is LEFT AS IT IS on the row -
    never silently reassigned - so the wrong ones stay visible and correctable."""
    global CANON
    if CANON is None:
        fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "owner-canon.json")
        if os.path.exists(fp):
            CANON = json.load(io.open(fp, encoding="utf-8"))
        else:
            CANON = {"allowed": ["Unassigned"], "aliases": {}}
    return CANON

def owner_short(full):
    f = (full or "").strip()
    if not f or re.match(r"^[-\u2014\u2013]$", f) or re.search(r"unassigned|no owner|nobody", f, re.I):
        return "Unassigned"
    low = re.sub(r"[*`\[\]]", "", f).lower()
    al = _canon()["aliases"]
    # longest alias first, and the one appearing EARLIEST in the string wins:
    # "Natalie Magurne ... Austin owns the travel" is Natalie's row.
    best, bestpos, bestlen = None, len(low) + 1, 0
    for a in sorted(al, key=len, reverse=True):
        m = re.search(r"(?<![a-z0-9])" + re.escape(a) + r"(?![a-z0-9])", low)
        if not m:
            continue
        i = m.start()
        if i < bestpos or (i == bestpos and len(a) > bestlen):
            best, bestpos, bestlen = al[a], i, len(a)
    if best:
        return best
    # unmapped: keep what the register says, trimmed, so it is visible and fixable
    return re.split(r"[,/;(\u2014]| - ", f)[0].strip().strip("*").strip()[:40] or "Unassigned"

def priority(reg, risk, state, section, desc):
    s = (state or "").lower()
    # word boundaries matter: "unresolved" contains "resolved" and CM-01 was
    # being reported as Closed because its status reads "documented
    # internally, unresolved".
    if re.search(r"\b(closed|resolved|complete|completed|done)\b", s): return "Closed"
    if reg == "Parked decisions": return "Awaiting your ruling"
    if "blocked" in s: return "Blocked"
    if re.search(r"decided.*(not action|never (done|actioned))", s): return "Decided, never actioned"
    r = (risk or "").lower()
    if "critical" in r or re.search(r"tier 1\b", (section or "").lower()): return "Critical (stated)"
    if "high" in r: return "High (stated)"
    if re.search(r"priority queue|tier [234]\b", (section or "").lower()): return "High (ledger)"
    if "deferred" in s or "waiting" in s: return "Open"
    return "Open"

_SLUGS = None
def _slug_names():
    """Proper community names from the portfolio table. Title-casing a slug
    gives 'Geiger Key Rv Resort'; the sheet says 'Geiger Key RV Resort'."""
    global _SLUGS
    if _SLUGS is None:
        _SLUGS = {}
        fp = os.path.join(VAULT, "60-Communities", "portfolio.md")
        if os.path.exists(fp):
            for m in re.finditer(r"\[\[60-Communities/([a-z0-9\-]+)\\?\|([^\]]+)\]\]",
                                 io.open(fp, encoding="utf-8").read()):
                _SLUGS.setdefault(m.group(1), m.group(2).strip())
    return _SLUGS

NOT_A_COMMUNITY = {"open-items","portfolio","regions","lots","activity","_model",
                   "asset-inventory","portfolio-baseline-warehouse","open-board"}
def community_of(text):
    m = re.search(r"60-Communities/([a-z0-9\-]+)", text or "")
    if m and m.group(1) not in NOT_A_COMMUNITY:
        return _slug_names().get(m.group(1), m.group(1).replace("-", " ").title())
    return ""

DUE_RE  = re.compile(r"\bdue\b[^0-9]{0,12}(20\d\d-\d\d-\d\d)", re.I)
COST_RE = re.compile(r"(?:est\.?\s*cost|cost)\b[^$]{0,12}\$\s*([\d,]+(?:\.\d+)?\s*[KkMm]?)", re.I)
BARE_RE = re.compile(r"\$\s*([\d,]+(?:\.\d+)?\s*[KkMm]?)")
def money_and_date(blob):
    """Two fields the registers never had. Parsed by convention, not guessed:
    a due date must be written as 'due YYYY-MM-DD', a cost as 'cost $N' or
    'est. cost $N'. A bare dollar figure counts only when the row has exactly
    one - more than one and it is prose about money, not the row's price."""
    d = DUE_RE.search(blob or "")
    c = COST_RE.search(blob or "")
    # Only the explicit form counts. A bare dollar figure in a sentence is
    # prose about money ("nearby $100K+ communities"), not the row's price,
    # and a wrong cost on a board row is worse than a blank one.
    cost = ("$" + c.group(1).strip()) if c else ""
    return (d.group(1) if d else ""), cost

def regurl(path):
    return "obsidian://open?vault=My%20Brain&file=" + urllib.parse.quote(path, safe="")

# ------------------------------------------------------------------ tables
def parse_table_register(relpath, regname, prefix, idcol_hint=None):
    p = os.path.join(VAULT, relpath)
    lines = io.open(p, encoding="utf-8").read().split("\n")
    out, section, headers = [], "", None
    for ln in lines:
        if ln.startswith("#"):
            section = clean(ln.lstrip("# ").strip()); headers = None; continue
        cells = split_row(ln)
        if cells is None:
            continue   # a blank line inside a table must NOT clear the header
        if is_sep(cells): continue
        joined = " | ".join(cells)
        if not ID_RE.search(joined):
            # candidate header row
            low = [c.lower() for c in cells]
            if any(h in low for h in ("item","finding","decision","promise","#")):
                headers = [c.strip() for c in cells]
            continue
        rid = ID_RE.search(joined).group(1)
        if not rid.startswith(prefix): continue
        h = headers if headers and len(headers) == len(cells) else None
        def pick(*names):
            if not h: return ""
            for n in names:
                for i, hd in enumerate(h):
                    if hd.lower().strip() == n: return cells[i]
            for n in names:
                for i, hd in enumerate(h):
                    if n in hd.lower(): return cells[i]
            return ""
        desc = pick("item","finding","decision","promise")
        if not desc:
            # fall back: the cell carrying the ID
            for c in cells:
                if ID_RE.search(c): desc = c; break
        desc, notes = split_notes(ID_RE.sub("", desc))
        desc = re.sub(r"^P\d+\s+", "", clean(desc)).strip()
        notes = clean(notes)
        owner = clean(pick("owner"))
        state = clean(pick("status"))
        risk  = clean(pick("risk","priority","confidence"))
        extra = " ".join(clean(pick(n)) for n in ("why it is here","what it blocks","context","where","raised"))
        blob  = " ".join(cells)
        person = clean(pick("person"))
        mu = re.search(r"\((https?://[^\s)]+)\)", blob)
        turl = mu.group(1) if mu else ""
        due, cost = money_and_date(blob)
        if not owner and h is None:
            owner = ""
        out.append(dict(id=rid, reg=regname, sec=section, desc=desc, notes=notes, owner_full=owner or "Unassigned",
                        state=state or "open", risk=risk, extra=extra,
                        file=relpath, community=community_of(blob) or clean(pick("property")),
                        age=None, lot="", srcurl=turl, srctype="", person=person, due=due, cost=cost))
    return out

# ------------------------------------------------------------ commitments
def parse_commitments(relpath="00-Meta/commitments.md"):
    lines = io.open(os.path.join(VAULT, relpath), encoding="utf-8").read().split("\n")
    out, section, cur = [], "", None
    for ln in lines:
        if ln.startswith("## "):
            section = clean(ln[3:]); continue
        # Two heading shapes, both live in this file. The original is `### 6. Title`,
        # numbered only. On 2026-09-02 another session wrote the permanent IDs into
        # the markdown as `### `CM-06` 6. Title`, per rule 15 - which is the right
        # move and broke a regex that required the digit first, silently dropping all
        # 25 commitment rows from the board. Accept both, and PREFER the written ID
        # over the position-derived one, because rule 15 says the file is authoritative.
        m = re.match(r"^###\s+(?:`(CM-\d{2,4})`\s+)?(\d+)\.\s+(.*)$", ln)
        if m:
            n = int(m.group(2))
            cur = dict(id=m.group(1) or ("CM-%02d" % n), reg="Commitments", sec=section or "Active",
                       desc=clean(re.sub(r"\s*[-—]\s*\*\*CLOSED.*$", "", m.group(3))), notes="",
                       owner_full="Unassigned", state="open", risk="", extra="",
                       file=relpath, community=community_of(m.group(3)), age=None, lot="",
                       srcurl="", srctype="")
            if "CLOSED" in m.group(3): cur["state"] = clean(re.search(r"\*\*(CLOSED[^*]*)\*\*", m.group(3)).group(1))
            out.append(cur); continue
        if cur is None: continue
        mo = re.match(r"^\s*-\s+\*\*Owner\*\*:\s*(.*)$", ln)
        if mo:
            if not cur.get("_owner_set"):
                cur["owner_full"] = clean(mo.group(1)); cur["_owner_set"] = True
            continue
        mp = re.match(r"^\s*-\s+\*\*Priority\*\*:\s*(.*)$", ln)
        if mp:
            cur["_pri"] = clean(mp.group(1)); continue
        ms = re.match(r"^\s*-\s+\*\*Status\*\*:\s*(.*)$", ln)
        if ms:
            if "CLOSED" not in cur["state"]: cur["state"] = clean(ms.group(1))
            continue
        if not cur["community"]: cur["community"] = community_of(ln)
        # every other bullet is body: the board shows it as Register notes, so a
        # commitment reads in the popup instead of being a bare headline.
        if re.match(r"^\s*-\s+\S", ln):
            cur.setdefault("_body", []).append(clean(re.sub(r"^\s*-\s+", "", ln)))
    # everything in Active outranks; risk from the page's own ranking language
    for r in out:
        if r["sec"].lower().startswith("active"): r["risk"] = "Critical"
        if r.get("_pri"): r["_prio"] = r.pop("_pri")
        r["notes"] = " · ".join(r.pop("_body", []))
        r.pop("_owner_set", None)
        r["due"], r["cost"] = money_and_date(r["desc"] + " " + r["notes"] + " " + r["state"])
    return out

# ------------------------------------------------- property follow-ups list
# The separator between a row's metadata and its statement used to be an em
# dash. On 2026-09-03 the voice rule (no em or en dashes, ever) was enforced
# across the registers under Austin's Path B ruling, and the separator became
# the middot the row already uses between its other fields. Accept BOTH, the
# same way the commitments heading regex above accepts both shapes: a parser
# that takes only the new one silently drops every row in any register copy
# that has not been cleaned yet, which is how 25 commitment rows vanished from
# the board on 2026-09-02.
PF_RE = re.compile(r"^- `(PF-\d{4})`\s+`?(\d+)d`?\s+\*\*([^*]+)\*\*\s*·\s*([^·]*)·\s*(.*?)\s*[—·]\s*(.*)$")
def parse_pf(relpath="60-Communities/open-items.md"):
    lines = io.open(os.path.join(VAULT, relpath), encoding="utf-8").read().split("\n")
    out, community = [], ""
    seen = set()
    for ln in lines:
        if ln.startswith("### "):
            # "### <community> — 29 open" became "### <community> · 29 open"
            # in the same 2026-09-03 pass. Split on either, or the count ends
            # up glued to the community name on every row in the section.
            community = re.split(r" — | · ", clean(ln[4:]))[0].strip()
            continue
        m = PF_RE.match(ln.strip())
        if not m:
            continue
        rid, age, state, cat, lot, rest = m.groups()
        if rid in seen: continue
        seen.add(rid)
        owner = ""; src = ""
        mo = re.search(r"\*\(owner:\s*([^;)]*)(?:;\s*([^)]*))?\)\*", rest)
        if mo:
            owner = clean(mo.group(1)); src = clean(mo.group(2) or "")
            rest = rest[:mo.start()].strip()
        rest = re.sub(r"\[source\]\(https?://[^)]*\)", "", rest).strip()
        url = ""
        mu = re.search(r"\((https?://[^\s)]+)\)", ln)   # scan the whole line: the link sits AFTER the owner block
        if mu: url = mu.group(1)
        out.append(dict(id=rid, reg="Property follow-ups",
                        sec=("Portfolio-wide and unattributed" if community.lower().startswith("portfolio") else community) or "Unfiled",
                        desc=clean(rest), notes="", owner_full=owner or "Unassigned", state=clean(state),
                        risk="", extra="", file=relpath,
                        community="" if community.lower().startswith("portfolio") else community,
                        age=int(age), lot=clean(lot) if lot.strip() not in ("-","") else "",
                        srcurl=url, srctype=src,
                        due=money_and_date(ln)[0], cost=money_and_date(ln)[1]))
    out += _parse_pf_tables(lines, relpath, seen)
    return out

# The property register carries rows in TWO shapes: the `- `PF-nnnn`` bullet list
# under `### Community` headings, and markdown tables in the sections appended by
# later sessions. Only the bullets were read until 2026-09-02, so `PF-0332` sat in
# the file and never appeared on the board - the same class of silent loss as
# `PD-01` to `PD-20`. This reads the tables too, keyed by their own header row.
_PF_TBL_MIN = {"community", "item"}
def _parse_pf_tables(lines, relpath, seen):
    import datetime as _dt
    today = _dt.date.today()
    out, hdr, idx = [], None, {}
    for ln in lines:
        t = ln.strip()
        if not t.startswith("|"):
            if t.startswith("#"):
                hdr = None
            continue
        # split on UNESCAPED pipes only: wiki links inside a table cell are
        # written `[[page\|Display]]`, and a naive split turns one cell into two,
        # which silently drops the row on the len(cells) != len(hdr) check.
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", t.strip("|"))]
        if all(set(c) <= set("-: ") for c in cells) and cells:
            continue
        low = [c.strip("*` ").lower() for c in cells]
        if _PF_TBL_MIN <= set(low):
            hdr, idx = cells, {n: i for i, n in enumerate(low)}
            continue
        if not hdr or len(cells) != len(hdr):
            continue
        raw = " ".join(cells)
        m = re.search(r"`(PF-\d{4})`", raw)
        if not m:
            continue
        rid = m.group(1)
        if rid in seen:
            continue
        seen.add(rid)
        get = lambda k: cells[idx[k]] if k in idx and idx[k] < len(cells) else ""
        comm_raw = get("community")
        mw = WIKI.search(comm_raw)
        comm = clean(mw.group(2) or mw.group(1).split("/")[-1].replace("-", " ").title()) if mw else clean(comm_raw)
        age = 0
        md = re.search(r"(\d{4})-(\d{2})-(\d{2})", get("found") or get("raised") or get("date"))
        if md:
            try:
                age = max((today - _dt.date(*map(int, md.groups()))).days, 0)
            except ValueError:
                age = 0
        desc = re.sub(r"^`PF-\d{4}`\s*", "", get("item")).strip()
        mu = re.search(r"\((https?://[^\s)]+)\)", get("item"))
        lot = get("lot")
        out.append(dict(id=rid, reg="Property follow-ups", sec=comm or "Unfiled",
                        desc=clean(desc), notes="",
                        owner_full=clean(get("owner")) or "Unassigned",
                        state=clean(get("state")) or "open", risk="", extra="",
                        file=relpath, community=comm, age=age,
                        lot=clean(lot) if lot.strip() not in ("-", "") else "",
                        srcurl=mu.group(1) if mu else "", srctype="",
                        due=money_and_date(raw)[0], cost=money_and_date(raw)[1]))
    return out

def build():
    rows = []
    rows += parse_commitments()
    rows += parse_table_register("00-Meta/parked-decisions.md", "Parked decisions", "PD")
    rows += parse_table_register("00-Meta/open-items.md", "Known problems", "KP")
    rows += parse_table_register("10-Business/eos/to-dos.md", "EOS to-dos", "TD")
    rows += parse_table_register("00-Meta/promises.md", "Promises", "PR")
    rows += parse_pf()
    for r in rows:
        r.setdefault("person", ""); r.setdefault("due", ""); r.setdefault("cost", "")
        r["category"] = categorise(r["desc"] + " " + r["extra"] + " " + r["sec"])
        r.pop("_pri", None)
        r["owner_short"] = owner_short(r["owner_full"])
        r["unowned"] = r["owner_short"] == "Unassigned"
        blob = " ".join([r.get("desc",""), r.get("notes",""), r.get("extra","")])
        oc, op = overrides(blob)
        r["priority"] = priority(r["reg"], r["risk"], r["state"], r["sec"], r["desc"])
        if r.get("_prio"): op = op or r.pop("_prio")
        PMAP = {"Open":"Open","Closed":"Closed","Blocked":"Blocked","Critical":"Critical (stated)",
                "High":"High (stated)"}
        if op: r["priority"] = PMAP.get(op, op)
        if oc: r["category"] = oc
        if r["reg"] == "Promises":
            r["category"] = "Promises"
            if (r["state"] or "").upper() == "VERIFY": r["priority"] = "Blocked"
        r["regurl"] = regurl(r["file"])
        if len(r["owner_full"]) > 200: r["owner_full"] = r["owner_full"][:200]
    return rows

if __name__ == "__main__":
    rows = build()
    import collections
    print("total", len(rows))
    print(collections.Counter(r["reg"] for r in rows))
    print(collections.Counter(r["priority"] for r in rows))
    print("unowned", sum(1 for r in rows if r["unowned"]))
    for rid in ("TD-0003","TD-0004","KP-0001","KP-0010","CM-07","PD-01","PF-0001","TD-0327"):
        for r in rows:
            if r["id"] == rid:
                print(rid, "|", r["desc"][:80], "|| owner:", r["owner_full"][:50], "|| pr:", r["priority"], "|| st:", r["state"][:40])
                break
        else: print(rid, "MISSING")
