# OneDrive (Austin Berk): Inventory

**What this is:** Austin's OneDrive, including the ~200 loose files at the root where work was done and lost.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

Surveyed: 2026-08-26 | Account: austin@parakeetcommunities.com (Austin Berk, `8189a099-e1bf-4744-a2df-7e23eec895bc`) | Drive: `b!T7oszY-3i0Wfg90hKVyzahK7n5ePxOxCk5Gda5Ku67vHoXSaMjFlQ7UBj3E2R9-m`
Web root: `https://parakeetcommunities-my.sharepoint.com/personal/austin_parakeetcommunities_com/Documents/`
Local sync root: `C:\Users\AustinBerk\OneDrive - Parakeet Communities\`

**This is Austin's corporate OneDrive for Business on the Parakeet tenant, not a personal drive.** Everything in it is company-tenant storage, which matters because it holds his personal financial statement, passport scan, W-2, personal tax returns, a vaccination card, and family medical records (Finding 6).

Coverage: root fully enumerated. All 28 OneDrive-hosted root folders opened at least one level, plus 3 previously-invisible SharePoint sync shortcuts discovered via the local sync (Finding 14). Four "second brain" candidates inventoried to leaf level. `Desktop` and `Documents` mapped two levels. Where the connector's 200-entry listing cap blocked enumeration (`Attachments`, `Microsoft Teams Chat Files`, `Pictures/Screenshots`, `Desktop`, `Desktop/downloads`, `Desktop/To Sort Through`), counts were closed against the **local synced copy** with read-only directory metadata (`find`, no file contents opened) and cross-validated against the cloud listing where both were available. `__To File` reconciled exactly at 50 folders / 124 files. Remaining gaps in **Gaps**.

## Summary

This drive is ~28.5 GB of Austin's individual working residue for Parakeet Communities and its predecessor A2Z entities, spanning 2020 to 2026. It is not a filing system; it is five years of desktop-and-email exhaust that happened to sync. Two branches, `Desktop` (13.18 GB) and `Documents` (10.84 GB), are 84% of the volume and are synced local folders, not curated stores. The genuinely organized material is a handful of islands: `untitled folder/Whiteboards/to_bmhcii` (a complete Bedrock MHC Fund II accounting archive, 1.02 GB), `Microsoft Teams Chat Files/Florida 2022 Cap Ex` (18 per-property folders), `__To File` (50 entity folders), and `Post Hurricane Assessment Photos` (6 claim-evidence folders). Everything else is either a dumping ground or a loose file that was never filed.

Verified totals: the local sync tree holds **546,237 files across 110,761 directories**, though that figure spans the three mounted SharePoint libraries as well as OneDrive proper, so treat it as the size of everything reachable from this drive, not of the drive alone. Root holds **28 OneDrive folders + 124 loose files, plus 3 SharePoint library sync shortcuts** (`Parakeet Communities`, `Parakeet Birdcage - Corporate`, `Parakeet Birdcage - Data & Analytics`) that the file connector does not return. The four biggest file populations are `Microsoft Teams Chat Files` (1,720 files), `Pictures/Screenshots` (1,298), `Attachments` (719), and `Desktop/downloads` (622). That is **4,359 files in four folders, none of which is an intentional filing location.**

The single biggest problem is not volume. It is that **five separate second-brain systems have been started here and none was finished.** `Austin_Brain_Vault` (built and opened 2026-08-26, 67 KB, 100% empty scaffolding), `BerkClaude` (last updated 2026-06-01, 30 KB, 2 project folders both empty), `Austin @ Work` (a OneNote notebook, 128 KB), `Command Center` (76.8 MB of Rent Manager CSVs and Power BI test exports, not notes), and the 6,051-row `Folder Structure Tracker_Outline.xlsx` sitting unfiled in the root, a complete 12-level SharePoint taxonomy spec authored in 2023, of which only the 12 top-level departments were ever built. A sixth exists off-surface: "The Parakeet Brain" proposal (2026-07-04) in Jon Wyss's OneDrive and the ParakeetBirdcage SharePoint site. Each attempt restarted from zero rather than building on the last, and the most recent one, `Austin_Brain_Vault`, had already accumulated nine rename orphans within a day of being created (Finding 10).

Second problem: the naming pathology is measurable and severe. 40 of 124 root loose files (32%) carry names that convey nothing: `Book.xlsx` through `Book8.xlsx`, `Drawing.vsdx` through `Drawing 8.vsdx`, four `Document*`/`Doc1` variants, `abc.xlsx`, `Its Done!.xlsx`. Third: sensitive material is scattered rather than contained: a plaintext credential file, a government ID, individually-named K-1s, resident PII screenshots, and personal tax returns all sit loose in auto-capture folders.

## Taxonomy

Root: **28 OneDrive folders + 124 loose files** (complete; under the 200-entry cap) **+ 3 SharePoint sync shortcuts** the connector omits.

```
/  (28 folders + 3 shortcuts, 124 loose files, ~28.5 GB)
│
├── SHAREPOINT SYNC SHORTCUTS (invisible to the file connector; see Finding 14)
│   ├── Parakeet Communities/ ......... → sites/main library. 24 top-level folders + FolderOutput.
│   │                                     ALL 12 departments from the 2023 taxonomy spec exist here.
│   ├── Parakeet Birdcage - Corporate/  → 6 folders: Administrative, Birdcage Files, Investor
│   │                                     Relations, Legal, Process & Procedures Working Folder, Strategy
│   └── Parakeet Birdcage - Data & Analytics/ → 9 folders incl. Claude Cowork, Dashboards,
│                                       DataWarehouse Feeds, Jotform, Rent Manager, Appenate, QuickBase
│
├── SECOND-BRAIN ATTEMPTS (4 folders, 76.9 MB, 0.3% of drive)
│   ├── Austin_Brain_Vault/ ............ 67 KB   Obsidian vault, PARA+GTD. 11 subfolders, 2 root .md.
│   │                                            Built/opened 2026-08-26. 100% scaffolding, 0 content.
│   ├── BerkClaude/ ................... 30 KB   Claude Code workspace. 2 subfolders (both EMPTY),
│   │                                            4 files. TASKS.md last updated 2026-06-01.
│   ├── Command Center/ ............... 76.8 MB Not notes: 1 subfolder (PowerBI, 41.3 MB) + 16 files.
│   │                                            13 of 16 are Rent Manager/PowerBI exports + templates.
│   └── Austin @ Work/ ................ 128 KB  OneNote notebook. 1 subfolder (OneNote_RecycleBin,
│                                                26 KB) + 4 files incl. "Folder Structure.one".
│
├── SYNCED LOCAL FOLDERS (2 folders, 24.02 GB, 84% of drive)
│   ├── Desktop/ ...................... 13.18 GB 95 subfolders + 635 loose files
│   │   ├── downloads/ ................ 5.03 GB  1 subfolder (TableauAutoUpdate) + 622 files
│   │   ├── To Sort Through/ .......... 3.18 GB  14 subfolders + 292 files
│   │   ├── Models/ ................... 910 MB   0 subfolders + 3 files
│   │   ├── CapEx Kick Off Close Out/ . 825 MB
│   │   ├── New Deal NC Photos/ ....... 818 MB
│   │   ├── Rent Manager/ ............. 238 MB
│   │   ├── Disposition Model/ ........ 192 MB
│   │   └── (88 more: entity/property/accounting-project folders, 2021 to 2026)
│   └── Documents/ .................... 10.84 GB 20 subfolders + 18 loose files (cloud);
│                                                21 + 20 locally
│       ├── My Tableau Prep Repository/ 8.70 GB  80% of Documents. Tableau Prep flow cache.
│       ├── My Tableau Repository/ ..... 627 MB
│       ├── Claude/ ................... 1.33 GB  8 subfolders + 24 files. Project 001 to 004 (004 EMPTY),
│       │                                        Financial Report-BMHCII (799 MB), Communications
│       │                                        Dashboard (211 MB), Jotform. Live Claude workspace.
│       └── (17 more: Outlook Files, Scanned Documents, RM Upload, Copilot, Fax, IDE/tool shells;
│           6 of them 0 bytes: Custom Office Templates, New folder, Perplexity, SQL Server
│           Management Studio, Visual Studio 2017, WindowsPowerShell, Zoom)
│
├── DUMPING GROUNDS (6 folders, 6.85 GB, 24% of drive)
│   ├── Microsoft Teams Chat Files/ ... 2.89 GB 1 subfolder + 1,720 loose files. Largest file
│   │   │                                        population on the drive.
│   │   └── Florida 2022 Cap Ex/ ...... 204 MB  18 per-property folders + Project Overview.docx.
│   │                                            ORGANIZED, the exception in this folder.
│   ├── __To File/ .................... 1.51 GB 50 subfolders + 124 loose files (cloud and local
│   │                                            counts reconcile exactly). A2Z-era AP/bill/scan
│   │                                            backlog, mostly 2021.
│   │   └── Organize and FIle/ ........ 611 MB  a dumping ground inside a dumping ground (sic)
│   ├── Attachments/ .................. 1.40 GB 0 subfolders, 719 loose files.
│   │                                            Flat email-attachment auto-save target, 2020 to 2026.
│   ├── untitled folder/ .............. 1.02 GB 1 subfolder + 27 loose IMG_*.jpg (complete).
│   │   └── Whiteboards/to_bmhcii/ .... 1.02 GB 19 subfolders + ~80 files. Bedrock MHC Fund II
│   │                                            accounting archive. ORGANIZED: misnamed, not junk.
│   ├── Microsoft Copilot Chat Files/ . 27.9 MB 0 subfolders, 8 files (complete). Cleanest of the six.
│   └── New folder/ ................... 0 bytes  EMPTY
│
├── OPERATIONAL (7 folders, 285 MB)
│   ├── Reporting/ .................... 270 MB  7 subfolders + 5 files. Asset Management Reporting
│   │                                            (75 MB), Data Files (91 MB), Tableau (51.5 MB),
│   │                                            BMHCII Q32021 Analysis (26.5 MB), Power App, Obo Water.
│   ├── Community Manuals/ ............ 3.6 MB  OneNote. Only 2 of 43 communities: Auburn Ridge
│   │                                            (2.6 MB), Paradise Palms (390 KB). 4% coverage.
│   ├── Form/ ......................... 11.1 MB 1 file: Parakeet Financial Reporting_MRC Model_
│   │                                            For Comparison.xlsx
│   ├── Rent Manager Exports/ ......... 1.09 MB 0 subfolders, 9 files. 8 RM report CSVs +
│   │                                            Asset Status Reference.xlsx. Cleanest RM copy.
│   ├── Notebooks/ .................... 216 KB  3 OneNote sections: JW Draft Notebook, SQL Script
│   │                                            Ideas & FAQs, Walton Street Site Visit Notes
│   ├── Meetings/ ..................... 0 bytes EMPTY
│   └── Recordings/ ................... 0 bytes EMPTY
│
├── FIELD / MEDIA (8 folders, 361 MB)
│   ├── Pictures/ ..................... 178 MB  3 subfolders (2 EMPTY) + 1 file.
│   │   └── Screenshots/ .............. 178 MB  1,298 PNGs. 1,288 are default-named
│   │                                            "Screenshot YYYY-MM-DD HHMMSS.png"; 9 are named
│   │                                            {account#}-{Full Name}, resident/employee PII.
│   ├── Office Lens/ .................. 93.5 MB 2 subfolders + 27 files (3 PDF, 24 JPG). 2024-07 →
│   │   └── Photo Uploader/ ........... 62.8 MB 2025-11. 12 dated inspection sessions across 5
│   │                                            communities, 2023-05 → 2024-02.
│   ├── Post Hurricane Assessment Photos/ 60.4 MB 6 per-community assessment folders. CLAIM EVIDENCE.
│   ├── Apps/ ......................... 24.5 MB 4 subfolders: Microsoft Forms (19.0 MB, respondent
│   │                                            uploads), JL_Corporate (4.9 MB), Edge, Power Query
│   ├── Palm Spring/ .................. 4.0 MB  22 unlabelled IMG_03xx.jpg
│   ├── Belle/ ........................ 838 KB  3 unlabelled IMG_03xx.jpg (same camera roll)
│   ├── Scans/ ........................ 0 bytes EMPTY
│   └── Shortcuts/ .................... 0 bytes EMPTY
│
├── OTHER (1 folder)
│   └── 2.0 Varian Expense/ ........... 598 KB  1 file: Variable Expenses.twb (Tableau workbook)
│
└── 124 LOOSE FILES: see Findings 4 and 5
```

### Austin_Brain_Vault, in full (11 subfolders, 67 KB total)

```
Austin_Brain_Vault/
├── .obsidian/                     4 files (app/appearance/core-plugins/workspace.json)
├── 00 - COMMAND CENTER/           4 files: _System Guide.md, Annual/Monthly/Weekly Review.md
├── 10 - PERSONAL OS/              6 subfolders + 10.0 - Personal Overview.md
│     ├── 10.1 - Health            EMPTY  ← orphan
│     ├── 10.1 - Health & Performance
│     ├── 10.2 - Finance & Wealth  EMPTY
│     ├── 10.3 - Family & Relationships EMPTY
│     ├── 10.4 - Learning & Growth EMPTY
│     ├── 10.5 - Identity          EMPTY  ← orphan
│     └── 10.5 - Identity & Vision
├── 20 - PARAKEET OS/              12 subfolders + 20.0 - Parakeet Overview.md
│     ├── 20.1 - Playbook, 20.2 - Workflows (8 files: _Workflow Index + WF001 to WF007, all ~390 B stubs)
│     ├── 20.3 - Communities (_Property Template/, States/ EMPTY, _Community Index.md)
│     ├── 20.4 - Team EMPTY ← orphan | 20.4 - Team & HR
│     ├── 20.5 - Performance & Finance EMPTY ← orphan | 20.5 - Sales EMPTY ← orphan | 20.5 - Sales & Marketing
│     ├── 20.6 - Technology Stack | 20.7 - Vendors & Partners EMPTY | 20.8 - Strategic
│     └── 20.9 - Performance EMPTY ← orphan | 20.9 - Performance & Finance
├── 30 - ANCILLARY PROJECTS/       10 subfolders + 30.0 - Projects Index.md
│     (_New Project Template, A2Z Community Partners, A2Z Fund One, A2Z Wind-Down,
│      Bedrock ← orphan, Bedrock MHC, Get Real, House on Belmont, House on Winterset, Serotonin Club)
├── 40 - SECOND BRAIN/             6 subfolders
│     ├── 40.1 - Ideas EMPTY ← orphan | 40.1 - Ideas & Insights
│     ├── 40.2 - Meeting Notes | 40.3 - Knowledge Base (5 files, all ~250 B stubs)
│     └── 40.4 - Reading & Learning EMPTY | 40.5 - People & Network
├── 50 - CLOUD CONNECTIONS/        2 files: All Connections.md, SharePoint Links.md
├── ARCHIVE/                       EMPTY
├── Daily Notes/                   EMPTY  ← the workflow was never started
├── INBOX/                         EMPTY
├── Templates/                     1.3 KB
├── 🏠 DASHBOARD.md                4.3 KB, the only substantive note in the vault
└── INBOX.md                       841 B
```

## Authoritative locations

| Document set | Canonical path (recommendation) | Competing copies |
|---|---|---|
| **Folder/taxonomy spec** | `parakeetcommunities.sharepoint.com/sites/main/Shared Documents/Administrative/Folder Structure Tracker_Outline.xlsx` (mod. **2025-03-10**) | (1) OneDrive root `/Folder Structure Tracker_Outline.xlsx` (2023-09-21); (2) `/Microsoft Teams Chat Files/Folder Structure Tracker_Outline.xlsx` (2023-09-18); (3) `dflynn` OneDrive `/Microsoft Teams Chat Files/Copy of Folder Structure Tracker_Outline.xlsx` (2023-09-26). **4 copies.** Companions: `.../Administrative/Folder Structure Glossary.xlsx` (2025-03-10) and OneDrive `/Desktop/Folder Layout.xlsx` (2023-11-07). |
| **Rent Manager 8-report export set** | `/Rent Manager Exports/` (9 files, cleanest, unprefixed names) | (1) `/Command Center/` root: 6× `PowerBI_Test_20250328113315118-*`; (2) `/Command Center/PowerBI/`: 5× `PowerBI_Test_20250327073710215-*` plus 6 undated `PowerBI_Test_*`; (3) `/Documents/Claude/`: 8 plain + 8 `Communication Dashboard_*` prefixed; (4) `/Microsoft Teams Chat Files/`: 13 `Asset Listing_*.csv` re-exports dated 2026. |
| **Summary Rent Roll** (single report, as example) | pick one and date it | **6 copies, 6 different byte sizes, only 2 dated in the filename**: 581,181 / 487,159 / 584,798 / 459,810 / 459,589 / 342,540 B. No way to tell which is current from the filesystem. |
| **General Ledger extract** | `/Reporting/Asset Management Reporting/General Ledgers/` (71.9 MB, structured) | 7 loose GL CSVs of 6 distinct sizes across root, `/Command Center/`, `/Command Center/PowerBI/`, `/Documents/Claude/`; plus `/Reporting/General Ledger Analysis.xlsx`, root `/BMHCII_General Ledger Analysis_01172022.xlsx`, `/Desktop/General Ledgers/`. |
| **Austin's second brain** | **undecided. This is the decision to make.** `brain/` (this vault, established 2026-08-26) | `Austin_Brain_Vault` (2026-08-26), `BerkClaude` (2026-06-01), `Austin @ Work` (OneNote), `Command Center`, plus off-surface "The Parakeet Brain" (2026-07-04) in Jon Wyss's OneDrive `/Microsoft Teams Chat Files/` (3 PDF versions) and `sites/ParakeetBirdcage/Data Analytics/Claude Cowork/Corporate/Parakeet Brain/`. |
| **Austin's task list** | `BerkClaude/TASKS.md` (2026-06-01), stale but the only real one | `Command Center/Daily Tasks Tracker.xlsx`, root `/Daily Tasks Tracker.pdf`, root `/Task Priority Tracker.xlsx`, root `/test task list2-5ca44db4-....xlsx`, `Austin_Brain_Vault/🏠 DASHBOARD.md` open-items table, `Austin @ Work/Routine Tasking.one`. **6 competing task surfaces.** |
| **CapEx tracker** | `parakeetcommunities.sharepoint.com/sites/main/.../CapEx/Tracker/` | On this drive alone: `/Desktop/Cap Ex Project Tracker_AB Version.xlsx`, `/Capex Project Tracker_07302025.xlsx`, `/CapEx Tracker_Dec2024.xlsx`, `/CapEx Tracker_Dec2024 v3.xlsx`, `/2024 Capex Budget Tracker - Jadian Properties v2.xlsx`, `/...v2ab.xlsx`; root `/Cap Ex Project Tracker_AB Version.xlsx`, `/2024 Capex Budget Tracker - Jadian Properties v2ab.xlsx`, `/capex pacing.xlsx`, `/Consolidated Jadian CapEx Summary.xlsx`; `/Documents/Parakeet_Capex_Tracker_Full_2026.05.12.html`; `/Attachments/CapEx Reimbursement Workbook.xlsx` + 4 `(N)` copies. |
| **Bedrock MHC Fund II financials** | `/untitled folder/Whiteboards/to_bmhcii/` (19 property/entity subfolders, the real archive) | `/Documents/Claude/Financial Report-BMHCII/` (799 MB), `/Desktop/BMHCII Cash Flow Project/`, `/Desktop/FundII CF Financials/`, `/Reporting/BMHCII Q32021 Analysis/`, root `/BMHCII_General Ledger Analysis_01172022.xlsx` + `/BMHCII_Payment Analysis_01172022.xlsx`. |
| **Org chart** | none is canonical: **at least 11 competing versions** | root `/Parakeet & Affiliates Org Chart.vsdx`, `/Org Chart Overview_122023.xlsx`, `/corporate org.csv`, `/comm structure.xlsx`, plus 12 untitled `Drawing*.vsdx` at root of which some are org-chart drafts; `/Desktop/To Sort Through/Parakeet - Jadian Org Chart_Year End 2022.pdf`, `/Parakeet Org Chart_092022.pptx`, `/Fund II Org Chart.xlsx`, `/org chart and staffing_Q42022.xlsx`, `/Parakeet Property Org Chart.pdf`, and the whole `/KEYBANK ORG CHARTS/` subfolder (2.49 MB); `/untitled folder/.../to_bmhcii/Bedrock Org Chart.xlsx`. |
| **Community manuals** | `/Community Manuals/` (OneNote) | Only Auburn Ridge and Paradise Palms exist, which is **2 of 43 communities**. `/Desktop/Auburn Ridge Manual/` (4.5 MB) is a competing copy of the one that does exist. |

## Findings

**1. Five unfinished second brains, and the newest one is 100% empty.**
`Austin_Brain_Vault` is 67,492 bytes total, an Obsidian vault whose files were all last modified **2026-08-26T02:11:44Z**, i.e. created within the last day. `.obsidian/workspace.json` exists (5,476 B), so it was opened in Obsidian at least once, but no community plugins were installed (the `_System Guide.md` says Templater, Calendar and QuickAdd are required for the daily-capture loop) and `Daily Notes/`, `INBOX/`, `ARCHIVE/` are all 0 bytes. Of its content files, `🏠 DASHBOARD.md` (4,262 B) is the only substantive note; `20 - PARAKEET OS/20.2 - Workflows/` holds 7 workflow files averaging 390 bytes each (pointer stubs), and `40 - SECOND BRAIN/40.3 - Knowledge Base/` holds 4 topic files averaging 253 bytes. `20.3 - Communities/` contains a template, an index, and an empty `States/` folder. That is zero of the 43 communities. **The scaffolding is good and the DASHBOARD is worth harvesting; there is no content to migrate.**
`BerkClaude` (29,650 B) is a Claude Code workspace with `CLAUDE.md` (4,815 B, a genuinely useful Austin profile: role, co-founder, 125 employees, schedule constraints, communication preferences) and `TASKS.md` (7,764 B, header reads "Updated: 2026-06-01", so **86 days stale**). Both its declared folders, `01 Daily Logs/` and `02 Projects/`, are 0 bytes. `CLAUDE.md` says "*(No projects yet)*".
`Austin @ Work` (127,646 B) is a OneNote notebook with 4 sections: `Folder Structure.one` (38,052 B), `Quick Notes.one` (41,731 B), `Routine Tasking.one` (17,395 B), `Open Notebook.onetoc2`, plus a 25,987 B `OneNote_RecycleBin`. The recycle bin being 20% of the notebook's size indicates active deletion, then abandonment.
`Command Center` (76.8 MB) is **not a notes system despite the name**: 13 of its 16 root files are Rent Manager/Power BI exports or Office templates (`Training Roadmap Template.xlsx` and `Copy of Training Roadmap Template.xlsx`, `Project Management Template.xlsx`, `Date_Table.xlsx`). Its `PowerBI/` subfolder (41.3 MB, 12 files) is a stale 2025-03-27/28 export set plus `test_weeklyops.pbix`. The name collides with `Austin_Brain_Vault/00 - COMMAND CENTER/`, which is a different thing entirely.
**Overlap verdict:** minimal content overlap because three of the four are nearly empty. The overlap is in *intent*: four attempts at the same job, each abandoned at the scaffolding stage. Total salvageable content across all four: `BerkClaude/CLAUDE.md`, `BerkClaude/TASKS.md`, `Austin_Brain_Vault/🏠 DASHBOARD.md`, and whatever is inside the three OneNote sections. Under 100 KB.

**2. `Folder Structure Tracker_Outline.xlsx` is a complete SharePoint taxonomy spec, built only at level 1, and it is the prior attempt at exactly this work.**
Path: `/Folder Structure Tracker_Outline.xlsx` (258,028 B, root, mod. 2023-09-21). It is a 2-worksheet workbook; Sheet1 is **6,051 rows × 13 columns** encoding a folder tree by indentation depth. Structure, counted:
- **12 top-level departments**: ACCOUNTING & FINANCE, ADMINISTRATIVE, ANALYTICS & REPORTING, COMPANY DOCUMENTS, CORPORATE, HUMAN RESOURCES, INVESTOR RELATIONS, JADIAN-PARAKEET, MARKET DATA, MARKETING, PARAKEET HOMES, PROPERTIES
- **88 level-2**, **212 level-3**, **748 level-4**, **772 level-5** folders
- **2,180 leaf entries at column 12 are filename conventions**, e.g. `Bank Name_Property Name_Bank Statement_MMYYYY`, `Wire Info_Bank Name_Property Name_MMYYYY`, `Property Name_Project Name_Scope of Work_Date`, `Property Name_Insurance Company_Policy Number_Start Date - End Date`
- The `PROPERTIES` branch (rows 179 to 5,166) contains a `PROPERTY NAME (CITY, STATE)` template with four standard children, **ASSET MANAGEMENT, INSURANCE, LEGAL, OPERATIONS**, then **42 named communities**, each replicated with an identical ~116-row subtree: AMERICAN (Auburn, MA), APPLE CREEK (Bismarck, ND), APPLEGATE (DeLand, FL), BAY OAKS VILLAGE I & II (Panama City, FL), CAMBRIDGE (Charles Town, WV), CARLEY'S (Miami, FL), CENTRAL (Cocoa, FL), CONGRESS (W. Palm Beach, FL), COUNTRYSIDE (Mandan, ND), CRYSTAL ACRES (Crystal River, FL), EVERGLADES (Clewiston, FL), GEIGER KEY (Key West, FL), GULF BREEZE (Hudson, FL), HARBOUR (Cocoa, FL), HUNTER SPRINGS (Crystal River, FL), J BAR J ESTATES (Miami, FL), LAKE SAUNDERS (Mt Dora, FL), LAKE WALES (Lake Wales, FL), LAMBERTON LAKE (Grand Rapids, MI), LUCK CLOVER (Melbourne, FL), MAYFLOWER (Plymouth, MA), MEADOW WOODS (Luxembourg, MA), MONSON (Monson, MA), OCEANAIRE (New Smyrna Beach, FL), ORMOND BEACH OASIS, PALM HAVEN ESTATES (Panama City, FL), PALM SPRING ESTATES (Tarpon Springs, FL), PARADISE LAKES (Deltona, FL), PARKTOWN (Mandan, ND), RIVER OAKS (Ruskin, FL), RIVIERA (Miami Gardens, FL), ROYAL OAKS (Vero Beach, FL), ROYAL PALM (Clewiston, FL), SEA SHELLS (Cape Canaveral, FL), SHADY OAKS (Miami, FL), SILVER BREEZE (Titusville, FL), SOUTHGATE (Cape Canaveral, FL), TOWN & COUNTRY (Jacksonville, FL), TRADEWINDS (Cocoa, FL), TRIPLE S MARINA (Atlantic Beach, NC), VANTAGE OAKS (Okeechobee, FL), WESTWOOD (Ormond Beach, FL). Several city names are misspelled in the source (TARPOON SPRINGS, CAPE CANAVARAL, MEADOW WOODS listed as Luxembourg MA).
It has two companion artifacts: `Folder Structure Glossary.xlsx` (SharePoint `/sites/main/Shared Documents/Administrative/`, mod. 2025-03-10) which maps `FOLDER | FILE (CURRENT FILE NAME) | ACCURATE FILE NAME | Description`, i.e. a rename crosswalk, and `Folder Layout.xlsx` (`/Desktop/`, mod. 2023-11-07) which indexes both.

**Correction on implementation status: it was partly executed.** The `Parakeet Communities` sync shortcut (Finding 14) resolves to the `sites/main` document library, and **all 12 of the spec's top-level departments exist there**: Accounting & Finance, Administrative, Analytics & Reporting, Company Documents, Corporate, Human Resources, Investor Relations, Jadian-Parakeet, Market Data, Marketing, Parakeet Homes, Properties. Twelve further top-level folders have been added since and are **not** in the spec: `Acquisitions`, `Acquisitions (ZS)`, `Asset Management & Finance`, `CC26`, `Construction`, `Executive`, `External`, `Harry & Lloyd`, `Operations`, `Sales`, `_Archive`, `_Errors`. So level 1 landed; the drift is at level 2+ and in the 2,180 filename conventions, none of which is visible anywhere in this OneDrive. `Asset Management & Finance` duplicating the spec's `ACCOUNTING & FINANCE` and `Acquisitions` / `Acquisitions (ZS)` existing as a pair are the clearest symptoms. **Do not re-derive a taxonomy. Reconcile against this spec and the live library, and find out what the second worksheet already records** (see Gaps 2).

**3. 84% of the drive is two synced local folders that were never meant to be a store.**
`Desktop` = 13.18 GB / **95 subfolders + 635 loose files** (94 of the folders are synced locally; `Auburn Ridge Manual` is online-only). `Documents` = 10.84 GB / 20 subfolders + 18 loose files. Within `Documents`, `My Tableau Prep Repository` alone is **8.70 GB, 80% of the branch and 31% of the entire drive**, and is machine-generated Tableau Prep flow cache, not authored work. Seven `Documents` subfolders are 0 bytes (empty IDE and app shells: `Custom Office Templates`, `New folder`, `Perplexity`, `SQL Server Management Studio`, `Visual Studio 2017`, `WindowsPowerShell`, `Zoom`). `Documents/Claude` (1.33 GB) is the live Claude workspace. `Project 001` to `003` have content, `Project 004` is 0 bytes. Note that `brain/`, this vault, lives at `C:\Users\AustinBerk\Documents\Claude\Code\brain\`, i.e. **inside the synced `Documents/Claude` tree**, but `Code/` did not appear in the cloud listing of `Documents/Claude`. Confirm whether it is syncing before treating this vault as backed up.

**4. The root holds 124 loose files, and 40 of them (32%) are untraceable by name.**
Exact counts at root:

| Pathology | Count | Files |
|---|---|---|
| `Book*` collisions | **12** | `Book.xlsx`, `Book 1` to `Book 7.xlsx` (7), `Book1`, `Book2`, `Book4`, `Book8.xlsx` |
| `Drawing*` collisions | **12** | `Drawing.vsdx`, `Drawing 1` to `Drawing 8.vsdx` (8), `Drawing1`, `Drawing2`, `Drawing3.vsdx` |
| `Document*` collisions | **4** | `Document.docx`, `Document 1.docx`, `Document1.docx`, `Doc1.docx` |
| `Copy of…` | **4** | `Copy of Copy of Copy of FMHA.xlsx`, `Copy of OBO Paving comparison 4.24.xlsx`, `Copy of River Oaks Invoices.xlsx`, `Copy of Water Utilities.xlsx` |
| GUID-suffixed | **3** | `Consolidated Action Plan-114f91ca-bff7-4e18-a6cc-3bdfcdd3fd49.xlsx`, `Consolidated Action Plan-5211b2a0-2041-4458-9da1-8db7eabee065.xlsx`, `test task list2-5ca44db4-9c51-4dd9-b15c-face84c66c50.xlsx` |
| Meaningless single-word | **5** | `abc.xlsx`, `Its Done!.xlsx`, `mail.pdf`, `mail 2.pdf`, `tax2.csv` |
| **Total unidentifiable** | **40 / 124 = 32%** | |

The two `Consolidated Action Plan-<guid>.xlsx` files (99,628 B and 101,658 B) are a Microsoft Planner/Loop export pair: two exports of the same plan, 2 KB apart, neither dated.
Rough category split of all 124: accounting/finance workbooks and GL/tax extracts ~45; generic/untitled ~40; scanned bills, mail and check PDFs ~12; property- or community-specific documents ~12; ops/reporting trackers ~10; corporate/HR/org ~7; personal/media 3 (`Body Diagram.jpg`, `Orangetheory.m4a` 15.6 MB, `Dealer License_1.PNG`).

**5. Substantive, unfiled root files: these are the ones that should not be at root.**
Corporate / equity / governance: `Parakeet Cap Table 2023.xlsx` (12,698 B), `Parakeet & Affiliates Org Chart.vsdx`, `Org Chart Overview_122023.xlsx`, `corporate org.csv`, `comm structure.xlsx`, `User Privilege Chart.xlsx`.
Valuation / investor: `Parakeet - Jadian Quarterly Valuation Figures - 06302023.xlsx` (7.07 MB), `Quarterly Investor Letter Draf.docx` (sic), `Keet Asset Mgmt Reporting_20211230020146188.pdf`, `StepStone Real Estate House Views Report - Fall 2024.PDF`, `BMHCIIQ32021 Letter.docx`, `KeyBank Update_102021.docx`.
Financial extracts: `General Ledger_20250321085617819.csv` (9.28 MB), `BMHCII_General Ledger Analysis_01172022.xlsx` (17.95 MB), `BMHCII_Payment Analysis_01172022.xlsx`, `Online Collections vs Delinquency_01182022.xlsx`, `Geiger File.xlsx` (3.02 MB), `FUNDIICSV.csv` (2.13 MB), `Consolidated Jadian CapEx Summary.xlsx`, `Loan Amort.xlsx`.
Portfolio operations: `Occupancy Report.xlsx` (5.28 MB), `Portfolio Vacancy.xlsx`, `Prospect Stage Listing.xlsx`, `Parakeet Mass_Data Tape.xlsx`, `SITE VISIT LIST.xlsx`, `Parakeet - MHI FEMA Communities Info.xlsx`, `Crystal Acres 2021 CCR.pdf`, `FMHA Application Info.xlsx`.
People / hiring: `VP Finance Search Bedrock.Parakeet.docx`, `Payroll Analysis 11022023'.xlsx` (17.94 MB; note the stray apostrophe in the filename), `02022024_PAYROLL.xlsx`, `Delegation Resources.pdf`.
Method / process: `Folder Structure Tracker_Outline.xlsx` (see Finding 2), `Project Management Template.pdf`, `Goal Setting Dashboard.pdf`, `Weekly Updates.pdf`, `Daily Tasks Tracker.pdf`, `Task Priority Tracker.xlsx`, `Notes from BACH Call_01142022.docx`.
Personal / tax: `Berk 2022 draft returns dtd 3.27.24.pdf` (683,301 B).

**6. Sensitive material is scattered across auto-capture folders, not contained.**
Named, not opened. Highest concern first:
- **`/Attachments/A2Z Utility Logins.xlsx`**: a plaintext credential store in a flat, unmanaged email-dump folder.
- **`/Microsoft Teams Chat Files/Berk_ID.pdf`**: a government identity document in a chat-attachment dump. Also `/Desktop/berk passport.jpg`.
- **`/Microsoft Teams Chat Files/34390133_MIDLAND CREDIT MANAGEMENT INC. VS. RACHAEL BAILEY_GarnishmentWithholding.pdf`**: a named third party's wage-garnishment record with no business reason to be there.
- **`/Pictures/Screenshots/`**: of 1,298 files, exactly **9** are named `{account#}-{Full Name}.png` (Jon Van Horne, Amy Kellogg, Jose Daniel Molin, Jorge Perez, Teri Tuggle, Janet Valdiviezo, Cesar Mendez, Gabriel Fisher, Greg Ballas), screen captures of individual resident/employee records. Verified count against the full local listing; there are no others matching that pattern, but the 1,288 default-named `Screenshot YYYY-MM-DD HHMMSS.png` files may contain the same kind of content invisibly.
- **`/Desktop/To Sort Through/`**: resident PII by filename: `Mobile Manor Resident Contact Info.pdf`, `Resident Info for Checks.pdf`, `Resident Info Sheet.pdf`, `Resident Info Form.pdf`. Also `Property Addition Spreadsheet with TINs 05922.xlsx` and `…with TINs 101922.xlsx`, i.e. **taxpayer ID numbers announced in the filename**.
- **`/Desktop/downloads/`**: full employee rosters (`17172215_Employee_Listings_Thursday_Mar_16_08_20_36_EDT_2023.csv`, `…Wednesday_Feb_08_19_20_33_EST_2023.csv`), `Parakeet Company Directory Updated as of 424.pdf`, 34 undifferentiated `CSVStatement*.csv` bank/card exports, `FRB Deposit Accounts Letter for AUSTIN BERK.pdf`, and two redline copies of an executive comp agreement (`Parakeet-Schwartz - Employment Ltr. Agreement…(Jadian Comments).docx` and `…_AB.docx`).
- **Explicitly confidentiality-marked legal material sitting loose in a downloads folder:** `/Desktop/downloads/Annexation of Apple Creek by City of Lincoln - Storslee - Confidential Mediation Statement (09-27-2019).pdf` and `/Desktop/downloads/FW_ 3084 Parakeet_4A Claim Notice_CONFIDENTIAL.zip` (plus its `(1)` duplicate). These need a deliberate decision on where they live.
- **Individually-named K-1s:** `/Microsoft Teams Chat Files/2022 1065 Grove Banyan Holdings, LLC K-1 Partner 1 Rai, Harpreet S.pdf` (+ Partner 2 Wyss, Abigail; Partner 3 Lee, Terrence); `/untitled folder/.../to_bmhcii/Bedrock I Group - Amended 2022 K-1 Draft_Murad.pdf`; `/Attachments/2022 K-1s`, `2023 K-1`, `2024 K1 - Tarheel MHC Investment, LLC.pdf`; `/Desktop/A2Z ND PORTFOLIO PARTNERS_LLC_2023_1065_K1_Onyx MHC.pdf`, `/Desktop/BedRock_Fund_II_K-1s_25_Melman_Enterprises_LLC.pdf`.
- **Austin's personal tax/ID/comp:** root `/Berk 2022 draft returns dtd 3.27.24.pdf`; `/Desktop/Berk Tax Returns.pdf`, `A Berk 2022 W-2.pdf`, `ACH enrollment form_Berk.pdf`, `A Berk 83b Delivery Confirm.docx`, `A Berk ReadyCap Signature Package.pdf`, `berk passport.jpg`.
- **Medical:** `/Desktop/Jamie_Berk_Lab Work/` (2.73 MB), `/Desktop/Jamie Results/` (4.87 MB), `/Desktop/downloads/Berk, Jamie 2-25-2023_17401.pdf` + `… REVISED.pdf`, `/Desktop/To Sort Through/JBerk_Cleveland Clinic.pdf`, `/Desktop/To Sort Through/Vaccination Card_A Berk.jpeg`, `/Desktop/To Sort Through/JLB Botox Since Nov21.xlsx`, root `/Body Diagram.jpg`. **All of this is family medical data on company-tenant storage.**
- **Austin's personal financial statement:** `/Desktop/To Sort Through/A Berk PFS.pdf`.
- **Payroll & comp:** root `/02022024_PAYROLL.xlsx`, `/Payroll Analysis 11022023'.xlsx`; `/Desktop/Payroll/`, `/Payroll Data/`, `/Payroll Files/`, `/2024 Payroll Allocation Model*.xlsx` (3 variants); `/Attachments/2026 payroll -employee list.xlsx`, `Corporate Payroll - Proposed 2023 Bonuses…` (3 near-identical copies, ~10 MB), `Copy of 2023 Year End Comp Suggestions.xlsx`, `Contractors - 2024 Bonus and 2025 Pay Increase.xlsx`; `/Microsoft Teams Chat Files/2025 EOY Pay & Bonus.xlsx` (×2), six `17172215_Payroll_Labor_Cost_*` workbooks.
- **KYC / beneficial ownership:** `/Attachments/25 percent Certification of Beneficial Ownership (Sched A) PARAKEET ENTITIES.docx`, `2. Business_CIP Signers.Owners.docx`.
- **Banking / wire instructions:** `/Documents/Parakeet MHC, LLC ACH & Wire Transaction Routing Instructions.pdf`, `/Microsoft Teams Chat Files/A2ZCP Wire Info.pdf`, `ACH - Wire Instructions -WSRED II REIT HOLDINGS, LLC.pdf`; `/Desktop/GBP JPM Checking - 2022/2023/2024/2025 statements/` (4 folders); root `/Checks_20240828105930178.pdf`.
- **Active litigation:** `/Microsoft Copilot Chat Files/Parakeet Motion to Dismiss 8.16.24 …pdf` (**two byte-identical copies at 13,302,091 B each, so 48% of that folder is a duplicate of one filing**); `/Desktop/Curtis Myers - INITIAL DRAFT of Settlement Agreement and INITIAL DRAFT of Proposed Agreed Order Of Dismissal, With Prejudice/`; `/Microsoft Teams Chat Files/32558011_CHRISTINE WILLIAMS VS. BELLE HAVEN MHC LLC_Demand Letter.pdf`.
- **Resumes / HR reviews:** 3 resumes and 3 `Acharya Employment Agreement` variants in `/Microsoft Teams Chat Files/`; `AF -` and `AS - Parakeet Communities - Investment Team - Self Review.docx` in `/Attachments/`; `/Office Lens/One-on-One Log/`; root `/VP Finance Search Bedrock.Parakeet.docx`; `/Desktop/Berman Offer Letter.docx` + `.pdf`.
- **Respondent uploads:** `/Apps/Microsoft Forms/` (19.0 MB). Forms upload folders routinely hold whatever respondents attached.

**7. `untitled folder` is the most valuable thing on the drive and the worst-named.**
1.02 GB, of which 99.3% is `Whiteboards/to_bmhcii/`: **19 subfolders + ~80 files forming a complete Bedrock MHC Fund II accounting archive**, organized per entity and per property with `(City, State)` naming: Bay Oaks Village, Bedrock I Group, Bedrock MHC Fund II GP, Bedrock MHC Fund II LP, Disposition, External Financials, Financials, Greenspot Village (Las Vegas, NV), Lake Wales (Lake Wales, FL), Lamberton Lake (Grand Rapids, MI), Mobile Manor (Rosedale, MD), Oceanaire (New Smyrna Beach, FL), Ormond Beach Oasis, Palm Spring Estates (Tarpon Springs, FL), Tarheel Portfolio, Town & Country (Jacksonville, FL), Valley View (Roseburg, OR), Westwood (Ormond Beach, FL), Wolf Bay (Elberta, AL). Anchor files: `BMHCII_Disposition Workbook.xlsx` (81.5 MB), `FUNDII Q22023 Analysis.xlsx` (74.1 MB), `BMHCII Lender Reporting Model.xlsx` (70.1 MB), `Capital Account Balance Spreadsheet.xlsx`, `Fund II_SPE_EIN Reference.xlsx`, `Bedrock Org Chart.xlsx`. It also holds the drive's single largest waste: `Contribution Distribution Workbook.xlsx` (172,500,778 B) and `Contribution Distribution Workbook2024.xlsx` (172,526,438 B). That is **345 MB, one third of the folder, in two near-identical files.** Rename this folder; do not purge it.

**8. Duplicate mass is concentrated and measurable.**
Confirmed byte-identical or near-identical pairs found without opening a single file:
- 345 MB: `Contribution Distribution Workbook.xlsx` / `…2024.xlsx` (`untitled folder/.../to_bmhcii/`)
- 13.3 MB: `Parakeet Motion to Dismiss 8.16.24 … cover ltr.pdf` / `… cover ltr 1.pdf` (both 13,302,091 B, `/Microsoft Copilot Chat Files/`)
- ~10 MB: `Corporate Payroll - Proposed 2023 Bonuses…` ×3 (`/Attachments/`)
- 12 MB: 13 `Asset Listing_*.csv` re-exports, including **four on 2026-05-14 and four on 2026-05-15** (`/Microsoft Teams Chat Files/`)
- `2023 Tax Summary_ZS.xlsx` / `… 1.xlsx` (both 1,731,043 B); `366 Lily Lane.doc` / `…(1).doc` (both 128,512 B); `2021_MH_Expense_Summary_-_Newmark.pdf` / `… 1.pdf` (both 79,653 B); `21st Mortgage Memo.docx` / `… 1.docx` (both 159,803 B)
- `/Attachments/`: 14 `Copy of …` files, 10 `BookN.xlsx` variants, 11 `(N)`-suffixed, a 5-copy `CapEx Reimbursement Workbook` set, and a 17-file `DocScan_1006` split-page family, **all within the 200 files visible, i.e. ~25% of that folder**
- 20 disposable UPS shipping-label PDFs in `/Microsoft Teams Chat Files/`
- Typo-duplicates: `bedrock group cash flow.xlsx` / `Bedrock Group Cash Flwo.xlsx`; `Bay Oaks VIllage` (capital I) as a folder name

**9. Twelve folders are 0 bytes: declared structure that was never used.**
Root: `Meetings`, `Recordings`, `Scans`, `Shortcuts`, `New folder`. `Documents`: `Custom Office Templates`, `New folder`, `Perplexity`, `SQL Server Management Studio`, `Visual Studio 2017`, `WindowsPowerShell`, `Zoom`, `Financial Reporting`, `Project 004`. `Desktop`: `BALANCE SHEETS ACCRUAL`, `Dolphin Photos`, `Go Pro Reviews`, `Insurance 2024 Entries`, `Jadian - General`, `New folder`, `transactions_ca6d17cd-23da-4fa7-a3f2-995bf6a34103`. `Pictures`: `Camera Roll`, `Saved Pictures`. `Austin_Brain_Vault`: 12 more (see Taxonomy). `BerkClaude`: `01 Daily Logs`, `02 Projects`. This is the recurring signature: structure gets declared, then nothing lands in it.

**10. `Austin_Brain_Vault` already contains rename orphans, one day after creation.**
Nine pairs where a folder was renamed and the empty original was left behind: `10.1 - Health` vs `10.1 - Health & Performance`; `10.5 - Identity` vs `10.5 - Identity & Vision`; `20.4 - Team` vs `20.4 - Team & HR`; `20.5 - Sales` vs `20.5 - Sales & Marketing`; `20.5 - Performance & Finance` vs `20.9 - Performance & Finance`; `20.9 - Performance` vs `20.9 - Performance & Finance`; `40.1 - Ideas` vs `40.1 - Ideas & Insights`; `Bedrock` vs `Bedrock MHC` (in `30 - ANCILLARY PROJECTS`). The vault's own `_System Guide.md` also describes folders that do not match what exists. It names `30 - PROJECTS` (actual: `30 - ANCILLARY PROJECTS`), `50 - CLOUD` (actual: `50 - CLOUD CONNECTIONS`), and an install path of `OneDrive\Austin Brain Vault` (actual: `Austin_Brain_Vault`). Its `🏠 DASHBOARD.md` has an internal date error too: "Open Items (Action Required — started 08/26/26)" against a vault footer of "Vault version 2.0 — Built August 2026". **The drift started immediately.**

**11. High-value material worth lifting out before any cleanup.**
- `/untitled folder/Whiteboards/to_bmhcii/`: Bedrock Fund II archive (Finding 7)
- `/Microsoft Teams Chat Files/Florida 2022 Cap Ex/`: 204 MB, 18 per-property folders + `Project Overview.docx`; the only curated thing in a 2.89 GB dump
- `/Post Hurricane Assessment Photos/`: 6 folders of storm-damage evidence (Applegate unit 34, Lucky Clover downed wires, Ormond Beach unit 95532, Tradewinds, Vantage Oaks, Whispering Pines FL). Insurance/FEMA claim material.
- `/Office Lens/Photo Uploader/`: 12 dated inspection sessions across Applegate, Lake Saunders, River Oaks, Westwood (2023-05-15 → 2024-02-28). Directly relevant to the Recurring Property Inspections workstream.
- `/Office Lens/Top MH Owners 1996.pdf`: industry reference, not reproducible
- `/2.0 Varian Expense/Variable Expenses.twb`: authored Tableau workbook ("Varian" is a typo for "Variable"); note a `.twb` stores only the definition, so confirm its data source still exists
- `/Attachments/` executed originals: `Belle Haven MHP-Purchase and Sale Agreement (Fully Executed) (9511311).PDF` + its First Amendment, `Closing Binder. Purchase of Geiger Key Marina (8988691).PDF` (15.5 MB), `22-360743.3_Phase_I_Report_-_Vantage.pdf` (17.4 MB Phase I ESA), `33 Cambridge_Land Lease.pdf` + `33 Cambridge_RTO.pdf`, `2024 1065 Parakeet MHC LLC.pdf`, `Core Values.pdf`, `Chain of Command updated 2023.docx`
- `/Microsoft Teams Chat Files/00-START HERE - Process Wiki Index.html`: somebody built an index; find out what it points at
- `/Command Center/Parakeet - CIM - December 2024_vF.pdf` (4.65 MB): final CIM
- `/Documents/Parakeet - Board Presentation 2024-02-15 v1.pdf`, `/Documents/Parakeet_90Day_Action_Plan.xlsx`
- `/Microsoft Copilot Chat Files/Parakeet Executive Summit Agenda - March 2026 v4.docx`, `FEMA Meeting on Housing Solutions for Storm-Impacted Communities.docx`, `Preventative Maintenance List.pdf`

**12. `Community Manuals` covers 2 of 43 communities.**
`/Community Manuals/` is a OneNote notebook holding `Auburn Ridge.one` (2.61 MB), `Paradise Palms.one` (390 KB), `Table of Contents.one` (24.9 KB) and a 578 KB `OneNote_RecycleBin`, larger than the Paradise Palms section. Against the 42 communities enumerated in the folder-structure spec (Finding 2), that is **4.7% coverage**. A competing copy of the one substantive manual exists at `/Desktop/Auburn Ridge Manual/` (4.55 MB).

**13. `__To File` is a 2021 A2Z-era accounting backlog that is better organized than the root.**
1.51 GB: **50 subfolders + 124 loose files** (complete enumeration). The subfolders are cleanly split between legal entities (14 `A2Z *` LLCs, `Bedrock EM Holdings LLC`, `Bedrock I Group LLC`, `Tarheel HoldCo LLC`, `Tarheel MHC Investment LLC`, `AP MHC Holdings LLC`, `Fund II LP`) and properties (Cedar Grove, Clewiston, Colonial, Deer Run, Everglades, Henderson, Journeys End, Lake Alfred, Lambeth, Mobile Manor, ND Communities, Parkwood, Ponderosa, Royal Oaks, Shasta Glen, Siesta Palms, Tarheel, Valencia MHP, Valley View, Vandemere, Alfred MHP, Beach Street Manor). The 124 loose files are AP artifacts: 11 `Bills_*.pdf`, 16 `Mail_*.pdf/jpeg`, 17 `Scan*.pdf`, utility and vendor invoices, dated almost entirely **2021**, with a few 2022. Two of its children are themselves dumping grounds: `Organize and FIle` (611 MB, sic) and `Separated Files` (11.1 MB). The largest child is `Southeast MHC Portfolio - Final Thirds` (351 MB), a disposition data room.

**14. Three SharePoint library sync shortcuts sit in the root and are invisible to the file connector.**
`read_resource` on the drive root returned 152 children and no shortcuts; the local sync shows three more folder entries that are "Add shortcut to OneDrive" links into SharePoint:
- **`Parakeet Communities`** → the `sites/main` document library. 24 top-level folders (listed in Finding 2) + a file named `FolderOutput`. **This is the company's real filing system, mounted inside Austin's OneDrive**, and it is where the 2023 taxonomy actually landed. Last modified 2026-08-06.
- **`Parakeet Birdcage - Corporate`** → 6 folders: `Administrative`, `Birdcage Files`, `Investor Relations`, `Legal`, `Process & Procedures Working Folder`, `Strategy`. Last modified 2026-08-06.
- **`Parakeet Birdcage - Data & Analytics`** → 9 folders: `3rdPartyInfoforInfill`, `Appenate`, `ARAP`, **`Claude Cowork`**, `Dashboards`, `DataWarehouse Feeds`, `Jotform`, `QuickBase`, `Rent Manager` + 22 files. Last modified 2026-05-21.
`Claude Cowork` on the Birdcage site is where "The Parakeet Brain" proposal lives (`.../Claude Cowork/Corporate/Parakeet Brain/`, 2026-07-04), the sixth second-brain attempt, and the only one that was written as a proposal to both founders rather than built solo. The root also holds two `.url` files (`Austin @ Work.url`, `Community Manuals.url`) pointing at the two OneNote notebooks, which is why those two folders sync as links rather than files.
**Consequence for this index: any survey of this drive that uses only the file connector will miss the three most current, most structured branches attached to it.**

**15. The three biggest Desktop children, characterized.** (Counts verified against the local sync.)
- **`downloads`: 5.03 GB, 1 subfolder (`TableauAutoUpdate`) + 622 files.** File mtimes run 2022-04-18 → 2023-12-18, with 610 of 622 in 2023. Types: 362 pdf, 104 csv, 41 xlsx, 35 zip, 24 docx, 16 xls, 6 exe. **~4.0 GB (80%) is six junk files**: `Ferrari 488 GTB.mp4` (1.15 GB), `TableauPrep-2023-1-0.exe` (852 MB), `TableauPrep-2022-4-1.exe` (816 MB) and its byte-identical `(1)` twin (816 MB), `TableauDesktop-64bit-2022-4-0.exe` (590 MB), `TableauServerTabcmd-64bit-2023-1-1.exe` (65 MB). Pathology: **158 files (25%) carry a ` (N)` download-collision suffix**; 88 `CocoaFL-4896xx-…` utility exports, roughly half of them `(1)` twins; **34 files named `CSVStatement.csv` / `CSVStatement (1..33).csv`**, bank and card statements with no issuer, account or period in the name; 31 `Invoice - <Entity> 2023-03-0N.pdf` of which 11 have `(1)` twins; 9 GUID-named files including one 5 MB JPEG present in three copies; `Parakeet MHC - Capital to Date - 12.19.2022 v2 (back up unit calc 1.5.23).xlsx` in **four copies**. Despite all that it holds a coherent **37-file Delaware annual-compliance set** (`… - DE - State Compliance - <Entity> LLC.pdf`, Mar to Apr 2023, ~35 entities), EIN confirmation letters, executed purchase and loan agreements (`Meadow Woods MHP-Purchase Agreement (Fully Executed).pdf`, `RE_ Paradise Lakes - Final Loan Documents.zip`), a board consent, `Employee Handbook Draft.pdf`, `Chain of Command updated 2023.docx`, and `Flow Charts for SOPs.pdf`. **Do not bulk-delete.**
- **`To Sort Through`: 3.18 GB, 14 subfolders + 292 files. This is the substantive one, and it is misnamed as a dumping ground.** 270 of 292 files (92%) are from 2022, a frozen operating snapshot. Only **1** `(N)`-suffixed file and **0** GUID names; naming is human and descriptive. Subfolders are all worth keeping: `Septic Email Winnie only_Export` (1.20 GB), `To send to avid` (724 MB), `Photos for Office Walls` (297 MB), `PCA Reports` (159 MB), `CapEx Receipts MRC`, `Property Tax Bills`, `Weekly Summaries & Recaps`, `AG Mass`, `Operating Agreements`, `KEYBANK ORG CHARTS`, `Procedures and Process for Operations`, `Agreements to Sign`, `Hurricane Ian_KeyBank'` (sic), `Executive Meeting Files`. Loose highlights: `Parakeet_SREO_12312022.xlsx`, `Parakeet_Balance Sheet_09302022.xlsx`, `11142022_PORTFOLIO MODEL.xlsx`, `CapTable.xlsx`, `Property Master Sheet.xlsx`, `Lot Audit.xlsx`, `Rent Roll Audit.xlsx`, `Staffing Grid.xlsx`, `Ops Calendar 2023.xlsx`, `Parakeet - Jadian Org Chart_Year End 2022.pdf`, `BMHCII Quarterly Update Q2 '22.pdf`, `ParaKeet - SharePoint Executive Report.docx`. Main waste: **244 MB in five successive saves of one workbook**: `Template with All Line Items.xlsx`, `…_010.xlsx` (49 MB), `Tabbed Template with All Line Items_011.xlsx` (52 MB), `_012.xlsx` (68 MB), `_014.xlsx` (80 MB). Also 11 basenames existing as docx+pdf or xlsx+pdf pairs, and sloppy near-twins (`Ops Calendar 2023.xlsx` / `Ops Calendar 2023sss.xlsx`, `pORTFOLIO.xlsx`, `Rent Increse data.xlsx`).
- **`Models`: 910 MB, 0 subfolders, 3 files.** `BudgetModel_v7.xlsx` (774.8 MB, 2023-02-14), `CashFlow Model with Roll Up.xlsm` (66.5 MB, 2022-04-10), `CashFlow Model with Roll Up.xlsx` (68.5 MB, 2022-04-06). Keep all three. A 775 MB `.xlsx` is pathological in itself and is a candidate for a size-reduction pass, not deletion. `_v7` implies v1 to v6 exist somewhere else; only v7 is here.


## Gaps

1. **Connector listing cap: counts closed, filenames still unread.** MCP `read_resource` returns at most 200 children per folder, exposes no offset parameter, and truncates silently. Six listings hit it: `/Attachments/`, `/Microsoft Teams Chat Files/`, `/Pictures/Screenshots/`, `/Desktop/`, `/Desktop/downloads/`, `/Desktop/To Sort Through/`. **Counts for all six were closed against the local synced copy** at `C:\Users\AustinBerk\OneDrive - Parakeet Communities\`, using read-only directory metadata only, and validated where both sources were complete (`__To File`: cloud 50/124 = local 50/124). What is still open is **content**: only the first ~200 filenames alphabetically were read in `/Attachments/` (719 files) and `/Microsoft Teams Chat Files/` (1,720 files). **Roughly 520 and 1,520 filenames respectively have never been looked at.** Every duplicate count and sensitive-file list for those two folders is therefore a floor, not a total. Close with Graph `/children` + `$skiptoken`, or a local filename dump.

2. **`Folder Structure Tracker_Outline.xlsx`: partially read.** The workbook declares **2 worksheets**; only Sheet1 was returned, and Sheet1 itself was cut with "400 more rows in this sheet and any later sheets not shown." So ~400 rows of the PROPERTIES tail and **the entire second worksheet are unread.** Sheet1's 6,051 rows were fully analysed structurally (depth histogram, all 12 departments, all 42 named communities). The second sheet is likely the status half of the "Tracker" and **may already record which parts of the taxonomy were implemented**, which would directly answer the question Finding 2 leaves open. Open it in Excel; do not re-derive.

3. **Per-community subtrees in the spec were sampled, not read line by line.** Rows ~3,000 to 5,166 were verified structurally (each community block is ~116 rows with the same four children: ASSET MANAGEMENT, INSURANCE, LEGAL, OPERATIONS) via the template block and the depth histogram. A deviation in one individual community's subtree would not have been caught.

4. **The SharePoint shortcuts were listed one level deep only.** `Parakeet Communities` (24 top-level folders), `Parakeet Birdcage - Corporate` (6), `Parakeet Birdcage - Data & Analytics` (9 + 22 files) were enumerated at level 1 from the local sync. **Their contents are out of scope for this OneDrive index and belong in separate SharePoint inventories**, but note they are reachable from this drive, so any "what's in Austin's OneDrive" answer that ignores them is wrong. `Parakeet Communities/FolderOutput` (a file, not a folder) was not opened and its name suggests a folder-tree dump worth reading.

5. **OneNote content not read.** `Austin @ Work` (`Folder Structure.one` 38,052 B, `Quick Notes.one` 41,731 B, `Routine Tasking.one` 17,395 B), `Community Manuals` (`Auburn Ridge.one`, `Paradise Palms.one`, `Table of Contents.one`), `Notebooks` (`JW Draft Notebook`, `SQL Script Ideas & FAQs`, `Walton Street Site Visit Notes`), and `/Documents/OneNote Notebooks/` are `.one`/`.onetoc2` binaries the file connector lists but cannot render. They sync as `.url` links, not files. **`Austin @ Work/Folder Structure.one` is very likely a third prior taxonomy artifact and remains unread**. Read it before designing anything. Needs the OneNote API or the app.

6. **File contents not opened, by design.** No file named in Finding 6 was opened; every sensitivity classification here is inferred from filename and location alone. That cuts both ways: some flagged files may be benign, and files with neutral names (the 1,288 default-named screenshots, `Book4.xlsx`, `Binder1.pdf`) may hold worse. `/Apps/Microsoft Forms/` (19.0 MB) and `/Apps/JL_Corporate/` (4.9 MB) were listed at parent level only; Forms respondent-upload folders routinely hold ID documents and signed paperwork and deserve a dedicated pass.

7. **Modification dates are missing for most items.** `read_resource` folder listings return name, type and size only. Real dates were obtained via `sharepoint_search` or the local sync for a handful: `Austin_Brain_Vault` 2026-08-26, `Austin @ Work` 2025-11-17, `untitled folder` 2025-06-23, `Parakeet Communities` shortcut 2026-08-06, `Parakeet Birdcage - Data & Analytics` 2026-05-21, `Folder Structure Tracker_Outline.xlsx` 2023-09-21 (SharePoint copy 2025-03-10), `Folder Layout.xlsx` 2023-11-07, `Desktop/Austin & Jon` 2023-10-17, plus full mtime ranges for `Desktop/downloads` (2022-04-18 → 2023-12-18) and `Desktop/To Sort Through` (2021-12-16 → 2025-09-19). **Everything else dated in this document is dated from its filename**, which is exactly the failure the naming pathology produces. For `Book4.xlsx` or `Summary Rent Roll.csv` there is no date at all, in the name or in what the connector returns.

8. **Deleted and versioned content not surveyed.** The OneDrive recycle bin, per-file version history, and the two `OneNote_RecycleBin` folders (`Austin @ Work` 25,987 B; `Community Manuals` 578,204 B) were not examined. The Community Manuals recycle bin is **larger than its entire Paradise Palms section**, so something substantive was deleted there and may be recoverable.

9. **Whether `brain/` is actually syncing was not confirmed.** This vault lives at `C:\Users\AustinBerk\Documents\Claude\Code\brain\`, inside the OneDrive-synced `Documents\Claude` tree, but the cloud listing of `Documents/Claude` returned no `Code` child. Either sync is pending, `Code/` is excluded, or the local path is not the synced one. Verify before treating this index as backed up.

10. **The 546,237-file drive-wide count is not decomposed.** `find` over the whole local sync root returned 546,237 files / 110,761 directories, but that traversal includes the three mounted SharePoint libraries (`Parakeet Communities`, `Parakeet Birdcage - Corporate`, `Parakeet Birdcage - Data & Analytics`), whose contents belong to separate inventories. **The OneDrive-only file count was not isolated** and cannot be derived from the figures in this document. Re-run excluding those three paths to get a clean number.

11. **Two `Desktop` items could not be reconciled.** `Desktop/Auburn Ridge Manual` (4,549,162 B) appears in the cloud listing but does not exist in the local sync. It is online-only, or the listing mis-sorted it. The cloud shows 95 Desktop subfolders; the local sync shows 94. The one-folder delta is this item.
