# Migration rulings — Austin, 2026-09-03

**What this is:** the decisions that govern the reconciliation of the retired Claude Code vault (`C:\Users\AustinBerk\Documents\Claude\Code\brain\`) into this Brain. Ruled by Austin on 2026-09-03. Any session or agent working the migration applies these rather than re-opening them.

**Status:** current. Five rulings, all VERIFIED against Austin's own words in session.

---

## 1. Unit count — this Brain's figure wins

**The ruling stands. The conflict as I first stated it was wrong, and the correction matters more than the ruling.**

**What I claimed, 2026-09-03:** that `Claude\Code\brain\04-index\portfolio-baseline.md` reports 6,635 units across 66 records.

**What is actually true. VERIFIED by grep across the entire old vault.** Neither figure is in that file. `6,635` returns **one hit and it is a substring**: line 301, `| Mar-26 | 78.25% | 7,336 | 46,635 |`, under the header `| Month | NOI margin | Utilities expense | Utility reimbursements |`. **That is $46,635 of utility reimbursement revenue.** `"66 records"` returns nothing at all. The file's own record counts are 82, 104, 134, 67 and 71. What it actually reports is **9,355 raw and 8,020 de-duplicated**, with its own instruction to `Use 8,020 / 77.67%`.

**Where 6,635 really came from.** It was **my own arithmetic**, computed live in a chat session on 2026-08-30 when the operating basis was recomputed against Austin's inclusion rules, and published in the *First Honest Count* artifact. **It was never written into any vault file.** Attributing it to a named page was the failure hard rule 3 exists to prevent, committed while writing the rule that cites hard rule 3.

**The real gap, and it is already tracked.** **6,379 governed against 8,020 warehouse de-duplicated, 1,641 units wide.** Registered as `KP-0010`, `KP-0025 C1` and `TD-0004`, with a reconciliation workbook against it. This was never an OLD-versus-NEW conflict; it is an open internal reconciliation.

**Ruling, unchanged.** `My Brain\CLAUDE.md`'s **67 active communities and 6,379 core units** is authoritative. `00-Meta\numbers-ledger.md` and `60-Communities\portfolio.md` already agree with it and with each other: the components add exactly (5,293 + 950 + 136), `portfolio.md` carries exactly 67 data rows, and the ledger already isolates the warehouse figures in a separate `Portfolio actuals` section with as-of dates and an explicit non-reconciliation note.

**How to apply it.** Nothing to edit. **The requirement was already satisfied before this ruling was written.** Any warehouse figure that surfaces later carries its as-of and its method, labelled SINGLE-SOURCE per rule 10, and never stands as the unit count.

---

## 2. The old constitution is superseded wholesale

**Conflict.** `Claude\Code\brain\CLAUDE.md` carries a **three-item ceiling**. Rule 12 of this Brain replaced that on 2026-09-01 with "show everything, highlight three," and records what the ceiling cost: a $250,000 lender reserve decision, a direct question from Leslie on a vendor partnership, a one-word yes Jon was waiting on, and an overdue month-end task, all held back in a single day.

**Ruling.** The old constitution does not merge. It is **archived as the artefact that rules 10, 11 and 15 came out of**, and nothing in it overrides a rule in this Brain.

**How to apply it.** File it to `99-Archive\` with a note naming which of its rules were adopted here and which were replaced. Do not copy any of its rules forward without checking them against `My Brain\CLAUDE.md` first.

---

## 3. Parked decisions map onto existing PD IDs

**Conflict.** `Claude\Code\brain\05-decisions\parked-decisions-register.md` holds **19 rows with no IDs**. `My Brain\00-Meta\parked-decisions.md` holds **PD-01 to PD-29**.

**Ruling.** Map the 19 onto the PD IDs they already correspond to. Anything genuinely new takes **the next number in sequence**, per rule 15. Never renumber and never recycle.

**How to apply it.** Produce the mapping as a table before writing anything. A row that cannot be matched to an existing PD is a candidate for a new ID, not an automatic one; some of the 19 will already be closed.

---

## 4. Nothing migrates before a dash pass

**Conflict.** This Brain's voice rule is absolute: **no em dashes or en dashes, ever.** Every file in the old vault uses them heavily.

**Ruling.** No file migrates as-is. Dashes are cleaned on the way in.

**How to apply it.** Rewrite the sentence rather than swapping the character. An em dash usually marks a clause that should be its own sentence or sit inside commas. A find-and-replace to a hyphen produces prose that reads wrong, which is the thing the rule exists to prevent.

---

## 5. Karen Doner is outside counsel, not a personnel matter

**Question raised.** `Claude\Code\brain\02-entities\karen-doner.md` (5.4KB) had no context attached and was provisionally flagged as possibly falling under rule 7.

**Austin, 2026-09-03:** *"Karen Doner is Parakeet and affiliates employment attorney."*

**Ruling.** She is **outside counsel**. The page belongs in `10-Business\outside-help\`, linked from `10-Business\MOC-Business.md`. **Rule 7 does not apply to the page itself** — she is a vendor relationship, not an employee.

**The nuance that does still bite.** She is an *employment* attorney, so the *matters* she advises on will frequently be personnel matters under rule 7. The page about her is open; specific employee matters she has handled stay in `10-Business\people\_private-assessments.md` or their own `_private-` file, never on her page.

---

## Related

- `My Brain\CLAUDE.md` — the constitution these rulings sit under
- `My Brain\00-Meta\id-conventions.md` — the ID scheme ruling 3 depends on
- `05-Inbox\vault-reconciliation\` — the three-part reconciliation report these rulings govern
