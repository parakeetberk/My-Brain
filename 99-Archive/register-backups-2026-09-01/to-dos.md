# Open to-dos

**What this is:** the open to-do register — every action with a named owner from the August 2026 southeast tour, every open [TBD] that is blocking an SOP approval, and every open SOP conflict, grouped by owner.

**Status:** current — 2026-08-31. The priority queue below was set by Austin on 2026-08-31 out of the second-vault merge. Five rows added the same day from the morning brief sweep, and **twenty-three more that evening from the Plaud transcript filing and Austin's ruling on it** — see *Routed from the 2026-08-31 morning brief* and *Routed from the 2026-08-31 Plaud transcript filing*.

## The facts

- **Every line carries an owner.** Where the source names nobody and no owner is obvious from the source itself, the line reads **"unassigned"**. No owner has been inferred, and no deadline has been added that the source did not state.
- **Status is "open" on every line.** Nothing in the vault records any of these as closed.
- Grouped by owner so one person's list can be read straight through before a Tuesday one-on-one.
- Owners are recorded as the source names them, usually a first name. Two of them are ambiguous against the people pages: **Alex** could be Alex Fals or Alexander Stuart, and **Chris** is not established as Chris Pitzer. Neither has been resolved by guessing.
- Three sources feed this register: the 27 filed tour transcripts in `70-Operations/meetings/2026-08-southeast-tour/`, the open [TBD] markers on the SOP process pages, and the open conflicts on [[70-Operations/sops/sop-library]].

## Priority queue — set 2026-08-31

**What this is:** everything the second-vault merge surfaced, raised to high priority by Austin on 2026-08-31. It sits above the tour register below because these are the items where the cost of not acting is measurable this week, not this quarter.

**Read the owner column honestly.** Five of these eleven have no owner and cannot get one from a file. The vault does not invent owners - where the source names nobody, the row says unassigned and names the forum where Austin can settle it in a minute. A proposed owner is marked *proposed* and is a role-based suggestion, not a fact.

### Tier 1 — name an owner today

| # | Item | Owner | Why it is here | Where | Status |
|---|---|---|---|---|---|
| P1 | **Lucky Clover - a resident pointed a gun at contractors, and a second threatened self-harm.** The manager was alone on-site. The source is explicit that this needs a trespass, law-enforcement and eviction protocol, not sympathy. | **unassigned** - the Monday 08:30 catch-up with Jon was the named forum and it ran on 2026-08-31 **double-booked against the Woods Oviatt "Hunter" call in the same slot**. No name came out of it. Next forum: the Friday 14:00 ET L10 | Physical safety, an employee alone on-site, and **twelve days with no owner across six channels**. The 2026-08-28 Friday L10 passed without it being raised, and so did the Monday catch-up that was supposed to fix that. This is the single item on this page where the downside is a person, not a number. | [[00-Meta/commitments]] item 7 · [[60-Communities/lucky-clover]] | open — day 12 |
| P2 | **Great Oak - boil water notice active, aerator pump out, vendor absent.** The road-trip review calls it the most urgent property item in the portfolio. | **unassigned** - same forum, same minute, and the forum collided | A public-health notice on a live RV resort with no named owner for **twelve days**. The 2026-08-26 construction call led its agenda with Great Oak and never mentioned the notice, and a targeted search of the whole of 2026-08-31 across mail and Teams returns **zero mentions of any kind**. The item does not have a forum rather than having been handled. | [[00-Meta/commitments]] item 8 · [[60-Communities/great-oak-rv-resort]] | open — day 12 |

### Tier 2 — the reporting numbers disagree with themselves

| # | Item | Owner | Why it is here | Where | Status |
|---|---|---|---|---|---|
| P3 | **Rule on what counts as an operating property, once.** Shell Pointe, Geiger Key and Congress sit in the 67-row portfolio table with current occupancy and lot data, and are excluded from reporting by Austin's own 2026-08-26 instruction. | **Austin** - it is his instruction on both sides | Two pages in this Brain currently give different answers to the same question depending on which one someone opens. Every downstream number inherits whichever they happened to read. | [[00-Meta/open-items]] C2 · [[80-Finance/portfolio-reporting-rules]] | open |
| P4 | **Reconcile the unit count. 6,379 against 8,020.** The Property Data Sheet and the RentViewer warehouse are 1,641 units apart and nothing in the vault reconciles them. | **unassigned** - *proposed: Zach Schwartz, who owns the warehouse rollout* | "How many units do we have" is a board question and a lender question, and right now the answer depends on which system you ask. The reporting-rules page flags the same gap independently. | [[00-Meta/open-items]] C1 · [[60-Communities/portfolio-baseline-warehouse]] | open |
| P5 | **Hunter Springs MHC is carrying $35,056 revenue on a leg that should be dormant.** Austin, 2026-08-26: MHC is the prior leg, MHP is the current one. | **David Berman** - the source itself says this needs one look from accounting | Either revenue is mis-booked to a legacy record or it is the tail of the transaction. Until it is settled, reporting both records double-counts roughly $35K. | [[00-Meta/open-items]] C6 · [[80-Finance/portfolio-reporting-rules]] | open |
| P6 | **Settle whether the warehouse or the Property Data Sheet answers occupancy.** 77.67% August 2026 warehouse against 82.5% December 2025 weighted, five rows excluded. | **unassigned** - *proposed: Zach Schwartz* | Different periods and different denominators, five points apart. Neither is wrong; nothing says which one answers the question when someone asks. | [[00-Meta/open-items]] C3 | open |

### Tier 3 — the migration items, all cheap now and expensive later

| # | Item | Owner | Why it is here | Where | Status |
|---|---|---|---|---|---|
| P7 | **Resolve `/sites/ParakeetHome` against `/sites/ParakeetHomes` before any consolidation touches site plans.** One letter apart, neither a superset, five communities differ materially. | **Albert** - he owns the migration | Deleting either one loses data that exists nowhere else. This is the most dangerous item in the file estate and consolidation is the only moment it is cheap to fix. | [[10-Business/storage-inventory/known-problems]] #1 | open |
| P8 | **Get the corporate Google Shared Drives out from under a personal Gmail account.** Cap tables, fund subscriptions, K-1s, an LPA and executed signature pages sit in Shared Drives that `austinrberk@gmail.com` is a standing member of. | **Austin with Albert** | No Workspace admin lifecycle governs that access and a standard audit query reports the account clean. If the account is lost or compromised, both continuity and confidentiality sit outside company control. Three drives is a floor - memberships cannot be enumerated. | [[10-Business/storage-inventory/known-problems]] #4 · [[10-Business/storage-inventory/gdrive-personal]] | open |
| P9 | **Normalise community names before the migration, not after.** Operations and Construction each hold 71 folders and they are not the same 71 - six, four and eight assets differ, including typos like `WHSIPERING PINES MA`. | **Albert** | Any join on community name silently mismatches about 18 assets, which quietly corrupts every cross-system report built on it. After the move it calcifies. | [[10-Business/storage-inventory/known-problems]] #3 | open |

### Tier 4 — housekeeping, but they cost something if left

| # | Item | Owner | Why it is here | Where | Status |
|---|---|---|---|---|---|
| P10 | **Name the on-site manager at Lucky Clover.** The road-trip review says Angel, the December 2025 org chart records no link, the March 2026 infill sheet says Erica. | **Resolved: Angel** — confirmed by Austin on the delegation board | P1 cannot be assigned to a person nobody can name. This one blocks the one above it. | [[00-Meta/open-items]] C5 | **CLOSED 2026-08-31 — Austin confirmed Angel** |
| P11 | **Decide whether the scheduled briefs get rebuilt against this Brain.** The morning brief ran Monday to Friday 6am and the Weekend Pulse Friday 7pm, both artifact-only by Austin's 2026-08-29 decision. Those tasks lived in the Claude Code project, not here. | **Austin** | The briefs were the only mechanism that noticed items 7 and 8 going eleven days without an owner. Nothing in this Brain currently does that job on a cadence. | [[00-Meta/decisions/2026-08-29-brief-delivery-artifact-only]] · `99-Archive/2026-08-briefs/` | open |

**Not on this list, deliberately.** The empty `05-Inbox/brain/` folder needs deleting by hand and Belmart has no home in this Brain. Both are noted in `05-Inbox/_needs-sorting.md`; neither costs anything to leave until Austin is at the machine.

## From the August 2026 southeast tour

### Named owners

**Austin** — 5 open

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Contact Chris (counsel) to set up the meeting with Adam and finalize the outstanding legal and financial terms on the contract extension. | Austin | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-management-and-strategic-ai-integration-review]] | 2026-08-18 | open |
| Get a photographer back out to the community for updated pictures. | Austin | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-management-and-strategic-ai-integration-review]] | 2026-08-18 | open |
| Add the new unit number markers to the master project list. | Austin | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-management-and-strategic-ai-integration-review]] | 2026-08-18 | open |
| Discuss the Corner IQ trial internally and follow up with the founders; their next onboarding batch is the week of 2026-08-26 to 2026-08-28. | Austin | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-management-and-strategic-ai-integration-review]] | 2026-08-18 | open |
| Connect MAV with Saad and Dan on the Rent Viewer team — after 2026-08-29. | Austin | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]] | 2026-08-24 | open |

**John** — 1 open

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Keep pushing the collapsed pipe repair to completion. | John | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-shady-and-druid]] | 2026-08-19 | open |

**Demetria** — 1 open

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Publish the Loan Coordinator job description. | Demetria | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-sam-brainstorming-session]] | 2026-08-24 | open |

**Chris** — 2 open

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Replace the chipped kitchen drawer fronts under manufacturer warranty, and sort the kitchen and stove outlet issue. | Chris | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-vantage-oaks-site-visit]] | 2026-08-21 | open |
| Arrange delivery of the needed home supplies with the store contacts. | Chris | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-vantage-oaks-site-visit]] | 2026-08-21 | open |

**Alex** — 1 open

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Help map and block the season lots (a speaker who is not individually identified is making the lot notes). | Alex | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-whispering-pines-mh-and-rv-site-visit]] | 2026-08-20 | open |

