# Numbers ledger — verified figures only

The only place a business number is trusted from. Every entry has a source and an as-of date. If a number isn't here, it isn't citable — say "unknown" and flag it.

Property-level operating data for all 67 communities lives in [[60-Communities/portfolio]], sourced to the Property Data Sheet with its own as-of date and its own data-quality warnings. That table is the property-level extension of this ledger; do not restate its figures elsewhere.

Project-level costs for capex and infill work live in [[60-Communities/projects]] on the same footing: sourced, dated, and not restated elsewhere. The floor line section below is the exception that stays here, because it is a facility position rather than a project cost.

## Rehab program — as of 2026-08-28

**Source for every row: `70-Operations/rehab-program/data/rehab_tracker_all_data_2026-08-28.csv`**, 219 unit rows, filed 2026-09-02. Program page [[70-Operations/rehab-program/overview]]. **Point-in-time export of a live vendor sheet** — quote the as-of date with any figure from this block.

| Metric | Value | As of | Source |
| --- | --- | --- | --- |
| Rehab/infill units tracked | 219 | 2026-08-28 | tracker CSV |
| Open units | 133 (73 In Progress, 59 Not Started, 1 unlabelled) | 2026-08-28 | tracker CSV |
| Complete units | 87 | 2026-08-28 | tracker CSV |
| **Rehab cost — general ledger** | **$1,338,235** | 2026-08-28 | tracker CSV, `glActual`. Accounting is 30–45 days in arrears (`KP-0003`) |
| **Rehab cost — Rent Manager** | **$1,169,997** | 2026-08-28 | tracker CSV, `cost`. **Only 75 of 219 rows carry a real typed cost**; 132 read `IN PROGRESS`, 12 read `NONE`. **Do not divide by 219** |
| **Rehab cost — vendor tracker** | **$1,064,057** | 2026-08-28 | tracker CSV, `trackerCost`. High Pace's own sheet |
| Active assets at tracker preparation | 182 (159 in-house on the `Mark` tab, 23 on `Alt Vendor`) | 2026-06-13 | `Rehab Tracker - Working Copy 7-26-26.xlsx`, Read Me. **Against 219 rows in the 2026-08-28 export** |
| **Homes flagged START missing-title** | **52** | 2026-06-13 | same workbook, title status pulled from Rent Manager. Owner named in the workbook: Melanie. **Distinct from the nine Royal Oaks titles in `CM-19`** |
| Completion-date assumption where no real date is known | start plus 45 days | 2026-06-13 | same workbook, colour key. **A completion date on the tracker may be this formula rather than a report from site** |
| **Three-way variance** | **$274,178** | 2026-08-28 | highest minus lowest of the three above. `KP-0040` |
| GL against open units | $351,442 across 77 units | 2026-08-28 | tracker CSV. The approximate WIP closing balance |
| **GL against units marked Complete** | **$989,786 across 56 units** | 2026-08-28 | tracker CSV. **Whether this has rolled out of WIP is unknown — the export carries a GL actual, not a GL account.** `KP-0041` |
| Rehabs completed with a 2026 end date | 77 | 2026-08-28 | tracker CSV. Board goal 100+. Monthly: Jan 7 · Feb 5 · Mar 8 · Apr 9 · May 9 · Jun 9 · Jul 14 · Aug 16 |
| 60-day turn rate | 85% (57 of 67 measurable turns), median 31 days | 2026-08-28 | tracker CSV. 2026 board goal is under 60 days |
| Open units past 60 days | 18, of which 15 past 90 | 2026-08-28 | tracker CSV. `KP-0045` |
| Open units with no start date | 40 | 2026-08-28 | tracker CSV. Not on the 60-day clock at all |
| Units in the un-onboarded intake cohort | 37 | 2026-08-28 | tracker CSV. Every row missing a WIP code and every row absent from the vendor tracker. `KP-0042` |
| Vendor concentration — High Pace | 165 of 219 units, 105 of the open ones | 2026-08-28 | tracker CSV. `KP-0046` |
| Units with no vendor assigned | 19, 15 of them open | 2026-08-28 | tracker CSV |

**Three figures from this pull are deliberately NOT entered as trusted numbers**, per rule 3:

- **`expected`, $4,198,591**, and **`remaining`, $2,833,406** — these are **models**, back-solved from tier averages with samples as small as six comparable jobs, and 27 rows priced off a flat portfolio average of 75 jobs. They are a statistical projection, not approved capital. **Never quote them to Jon, an LP or a lender as a forecast.** `PD-26` asks whether they may be used at all before `TD-0415` reconciles them to the $9,954,600 capex plan.
- **Any per-community rollup** — 37 rows carry a unit-code prefix instead of a community name, so the same property appears twice and every by-community total double-counts. The dashboard resolves the codes it can; `NGMH`, `LS` and `PPH` cannot be resolved from anything in this Brain and are not guessed. `KP-0042`.

## Portfolio

| Metric | Value | As of | Source |
|---|---|---|---|
| Active communities | 67 | 2026-08-30 | Property Data Sheet, less Cambridge (sold) per Austin |
| Core units, active portfolio | 6,379 | Dec 2025 vintage | Property Data Sheet, PDS Clean |
| MH lots | 5,293 | Dec 2025 vintage | Property Data Sheet |
| RV sites | 950 | Dec 2025 vintage | Property Data Sheet |
| Other units | 136 | Dec 2025 vintage | Property Data Sheet |
| Park-owned homes | 784 | Dec 2025 vintage | Property Data Sheet |
| Acres | 934.3 | Dec 2025 vintage | Property Data Sheet |
| Aggregate purchase price | $487,974,500 | acquisitions 2017 to 2026-05 | Property Data Sheet |
| Weighted occupancy | 82.5% across 5,874 units / 62 properties | December 2025 | Property Data Sheet — excludes 5 unreliable rows |
| Properties by state | FL 47, SC 7, MA 5, GA 5, MI 1, NC 1, AL 1 | 2026-08-30 | Property Data Sheet + Austin |
| Core units by state | FL 3,950, GA 983, SC 841, MA 273, NC 234, MI 53, AL 45 | Dec 2025 vintage | Property Data Sheet |
| Properties by vehicle | JREFI 22, JREFII 22, Origins 10, Single Asset 4, Baker 3, Kippy 3, Harpreet 2, Fund II 1 | 2026-08-30 | Property Data Sheet |
| 2026 MH lot rent | $373 to $1,367, average $691 across 63 properties | 2026 | Property Data Sheet |
| 2026 RV lot rent | $600 to $2,275, average $897 across 18 properties | 2026 | Property Data Sheet |
| Properties acquired in 2025 | 25 of 67 | 2025 | Property Data Sheet |
| Largest single asset | Regency I & II, 424 lots, $37,293,000 | acquired 2026-04-14 | Property Data Sheet |
| Lamberton Lake year to date utility expense over budget | **roughly $52,000**, per the Capital One asset manager, asked twice with no written answer | 2026-09-03 | George Ksenics, Capital One, on `CM-29`. Consistent with the Grand Rapids water bill running $4,356 (June), $4,966 (July), $9,463.14 (August) against a leak flagged in March 2026, `PF-0459`, `PF-0460` |
| Mayflower Hills buyer financing deadline | **2026-10-19**, moved by the buyer through counsel | 2026-09-15 | Counsel email read at the 2026-09-15 close, `00-Meta/daily-close/2026-09-15.md` item 18. Sale recorded on `TD-0627` 2026-09-10 |
| Mayflower Hills purchase price credit under the ROFR | **None.** A credit is not a substantially equivalent offer under the ROFR | 2026-09-10 | Robert Kraus 14:30 ET, Austin 14:43 ET, Adam Freedman 15:49 ET *"Let's do it."* `TD-0627` closed. `00-Meta/daily-close/2026-09-10.md` |
| Silver Breeze loan maturity | **2026-12-01**, second 12 month extension agreed by seller and lender, same terms, same documents | 2026-09-14 | Jon Wyss to Paul Hastings 16:09 ET, read at the 2026-09-14 close. Agreed in email; executed extension documents not seen here |
| Silver Breeze Brevard County SOIRL date | **2026-09-25, UNCORROBORATED.** Jon pasted it into the construction chat and said he did not know if it was right | 2026-09-09 | Teams construction thread 16:37 ET. `KP-0106`, `TD-0621`. Nothing in this vault sources the date and the executed SOIRL agreement has not been pulled |

## Organisation

| Metric | Value | As of | Source |
|---|---|---|---|
| Total employees | ~125 | 2026-08-30 | Austin, in the Structure Interview |
| Corporate employees incl. offshore | 42 | March 2026 | Executive Strategy Meeting deck, slide 9 |
| Offshore and support staff | 20 (8 Acctg/Fin/HR, 5 Ops, 7 AM) | December 2025 | Staffing Org Chart JSON |
| Regional managers | 3 | 2026-08-30 | Austin — Godinez, Santiago, Alex |
| Facilities managers | 3 | December 2025 | Staffing Org Chart JSON |
| Named on-site community managers | 28 named plus 1 vacant | December 2025 | Staffing Org Chart JSON |
| Field employees replaced or upgraded, prior 6 months | 13 | March 2026 | Executive Strategy deck, slide 52 |
| ClickUp renewal | **$4,104 for 18 seats, renewing 2026-11-09** | 2026-09-11 | Renewal notice read at the 2026-09-10 close; `TD-0630` closed 2026-09-11 as renewed |
| SharePoint Online tenant usage against entitlement | **6,567.38 GB used against 2,394 GB** | 2026-09-11 | Microsoft tenant notice read at the 2026-09-11 close. Up from 6,550.52 GB on 2026-09-07 in the gaps section below. `KP-0111` |

## 2026 operating targets

