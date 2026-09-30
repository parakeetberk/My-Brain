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

## Decisions

- **2026-08-31 - August allocations run as circulated. The model audit runs after, not before.** Jon holds that the model is wrong and Austin's comment was that it "needs to be reviewed and audited." Asked directly whether that meant holding the August run, he chose run-and-audit, with any error corrected in a September true-up rather than delaying the August close. The audit is authorised and owned by Jon; it does not gate the close. **The distinction matters and is recorded deliberately:** "needs to be audited" and "hold the run" are not the same instruction, and this page would be read the wrong way round if only the first half survived. (Source: Austin, on the 2026-08-31 delegation board. Closes `00-Meta/commitments.md` item 21.)
- **What the audit is looking for is already on this page.** The defects above are the brief: the zeroed-out deficits that manufacture a $40,705.48 surplus out of a $176,474.53 overage, the `#N/A` on Geiger Key that stops two totals computing, the Total Revenue column that is zero on every November row, the 17 properties whose two tabs disagree on pad count, and the absence of headcount anywhere in the workbook.

## Sources

- [[80-Finance/planning/2026-executive-strategy/Payroll Breakdown Allocation by Property.xlsx]] — `Sheet1` (2026 allocation), `Payroll Overage Analysis - Nov` (November 2025 actuals) and the embedded `PDS` tab.
- [[60-Communities/Property Data Sheet.xlsx]] — the `PDS Clean` tab used to check pad counts against Total Core Units.