**Fernando** — 1 open

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Check the graveling. | Fernando | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-whispering-pines-mh-and-rv-site-visit]] | 2026-08-20 | open |

**Heidi** — 1 open

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Update the deck with the numbers circulated on Monday 2026-08-17. | Heidi | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-car-convo-with-joe]] | 2026-08-20 | open |

**Joe** — 1 open

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Send through his thoughts to be put together and shared — Wednesday 2026-08-26. | Joe | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-sam-brainstorming-session]] | 2026-08-24 | open |

**MAV** — 3 open

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Send the duplicate and merge testing document — 2026-08-25. | MAV | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]] | 2026-08-24 | open |
| Complete the MCP sandbox setup (Prospects, Tenants, Units, Properties, Tours/Meetings) — 2026-08-29. | MAV | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]] | 2026-08-24 | open |
| Send details on the 900-plus MCP tools and example use cases before the Friday call. | MAV | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]] | 2026-08-24 | open |

**MAV and Parakeet** — 1 open

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Review the testing document and the workflow rules together — 2026-08-26. | MAV and Parakeet | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]] | 2026-08-24 | open |

**Vendor** — 3 open

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Email John and Austin a Calendly link to schedule a 30-minute intro call with an executive. | Vendor | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-rellit-conversation]] | 2026-08-21 | open |
| Prepare for the intro call around the business model, with targeted follow-up questions. | Vendor | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-rellit-conversation]] | 2026-08-21 | open |
| Plan and schedule the deep-dive technical demo of the end-to-end flow from the current finance stack. | Vendor | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-rellit-conversation]] | 2026-08-21 | open |

**Team** — 6 open

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Overnight in Savannah — 2026-08-18. | Team | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-auburn-ridge-visit]] | 2026-08-18 | open |
| Regency 8:30 to 9:00 AM, then Brunswick and Town and Country, possibly Ormond and New Smyrna — 2026-08-19. | Team | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-auburn-ridge-visit]] | 2026-08-18 | open |
| Visit Space Coast — 2026-08-20. | Team | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-paradise-lakes-site-visit]] | 2026-08-19 | open |
| Visit Vantage — 2026-08-21. | Team | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-paradise-lakes-site-visit]] | 2026-08-19 | open |
| MCP review call: connect the sandbox to the Claude account and run test prompts — 2026-08-29 at 3:00 PM EST. | Team | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]] | 2026-08-24 | open |
| Hold the planning call in two parts — 2026-08-26. | Team | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-sam-brainstorming-session]] | 2026-08-24 | open |

**Group** — 1 open

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Review the CRM, contact funnel and workflows, including his part of it — week of 2026-08-24. | Group | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-leslie-call-re-auzzi]] | 2026-08-22 | open |

### Unassigned — no owner named in the source, and none obvious

