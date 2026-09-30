---
type: model
tags: [type/model, dept/accounting, dept/construction, status/active]
---

# How a rehab dollar moves — and where it gets lost

**What this is:** the money spine of [[70-Operations/rehab-program/overview]]. Built 2026-09-02 on Austin's instruction to make the reporting *"update everything with invoices coming in and out wip accounts."*

**The short version:** there are **seven steps** between a scope being approved and a rehab dollar landing on the balance sheet. **This company has visibility into three of them.** Everything on this page follows from that.

## The seven steps, and which ones we can see

| # | Step | System that should hold it | Can we see it today? |
|---|---|---|---|
| 1 | Scope assessed and priced | vendor tracker (High Pace sheet) | **partly** — 36 units are on the board and not in the tracker at all |
| 2 | Scope approved | nowhere | **no** — see [[10-Business/eos/drafts/2026-08-31-natalie-rehab-approvals]]; approvals sit in email |
| 3 | Work starts | Rent Manager issue, `start` field | **partly** — **40 open units have no start date** |
| 4 | **Vendor invoice received** | AP | **no** |
| 5 | **Invoice coded to a WIP account** | GL, `code` field | **partly** — the code exists on 191 of 219 rows, the invoice behind it does not |
| 6 | **Invoice approved and paid** | AP / Ramp | **no** |
| 7 | Unit placed in service, WIP transfers to the asset | GL | **no** |

**Steps 4, 6 and 7 are invisible, and step 7 is the expensive one.**

## The WIP question nobody can answer today

`glActual` tells us **$1,338,235** has been booked against these 219 units. It does not say **which account it is sitting in.**

| | Units | GL booked |
|---|---|---|
| Open units carrying GL spend | 77 | **$351,442** — legitimately in WIP |
| **Units marked Complete still carrying GL spend** | **56** | **$989,786** |

**That $989,786 is the whole question.** If those 56 completed units have been placed in service, the money is capitalised to the asset and WIP is clean. If they have not, **there is roughly a million dollars sitting in a work-in-progress account for homes that are finished** — which overstates WIP, understates the depreciable base, and shows up as a prior-period adjustment the first time someone reconciles it properly.

**No source in this Brain can tell you which.** `INFERRED` — the export carries a GL actual, not a GL account. **This is not a reporting gap, it is a close-process gap.** Accounting runs 30 to 45 days in arrears (`KP-0003`), so the answer does not exist in real time even inside the GL.

**Where it sits by fund**, complete-but-still-GL-carrying:

| Vehicle | Units | GL booked |
|---|---|---|
| **JREFI** | — | **$556,279** |
| JREFII | — | $419,507 |
| Origins | — | $7,000 |
| Kippy | — | $7,000 |

**Where it sits by community**, top five: Belle Haven **$289,254** · Whispering Pines FL $196,101 · Brunswick Estates $171,058 · Fox Creek $119,250 · Auburn Ridge $96,441. **Belle Haven alone is 29% of it, and Belle Haven is 17 of 18 units complete** — it is the most finished community in the portfolio and the biggest unrolled balance. **Start the WIP roll-forward there.** `VERIFIED`.

## The WIP roll-forward that has to be built

**Nothing in this company produces this table today.** It is the single deliverable that makes the rehab program auditable, and it is monthly by vehicle.

```
                            JREFI    JREFII   Origins   Kippy    Total
Opening WIP balance            ?         ?        ?        ?        ?
+ Invoices received            ?         ?        ?        ?        ?
+ Internal labour (Ops)        ?         ?        ?        ?        ?
− Placed in service            ?         ?        ?        ?        ?
− Written off / abandoned      ?         ?        ?        ?        ?
= Closing WIP balance          ?         ?        ?        ?        ?
  Units in WIP at close        ?         ?        ?        ?        ?
  Avg age of WIP unit          ?         ?        ?        ?        ?
```

**Every cell is a question mark and that is the honest state.** The closing balance is the only line that can be approximated today, at $351,442 across 77 open units, and even that assumes every completed unit has already rolled out — which is exactly what is in doubt.

**Two rules on this table once it exists.** A unit **enters** WIP when the first invoice is coded to it, not when the scope is approved. A unit **leaves** WIP when it is available to rent or sell, not when the last invoice is paid — those are different dates and the gap between them is real depreciation.

## Where invoices are going wrong right now

Five failure modes, all VERIFIED against `data/rehab_tracker_all_data_2026-08-28.csv`.

**1. GL has spend, Rent Manager has nothing — 69 units, $345,883.** Accounting booked it, ops cannot see it. The field team's own tracker says these units cost nothing. **12 of them are marked Complete with no cost in Rent Manager at all**, so a completed rehab looks free to anyone reading Rent Manager.

**2. Twelve units have no WIP or GL code on the issue.** An invoice arriving for one of these has nowhere clean to land, so it goes to a default account or an expense line. **None of the twelve currently carries GL spend, which means the invoices have not arrived yet** — this is the one gap on this page that is cheap to close before it costs anything. Fix the codes now.

