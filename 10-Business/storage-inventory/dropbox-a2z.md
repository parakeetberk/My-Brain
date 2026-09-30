# Dropbox (A2Z MHC team space): Inventory

**What this is:** The A2Z Dropbox tenant: 445 GB of 2016 to 2021 acquisition-era provenance, and the Lamberton Lake syndication records that appear to exist nowhere else.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

Surveyed: 2026-08-26 | Account: Austin Berk `austin@a2zcp.com`, team "A2Z MHC", root namespace `11855305057` (home namespace `4802313104`) | Coverage: all 10 top-level mounts enumerated; 2 to 4 levels deep in every branch; full recursive sweeps of `Cambridge - SCH 2025`, `Lamberton Lake DD Files`, `Crystal Acres and Hunter Springs Cleanouts`, and `A2ZMHC/Entities`; cross-checked against SharePoint `parakeetcommunities.sharepoint.com` for the Lamberton Lake authority question.

## Summary

This is a ~445 GB legacy archive of the A2Z / Bedrock manufactured-housing business, spanning roughly 2016 to 2021, that the company has since left behind for Microsoft 365 under the Parakeet Communities tenant. Nine of the ten mounts are frozen: the newest genuine content in `Corporate` is 2019, in `Pipeline` and `Accounting` 2020, in `Property Management` January 2021, and in `Business Lines` November 2020. Only one branch is genuinely alive: a folder of ~170 field photos inside Austin's personal space uploaded 2026-08-05. The second-newest, `Cambridge - SCH 2025`, has been untouched for exactly twelve months. The single biggest problem is that the mount literally named `Lamberton Lake DD Files` is **completely empty** while a live 2026 sale runs in SharePoint, and meanwhile the real Lamberton ownership record (formation, original PSA, refinancing, and **LP syndication files that appear to exist nowhere else**) sits buried five levels deep under `Business Lines`, where nobody working the sale would look.

The archive is not dead weight. It is the provenance layer: the acquisition-era, entity-formation, and syndication history that SharePoint's operational and sale-side trees do not carry.

## Taxonomy

Sizes are `folder_size` from `get_file_metadata` (bytes, includes nested mounts). "Newest content" is the newest file/folder timestamp actually observed inside the branch, not the mount timestamp, which is unreliable (see Finding 3).

