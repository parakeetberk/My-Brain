# ClickUp — True State of Austin Berk's Open Work

Generated 2026-08-26. Read-only audit. Workspace `10598655` (Parakeet Communities). Austin Berk = user ID `4294267`.

Every claim below carries a confidence tag:
- **VERIFIED** — the task record itself was read (`get_task` / `get_task_comments`), timestamp confirmed
- **SINGLE-SOURCE** — appears in exactly one API response, not independently confirmed
- **INFERRED** — reasoned from a title, list name, or pattern

---

## VERDICT: PARTIAL — and the live part is not the part you'd guess

**ClickUp is not abandoned. It is the system of record for exactly one active project — the SharePoint Restructure 2026 migration — plus a weekly EOS meeting cadence and one live acquisition deal. Everything else is a graveyard.**

The premise that Austin moved *off* ClickUp *toward* Microsoft/SharePoint is backwards in an important way. He is running the SharePoint migration **inside ClickUp**. The two systems are not competing; ClickUp is the control plane for the SharePoint build-out.

### The dated evidence

Recency was measured by pulling every task ordered by `date_updated` descending and reading actual timestamps off the task records — not by reading status fields.

| Anchor | Task ID | Last activity | Confidence |
|---|---|---|---|
| Newest task in entire workspace | `868kwnn9w` (EOS-Weekly Executive) | **2026-08-25** (today) | VERIFIED |
| SharePoint Restructure, newest | `868krqzgz` (_Errors reconciliation) | **2026-08-24** | VERIFIED |
| Live acquisition deal, newest | `868k4n9k5` (Final DD Review) | **2026-08-24** | VERIFIED |
| **200th most-recently-updated task in the workspace** | `868kgcce4` (WIND-Maint Barn) | **2026-07-27** | VERIFIED |
| "CEO Operating System" folder task | `868jwx9yp` | **2026-06-03** (`date_created` == `date_updated` — never touched after creation) | VERIFIED |
| Property Asset Management space, newest of any task | `2dfnu4h` (Spectrum, Triple S) | **2022-07-21** | VERIFIED |

**The single most telling number: only ~200 tasks in the whole workspace have been touched in the last 30 days.** And a large share of those 200 are not human activity — they are the one-shot Home Infill "Asset Register" bulk import (several hundred records all created and last-updated within the same few seconds on 2026-07-27) and a triplicated month-end-close template expansion.

Strip those out and **genuine human activity in the last 30 days is concentrated in four places**.

### What is actually moving

| Space / Folder | Status | Evidence |
|---|---|---|
| **Command Center → SharePoint Restructure 2026** | **LIVE — the only real project** | 60 tasks created by Austin 2026-08-15→16; Albert Gano working them 2026-08-19→24; comment threads with real deliverables and exceptions. VERIFIED |
| **EOS → Weekly EOS Meetings** (esp. EOS-Weekly Executive) | **LIVE — meeting cadence** | `868kwnn9w` created + updated 2026-08-25. VERIFIED |
| **Deals Under Contract → "ClickUP Template – v2 (Claude)"** | **LIVE — a real deal, badly named** | `868k4n9k5` updated 2026-08-24, created by Alex Fals, 4 dependencies, 5 watchers. VERIFIED |
| **EOS → Property Operations Department L10** | **LIVE-ish — meeting list** | Multiple tasks in the top-100 by recency. SINGLE-SOURCE |
| **Geiger Key → RV Park / Restaurant Operations** | **Semi-live** | Tasks appear in top-100 workspace recency (e.g. `868ku1v2k` DBPR inspection, `868ku6j12` merch count). SINGLE-SOURCE |

### What is frozen

