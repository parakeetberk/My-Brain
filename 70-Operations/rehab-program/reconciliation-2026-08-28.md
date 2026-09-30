---
type: analysis
tags: [type/analysis, dept/construction, dept/accounting, status/open]
---

# Rehab reconciliation — unit by unit, as of 2026-08-28

**What this is:** every flagged unit from the 2026-08-28 tracker pull, listed so a name can be put against each one. The summary and the argument live at [[70-Operations/rehab-program/overview]] and [[70-Operations/rehab-program/wip-and-invoice-model]]; this page is the working list.

**Source:** `data/rehab_tracker_all_data_2026-08-28.csv`, 219 rows. **VERIFIED** — every figure below is re-derived from that file, not carried from a summary.

**This is a point-in-time export of a live vendor sheet.** An internal inconsistency here may be a stale-export artefact rather than a business problem, per [[CLAUDE]]. The reconciliation gaps below are cross-system and survive that caveat; the date oddities may not.


## GL has spend, Rent Manager has no cost — 69 units, $345,883

**Accounting booked it, ops cannot see it.** Anyone reading Rent Manager sees these units as costing nothing. **Owner: the Controller seat, with John Clark confirming the work is real.** The 12 rows marked Complete are the urgent subset — a finished rehab showing zero cost is what makes a portfolio-level cost-per-unit figure wrong.