```
ns:11855305057//  (A2Z MHC team root) — 10 mounts, ~445.2 GB total
│
├── Austin Berk                  ns:4802313104   330.72 GB   newest 2026-08-05   LIVE (one folder only)
│   │   Personal/home namespace. ~60 loose root files + ~25 folders + ~22 nested mounts.
│   ├── Crystal Acres and Hunter Springs Cleanouts   170 files, 2026-08-05   ← only live content in the space
│   ├── Cambridge MHC Due Diligence Folder  ns:4436920385  17 numbered DD folders, content 2023-08
│   ├── Migrated Paper Docs (2025-06-16), Dropbox Business reports (2022), 2019/2020/2021 year folders
│   ├── Departed-staff folders: Jorden Angel, Nicole Wood, Chrissy Fitzgerald, Winnie Bretz
│   └── 22 nested mounts (Lasso/KeyBank/Tar Heel/Shared Loan Diligence/tresvista/Payroll Reports/…)
│
├── Pipeline                     ns:4549709616    46.28 GB   newest 2020-09-24   FROZEN
│   ├── _LOIs        ~103 files, ~45 distinct deals, 2016-03 → 2020-09  (deal-flow history)
│   ├── New / Review / Archives / __Miscellaneous / Templates
│
├── Property Management          ns:4524714528    35.31 GB   newest 2021-01-19   FROZEN
│   ├── Communities  ns:7525050192   16 state folders, 23 community/portfolio folders
│   │     AL 1 · FL 4 · IN 1 · KS 1 · KY 1 · MA 1 · MD 2 · MI 2 · NC 2 · ND 1 · NV 1
│   │     NY 1 · OR 2 · TX 1 · WA 1 · WV 1
│   ├── 3 nested mounts: Communities, "Refuse Specialist to review", _5200
│   └── Invoices and Receipts, Manuals and Templates, Regulatory, __Agreements, New Hire Packet …
│
├── Business Lines               ns:4566704256    28.71 GB   newest 2020-11-12   FROZEN
│   ├── A2ZCP        Holdings/Single Asset SPVs (13 SPVs) + Fund 1 (A2Z); Legal, Accounting, Strategy
│   ├── Bedrock Group  Entities/{BMHCII (Fund 2), Bedrock EM Holdings}; Admin, Legal, Marketing, Strategy
│   │     BMHCII Holdings: Tarheel Portfolio, Mobile Manor, Greenspot Village, Valley View
│   │     Bedrock EM Holdings → Lamberton Lake  ← full ownership lifecycle, see Finding 1
│   ├── A2ZMHC       Entities (5 management LLCs, formation docs), Contracts, Financials
│   ├── MoMa Lending ns:7739399456  Legal, Strategy, Analyses, Triad Docs, Parklane Finance Docs
│   ├── Mobile Manage  5 files — property-management agreements + community list (software/PM line)
│   └── NewCo        Recapitalization, RollUp Model, Promote Valuation, Buyout  (2019–2020 strategy)
│
├── Reference                    ns:5948259680     3.47 GB   newest 2020-05-12   FROZEN
│       JLT Reports, Research, News Articles, DD Manuals, Modeling Templates, ND Leases, OR ROFR
│
├── Corporate                    ns:5940707216   426.93 MB   newest 2019-10-07   FROZEN (oldest branch)
│       Human Resources · Finances · Payroll · Technology · Branding · Facilities · Travel
│       Stationary · Service Providers · Templates · Analysis        (11 folders, all 2019)
│
├── Cambridge - SCH 2025         ns:12972052483  194.22 MB   newest 2025-08-25   FROZEN 12 months
│       Cambridge DD 2025/ — 271 files, 46 folders, 11 of ~25 numbered DD items present
│
├── Accounting                   ns:4566106320    84.05 MB   newest 2020-10-06   FROZEN
│       12 folders + 8 loose files. Period coverage 2018 → 2020-10. Monthly Recons cover
│       only Oct–Dec 2019. Tax Filings has no subfolders.
│
├── Team Paper Docs              ns:12461723825    3.00 KB   migrated 2025-06-16  EMPTY IN SUBSTANCE
│       9 mounts holding ~15 × 200-byte `.paper` stubs (2019-era). No file bytes; content
│       lives in Dropbox Paper, not retrievable as files.
│
└── Lamberton Lake DD Files      ns:4960725313        0 B    EMPTY — zero entries, recursive
```

## Authoritative locations

