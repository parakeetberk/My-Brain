---
type: program
tags: [type/program, dept/construction, dept/accounting, status/active]
---

# The rehab program

**What this is:** the single page for the rehab and infill turn program — the work, the money, and the cadence that reviews both. Built 2026-09-02 on Austin's instruction: *"this also should be a separate reporting and cadence as it should also update everything with invoices coming in and out wip accounts plus anything else to make sure we can analyze from any angle."*

**Status:** current, 2026-09-15. Data still as of **2026-08-28**, 219 unit rows: no fresh export has arrived through 2026-09-15, and the two September pre-call packs say so (see `70-Operations/rehab-program/weekly-call`). **The tracker's own collection design was filed 2026-09-08** and is the section headed "Where the tracker's fields come from" below.

**Dashboard:** `https://claude.ai/code/artifact/34a291f1-59a7-4d4b-952c-3bf5404eaa87` — the five scorecard metrics, both board goals, the WIP split by fund, the nine reconciliation gaps as collapsible unit lists, and all 219 units filterable by status, fund, community, vendor, tier, age band, category or defect. **Rebuildable from `build/make_data.py` and `build/assemble.py`**, not hand-assembled. All 28 published figures were re-derived from the CSV by re-running the builder and diffed against what shipped.

**Why it is one program and not four findings.** Rehab touches Construction (does the work), Accounting (books the invoice), Asset Management (owns the return), and Property Operations (rents or sells the finished home). Every reconciliation gap on this page lives in the seam between two of them. Split into four department pages it becomes four people each holding a quarter of a problem. One program, one weekly forum, one set of numbers.

**Owner:** **unassigned — Austin to name at the Friday 14:00 ET Executive EOS call.** The work is John Clark's. The money is the Controller's, and that seat is in transition ([[00-Meta/commitments]] item 16). **Nobody owns the reconciliation between them today, which is the whole reason the three cost figures disagree.**

## Related pages

- [[70-Operations/rehab-program/wip-and-invoice-model]] — how a rehab dollar moves, and where it currently gets lost
- [[70-Operations/rehab-program/weekly-call]] — the Wednesday 10:00 ET cadence, agenda and pre-call pack
- [[70-Operations/rehab-program/reconciliation-2026-08-28]] — every gap in this pull, unit by unit
- [[10-Business/departments/construction]] · [[10-Business/eos/scorecard]] · [[60-Communities/open-items]]
- [[70-Operations/rehab-program/ledger-cost-analysis-2026-09-16]] — the fourth system: the RentViewer warehouse queried directly on 2026-09-16, and why it cannot see rehab capital at all. Added 2026-09-22.

## The data contract — read this before quoting any number off this program

**Three systems hold a rehab cost and none of them is authoritative.**

| Source | Field in the export | Total, 219 rows | What it actually is |
|---|---|---|---|
| Rent Manager UDF | `cost` / `typed` | **$1,169,997** | what ops typed on the issue. **132 of 219 rows carry the literal string `IN PROGRESS` instead of a number**, and 12 carry `NONE`. Only **75 rows have a real typed cost.** |
| General ledger | `glActual` | **$1,338,235** | what Accounting booked. The closest thing to truth, and 30 to 45 days in arrears ([[00-Meta/open-items]] `KP-0003`). |
| Vendor tracker | `trackerCost` | **$1,064,057** | what High Pace's own sheet says. A point-in-time export of a live shared sheet, per [[CLAUDE]] rule on snapshots. |

**$274,178 between the highest and the lowest.** **VERIFIED** against `data/rehab_tracker_all_data_2026-08-28.csv`.

**`expected` and `remaining` are models, not budgets.** `expected` is back-solved from tier averages — `External · L3 (n=6)` means six comparable jobs. **27 of 219 rows use a flat `portfolio avg (n=75)`** because they have no tier at all. So:

