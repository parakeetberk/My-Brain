---
type: process
tags: [type/process, dept/finance, dept/asset-management, status/active]
---

# The 2027 budget build

**Status:** active. **Page created 2026-09-02** from [[70-Operations/meetings/2026-09-02-founders-and-asset-management-budget-session]], which is the first time the build was described end to end. **Nothing in this Brain described the 2027 budget process before today.**

**What this is.** How the 2027 property and Opco budgets get built, who feeds them, and the two design decisions that determine whether the output is defensible. Figures on this page are **shapes and mechanisms, not numbers**: the model was walked through with placeholder values and the call said so repeatedly - *"ignore the numbers for now."* **Nothing from it is entered in `00-Meta/numbers-ledger.md`.**

---

## The build

Excel model, formulas driven with Claude and code, rendered to an **HTML dashboard** so everyone reviews the same thing on their own screen.

- **Cut by market, then property within market.** Filters for **regionals, markets and portfolios** - regionals is the primary cut they settled on, so a regional can be sent their own slice and add input.
- **P&L ties to the actual GLs**, above and below the line. An infill tab summarising the asset summary. **Occupancy over time, January 2025 to December 2027**, annual, plus ready spaces.
- **The dashboard cannot save state**, so an override typed into it is purely visual. The plan is to keep the source files in one place and have the page pull from them, so a refresh reflects a real change.

## Where the inputs come from, and this is the part that makes it defensible

**Infill is driven off Leslie's planned order sheet.** The order cadence drives occupancy; timelines come from agreed-upon timelines with the field, based on what they have been and what they should be. **The sale timeline is 90 days.** So the plan runs off the field's own inputs rather than a target set centrally, which is the stated fix for last year.

**The absorption cap is the design decision worth remembering.** The final model carries **no manual per-unit overrides.** Instead there is a **cap input per community per month** of homes sold: set Applegate at three a month and every home that stages and is ready gets absorbed at three a month until the plan is hit. It may be driven off **occupancy percentage rather than home count** so it scales with community size - a 400-site community perhaps eight a month against a 100-site community at two.

**Both founders gave the reason, and they are slightly different reasons.** Jon: **"manual inputs by unit is what caused a lot of the pain last time,"** and the goal is *"not to be a hundred percent exact, but to have it roll in on a reasonable, defensible basis."* Austin went further - the final should be **entirely formulaic, with no room for tweaking**: *"here's the plan, this is what we need to get to."* **The tension between shooting for the moon and being achievable is explicit and unresolved on the call**, and it has a hard reason to resolve: if the company is under contract with someone in January, February or March, the plan has to be one it can hit.

## Cash flow, and the thing it is actually for

The property budgets come first. Then anything on a property cash flow sheet that can be pushed to property level is pushed down, and **whatever cannot is layered on top in a portfolio cash flows page** - escrows, the unplanned capex reserve, corporate capital events.

**The point of it is a live cash position**, so the question *"which capex project do we adjust"* has an answer in real time rather than after the fact. **This is also the argument for Opco existing as its own layer.**

**JREF I gets its own module**, pulling the cash flows, running the IRR and producing a price. **Not for distribution** - a back-of-envelope of what they are tracking to, so price and achievability get maximised together rather than one at the other's expense.

## Schedule

- **Applegate was built first**, with the analyst, on the night of 2026-09-01.
- **Thursday 2026-09-03 evening: the session to finalise the mechanics and the template**, then prove it by replicating for Whispering Pines. After that it is replication.
- **More than one further working session is needed** and both founders said so; the week of 09-08 was named for it.
- **Distribution date is ambiguous in the source and is recorded that way.** The call said both *"everything out by next Friday"* with two full days plus the weekend to review, and *"if we're aiming to try to finalize and distribute by Friday."* **From a Wednesday those are 2026-09-11 and 2026-09-04**, and the review-window arithmetic fits neither cleanly. `TD-0437` settles it, because the regionals and managers are the people who need the date.

- **Budget week, 2026-09-15 to 09-18, was cancelled on 2026-09-11** (Austin to Moe and Jon, 14:50 ET). No replacement date is on record; `TD-0647` holds the calendar entry that still says otherwise for nine people. **The ledger every one of these budgets runs off had several Rent Manager controls switched off on 2026-09-09** with Moe named as monitor, and nothing says what the controls are or who is told, `KP-0108`. Added 2026-09-15 by the Page Update from the closes of 2026-09-09 and 09-11.
## What the property review will cover

Jon expects it to be straightforward: **expenses are expenses across the properties at this point**, infill comes straight off the order sheets which is Leslie's, then **rent increases**, then **capex** - with John Clark working on capex intel and managers holding views.

## Two gaps in how the money is booked, and one of them may be revenue

**Sales and marketing organisational expenses have no known booking treatment.** Leslie asked how to think about them in a property budget and nobody on the call knew. Jon: *"I don't know how that stuff is getting booked. I'm guessing it's all going to Opco"* - flyers, flags, the state MLS subscription. He wants them broken out because **they flex with sales activity**, so the Opco run-rate burn should be readable with and without them. The working frame is **roughly $5,000 of internal budget per home to get it sold.** `TD-0438`.

**The admin fee on home closings may be budgeted and not charged, and that is revenue.** Austin asked; Jon's answer was *"Are we? I don't know. I think we are. We budgeted to have an amount, but I don't know how any of that is being done."* And nobody could say where gains and losses on home sales land - **"it's all one bucket."** `KP-0057`, `TD-0440`.

**Related, and it is a booking question rather than a payroll one:** an on-site sales and leasing person pushes payroll over on overage, and **if the role is sales and leasing it arguably books to the dealership rather than Opco.** That single reclassification changes the payroll overage picture.

## Opco

Renamed on the call from a future review to the **Opco 2027 budget, on the same cadence as everything else.** They want a proper Opco review covering **non-payroll departmental expenses** and **payroll overage**, for the reason Jon gave plainly: **"we've ramped a lot up without really analysing the impact."** `TD-0439`.

One mechanical complaint is recorded without figures, per [[CLAUDE]] rule 9: the current model **nets rather than showing the build** - *"all he does is net it, and there's no way to track back to understand it"* - and it was pulled from the GL rather than the payroll model.

## Sources

- [[70-Operations/meetings/2026-09-02-founders-and-asset-management-budget-session]] - the primary and, as of today, only source for everything on this page.
