---
type: project
tags: [type/project, dept/systems, status/on-hold]
---

# SharePoint Restructure 2026

**What this is:** the project page for moving Parakeet off `/sites/main` and onto Birdcage — seven waves, six gates, 2026-08-17 to 2026-12-31. The working detail already lived in `10-Business/sharepoint/` and `10-Business/storage-inventory/`; this page is the spine that names the waves, the gates and the open decisions in one place.

**Status: ON HOLD — 2026-09-04, Austin.** *"Put this all on hold as it won't be covered on EOS today."* Four Gate 0 decisions were ruled earlier the same day and stand; the rest is held. See **The hold** below for what that means and who has to be told.

**Owner:** Austin Berk owns the project and signs every gate. **Albert Gano executes.** A department owner signs each disposition plan and an automated check verifies the result — three parties on purpose, so nobody grades their own homework.

**Decision page:** `https://claude.ai/code/artifact/4766cf9e-ccb7-4910-96f6-4e8348490822` — the five `[AUSTIN]` Gate 0 items and `EX-003`, with the evidence and the rulings recorded against each.

## Why this project exists

`/sites/main` is roughly **2,876 GB across 25 top-level branches**, grown for years with nobody governing it. **About 61% of that volume goes to an archive rather than to the new site** — which is the only reason a December finish is realistic. It is not a copy-and-paste: the remainder gets re-routed, renamed and permissioned on the way in.

The governing decision is [[00-Meta/decisions/2026-08-26-storage-target-state]] — **Birdcage becomes the system of record for everything manufactured-housing**, and Dropbox becomes the personal and non-MH home.

**This project is the parent dependency of the two projects that already have folders.** `KP-0037` records that **no master community list exists across the 13 JotForm forms, and every FastField cascade and QuickBase relationship field keys off it.** The property name canon this project ratifies is the same object that blocks [[15-Projects/fastfield-phase-i/overview]] and [[15-Projects/quickbase-build/overview]]. Three projects, one canon.

## The seven waves

Hard dates. **Every wave ends on a gate with an explicit go / no-go, and a failed gate stops the next wave — it does not get waived to protect the date.**

| Wave | Workstream | Dates | Wks | Owner | Gate |
|---|---|---|---|---|---|
| **W0** | Foundation — freeze and architecture | 2026-08-17 → **2026-09-04** | 3 | Austin | **GATE 0 — unsigned** |
| **W1** | Corporate, HR and restricted content | 2026-09-07 → 2026-09-25 | 3 | Austin + Albert | GATE 1 |
| **W2** | Tooling validation and pilot close-out | 2026-09-28 → 2026-10-09 | 2 | Albert | GATE 2 |
| **W3** | Property Operations bulk — 68 communities | 2026-10-12 → 2026-11-27 | 7 | Albert + 2 admin | GATE 3 |
| **W4** | Finance, Construction and Homes | 2026-11-02 → 2026-12-11 | 6 | **Dept owners** | GATE 4 |
| **W5** | Archive tier — ~1,747 GB, agent-driven | 2026-10-19 → 2026-12-18 | 9 | Agent + Albert | — |
| **W6** | Cutover, training and lockdown | 2026-12-21 → 2026-12-31 | 2 | Austin | GATE 6 |

**W1 is the restricted cluster** and it is deliberately first, *"while the team is smallest and attention is highest"*: Company Documents, then Investor Relations, Jadian-Parakeet, Corporate, Administrative, Executive, Harry & Lloyd split three ways, and **Human Resources last and slowest**. Two-person rule on every restricted item.

**W4 runs parallel to W3 with different owners** so the two do not compete for Albert.

## GATE 0 — where it actually stands

Nine criteria, verbatim from the Wave Schedule. **No bulk migration before this gate clears.**