> **The $4,198,591 "expected" and $2,833,406 "remaining" are statistical projections off as few as six comps. They are not approved capital and must never be quoted to Jon, an LP, or a lender as a forecast.** `INFERRED`.

**The approved capital number lives elsewhere** — the CapEx Overview workbook, $9,954,600 across 169 line items ([[10-Business/departments/construction]]). **Reconciling the rehab model against the capex plan has never been done** and is the largest single hole in this program.
**Fourth system, added 2026-09-22.** The RentViewer warehouse was queried on 2026-09-16 and does not agree with any of the three sources above, because it cannot see the rehab capital accounts at all; the POH and REO operating accounts it does carry are turnover consumables and must never be quoted as rehab spend. Detail and figures on [[70-Operations/rehab-program/ledger-cost-analysis-2026-09-16]]; Jon's 2026-09-21 WIP figures are on the WIP page and in the ledger.

## Where the tracker's fields come from, and the title workflow nobody has on a page

**Filed 2026-09-08 from the request workbook that built this tracker**, `70-Operations/rehab-program/data/Rehab Tracker - Working Copy 7-26-26.xlsx`, prepared 2026-06-13 and last saved 2026-09-03. **It is the outbound version, the one sent out to be filled in, which is why it explains the data contract above better than the export does.**

**Two tabs, two owners, and the colour is the assignment.** `Mark` holds the 159 in-house homes; `Alt Vendor` holds 23 that are all John's. **182 active assets at preparation**, against the 219 in the 2026-08-28 export. Amber cells are Mark's to fill, magenta are John's, teal are pre-filled from signed capex and rehab documents and invoices and are marked **verify**, and light green is an assumption rather than a fact: **completion auto-computed as start plus 45 days, to be overwritten when the real date is known.**

**So a completion date on this tracker may be a formula, not a report from site.** That is the same class of defect as the three cost columns, and it explains part of the reconciliation gap rather than sitting beside it.

**The two identifiers are different things and get confused.** `GL #` is the Rent Manager accounting code for the cost. `ISSUE #` is the construction job and ClickUp number. **Final cost per home is only recoverable through the `ISSUE #`, and only once every one is filled**, which is the workbook's own stated roadmap rather than a live capability.

### The missing-title workflow, and it is on no other page in this Brain

**52 homes carry a title status of "START missing-title" with Melanie named as the owner.** Title status in the workbook is pulled from Rent Manager and a second column flags the action.

**The design intent is the part worth keeping:** when a rehab **starts**, the missing-title work begins in parallel, so the title is in hand at completion and the home can actually be sold. **A finished rehab with no title is not a sellable asset**, which makes this a revenue gate on the whole program and not a records chore.

**This is a different matter from the nine Royal Oaks titles in `CM-19`**, which is a dispute with a named counterparty. **These 52 are a process, and nothing in this Brain currently tracks whether it runs.**

### What the workbook says is deferred

Before and after photo links per home, title-status integration tying rehab completion to a sellable titled asset, cost tracking through the `ISSUE #`, handoff-date tracking of how fast rehabs are assigned and turned, and estimated budget against final cost with permit and demo flags. **All named as roadmap by the workbook itself, none of them live.**

## The single biggest finding: 37 rows came in through a different door

**Four things looked like four data problems. They are one cohort, and the partition is perfect.**

**37 of 219 rows carry a unit-code prefix in the community field instead of a community name** — `TO`, `PARK`, `RW`, `FOX`, `SILVER`, `BRUN`, `ROYAL`, `RO`, `DO`, `SH`, `SOUTH`, `TC`, `BOVIIPO`, `BOVIPO`, `WPMH`, `HARB`, `GULFPO`, `NGMH`, `LS`, `PPH`, `Central`, and one row with no community at all.

**Those same 37 rows are, exactly, every defective row in the file.**

| Defect | Count in the file | How many are in this cohort |
|---|---|---|
| Not in the vendor tracker | 36 | **36 — all of them** |
| No WIP / GL code on the issue | 28 | **28 — all of them** |
| No vendor assigned | 19 | 16 |
| Untiered, so priced off a portfolio average | 82 | 36 of the 37 |

