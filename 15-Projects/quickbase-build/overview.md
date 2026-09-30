---
type: project
tags: [type/project, dept/systems, dept/operations, status/active]
---

# QuickBase Build, the operational OS

**Status:** active. **Wave 0 is in build**, per Austin 2026-09-02: `WF001`, `WF002` and `WF003` are being built with **QuickBase's own internal team, which is the vendor**, in his words *"assisting in building out the system for us."* So this is a **co-build with a vendor, not a turnkey delivery and not an internal build.** Waves 1 through 8 are still Phase 0. Page created 2026-09-02 by the Page Update, from the drop Austin left in `05-Inbox/` on 2026-09-01.

**What this is.** The build of Parakeet's operating system in QuickBase, with FastField as the field-capture layer in front of it and Rent Manager staying the system of record behind it. Ninety-one SOPs mapped to forty-six workflows, sequenced into nine dependency waves. [[15-Projects/fastfield-phase-i/overview]] is the front end of this; this page is the engine.

**Why it has a page now, and the honest version of the delay.** The source material has been in this Brain since 2026-09-01 and had no page until 2026-09-02. Eighty-six files, six versioned build specs, a master gameplan, a build playbook, a living decision register and a cascade logic map, all in the drop zone. **QuickBase is named on thirty pages in this vault and owned none of them.** The child project got a folder, a register and thirteen tracked rows on 2026-09-02 morning; the parent build had a pile of PDFs. That is the wrong way round, because the child's scope question, whether six or thirteen forms go to FastField, is answered by the parent's mapping table.

---

## The shape of it

| | | Source |
|---|---|---|
| Total SOPs mapped | **91** | Master gameplan v1.1, Executive Summary. **VERIFIED** |
| QB workflows | **46**, `WF001` to `WF046` | Same. **VERIFIED** |
| Already specced | **5** | `WF001` LOCKED v1.2, `WF002` LOCKED v1.3, `WF003` LOCKED v1.1, `WF004` DRAFT v1.0, `WF006` DRAFT v1.0. **VERIFIED** |
| Build waves | **9**, Wave 0 through Wave 8 | Same. **VERIFIED** |
| Shared tables required before Wave 1 | **5** | Section 4. **VERIFIED** |
| Open decisions logged | **18**, of which **11 BLOCKING** | Section 8. **VERIFIED** |
| Current phase | **Wave 0 in build; Waves 1 to 8 in design** | Austin 2026-09-02 on `TD-0422` for Wave 0. The build audit log v1.0 Section 01 still says "Phase 0 - Design & Spec", which was true when written. **VERIFIED** both ways, with dates. |
| Annual asset movement the specced five handle | **$3M to $5M** | Master gameplan, Executive Summary. **SINGLE-SOURCE**, and the gameplan does not show its working. Not entered in `00-Meta/numbers-ledger.md` for that reason. |

Per-workflow status is in [[15-Projects/quickbase-build/workflow-register]].

## The architecture, and it is already decided

Established in `WF001` and governing every workflow after it. This is the answer to the question [[10-Business/systems-architecture]] records as undecided, at least for the workflow layer:

- **FastField is field capture.** Anything a community manager or field person fills in on site or on a phone. Inspections, move-in and move-out reports, site visits, utility verification.
- **QuickBase is the workflow engine.** Stages, gate rules, automations, approval routing, record creation, reporting. It operates in the gaps between Rent Manager's capabilities and field reality.
- **Rent Manager stays the system of record.** Financial ledger, charge schedules, leases, deposits. **QB never writes financial records to RM directly.** Everything flows through a daily batch CSV sync at 18:00 ET.

## The five tables that block everything

These are pre-work, not Wave 1 tasks, because each is read by three or more workflows. The gameplan's estimate is one to two weeks of work that prevents three to six weeks of rework.

| Table | Priority | Feeds | The point |
|---|---|---|---|
| **Residents** | CRITICAL, build first | **21 workflows** | The single most important missing table in the build. Records originate in RM and import by daily batch; QB writes status changes back by automation. |
| **Lease Records** | CRITICAL, build with Residents | 12 workflows | Carries the state field, and **cure period by state has to be stored or derivable from it**: FL 5 business days, SC 5 days, GA 3 business days, NC 10 days, MA 30 days. |
| **Work Orders** | HIGH | 6 workflows | Every maintenance, repair and infrastructure item across the portfolio. |
| **Title & Document Records** | HIGH | 8 workflows | Chain of title for park-owned homes. **Prevents two conflicting title actions on the same asset**, which is the [[00-Meta/commitments]] `CM-19` Royal Oaks failure written as a data model. |
| **Utility Accounts** | HIGH | Utility activation and transfer | Community-level and lot-level where metering applies. |

**Why this section matters more than the wave plan.** The gameplan's Principle 5 names the failure it exists to prevent: build the Eviction pipeline before the Residents table and the eviction workflow has nothing to look up, so it gets rebuilt. **Nobody owns the Residents table build.** That is decision `O-PRE-001` and it is the first BLOCKING item on the list.

