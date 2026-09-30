# Google Drive (Personal): Inventory

**What this is:** The personal Google Drive, and the three corporate Shared Drives a consumer Gmail account is a standing member of.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

Surveyed: 2026-08-26 | Account: `austinrberk@gmail.com` (consumer Gmail; My Drive root `0AA-ebv6mPPW-Uk9PVA`, ouid `115829884405538186423`) | Coverage: My Drive owned files enumerated to exhaustion (~255 items, 3 pages, no continuation token); top-level shared-in enumerated to exhaustion (~90 items, no continuation token); three corporate Shared Drives discovered and mapped at the top level only. Their interiors were sampled by keyword, not enumerated.

## Summary

This is a low-volume personal Drive (~255 owned items, ~90 top-level shared-in items) whose My Drive is genuinely mostly personal: kids' schoolwork, lawn care, a workout tracker, Amex statements, car service records. The headline is not what is *in* My Drive but what this consumer Gmail identity has *standing membership in*: three corporate Google Shared Drives holding the Parakeet Communities and A2Z Capital Partners record base. That is roughly 30 manufactured-housing community property folders, an operations/HR drive, and a fund drive containing LP subscription agreements, cap tables, K-1s, certificates of merger, and an employee employment agreement. That access is invisible to a "shared with me" review because Shared Drive contents carry neither an `owner` field nor a `sharedWithMeTime`, so a casual audit of this account would report it clean. Secondarily, My Drive itself holds a real estate closing set (9100 Belmart Road), several entity financials (JLB Group LLC, Gilchrist, BMHCII sponsor schedule), an investor contact list, and the Parakeet brand guide. The single biggest problem: **a personal consumer Gmail account is a standing member of corporate Shared Drives containing investor, entity, and employee records, with no Workspace admin lifecycle governing that access**. If Austin loses this Gmail account, or if it is ever compromised, both the continuity and the confidentiality exposure sit entirely outside company control.

## Taxonomy

### A. My Drive, owned (`owner = 'me'`), ~255 items

Exactly **12 root folders**:

| Folder | Character | Notes |
|---|---|---|
| `Banner` | Business (empty scaffold) | Acquisition diligence tree, 20+ nested folders, **zero files** |
| `Amex` | Personal finance | 54 monthly statement PDFs, 2021-01 → 2023-12 |
| `Saved from Chrome` | Auto-dump | 1 file only (`Journal Entry (Report).pdf`) |
| `Google AI Studio` | Auto-dump | 3 files, supplement-tracker app build |
| `Google Earth` | Auto-dump | Empty at time of survey |
| `Winterset Renderings` | Personal/property | ~30 JPG renderings, 2023 |
| `Julia Schoolwork` | Family | ~10 JPGs, 2020 |
| `JULIA MONTAGE` | Family | 2026 |
| `Dolphin 2023` | Personal | 4 ZIPs (~180 MB) + JPGs |
| `Land Rover Service Issues` | Personal | 4 `BERK *.pdf` service records |
| `Anyfile Notepad Files` | Cruft | 2020 |
| `Untitled spreadsheet (File responses)` | Cruft | 2019 Forms artifact |

Loose at root: ~90 files, heavily weighted to untitled/abandoned Sheets.

### B. Shared-in, top level (`sharedWithMe = true`), ~90 items

Fully enumerated. Roughly: 25% school/family (Bullis School, lacrosse/BLC, tutoring), 20% AI-tooling newsletter clutter (2026), 20% vendor/contractor media, 20% aged real-estate deal material (2016 to 2021), 15% misc templates.

### C. Shared Drives: corporate, NOT owned and NOT flagged as shared-in

Three distinct Shared Drive roots were reached by following `parentId` chains. Their files carry **no `owner` field and no `sharedWithMeTime`**, so they appear in neither of the two standard queries above.

