# FastField Phase I Build

**What this is:** the build project that puts the 13 audited JotForm forms into FastField with live workflows behind them, ahead of the QuickBase launch. FastField is the front end; QuickBase is the engine it feeds.

**Status:** active, opened 2026-09-02. **Owner: Austin**, per his 2026-09-02 disposition. **Per-form status lives in [[15-Projects/fastfield-phase-i/build-register]], not on this page.** 1 of 13 built, 0 with a live workflow. Parent project: [[15-Projects/quickbase-build/overview]]. **Per-form status lives in [[15-Projects/fastfield-phase-i/build-register]], not on this page.** 1 of 13 built, 0 with a live workflow.

## Goal

Get as many forms live in FastField as it takes to reach **85% field adoption before QuickBase launches**, with an automated workflow behind every form on the list. Not forms for their own sake. Forms that route, notify and write somewhere.

## Why

**JotForm is a dying platform for us and we have outgrown it.** SINGLE-SOURCE, Austin 2026-09-02. The need is a more institutional, tech-integrated platform, and FastField is the front end of QuickBase, which becomes the data and process control engine.

The strategic point is the sequencing. FastField is the wiring, and forms can be changed as QuickBase gets built out. Building forms now is not throwaway work waiting on QB, it is what stops the company sitting in limbo on a platform it has outgrown while the data-heavy build runs. Phase I is also the adoption play: **it bridges the gap and kick-starts field and company-wide adoption before the QB rollout asks anyone to change how they work.**

## Tangible outcomes

- All 13 listed forms live in production in FastField.
- A live workflow behind each one, not just a form that collects.
- **Delivery pace: 3 to 5 forms per week.** Set 2026-09-02, before the AI Form Converter was in scope. **Re-set it against workflows delivered rather than forms drawn**, since the converter accelerates only the drawing.
- Timeline anchor: **done by the time QuickBase discovery closes with the QB team.** The discovery end date is not recorded in this Brain yet.
- 85% field adoption measured before QB launch. The measurement method is not defined yet.

## The 13 forms

VERIFIED against `15-Projects/quickbase-build/source-data/parakeet_jotform_audit.xlsx`, sheet `MASTER INVENTORY`, JotForm Audit Build Reference v1.0.

| # | Form | Primary user | Frequency | Fields | Audit's migration target | Audit priority |
|---|---|---|---|---|---|---|
| 1 | Home Listing Confirmation | Community Manager | Per event | 4 | QB Only | High |
| 2 | Home Listing Request | Community Manager | Per event | 30 | QB + FastField | High |
| 3 | Offer to Purchase / Rent | Community Manager / Agent | Per event | 15 | QB Only | High |
| 4 | Utility Request Application | Community Manager | Per event | 12 | QB Only | High |
| 5 | Weekly Maintenance Checklist | Facility Manager | Weekly | 40 | FastField + QB | Low |
| 6 | Incident Report | Community Manager | Per event | 45 | QB Only | Medium |
| 7 | Monthly Equipment & Inventory | Technician | Monthly | 50 | FastField + QB | Low |
| 8 | Month End Checklist | Community Manager | Monthly | 25 | QB Only | Medium |
| 9 | Move Out Inspection | Community Manager / Inspector | Per event | 95 | FastField + QB | Medium |
| 10 | Resident Information Sheet | Community Manager | One-time | 20 | QB Only | Medium |
| 11 | Community Site Visit Inspection | Regional Manager / Director | Per visit | 55 | FastField + QB | Medium |
| 12 | Rehab Walkthrough Punchlist | Community Manager / Inspector | Per event | 35 | FastField + QB | High |
| 13 | Move In / Move Out Request | Community Manager | Per event | 30 | QB Only | High |

**Total field count across the 13: 456.** The three heaviest, Move Out Inspection at 95, Community Site Visit at 55 and Monthly Equipment at 50, carry 44% of it. A flat 3 to 5 forms per week will not hold across a set with that spread, so the weekly count should be read as an average and the heavy three planned as their own week.

## Build approach: the AI Form Converter

