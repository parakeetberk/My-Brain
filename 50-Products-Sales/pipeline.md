# Pipeline

**What this is:** enquiry to resident, end to end — every stage, who owns it, and what the clock is. Assembled from the six sales process pages, because no single document in the company covers the whole path.

**Status:** current — 2026-08-30

## The facts

### 1. Lead in

- **A lead arrives by phone, email, web form, walk-in, referral or local outreach.** All six are named triggers on [[70-Operations/sops/006-lead-intake-tracking-application-and-screening]]. Where they come from is on [[20-Brand-Marketing/online-presence]].
- **The intake rule: whoever receives the lead logs it immediately, at first contact — not after the application is sent, and not at end of week.**
- **Check for a duplicate prospect record before creating one.** If a duplicate exists, update it; never create a second.
- **Logged in Rent Manager Prospects at status New Prospect**, with the application-sent date in History & Notes. **Sales also logs the prospect in the CRM**, which is MAV Consulting ([[10-Business/vendors/mav-consulting]]).
- **The CRM's duplicate-and-merge workflow launched 2026-08-25, for new prospects only.** If Google Ads is the ad source that value is retained; otherwise the oldest lead source wins. Two people with the same name but different contact details — roommates, for example — **would be merged under that rule.** Unsolved.
- **The funnel stage names the team uses, verbatim: "new prospect" to "engaged prospect" to "tour completed" to "application completed."**

### 2. Application

- **Whoever logged the lead sends the application. Weekly follow-up** until it is complete or the prospect is Lost, every attempt documented with date, channel and outcome. The older generation sets Lost after **five** follow-up attempts.
- **Required before screening:** government-issued photo ID, income documentation, a signed consent form, all fields complete, and **the application fee paid.** The older PDF is stricter — two recent paystubs, W-2s, and two to three months of bank statements, all pages.

### 3. Screening

- **The Screening Coordinator runs AmRent inside Rent Manager — never outside either system.** There is no direct-login path in any SOP ([[10-Business/vendors/amrent]]).
- **Results take up to 72 hours, and no preliminary decision or outcome may be communicated to the prospect before full results are received.**
- **Report review covers** identity, SSN/ITIN, credit history, criminal background, bankruptcy and eviction history.
- **The income standard: gross monthly income at or above 2.5× the monthly lot rent.** Below it is a basis for denial; the calculation is documented in Rent Manager. R:I and D:I ratios are both calculated.

### 4. Decision

- **Approved** — move-in coordination begins.
- **Denied** — **the Community Manager is notified before the prospect.** Denial notices must comply with fair housing and adverse-action notice requirements; the recording schedule's own note is "same screen, every applicant."
- **Further review** — escalated to the Directors of Sales and Operations, **carrying a limited summary only, never the full application packet.**

### 5. Offer

- **The offer goes in on a PSA, submitted by the Community Manager or Regional Sales Representative.**
- **The Director of Sales approves or rejects within 24 hours** of receiving the PSA or LOP ([[10-Business/people/leslie-croft]]).
- On acceptance: an Offer Accepted / Pending Approval email goes out and the listing is updated to Pending via a Change Request Form.
- **Rehab Addendum is collected at time of offer or within 3 business days after.**

### 6. Deal-type routing

- **The Closing Coordinator routes every accepted offer to one of three paths — Cash, Financed, or Lease with Option to Purchase** — and compiles the package for that path and that state ([[10-Business/people/melanie-sanchez-soto]]).
- **Financed:** buyer maintains lender contact with **follow-up every 48 hours**, and **no closing documents are compiled before the lender issues clear to close.** Lender registration per community is a prerequisite ([[10-Business/vendors/triad]]).
- **LOP:** the declined-buyer path, with three commercial terms needing Director of Sales approval first ([[50-Products-Sales/lease-with-option-to-purchase]]).

### 7. Closing package and signature

- **Cash package:** Closing Checklist, PSA, Flood Addendum, Closing Worksheet including sales tax, Bill of Sale, payment by wire or certified bank check, Community Lease, Rules and Regulations, **Prospectus (Florida only)**, Rehab Addendum if applicable, and **Forms 400 and 500 (South Carolina only)**. Financed adds all lender-required documentation.
- **24 hours for buyer e-sign via SignEasy. If the buyer misses the window the closing date does not move** ([[10-Business/vendors/signeasy]]).
- **E-sign versus wet-sign is by state** — and the documents contradict each other on Georgia. All deadlines anchor to the closing date in the PSA, or the lease start date in the LOP.
- Executed packages save to SharePoint (Sales Folder › Agreements and Closing Docs) and upload to the Rent Manager Prospect record.