150 items. These are recorded exactly as the transcripts left them. **Assigning an owner to each is itself a to-do**, and the fastest place to do it is the Friday Executive EOS call.

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Paint the three remaining speed bumps. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-auburn-ridge-visit]] | 2026-08-18 | open |
| Price a utility golf cart with a folding back seat. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-auburn-ridge-visit]] | 2026-08-18 | open |
| Hold the call with Leslie and John on the make ready board and infill process findings, ahead of the Friday presentation — 2026-08-19. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-auburn-ridge-visit]] | 2026-08-18 | open |
| Follow up on the entrance sign near lots 6 and 114. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-auburn-ridge-visit]] | 2026-08-18 | open |
| Price and assess a Metron meter installed after the main city meter to detect supply line leaks. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-auburn-ridge-visit]] | 2026-08-18 | open |
| Settle the donation amount and mechanism for the Path Kids Club flooring. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-auburn-ridge-visit]] | 2026-08-18 | open |
| Decide what the old office structure becomes: picnic area or community library. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-auburn-ridge-visit]] | 2026-08-18 | open |
| Receive the homes delivering at Northgate around 2:00 PM — 2026-08-20 (Leslie also arrives that day). | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-auburn-ridge-visit]] | 2026-08-18 | open |
| Send the three power of attorney documents to Melanie for overnight shipping to the title company. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-management-and-strategic-ai-integration-review]] | 2026-08-18 | open |
| Walk the incoming rehab crew through the floor repairs and rehab tasks when they arrive, and get spot repairs done on the floors of existing rentals. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-management-and-strategic-ai-integration-review]] | 2026-08-18 | open |
| Help the prospective buyer finish their application so the pending purchase can close. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-management-and-strategic-ai-integration-review]] | 2026-08-18 | open |
| Hold the walkthrough of Rent Manager with the implementation team — 2026-08-25 (date stated in the meeting; no owner named). | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-operations-roadwork-warranty-and-system-integration-alignment]] | 2026-08-18 | open |
| Draft and send the firm response to the roadwork vendor, with prior emails, photos and the contract attached. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-operations-roadwork-warranty-and-system-integration-alignment]] | 2026-08-18 | open |
| Make the compromised storm drain safe; it is an immediate hazard. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-operations-roadwork-warranty-and-system-integration-alignment]] | 2026-08-18 | open |
| Provide the implementation team with the Rent Manager metadata exports: community list, property IDs, lot numbers, occupancy status. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-operations-roadwork-warranty-and-system-integration-alignment]] | 2026-08-18 | open |
| Contact the county about the deemed-real-property status and what it requires. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-operations-roadwork-warranty-and-system-integration-alignment]] | 2026-08-18 | open |
| Inventory the newly found maintenance shed, including the zero-turn mower. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-operations-roadwork-warranty-and-system-integration-alignment]] | 2026-08-18 | open |
| Secure and clarify the title for the pending sale, and identify the right contact for the resident home title problem. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-operations-roadwork-warranty-and-system-integration-alignment]] | 2026-08-18 | open |
| Scope and budget fence renewal and removal of the chain link sections. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-operations-roadwork-warranty-and-system-integration-alignment]] | 2026-08-18 | open |
| Buy a batch of gift cards for resident recognition, that night if possible. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-applegate-site-visit]] | 2026-08-19 | open |
| Clear the backlog on 227, 248 and the home delivered July 22. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-applegate-site-visit]] | 2026-08-19 | open |
| Escalate Champion repeated absence and unblock the two waiting homes. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-applegate-site-visit]] | 2026-08-19 | open |
| Find out whether a regulation prevents extending the white PVC sleeve on the wellhead. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-applegate-site-visit]] | 2026-08-19 | open |
| Deal with the home that has no wood under it and is about to fall over. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-applegate-site-visit]] | 2026-08-19 | open |
| Complete utility locating and mapping for all existing and new lines before any further digging. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-paradise-lakes-site-visit]] | 2026-08-19 | open |
| Get Spectrum timeline for removing its pole and wires so the new pole can be moved back. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-paradise-lakes-site-visit]] | 2026-08-19 | open |
| Install the temporary barriers at the roadside pole and the broken gate exit. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-paradise-lakes-site-visit]] | 2026-08-19 | open |
| Re-add the septic and seawall items to the project list. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-paradise-lakes-site-visit]] | 2026-08-19 | open |
| Keep the sign design and approval moving. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-paradise-lakes-site-visit]] | 2026-08-19 | open |
| Finalize the mailbox vendor and start the replacement. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-regency-i-site-visit]] | 2026-08-19 | open |
| Install the new sign at the entrance and confirm placement against the city easement. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-regency-i-site-visit]] | 2026-08-19 | open |
| Schedule tree trimming before hurricane season. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-regency-i-site-visit]] | 2026-08-19 | open |
| Patch and seal coat Green Oak and assess sections for repaving. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-regency-i-site-visit]] | 2026-08-19 | open |
| Clear the dumpster area, remove the tire container, cancel the dumpster service and convert the space to trailer storage. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-regency-i-site-visit]] | 2026-08-19 | open |
| Inspect the sinkholes near the speed bump and in the middle of the road. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-regency-i-site-visit]] | 2026-08-19 | open |
| Take down the fences called out on the walk. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-regency-ii-visit]] | 2026-08-19 | open |
| Price a zero-turn mower and assess a small excavator against current ditch and overgrowth clearing costs. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-regency-ii-visit]] | 2026-08-19 | open |
| Set a standard day for required resident lawn mowing and enforce it. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-regency-ii-visit]] | 2026-08-19 | open |
| Get the sideways double-wides on two blocks properly tied down. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-regency-ii-visit]] | 2026-08-19 | open |
| Resolve the resident plantings sitting on land that is not theirs, particularly along the county ditch access route. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-regency-ii-visit]] | 2026-08-19 | open |
| Send the resident memo by email and in print. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-shady-and-druid]] | 2026-08-19 | open |
| Consult the post office before standardizing the mailboxes, then replace them all with white PVC singles and reflective numbering. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-shady-and-druid]] | 2026-08-19 | open |
| Price a Gator or similar utility vehicle for the maintenance role. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-shady-and-druid]] | 2026-08-19 | open |
| Get the streetlights on the left side replaced. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-shady-and-druid]] | 2026-08-19 | open |
| Treat the pond duckweed and cut back the pond overgrowth (the pond crew is scheduled to return). | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-shady-and-druid]] | 2026-08-19 | open |
| Post notices on cleanup responsibility for residents using the field area. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-shady-and-druid]] | 2026-08-19 | open |
| Get the Habitat subpoena documents signed and calculate the holdback before sending the distribution. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-shady-and-druid]] | 2026-08-19 | open |
| Set up the call with the external party on data integration and dashboard capability. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-shady-and-druid]] | 2026-08-19 | open |
| Consolidate the trip notes and send them to Natalie. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-shady-and-druid]] | 2026-08-19 | open |
| Research the journal entries that lack detailed descriptions. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-19-shady-and-druid]] | 2026-08-19 | open |
| Reserve 20 million dollars of capacity for the Bay Area deal. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-car-convo-with-joe]] | 2026-08-20 | open |
| Decide how to handle on-site prospects who call the 24-hour line instead of coming into the office. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-car-convo-with-joe]] | 2026-08-20 | open |
| Drop the bag at Southgate. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-car-convo-with-joe]] | 2026-08-20 | open |
| Check whether Rhonda has the keys for the other unit. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-car-convo-with-joe]] | 2026-08-20 | open |
| Confirm the permit requirement for the porch wall and the plan to cut it in half. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-car-convo-with-joe]] | 2026-08-20 | open |
| Decide whether to cut the equity commitment from 5 percent to 3.5 percent and where the difference is reallocated. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-car-convo-with-joe]] | 2026-08-20 | open |
| Draft and distribute the resident notice with the engineering and septic cover letter. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-lucky-clover-site-visit]] | 2026-08-20 | open |
| Create the Power Automate server accounts and move off individual drive access. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-lucky-clover-site-visit]] | 2026-08-20 | open |
| Buy the larger flag and the parakeet flag and install them. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-lucky-clover-site-visit]] | 2026-08-20 | open |
| Remove the three tires from the storage area. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-lucky-clover-site-visit]] | 2026-08-20 | open |
| Install the lighting in the shuffleboard and common area off the dumpster photocell. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-lucky-clover-site-visit]] | 2026-08-20 | open |
| Replace the rotting perimeter fence. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-lucky-clover-site-visit]] | 2026-08-20 | open |
| Install the new bulletin board enclosure. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-lucky-clover-site-visit]] | 2026-08-20 | open |
| Contact Kelly and tell him he is needed at 11:00 AM — 2026-08-21. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-lucky-clover-site-visit]] | 2026-08-20 | open |
| Order the new street signs. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-whispering-pines-mh-and-rv-site-visit]] | 2026-08-20 | open |
| Call the person to make sure they saw the text. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-whispering-pines-mh-and-rv-site-visit]] | 2026-08-20 | open |
| Pre-order burgers and chicken sandwiches to Northgate for 1:30 PM — 2026-08-20. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-whispering-pines-mh-and-rv-site-visit]] | 2026-08-20 | open |
| Assess the current grill and hibachi setup as a fire hazard and decide on removal or relocation. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-great-oaks-site-visit]] | 2026-08-21 | open |
| Check the status of the boil water notice and the aerator pump, and confirm whether the crew is coming back. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-great-oaks-site-visit]] | 2026-08-21 | open |
| Verify whether the storage area is open and secure it. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-great-oaks-site-visit]] | 2026-08-21 | open |
| Review the electrical rerouting and upgrades needed to get power where it is required, with a plan, budget and owner. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-great-oaks-site-visit]] | 2026-08-21 | open |
| Walk and inspect the lift station. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-great-oaks-site-visit]] | 2026-08-21 | open |
| Confirm the delivery schedule for the remaining items. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-great-oaks-site-visit]] | 2026-08-21 | open |
| Evaluate the solar light placement, or replace it. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-great-oaks-site-visit]] | 2026-08-21 | open |
| Meet the resident and call the water company together — 2026-08-24. | unassigned (Speaker 1 on the recording) | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-gulf-breeze-site-visit]] | 2026-08-21 | open |
| Meet regarding the home of the deceased resident — 2026-08-24 at 11:00 AM. | unassigned (Speaker 1) | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-gulf-breeze-site-visit]] | 2026-08-21 | open |
| Show the property to a potential buyer — 2026-08-24. | unassigned (Speaker 1) | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-gulf-breeze-site-visit]] | 2026-08-21 | open |
| Call back the previous applicant for the home on lot two. | unassigned (Speaker 1) | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-gulf-breeze-site-visit]] | 2026-08-21 | open |
| Get a second roof repair quote to compare against the roughly 700 dollar offer. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-gulf-breeze-site-visit]] | 2026-08-21 | open |
| Evaluate buying a zero-turn mower and trailer to replace the landscaper, and price adding lawn care for all residents. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-gulf-breeze-site-visit]] | 2026-08-21 | open |
| Verify permitting on the FEMA homes and decide their disposition. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-gulf-breeze-site-visit]] | 2026-08-21 | open |
| Plan the Palm Spring, Clearwater, Crystal and Hunter visits. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-gulf-breeze-site-visit]] | 2026-08-21 | open |
| Travel to Okeechobee to pay the permit fees and collect the permits within 72 hours of issuance. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-vantage-oaks-site-visit]] | 2026-08-21 | open |
| Review the written estimate for paving, curbs and driveways when it arrives. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-vantage-oaks-site-visit]] | 2026-08-21 | open |
| Notify Amanda to schedule the walkway installations once the COs are in hand. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-vantage-oaks-site-visit]] | 2026-08-21 | open |
| Draft and send the letter to the Nantucket HOA on the approval dispute, and respond on the settlement statement after conferring with John. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-vantage-oaks-site-visit]] | 2026-08-21 | open |
| Contact end-lot residents to negotiate flyer flag placement, offering a 100 dollar Amazon gift card. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-vantage-oaks-site-visit]] | 2026-08-21 | open |
| Deploy the fifty for-sale signs and twenty flags as soon as they arrive. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-vantage-oaks-site-visit]] | 2026-08-21 | open |
| Implement the bulk siding purchase program with purchase credits. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-vantage-oaks-site-visit]] | 2026-08-21 | open |
| Visit the resident lot to look at the water meter and the pipe leak — Monday 2026-08-24. | unassigned (Speaker 2 on the recording) | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-belle-haven-site-visit]] | 2026-08-22 | open |
| Run the flyer flag campaign throughout the property. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-belle-haven-site-visit]] | 2026-08-22 | open |
| Buy, skirt and list one RV to test market demand. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-belle-haven-site-visit]] | 2026-08-22 | open |
| Launch the block and blast Facebook campaign for RV occupancy. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-belle-haven-site-visit]] | 2026-08-22 | open |
| Repair the roof on the occupied unit currently being patched, budget 5,000 to 7,000 dollars. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-belle-haven-site-visit]] | 2026-08-22 | open |
| Install the pickleball court, dog park and covered grill area. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-belle-haven-site-visit]] | 2026-08-22 | open |
| Collect the materials from the site and return them to the office and storage. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-belle-haven-site-visit]] | 2026-08-22 | open |
| Call Zach for his read on the performance question — the same day, 2026-08-22. | unassigned (Speaker 1 on the recording) | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-leslie-call-re-auzzi]] | 2026-08-22 | open |
| Draft and formalize the written performance-based bonus policy, with metrics and payout conditions. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-leslie-call-re-auzzi]] | 2026-08-22 | open |
| Sit with Leslie to learn the NAV system and workflows. | unassigned (Speaker 3) | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-leslie-call-re-auzzi]] | 2026-08-22 | open |
| Get him to sign the official job description. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-leslie-call-re-auzzi]] | 2026-08-22 | open |
| Brief both crews together on the stair and door configuration standard before the next sets. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-paradise-palms-visit]] | 2026-08-22 | open |
| Walk the whole park and log the exceptions (misoriented stairs, exposed wood, missing caps, hardscape misalignment) with lot numbers and photos. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-paradise-palms-visit]] | 2026-08-22 | open |
| Decide whether the non-compliant stairs get rebuilt or the doors get rehung. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-paradise-palms-visit]] | 2026-08-22 | open |
| Verify the drain field boundaries and install a temporary barrier, then coordinate the permanent solution. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-paradise-palms-visit]] | 2026-08-22 | open |
| Inspect the areas with root damage from the electrical trenching and propose corrective landscaping or root protection. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-paradise-palms-visit]] | 2026-08-22 | open |
| Audit and fix the entry codes for the houses and clubhouse. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-paradise-palms-visit]] | 2026-08-22 | open |
| Paint the office front door. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-paradise-palms-visit]] | 2026-08-22 | open |
| Replace the missing post cap (referenced as 1923). | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-paradise-palms-visit]] | 2026-08-22 | open |
| Block the three uninterrupted hours for the SOPs and start with the folder review at the start of the week. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-post-river-oaks-discussion]] | 2026-08-22 | open |
| Meet Zach to review the asset management tasks. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-post-river-oaks-discussion]] | 2026-08-22 | open |
| Speak to Mo about the accounting responsibilities and possible reassignment. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-post-river-oaks-discussion]] | 2026-08-22 | open |
| Brief Vicky and start the referral programme with other communities. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-post-river-oaks-discussion]] | 2026-08-22 | open |
| Create and distribute River Oaks flyers to the RV parks and local gathering places. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-post-river-oaks-discussion]] | 2026-08-22 | open |
| Price billboard options in Ruskin, starting with the blank board on Bayshore Road at Route 41. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-post-river-oaks-discussion]] | 2026-08-22 | open |
| Review the clubhouse inspection report and assess the restroom, leaks, structural lean, windows and walls. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-river-oaks-site-visit]] | 2026-08-22 | open |
| Restore power to the pier and confirm the status of the work George started. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-river-oaks-site-visit]] | 2026-08-22 | open |
| Buy the used bingo machine. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-river-oaks-site-visit]] | 2026-08-22 | open |
| Evaluate and install a proper fish-cleaning station. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-river-oaks-site-visit]] | 2026-08-22 | open |
| Buy a microwave and plan the new clubhouse windows and wall repairs. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-river-oaks-site-visit]] | 2026-08-22 | open |
| Create and distribute the resident survey on activities and amenities. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-river-oaks-site-visit]] | 2026-08-22 | open |
| Price the new well and the horseshoes relocation against the six to eight lots reclaimed. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-river-oaks-site-visit]] | 2026-08-22 | open |
| Build the process to list and sell homes through Rent Manager, since they are not on the platform. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-river-oaks-site-visit]] | 2026-08-22 | open |
| Define the terms of a 15 percent discount for current RV residents, if it goes ahead. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-river-oaks-site-visit]] | 2026-08-22 | open |
| Install the quoted aerator. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-river-oaks-site-visit]] | 2026-08-22 | open |
| Decide whether to pause new home deliveries until current inventory sells. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-river-oaks-site-visit]] | 2026-08-22 | open |
| Confirm which lots can host RVs and where the RVs currently sit, then draft the relocation plan. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-riverwalk-site-visit]] | 2026-08-22 | open |
| Audit and remediate the door, stair and tread install defects as a punch list. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-riverwalk-site-visit]] | 2026-08-22 | open |
| Verify lock boxes on all homes and install them on the two new ones. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-riverwalk-site-visit]] | 2026-08-22 | open |
| Confirm the status of the window that was supposed to be removed. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-riverwalk-site-visit]] | 2026-08-22 | open |
| Schedule the clear-out of old items and set the end-of-shift cleanup expectation for crews. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-riverwalk-site-visit]] | 2026-08-22 | open |
| Pursue the Hillsborough County home replacement program for this community: eligibility, contact and application steps. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-riverwalk-site-visit]] | 2026-08-22 | open |
| Confirm John received and reviewed the lot issues list. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-riverwalk-site-visit]] | 2026-08-22 | open |
| Define the fence specification, select a vendor, get approvals and schedule the wastewater plant fence before listings. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-the-oaks-site-visit]] | 2026-08-22 | open |
| Confirm the trash plan (cans versus dumpster at Terrace Crossings), the rollout dates and the resident communication, aligned to the rent increase timing. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-the-oaks-site-visit]] | 2026-08-22 | open |
| Review the 15,000 dollar trash cost and how it sits in the rent structure. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-the-oaks-site-visit]] | 2026-08-22 | open |
| Compile and price the basic tool package and procure it. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-the-oaks-site-visit]] | 2026-08-22 | open |
| Finalize the shed design, budget, vendor and timeline. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-the-oaks-site-visit]] | 2026-08-22 | open |
| Run the cost-benefit on the gator against the procurement policy. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-the-oaks-site-visit]] | 2026-08-22 | open |
| Scope and budget re-striping the basketball court and adding double hoops. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-the-oaks-site-visit]] | 2026-08-22 | open |
| Develop the pavilion proposal: site, design, permitting and budget. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-the-oaks-site-visit]] | 2026-08-22 | open |
| Start the rehab on the three homes. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-the-oaks-site-visit]] | 2026-08-22 | open |
| Set pricing for the new homes and keep the online-scheduled showings running. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-the-oaks-site-visit]] | 2026-08-22 | open |
| Connect the on-site team with the in-house financing specialist and define the support workflow. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-the-oaks-site-visit]] | 2026-08-22 | open |
| Follow up on the I-4 corridor expansion meeting advertised on the community sign out front — 2026-08-27. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-windward-knoll-note]] | 2026-08-22 | open |
| Schedule the broader call with internal teams and the Rent Viewer team on the data warehouse integration. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]] | 2026-08-24 | open |
| Notify Justin about the incorrect Brunswick Estates address (started during the call). | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-sam-brainstorming-session]] | 2026-08-24 | open |
| Circulate the latest reporting dashboard for everyone to sign up. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-sam-brainstorming-session]] | 2026-08-24 | open |
| Send Zach the latest dashboard file and the CRM workflow documentation to prepare for the call — before 2026-08-26. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-sam-brainstorming-session]] | 2026-08-24 | open |
| Draft the listing audit and creator tool for Tanya. **ADVANCED 2026-08-31: the audit half is built and has been running 60 days**, flags down from 50 at rollout to a few a day. The **generator half is not built** and is gated on the current listing data cleanup finishing. Built by John, not by Tanya, so the owner question on this row has moved rather than been answered. | unassigned — *the work has an author; the row needs to say whether Tanya still owns anything* | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-sam-brainstorming-session]] · [[70-Operations/meetings/2026-08-31-listings-pipeline-and-ai-cost-consultation]] | 2026-08-24, advanced 2026-08-31 | open |
| Put out the job ads for the roles that need filling, allowing for the lead time to have people seated in about four weeks. | unassigned | [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-sam-brainstorming-session]] | 2026-08-24 | open |