**The other 182 rows have zero of these defects.** Not one is missing a WIP code. Not one is absent from the vendor tracker. `VERIFIED`.

**So this is not data quality drifting. It is a second intake path that was never onboarded.** The cohort is **16 internal Parakeet Ops jobs and 16 unassigned units** — work the field did itself or work nobody was given — keyed by unit code, untiered, uncoded, and invisible to the vendor sheet the weekly call reads from. **$386,175 of modelled scope and $19,374 of booked spend live in it.**

**Why this matters more than any single number on this page.** Every by-community rollup double-counts, because `TO` and `The Oaks` are the same place and so are `PARK`/`Parkwood`, `RW`/`Riverwalk`, `FOX`/`Fox Creek`, `SILVER`/`Silver Breeze`, `BRUN`/`Brunswick Estates`, `BOVIIPO`/`Bay Oaks Village II`. And **the internal track has no cost discipline at all** — no tier, no code, no vendor record — which is precisely the work that never gets invoiced and therefore never gets questioned.

**Three codes cannot be resolved from anything in this Brain — `NGMH`, `LS`, `PPH`.** They are not guessed.

**One fix, not four.** The cohort needs an intake standard: a community from the master list, a tier, a WIP code, and a vendor record even when the vendor is us. **`KP-0037` already records that no master community list exists across the 13 JotForm forms, and every FastField cascade and QuickBase relationship field keys off it.** This is the same defect surfacing in a third system — the argument for fixing it once at source rather than mapping it per report. See [[15-Projects/fastfield-phase-i/overview]].

## Where the program actually stands against the board goals

**Two 2026 board goals run through this program**, both from the March deck ([[10-Business/eos/scorecard]]).

**"COMPLETE 100+ REHABS ACROSS THE PORTFOLIOS."** **77 completed with a 2026 end date** as of 08-28. Monthly: Jan 7 · Feb 5 · Mar 8 · Apr 9 · May 9 · Jun 9 · Jul 14 · **Aug 16**. **The run rate is accelerating and the goal will be met** — 9.6/month against four months left puts the year around 115. **This is the one number on this program that is good news, and nobody is reporting it.** `VERIFIED`.

**"Turn any vacated home for sale or lease in under 60 days."** Of 67 completed rehabs with a measurable duration: **57 came in at or under 60 days, median 31 days.** That is an 85% hit rate and it is genuinely strong. **The failure is not in the completions, it is in the tail:** **18 open units are past 60 days and 15 are past 90.** `VERIFIED`.

**John Clark's Q1 rock — "complete all rehabs backlogged as of 3/31" — is two units from done, five months late.** `SOUTH-86` (Southgate, started 2025-11-25, **274 days**, High Pace) and `BRUN-203` (Brunswick Estates, started 2025-12-19, **250 days**, Primary Home Repair). **Everything else from that backlog has closed.** Two units close a rock. `VERIFIED`.

## The nine angles this program gets analysed from

Austin asked to be able to *"analyze from any angle."* These are the cuts, and each one has to hold on its own or the number is wrong.

| Angle | Cut by | What it answers | Blocked by |
|---|---|---|---|
| **Money reconciliation** | GL vs Rent Manager vs vendor tracker, per unit | which of three numbers is right | nothing — runs today |
| **WIP** | vehicle → community → unit, opening/additions/transfers/closing | what is capitalisable and what should have rolled out | **no roll-forward exists** — see [[70-Operations/rehab-program/wip-and-invoice-model]] |
| **Invoice flow** | invoice in → coded → approved → paid, by vendor | where an invoice sits and how long it has sat | **not captured anywhere today** |
| **Vehicle / fund** | JREFI · JREFII · Origins · Kippy | fund-level capex exposure, for Jon and for LP reporting | community mapping |
| **Community** | 67 communities | which properties are absorbing spend | **name mapping is broken** — 20 rows |
| **Vendor** | High Pace · Primary Home Repair · Jams + Stark · A New Day · Parakeet Ops · Unassigned | concentration and per-vendor cost per unit | nothing |
| **Tier / scope** | L1 · L2 · L3 · Full Gut · Untiered · N/A | whether tier predicts cost, which is what makes `expected` trustworthy | **82 rows are Untiered** |
| **Aging** | days open, banded 0-30 / 31-60 / 61-90 / 90+ | the 60-day board goal, unit by unit | nothing |
| **Status integrity** | date and flag validation | rows the data itself says are wrong | nothing |