| Space / Folder | Last activity | Confidence |
|---|---|---|
| **Property Asset Management** (all 26 community lists: American, Bay Oaks, Congress, Everglades, Gulf Breeze, Hunter Springs, J Bar J, Lamberton Lake, Lake Saunders, Lake Wales, Lucky Clover, Mayflower, Oceanaire, Ormond Beach, Palm Haven, Palm Spring, Parktown, River Oaks, Royal Oaks, Royal Palm, Shady Oaks, Southgate, Town & Country, Tradewinds, Triple S, Whispering Pines) | **2022-07-21** — four years dead | VERIFIED |
| **Command Center → 🧠 CEO Operating System** (Daily CEO Dashboard, CEO Idea Drop, CEO To-Do, 2026 Priorities and Rocks, One on Ones, Prompt and AI Playbook, Department Pulse, Follow Ups) | **2026-06-03**, created and never revisited | VERIFIED for `868jwx9yp`; INFERRED for sibling lists |
| **Command Center → 🤖 AI, Automations & More** (13 lists) | No task appeared in the 200 most-recent | INFERRED |
| **Command Center → 🦜 Jhosua Saet 90-Day Onboarding** (4 lists) | No task appeared in the 200 most-recent | INFERRED |
| **Command Center → Rent Manager, Analytics & Reporting, Corporate, Home & Personal, Marketing** | No task appeared in the 200 most-recent; Austin's tasks there date 2023–2024 | VERIFIED for individual tasks below |
| **Standard Operating Procedures** space | **Could not see any lists** — hierarchy returned `children: []`. Not proof of emptiness. | UNKNOWN |
| **Miami Team EOS** space | **Could not see any lists** — hierarchy returned `children: []`. Not proof of emptiness. | UNKNOWN |

### Visibility caveats (read before acting)

1. **Two spaces returned no children** (Standard Operating Procedures `90110007420`, Miami Team EOS `90110676118`). I could not see inside them. They may hold content. **Do not treat them as empty.**
2. **A space exists that the hierarchy call did not list**: `90113731381` ("Shared with me"), discovered only because task `868gfh8vt` lives there. There may be other unlisted spaces.
3. **The `clickup_search` tool's sort is unreliable** when combined with a location filter — it returned 0 results for a space I had already confirmed holds tasks, and returned non-newest results when asked for newest. All recency claims above therefore rest on `filter_tasks order_by=updated` (verified descending) and direct `get_task` reads, not on search.
4. **"done" is not "closed" in this workspace.** Several lists use `done` / `completed` as custom statuses that the API still returns as open. Raw open/overdue counts overstate real work.

---

## 1. Austin's open tasks — 160 open, 26 that matter

`filter_tasks` on assignee `4294267` returned **171 tasks**; 11 carry a `done` status, leaving **~160 open**. Of those:

- **26** are SharePoint Restructure 2026 (the real work)
- **~16** are semi-live EOS / JotForm / Follow-Up items
- **~118 are dead scaffolding** — month-end-close checklist rows, Data Warehouse report stubs, blank "1st Draft / 2nd Draft / Roll Out" form-workflow placeholders, and 2023-era marketing bullet fragments ("Craigslist", "Facebook", "what is the cadence"). These are not tasks. They are the residue of abandoned list-building.

**Only 22 of Austin's open tasks carry a past due date.** Ordered by days overdue:

### ACUTE — the SharePoint critical path (this is where the leverage is)

| Task | ID | List | Due | Days | Last activity | Conf. |
|---|---|---|---|---|---|---|
| **[MON] Freeze _Errors and FolderOutput** — protect ~2,000 files that a 2022 Dropbox→SharePoint MOVE left as the *only* copy (recorded mortgages, UCC filings, title policies) | `868krqz9u` | W0 · Foundation | 2026-08-17 | **9** | 2026-08-19 | VERIFIED |
| **[AUSTIN] DECISION 0 — pick one property folder standard** (8 numbered vs 7 unnumbered) | `868krr105` | W0 · Foundation | 2026-08-21 | **5** | 2026-08-16 | VERIFIED |