## SOP blockers — open [TBD] items that stop a process being approved

Owners are the process owners named in each SOP's own header. Where the document names none, the line reads unassigned.

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Resolve the three open TBDs on SOP 201 — the JotForm Home Drop Confirm link, the SharePoint infill folder link, and the Bill of Lading retention period. The SOP states it cannot be marked Approved until all three are resolved. | Construction (process owner per the SOP header; no individual named) | [[70-Operations/sops/201-new-home-delivery-and-set]] | 2026-08-30 | open |
| Confirm the manufacturer warranty reporting window on SOP 203 — the number of days from delivery within which defects must be reported to preserve coverage. Until it is set, nobody can tell whether a claim is late. | Director of Construction (process owner per the SOP header) | [[70-Operations/sops/203-new-home-readiness]] | 2026-08-30 | open |
| Define the escalation path on SOP 203 for a non-responsive vendor or manufacturer. The FAQ says it is [TBD]. | Director of Construction (process owner per the SOP header) | [[70-Operations/sops/203-new-home-readiness]] | 2026-08-30 | open |
| Confirm the consequence of missing a lender deadline, and the payment timing after the decision, on SOP 302. The SOP says "David and Austin to confirm". | David Berman with Austin Berk | [[70-Operations/sops/302-home-lender-repo]] | 2026-08-30 | open |
| Build the Repo Tracker named in SOP 302. It does not exist; the interim tracker is an email thread to a distribution list. | David Berman | [[70-Operations/sops/302-home-lender-repo]] | 2026-08-30 | open |
| Build the Data Pack Template and supply the Prospect Report link, both [TBD] in SOP 302. | David Berman with Leslie Croft (Leslie compiles the pack) | [[70-Operations/sops/302-home-lender-repo]] | 2026-08-30 | open |
| Supply the HR email address that SOP 108 requires for same-day written notification of every personnel incident. It reads [TBD]. | Operations and HR (shared owner per the SOP header) | [[70-Operations/sops/108-incident-reporting]] | 2026-08-30 | open |
| Name the downstream insurance / property damage claim process that SOP 108 triggers. It reads [TBD], so the insurance feed the process exists to serve has no destination. | Operations and HR (shared owner per the SOP header) | [[70-Operations/sops/108-incident-reporting]] | 2026-08-30 | open |
| Define the formal one-week extension documentation process on SOP 105. The document says "[TBD — Operations to define]". | Natalie Magurne | [[70-Operations/sops/105-poh-rehab]] | 2026-08-30 | open |
| Replace the placeholder GL codes in SOP 105b — every code reads [GL-XXXX] — and supply the three form links marked [Link TBD]. | Natalie Magurne with David Berman (GL codes) | [[70-Operations/sops/105-poh-rehab]] | 2026-08-30 | open |
| Fill in the empty "PENDING DECISIONS" heading on SOP 001, and settle whether the delivery confirmation form lives in FastField or JotForm. | Director of Sales & Marketing (process owner per the SOP header) | [[70-Operations/sops/001-home-ordering-delivery-and-set]] | 2026-08-30 | open |
| Name the Process Owner on SOP 104's data-entry draft. It reads [TBD]. | Natalie Magurne (owner of the companion Ops SOP) | [[70-Operations/sops/104-tbd-unit-review-and-allocate]] | 2026-08-30 | open |
| Create the Weekly PPE Inspection Checklist that SOP 122 depends on. The SOP says it is "to be created". | Regional Manager (process owner per the SOP header; no individual named) | [[70-Operations/sops/122-safety-and-ppe]] | 2026-08-30 | open |
| Build the Closing Walkthrough Checklist that gates key handover in SOPs 003 and 004. It reads "[TBD — in development]". | Director of Sales and Director of Operations (joint owners per the SOP header) | [[70-Operations/sops/003-closing-prep-and-documentation]] | 2026-08-30 | open |
| Name an owner for SOP 704. The document names none, and carries no SOP ID, version, effective date or status field. | unassigned | [[70-Operations/sops/704-disciplinary-action-forms]] | 2026-08-30 | open |
| Name an owner for SOP 123. Neither an owner nor a trigger nor a procedure is stated anywhere in the file. | unassigned | [[70-Operations/sops/123-maintenance-tools-standard]] | 2026-08-30 | open |

## SOP conflicts open for a decision

The full risk-ranked list is on [[00-Meta/open-items]]. These are the ones that need a person to do something. Owners are the process owners named in the SOPs themselves; the SOP initiative as a whole is Natalie Magurne's, per the March deck ("NATALIE OWNS THE SOP INITIATIVE").

