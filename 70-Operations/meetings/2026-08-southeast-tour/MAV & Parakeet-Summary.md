# MAV & Parakeet

## Meeting Information
> **Date:** 2026-08-24 15:05:09
> **Location:** [Insert Location]
> **Participants:** [Speaker 1] [Speaker 2] [Speaker 3] [Speaker 4]
---
## Meeting Notes
### Duplicate/Merge Workflow Launch for Parakeet’s CRM Account
- The duplicate/merge workflow will launch on Parakeet’s account on **2026-08-25**.
  - Logic: If Google Ads is the ad source, retain that value; otherwise, use the oldest lead source.
  - Applies only to **new prospects** created after launch, not existing duplicates.
- Speaker 2 requested a written rules document prior to launch.
  - Speaker 1 confirmed a testing document exists and will share it.
- Edge case: Two people (e.g., roommates) with the same name but different contact info.
  - Speaker 1 noted the current logic would use the oldest value; further discussion is needed.
- A review call is scheduled for **2026-08-26** to walk through the testing document together.
---
### MCP Sandbox Account Setup and Capabilities
- Speaker 1 will create a **trial MCP sandbox account by 2026-08-29 (Friday)**.
  - Modules to include: Prospects, Tenants, Units, Properties, and Tours/Meetings.
  - Speaker 2 asked to prioritize Meetings/Tours as second or third in migration order (after converted prospects).
  - All current CRM data will be imported so the sandbox uses Parakeet’s actual data.
  - The sandbox will **not** be connected to the live Rent Manager CRM account.
- The sandbox includes ~**900 tools** in Zoho (workflows, field updates, data cleaning, reporting).
- **Limitation:** Historical timelines (e.g., conversions by month) won’t be available in the initial export; timeline-based reporting will be available after full migration.
- Goal for the **2026-08-29 Friday call (3:00 PM EST)**: Connect the sandbox to the team’s Claude account and run initial test prompts (e.g., pull CRM data, generate a dashboard).
---
### Rent Viewer Integration and Data Warehouse Discussion
- Speaker 1 noted Parakeet is using Rent Viewer and asked about the reporting workflow.
  - Currently, Speaker 3 (Ozzy) manually pulls backups and pushes them to the cloud — a manual and sometimes inaccurate process.
- Speaker 4 described the preferred approach: use Rent Viewer to sync data daily into a **data warehouse** to remove manual pulls and centralize reporting.
  - The warehouse receives data from Rent Manager and other sources; refresh timing varies by report.
  - Speaker 1 asked about the warehouse tech stack; Speaker 4 said it is likely **Microsoft SQL** and offered to connect Speaker 1 with **Saad and Dan** from the Rent Viewer team.
- Rent Viewer’s website indicates a CRM integration capability, potentially centralizing reporting (similar to the MH Village integration).
- Speaker 1 flagged duplication risks if data flows from Mav → Rent Manager → Rent Viewer’s warehouse → CRM simultaneously.
  - Recommended engaging the Rent Viewer team before proceeding to avoid conflicts.
---
### AI/Claude Integration Strategy and Governance
- Speaker 4 and Speaker 3 want all data accessible via Claude or a similar LLM interface through the data warehouse.
- Speaker 3 cautioned against “round-tripping” data across MCP, the data warehouse, and cloud services without a clear routing plan.
- Speaker 4 suggested choosing **one source of truth** (Mav or Rent Manager) for prospecting/lead generation data to prevent conflicts.
- Speaker 1 outlined three areas to assess before full deployment:
  1. **Cost:** Token usage and API consumption — multiple agents/workflows can quickly exhaust API limits.
  2. **Governance:** Data privileges, audit logs, and safeguards to prevent accidental deletions; noted Claude’s audit log visibility is limited.
  3. **Workflow capabilities:** Define which agents, scheduled functions, and workflows will push/pull data into the CRM.
- All parties agreed to schedule a broader call with internal teams and the Rent Viewer team before finalizing the integration plan.
---
## Next Arrangements
- [ ] Speaker 1 to send the testing document for the duplicate/merge workflow to Speaker 2 by **2026-08-25**
- [ ] Duplicate/merge workflow goes live on Parakeet’s account on **2026-08-25**
- [ ] Speaker 2 and Speaker 1 to meet on **2026-08-26** to review the testing document and workflow rules
- [ ] Speaker 1 to complete MCP sandbox setup (Prospects, Tenants, Units, Properties, Tours/Meetings) by **2026-08-29 (Friday)**
- [ ] Speaker 1 to send details on the 900+ MCP tools and example use cases before the Friday call
- [ ] MCP review call on **2026-08-29 at 3:00 PM EST** to connect the sandbox to the Claude account and run test prompts
- [ ] Speaker 4 to connect Speaker 1 with **Saad and Dan** from the Rent Viewer team after **2026-08-29**
- [ ] Schedule a broader call with internal teams and the Rent Viewer team to discuss data warehouse integration and avoid duplication risks
---
## AI Suggestions
> **AI Suggestions**
> AI has identified the following issues that were not concluded in the meeting or lack clear action items; please pay attention:
> 1. **Data routing strategy is undefined:** The optimal routing of data across MCP, the data warehouse, and Claude is not documented, risking redundant or conflicting flows between Mav, Rent Manager, Rent Viewer, and the CRM.
> 2. **Rent Viewer integration risks are unresolved:** Potential duplication between the CRM integration and Rent Viewer’s warehouse sync remains unaddressed. No timeline exists for the Rent Viewer team call, and the integration design is unknown.
> 3. **Duplicate workflow edge cases not finalized:** The scenario of two individuals (e.g., roommates) sharing a name but with different contact details is unresolved. The current “oldest value” logic may misidentify distinct individuals as duplicates.
> 4. **Claude audit log and governance gaps:** Limited audit log visibility in Claude presents governance risks if agents delete or overwrite records. No mitigation plan or timeline was discussed.
> 5. **Source of truth for lead/prospecting data not decided:** Choosing Mav or Rent Manager as the single source of truth is still pending, risking conflicts once MCP and data warehouse integrations go live.