| Document set | Canonical path | Competing copies / notes |
|---|---|---|
| **Lamberton Lake 2026 sale diligence** | **SharePoint** `/sites/main/Shared Documents/External/Lamberton Lake (Sale 2026)/` (mod. 2026-07-29) | Dropbox `ns:11855305057//Lamberton Lake DD Files` is **empty**. SharePoint wins outright. Also SP `…/External/Lamberton Lake Nov 2025 DD` (prior round) and `…/Ad Hoc Analysis/Due Diligence Files - Properties for Sale/Lamberton Lake - DD Requirements` (2026-07-29). |
| **Lamberton Lake ownership & acquisition record** | **Dropbox** `ns:4566704256//Bedrock Group/Entities/Bedrock EM Holdings/Holdings/Lamberton Lake/` with 9 subfolders: Legal, Purchase, Sale, Due Diligence, Financing, Syndication, Pro Forma, Accounting, Reporting | Not mirrored in SharePoint as a unit. SP holds formation docs separately (below) and lender/loan docs, but no equivalent acquisition tree. |
| **Lamberton LP syndication records** | **Dropbox only (apparent)** `ns:4566704256//Bedrock Group/Entities/Bedrock EM Holdings/Holdings/Lamberton Lake/Syndication` (2019-12-17) | SharePoint folder-name search for "Syndication" returns 17 results (Tarheel, ND Communities, Knollwood, Cherrywoods, Fishin, Northgate, Victoria Woods, Shasta Glenn) and **no Lamberton**. See Gaps for method limits. |
| **Lamberton operating records (2017 to 2020)** | Dropbox `ns:7525050192//Michigan/Lamberton Lake (Grand Rapids, MI)/` holds bank statements 2017 to 2020, ~40 vendor folders, utilities, taxes, POH, photos, legacy seller docs | SharePoint `/sites/main/Shared Documents/Operations/Lamberton Lake (Grand Rapids, MI)/` (mod. 2026-04-24) is the live operations home. Dropbox holds the older tail. |
| **Lamberton entity formation** | **SharePoint** `/sites/Corporate-Legal/Shared Documents/Formation Documents/Lamberton Lake MHC LLC` (2026-03-15) | Replicated across ≥6 SP sites: LegalParakeet, ParakeetHome, ParakeetCompanyPortal, main/Accounting & Finance, main/External/Paro & Parakeet, plus `_Archive`. Duplication problem is on the M365 side, not Dropbox. |
| **Entity structure / cap tables / org chart** | Dropbox `ns:4802313104//Org Chart Overview.xlsx` (2020-03-28), 11 tabs | Only consolidated map found anywhere in this survey, but a 2020 snapshot. Partner-level detail also in `Holdco Presentation.pdf` (2020-08-31), same folder. |
| **Entity formation documents (management LLCs)** | Dropbox `ns:4566704256//A2ZMHC/Entities/` holds 5 entities, each with Legal/{Formalities,Agreements} and Taxes/Formalities | SharePoint has parallel `Formation Documents` trees for property-level entities; these five *management* LLCs were not seen there. |
| **Business-line entity trees (Bedrock/A2Z holdings)** | Dropbox `ns:4566704256//` | Partially mirrored at SharePoint `/sites/GoogleBackup/Shared Documents/Holding Companies/` (Bedrock MHC Fund II, A2Z Community Partners), a 2021 Google-era backup, not a live tree. |
| **Cambridge DD, 2023 buy-side** | Dropbox `ns:4436920385//` (via `/Austin Berk/Cambridge MHC Due Diligence Folder`), 17 items numbered 1 to 17, complete | Distinct transaction from the 2025 set below; not duplicates. |
| **Cambridge DD, 2025 sell-side ("SCH")** | Dropbox `ns:12972052483//Cambridge DD 2025/`, 271 files, numbered to 25 with 14 gaps | Different numbering scheme and different counterparty from the 2023 set. Cambridge is the WV community (`Communities/West Virginia/Cambridge (Charles Town, WV)`). |
| **Accounting / month-end close** | **SharePoint** `/sites/main/Shared Documents/Accounting & Finance/` (FY25 activity observed) | Dropbox `ns:4566106320//` stops at 2020-10 and its Monthly Recons cover only Oct to Dec 2019. Dropbox is superseded. |
| **Property operations** | **SharePoint** `/sites/main/Shared Documents/Operations/` | Dropbox `ns:4524714528//Communities` stops 2021-01. Overlapping but superseded; Dropbox retains the deeper pre-2021 vendor/invoice tail. |

## Findings

**1. The folder named for the live deal is empty; the real Lamberton record is somewhere else entirely.**
`ns:11855305057//Lamberton Lake DD Files` (shared_folder_id `4960725313`) returns **zero entries** both non-recursively and recursively, and reports no `descendants_count` or `folder_size`. Meanwhile a keyword search for "Lamberton Lake" across the whole space returns 100+ hits (paginated, `has_more: true`) distributed 62 under `Business Lines`, 25 under `Property Management`, 13 under `Austin Berk`, and **none dated later than 2021** (2019: 5, 2020: 80, 2021: 11). The substantive record is the 9-subfolder ownership tree at `ns:4566704256//Bedrock Group/Entities/Bedrock EM Holdings/Holdings/Lamberton Lake/`, covering Legal/Formation, Purchase/Closing, Due Diligence (incl. Purchase & Sale Agreement, Electrical Evaluations), Financing/3Q2019 Refinancing (Capital One), Syndication, Pro Forma/Original Models, Reporting/Lender Reporting, and a 2019 `Sale` folder. Anyone told "the Lamberton diligence is in Dropbox" would find nothing.

**2. SharePoint is authoritative for the 2026 sale, but Dropbox appears to hold the only copy of the LP syndication file.**
SharePoint carries the live sale: `/sites/main/Shared Documents/External/Lamberton Lake (Sale 2026)/` modified 2026-07-29 (28 days ago), `Lamberton Lake - DD Requirements` 2026-07-29, Q2-2026 Capital One lender reporting 2026-07-22, operations 2026-04-24. Dropbox's newest Lamberton artifact is from 2021. **For the live sale, use SharePoint; Dropbox adds nothing.** However: a SharePoint folder-name search for "Syndication" returns 17 total results covering Tarheel, ND Communities, Knollwood, Cherrywoods, Fishin, Northgate, Victoria Woods and Shasta Glenn, but **no Lamberton Lake**. Dropbox's `…/Lamberton Lake/Syndication` (2019-12-17) therefore looks like the sole surviving copy of the LP subscription/syndication records for the asset now being sold. That is a real exposure in a live transaction and should be verified and copied before any Dropbox decommission.