**Five of nine run today. Four are blocked, and three of those four are blocked on the same thing — nothing captures the invoice.**

## Vendor concentration

| Vendor | Units | Open | Vendor tracker cost |
|---|---|---|---|
| **High Pace** | **165** | **105** | $740,192 |
| Parakeet Ops (internal) | 16 | 3 | — |
| Primary Home Repair | 10 | 7 | $159,460 |
| Jams + Stark | 6 | 3 | $68,814 |
| A New Day Construction | 3 | 0 | $95,590 |
| **Unassigned** | **19** | **15** | — |

**High Pace holds 75% of the units and 79% of open work.** That is a single point of failure on a board-goal program, and it is also why the vendor tracker is treated as a third system of record — one vendor's spreadsheet is effectively the company's rehab schedule. **19 units have no vendor at all**, 15 of them open, which means $381K of modelled scope with nobody assigned to do it. `VERIFIED`.

## Fund exposure

| Vehicle | Units | Open | GL booked | Vendor tracker | GL − tracker | Modelled remaining |
|---|---|---|---|---|---|---|
| JREFI | 61 | 25 | $642,939 | $650,192 | −$7,253 | $477,970 |
| **JREFII** | **119** | **75** | $609,007 | $413,864 | **+$195,142** | **$1,658,102** |
| Origins | 22 | 19 | $53,760 | $0 | +$53,760 | $475,692 |
| Kippy | 16 | 14 | $32,530 | $0 | +$32,530 | $221,642 |

**JREFI reconciles to within 1%. JREFII is off by $195,142, and Origins and Kippy have no vendor tracker coverage at all** — $86,290 of GL spend against zero vendor records. **That is not a rounding problem, it is two funds running outside the tracker.** `VERIFIED`.

**JREFII also carries the Responsible Contractor Policy question** — `KP-0014` asks whether that policy applies at 50%+ ownership, which points at JREFII's 22 properties. **The fund with the worst reconciliation is the fund with the contractor-audit obligation.** Worth knowing before the 2026-09-30 audit date.

## Live from the 2026-09-02 rehab call

**Pushed here 2026-09-02 from [[70-Operations/meetings/2026-09-02-weekly-rehab-call]].** The pages in this folder were built the same morning from a **2026-08-28 tracker export**; this section is what the vendor said on the call a week later, and where the two disagree the call is newer.

**The crew map, which the tracker does not carry at all.** Silver Breeze finishes all rehabs **2026-09-10** and then splits into three crews. Silver Hill SC started 09-02, two level-one units, a few days. Parkwood SC follows, materials and a Conex trailer dropping 09-02 and 09-03, mostly level one so it moves fast. Fox Creek starts the following week, **siding-only homes first** so they can be listed. Vero takes a crew off Silver Breeze. Santa Rosa and Panama City already started. Applegate has two units left after 208, 335 and 240, then the crew moves to Oceanair in New Smyrna with a new crew joining in two weeks. **Hunter Springs takes priority over Lake Wales**, and **Lake Wales is paused.** Crystal Acres is on hold and **is Kippy's responsibility, not ours** - see `KP-0055`.