| Metric | Value | As of | Source |
|---|---|---|---|
| New homes to order | ~230 | 2026 target | Executive Strategy deck, slide 50 |
| Homes to list | ~400 | 2026 target | Executive Strategy deck, slide 50 |
| Homes to sell | ~400 at max 30% loss | 2026 target | Executive Strategy deck, slide 50 |
| Home lot preps, deliveries and installs | ~200 | 2026 target | Executive Strategy deck, slide 51 |
| Rehabs to complete | 100+ | 2026 target | Executive Strategy deck, slide 51 |
| Community improvement projects to kick off | 150+ | 2026 target | Executive Strategy deck, slide 51 |
| POH count reduction | 100+ units | 2026 target | Board Presentation 2026-03 |
| Monthly delinquency | under 2% | 2026 target | Executive Strategy deck, slide 52 |
| Eviction turnover | under 90 days | 2026 target | Executive Strategy deck, slide 52 |
| Residents on signed leases | 95% by year end | 2026 target | 2026 Rocks & KPIs; deck slides 30, 52 |
| Resident turnover | under 5% | 2026 target | Executive Strategy deck, slide 30 |
| Controllable expenses | within 5% of budget | 2026 target | Executive Strategy deck, slide 52 |
| Turn any vacated home for sale or lease | under 60 days | 2026 target | Executive Strategy deck, slide 51 |

## Infill and occupancy plan

| Metric | Value | As of | Source |
|---|---|---|---|
| Total occupant gain target | 675 | March 2026 | [[80-Finance/planning/2026-executive-strategy/Infill Strategy Planning (hardcodes).xlsx]] — **a March 2026 point-in-time snapshot. The live infill numbers are managed by the team on shared sheets reviewed on a weekly call; this file is an export, not the source of truth.**, **Sheet1** (portfolio subtotals, 58 properties) |
| Occupant gain by portfolio | JREFI 292, JREFII 277, Origins 106 | March 2026 | [[80-Finance/planning/2026-executive-strategy/Infill Strategy Planning (hardcodes).xlsx]] |
| Vacant lots portfolio-wide | 675 | March 2026 | [[80-Finance/planning/2026-executive-strategy/Infill Strategy Planning (hardcodes).xlsx]], Sheet1. Genuinely also 675 — the same figure as the occupant-gain target, verified independently, not a copy error |
| Total occupant gain target, per-property view | 661 against 925 total vacancy | March 2026 | [[80-Finance/planning/2026-executive-strategy/Infill Strategy Planning (hardcodes).xlsx]], **Sheet2** (51 properties). **The workbook disagrees with itself — see the gaps section** |
| Vacant POH portfolio-wide | 306 | March 2026 | [[80-Finance/planning/2026-executive-strategy/Infill Strategy Planning (hardcodes).xlsx]] |
| Rehab & Sell / Infill & Sell / Sell | 142 / 498 / 35 | March 2026 | [[80-Finance/planning/2026-executive-strategy/Infill Strategy Planning (hardcodes).xlsx]], Sheet1 (Sheet2 gives Infill & Sell as 484) |
| JREFI December 2026 occupancy target | +12% to 94% | 2026 budget | Executive Strategy deck, slide 40 |
| JREFII planned occupancy increase | 137 units | 2026 budget | Executive Strategy deck, slide 41 |

## Home and infill economics

| Metric | Value | As of | Source |
|---|---|---|---|
| Home cost assumption | $65,000 | March 2026 | home pricing vs. market lot rent workbook |
| Infill (install) cost assumption | $35,000 | March 2026 | home pricing vs. market lot rent workbook |
| Total home plus infill cost | $100,000 | March 2026 | home pricing vs. market lot rent workbook |
| Financing assumption | 10% interest, 20 years, 5% down | March 2026 | home pricing vs. market lot rent workbook |
| Two-bedroom market rent benchmark | $1,448, less 10% = $1,303.20 POH market rent | 2026 | home pricing vs. market lot rent workbook |
| Resident total payment at full cost | $1,569.89 (loan $929.89 plus $640 lot rent) | 2026 | home pricing vs. market lot rent workbook |
| Starting home-price discount policy | 25% | March 2026 | Executive Strategy deck, slide 20 |
| Cavco trim-out invoices never submitted for payment | **13 home invoice, first sent by the plant 2026-08-10**; none had been sent over for payment | 2026-09-14 | John Clark 15:48 ET; Michele Newell at the Douglas plant; Jason Calvert resending park specific. Dollar amount not stated in any message read. `00-Meta/daily-close/2026-09-14.md` |

## Home asset inventory and floor line

Added 2026-08-31. Every figure here comes from one of two emails, both read in full. **These are a position at a moment in a reconciliation that is not finished** — the underlying home list is known to be wrong, so treat them as the best current read and not as a closed number. The analysis is at [[60-Communities/asset-inventory]].

| Metric | Value | As of | Source |
|---|---|---|---|
| 21st Mortgage utilisation, once pending orders come off | $2,741,192.13 | 2026-08-31 | Berman floor line rebuild, email 02:13 ET |
| Triad utilisation against facility | $3,123,807.35 of $4,500,000 | 2026-08-31 | Berman floor line rebuild, email 02:13 ET |
| CountryPlace | effectively maxed; no figure stated | 2026-08-31 | Berman floor line rebuild, email 02:13 ET |
| Orders the lenders were never told about | $1,408,256.25 across 28 homes | 2026-08-31 | Berman floor line rebuild, email 02:13 ET |
| Reserve 21st wants against the insurance deductible | $250,000, proposed funded from Home Sales SC capital | 2026-08-31 | Berman floor line rebuild, email 02:13 ET |
| Insurance deductible the reserve sits against | $500,000 | 2026-08-31 | Berman floor line rebuild, email 02:13 ET |
| Add-on approvals riding already-funded serials | $3,100 to $3,800 each, 13 of them | 2026-08-27 | Jon Wyss, Floor Line Tie-Out email 11:55 ET |
| Triad floor plan line | **$7,500,000, up from $4,500,000**, plus a **$2,000,000 CAP program** approved | 2026-09-10 | David Berman email 17:03 ET, read at the 2026-09-10 close. Supersedes the $4,500,000 facility on the 2026-08-31 row above, which stays as that date's utilisation denominator |
| 21st Mortgage reserve, decided | **$250,000**, wire sent 2026-09-10 | 2026-09-09 | Austin to Greg Valentine 2026-09-08 16:34 ET; `PD-35` decided 2026-09-09 15:59 ET. Final approval for the new locations and the credit line increase follows funding (Valentine, 2026-09-08 16:59 ET) |
| Line capacity across CountryPlace, 21st and Triad | **Not established.** The precondition Austin set 2026-08-31 was never met and the Triad change moved it by $3,000,000 | 2026-09-10 | `KP-0107`, `TD-0622`, `CM-15` |

## CapEx

| Metric | Value | As of | Source |
|---|---|---|---|
| Total 2026 capex plan | $11,588,600 original cost column; $12,416,500 revised | March 2026 | CapEx Overview workbook |
| Plan excluding Deleted rows | $10,300,100 original; $10,984,000 revised | March 2026 | CapEx Overview workbook |
| By portfolio | JREFI $6,747,600; JREFII $4,072,000; Legacy $769,000 | March 2026 | CapEx Overview workbook |
| Line items | 245 (169 Existing, 53 Deleted, 18 Complete, 5 New) | March 2026 | CapEx Overview workbook |
| Capex still marked "Existing" | $9,954,600 across 169 line items, 53 properties | March 2026 | CapEx Overview workbook, Data sheet filtered to Update = Existing |
| Utility categories combined | $5,978,500, 52% of the plan | March 2026 | CapEx Overview workbook |
| Largest property allocation | Paradise Lakes $2,825,000 | March 2026 | CapEx Overview workbook |
| Peak monthly spend | $994,810 | October 2026 | CapEx Overview workbook |
| Lucky Clover sewer tie-in | $1.6M cost, $1.4M (86%) covered by a SOIRL grant, 58 septics retired | target March 2026 | Executive Strategy deck, slide 43 |
| Triple S boat lifts tranche 2 | $252,000, 19 lifts at ~$14,000/slip, rent $215 to $625/mo, ~35% ROI | est. July 2026 | Executive Strategy deck, slide 47 |
| Silver Breeze sewer tie-in | **$500,000** | 2026-09-09 | `00-Meta/daily-close/2026-09-09.md` question 3, restating the figure on `PF-0487`. Permit *"expected any moment"*, construction 8 to 10 weeks after it (John Clark, Teams, 2026-09-09) |
| Hunter Springs home rehab quote, Doucette | **$30,000 a home**, raised from the $20,000 *"lipstick on the pig"* plan of 2026-09-02 | 2026-09-15 | Doucette email 17:26 ET; Jon 11:43 ET *"We will sign and kick off today"*; Jon 17:27 ET *"I think we r good austin can confirm."* `TD-0662`. No kickoff had reached For Signature by 18:05 ET |
| Gunster aerial imagery, Clearwater and Titusville site plans | **roughly $7,000**, all flights 2007 to 2026 | 2026-09-15 | Jon Wyss email 16:27 ET, read at the 2026-09-15 close. Committed by Jon, not yet invoiced |
| Lucky Clover park models under entitlement review with Melbourne Community Development | **22** | 2026-09-14 | Meeting invitation from Mary Wolak for 2026-09-15 10:00 ET, read at the 2026-09-14 close |

## Payroll

| Metric | Value | As of | Source |
|---|---|---|---|
| 2026 revenue basis | $54,487,005.11 | 2026 budget | Payroll Breakdown workbook |
| Payroll benchmark | 5% of property revenue | 2026 budget | Payroll Breakdown workbook |
| 5% benchmark value | $2,724,350.26 | 2026 budget | Payroll Breakdown workbook |
| Annualized allocation | $2,900,824.79 | 2026 budget | Payroll Breakdown workbook |
| Pad count in model | 5,640 | 2026 budget | Payroll Breakdown workbook |
| Average salary per pad | $514.33 | 2026 budget | Payroll Breakdown workbook |
| Worst payroll deficit | Terrace Crossings, 25% of revenue, $3,067.11 per pad, $158,775 deficit | 2026 budget | Payroll Breakdown workbook |
| November 2025 total payroll | $436,638.33 ($404,077.19 salary + $32,561.14 health) | Nov 2025 | Payroll Breakdown workbook |
| Corporate share of Nov 2025 payroll | $221,762.42, ~51% | Nov 2025 | Payroll Breakdown workbook |

