# Payroll model

**What this is:** how payroll is allocated to properties — a 5%-of-revenue benchmark rather than a headcount build-up — the properties that break it, the two allocation methods that coexist, and the defects that make parts of the workbook unusable as it stands.

**Status:** current — 2026-08-30. Source workbook `Payroll Breakdown Allocation by Property.xlsx`.

## The facts

### The model

- **Payroll is benchmarked to 5% of property revenue, not allocated by headcount.** Each property carries a 5% target against its revenue basis, and the annualised allocation is compared to it.
- **Portfolio totals (2026 revenue basis):** revenue **$54,487,005.11**; 5% benchmark **$2,724,350.26**; annualised allocation **$2,900,824.79**; net surplus reported as **$40,705.48**.
- **Pad count 5,640; average salary per pad $514.33.** "Pad" is the workbook's word for a lot — in the field, a pad means concrete. Read every "pad" figure here as per-lot.
- **The reported net surplus is an artefact.** Allocation exceeds the 5% benchmark by $176,474.53 in total, yet the surplus column reports a positive $40,705.48 — because deficits are zeroed out on every non-JREF row (see defects below).

### Two allocation methods coexist

- **KEET and KEET II** (the JREFI and JREFII portfolios) are **charged at 5% of revenue, with the excess booked as payroll overage.**
- **Baker, Fund II, Kippy, Post, Single Asset (SA), Corporate and Geiger** are **charged at actual and fully reimbursed** — no overage is calculated for them.
- Geiger is the exception inside the exception: its method cell reads `#N/A` rather than "Actual", so no method is applied to it at all.

### Where the model breaks

- **Terrace Crossings** — allocation is **25% of revenue** at **$3,067.11 per pad**, a **$158,775.30 deficit** against benchmark. The worst row in the workbook.
- **Lake Saunders** — **32% of revenue**, **$2,643.67 per pad**, a **$104,926.08 deficit**.
- **A cluster around $46–47k of deficit each:** River Oaks $47,412.93 (12% of revenue, $753.50 per pad), Lucky Clover $47,335.11 (8%, $1,041.31), Vantage Oaks $47,212.49 (8%, $513.52), Belle Haven $46,446.06 (11%, $884.01).
- **Lowest cost per pad:** Druid Oaks **$134.38**, Shady Acres **$138.17**, Great Oak **$140.92** — all three at 2–3% of revenue.
- **Highest allocation as a share of revenue sits in the non-JREF portfolios, where no overage is ever calculated:** Crystal Acres 31%, Lamberton Lake 28%, Gulf Breeze 18%, Palm Spring 10%.

### November 2025 actuals

- **Salary $404,077.19 plus health insurance $32,561.14 equals $436,638.33** for the month.
- **The Corporate row alone is $221,762.42 — about 51% of the total — and is fully reimbursed.** It carries a pad count of 1.
- Geiger Key shows $20,990.38 of salary against **negative $919.96 of health insurance**.

### Defects to record