| # | Criterion | Owner | State as of 2026-09-04 |
|---|---|---|---|
| 01 | Structure conflict resolved in writing — 8 numbered or 7 unnumbered | Austin | **RESOLVED** — seven unnumbered |
| 02 | Name canon signed by Austin | Austin | **Resolved on substance**, three mechanical items short of a signature |
| 03 | Five destinations exist and are permissioned | Austin + Albert | Pending rows held out of W0; **`D4` still open** |
| 04 | 16 function-group objects and 68 per-community groups provisioned | Albert | Blocked on 02. **The number 68 is now wrong — see below** |
| 05 | Property Reference Hub confirmed retired | Albert | **Unknown here** |
| 06 | Metadata columns live | Albert | Blocked on 02 for the `Property` choice list |
| 07 | Personal Files restricted in place | Albert | **Unknown here** |
| 08 | All 10 exposures locked in place and verified by report | Albert | **Unknown here** |
| 09 | Policy rules published | Austin | Not started |

**Why four criteria read "unknown here."** The tracker this page is built from is the **2026-08-15** build, where W0 still reads *Not started*. Albert worked three weeks after it and **ClickUp is unauthorised in this Brain**, so his side of the gate cannot be seen rather than being assumed. **The missing input is his Friday five lines**, due 2026-09-04: what finished, what did not, what `FolderOutput` turned out to be, what is sitting on Austin, and whether the folder standard is still the only thing blocking him. Criterion 01 answers that last one.

## Decisions taken 2026-09-04

All filed to [[00-Meta/decisions-log]]. The four canon rulings also sit on [[10-Business/sharepoint/community-naming-standard]].

1. **The community folder standard is B, seven unnumbered.** Nothing already scaffolded gets renamed; the permission grid is re-keyed instead — `Facilities` becomes `Facilities and Maintenance`, and the `8-Templates` row drops because W0 already built a site-level Templates library. The comparison behind it: the grid is one workbook, against 62 scaffolded communities × 8 folders where a rename changes the URL and breaks every shared link into it. **Releases all community-folder work in W2 and W3.**
2. **Bay Oaks Village I & II is one folder and two leases.** One canonical community, code `BAYO`, superseding `BOV1` and `BOV2`. The separate fillable leases stay separate inside `6-Legal / Lease Agreements`, so that filing convention needs a I/II token.
3. **The Kissimmee RV asset is Great Oaks.** One asset, one name — retiring Rule 4's standing warning that *"Great Oak and Great Oaks are not the same thing."*
4. **Hendersons is South Bay, FL.** `EX-003` closed inside its 48 hours.
5. **`Gulf Breeze (Hudson, FL)` is canonical** and the bare `Gulf` folder merges into it.
6. **The two Parkwoods are two different communities and never merge.** SC is live under Operations as `Parkwood (Columbia, SC)`, code `PRKW`; the divested NC asset routes to `Archive / Divested Communities`.
7. **`Riviera (Miami Gardens, FL)` is canonical**; the Jadian tree's `Riviera Park (Miami, FL)` is an alias, not a second asset.
8. **The nine Pending rows in the security workbook stay out of Wave 0.**

## Open decisions

**Both are Austin's, and both are held as of 2026-09-04.**

| # | Decision | What it blocks | Clock |
|---|---|---|---|
| `D4` | **The Asset Management level-2 conflict.** The area contains a folder with the same name as itself, and all three level-2 rows carry no ACL at all — only their level-3 children have grants. A folder with no ACL row inherits, which is the exact failure the permission grid exists to stop. | Criterion 03, and **the routing map for the old site's single `Asset Management & Finance/` branch at 753.85 GB** — roughly fifty children have to be split between two destinations, which cannot be written while the destination names are ambiguous. | No hard date |
| `D5` | **Name the six department owners who sign disposition plans.** Legal · Finance · Construction · Homes · Marketing · Acquisitions and Asset Management. Until they are named, every exception Albert logs routes to Austin and burns 48 hours of its own SLA before reaching the person who can answer it. | **GATE 4**, which requires every department owner to have signed their disposition plan. | Wave 4 starts **2026-11-02** |

### Three mechanical items between the canon and a signature

Not judgment calls — arithmetic and spelling, and all three change what Albert provisions.