**3. The 2024-10-26 hypothesis is right about the conclusion and wrong about the evidence.**
Eight of ten mounts do show `modified_time` 2024-10-26, but that field is a mount/permission event, not content, and it is unreliable in both directions. Counter-examples: `Austin Berk` shows 2024-10-26 yet contains files from 2026-08-05; `Cambridge MHC Due Diligence Folder` shows 2026-03-31 yet every file inside is from August 2023. Judged on actual deepest content dates, the space is even colder than the mount stamps suggest:

| Branch | Newest real content | Verdict |
|---|---|---|
| Austin Berk | 2026-08-05 | **LIVE** (one folder) |
| Cambridge - SCH 2025 | 2025-08-25 | Frozen 12 months |
| Team Paper Docs | 2025-06-16 (migration of 2019 stubs) | Frozen |
| Property Management | 2021-01-19 | Frozen |
| Business Lines | 2020-11-12 | Frozen |
| Accounting | 2020-10-06 | Frozen |
| Pipeline | 2020-09-24 | Frozen |
| Reference | 2020-05-12 | Frozen |
| Corporate | 2019-10-07 | Frozen |
| Lamberton Lake DD Files | none | Empty |

**4. The only consolidated entity/cap-table map in the business is a 2020 spreadsheet in a personal folder.**
`ns:4802313104//Org Chart Overview.xlsx` (2020-03-28, 126 KB) contains 11 tabs that resolve exactly the Parakeet / A2Z / personal relationship gap: a property-focused master org chart, a property-management-focused chart splitting the operating companies into software / property-management / utility-collection lines, an employee org chart with five departments, and seven deal-level ownership charts (Lamberton Lake, Wolf Bay, Knollwood, Cherrywoods, Northgate, Rio Vista, Town & Country / Rainbow) plus fund-level charts for BEDROCK I GROUP, Bedrock MHC Fund II LP and Bedrock MHC Fund II GP. It carries entity domiciles, ownership percentages, EINs, and a named LP roster of 58 investors. Caveats: it is six years stale, several formula columns render as `#N/A`, and it sits in a personal folder rather than a governed corporate location. It is nonetheless the highest-value single artifact found in this survey.

**5. Entity formation documents for the five management LLCs live only in `Business Lines`.**
`ns:4566704256//A2ZMHC/Entities/` holds complete formation packets for **A2Z MHC Management**, **A2Z ND MHC Management** (ND MHC Management, LLC), **A2Z AL MHC Management**, **A2Z Knollwood Management**, and **Bedrock MHC**: certificates of formation, executed LLC/operating agreements, IRS Form SS-4s, EIN confirmation letters, a beneficial-ownership form, and 25 Bank of America statements (2017-12 → 2019-12). SharePoint's `Formation Documents` trees cover property-level entities; these five management entities were not seen there. Newest activity 2020-11-02.

**6. Cambridge exists as two different DD sets for two different transactions, and the 2025 one is incomplete.**
The 2023 set (`ns:4436920385//`, reached via `/Austin Berk/Cambridge MHC Due Diligence Folder`) is a clean 1 to 17 numbered request list with no gaps, content dated 2023-08-21 → 2023-08-23. The 2025 set (`ns:12972052483//Cambridge DD 2025/`) uses a different scheme numbered to 25 and has folders for only 11 items. Numbers 1, 4, 5, 8, 9, 13, 14, 15, 17, 19, 21, 22, 23 and 24 have no folder at all. Present-item file counts: utility bills 140, aged receivables 59, rent rolls 31, licenses/permits 30, P&L 3, tax bills 2, and 1 file each for move-in/out, repairs, survey, loss runs and environmental. Total 271 files / 185.2 MB, all uploaded in a single ~5-minute window on 2025-08-25 (02:07 to 02:11 UTC), with a `Request List Tracker.xlsx` at the root. These are complements, not duplicates, but the 2025 set reads as an abandoned mid-flight upload.

**7. `Austin Berk` is 74% of the entire space and functions as an unsorted dumping ground.**
330.72 GB of 445.2 GB. Its root alone holds ~60 loose files with no organizing scheme: seven per-property general-ledger CSVs, two 34 MB / 61 MB investment decks, DD memos for Knollwood Village and Oceanaire, K-1s for three entities, tax returns, a 6.5 MB `inMotion.zip`, and `scratch pad.xlsx`. It contains 22 nested mounts and four departed-employee folders (Jorden Angel, Nicole Wood, Chrissy Fitzgerald, Winnie Bretz; the last containing an entire nested `BEDROCK I GROUP` corporate tree). Any Dropbox decommission has to triage this folder specifically; the other nine mounts together are only 114 GB.

