# SharePoint `sites/main`: Inventory

> **Source-state paths, 2026-08-31.** The numbered `1. …` through `8. …` community subfolders quoted on this page describe `/sites/main/Shared Documents/` **as it exists today**. They are deliberately left as written: that estate is read-only (see [[CLAUDE]]) and a Brain page that renumbered them would misdescribe live reality and send people to folders that do not exist. The **Birdcage** template is unnumbered per Austin's 2026-08-31 ruling. See [[10-Business/sharepoint/target-structure]].

**What this is:** The full inventory of `/sites/main`, 2.88 TB across 24 top-level branches, surveyed before Albert's migration so nothing moves blind.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

Surveyed: 2026-08-26 | Account: austin@parakeetcommunities.com (Austin Berk) | Coverage: all 24 top-level branches of the `Shared Documents` root enumerated; level 2 enumerated for all 24; level 3 enumerated for the branches named in scope (Accounting & Finance → Monthly Close / Parakeet Audit; Sales → Agreements_Closing Docs → Buyers Closing Files; Operations → community template + Bay Oaks; Construction → Bay Oaks; Asset Management & Finance → Due Diligence Files). One branch (`External`) hit a listing cap. See Gaps.

Drive: `b!njiksR7MZEmG_M8Yw6axW2jvA8VrjgNBiM1tPu0OIH9brRpFexZsTZOcYyA732ur`
Site: `https://parakeetcommunities.sharepoint.com/sites/main`

## Summary

This is a ~2.88 TB single-library repository holding essentially every operating, deal, construction, and finance record Parakeet has produced since 2021. It is organized by **function at the top level and by community at the second level**, but the same community appears under at least five different naming conventions across branches (`Bay Oaks Village I & II (Panama City, FL)` in Operations, `BAY OAKS VILLAGE I` + `BAY OAKS VILLAGE II` in Construction, `Bay Oaks Village_Due Diligence Files` in Asset Management, `Panama City Communities` in External), so no single community key joins the tree. Five of the 24 branches carry 96% of the bytes (Operations, Asset Management & Finance, Acquisitions, External, Construction) and three of those are effectively parallel universes of the same deal material. The single biggest problem is **structural duplication at the multi-gigabyte scale**. Flood/site elevation certificates exist twice at byte-identical 4.71 GB, due diligence material exists in four independent hierarchies, and community photos exist in at least eight. That means "where is that file" has no correct answer, only several partially-correct ones. A secondary and more urgent problem: sensitive HR, payroll, cap-table, and buyer-PII material sits in the same library as broadly-shared operational folders (see Findings 9 and 10).

A governance artifact already exists and is being ignored: `Administrative/Folder Structure Glossary.xlsx` (5.0 MB) and `Administrative/Folder Structure Tracker_Outline.xlsx` (675 KB) define the intended taxonomy. The live tree has drifted well past it.

## Taxonomy

Root: 24 folders + 1 stray file (`FolderOutput`, 30.0 MB, no extension). Sizes are the folder totals SharePoint reports.