| Item | Owner | Source | Raised | Status |
|---|---|---|---|---|
| Remove the lender's account name, account number, beneficiary bank and ABA routing number from SOP 302 and take payment instructions from each notice instead. | David Berman with Natalie Magurne | [[70-Operations/sops/302-home-lender-repo]] | 2026-08-30 | open |
| Settle Florida's cure period to one number with counsel. Four live SOPs give four different values, all citing FS 723.061. This blocks approval of SOP 100, SOP 107 and the whole Florida block. | Natalie Magurne with outside counsel | [[70-Operations/sops/107-eviction]] | 2026-08-30 | open |
| Commission Massachusetts and North Carolina compliance SOPs. Both are live operating states with statutory detail already carried in SOPs 100 and 101 and no counsel-reviewed process behind it. | Natalie Magurne with outside counsel | [[70-Operations/sops/100-ar-and-collections]] | 2026-08-30 | open |
| Commission a Chapter 513 / RV compliance process. None exists anywhere, and three RV properties have no documented path for rent increases, notices, violations, evictions or deposits. | Natalie Magurne with outside counsel | [[70-Operations/sops/800-fl-compliance]] | 2026-08-30 | open |
| Decide the eviction SOP number: 107 or 800. Both files are live, neither is authoritative, and they disagree on cure periods and on who may unlock a locked account. Asked on 2026-08-30 and deferred. | Austin Berk | [[70-Operations/sops/107-eviction]] | 2026-08-30 | open (deferred) |
| Decide which closing generation is authoritative, and whether the Title Coordinator role exists. Two generations of the closing process are both live and the newer one adds a role and a Make Ready Board gate the older one lacks. | Director of Sales and Director of Operations (joint owners per the SOP header) | [[70-Operations/sops/003-closing-prep-and-documentation]] | 2026-08-30 | open |
| Reconcile South Carolina's rent increase notice — 90 days in SOP 101, 30 days with a 60-day company standard in SOP 821, both citing SC Code 27-47-420 — and Georgia's 60-day notice, cited to two different code sections. | Natalie Magurne with outside counsel | [[70-Operations/sops/800-sc-compliance]] | 2026-08-30 | open |
| Add the prospectus delivery step to SOP 103 and the deposit step to SOP 102. SOP 804 makes prospectus delivery with a signed receipt the gate on every Florida lot tenancy; the move-in SOP has no such step, and the move-out SOP has no deposit clock. | Natalie Magurne | [[70-Operations/sops/103-move-in]] | 2026-08-30 | open |
| Bring the master tracker current on the seven processes it has wrong and add rows for 122, 123, 202, 203 and 704, which are not on it at all. | Natalie Magurne | [[70-Operations/sops/sop-library]] | 2026-08-30 | open |
| Publish the ten documented processes that exist only in the drafting room and are invisible to anyone reading the wiki index. | Natalie Magurne | [[70-Operations/sops/sop-library]] | 2026-08-30 | open |
| Settle the form platform question across the library — FastField or JotForm for the same forms — and produce the form ecosystem document the tracker calls for. | Natalie Magurne | [[70-Operations/sops/sop-library]] | 2026-08-30 | open |
| Settle the title function's name and whether it is a role or a department. It is called six different things across six documents. | Natalie Magurne with Leslie Croft | [[70-Operations/sops/005-poh-title-transfer]] | 2026-08-30 | open |
| Retire the competing CONST-nnn and SOP-LOTS-nnn identifiers in the 200s in favour of the nine-band numeric scheme. | Director of Construction (process owner on the affected SOPs) | [[70-Operations/sops/202-site-condition-assessment]] | 2026-08-30 | open |
| Correct the status fields that read "Approved" on documents the tracker and the wiki both mark as drafts, and record an approver and approval date on SOP 200, the one genuinely approved process. | Natalie Magurne | [[70-Operations/sops/sop-library]] | 2026-08-30 | open |
| Create the `_Archive` subfolders the library's own standards document requires, and move the superseded drafts sitting beside current versions into them. | Natalie Magurne | [[70-Operations/sops/sop-library]] | 2026-08-30 | open |
| Start recording the training videos. All 27 `_Video Links.txt` files are empty templates against a schedule that had every populated process covered by the week of 2026-09-28. | Natalie Magurne | [[70-Operations/sops/sop-library]] | 2026-08-30 | open |
| Add effective, revision and version fields to the Employee Handbook, and add Georgia and South Carolina to its state addendum. | Demetria Loukas | [[10-Business/hr/Parakeet Communities Employee Handbook.pdf]] | 2026-08-30 | open |
| Reconcile the scorecard KPI names to the numeric year-end targets, and give each metric a definition and a reporting frequency. This is Zach Schwartz's own Q1 rock. | Zach Schwartz | [[10-Business/eos/scorecard]] | 2026-08-30 | open |

## Decisions

- 2026-08-30 — No owner and no deadline is inferred on this register. Lines with neither read "unassigned". (Source: Austin, in the Structure Interview, 2026-08-30.)

## Sources

- The 27 filed transcripts in `70-Operations/meetings/2026-08-southeast-tour/` — every action line, quoted as filed.
- [[70-Operations/sops/sop-library]] — the open conflicts and the [TBD] markers, each stated in full on its own process page.

## From the 2026-08-31 email, Teams and transcript harvest

**What changed.** 368 property-level items were harvested from 90 days of Outlook, 90 days of Teams and the 27 filed tour transcripts, and filed against the communities and lots they belong to. 331 are still open. The full register, oldest first, is [[60-Communities/open-items]]; every line below links to the lot or community page that carries the detail. Owners are recorded as the source names them.

### The items with a clock on them

| Item | Owner | Where | Raised | Status |
|---|---|---|---|---|
| Brevard County zoning refuses to allow a home onto Lot 46. Gunster file opened to argue rebuildability sits at the park and lot level. Ormond Beach Oasis, Westwood and Lake Wales are flagged for the same argument and the documentation has not been assembled. | Jon, with John and Leslie | [[60-Communities/tradewinds-mhc]] | 2026-08-29 | blocked |
| Miami-Dade notice that Pulles Plumbing has a permit expiring within 30 days that could stop scheduled work. John Clark says he never contracted them, so nobody has established who did. | John, with Natalie | [[60-Communities/shady-oaks-mhp]] | 2026-08-31 | open |
| Capital One deferred maintenance notice on asphalt cracking and potholes at 40 percent pervasiveness. The stated due date of 2026-08-26 has passed and the thread has no answer in it. | Natalie, needs Austin | [[60-Communities/mayflower-hills]] | 2026-07-23 | open |
| Trimont sent the 2026 inspection report citing deferred maintenance and asked for a status update. No reply in the thread, 41 days. | Jon | [[60-Communities/hendersons]] | 2026-07-21 | open |
| Active EPD violation over a broken cement pond wall causing seepage, reportedly damaged by the previous owner. No plan, timeline or owner. | unassigned | [[60-Communities/druid-oaks-mhc]] | 2026-08-19 | open |
| All excavation stopped until roughly 30,000 dollars of utility locating and mapping is complete. No owner, no budget approval, no start date. | John | [[60-Communities/paradise-lakes]] | 2026-08-19 | blocked |
| Temporary warning barriers at the roadside pole and the broken gate exit were agreed and never installed. Residents exit there at night into unseen obstacles. | Natalie | [[60-Communities/paradise-lakes]] | 2026-08-19 | decided-not-actioned |
| Sinkholes forming near a speed bump and mid-road, no owner assigned to inspect or repair. | John | [[60-Communities/regency-i-and-ii]] | 2026-08-19 | open |
| A home has no wood under it and is about to fall over. Nobody was assigned. | John | [[60-Communities/applegate-mhc]] | 2026-08-19 | open |
| A storm drain compromised by the road project is covered with two-by-fours and metal sheathing and was called an immediate hazard. No owner. | John | [[60-Communities/open-items]] | 2026-08-18 | open |

### Rehab scopes waiting on an approval

High Pace assessed and priced these and asked for direction. The oldest have been sitting 56 days. Nothing moves until someone says yes.

| Item | Owner | Where | Raised | Status |
|---|---|---|---|---|
| 14 lots assessed and awaiting approval to schedule. Lots 42 and 60 are blocked on a separate question: a prior contractor left work incomplete and High Pace asked what to do before scoping. | Natalie | [[60-Communities/parkwood-mobile-home-park]] | 2026-07-22 | blocked |
| 10 lots assessed from Level 1 to full gut. Lot 32 has rotted floors, no kitchen and no bathroom and needs leveling. | Natalie | [[60-Communities/lake-wales-mhc]] | 2026-07-16 | open |
| 9 lots assessed, awaiting approval to schedule. | Natalie | [[60-Communities/auburn-ridge]] | 2026-07-27 | open |
| 6 lots assessed, one of them a Level 3 near-full gut. | Natalie | [[60-Communities/fox-creek]] | 2026-07-22 | open |
| 6 lots assessed including a Level 3 at Lot 701. | Natalie | [[60-Communities/brunswick-estates]] | 2026-07-07 | open |
| Estimate 1037 submitted with an open question on roughly 10 sets of missing prefab stairs. | Jon | [[60-Communities/hunter-springs-mhp]] | 2026-08-25 | open |
| High Pace asked whether to add AC to Lots 31 and 74, now complete. Belle Haven homes have historically been window units, so this is a standard, not a one-off. | Natalie | [[60-Communities/belle-haven]] | 2026-08-04 | open |
| High Pace priced an elevated stilted set at 70k to 100k per single wide against roughly 50k for a full gut and asked which direction to take. 52 days, no answer. | John | [[60-Communities/gulf-breeze-mhc]] | 2026-07-10 | open |

### The Rent Manager versus Cavco conflicts

These are one problem, not eight. Two systems disagree about which homes exist and where they are, and money has been invoiced against the disagreement.

| Item | Owner | Where | Raised | Status |
|---|---|---|---|---|
| Eleven homes struck through on the Cavco sheet with no live order and shared order numbers, but invoices logged against all eleven. What is actually owned has not been confirmed. | Leslie | [[60-Communities/lucky-clover]] | 2026-08-27 | blocked |
| Six homes show delivered in Rent Manager with jotforms dated 8/18 while Cavco has them queued to ship. Needs field confirmation. | John | [[60-Communities/vantage-oaks]] | 2026-08-29 | blocked |
| Order 2026-1162411-00 moved off 46 Olsen Road to Central B02 between two daily Cavco sheets, leaving the lot holding a July 8 offline date for a home it does not have. | Leslie | [[60-Communities/assets/ORDER-2026-1162411-00]] | 2026-08-27 | open |
| TO-72 shipped 7/1 but showed sitting in storage since 6/10 because the Cavco row was deleted. No delivery jotform, not marked delivered. | John | [[60-Communities/assets/TO-72]] | 2026-08-29 | blocked |
| RO-2712 and RO-2726 both show delivered on one side and queued to ship on the other. | John | [[60-Communities/river-oaks-rv-resort]] | 2026-08-29 | open |
| Four Northgate RV homes appear nowhere in the Cavco workbook at all. | John | [[60-Communities/northgate-mh]] | 2026-08-27 | open |
| NGRV-99 has a blank Home Delivery Date in Rent Manager despite a Delivered status. | Justin | [[60-Communities/northgate-mh]] | 2026-06-23 | open |

### Questions Austin asked that never came back

| Item | Owner | Where | Raised | Status |
|---|---|---|---|---|
| Who is the landscaper at Fox Creek now. Natalie answered that they fired one and hired the Parkwood landscaper; the vendor was never named. | Natalie | [[60-Communities/fox-creek]] | 2026-08-18 | open |
| Where do we stand on the titles for Applegate. No answer in the thread, 90 days. | Melanie | [[60-Communities/applegate-mhc]] | 2026-06-02 | open |
| Was the water issue at Riverwalk fixed. No reply captured, 89 days. | Natalie | [[60-Communities/riverwalk]] | 2026-06-03 | open |
| Complete Oakside and Fox Creek vendor paper trail in one organized folder. | John | [[60-Communities/oakside-mhp]] | 2026-08-18 | open |

### Routed from the 2026-08-31 morning brief

**Why this section exists:** rule in [[CLAUDE]] — a finding is not delivered until it has a row with a name on it. These three came out of the 2026-08-31 sweep (`99-Archive/2026-08-briefs/brief-2026-08-31.html`). Where the source names nobody the row reads **unassigned** and names the forum, per the register's own rule above.

