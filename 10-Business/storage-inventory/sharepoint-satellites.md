# SharePoint Satellite Sites: Inventory

> **Source-state paths, 2026-08-31.** Numbered `1. …` through `8. …` community subfolders quoted on this page describe `/sites/main/Shared Documents/` **as it exists today** and are deliberately left as written. That estate is read-only (see [[CLAUDE]]). The Birdcage template is unnumbered per Austin's 2026-08-31 ruling; see [[10-Business/sharepoint/target-structure]].

**What this is:** Every SharePoint site outside `/sites/main`: the eleven satellites, what each holds, and which of them are clones of each other.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

Surveyed: 2026-08-26 | Account: Austin Berk (austin@parakeetcommunities.com) | Coverage: 11 satellite sites across 14 distinct drives, plus the tenant root site (2 libraries) and 6 personal OneDrives identified as a category. Top three levels enumerated for every satellite; deeper drilling done only where needed to settle the Bay Oaks duplication question and to characterize the prior AI pass in `Claude Cowork/Acquisitions/UW Model Engine`. `/sites/main` deliberately not indexed (owned by another agent) except where its folders are one leg of a cross-site duplicate.

## Summary

The satellite estate is not a set of purpose-built team sites. It is a graveyard of partial migrations, with one glaring exception: a substantial, disciplined prior AI/automation pass over this same corpus already exists at `/sites/ParakeetBirdcage/Data  Analytics/Claude Cowork` (23.07 GB), and its `Acquisitions/UW Model Engine` project has already produced a 63-deal dossier fleet, a 96-deal knowledge base, and a validated underwriting engine. This should be salvaged, not redone (Finding 4). Eleven satellite sites exist beyond `/sites/main`; four of them (`Operations95`, `ParakeetOperations9-Amsterdam-General`, and both root-site libraries) are effectively empty shells, and a fifth (`LegalParakeet`) has been superseded in place by `Corporate-Legal` without being retired. The Bay Oaks Village I site plans are not duplicated four ways in any meaningful sense. Three of the four are **byte-for-byte identical clones** created in a three-day copy chain on 2026-02-02/03/05, and the fourth is a different document set entirely. That clone pattern is not specific to Bay Oaks: it covers **22 of 23 shared communities** across three separate Site Plans trees, roughly **16.6 GB of pure redundancy**, and a *fifth*, genuinely divergent Site Plans tree on `/sites/ParakeetHome` makes the "which site plan is current" question unanswerable from folder structure alone. The single biggest problem is that Parakeet has two sites whose names differ by one letter, `/sites/ParakeetHome` and `/sites/ParakeetHomes`, holding overlapping-but-different copies of the same construction drawings, and nothing in either site tells a user which one to trust.

## Taxonomy

Sizes are Graph-reported folder byte totals. `(0)` means the folder reports zero bytes, created but never filled.