| Drive root ID | Contents | Top-level scale |
|---|---|---|
| `0ANSvtCpaQmhVUk9PVA` | Property/asset files, per-community | ~30 community folders + `_Archive`, `Administrative`, `_Property Name (City, State)_Template` |
| `0AHN7ilIBrGJRUk9PVA` | Parakeet corporate & operations | 14 folders + ~9 loose files |
| `0AFtyceEG0HhKUk9PVA` | A2Z / fund, entity & investor | 7 folders + loose files |
| **`0AJ8dOob9gR0HUk9PVA`** | **A2Z and Bedrock entity layer, one folder per vehicle: `Parakeet Companies`, `Mobile Management` (A2ZMHC), `A2Z Community Partners`, `Bedrock MHC Fund II`, `BEDROCK I GROUP`, `A2Z MH Fund I`, `MoMa Lending`, `NewCo`** | **8 folders. FOUND 2026-09-03, not in this survey. Three was a floor and it held.** VERIFIED by direct listing |

## Findings

**1. Three corporate Shared Drives are accessible from this personal Gmail identity. This is the central governance finding.**
Reached by parent-chain walking, not by any shared-in query. `0ANSvtCpaQmhVUk9PVA` holds ~30 manufactured-housing community folders, many prefixed `____UPLOADED___`: Bay Oaks I & II (Panama City, FL), Mayflower (Plymouth, MA), J Bar J Estates (Miami, FL), Mobile Manor (Rosedale, MD), Royal Oaks (Vero Beach, FL), Apple Creek (Bismarck, ND), Westwood (Ormond Beach, FL), Wolf Bay (Elberta, AL), Gulf Breeze (Hudson, FL), Hunter Springs (Crystal River, FL), Lake Wales, Palm Spring Estates, Ormond Beach Oasis, Cambridge (Charles Town, WV), Journey's End (Okeechobee, FL), Colonial (New Bern, NC), Parkwood and Lambeth (Winston Salem, NC), Vandemere (Greenville, NC), Cedar Grove (Kernersville, NC), Town and Country (Jacksonville, FL), Oceanaire (New Smyrna Beach, FL), Royal Palm and Everglades (Clewiston, FL), Countryside and Parktown (Mandan, ND), Shasta Glen (Klamath Falls, OR), Valley View (Roseburg, OR), Lamberton Lake (Grand Rapids, MI). Seven of the eight community names supplied in the brief resolve here. `0AHN7ilIBrGJRUk9PVA` is the Parakeet ops drive: `Corporate Files`, `Human Resources`, `Investor Relations`, `Investment Vehicles`, `Strategy`, `Training`, `Marketing`, `Properties`, `Meetings & Check Ins`, `Communication`, `Admin Files`, `Community Maps`, `Mileage Logs`, `Tollett Intro Info`, plus loose `Parakeet Directory.xlsx`, `Business_Cap Ex Budget.xlsx`, `AR Report for Ops Call.csv`, `Aged Receivables_20211206083818672.csv`, `Bank Register_20211206122750750.pdf`, `Waiver and Release of Lien.pdf`, `Support Staff Duties-Parakeet[73] (1).docx`, `Agreement to Demo Home_FL.docx`.