- **Stakes on `868krqz9u`:** this is the highest-consequence item in the workspace. Albert has already applied the permission lock and posted screenshot evidence (2026-08-19). It sits unreviewed. **Suggested next action:** Austin verifies the three-entry permission set and closes it. **Owner:** Austin. **Urgency: ACUTE.**
- **Stakes on `868krr105`:** DECISION 0 blocks the naming canon, which blocks the metadata choice lists, which blocks the 68 per-community groups. Everything downstream is queued behind it. **Suggested next action:** pick one standard in writing. **Owner:** Austin. **Urgency: ACUTE.**

### SOON — dated this month, still live

| Task | ID | List | Due | Days | Last activity | Conf. |
|---|---|---|---|---|---|---|
| Create and tweak jot forms for better data input/reporting (with John Clark) | `868krk0nm` | EOS-Weekly Executive | 2026-08-21 | 5 | 2026-08-14 | VERIFIED |
| Making year end ROCKS! (with Jon Wyss) | `868k35mg9` | EOS-Weekly Executive | 2026-08-21 | 5 | SINGLE-SOURCE | SINGLE-SOURCE |

Both sit in status `off track` — self-declared, and consistent with the dates.

### SOON — one task not yet overdue but about to be, and strategically important

| Task | ID | List | Due | Last activity | Conf. |
|---|---|---|---|---|---|
| **Create a workflow effectively using SharePoint, Teams and ClickUp** | `868gfh8vt` | "Shared with me" (space `90113731381`) | **2026-09-01 — 6 days out** | 2026-04-13 | VERIFIED |

This is the task that settles the "are we leaving ClickUp?" question. Its description is a full written proposal defining SharePoint as document hub, Teams as comms, **RentManager as operational source of truth, and ClickUp as cross-departmental project management**. It has not been touched since April. **Stakes:** it is the only artifact stating the intended end-state tool architecture, and it comes due in a week. **Suggested next action:** Austin and Albert either ratify it or formally kill it. **Owner:** Austin + Albert Gano. **Urgency: SOON.**

### SCHEDULED — real work, long overdue, probably needs killing not doing

| Task | ID | List | Due | Days overdue | Conf. |
|---|---|---|---|---|---|
| **New Home walk-through checklist | `868jkv5z6` | JotForm To Do | 2026-05-11 | 107 | VERIFIED |
| Automated Ops Dashboard | `868j5bhfh` | EOS-Weekly RM & Integrations | 2026-05-28 | 90 | VERIFIED |
| PFG → JREF Agreement for Home Sales Entities | `868hwtmqb` | EOS-Weekly Finance | 2026-04-30 | 118 | VERIFIED |
| Standardize Rehab Tracker across vendors | `868j556tf` | EOS-Weekly Construction | 2026-04-27 | 121 | VERIFIED |
| Open JPM Accounts for Home Sales Entities | `868j67ua7` | EOS-Weekly Finance | 2026-04-13 | 135 | VERIFIED |
| CO Notification Email | `868j2900a` | EOS-Weekly Executive | 2026-04-07 | 141 | VERIFIED |
| Commission Calculator in RM | `868j3z465` | EOS-Weekly Inv/Mktg/Sales | 2026-04-04 | 144 | VERIFIED |
| Operations Asset Management Report | `2jvcpmc` | Report Batches | 2026-03-20 | 159 | VERIFIED |
| Cash Flow Projections | `868f3cx4u` | AB Comments, Thoughts, To Dos | 2026-02-19 | 188 | VERIFIED |
| Insurance Renewal Bid Package | `868f3dqe8` | AB Comments, Thoughts, To Dos | 2026-02-05 | 202 | VERIFIED |
| Mercedes (personal) | `868ch3h2t` | Personal | 2026-02-01 | 206 | VERIFIED |