```
parakeetcommunities.sharepoint.com
│
├── /sites/ParakeetHomes                        drive b!SCgEpP1GtEiYW9ZsBo1oxu0rZVmA6j5JjJsNlEWKw6Gr64r96F0TTZ6LQNwO5t4d
│   └── Shared Documents/                       5 top-level folders, 4 of them empty
│       ├── Files (0)                           Teams-created shell
│       ├── General (0)                         Teams-created shell
│       ├── Home Inventory (0)                  shell
│       ├── Infill Budget and Plan (0)          shell
│       └── Property and Site Data  9.44 GB     ← the ONLY live content on this site
│           └── Site Plans  9,443,687,497 B     24 communities  [CANONICAL site-plan library]
│
├── /sites/ParakeetHomes-ParakeetHomesxCavco    drive b!UJGcv16GCEyZ2B2zVaAckFFHex8i39lDjkYHQ4uC28wDJUD0uaIiTLo2uTHm2SRX
│   └── Shared Documents/                       1 top-level folder, nothing else
│       └── Site Plans  8,296,062,918 B         23 communities  [CLONE of the above, minus Druid Oaks]
│                                               Teams shared/private-channel site hung off ParakeetHomes
│
├── /sites/UserArchive                          drive b!qHBXoArJC02i9Yhsdl67dnN4d672gABKv8icn4E2ZuQIJxa4wJb7T78d59vyS9yT
│   └── Shared Documents/General  268.6 GB      93 top-level folders (92 person archives + 1 eDiscovery)
│                                               see "UserArchive roster" below
│
├── /sites/ParakeetHome  (SINGULAR, not a typo) drive b!gf2Ko5H70UixbFcr7LrmO_uFB7ZwrpZKn1tUZaKMmsTGQWhOArzeQY9GXz5Bn7OT
│   └── Shared Documents/                       13 folders + 7 loose root files
│       ├── Parakeet Homes            15.94 GB  incl. Site Plans (29 communities), Home Information
│       ├── Company Documents          2.69 GB
│       ├── Legal                      1.74 GB  Formation Documents 584.8 MB, Property Closing Binders 583.0 MB,
│       │                                       License & Permits Annual Reports 246.8 MB, Property Prospectus 301.0 MB,
│       │                                       Property Management Agreements 23.7 MB
│       ├── Accounting                 1.35 GB
│       ├── Reporting                392.9 MB
│       ├── Marketing                211.1 MB
│       ├── Asset Managment [sic]     37.6 MB
│       ├── Operations                11.9 MB
│       ├── Claude Homes             665.8 KB
│       ├── Processes                301.0 KB
│       ├── _PrettyBird               66.4 KB
│       ├── Acquisitions (0)
│       └── Human Resources (0)
│       loose root files: folder_structure.csv, FolderStructure.csv, FolderStructure.txt,
│                        Full Addresses.xlsx, Structure Thoughts.xlsx, + 2 PDFs
│                        (three near-identical folder-structure dumps, 400 to 471 KB each)
│
├── /sites/ParakeetBirdcage                     THREE separate document libraries = three drives
│   ├── Property Operations   drive b!xyOQz3MDX0KO4DwwD8HVIt10RnZ14ehEpxBSsCZX7QBp6sE8EakWRaQRyC-NaaAT
│   │   └── 74 "Community (City, ST)" folders + Regional Breakdown_062026.xlsx
│   │       Only 8 hold data: American (Auburn, MA) 10.12 GB, Applegate 261.6 MB,
│   │       Carleys 10.29 MB, Bay Oaks Village I & II 10.48 MB, Crystal Acres 12.08 MB,
│   │       Central 9.50 MB, Brunswick Estates 2.85 MB, Auburn Ridge 1.31 MB.
│   │       The other 66 report 0 bytes: a scaffold built, then abandoned (created 2026-06-11/15).
│   │       Per-community subtree is uniform: Communications / Construction / Insurance /
│   │       Legal / Operations (+ Operations/Incident Reports)
│   ├── Marketing             drive b!xyOQz3MDX0KO4DwwD8HVIt10RnZ14ehEpxBSsCZX7QC5gGBF35NHTbxHKrsEpMnH
│   │   └── Community Photos 1.45 GB, Community Notices/Flyers/Forms 579.2 MB,
│   │       Brand Assets 108.8 MB, Apparel 54.0 MB, Digital Marketing (0),
│   │       Photography (0), Print Marketing (0)
│   └── Data  Analytics       drive b!xyOQz3MDX0KO4DwwD8HVIt10RnZ14ehEpxBSsCZX7QBJfg0Odv_GQ7Z2fmJye92a
│       ├── Claude Cowork 23.07 GB   ← largest single satellite folder in the tenant;
│       │   │                          the PRIOR AI/automation pass over this corpus
│       │   ├── Corporate            19.04 GB  (Parakeet OS, Asset Listing Work, Core+ Fee Research)
│       │   ├── Acquisitions          2.51 GB  ← contains UW Model Engine (see Finding 4)
│       │   ├── Sales-Marketing       1.29 GB  (SAM Umbrella, Community Marketing Reports,
│       │   │                                   New Home Purchase Data Entry)
│       │   ├── Construction         90.60 MB
│       │   ├── Infill               89.84 MB  (Infill Tracker)
│       │   ├── Market-Intelligence  53.84 MB  (2BR Rents Analysis - ZORI)
│       │   ├── Operations            6.06 MB
│       │   ├── Scheduled               999 B
│       │   ├── Accounting-Finance (0)
│       │   ├── Asset-Management (0)
│       │   └── Asset_Inventory_Dashboard_2026.08.05.html (1.92 MB), dummy_test2.html (6 B)
│       ├── Rent Manager 91.0 MB, DataWarehouse Feeds 52.4 MB, ARAP 23.4 MB,
│       │   3rdPartyInfoforInfill 3.2 MB, QuickBase, Jotform, Appenate, Dashboards
│       └── 21 root files incl. 17 dated "SharePoint Audit Report - YYYY-MM-DD.docx"
│           (2026-06-05 → 2026-08-25); someone is already auditing this estate weekly
│
│       Claude Cowork / Acquisitions / UW Model Engine
│         item 01MYSBHX5U2O3L6KNSLJHJMLBKPTBX3FF5 · folder stamp 2026-07-03T03:42:00Z
│         (live work continues inside to 2026-08-06)
│         ├── batch          1,686,801,472 B   the deal corpus (see below)
│         │   ├── process    1,642,627,968 B   63 deal-process dossiers + email/PST indexes
│         │   │   ├── pst_full_index   1,119,243,650 B
│         │   │   ├── email archive      520,430,167 B
│         │   │   ├── _mobile_drafts        439,800 B
│         │   │   └── archive               414,778 B
│         │   ├── email drafts   42,432,262 B   incl. the 225-question review emails
│         │   ├── kb                593,084 B   96 per-deal .md KBs + INDEX.md
│         │   └── scout            573,364 B   DD-folder scout / 3-era taxonomy
│         ├── logic review   13,754,888 B   BL_REVIEW_PROTOCOL.md + tieout/ (10 harnesses)
│         ├── archive         3,866,044 B
│         ├── brand           3,649,604 B
│         ├── dissection      3,340,779 B   McGregor model teardown
│         ├── engine            206,023 B   the code parser/evaluator port
│         └── 45 root files: 34 .xlsm (2 McGregor "FIXED" + 32 template versions,
│             Template Base v0.1 → TEMPLATE v1.21), Roadmap & Completion Status.docx,
│             Model Spec & Break Audit - McGregor Downs.md (91 KB),
│             Grid Documentation (draft).md (104 KB), Removal Registry.md (324 KB),
│             Tax Truth File.xlsx + NOTES.md, MHP Sales Comps Database.xlsx,
│             Template Tie-Out SMOKE TEST, Port Validation Report.md,
│             Parakeet UW Model_2026.07.03.1.html
│
├── /sites/Corporate-Legal                      drive b!z8isIDeogE-XNOg5C8Vv-FYKR_9EJIFOrONtcrVbgnMgYy4ah1O2RJpHXpKtl__q
│   └── Shared Documents/
│       ├── Formation Documents          391.0 MB   141 entity folders  [CANONICAL entity library]
│       ├── Property Closing Binders      60.6 MB
│       ├── Property Management Agreements 9.6 MB
│       └── governance files: _Missing Documents Report.xlsx, _Special Cases Log.xlsx,
│                             LLC Entities.csv, Master Entity Database.xlsx,
│                             Parakeet Communities - Org Chart.html
│
├── /sites/LegalParakeet                        drive b!WLFJMZw5jEWdDRCDAQHmW_uFB7ZwrpZKn1tUZaKMmsTGQWhOArzeQY9GXz5Bn7OT
│   └── Shared Documents/                       [SUPERSEDED by Corporate-Legal, never retired]
│       ├── Property Level Formation Documents 255.6 MB
│       ├── Corporate Level Formation Documents 25.6 MB
│       ├── Closing Documents (0)
│       ├── Property Management Agreements (0)
│       └── Document Project Tracking.xlsx
│
├── /sites/SouthernaireNorthRidge               drive b!28u0_WlNykq2V4E7V4p-fg7dzXGOcKlMqh7qw0V3L79bUFKI-ruoQaEX9C6U9nin
│   └── Shared Documents/                       single-deal data room, 10 folders
│       Underwriting 172.9 MB, Third Party Reports 29.9 MB, Buyer DD 24.0 MB,
│       Seller DD 15.4 MB, Insurance 2.2 MB, Contract 1.4 MB, Closing 304 KB,
│       Financing - Debt 145 KB, General 12 KB, Milestone Reports (0)
│
├── /sites/ParakeetOriginsAcquisition           drive b!_e2bKFXeFU28qob3gxcXRO0rZVmA6j5JjJsNlEWKw6Gr64r96F0TTZ6LQNwO5t4d
│   └── Origins Acquisition - General 2.17 MB, Microsoft Planner 26 KB, Whiteboards 18 KB
│
├── /sites/ParakeetOperations9-Amsterdam-General drive b!n-NT_CQsI0-88RGNLdctM1YKR_9EJIFOrONtcrVbgnMgYy4ah1O2RJpHXpKtl__q
│   └── Amsterdam - General (0)                 EMPTY, one folder, zero bytes
│
├── /sites/Operations95                         drive b!3VqZr7scN0qVlKW0iJk9YO0rZVmA6j5JjJsNlEWKw6Gr64r96F0TTZ6LQNwO5t4d
│   └── Shared Documents/                       156,703 bytes total, three spreadsheets
│       ├── Files/Reporting/  Aged Receivables.xlsx (88,010 B),
│       │                     Prospect Stage Listing.xlsx (50,166 B),
│       │                     Property Buckets.xlsx (18,527 B)
│       ├── Files/Property A (0)
│       ├── Files/Winward Knoll (0)
│       └── Postings (0)
│
└── Tenant root site  https://parakeetcommunities.sharepoint.com   (2 libraries)
    ├── /Shared Documents      drive b!mw84v0UggEyK-YyZ--L4u3T9XaUeoxROphyAcWNiHblytj6xHyirT4KAQ8FiLEku
    │   └── Formation Documents 678 KB  ← a THIRD formation-docs stub
    │       Current projects (0), Marketing assets (0), Newsletters (0),
    │       Onboarding (0), Presentations (0)   (5 of 6 folders empty)
    └── /Document Library      drive b!mw84v0UggEyK-YyZ--L4u3T9XaUeoxROphyAcWNiHbnjD--bMj-hSYTg-GIdylHE
        └── _Old/Education/...  legacy training material (MHU home-study course, 2008 files)

PERSONAL ONEDRIVES  (category; surfaced in search, deliberately not indexed)
  austin@   b!T7oszY-3i0Wfg90hKVyzahK7n5ePxOxCk5Gda5Ku67vHoXSaMjFlQ7UBj3E2R9-m
  jclark@   b!BzFMO7Uv70GR0Gc-d2eN1TjriAeQtW1ItP-lN2WgZKAee9h9ZFUpTJyaxDpm0Akr
  natalie@  b!Fcb4EbyWWEeks4KF6OqLAv52q1LaAGZMpWxiyolr3erUoNGej_d0SJFFj-H78C3t
  demetria@ b!vWv9hU0yhEiQIlZGMIS6UMTuKscBEz9JouWYuD8tbi9UWgY6cXOjSb5c8vN0oYLY
  jon@      b!dvIAl0KRAUqjP0PSixUJPRK7n5ePxOxCk5Gda5Ku67vHoXSaMjFlQ7UBj3E2R9-m
  dflynn@   b!DUjPCMI7j0iQW_bTSE2g9QvFyITJMY5Jmf1eQ0Ka99LZgS3njN6yQosueZhWyXLb
```