```
Shared Documents/                                              ~2.88 TB
├── Operations/                                   977.58 GB  ← largest branch
│   ├── 71 community folders, "Name (City, ST)"              community system of record
│   │   └── each: 1. Asset Management / 2. Communication and Photos /
│   │             3. Facilities / 4. Insurance / 5. Legal /
│   │             6. Notes and Templates / 7. Operations / 8. Reports
│   ├── _Archive Communities/                     114.43 GB  36 disposed/never-owned assets
│   ├── _Marketing/                               113.61 GB  photo & video mass
│   ├── 24 other "_" functional folders                      _Training, _Legal Notices, _Eviction Folder,
│   │                                                        _Hurricane Related, _rent increase, _Transitions,
│   │                                                        _Operations Report, _Weekly Reports, _utilites, …
│   └── _Property Template (City, State)/                    the 8-folder template above (mostly empty)
├── Asset Management & Finance/                   753.85 GB
│   ├── Due Diligence Files/                      652.96 GB  60 community DD folders  ← 85% of branch
│   ├── Budgets/ 15.13 GB · Quarterly Reports/ 12.28 GB · Third Party Reports (Post-Acq)/ 8.93 GB
│   ├── Monthly Reports/ 7.97 GB · Geiger Management/ 6.46 GB · Flood Elevation Certificates/ 4.71 GB
│   ├── Closing Documents/ 4.07 GB · Loan Documents/ 3.84 GB · Utilities/ 3.72 GB · Taxes/ 1.80 GB
│   └── ~50 more: CapEx, Insurance, Wire Info, Property Tax Bills, Rent Roll Audits, Prospectus
│       Documents, Cost Seg Reports, Waterfall Models, EOS, Claude Workflows (14.07 GB), …
├── Acquisitions/                                 556.58 GB  deal pipeline (pre-close)
│   ├── 2. Live Deals/ 395.73 GB · _Archives1/ 54.97 GB · GoPro SD Backup 10-29-24/ 24.01 GB
│   ├── PH Projects/ 20.34 GB · Lender Outputs/ 18.11 GB · 1. In Contract/ 14.13 GB
│   ├── _Misc/ 11.73 GB · _Unsorted Park Videos/ 7.55 GB · Midnight Marauders/ 6.42 GB
│   └── + 10 versions of `historical capex data tape*.xlsx` loose in the branch root
├── External/                                     314.89 GB  counterparty / lender / diligence share-out
│   ├── Rodesi - Parakeet Website/ 27.93 GB · Steiner Internal DD/ 20.28 GB
│   ├── Berkadia/ 10.00 GB · New Executive Hire Portfolio Materials - May 2025/ 10.47 GB
│   ├── Leslie Croft - Kickoff Materials/ 10.16 GB · Newmark DD Equity/ 8.52 GB
│   ├── 14× `Parakeet DD Folder - <Counterparty>` (Rockpoint, Wafra, Tiger, Soroban, Pulte,
│   │   Corigin, Durational, SCP, Spectrum, RWN, West End, Brean, Morningview, Joel Gantcher)
│   ├── WSRED - JREFII Tranche 2 / 3 / 4, WSRED Appraiser  (lender data-room drops)
│   ├── Deal/dispo: Lamberton Lake (Sale 2026), Lamberton Lake Nov 2025 DD, Lamberton Seller File,
│   │   Kippy DD, Cambridge DD 2025, Royal Oaks DD 8.6.26, Ascent DD Feb, Hunter Springs Data Room
│   ├── Photo drops: ARD POH Pictures, Datacomp POH Pictures, BRUN POH Photos, OM Pictures, Steiner Photos
│   ├── Utility/tax: Mass Historical Utility Bills, MA Tax Bills, Northgate Utility, Cleartrail utilities,
│   │   Real Advice - Tax Info, Real Estate Tax Disbursement, Ryan Tax Data Drop, Cost Segs
│   └── Loan: MRC Loan Tranche 2 / 3, MRC Tranche 2 Signed Docs, RRA Bridge Loan, Parakeet SE Portfolio Loan
├── Construction/                                 136.38 GB
│   ├── 71 ALL-CAPS community folders                        each: CONTRACTS / DEVELOPMENT / MAPS /
│   │                                                        PHOTOS / PROJECTS / PROPERTY INFORMATION
│   ├── __SITE ELVATION CERTIFICATES/ 4.71 GB [sic]          duplicate of Asset Mgmt branch
│   ├── ___VLAD___/ 2.57 GB · ___Meter Can Recon File___/ 844 MB
│   ├── __SIGNAGE/ 634 MB · __COMMUNITY SIGNS/ 552 MB        two signage folders
│   ├── _FLOOR PLANS FILE/ 415 MB · zzzzzzFLOOR PLANS/ 5.6 MB  two floor-plan folders
│   └── __SITE PLANS/ 91 MB · _SCOPES/ 14 MB · ___EXCEL FILES___/ 28 MB
├── Parakeet Homes/                                42.58 GB  home inventory / titles / dealer ops
│   ├── Park owned assets/ 28.09 GB · Manufacturers/ 8.85 GB · Titles/ 4.73 GB
│   └── Dealership Information, Home Lending, Tiny Homes, 21st Mortgage title batches
├── Accounting & Finance/                          21.26 GB
│   ├── Accounting Team Files/ 6.80 GB · Parakeet Audit/ 3.50 GB · Bank Information/ 2.25 GB
│   ├── Tax Filings/ 2.14 GB · Vendor Packages/ 1.40 GB · Monthly Close/ 1.36 GB
│   ├── __Pre Avid_Bills & Invoices/ 1.15 GB · FP&A/ 978 MB · Monthly & Quarterly Taxes/ 485 MB
│   └── Citrin Reports, Formation Documents, Credit Applications, Balance Sheet Recon,
│       GL BALANCE SHEET, JPM Rec Accounts, Prepaid and Accurals, Census Reports, CASS Uploads
├── Analytics & Reporting/                         14.78 GB  Lender Reporting/ 6.74 GB, Tableau, dashboards
├── Marketing/                                     11.47 GB  Community Photos/ 10.45 GB, Branding, Brochures
├── Properties/                                     8.92 GB  Cambridge, Geiger Key, Lamberton Lake +
│   └── To Clean Up Remaining Files/ 8.24 GB               ← 92% of the branch is an unsorted dump
├── Executive/                                      8.62 GB  G&A/ 2.65 GB, Jadian, board/strategy, cap table
├── Human Resources/                                5.35 GB  employee files, payroll, benefits, workers comp
├── _Errors/                                        5.09 GB  flat legacy dump (see Finding 5)
├── Corporate/                                      4.66 GB  Minutes & Notes/ 2.83 GB, Formation Documents/ 1.16 GB
├── Harry & Lloyd/                                  3.35 GB  Corporate/ 3.09 GB + State Association Membership
├── Market Data/                                    3.33 GB  JLT Reports/ 2.91 GB, market/expense surveys
├── Administrative/                                 3.09 GB  Corporate/ 3.09 GB + the folder-structure glossaries
├── Sales/                                          2.49 GB
│   ├── External Assets_third party sites_ads/ 1.76 GB
│   ├── Agreements_Closing Docs/ 331 MB                     ← Buyers Closing Files/ 319 MB
│   ├── Training Materials and Resources/ 270 MB · Reporting/ 35 MB · Lenders/ 19 MB
│   └── Commissions, Dealer Licenses, Community Manager Contacts, Home Listing Photos, zz_ARCHIVE
├── Jadian-Parakeet/                                2.17 GB  Corporate Model/ 634 MB, Parakeet Master Model/ 835 MB
│                                                            + 5 copies of Monthly Payroll Analysis_2024
├── Company Documents/                              1.49 GB  Industry Education/ 1.43 GB, Core Values, SOPs
├── Investor Relations/                             577 MB   BMHCII/ 558 MB, A2Z Fund I, IR templates
├── _Archive/                                       545 MB   2 folders: KEET Asset Mgmt (ZS), Analytics & Reporting
├── Acquisitions (ZS)/                              24.6 MB  hollow mirror of Acquisitions (see Finding 6)
├── CC26/                                           126 KB   in contract / Office only / other data / templates
└── FolderOutput (file, 30.0 MB, no extension)
```

### Accounting & Finance → Monthly Close (13 children)
`07212026 SCANS` (468 MB) · `2025` (220 MB) · `2026` (59.5 MB) · `MASTER Files` (109 MB) · `FY25 Tax bills` (107 MB) · `Audit 2025 - Temporary for PH` (249 MB) · `Temporary Audit- Lease Agreements` (110 MB) · `SILVER - PL - RO - Bank Statements & Recons` (25.9 MB) · `Congress` (6.9 MB) · `S&U Filings` (4.6 MB) · `AM Fee & JREFII Invoice` · `POH & REO expense reclass` · `Accounting Team Calendar.xlsx`

Note: two of the thirteen are labelled "Temporary" and one is a raw scan dump keyed by date, not period.