## What is blocking, and none of it is routed

Eleven of the eighteen open decisions are marked BLOCKING, meaning the wave cannot be designed until someone answers. **They are recorded here rather than assigned, because the gameplan's owner column is the document's own guess and [[CLAUDE]]'s rule is that no owner beats a guessed one.** The four that gate the most:

- **`O-PRE-001`** Who owns the QB Residents table build, Austin or Justin? It feeds 21 workflows and Wave 1 cannot spec without it.
- **`O-PRE-002`** Does the FastField account support multi-step approval routing, CM to Regional Manager to Regional Director? `WF004`, `WF005`, `WF013` and `WF028` all need it. **This is a question for the vendor and it has the same shape as the photo-capture question already open on the FastField project.**
- **`O-WF004-001` and `O-WF006-002`** The exact Rent Manager field and UDF names for the Move Out and Listings batch sync. Justin or the RM admin. **Two specs cannot lock without them**, and both are in Wave 0.
- **`O-WF014-001`** On a utility transfer, does Parakeet call the utility or does the resident? It may be community-specific, and both `WF014` and `WF005` need it settled.

The full eighteen are in the gameplan's Section 8. **Routing them is the next action on this project**, and it is a routing job rather than a build job.

## Open problems

1. **The portfolio count disagrees with itself across every document in the drop.** The gameplan says **68 communities**, the build audit log says **65+**, the JotForm audit ships a **65-community dropdown**, and [[CLAUDE]] records **67**. This is `KP-0037` seen from a second angle: the same defect the FastField project calls a gate on conversion runs through the QuickBase specs as well. **A relationship field keyed to a wrong community list fails silently and downstream**, which is worse in QB than in a form, because the form at least gets submitted.

2. **The state list disagrees with the portfolio.** The gameplan names **eight states, AL FL GA MA MI NC SC WV**, and encodes state-specific logic against them. [[CLAUDE]] records six live states plus Michigan under management and sale. **West Virginia appears nowhere else in this Brain.** Either the gameplan is carrying a state we do not operate in, or we operate in one nothing here records. Recorded, not resolved.

3. **The SOP denominator disagrees too.** 91 SOPs here against the **109 processes** [[70-Operations/sops/sop-library]] tracks. The two are almost certainly counting different things, the library counting processes and the gameplan counting mapped SOPs, but **neither document says so**, and every effort estimate on this build divides by 91.

4. **Six documents exist in multiple versions and nothing says which is current.** Rehab spec v1.0 through v1.3, home ordering v1.0 through v1.2, disposition v1.0 and v1.1, rollout overview v1.0 and v1.1, gameplan v1.0 and v1.1. **This page reads the highest version number as current**, which is an assumption and is labelled as one. The lower versions are filed to `_superseded/` rather than deleted.

5. **ANSWERED 2026-09-02.** The playbook's "Approved for Build" stamp was real. Austin: *"WF001, WF002, WF003 are being build by QuickBase team. Therefore it is approved for build."* **What the answer opens is bigger than what it closed** - see the two entries below, both of which only became visible once the build was known to be running.

6. **`WF001` depends on three FastField forms that are on no build register in this Brain.** Its spec names four: Home Delivery Confirmation, an **89-item Construction Inspection Checklist**, a **71-item Ops & Sales Readiness Checklist**, and the Listing Form. **Only the Listing Form maps to [[15-Projects/fastfield-phase-i/build-register]]**, as `FF-01` and `FF-02`. The other three appear in no register, no wave beyond this spec, and no owner's list. **The QuickBase team is building the QB side; nobody has said who builds these.** `KP-0053`. Two checklists at 89 and 71 items are the same order of magnitude as the Move Out Inspection at 95 fields, which the FastField project already flags as a live risk against the converter's 20-page ceiling.

7. **This also explains a discrepancy this Brain logged on 2026-09-02 and could not account for.** [[10-Business/vendors/fastfield]] names three FastField forms - delivery confirmation, home listing, weekly PPE check - while the JotForm audit names thirteen and includes neither the delivery confirmation nor the PPE check. **The two sources were counting different things and now the difference has a name:** the audit counts JotForm forms to be migrated, and `WF001`'s spec counts FastField forms in the QuickBase build. **The delivery confirmation was never a JotForm form**, which is why it is absent from a JotForm audit. It is still a form somebody has to build.

8. **RESOLVED 2026-09-02, and it moves the whole project into vendor-management territory.** Austin: *"QuickBase Team is the internal team at QuickBase ie Vendor. They are assisting in building out the system for us."* So the builder is **the vendor's own delivery team**, and the model is **assistance, not turnkey.** [[10-Business/people/road-trip-roster-2026-08]] listing Kevin under **QuickBase** is consistent with this; [[10-Business/vendors/vendor-status-2026-08]] writing *"Kevin (Parakeet)"* looks like the error, **but Austin named the team and not the man**, so the individual is left as recorded rather than reassigned on an inference. `TD-0433`.

