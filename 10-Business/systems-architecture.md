# Systems / Data Architecture

**What this is:** The undecided single source of truth across MAV, Rent Manager, the RentViewer warehouse and Camp Spot, and the five-week runway that governs it.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26. **Two documents filed beside this page 2026-09-15**, see the section *A canonical key standard arrived* at the foot.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

**Created**: 2026-08-26, from `C:\Users\AustinBerk\Desktop\Parakeet Week in Review.docx` (compiled 2026-08-25 from Plaud recordings, 2026-08-19–24 road trip). **SINGLE-SOURCE** unless otherwise noted.

**Naming flag, added same day**: `00-Meta/decisions/2026-08-26-company-assessment-plan.md` (a separate, not-yet-executed plan from the same evening) proposes a WS4 output at `10-Business/systems-architecture.md` covering this exact question — MAV/Rent Manager/RentViewer/Camp Spot single source of truth. That plan file has not been executed. **Before building that WS4 output, reconcile it with this file rather than creating a second one** — this file already carries the current facts on that question.

## The open question

**Single source of truth across MAV CRM, Rent Manager, the RentViewer warehouse, and Camp Spot has not been decided, and it governs real spend.**

Jon Wyss's stated position (source writes "John" — see the spelling note in `10-Business/people/road-trip-roster-2026-08.md`): **warehouse-first may make the MAV MCP redundant.** If the RentViewer warehouse becomes the single source of truth, continued MAV MCP build spend is money on overlap. Nothing has decided this yet. Tracked as a standing decision at `00-Meta/parked-decisions.md` #4.

**Next action, per the source**: get the joint call scheduled between MAV and RentViewer (Saad and Dan) to scope the CRM ↔ warehouse integration, and decide the single source of truth before paying for both.

## The clock

**A 5-week runway to October snowbird season governs this entire convergence**, not just the architecture question. In the same window:

- Uniti AI sales agent — target live ~end of September 2026 (vendor's own standard is 30–45 days from kickoff).
- MAV dedup rules + MCP sandbox — sandbox call scheduled 2026-08-29, 3:00 PM ET, connecting to the Claude Teams account with ~900 tools and real data.
- RentViewer warehouse rollout — sequenced Austin + one, then Zach and Stewie; GL not yet in the warehouse.
- Sales org hires — seats targeted filled within 4 weeks (see `50-Products-Sales/sales-org-buildout.md`).

Missing this runway means going into snowbird season — the highest-volume selling window — without the systems the sales org will depend on.

## What the 2026-08-31 consultation established

Added 2026-08-31 from [[70-Operations/meetings/2026-08-31-listings-pipeline-and-ai-cost-consultation]], recording read in full. **This is the first VERIFIED material on this page**; everything above it is 2026-08-26 SINGLE-SOURCE and has not been re-verified.

- **The listings chain, in order:** Rent Manager asset record, then either straight to the Parakeet website and MH Village, or through **My State MLS** and out to Realtor.com, Zillow and Trulia. My State MLS is a mandatory hop, not a choice. Detail on [[50-Products-Sales/home-sales]].
- **The data warehouse is the historical layer, and it exists because Rent Manager overwrites.** Microsoft SQL, run by a third party who originally built it for Tableau and Power BI. It snapshots daily, weekly or monthly depending on the report. The worked example given: listing price is **a single field** in Rent Manager with no history, so without the warehouse there is no way to answer when a price was dropped or what happened after. It does the same for prospect stage status, which Rent Manager also overwrites.
- **The MCPs are live, and that is a change from this page's 2026-08-26 position.** Austin, on the recording: MCPs direct to the Rent Manager API and to the data warehouse, turned on *"in the last two weeks."* Corroborated independently by `10-Business/connector-status.md`, which records both as live on 2026-08-31 with `GeneralLedger` report 51 still failing. **VERIFIED across two sources.**
- **The consultant's design rule, accepted on the call without pushback:** anything built on top of the source of truth should only visualise it, never re-save it. His reasoning is that every re-save is a desynchronisation risk, and John confirmed that is exactly what the current CSV hop produces *"every once in a while."* This is the same question as the open one at the top of this page, arrived at from a different direction.
- **His recommendation on which source to build the dashboard against was the warehouse, not Rent Manager**, on two grounds: historical analytics need it, and the warehouse operator will move faster on access than the property management vendor will. *"They won't move their ass for the AI advancement as fast as those guys processing your data."*
- **The prospect funnel dashboard aggregates roughly fifteen sources**, named on the recording: Nav CRM exports, a data warehouse CSV, Rent Manager CSV drops including the asset listing, Microsoft Bookings for tour booking, an RV bookings website, Google Analytics and RingCentral. It is not live or circulated.
- **Naming discrepancy, flagged not resolved:** this page records the AI sales agent as **Uniti**; the 2026-08-31 recording says **Unity**, describing it as mobile-home-park specific, integrating with Rent Manager by API, and used by the major operators such that Parakeet is *"kind of locked into using them."* Almost certainly the same vendor under two spellings, but nothing confirms it and `10-Business/vendors/vendor-status-2026-08.md` carries the other spelling too. Worth one look before either name reaches a contract or a report.
- **QuickBase and FastField are further along than this page's carryover note suggests.** See [[10-Business/tools-and-systems]] for what the recording establishes about scope and sequencing.

## Known gaps

- **Camp Spot invisibility**: 6 RV communities (~400 sites) are not visible to Rent Manager at all. Interim fix is a nightly CSV drop to Uniti (owned by Jon Wyss); webhooks are the longer-term plan. Park models sold at all-Camp-Spot properties could be missed entirely under the current gap.
- **No formula-change approval process** for the RentViewer warehouse — needs to be defined as part of the rollout, before more than two people are touching it.
- **Power Automate governance**: dedicated server accounts only, no individual-drive access, nobody builds their own automations — a rule Jon Wyss has stated but that has no enforcement mechanism recorded yet.
- **AI adoption is currently gated to a small group** — output access limited on purpose. The source's own framing: "95% of the company doesn't use AI yet" — education, not access, is described as the bottleneck. Jon Wyss separately wants an independent tech advisor for the broader build-vs-buy question (self-built vs. Corner IQ vs. others) — see `00-Meta/parked-decisions.md` #6.
- **QuickBase carryover**: a walkthrough has happened; Kevin needs the metadata exports and wants a signed solution design doc before build starts.
- **Nobody owns scheduled-task reliability, and it failed on 2026-08-31.** The listings dashboard fires at 06:00 on weekdays; on the morning of 2026-08-31 John said on the call *"this is the wrong version that misfired this morning"*, and the point went by unremarked. The earlier Chrome-driven version of the same job *"was always breaking with the attachment."* There is no logging, alerting or retry recorded anywhere, and no owner.
- **The website's field mapping has no internal owner.** A third party holds an API into Rent Manager and maps fields out to the portals. Asked how it works, the answer twice on the recording was *"I don't really know how that works… but it seems to be working."* It is the only link in the listings chain nobody inside the company can describe.

## An idea worth reviving

Dan's "podcast digest" concept for asset-management updates — surfaced once this week, not developed. Noted here so it isn't lost.

## A canonical key standard arrived, and it answers part of the open question without anyone deciding it

**Filed 2026-09-15 by the Page Update** from `05-Inbox/Building Automated Dashboard/`, where the two files landed 2026-09-09 22:16 ET and sat six days. Now at [[10-Business/systems-architecture/01_DATA_DICTIONARY_AND_KEYS]] and [[10-Business/systems-architecture/02_CROSSWALK_SCHEMAS]]. Austin's ruling on where: *"go with recommendation"*, beside this page rather than a new project folder.

**What they are.** A version 1.0 *Data Dictionary and Canonical Key Standards* and the matching *Crosswalk Schemas* DDL for a `core` warehouse schema: surrogate keys (`PROP-`, `UNIT-`, `ASSET-`, `EMP-`) that downstream dashboards join on, source IDs kept only to map ingestion, names and lot labels treated as mutable display attributes, a unit key tied to the dirt and an asset key tied to the home so a home can move lots without breaking either, Microsoft Entra ID as the identity anchor for every employee login, and a quarantine table so an unmatched record fails loudly. Six tables: property, unit, asset, employee, employee to property assignment, and the quarantine log.

**What they decide, or appear to.** The dictionary declares system of record boundaries: **Rent Manager** for the ledger, tenancy and lot status; **FastField** for point in time audits; **Quickbase** for infill milestones, capex and utility tie ins; **Entra ID** for identity; **SharePoint** for documents. **That is an answer to the question at the top of this page**, which records the single source of truth as undecided across MAV, Rent Manager, the warehouse and Camp Spot. The dictionary does not mention MAV, the RentViewer warehouse or Camp Spot at all.

**What is not established, stated plainly.** Both files say *Approved Architecture* and *Version 1.0* and carry **no author, no date and no approver**. **Austin was asked who wrote them and answered on 2026-09-16: *"i don't know who wrote the data dictionairy."*** The owner of this vault cannot source a document in it that calls itself approved. Traced as far as it goes the same morning: the files were written to the Inbox at 22:16 and 22:17 ET on 2026-09-09, ninety seconds apart; no Outlook message in any folder contains *Canonical Key Standards* or `property_crosswalk`; no Teams chat since 2026-09-01 mentions a data dictionary (48 of 50 chats scanned, no channel coverage); the vault's git history stops at 2026-09-02, before they arrived. **So nobody sent them and nobody discussed them where this Brain can see.** The folder name reads like a chat or project title, the numbered filenames and the twice-pasted first half of file 01 are the shape of an assistant's output saved by hand; that is an inference and is labelled as one. **Standing ruling for this page: treat both files as an unsigned proposal. Nothing on this page or any other is to cite them as an approved standard until a person puts their name to them.** File 01 also contains its own first half twice, a paste defect, left as found. **A standard nobody has signed is not a decision; it is a proposal that has been formatted like one.** The property level crosswalk this Brain already builds (`property-master-table-refresh`) and the eleven warehouse models on `10-Business/data-lineage` are the two things it would have to reconcile with before anyone builds a table from it.

## Related

- `10-Business/vendors/vendor-status-2026-08.md` (MAV, RentViewer, Camp Spot, Uniti, Corner IQ)
- `00-Meta/parked-decisions.md` #4, #6
- `50-Products-Sales/sales-org-buildout.md`