**3. Nine units where the vendor tracker is far above GL — $238,389 tracker against $75,266 GL.** Either **$163,123 of invoices have not been submitted**, or the tracker is priced above what the vendor will actually bill. **Those are opposite problems** — one is an accrual we are missing, the other is a forecast that is too high — and until someone asks High Pace directly, we do not know which.

**4. Thirty-six units on the board are not in the vendor tracker at all — $534,700 of modelled scope.** All of Origins and all of Kippy fall in here: **$86,290 of GL spend against zero vendor tracker records.** Two funds are spending money outside the sheet the weekly call reads from.

**5. Two-thirds of the cost field is a placeholder.** `costSrc` says **132 of 219 rows carry the literal string `IN PROGRESS`** where a number should be, and 12 say `NONE`. **Only 75 rows have a real typed cost.** So Rent Manager's $1,169,997 is not a total of 219 costs — it is a total of 75 costs plus 144 blanks. **Anyone dividing it by 219 to get a cost per unit is wrong by a factor of nearly three.**

## Aging, with the money attached

Open units only, banded by days since start.

| Band | Units | Modelled remaining |
|---|---|---|
| 0–30 days | 53 | $1,177,210 |
| 31–60 days | 22 | $488,931 |
| 61–90 days | 3 | $67,268 |
| **90+ days** | **15** | **$276,229** |
| **No start date at all** | **40** | **$823,768** |

**The 40 rows with no start date are the finding, not the 90+ band.** $823,768 of modelled scope on units nobody has scheduled. Some are genuinely not started and fine; **26 rows carry a start date in the future and 6 carry dates that do not make sense** (`badDates`), which means the schedule field is not being maintained rather than that the work is unscheduled. **A start date is how a rehab enters the 60-day board goal clock. Forty units are not on the clock.**

## What has to get built, in order

**Sequenced deliberately — each step is worthless without the one before it.**

1. **Resolve the 20 broken community codes** into one master list. Every cut on this program keys off it, and so do the FastField cascades and the QuickBase relationship fields (`KP-0037`). One list, fixed at source.
2. **Fix the 12 missing WIP/GL codes** before their invoices arrive. Cheapest item on the page.
3. **Answer the $989,786 question.** Pull the WIP trial balance by vehicle and diff it against the 56 completed units. This is a query, not a project.
4. **Stand up the WIP roll-forward** as a monthly close deliverable, by vehicle.
5. **Capture the invoice.** Received date, vendor, unit, amount, coded date, approved date, paid date. Until step 5 exists, steps 4, 6 and 7 of the seven above stay invisible and this program is reporting on a forecast rather than on money.
6. **Reconcile the model against the capex plan** — $4,198,591 modelled against $9,954,600 approved. Nobody has ever put those two numbers next to each other.

## The WIP balance now has a number on it, and the mechanics have names, 2026-09-16 to 09-21

**Added 2026-09-22 by the Page Update.** Figures in `00-Meta/numbers-ledger.md`, the dated row *Parakeet WIP, open balance and clearing history*, SINGLE-SOURCE and Jon's own.

- **Jon put real numbers on the WIP question on 2026-09-21**: roughly $10.8M sitting open, 37 projects and roughly $744k reversed out in 2025 against 2 projects and roughly $7k so far in 2026. His line at 01:30 ET on the intercompany thread: *"How did we even pass the audit. You should talk to citrin about that stuff Tuesday too."* **He named the mechanics rather than the backlog**, and they are the three faults this page had been inferring: **quarterly clearing** rather than clearing on closeout; **bills posted inconsistently to WIP against checks written straight to it**, which is the invoice path this page's seven steps describe going two ways; and **no separate depreciation schedules on tie-ins that mix roads and lift stations**, so a combined capex project cannot be depreciated by component once it does clear. `KP-0041` advanced with the first real figures; `TD-0685` carries them into the 2026-09-22 Citrin conversation. Read with `TD-0405`.
- **A fourth system was checked on 2026-09-16 and it cannot see the money either.** [[70-Operations/rehab-program/ledger-cost-analysis-2026-09-16]] queried the RentViewer warehouse directly: the `capexAccounts` segment returns zero rows for 2026, `VW_Budget_Comparison` carries only Income and Expense sub-types with no asset or WIP accounts, and every non-operating expense row in `VW_General_Ledger` has a blank unit tag. **So the question this page opened, which account the $989,786 against completed units is sitting in, cannot be answered from the ledger view this Brain can reach**, and a per-unit rehab cost cannot be produced from it. The workbook's own note that final cost per home is only recoverable through the `ISSUE #` is now verified rather than asserted.
- **What that does to the roll-forward this page says has to be built.** It still has to be built, and it cannot be built off the warehouse; it needs the GL account level detail Accounting holds. Jon's $10.8M is the opening balance the roll-forward would have to reconcile to, and the 2026 clearing of two projects is the reason the balance grows.