**Two of these have real financial stakes** — `868hwtmqb` (PFG→JREF agreement) and `868j67ua7` (JPM accounts for the home-sales entities) are entity/banking infrastructure for a live business line, both ~4 months late, both still `on track` by status field. **Status field is lying; the dates are not.** Suggested owner for both: David Berman (he owns the adjacent Finance EOS items). Urgency: **SOON**, not scheduled — an unopened operating account for an active sales entity is a real problem.

### Beyond salvage — recommend bulk close, do not migrate

| Task | ID | Due | Days overdue |
|---|---|---|---|
| Eviction Workflow Reporting | `868by53hq` | 2025-01-17 | 586 |
| Review Outstanding Ramp Charges (+2 identical siblings) | `8689408qm` | 2024-07-31 | 756 |
| Finish Cash Flow Projection Report (with Zach) | `86875a8x3` | 2024-01-31 | 938 |
| Valley View / Knollwood | `2jvj0z2`, `2jvj0yn` | 2023-11-01 | 1029 |
| Review and Send | `8685axqfx` | 2023-09-15 | 1076 |
| Review and Send (duplicate) | `8684ux539` | 2023-07-15 | 1138 |
| Spectrum going onsite to meet with team | `2dfnu4h` | 2022-09-30 | **1426** |

Plus the **~118 undated scaffolding rows** described above. All VERIFIED as open with those due dates.

---

## 2. Delegation ledger — what Austin is waiting on

Retrieved via `search` filtered on `creators: [4294267]` with open statuses, sorted by update descending; pagination verified (page 2 was uniformly older, confirming true descending order).

**Austin created 60 open SharePoint Restructure tasks on 2026-08-15/16. 34 are assigned to Albert Gano. This is essentially his entire delegation ledger.**

### The live queue — Albert Gano, awaiting Austin

**15 tasks sit in status `to review`.** Albert has done the work and pushed them back; they are waiting on Austin, not on Albert. This is the single biggest bottleneck in the workspace.

| Task | ID | Due | Days late | Albert last touched | Conf. |
|---|---|---|---|---|---|
| [FRI] Create metadata columns and content types | `868krqzcf` | 2026-08-21 | 5 | **2026-08-21** | VERIFIED |
| [THU] Provision the 16 function groups | `868krr10g` | 2026-08-20 | 6 | **2026-08-21** | VERIFIED |
| [WED] Build seven areas and two libraries | `868krr3ez` | 2026-08-19 | 7 | 2026-08-19 | VERIFIED |
| [WED] Build the Archive library with retention labels | `868krqzbb` | 2026-08-19 | 7 | 2026-08-19 | VERIFIED |
| [WED] Build the Templates library | `868krqzbh` | 2026-08-19 | 7 | 2026-08-19 | VERIFIED |
| [TUE] Open FolderOutput in a sandboxed viewer | `868krqz9w` | 2026-08-18 | 8 | 2026-08-19 | VERIFIED |
| [MON] Tighten Buyers_Closing Files (317 MB consumer PII) | `868krr5ex` | 2026-08-17 | 9 | 2026-08-19 | VERIFIED |
| [MON] Restrict loose payroll files at Executive root | `868krqz9r` | 2026-08-17 | 9 | 2026-08-19 | VERIFIED |
| [MON] Restrict Harry & Lloyd / Personal Files | `868krqz9p` | 2026-08-17 | 9 | 2026-08-19 | VERIFIED |
| [MON] Pull permissions reports on top 10 exposures | `868krqzcm` | 2026-08-17 | 9 | 2026-08-19 | VERIFIED |
| [WEEK 2] Draft blanket policy rules for Austin to publish | `868krqzcy` | 2026-08-24 | 2 | **2026-08-24** | VERIFIED |
| _Errors reconciliation (joint Austin+Albert) | `868krqzgz` | 2026-10-08 | — | **2026-08-24** | VERIFIED |

**Read:** Albert is not the constraint. He worked through 2026-08-24 and is ahead of Austin. **Suggested next action:** one review pass clearing all 15. **Owner:** Austin. **Urgency: ACUTE.**

