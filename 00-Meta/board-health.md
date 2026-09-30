# Board health

**What this is:** the one page that says whether the six registers can be worked, as opposed to how many rows they hold. Built from the 2026-09-03 triage, which read all six registers in full and proposed a priority, an owner and an agent-ability call for every open row without editing a single one. **It is a hygiene page, not a register.** The rows themselves live in the six files.

**Status:** current, 2026-09-08, **corrected the same day.** The first version of this page repeated the triage's unowned figures without checking them against the registers, and they were stale by five days. **Corrected counts are below and the triage's own numbers are marked as the 2026-09-03 snapshot they are.** Two of the four defects it named are still live.

**Why the correction matters more than the numbers.** The triage read `board.json`, a parse taken before Austin's 2026-09-03 assignment pass. **A parse is a photograph; the register is the thing.** This page now counts the register files directly and says when it counted.

## The facts

- **The triage covered 1,183 board rows across six registers.** Nothing was held back and no ID was renumbered, merged away or recycled. Source reports are in `00-Meta/analysis/board-triage-2026-09-03/`.
- **The board carries 291 unassigned rows out of roughly 1,282, or 23%. VERIFIED by counting the six register files 2026-09-08.** The triage's 479 and 36% were the 2026-09-03 snapshot and are superseded.
- **Almost all of the improvement is one thing Austin did himself.** The property register now reads **19 unassigned of 482, or 4%.** On 2026-09-03 he assigned all 115 roadtrip rows off the regional coverage notes: **61 to Liz Santiago, 43 to Alex Pontes, 11 to Ashlyne Godinez**, exactly the split the triage had listed as unowned. **The mapping the triage recommended asking Natalie for had already been made.**
- **The to-do register is now where the whole problem lives: 239 unassigned of 612, or 39%.** Every other register is in reasonable shape. Known problems 26 of 102, parked decisions 7 of 46, property follow-ups 19 of 482, promises and commitments none. **Promises reading 58% unowned in the triage does not survive contact with the file**, which is the clearest sign the snapshot had aged.
- **One week of one road trip produced 162 of the unowned rows as of 2026-09-03**, and the 150 still sitting in the to-do register are the remainder of it. The 2026-08-18 to 08-24 southeast tour. A walk-through captures the problem and the place; **nothing in the capture step forces a name**, and the register has no field that refuses a row without one.
- **The regional-coverage pattern was real and it is closed.** Rows that named a region and not a person were the largest unowned block on the board, and **one pass off the coverage notes cleared all 115 of them.** That is the pattern worth remembering: **when a register already knows the answer, assignment is a reading exercise, not a decision.**
- **An unowned row generates no pressure.** Only 127 of the 479 carry an age and only 5 carry a due date. **A row with no owner and no date cannot be late, and something that cannot be late does not get worked.** That is the accumulation mechanism in one sentence.
- **It is not duplication.** Only 2 of the 479 share their opening sixty characters with another unowned row. These are distinct pieces of work.
- **42% of the to-do register is noise**, and 150 of those 215 rows are the tour field block. The register's own `TD-0459` says so and recommends handing the block to Property Operations.
- **97 open to-do rows are `AGENT NOW`.** Retrieval, reconciliation, list-building and monitoring against sources this Brain can already read. Another 140 are agent work with a human check, many gated on a connector rather than on judgement.
- **Only 5 of the 144 rows in the three corporate registers have a real external clock on them.** Almost every date on the board is one Austin set himself. **The hardest genuine deadline was not on any of those rows**: it sat inside a commitment, as a counterparty's own corporate filing date.
- **P0 is 43 of those same 144, which is not a credible distribution**, and the reason is the finding: 21 of the 29 P0 known problems fall into two clusters, one on the fund and legacy tenant, one on compliance and SOP text.

## The four defects, and where each stands

**1. Duplicate IDs. FIXED 2026-09-03.** Four `TD` IDs existed twice on different rows, the second recurrence of a defect `TD-0476` and `KP-0060` were opened for the day before. **The second set was renumbered to `TD-0530` through `TD-0533`, each row carrying its own former ID in the text.** That is the right fix, because it leaves the collision auditable rather than silently resolved.

