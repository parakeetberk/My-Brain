# Agent brief: SharePoint migration

**The job in one sentence:** support Albert's migration from the Parakeet Communities SharePoint to the Parakeet Birdcage SharePoint in the new structure, starting by inventorying and de-duplicating the source, because the target structure is now written down and everything can be checked against it.

**Runs when:** the user asks for help with the SharePoint migration, or Albert asks for an inventory, a mapping or a verification pass.

## The prerequisite, now met

**The target Birdcage structure is documented.** `10-Business/sharepoint/Data Storage Security Direction.xlsx` was filed on 2026-08-31 and is written up as three pages:

- [[10-Business/sharepoint/target-structure]]: the target folder tree, its nine top-level areas, and the per-community 8-folder template.
- [[10-Business/sharepoint/permissions-matrix]]: WRITE / READ / NO ACCESS by group, the patterns, the exceptions, and every row where the permission is still blank.
- `10-Business/sharepoint/security-groups` and `10-Business/sharepoint/migration-plan`: the 15 groups with real membership counts, and the sequence.

**Check every mapping and every verification against those pages, not against what the old SharePoint happens to look like.** Two things they do not settle, and this job must not settle on its own: the workbook holds **two trees that disagree** (the newer nine-area `Folder Structure` sheet is the one rendered; the older hidden six-area `Structure` sheet holds folder descriptions and a `Company Policies & SOPs` area the newer one lacks), and **the 242-file SOP library has no home in the newer tree.** Both are questions for Albert and Austin.

**Albert and Austin still have to confirm the write-up before anything moves.** Documented is not the same as agreed.

## Inputs

- [[10-Business/sharepoint/target-structure]] and [[10-Business/sharepoint/permissions-matrix]] are the written target. Every mapping row resolves against these.
- `10-Business/sharepoint/migration-plan.md`: the sequence, the source inventory list and the open questions.
- `10-Business/sharepoint/security-groups.md`: the 15 groups, their real membership, and the two gaps (`Ops Administration` has no members; Alexandra Pontes has no account row).
- `10-Business/people/albert.md`: whose project this is.
- The **Microsoft 365 connector's `sharepoint_*` tools**: `sharepoint_search`, `sharepoint_folder_search`, `sharepoint_create_folder`, `sharepoint_copy_item`, `sharepoint_move_item`, `sharepoint_rename_item`, `sharepoint_upload_file`, `sharepoint_update_file`. This is the mechanism for the whole job.
- Albert, and Austin: the two who confirm the documented target and answer every unresolved mapping row.
- `10-Business/entity-structure/` and `70-Operations/sops/`, the two known duplicate-heavy areas, useful as the pilot set.
- `00-Meta/austin-operating-manual.md`: Austin's own background is Microsoft 365 architecture; expect him to have opinions on the structure and to want to see the reasoning.

## Steps

1. **Inventory the source and de-duplicate it.** Use `sharepoint_folder_search` and `sharepoint_search` to walk the Parakeet Communities SharePoint. Produce a full inventory: path, item count, size, last-modified date, and owner where recorded. Record it in the vault so a later session does not re-crawl. **`Sheet2` of the source workbook is a worked example of the output for one community**: the existing Applegate folder, 377 directories and ~1,577 files, 937 of them images. It shows what to expect. **De-duplicate before moving, not after**, by hash and not by filename. Two sets are already measured and make a good pilot:
   - **The entity folder holds 60 byte-identical Property Management Agreement pairs**: 129 PDFs, 69 unique files, caused by two naming conventions running in parallel. Pick one convention, keep one copy, archive the other.
   - **The process folder holds 96 duplicate files**: 48 byte-identical sets, every numbered process existing twice (drafting room and published wiki), plus the 14 state compliance SOPs existing twice again.
   - Compare by hash, not by filename. Report the sets and the recommended survivor; do not act on it yet.
2. **Map old to new.** One row per source folder: its destination in the documented Birdcage structure, or "archive", or "unresolved: ask". **Every unresolved row is a question for Albert, not a judgement call.** Known unresolved before you start: where the SOP library goes, where MIP II goes, whether litigation gets a folder, whether the older draft's `PROPERTY REFERENCE HUB` survives, and who `Ops Administration` is.
3. **Resolve the blank permission rows and stand the groups up first.** The permissions page lists every folder row where the permission is unspecified: `Home Info Packets`, `Quotes & Invoices`, the whole `Acquisitions` area, and every HR and Finance row in the older draft. Get them decided, create the 15 groups plus `Property Operations` and the 68 per-community groups, apply the model and verify it with a test file **before a single real file lands**. Otherwise the first thing that moves lands in an open folder. Creating groups and applying permissions is Austin's to approve and Austin's to do, not this agent's.
4. **Sequence the move.** Order the migration so that the least-coupled, most-duplicated areas go first and anything a live process depends on goes last. The SOP library, the title-transfer folders and the Operations month-end closeout folders are all referenced by live SOPs and break work if they move mid-cycle. Write the sequence down with a stated reason per phase.
5. **Get Austin's approval on the migration plan before anything moves.** The plan is the structure document, the permissions model, the mapping, the duplicate report and the sequence, together.
6. **Move in phases, verifying each.** After each phase: item counts match, no file is only in the destination without a source record, links in live SOPs that point at moved folders are identified and reported. Verification is part of the phase, not a later step.
7. **Report after each phase:** what moved, what was archived, what is still unresolved, and what SOP links now need updating.

## Output

- **The written Birdcage target structure, already delivered.** [[10-Business/sharepoint/target-structure]] and [[10-Business/sharepoint/permissions-matrix]]. What remains is Albert's and Austin's confirmation of it.
- A source inventory, recorded in the vault. **This is now the deliverable that unblocks everything else.**
- An old-to-new mapping table with unresolved rows flagged as questions.
- A duplicate and superseded report, by hash, with a recommended survivor per set.
- A phased migration plan with Austin's approval recorded.
- Per-phase verification results and a list of SOP references that need updating.

## Rules for this job

- **Never delete anything on the user's behalf.** Not a duplicate, not an empty folder, not an obvious mistake. **Superseded material moves to an archive location** and stays there. If deletion is genuinely the right answer, say so and let a human do it.
- **The migration plan is approved by Austin before anything moves.** No phase starts on this agent's own judgement.
- **Do not move anything a live process depends on without saying so first.** The SOP library, the title-transfer folders, the Operations month-end closeout folders and the Main Eviction Cases Sheet are all named inside working SOPs. Moving them silently breaks a process someone runs on the 6th, the 25th or the 27th.
- **Resident files are in scope for structure and out of scope for content.** Move folders; do not open, read out, summarise or relocate an individual resident's file content, and never generate anything with a resident's name on it.
- **Investor and board material moves last and only with explicit approval**: anything touching the Bedrock Fund II LPs while the fund is open, and anything in the board or fund-reporting areas.
- **Personnel files are Austin-only.** Structure work on an HR library is fine; reading or relaying its contents is not.
- **Nothing in this job spends money or changes a permission.** Sharing settings, external access and licence changes are Austin's, not this agent's.
- **Never reproduce any individual's personal compensation** encountered in a source folder while inventorying.
- Record what was done in `00-Meta/log.md`, one line per phase.