- **The code-change count contradicts itself.** The tracker header warns *"17 codes differ from the previously ratified 64-property list"*; the sheet marks **25** rows `CHANGED`. Files already renamed in the American pilot carry `WPES-`, `MAYF-` and `MONS-` prefixes and are non-compliant against the new codes, so signing the wrong count means renaming files twice.
- **The per-community group count is now 67, not 68.** Combining Bay Oaks collapses groups **#20** and **#21** into one. **GATE 0 criterion 04 states 68**, so that criterion cannot pass as written until its own number is corrected.
- **Group names do not match canonical spellings.** **18 of the 68 per-community group names fail a character-for-character match** against the tracker's canonical names — mostly typos and suffixes (`Shelle Pointe MHC`, `Mcgregor`, `Palm Spring`, `Carley's`, `Northgate MH`), which matters because the work order makes the group names the canon and requires them to match real folder names. **Three are genuinely ambiguous rather than typos:** `Silver Hill MHC` against canon `Silver Hills`, `Silver Breeze` against canon `Silverbreeze`, and a bare `Whispering Pines` group that could resolve to the Titusville FL or the Auburn MA asset — the exact case Rule 4 says has no answer from the name alone. **Note this is a different cut from the 21-row mapping table and the 30-of-142 join failure on [[10-Business/sharepoint/community-naming-standard]]**: those compare source trees to canonical, this compares group names to canonical. The three lists should reconcile to one.

## The hold

**Austin, 2026-09-04:** *"Put this all on hold as it won't be covered on EOS today."*

**What the hold does and does not touch.** The eight decisions above stand — they were ruled before the hold and are filed. What is held is `D4`, `D5`, the canon signature, the Gate 0 signature, and therefore the start of Wave 1.

**One consequence that needs an action, not a note.** Wave 1 was scheduled to start **Monday 2026-09-07**, which is Labor Day, so the calendar cost of the hold this week is close to zero. But **Albert is expecting a reply today** and is blocked on `D5` for exception routing — he has been told to route anything in the middle six rows to Austin in the meantime, so he is not stopped, but he does not know the project is on hold. **Somebody has to tell him**, or he spends Monday waiting on a gate nobody is signing.

**Why holding Gate 0 is defensible on its own terms.** The gate could not have been signed today regardless: four of its nine criteria are Albert's and their state is unknown here. And Wave 1 is the restricted cluster — HR, investor relations, executive, and the folder holding passports, driver's licences and FinCEN identity documents. **That is not the wave to open on an unverified permissions report**, and the work order already says a failed gate stops the next wave rather than getting waived.

## Where the working detail lives

**`10-Business/sharepoint/`** — the design:

- [[10-Business/sharepoint/target-structure]] — the Birdcage tree, area by area
- [[10-Business/sharepoint/permissions-matrix]] — WRITE / READ / NO ACCESS per area, and the rows with blank permissions
- [[10-Business/sharepoint/security-groups]] — the function groups and their members. **Says 15 groups; the work order and the tracker both say 16** (Ops Administration appears in the grid with no members). Unreconciled.
- [[10-Business/sharepoint/community-naming-standard]] — the seven naming rules, locked 2026-08-31, and the mapping table
- [[10-Business/sharepoint/migration-plan]] · [[10-Business/sharepoint/migration-risks]] — the sequence, and what breaks if it runs before the blockers clear
- `Data Storage Security Direction.xlsx` — the source workbook the permission grid comes from

**`10-Business/storage-inventory/`** — the survey: nine pages covering Birdcage, `/sites/main`, the satellites, OneDrive, the A2Z Dropbox, the personal Google drives, the 2023 folder-structure spec, and [[10-Business/storage-inventory/known-problems]] — the eight structural defects, all cheap to fix during the migration and expensive after it.

**ClickUp** — the execution tracker, and the only place the per-task *how* is written: Space **Command Center**, folder **SharePoint Restructure 2026**, lists `W0 · Foundation (Aug 17 - Sep 4)` and `Exceptions & Escalations (48h SLA)`. **Click through the folder rather than searching** — the list names use characters that will not match if retyped. **Not readable from this Brain**: the connector is unauthorised.

## The five rules Albert works to

Printed on his work order, and they govern anything anyone does in this project.

1. **Nothing gets deleted, ever.** Approved removals go to `_QUARANTINE_202608` in the Archive library for **93 days**. This applies to obviously worthless content too — empty folders, sync garbage. Move it, do not delete it.
2. **A judgement call gets logged, not made.** It goes to the Exceptions list with a 48-hour clock and a named owner, and auto-escalates to Austin past that. **An exception is the correct output when the rules do not cover something. A guess is not.**
3. **Read-only until something is explicitly approved.** The one exception: tightening permissions is always safe and always allowed. Find something exposed, lock it and log it.
4. **Never match a property name by eye.** Two different properties are both called Parkwood. `Whispering Pines` with no state could be either. Great Oak and Great Oaks; Silver Hill and Silver Hills; Apple Valley is not Apple Creek; Auburn Hills is not Auburn Ridge. **Character for character against the canon, or log an exception.**
5. **Two people on anything sensitive.** Personnel, payroll, compensation, medical, investigations, government IDs, investor subscriptions, buyer closing files. Austin plus one named other, both names in the log entry. *"A permissions mistake on 273 personnel files is invisible until it is a very bad day."*

## The live exposures this project exists to close

From the Risk Register — the first six are live today, independent of any migration timeline.

| Risk | Where | Why |
|---|---|---|
| Government identity documents in a shared library | `Harry & Lloyd / Personal Files` | Passports, two driver's licences, FinCEN beneficial-ownership IDs. **Share scope unknown**, and migration tools copy permissions forward by default |
| `_Errors` was a move, not a copy | `/_Errors/` — 5.09 GB, ~2,000 loose files | A 2022 Dropbox script quarantined everything that failed. Where the source delete worked and the write did not, **this folder holds the only copy** — of recorded mortgages, UCC filings, title policies, environmental reports and formation documents |
| 273 personnel folders with no destination | `/Human Resources/` — 5.31 GB | Medical files, investigations naming six individuals, E-Verify, six years of payroll. **Birdcage has no HR site built** |
| Consumer financial PII at volume | `Sales / Agreements_Closing Docs / Buyers_Closing Files` — 317 MB | Buyer closing packages with SSNs and credit applications. Regulated data, and it does not look sensitive from the folder name |
| External sharing exposure | `/External/` — 314.9 GB | **Thirteen byte-identical copies of the full company diligence data room**, in a folder whose name announces it is shared outward |
| The decision volume exceeds the calendar | whole estate | **~4,150 decisions against 99 working days** — about 42 a day. That arithmetic only works if decisions fan out to department owners instead of converging on Austin, which is what `D5` is for |

## Related

- [[15-Projects/fastfield-phase-i/overview]] · [[15-Projects/quickbase-build/overview]] — both key off the canon this project ratifies
- [[00-Meta/decisions/2026-08-26-storage-target-state]] — the governing decision
- [[10-Business/eos/to-dos]] — `TD-0555` (the five `[AUSTIN]` items), `TD-0007`, `TD-0008`, `TD-0009`
- [[70-Operations/sops/folder-and-file-intake]] — the SOP that keeps new material compliant after cutover

## Sources

- `Albert_Week1_WorkOrder_20260817_1.docx` — the Wave 0 work order, read in full. Austin to Albert, 2026-08-16.
- `Parakeet_SharePoint_Migration_Tracker_20260815_1.xlsx` — tabs Summary, Legacy Inventory, Routing Map, Wave Schedule, Property Tracker, QA Gates, Dedup Register, Exception Log, Risk Register, Weekly Scorecard, Naming Reference, Agent Playbook, Target Structure + ACL, Security Groups. Attached to the same email.
- The seven pages in `10-Business/sharepoint/` and the nine in `10-Business/storage-inventory/`.