| Item | Owner | Where | Raised | Status |
|---|---|---|---|---|
| Name an owner for the Lucky Clover trespass / law-enforcement / eviction path. Day 11 unassigned. Angel is the manager of record and alone on site. **Forum: the 08:30 Monday catch-up with Jon** — which is double-booked against a Woods Oviatt call, so the slot itself may need moving first. | **unassigned** — Austin to name at the 08:30 | [[00-Meta/commitments]] item 7 | 2026-08-20 | open |
| Rule on the August payroll allocations before EOD today: run as circulated with the audit after, or hold. Do not let it default by silence. | **Austin** — Berman set the deadline, Jon disputes the model, neither can settle it against the other | [[00-Meta/commitments]] item 21 · [[80-Finance/payroll-model]] | 2026-08-30 | open |
| Settle the Geiger House liability cap and survival position with Jon before counsel's open issues list lands. Buyer at 12 months / 10%, Parakeet at 6 / 2. | **Austin with Jon** | [[00-Meta/commitments]] item 22 | 2026-08-31 | open |
| Decide with Jon whether the $250,000 reserve 21st wants against the $500,000 insurance deductible gets funded from the Home Sales SC capital. Tagged AB/JW by Berman. **Was held from the 2026-08-31 brief under the since-removed three-item ceiling; from 2026-09-01 it shows on the brief's tail.** | **Austin with Jon** | [[00-Meta/commitments]] item 15 | 2026-08-31 | open |
| Give the serial-by-serial insurance tie-out a different owner or a date. Assigned to Berman, Bennett and Moe on 2026-08-27; answered around twice without being accepted. | **Austin** to re-assign | [[00-Meta/commitments]] item 15 | 2026-08-27 | open |

### Routed from Austin's comments on the delegation board, 2026-08-31

**Why this section exists:** Austin left 18 comments on the delegation board between 13:46 and 14:02. Six were rulings and are in [[00-Meta/decisions-log]]; these are the tasks the rest of them created or reassigned. Owners here are **stated by Austin**, not proposed.