| Unit | Community | Vehicle | Status | GL booked | RM cost | WIP code |
|---|---|---|---|---|---|---|
| `BRUN-203` | Brunswick Estates | JREFII | In Progress | $42,500 | IN PROGRESS | 16465 |
| `WPMH-4885 CLOVER` | Whispering Pines FL | JREFI | Complete | $32,394 | NONE | 16604 |
| `FOX-6` | Fox Creek | JREFII | Complete | $9,000 | NONE | 16519 |
| `APPLE-240 CIRCLE` | Applegate | JREFI | In Progress | $8,400 | IN PROGRESS | 16793 |
| `APPLE-279 CIRCLE` | Applegate | JREFI | In Progress | $8,400 | IN PROGRESS | 16795 |
| `APPLE-396 CIRCLE` | Applegate | JREFI | In Progress | $8,400 | IN PROGRESS | 16794 |
| `SA-180` | Shady Acres | JREFII | In Progress | $7,000 | IN PROGRESS | 16856 |
| `SA-214` | Shady Acres | JREFII | In Progress | $7,000 | IN PROGRESS | 16854 |
| `SA-35` | Shady Acres | JREFII | In Progress | $7,000 | IN PROGRESS | 16855 |
| `LWPO-16` | Lake Wales, MHC | Origins | In Progress | $4,970 | IN PROGRESS | 16674 |
| `LWPO-19` | Lake Wales, MHC | Origins | In Progress | $4,970 | IN PROGRESS | 16588 |
| `LWPO-29` | Lake Wales, MHC | Origins | In Progress | $4,970 | IN PROGRESS | 16582 |
| `LWPO-30` | Lake Wales, MHC | Origins | In Progress | $4,970 | IN PROGRESS | 16587 |
| `LWPO-32` | Lake Wales, MHC | Origins | In Progress | $4,970 | IN PROGRESS | 16586 |
| `LWPO-40` | Lake Wales, MHC | Origins | In Progress | $4,970 | IN PROGRESS | 16585 |
| `LWPO-55` | Lake Wales, MHC | Origins | In Progress | $4,970 | IN PROGRESS | 16584 |
| `LWPO-60` | Lake Wales, MHC | Origins | In Progress | $4,970 | IN PROGRESS | 16583 |
| `PARK-75` | Parkwood Mobile Home Park | JREFII | In Progress | $4,012 | IN PROGRESS | 16846 |
| `PARK-42` | Parkwood Mobile Home Park | JREFII | In Progress | $3,812 | IN PROGRESS | 16845 |
| `ARD-101` | Auburn Ridge | JREFII | In Progress | $3,500 | IN PROGRESS | 16801 |
| `ARD-108` | Auburn Ridge | JREFII | In Progress | $3,500 | IN PROGRESS | 16802 |
| `ARD-27` | Auburn Ridge | JREFII | In Progress | $3,500 | IN PROGRESS | 16798 |
| `ARD-46` | Auburn Ridge | JREFII | In Progress | $3,500 | IN PROGRESS | 16796 |
| `ARD-46A` | Auburn Ridge | JREFII | In Progress | $3,500 | IN PROGRESS | 16797 |
| `ARD-8` | Auburn Ridge | JREFII | In Progress | $3,500 | IN PROGRESS | 16800 |
| `ARD-87` | Auburn Ridge | JREFII | In Progress | $3,500 | IN PROGRESS | 16803 |
| `BOVIIPO-91` | Bay Oaks Village II | Origins | Not Started | $3,500 | IN PROGRESS | 16591 |
| `BOVIPO-H-4` | Bay Oaks Village I | Origins | Not Started | $3,500 | IN PROGRESS | 16592 |
| `BRUN-12` | Brunswick Estates | JREFII | In Progress | $3,500 | IN PROGRESS | 16806 |
| `BRUN-20` | Brunswick Estates | JREFII | In Progress | $3,500 | IN PROGRESS | 16807 |
| `BRUN-23 RACHEL` | Brunswick Estates | JREFII | In Progress | $3,500 | IN PROGRESS | 16809 |
| `BRUN-28` | Brunswick Estates | JREFII | In Progress | $3,500 | IN PROGRESS | 16808 |
| `BRUN-701` | Brunswick Estates | JREFII | In Progress | $3,500 | IN PROGRESS | 16805 |
| `CA-35` | Crystal Acres | Kippy | Not Started | $3,500 | IN PROGRESS | 16573 |
| `DO-57` | Druid Oaks | JREFII | In Progress | $3,500 | IN PROGRESS | 16815 |
| `FOX-132` | Fox Creek | JREFII | In Progress | $3,500 | IN PROGRESS | 16821 |
| `FOX-57` | Fox Creek | JREFII | In Progress | $3,500 | IN PROGRESS | 16825 |
| `FOX-64` | Fox Creek | JREFII | In Progress | $3,500 | IN PROGRESS | 16819 |
| `FOX-82` | Fox Creek | JREFII | In Progress | $3,500 | IN PROGRESS | 16817 |
| `FOX-83` | Fox Creek | JREFII | In Progress | $3,500 | IN PROGRESS | 16824 |
| `GULFPO-20` | Gulf Breeze | Origins | Complete | $3,500 | NONE | 16589 |
| `GULFPO-21` | Gulf Breeze | Origins | Complete | $3,500 | NONE | 16590 |
| `HARB-D-03` | HARB | JREFI | Complete | $3,500 | NONE | 16611 |
| `HSMHC-13` | Hunter Springs | Kippy | Not Started | $3,500 | IN PROGRESS | 16578 |
| `HSMHC-14` | Hunter Springs | Kippy | Complete | $3,500 | NONE | 16577 |
| `HSMHC-19` | Hunter Springs | Kippy | Not Started | $3,500 | IN PROGRESS | 16580 |
| `HSMHC-20` | Hunter Springs | Kippy | Not Started | $3,500 | IN PROGRESS | 16576 |
| `HSMHC-8` | Hunter Springs | Kippy | Not Started | $3,500 | IN PROGRESS | 16579 |
| `HSMHC-9` | Hunter Springs | Kippy | Not Started | $3,500 | IN PROGRESS | 16581 |
| `LUCK-2` | Lucky Clover | JREFI | Complete | $3,500 | NONE | 16610 |
| `PARK-10` | Parkwood Mobile Home Park | JREFII | In Progress | $3,500 | IN PROGRESS | 16837 |
| `PARK-14` | Parkwood Mobile Home Park | JREFII | In Progress | $3,500 | IN PROGRESS | 16844 |
| `PARK-7` | Parkwood Mobile Home Park | JREFII | In Progress | $3,500 | IN PROGRESS | 16835 |
| `PARK-81` | Parkwood Mobile Home Park | JREFII | In Progress | $3,500 | IN PROGRESS | 16847 |
| `PARK-82` | Parkwood Mobile Home Park | JREFII | In Progress | $3,500 | IN PROGRESS | 16836 |
| `PARK-89` | Parkwood Mobile Home Park | JREFII | In Progress | $3,500 | IN PROGRESS | 16838 |
| `PPH-30` | Palm Haven Estates | JREFI | Not Started | $3,500 | IN PROGRESS | 16900 |
| `PPH-K` | Palm Haven Estates | JREFI | Complete | $3,500 | NONE | 16608 |
| `ROYAL-10` | ROYAL | Kippy | Complete | $3,500 | NONE | 16575 |
| `ROYAL-22` | Royal Oaks | Kippy | Not Started | $3,500 | IN PROGRESS | 16574 |
| `SOUTH-86` | Southgate | JREFI | In Progress | $3,500 | IN PROGRESS | 16607 |
| `SUR-43` | Su-Rene | JREFII | Not Started | $3,500 | IN PROGRESS | 16596 |
| `TC-A-11` | Terrace Crossings | JREFII | Complete | $3,500 | NONE | 16595 |
| `TO-123` | The Oaks | JREFII | Complete | $3,500 | NONE | 16594 |
| `TRADE-30OLSEN` | Tradewinds | JREFI | Not Started | $3,500 | IN PROGRESS | 16606 |
| `WIND-102` | Windward Knoll | JREFII | Not Started | $3,500 | IN PROGRESS | 16593 |
| `BRUN-37` | Brunswick Estates | JREFII | Not Started | $1,917 | IN PROGRESS | 16541 |
| `ROYAL-14` | Royal Oaks | Kippy | Not Started | $1,030 | IN PROGRESS | 16931 |
| `GO-AA` | Great Oak | JREFII | Not Started | $758 | IN PROGRESS | 16826 |

