# 400 — Capex kickoff and closeout

**What this is:** how a capital project gets approved and closed at Parakeet. Every capex and infill project in the company runs through this and **nothing about it was written down until 2026-08-31**. Reconstructed from eight signed documents, not from a written procedure, because no written procedure was found.

**Status:** current, 2026-09-15. `PD-46`, the proposed emergency exception, added by the Page Update; the flow itself is as of 2026-08-31. **Reconstructed, not authored.** Confirm with Vladimir Baga before treating it as the standard.

## The flow

Two documents per project, sharing one number.

1. **Kickoff.** Vladimir Baga creates it from a fixed template in Adobe Acrobat Sign and routes it. Approval authorises the spend.
2. **Work happens.** The project lives as a Rent Manager Service Manager issue under the same number.
3. **Closeout.** Vlad creates the closeout on the same number, carrying the final invoice, before and after photos, the signed kickoff and the handover email.

**The number is the spine.** `CODE_TYPE_NUMBER`, where the number is simultaneously the project ID, the Adobe Sign document name and the **Rent Manager Service Manager issue ID** at `bedg.rmx.rentmanager.com/#/servicemanagerissues/<number>/details`. Lucky Clover 17178 is the confirmed matched pair: kickoff and closeout on one number.

TYPE is `CAPEX_KICKOFF`, `CAPEX_CLOSEOUT`, `INFILL_KICKOFF`, `INFILL_CLOSEOUT` or `CHANGEORDER`. One document breaks it: `VO_INFILL_KICKOFF_MULTI` has no number and can never be matched to a closeout.

## The signing order

Six people, always this order, observed identically on all eight documents:

| # | Role | Person | Action |
| --- | --- | --- | --- |
| 1 | Controller | David Berman | sign |
| 2 | Director of Acquisitions | Zachary Schwartz | sign |
| 3 | Director of Construction | John Clark | sign |
| 4 | Director of Property Operations | Natalie Magurne | sign |
| 5 | | **Austin Berk** | **approve** |
| 6 | | **Jon Wyss** | **approve** |

Cindy Wigfall is copied on every completion notice. **Austin is an upstream approver, not the last one**: a document sitting unread in his queue holds up Jon behind him.

## What the kickoff template asks for

General project information: project name, project lead, project sponsor as `COMMUNITY - DEPARTMENT`, contractor, representative, email, phone. Overview: problem or issue, purpose. Capex type: PLANNED, UNPLANNED or INFILL, plus inclusions and exclusions. Budget: **budget allocation, assigned GL code, proposal link, project estimate, payment terms**. Tentative schedule: kickoff, implementation, target completion. Project links: SharePoint, Rent Manager, Outlook. Then project photos, a before-photos link and the signature block.

## What the closeout template asks for

Project information and vendor information as above, then budget allocation, **assigned GL code, estimated quotation, final invoice amount** and payment terms. Then a deliverables checklist across Kickoff and Procurement, Project Implementation and Closeout; before and after photos; and a document checklist naming the signed kickoff, progress photos, the handover email and the final invoice.

**Both estimate and final invoice sit on the closeout**, which means budget-versus-actual is computable from that one document without Rent Manager and without the kickoff.

## Where it breaks, observed on the 2026-08-31 batch of eight

Facts, not fixes. Each is checkable against the named document.

- **The Budget Allocation field is empty on seven of eight.** Six read `UNPLANNED, NO BUDGET ALLOCATION`, one reads `INFILL, NO BUDGET ALLOCATION`.
- **Lake Saunders 11055, the one with an allocation, was approved sixty percent over it**: $30,000.00 allocated, $48,000.00 estimated, both on the same page.
- **The Assigned GL Code field is empty on all five kickoffs.** Closeouts populate it, with 16741, 16961 and 16971, and none of those three appears in the Rent Manager chart of accounts.
- **The FINAL INVOICE field means the last payment, not the project total.** Whispering Pines 15603: estimate $9,901.90, deposit invoice $4,950.95, final invoice $4,950.95.
- **Applegate 17021 was signed as a closeout with the final invoice amount blank**, with the invoice PDF listed in its own checklist.
- **Two of three closeouts show Project Implementation as "In progress"** while being signed as closeouts.
- **Implementation date reads TBD on every kickoff**, and target completion is set at exactly three months after kickoff on all five.
- **Su Rene 17011 is named RETAINING WALL, describes a seawall, and excludes retaining walls.**

## The emergency exception Jon asked for, `PD-46`, unowned

**Added 2026-09-15.** On 2026-09-07 at 18:59 ET Jon waived the second bid on the River Oaks electrical repair himself, gave Natalie six numbered actions and took the sequencing call, saying the two bid process is what put eight weeks between a failed service and a repair. The next day he asked for the general version: **loss of an essential service to an occupied home should skip the second bid and carry same day authority up to a set threshold.** `PD-46` opened 2026-09-08 on his own words. **It has no owner, no threshold and no name on the authority, and it is Austin's ruling.** Until it lands, this flow has no emergency path and the next failed service waits the same eight weeks. The case is on `60-Communities/river-oaks-rv-resort`.

## Timing

Eight documents arrived in Austin's For Signature folder between 10:52 and 11:01 ET on 2026-08-31 and all eight were fully executed by 11:44. Jon's email of 2026-08-21 is titled "Last night's 11 approvals, all signed."

## Related

- [[60-Communities/projects]] - the ledger every one of these documents lands in.

## Sources

- Eight signed PDFs attached to their Adobe Sign completion notices, read in full 2026-08-31: 11055, 16996, 17011, 17021, 17178, 17285, 17386, 15603.
- Rent Manager chart of accounts, `list_entities` GLAccounts, read live 2026-08-31.
- [[00-Meta/daily-close/2026-09-08]] — the waiver, Jon's request and `PD-46`. Added 2026-09-15.
