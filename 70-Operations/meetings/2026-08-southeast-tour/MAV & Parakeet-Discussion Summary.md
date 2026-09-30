# 08-24 Meeting: Deduplication Workflow, MCP Sandbox, and Data Warehouse Integration

Date & Time: 2026-08-24 15:05:09
Location: [Insert Location]
Attendees: [Speaker 1], [Speaker 2], [Speaker 3], [Speaker 4]
## 1. Deduplication Workflow Launch
### Conclusion
A new deduplication workflow will be launched on the Parakeet account on August 25, 2026. This workflow will only apply to new prospects moving forward, not existing ones. The logic for merging duplicates will take the oldest lead source value, unless the source is 'Google ad'.
### Plan
- [ ] Launch the new deduplication workflow live on the Parakeet account. -- *Speaker 1* 2026-08-25
- [ ] Send the testing document to Speaker 2. -- *Speaker 1*
- [ ] Review deduplication rules and any flagged issues on a call. -- *Speaker 1, Speaker 2* 2026-08-26
### Discussion Points
1. [Speaker 1]: The new merge and duplication workflow will take the oldest lead source value unless the ad source is 'Google ad'.
2. [Speaker 2]: The team needs clarity on specific workflow rules before launch, especially for cases where names differ but phone numbers/emails match, which could indicate different people applying for the same home.
3. [Speaker 1]: In the scenario described by Speaker 2, the workflow would take the oldest value.
4. [Speaker 2]: The workflow will only apply to new prospects moving forward, not existing ones.
   - [Supporting info/data 1 for Discussion Point 4] It will trigger whenever a new prospect is created in the account.
## 2. MCP Sandbox Account Setup and Migration
### Conclusion
A trial sandbox account for the MCP (Mav's Connection Platform) will be created by August 28, 2026. Data from the prospects, tenants, units, properties, and meetings/tours modules will be migrated from the current CRM into this sandbox environment. This is a preview to demonstrate MCP's capabilities, including its over 900 tools, and how it syncs with the Claude account. It will not have historical timeline data for past records but will track it for new records moving forward.
### Plan
- [ ] Create a trial MCP sandbox account with Parakeet's data. -- *Speaker 1* 2026-08-28
- [ ] Hold a meeting to set up the MCP account, connect it to the Claude account, and run test prompts. -- *Speaker 1, Speaker 2, Speaker 3, Speaker 4* 3 p.m. EST on 2026-08-28
- [ ] Send the meeting invite. -- *Speaker 2*
### Discussion Points
1. [Speaker 2]: The meetings module should be a high priority for data migration, following prospects.
   - [Supporting info/data 1 for Discussion Point 1] The priority should be prospects, meetings/tours, then properties.
2. [Speaker 1]: The initial sandbox migration will not include historical timeline data, so reports like "prospects converted in May" won't be possible for existing records.
3. [Speaker 3]: Once live, the system will track the complete funnel flow by time for new prospects, but it will not retroactively apply to old data.
4. [Speaker 1]: The sandbox is a preview to test functionalities, privileges, and workflows before planning a full migration that would include all historical timeline data.
## 3. Reporting and Data Warehouse Integration (RentViewer)
### Conclusion
The team discussed integrating RentViewer to pull data into their data warehouse (Microsoft SQL) to centralize reporting and eliminate manual data backups. There are concerns about potential data duplication, conflicts between data sources (Mav vs. Rent Manager), and the overall data flow architecture. It was decided that after the MCP capabilities are reviewed on Friday, the next step is to connect with the RentViewer team to scope the integration, ensure no data conflicts, and understand the workflow.
### Plan
- [ ] Connect with the RentViewer team to discuss integration possibilities with the CRM and data warehouse. -- *Speaker 1, Speaker 4, Saad, Dan* After 2026-08-28
### Discussion Points
1. [Speaker 4]: The ideal state is to have all data from Rent Manager and other sources sync into a central data warehouse for unified reporting accessible via agents in Claude.
2. [Speaker 4]: To avoid conflicts, a single source of truth should be chosen for prospecting and lead generation information rather than pulling from both Mav and Rent Manager.
3. [Speaker 3]: The team needs to be thoughtful about data architecture to avoid inefficiently "round-tripping" data between the data warehouse, MCP, and other systems.
4. [Speaker 1]: Scoping the integration requires assessing three key areas: cost (API usage, tokens), governance (data privileges, audit logs), and workflow capabilities (what agents and scheduled functions can be built).
5. [Speaker 1]: Integrating RentViewer could cause data duplication issues with the existing Rent Manager integration, so it's critical to involve the RentViewer team to ensure workflows are compatible and there are no gaps.
> **AI Suggestions**
> AI has identified the following issues that were not concluded in the meeting or lack clear action items; please pay attention:
> 1. **Master Data Source and Architecture:** There is no clear decision on the primary source of truth. Define whether MCP, the central data warehouse, or Rent Manager will serve as the source of truth for different data types (e.g., prospecting data) to avoid conflicts and redundancy. A follow-up architectural discussion is needed.
> 2. **Deduplication Rule Specifics:** While a call is scheduled for Wednesday, the exact rules for complex duplicates (e.g., same address, different names) were not finalized. Speaker 2 raised concerns about potential roommates being incorrectly merged. These edge cases must be explicitly defined and confirmed before or during the Wednesday call.
> 3. **Risks of Claude Integration:** Speaker 1 highlighted significant governance risks with using Claude, such as potential accidental mass record deletion and insufficiently defined audit logs. There is no mitigation plan. A dedicated discussion on safety protocols, data privileges within Claude, and audit solutions is necessary before expanding its use.
> 4. **Scope and Cost of Full MCP Migration:** The meeting focused on launching a sandbox, but the process, timeline, cost (API usage and tokens), and resources for a full migration of historical data and timelines into the live MCP environment were not discussed. This needs to be scoped as a follow-up to the sandbox review.