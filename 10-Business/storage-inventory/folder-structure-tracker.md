# Folder Structure Tracker_Outline.xlsx: Full Read

**What this is:** The 2023 SharePoint design spec Austin authored, covering 12 departments, a 9-deep tree, and 79 file-naming conventions. The original intent behind the target structure.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

Read: 2026-08-26 | Source: root of Austin Berk's OneDrive, drive `b!T7oszY-3i0Wfg90hKVyzahK7n5ePxOxCk5Gda5Ku67vHoXSaMjFlQ7UBj3E2R9-m`, item `015MWN5VJWC4BXXDZTGVA3HHBDERMXTJI4`, 258,028 bytes
Local sync copy used for the complete read: `C:\Users\AustinBerk\OneDrive - Parakeet Communities\Folder Structure Tracker_Outline.xlsx` (byte-identical size, mtime 2023-09-20)

## Coverage: VERIFIED, 100%

The Graph `read_resource` conversion **truncated** at ~5,651 of 6,051 rows of Sheet1 and never reached Sheet2 ("[Output truncated — 400 more rows in this sheet and any later sheets not shown]"). It offers no `startPage` continuation for xlsx. Coverage was therefore closed by opening the **locally synced identical copy** as a zip archive and parsing `xl/worksheets/sheet1.xml`, `sheet2.xml`, `sharedStrings.xml`, and `docProps/*` directly (read-only; nothing modified, moved, or renamed).

Result: **every populated cell of both worksheets was read.** Sheet1 dimension `A5:M6055`, 4,717 non-empty rows, 2,323 folder cells + 2,389 filename cells + 54 status cells + 7 note cells. Sheet2 dimension `A4:AV11`, 8 rows, all read. Shared string table: all 324 entries resolved. No hidden sheets, no comments/threaded comments, no defined names, no formulas anywhere in the workbook.

**Corrections to the prior survey (all VERIFIED):** it is a **9-level** taxonomy (folder columns A to I), not 12. The 13 columns are 9 folder levels + status + filename + note. There are **224** level-4 folder cells, not 748. There are **2,389** filename-convention cells but only **79 distinct conventions**, not 2,180. There are **45** named communities in Sheet1 (46 blocks counting the blank template), not 42.

## Summary

This is a **design spec, not a build tracker**, with one small, abandoned exception. Austin authored it over three days in September 2023 as a top-to-bottom map of what the Parakeet SharePoint file structure should look like: 12 departments, a 9-deep folder tree, and a file-naming convention attached to most leaf folders. The property side is a single 97-node subtree stamped out 46 times, once per community plus a blank template.

Implementation status **is** tracked. A four-value dropdown (`In Folder / Need / Draft Only / Not Applicable`) sits in column K of Sheet1 and across all of Sheet2. It was filled in for almost nothing and then dropped. **54 status cells exist on Sheet1 out of ~2,400 possible slots (2.2%), covering 3 of 45 communities.** Sheet2 is a second, incompatible attempt at the same tracking (a community-by-document matrix) that got **12 cells filled out of 276 (4.3%)** before being abandoned. Both attempts stop alphabetically at "Applegate", the third community. Whoever started auditing quit within the first hour.

For Birdcage the practical read is: **the taxonomy is complete and buildable; the status tracking is worthless and should be discarded.** Nothing in this document tells you what exists today. The live-library check has to be done fresh.

## 1. Worksheets: VERIFIED

Two sheets, both named with Excel defaults (`Sheet1`, `Sheet2`), never titled.

| Sheet | Dimension | Content |
|---|---|---|
| **Sheet1** | `A5:M6055`, 6,051 rows × 13 cols | The taxonomy. Columns A to I = folder nesting levels 1 to 9 (indentation by column). Column J = unused. Column K = implementation status dropdown (54 cells). Column L = filename convention for the enclosing folder (2,389 cells). Column M = free-text notes (7 cells). |
| **Sheet2** | `A4:AV11`, 8 rows × 48 cols | An abandoned per-community document-status matrix. Row 4 = 46 community names across C4:AV4. A5 = the single section label `FORMATION DOCUMENTS`. B6:B11 = 6 document names. C:AV = status dropdown cells, of which **12 are filled**. |