Austin, 2026-09-02: FastField can create forms by uploading samples. **VERIFIED, it exists and it is a real accelerator, but it does roughly half of what this project defined as done.**

**What it is.** FastField's AI Form Converter, now sold under Quickbase. Upload a PDF, Word doc, Excel file or image and it generates a mobile form. Ceiling of 20 pages per PDF or 20 images. It recognises text boxes, checkboxes, date pickers and signature fields and places them. Vendor's own caveat: more complex or customised field types "may not be recognised" and get added manually afterwards, low-resolution scans place fields badly, and testing before deployment is explicitly recommended.

**What it does not do, and this is the part that matters.** The vendor documentation covers field placement and nothing downstream. **No conditional logic, no cascading dropdowns, no routing, no notifications, no integrations.** This project's definition of done is *"forms with automated workflows for all listed forms."* **The converter builds the form. It builds none of the workflow.**

So the constraint moves rather than disappears. Scaffolding 13 forms stops being the long pole; **the workflow build becomes 100% of the critical path**, and the 3-to-5-a-week pace should be re-set against workflows delivered, not forms drawn.

### Where it will and will not carry a form

VERIFIED from the audit's own columns.

- **Clean conversion candidates, 10 of 13.** No conditional logic. Forms 1, 2, 3, 4, 5, 7, 8, 10, 11, 12.
- **Hand-build the logic regardless, 3 of 13.** Conditional logic on **Incident Report (45 fields), Move Out Inspection (95 fields) and Move In / Move Out Request (30 fields)**. These are also three of the four highest-stakes forms on the list. The converter can lay out the fields; the branching is manual either way.
- **Signature fields, 5 of 13.** Forms 7, 8, 9, 12, 13. The converter claims signature recognition, so these should survive.
- **File and photo capture, 8 of 13.** Forms 2, 3, 5, 6, 7, 9, 10, 13. **The vendor's recognised-field list names text, checkbox, date and signature. It does not name photo or file capture.** Photo capture in the field is the reason FastField is the front end at all, so **assume it does not convert and verify on the first form before planning around it.**
- **The 20-page ceiling is a live risk on one form.** Move Out Inspection at 95 fields, room-level, plausibly renders past 20 pages as a PDF. Split it or hand-build it.

### Test form and where its source files live

**`FF-12` Rehab Walkthrough Punchlist was built with the AI Form Converter.** Austin, 2026-09-02. **The converter works, and this is the evidence: a 45-field form with 36 checkboxes, 3 dropdowns, 2 text, 2 email, 1 date and 1 signature, off a one-page clean PDF.**

**Read it for what it proves and no further.** Every field type on `FF-12` is one of the four the vendor documents as recognised, and its source was a single clean digital page. **It confirms the documented easy case and de-risks nothing outside it.** Still unverified after this build: **photo and file capture** (8 of 13 forms), **conditional logic** (3 forms), and the **20-page ceiling** against `FF-09` at 95 fields. `FF-12` also carries **no file uploads**, so it could not have tested capture even by accident.

**The check worth running on it today.** The audit records `FF-12`'s Community field as a **65-community dropdown**; the fillable PDF the converter read has Property as a **plain text field**. So the built form has either a text box where a controlled value belongs, or a 65-item list against 67 active communities. **Either way `KP-0037` is no longer a future risk on this form, it is already in it**, and this is the cheapest possible look at what the converter does with community data before twelve more forms go through it. **Weekly Maintenance Checklist `FF-05` becomes test one.** It is the better test anyway: 40 fields, no conditional logic, and file uploads, so it is the only clean form that exercises photo capture.

**Two test forms, not one.** Rehab Walkthrough Punchlist proves conversion and signature capture. It cannot prove photo capture, because the audit records **Has File Uploads: No** on it, and photo capture is the biggest unknown on the list. **Weekly Maintenance Checklist** is the second test: 40 fields, no conditional logic, file uploads Yes. Between them the two settle every open converter question except conditional logic, which is hand-built regardless.

**Rehab Walkthrough Punchlist source files**, VERIFIED 2026-09-02:

- **The blank fillable form, and the best converter input.** `70-Operations/sops/105- rehab_walk_punchlist_fillable (1).pdf`. **One page**, a clean digital PDF rather than a scan, so it clears both the 20-page ceiling and the resolution caveat.
- **The structured field map.** `15-Projects/quickbase-build/source-data/parakeet_jotform_audit.xlsx`, sheet `12-Rehab Punchlist`. **45 field rows: 36 checkboxes, 3 dropdowns, 2 text, 2 email, 1 date, 1 signature.** Every row is marked `FastField? Yes`.
- **The live form.** JotForm `261234541071043`.
- **Real submissions, and the closest thing to ground truth.** Completed walkthroughs filed as `.eml` under `/sites/main/Shared Documents/Construction/BELLE HAVEN/DEVELOPMENT/`, for example `Lot 5 - Rehab/Post Rehab Walkthrough_ Belle Haven - 5 - Needs Additional Punchlist Items.eml`. **A submission shows what the live form actually produces**, which is the check on whether the audit sheet is complete.
- **The process behind it.** `70-Operations/sops/105- SOP - Rehab Jotform.pdf`, 7 pages, and [[70-Operations/sops/105-poh-rehab]].

**One discrepancy inside the audit, recorded not resolved.** `MASTER INVENTORY` gives this form a **Total Field Count of 35**; sheet `12-Rehab Punchlist` lists **45 field rows**. The workbook is a point-in-time export, so this is most likely a stale summary column rather than a business problem, **but the sheet is the detail and 45 is the number to build against.** The same gap may exist on the other twelve rows and nothing has checked.

### The risk that gets worse, not better

**`KP-0037` is the reason to freeze the community list before converting anything, not after.** The audit records a **65-community dropdown** against the 67 active communities in [[CLAUDE]], one form using a different community list entirely, and another still carrying "Community 1, 2, 3, 4" placeholders. **An AI converter reads a sample and reproduces what it sees.** Feed it the current JotForm exports and it will bake the wrong static list into thirteen forms in an afternoon, faster and more consistently than any human would have. **Speed applied to an unresolved data defect industrialises the defect.**

The cascade map's own fallback is the answer and it is better than a corrected dropdown anyway: **pre-populate Community and Lot on the form from QuickBase via QR code or link launch**, so field staff never hand-select. That removes the dropdown from the failure path instead of fixing it.

### Better input than the JotForm PDFs

The converter accepts **Excel**. `parakeet_jotform_audit.xlsx` already holds a structured per-form field map, thirteen sheets of section name, field name, field type, required flag and options. **That is a cleaner input than a PDF render of a JotForm**, which is a picture of a form rather than a description of one, and it sidesteps the resolution caveat entirely. Test both on one form before committing the batch.

## Open problems, all eight dispositioned by Austin 2026-09-02

His answers are quoted. Where an answer settles something, it says so; where it opens work, the to-do is named.

