# 08-18 Meeting: Property Operations, Roadwork Warranty, and System Integration Alignment

## Meeting Information
> Date: 2026-08-18 08:46:34
> Location: [Insert Location]
> Participants: [Speaker 1], [Speaker 2], [Speaker 3], [Speaker 4], [Speaker 5], [Speaker 6], [Speaker 7], [Speaker 8], [Speaker 9], [Speaker 10]
## Meeting Notes
### Property Management and Operations
- **Use of Lawn Area and Amenities:** Discussion centered on the current use of the lawn for kids’ soccer and dog walking. Suggestions included adding a small playground or a general park area. There was also interest in renting out the clubhouse for private events, which would require a rental/deposit model. No final decisions were made.
- **Property Sales, Titles, and Pricing:** A prior sale reportedly fell through. The team identified securing the property title as the next critical step. Pricing was mentioned in ranges of "$1,100 rental" and "$30,000 purchase." The strategy is to list the property to gauge market interest before considering rehab.
- **Real Property Status and Regulatory Items:** The property is "deemed real property," and the team will contact the county for clarification. The ability to sell a unit is tied to the completion of herbicide/preventative applications. It was noted that many prospective applicants fail to submit their applications.
- **Fencing, Curbing, and Site Upgrades:** The team suggested budgeting to renew fencing and remove aesthetically unpleasing chain link sections. Drainage issues were noted, with water flowing into backyards due to a single rolled curb. Mailbox standardization and uniform mini blinds were mentioned as potential marketing improvements.
- **Pool Operations and Compliance:** The pool is currently unmaintained and remains closed. Three estimates for maintenance service (3, 5, or 7-day) are pending a decision. A permit has been obtained, but the pool cannot open until the surrounding fence is replaced to meet height compliance. The idea of staff adding chlorine was raised but with concerns about proper training.
- **Security, Cameras, and Office Safety:** Security incidents include kids breaking into houses, a car theft, and theft of signs/flowers. A new doorbell camera at the office has reduced aggressive entries. The team recommended installing more cameras inside and outside the office, around parks, and at the clubhouse.
- **Trash Management and Dumping Issues:** Bulk items are blocking dumpsters, preventing haulers from accessing bins. Options discussed included switching to individual cans, removing dumpsters entirely, or requiring residents to haul their own trash. The team supported moving to individual cans with a chargeback system and implementing escalating fines ($75, then $150) for illegal dumping.
- **Community Events and Resident Engagement:** A recent back-to-school event with hot dogs and backpacks was held. There is resident interest in renting the clubhouse, but logistics around access control and potential pool access need to be defined.
- **Home Title Issues from Prior Management:** Residents have reported that the prior manager registered home titles in her own name, preventing residents from obtaining insurance. The team believes the seller should resolve this and is working to identify the correct contact for title resolution.
- **Maintenance and Equipment:** A maintenance shed containing a zero-turn mower and other equipment was discovered. The team plans to inventory these assets. The pool/pond has multiple patches, was recently cleaned but is deteriorating again. The team suggested getting staff certified for water management and assessing the concrete deck for grinding and sealing.
### Roadwork and Vendor Dispute
- **Description:** A recent road project has resulted in significant flooding and drainage failures, with some storm drains completely plugged. One drain covered with two-by-fours and metal sheathing poses an immediate safety risk. The team is considering pursuing a warranty claim against the vendor.
- **Action Plan:** [Speaker 4] will draft a firm response to the vendor, gathering all prior communications and confirming warranty terms. The team will also get quotes from national vendors (e.g., Rose Paving) to document the scope and cost of necessary repairs. [Speaker 8] is prepared to engage the vendor directly if needed. Legal action is a possibility if the vendor is unresponsive.
### System Integration: Rent Manager, QuickBase, and FastField
- **Project Status and Frustration:** [Speaker 4] expressed significant frustration with project delays, as the initial launch target of July has passed. A communication gap was identified: critical information shared with the vendor's sales team was not passed to the implementation team. The team proposed a "reset" by conducting a full walkthrough of Rent Manager to align on objectives.
- **System Architecture and Workflow:** The agreed-upon goal is to use QuickBase as a central system to govern data and enforce workflows that Rent Manager lacks. The process will involve a daily Power Automate function exporting data from Rent Manager to SharePoint, which QuickBase will then read. QuickBase will house this metadata to control dynamic dropdown lists in FastField forms (e.g., showing only vacant units for a move-in).
- **Use Cases:**
  - **Move-in/Move-out:** The system will create a full lifecycle view, tracking residents from initial interest to move-in. It will enforce compliance steps and checklists, such as preventing a move-in to an occupied unit.
  - **User Roles:** Field staff (e.g., community managers) will primarily use FastField for data entry, while corporate staff will use QuickBase for analytics, process monitoring, and identifying bottlenecks.