9. **A vendor is building the company's operating system and QuickBase has no vendor page.** JotForm has one. FastField has one. **The platform the entire OS runs on has a single row in a status table.** No contract, no contacts, no cost, no renewal date, no named delivery owner on either side, and **no record of what data the vendor's team has been given** - Kevin's outstanding ask was the metadata exports, which are the company's own asset and unit records. **That last one is the same shape as the two identity findings already open in this Brain**: `CM-02`'s indexed credential file and item 2's departed employee still holding two live utility logins. **A vendor team with tenant access and no named owner is how those started**, and the moment to write the owner down is while the relationship is being set up rather than after somebody leaves. `TD-0432`.

10. **"Assisting" means the split has to be written down, and it is not.** A co-build has a line through it: what the vendor configures, what Parakeet configures, who owns testing, who signs off a workflow as done. **Nothing anywhere states that line.** The clearest evidence that it matters is problem 6: `WF001` needs three FastField forms and **each project can see only its own list**, so the forms sit in exactly the gap a co-build creates. `TD-0430`.

11. **Two workflows are marked MERGED and one is a sub-form.** `WF027` absorbed the utility transfer workflow, `WF009` absorbed the construction preventative checklist, and `WF012` Move Out Inspection is a FastField form inside `WF004` rather than a workflow of its own. So **46 is the workflow count, not the count of things to build.**

**Added 2026-09-22 by the Page Update, from the daily closes 2026-09-16 to 09-21.**

9. **The vendor escalated and Zach asked for a week.** A Quickbase discovery session ran 2026-09-17 at 09:00 ET (it had collided with the Melbourne Community Development meeting on 09-15 and moved). **On 2026-09-18 at 12:48 ET Quickbase escalated to Austin, Zach Schwartz and Natalie Magurne, and Zach asked for another week before calling an intervention.** What the escalation concerns is not recorded in the close and is not guessed here. The next discovery session is **2026-09-22 at 10:00 ET, and it collides with Rent Manager with John Hemelgarn at the same hour**; the 09-21 close called that collision the cheapest thing on the page to fix. Read with item 8: this is a vendor managed dependency, so a vendor escalation is the vendor telling you its own delivery is at risk.

## Decisions

- **2026-08 (undated in the source)** - Three-system architecture set: FastField captures, QB routes, RM holds the record, with a daily 18:00 ET batch CSV between QB and RM. Established in the `WF001` spec and applied to every workflow since. **VERIFIED** from the gameplan's Principle 4.
- **2026-08 (undated in the source)** - Shared tables before workflows, and revenue protection after field adoption. The wave order follows data dependency first and business criticality second. **VERIFIED** from Principles 1 and 2.
- **2026-08-19** - Build playbook v1.0 marked "Approved for Build" for `WF001`, `WF002` and `WF003`. **Confirmed by Austin 2026-09-02**, upgraded from SINGLE-SOURCE: *"WF001, WF002, WF003 are being build by QuickBase team. Therefore it is approved for build."* **VERIFIED**, owner-confirmed. The approver is Austin; the builder is the QuickBase team. **Still unrecorded: whether the signed solution design doc Kevin asked for before build proceeded ever existed, or whether this playbook is it.**
- **2026-09-02, Austin** - Wave 0 build is running. `WF001`, `WF002`, `WF003` marked **in build** rather than Built on [[15-Projects/quickbase-build/workflow-register]], because being built is not built and this register exists because of that distinction.
- **2026-09-02, Austin** - The builder is **QuickBase's own internal team, the vendor**, assisting rather than delivering turnkey. **VERIFIED**, owner-stated. This makes Wave 0 a vendor-managed dependency and the delivery split a thing that has to be written down.
- **2026-09-02, Austin** - All thirteen JotForm forms route through FastField and QuickBase. Recorded on [[15-Projects/fastfield-phase-i/overview]] and still in tension with the audit's own migration-target column.

## Related

- [[15-Projects/fastfield-phase-i/overview]] - the front end. Its thirteen forms are the field-capture half of these workflows.

## Sources

- [[15-Projects/quickbase-build/parakeet_master_build_gameplan_v1.1.pdf]] - the primary artefact for everything on this page. 91 SOPs, 46 workflows, 9 waves, 5 tables, 18 open items.
- The rest of the drop is filed to this folder: six build specs in `specs/`, the playbook, the rollout overview, the living build audit log, the cascade logic map, and the superseded versions in `specs/_superseded/`.
- [[00-Meta/daily-close/2026-09-18]] — item 13, the escalation; `00-Meta/daily-close/2026-09-17.md` calendar for the discovery session and `2026-09-21.md` item 12 for the collision. Added 2026-09-22.

