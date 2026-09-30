# The open board

**What this is:** every open item from all five registers on one page, enumerated rather than summarised. Built 2026-09-01 when Austin asked where the 723 items were on the morning brief, and the answer was nowhere.

**Status:** current - 2026-09-02, rebuilt again the same afternoon. **892 rows.** Rebuilt after Austin's second working pass and after three other sessions added rows overnight (`KP-0037` to `KP-0039`, `PD-21` to `PD-23`, `TD-0368` to `TD-0396`). Every row carries a permanent reference ID written into its register file - see [[00-Meta/id-conventions]] and [[CLAUDE]] rule 15.

**Dashboard:** `https://claude.ai/code/artifact/de27b6c8-cbac-4342-a5cc-32e0598f6144` - collapsible by register and sub-section, **multi-select** filters on priority, category, community and owner, a **commented-only** toggle, full-text search, and **a comment thread on every row**. See the section below.

**The rebuild, and why it matters more than the row count.** Austin, 2026-09-01: *"on TD-0003 through 0006 the layout doesn't let us see anything. Looks like their is a mapping issue,"* then *"the same issue is in TD-0007 through TD-0009 and TD-0001 & TD-0002 as well as TD-0011."*

- **The cause.** The first build read every markdown table by a **fixed column order**. The eleven priority-queue rows in [[10-Business/eos/to-dos]] have six columns (`# | Item | Owner | Why it is here | Where | Status`) and every other table has five. So the priority marker landed in the description - which is why those rows read *"P1"*, *"P2"* - and the item text was pushed into the owner column.
- **The same defect was doing worse damage where nobody was looking.** The `Needs action now` table in [[00-Meta/open-items]] is `Finding | Risk | Owner | Status`, so **every `KP-` row on the old board showed its owner as "Critical" or "High"** and the real owners were never displayed at all. Austin found the visible symptom; the invisible one was bigger.
- **The fix is structural, not a patch.** The parser now reads **every table by its own header row**, so a six-column table and a five-column table both map correctly and a future table with a new column will too.
- **A second finding came out of the rebuild.** [[00-Meta/audit-log]] records that all 738 rows had IDs *written into the register files*. Twenty had not: `PD-01` to `PD-20` existed only in the board's own output and [[00-Meta/parked-decisions]] carried none. They vanished from the rebuild, which is how it was caught. **They are written into the file now.**
- **The build is now a script in the vault** rather than a thing assembled by hand: `00-Meta/board-data/builder/`. Run `VAULT="$HOME/mnt/My Brain" python3 build_board.py`. **A dashboard that cannot be regenerated is a screenshot**, and a hand-assembled one is where a mapping defect survives four hundred rows without anyone noticing.
- **One number was overstated and is corrected here.** The audit log says 10 rows carry a real source link. A parse of the registers finds **2** - `PF-0199` and `PF-0324`. The other eight were resolved in conversation and never written back.

**Rebuilt 2026-09-02 afternoon: the rehab program's 33 rows added, and a second silent-loss defect fixed.** `KP-0040` to `KP-0048`, `TD-0405` to `TD-0420`, `PD-24` to `PD-26`, `PF-0333` to `PF-0337` - see [[70-Operations/rehab-program/overview]].

- **`PF-0332` had never been on this board.** An earlier session wrote it into [[60-Communities/open-items]] as a **markdown table row**, and the property parser read only the `- \`PF-nnnn\`` bullet format. The row sat in the file, correctly ID'd, and was invisible. **This is `PD-01` to `PD-20` repeating in a different register**, and it is the second time in two days that checking whether a write landed caught something that trusting it would have missed.
- **The fix is structural, not a reformat.** The register genuinely carries two shapes - bullets under `### Community` headings, and tables in the sections later sessions appended - so rewriting the five new rows as bullets would have hidden the defect instead of fixing it. `_parse_pf_tables()` now reads those tables by their own header row, the same rule that fixed the 2026-09-01 mapping bug.
- **A second bug surfaced one minute behind the first.** The row splitter split on every `|`, including the **escaped pipe inside a wiki link**, so `[[page\|Display]]` turned one cell into two and the row was dropped on the column-count check. Caught only because `PF-0337` vanished after a purely cosmetic edit to its link. Split is now on unescaped pipes only.
- **The pre-rebuild pull ran and was verified rather than assumed.** `comments.json`, `edits.json` and `flags.json` came back md5-identical to the vault copies, so nothing had been saved on the page since the morning pull - but the pull is not skippable even when it is almost certainly unnecessary, because the cost of skipping is unrecoverable and the cost of checking is one command. Snapshots at `00-Meta/board-data/builder/_prepull/`.
- **Four comments read as `open` and were left alone.** All four are Claude replies on `CM-19`, `PD-06` and `PD-16`. A reply never counts as an open comment, because it is not something Austin owes anyone.

## Commenting on a row, and the one rule that protects it

**Added 2026-09-01 evening on Austin's instruction.** Every row now carries a **Comment** button beside Copy search. It opens the item in full with its register notes and a **date-stamped comment history**, and takes a new note.

**Three states, all visible in the popup.**

| State | Where it lives | What it means |
|---|---|---|
| **pending** | Austin's browser only (`localStorage`) | typed, not yet saved. Lost if he clears site data. |
| **open** | inside the published page | saved. Survives reload, visible to anyone with the link, waiting on Claude. |
| **actioned** | inside the published page | written into its register. Kept visible for the audit trail, never deleted. |