### Other delegations

| Task | ID | Owner | Due | Days late | Conf. |
|---|---|---|---|---|---|
| Get up standalone RV websites / Parakeet Retreats page | `868hwfv8k` | Leslie Croft | 2026-08-11 | 15 | VERIFIED (updated 2026-08-07) |
| Robust Sales & Leasing Reporting — CRM integration | `868hwfv7v` | Leslie Croft | 2026-06-30 | 57 | VERIFIED (updated 2026-08-04) |

Both status `off track`. Urgency: **SOON**.

### Unassigned work Austin created — nobody owns it

The **21 "July Close" tasks** (see §4) and the **~500 Home Infill Asset Register records** were all created by Austin with **zero assignees**. The Asset Register rows are data, not tasks, and should never have been tasks. The July Close rows are real process steps with no owner. **Urgency: SOON** for the close; **SCHEDULED** (bulk archive) for the register.

---

## 3. Unanswered comments — one blocking exception

Comments were read on the SharePoint Restructure review queue. The pattern: **Austin writes long, detailed work orders as comments; Albert replies with completion evidence; Austin does not respond.** Comment volume outside this project is effectively nil.

### The one that is actually blocking

**Task `868krr10g` — [THU] Provision the 16 function groups.** On **2026-08-21** Albert posted a formal exception (thread `90110261142044`, 3 replies) and Austin has not answered:

> Regional-Mgrs: 2 of 3 identified, 1 TBD · Construction-Team: John Clark only, additional reports unnamed · Offshore-Ops: 8 referenced, **none named** · Offshore-Fin: 5 referenced, **none named** · Offshore-AcqAM: 7 referenced, **none named** · Ops Administration: created empty

**21 people are unnamed across 6 SharePoint security groups.** Albert correctly refused to guess. Until Austin supplies the names, those groups are hollow — and the whole point of the exercise is that the wrong people must not get HR access. Austin's own work order flags this as "THE TRAP, AND IT IS A REAL ONE." **Suggested next action:** Austin supplies 21 names. **Owner:** Austin (likely needs Demetria Loukas / HR). **Urgency: ACUTE.** VERIFIED.

### Secondary

**Task `868krqzcf`** — Albert replied 2026-08-21: *"all columns and content types done and choices are empty. one exception added to the five lines."* The exception was raised; no acknowledgement from Austin. **Urgency: SOON.** VERIFIED.

**Task `868krqz9u`** — Albert replied 2026-08-19 with permission screenshots for both `_Errors` and `FolderOutput`. Awaiting Austin's verification. **Urgency: ACUTE** (see §1). VERIFIED.

*Scope note: comments were sampled across the active review queue, not read on all ~160 of Austin's tasks. The dormant spaces were not comment-swept — given they have had no activity since 2022–2026-06, unanswered questions there are moot.*

---

## 4. Overdue across the workspace — a process finding, not a task list

I verified **300+ open tasks with a 2026 due date already past** (paged three times through `filter_tasks`; more pages existed — treat 300 as a floor, not a total). Separately, the all-time overdue query returned a first page that was **almost entirely 2022 due dates** from the Property Asset Management space.

Before calling anything overdue I checked that the dates were real rather than bulk-import artifacts. They are: `868k4n9k5` (a representative "overdue"-status task) was created by Alex Fals on 2026-04-24, has 4 dependencies and 5 watchers, and was last updated 2026-08-24. These are genuine dates on genuinely tracked work.

**Three distinct failure modes, and only one is a real backlog:**

**(a) The 2022 fossil layer — Property Asset Management.** Roughly 100+ tasks across 26 community lists, due March–July 2022, sitting in `in progress` / `status update`. Nothing in that space has been updated since **2022-07-21**. These are not overdue tasks; they are an abandoned system. *This is the clearest illustration of why status fields cannot be trusted here — dozens read "in progress" and have for four years.*