### Accounting & Finance → Parakeet Audit (5 children, clean)
`Parakeet Audit 2022` (840 MB) · `2023` (454 MB) · `2024` (1.71 GB) · `2025` (452 MB) · `MA UA 2022` (41.8 MB)
Sibling: `Parakeet Audit-Sony/` (172 MB) sits outside this folder at the branch root.

### Sales → Agreements_Closing Docs (6 children)
`Buyers Closing Files` (319 MB) · `Agreements_standard` (1.43 MB) · `Closing Docs` (7.84 MB) · `Renter Docs` (373 KB) · `Title Procedural Docs_FFT` (743 KB) · `working_Word files` (1.61 MB)

**Buyers Closing Files** uses a real, enforced convention: `Asset#_Type of Transaction_Last Name_Move-in Date` (the naming rule is itself an empty folder acting as documentation). Live examples: `FOX-27_Financed_Rojas-Herrera_09-18-2026`, `SOUTH-47_Financed_Landry_08-21-26`, `PARK-41_Finance_Mobley_08-01-2026`, `HS-13_Cash_Yousman_07-16-26--ON HOLD--Eviction Home`. Status buckets: `__Sold_Closed & Funded` (159 MB), `__Leases with Option to Purchase (LOP)` (64.6 MB), `__Cancelled Contracts` (26.1 MB). This is the best-governed folder in the entire library.

### Community footprints (complete lists)

**Operations, 71 communities** (all named `Name (City, ST)`):
American (Auburn, MA) · Apple Creek (Bismarck, ND) · Applegate (Deland, FL) · Auburn Ridge & Duplexes (Auburn, GA) · Bay Oaks Village I & II (Panama City, FL) · BelleHaven (Clearwater, FL) · Brunswick Estates (Brunswick, GA) · Cambridge (Charles Town, WV) · Carley's (Miami, FL) · Central (Cocoa, FL) · Congress (West Palm Beach, FL) · Countryside (Mandan, ND) · Crystal Acres (Crystal River, FL) · Druid Oaks (Brunswick, GA) · Everglades (Clewiston, FL) · Fox Creek (Fountain Inn, SC) · Geiger Key (Key West, FL) · Great Oak RV Resort (Kissimmee, FL) · Greene Pointe (Summerville, SC) · Gulf Breeze (Hudson, FL) · Harbour (Cocoa, FL) · Hendersons (Clewiston, FL) · Hershey Park (Summerville, SC) · Hunter Springs (Crystal River, FL) · J Bar J Estates (Miami, FL) · Lake Saunders (Mt Dora, FL) · Lake Wales (Lake Wales, FL) · Lamberton Lake (Grand Rapids, MI) · Lucky Clover (Melbourne, FL) · Mayflower (Plymouth, MA) · McGregor Downs (West Columbia, SC) · Meadow Woods (Lunenburg, MA) · Monson (Monson, MA) · Nalls Ct (Celwiston, FL) · Northgate MH & RV Park (Mims, FL) · Oakside MHP (Goose Creek, SC) · Oceanaire (New Symrna Beach, FL) · Ormond Beach Oasis (Ormond Beach, FL) · Palm Haven Estates (Panama City, FL) · Palm Spring Estates (Tarpon Springs, FL) · Paradise Lakes (Deltona, FL) · Paradise Palms (Lakeland, FL) · Parktown (Mandan, ND) · Parkwood (West Columbia, SC) · Redlands (Miami, FL) · Regency I & II (Savannah, GA) · River Oaks (Ruskin, FL) · Riverwalk (Gibsonton, FL) · Riviera (Miami Gardens, FL) · Royal Oaks (Vero Beach, FL) · Royal Palm (Clewiston, FL) · Sea Shells (Cape Canavaral, FL) · Shady Acres (Brunswick, GA) · Shady Oaks (Miami, FL) · Shell Pointe (Ruskin, FL) · Shirley's · Silver Breeze (Titusville, FL) · Silver Hill (Columbia, SC) · Southgate (Cape Canaveral, FL) · Su-Rene (Vero Beach, FL) · Terrace Crossing (Thonotosassa, FL) · The Oaks (Thonotosassa, FL) · Town & Country (Jacksonville, FL) · Tradewinds (Cocoa, FL) · Triple S Marina (Atlantic Beach, NC) · Vantage Oaks (Okeechobee, FL) · Westwood (Ormond Beach, FL) · Whispering Pines Estates (Auburn, MA) · Whispering Pines MH & RV (Titusville, FL) · Windward Knoll (Thonotosassa, FL) · Wolf Bay (Elberta, AL)

**Construction, 71 communities** (ALL CAPS, no city/state):
AMERICAN · APPLEGATE · AUBURN RIDGE · AVALON MHP (0 B) · BAY OAKS VILLAGE I · BAY OAKS VILLAGE II · BELLE HAVEN · BRUNSWICK ESTATES · CAMBRIDGE · CARLEY'S MHP · CENTRAL · CONGRESS · CREEK WOOD (0 B) · CRYSTAL ACRES · DRUID OAKS · EVERGLADES MHC · FOX CREEK · GEIGER KEY MARINA RV · GREAT OAKS RV · GREENE POINTE · GULF BREEZE · HARBOUR · HENDERSONS MHC · HERSHEY PARK · HUNTER SPRINGS · INLAND VILLAGE - POSSIBLE · J BAR J · LAKE SAUNDERS · LAKE WALES · LAKESIDE ESTATES · LAMBERTON LAKE · LUCKY CLOVER · MAYFLOWER · MCGREGOR DOWNS · MEADOW WOODS · MONSON · NALLS COURT · NORTHGATE · OAKSIDE · OCEANAIRE · ORMOND BEACH OASIS · PALM HAVEN ESTATES · PALM SPRINGS ESTATES · PARADISE LAKES · PARADISE PALMS · PARKWOOD · REDLANDS · REGENCY I & II · RIVER OAKS · RIVERWALK · RIVIERA PARK · ROYAL OAKS · ROYAL PALM · SEASHELLS · SHADY ACRES · SHADY OAKS · SILVER BREEZE · SILVER HILL · SOUTHGATE · SU-RENE · TERRACE CROSSINGS · THE OAKS · TOWN & COUNTRY · TRADEWINDS · TRIPLE S MARINA VILLAGE · VANTAGE OAKS · WESTWOOD · WHISPERING PINES FL · WHSIPERING PINES MA [sic] · WINDWARD · WOLF BAY