- **The Surplus/(Deficit) column is hardcoded to zero for every non-JREF portfolio row**, including rows running 18% to 31% of revenue. The model cannot see a deficit outside JREFI and JREFII.
- **Six properties show $0 allocation despite carrying revenue:** Greene Pointe ($713,574), Congress ($435,348), Northgate MH ($1,929,805), Paradise Palms ($348,796), The Oaks ($2,024,934), Silver Hill ($1,068,744). Their whole 5% benchmark falls straight into the surplus column as a false positive.
- **`#DIV/0!` errors on three rows** — Hunter Springs, Henderson's and Nalls Court, all with zero revenue.
- **An `#N/A` on the Geiger Key row of the November analysis propagates into the Payroll Reimbursement and Payroll Overage totals**, so neither month-level total computes.
- **The Total Revenue column is zero on every row of the November analysis**, so "Overage % of Revenue" reads 0.00% throughout — the column exists but measures nothing.
- **Headcount appears nowhere in the workbook.** There is no employee count, no FTE column and no per-property staffing table anywhere in it, so the model cannot be reconciled to who is actually on site.
- **The workbook's own two tabs disagree on pad counts for 17 properties.** The November analysis and the 2026 allocation sheet differ on Applegate (87 vs 88), Auburn Ridge (160 vs 157), Brunswick (65 vs 62), Carley's (71 vs 75), Geiger Key (36 vs 0), Great Oak (230 vs 198), Hunter Springs (25 vs 0), Lake Wales (39 vs 47), Lucky Clover (128 vs 121), Shady Acres (219 vs 213), Triple S (233 vs 234), Windward Knoll (155 vs 154), and five more by one lot each.
- **Twelve properties in the allocation sheet have no counterpart in the current Property Data Sheet** — Bay Oaks Village I and II, Geiger Key, Gulf Breeze, Hunter Springs, Lake Wales, Oceanaire, Ormond Beach, Palm Spring, Town & Country, Westwood and Wolf Bay — so the pad basis for those rows cannot be checked against the portfolio record.
- The March 2026 board deck records the payroll model as **rebuilt** in the six months to March ("REBUILT ENTIRE PAYROLL MODEL — Real-time and robust allocation of payroll & healthcare expenses by property and geography"). The defects above are in the rebuilt version.

## The payroll reconciliation rebuild, working record (from Claude memory)

**Why this section exists.** Moved verbatim on 2026-09-29 from Claude's memory (the Payroll Model project file, last written 2026-09-22), Phase 1 of `00-Meta/brain-architecture.md`, so every agent reads it here instead of in one project's memory. `[stated]` lines are Austin's own rulings. Figures below are the working record as written at the time, not ledger entries; `00-Meta/numbers-ledger.md` stays the only place a number is trusted from. Where this section and the page above disagree, both stay visible and the newer dated line wins.