## Authoritative locations

| Document set | Canonical path | Competing copies |
|---|---|---|
| Community site plans (drawings by lot) | `/sites/ParakeetHomes/Shared Documents/Property and Site Data/Site Plans`: 24 communities, 9,443,687,497 B, the only complete set | (a) `/sites/ParakeetHomes-ParakeetHomesxCavco/Shared Documents/Site Plans`: 23 communities, byte-identical clone; (b) `/sites/main/Shared Documents/Parakeet Homes/Manufacturers/Cavco Homes/Plans for Sites`: 23 communities, byte-identical clone; (c) `/sites/ParakeetHome/Shared Documents/Parakeet Homes/Site Plans`: 29 communities, **genuinely divergent** generation, not a clone |
| Bay Oaks Village I site plans | `/sites/ParakeetHomes/.../Site Plans/Bay Oaks Village I`: 812,391,202 B, 27 lot folders, modified 2026-02-02T14:05:26Z (earliest of the three identical copies) | `…-ParakeetHomesxCavco/Shared Documents/Site Plans/Bay Oaks Village I` (2026-02-03T17:18:53Z); `/sites/main/.../Cavco Homes/Plans for Sites/Bay Oaks Village I` (2026-02-05T16:49:25Z). Both identical byte-for-byte. |
| Bay Oaks Village I construction record | `/sites/main/Shared Documents/Construction/BAY OAKS VILLAGE I`: **not a duplicate**; different document set (CONTRACTS / DEVELOPMENT 813.1 MB / MAPS / PHOTOS / PROJECTS 644.8 MB / PROPERTY INFORMATION), modified 2025-05-27T12:56:40Z | none; authoritative for its own content |
| Entity formation documents | `/sites/Corporate-Legal/Shared Documents/Formation Documents`: 391.0 MB, 141 entity folders, ships with `_Missing Documents Report.xlsx`, `_Special Cases Log.xlsx`, `Master Entity Database.xlsx` (only copy with governance artifacts) | `/sites/LegalParakeet/Shared Documents/Property Level Formation Documents` (255.6 MB) + `Corporate Level Formation Documents` (25.6 MB); `/sites/ParakeetHome/Shared Documents/Legal/Formation Documents` (584.8 MB, split into BEDROCK/ and PO/ subtrees); tenant-root `/Shared Documents/Formation Documents` (678 KB stub) |
| Property Management Agreements | `/sites/Corporate-Legal/Shared Documents/Property Management Agreements`: 9.6 MB | `/sites/ParakeetHome/Shared Documents/Legal/Property Management Agreements` (23.7 MB; larger, may hold superset); `/sites/LegalParakeet/…/Property Management Agreements` (0 bytes, empty shell) |
| Property closing binders | `/sites/ParakeetHome/Shared Documents/Legal/Property Closing Binders`: 583.0 MB | `/sites/Corporate-Legal/Shared Documents/Property Closing Binders`: 60.6 MB (about 10% the size; likely partial migration in flight) |
| Community photos | `/sites/ParakeetBirdcage/Marketing/Community Photos`: 1.45 GB | `/sites/main/Shared Documents/Marketing/Community Photos`; `/sites/main/Shared Documents/Operations/_Marketing/Community Photos`; per-property copies under `/sites/main/.../Operations/<Community>/2. Communication and Photos/…` |
| Deal history & underwriting knowledge (prior AI pass) | `/sites/ParakeetBirdcage/Data  Analytics/Claude Cowork/Acquisitions/UW Model Engine`: `batch/kb/INDEX.md` for the deal register, `batch/process/*.md` for the 63 dossiers, `Roadmap & Completion Status.docx` for build state | none; this is original work, not a copy. But it *documents* narrative duplication inside the deal models themselves (Triple S / Southgate / Riviera / Lucky Clover clone prose, tagged `do-not-quote`). See Finding 4. |
| Underwriting pro-forma template | `…/UW Model Engine/Parakeet Pro Forma - TEMPLATE v1.21 (Sample Park).xlsm` (3,956,254 B), the current head | 31 older versions in the same folder (`Template Base v0.1` → `v1.20`); `v1.10a` is the version circulated to reviewers on 2026-07-31 and is the one referenced by the business-logic review protocol |
| Departed-employee drives | `/sites/UserArchive/Shared Documents/General`: 268.6 GB, 93 folders | none; but Leslie Warden appears three times (see Finding 6) |
| Departed-employee meeting recordings | inside each `UserArchive/…/<Person>/Recordings` folder | Teams recordings also land in live personal OneDrives and in `/sites/main/Shared Documents/Harry & Lloyd/2026  RoadTrip Recordings` |

