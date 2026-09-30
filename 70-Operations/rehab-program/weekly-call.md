---
type: cadence
tags: [type/cadence, dept/construction, dept/accounting, status/active]
---

# The rehab cadence — two forums, not one

**What this is:** the reporting rhythm for [[70-Operations/rehab-program/overview]]. Built 2026-09-02 on Austin's instruction that rehab *"should also be a separate reporting and cadence."*

## The call that exists today

**Weekly Rehabs Call** — every **Wednesday 10:00 to 10:30 ET**, 30 minutes. Organiser **Jon Wyss**. `VERIFIED` from Austin's Outlook calendar 2026-09-02.

| Attendee | Seat |
|---|---|
| Jon Wyss | CIO, organiser |
| **Mark Doucette** | **High Pace Construction — the vendor** |
| John Clark | Director, Construction |
| Natalie Magurne | Director, Property Operations |
| Leslie Croft | Director, Sales & Marketing |
| Austin Berk | CEO |
| `cwigfall@parakeetcommunities.com` | **not in this Brain** — not on [[10-Business/people/staff-roster]] or the field roster. Same class of gap as `KP-0023`. |

**Two things about that list decide the whole cadence design.**

**The vendor is in the room.** Mark Doucette owns 64 rows in this Brain and 165 of the 219 units in the tracker. Having him on the call is right — it is the fastest path from a blocker to a crew. **But you cannot run a general-ledger reconciliation with your largest contractor listening.** The nine units where his tracker sits $163,123 above what Accounting has booked is a conversation to have *with* him; the question of whether $989,786 is stuck in a WIP account is not.

**Accounting is not in the room.** No Controller, no Moe Mehmood, nobody who touches an invoice. **A weekly call reviewing $1.3M of booked spend has no one present who can say what was booked.** That is the structural reason three cost figures disagree and nobody catches it: the people who hold the numbers are never in the same meeting.

> **So: two forums.** The Wednesday call stays operational and keeps High Pace in it. **A separate internal money review** — no vendor — carries WIP, invoices and the reconciliation. One 30-minute call cannot do both jobs, and trying to make it is how the money side has gone unexamined for as long as it has.

## Forum 1 — Weekly Rehabs Call, Wednesday 10:00 ET

**Purpose:** get work moving. Schedule, scope, approvals, blockers. **Not money.**
**Chair:** Jon Wyss. **Pre-call pack owner:** *to be set — see the decision below.*

**Standing agenda, 30 minutes, in this order.**

| Min | Item | Reads from |
|---|---|---|
| 0–3 | **The two board numbers.** Rehabs completed year to date against 100+. 60-day turn hit rate. | scorecard cut |
| 3–8 | **Past 60 days, unit by unit.** 18 units today. Each one gets a date or an escalation, not a status. | aging cut |
| 8–13 | **Approvals sitting.** What High Pace has priced and is waiting on. Oldest first. | approvals queue |
| 13–18 | **The 40 units with no start date.** $823,768 of scope that is not on the clock. Schedule or park, explicitly. | aging cut |
| 18–23 | **Unassigned work — 15 open units, $381,225.** Nobody is doing these. Assign or park. | vendor cut |
| 23–27 | **Completions to hand off.** Finished units that Leslie needs to list or Natalie needs to rent. | status cut |
| 27–30 | **Decisions Austin owes**, read out loud. | [[00-Meta/parked-decisions]] |

**Two rules on this agenda.** **Aging leads, not completions** — the completions are already good (85% under 60 days) and reading them first burns the half hour on the half that works. And **no unit is discussed twice without a date attached** — an item that appears three weeks running with a verbal update becomes a decision Austin rules on, not a fourth update.

## Forum 2 — Rehab money review, monthly, internal only

**Purpose:** WIP, invoices, and the reconciliation between three systems. **Does not exist today. This is the gap.**
**Proposed:** monthly, 45 minutes, in the week after close.
**Proposed attendance:** Austin, the Controller seat, Moe Mehmood, John Clark, Zach Schwartz. **No vendor.**
**Owner: unassigned** — the Controller seat is in transition ([[00-Meta/commitments]] item 16), so **Austin names an interim at the Friday 14:00 ET Executive EOS call** or this forum does not start.

**Standing agenda.**