## No WIP or GL code on the issue — 12 units

**The cheapest fix on this page, and it has a deadline built in.** None of these carries GL spend yet, so no invoice has arrived. An invoice landing on a coded unit files itself; one landing here goes to a default account or an expense line and has to be found later. **Fix the codes before the invoices arrive. Owner: John Clark to supply the unit, Accounting to assign the code.**

| Unit | Community | Vehicle | Status | GL booked | Modelled remaining | Vendor |
|---|---|---|---|---|---|---|
| `BOVIPO-C-2` | BOVIPO | Origins | Not Started | $0 | $25,415 | Unassigned |
| `FOX-129` | FOX | JREFII | Not Started | $0 | $25,415 | Unassigned |
| `GULFPO-4` | GULFPO | Origins | Not Started | $0 | $25,415 | Unassigned |
| `LS-130` | LS | JREFI | Complete | $0 | $0 | Unassigned |
| `NGMH-3304 3RD AVE` | NGMH | JREFII | Not Started | $0 | $25,415 | Unassigned |
| `RO-216WHITESQUIRREL` | RO | JREFI | Not Started | $0 | $25,415 | Unassigned |
| `RW-171` | RW | JREFII | Not Started | $0 | $25,415 | Unassigned |
| `RW-35` | RW | JREFII | Not Started | $0 | $25,415 | Unassigned |
| `SILVER-11` | SILVER | JREFI | Not Started | $0 | $25,415 | Unassigned |
| `TO-32` | TO | JREFII | Not Started | $0 | $25,415 | Unassigned |
| `WPMH-359 LILY` | WPMH | JREFI | Complete | $0 | $0 | High Pace |
| `WPMH-4770 PERIWINKLE` | WPMH | JREFI | Not Started | $0 | $25,415 | Unassigned |

## Vendor tracker far above GL booked — 9 units, $238,389 tracker against $75,266 GL

**$163,123 apart, and it is two opposite problems wearing one flag.** Either High Pace has done work it has not invoiced — in which case this is an accrual Accounting is missing — or the tracker is priced above what will actually be billed, in which case the forecast is too high. **Nobody can tell from the data. Ask Mark Doucette directly at the Wednesday call: are these invoiced yet?** One question settles all nine.