**(b) Recurring tasks nobody closes — the loudest signal.**
- **`Capital One (Mayflower)` exists 20 times** in list `Asset Management` (`901103146982`), all subtasks of parent `AM Recurring Tasks` (`8687zycc5`). **19 Open, 1 done.** Instances span 2026-04 → 2026-08-19. VERIFIED — exact count confirmed by scoped search.
- The Asset Management list carries many more of the same shape (`Trash Overage Report`, `Prebill Summary Review`, `CapEx Report Refresh (every Tue & Thurs)`, `LC Home Listing Tracker (every T/TH)`, `Controllable Expense Tracker`), mostly assigned to Anna Maria Lapitan or unassigned, all Open and past due.

A recurrence generating 20 uncompleted instances means the recurrence is firing and no one is closing it. The overdue count here measures **automation, not human lateness.**

**(c) The live deal pipeline — genuinely behind.** List `ClickUP Template – v2 (Claude)` (space Deals Under Contract) holds ~40 tasks in a literal `overdue` status: Underwriting, Rent Roll, AR/AP, P&L Audit, Revenue Reconciliation, Environmental (ESA/Phase I), PZR, Survey, WWTP, Final DD Review, Final Budget Review, Milestones 3 and 4. Owners: Alex Fals, Alexander Stuart, Mark Anthony Vido, Kris Ruedas, Ma Jerna Pol, Austin Dixon. Due dates run 2026-06-05 → 2026-08-23; the list was updated **2026-08-24**.

**This is the one overdue cluster that is both real and current.** Austin is not assigned to any of it, but `868k4n9em` — *"Sign off to Jadian (Approval to Go Hard)"*, priority urgent, due 2026-08-25 — is unassigned and gates the deal. **Urgency: ACUTE for the deal team; SOON for Austin to confirm who signs.**

**The process finding:** overdue in this workspace does not mean "the team is late." It means (i) a dead space was never archived, (ii) recurrences run unattended, and (iii) one live pipeline is genuinely slipping. Treating these as one backlog would produce exactly the wrong response.

---

## 5. Duplicates and drift

**Triplicated month-end close — VERIFIED.** The list `Month End Close Process` (`901103857489`) contains **three complete copies** of the July 2026 close, all created by Austin, all unassigned, all Open:

| Series | IDs | Created |
|---|---|---|
| "July Close – Day 1…7 (Controller)" | `868kjjx2u` … `868kjjx58` | 2026-07-31 |
| "July 2026 Close — Day 1…7" | `868kj0r51` … `868kj0r77` | 2026-07-30 |
| "July 2026 Close – Day 1…7" | `868khmw7x` … `868khmwa8` | 2026-07-29 |

21 tasks for a 7-step process, distinguishable only by em-dash vs en-dash and a parenthetical role. Three attempts on three consecutive days to instantiate the same template. Days 1–7 are 12–22 days overdue (+1 day as of 2026-08-26). **Suggested next action:** keep one series, delete two, assign owners. **Owner:** David Berman (Controller). **Urgency: SOON.**

**20× Capital One (Mayflower)** — see §4(b). **Urgency: SOON** (fix the recurrence, bulk-close the instances).

**Duplicate month-end close *lists*** — `Month End Close Process` (`901103857489`) and `Month End Close Process Geiger` (`901103862963`) hold near-identical step names both assigned to Austin (Full Bank Reconciliation, Electronic Bank Reconciliations, Reconcile Intercompanies, Operational Review, Distribute Final Reports, Finalize Review…). SINGLE-SOURCE / INFERRED that these are redundant rather than genuinely separate entity closes — **verify before deleting.**

**Self-declared supersessions inside the live project — VERIFIED.** Three tasks Austin created carry `SUPERSEDED` in their own titles and are still open in the review queue: `868krqzae` (HR site), `868krqzak` (Finance site), `868krqzbv` (function groups). Low-effort cleanup that would shrink the review queue from 15 to 12.

