---
type: register
tags: [type/register, dept/systems, status/active]
---

# QuickBase Workflow Register

**Status:** current - 2026-09-02, created by the Page Update and updated the same day on Austin's answer. **46 workflows, `WF001` to `WF046`. 3 in build, 2 draft, 41 not started.**

**What this is.** Per-workflow build status for [[15-Projects/quickbase-build/overview]], so the question *is it built* has an answer for each of the forty-six rather than only for the five that have specs. Austin closes a row by quoting its `WF` number.

**The ID is the vendor document's own, not one this Brain assigned.** `WF001` to `WF046` come from the master gameplan and are used across every spec, the playbook and the cascade map, so renumbering them here would break the link to the source documents. That is why this register uses `WF` rather than a new prefix, and why the range is fixed at 46 rather than growing.

**Three gates, not one, and the distinction is the same one the FastField register was given.** **Spec** means a locked build specification exists. **Built** means configured in QuickBase and FastField. **Live** means field staff are using it and the automations fire. A workflow with a locked spec and nothing configured is a document, and three of these are documents today.

**Two rows are merges and one is a sub-form**, so 46 is the workflow count and not the count of things to build: `WF027` absorbed the utility transfer workflow, `WF009` absorbed the construction preventative checklist, and `WF012` is a FastField form inside `WF004`.

**Wave order is dependency order, not calendar.** A wave cannot spec until the wave before it is at least in draft, and **no wave past 0 can start until the five shared tables exist** - see the overview. Waves are estimated at two to four weeks each in the gameplan; **no date is recorded anywhere and none is invented here.**

| ID | Workflow | Wave | Capture | Spec | Built | Live | Dept |
|---|---|---|---|---|---|---|---|
| `WF001` | Home Ordering, Delivery & Set | 0 | FF + QB | **LOCKED v1.2** | **in build** - QuickBase team, per Austin 2026-09-02 |  | Construction |
| `WF002` | Rehab | 0 | FF | **LOCKED v1.3** | **in build** - QuickBase team, per Austin 2026-09-02 |  | Operations |
| `WF003` | Asset TBD / Disposition Review | 0 | QB | **LOCKED v1.1** | **in build** - QuickBase team, per Austin 2026-09-02 |  | Operations |
| `WF004` | Move Out | 0 | FF x2 | DRAFT v1.0 |  |  | Operations |
| `WF006` | Listings | 0 | FF | DRAFT v1.0 |  |  | Sales |
| `WF012` | Move Out Inspection | 0 | FF | part of `WF004` |  |  | Operations |
| `WF005` | Move In | 1 | FF | not started |  |  | Operations |
| `WF014` | Utility Transfers | 1 | QB | not started |  |  | Operations |
| `WF015` | Resident Information Sheet | 1 | FF | not started |  |  | Operations |
| `WF016` | Lease Renewal Process | 1 | QB | not started |  |  | Operations |
| `WF007` | Offer to Purchase / Rent | 2 | QB | not started |  |  | Sales |
| `WF022` | Home Closing Process | 2 | QB | not started |  |  | Sales |
| `WF023` | POH Sales Title Transfer | 2 | QB | not started |  |  | Sales |
| `WF024` | Asset Title Transfer & Title Work | 2 | QB | not started |  |  | Legal |
| `WF008` | Community Site Visit Inspection | 3 | FF | not started |  |  | Operations |
| `WF009` | Weekly Maintenance Checklist | 3 | FF | not started, absorbed the construction preventative checklist |  |  | Construction |
| `WF010` | Monthly Equipment & Inventory | 3 | FF | not started |  |  | Operations |
| `WF025` | Demo to Infill | 3 | QB | not started |  |  | Construction |
| `WF026` | Lot Prep | 3 | FF | not started |  |  | Construction |
| `WF027` | Utility Activation & Physical Verification | 3 | FF | not started, absorbed the utility transfer workflow |  |  | Acctg / Ops / Const |
| `WF028` | Rental Inspections | 3 | FF | not started |  |  | Operations |
| `WF013` | Incident Report | 4 | FF | not started |  |  | Operations |
| `WF029` | Violation Process | 4 | QB | not started |  |  | Legal |
| `WF030` | License & Permit Renewals | 4 | QB | not started |  |  | Legal |
| `WF031` | Fair Housing & Annual Training Tracking | 4 | QB | not started |  |  | Legal |
| `WF032` | Insurance Renewals | 4 | QB | not started |  |  | Legal |
| `WF017` | Collections / AR | 5 | QB | not started |  |  | Operations |
| `WF018` | Stipulation Process | 5 | QB | not started |  |  | Operations |
| `WF019` | Eviction Pipeline | 5 | QB | not started |  |  | Legal |
| `WF020` | Post-Eviction Title Process | 5 | QB | not started |  |  | Legal |
| `WF021` | Rent Increase & Tax Pass-Throughs | 5 | QB | not started |  |  | Legal |
| `WF011` | Month End Ops Close Out | 6 | QB | not started |  |  | Operations |
| `WF033` | AP / Avid Exchange Process | 6 | QB | not started |  |  | Accounting |
| `WF034` | Security Deposit Refund | 6 | QB | not started |  |  | Accounting |
| `WF035` | Utility Recapture Reporting | 6 | QB | not started |  |  | Accounting |
| `WF036` | Home Lender Repo Process | 6 | QB | not started |  |  | Accounting |
| `WF037` | Financial Reporting, P&L / Rent Roll / Quarterly | 6 | QB | not started |  |  | Accounting |
| `WF038` | Due Diligence & Acquisition | 7 | FF | not started |  |  | Acquisitions |
| `WF039` | Acquisitions Transition | 7 | FF | not started |  |  | Acquisitions |
| `WF040` | Utility Onboarding, Acquisitions | 7 | QB | not started |  |  | Acquisitions |
| `WF041` | Acq-OPS Transition Recaps | 7 | QB | not started |  |  | Acquisitions |
| `WF042` | Manager Onboarding | 8 | QB | not started |  |  | HR |
| `WF043` | Team Onboarding & Training Tracking | 8 | QB | not started |  |  | HR |
| `WF044` | Property Business Plan | 8 | QB | not started |  |  | Operations |
| `WF045` | Prospect Screening & Background Check | 8 | QB | not started |  |  | Sales |
| `WF046` | Online Loan Application Process | 8 | QB | not started |  |  | Sales |