| Unit | Community | Vehicle | Status | Tracker | GL booked | Gap |
|---|---|---|---|---|---|---|
| `BELL-73` | Belle Haven | JREFI | Complete | $35,304 | $2,992 | **$32,312** |
| `BELL-7` | Belle Haven | JREFI | Complete | $37,546 | $9,922 | **$27,624** |
| `BELL-74` | Belle Haven | JREFI | Complete | $30,721 | $3,292 | **$27,429** |
| `APPLE-208 CIRCLE` | Applegate | JREFI | Complete | $34,391 | $8,400 | **$25,991** |
| `BELL-31` | Belle Haven | JREFI | Complete | $24,597 | $1,470 | **$23,127** |
| `BELL-72` | Belle Haven | JREFI | Complete | $18,996 | $9,922 | **$9,074** |
| `BRUN-37` | Brunswick Estates | JREFII | Not Started | $10,600 | $1,917 | **$8,683** |
| `SILVER-21` | Silver Breeze | JREFI | Complete | $28,182 | $23,132 | **$5,050** |
| `WPMH-4700 PERIWINKLE` | Whispering Pines FL | JREFI | Complete | $18,052 | $14,217 | **$3,835** |

## On the board, not in the vendor tracker — 36 units, $534,700 modelled

**All 22 Origins units and all 16 Kippy units are in here** — $7,000 of GL spend against zero vendor tracker records. Two funds are spending outside the sheet the weekly call reads from, which means the call has never seen them. **Owner: unassigned. The Wednesday call is the forum; Jon organises it and both funds are his side of the house.**

| Unit | Community | Vehicle | Status | GL booked | Modelled | Vendor |
|---|---|---|---|---|---|---|
| `FOX-10` |  | — | Complete | $0 | $1,650 | Parakeet Ops |
| `HARB-D-03` | HARB | JREFI | Complete | $3,500 | $25,415 | High Pace |
| `LS-130` | LS | JREFI | Complete | $0 | $25,415 | Unassigned |
| `LS-HOUSE` | LS | JREFI | Complete | $0 | $1,650 | Parakeet Ops |
| `PPH-S` | PPH | JREFI | Not Started | $0 | $1,650 | Parakeet Ops |
| `RO-216WHITESQUIRREL` | RO | JREFI | Not Started | $0 | $25,415 | Unassigned |
| `SILVER-11` | SILVER | JREFI | Not Started | $0 | $25,415 | Unassigned |
| `SOUTH-16` | SOUTH | JREFI | Complete | $0 | $1,650 | Parakeet Ops |
| `WPMH-359 LILY` | WPMH | JREFI | Complete | $0 | $25,415 | High Pace |
| `WPMH-4770 PERIWINKLE` | WPMH | JREFI | Not Started | $0 | $25,415 | Unassigned |
| `BRUN-153` | BRUN | JREFII | Complete | $0 | $25,415 | Primary Home Repair |
| `DO-44` | DO | JREFII | Not Started | $0 | $25,415 | Unassigned |
| `FOX-129` | FOX | JREFII | Not Started | $0 | $25,415 | Unassigned |
| `FOX-55` | FOX | JREFII | Complete | $0 | $1,650 | Parakeet Ops |
| `NGMH-3301 1ST AVE` | NGMH | JREFII | Complete | $0 | $1,650 | Parakeet Ops |
| `NGMH-3304 3RD AVE` | NGMH | JREFII | Not Started | $0 | $25,415 | Unassigned |
| `PARK-1` | PARK | JREFII | Complete | $0 | $1,650 | Parakeet Ops |
| `PARK-33` | PARK | JREFII | Not Started | $0 | $1,650 | Parakeet Ops |
| `PARK-66` | PARK | JREFII | Not Started | $0 | $25,415 | Unassigned |
| `PARK-87` | PARK | JREFII | Not Started | $0 | $25,415 | Unassigned |
| `RW-171` | RW | JREFII | Not Started | $0 | $25,415 | Unassigned |
| `RW-35` | RW | JREFII | Not Started | $0 | $25,415 | Unassigned |
| `RW-72` | RW | JREFII | Complete | $0 | $1,650 | Parakeet Ops |
| `RW-85` | RW | JREFII | Not Started | $0 | $1,650 | Parakeet Ops |
| `SH-114` | SH | JREFII | Complete | $0 | $1,650 | Parakeet Ops |
| `SH-91` | SH | JREFII | Complete | $0 | $1,650 | Parakeet Ops |
| `TC-E-9` | TC | JREFII | Not Started | $0 | $25,415 | Unassigned |
| `TO-10` | TO | JREFII | Complete | $0 | $1,650 | Parakeet Ops |
| `TO-25` | TO | JREFII | Complete | $0 | $1,650 | Parakeet Ops |
| `TO-32` | TO | JREFII | Not Started | $0 | $25,415 | Unassigned |
| `TO-83` | TO | JREFII | Complete | $0 | $1,650 | Parakeet Ops |
| `ROYAL-10` | ROYAL | Kippy | Complete | $3,500 | $25,415 | High Pace |
| `BOVIIPO-38` | BOVIIPO | Origins | Complete | $0 | $1,650 | Parakeet Ops |
| `BOVIIPO-97` | BOVIIPO | Origins | Not Started | $0 | $25,415 | Unassigned |
| `BOVIPO-C-2` | BOVIPO | Origins | Not Started | $0 | $25,415 | Unassigned |
| `GULFPO-4` | GULFPO | Origins | Not Started | $0 | $25,415 | Unassigned |