**Delta between Operations and Construction**: both have 71, but they are not the same 71:
- In Operations, absent from Construction (6): Apple Creek (ND), Countryside (ND), Parktown (ND), Shell Pointe, Shirley's, Geiger Key appears only as `GEIGER KEY MARINA RV`.
- In Construction, absent from Operations (4): AVALON MHP (0 B), CREEK WOOD (0 B), INLAND VILLAGE - POSSIBLE, LAKESIDE ESTATES.
- Name drift on the same asset: `Windward Knoll` / `WINDWARD` · `Sea Shells` / `SEASHELLS` · `Riviera (Miami Gardens)` / `RIVIERA PARK` · `Nalls Ct` / `NALLS COURT` · `Great Oak RV Resort` / `GREAT OAKS RV` · `Palm Spring Estates` / `PALM SPRINGS ESTATES` · `Terrace Crossing` / `TERRACE CROSSINGS` · `Whispering Pines Estates` / `WHSIPERING PINES MA`.

All eight assets named in the assignment were confirmed present: Bay Oaks Village I and II, Auburn Ridge, Terrace Crossing (Thonotosassa FL), Palm Haven Estates (Panama City FL), Harbour, Crystal Acres, Lamberton Lake.

**Asset Management & Finance → Due Diligence Files, 60 community DD folders** (suffix `_Due Diligence Files`, four exceptions use `(City, ST)`): 3 Geiger · Applegate · Auburn Ridge & Duplexes · Baker Mass 3 Park Port · Bay Oaks Village · Belle Haven · Brunswick Estates · Cambridge · Carleys · Central · Congress · Crystal Acres · Druid Oaks & Shady Acres · Everglades · Fox Creek (Fountain Inn, SC) · Geiger Key (Key West, FL) · Great Oak RV Resort · Greene Pointe · Gulf Breeze · Harbour · Henderson · Hershey Park · Hillard Portfolio (Silver Hill) · Hunter Springs · J Bar J · Lake Saunders · Lake Wales · Lamberton Lake · Lucky Clover · Mayflower · McGregor Downs · Meadow Woods · Monson · Northgate MH & RV Park · Oakside · Oceanaire · Ormond Beach Oasis · Palm Haven Estates · Palm Spring Estates · Paradise Lakes · Paradise Palms (Lakeland, FL) · Parkwood · Regency I & II · River Oaks · Riviera · Royal Oaks (`_Due Dilligence` [sic]) · Royal Palm · Sea Shells · Shady Oaks · Silver Breeze · Southgate · Steiner Portfolio · Su-Rene & Redlands · Town & Country (`_Due Diligence FIles` [sic]) · Tradewinds · Triple S Marina · Vantage Oaks · Westwood · Whispering Pines Mass · Whispering Pines MHRV · Wolf Bay. Plus one loose 3.07 GB video, `GH010152.MP4`, at the branch root.

**Operations → _Archive Communities, 36 disposed/never-owned assets**: Congress · Central · Crystal Acres · Everglades · Wolf Bay (these five are prefixed with 4 to 5 underscores and also live as active Operations folders) · Bee's RV Resort · Cedar Grove (Kernersville, NC) · Cherrywoods · Colonial (New Bern, NC) · Fishin · Kimball Estates · Knollwood Village (Sherman) · Lake Saunders (Mt1. Dora, FL) [sic] · Lake Toho RV Resort (FL) · Lambeth (Winston Salem, NC) ×3 variants · Mobile Manor (Rosedale, MD) ×3 variants · Moores Hill · Northgate · Parkwood (Winston Salem, NC) ×2 variants · Plattsburgh · Ponderosa · Rio Vista · Shasta Glenn · University · Valley View (Roseburg, OR) ×3 variants · Vandemere (Greenville, NC) ×3 variants · Victoria Woods

## Authoritative locations