**Save to the page** republishes the board with the comments baked in. **Copy open comments** puts every unactioned note on the clipboard as `KP-0001: text`, one line per row, to paste into chat. **That paste is the channel that reaches Claude** — a cloud session cannot be woken by a republish or a comment, confirmed by trying to register a watch on 2026-09-01 and being refused. So the page is the memory and the clipboard is the messenger.

### What can be changed on a row

| Thing | How | Lands as |
|---|---|---|
| Comment | Comment button, date stamped | `KP-0001: text` |
| Priority, category, community, owner | click the value, pick from the list | `TD-0044: Community -> Riverwalk (was blank)` |
| **Due date** | click the `+ due` chip, date picker. Overdue goes red | `TD-0021: Due date -> 2026-09-15` |
| **Est. cost** | click the `+ cost` chip, type a figure | `TD-0021: Est. cost -> $4,500` |
| Budget-week flag | the `BW` box on the left | `TD-0044: FLAG Budget week` |

**All five ride the same Save and the same Copy**, and all five carry pending, open and actioned.

### Claude replies in the thread

**Ask for a draft in a comment and it comes back on the same row.** *"Draft an email to Melanie about the Royal Oaks titles"* on `CM-19`, sent over, and the draft lands in that row's comment history with a **copy** button. Worked example on `CM-19` as of 2026-09-01.

- A reply is marked `Claude` rather than pending, open or actioned. **It never counts as an open comment and never lands on the clipboard with them**, because a reply is not something Austin owes anyone.
- **This is where drafts live now.** The Microsoft 365 connector is read-only in this session (`KP-0002`), so nothing can be put in Outlook. The row is the next best place: it keeps the draft next to the thing it is about instead of scrolling away in a chat.

**THE RULE, and it is the whole risk of this feature.** The comment history exists **only inside the published page**. There is no copy in this vault. So:

> **Before every rebuild, pull the comments out of the live page.** `python3 pull_comments.py live.html comments.json`, then rebuild. `build_board.py` picks `comments.json` up automatically and carries the history through untouched. **Skipping that step destroys every comment Austin has saved, silently, and there is nothing to restore from.**

After writing a row's comments into its register, mark them done rather than deleting them: `python3 pull_comments.py live.html comments.json --action KP-0010 TD-0004`.

**How the page rewrites itself.** It carries a base64 copy of its own template with two markers, one for that template and one for the data. Saving decodes the template, puts the same base64 back and the new data in, and publishes. The template is a fixed point — only the data ever changes — which was verified across three generated versions before shipping.

**Data:** `00-Meta/board-data/open-board-2026-09-01.json` - regenerated by the builder, not edited by hand.

## The figures, 2026-09-01 (rebuild)

| Register | Rows | Unowned |
|---|---|---|
| [[00-Meta/commitments]] | 25 | 3 |
| [[00-Meta/parked-decisions]] | 20 | 20 - the register has no owner column; every row awaits Austin |
| [[00-Meta/open-items]] | 36 | 18 |
| [[10-Business/eos/to-dos]] | 342 | 178 |
| [[60-Communities/open-items]] | 331 | 4 |
| **Total** | **858** | **283** |

*Unowned counts exclude closed rows. Parsed from the registers by `00-Meta/board-data/builder/`, not restated from any page's own headline.*

**737 are open; 17 are marked closed and kept visible.** 44 are either stated-critical or awaiting Austin's ruling.

**These figures supersede the 738 / 206 published this morning, and the difference is not growth.** 16 rows were added by the day's dispositions (`TD-0327` to `TD-0342`), 20 are the parked decisions that were missing entirely, and the rest is the corrected parse: the known-problems register now reads 36 rather than 24 because the old parse merged rows, and the unowned count moved because `KP-` owners were previously being read as risk ratings. **A count that changes when the parser is fixed was never a count of the work; it was a count of what the parser could see.**

## How each field was derived

- **Owner, age, state, category** come from the register that holds the row wherever it states them. The property register states all four, which is why its rows are the richest and why exactly one of its 331 reads unassigned - matching that page's own note, which is the check that validated the parse.
- **Category** is inferred from the text where the register states none. **123 rows resist inference and sit in `Uncategorised`** rather than being forced into a bucket.
- **Priority is the source's own signal, never invented.** `Critical` means the page itself ranks it critical or Tier 1. `High` means it sits in the priority queue. `Awaiting your ruling` is the parked-decisions register. Everything else reads `Open`.
- **Age exists only where the source recorded one.** Most corporate rows have none.

## What the first run exposed

**The five registers overlap, against what [[CLAUDE]] asserts.** Filtering to Lucky Clover returns the armed-resident incident three times - [[00-Meta/commitments]] item 7, a `Needs action now` row in [[00-Meta/open-items]], and Tier 1 of the EOS queue. CLAUDE.md says "Five registers, and they do not overlap." In practice the same finding was routed into three as it escalated. So **726 is a row count, not a count of distinct problems.** Open question for Austin: does the five-register rule need a dedup convention, or is cross-register presence a deliberate escalation signal worth keeping?

## Related

- [[00-Meta/delegation-board]] - the same data read for delegation rather than enumeration
- [[CLAUDE]] rule 12 - show everything, highlight three