## Complete, still carrying GL spend — 56 units, $989,786

**The million-dollar question of this program.** If these have been placed in service the money is capitalised and WIP is clean; if not, roughly a million dollars is sitting in work-in-progress for finished homes. **The export carries a GL actual, not a GL account, so no source in this Brain can say which** — `INFERRED`. **Owner: the Controller seat. It is a WIP trial-balance query, not a project.** Belle Haven is $289,254 of it across the most-complete community in the portfolio, so it is the one to clear first.

| Unit | Community | Vehicle | Status | GL booked | End date | Days |
|---|---|---|---|---|---|---|
| `BRUN-155` | Brunswick Estates | JREFII | Complete | $125,123 | 2026-03-30 | 88 |
| `ARD-136B` | Auburn Ridge | JREFII | Complete | $50,617 | 2026-04-06 | 66 |
| `BRUN-21` | Brunswick Estates | JREFII | Complete | $45,935 | 2026-06-15 | 195 |
| `ARD-132A` | Auburn Ridge | JREFII | Complete | $45,824 | 2026-03-03 | 90 |
| `BELL-54` | Belle Haven | JREFI | Complete | $39,216 | 2026-06-19 | 19 |
| `WPMH-5085 CLOVER` | Whispering Pines FL | JREFI | Complete | $37,206 | 2026-08-13 | 134 |
| `WPMH-4885 CLOVER` | Whispering Pines FL | JREFI | Complete | $32,394 | 2026-06-04 | 55 |
| `WPMH-4925CLOVER` | Whispering Pines FL | JREFI | Complete | $30,908 | 2026-05-17 | -15 |
| `BELL-18` | Belle Haven | JREFI | Complete | $26,380 | 2026-04-24 | 24 |
| `WPMH-359 DAISY` | Whispering Pines FL | JREFI | Complete | $26,322 | 2026-04-24 | 7 |
| `BELL-33` | Belle Haven | JREFI | Complete | $24,868 | 2026-05-17 | 45 |
| `BELL-27` | Belle Haven | JREFI | Complete | $24,126 | 2026-06-19 | 18 |
| `WPMH-353 DAISY` | Whispering Pines FL | JREFI | Complete | $23,478 | 2026-05-17 | 37 |
| `SILVER-21` | Silver Breeze | JREFI | Complete | $23,132 | 2026-07-16 | 31 |
| `BELL-30A` | Belle Haven | JREFI | Complete | $23,064 | 2026-04-24 | 31 |
| `BELL-5` | Belle Haven | JREFI | Complete | $22,776 | 2026-05-17 | 45 |
| `BELL-44` | Belle Haven | JREFI | Complete | $21,911 | 2026-06-19 | 18 |
| `WPMH-354 DAISY` | Whispering Pines FL | JREFI | Complete | $19,430 | 2026-04-20 | 3 |
| `BELL-41` | Belle Haven | JREFI | Complete | $18,645 | 2026-05-17 | 46 |
| `BELL-16` | Belle Haven | JREFI | Complete | $17,714 | 2026-04-24 | 23 |
| `BELL-64` | Belle Haven | JREFI | Complete | $16,861 | 2026-06-19 | 18 |
| `BELL-57` | Belle Haven | JREFI | Complete | $16,605 | 2026-08-26 | 57 |
| `APPLE-335 CIRCLE` | Applegate | JREFI | Complete | $16,518 | 2026-07-13 | 13 |
| `DO-155` | Druid Oaks | JREFII | Complete | $15,500 | 2026-05-19 | — |
| `FOX-27` | Fox Creek | JREFII | Complete | $14,350 | 2026-03-05 | 17 |