Sheet2 in full (VERIFIED, this is the entire sheet):

```
A5 = FORMATION DOCUMENTS
Row 4 (C..AV): American | Apple Creek MHC | Applegate MHC | Applegate Utility | Bay Oaks Village I |
  Bay Oaks Village II | Cambridge | Carley's Mobile Home Park | Central Mobile Home Park |
  Congress Mobile Home Park | Countryside MHC | Crystal Acres | Everglades Mobile Home Park |
  Geiger Key | Gulf Breeze MHP | Harbour Mobile Home Park | Hunter Springs MHC | J Bar J Estates |
  Lake Saunders | Lake Wales MHC | Lamberton Lake MHC | Lucky Clover | Mayflower Hills |
  Meadow Woods Mobile Home Park | Monson | Oceanaire MHC | Ormond Beach Oasis | Palm Haven Estates |
  Palm Spring Estates | Paradise Lakes | Parktown MHC | River Oaks RV Resort | Royal Oaks MHC |
  Royal Palm Trailer Park | Sea Shells Manufactured Housing Community | Shady Oaks MHP |
  Silver Breeze | Southgate | Town & Country MHC | Tradewinds MHC | Triple S Marina |
  Vantage Oaks | Westwood MHP | Whispering Pines | Whispering Pines MH |
  Wolf Bay Manufactured Housing Community

                                       C:American   E:Applegate MHC   F:Applegate Utility
B6  Property Name_Certificate of Formation      In Folder    Need              In Folder
B7  Property Name_EIN Letter                    In Folder    In Folder         —
B8  Property Name_Certificate of Good Standing  In Folder    Need              —
B9  Property Name_LLC Agreement                 Draft Only   Need              —
B10 Property Name_LLC Agreement_A&R             —            In Folder         —
B11 Property Name_State Registration            In Folder    In Folder         —
```

Every other cell on Sheet2 is empty. Column D (Apple Creek) and columns G to AV (41 communities) are untouched.

## 2. Implementation status: YES, tracked; effectively unused. VERIFIED

**Mechanism.** A data-validation dropdown, identical on both sheets, with exactly four options:

> `"In Folder,Need,Draft Only,Not Applicable"`

On Sheet2 it is applied to `sqref="C6:C11 E10:F11 E6:F7 E8:E9"`, i.e. only the three columns actually used, not the full 46-column grid. That is itself evidence the matrix was hand-extended cell by cell and never rolled out.

**Sheet1 counts (VERIFIED, exhaustive):** 54 status cells total, all between rows 204 and 629.

| Value | Count |
|---|---|
| Need | 25 |
| In Folder | 24 |
| Not Applicable | 3 |
| Draft Only | 2 |
| **Total** | **54** |

Distribution by block:

| Block | Rows | Status cells |
|---|---|---|
| `PROPERTIES/_ADMINISTRATIVE` | 203 to 207 | 4 |
| `AMERICAN (AUBURN, MA)` | 332 to 465 | 23 |
| `APPLE CREEK (BISMARCK, ND)` | 466 to 592 | 10 (all `Need`) |
| `APPLEGATE (DELAND, FL)` | 593 to 724 | 17 |
| All other 42 communities | 725 to 6055 | **0** |
| All 11 non-PROPERTIES departments | 5 to 201 | **0** |

**Against the counts asked for:**