## Findings

**1. The "four-way" Bay Oaks duplication is really a three-way byte-identical clone plus one unrelated document set.**
Three of the four named paths hold exactly the same 27 lot folders (`A 3, A 5, A 7, A 13, A 15, A 16, B 3, B 4, B 5, B 8, B 10, B 12, B 13, B 14, B 16, B 18, C 7, C 9, C 13, C 17, E 3, F 3, G 4, G 6, G 8, H 3, H 5`) at exactly the same aggregate size, **812,391,202 bytes each**. Verified down to file level: lot `A 13` in all three contains `A13 Pics.pdf` (39,976,909 B) and `A13.pdf` (251,469 B), identical sizes in all three drives. Folder modification stamps form a clean copy chain: ParakeetHomes 2026-02-02T14:05:26Z → Cavco satellite 2026-02-03T17:18:53Z → main/Cavco Homes 2026-02-05T16:49:25Z. **ParakeetHomes is authoritative**. It is the source of the chain and the only one whose parent tree is complete. The fourth path, `/sites/main/Shared Documents/Construction/BAY OAKS VILLAGE I` (modified 2025-05-27T12:56:40Z), is **not a duplicate at all**: its children are `CONTRACTS`, `DEVELOPMENT` (813,102,571 B), `MAPS`, `PHOTOS` (0), `PROJECTS` (644,760,179 B), `PROPERTY INFORMATION`, the construction execution record, which contains no lot-numbered site-plan folders. Treating it as a redundant copy would destroy the only construction file for that community.

**2. The clone pattern covers 22 of 23 shared communities: roughly 16.6 GB of pure redundancy.**
Comparing all three Site Plans trees folder-by-folder:

| Community | ParakeetHomes | Cavco satellite | main /Cavco Homes/Plans for Sites |
|---|---|---|---|
| Applegate | 245,880,073 | 245,880,073 | 245,880,073 |
| Bay Oaks Village I | 812,391,202 | 812,391,202 | 812,391,202 |
| Bay Oaks Village II | 351,441,488 | 351,441,488 | 351,441,488 |
| Belle Haven | 574,010,305 | 574,010,305 | 574,010,305 |
| Central | 39,882,599 | 39,882,599 | 39,882,599 |
| **Druid Oaks** | **1,147,624,067** | *absent* | *absent* |
| Everglades | 136,631,423 | 136,631,423 | 136,631,423 |
| Gulf Breeze | 357,535,792 | 357,535,792 | 357,535,792 |
| Harbour | 73,718,803 | 73,718,803 | 73,718,803 |
| **Lake Saunders** | **112,163,077** | **112,162,565** | **112,169,221** |
| Lake Wales | 102,170,078 | 102,170,078 | 102,170,078 |
| Lucky Clover | 611,276,785 | 611,276,785 | 611,276,785 |
| Northgate | 158,622,325 | 158,622,325 | 158,622,325 |
| Ormond Beach | 738,350,953 | 738,350,953 | 738,350,953 |
| Palm Spring Estates | 57,591,523 | 57,591,523 | 57,591,523 |
| Paradise Palms | 356,001,878 | 356,001,878 | 356,001,878 |
| Riverwalk | 353,936,461 | 353,936,461 | 353,936,461 |
| Royal Palms | 59,215,285 | 59,215,285 | 59,215,285 |
| Seashells | 279,272,358 | 279,272,358 | 279,272,358 |
| Southgate | 519,881,580 | 519,881,580 | 519,881,580 |
| Sue Rene | 329,319,991 | 329,319,991 | 329,319,991 |
| The Oaks | 1,635,176,734 | 1,635,176,734 | 1,635,176,734 |
| Tradewinds | 363,381,206 | 363,381,206 | 363,381,206 |
| Winward Knoll | 28,211,511 | 28,211,511 | 28,211,511 |
| **totals** | **9,443,687,497 (24)** | **8,296,062,918 (23)** | ≈8,296,069,574 (23, summed from children) |

The arithmetic closes exactly: 9,443,687,497 − 1,147,624,067 (Druid Oaks) − 512 (the Lake Saunders delta) = 8,296,062,918. **22 of the 23 shared communities are byte-identical across all three trees.** Only Lake Saunders diverges, and only by 512 and 6,656 bytes, three slightly different snapshots of the same folder, with no way to tell which is current. Redundant volume: ≈**16.6 GB** (two extra copies of the 8.30 GB shared set).

**3. A fifth, genuinely different Site Plans tree exists on the near-identically-named `/sites/ParakeetHome` (singular).**
`/sites/ParakeetHome/Shared Documents/Parakeet Homes/Site Plans` holds **29** communities. Of the 19 that overlap with ParakeetHomes, **14 are byte-identical** (Applegate, Bay Oaks Village II, Belle Haven, Central, Druid Oaks, Gulf Breeze, Lake Wales, Ormond Beach, Palm Spring Estates, Paradise Palms, Riverwalk, Southgate, The Oaks, Winward Knoll) and **5 genuinely differ**:

| Community | ParakeetHome (singular) | ParakeetHomes (plural) | delta |
|---|---|---|---|
| Harbour | 179,088,569 | 73,718,803 | +105.4 MB on singular |
| Northgate | 378,438,714 | 158,622,325 | +219.8 MB on singular |
| Seashells | 327,329,433 | 279,272,358 | +48.1 MB on singular |
| Lucky Clover | 366,356,330 | 611,276,785 | −244.9 MB on singular |
| Everglades | 136,799,871 | 136,631,423 | −168 KB on plural |

Ten communities exist **only** on the singular site (Auburn Ridge, Crystal Acres, Great Oaks, Paradise Lakes, River Oaks, Shady Acres, Silver Breeze, Silver Hill, Vantage Oaks, Whispering Pines) and five **only** on the plural site (Bay Oaks Village I, Lake Saunders, Royal Palms, Sue Rene, Tradewinds). **Neither site is a superset of the other.** This is the most dangerous finding in the survey: two sites one letter apart, each holding drawings the other lacks, with five communities where the same-named folder contains materially different content.