**2. Work still routed to a departing person. LIVE, and it is now the top item on this page.** 14 open to-do rows still name David Berman as owner, plus 7 in known problems, 6 in commitments, 5 in property follow-ups and 1 parked decision. **Three of the to-do rows are the only route to something time-bound**: a state regulatory notice on a fund in wind-down, a lender inventory confirmation, and the file-by-file resolution of a subscription folder that a books-and-records demand reaches. **Nothing new should go to him and these need re-seating before they go quiet.**

**3. The 150-row field block. LIVE.** Still sitting in the to-do register, still the single largest source of noise on the board, still with a `PF` twin for almost every row that is being maintained separately.

**4. The 45 unreadable rows.** A table-shape problem in two files plus a parser that gives up on them. **Cheapest thing on this page to fix and it moves the headline number by four points.**

## The six orphan functions

**This is worth more than any individual row.** An orphan function is a cluster of unowned items that all need the same kind of person, where no such person exists. Six are on this board, and each is a hiring or engagement finding rather than a task.

1. **Corporate secretary and entity compliance. Nobody, and not one row routes here.** Small in row count, large in consequence: a registered agent past due three consecutive months, an entity put in "Impending Not in Good Standing" over an annual filing, an unread state regulatory notice. **An entity falling out of good standing produces no ticket. It produces a letter, to an address, that somebody may or may not open**, so the row count is the count of notices that happened to be seen. **Needs a named owner plus a calendar, not a seat.** Roughly 115 entities, so it is a real recurring obligation.
2. **Insurance and risk. A broker relationship with no internal counterpart.** **A broker sells and places cover. A broker does not notice that you stopped being covered.** Needs a named internal counterpart with a renewal calendar and a schedule of insured assets, **which is the same calendar as item 1 and should be one build.**
3. **Utilities and permits.** Explicitly moved out of accounting to a destination that was never named.
4. **Construction QA and install inspection. The largest cluster at 149 unowned rows**, and the audit role inside it is ownerless by name in `PD-32`. **The honest recommendation here is not a hire**: make QA a contractual condition of payment audited by the vendor, because that is a contract amendment and a QA lead is a quarter.
5. **Business systems analyst and data steward, and the function is currently Austin.** 77 unowned rows, 17 of them in known problems, the highest concentration of critical findings on the board. **`00-Meta/austin-operating-manual.md` already carries the diagnosis in his own words. The 77 rows are what that sentence looks like as a backlog.** Second strongest hiring case, largest opportunity cost, because the alternative is his calendar.
6. **Fund administration and investor relations. One person plus an outside accountant**, and these are the rows with statutory dates. **Engagement of a fund administrator is faster than hiring and the deadline is real.**

## What this page asks for

Two things, and the property mapping is off this list because it is done.

1. **Hand the 150-row field block to Property Operations**, per `TD-0459`, and stop maintaining it twice. **This is now the cheapest move on the board**: it is 63% of every unassigned row left, and the register's own row already recommends it. **The property assignment pass is the precedent**, because it proves the block can be cleared by reading coverage rather than by deciding anything.
2. **Re-seat the Berman rows**, starting with the three that are the only route to a dated obligation: the state regulatory notice on a fund in wind-down, the lender inventory confirmation, and the subscription-folder resolution a books-and-records demand reaches.

## Related

- [[00-Meta/open-board]]. The enumerated board itself, and the parser this page's defect 4 is about.

## Sources

- [[00-Meta/analysis/board-triage-2026-09-03/decision-queue-and-orphans]]. The 39 decision briefs and the unowned analysis, including the six orphan functions.
- [[00-Meta/analysis/board-triage-2026-09-03/td-triage]]. 514 open to-do rows triaged, and the duplicate-ID finding.
- `00-Meta/analysis/board-triage-2026-09-03/pf-triage.md`. All 465 property rows.
- `00-Meta/analysis/board-triage-2026-09-03/kp-pr-cm-triage.md`. The 144 rows of the three corporate registers.
- The six register files, counted directly 2026-09-08. **Where this page and the triage disagree, the register wins.**