- **Level-4 folders "marked done": 0 of 224.** No status cell is attached to a level-4 folder anywhere. Statuses attach to filename rows (col L) and to three level-6 folders. (VERIFIED)
- **Community subtrees marked done: 0 of 45.** Three communities are *partially* audited (American, Apple Creek, Applegate). Not one is complete. American, the most-worked, has 23 statuses against 102 trackable nodes. (VERIFIED)
- Sheet2: **12 filled of 276 possible** (6 documents × 46 communities), covering 3 columns. (VERIFIED)

**INFERRED:** the audit was attempted twice, once inline on Sheet1 and once as a matrix on Sheet2. Both times it was abandoned at the same alphabetical point. The two attempts do not agree with each other (see Gaps).

## 3. The 12 departments: VERIFIED, verbatim

Level 1 is the single root `PARAKEET COMMUNITIES` (A5). The 12 level-2 departments, in sheet order:

| # | Name (verbatim) | Row |
|---|---|---|
| 1 | `ACCOUNTING & FINANCE` | 6 |
| 2 | `ADMINISTRATIVE` | 54 |
| 3 | `ANALYTICS & REPORTING` | 65 |
| 4 | `COMPANY DOCUMENTS` | 112 |
| 5 | `CORPORATE` | 135 |
| 6 | `HUMAN RESOURCES` | 144 |
| 7 | `INVESTOR RELATIONS` | 155 |
| 8 | `JADIAN-PARAKEET` | 157 |
| 9 | `MARKET DATA` | 159 |
| 10 | `MARKETING` | 162 |
| 11 | `PARAKEET HOMES` | 183 |
| 12 | `PROPERTIES` | 202 |

Depth is wildly uneven: `PROPERTIES` occupies rows 202 to 6055 (97% of the sheet); `INVESTOR RELATIONS` and `JADIAN-PARAKEET` are **bare department names with no children at all**. Folder nodes by level: L1=1, L2=12, L3=91, L4=224, L5=799, L6=828, L7=92, L8=138, L9=138. That is **2,323 folder nodes total**, of which 2,210 are inside `PROPERTIES`.

## 4. The standard community subtree: VERIFIED

`PROPERTIES` contains `_ADMINISTRATIVE` (4 tracking grids), one blank template block `PROPERTY NAME (CITY, STATE)`, and 45 named community blocks. **43 of the 45 named blocks are byte-for-byte identical** in structure and filename conventions; `AMERICAN` and `APPLEGATE` carry local additions. The blank template is *out of date*: it is the only block missing `LOAN DOCUMENTS`.

This is the canonical pattern (reproduced verbatim from `APPLE CREEK (BISMARCK, ND)`, rows 466 to 592, the exact structure shared by 43 communities). Indented lines prefixed `→` are filename conventions attached to that folder, not subfolders.