**4. A prior AI/automation pass over this same corpus already exists and is far more advanced than expected. Salvage it before redoing any of it.**
`/sites/ParakeetBirdcage/Data  Analytics/Claude Cowork` (23.07 GB, drive `b!xyOQz3MDX0KO4DwwD8HVIt10RnZ14ehEpxBSsCZX7QBJfg0Odv_GQ7Z2fmJye92a`) is a ten-project workspace of prior agentic work. Its flagship, `Claude Cowork/Acquisitions/UW Model Engine` (item `01MYSBHX5U2O3L6KNSLJHJMLBKPTBX3FF5`, folder stamp 2026-07-03, live work inside through 2026-08-06), is a disciplined, governed build with its own roadmap, protocols, and audit trail. It operates under a stated invariant, *"model-is-truth; no changes to historical models ever"*, and every pass in it is described as read-only over the source corpus.

*Roadmap and current state* (from `Roadmap & Completion Status.docx`, 16,630 B, "rev 2", last updated 2026-07-05 with later step-level updates through 8/6). 21 numbered steps in two halves; the doc's own framing: *"the learning half (1–10) is complete; the building half starts at #11."*
- **Done (1 to 13):** McGregor Downs model dissected tab-by-tab (#1); break audit + Model Spec (#2); clean template minted, 44 MB → 3.8 MB, 15 core tabs, zero `#REF!` (#3); ported to a code engine: parser + evaluator, ~45 Excel functions, cyclic solver (#4); **engine validated to 100.000% on 115,152 McGregor cells** (#5); 36 Assumptions grids semantically mapped (#6); HTML model v1 shell (#7); **batch validation of 92 historical models, 2.05M cells, every diff explained** (#8); **deal knowledge base ~95 deals + MHP sales comps DB, 78 comps** (#9); **deal-process deep-dive, 64/64 dossiers + corpus synthesis, 2026-07-05** (#10); business-logic review, 10 sections + MASTER register (#11); format/color/border/formula-hygiene audits (#12); **Template Tie-Out: 42/42 eligible deals, 0 unexplained gaps, certified as v2 arithmetic ground truth (memo 2026-08-03)** (#13).
- **In progress:** #14 Template v2 build (v1.10b hygiene shipped 8/3, error census 539→0; TAX MODULE shipped v1.11; waterfall hardening v1.12, 2,057 comparisons ROUND-armored; vacancy/collections v1.13a→v1.17; rate-cap + debt instruments v1.14; infill program v1.21 on 8/6). #21 dropped-deal storylines. **#10.4 questions, "ZS pass + final ingestion pending"**. This is the single open dependency blocking closure of the learning half.
- **Ahead (not started):** 14.3 As-Of Date, 14.5 supplemental income, 14.7 seller financing, 14.9 POH sell-down, 14.10 lease-option program, 14.11 market rents on turns, 14.12 origination drivers from DD, 15 sensitivities, 16 lock template + re-run tie-out, 17 HTML model full build, 17.1 team beta (Zach + Austin), 18 portfolio construct, 19 outputs & memos, 20 full handoff (uw-model skill + training for Zach & Austin).

*What the 63-deal dossier build actually produced*: two parallel artifact sets, both Markdown, both current as of 2026-07-28 to 2026-08-03:
- **`batch/process/`: 63 deal-process dossiers** (`.md`, 6 to 39 KB each; e.g. `steiner_portfolio.md` 31,783 B, `su_rene_redlands.md` 39,484 B, `hershey_park.md` 39,417 B). Each is a narrative reconstruction of how a deal was actually run: DD folder taxonomy era, file/GB counts, extraction method, LOI/PSA trail, dates, and what could not be read. Roadmap #10 claims 64/64; I count 63 deal-named `.md` files plus 4 non-deal synthesis files (`closing_statements_tape.md`, `jadian_emails_unmatched.md`, `lasso_facility_and_leverup_wave.md`, `ahh_portfolio.md`) and an apparent near-duplicate pair (`henderson.md` 6,318 B / `hendersons.md` 16,683 B). Supporting: `PROCESS_REPORT.md` (365,809 B), `DEEPDIVE_PROTOCOL.md`, `deepdive_manifest.json`, per-lane process reports, and Python indexers (`agentB_indexer.py`, `agentH2_indexer.py`, `pst_indexer_laneC.py`). The build ran as a multi-lane parallel agent race with claim/lock coordination (`pst_campaign.lock`, `deal_hits_ckpt.json`, `WORKER_PROTOCOL.md`).
- **`batch/kb/`: 96 per-deal knowledge-base files + `INDEX.md`** (593,084 B total; INDEX.md is 18,691 B). `INDEX.md` is the single most immediately reusable artifact in the whole estate: one line per deal giving the investment thesis in brief plus an inventory of which memo documents were found and which are missing (e.g. *"regency — Savannah rent mark-to-market — memo docs found: 8"*, *"surene — Vero Beach 47%-below-market rents — memo docs found: 0"*).
- **Email/PST layer:** `batch/process/pst_full_index` (1,119,243,650 B) and `email archive` (520,430,167 B). Roadmap #10.3 records the coverage precisely: Gmail pass complete, archive PST (Jun to Nov 2021) complete, INBOX PST 134k messages indexed, with an explicit **Dec 2021 to Apr 2024 gap**. #10.5 folded 34 Jadian first-look emails into the dossiers.
- **Model artifacts at the project root:** 34 `.xlsm` files: 2 McGregor "FIXED" workbooks (43.7 MB, 41.1 MB) and 32 template versions tracing `Template Base v0.1` → `CORE Template v0.5 to v0.8` → `TEMPLATE v1.0 … v1.21`. **v1.21 (3,956,254 B) is the current head.** Note v1.16 is absent from the sequence (v1.15a → v1.17), and v1.8 exists twice (`v1.8` and `v1.8 … vJW1`). Plus `Model Spec & Break Audit - McGregor Downs.md` (91,262 B), `Grid Documentation (draft).md` (104,321 B), `Removal Registry.md` (323,503 B), `Tax Truth File.xlsx` + NOTES, `MHP Sales Comps Database.xlsx`, `Port Validation Report.md`, `Template Tie-Out SMOKE TEST - Fox Creek + Regency.md`.

*What the 225-question list covers, and who it is addressed to.* The brief described it as "addressed to someone named Jon". That is inverted. **Jon (JW) is the author; the 225 questions are addressed to Zach (ZS) and Alex (AF).** Source: `batch/email drafts/ZS-AF - UW Deep-Dive Questions review.eml` and `…review v2.eml` (both stamped 2026-07-31), attaching `UW Model & Deal Questions - ZS-AF Review.docx` (79.85 KB) and `Parakeet Pro Forma - TEMPLATE v1.10a (Sample Park).xlsm`. Jon's instructions: it is *"the consolidated question set from the underwriting-model and deal deep-dive work (225 questions)"*; **yellow-highlighted rows are model-mechanics questions and are the stated priority**, best answered with the pro forma open; remaining rows are per-deal questions. The doc is a three-column review sheet: a `JW Comments` column Jon has already filled, and a `ZS / AF Comments` column for the reviewers to initial. He explicitly permits "don't know" and blanks, and asks for a partial pass back rather than waiting for completeness. One unrelated ask rides along: file the RealAdvice reports (Steiner, Greene Pointe) into the deal DD folders.
  There is a **second, separate question stream flowing the other way**, from the dossier build *to* Jon: `batch/process/Deep-Dive Questions for Jon (Combined).docx` (82,798 B), `batch/process/archive/Deep-Dive Questions for Jon (Round 1).docx` (16 questions drawn from the first 31 of 63 dossiers, 2026-07-05), and `batch/Knowledge Questions for Jon.docx` (31,467 B) + `v2` (58,219 B). Roadmap #8.3 records 133 answers ingested from the v2 knowledge set, and #10.4 records **89 JW + 80 AF answered with JW/AF/engine conflicts resolved**, leaving the ZS pass and final ingestion as the open item. Answered material is machine-tracked in `batch/process/mobile_answers_map.json` (80,431 B) and `mobile_answers_ledger.json` (34,201 B).

*Why this matters to the indexing problem specifically.* `batch/kb/INDEX.md` documents the same duplication disease this survey found in folders, but one level down, **inside the models themselves**. Dozens of deal workbooks carry Page 1 / "New Deal - Jadian" memo tabs whose prose was cloned from a handful of source deals and never rewritten, and the index tags them `do-not-quote`: Triple S is named as *"CANONICAL source of prose leaked into 2021-22 templates"*, with Southgate, Riviera, and Lucky Clover as the other clone sources. Contaminated examples it names include tradewinds, seashells, crystalacres, lakesaunders, congress, jbarj, palmhaven, riveroaks, vantageoaks, geigerkey, oakcrest, schenley, hwoods, baytree, sunterrace, oakhill, englewood, rosewood, windwardgardens, trailmore, northridge, cindyrae, spines, russellv, hiltonhead, and more. It also flags live arithmetic breaks (`#VALUE!` returns at Bay Oaks-adjacent Lake Saunders and Triple S, `#N/A` levered returns at bellehaven and parkwood, `addr=#REF!` at crystalacres) and prose-vs-model price conflicts (oakside $8.29M vs $8.2M; greenepointe $9M vs $8.7M; druidoaks $4.2M vs $3.9M; shadyacres $11.3M vs $11.6M; surene $79k/pad vs $94.9k). **Any second-brain index that quotes model narrative text without consulting this file will propagate known-wrong prose into new deliverables.**

*Recommended salvage order:* (1) `batch/kb/INDEX.md`, 19 KB, gives a one-line thesis and memo-artifact inventory for ~96 deals and the do-not-quote register; (2) `Roadmap & Completion Status.docx`, which tells you exactly what is done, in flight, and untouched; (3) `batch/process/PROCESS_REPORT.md` + `DEEPDIVE_PROTOCOL.md` + `WORKER_PROTOCOL.md`, the method, already proven at scale on this corpus; (4) the 63 dossiers as the per-deal source of truth for deal history. Do not re-derive any of it.

**5. `/sites/UserArchive` holds 268.6 GB across 93 folders, 92 departed-employee drives plus one eDiscovery hold, and it is entirely unindexed institutional memory.**
Path: `/sites/UserArchive/Shared Documents/General`. Naming convention is `Firstname Lastname (YYYY-MM-DD)`, the date being the archive/departure date; three folders break it (`Sue` with no date, `Sarah Wynn (2026-4-7)` unpadded, `Sherry Chesbrough (2026-07-25 )` trailing space). Archive dates span 2022-11-11 (Shiendra Halipa) to 2026-08-25 (Colin Manor, Judy Marcano).

Ten largest archives (63% of the total on their own):

| Person | Archived | Size |
|---|---|---|
| Laura OMeara | 2023-12-07 | 78.29 GB |
| Wendy Milenkevich | 2024-01-30 | 27.65 GB |
| Leslie Warden | 2025-07-29 | 21.55 GB |
| Leslie Warden | 2025-09-30 | 21.55 GB *(duplicate, see Finding 5)* |
| Brooke Stonecipher | 2025-09-30 | 17.85 GB |
| Tina Monroe | 2024-10-30 | 11.31 GB |
| Ivette Casey | 2025-11-07 | 9.96 GB |
| Deborah Koester | 2025-10-08 | 9.88 GB |
| Stephanie Roth | 2026-03-20 | 7.46 GB |
| Debora Zetino | 2024-03-05 | 7.02 GB |

**Nine archives are 0 bytes.** The folder was created but the drive was never copied, or the person had no OneDrive content: Charity Gonyer (2025-12-12), Charles Bailey (2025-05-19), Charlie Sapp III (2026-07-08), Colin Manor (2026-08-25), Edward Seidel (2026-05-13), Kevin Osti (2026-04-27), Leslie Warden (2025-11-07), Mariano Rivera (2026-08-24), Scott King (2026-07-11).

**Categories each archive holds** (from sampling two: Deborah Koester and Amy Furbush). The shape is a raw OneDrive dump, not a curated handover:
- *Property working files by community*: the largest and most valuable category. Deborah Koester's drive alone holds `Palm haven Estates` (4.32 GB), `Bay Oaks I` (2.87 GB), `Bay Oaks II` (1.56 GB), `WolfBay` (885.0 MB). Amy Furbush's holds `D row Great Oaks` (1.27 GB), `A row Great Oaks`, `lake Saunders utilities map`, `Lk Saunders Lot 120`, `Violationslake saunders_files`.
- *Teams/Copilot chat file dumps*: `Microsoft Teams Chat Files` and `Microsoft Copilot Chat Files` appear in every archive sampled (Koester 43.5 MB / 335.7 KB; Furbush 8.2 MB / 6.7 MB).
- *Meeting recordings and transcripts*: a `Recordings` (and sometimes `Transcribed Files`, `Meetings`) folder appears in at least 22 archives; a folder-name search for "Recordings" returns `totalResultCount: 549` tenant-wide, dominated by UserArchive.
- *Photos and video*: `Pictures` (Furbush 190.4 MB), `Videos` (Koester 25.5 MB, Furbush 7.6 MB).
- *Loose operational documents at the drive root, uncategorized*. Furbush's root alone holds 100+ loose files: aged-receivables PDFs under a dozen different ad-hoc names (`AR go 101525.pdf`, `Aged Receivablessssssssssssssssssssss.pdf`, `GO arn.pdf`, `GOarn.pdf`), stipulation agreements in three near-identical versions (`121 stip agreement.docx` 145,091 B / `121 stip agreement 05082026.docx` 226,514 B / `121 stip agreement 05082026  1.docx` 226,472 B), commission and mileage sheets, resident correspondence, and legal demand letters. This is the institutional knowledge nobody can find. It is findable only by full-text search, never by browsing.
- *Personal / non-business material* mixed in with business records (e.g. a child's note saved as a .docx in Furbush's root), relevant if the archive is ever produced in discovery.
- *`eDiscovery`* (130.4 MB) is a separate non-person folder holding two legal holds: `Request 2024-08-02` (101.9 MB) and `Request 2024-08-06` (28.5 MB).

**6. Leslie Warden is archived three times, wasting 21.5 GB.**
`Leslie Warden (2025-07-29)` = 21,551,756,905 B and `Leslie Warden (2025-09-30)` = 21,551,707,463 B, a 49,442-byte difference across 21.5 GB, i.e. the same drive captured twice two months apart. A third, `Leslie Warden (2025-11-07)`, is 0 bytes. Reclaimable: **~21.5 GB**, the third-largest single win in the estate after the site-plan clones.

**7. Four satellite sites are empty shells that should be decommissioned or filled.**
- `/sites/ParakeetOperations9-Amsterdam-General`: one folder, **0 bytes**. Nothing has ever been stored here.
- `/sites/Operations95`: **156,703 bytes total**, three spreadsheets (`Aged Receivables.xlsx`, `Prospect Stage Listing.xlsx`, `Property Buckets.xlsx`) under `Files/Reporting`; `Files/Property A`, `Files/Winward Knoll`, and `Postings` are all 0 bytes. A site provisioned for a workflow that never started.
- Tenant root `/Shared Documents`: 5 of 6 folders empty; the only content is a 678 KB `Formation Documents` stub that shadows the real 391 MB library on Corporate-Legal.
- `/sites/ParakeetHomes`: 4 of its 5 top-level folders (`Files`, `General`, `Home Inventory`, `Infill Budget and Plan`) are 0 bytes. The site is a 9.44 GB site-plan library wearing the costume of a general-purpose team site.

**8. `/sites/ParakeetBirdcage/Property Operations` is a 74-community scaffold that was built and abandoned within four days.**
74 folders named `Community (City, ST)` were created 2026-06-11 through 2026-06-15 with a uniform five-child subtree (`Communications`, `Construction`, `Insurance`, `Legal`, `Operations`, plus `Operations/Incident Reports`). **66 of the 74 report 0 bytes.** Only 8 were ever populated, and one of those, American (Auburn, MA) at 10.12 GB, holds 97% of the library's content. Meanwhile the live per-community operational records still sit in `/sites/main/Shared Documents/Operations/<Community>/`. This is a migration that was started and stopped, and it now competes with `main` for the same document set.

**9. Formation documents exist in four places with no clear precedence signal except governance artifacts.**
`/sites/Corporate-Legal/Shared Documents/Formation Documents` (391.0 MB, 141 entity folders) is the only copy that ships with `_Missing Documents Report.xlsx`, `_Special Cases Log.xlsx`, `LLC Entities.csv` and `Master Entity Database.xlsx`. It is being actively governed, so it is authoritative. But `/sites/ParakeetHome/Shared Documents/Legal/Formation Documents` is **584.8 MB, 50% larger**, and organizes by sponsor (`BEDROCK/`, `PO/`) rather than by entity. That size gap is unexplained and could mean either (a) Corporate-Legal is an incomplete migration, or (b) ParakeetHome holds duplicated per-sponsor copies of the same instruments. `/sites/LegalParakeet` (281.2 MB across two folders) is the superseded predecessor. Note also that `ParakeetHome/Legal` and `Corporate-Legal` each carry their own `Master Entity Database.xlsx` (128,958 B vs 32,982 B), two different master lists of the same entities.

**10. Personal OneDrives are functioning as an unofficial fourth tier of the document estate.**
Six live personal drives surfaced in search without being targeted: austin@, jclark@, natalie@, demetria@, jon@, dflynn@. Their `Microsoft Teams Chat Files` folders (`totalResultCount: 4,377` for that folder name tenant-wide) hold operational business records that exist nowhere else, e.g. `SS-ELECTRICAL UPGRADE - MICHAELS EST. $704,440.60.pdf` and `DEMO LOT CHECKLIST.pdf` (jclark@), `Open Evictions_20260823012931767.csv` and `HOME DELIVERY PROCEEDURE. 1.pdf` (natalie@), candidate CVs (natalie@), `BELLE HAVEN - RV SITE PLAN MAP 2.13.26.pdf` and `Bill Import File.xlsx` (austin@). demetria@ holds marketing/Canva proofs. austin@ additionally holds an `Austin_Brain_Vault` tree (`10 - PERSONAL OS`, `20 - PARAKEET OS`, `40 - SECOND BRAIN`, `50 - CLOUD CONNECTIONS`, all touched 2026-08-26) and prior restructuring analyses (`Parakeet_SharePoint_Restructuring.pdf`, `SharePoint_Restructure_EOM_Sprint_Plan.docx`, `Folder Structure.xlsx`). Anything only in a personal drive becomes a UserArchive folder the day that person leaves.

**11. Someone is already generating weekly SharePoint audit reports, and the second brain should read them before duplicating the work.**
`/sites/ParakeetBirdcage/Data  Analytics/` root holds 17 files named `SharePoint Audit Report - YYYY-MM-DD.docx`, dated 2026-06-05, 06-12, 06-22, 06-26, 07-04, 07-10, 07-17, 07-24, 07-31, 08-07, 08-18, 08-19, 08-21, 08-22, 08-24, 08-25 (43 to 79 KB each). There is an existing audit cadence. This inventory should be reconciled against it rather than run in parallel. Note the library name contains a **double space** (`Data  Analytics`), which breaks naive path construction.

**12. Small structural hygiene issues worth a single cleanup pass.**
- `/sites/ParakeetHome/Shared Documents/Asset Managment`, misspelled ("Managment"), which defeats folder-name search.
- Three near-identical folder-structure dumps sit loose in `/sites/ParakeetHome/Shared Documents/`: `folder_structure.csv` (400,903 B), `FolderStructure.csv` (470,755 B), `FolderStructure.txt` (470,730 B).
- Community-name spellings are inconsistent across sites and will defeat any join: `Winward Knoll` (ParakeetHomes) vs `Windward Knoll (Thonotosassa, FL)` (Birdcage) vs `WINDWARD` (main/Construction); `Seashells` vs `Sea Shells (Cape Canaveral, FL)`; `Sue Rene` vs `Su-Rene (Vero Beach, FL)`; `Palm Spring Estates` vs `Palm Springs Estates (Tarpon Springs, FL)`; `Silver Hill` vs `Silver Hills (Columbia, SC)`; `Royal Palms` vs `Royal Palm (Clewiston, FL)`.

## Gaps

- **`/sites/main` was not indexed**: by instruction, another agent owns it. Its folders appear here only where they are one leg of a cross-site duplicate (`Construction/BAY OAKS VILLAGE I`, `Parakeet Homes/Manufacturers/Cavco Homes/Plans for Sites`, plus Site Plans and Community Photos paths named in the Authoritative-locations table). Nothing in this document should be read as a survey of `/sites/main`.
- **Byte-for-byte identity is inferred from size, not from checksums.** The Graph API surfaced through `read_resource` returns folder and file sizes but no content hash. Every "byte-identical" claim in Findings 1 to 3 rests on exact matching aggregate sizes at both folder and file level (27 folders and 2 sampled files matching to the byte across three drives). That is extremely strong evidence but is not a cryptographic proof; two files of identical size could in principle differ. Confirm with a hash comparison before deleting anything.
- **The parent total for `/sites/main/.../Cavco Homes/Plans for Sites` (≈8,296,069,574 B) is summed from its 23 children, not read from the folder itself.** I read the children's sizes directly but did not fetch the parent's own byte total. The 23 individual child sizes are all directly observed.
- **`lastModifiedDateTime` was captured only for folders that came back through `sharepoint_folder_search`.** `read_resource` folder listings return name/type/size but no timestamps, so the Site Plans community folders other than the four Bay Oaks paths have no dates in this report. The Lake Saunders divergence in particular could not be dated. I could not determine which of the three snapshots is newest, only that they differ. Targeted `sharepoint_folder_search` for "Lake Saunders" returned 15 of 2,822 matches and none of them were the three Site Plans copies.
- **UserArchive was sampled, not fully enumerated.** All 93 top-level folders are listed with sizes, but only two archives (Deborah Koester, Amy Furbush) were opened to determine category structure. The category taxonomy in Finding 4 generalizes from those two plus the 22 `Recordings` folders returned by folder search; the other 90 archives are assumed to follow the same raw-OneDrive-dump shape but were not verified. Sub-drive contents of the 78.29 GB Laura OMeara archive, by far the largest, were not opened at all.
- **Personal OneDrives were deliberately not indexed** (per instruction). Six were identified by name from search results; there may be more. The `Microsoft Teams Chat Files` search hit `totalResultCount: 4,377`, of which I inspected 40. The true breadth of business records living only in personal drives is larger than Finding 9 documents.
- **Site discovery was by search-and-inspect-webUrl, which cannot prove completeness.** Eleven satellites were found by running varied folder and content searches ("Site Plans", "Bay Oaks Village I", "Reports", "Documents", "General", "Recordings", "Teams Chat Files", "meeting recording transcript") and reading site paths out of result `webUrl` fields. Sites containing no documents matching any of those terms, or containing no documents at all, would not appear. There is no tenant site-enumeration endpoint exposed through the available tools, so **I cannot state that eleven is the complete satellite count.** Sites named in the assignment brief were all found and confirmed.
- **The 17 `SharePoint Audit Report - *.docx` files in `/sites/ParakeetBirdcage/Data  Analytics/` were not opened.** They almost certainly contain prior findings that overlap this survey and should be read before acting on it.
- **`Claude Cowork` was enumerated to two levels; only the `Acquisitions/UW Model Engine` branch was characterized in depth.** The nine sibling projects were listed with sizes but not opened, including **`Corporate` at 19.04 GB, which is 83% of the entire Claude Cowork workspace and four times the size of the UW Model Engine's parent.** Whatever is in `Corporate` (Parakeet OS, Asset Listing Work, Core+ Fee Research were glimpsed via search) is the largest un-surveyed body of prior AI work in the tenant and warrants its own pass.
- **Within UW Model Engine, four branches were listed but not read:** `logic review/` (13.75 MB, incl. 10 named tie-out harnesses), `dissection/` (3.34 MB, the McGregor teardown), `engine/` (206 KB, the code port), and `brand/` (3.65 MB). `batch/email drafts/` (42.4 MB) was searched but not enumerated.
- **The 225-question document itself was not opened**, only Jon's covering email (`ZS-AF - UW Deep-Dive Questions review.eml`, 2026-07-31) which describes it. The attachment `UW Model & Deal Questions - ZS-AF Review.docx` (79.85 KB) does not appear as a standalone file in the folders I enumerated; it may exist only as an attachment inside the two `.eml` files. **The actual question text, the yellow/non-yellow split, and how many of the 225 already carry JW answers are therefore uncharacterized**. I am reporting the email's own description of its contents, not the document. Likewise `Deep-Dive Questions for Jon (Combined).docx` (82,798 B) and the two `Knowledge Questions for Jon` docs were located but not read.
- **Roadmap #10 says "64/64 dossiers"; I count 63 deal-named `.md` files in `batch/process/`.** Roadmap #9 says "~95 deals" in the KB; I count 96 `.md` files in `batch/kb/` excluding `INDEX.md`. Both discrepancies are small and probably explained by the AHH portfolio being dropped mid-build (the roadmap says so explicitly) and by the `henderson.md` / `hendersons.md` pair, but I did not reconcile them file-by-file.
- **Roadmap step statuses are as of the document's own last edit** (rev 2, 2026-07-05, with step-level entries added through 2026-08-06). Work may have progressed since; the folder tree shows activity to 2026-08-06 and the wider library to 2026-08-25. Treat "#14 in progress / ZS pass pending" as the state on 2026-08-06, not necessarily today.
- **`read_resource` folder listings return roughly 200 children with no pagination parameter.** Every listing in this document is below that ceiling and I saw no truncation markers. The largest were Corporate-Legal Formation Documents (141 folders + 5 files = 146), UserArchive General (93), `batch/kb` (97), ParakeetBirdcage Property Operations (75), and `batch/process` (~85). Alphabetical sequences all run to completion (e.g. Corporate-Legal ends at "Wolf Bay Manufactured Housing Community" then its files; `batch/kb` ends at `wolfbay.md`). No branch in this survey required tail recovery via `sharepoint_search`, but any future deeper pass into `/sites/main`-scale folders should assume the cap applies.
- **No permissions, sharing, or retention-policy data was collected**. The available tools expose content and metadata but not access control. The UserArchive `eDiscovery` folder in particular (two 2024 legal holds) may carry retention obligations that constrain any cleanup, and that could not be checked here.