### 8. Closing day

- Schedule the appointment → **final walkthrough with the buyer** → open work orders for anything found, resolved on site by Maintenance → **wait for Accounting's "Funds Received — Clear to Close"** → **hand over keys** → **Move-In Request submitted the same day** with the Closing Coordinator copied → Accounting sends the Closed & Funded notification.
- **Keys are not handed over until Accounting confirms funds received** ([[70-Operations/sops/004-closing-day]]).
- Accounting's three confirmations before an asset can close out: wire payment received, home loan paid off on the floorplan, insurance updated.
- **The alternate closing generation adds harder signing rules:** all parties sign at least one day prior to, but no more than five days before, the official closing date; deposit collected at offer and submitted within 3 days of signing the PSA.

### 9. Prospect becomes Resident

- **Asset Management moves Prospect to Resident and marks the asset inactive only after payment is confirmed AND the floorplan loan is paid off.** Both conditions, not either ([[10-Business/people/justin-minkoff]]).
- Sales adjusts the Rent Manager Asset UDFs to modify the listing feed and updates the CRM; Operations uploads the executed documents.
- **Move-in itself is a Property Operations process** — [[70-Operations/sops/103-move-in]], whose own gate is "no move-in is approved without all required documents and a signed lease on file."
- The flowchart adds two steps the SOP text does not: update the file as the final Home Sales Package and send home files to the community, and a **Sales 30-day follow-up.**

### Known problems

- **Applicants abandon applications, often over concerns about their own history.** The counter-play decided on 2026-08-18 is to call them before they pay the non-refundable fee and deal with whatever stopped them.
- **Legacy residents repeatedly fail credit approval on conversion — "denial after denial."** The absorbers are the AutoMHatic lower-credit buckets and the LOP.
- **The rejected-offer response window has three values and a blank across four closing documents** — 3 days in the closing SOP, 2 days in the combined document, 2 days in 003a, and a missing number in the checklist.
- **Two generations of SOP 006 disagree on who decides an escalated application** — the Directors jointly, or the Regional Manager — and on the terminal state of a denial, Denied or Lost, which changes reporting.
- **002 has no sales-process SOP document at all**, so the offer stage exists only as flowcharts.
- **Two generations of the closing process are both live**, disagreeing on whether a Title Coordinator role and a Make Ready Board gate exist.
- **The Closing Walkthrough Checklist that gates key handover is [TBD — in development] in every version.**
- **Funnel stage ownership is unassigned.** The team agreed on 2026-08-24 to map an owner to every touch, but held the assignments pending a tool capability review.
- **Which system is the single source of truth for prospecting and lead data — MAV or Rent Manager — has not been chosen.**
- **The entire path runs through one Closing Coordinator**, and no one else in the SOP library does that work. "Title Work Process (Master)" is a Tier 1 Critical gap ([[10-Business/people/melanie-sanchez-soto]]).

## Decisions

- 2026-08-24 — Map the funnel touch by touch — new prospect, engaged prospect, tour completed, application completed — with a named owner at each stage, holding assignments until the tool capability review. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-sam-brainstorming-session]])
- 2026-08-25 — Launch the CRM duplicate and merge workflow, new prospects only: Google Ads source retained, otherwise the oldest lead source wins. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]])
- 2026-08-18 — Contact prospective applicants who start but do not finish an application, before they pay the non-refundable fee, to deal with whatever concern stopped them. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-operations-roadwork-warranty-and-system-integration-alignment]])

## Sources

- [[70-Operations/sops/006-lead-intake-tracking-application-and-screening]] — intake, duplicate control, follow-up cadence, screening, the 2.5× income standard and the decision branches.
- [[70-Operations/sops/003-closing-prep-and-documentation]] — the 24-hour and 48-hour clocks, the three deal paths, the state-specific package and the documentation conflicts.
- [[70-Operations/sops/004-closing-day]] — the walkthrough, the funds gate, key handover and the Prospect-to-Resident step.