```
{PROPERTY NAME (CITY, STATE)}/
├── ASSET MANAGEMENT/
│   ├── CLOSING DOCUMENTS/
│   │   ├── CLOSING BINDER/
│   │   │   → Property Name_Closing Binder
│   │   ├── CLOSING RECON/
│   │   │   └── PRORATIONS/
│   │   │       → Property Name_Closing Reconciliation
│   │   │       → Property Name_Final Settlement Statement
│   │   │       → Property Name_Final Proforma
│   │   ├── RENT MANAGER IMPORT/
│   │   │   → Property Name_Property Import
│   │   │   → Property Name_Unit Import
│   │   │   → Property Name_Resident Import
│   │   │   → Property Name_Beginning Balance Import
│   │   │   → Property Name_Recurring Charge Import
│   │   ├── LOAN DOCUMENTS/
│   │   └── OTHER/
│   └── DUE DILIGENCE FILES/
│       └── TRANSFER OF ACQUISITIONS FOLDER/
├── INSURANCE/
│   ├── POLICY/
│   │   → Property Name_Insurance Company_Policy Number_Start Date - End Date   (×2)
│   ├── CLAIMS/
│   └── INSPECTIONS & RESPONSES/
├── LEGAL/
│   ├── FORMATION DOCUMENTS/
│   │   → Property Name_Articles of Organization
│   │   → Property Name_EIN Letter
│   │   → Property Name_W-9_202X
│   ├── LICENSE & PERMITS/
│   │   ├── OPERATING PERMIT/
│   │   │   → Property Name_Operating Permit_09302022
│   │   │   → Property Name_Operating Permit_09302023
│   │   ├── BUSINESS TAX RECEIPTS/
│   │   ├── UTILITY PERMITS/
│   │   └── LLC ANNUAL REPORTS/
│   ├── INSPECTIONS / VIOLATIONS/
│   │   → Property Name_Violation/Inspection_Reference Number_Notice_Date
│   │   → Property Name_Violation/Inspection_Reference Number_Response_Date
│   ├── PROSPECTUS/
│   │   → Property Name_Prospectus_Version X_Date
│   │   → Property Name_DBPR Approval Letter_Version X_Date
│   └── LEASE & RULES/
│       → Property Name_Lot Rent Lease_As Of MMYYYY
│       → Property Name_Rental Lease_As Of MMYYYY
│       → Property Name_Rules & Regs_As Of MMYYYY
└── OPERATIONS/
    ├── COMMUNICATIONS/
    │   ├── RENT INCREASE NOTICES/
    │   │   → Property Name_Rent Increase_Effective MMYYYY   (×2)
    │   └── COMMUNITY EVENTS/
    │       → Property Name_Name of Event_Date Sent
    ├── CONTRACTS/
    │   └── VENDOR/
    │       → Property Name_Vendor_Contract Type_Contract_Date of Contract   (×2)
    ├── FORMS & TEMPLATES/
    │   → Property Name_Lot Rent Lease_As Of MMYYYY
    │   → Property Name_Rental Lease_As Of MMYYYY
    │   → Property Name_Rules & Regs_As Of MMYYYY
    │   → Property Name_Violation Notice
    │   → Property Name_Site Improvement Request
    ├── SITE VISTS & INSPECTIONS/        [sic — "VISTS"]
    ├── MAPS/
    │   → Property Name_Survey_As Of_MMYYYY
    │   → Property Name_Marketing Map_As Of_MMYYYY
    │   → Property Name_(Utility Type)_Utility Map_As Of_MMYYYY
    ├── COMMUNITY PHOTOS & VIDEOS/
    │   ├── PHOTOS/
    │   │   → Property Name_Description_Date
    │   └── VIDEOS/
    │       → Property Name_Description_Date
    │       → Property Name_Monthly 360 Video_Date
    └── FACILITIES/
        ├── PROJECTS & SERVICE ORDERS/
        │   └── {PROJECT NAME}/
        │       → Property Name_Project Name_Financial Tracker
        │       ├── SOW/
        │       │   → Property Name_Project Name_Scope of Work_Date
        │       ├── BIDS/
        │       │   → Property Name_Project Name_Vendor_Date   (×3)
        │       └── PHOTOS/
        │           ├── BEFORE/
        │           │   → Property Name_Project Name_Before Photos_Date   (×2)
        │           ├── Progress/          [sic — title case, unlike siblings]
        │           │   → Property Name_Project Name_Progress Photos_Date   (×2)
        │           └── Completion/        [sic — title case]
        │               → Property Name_Project Name_Completed Photos_Date   (×2)
        ├── MAINTENANCE LOG/
        └── WATER TESTING/
            → Property Name_Water Testing Results_Date
```

Per-community shape: **4 level-4 folders** (`ASSET MANAGEMENT`, `INSURANCE`, `LEGAL`, `OPERATIONS`), 17 level-5, 18 level-6, 2 level-7, 3 level-8, 3 level-9 = **47 folders and 50 filename conventions per community**.