1. **WIP roll-forward by vehicle** — opening, invoices in, internal labour, placed in service, written off, closing. The table at [[70-Operations/rehab-program/wip-and-invoice-model]]. **Every cell is currently a question mark.**
2. **Completed units still carrying WIP.** 56 units, $989,786. Belle Haven is $289,254 of it and is 17 of 18 complete — **it is the first one to clear.**
3. **Three-way tie-out.** GL against Rent Manager against the vendor tracker, per unit, with a named owner on every break. $274,178 apart today.
4. **Invoice aging** — received, coded, approved, paid. **Not captured anywhere today**, so this line starts as a build item and becomes a report once step 5 of the build sequence lands.
5. **Model against approved capital.** $4,198,591 modelled against $9,954,600 in the capex plan. Never once compared.
6. **Fund-level exposure**, for Jon and for LP reporting. JREFII is the one to watch — $195,142 out and $1,658,102 of modelled remaining.

## The pre-call pack

**Lands Tuesday by 17:00 ET**, so the call is spent deciding rather than reading. **One page, seven blocks**, in agenda order, off the same data the dashboard uses. Point-in-time by design and it says its own as-of date at the top, per [[CLAUDE]] rule on snapshots.

**What it must not do:** carry the modelled `expected` and `remaining` figures as if they were budget. They appear labelled **model** or they do not appear.

**It is scheduled, not remembered.** A recurring task fires **every Tuesday at 17:00 ET** (`trig_01MDcyYXyogo9xgQqWAxkTNq`, first run 2026-09-08) and builds the pack off the newest export in `data/`. It also checks whether a fresh tracker export has arrived; if one has, it files it under its own as-of date **without overwriting the previous one**, rebuilds the dashboard, and says which gaps closed and which widened since the prior export. **If no new export has arrived it says so and states how old the data is**, because a pack that silently reports three-week-old numbers as current is worse than no pack.

## Scorecard metrics this program should feed

John Clark's four scorecard KPIs are `Capex Spend vs. Budget · Project Completion Rate · In-Fill Homes Completed · Rehabs Completed`, and **none of them has a target or a tolerance band** (`KP-0004`, [[10-Business/eos/scorecard]]). **This program can now measure five things properly**, which is the first time any of them is scoreable:

| Metric | Today | Definition |
|---|---|---|
| Rehabs completed YTD | **77** | 2026 end date. Board goal 100+. |
| 60-day turn rate | **85%** | completed units with duration ≤60 days ÷ completed units with a duration |
| Units past 60 days open | **18** | of which 15 past 90 |
| Units with no start date | **40** | open, no start — not on the turn clock at all |
| Three-way cost variance | **$274,178** | highest of GL/RM/tracker minus lowest |

**Two of these are wins and should be reported as wins.** 77 against 100 with four months left, and an 85% turn rate against a board goal, are both on track. Austin's own rule — visible completed work is the antidote to the sense of standing still — applies to the department as much as to him.

## 2026-09-08 and 2026-09-15, two packs on stale data, and a day of the week to hold onto

**Added 2026-09-15 by the Page Update.** Both scheduled pre-call packs ran, at `70-Operations/rehab-program/pre-call-2026-09-08.md` and `pre-call-2026-09-15.md`, and **both ran on the 2026-08-28 export because no fresh tracker export has arrived by mail or Inbox since**; 11 days old on 09-08, 18 on 09-15, stated on each pack's face. The daily `donotreply@rentmanager.com` "test" and `EvictionTracker` mails are lease and eviction extracts, not this tracker. **So no gap on the reconciliation page can be said to have closed or widened**, because there is still only one export. The first scheduled run also could not reach this vault for two and a half hours on 2026-09-08 because the folder was not connected to the scheduled task.

**The call is Wednesday 10:00 to 10:30 ET and this page is right.** The 2026-09-08 close said *"Wednesday carries the Weekly Rehabs Call at 17:00 ET"* and the 2026-09-09 close said *"Thursday carries the Weekly Rehabs Call at 10:00 ET"*; both were wrong in one field, the first confusing the pack build time with the call and the second the day. The calendar series and the 2026-09-15 close (*"rehabs at 10:00"* for Wednesday 09-16) agree with this page. Recorded so no run moves the call on the strength of a close.

## 2026-09-02, the call as it actually ran

Filed in full at [[70-Operations/meetings/2026-09-02-weekly-rehab-call]]. **It confirms this page's standing finding rather than resolving it: the vendor was in the room, Operations chaired, both founders and the Director of Construction attended, and accounting was not there.** Three of the items raised were accounting items - the closed red rows retained for deposit purposes, the vendor's own *"convoluted"* skirting accounting, and whether a $20,000 Hunter Springs rehab is even Parakeet's to pay - and **none of them could be answered in the room.** `PD-25` is the open decision on whether this becomes two forums.