**The tracker's own owner says the tracker is broken.** On the call the vendor asked for someone to fix *"the formulas that I've blown up and all the bad spacing"* and said *"the numbering needs to be redone."* **This matters for every figure on these four pages**, because they were derived from an export of that sheet. `KP-0056`, `TD-0450`. **One convention must survive the fix: the closed red rows stay**, because money was moved between them and the vendor still has accounting to square against them. A cleanup that tidies them away destroys a reconciliation trail.

**A new scope rule was agreed and it is not in the SOP.** While a rehab is in progress the crew now checks **HVAC, hot water heater, roof and, as far as possible, windows.** The vendor named the limit himself: it cannot be caught during leveling, and a roof leak is often only findable while it is raining. `TD-0448`.

**Two capex questions came out of the call rather than out of the tracker.** Fox Creek started with 120 rentals and has a heavy AC repair run with replacements coming due on large package units at two to two and a half tons; **priced as one bulk decision across rehab homes and occupied rentals it is a capex decision, not twenty repairs.** Against that, the vendor's Silver Breeze alternative is **roughly $3,500 installed for two one-ton mini splits** plus tankless water heaters, which he rates highly and also flags as unproven over time. `TD-0449`. **Neither figure is in `00-Meta/numbers-ledger.md`**: both are prices quoted out loud on a call.

## Live-data rebuild, 2026-10-20

**Austin asked on 10-20 to get arms around every rehab (completed, in progress, upcoming, needed), tie out all costs, and push inventory ready.** Rebuilt off live sources, replacing the 08-28 snapshot.

- **Sources:** live High Pace tracker on SharePoint (`Operations/_Operations Report/rehab 2026/High Pace rehab tracker/Rehab Tracker - Working Copy 7-26-26.xlsx`, modified 10-20); Rent Manager API General Ledger, accrual, 2025-01-01 to 2026-10-20, all 638 accounts under 16400 Work in Process; Rent Manager Asset Listing active and inactive; Ramp spend by GL category.
- **The 09-16 "ledger cannot see rehab capital" finding is superseded.** That was the RentViewer warehouse. Rent Manager's own GL report reads every unit WIP account. `VERIFIED`.
- **Pipeline:** 64 completed in 2026 (47 with a tracker end date, 17 complete with no date), 72 in progress, 38 upcoming, 11 cleaned out only, 46 active homes RM marks Needs Rehab with no tracker row.
- **Money:** $1,997,896 rehab GL spend since 1/1/25 against $1,522,491 on the tracker. 61 of 73 completed units still carry $1,272,793 in WIP; only 10 placed in service. 36 in-progress units show only the $3,500 deposit. Silver Breeze GL is ~$92K behind the tracker. Ramp holds only $71,531 coded to WIP; $2,177,106 of Ramp spend is Uncategorized.
- **Inventory push:** 6 finished homes still Needs Rehab in RM, 8 finished with title issues, 9 For Sale in RM but In Progress on the tracker.
- **Not yet tied:** High Pace invoice by invoice. Draft to Mark asks for his open-invoice list.
- Data: `data/rehab_tieout_2026-10-20.csv`, `data/needs_rehab_not_tracked_2026-10-20.csv`. Board: `build/rehab-board-2026-10-20.html`, published to the dashboard artifact.
- Drafts in Austin's Outlook (not sent): to Natalie and Moe cc John, Leslie, Jon; to Mark cc Natalie.

## Job costing replaces per-unit WIP accounts, decided 2026-10-21

- **Austin: "We are a go."** Job costing replaces the 638 per-unit WIP sub-accounts under 16400, rehabs first, then infill, then community capex.
- **Adobe kickoff and closeout forms go away** and move into the forms module in the React Parakeet Birdcage. Birdcage generates the job ID; the display name is a scripted template.
- **Rent Manager carries a job ID** and the API can pull it (Austin, 10-21). The open risk is the RentViewer warehouse loading it; Dan is looking into it.
- Rollout plan: Claude Doc "Rehab Job Costing Rollout", https://claude.ai/artifact/Rb76DTs5ou9iPGGzC6z7FE