**The 45 named communities** (verbatim, Sheet1 col C order): AMERICAN (AUBURN, MA) · APPLE CREEK (BISMARCK, ND) · APPLEGATE (DELAND, FL) · BAY OAKS VILLAGE I & II (PANAMA CITY, FL) · CAMBRIDGE (CHARLES TOWN, WV) · CARLEY'S (MIAMI, FL) · CENTRAL (COCOA, FL) · CONGRESS (W. PALM BEACH, FL) · COUNTRYSIDE (MANDAN, ND) · CRYSTAL ACRES (CRYSTAL RIVER, FL) · EVERGLADES (CLEWISTON, FL) · GEIGER KEY (KEY WEST, FL) · GULF BREEZE (HUDSON, FL) · HARBOUR (COCOA, FL) · HUNTER SPRINGS (CRYSTAL RIVER, FL) · J BAR J ESTATES (MIAMI, FL) · LAKE SAUNDERS (MT DORA, FL) · LAKE WALES (LAKE WALES, FL) · LAMBERTON LAKE (GRAND RAPIDS, MI) · LUCK CLOVER (MELBOURNE, FL) · MAYFLOWER (PLYMOUTH, MA) · MEADOW WOODS (LUXEMBOURG, MA) · MONSON (MONSON, MA) · OCEANAIRE (NEW SMYRNA BEACH, FL) · ORMOND BEACH OASIS (ORMOND BEACH, FL) · PALM HAVEN ESTATES (PANAMA CITY, FL) · PALM SPRING ESTATES (TARPOON SPRINGS, FL) · PARADISE LAKES (DELTONA, FL) · PARKTOWN (MANDAN, ND) · RIVER OAKS (RUSKIN, FL) · RIVIERA (MIAMI GARDENS, FL) · ROYAL OAKS (VERO BEACH, FL) · ROYAL PALM (CLEWISTON, FL) · SEA SHELLS (CAPE CANAVARAL, FL) · SHADY OAKS (MIAMI, FL) · SILVER BREEZE (TITUSVILLE, FL) · SOUTHGATE (CAPE CANAVERAL, FL) · TOWN & COUNTRY (JACKSONVILLE, FL) · TRADEWINDS (COCOA, FL) · TRIPLE S MARINA (ATLANTIC BEACH, NC) · VANTAGE OAKS (OKEECHOBEE, FL) · WESTWOOD (ORMOND BEACH, FL) · WHIPSERING PINES ESTATES (AUBURN, MA) *[sic]* · WHISPERING PINES MH & RV RESORT (TITUSVILLE, FL) · WOLF BAY (ELBERTA, AL)

**The two non-conforming blocks (VERIFIED):**

- `AMERICAN (AUBURN, MA)` replaces `Property Name_Articles of Organization` with four conventions (`Certificate of Formation`, `Certificate of Good Standing`, `LLC Agreement`, `State Registration`), moves `Property Name_W-9_202X` up under `OPERATIONS`, and adds `Property Name_Lot Measurements_MMYYYY` under `MAPS`.
- `APPLEGATE (DELAND, FL)` adds a level-6 `DBPR ANNUAL FEES` folder under `LICENSE & PERMITS`, adds `LLC Agreement` and `State Registration` conventions, and replaces the two generic operating-permit names with Florida-specific ones: `Property Name_DOH Operating Permit_Permit Number_ Exp09302022` / `..._ Exp09302023` (note the stray space after the underscore, in both).

`PROPERTIES/_ADMINISTRATIVE` (rows 203 to 207) holds four cross-property tracking files, all marked `Need`: `LLC Renewal Grid`, `Permit Grid`, `License Grid`, `Rent Increase Grid`.

## 5. Filename conventions: VERIFIED

**Form.** Underscore-delimited positional tokens, left to right from most general to most specific, ending in a date token. Placeholders are written as literal English words to be substituted: `Property Name`, `Vendor`, `Bank Name`, `Project Name`, `Shortname - Unit`. Date tokens are spelled as format masks: `MMYYYY`, `MMDDYYYY`, `YYYY`, `QQYYYY`, `202X`, or the phrase `As Of MMYYYY` / `Effective MMYYYY` / `Date`. **No file extensions are ever specified, and no general rule is written down anywhere in the workbook**. The convention is expressed only by example. That is an INFERRED rule read off 79 examples, not a stated one.

