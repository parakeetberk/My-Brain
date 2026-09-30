# 302 — Home lender repo

**What this is:** what happens when a lender sends a repossession notice on a home Parakeet backstops — assemble a data pack, decide among three purchase options, and answer the lender before the deadline.

**Status:** draft — the document states "STATUS: NEEDS APPROVAL." Tier 2 High. Initial draft July 1 2026. Read 2026-08-30. **Credential exposure fixed 2026-09-01 (`KP-0001`); the five open [TBD] markers below are untouched.**

## The facts

- **Owner:** David (Accounting) — the header reads "Asset Management SOP" with David as process owner. **Executes:** Lender Distribution email list, Accounting/David, Leslie (Director of Sales & Marketing), Ops, Austin (Owner). **Trigger:** receipt of a repossession notice from a lender (e.g. 21st Mortgage). **Ends when:** Parakeet communicates the chosen option to the lender before the expiration deadline and David initiates payment.
- **Why the clock matters, stated up front:** "Parakeet's response time on repossession notices is tracked by lenders and directly impacts the company's ability to secure future line increases and strategic business opportunities."
- Five timelines: notice receipt & distribution → data pack assembly → decision review → lender response → post-mortem analysis.
- The notice arrives at an internal distribution list carrying customer name, loan number, serial number, purchase price, the three purchase options and the lender expiration date. Accounting logs all of it.
- **The internal deadline is 2 weeks before the lender expiration date — not the lender's date.** Accounting calculates it and communicates it to the full distribution list. "Do not wait until the last day."
- **Three deliverables, each due within 3 business days of notice receipt:** Leslie's **1-page Sales summary** (current demand, sales velocity, pricing, funnel status, marketability in current condition and what updates would make the home sellable); **Ops** confirmation of unit condition, estimated turn time and resident ledger status; **David's** confirmation of credit line capacity for each of the three options.
- Leslie compiles the seven-part data pack — lot status, current demand from the Prospect Report, recent sales/rent velocity, estimated turn costs, the Sales 1-pager, Finance capacity confirmation, Ops condition report — and delivers it to Austin and David.
- **Austin and David review together and jointly select the option, by the internal deadline.** If the data pack is incomplete, Leslie escalates to David immediately.
- **The three options:**
  - **Option 1 — Spec Home Inventory:** pay **10%** of purchase price. Home must be secured, de-trashed, cleaned and leak-repaired **within 30 days**; fully repaired and marketable **within 60 days**. **Maximum inventory term 6 months.**
  - **Option 2 — Rental Asset:** pay **10%** of purchase price; the home converts to rental financing per the Agreement, **no origination points charged.**
  - **Option 3 — Full Payoff:** pay the full purchase price by wire or certified funds immediately.
- Accounting emails the lender the chosen option **before** the expiration date, then initiates the 10% down payment or full payoff by wire or certified funds. **Reference the customer's last name and loan number on all payments.**
- **Every repossession notice requires a post-mortem — no exceptions.** Leslie and David co-lead the recap (what went well, what did not, early warning signs visible in the data) and Leslie emails findings to the full distribution list — Sales, Ops, Finance, Asset Management. The goal is stated as pattern-spotting and improving Parakeet's lender reputation.
- Compressed timeline rule: a notice arriving with less than 2 weeks left means compress everything and escalate to David the **same day** — the full data pack is still assembled.
- **Systems used:** email (the process runs on a distribution list), Rent Manager (lot status, resident ledger), Prospect Report.
- **Known problems:**
  - ~~**This SOP contains live payment credentials.**~~ **FIXED 2026-09-01.** Austin, dispositioning `KP-0001`: *"Updated and information removed."* Related Resources previously published 21st Mortgage's mailing address, **account name, account number, beneficiary bank and ABA routing number** in full, in a document distributed through the wiki. **The original finding is kept visible rather than deleted** so the reason the SOP changed survives the change, per [[CLAUDE]] rule 13.
    - **Two things the fix does not tell us, and neither is assumed here.** Which artefacts were edited — the wiki page, the source document, any PDF already circulated — and whether the ABA and account number were rotated at the lender or only removed from the page. **Removing a credential from a document does not un-circulate it.** If the SOP was distributed with those details in it, the exposure is with whoever holds a copy. Worth one sentence from David if anyone wants this closed on evidence rather than on word.
    - The SOP's own text already carried the fix: payment instructions vary by lender and should be taken from the notice.
  - **The consequence of missing a lender deadline is [TBD]** — in a process whose stated purpose is protecting credit line relationships. "David and Austin to confirm specific consequences and any cure period for each lender."
  - **The tracking artifact does not exist.** "Repo Tracker [TBD — to be built. Will log all notices, internal deadlines, decisions, and post-mortem status. **Interim: log via email to full group distribution list.**]" So the deadline that drives the whole process is tracked in an email thread.
  - **The Data Pack Template [TBD]** is also unbuilt, and the Prospect Report is "[Link TBD]" — the seven-part pack has no format and one of its sources has no location.
  - **The status block undercounts its own gaps:** "NEEDS APPROVAL — **2 OPEN [TBD] ITEMS**," while the body carries at least five distinct [TBD] markers (repo tracker, payment timing and delay consequences, data pack template, Prospect Report link, missed-deadline consequences).
  - **Payment timing after the decision is [TBD]** — "payment timing and consequences of delayed payment to be confirmed by David and Austin per lender agreement."
  - **Department attribution is threefold:** headed "Asset Management SOP," owned by Accounting, filed in the 300s Accounting band. The Asset Management band (400s) is empty.
  - Option 1's 30/60-day repair clocks and 6-month inventory cap have no owner, no tracking field and no link to SOP 105's rehab process, which is where that work would actually be executed.
  - `_Video Links.txt` is an empty template; a 302 overview video was scheduled for the week of Aug 24, 2026.

## Decisions

- None recorded yet.

## Sources

- [[70-Operations/sops/Process Wiki/300-399 Accounting/302 Home Lender Repo/302-Home lender repo-draft V1.docx]] — the SOP, five timelines, three purchase options and the open [TBD] items.
- [[70-Operations/sops/Process Wiki/300-399 Accounting/302 Home Lender Repo/302_Home lender repo-lucid workflow draft V1.pdf]] — the workflow draft.
