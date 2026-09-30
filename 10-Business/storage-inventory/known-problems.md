# Storage estate: known problems

**What this is:** The eight structural defects in the file estate, ranked. Every one of them is cheap to fix during Albert's migration and expensive to fix after it. Consolidation is the only moment these are in reach.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

## The facts

**1. `/sites/ParakeetHome` and `/sites/ParakeetHomes` are one letter apart and neither is a superset.** The singular site holds 29 communities, the plural 24. Of the 19 that overlap, 14 are byte-identical but five differ materially - Northgate is 219.8 MB larger and Harbour 105.4 MB larger on the singular site, Lucky Clover is 244.9 MB smaller. Ten communities exist only on singular, five only on plural. Deleting either one loses data. This is the most dangerous item in the estate and it has to be resolved before any consolidation touches site plans. VERIFIED.

**2. Site plan cloning is a three-way, not a four-way, and one of the four paths must not be deduped.** `/sites/ParakeetHomes`, the Cavco satellite, and `/sites/main/.../Cavco Homes/Plans for Sites` hold byte-identical trees - 27 Bay Oaks lot folders at exactly 812,391,202 bytes each - created in a copy chain running 2026-02-02 to 02-03 to 02-05. `/sites/ParakeetHomes` is authoritative; it is the source of the chain and the only complete tree. The fourth path, `/sites/main/Shared Documents/Construction/BAY OAKS VILLAGE I`, is the construction record, not a duplicate. The pattern extends to 22 of 23 shared communities, roughly 16.6 GB redundant. VERIFIED.

**3. Community names do not reconcile between Operations and Construction.** Both hold 71 folders and they are not the same 71. Six Operations assets have no Construction folder, four the reverse, and eight are spelled differently including outright typos such as `WHSIPERING PINES MA`. Any join on community name silently mismatches about 18 assets, which corrupts every cross-system report built on it. VERIFIED.

**4. Securities and investor records sit under a personal Gmail account.** `austinrberk@gmail.com` holds standing membership in three corporate Google Shared Drives, one of which contains cap tables, fund subscriptions, K-1s, an LPA and executed signature pages. That access sits outside any Workspace admin lifecycle and is invisible to a standard audit query, because Shared Drive contents carry neither an owner field nor a shared-with-me timestamp. Three drives is a floor - memberships cannot be enumerated. VERIFIED. Detail at [[10-Business/storage-inventory/gdrive-personal]].

**5. OneDrive root is a dumping ground.** Roughly 200 loose files at the root, including `Book1.xlsx` through `Book8.xlsx`, `Drawing 1-8.vsdx`, and `Copy of Copy of Copy of FMHA.xlsx`. Real work was done here and lost. VERIFIED.

**6. Institutional knowledge is locked in archived user drives.** `/sites/UserArchive` holds departed employees' files that nobody can find - Deborah Koester from 2025-10-08 and Amy Furbush from 2026-06-12. VERIFIED.

**7. Two legal sites exist with no documented distinction.** `/sites/Corporate-Legal` and `/sites/LegalParakeet`. Resolve which is which before filing anything legal to either. VERIFIED.

**8. The deal models carry known narrative contamination.** `Claude Cowork/.../batch/kb/INDEX.md` documents prose from one deal, Triple S, cloned into dozens of workbooks and tagged `do-not-quote`. Any index or summary that quotes model narrative without honouring that flag propagates text already known to be wrong. Read that INDEX before building anything on the underwriting corpus. VERIFIED.

## Related

- [[10-Business/sharepoint/migration-risks]] - what breaks operationally if the migration runs before these are resolved.

## Sources

- `99-Archive/2026-08-catchup/superseded-brain-CLAUDE.md`, the Known problems section, compiled 2026-08-26 from the six-agent storage survey.
- The seven inventory pages in this folder, which carry the underlying counts.