**Volume.** 2,389 convention cells, but only **79 distinct strings**. The property-side ones repeat once per community block (×46 or ×92 where a folder shows two sample files).

Representative examples, verbatim:

1. `Bank Name_Property Name_Bank Statement_MMYYYY`
2. `Property Name_Lender Name_QQYYYY_Financial Report`
3. `Property Name_Insurance Company_Policy Number_Start Date - End Date`
4. `Property Name_Violation/Inspection_Reference Number_Notice_Date`
5. `Property Name_Vendor_Contract Type_Contract_Date of Contract`
6. `Property Name_(Utility Type)_Utility Map_As Of_MMYYYY`
7. `Property Name_Project Name_Before Photos_Date`
8. `Shortname - Unit_Bill of Sale_Date of Transaction`
9. `Parakeet - Jadian Quarterly Valuation Workbook_MMYYYY`
10. `Meeting Name_Agenda_MMDDYYYY`

Two real-world instantiations appear in the notes column, and they confirm how the masks resolve: `American_Ryan Specialty_Inspection Letter_CPS7564987_09192022` and `American_Fire Department_Oil Appication_012023` *[sic]*. Note the first is 5 tokens where the folder's stated convention was 4; the second misspells "Application".

## 6. Provenance: VERIFIED

| Field | Value |
|---|---|
| `dc:creator` | **Austin Berk** |
| `cp:lastModifiedBy` | **Austin Berk** |
| Created | **2023-09-18T19:51:39Z** |
| Last modified | **2023-09-21T01:36:25Z** |
| Authored from | `https://parakeetcommunities-my.sharepoint.com/personal/austin_parakeetcommunities_com/Documents/` (his own OneDrive root) |
| Revision pointer | `revIDLastSave="0"`, `uidLastSave` all zeros, so **no co-authoring revision history retained** |
| App | Excel 16.0300, `coauthVersionMax=47` |

**Three days of work, one author, never touched again in ~3 years.** No approval column, no sign-off row, no reviewer names, no version number, no changelog, no README tab. **Nothing in the file indicates it was ever ratified.** (VERIFIED, absence confirmed across both sheets, all doc properties, and the shared-string table.)

There is a **second, larger copy** at `C:\Users\AustinBerk\OneDrive - Parakeet Communities\Microsoft Teams Chat Files\Folder Structure Tracker_Outline.xlsx`, 280,569 bytes, dated **2023-09-18** (SINGLE-SOURCE: local file metadata; contents not opened). Being in `Microsoft Teams Chat Files` means it was **shared into a Teams chat**. INFERRED that this was circulated for comment. Larger and older than the root copy, so it likely differs; worth diffing if the ratification question matters.

## 7. Gaps and contradictions: VERIFIED unless noted