**2. The A2Z fund drive contains the most sensitive category in the entire surface: securities and investor records.**
`0AFtyceEG0HhKUk9PVA` top level: `Cap Tables`, `Investor Relations`, `BMHCII - InvestorsRelations`, `A2Z Fund I - Subscriptions`, `RealPage_IMS`, `Violet Smears`, and loose `Investnext Investor Distribution Schedule.xlsx`. Beneath it sits a `Legal` tree (`Legal` → `MD_NY Merger` → `Draft_Archive`) alongside `Accounting` and `Assets`. Keyword sampling surfaced, by title: `A2Z Fund I Sub. Agmt. - Robert A Samit Family Trust.pdf`, `A2Z Fund I Sub. Agmt. -Terri Sanker Revocable Trust_Revised.pdf`, `A2Z Community Partners_Victoria Woods_K1_2018.pdf`, `2020US P156715 K1P V1 6 A2Z Community Partners, LLC .pdf`, `NOTES AND COMMENTS - A2Z ND PORTFOLIO PARNTERS LPA (v.1).pdf`, `A2Z Community Partners LLC - Certificate of Merger (New York) (7682974).docx`, `A2Z Community Partners LLC - Filed Articles of Merger (MD) (7755024).pdf`, `A2Z Community Partners LLC - signature pages (merger) (7685060) (1)-signed.pdf`, `A2Z Community Partners LLC - Written Consent (financing) (7968831).docx`, `A2Z Holdings & Subsidiaries.pdf`, `Berk_Signature Pages.pdf`. Category: named third-party investor identities, trust vehicles, tax K-1s, LP agreements, and executed signature pages. Also present, under a `Tracey Taylor` personnel folder: `Employment Agreement  Parakeet-Theresa Tracey Taylor.pdf`, an individual employee's contract.

**3. Parakeet-branded material also sits directly in My Drive, owned by the personal account.**
`Parakeet Brand guide.pdf` (76 MB, root, owned, 2021-10-07) is the clearest case: a company brand asset owned by a consumer Gmail identity. Additional Parakeet-era material in the Shared Drives includes `Parakeet MHC Term Sheet - Execued Copy JW+AB - 8.13.2021.pdf`, `Parakeet MHC Term Sheet - Fully Executed Copy - 8.17.2021.pdf`, `Parakeet Communities Introduction 2021.pptx/.pdf`, `Parakeet FL MHC Pipeline - Overview June 2021.pptx/.pdf`, `Jadian & Parakeet - Lender Overview (November 2021).pptx`, `Parakeet Meaning Snippets.docx`, and `Non-CA A2Z Comminity Partners Handbook.docx` [sic].

**4. The `Banner` folder is a complete, correctly-structured acquisition diligence data room containing zero files.**
Created 2025-08-12 (every folder shares the same creation timestamp, a template drop). Structure: `Banner` → `Banner Management` → `Financial` (`Monthly Financial Statements`, `Tax Returns`, `General Ledger (36 Months)`, `Bank Statements`, `Debt Schedule`, `Accounts Receivable`, `Accounts Payable`), `Baylen` (`Financials`, `Operations`, `Agreements`), `Staffing_Payroll` (`Org Chart`, `Payroll Costs`), `Operations_Store_Level` (`Store-by-Store P&L`, `Sales Trends`, `Inventory Reports`, `Lease Agreements`), `Licensing_Key_Contracts` (`Hallmark License_Franchise Agreement`, `LLC_Operating Agreement`, `Vendor Agreements`, `Pending Issues_Litigation_Disputes`). I queried eight leaf folders directly and every one returned zero files. The `Hallmark License_Franchise Agreement` node implies Banner is a Hallmark-licensed retail business under evaluation. The only actual Banner file anywhere is `Banner A_R 8-27-25.XLSX` sitting loose at root. **This is an abandoned or never-started diligence effort, not a populated data room**. Worth confirming whether it stalled or whether the files went somewhere else.

**5. A complete real-estate closing set for 9100 Belmart Road is owned and loose at My Drive root, and duplicated.**
`Ratified contract for 9100 Belmart Road.pdf` (8.6 MB), `Final Disclosures for 9100 Belmart Road.pdf` (18.3 MB), `belmart emd.pdf`, `9100 Belmart Assignment .pdf`, plus `Belmart Docs.zip` (27 MB). All created 2025-06-16. Each of the four PDFs exists as **two identical copies** with different file IDs, an upload run that fired twice. Category: executed purchase contract, seller disclosures, earnest money deposit, and a contract assignment.