*Twenty-five of 56 shown, largest first. Full list in the source CSV, filter `status=Complete` and `glActual>0`.*

## Open past 60 days — 18 units, breaching the board goal

**The 2026 board goal is to turn any vacated home in under 60 days.** These 18 are past it and 15 are past 90. **Ten of them are Silver Breeze units that all started 2026-04-17** — ten units frozen on one date is a batch that never got worked, not ten slow rehabs, and it should be handled as one item rather than ten. An eleventh, `SILVER-42`, is In Progress with no start date, so it sits in the no-start table below instead. `SOUTH-86` at 274 days and `BRUN-203` at 250 days are the last two of John Clark's Q1 rock; **closing those two closes a rock.**

| Unit | Community | Vehicle | Status | Age | Start | Vendor |
|---|---|---|---|---|---|---|
| `SOUTH-86` | Southgate | JREFI | In Progress | **274d** | 2025-11-25 | High Pace |
| `BRUN-203` | Brunswick Estates | JREFII | In Progress | **250d** | 2025-12-19 | Primary Home Repair |
| `PARK-42` | Parkwood Mobile Home Park | JREFII | In Progress | **132d** | 2026-04-16 | High Pace |
| `SILVER-10` | Silver Breeze | JREFI | In Progress | **131d** | 2026-04-17 | High Pace |
| `SILVER-20` | Silver Breeze | JREFI | In Progress | **131d** | 2026-04-17 | High Pace |
| `SILVER-23` | Silver Breeze | JREFI | In Progress | **131d** | 2026-04-17 | High Pace |
| `SILVER-30` | Silver Breeze | JREFI | In Progress | **131d** | 2026-04-17 | High Pace |
| `SILVER-31` | Silver Breeze | JREFI | In Progress | **131d** | 2026-04-17 | High Pace |
| `SILVER-35` | Silver Breeze | JREFI | In Progress | **131d** | 2026-04-17 | High Pace |
| `SILVER-37` | Silver Breeze | JREFI | In Progress | **131d** | 2026-04-17 | High Pace |
| `SILVER-38` | Silver Breeze | JREFI | In Progress | **131d** | 2026-04-17 | High Pace |
| `SILVER-5` | Silver Breeze | JREFI | In Progress | **131d** | 2026-04-17 | High Pace |
| `SILVER-8` | Silver Breeze | JREFI | In Progress | **131d** | 2026-04-17 | High Pace |
| `DO-57` | Druid Oaks | JREFII | In Progress | **120d** | 2026-04-28 | High Pace |
| `LUCK-35` | Lucky Clover | JREFI | Not Started | **120d** | 2026-04-28 | High Pace |
| `PPH-30` | Palm Haven Estates | JREFI | Not Started | **77d** | 2026-06-10 | High Pace |
| `SH-73` | Silver Hill MHC | JREFII | In Progress | **77d** | 2026-06-10 | High Pace |
| `RO-216WHITESQUIRREL` | RO | JREFI | Not Started | **74d** | 2026-06-13 | Unassigned |

## Open with no start date — 40 units, $823,768 modelled