- **Approval and Data Flow:** A multi-tier approval flow was defined (community manager → regional/district manager → "Natalie" for final approval) that QuickBase will manage. The long-term goal is to establish a two-way API integration between QuickBase and Rent Manager, but the initial phase will rely on file exports.
- **Data Requirements:** Progress is dependent on receiving metadata exports from Rent Manager, including community lists, property IDs, unit numbers, and occupancy status.
### Administrative and Procedural
- **Document Management:** Physical archives (maps, photos, water system documents) will be shipped to the office for scanning and digitization to create a secure digital backup.
- **Application Process:** The team noted that many prospective renters start but do not complete their applications, often due to concerns about their history. The strategy is to proactively contact these applicants to address concerns before they pay the non-refundable application fee.
- **Meeting Logistics:** The next meeting is scheduled for Tuesday, August 25, 2026, to conduct a walkthrough of the Rent Manager system.
## Next Arrangements
- **Property & Operations**
  - [ ] Clarify and secure property title for the pending sale.
  - [ ] Finalize a pricing strategy ($1,100 rent vs. $30,000 purchase) and list the property.
  - [ ] Contact the county regarding the real property status and its requirements.
  - [ ] Select a pool maintenance plan and replace the pool fence to meet compliance.
  - [ ] Draft a clubhouse rental policy, including fees, deposits, and access control.
  - [ ] Scope and budget for fence renewal and removal of chain link sections.
  - [ ] Assess the feasibility and cost of a small playground installation.
  - [ ] Follow up with the responsible party on home title issues and verify registrations.
  - [ ] Inventory the contents of the newly discovered maintenance shed.
  - [ ] Arrange for staff certification in pool/water maintenance.
- **Roadwork & Vendor Management**
  - [ ] Address the immediate safety risk at the compromised storm drain.
  - [ ] [Speaker 4] to send a firm email to the roadwork vendor regarding warranty claims.
  - [ ] Gather all documentation related to the roadwork project (emails, photos, contract).
  - [ ] Obtain quotes from national paving vendors to scope and price repairs.
- **Systems & Data Integration**
  - [ ] Schedule the next meeting for a walkthrough of Rent Manager for Tuesday, August 25, 2026.
  - [ ] [Speaker 4] to provide the implementation team with data exports and trial feeds from Rent Manager.
  - [ ] Define and share a written scope covering the full resident lifecycle workflow.
  - [ ] Document the multi-tier approval chain in QuickBase.
  - [ ] Ship physical documents to the office for scanning and digital archiving.
## AI Suggestions
> AI has identified the following issues that were not concluded in the meeting or lack clear action items; please pay attention:
> 1. **Vendor Information Gap:** There's a significant misalignment between information given to the sales team and the knowledge of the implementation team, causing major frustration. A process review is needed at the vendor's company, but no action was assigned.
> 2. **Title Resolution:** The path to resolving home title issues is unclear. The specific counterparty (seller, prior manager) and the owner for driving this task to completion have not been defined.
> 3. **Roadwork Warranty & Safety:** The warranty status for the failed roadwork needs confirmation. The immediate hazard at the storm drain requires an assigned owner for mitigation and inspection.
> 4. **Trash Policy Implementation:** While there is support for switching to individual cans, the operational plan (vendor selection, distribution, billing, enforcement) and communication strategy are undefined.
> 5. **Pool Compliance and Maintenance:** Responsibility and budget for the required fence replacement are not assigned. A detailed maintenance plan (daily procedures, chemical logs) is also needed, especially until staff are certified.
> 6. **Security Camera Deployment:** The plan for camera installation lacks specifics on locations, equipment standards, data access/retention policies, and budget.