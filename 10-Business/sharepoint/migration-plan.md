# Migration plan — into the Parakeet Birdcage SharePoint

**What this is:** the plan for moving everything into the new SharePoint structure, now that the target and its permissions are written down.

**Status:** current — 2026-08-31

## The facts

- **The prerequisite is met.** Until 2026-08-31 the target Birdcage structure was undocumented, and that was the one thing blocking this work. `Data Storage Security Direction.xlsx` was filed on 2026-08-31 and is now written up as the target-structure and permissions-matrix pages in this folder. The migration can be planned against a written destination.
- **Albert Gano owns the migration.** Austin Berk approves the plan before anything moves.
- The workbook already carries a **partial build status** per folder: Marketing's four folders, `Corporate Legal Matters` and `Entity Structure` are marked **Done**; `Compliance`, `Sales`, `Lending` and `Administrative` are **To Do**; `Tax > Filings`, `Inventory`, `Dealership Information` and the whole `Sales & Inventory` area are **Pending** on a named discussion. Use that column as the build tracker rather than starting a new one.
- **One community's current contents have already been inventoried.** `Sheet2` of the workbook is a `tree /f` dump of the existing Applegate folder: **377 directories and roughly 1,577 files**, of which **937 are images** (605 .jpg, 212 .jpeg, 95 .png, 25 .dng) and **330 are PDFs**. Its top level uses the **old** eight-folder convention — `1. Asset Management, 2. Communication and Photos, 3. Facilities, 4. Insurance, 5. Legal, 6. Notes and Templates, 7. Operations, 8. Reports` — which maps to the new template's **unnumbered** `Asset Management, Communications, Construction, Facilities, Insurance, Legal, Operations, Templates` (numbers removed 2026-08-31 by Austin's ruling — see [[10-Business/sharepoint/target-structure]]; the source keeps its numbering because that estate is read-only). **Communications and Photos split apart; Reports goes away and Construction appears.** Note the two lists are no longer positionally comparable: source `4. Insurance` maps to target `Insurance`, which sits fifth alphabetically, so **this mapping must be read by name, never by number.** That mapping applies to all 68 communities, not just Applegate.
- **Nothing in this plan deletes anything.**

## Source inventory that lives in this vault

| Source | What is in it | Maps to |
| --- | --- | --- |
| `10-Business/entity-structure/` | **430 entity documents.** Of the 129 Property Management Agreement PDFs, **only 69 are unique — 60 byte-identical pairs**, caused by two naming conventions running in parallel. Plus 7 non-entity files that belong elsewhere. | `00-Corporate > Legal > Entity Structure` — Formation Docs, PMAs, Filings. Marked **Done** in the workbook and owned by AG. |
| `70-Operations/sops/` | **242 process files** in four zones, with **48 byte-identical duplicate sets (96 files)** and **four coexisting SOP Master Tracker versions** (only `SOP_Master_Tracker_v3.xlsx` is current). | The earlier draft's `CORPORATE > Company Policies & SOPs > Operational SOPs`. **The newer tree has no such folder — this is the single biggest unresolved mapping question.** |
| `10-Business/hr/` | The Employee Handbook PDF and 7 MIP II documents. | Handbook to `00-Corporate` (policies); MIP II to `Human Resources`, or to `00-Corporate > Investor Relations` if it is treated as equity rather than compensation. Ask. |
| `80-Finance/` | The nine 2026 executive-strategy workbooks, the March-2026 board deck, and 5 Bedrock (BMHCII) investor letters including the April-2026 wind-down update. | Strategy workbooks to `00-Corporate > Strategy > Corporate Models`; board deck to `00-Corporate > Investor Relations > Board Materials`; Bedrock letters to `Asset Management > Investor & Lender Relations > Investor Packages`. **All three are Board-plus-one-team folders. This is the last phase, not the first.** |
| `60-Communities/` plus the per-community operational material | 68 community pages and the Property Data Sheet. | `Operations > [Community Name] [City, State]` and the 8-folder template. The Property Data Sheet is already named as a live file in `00-Corporate > Birdcage Files`, owned by ZS. |

## The sequence

1. **Document the target.** Done — this page, plus target-structure and permissions-matrix. Get Albert and Austin to confirm both before step 2.
2. **Inventory the source.** Walk the current Parakeet Communities SharePoint with `sharepoint_folder_search` and `sharepoint_search`: path, item count, size, last-modified, owner where recorded. Record it in the vault so a later session does not re-crawl. `Sheet2` is a worked example of the output for one community and shows what to expect — a photo-heavy tree four to six levels deep.
3. **De-duplicate before moving, not after.** Compare by hash, not filename. The two measured sets are the pilot: the 60 PMA pairs and the 48 SOP sets. Produce the set list and the recommended survivor per set. **Do not act on it — report it.** Moving duplicates just relocates the problem, and de-duplicating after the move means doing it twice.
4. **Map old to new.** One row per source folder: destination, or "archive", or "unresolved — ask". Every unresolved row is a question for Albert. Known unresolved already: where the SOP library goes, where MIP II goes, whether litigation gets a folder, whether the PROPERTY REFERENCE HUB survives, and what `Ops Administration` is.
5. **Stand up the groups and permissions first.** Create the 15 groups plus `Property Operations` and the 68 per-community groups in Entra, apply the permission model, and verify it with a test file **before a single real file lands**. Otherwise the first thing that moves lands in an open folder. Resolve the blank-permission rows before this step: `Home Info Packets`, `Quotes & Invoices`, `Acquisitions`, and every unspecified HR and Finance row.
6. **Move area by area, least coupled first.** Marketing and `00-Corporate > Legal > Entity Structure` are already marked Done and are the natural first movers. Then Data & Analytics, then Sales & Inventory, then Operations community by community, then Finance, then HR, then Investor Relations and Board Materials last.
7. **Verify each phase as part of the phase.** Item counts match; nothing exists only at the destination without a source record; every live SOP that names a moved folder path is identified and reported for updating.
8. **Report after each phase** — what moved, what was archived, what is unresolved, what SOP links now need changing.

## The guardrail

- **Nothing gets deleted.** Not a duplicate, not an empty folder, not an obvious mistake. **Superseded material moves to an archive location and stays there.** `Acquisitions > _Archive` already exists in the target tree; the other areas need an equivalent before anything is superseded.
- **Austin approves the plan before anything moves.** The plan is the target structure, the permissions model, the mapping, the duplicate report and the sequence, together. No phase starts on an agent's or an assistant's own judgement.
- Resident files are in scope for structure and out of scope for content.
- Nothing here spends money or changes a sharing setting. External access and licence changes are Austin's.

## Still unknown

- **Whether the current Parakeet Communities SharePoint has been inventoried.** `Sheet2` covers one community out of 68. There is no count of the whole source — no total item count, no size, no top-level map. Step 2 exists because this is unknown.
- **Whether the 15 groups exist in Entra yet or are still a plan.** `User Groups` reads like an export — it has display names, user principal names and a group object row per group, which is the shape of a tenant export rather than a wish list. But two things say otherwise: `Ops Administration` has a permission column and no membership column at all, and one group object is spelled `Prop Ops` where its column header reads `Property Operations`. If these were live groups those two would not disagree. **Ask Albert whether the groups are created, and whether the sheet was exported from Entra or typed into it.**
- **What cutover looks like for people mid-work.** 60 people have `Property Operations` access and work in community folders daily; the offshore finance team works in Bank Accounts and Monthly Close on a monthly clock. There is no stated cutover window, no read-only freeze, and no answer to what happens to a file someone has open when its folder moves. The month-end close, the 6th/25th/27th SOP cycles and the title-transfer folders are the specific things that break if a folder moves mid-cycle.
- **Where the SOP library lands.** 242 files with nowhere in the newer tree to go.
- **Who `Ops Administration` is.** It holds WRITE on a large number of community folders and has no members.
- **Alexandra Pontes has no account row in the workbook.** The third regional manager cannot be put into Regional-Mgrs until she is provisioned.

## Decisions

- 2026-08-31 — the target structure is documented, so the migration's step one becomes the source inventory rather than documenting the target. (Source: [[10-Business/sharepoint/Data Storage Security Direction.xlsx]])

## Related

- [[10-Business/sharepoint/target-structure]] — the destination this plan moves things into.

## Sources

- [[10-Business/sharepoint/Data Storage Security Direction.xlsx]] — the target structure, the permissions model, and the `Sheet2` inventory of the existing Applegate folder.
- [[70-Operations/sops/sop-library]] — the 48 duplicate sets, the 96 files and the four tracker versions.
- The entity-map page in `10-Business/entity-structure/` — the 430-document count and the 60 byte-identical PMA pairs.