## 2025 results and misses

| Metric | Value | As of | Source |
|---|---|---|---|
| JREFI 2025 NOI miss | ~$700,000 | FY2025 | Board Presentation 2026-03 |
| Rental income miss | $920,000, ~60% RV occupancy, ~40% infill delay | FY2025 | Board Presentation 2026-03 |
| Geiger Key Fish Camp income miss | $275,000 | FY2025 | Board Presentation 2026-03 |
| Interest expense over budget | $1,403,926 | FY2025 | Board Presentation 2026-03 |
| Insurance over budget | 22% | FY2025 | Board Presentation 2026-03 |
| Acquisition volume | $171.5M against a $273.8M budget | FY2025 | Board Presentation 2026-03 |
| OpCo result | loss in 2025, larger loss budgeted for 2026 | FY2025 / 2026 budget | Board Presentation 2026-03 |
| Founder accrued bonuses left unpaid | $900,000 | 2025-12-31 | Board Presentation 2026-03 |
| JREFI 2026 budget | revenue +15% (60% occupancy, 40% rent), NOI +24% | 2026 budget | Executive Strategy deck, slide 40 |

## Bedrock MHC Fund II wind-down

| Metric | Value | As of | Source |
|---|---|---|---|
| Southeast portfolio sale | closed, 10 of 13 portfolio investments | 2025-12-30 | BMHCII Wind Down Update April 2026 |
| Seller note payoff | $18.78M | 2026-03-14 | BMHCII Wind Down Update April 2026 |
| LPs made whole on capital and preferred return | complete, no promote taken | 2026-07-31 | BMHCII Quarterly Update Q22026 |
| Distribution per unit | $0.99, ~$11M distributed | 2026 | BMHCII Quarterly Update Q22026 |
| MOIC | 1.87x | 2026 | BMHCII Quarterly Update Q22026 |
| Remaining assets | 3 — Lamberton Lake, Royal Palm, Everglades | 2026-06-30 | BMHCII Quarterly Update Q22026 |
| Target dissolution | Q4 2026 | stated plan | BMHCII Wind Down Update April 2026 |
| Fund IRR, target at close | 8 to 9% | 2026-08-31 | Austin, LP call — SINGLE-SOURCE, spoken |
| Fund IRR, current estimate | ~7.9% | 2026-08-31 | LP call, both parties agreed the number — SINGLE-SOURCE, spoken |
| Gross multiple | 1.89x | 2026-08-31 | Austin, LP call. **Does not match the filed 1.87x MOIC** and may not be the same measure — SINGLE-SOURCE |
| Individual LP entry spread | 18 to 20 months | 2026-08-31 | Austin, LP call — why no single per-investor IRR is quoted |
| WCO Capital capital balance on the disputed statement | $52,000, accruing the 8% preferred | 2026-08-31 | LP call — one LP only, and the statement date is not established |
| Misdirected 2021 distribution, untraced | $7,000, dated 16 or 21 July 2021 | 2026-08-31 | LP call — sent to the former Kadara account instead of WCO Capital |
| Phantom shortfall from the duplicated-payment error | $30,000 | 2026-08-31 | LP call — **not a real shortfall**, a reconciliation artefact on an issued statement |
| Fund II 2025 return, North Carolina balance due | **$47,183**, authorised by Austin | 2026-09-09 | Austin to Lisa Timbrook 15:03 ET, read at the 2026-09-09 close |
| Fund II 2025 return, New Jersey | **$15,300 refund** | 2026-09-10 | Lisa Timbrook 09:20 ET, read at the 2026-09-10 close |
| Fund II 2025 return signed | **2026-09-10**, *"yes and posted on portal"* | 2026-09-10 | Austin in chat, answering question 1 of `00-Meta/daily-close/2026-09-10.md`. `CM-25` dated |
| Fund II 2025 K-1 broadcast to the LP base | **2026-09-10 05:51 ET** from `ir@thebedrockgrp.com`, pointing at `mhcportal.investnext.com` | 2026-09-11 | Gmail thread read at the 2026-09-11 close. Supersedes the *0 final* row of 2026-09-03 in the gaps section. Five LPs reported they could not get in within three days, `KP-0110` |
| LPs served by password protected PDF after the portal failed | Koretsky 2026-09-11 08:32 ET; Scruggs 2026-09-11; Buckwalter and Brown (Fund II) by 2026-09-13; Brown (A2Z), Alpert, Perkins, Sjulsen 2026-09-15 | 2026-09-15 | Closes of 2026-09-11, 09-14 and 09-15. Key is the last four of the tax ID. Don at Geekdom Fund unconfirmed, `TD-0633` |
| Ridaa Murad's stated date for counsel to take over | **2026-09-30** | 2026-09-15 | His message 10:23 ET, read at the 2026-09-15 close: *"On Sep 30 everything goes away from me and only counsel gets involved."* `CM-26`, `TD-0659` |

### Investor capital, re-derived from primary records 2026-09-03

**Every row below was recomputed from cell values in the Fund's own workbooks and general ledger, never read off a total row.** Source detail and method: [[80-Finance/fund-reporting/wp36-38-integrity-reaudit]]. **These figures are what `WP-36-M3` asserts, so read the two disputed rows before quoting the total.**