**8. `Team Paper Docs` is structurally empty.**
Nine mounts totalling 3,000 bytes. Every file is a 200-byte `.paper` stub (e.g. `ns:12472914433//Wolf Bay_ Due Diligence Overview.paper`, 2019-01-08) whose content lives in Dropbox Paper rather than in file storage. The mounts are named for real assets: `Current Due Diligence Files`, `BMHCII Quarterly Updates`, `DD Process Overview Files`, `BEDROCK MHC Docs (Archived)`, `Meeting Notes`, `Templates`, `A2Z MHC Docs`, and two Property Management sets. So the index reads as substantive while the bytes are not there. Migrated 2025-06-16; underlying docs are 2019-era.

**9. Pipeline is a closed 2016 to 2020 deal-flow archive of ~45 opportunities.**
`ns:4549709616//_LOIs` holds ~103 files (many docx/pdf pairs and multiple versions of the same LOI; Valley View alone has 8). Named opportunities include Tarheel Portfolio, Mobile Manor, Valley View, Greenspot Village, Mayflower Hills, Knollwood-adjacent deals, Queen City Portfolio, KDM NY Portfolio, Michigan Portfolio, Lakeshore Communities, Longmeadow, Jeffersonville, Shepherdsville, Buena Vista, Blue Belle/Sunnyside/Westhaven, Caribbean MHE, J Bar J Trailer Ranch, and ~25 more. Last LOI 2020-09-24. Sibling folders `New`, `Review`, `Archives` carry the bulk of the 46.3 GB (`New` alone is 926 MB).

**10. Entity-tree and operations-tree portfolios do not reconcile.**
`A2ZCP/Holdings/Single Asset SPVs` lists 13 SPVs (Cherrywoods, Victoria Woods, Wolf Bay, Knollwood Village (Sherman), Northgate, Fishin, Shasta Glenn, Ponderosa, Town and Country, Rio Vista, Oceanaire, ND Communities Portfolio, Mayflower Hills) plus `Fund 1 (A2Z)`; `BMHCII/Holdings` lists 4 more. But `Property Management/Communities` lists 23 community folders across 16 states, and Cherrywoods, Victoria Woods and Northgate have SPV folders with no matching Communities folder. Any portfolio reconstruction from this archive needs both trees plus the 2020 org chart to be trustworthy.

## Sensitive content: locations and categories only

Flagged by location and category; contents not reproduced or extracted beyond what was needed to identify them.