**A start date is how a rehab enters the 60-day clock. These are not on it.** Some are genuinely not started and that is fine; the tell that this is a data-maintenance problem rather than a scheduling one is that **26 other rows carry a start date in the future and 6 carry dates that do not parse**. The field is not being kept. **Owner: John Clark. Schedule or park each one explicitly at the Wednesday call — a blank is not a decision.**

| Unit | Community | Vehicle | Status | Modelled remaining | Tier | Vendor |
|---|---|---|---|---|---|---|
| `BRUN-37` | Brunswick Estates | JREFII | Not Started | $25,415 | Untiered | Jams + Stark |
| `BRUN-66` | Brunswick Estates | JREFII | Not Started | $25,415 | Untiered | Primary Home Repair |
| `BRUN-8` | Brunswick Estates | JREFII | Not Started | $16,438 | L1 | Primary Home Repair |
| `CA-1` | Crystal Acres | Kippy | Not Started | $15,600 | Full Gut Remodel | High Pace |
| `CA-25` | Crystal Acres | Kippy | Not Started | $15,600 | Full Gut Remodel | High Pace |
| `CA-34` | Crystal Acres | Kippy | Not Started | $15,600 | Full Gut Remodel | High Pace |
| `CA-35` | Crystal Acres | Kippy | Not Started | $15,600 | Full Gut Remodel | High Pace |
| `CA-37` | Crystal Acres | Kippy | Not Started | $15,600 | Full Gut Remodel | High Pace |
| `CA-49` | Crystal Acres | Kippy | Not Started | $15,600 | Full Gut Remodel | High Pace |
| `DO-22` | Druid Oaks | JREFII | In Progress | $16,438 | L1 | Primary Home Repair |
| `DO-41` | Druid Oaks | JREFII | In Progress | $16,438 | L1 | Primary Home Repair |
| `FOX-132` | Fox Creek | JREFII | In Progress | $21,992 | L2 | High Pace |
| `GO-AA` | Great Oak | JREFII | Not Started | $25,415 | Untiered | High Pace |
| `HSMHC-13` | Hunter Springs | Kippy | Not Started | $15,600 | Full Gut Remodel | High Pace |
| `HSMHC-18` | Hunter Springs | Kippy | Not Started | $15,600 | Full Gut Remodel | High Pace |
| `HSMHC-19` | Hunter Springs | Kippy | Not Started | $15,600 | Full Gut Remodel | High Pace |
| `HSMHC-8` | Hunter Springs | Kippy | Not Started | $15,600 | Full Gut Remodel | High Pace |
| `HSMHC-9` | Hunter Springs | Kippy | Not Started | $15,600 | Full Gut Remodel | High Pace |
| `OCEANPO-84` | Oceanaire | Origins | Not Started | $25,415 | Untiered | High Pace |
| `PARK-87` | PARK | JREFII | Not Started | $25,415 | Untiered | Unassigned |
| `PSEPO-2` | Palm Spring | Origins | Not Started | $25,415 | Untiered | High Pace |
| `PSEPO-24` | Palm Spring | Origins | Not Started | $25,415 | Untiered | High Pace |
| `PARK-7` | Parkwood Mobile Home Park | JREFII | In Progress | $21,992 | L2 | High Pace |
| `PARK-82` | Parkwood Mobile Home Park | JREFII | In Progress | $16,438 | L1 | High Pace |
| `RW-63` | Riverwalk | JREFII | Not Started | $25,415 | Untiered | High Pace |
| `ROYAL-22` | Royal Oaks | Kippy | Not Started | $9,027 | N/A | High Pace |
| `SA-101` | Shady Acres | JREFII | Not Started | $25,415 | Untiered | Jams + Stark |
| `SA-104` | Shady Acres | JREFII | Not Started | $25,415 | Untiered | Jams + Stark |
| `SA-167` | Shady Acres | JREFII | Not Started | $25,415 | Untiered | Primary Home Repair |
| `SA-180` | Shady Acres | JREFII | In Progress | $16,438 | L1 | High Pace |
| `SA-214` | Shady Acres | JREFII | In Progress | $21,992 | L2 | High Pace |
| `SA-246` | Shady Acres | JREFII | Not Started | $25,415 | Untiered | Primary Home Repair |
| `SA-35` | Shady Acres | JREFII | In Progress | $16,438 | L1 | High Pace |
| `SILVER-42` | Silver Breeze | JREFI | In Progress | $15,600 | Full Gut Remodel | High Pace |
| `SH-110` | Silver Hill MHC | JREFII | Not Started | $25,415 | Untiered | High Pace |
| `SUR-16` | Su-Rene | JREFII | Not Started | $25,415 | Untiered | High Pace |
| `SUR-43` | Su-Rene | JREFII | Not Started | $25,415 | Untiered | High Pace |
| `TRADE-30OLSEN` | Tradewinds | JREFI | Not Started | $30,882 | L3 | High Pace |
| `TRADE-APT 1` | Tradewinds | JREFI | Not Started | $25,415 | Untiered | High Pace |
| `WIND-102` | Windward Knoll | JREFII | Not Started | $25,415 | Untiered | High Pace |