1. **Two incompatible status systems.** Sheet1 tracks status inline per filename row; Sheet2 tracks it as a community × document matrix. Neither references the other, and **they disagree on the underlying document list**. Sheet1's `LEGAL/FORMATION DOCUMENTS` for a standard community specifies `Articles of Organization`, `EIN Letter`, `W-9_202X`. Sheet2's `FORMATION DOCUMENTS` rows are `Certificate of Formation`, `EIN Letter`, `Certificate of Good Standing`, `LLC Agreement`, `LLC Agreement_A&R`, `State Registration`. Only `EIN Letter` is common to both.
2. **The community lists don't match.** Sheet1 has 45 named communities; Sheet2 has 46 column headers. Sheet2 **omits Riviera (Miami Gardens, FL)** entirely, splits `BAY OAKS VILLAGE I & II` into two columns, and adds `Applegate Utility` as a separate community. Sheet2 uses full marketing names (`Carley's Mobile Home Park`, `Sea Shells Manufactured Housing Community`); Sheet1 uses short names with city/state. **There is no shared key between the two sheets**. A rename map would have to be built by hand.
3. **The blank template is stale.** `PROPERTY NAME (CITY, STATE)` (rows 208 to 331) is missing the `ASSET MANAGEMENT/CLOSING DOCUMENTS/LOAN DOCUMENTS` folder that all 45 real communities have. Anyone provisioning a new community from the template would build it wrong. Use `APPLE CREEK` as the master, not the template.
4. **Abandoned mid-edit, twice, at the same place.** Both status passes cover American → Apple Creek → Applegate and then stop dead. 42 of 45 communities were never touched by either.
5. **Two departments are empty stubs.** `INVESTOR RELATIONS` (row 155) and `JADIAN-PARAKEET` (row 157) have no children whatsoever. `ADMINISTRATIVE` has only `CORPORATE/{MARYLAND, MIAMI}`. `MARKET DATA` has one child. These are placeholders, not specs.
6. **Hardcoded dates baked into folder specs.** `Property Name_Operating Permit_09302022` and `_09302023` appear as permanent conventions in all 45 communities, as do `PARAKEET AUDIT/{2022, 2023}` and `TAX RETURNS/{2021, 2022, 2023}`. Three years on, these are stale by design and need a year-agnostic rule.
7. **Typos that will propagate into real folder names if built literally.** `SITE VISTS & INSPECTIONS` (in all 46 blocks, so 46 misspelled folders), `WHIPSERING PINES ESTATES`, `LUCK CLOVER` (Sheet2 says `Lucky Clover`), `VIDEOMS`, `UTILTIY ANALYSIS`, `Property Management Fee Workbook_MMYYY` (5-char mask, should be `MMYYYY`), `MEADOW WOODS (LUXEMBOURG, MA)` (Luxembourg is not in Massachusetts; likely Leicester or Lunenburg), `TARPOON SPRINGS`, `CAPE CANAVARAL` in one block and `CAPE CANAVERAL` in another.
8. **Inconsistent casing.** Everything is `UPPER CASE` except `Progress` and `Completion` under `FACILITIES/.../PHOTOS`, which are Title Case, in all 46 blocks.
9. **A slash inside a folder name.** `INSPECTIONS / VIOLATIONS` is legal in SharePoint as a folder name but awkward, and the same slash appears inside the filename convention `Property Name_Violation/Inspection_...`, where it is **illegal in a SharePoint filename** and will be rejected or stripped.
10. **The four `_ADMINISTRATIVE` tracking grids never existed.** All four are marked `Need`. The LLC/permit/license/rent-increase registries the taxonomy depends on were specified and never built.
11. **No column J.** A blank spacer column sits between the folder levels and the status column, suggesting a column was deleted or reserved mid-build.

## Bottom line for Birdcage

**Buildable as-is: yes, for the folder tree.** The 12 departments, the 2,323 folder nodes, and the 47-folder community subtree are fully specified and internally consistent (43/45 communities identical). Albert can provision from `APPLE CREEK` as the master pattern with a per-community name substitution.

**Not usable as-is: the status data.** 2.2% coverage, three years stale, two mutually contradictory tracking schemes. Discard it and re-derive current state from the live library.

**Decisions Albert needs before building** (none of which this document answers): (a) fix or preserve the 9 propagating typos; (b) resolve the Sheet1 vs Sheet2 formation-document list; (c) resolve the community-name convention, short+city/state vs full marketing name, and reconcile Riviera / Bay Oaks / Applegate Utility; (d) replace the hardcoded 2022/2023 date tokens with a year rule; (e) fill or drop the two empty departments; (f) confirm whether `PROPERTIES` folders keep the 46-way duplication or move to a metadata-driven library, since 2,210 of 2,323 nodes are the same 47 folders repeated.
