# Migration Risk Brief — for Albert

**What this is:** The operational landmines in Albert's migration - what breaks if the move runs without resolving them first.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

**Date**: 2026-08-26
**Context**: Consolidating all Parakeet / A2Z / Bedrock MH files into SharePoint Birdcage. Personal items (Belmart, Winterset, Get Real, investments, financials) go to Dropbox.
**Source**: Automated survey of SharePoint (12+ sites, 2.88 TB on `/sites/main` alone), Dropbox A2Z (445.2 GB), Austin's OneDrive, and personal Google Drive, conducted 2026-08-26. Full inventories in `brain/10-Business/storage-inventory/`.

Everything below is read-only observation. Nothing has been moved.

---

## USE THIS — the target taxonomy already exists

**`Folder Structure Tracker_Outline.xlsx`** (Austin's OneDrive root). Both worksheets read in full and verified — Graph truncated the conversion, so the local sync copy was parsed directly as a zip.

**Corrected figures** (an earlier pass of this brief overstated several — use these): **9 levels** deep, not 12. **224** level-4 folders, not 748. **79 distinct** filename conventions across 2,389 cells, not 2,180. **45** communities, not 42. Row count of 6,051 was right.

**The folder tree is usable as-is. The status data is not.**

- **Tree**: complete, internally consistent, provisionable. Build from it.
- **Status column**: a four-value dropdown (`In Folder / Need / Draft Only / Not Applicable`) with only **54 cells filled — 2.2% coverage**, all in rows 204–629. It covers `_ADMINISTRATIVE` plus **3 of 45 communities** (American, Apple Creek, Applegate). **Zero of 224 level-4 folders and zero of 45 community subtrees are marked complete.** Three years stale. **Discard it** — re-audit against live SharePoint instead.
- **Sheet2** is a *second, incompatible* attempt: a 46-community × 6-document matrix scoped only to `FORMATION DOCUMENTS`, **12 of 276 cells filled**, same 3 communities. Both attempts stop alphabetically at "Applegate."

### The standard community subtree

Four level-4 folders — **ASSET MANAGEMENT, INSURANCE, LEGAL, OPERATIONS** — expanding to **47 folders and 50 filename conventions per community**, 9 levels at the deepest: `OPERATIONS/FACILITIES/PROJECTS & SERVICE ORDERS/{PROJECT NAME}/PHOTOS/BEFORE`. **43 of 45 communities are structurally identical**; American and Applegate carry local additions.

**Build from `APPLE CREEK`, not from the blank `PROPERTY NAME (CITY, STATE)` template.** The template is stale — it is the only block missing `ASSET MANAGEMENT/CLOSING DOCUMENTS/LOAN DOCUMENTS`.

### Six things the document does not answer — decide before provisioning

1. **Nine typos will propagate into real folder names.** `SITE VISTS & INSPECTIONS` appears in all 46 blocks. Fix at build time; renaming 46 live folders later is far worse.
2. **One filename convention contains a slash** — `Property Name_Violation/Inspection_...`. **Illegal in a SharePoint filename.** Must be rewritten.
3. **Hardcoded date tokens** `09302022` and `09302023` are baked into all 45 communities.
4. **Sheet1 and Sheet2 disagree on the formation-document list** — only `EIN Letter` is common to both.
5. **No shared community key between the two sheets.** Different naming; Sheet2 omits Riviera, splits Bay Oaks, and adds "Applegate Utility."
6. **`INVESTOR RELATIONS` and `JADIAN-PARAKEET` are empty stubs.**

### Worth deciding before you build

**2,210 of 2,323 folder nodes are the same 47 folders repeated 46 times.** That is a strong candidate for a **metadata-driven library** — one library, community as a column — rather than physical folder duplication in Birdcage. Physical duplication is what produced the current mess.

### Provenance — it was never ratified

Authored by Austin Berk, created **2023-09-18**, last modified **2023-09-21**. Three days of work, one author, untouched since. No approval column, sign-off, version number, or changelog. A second, larger copy (280,569 bytes, same creation date) sits in `Microsoft Teams Chat Files`, implying it was circulated for comment — **worth diffing before you commit to this version.**

---

A sixth second-brain attempt, **"The Parakeet Brain"** (2026-07-04), sits in Jon Wyss's OneDrive and on the Birdcage site — check it before designing anything new.

---

## BLIND SPOT — three libraries the survey tools cannot see

Austin's OneDrive carries **three SharePoint library sync shortcuts that the Graph file connector does not return**:

- `Parakeet Communities` — the real 24-folder company filing system
- `Parakeet Birdcage - Corporate`
- `Parakeet Birdcage - Data & Analytics`

These are the three most current and most structured branches attached to the drive, and **any survey using only `read_resource` misses all of them.** They were found only through the locally synced copy.

Assume the same class of blind spot exists on other team members' drives. If migration scope is built from connector output alone, it will be incomplete in exactly the places that matter most.

---

## STOP — do not delete these as duplicates

### 1. `/sites/ParakeetHome` vs `/sites/ParakeetHomes` — singular and plural, both real

One letter apart. **Neither is a superset of the other.**

- Singular: 29 communities. Plural: 24.
- Of the 19 overlapping, 14 are byte-identical — but **5 differ materially**: Northgate (+219.8 MB on singular), Harbour (+105.4 MB on singular), Lucky Clover (−244.9 MB on singular).
- **10 communities exist only on singular. 5 exist only on plural.**

**Collapsing these by picking one loses data.** They must be merged by content, community by community. This is the single highest-risk item in the estate.

### 2. Construction folders are not site-plan duplicates

`/sites/main/Shared Documents/Construction/BAY OAKS VILLAGE I/` looks like a fourth copy of the Bay Oaks site plans. **It is not.** It is the construction record — CONTRACTS / DEVELOPMENT / PROJECTS. Same applies to other communities' Construction folders.

Verified: the actual site-plan clone is a **three-way**, and all three are byte-identical.

### 3. `_Archive Communities` contains live assets

46.5 GB of shadow copies. **Five currently-owned communities** have duplicates in there, distinguished from the live folders only by a leading underscore. Confirm ownership status per folder before treating anything in `_Archive Communities` as archival.

---

## SAFE to consolidate — verified byte-identical

- **Site plan three-way clone**: `/sites/ParakeetHomes`, the Cavco satellite, and `/sites/main/.../Cavco Homes/Plans for Sites` hold identical trees. 27 Bay Oaks lot folders at exactly 812,391,202 bytes each; verified to file level. Copy chain runs 2026-02-02 → 02-03 → 02-05. **Keep `/sites/ParakeetHomes`** — it is the source and the only complete tree. Pattern holds for 22 of 23 shared communities, ~16.6 GB recoverable. Lake Saunders is the one exception (diverges by 512 and 6,656 bytes) — check it manually.
- **Elevation certificates**: `Asset Management & Finance/Flood Elevation Certificates/` and `Construction/__SITE ELVATION CERTIFICATES/` both report exactly 4,709,027,380 bytes. Cleanest single win available — 4.71 GB.

Caveat on both: duplication was established from folder byte-totals, not content hashes. Byte-identical at folder level is strong evidence, not proof.

---

## MUST NOT BE MISSED — content that will be skipped if scope is set naively

### 4. Lamberton Lake LP syndication records — active sale, possibly single copy

Filed under a path that does not read as Parakeet:

`ns:11855305057//Business Lines/Bedrock Group/Entities/Bedrock EM Holdings/Holdings/Lamberton Lake/`

Contains formation documents, the original PSA, 2019 Capital One refinancing, lender reporting, and **LP syndication files**. A SharePoint search for "Syndication" returns 17 results across eight other properties and **no Lamberton** — so this may be the only copy of LP subscription records for an asset **under active sale in 2026**.

Inferred, not proven — that search matched folder names only. **Confirm before any Dropbox decommission.**

Related: the Dropbox mount literally named `Lamberton Lake DD Files` is **empty** — zero entries, recursively. Do not spend time on it. SharePoint `External/Lamberton Lake (Sale 2026)/` is authoritative for the sale itself.

### 5. Three corporate Google Shared Drives under Austin's personal Gmail

`austinrberk@gmail.com` holds standing membership in three corporate Shared Drives. These are **invisible to standard audits** — Shared Drive files carry no `owner` field and no `sharedWithMeTime`, so the usual queries return clean. Found only by walking parent chains.

- `0ANSvtCpaQmhVUk9PVA` — ~30 MHC community folders (Bay Oaks, Cambridge, Lamberton Lake, Crystal River / Hunter Springs)
- `0AHN7ilIBrGJRUk9PVA` — Parakeet ops: Corporate Files, HR, Investor Relations, staff directory, bank register, aged receivables
- `0AFtyceEG0HhKUk9PVA` — A2Z fund: Cap Tables, A2Z Fund I Subscriptions, BMHCII InvestorRelations, K-1s, ND Portfolio Partners LPA, articles of merger, executed signature pages

**Three is a floor, not a total** — there is no way to enumerate Shared Drive memberships. All MH content here belongs in Birdcage.

### 6. The only consolidated entity map is in a personal Dropbox folder

`ns:11855305057//Austin Berk/Org Chart Overview.xlsx` — 11 tabs, A2Z Community Partners (Maryland hold-co) through BEDROCK I GROUP and Bedrock MHC Fund II LP/GP, seven deal-level ownership charts, domiciles, ownership percentages, EINs, and 58 named LP investors. Dated 2020, broken formula columns, ungoverned. Formation packets for five management LLCs sit at `Business Lines/A2ZMHC/Entities/`.

---

## FIX DURING THE MOVE — cheap now, permanent later

### 7. Community names do not reconcile

Operations and Construction each hold 71 folders. **They are not the same 71.** Six Operations assets have no Construction folder, four the reverse, and eight are spelled differently across the two — including outright typos such as `WHSIPERING PINES MA`.

**CORRECTED 2026-08-31 against live SharePoint — the figures below were understated.** Both trees were re-read live on 2026-08-31 (`Operations` 71, `Construction` 71, confirming the counts). The drift is **21 name pairs, not eight**, and the Operations-only set is **5, not six** — Geiger Key was counted as missing when it is in fact a rename (`GEIGER KEY MARINA  RV`, which also carries a **double space**). Three Operations folders additionally misspell their own city (`Celwiston`, `Canavaral`, `Symrna`), and Bay Oaks is a cardinality mismatch rather than a rename: two Construction folders against one Operations folder. **Total folders that fail an exact-name join: 30 of 142, not 18.** Full row-by-row list, the seven-rule naming standard and the nine items needing Austin's decision: `https://claude.ai/code/artifact/2d7225e8-a4f1-48ec-b91b-aebbb4f550d2`. The original claim is left below as written.

**Any report joining on community name silently mismatches about 18 assets.** Migration is the one moment renaming is free. Normalize to a single canonical community list or this defect moves with the data.

Start from `Administrative/Folder Structure Glossary.xlsx` — a governance artifact that already exists, untouched since 2025-03-10.

### 8. Permissions on sensitive material

Currently co-located with broadly-shared operational folders. Re-point permissions at the destination rather than replicating what exists:

- HR employee files / payroll / confidential — 3.5 GB
- Five loose copies of a 2024 payroll analysis in the `Jadian-Parakeet` branch root
- Cap table plus six files on one named individual's §83(b) election in `Executive/`
- Buyer PII in `Sales/Buyers Closing Files` — folder names carry surnames, one carries an eviction annotation
- `External/` (314.89 GB) — internal loan and tax material sitting alongside 14 named counterparty data rooms

No permission audit has been run. That is the gap.

### 9. `External/` counterparty data rooms

Eight of the 14 are within 0.05% of the same size — the same room was copied per counterparty rather than shared once. Likely large dedupe win, **but verify before collapsing**: different counterparties may legitimately have received different subsets, and that distinction may matter legally.

---

## HANDLE WITH CARE

### 10. Known narrative contamination in the deal models

`Claude Cowork/.../batch/kb/INDEX.md` (19 KB) documents prose from one deal — "Triple S" — cloned into dozens of workbooks, tagged `do-not-quote`. **Keep that INDEX with the models it describes.** If it is orphaned during the move, anything later built on that corpus will propagate known-wrong text with no warning attached.

### 11. Birdcage already has 23 GB of prior work

`Data  Analytics/Claude Cowork` holds a substantially complete underwriting effort: UW Model Engine at roadmap steps 1–13 of 21, engine validated to 100.000% on 115,152 cells, 92 historical models batch-validated, 63 deal dossiers, 96-deal knowledge base, 42/42 template tie-out certified 2026-08-03, template v1.21. Open dependency is step 10.4, "ZS pass + final ingestion pending."

Decide whether incoming volume merges into this structure or sits alongside it **before** bulk migration lands on top of it.

### 12. Two legal sites, no documented distinction

`/sites/Corporate-Legal` and `/sites/LegalParakeet` both exist. Resolve which is which before filing anything legal.

### 13. Empty or stub content — do not migrate blind

- Dropbox `Team Paper Docs` — looks substantive but is 3 KB of 200-byte Paper stubs with no file content. Confirm the actual Paper docs were exported somewhere.
- Cambridge SCH 2025 DD set — folders for only 11 of ~25 numbered request items, all uploaded in one five-minute window. Reads as an abandoned mid-flight upload.
- Google Drive `Banner` acquisition data room — 20+ correctly-structured folders, all created 2025-08-12, **all empty**. Eight leaf nodes queried directly, zero files. The only Banner file anywhere is `Banner A_R 8-27-25.XLSX` loose at Drive root.

---

## Known limits of this brief

- Duplication claims rest on folder byte-totals, not content hashes.
- No permission audit was run on any surface.
- `External/` listing is truncated — `read_resource` caps at ~200 children with no pagination; enumeration stopped alphabetically at `Steiner Photos`. An unknown number of children sorting after "S" remain unlisted.
- Sensitivity categories are inferred from file and folder names. No file contents were opened.
- Shared Drive membership on the Google side cannot be enumerated; three is a floor.
- 22 mounts under Dropbox `Austin Berk` were not descended.
- Two surveys were still running when this was written: Austin's OneDrive, and `Claude Cowork/Corporate` (19.04 GB).