## How a row moves

A locked spec fills **Spec**. Configuration in both systems fills **Built**. Field staff using it with automations firing fills **Live**. **Nothing gets ticked on a verbal "that's done"** without the row saying what evidences it, the same rule `FF-12` is recorded under on [[15-Projects/fastfield-phase-i/build-register]].

## Answered 2026-09-02, and it moved the project a wave forward

**Austin, on `TD-0422`:** *"WF001, WF002, WF003 are being build by QuickBase team. Therefore it is approved for build."*

So the playbook's "Approved for Build" stamp of 08/19/26 is real, the approval is his, and **the QuickBase team is the builder.** Three rows move from unknown to **in build**.

**They are marked in build and not Built, and that is deliberate.** *Being built* is not *built*, and this register's whole reason for existing is that `FF-12` was closed on the word "complete" while its workflow column stayed blank. **A row goes to Built when someone says the configuration is finished**, and to Live when field staff are using it and the automations fire.

**Four things this answer does not settle, and they are recorded rather than assumed:**

1. **Who builds the FastField half.** `WF001` alone specifies **four FastField forms**: Home Delivery Confirmation, a **89-item Construction Inspection Checklist**, a **71-item Ops & Sales Readiness Checklist**, and the Listing Form. **Three of those four are on no build register anywhere in this Brain** - the FastField Phase I register tracks thirteen forms and none of them is the delivery confirmation or either checklist. See `KP-0053`. If the QuickBase team is building QB and Parakeet is building FastField, **the forms `WF001` depends on have no owner and nobody has noticed** because each project can see only its own list.
2. **Whether the solution design doc was ever signed.** [[10-Business/vendors/vendor-status-2026-08]] records, as of 2026-08: *"Walkthrough held; Kevin needs the metadata exports and wants a signed solution design doc before build proceeds."* Build has since proceeded. **INFERRED, not established: the playbook dated 08/19/26 may be that document.** Both statements are kept with their dates per the contradictions rule rather than the newer one quietly replacing the older.
3. **When it started, and when it lands.** No start date, no target date and no build cadence is recorded anywhere. **Wave 0 has no clock on it**, and Waves 1 through 8 are still gated on the five shared tables and eleven unrouted decisions.
4. **Whether `WF004` and `WF006` are in the same batch.** Both are Wave 0 and both are DRAFT rather than locked, with five open items each. Austin named three. **The other two are not assumed into the answer.**