**6. Older entity financials and an investor contact list sit unfoldered at root.**
`JLB Group LLC - July 2020 Financials` (Sheet) and `.xlsx` duplicate, `JLB Profit and Loss.xlsx`, `JLB Oct 2019.xlsx`, `JLB November.xlsx`, `JLB Order Records`, `JLB Order Form`; `Gilchrist Financials`; `BMHCII_Sponsor_Contribution Schedule`; `General Ledger_2022.csv` (1.5 MB); `Parkway Rent Roll.xlsx` (576 KB) and `Utility work sheet Parkway.xlsx`; `Investor Contact List` (2015); `Calyx Ventures Structure`; `150 Potrero Model.xlsx`; `i need to create an investor statement to calcula...` (2025-12); `Loan Amortization Schedule`; `Bank Recon Checklist`; `Berk Plan.docx`.

**7. Personal systems already running here are thin but real, and health/fitness is the live one.**
Actively maintained: `13-Week Workout Tracker — Golden Era Plan` (Sheet, owned, created and last touched 2026-08-24, the newest owned file in the account). Health also appears as `HealthTrack Pro` (Google AI Studio applet, 2026-01, supplement adherence tracker) with its build transcript. Home/property: `Lawn Project` and `Potomac Lawn Care: Seed, Soil, and Timing` (both 2026-03). Family/community: `Mitzvah List` (2026-02), `JULIA MONTAGE` (2026-02), `Julia Schoolwork`, `Ashlyn Vacation` (2024). Personal finance: the `Amex` folder (54 statements). Planning-system attempts, all stalled at 2025-08/09: `Copy of ⭐️ One-Page Monthly Planner`, `Copy of ⭐️ Weekly Planner`, `Copy of Task Priority Tracker, Eisenhower Matrix`, `Copy of ReadyExcels Simple Bookkeeping`. **Pattern: templates get copied in bursts and abandoned within days; the only personal system that survived contact is the workout tracker.** Nothing here covers travel or insurance.