| Metric | Value | As of | Source |
|---|---|---|---|
| Total contributed capital, Class A | $12,589,708 | 2026-09-03 re-derivation | BEDROCK FUND II FINANCIALS.xlsx, sum of the 66 Investment rows to the cent, corroborated on sheet "LP" quarterly EQUITY CONTRIBUTIONS. VERIFIED twice |
| **Same figure if the Forster item is a mis-key** | **$12,584,910 across 65 transactions** | 2026-09-03 | R-46 GL full-life pull. The $4,798 is booked as an outbound ACH, debit `36000 LP Distributions`. **This is the figure in dispute, not the total above** |
| Forster standing quarterly distribution | $4,798.20 | Q4 2019, Q3 2020, Dec 2020 | R-46 GL full-life pull, lines 1008, 1206, 1329, each with the matching `36000 LP Distributions` leg. **The disputed $4,798 is twenty cents off this, same payee, same account, same treatment** |
| Investor activity report rows | 2,123 | 2026-09-03 | rows 2:2124, no gaps. **`WP-38` says 2,128 and its own type counts sum to 2,123** |
| Activity types | Dividend 2,043, Investment 66, Transfer Out 7, Transfer In 7 | 2026-09-03 | activity report column E, all rows. No call, drawdown or contribution-notice row anywhere |
| Capital raised 2018 | $10,526,250 across 55 subscriptions | 2026-09-03 | recomputed, corroborated by the quarterly contributions row |
| Capital raised 2019 | $1,108,660 across 7 | 2026-09-03 | same |
| Capital raised 2020 | $954,798 across 4 | 2026-09-03 | same. Includes the disputed $4,798 |
| Actual transaction window | 2018-01-10 to 2026-03-16 | 2026-09-03 | activity report column C. **No 2017 activity despite the report window opening 2017-01-01** |
| Register contribution amount with no cash receipt behind it | $142,298 | 2026-09-03 | Bedrock I Group's $137,500 Class A position plus the Forster $4,798. Neither appears in the full-life GL pull. **May have an innocent explanation if Lamberton was contributed as property; that is a CPA question** |
| Account 1034 distributions, reports against the LP statement | $573,357.31 against $541,351.83 | 2026-09-03 | nine distribution reports against `Bedrock_FundII_Statement_WCO.pdf` page 2 |
| **Variance between those two** | **$32,005.48, and 33 rows against 26** | 2026-09-03 | **`WP-38` certifies the statement set as "Correct" and tells the reader to correct the register toward it. That propagates this gap** |
| Second-tranche subscriptions | $498,548 total, five accounts | 2026-09-03 | total correct. **Three of the five per-account amounts in `WP-38`'s table are displaced by one row**: Khodara $200,000, Slab $75,000, Taub $125,000 |
| LP statements issued 06/30/2026 | 62 | 2026-09-03 | `02_Investor_Capital\LP_Statements_06302026\`, exact count |
| Ledger accounts | 69, numbered 1001 to 1069, no gaps, all Class A | 2026-09-03 | R-46 GL full-life pull |
| Lamberton wire overage, `J316` | $22,970.55 credit, 2017-12-27 | 2026-09-03 | takes account `14211` from $160,150.00 to $137,179.45, leaving a $470.55 residual. **`WP-38` reports this gap as unexplained at $22,500** |
| Bedrock I Group receivable from A2Z Community Partners | $59,284.95 | every date tested, 2026-09-03 | GL `12101`. **`WP-38` says $46,535** |
| Bedrock I Group A2Z-family payables | $391,926.00 at 2024-12-31, $48,139.00 thereafter | 2026-09-03 | GL. **`WP-38` says $155,311, a string that appears nowhere in the project** |
| WCO Capital 2020 beginning capital account | $23,120 | 2026-09-03 | WP-2b row 437. **Unexplained. WCO has no 2018 or 2019 K-1 and `WP-38` states its beginning capital percentage was zero** |

## Process library

| Metric | Value | As of | Source |
|---|---|---|---|
| Processes tracked | 109 | 2026-08-06 | SOP_Master_Tracker_v3.xlsx |
| Approved | 1 workflow, 1 SOP document | 2026-08-30 | SOP_Master_Tracker_v3.xlsx |
| Drafted pending review | 36 | 2026-08-06 | SOP_Master_Tracker_v3.xlsx |
| Not started | 59 workflows, 43 SOP documents | 2026-08-06 | SOP_Master_Tracker_v3.xlsx |
| Tier 1 critical not started | 7 | 2026-08-06 | SOP_Master_Tracker_v3.xlsx |
| Training videos recorded | 0 of 27 slots | 2026-08-30 | 27 empty _Video Links.txt files |
| Byte-identical duplicate file sets | 48 sets, 96 files | 2026-08-30 | MD5 audit of the sops folder |
| Documented open conflicts | 19 | 2026-08-30 | [[70-Operations/sops/sop-library]] |

## Entity structure

| Metric | Value | As of | Source |
|---|---|---|---|
| Filed entity documents | 430 | 2026-08-30 | 10-Business/entity-structure |
| Entities with formation documents | ~89 certificates or articles | 2026-08-30 | entity-structure audit |
| EIN letters and SS-4s | 99 | 2026-08-30 | entity-structure audit |
| LLC and operating agreements | 71 | 2026-08-30 | entity-structure audit |
| Foreign qualifications | 22 (FL 12, GA 4, SC 2, MA 2, ND 1, plus 1 archived duplicate) | 2026-08-30 | entity-structure audit |
| Property Management Agreements | 129 PDFs, 69 unique, 60 byte-identical pairs | 2026-08-30 | entity-structure audit |
| Debt schedule | 74 loans, 13 lenders | archived, undated | 99-Archive/rock-processes/David/MASTER Debt Overview.xlsx |


## Portfolio actuals — RentViewer warehouse

Trailing twelve months ended 2026-07-31, the last complete GL month. These are actuals, not plan. The inclusion rules that produce them are at [[80-Finance/portfolio-reporting-rules]]; the full query record is at [[60-Communities/portfolio-baseline-warehouse]]. **They do not reconcile with the Property Data Sheet figures above — see conflicts C1 to C4 in [[00-Meta/open-items]].**

| Metric | Value | As of | Source |
|---|---|---|---|
| Reporting records | 71 (67 communities + 3 utilities + Triple S Marina) | TTM to 2026-07-31 | RentViewer warehouse, rules confirmed by Austin 2026-08-26 |
| Revenue | $44,412,071 | TTM to 2026-07-31 | RentViewer `VW_Budget_Comparison` |
| NOI | $27,870,728 | TTM to 2026-07-31 | RentViewer `VW_Budget_Comparison` |
| NOI margin | 62.75% — against a >50% target | TTM to 2026-07-31 | RentViewer `VW_Budget_Comparison` |
| Operating expense ratio | 37.25% — against a 45 to 50% target | TTM to 2026-07-31 | RentViewer `VW_Budget_Comparison` |
| Total units, raw | 9,355 | Snapshot 2026-08 | RentViewer `VW_Rental_Unit_Listing` |
| Total units, de-duplicated | 8,020 | Snapshot 2026-08 | RentViewer `VW_Rental_Unit_Listing`, filtered |
| Occupancy, de-duplicated | 77.67% | Snapshot 2026-08 | RentViewer `VW_Rental_Unit_Listing`, filtered |
| Margin when corporate overhead and Geiger Key are blended in | 48.43% | TTM to 2026-07-31 | Same query, unfiltered — the reason the portfolio looked like it was underperforming |

**The corporate entity is never included in property reporting.** `Parakeet Communities` carries −$3,636,103 NOI on $2,479,722 revenue. It is pure overhead and it drags portfolio margin roughly eight points.

## Massachusetts class settlement, American and Whispering Pines MA

Added 2026-08-31 from the "Parakeet - Confidential Settlement Communication" chain in Outlook, read end to end back to 2026-06-11. **VERIFIED against the primary thread.** The chain is marked *"Inadmissible Mass. G. Evid. § 408 Settlement Communication"* and is privileged. **The lump sum is agreed between the parties; the rent schedule is not.** Detail and context in `00-Meta/commitments.md` item 20.

| Metric | Value | As of | Source |
|---|---|---|---|
| Lump sum payment, **agreed by both sides** | $400,000.00, resolving all class claims, individual plaintiffs' claims, attorneys' fees and administrative costs | Offered 2026-07-14, accepted 2026-07-31 | Wallack to Allison 2026-07-14; Allison to Wallack 2026-07-31 |
| November 2023 lease rate, owner-tenants at **American** | $575.00 | 2026-07-14 | same chain |
| November 2023 lease rate, owner-tenants at **Whispering Pines MA** | $615.00 | 2026-07-14 | same chain |
| November 2023 lease rate, renter-tenants | $1,315.00 | 2026-07-14 | same chain |
| Monthly credit to owner-tenants, to 2028-11-30 | $115.00 | 2026-07-14, framework agreed in principle | same chain |
| Monthly credit to renter-tenants, to 2028-11-30 | $345.00 | 2026-07-14, framework agreed in principle | same chain |
| Effective rent, Whispering Pines owner-tenants until 2028-11-30 | $500.00 | 2026-06-11 | Wallack to Allison 2026-06-11 |
| **Parakeet's position from 2028-12-01** | lease amount **plus $50**, giving $665.00 at Whispering Pines | 2026-06-11 | same chain |
| **Plaintiffs' position from 2028-12-01** | **$20 annual** increase for owner-tenants | 2026-07-31 | Allison to Wallack 2026-07-31 |
| Plaintiffs' characterisation of the November 2023 increases | **23 to 25%** on owner tenants, **35 to 42%** on rental tenants | 2026-08 | Allison, same chain |
| Damages sought | *"at least double and likely treble"* overpayments of rent, plus attorneys' fees, under the Manufactured Housing Act and Chapter 93A | 2026-08 | Allison, same chain |

**The number that is missing, and it is the one that matters.** The whole remaining dispute is a one-time $50 step against $20 a year from December 2028, across owner-tenants and renter-tenants at two communities. **Nobody has valued that gap** — not in the chain, not on the 2026-08-31 call, not anywhere in this Brain. Until someone does, the choice between letting CBRE carry the argument and handing the number to a binding appraiser is being made without knowing what is being risked. It is arithmetic against a class list, not a judgement call, and it has no owner.

## Kippy dispute — positions, not company figures

Added 2026-08-31 from [[70-Operations/meetings/2026-08-31-kippy-dispute-legal-strategy]], recording read in full. **Every figure here is a negotiating position stated on a strategy call, not a reconciled company number**, and the same convention applies as to the floor line section above: recorded so the position is auditable later, not so it can be cited as fact. Two of them are explicitly approximate on the recording itself.

| Metric | Value | As of | Source |
|---|---|---|---|
| Management fees invoiced to Kippy across three properties | roughly $1,000,000. Stated as *"a million dollars, give or take"* and *"whether it's a million something more or something less, maybe based on some additional info, remains to be seen"* | 2026-08-31 | Plaud `93ccd143cd9e89f696ab82b994228e38` |
| Split of that total across the three properties | **not thirds.** Counsel proposed a third each as a working assumption and was corrected on the spot: *"let's just say it's a third, a third, a third, which it's not"* | 2026-08-31 | same recording |
| Time the note sat in default past maturity | roughly 3 months | 2026-08-31 | same recording |
| Kippy's settlement offer | the loan **less $250,000**, and nothing on the receivable. Rejected on the call | 2026-08-31 | same recording |
| Note extension sought by Kippy's side | to 2027-03-31 | 2026-08-31 | same recording |
| Note extension Parakeet would prefer | to end of 2026 | 2026-08-31 | same recording |
| Home rehabilitation cost referenced | *"twenty grand a home"* | 2026-08-31 | same recording |
| Number of homes in the refurbishment claim | **unresolved on the recording.** Six is referenced, one email *"only mentions three"*, and counsel believes the amendment covers rent on six lots with nothing to do with rehab | 2026-08-31 | same recording |
| Home rehab or occupancy date given to Kippy's side | 2026-11-30 | 2026-08-31 | same recording |

**Not in this table, and deliberately:** the $67,500 nine-title figure from `00-Meta/commitments.md` item 19. It is a different thread about the same community and it is not established that it involves the same counterparty. Merging the two sets of numbers before that is settled is exactly how a dispute total gets overstated. See [[00-Meta/open-items]] T2.

## Listings and sales operations

Added 2026-08-31 from [[70-Operations/meetings/2026-08-31-listings-pipeline-and-ai-cost-consultation]], recording read in full. **Operational counts stated on a call, not pulled from a system**, so each is SINGLE-SOURCE against the person who said it and should be confirmed against Rent Manager or the crawler output before it is used in a report.

| Metric | Value | As of | Source |
|---|---|---|---|
| Rows in the Rent Manager asset listing report | *"about six thousand deep"* | 2026-08-31 | Plaud `16db0fb3adb2bc134f01689b578afb46` |
| MH Village listings crawled nightly, across Parakeet's states | *"all six thousand listings"* | 2026-08-31 | same recording |
| Home preparation time from order to listing | 100 to 120 days | 2026-08-31 | same recording |
| Listing audit flags, at rollout versus now | 50 at rollout, *"a few a day"* now, over 60 days of running | 2026-08-31 | same recording |
| Listing revision trigger used by sales and marketing | 60 to 90 days listed | 2026-08-31 | same recording |
| Price drop referenced as the lever, with outcome not yet measured | 10% | 2026-08-31 | same recording |
| Sources feeding the prospect funnel dashboard | *"like 15 different things"* | 2026-08-31 | same recording |
| Railway server cost to start | *"five dollars"* to *"five bucks"* per month, the consultant's figure | 2026-08-31 | same recording |
| GLM 5.2 cost claim | *"40 times cheaper per token"* at *"the level of Opus 4.8"* | 2026-08-31 | same recording. **The consultant's claim, sourced to Twitter on the recording. Unverified and not a Parakeet figure.** |

**One number on that recording is deliberately not tabled.** John said *"It doesn't even have to fit in a two hundred dollar plan. Like, just can't fit into a twenty five thousand dollar."* Read one way that is a statement about AI spend at a scale that would matter a great deal; read another it is a half-finished sentence. **It is quoted and not interpreted**, because putting $25,000 in this ledger as an AI spend figure on the strength of an unfinished sentence is precisely what rule 3 exists to prevent. The Anthropic console, or Ramp, settles it in one look.

## 2025 tax season, A2Z and Parakeet entities

Added 2026-09-15 by the Page Update from the closes of 2026-09-08 to 2026-09-15. **Every figure is what Citrin or Austin stated in email; none is a reconciled book figure.** The Fund II return sits in its own section above.

| Metric | Value | As of | Source |
|---|---|---|---|
| Returns signed or good to file on the 2026-09-15 deadline | **5**: Founders (overnight), Parakeet Origins I GP 08:41 ET, A2Z MH Fund I 12:56 ET, Parakeet Origins Portfolio I 14:02 ET, A2Z ND Portfolio Partners 15:59 ET | 2026-09-15 | SafeSend signature notices read at the 2026-09-15 close |
| A2Z ND Portfolio Partners, Evergreen distribution in question | **$100,000**; whether it needs a journal entry is unanswered | 2026-09-11 | Citrin (Lisa Timbrook) 2026-09-11, chased 2026-09-14 11:38 and 11:48 ET. `TD-0638`, `KP-0084` |
| A2Z ND Portfolio Partners 2024 return | **Being amended by Citrin** because OPR's 2025 beginning capital will not tie | 2026-09-15 | Austin approved telling Bill Stasiulatis at 16:42 ET. Same shape as `KP-0083` |
| A2Z Community Partners, Miscellaneous Expense to recharacterise | **roughly $165,000** in accounts 51616 and 51904, plus **$311,000** of Consulting to explain | 2026-09-15 | Tim McNamara, Citrin, 15:37 ET. Unanswered. `TD-0657` |
| A2Z Fund One trial balance break | **Located in 2022**, between sheets 1 and 2 of the TB Import | 2026-09-10 | Austin to Citrin 13:24 ET. Citrin cannot open 2021 and earlier workpapers. `TD-0626`, `TD-0603`, `KP-0083` |

## Added 2026-09-26 from the daily closes of 2026-09-22 to 09-25

Added by the Page Update. **Every row is sourced to a daily close, which read the primary message; the primary was not re-opened this run.** The confidence label on each row is the close's own.

| Metric | Value | As of | Source |
|---|---|---|---|
| Lucky Clover sewer tie-in, Brevard County grant reimbursements already booked | **$926,860**, credited to a WIP account with the 2025 treatment unconfirmed. **$742,000** more still to arrive across two properties | 2026-09-22 | Jon Wyss grant accounting memo 17:56 ET, read at `00-Meta/daily-close/2026-09-22.md`. **VERIFIED** as to the memo, not to a trial balance. Jon asked Citrin whether a correction changes any K-1s. `TD-0700` (closed, sent), `KP-0125` |
| Hunter Springs Third Amendment, vacant lot obligation | **$505 a month per vacant lot, capped at $72,720, expired 2026-08-29.** All six lots named; **no rehab or repair language anywhere in it** | 2026-09-21 | Jon Wyss reading the executed Third Amendment 23:13 ET 2026-09-21, recorded at `00-Meta/daily-close/2026-09-22.md`. The Amendment itself was not opened by the close. Corrects the six home rehab reading in the *Kippy dispute* block above, which stays as the counterparty's position |
| Hunter Springs rent credit, contract terms against the booked figure | **$57,570, possibly $64,640, by the contract's terms, against $47,000 booked**, inside the cap | 2026-09-22 | `00-Meta/daily-close/2026-09-22.md`, tail item 1. **INFERRED** arithmetic from the Amendment terms, not a statement from either side. Whether it was recomputed before the new Amendment executed at 16:00 ET is unanswered. `TD-0696` |
| Hunter Springs, credit Larry Brokaw is asking about | **$166,607.05** on a new Due Diligence Expenses account in our 2025 ledger | 2026-09-24 | Larry Brokaw email, preview only, `00-Meta/daily-close/2026-09-24.md`. **SINGLE-SOURCE, his figure, full message not opened.** No written answer as of 2026-09-25. `TD-0713` |
| Walton Street, JREF add on floated | **$10,000,000**, described as "very attractive and doable" and being run up Walton's chain | 2026-09-25 | Jon Wyss in chat 17:25 ET, `00-Meta/daily-close/2026-09-25.md`. **SINGLE-SOURCE and verbal.** A conversation, not a term sheet. `TD-0717` |

**Deliberately not added:** the roughly $106M of JREF II equity implied by Zach Schwartz's asset management fee arithmetic (`TD-0711`, 2026-09-24). Zach's own words on it are *"actually it feels off"* and the fee workbook no longer exists, so it is a hypothesis rather than a figure.

## Added 2026-09-28 from the daily close of 2026-09-26

Added by the Page Update. **Every row is sourced to the 2026-09-26 close, which read the primary message; the primary was not re-opened this run.**

| Metric | Value | As of | Source |
|---|---|---|---|
| Everglades and Royal Palm, Fund II ownership percentage, operating agreement against books | **OA (Word copy) shows 35/65. Books and Citrin's 2024 and 2025 allocations use 20.30% and 21.36%**, from a confirmation Citrin received last year | 2026-09-26 | Tim McNamara, Citrin Cooperman, 00:02 ET, `Bedrock File Follow Up & Intercompany Approach`; Jon Wyss 00:06 ET confirming the 20% figures. **VERIFIED** per the close. **Both kept, not reconciled**, per the contradictions rule. Citrin: *"Ultimately, this is really your call."* `TD-0718` |
| Bedrock I Group, sponsor payment Citrin reads as double counted | **$165,000**, Citrin suggests leaving it on Bedrock I Group as a 2026 correction | 2026-09-26 | Same Citrin message. **Citrin's reading, not a company number.** Not asserted to be the same item as `TD-0657` or the roughly $165,000 A2Z Community Partners miscellaneous expense row above, which sit on different entities and accounts |
| Capitalization threshold before Berman | **$2,500** | 2026-09-26 | Austin in Teams to Jon, 22:49 ET: *"capitalization policy pre berman was 2500"*. **SINGLE-SOURCE.** A past threshold. **The current threshold is unknown**: nothing in this Brain records a figure, who set it or where it is written. Context question 2 on the 2026-09-26 close. `KP-0041` |
| Carley's, trash bill back recovery | **71% recovered**; bulk pickup is not being captured | 2026-09-26 | Jon Wyss and Natalie Magurne, 2026-09-26, per the close. **SINGLE-SOURCE**, the thread was not re-opened here |

**A label conflict on an existing row, kept visible rather than fixed.** The 2026-09-26 row above reads *"Hunter Springs, credit Larry Brokaw is asking about"*. Brokaw's own message, as quoted on `TD-0713` in `10-Business/eos/to-dos.md`, ties the $166,607.05 to *"the wire that hit Royal Oaks' new Evermore account on 4/11/25"* and the thread subject is `Royal Oaks Question`. **So the figure belongs to Royal Oaks, not Hunter Springs**, on Brokaw's words. Both are Kippy portfolio properties, which is how the label slipped. The old row is left as written, per rule 13, and this note supersedes its label from 2026-09-28.

## Intercompany reconciliation, v21 — as of 8/31/2026 book date, computed 2026-09-29

Added 2026-09-29 at the Intercompany project close-out. **Source for every row: the Rent Manager accrual general ledger exports of all 210 books in `C:\Users\AustinBerk\Documents\Claude\Projects\Intercompany\GL Exports\GL 09282026` (every book 9/28, books re-exported after each posting round), run through the project's pair engine; the workbook named on each row holds the tab that shows it.** The project's files carry a 9/30 stamp (UTC clock); the work was done 2026-09-28 to 09-29 ET. These are ledger positions, not accepted by Accounting or Citrin; nothing here is a company-reported figure. Pages: [[80-Finance/intercompany-arap-recon]], `80-Finance/intercompany-operating-rules.md`.

| Metric | Value | As of | Source |
|---|---|---|---|
| Intercompany pairs tested (books with a balance against each other, elimination books out) | **570 pairs; 234 broken** (141 one sided, 93 both sides), 336 match | 8/31/2026 | `Intercompany Matrix 8-31-2026 v21.xlsx`, Summary and Pair Recon. VERIFIED from the exports; engine ties 234 of 234 |
| Gross difference across the broken pairs | **$13,846,039.03** (v20 the same day: $13,864,861.48) | 8/31/2026 | same workbook. Sum of the absolute pair differences, so it is a measure of disagreement between books, not money owed |
| Of which Parakeet vs Parakeet | 140 pairs, **51 broken, $1,789,209.29** | 8/31/2026 | same workbook, Matrix block 1 plus the affiliate block |
| Of which Parakeet vs external | 169 pairs, **6 broken, $236,030.54**: HSMHC/HSRC 67,202.50, HSMHC/PC 41,367.38, A2Z/HSRC 16,300.00, CA/HSRC 6,000.00, HSMHC/KEET 5,160.66 (Hunter Springs, five), KEET/MWMHP 100,000.00 (Meadow Woods EMD) | 8/31/2026 | `GL Compare 8-31-2026 v18 - Parakeet vs External.xlsx`, Summary |
| Of which external vs external | 261 pairs, **177 broken, $11,820,799.20** | 8/31/2026 | `GL Compare 8-31-2026 v18 - External vs External.xlsx`. Not Parakeet's exposure; untouched apart from A2Z/GB, A2Z/GBH and the Fund II pairs |
| 9/30/2026 preliminary, same test | **242 broken, $14,032,269.03**; the gap to 8/31 is PC J26153 "Monthly Simplified Fee" export timing on nine managed books | 9/30/2026 prelim | `Intercompany Matrix 9-30-2026 prelim v17.xlsx`. September open; moves with every posting |
| Entries posted and verified leg by leg by the project | **1 to 146, 168, 169** (plus 32B, 121R; 115R by deletion). Held: 134, 147 to 167 | 2026-09-29 | `GL Compare 8-31-2026 v18.xlsx`, Proposed Entries tab (status and journal number per entry). Austin posts every entry himself |
| PC owes KEET, net, per both books | **$7,703,803.15**, both books agree | 8/31/2026 | `Parakeet Exposure 9-30-2026 v17.xlsx`, memo line. Reimbursement account between the shared bank accounts and the management company, not a loan (Austin 2026-09-24) |
| Outside books owe Parakeet, per Parakeet's books, all Parakeet books | **$4,404,741.88 in, $782,785.23 out**; 109 balances, 44 outside books, 9 owner groups | 8/31/2026 | `Parakeet vs External Settlement Plan 8-31-2026 v1.xlsx`, Legs tab totals. The KEET and PC legs tie to `Parakeet Exposure 9-30-2026 v17.xlsx` per group |
| Settlement, option 1, pay every leg as booked | **$5,187,527.11** moves, 109 payments | 8/31/2026 | same workbook, Summary by owner. PROPOSED |
| Settlement, option 2, net inside each owner group | **$3,623,756.65** moves, nothing paid out by Parakeet; $1,563,770.46 less than option 1, all from set off inside Baker (1,273,991.66), Grove Banyan (221,142.84), A2Z (61,196.64), PO, Fund II, Kippy | 8/31/2026 | same. Needs a netting agreement per owner across separate LLCs. PROPOSED |
| Settlement, option 3, cash still to collect from third parties after paper | **$2,110,593.46**: Baker 882,843.87 (982,843.87 if MWMHP's book is right), Royal Oaks 430,385.69, Crystal Acres 238,967.56, Mayflower 458,866.31, Grove Banyan 73,312.02, PO 26,218.01 | 8/31/2026 | same. Each convertible to a promissory note. PROPOSED, eleven decisions open |
| Net owed to Parakeet by owner group, per Parakeet's books | A2Z group **$1,239,305.80** (Austin's own books); Baker **$882,843.87**; Kippy **$708,327.20** (of which Hunter Springs 38,973.95 per Parakeet, 152,704.49 per Kippy's books, under review); POST / Mayflower **$458,866.31**; Fund II **$233,983.34** (creditor claim in the Close It Down waterfall); Grove Banyan **$73,312.02**; PO **$26,218.01**; Bedrock Group 0.10; Bee's RV (900.00) Parakeet owes | 8/31/2026 | same, Summary by owner. Six legs unproven (the two books disagree) and excluded from any cash figure until proven |
| American, the day one example, at 8/31/2026 | American owes KEET **$860,627.64**, PC **$160,560.40**, PFG **$53,901.96**; American is owed **$536,914.07** by Parakeet Homes (KEETHOME 21166 / AMER 12190); net American owes Parakeet **$538,525.93** | 8/31/2026 | same, Legs tab, and `Parakeet Exposure 9-30-2026 v17.xlsx` BAKER block. Both books agree on every leg. The project brief (mid September) quoted 838,000 / 536,915 from Austin; the 536,914.07 is the same receivable, the KEET figure is the ledger at 8/31/2026 after the posted entries, and the brief's 838,000 was not traced to a specific cut |
| KEET / Lucky Clover | **$541,680.00**, classification break only: KEET J17877 booked equity (14539), Lucky Clover J22047 booked a loan (21148); the 8/1/2025 transfer 5517 to 5222 is on the 5517 August 2025 statement | 8/31/2026 | `GL Compare 8-31-2026 v18.xlsx` KEET-LUCK tab; `Workpapers\JPM_PARAKEET5517_08312025.pdf`. VERIFIED. Loan or contribution is Austin and Jon's call with the CPAs; nothing sent |
| Hunter Springs after the held entries 147 to 167 (sale date cut) | Kippy would owe Parakeet **$2,050.49** on current account, principal on the seller note apart; only A2Z/HSRC 4,741.17 left | 8/31/2026 | `Workpapers\Hunter Springs Sale Date Cut 9-29-2026.xlsx`, Pairs tab. **Rests on Austin's stated working assumption** that the bank statements from 9/2024 belong to HSMHC; entries held, to the internal reviewer |

## Intercompany reconciliation, v22 — 8/31/2026 restated and 9/30/2026 as pulled, computed 2026-10-03

Added 2026-10-03 after the 9/30 close pull. **Source for every row: the Rent Manager accrual general ledger exports of every book (230 files, 210 with lines, 3,593,642 lines) in `C:\Users\AustinBerk\Documents\Claude\Projects\Intercompany\GL Exports\GL 10032026`, pulled 10/3/2026, run through the project's pair engine; the workbook named on each row holds the tab that shows it.** KEET, KEETII, JBJ and SOUTH first exported on cash basis and were re-exported on accrual the same morning; the ledger holds the accrual files. Whether Accounting has locked September is not confirmed, so the 9/30 rows are "as pulled 10/3", not a close. Ledger positions, not accepted by Accounting or Citrin. Pages: [[80-Finance/intercompany-arap-recon]], `80-Finance/intercompany-operating-rules.md`; project doc claude/refresh-v22-10-3-2026.md.

| Metric | Value | As of | Source |
|---|---|---|---|
| Intercompany pairs tested, 8/31 restated | **570 pairs; 235 broken** (141 one sided, 94 both sides), 335 match | 8/31/2026 | `Intercompany Matrix 8-31-2026 v22.xlsx`, Summary and Pair Recon. VERIFIED; engine ties 235 of 235 |
| Gross difference across the broken pairs, 8/31 restated | **$13,830,962.65** (v21: $13,846,039.03) | 8/31/2026 | same workbook. Moves against v21: BEDROCKGRP/VV 31,500 closed (VV J26398); KEET/WBH and KEET/WOLF 8,211.81 each opened by the entry 78 rollback (entry 170 closes them at 9/30); AMER/NALLS to net only (J26181) |
| Of which Parakeet internal and affiliates | 140 pairs, **51 broken, $1,789,209.29** (130 / 44 / 1,638,773.35 and 10 / 7 / 150,435.94), unchanged | 8/31/2026 | same workbook, Matrix blocks 1 and 2 |
| Of which Parakeet vs external | 169 pairs, **8 broken, $252,454.16**: the five Hunter Springs pairs and KEET/MWMHP as in v21 (236,030.54) plus KEET/WBH (8,211.81) and KEET/WOLF 8,211.81 | 8/31/2026 | `GL Compare 8-31-2026 v19 - Parakeet vs External.xlsx`, Summary |
| Of which external vs external | 261 pairs, **176 broken, $11,789,299.20** | 8/31/2026 | `GL Compare 8-31-2026 v19 - External vs External.xlsx` |
| Same test at 9/30/2026, first full set | **570 pairs; 235 broken** (142 one sided, 93 both sides), **$14,293,011.51**; Parakeet vs external **6 broken, $236,030.54**; external vs external 178 broken, $12,267,771.68; Parakeet internal and affiliates as 8/31 | 9/30/2026 as pulled 10/3 | `Intercompany Matrix 9-30-2026 v19.xlsx`, Summary; tab "Aug 31 to Sep 30" lists every pair that moved. The J26153 fee timing of the prelims is gone |
| Pair differences that moved 8/31 to 9/30 (none ours) | EG/FUNDIILP 0 to **193,173.75** one sided (FUNDIILP J25999 9/30, Everglades extinguished, reg 6.09); A2ZPM/FUNDIILP 8,960.56 to (126,039.44) and A2Z/FUNDIILP (28,275.70) to 106,724.30 (FUNDIILP J26211 9/29, **135,000** between the A2ZCP and A2ZPM payables); BOVI/OCEANPO **50,000** and BOVIPO/OCEAN (50,000) (J26441 9/2 cash transfer booked to the pre PO names, wrong side); FUNDIILP/RP 10,228.75 closed; KEET/WBH and KEET/WOLF closed (entry 170) | 9/30/2026 | same tab. VERIFIED from both books' lines; the three Fund II items belong to the Close It Down log; J26441 is Outstanding List question 14 (proposed reclass, nothing cut) |
| Entries posted and verified leg by leg by the project | **1 to 146, 168 to 170** (plus 32B, 121R; 115R by deletion; 78 rolled back and replaced by 170). Held: 134, 147 to 167 | 2026-10-03 | `GL Compare 8-31-2026 v19.xlsx`, Proposed Entries tab; check row 5,653,393.13 balanced |
| PC owes KEET, net, per both books | **$7,703,803.15** at 8/31 and at 9/30, both books agree | 9/30/2026 | `Parakeet Exposure 9-30-2026 v18.xlsx`, memo line on both tabs |
| KEET's intercompany book, net | **$2,133,928.44** at 9/30 (v16 at 9/28: $1,893,928.44; the move is SILVER +335,000 in September bank transfers, AMER (40,000), WPMA (40,000), MON (15,000)); PC **($8,620,303.16)** unchanged | 9/30/2026 | `Intercompany Balance Map KEET PC 9-30-2026 v17.xlsx` (KEET 80 lines, 59 agree; PC 83 lines, 56 agree) |
| Outside groups, per Parakeet's books, 8/31 to 9/30 | A2Z 746,247.86 unchanged; Baker 1,351,886.84 to **1,258,146.84** (American and WPMA paid KEET 40,000 each, Monson 15,000, PC fees); Kippy 674,902.36 to 676,187.36; POST 458,866.31 to 459,181.31; Fund II 233,870.62 to 234,545.62; Grove Banyan 59,562.03 to 60,912.03; PO 26,218.01 unchanged | 9/30/2026 | same workbook, group totals on the two tabs (KEET + PC columns). These are the Exposure workbook's KEET + PC groupings; the Settlement Plan's per owner figures (Baker 882,843.87 etc.) are a different cut of the same ledger (every Parakeet book, unproven legs excluded) and were not re-run on 9/30 yet |

## Intercompany reconciliation, v24 — 8/31/2026 locked, 9/30/2026 open, computed 2026-10-06

Added 2026-10-06. **Source for every row: the 10/3 ledger above with 83 books replaced by their 10/6 re-exports (`GL Exports\GL 10062026`: 82 books re-exported after a 9/30 balance sheet export of every book was screened against the 10/3 ledger, plus KEETII's GL sent in the chat the same evening); 3,594,500 lines, every (book, account) sums to its running balance, 0 exceptions.** Austin 10/6: August is locked, September is open and being finished for quarter end; so the 8/31 rows are final unless Accounting posts into the locked month (it did, see the row below) and the 9/30 rows move with every posting. MWMHP and ROYAL moved on the screen and were not re-exported; their September PC fees (2,151.75 and 1,210.89) are one sided here. Ledger positions, not accepted by Accounting or Citrin. Pages: [[80-Finance/intercompany-arap-recon]], `80-Finance/intercompany-operating-rules.md`; project doc claude/refresh-v23-10-6-2026.md.

| Metric | Value | As of | Source |
|---|---|---|---|
| Intercompany pairs tested, 8/31 | **570 pairs; 226 broken** (141 one sided, 85 both sides), 344 match | 8/31/2026 | `Intercompany Matrix 8-31-2026 v24.xlsx`, Summary and Pair Recon. VERIFIED; engine ties 226 of 226 |
| Gross difference across the broken pairs, 8/31 | **$13,566,457.79** (v22: $13,830,962.65). The whole move is the nine BOVIPO / sibling PO pairs closing (264,504.86): Accounting re-pointed BOVIPO J24628 (6/9/2026) in place to the accounts entry 172 proposed, read in the 10/6 re-export | 8/31/2026 | same workbook, tab "v23 to v24" (with the v22 to v23 reading). KEETII/PC broke by 56,966.62 in the 82 book set and closed again when KEETII's GL came in |
| Of which Parakeet internal and affiliates | 140 pairs, **51 broken, $1,789,209.29**, unchanged since v22 | 8/31/2026 | same workbook, Matrix blocks 1 and 2 |
| Of which Parakeet vs external | 169 pairs, **8 broken, $252,454.16**, unchanged (five Hunter Springs, KEET/MWMHP, KEET/WBH, KEET/WOLF) | 8/31/2026 | `GL Compare 8-31-2026 v21 - Parakeet vs External.xlsx`, Summary |
| Of which external vs external | 261 pairs, **167 broken, $11,524,794.34** (v22: 176 and $11,789,299.20) | 8/31/2026 | `GL Compare 8-31-2026 v21 - External vs External.xlsx` |
| Posted into the locked August after the 10/3 pull (none ours) | PC and KEETII **J26541** 8/31/2026, the August Hold Co II asset management fee **$56,966.62** (PC Dr 12199 / Cr 47201 44,550.45, 47205 12,416.17; KEETII Cr 21147 / Dr 53501), both sides, pair matched; POPIGP J26488 8/31 GP distribution **$100,000** (equity, A2Z 50,000 and GBP 50,000); A2Z J26540 8/6 (3,604 bank reclass) and an 8/10 ACH (699.28); A2Z family receivable accounts renumbered (12003 to 12241, 12001 to 12239, 12002 to 12240), same amounts; one tenant charge removed on each of MCG (50.00, 8/6/2026) and SSS (610.00, 11/1/2025) | 10/6/2026 | tab "v23 to v24" section 2 and `GL Compare 8-31-2026 v21.xlsx` Ties (2 10/6), every line listed with a reading. VERIFIED from the line diff of each re-export against its 10/3 state. Outstanding List question 15 |
| Same test at 9/30/2026 | **570 pairs; 248 broken** (148 one sided, 100 both sides), **$13,971,067.23** (v19 at 10/3: 235 and $14,293,011.51); Parakeet internal and affiliates **53 broken, $1,804,233.54**; Parakeet vs external **28 broken, $263,566.87**; external vs external 167 broken, $11,903,266.82 | 9/30/2026 (open) | `Intercompany Matrix 9-30-2026 v21.xlsx`, Summary; tab "Aug 31 to Sep 30" lists every pair that moved; tab "Postings 10-6" every changed line |
| New September breaks, found in the 10/6 re-exports (none ours) | PC's September fee journal **J26535** billed the ten PO parks on the pre PO receivables while the PO books credited 21147 (**$11,892.97**, twenty pairs) and billed Meadow Woods' fee (**$2,151.75**) to Mayflower's receivable (the two template errors entries 95 and 72 fixed once already); **J26520** 9/24 "Reimbursement to PC from KEET" **$200,000** from fourteen parks' shares of the 5222 account, Shady Oaks' leg on 21148 (KEET) instead of 21147 (PC), **$7,706** (SO/PC and SO/KEET); ROYAL's **$1,210.89** fee one sided (not re-exported) | 9/30/2026 | same tabs. VERIFIED on both books' lines. Entries 174 (SO), 175 (PC, ten PO fees) and 176 (PC, Meadow Woods) proposed 2026-10-06, dated 9/30/2026, held in `RM Imports\Held` for Austin's go |
| Entries done by Accounting editing the journal in place (read 10/6) | **171** (OCEANPO and BOVIPO J26441 9/2/2026, **$50,000**, re-pointed to 21188 / 12233) and **172** (BOVIPO J24628 6/9/2026, **$264,504.86**, 18 credits re-pointed from 21188 to 12225-12233). Same result as the proposed entries; nothing imported. **173** (KEET Dr 12192 / Cr 32000 **$100,000**, 9/30/2026) NOT posted as of the 10/6 KEET export | 2026-10-06 | `GL Compare 8-31-2026 v21.xlsx`, Proposed Entries tab (171 / 172 DONE BY EDIT, 173 CUT, 174 to 176 PROPOSED); check row **6,139,648.71** balanced |
| KEET to PC bank transfers in September | **$345,000** (J26521 9/9 **$245,000** from FRB 5517; J26522 9/28 **$100,000** from JPM 5222), booked KEET 12160 receivable / PC 21148 payable on both books, pair still matched | 9/30/2026 | `Intercompany Balance Map KEET PC 9-30-2026 v19.xlsx`. VERIFIED both books. Outstanding List question 17: the rule says shared account cash is reimbursement, not a loan |
| PC owes KEET, net, per both books | **$7,703,803.15** at 8/31 (unchanged); **$8,048,803.15** at 9/30 (the 345,000 above), both books agree | 9/30/2026 | `Parakeet Exposure 9-30-2026 v20.xlsx`, memo line on both tabs |
| KEET's intercompany book, net | **$2,476,428.44** at 9/30 (v17: $2,133,928.44; the 345,000 to PC less Mayflower's 2,500 repayment J26487); PC **($8,768,862.89)** (v17: ($8,620,303.16)). KEET 80 lines, 58 agree; PC 91 lines, 41 agree (the new disagreements are the PO / pre PO fee accounts, Mayflower, Royal Oaks, Shady Oaks) | 9/30/2026 | `Intercompany Balance Map KEET PC 9-30-2026 v19.xlsx` |
| Outside groups, per Parakeet's books, 9/30 | A2Z **746,247.86** unchanged; Baker **1,263,511.22** (8/31 1,351,886.84); Kippy **678,059.84** (674,902.36); POST (Mayflower) **460,646.06** (458,866.31); Fund II **235,851.15** (233,870.62); Grove Banyan **63,226.03** (59,562.03); PO **38,110.98** (26,218.01; the 11,892.97 is the J26535 template error, PC's side only) | 9/30/2026 | same workbook, group totals (KEET + PC columns) |

## Known gaps — flagged, never guessed

- **Occupancy is unreliable on five properties.** Great Oak RV Resort, Paradise Lakes, River Oaks RV Resort, Nalls Court and Hendersons all read 0%. Confirmed by Austin on 2026-08-30 as a data gap rather than reality. They are excluded from the weighted occupancy figure above.
- **The Property Data Sheet's "Total Units" column reads 40 on every row.** Broken. Never use it; use Total Core Units.
- **The 2026 rents disagree between two workbooks.** The Property Data Sheet and the 2026 Rents + Mkt Rents workbook differ on several properties, including Belle Haven, Druid Oaks, Oakside and Parkwood.
- **The Origins block in the rents workbook is annotated 2025, not 2026,** unlike the other two portfolio blocks.
- **The same properties carry different portfolio labels in four different workbooks.** The 10 Origins properties appear as Origins, BEDROCK FUND II, Legacy and Fund II.
- **The infill workbook disagrees with itself.** Sheet1, grouped by portfolio across 58 properties, gives a 675-occupant gain target (JREFI 292, JREFII 277, Origins 106) and 675 vacant lots. Sheet2, per property across 51 properties, gives a 661 goal against 925 total vacancy, and 484 Infill & Sell against Sheet1's 498. Rehab & Sell (142) and Sell (35) agree. The deck echoes Sheet1 but states JREFII as 263, not 277. Nothing says which sheet governs.
- **The KPI names and the numeric targets live in two different files and are not reconciled.** A scorecard with metric names and no targets cannot be scored. See [[10-Business/eos/scorecard]].
- **No LP count exists for Bedrock Fund II** in any of the five investor documents.
- **No loan or mortgage documents are filed anywhere,** so the debt terms in the board deck have no supporting agreements in this vault. A 74-loan schedule exists only as archived raw material.
- **Individual compensation is deliberately not recorded anywhere in this Brain.** The board deck holds a named salary and bonus table on page 63 and per-person equity awards on pages 65 to 66. Nothing from those pages is reproduced here.
- **Headcount by property or region exists nowhere.** The payroll workbook is expressed only in dollars, dollars per pad and percent of revenue.
- **The payroll workbook's own two tabs disagree on 17 properties,** and 12 allocation rows have no counterpart in the current Property Data Sheet.
- **The Employee Handbook carries no effective date, revision date or version number.** The only date in 61 pages is an e-signature timestamp of 2024-08-29.
- Unconfirmed as of 2026-08-31: Alex Pontes's start date; whether the SR region territory is being redrawn; the status of the standalone RV websites and the Parakeet Retreats page.
| Bedrock Fund II transfers, CS Partners IV to individual transferees | **7**, effective 2022-01-01 | 2026-08-30 | `WP-38 Investor Records Integrity Review`, quoted in `/Austin Berk/BMHCII/2. Investor Records/Archive_Superseded/_WHY THESE ARE HERE.txt`. Corrects a withdrawn memo that asserted none occurred |
| Bedrock Fund II second-tranche subscriptions | **5 limited partners, $498,548 total**, between 01/2019 and 07/2020 | 2026-08-30 | same source. Corrects a withdrawn memo that asserted none were accepted |
| BMHCII memorialization vault, total contents | **1,513 files, 181 folders, 1.29 GB** | 2026-09-03 | full depth listing of Dropbox ns:15029193027, every page confirmed complete. `1.8 Subscription Agreements` alone is 179 files / 204,703,717 bytes; `4.5 Tax Returns` is 989 files |
| BMHCII files opened during the 2026-09-03 audit | **fewer than 150 of 1,513, under 10%** | 2026-09-03 | audit coverage statement. **Every completeness figure below is a floor, not a total** |
| Bedrock Fund II LP capital contributions, Jan to Nov 2018 | **$10,063,750 across 54 contribution events** | 2026-09-03 | `1.8/LP Pref Schedule_012019.xlsx`, extracted cleanly |
| Bedrock Fund II investor accounts on the authoritative roster | **68 distinct accounts, 70 rows** | 2026-09-03 | `2.1 Investor Schedule/bmhciilp positions.xlsx`, accounts 1001 to 1069 |
| Bedrock Fund II investors with no subscription agreement anywhere reachable | **12**, of which 5 are primary subscriptions rather than transferees | 2026-09-03 | audit LP roster lane, vault and the older Dropbox tree both searched |
| Bedrock Fund II 2025 Schedule K-1s | **0 final. 68 per investor draft letters dated 2026-08-06 stand in their place** | 2026-09-03 | `4.5 Tax Returns/2025_K-1_BMHCII_Draft Letter`. Filing deadline 2026-09-15 |

| SharePoint Online tenant usage against entitlement | **6,550.52 GB used against 2,394 GB, 274% of quota** | 2026-09-07 | Microsoft tenant notice `no-reply@sharepointonline.com`, 18:12 ET. VERIFIED. `KP-0100` |
| Parakeet MHC uncollected AR | **roughly $5,000,000 plus**, named as what must be collected to fully fund ongoing infill | 2026-09-07 | David Berman in email, his own approximate figure. **SINGLE-SOURCE, no schedule behind it.** `CM-31`, `KP-0101` |
| Cash recovered on the remaining Tarheel Portfolio stake | **roughly $2,000,000 plus**, autumn 2025 | 2026-09-07 | David Berman in email, his own approximate figure. **SINGLE-SOURCE.** `CM-31` |
| AvidXchange invoice unassigned longest | **$108,919.00**, A & A Development Inc. invoice 3452, invoice date 2026-04-02, entered 2026-04-08, still in Pending WorkFlow Assignment | 2026-09-07 | AvidXchange daily `_Invoices in Pending WorkFlow Assignment` report. VERIFIED. `TD-0609` |

| Key Bank defeasance premium, 12/30/2025, loan 10222238 | **$147,831.28 net**, securities over principal, split across the six Fund II ledgers as filed in 2025 | 2026-09-17 | Austin Berk to Lisa Timbrook at Citrin Cooperman, Outlook Sent Items `Re: Big Tax Push Breather` 19:58 UTC. **SINGLE-SOURCE**, his own figure, not traced to a statement. `CM-35` |
| Tarheel deferred 1031 gains recognised at 2/28/2026 | **$5,151,983.30 total**: Cedar Grove $1,913,377.17, Colonial $1,071,639.62, Lambeth $897,160.12, Parkwood $1,269,806.39. Vandemere's $1,120,199.44 was taken into income at 12/31/2024 and is excluded | 2026-09-17 | same message. **SINGLE-SOURCE**, Austin's own figures, offered to Citrin for confirmation rather than confirmed by them. `CM-35` |
| Bedrock fund level income pickups never taken at the Fund | **roughly $8,900,000** of property income, across the 2025 sale gains at the Fund's ownership percentages, the 2024 Vandemere and Valley View deferred gain recognitions and the 2026 Lambeth and Parkwood gains, net of 2021 to 2024 pickups taken at 100% where Grove Banyan owned a piece | 2026-09-17 | same message. **SINGLE-SOURCE and explicitly unbooked.** Austin: *"the year each one lands in drives the partner capital accounts, so I want your read before we book them."* `CM-35` |
| 21st Mortgage escrow funding | **$250,000, released 2026-09-17** | 2026-09-17 | Moe Mehmood *"Pending release in JPM. $250K"* 15:24 UTC, Austin *"Wire has been released"* 16:41 UTC. **VERIFIED** from both messages. Receipt by 21st is not evidenced. `TD-0666` closed |
| Lucky Clover sewer change orders, High Pace, dated 2026-09-10 | **$304,841.00 across three**, of which **$179,200.00 is unfunded and carried by nobody**: 128 unit connections at $1,400.00 each, profit and overhead waived, insurance only. The other two are absorbed elsewhere: **$95,641.00** for the lift station elevation conflict, paid by the engineering firm as its own error and omission, and **$30,000.00** for the septic C1 decommissioning, covered by High Pace and two subcontractors | 2026-09-18 | Mark Doucette, High Pace Construction, to John Clark and Auzzi Dixon 2026-09-10 23:39 ET, forwarded to Austin and Jon 2026-09-18 17:54 ET. **VERIFIED**, the message read end to end. **Dated as a thirty day invoice, so it runs to approximately 2026-10-10.** `TD-0678`, `KP-0118` |
| Lucky Clover sewer change order, the covering summary that does not reconcile | John Clark's forward states the engineer covered *"about 25% of the original change cost for approx.. $350K"*. **The underlying email totals $304,841.00 and the engineer's share is $95,641.00, which is 31% of it.** Neither the $350K nor the 25% appears in the primary document | 2026-09-18 | Same two messages, both read. **Both figures kept with their dates rather than reconciled**, per the contradictions rule; the primary document governs per rule 16 |
| Triad inventory insurance, the method for cost per home | **Unit or location total value x .01 x rate = premium**, with the community address rate included and rates varying by location. Worked example supplied for Parakeet Home Sales at Applegate: $465,063.50 x .01 x 0.219 = $1,018.49 location premium; vacant rate 0.219, rental rate 0.287 | 2026-09-18 | Katelyn Houseworth, Triad Financial Services, Outlook Inbox 15:07 UTC. **VERIFIED**, message read in full. This is the method Jon asked her to confirm for budgeting, not a Parakeet-computed figure. `TD-0677` |
| Parakeet WIP, open balance and clearing history | **roughly $10,800,000 sitting open in WIP.** Cleared in 2025: **37 projects, roughly $744,000 reversed out.** Cleared so far in 2026: **2 projects, roughly $7,000.** | 2026-09-21 | Jon Wyss, intercompany thread and Teams, afternoon of 2026-09-21, read at the 2026-09-21 close. **SINGLE-SOURCE, Jon's own figures, not tied to a trial balance pull.** He named the mechanics behind the balance rather than the backlog: quarterly clearing, bills posted inconsistently to WIP against checks written straight to it, and no separate depreciation schedules on tie-ins that mix roads and lift stations. `KP-0041`, `TD-0685`. Carried into the 2026-09-22 Citrin conversation |
| Lamberton Lake sale, seller redline terms added by Parakeet's own counsel | **Liability cap $100,000, floor $10,000**, added by Christopher Hoke to the Crystal View PSA redline | 2026-09-21 | Christopher Hoke, Woods Oviatt, to Austin 13:24 ET, read at the 2026-09-21 close. **VERIFIED** as to the message; **the redline itself was not opened**, so nothing else in the document is asserted. Hoke expects the buyer to push back on both. `TD-0691` |
| MHVillage card limit increase requested by Leslie Croft | **$7,500 requested, not ruled on.** The card is the Ramp virtual card Austin created for Leslie and Melanie on 2026-08-27 so open house spend would not hit their individual limits | 2026-09-19 | Leslie Croft to Austin 07:14 ET 2026-09-19, read at the 2026-09-19 close; the card identification is Austin's own words in `00-Meta/commitments.md` from 2026-08-27. **A request, not an approval.** `TD-0682` |
| Kippy dispute, counterparty's written rehab claim at Hunter Springs | **Six homes, Lots 1, 5, 9, 21, 22 and 25, at $30,000 to $40,000 a lot, delivered on or before 2026-12-10, extended from 2026-11-15.** Position of Kippy's counsel, attributed to a conversation with Austin. Parakeet's internal read the same week: Jon, five not six (Lot 21 resident owned, confirmed by title pull 2026-09-18); Natalie, 1, 5 and 25 are vacant lots and the rehabbed set is 8, 9, 13, 18, 19 and 20, so only Lot 9 ties | 2026-09-17 | Adam Steinberg email 19:11 ET 2026-09-17, quoted in full on `10-Business/eos/to-dos.md` and re-quoted by Jon in Teams 14:31 ET 2026-09-21. **A negotiating position, not a company number, same convention as the Kippy block above.** The internal lot dispositions are Natalie's recollection in chat, SINGLE-SOURCE, not a rent roll pull. `CM-24` |