- [stated] Rebuilding a payroll reconciliation model to understand cash flow and allocate employees correctly across the organization
- [stated] The old "Payroll Model - DB.xlsx" (SharePoint, HR/Payroll/Parakeet Payroll Allocations/DB/) was created long ago, David broke it and it's no longer used — but it's the concept being rebuilt
- [stated] Goals: verify cash in and out of the account, and project the impact of hiring/firing employees across the portfolio on overall payroll and ultimately on Parakeet's own balance sheet
- [stated] Source data = payroll provider (Paychex) reports; allocation dimension = property/community; files go back to 2021 but focus is 2025–2026; wants both an Excel workbook and a live sheet version
- [stated] Cash Requirement files live in the OneDrive-synced SharePoint tree C:\Users\AustinBerk\OneDrive - Parakeet Communities\Parakeet Communities\Human Resources\Payroll, in folders titled by year; he was moving copies to C:\Users\AustinBerk\Documents\Claude\Projects\Payroll Project
- [stated] 2026-09-17 go-forward decision (superseded on the journal point 9/18): the per-check-date payroll tie-out runs on the Cash Requirements PDF + bank transactions, with allocation on the quarterly Paychex Labor Cost pull
- [stated] 2026-09-18: the payroll journals are the per-employee source for tie-outs; after the 9/18 PM folder reorg Austin approved, Paychex source files live in \Payroll\<year>\ (with the Payroll Journals subfolders), delivered workbooks go in \Claude outputs\, and Kelly Benefits health insurance statements he saves in \Health Insurance\ — all inside the Payroll Project folder
- [stated] 2026-09-17 approved the Cash Req + Bank tie-out template ("this is what we need"), asking it to also break down by employee with a total Parakeet payroll cost column
- [stated] Parakeet runs insurance allocations separately from payroll, so the EE-withheld insurance amounts that never draft must be broken out per employee to show true cost when allocating
- [stated] 2026-09-17 source-of-truth rule: do not reference David's files — the only files to reference are the ones in the Claude Projects Payroll Project folder (C:\Users\AustinBerk\Documents\Claude\Projects\Payroll Project); accurate files will be moved there and it is the going-forward system
- [stated] 2026-09-18: added a "Bank Statements" folder inside the Payroll Project folder — bank statements will be saved there going forward
- [stated] 2026-09-18: ER taxes must be allocated per employee (prorated; Austin approved gross earnings as the proration base) and added into each employee's Total Parakeet Cost
- [stated] 2026-09-18: keep old-model references and old-model variance comparisons OFF the payroll dashboard — Austin will address the old model and the variances later (they remain tracked as open items in the project status doc)
- [stated] 2026-09-18: bringing Kelly Benefits health insurance invoices into the model — run the analysis combined with payroll, but change Rent Manager booking from past practice to book payroll and insurance separately
- [stated] 2026-09-18: will restate the 2026 payroll numbers and rebook the Rent Manager entries (restatement back to January, not go-forward)
- [stated] 2026-09-18 (evening) architecture decision: the calculation is a skill/pipeline, Excel is the output, the Rent Manager import is a byproduct — "let's start building i like your idea"; AllocationModel_2.1.xlsx (root of Payroll Project folder) is the spec, not the live model
- [stated] 2026-09-18: the reference table (employee→property assignments + property master) is maintained by HR going forward — HR will save or send a file with allocation changes and staff additions/subtractions; "otherwise all else stays the same for the check period"
- [stated] 2026-09-18: wants the artifact to be a dynamic model for Jon and him that analyzes the overage — rotations, hires etc. brought to them get entered so they see the effect before approving (Overage Model artifact: https://claude.ai/artifact/2bLjGEsmgQ53cC4KZGCnbN)
- [stated] 2026-09-18: keep an audit file of where every data point comes from so feeds can become seamless (Reference\Data Lineage.xlsx)
- [stated] 2026-09-18: the 5% payroll recapture base is ALL property-level Rent Manager entities (utility, RV, opco, etc.), not hold cos like KEET / KEET II
- [stated] 2026-09-18: January 2026 payroll had rollover from 2025 as well as into February 2026 (explains Jan/Feb differences between the Paychex Labor Cost pull and the check-date tie-outs)
- [stated] 2026-09-18: wants a meeting with Demetria on Tuesday (9/22) to discuss the allocation process (the five 2026 hires with no assignment)
- [stated] 2026-09-18: the Ops Dashboard v3 wireframe artifact (https://claude.ai/artifact/HqQQ4iTB9Vtndcpo1JLGzB) is the format for these artifacts and dashboards going forward — show data source, calc descriptions and logic (spec cards, feed badges)
- [stated] 2026-09-18: coverage goal for payroll recapture is 85%; wants the recapture chart with a water image (rough water on expense, calm on income) shaded in Parakeet green/red by level vs the 85% goal
- [stated] 2026-09-18: scenario tool must allow adding communities and revenue (pipeline with closing dates, budget and business plan), a 12-month forecast and a 12-month cash flow model; optionally sales roles on low base + commission projected on sales and infills
- [stated] 2026-09-18: wants to queue multiple moves before running the financial impact; property selection as a dropdown ("condensed format we are moving to"); rotation/reassign should show dynamic reductions and increases across the multi-selected properties
- [stated] 2026-09-19: the 2027 budgets were just finished (week of 9/14) and are coming — they will feed the model's income side once the file arrives
- [stated] 2026-09-19: the New community form on the Overage Model is the acquisition pipeline entry for now; link to Jon's pipeline later
- [stated] 2026-09-19: found the 85% coverage-goal pushback (blended vs 5%-properties-only) interesting; will think about it
- [stated] 2026-09-19: wants the monthly Rent Manager import export for the allocations as a standing output file (draft built at Claude outputs\RM Import\; GL map needs accounting confirmation)
- [stated] 2026-09-18 scope: 2026 only for now — 2025 and earlier parked ("we aren't doing 25 yet we will redo later if we want to go back that far"); he deleted the old 3.13.25 template workbook accordingly
- [stated] 2026-09-19: AllocationModel_2.1 now holds all bank-reconciled payroll journals per check date (Jan–Aug, 21 dates) and is the tie-out reference for the rebuild (comparison workbook: Claude outputs\Model Comparison 2.1 vs Rebuild Jan-Aug 2026.xlsx)
- [stated] 2026-09-19: August allocations aren't in the system yet — for anything that must match RM, use July or stop at 7/31
- [stated] 2026-09-20: AllocationModel_2.1 is frozen — nobody touches it but Austin; kept only to compare against the rebuild until the rebuild's own proof (Proof tab in the Baseline workbook) has run for a few months, then 2.1 gets deleted; "whatever we amend the procedure to is what it will be"
- [stated] 2026-09-20: wants a toggle for the 85% coverage reading (blended vs 5% properties only) — "important distinction" (added to the Overage Model header + Assumptions)
- [stated] 2026-09-20: wants to see how the allocation process is done so he can train Demetria
- [stated] 2026-09-20: asked for what Rent Manager currently has booked for payroll allocations compared to the rebuild, with variance and reasons (Claude outputs\RM vs Rebuild Payroll Allocations Jan-Jul 2026.xlsx)
- [stated] 2026-09-20 booking rule: at the property level (non-Parakeet entities) payroll and insurance are one combined expense line; for Parakeet the 5% recapture is on the combined cost; everywhere else (Parakeet's books, the model outputs) payroll and insurance are broken out
- [stated] 2026-09-20 Overage Model design direction: Overview = summary of current operations; cost vs recapture chart = trailing 6 months + next 6, no wave patterns; by-vehicle table = past 6 vs next 6 and only KEET / KEET II (others are 100%); clicking a property in "where the overage sits" pops up the staff included, a historical trend line and time to break even; add employee count change by employee and position (MoM, QoQ, YoY) and upcoming health insurance eligibility with estimated impact
- [stated] 2026-09-20: Geiger Key is an Actual-method property (charged its allocated cost), not a 5% property — override in extract.py METHOD_OVERRIDE
- [stated] 2026-09-22: commissions are NOT part of an employee's total cost — commission runs are held separately (out of employee cost, property allocation and the forecast) until he confirms with the team where they belong; wants the coverage calcs walked through exactly (asked how Fox Creek got to 28%)
- [stated] 2026-09-22: for the team review he wants backup working papers that walk each step — total employee cost → allocation of that employee to properties → property reimbursement calcs — and a defined order of spreadsheets to reconcile step by step (Working Papers tab added to the Baseline workbook)

## Decisions

- **2026-08-31 - August allocations run as circulated. The model audit runs after, not before.** Jon holds that the model is wrong and Austin's comment was that it "needs to be reviewed and audited." Asked directly whether that meant holding the August run, he chose run-and-audit, with any error corrected in a September true-up rather than delaying the August close. The audit is authorised and owned by Jon; it does not gate the close. **The distinction matters and is recorded deliberately:** "needs to be audited" and "hold the run" are not the same instruction, and this page would be read the wrong way round if only the first half survived. (Source: Austin, on the 2026-08-31 delegation board. Closes `00-Meta/commitments.md` item 21.)
- **What the audit is looking for is already on this page.** The defects above are the brief: the zeroed-out deficits that manufacture a $40,705.48 surplus out of a $176,474.53 overage, the `#N/A` on Geiger Key that stops two totals computing, the Total Revenue column that is zero on every November row, the 17 properties whose two tabs disagree on pad count, and the absence of headcount anywhere in the workbook.

## Sources

- [[80-Finance/planning/2026-executive-strategy/Payroll Breakdown Allocation by Property.xlsx]] — `Sheet1` (2026 allocation), `Payroll Overage Analysis - Nov` (November 2025 actuals) and the embedded `PDS` tab.
- [[60-Communities/Property Data Sheet.xlsx]] — the `PDS Clean` tab used to check pad counts against Total Core Units.
