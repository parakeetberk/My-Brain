# FastField Phase I, build register

**What this is:** the per-form status of the 13 forms. One row per form, a permanent ID on each, per [[CLAUDE]] rule 15. **This is where "is it done" gets answered**, and the prose on [[15-Projects/fastfield-phase-i/overview]] stays out of it.

**Status:** current, 2026-09-02. **Owner: Austin**, per his 2026-09-02 disposition. **Scope: all 13, ruled by Austin 2026-09-02.** Opened because the project had no per-form tracking at all and Austin closed a form against it on day one.

## How a row closes

**Two gates, and a form is not done until both are green.** The project's definition of done is *"forms with automated workflows for all listed forms"* (Austin, 2026-09-02), so a built form with no workflow behind it is **half a row**, not a closed one.

- **Built** , the form exists in FastField and collects the right fields.
- **Workflow** , routing, notifications and destination are live behind it.
- **Live** , field staff are using it in production, not a test account.

Austin closes by ID: *"FF-12 workflow done"* is a complete instruction.

## The register

`Built` / `Workflow` / `Live`: `done`, `wip`, or blank for not started.

| ID      | Form                            | Fields      | Cond. logic | Files/photos | Sig     | Built    | Workflow | Live | Notes                                                                                                                                                              |
| ------- | ------------------------------- | ----------- | ----------- | ------------ | ------- | -------- | -------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `FF-01` | Home Listing Confirmation       | 4           | No          | No           | No      |          |          |      | Smallest form on the list.                                                                                                                                         |
| `FF-02` | Home Listing Request            | 30          | No          | **Yes**      | No      |          |          |      |                                                                                                                                                                    |
| `FF-03` | Offer to Purchase / Rent        | 15          | No          | **Yes**      | No      |          |          |      | Open item: where the signed PSA file goes. Drives storage architecture.                                                                                            |
| `FF-04` | Utility Request Application     | 12          | No          | No           | No      |          |          |      |                                                                                                                                                                    |
| `FF-05` | Weekly Maintenance Checklist    | 40          | No          | **Yes**      | No      |          |          |      | **Converter test 2**, the one that answers photo capture. Also on a different community list from every other form.                                                |
| `FF-06` | Incident Report                 | 45          | **Yes**     | **Yes**      | No      |          |          |      | Logic hand-built regardless.                                                                                                                                       |
| `FF-07` | Monthly Equipment & Inventory   | 50          | No          | **Yes**      | **Yes** |          |          |      | Still ships "Community 1, 2, 3, 4" placeholder values.                                                                                                             |
| `FF-08` | Month End Checklist             | 25          | No          | No           | **Yes** |          |          |      |                                                                                                                                                                    |
| `FF-09` | Move Out Inspection             | 95          | **Yes**     | No           | **Yes** |          |          |      | Heaviest form. Live risk against the converter's 20-page ceiling.                                                                                                  |
| `FF-10` | Resident Information Sheet      | 20          | No          | **Yes**      | No      |          |          |      |                                                                                                                                                                    |
| `FF-11` | Community Site Visit Inspection | 55          | No          | No           | No      |          |          |      |                                                                                                                                                                    |
| `FF-12` | Rehab Walkthrough Punchlist     | 35 / **45** | No          | No           | **Yes** | **done** |          |      | **Built with the AI Form Converter.** Austin, 2026-09-02, confirmed. **First form on the board and the converter's only proof point.** Workflow and Live not stated, not assumed. Summary column says 35 fields, detail sheet says 45. **Check the Community field: `KP-0037` may already be baked in.** |
| `FF-13` | Move In / Move Out Request      | 30          | **Yes**     | **Yes**      | **Yes** |          |          |      | Triggers Rent Manager entries. Drives the integration pattern.                                                                                                     |

**1 of 13 built. 0 of 13 with a live workflow. 0 of 13 in production.**

**Build method, where known:** `FF-12` AI Form Converter. The other twelve are unstarted.

Field counts and the logic, file and signature flags are VERIFIED from `15-Projects/quickbase-build/source-data/parakeet_jotform_audit.xlsx`, sheet `MASTER INVENTORY`.

## Candidate rows, scope not ruled

**Four FastField forms exist that this register does not track, and no ID is assigned to them because the scope call is Austin's.** Listed so they stop being invisible. `TD-0431` is open on the first three.

| Form | Where it comes from | Size | Why it is not a row yet |
|---|---|---|---|
| Home Delivery Confirmation | `WF001` locked spec v1.2 | not stated | Never a JotForm form, so the audit that built this register does not contain it. |
| Construction Inspection Checklist | `WF001` locked spec v1.2 | **89 items** | Same magnitude as `FF-09` at 95 fields, which is already a converter ceiling risk. |
| Ops & Sales Readiness Checklist | `WF001` locked spec v1.2 | **71 items** | As above. |
| Weekly PPE Inspection Checklist | SOP 122 Related Resources | not stated | **The form does not exist.** SOP 122 is not on the SOP Master Tracker either. |

**`WF001` is in build with the QuickBase vendor team as of 2026-09-02**, so three of these four are on the critical path now. See `KP-0053`.

## What this register does not hold

- **Scope.** Whether all 13 or only 6 go to FastField is unsettled. Every row is listed because Austin scoped all 13 on 2026-09-02; the audit's own column disagrees on 7 of them. See open problem 1 on [[15-Projects/fastfield-phase-i/overview]].
- **The community master list.** `KP-0037` gates the whole build and is not a per-form item.
- **Field-count truth.** The audit's summary and detail columns disagree on `FF-12` and nothing has checked the other twelve.