| Document set | Canonical path (recommended) | Competing copies |
|---|---|---|
| Community operating file | `Operations/<Name (City, ST)>/` (8-folder template, 71 assets) | `Construction/<NAME>/` (71) · `Properties/` (3) · `Operations/_Archive Communities/` (36, 5 overlap live assets) |
| Due diligence (closed deals) | `Asset Management & Finance/Due Diligence Files/<Name>_Due Diligence Files/` (652.96 GB, 60) | `Acquisitions/2. Live Deals/` (395.73 GB) · `Operations/<Name>/1. Asset Management/Due Diligence - Buyer/` · `External/*DD*` (Kippy DD, Cambridge DD 2025, Ascent DD Feb, Royal Oaks DD 8.6.26, CAMMHC Due Diligence, Shell Pointe DD File, Lamberton Lake Nov 2025 DD, ND Communities, Hunter Springs Data Room, Steiner Internal DD, Steiner Additional DD, `don't use_Cambridge Due Diligence Materials`); **4 hierarchies** |
| Flood / site elevation certificates | `Asset Management & Finance/Flood Elevation Certificates/` (4,709,027,380 B) | `Construction/__SITE ELVATION CERTIFICATES/` (4,709,027,380 B); **byte-identical, 4.71 GB each** |
| Site plans / maps / parcels | `Construction/__SITE PLANS/` (91.4 MB) | `External/Site Maps/` (66.6 MB) · `External/FL Maps & Surveys/` (184 MB) · `External/Parcel Outlines/` (88.3 MB) · `Asset Management & Finance/Permanent Lot Map/` (199 MB) · `Construction/<NAME>/MAPS/`; **6 locations** |
| Floor plans | `Construction/_FLOOR PLANS FILE/` (415 MB) | `Construction/zzzzzzFLOOR PLANS/` (5.6 MB) |
| Community signage | `Marketing/Signage/` (2.35 MB) + `Marketing/Signage Catalog.pdf` | `Construction/__SIGNAGE/` (634 MB) · `Construction/__COMMUNITY SIGNS/` (552 MB) · `Operations/_community signage/` (658 MB); **4 locations, 1.84 GB** |
| Community photos / video | `Marketing/Community Photos/` (10.45 GB) | `Operations/_Marketing/` (113.61 GB) · `Operations/<Name>/2. Communication and Photos/` · `External/OM Pictures/` (2.99 GB) · `External/Steiner Photos/` (3.96 GB) · `External/Datacomp POH Pictures/` (846 MB) · `External/ARD POH Pictures/` (350 MB) · `External/BRUN POH Photos/` (118 MB) · `External/Great Oak Photos/` (15 MB) · `Acquisitions/_Unsorted Park Videos/` (7.55 GB) · `Acquisitions/GoPro SD Backup 10-29-24/` (24.01 GB); **10 locations** |
| Closing documents / binders | `Asset Management & Finance/Closing Documents/` (4.07 GB) | `External/Closing Binders/` (1.95 GB) · `Investor Relations/Closing Binders/` (1.08 GB) · `Sales/Agreements_Closing Docs/Closing Docs/` · `External/PSE Closing Documents/` · `External/JREF II Closings/` · `Acquisitions/Post-Closing Meeting Agenda/`; **6 locations** |
| Budgets | `Asset Management & Finance/Budgets/` (15.13 GB) | `Analytics & Reporting/Budget Files/` (1.13 GB) · `Investor Relations/2023 Property Level Budgets/` + `2024 Budgets/` + `1H OpCo Budget/` · `External/2023 Budgets Parakeet/` + `2024 Budget Upload DW/` + `2026 Budgets - Jadian/` + `_Q42024 Budget Upload/` · `Acquisitions/2023 Budgets/` · `Harry & Lloyd/Corporate/2023 Budgets/`; **10 locations** |
| Formation / entity documents | `Corporate/Formation Documents/` (1.16 GB) | `Accounting & Finance/Formation Documents/` (254 MB) · `Asset Management & Finance/Corporate Entities/` (1.6 MB) |
| Loan documents | `Asset Management & Finance/Loan Documents/` (3.84 GB) | `Executive/MRC Loan Documents/` (73.8 MB) · `External/Loan Docs/` (79.4 MB) · `External/MRC Loan Tranche 2/` (791 MB) + `Tranche 3/` (2.03 GB) + `MRC Tranche 2 Signed Docs/` (201 MB) · `External/Baker Loan Docs/` (0 B) · `Asset Management & Finance/Property & Portfolio Mortgage Documents/` (1.30 GB); **7 locations** |
| Insurance | `Asset Management & Finance/Insurance/` (1.39 GB) | `Accounting & Finance/Insurance Policies/` (4.3 MB) · `Market Data/Insurance/` (5.8 MB) · `External/IOA Policies/` (0 B) · `Operations/<Name>/4. Insurance/` |
| Cost segregation | `Asset Management & Finance/Cost Seg Reports/` (202 MB) | `Asset Management & Finance/Cost Seg Studies/` (0 B) · `External/Cost Segs/` (79.8 MB) · `External/Source Advisors/` (36.6 MB) · `External/PCA - Source Advisors/` (210 MB) |
| ESG | `Corporate/ESG/` (6.6 MB) | `Asset Management & Finance/ESG/` (13.0 MB) · `Acquisitions/ESG Jadian/` (44.0 MB) · `External/ESG DD Checklist - Jadian/` (5.7 MB) |
| Property data sheet | `Asset Management & Finance/Property Data Sheet/` (89.7 MB) | `Construction/Property Data Sheet 6.12.2026.xlsx` · `Sales/Portfolio_Property Data Sheet_07-16-2026.xlsx` · `Asset Management & Finance/Property Data/` (29 KB); three different "current" dates |
| Home / POH inventory & titles | `Parakeet Homes/` (Park owned assets 28.09 GB, Titles 4.73 GB) | `Asset Management & Finance/POH/` (23.8 MB) · `External/4 Star Homes/` + `Parakeet Homes/4 Star Homes/` · `External/Scenic View Titles/` · `External/Fast Title/` · `Parakeet Homes/Titles for 21st Mortgage 012024/` |
| Buyer closing files (home sales) | `Sales/Agreements_Closing Docs/Buyers Closing Files/` | none found; **clean, best-governed set in the library** |
| Audit | `Accounting & Finance/Parakeet Audit/` (3.50 GB, 2022 to 2025) | `Accounting & Finance/Parakeet Audit-Sony/` (172 MB) · `Accounting & Finance/Monthly Close/Audit 2025 - Temporary for PH/` (249 MB) · `External/JREFI - Audit/` (284 MB) · `External/Jadian Audit Financials/` · `External/Jadian - Audit Support Request/` (0 B) · `Human Resources/Audits/` (55 MB) |
| Folder-taxonomy governance | `Administrative/Folder Structure Glossary.xlsx` (5.0 MB) | `Administrative/Folder Structure Tracker_Outline.xlsx` (675 KB) · `Administrative/New Document Checklist for SharePoint.xlsx` (250 KB) |

## Findings