| Item | Owner | Where | Raised | Status |
|---|---|---|---|---|
| Audit the payroll allocation model. Allocations run tonight as circulated by Austin's ruling, so this is a parallel audit with a September true-up as the correction path, not a gate on the close. | **Jon** — he asked for the audit | [[00-Meta/commitments]] item 21 · [[80-Finance/payroll-model]] | 2026-08-31 | open |
| Draft the Corner IQ decline. Positioning is fixed by Austin: Parakeet is **not ready for it**, not that there is a problem with the system. Recipients are Zayv and Luke per the parked-decision row. | **Austin** to send, draft owed to him | [[00-Meta/parked-decisions]] 6 | 2026-08-31 | open |
| Shuffleboard roof at Lucky Clover — metal roof or re-anchored shades, plus the lighting walk-through already promised. | **Angel and Jason Davis**, via Natalie | [[00-Meta/parked-decisions]] 15 | 2026-08-31 | open |
| Resident amenity preference survey at River Oaks, ahead of any pickleball spend. Scope is River Oaks only, not portfolio-wide. | **Vikki**, via Natalie | [[00-Meta/parked-decisions]] 12 | 2026-08-31 | open |
| Come back with options on the Gulf Breeze FEMA homes: sell cheap or scrap for parts. Permit and utility verification informs it. | **Rose and Natalie** | [[00-Meta/parked-decisions]] 10 | 2026-08-31 | open |
| Ozzie evaluation — make the call and report it. Moved off Austin because Auzzi sits in Jon's office. | **Jon** | [[00-Meta/parked-decisions]] 1 | 2026-08-31 | open |
| Pull the nine Royal Oaks titles from the 2022 Twin Lakes folder. Intent is to cure the titles by closing rather than negotiate the $67,500. | **Melanie** | [[00-Meta/commitments]] item 19 | 2026-08-31 | open |
| ~~Produce the community-name normalisation list.~~ **DONE 2026-08-31** — built from a live read of both trees, not the survey. **21 renames, not eight**; 5 Operations-only, not six; 30 of 142 folders fail an exact-name join. Standard and list at [[10-Business/sharepoint/community-naming-standard]]. | — | [[10-Business/sharepoint/community-naming-standard]] | 2026-08-31 | **closed** |
| ~~Execute the 21 community-folder renames under `Construction/`.~~ **SUPERSEDED 2026-08-31** — Austin: do not touch Construction, and nothing in the Parakeet Communities SharePoint is edited or renamed without permission. Replaced by the row below. | — | [[CLAUDE]] | 2026-08-31 | **closed** |
| Apply the 21 mapping rows on the **write into Birdcage**, Operations spelling governing. Two need care: the Whispering Pines pair are different properties in different states and must not be merged, and Bay Oaks is a cardinality question a mapping table cannot resolve. Correct the three city misspellings and `__SITE ELVATION CERTIFICATES` in the destination name only; migrate the elevation certificates once, not twice. | **Albert** | [[10-Business/sharepoint/community-naming-standard]] | 2026-08-31 | open |
| **Define the Birdcage metadata columns before any leading underscore comes off.** Minimum: `Community`, `Status` (active/archived/prospect), `Department`, `Record Type`, `Effective Date`, with default views built on them. Rule 6 is blocked on this — `_Archive Communities` is 114.4 GB and an underscore is currently the only thing separating 36 disposed assets from 71 live ones, five of which exist in both. | **Albert**, spec owed to Austin | [[10-Business/sharepoint/community-naming-standard]] | 2026-08-31 | open |
| ~~Rule on whether rule 6 extends to the numbered community subfolder template.~~ **RULED 2026-08-31 — the numbers come off.** Austin's reason is permission trimming: scoped access makes a numbered list show holes. Applied across the Brain the same day. | — | [[10-Business/sharepoint/target-structure]] | 2026-08-31 | **closed** |
| Build the cutover path-change list: every SOP, form, template, Power Query path and Teams tab pointing at a numbered or underscore-prefixed source path, to be repointed **on cutover day, not before**. SOP 301 is the first known entry (`8. Reports_Month End Closeout` becomes `Reports_Month End Closeout`); [[70-Operations/supply-chain-model]] is the second. | **Albert with Natalie** — Natalie owns the SOP library | [[10-Business/sharepoint/target-structure]] | 2026-08-31 | open |
| Rule on the six open decisions in the intake design: the drop location, how the description is captured, who files and on what cadence, the SLA, who may bypass (recommendation: nobody), and the metadata columns. Each has a recommendation attached. The SOP cannot be written until these land. | **Austin** | [[70-Operations/sops/folder-and-file-intake]] | 2026-08-31 | open |
| Write the folder-and-file intake SOP proper, with the swim-lane flowchart and the intake form, once Austin has ruled on the six design decisions. | **unassigned** — *proposed: Austin as submitter via the SOP builder, since the process is his design and nobody performs it yet* | [[70-Operations/sops/folder-and-file-intake]] | 2026-08-31 | open |
| Rule on the nine folders that cannot be settled from a folder tree: the three North Dakota assets (still owned or disposed), Shell Pointe's non-operating status, what and where `Shirley's` is, whether `LAKESIDE ESTATES` is an asset, and whether Bay Oaks I and II are one asset or two. `AVALON MHP` and `CREEK WOOD` are 0 bytes and recommended for deletion; `INLAND VILLAGE - POSSIBLE` for a move to Acquisitions. | **Austin** | [[10-Business/sharepoint/community-naming-standard]] | 2026-08-31 | open |
| Adopt the seven-rule community naming standard as governing, so new folders stop reintroducing the drift. | **Austin** to adopt, **Albert** to apply | [[10-Business/sharepoint/community-naming-standard]] | 2026-08-31 | open |
| Put a date on the serial-by-serial insurance tie-out. Austin declined to reassign it — it stays with accounting — so it needs a deadline instead of a new owner. | **Accounting** (Berman, Bennett, Moe) | [[00-Meta/commitments]] item 15 | 2026-08-31 | open |
| Confirm Albert actually holds the migration risk brief's contents, in particular the `/sites/ParakeetHome` vs `/sites/ParakeetHomes` item. Austin says it was discussed; the written brief has not been sent. | **Austin** | [[00-Meta/commitments]] item 4 | 2026-08-31 | open |
| Schedule the budget review with Rick. | **Austin** | [[00-Meta/commitments]] item 10 | 2026-08-31 | open |
| Report the injured employee's status and confirm workers'-comp documentation is filed. Austin asked directly. | **unassigned** — *proposed: Demetria Loukas, HR owns workers' comp* | [[00-Meta/commitments]] item 10 | 2026-08-31 | open |

### Both live Rent Manager feeds are down

| Item | Owner | Where | Raised | Status |
|---|---|---|---|---|
| Every RentViewer data warehouse query timed out at 60 seconds on 2026-08-31, including a single measure grouped by property. The Live block on all 67 community pages is empty because of it. | Zach | [[90-Skills/community-hot-sheet-refresh]] | 2026-08-31 | blocked |
| The Rent Manager report API returned HTTP 500 on FilteredIssueList and UnitAvailability. The Issues, UnitListing and AssetListing CSVs still arrive daily by email but their attachments cannot be read programmatically. | Zach, with Justin | [[60-Communities/_model]] | 2026-08-31 | blocked |

### Routed from the 2026-08-31 Plaud transcript filing

**Why this section exists:** three recordings from 2026-08-31 were filed into `70-Operations/meetings/` the same evening. These are the actions they created. **Owners are stated on the recordings, never inferred** — where nobody took an action it says unassigned and names the forum. Counsel's own actions are on the filed notes and are not repeated here, because outside counsel is not an eos owner.

| Item | Owner | Where | Raised | Status |
|---|---|---|---|---|
| Call **Justin Stelmac** back on the Auburn, MA rent control meeting, and say whether there is a date and which community it concerns. | **Natalie** — her own words: *"I owe Justin Stelmac a call back"* | [[00-Meta/commitments]] item 23 · [[70-Operations/meetings/2026-08-31-settlement-strategy-and-auburn-rent-control]] | 2026-08-31 | open |
| Get Stelmac and **Zach** on a joint call, then settle the Massachusetts trip and the budget-session reschedule. Zach asked to be on the call and at the meeting. | **Natalie** | [[00-Meta/commitments]] item 23 | 2026-08-31 | open |
| ~~Rule on whether the rent increase settlement is the Belle Haven matter or a Massachusetts one.~~ **DONE 2026-08-31** — Austin: *"Settlement was in regards to the Mass case, Bellehaven is completely separate."* Item 20 retitled. | — | [[00-Meta/open-items]] T1 · [[00-Meta/commitments]] item 20 | 2026-08-31 | **closed** |
| ~~Say **which** Massachusetts community the rent increase settlement concerns.~~ **DONE 2026-08-31** — answered from the primary settlement chain rather than by asking. It is **both Auburn, MA communities: American and Whispering Pines MA.** Facts pushed to both community pages. | — | [[00-Meta/commitments]] item 20 | 2026-08-31 | **closed** |
| **Value the rent-schedule gap in dollars.** The whole remaining dispute is a one-time $50 step against $20 a year from 2028-12-01, across owner-tenants and renter-tenants at two communities. **Nobody has put a number on it** — not counsel, not the call, not this Brain. It is arithmetic against a class list, and it is what says whether the binding-appraiser risk is worth taking. | **unassigned** — settle at the next Jon and Austin catch-up | [[00-Meta/commitments]] item 20 · `00-Meta/numbers-ledger.md` | 2026-08-31 | open |
| Decide the path. **2026-08-31: Austin prefers path 1**, share the CBRE report, matching Jon's 2026-08-28 written preference; counsel argued path 2 on the call and **Wallack is coming back with a recommendation**, so it is a stated preference not a closed decision. Two things to hold when it lands: *"already paid for"* does not distinguish the paths, since path 2 also uses the CBRE analysis as Parakeet's submission; and if plaintiffs are right that the *increase* is the test rather than the resulting *rate*, an appraiser's fair-market number does not dispose of the claim. | **Austin** | [[00-Meta/commitments]] item 20 | 2026-08-31 | open |
| Say whether the Massachusetts settlement and the Auburn rent control proceeding are the same matter. **Sharper as of 2026-08-31**: the settlement is over the November 2023 rent increases at American and Whispering Pines MA, **both in Auburn**, and item 23 is a rent control meeting in Auburn about lot rent. **Two forums may be forming a view on fair market rent at the same two parks while the settlement contemplates handing that number to a binding appraiser.** Natalie's call to Stelmac is the cheapest way to find out. | **Austin**, with Natalie's call as the input | [[00-Meta/open-items]] T5 · [[00-Meta/commitments]] items 20 and 23 | 2026-08-31 | open |
| ~~Find out what the *"RV data"* on the 2026-08-31 settlement call was.~~ **DONE 2026-08-31** — Austin: it is house shorthand for the comparable set, MH & RV against single-family and apartments. Not inventory, not a mis-transcription. | — | [[00-Meta/open-items]] T3 | 2026-08-31 | **closed** |
| **Record the comp-set decision for the fair market rent analysis.** MH & RV against single-family and apartments, or MH & RV against other Massachusetts manufactured housing communities. **The case turns on whether $665 is fair market rent and the benchmark decides that number.** It is the instruction CBRE is working to and the instruction any appraiser would get, and it is written down nowhere. | **Austin**, with Wallack | [[00-Meta/commitments]] item 20 | 2026-08-31 | open |
| **Find out what Natalie and Wallack discussed one-to-one after the 2026-08-31 call.** Nothing from it is recorded, the path is undecided, and Wallack is actively forming a recommendation, so it is an input to that recommendation. | **Austin** to follow up, Natalie to report | [[00-Meta/commitments]] item 20 | 2026-08-31 | open |
| **Ask Wallack to consolidate the path conversation into one channel.** Four separate contacts with counsel on an open decision (Jon in writing, the group call, Natalie one-to-one, and Wallack's pending recommendation) and the decision owner authored one of them. | **Austin** | [[00-Meta/commitments]] item 20 | 2026-08-31 | open |
| Establish whether a separate Belle Haven settlement exists and get its facts on the record. If it does, it currently has **zero** detail anywhere, because everything under the old label belonged to Massachusetts. | **Austin** | [[00-Meta/open-items]] T4 | 2026-08-31 | open |
| Rule on whether the Kippy dispute and the Royal Oaks nine-title matter share a counterparty. Two letters are queued to Royal Oaks counterparties with opposite tones. | **Austin** | [[00-Meta/open-items]] T2 · [[00-Meta/commitments]] items 19 and 24 | 2026-08-31 | open |
| Push CBRE for the rent study by end of week, target 2026-09-04. **Counsel said it should happen and nobody on the call took it.** | **unassigned** — settle at the next Jon and Austin catch-up | [[00-Meta/commitments]] item 20 | 2026-08-31 | open |
| If the appraiser route is taken, define the floor and ceiling range for the settlement agreement. No number was discussed beyond rejecting $400 as a floor. | **unassigned** — same forum | [[00-Meta/commitments]] item 20 | 2026-08-31 | open |
| Re-read the original Kippy note and the third amendment and establish whether the home obligation is three homes or six, and whether it is rehab or rent credit. Counsel said the note has to be looked at; nobody took it. | **unassigned** — settle at the next Jon and Austin catch-up | [[60-Communities/hunter-springs-mhp]] · [[70-Operations/meetings/2026-08-31-kippy-dispute-legal-strategy]] | 2026-08-31 | open |
| Get a researched answer on whether a lien can attach for management fees in the relevant jurisdiction. Counsel's view is **explicitly off the cuff** and this is one of only two levers on the Royal Oaks sale. | **unassigned** — a question for counsel, but somebody has to ask it | [[60-Communities/royal-oaks-mhc]] | 2026-08-31 | open |
| Decide whether the internal cash-transfer failure inside the Kippy dispute origin gets tracked as a control issue anywhere. Parakeet's own words on the recording: *"we should have been transferring the money. Again, internal issue that we're working through."* Currently it exists only as a dispute fact. | **unassigned** — *proposed: accounting, but it is a controls question and needs Austin to place it* | [[00-Meta/commitments]] item 24 | 2026-08-31 | open |
| Send the consultant the listings dashboard and the listings audit. | **John** — stated on the recording | [[70-Operations/meetings/2026-08-31-listings-pipeline-and-ai-cost-consultation]] | 2026-08-31 | open |
| Upgrade the Railway account to Pro so the consultant can be invited. Free-tier signup is already done. | **Austin** — stated on the recording | [[00-Meta/parked-decisions]] row 20 | 2026-08-31 | open |
| Answer the consultant's question set when it arrives by email: the full list of listing websites to monitor, and the exact CRM product name. | **Austin** | [[00-Meta/parked-decisions]] row 20 | 2026-08-31 | open |
| Build the second audit leg covering My State MLS, and through it Realtor.com, Zillow and Trulia. **This is the largest known blind spot in listing quality and John said he does not know how to do it** — either the My State MLS login or scraping the end sites. | **unassigned** | [[20-Brand-Marketing/online-presence]] · [[50-Products-Sales/home-sales]] | 2026-08-31 | open |
| Find out what the website's third party actually does with the field mapping between Rent Manager and the portals. Twice on the recording: *"I don't really know how that works… but it seems to be working."* It is the only link in the listings chain nobody inside the company can describe. | **unassigned** — Austin's line was *"Park web and make sure that they're doing something like that"*, which is an instruction without a name on it | [[10-Business/systems-architecture]] | 2026-08-31 | open |
| Give scheduled-task reliability an owner, logging and alerting. The listings dashboard **misfired on the morning of 2026-08-31** and the point went by unremarked on the call; the previous Chrome-based version *"was always breaking."* | **unassigned** | [[10-Business/systems-architecture]] | 2026-08-31 | open |
| Arrange the consultant's interview with the listing-submission employee. Austin said *"anybody will be at your disposal"*, which is permission, not an owner. Gated on the engagement decision. | **unassigned** | [[00-Meta/parked-decisions]] row 20 | 2026-08-31 | blocked |
| Settle the **Unity versus Uniti** spelling before either name reaches a contract or a report. `10-Business/systems-architecture.md` and `10-Business/vendors/vendor-status-2026-08.md` say Uniti; the 2026-08-31 recording says Unity. Almost certainly one vendor; nothing confirms it. | **unassigned** — one look settles it | [[10-Business/systems-architecture]] | 2026-08-31 | open |
| Decide where the 2026-08-31 personnel recording lives, and whether it stays in this vault at all. It is parked at `05-Inbox/_private-2026-08-31-controller-performance-and-transition.md`. | **Austin** | `05-Inbox/_needs-sorting.md` | 2026-08-31 | open |
| Trigger transcription on the 2026-08-31 14:01 Plaud recording, 23 min 53 sec, which has no transcript and no notes. Nobody knows what was on it. | **Austin** | `05-Inbox/2026-08-31-plaud-1401-not-transcribed.md` | 2026-08-31 | open |

## Routed from the 2026-08-31 end of day close

**Source:** the 2026-08-31 EOD sweep of the Outlook Inbox, Sent Items and For Signature, Teams, the calendar and Plaud, all read only, all Eastern, diffed against `99-Archive/` and the day's own `00-Meta/log.md` entries before anything below was written. Seven rows. **Every one is new to this register**; nothing here restates a row routed earlier today from the morning brief or the transcript filing.

| Item | Owner | Where | Raised | Status |
| --- | --- | --- | --- | --- |
| **Produce the floor line capacity number across CountryPlace, 21st and Triad, once, sourced and dated.** Both founders made the $250,000 21st Mortgage escrow conditional on it within four minutes of each other on 2026-08-31 evening. Austin: *"would like understand where our capacity is on all three lines before making that decision. where do we stand on the analysis?"* **This is now a gate on a capital decision, not an accounting chore.** | **unassigned** — the assignment has been proposed and unaccepted since 2026-08-27; it now needs a name and a date rather than a third proposal | [[00-Meta/commitments]] item 15 · [[60-Communities/asset-inventory]] | 2026-08-31 | open |
| **Complete the nine Royal Oaks title transfers under option 1 while the Titan Mobile Homes reinstatement is live.** Brokaw reinstated the dissolved LLC himself on 2026-08-31 at 16:46 ET and sent the receipt. The reinstatement is the window; the transfers are the work. | **Melanie Sanchez** — Austin, 16:48 ET: *"Here we go. Let's get this done please."* | [[00-Meta/commitments]] item 19 | 2026-08-31 | open |
| **Revise the Delivery JotForm to require both SERIAL and VIN with photos for each.** Leslie asked Austin directly at 12:09 ET. **Blocked, not just open:** John Clark asked at 13:13 ET whether the serial is the VIN, and if not, where his crews find the VIN on the home. The form cannot be changed until that is answered, and the answer decides whether this is a form change or a field-training change. | **Austin** to revise; **John Clark** owes the serial-versus-VIN answer first | [[60-Communities/asset-inventory]] · the "Rent Manager vs Cavco - 141 data conflicts" thread | 2026-08-31 | blocked |
| **Name who fills out the KeyBank Capital Expenditure Reserve Draw Request forms for the Walton escrow.** Berman opened the request at 16:56 ET, KeyBank returned the forms with the invoice, lien waiver and proof-of-payment requirements at 17:54 ET. Austin to Zach and Jon at 17:13: *"Dont you guys do this?"* **A question is not an assignment and neither of them has answered it.** | **unassigned** — Austin's own question, addressed to two people, unanswered | [[30-Customers/capital-partners]] · the "Walton Escrow Reimbursement Request" thread | 2026-08-31 | open |
| **Answer Tim McNamara's A2Z ND Portfolio Partners contributions question and send Lisa Timbrook the Business Extensions.** Neither went again today. Austin sent four things to Citrin Cooperman on 2026-08-31 — a returns-timing chase, the Plattsburgh K-1, and two draft sign-off replies — and **none of them is either of these.** The answer to Tim already exists verbatim in Austin's own 2026-08-27 21:35 ET message; it needs sending, not drafting. | **Austin** | [[00-Meta/commitments]] item 18 | 2026-08-31 | open — **slipped a third time**, and the ledger's own rule says a loop that slips twice gets escalated rather than re-scheduled |
| **Settle whether the LOP annual increase needs legal to redraft the agreement.** Leslie, 17:00 ET: the LOP does not spell out the annual increases, and the asset UDFs Austin built track a fixed amount. Resolved between them in the same conversation on the reading that the existing clause plus written revisions covers it, **but that reading is Leslie's and it has not been put to counsel.** | **Austin** — his question was *"does legal need to redraft"* and he accepted the answer without asking anyone outside the room | [[50-Products-Sales]] · Teams, 2026-08-31 17:00 to 17:07 ET | 2026-08-31 | open |
| **Enforce the field-laptop purchasing rule and recover anything already bought.** Austin, 11:40 ET, to Demetria and Natalie: *"These all need to be purchased through IT and sent out... Please make sure if anything has been purchased that they are returned immediately as we will not be covering that cost."* **The instruction went out; nobody has reported back whether anything was in fact purchased.** | **Demetria Loukas** with **Natalie Magurne** | the "** LAPTOPS FOR FIELD STAFF **" thread | 2026-08-31 | open |

**Two things deliberately not routed here.** The Geiger House open-issues exchange with Paul Hastings moved again at 17:27 ET on condemnation and related terms, and it is **Jon's 100% by Austin's own correction of 2026-08-31** — it stays FYI and gets no row. And the Triad past-due insurance premium opened and closed inside twenty-eight minutes this afternoon, Austin to finance at 15:36 and Moe returning payment receipts at 16:03; recorded in the close file so it does not resurface as a false open, not carried as a task.

## Routed from the 2026-08-31 end of day close, refresh pass

**Source:** two Plaud recordings that were not available when the close ran at 18:10 ET. The 16:02 LP call had not been uploaded; the 14:01 call had been uploaded but not transcribed and was filed as a placeholder. Both were pulled and read in full at 19:30 ET. Six rows, all new to this register. **The Ramp / Rillet demo rows and the fund rows do not overlap with anything routed earlier today.**

| Item | Owner | Where | Raised | Status |
| --- | --- | --- | --- | --- |
| **Request the Fed reference ID and Bank of America confirmation on the July 2021 $7,000 distribution and send it to the LP.** Sent to the LP's former Kadara account instead of WCO Capital. Nothing bounced, the old account entry was deleted right afterwards, and it has never been traced. Austin put it on his own list on the call. | **Austin** | [[00-Meta/commitments]] item 25 · [[70-Operations/meetings/2026-08-31-bedrock-fund-ii-lp-call]] | 2026-08-31 | open |
| **Put a date on the CPA-prepared, CPA-signed fund-level waterfall, and decide whether one LP gets it or all of them do.** Austin agreed to it unconditionally on the call. The filed plan promises a final waterfall in **Q3 2026**, which ends in thirty days, and never promised an outside representation. | **Austin** | [[00-Meta/commitments]] item 25 · [[80-Finance/fund-reporting/bedrock-fund-ii-winddown]] | 2026-08-31 | open |
| **Reconcile the $52,000 statement balance against the "all LPs made whole, zero remaining balance as of 2026-07-31" position in the Q2 2026 letter.** One look at the statement dates settles whether these describe the same account at two moments or a genuine disagreement. **On a base flagged as litigious this is worth an hour, not a shrug.** | **Austin** — nobody else can pull the LP-level statements | [[30-Customers/capital-partners/bedrock-fund-ii-lps]] | 2026-08-31 | open |
| **Name the internal controller candidate and get them into the Friday 2026-09-04 15:00 ET vendor demo.** Jon committed to bringing them; nobody said who. **This is a sequencing question as much as a scheduling one** — the exit under commitments item 16 is not complete. | **Austin with Jon** | [[70-Operations/meetings/2026-08-31-accounting-platform-intro-rillet]] · [[00-Meta/commitments]] item 16 | 2026-08-31 | open |
| **Settle the vendor's actual name, and read the prior work on it that this vault has never seen.** The transcript spells it Realest, Relit, Rulit and Relet; the **Parakeet Brain vault carries an active project page called "Realit Live Close Evaluation"**, a fifth spelling. **The name is the small half of this row.** The large half is that a live evaluation of this vendor already exists outside this vault, so the 2026-09-04 demo is not a first look and nobody here knows what the prior look concluded. | **unassigned** — the name is one look; the prior page is a read | [[10-Business/tools-and-systems]] · [[70-Operations/meetings/2026-08-31-accounting-platform-intro-rillet]] | 2026-08-31 | open |
| **Get an answer on whether Ramp can be made to post more often than monthly, before the demo.** Ramp moving to **once-a-month journal entries** is the named cause of no intra-month expense visibility, and it is a **vendor behaviour change rather than an internal process failure**. If Ramp will change it, half the problem being demoed on Friday goes away without buying anything. | **unassigned** | [[10-Business/tools-and-systems]] · [[00-Meta/open-items]] "accounting runs 30 to 45 days in arrears" | 2026-08-31 | open |

**Deliberately not routed.** Austin's aside that the company might look at QuickBooks *"overall"* rather than staying inside Rent Manager. Jon did not respond to it and the vendor moved on. **It is the largest question that call opened and it is not a task** — it is a decision nobody has taken, and it would be dishonest to route it as though someone had.

## Routed from Austin's 2026-08-31 answers

**Source:** Austin answered the close's questions the same evening. One answer was itself a question — "what credentials for A2Z" — which nobody in this vault could answer, so the file was read. Five rows.

| Item | Owner | Where | Raised | Status |
| --- | --- | --- | --- | --- |
| **Find out where the three reused password roots from the A2Z file are used outside it, starting with the four shared service mailboxes.** Three roots and their punctuation variants cover **21 of 38 rows**. **This is the actual exposure and it is the only step on this item that addresses it** — the utility portals are the symptom. | **Austin** to direct, IT to execute | [[10-Business/sharepoint/a2z-utility-logins-exposure]] · [[00-Meta/commitments]] item 2 | 2026-08-31 | open |
| **Treat the Triple S Marina Spectrum row as its own incident.** It carries the account number, the account security code **and** the answer to the account security question alongside the password. That combination defeats a phone identity check at the carrier, so it needs Spectrum called, not a portal reset. | **unassigned** | [[10-Business/sharepoint/a2z-utility-logins-exposure]] | 2026-08-31 | open |
| **Find out whether anyone still administers the `a2zcp.com` tenant, and whether Winnie Bretz's account was ever disabled.** **Rewritten 2026-08-31 after Austin corrected the premise** — a2zcp.com is his own legacy holding company, so control was never the question. **`winnie@a2zcp.com` is a departed employee and is still the login of record on two live utility portals.** Eleven rows run through this legacy tenant, covering Origins and Kippy assets as well as legacy ones: **the entities changed and the logins never followed.** | **Austin** — it is his entity and nobody else can answer whether it still has an admin | [[10-Business/sharepoint/a2z-utility-logins-exposure]] · [[10-Business/entity-structure/berk-inc-umbrella]] | 2026-08-31 | open |
| **Extend the Berman revocation check to the `a2zcp.com` legacy tenant.** A revocation exercise scoped to Parakeet's tenant does not reach a separate tenant that is still the identity of record on live billing portals. Same logic as the shared-mailbox row above, different tenant. | **Austin with Demetria Loukas** | [[00-Meta/commitments]] items 2 and 16 | 2026-08-31 | open |
| **Check the Berman access revocation against the four shared service accounts before item 16 is called closed on access.** *"ALL BANK ACCOUNTS"* disabled a named individual. **It did not rotate a shared password.** Standard consequence of shared credentials meeting a departure; nobody has looked. | **Austin with Demetria Loukas** | [[00-Meta/commitments]] items 2 and 16 | 2026-08-31 | open |
| **Rewrite the IT credential-rotation email before it goes.** Its premise is that the file's contents are unknown, and its first ask is to rotate all 38 as though they were 38 secrets. Flagged in place at `10-Business/sharepoint/drafts/draft-it-credential-rotation.md`. | **Austin** | [[10-Business/sharepoint/a2z-utility-logins-exposure]] | 2026-08-31 | open |
