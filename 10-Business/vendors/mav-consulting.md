# MAV Consulting

**What this is:** the CRM — the system referenced but never named throughout the SOP library — and the same relationship that covers the RentViewer data warehouse work.

**Status:** current — 2026-08-30

## The facts
- **What they supply:** the CRM used for prospect tracking, plus the data-warehouse and MCP integration work around it. **The owner confirmed on 2026-08-30 that the CRM referenced anonymously throughout the process library is MAV Consulting.** The MCP sandbox is described on the 2026-08-24 recording as a Zoho environment with roughly **900 tools** available.
- **Who uses it:** Sales logs every prospect in the CRM at first contact (SOP 006) and updates it on every lease-with-option-to-purchase (SOP 003a); the CRM is named in SOP 002's systems list for the offer-to-approval path. Ozzy, John and Austin were on the vendor call.
- **This closes a documented gap.** SOP 006 and SOP 003a both reference "the CRM" without naming it, and **the 600–699 Systems / IT / Reporting SOP band is entirely empty** — so the CRM had no page, no SOP and no named vendor anywhere in 242 process files until now. **Leslie Croft's Q1 2026 rock was "Implement CRM."**
- **How critical: high.** Every lead the company takes lands here, against a 2026 plan to list ~400 homes and sell ~400. Rent Manager's Prospect module holds the record of truth for a prospect who converts, so the base business survives — but pull the CRM and lead intake, duplicate control, follow-up cadence and the whole sales reporting layer go with it, and the company loses the only system that tracks demand before it becomes a resident.
- **Duplicate/merge workflow — launched 2026-08-25**, for **new prospects only**, not the existing duplicates: if Google Ads is the ad source that value is retained, **otherwise the oldest lead source wins**.
- The rules were to be documented in writing and sent **before** launch, with a walkthrough call on **2026-08-26** — rules document first, then launch.
- **MCP sandbox, due 2026-08-29:** built on Parakeet's **real CRM data** across Prospects, Tenants, Units, Properties and Tours/Meetings, but **deliberately not connected to the live Rent Manager account**. The 3:00 PM EST Friday call was to connect it to the team Claude account and run initial test prompts. Historical timelines do not come across in the first export.
- **Migration order: Meetings/Tours second or third**, after converted prospects.
- **Reporting design: a daily RentViewer sync into the data warehouse** — likely Microsoft SQL — replacing the current practice of someone manually pulling backups and pushing them to the cloud, which is slow and sometimes wrong. **Everything should be reachable through Claude via the warehouse**, so field and corporate users get information in digestible form through agents.
- **Engage the RentViewer team before building anything**, to avoid duplicate flows between MAV, Rent Manager, the warehouse and the CRM. Austin owns the introduction to Saad and Dan on the RentViewer side.
- **Cost, governance and workflow capability are to be assessed before any full deployment:** token and API consumption, data privileges and audit logs, and which agents and scheduled functions push or pull CRM data.
- **Known problems, all flagged on the call and none solved:** two people with the same name but different contact details — roommates, for example — **would be merged under the oldest-value rule**; **Claude audit log visibility was described as limited**, a governance gap if agents can delete or overwrite records, with no mitigation plan or timeline; and **which system is the single source of truth for prospecting and lead data, MAV or Rent Manager, was agreed as necessary but not chosen.**
- The wider unfinished business: the March deck's CRM slide still asks "Where are we, what's left to launch? Roadmap to full onboarding. Users & Admins? RM Integration" and "What reporting will the system provide?" — none of which the SOP library answers.

## Decisions
- 2026-08-24 — Launch the duplicate and merge workflow on the Parakeet account on 2026-08-25, new prospects only: Google Ads source retained, otherwise the oldest lead source wins. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]])
- 2026-08-24 — Build the MCP sandbox on real CRM data across Prospects, Tenants, Units, Properties and Tours/Meetings, kept disconnected from the live Rent Manager account. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]])
- 2026-08-24 — Use RentViewer to sync data daily into the data warehouse instead of manual backup pulls, engage the RentViewer team before building, and make everything reachable through Claude over the warehouse. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]])
- 2026-08-24 — Assess cost, governance and workflow capability — token and API consumption, data privileges and audit logs, and which agents push or pull CRM data — before any full deployment. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]])

## Sources
- [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]] — the merge rules, the launch and sandbox dates, the migration order, the warehouse design and the three open flags.
- [[70-Operations/sops/006-lead-intake-tracking-application-and-screening]] — where "the CRM" is used and never named.
- Austin, in the Structure Interview, 2026-08-30.