### Drift: ClickUp vs SharePoint

There is **no true duplication of tracked work between ClickUp and SharePoint** — the SharePoint restructure is *tracked* in ClickUp and *executed* in SharePoint. That is a correct division, not drift.

The real drift is **naming and containment**:
- The live acquisition deal runs in a list named **"ClickUP Template – v2 (Claude)"** inside a folder named "DD Process." A live deal is executing inside something labelled a template. Anyone reasonably assumes it is disposable scaffolding. **This is the most dangerous naming problem in the workspace.** VERIFIED — the list is live (updated 2026-08-24) despite the name.
- A task exists in ClickUp titled **"Create SharePoint folder structure: HR / Executive 1-on-1s"** (`868jwx9yp`'s sibling `868jwx9vf`, CEO To-Do, due 2026-06-07) — SharePoint work stranded in the abandoned CEO folder while the live SharePoint project runs elsewhere. INFERRED that this is now covered by the W1 Corporate/HR migration tasks; **confirm before closing.**
- **Home Infill "Asset Register"** holds ~500 property records as ClickUp tasks with 127 custom fields each. This is a database in a task tracker. It duplicates what RentManager is designated to own per `868gfh8vt`. **Urgency: SCHEDULED** — migrate to RentManager or SharePoint, then archive.

---

## Recommendation: keep a scalpel, not the whole hospital

**Do not revive ClickUp wholesale, and do not shut it down.** Both would be wrong.

**Keep — these are live and working:**
1. **SharePoint Restructure 2026** — leave it exactly where it is through project close (GATE 6, 2026-12-31). It is well-structured, actively worked, and moving it mid-flight would be self-defeating. It is also, ironically, the thing building the system meant to replace this one.
2. **Weekly EOS Meetings** — a functioning meeting cadence with same-day activity.
3. **Deals Under Contract** — a live deal. **Rename the list immediately** so nobody mistakes it for a template.
4. **Geiger Key permits & operations** — regulatory dates with real consequences (DBPR inspection, FDEP lease renewal).

**Archive now — dead, and their presence is what makes the workspace look busy:**
- Property Asset Management space (26 lists, nothing since 2022-07-21) — export the ~100 open items to a spreadsheet for property-manager triage, then archive the space
- 🧠 CEO Operating System (8 lists, never used after 2026-06-03)
- 🤖 AI, Automations & More (13 lists), 🦜 Jhosua 90-Day Onboarding (4 lists)
- Rent Manager, Analytics & Reporting, Corporate, Home & Personal, Marketing folders
- ~118 of Austin's undated scaffolding rows
- Two of the three July Close series; 19 of the 20 Capital One instances

**Fix the recurrences before archiving anything** — otherwise `AM Recurring Tasks` will keep generating a 21st, 22nd, 23rd Capital One (Mayflower) into an archived list.

**Decide, within 6 days:** `868gfh8vt` comes due 2026-09-01 and is the only written statement of the target architecture. Ratify it — including its explicit role for ClickUp as cross-departmental project management — or kill it and say plainly what replaces ClickUp. Right now the org is running two systems without a decision, and this audit found the evidence for that in a task nobody has opened since April.

---

## The three things worth doing first

1. **Clear the 15-task review queue** (`868krqz9u` first — the `_Errors` freeze protecting ~2,000 irreplaceable legal documents). Albert is 7 days ahead of Austin and blocked. One sitting.
2. **Answer the function-groups exception on `868krr10g`** — name the 21 unnamed people across 6 SharePoint security groups. Everything about who can see HR files depends on it.
3. **Make DECISION 0** (`868krr105`) — pick the property folder standard. The naming canon, the metadata choice lists, and the 68 per-community groups are all queued behind it.

All three are Austin's, all three are ACUTE, and all three are single decisions rather than projects.