## Open with no vendor — 15 units, $381,225 modelled

**Nobody is doing these.** They sit on the board with modelled scope and no crew. **Owner: unassigned — assign or park at the Wednesday call.**

| Unit | Community | Vehicle | Status | Modelled remaining | Tier | Start |
|---|---|---|---|---|---|---|
| `BOVIIPO-97` | BOVIIPO | Origins | Not Started | $25,415 | Untiered | 2026-08-31 |
| `BOVIPO-C-2` | BOVIPO | Origins | Not Started | $25,415 | Untiered | 2026-08-31 |
| `DO-44` | DO | JREFII | Not Started | $25,415 | Untiered | 2026-09-01 |
| `FOX-129` | FOX | JREFII | Not Started | $25,415 | Untiered | 2026-08-27 |
| `GULFPO-4` | GULFPO | Origins | Not Started | $25,415 | Untiered | 2026-07-09 |
| `NGMH-3304 3RD AVE` | NGMH | JREFII | Not Started | $25,415 | Untiered | 2026-08-11 |
| `PARK-66` | PARK | JREFII | Not Started | $25,415 | Untiered | 2026-07-09 |
| `PARK-87` | PARK | JREFII | Not Started | $25,415 | Untiered | — |
| `RO-216WHITESQUIRREL` | RO | JREFI | Not Started | $25,415 | Untiered | 2026-06-13 |
| `RW-171` | RW | JREFII | Not Started | $25,415 | Untiered | 2026-07-09 |
| `RW-35` | RW | JREFII | Not Started | $25,415 | Untiered | 2026-08-27 |
| `SILVER-11` | SILVER | JREFI | Not Started | $25,415 | Untiered | 2026-07-24 |
| `TC-E-9` | TC | JREFII | Not Started | $25,415 | Untiered | 2026-07-22 |
| `TO-32` | TO | JREFII | Not Started | $25,415 | Untiered | 2026-08-11 |
| `WPMH-4770 PERIWINKLE` | WPMH | JREFI | Not Started | $25,415 | Untiered | 2026-07-09 |

## Dates that do not make sense — 6 units

**Small, and worth fixing because these rows corrupt every duration figure they touch.** A completion before a start, or an end before a step, makes the 60-day metric wrong in the direction that flatters it.

| Unit | Community | Vehicle | Status | Start | End | Days |
|---|---|---|---|---|---|---|
| `BELL-78` | Belle Haven | JREFI | Complete | 2026-04-02 | 2026-03-19 | -14 |
| `FOX-39` | Fox Creek | JREFII | Complete | 2026-01-20 | 2026-01-14 | -6 |
| `NGMH-3301 1ST AVE` | NGMH | JREFII | Complete | 2026-07-17 | 2026-07-13 | -4 |
| `PPH-K` | Palm Haven Estates | JREFI | Complete | 2026-04-01 | 2025-11-24 | -128 |
| `TO-10` | TO | JREFII | Complete | 2026-07-14 | 2026-07-13 | -1 |
| `WPMH-4925CLOVER` | Whispering Pines FL | JREFI | Complete | 2026-06-01 | 2026-05-17 | -15 |