1. **`Flood Elevation Certificates` is stored twice at byte-identical size: 4.71 GB duplicated.** `Asset Management & Finance/Flood Elevation Certificates/` and `Construction/__SITE ELVATION CERTIFICATES/` both report exactly **4,709,027,380 bytes**. This is the single cleanest deduplication win in the library and the byte match makes it safe to verify mechanically. (Construction's copy also carries a typo: "ELVATION".)

2. **Due diligence material lives in four independent hierarchies totalling ~1.06 TB.** `Asset Management & Finance/Due Diligence Files/` (652.96 GB, 60 communities) is the largest and most complete; `Acquisitions/2. Live Deals/` (395.73 GB) is the pre-close pipeline; `Operations/<Name>/1. Asset Management/Due Diligence - Buyer/` holds per-community buyer DD; and `External/` holds at least 12 separate DD folders for outside parties. Same underwriting models appear in three of the four. For example, `Steiner Updated Model` was found at four distinct paths under `Operations/The Oaks (Thonotosassa, FL)/` and `Operations/Riverwalk (Gibsonton, FL)/`, one of them nested two levels deep inside another copy of itself (`.../1. Asset Management/Steiner Portfolio (FL)/Due Diligence - Buyer/Underwriting/Steiner Updated Model`).

3. **Operations and Construction disagree on which communities exist and what they are called.** Both branches carry 71 community folders, but 6 Operations assets have no Construction folder (Apple Creek, Countryside, Parktown, Shell Pointe, Shirley's, plus a Geiger naming mismatch) and 4 Construction folders have no Operations counterpart (AVALON MHP and CREEK WOOD are both 0 bytes; INLAND VILLAGE - POSSIBLE is a prospect, not an asset; LAKESIDE ESTATES). Eight assets are spelled differently between the two, including one outright typo (`WHSIPERING PINES MA`). Any script that joins Operations to Construction on community name will silently drop or mismatch ~18 assets.

4. **Five communities exist simultaneously as live Operations folders and as archived ones.** `Operations/_Archive Communities/` contains `_____Congress (West Palm Beach, FL)` (2.32 GB), `____Central (Cocoa, FL)` (19.52 GB), `____Crystal Acres (Crystal River, FL)` (8.96 GB), `____Everglades (Clewiston, FL)` (0 B) and `____Wolf Bay (Elberta, AL)` (15.69 GB), while all five also exist as active `Operations/<Name (City, ST)>/` folders. That is **46.5 GB of shadow copies of currently-owned assets sitting in an archive folder**, distinguished only by a leading run of underscores. Central's archive copy (19.52 GB) is roughly the same size as its live copy (20.34 GB).

5. **`_Errors/` (5.09 GB) is an unstructured legacy dump with no owner.** It holds ~30 numbered DD-request folders (`No.1-` through `No.26-`, all 0 bytes), plus several hundred loose files spanning 2017 to 2022: recorded mortgages and UCC filings, Phase I environmental reports for six communities, rent rolls, bank statements, 1040 Schedule Es, tenant compliance notices, and ~40 loose JPGs. Some of it is legally significant (recorded assignments of mortgage, title insurance policies, entity formation documents for Lamberton Lake MHC LLC and five affiliates) and it is not indexed anywhere else. Two near-duplicate pairs are visible in the root alone (`03 - Amended and Restated Mortgage...` appears twice at 1,889,166 B and 1,884,457 B; `21-340192.2_Phase_I_Report_-_Triple_S_Marina_Village` appears twice at identical 33,795,599 B).

6. **`Acquisitions (ZS)/` is a hollow 24.6 MB skeleton of `Acquisitions/` (556.58 GB).** It reproduces 16 of the parent's folder names (`1. In Contract`, `2. Live Deals`, `_Archives1`, `_Misc`, `_New Hire`, `_Templates`, `_Unsorted Park Videos`, `GL`, `Midnight Marauders`, `Notes`, `PH Projects`, `Projects`, `RV Strategy`, `Wire Requests`, …) of which **11 are 0 bytes**. The only real content is `1. In Contract` (9.87 MB), `2. Live Deals` (13.9 MB), `_Archives1` (485 KB) and a loose `acq.txt` (373 KB). It reads as an abandoned personal reorganization attempt and is actively misleading: a user searching "In Contract" gets two hits, one of them empty.

7. **Ten versions of the same workbook sit loose in the `Acquisitions/` root.** `historical capex data tape.xlsx` plus `v2` through `v9` (710 KB → 1,013 KB, monotonically growing), 9.16 MB across 10 files with no indication which is current. The same pattern recurs in `Jadian-Parakeet/` with **five** copies of `Monthly Payroll Analysis_2024` (`.xlsx`, `-PKC-AP-FSG37M3.xlsx`, `v2`, `v3`, `v4`; 7.0 to 16.2 MB each, 44.8 MB total, and this is payroll data, see Finding 9) and in `Corporate/Minutes & Notes/Board Meetings/Board Meeting 2026-03/` with seven variants of the March 2026 board deck (`v5 DRAFT FINAL ITERATION JADIAN COMMENTS`, `v6 DRAFT FINAL ITERATION JADIAN COMMENTS`, `v7 FINAL SIGNOFF`, `vFINAL`, each in both .pptx and .pdf).

8. **`Properties/` is 92% unsorted backlog.** The branch is 8.92 GB, of which `To Clean Up Remaining Files/` is 8.24 GB. The remaining three folders are single communities (Cambridge, Lamberton Lake, and a 0-byte Geiger Key) that duplicate their Operations entries. This branch has no reason to exist separately from Operations.

9. **Sensitive material: location and category only, contents not opened.** All paths below are inside the same `Shared Documents` library as broadly-accessed operational folders:
   - **Employee PII / HR**: `Human Resources/` `Employee Files` (2.27 GB), `Confidential` (613 MB), `Payroll` (434 MB), `Tax Docs` (86.2 MB), `Unemployment` (324 MB), `Workers Comp` (84.5 MB), `Benefits` (113 MB), `Recruiting` (37.5 MB). Also `Human Resources/User Permissions and Security Groups.xlsx` (59.8 KB), an access-control map stored beside the data it governs.
   - **Payroll analytics**: `Jadian-Parakeet/Monthly Payroll Analysis_2024*.xlsx` (5 copies, 44.8 MB) sitting at the root of a branch shared with a JV partner's name.
   - **Cap table / founder equity / individual tax elections**: `Executive/Parakeet Cap Table 2023.xlsx`, `Parakeet Founders Liquidity Schedule - JW.xlsx` + `- JW - DRAFT.xlsx`, `Parakeet MHC - Capital to Date - 03.25.2024.xlsx`, and **six files relating to one named individual's IRC §83(b) election** (`A Berk 83b.pdf`, `A Berk 83b Delivery Confirm.docx`/`.pdf`, `A Berk 83b_receipttracking.pdf`, `Certified Confirm of Delivery A Berk 83b.pdf` ×2, `Form 83b_08032023.pdf`), plus `Berman x Parakeet Offer Letter - signed.pdf` and `Executive/Personal Files/` (7.96 MB).
   - **Deliberately-flagged sensitive**: `Corporate/Newmark Recap Materials - SENSITIVE/` (579 MB). This is the only folder in the library whose name carries a classification.
   - **Board / governance**: `Corporate/Minutes & Notes/` (2.83 GB, includes Board Meetings marked CONFIDENTIAL in-deck).
   - **Lender & debt**: `Asset Management & Finance/Loan Documents/` (3.84 GB, incl. `Walton St - JREFII`), `Wire Info/` (57.6 MB), `Property & Portfolio Mortgage Documents/` (1.30 GB), `Mortgage Statements/` (7.6 MB); `External/MRC Loan Tranche 2` + `3` (2.82 GB), `External/RRA Bridge Loan - Baker Portfolio/` (320 MB), `Executive/MRC Loan Documents/` (73.8 MB), `Sales/Lenders/` (18.9 MB).
   - **Tax**: `Accounting & Finance/Tax Filings/` (2.14 GB), `Monthly & Quarterly Taxes/` (485 MB), `Asset Management & Finance/Taxes/` (1.80 GB), `Property Tax Bills/` (139 MB), `External/Real Advice - Tax Info/` (340 MB), `External/MA Tax Bills/`, `External/Ryan Tax Data Drop/`, `External/Real Estate Tax Disbursement/` (342 MB).
   - **Banking**: `Accounting & Finance/Bank Information/` (2.25 GB), `Credit Applications/` (17.0 MB), `JPM Rec Accounts/`, `Monthly Close/SILVER - PL - RO - Bank Statements & Recons/`.
   - **Resident / buyer PII**: `Sales/Agreements_Closing Docs/Buyers Closing Files/` (319 MB; folder names contain buyer surnames and one carries an eviction annotation), `Sales/Renter Docs/`, `Operations/_Eviction Folder/` (21.8 MB), `Operations/_Legal Notices/` (904 MB), `Parakeet Homes/Home Lending/` (201 MB).

10. **`External/` is the highest-risk branch and the least governed.** It is 314.89 GB shared with counterparties and contains **14 named third-party diligence folders** (`Parakeet DD Folder - Rockpoint`, `- Wafra`, `- Tiger`, `- Soroban`, `- Pulte`, `- Corigin`, `- Durational`, `- SCP`, `- Spectrum`, `- RWN`, `- West End`, `- Brean Asset Management`, `- Morningview Communities`, `- Joel Gantcher`). Eight of these are within 0.05% of the same size (146.0 to 146.2 MB), i.e. **the same data room was copied per-counterparty rather than shared once**, roughly 1.17 GB of identical content across eight folders. The branch simultaneously holds sensitive internal material (`Loan Docs`, `Real Advice - Tax Info`, `Cost Segs`, `MRC Loan Tranche 2/3`) and a 27.93 GB website asset dump (`Rodesi - Parakeet Website`).

11. **`External/` deal and diligence material for the specific items in scope, confirmed present:** `Lamberton Lake (Sale 2026)` (34.3 MB), plus four sibling Lamberton folders (`Lamberton Lake (Crystal View)` 12.4 MB, `Lamberton Lake Nov 2025 DD` 15.5 MB, `Lamberton Seller File` 504 MB, `Sales Package_Lamberton Lake` 14.4 MB), so the Lamberton disposition is spread across **five** External folders plus `Operations/Lamberton Lake (Grand Rapids, MI)/` (17.26 GB), `Properties/Lamberton Lake (Grand Rapids, MI)/` (216 MB), `Construction/LAMBERTON LAKE/` (757 MB) and `Asset Management & Finance/Due Diligence Files/Lamberton Lake_Due Diligence Files/` (1.92 GB). That is **nine locations for one asset's records.** Also confirmed: `Kippy DD` (126 MB), `Mass Historical Utility Bills` (33.0 MB), `ARD POH Pictures` (350 MB).

12. **Empty folders are used as structure, and there are a lot of them.** At least 30 zero-byte folders were observed across the branches enumerated, including `Accounting & Finance/New folder`, `Analytics & Reporting/New folder`, `Asset Management & Finance/Cost Seg Studies`, `AM Transition`, `AM-OPS calls`, `Individual Projects` (which shadows a populated `_Individual Projects`), `Construction/AVALON MHP`, `Construction/CREEK WOOD`, `External/Baker Loan Docs`, `External/Big Okee DD`, `External/IOA Policies`, `External/Jadian - Audit Support Request`, `External/JREFII - Appraisals`, `External/MHVillage`, `External/Newmark RR`, `External/Paro & Parakeet`, `External/Parakeet Chapter 723 Database`, `External/Real Advice - Tax Allocation`, `External/21st Mortgage Business Licenses`, plus 11 of the 16 folders in `Acquisitions (ZS)/` and ~30 numbered request folders in `_Errors/`. Two are intentional documentation (`Sales/.../Buyers Closing Files/Asset#_Type of Transaction_Last Name_Move-in Date` encodes a naming rule; `Operations/_Property Template (City, State)/` encodes the community template); the rest are noise that defeats folder-tree navigation.

13. **Naming conventions actively fight sort order.** Folders are prefixed to force position: 1 to 5 leading underscores (`_Archive`, `__Pre Avid_Bills & Invoices`, `___VLAD___`, `____Central (Cocoa, FL)`, `_____Congress (West Palm Beach, FL)`), trailing `z` runs (`zz_ARCHIVE`, `zzzzzzFLOOR PLANS`), numeric prefixes (`1. Asset Management` … `8. Reports`), and inline instructions in folder names (`_ARCHIVE Operations Process Documents (use _training)`, `Rehab Homes(look in park owned assets)`, `don't use_Cambridge Due Diligence Materials`, `INLAND VILLAGE - POSSIBLE`, `Audit 2025 - Temporary for PH`). Four folders carry typos that will break exact-match lookups: `__SITE ELVATION CERTIFICATES`, `WHSIPERING PINES MA`, `Nalls Ct (Celwiston, FL)`, `Town & Country_Due Diligence FIles`, `Royal Oaks_Due Dilligence`, `Oceanaire (New Symrna Beach, FL)`, `Meadow Woods (Lunenberg, MA)` vs `(Lunenburg, MA)`, `Lake Saunders (Mt1. Dora, FL)`, `Prepaid and Accurals`, `_utilites`, `_October 26 strom damage`.

14. **The intended taxonomy is already documented and already stale.** `Administrative/Folder Structure Glossary.xlsx` enumerates the top-level branches (`_Archive`, `_Errors`, `Accounting & Finance`, `Acquisitions`, `Acquisitions (ZS)`, `Administrative`, `Analytics & Reporting`, …) with a "CURRENT FILE NAME → ACCURATE FILE NAME → Description" mapping, last modified **2025-03-10**. It is the correct starting point for any cleanup and it has not been touched in ~17 months. `Administrative/New Document Checklist for SharePoint.xlsx` and `Folder Structure Tracker_Outline.xlsx` sit beside it.

15. **`Operations/` mixes 71 community folders with 26 functional `_`-prefixed folders at the same level.** The functional ones (`_Training` 2.35 GB, `_Marketing` 113.61 GB, `_Legal Notices` 904 MB, `_Operations Report` 2.04 GB, `_Hurricane Related` 546 MB, `_rent increase` 129 MB, `_Transitions` 415 MB, `_Eviction Folder`, `_Weekly Reports`, `_Campspot Resources`, …) are department-level, not asset-level, and `_Marketing` alone is larger than every branch except the top four. Two of them shadow each other (`_Marketing` 113.61 GB vs `_Marketing Documents` 53.9 MB; `_ARCHIVE Operations Process Documents (use _training)` 2.54 GB vs `_Training` 2.35 GB), and `_October 26 strom damage` (91.2 MB) exists alongside a 0-byte `October 26 strom damage` in the same directory.

16. **A parallel Claude/AI working corpus already exists on a different site.** `sites/ParakeetBirdcage/Data  Analytics/Claude Cowork/Acquisitions/UW Model Engine/` holds a completed 63-deal dossier build (`PROCESS_REPORT.md`, `Batch Validation Report.md`, per-community `.md` dossiers such as `hershey_park.md`, and a 225-question `Deep-Dive Questions for Jon (Combined).docx` with four superseded versions). Out of scope for this index but directly relevant to the second-brain effort: it is prior art on exactly this corpus.

## Gaps

1. **`External/`: listing truncated.** `read_resource` on the External folder returned approximately 200 child entries and stopped alphabetically at `Steiner Photos`, with no file entries returned at all. Confirmed truncation, not an empty tail: targeted searches surfaced four direct children that were absent from the listing: `WSRED - JREFII Tranche 2`, `WSRED - JREFII Tranche 3`, `WSRED - JREFII Tranche 4`, `WSRED Appraiser`. The cause appears to be a per-call result cap in `read_resource` with no pagination parameter exposed. **Unknown: the full set of External children sorting after `Steiner Photos`.** Four recovered; an unknown number remain unlisted. Everything reported above for External covers the A to S range plus those four.

2. **Level 3 not enumerated for most branches.** Level 3 was read for the branches named in the assignment (Monthly Close, Parakeet Audit, Agreements_Closing Docs → Buyers Closing Files, the Operations community template, Bay Oaks under both Operations and Construction, and Due Diligence Files). Level 3 was **not** enumerated for: `Acquisitions/2. Live Deals` (395.73 GB), `Operations/_Marketing` (113.61 GB), `Operations/_Archive Communities` children, `Asset Management & Finance/Budgets` (15.13 GB), `Quarterly Reports` (12.28 GB), `Claude Workflows` (14.07 GB), `Analytics & Reporting/Lender Reporting` (6.74 GB), `Parakeet Homes/Park owned assets` (28.09 GB), `Human Resources/*`, or the 70 non-Bay-Oaks community folders under Operations and Construction. Per-community internal structure is asserted only from the two sampled communities plus the `_Property Template`; individual communities may deviate.

3. **Duplication claims rest on folder byte-totals and names, not content hashes.** The Flood Elevation Certificates finding (Finding 1) is a byte-exact match of folder totals, which is strong evidence but not proof of identical file sets. The eight ~146 MB `Parakeet DD Folder -` counterparty folders (Finding 10) are within 0.05% of each other, not exact. No file-level comparison was performed anywhere. This survey was read-only and did not open or hash any document.

4. **No permission or sharing audit was performed.** Finding 9 lists where sensitive material *is*, not who can reach it. `Human Resources/User Permissions and Security Groups.xlsx` exists and was not opened. Whether the External branch is actually externally shared, and at what scope, was not determined.

5. **Other drives on the tenant were observed but not surveyed** (out of assigned scope). At least four distinct `driveId`s surfaced incidentally: `sites/UserArchive` (departed-employee archives, e.g. `Lowil May O. Malco (2025-09-12)`, `Lark Arielle Lo (2024-11-18)`, each containing PRKT working copies), `sites/ParakeetBirdcage` (the Claude Cowork corpus, Finding 16), a fourth site drive `b!T7oszY-3i0Wfg90h…`, and Austin's personal OneDrive (`parakeetcommunities-my.sharepoint.com/personal/austin_parakeetcommunities_com`, which holds a `Desktop/PARAKEET - Acquisitions - Pipeline.xlsx`). These represent additional copies of main-site material and should be indexed separately.

6. **`totalResultCount` values are library-wide, not branch-scoped.** The folder-search calls returned totals of 17,428 and 2,752 folders and 157/18 files for their respective queries; these count matches across all drives the account can reach and cannot be used to size any branch. No reliable total file count for `sites/main` was obtainable with the available tools.