1. **The 6-versus-13 scope question. SETTLED.** *"Create all 13."* **The denominator is 13.** The audit's `Migration Target` column, which routes 7 of the 13 to QB Only, is superseded for build purposes and kept on the page with its date rather than deleted. Every row in the register stands.
2. **Community dropdown. IN SCOPE as cleanup.** *"Community Dropdown needs to be configured to be from the same list in all fields. This is part of the task to clean up the forms."* `TD-0454`, owner Austin, against `KP-0037`. **The one place this ruling is worth a second look:** as written, the list gets fixed inside each form's cleanup, which is thirteen fixes rather than one. **Defining the single master list once, before the remaining twelve are converted, is the same work done at a thirteenth of the cost** , and `KP-0037` has already widened beyond this project, with four different community counts across four documents in the QuickBase drop. Not a disagreement with the ruling, a question about its order.
3. **Cascading lists. CONFIRMED in scope.** *"Yes this is true need cascading lists built."* `TD-0455`, owner Austin. **It carries an unmade platform decision:** the cascade map says full status filtering needs FastField Enterprise API integration, and names pre-populating Community and Lot from QuickBase by QR code or link launch as the fallback. **The fallback is the better mechanism for adoption**, because field staff never hand-select at all. That choice has not been made and it changes what gets built.
4. **Lot Status and Asset Status maintained by QB automations. CONFIRMED.** *"Correct."* **This is a hard dependency on the parent project, not a Phase I task.** Every cascade filter keys off these two fields and the automations that maintain them live in QuickBase, which is at Wave 0. **Phase I can build the forms; it cannot make the filters correct on its own.**
5. **The twelve form-design questions. TBD.** *"TBD."* Austin's word. Left open, no to-do raised, no owner assumed. Several are architectural rather than cosmetic: where the signed PSA file goes drives file storage architecture, and whether Move In / Move Out writes to Rent Manager drives the integration pattern.
6. **Project owner. SETTLED.** *"Austin is the owner now."* Recorded on this page and on the register.
7. **The JotForm and FastField overlap in the SOP library. SETTLED, and this is the widest of the eight.** *"All JotForm refrences need to be updated to FastField."* `TD-0456`, owner Austin. **This answers a question that has been open across the whole SOP library, not just this project:** `TD-0215` had Natalie settling the platform question and producing the form ecosystem document; `TD-0199` had SOP 001 unable to decide between the two platforms inside its own text; `TD-0189` had SOP 201's JotForm Home Drop Confirm link unresolved. **The ruling closes the question behind all three.** The tracker's *"Jotform Process (Form Ecosystem)"* row, a Tier 2 with nothing started, now has its answer. **The work is a library-wide sweep, not a note**: SOP 001, 105, 105b, 122 and 201 all name JotForm, and SOP 105 contradicts itself inside a single task.
8. **AI Converter photo and file capture. OPEN, under review.** *"Will review."* `TD-0457`, owner Austin. **8 of the 13 forms need it and `FF-12` could not test it**, having no file uploads. `FF-05` Weekly Maintenance Checklist is the test.

### The scope boundary his answer does not cover

**"All 13" answers the JotForm audit's list. The FastField build is bigger than 13.**

`TD-0431` is already open on this: `WF001`'s locked spec depends on **three FastField forms that appear on no register anywhere** , Home Delivery Confirmation, an **89-item Construction Inspection Checklist** and a **71-item Ops & Sales Readiness Checklist**. Only the Listing Form maps here. **`WF001` is in build with the QuickBase vendor team right now**, so those three are on the critical path today rather than in a later wave. Separately, SOP 122's **Weekly PPE Inspection Checklist does not exist** and is the safety programme's only recurring control.

**So Phase I as scoped can hit 85% adoption across thirteen forms while `WF001` stays blocked on three that were never counted.** The two registers each see only their own list, which is the mechanism `KP-0053` was opened to name. **A ruling is needed on whether those four forms join this register or stay with the parent**, and it is not assumed here either way.

## What is not settled

- When QuickBase discovery ends. The whole timeline hangs off it.
- How 85% adoption gets measured, and against what population.
- Who owns the build.
- Whether the three Home Ordering, Rehab and Disposition build specs already written are Phase I scope or QB Phase II.

**Source paths changed 2026-09-02 and the links here were repointed.** The JotForm audit workbook and the cascade logic map moved out of `05-Inbox/` when the QuickBase drop was filed to [[15-Projects/quickbase-build/overview]]. **Nothing about the content changed**; the files are the same and the citations still resolve. Worth knowing because **this project's open scope question, 6 forms or 13, is answerable from that parent project's SOP-to-workflow mapping table**, which nothing had read while the drop sat in the Inbox.

## Sources

- [[15-Projects/quickbase-build/source-data/parakeet_jotform_audit.xlsx]], the 13-form master inventory, per-form field maps and the 13 open items. The authoritative form list.
- [[15-Projects/quickbase-build/cascade_logic_map.md]], the Community, Lot, Asset filter rules per form and the FastField implementation constraints.
- FastField AI Form Converter help article, `mergemobile.zendesk.com`, and the Quickbase FastField AI Form Converter blog post. Read 2026-09-02 for the accepted inputs, the 20-page ceiling, the recognised field types and the manual-adjustment caveat.
- Austin, 2026-09-02, project interview and the AI-conversion capability.