**8. Shared-in splits cleanly into signal and noise.**
*Noise (newsletter/lead-magnet clutter, all 2026):* `MomAIHacks_Family-Logistics-Guide.pdf` (hellomomaihacks@gmail.com), `20 Essential Claude Skills Guide.docx` and `Claude Code Setup Guide` (nick@nsdmt.com), `cowork-os-golden-rule-setup.pdf` and `Claude Council Skill` (charlie@linked-agency.com), `Workflow n8n.mp4` / `GHL workflow 1.mp4` / `GHL workflow 2.2.mp4` / `Automation portfolio` (jhosuasaetdev@gmail.com, an inbound automation freelancer's pitch). ~10 items, safe to ignore.
*Signal (counterparties, advisors, family):* `SUNDAY Guide` (2026-08-17, shared 2026-08-26, the most recently shared item in the account, no owner shown). `Updated Budget_October2025` and `*Contacts 2020` from **arleighbanner@gmail.com**, who also shared `Resident Contact Information Form` and `Residents Welcome Letter.docx`. A recurring counterparty across both household budget and property operations. `ASHLYN RAISE` (ashlynbanner@gmail.com, 2025-02), a compensation discussion. `Austin Berk's User Manual` (file.dump@athena.com, 2025-03), an executive-assistant onboarding artifact, directly relevant to chief-of-staff work. `Client - EA Preferences Template` (c@chrisyork.co) and `Highland // CEO Bundle Worksheets` (me@scotchisholm.com), both coaching/EA advisory. `Digital scan of all Regency maps and site plans.pdf` (grantakb@gmail.com, 134 MB, 2026-01), live property material. `I have a buyer - Version C` (cara@compass.com, 2025), brokerage. `Submittal 2026.05.10.zip` (aaljbour.work@gmail.com, 55 MB). Bullis School (`link_share@bullis.org`, `katy_dorsey@bullis.org`, `erin_mcdonald@bullis.org`, `katrina_hunter@bullis.org`) and lacrosse (`anna.c.chou@gmail.com`, `leander.perun@gmail.com`) are the standing family-logistics feed.

**9. Sensitive material by location and category (flagged, not reproduced).**
- Shared Drive `0AFtyceEG0HhKUk9PVA`: named investor identities, family trusts, tax K-1s, LP agreements, cap tables, executed signature pages, one employee employment agreement.
- Shared Drive `0AHN7ilIBrGJRUk9PVA`: HR folder, staff directory, bank register, aged receivables.
- My Drive root: real estate closing package (Belmart), entity general ledger and P&Ls, investor contact list.
- My Drive `/Amex`: 54 consecutive months of personal credit card statements.
- My Drive root: `final_patient_report_181872.pdf` and `COVID screening questions for patients` (health/medical category).
- My Drive root: `Austin Berk - Austinrberk@gmail.com - 2025.6.26.pdf` (account/identity export, unexamined).

**10. Hygiene: duplication, untitled sprawl, and a dead-since-2021 corporate record base.**
At least 15 root files titled `Untitled spreadsheet`/`Untitled document`/`Untitled presentation`/`Untitled form`/`Untitled site`, spanning 2014 to 2026. Several Sheets are named with the raw prompt that created them (`Hey Can you read this https://www.damotech.com/blog/... and give me a spreadsheet of all the warehouses...`, `can you send me a list of all the mobile home parks in these areas`, `Can you tell me the exact address of each`), AI-export artifacts, never renamed. `IMG_7156` to `IMG_7166` exist twice (root and `Julia Schoolwork`); the Belmart set exists twice; `3'S POD CONTRACT.pages` exists twice. Across the Shared Drives, nearly all activity timestamps cluster in **2021**, with the property drive's last meaningful edits in early 2022 and one 2026-04 touch on Mayflower. The Parakeet/A2Z record base in this account is effectively frozen and historical, not live.

## Gaps

- **Shared Drive interiors were not enumerated.** No folder-tree tool exists, and Shared Drive files return neither `owner` nor `sharedWithMeTime`, so neither `owner = 'me'` nor `sharedWithMe = true` reaches them. Everything reported for the three drives comes from (a) top-level `parentId` queries against the three roots and (b) keyword searches on Parakeet/A2Z/community/deal terms. **The true file count in these drives is unknown and is very likely in the thousands.** Community folders were confirmed to exist but their contents were not enumerated beyond samples (e.g. Bay Oaks yielded 26+ `MH Titles` PDFs from a single title query).
- **I cannot confirm the three Shared Drives are the only ones.** There is no tool to list Shared Drive memberships. Three roots were found by chance, via parent-chain walking from keyword hits. A fourth drive containing no Parakeet/A2Z/community keyword in any filename would not have surfaced. Treat "three" as a floor, not a total.
- **Shared Drive names are unavailable.** `get_file_metadata` returns `"title": "Drive"` for all three roots, so they are identified by ID only. Confirming which legal entity administers each drive requires the Drive UI.
- **No file contents were opened.** Every claim is from filename, folder path, MIME type, size, and timestamp. Categorizations of sensitivity (e.g. "K-1s", "cap tables", "employment agreement") are inferred from titles and folder names, not verified by reading. Untitled files were not opened, so ~15 root Sheets remain entirely uncharacterized; one or more could contain business data.
- **Two folders read as empty but may not be.** `Google Earth` and several `Banner` leaf nodes returned no children; I queried eight of the ~20 Banner leaves directly. The remaining Banner leaves are inferred-empty from the uniform creation timestamp and the absence of any Banner file in the full `owner = 'me'` enumeration, which is strong but not direct evidence.
- **Trash and version history were not examined**, and the survey was read-only by instruction, so nothing was opened, moved, or restored.
- **`SUNDAY Guide` has no `owner` field**, meaning it too may originate from a Shared Drive rather than an individual's My Drive; its provenance is unresolved.
- **Storage totals are unavailable.** No quota tool was exposed; the ~255 owned items include several large ZIPs (Dolphin 2023 at ~180 MB, Belmart Docs at 27 MB) but total consumption was not measured.