- **Government ID**: `ns:4802313104//Berk_Drivers License.jpg` (driver's licence image, 4 MB, 2020-10-29).
- **Personal financial / tax**: `ns:4802313104//` root: two personal financial statements (`Berk PFS_082020.pdf`, `Berk_PFS_10252020.pdf`), `Berk 2017 Tax Return.pdf`, `Insurance Card.pdf`, and IRS extension-acceptance filings for Austin & Jamie Berk and for A2Z Community Partners LLC.
- **Cap table & investor PII**: `ns:4802313104//Org Chart Overview.xlsx`: entity ownership percentages, EINs, and a roster of 58 named LP investors (individuals, family trusts, IRAs, LLCs) with investment dates and amounts. Also `Holdco Presentation.pdf` in the same folder.
- **Investor tax documents**: `ns:4566106320//Investor K1's`; K-1 PDFs for BEDROCK I GROUP and LAMBERTON LAKE MHC LLC loose at `ns:4802313104//` root.
- **Banking**: `ns:4566106320//Bank Statements`, `ns:4566106320//Mortgage Statements`, `City National Account Documentation.pdf`; `ns:4566704256//A2ZMHC/Entities/Bedrock MHC/Accounting/Banking/` (25 Bank of America statements 2017-12→2019-12, CNB new-account paperwork, and a **beneficial ownership form**); `ns:7525050192//Michigan/Lamberton Lake (Grand Rapids, MI)/Bank Statements/` (2017 to 2020).
- **Tax filings / PPP**: `ns:4566106320//Tax Filings`, `ns:4566106320//PPP Files`, `ns:4566704256//A2ZMHC/Entities/Bedrock MHC/Accounting/Taxes/` (941 overpayment), Form 1065 request for Bedrock MHC Fund II LP.
- **EINs and entity identifiers**: `ns:4566704256//A2ZMHC/Entities/**`: SS-4s and EIN confirmation letters for four entities.
- **Employee PII**: `ns:5940707216//Human Resources/{Employees, Resumes, Contractors, Benefits, Manager Verifications}`; `ns:5940707216//Payroll`; `ns:4802313104//Payroll Reports` (mount); `ns:4802313104//Employee Chart.xlsx`.
- **Securities offering documents**: `ns:4566704256//Bedrock Group/Entities/BMHCII (Fund 2)/Entities/LP/Legal/Subscription/PPM/` and drafts under `bedrock group/marketing/collateral/Deliverables/`.
- **Resident data**: rent rolls, move-in/move-out and aged-receivables reports throughout `ns:12972052483//Cambridge DD 2025/` and `ns:4436920385//`; leases under `Communities/*/Lease Templates` and `10. Current Leases`.

## Gaps

- **`Lamberton Lake DD Files` (`ns:4960725313`)**: enumerated successfully and is genuinely empty; this is a finding, not a coverage gap. Noted here because "empty" and "unreachable" must not be confused.
- **Syndication uniqueness is inferred, not proven.** The claim in Finding 2 rests on `sharepoint_folder_search`, which matches **folder names only**. Lamberton syndication documents could exist in SharePoint inside a differently-named folder (e.g. under `Formation Documents`, `External`, or a closing binder) and would not surface. Confirm by content search or by opening `/sites/main/.../Lamberton Lake (Sale 2026)/` before treating Dropbox as the sole copy.
- **22 nested mounts under `Austin Berk` not descended into**: `A2Z- Lasso Partners`, `Lasso MHC Portfolio`, `KeyBank-Lasso - MHP Portfolio`, `Tar Heel MHC Portfolio - Seller`, `Lender Diligence - PSE & OBO`, `Shared Loan Diligence`, `Shared Loan Diligence (1)`, `2021 JLT Reports`, `tresvista`, `Vangsness-A2Z`, `Mobile Manor - DD Files`, `A2Z Community Partners`, `Discovery Documents`, `Photos and More`, `E Town Pics`, `Water Utility Reads`, `Erie MHP Tour (April 2020)`, `Payroll Reports`, `turf holdings`, `Migrated Paper Docs`, plus the two examined. Reason: breadth-before-depth budget; this branch alone is 330 GB and each mount is a separate namespace. `Payroll Reports` and `Shared Loan Diligence` are the highest-priority follow-ups (payroll PII; a Gulf Breeze closing binder was already surfaced incidentally at `ns:2310939153//Closing Binder/`).
- **`Property Management` mounts `Refuse Specialist to review` (`ns` unresolved) and `_5200`**: listed at level 1, not descended.
- **`Property Management/Communities` full recursive sweep abandoned**: the tree is very deep (Lamberton alone has ~40 vendor subfolders). Community *counts* per state are exact; per-community file counts are not established.
- **`Pipeline/New`, `Review`, `Archives`, `__Miscellaneous`**: not enumerated below level 1. Together they hold ~45 GB, the bulk of the mount. Only `_LOIs` and `Templates` were examined.
- **`Corporate` levels 3+**: only `Analysis` (4 subfolders) and `Human Resources` (8 subfolders) were opened. `Finances`, `Payroll`, `Technology`, `Branding`, `Facilities`, `Travel`, `Stationary`, `Service Providers`, `Templates` were listed at level 2 only.
- **`Accounting` sub-branches**: `Weekly Exports`, `Investor Reporting`, `Lender Quarterly Reporting`, `The Source`, `Selection Items Requested`, `Bank Statements`, `Investor K1's`, `Tax Filings` were not enumerated internally, so the stated period coverage (2018 → 2020-10) is derived from level-1 and `Monthly Recons` evidence and may understate depth in those folders.
- **`Team Paper Docs` Paper content not retrieved.** The `.paper` stubs point to Dropbox Paper documents; whether that content is still live and readable was not tested. Nine mounts, only `Current Due Diligence Files` (3 stubs) was opened.
- **`MoMa Lending`, `NewCo`, `Reference`, `Business Lines/Bedrock Group/{Admin, Legal, Marketing, Strategy}`**: level-2 structure captured, contents not enumerated.
- **SharePoint side surveyed only for Lamberton Lake and "Syndication".** The Accounting & Finance and Operations overlap claims rest on folder paths surfaced incidentally in those two searches, not on a systematic SharePoint inventory. `sharepoint_folder_search` reported `totalResultCount: 18900` for the Lamberton query, which is an index-wide figure and should not be read as a Lamberton document count.
