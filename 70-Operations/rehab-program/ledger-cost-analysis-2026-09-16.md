---
type: analysis
tags: [type/analysis, dept/construction, dept/accounting, status/active]
---

# Rehab cost analysis from the ledger — addendum to the 2026-09-16 pre-call pack

**Built 2026-09-16 09:30 ET from the RentViewer Data Warehouse**, models `VW_General_Ledger` (cash basis, transaction level) and `VW_Budget_Comparison` (budget vs actual by property, GL account and month). Every figure below is `VERIFIED` by direct query this morning. It is a **fourth** system alongside the three in the data contract, and it does not agree with any of them — which is the finding, not a footnote.

## The headline: the warehouse cannot see rehab capital at all

**Three independent proofs, all from this morning's queries.**

1. **The `capexAccounts` segment returns zero rows for 2026, and the `capexExpense` measure returns null.** There is a capex measure defined in the model and nothing behind it.
2. **`VW_Budget_Comparison` carries only two GL account sub-types: Income and Expense.** No asset accounts, no work-in-progress. **The tracker's $1,338,235 of `glActual` is not reachable through this warehouse**, because the account it sits in is not in the view.
3. **Every non-operating expense row in `VW_General_Ledger` comes back with a blank `unitName`.** Queried across all 60 properties: not one unit-level tag. **A per-unit rehab cost cannot be produced from the ledger.**

**This confirms from a second system what `wip-and-invoice-model.md` could only infer.** That page said no source in this Brain can tell you which account the $989,786 is sitting in. **The warehouse cannot tell you either.** And the workbook's own note — that final cost per home is only recoverable through the `ISSUE #` — is now verified rather than asserted: the ledger has no unit key on this spend.

**So `PD-26` gets sharper, not softer.** We have a $4,198,591 `model` forecast, a $9,954,600 approved plan, and **a ledger that cannot report the actual against either.** Three numbers, none of them tied to the one system that books the money.

## What the ledger CAN show: the POH and REO accounts

Fourteen Park Owned Home / Real Estate Owned accounts carry **$124,359 across 718 transactions** for all of 2026. Largest: R&M Supplies $19,365 (319 txns), POH Property Insurance $34,630, POH & REO Expenses $35,901, Cleaning $6,427, Sewer $6,635, A/C Repair $5,184, Appliance $4,080, Plumbing $3,423, Demolition $3,031.

**$124,359 against a tracker that says $1,338,235.** These accounts are turnover consumables, not the rehab. **Nobody should quote a POH figure as rehab spend**, and the gap is the size of the thing that is missing.

## Repairs & Maintenance against budget — the closest proxy that exists

**Read this as operating R&M, not as rehab budget variance.** The rehabs bleed into it; they are not it. Same discipline as `model`.

| Month | R&M actual | R&M budget | Variance |
|---|---|---|---|
| Jan | $350,993 | $104,739 | **+235%** |
| Feb | $337,644 | $104,739 | **+222%** |
| Mar | $117,326 | $105,754 | +11% |
| Apr | $199,843 | $106,032 | +88% |
| May | $133,847 | $109,383 | +22% |
| Jun | $160,661 | $109,383 | +47% |
| Jul | $141,315 | $109,759 | +29% |
| **Aug** | **$41,013** | $109,759 | **−63%** |
| **YTD** | **$1,482,642** | **$859,548** | **+$623,094, +72%** |

**August is the number to look at, and it is not good news.** R&M collapsed to $41,013 in **the month the tracker records 16 completions, the best month of the year.** Work at its annual peak, spend at its annual floor. **That is the 30-to-45-day accounting lag (`KP-0003`) made visible in the ledger** — August work is done and August invoices are not booked.

**Which means three open items are one item.** The $989,786 sitting against completed units, the $163,123 where High Pace's tracker runs above our GL, and this August trough are **the same unbooked-invoice problem seen from three angles.** Mark's own line on 09-11 — *"I will be sending invoices and updating the tracker"* — is the confirmation. `TD-0407` is not a reconciliation question any more; it is an accrual we can size.

## Where R&M is running hot, rehab communities only

| Community | Actual YTD | Budget YTD | Variance |
|---|---|---|---|
| **Parkwood Mobile Home Park** | $44,857 | **$0** | **no budget at all** |
| **Hunter Springs MHP** | $2,786 | **$0** | **no budget at all** |
| Palm Haven Estates | $8,219 | $861 | **+855%** |
| Su-Rene | $21,320 | $4,670 | **+357%** |
| Silver Hill MHC | $29,358 | $11,687 | +151% |
| Riverwalk | $45,636 | $20,160 | +126% |
| Silver Breeze | $4,845 | $2,422 | +100% |
| Belle Haven | $8,361 | $4,781 | +75% |
| Fox Creek | $43,839 | $29,008 | +51% |
| Southgate | $12,063 | $8,318 | +45% |
| Auburn Ridge | $64,012 | $45,959 | +39% |
| Shady Acres | $24,983 | $19,195 | +30% |
| Lucky Clover | $37,390 | $29,720 | +26% |
| Druid Oaks | $24,085 | $19,965 | +21% |
| Brunswick Estates | $21,545 | $20,468 | +5% |
| Crystal Acres | $10,290 | $15,110 | −32% |
| **Northgate MH** | $29,489 | $89,225 | **−67%** |
| Lake Wales MHC | $827 | $7,265 | −89% |

**Two rows on this table are worth the whole page.**

**Hunter Springs carries a zero R&M budget for 2026, and yesterday Jon signed a rehab package there at $30,000 a home.** No budget line, a Kippy-vehicle asset, and roughly $180,000 committed. Highlight 1 of the pre-call pack now has a budget answer attached to it, and the answer is that there is no budget.

**Silver Breeze has a $2,422 R&M budget for the year and ten full-gut rehabs that have been running 152 days.** That is not an overrun, it is proof that the rehab capital is nowhere near these accounts — which is the same finding as section 1, arriving from the other direction.

**Lake Wales at −89% is the one clean confirmation in the table:** the property is genuinely paused, and the ledger agrees with the 09-02 call.

## The budget itself does not survive contact with the ledger

**Total operating expenses, 2026 YTD: $19,190,890 actual against $10,683,606 budget. +$8.5M, +80%.** Every single month is between 1.3x and 2.1x budget. **A budget that is wrong by 80% in the same direction for eight consecutive months is not a control, it is a number somebody typed in January.**

**Eight properties carry real spend against a zero budget** — A2Z Community Partners ($310,950), Parkwood ($44,857), Geiger Key Fish Camp ($29,336), McGregor Downs ($24,963), Geiger Key RV ($16,351), Regency I & II ($8,282), Northgate RV ($1,530), Hunter Springs. **And Meadow Woods carries a negative R&M budget of −$10,635**, which is a data error rather than a plan.

**This is the `PD-26` argument restated in the ledger's own terms.** The objection to the `model` forecast was that it has never been compared to approved capital. **The deeper problem is that the approved side is not trustworthy either** — at least not as it reaches this warehouse.

## What to do with this

**One question for the room, and it is not for Mark.** Which GL account does a High Pace rehab invoice actually land in? **If the answer is a WIP or fixed-asset account, this warehouse cannot report on the rehab program at all** and the dashboard's cost figures will stay un-auditable no matter how clean the tracker gets. **That is a two-minute answer from whoever codes the invoice, and it unblocks steps 3, 4 and 5 of the build sequence.**

**And one for the Friday EOS, under `PD-24`.** The person who can answer it is the Controller seat, which is the seat that is empty.
