# Index, the map of this Brain

One line per thing that matters. Claude keeps this current, when a page is added, renamed, or retired anywhere in the vault, its row here changes in the same session. Read this first, then the folder's MOC, then only the files you need.

**Built by the Structure Interview on 2026-08-30; restructured to twelve top-level folders on 2026-08-31; thirteenth folder `15-Projects/` added 2026-09-02.** **Counted 2026-09-08 by the Index Rebuild: 592 pages and 1,754 documents outside `99-Archive/`, 2,346 files**, plus 47 pages and 97 documents retired into the archive. The previous figure on this line, 546 pages and ~2,275 files, was carried forward rather than counted. Every folder's MOC lists what that folder owns, and every MOC now closes with its own page and document count; this table is the business-level view.

**Counted 2026-09-26 by the Index Rebuild: 616 `.md` pages and 1,755 documents outside `99-Archive/`, 2,371 files, plus 49 pages and 107 documents in the archive.** Up from 611 and 1,755 on 2026-09-22 by exactly the five pages that landed since: the daily closes of 09-22, 09-23, 09-24 and 09-25, and `70-Operations/rehab-program/pre-call-2026-09-22`, which was on disk four days without a map line. The archive gained the superseded 17:44 run of the 2026-09-22 close and the briefs of 09-22 and 09-23. **Same counting method as 2026-09-22**: every `.md` outside the archive is a page here, so the two `systems-architecture/` data dictionary files count as pages on this line and as documents on `MOC-Business`. Register ceilings re-read the same day against the files.

**Counted 2026-09-22 by the Index Rebuild: 611 `.md` pages and 1,755 documents outside `99-Archive/`, 2,366 files, plus 48 pages and 105 documents in the archive.** Up from 605 and 1,755 on 2026-09-16 by exactly the six pages that landed since: the daily closes of 09-16, 09-17, 09-18, 09-19 and 09-21, and `70-Operations/rehab-program/ledger-cost-analysis-2026-09-16`, which was on disk six days with no map line until the 2026-09-22 Page Update listed it. **Counting note, so the next run can reconcile:** the 605 counted the two `systems-architecture/` data dictionary `.md` files as pages, while `MOC-Business` counts them as documents; on the MOC's method the figure is 609 pages and 1,757 documents. Both are stated so neither is mistaken for drift. The archive grew by the restored-from `2026-09-16` close file and four brief snapshots. **Every map resolves: zero dead wikilinks in any MOC, README or this page; 11 dead links vault-wide, none in a map, not touched.** Register ceilings re-read from the register files: `TD-0691`, `KP-0123`, `CM-36`, `PR-0040`, `PD-54`, `PF-0494`.

**Counted 2026-09-16 by the Index Rebuild: 605 pages and 1,755 documents outside `99-Archive/`, 2,360 files, plus 47 pages and 101 documents in the archive.** Up from 592 and 1,754 on 2026-09-08: six daily closes, two rehab pre-call packs, the data lineage register and its probe skill, the Murad page, and the two data dictionary files, which are `.md` and are counted as documents on their MOC. **Every folder's map now covers its folder**: the two pre-call packs were on disk and off `MOC-Operations`, four loose Brand files had no set line, nine archive sets had no line on the archive README, and `90-Skills/data-lineage-probe` had no row here. All fixed this run. Register ceilings on the rows below re-read from the register files: `TD-0662`, `KP-0113`, `CM-34`, `PR-0040`, `PD-48`, `PF-0490`.

**Rebuilt 2026-09-08 by the Index Rebuild, and the defect it found was in the counting method rather than in any row.** A link audit reported 310 unmapped pages and 215 with nothing pointing at them. **Both numbers were wrong and the cause was one character**: the audit split wikilinks on `|` without handling the escaped `\|` form this vault uses for display aliases, so every wikilink carrying a display alias resolved to a path with a trailing backslash and counted as broken. **This is the same escaped-pipe defect [[00-Meta/open-board]] records its builder hitting on 2026-09-02.** Corrected: **23 orphan pages and 98 with nothing pointing at them**, and the 99 lot sheets and 18 community pages the first pass called unmapped were correctly linked all along. **A map audit that cannot parse the vault's own link syntax invents holes.**

**Re-verified 2026-09-08 by the Page Update, and every register count on this page was wrong.** Known problems read 57 against 102, commitments 25 against 34, promises 36 against 40, parked decisions 29 against 45, to-dos ended at `TD-0453` against `TD-0611`, property follow-ups at `PF-0343` against `PF-0482`. **The registers had grown for six days and the map had not.** All corrected against the six files.

**Rebuilt 2026-09-02 by the Page Update, and what was wrong with it is worth recording.** Three rows were duplicated, two pages sat under the wrong folder heading, four rows had been tacked on as loose bullets below the table, and **twenty-two pages had no row at all** - including [[00-Meta/promises]], which is one of the six registers [[CLAUDE]] names. Every count on this page had also gone stale in the same direction: it claimed 26 known problems against 48, 20 commitments against 25, and a 660-row board against 892. **A map that undercounts is worse than one that is missing, because a session reads it and stops looking.** Counts here are now sourced from each register's own rows, not from `00-Meta/log.md`, per rule 10.

| Where | What |
|---|---|
| [[CLAUDE]] | The constitution. Identity, hard rules, Austin's guardrails, the folder map, our vocabulary. |
| [[README]] | The vault root stub, one heading and nothing else. Listed so no page is unmapped; not a place to write. |
| **00-Meta** | |
| [[00-Meta/start-here]] | New to this Brain? Five files, ten minutes. |
| [[00-Meta/index]] | This page. The map. |
| [[00-Meta/numbers-ledger]] | The only place a business number is trusted from. Every entry sourced and dated. |
| [[00-Meta/open-items]] | **Known problems, `KP-0001` to `KP-0128`, ranked by risk. Work it down; don't rediscover it.** Ceiling re-read 2026-09-26 (`KP-0123` on 2026-09-22); closed rows stay in the file, so the ID ceiling is not the open count. |
| [[00-Meta/commitments]] | **What Austin owes and is owed. `CM-01` to `CM-37`. Every line has an owner and a next action.** Ceiling re-read 2026-09-26 (`CM-36` on 2026-09-22; `CM-37` opened state only 2026-09-25). Closed rows sit in a full-text tail under `## Recently closed`, never under Active. |
| [[00-Meta/promises]] | **The sixth register: 40 promises to a named person, `PR-0001` to `PR-0040`.** It closes when the person is told, not when the work is done. **58% carry no owner, the worst share on the board.** |
| [[00-Meta/parked-decisions]] | **Decisions `PD-01` to `PD-56`, waiting on Austin's ruling.** A row leaves when he rules, not when it ages. Ceiling re-read 2026-09-26 (`PD-55` acceleration fees, `PD-56` the reporter request converted from `TD-0693`); on 2026-09-22 `PD-53` and `PD-54` are the three-close rule parking Murad's reply and the Massachusetts entrance fee. |
| [[00-Meta/open-board]] | **Every open item across all six registers, enumerated, filterable and two-way.** The answer to "how much is actually open", and where Austin comments, corrects and flags. **Its row and unowned counts are the 2026-09-02 build; the registers have moved since, see [[00-Meta/board-health]].** |
| [[00-Meta/board-health]] | **Whether the board can be worked, as opposed to how big it is. 291 unassigned rows of ~1,282, 239 of them in one register, six orphan functions.** Counts taken from the register files, not from a parse. |
| [[00-Meta/id-conventions]] | The `CM` `PD` `KP` `TD` `PF` `FF` reference-ID scheme. Read before closing an item by ID. |
| [[00-Meta/delegation-board]] | What should leave Austin's desk. **Its 660-open / 173-unowned figures are the 2026-08-31 baseline and are superseded by the board.** Not a register. |
| [[00-Meta/decisions-log]] | Where a decision gets written down. Append-only. |
| `00-Meta/decisions/` | The six full decision records behind the log lines: storage target state, DR-035, the company assessment method, brief delivery, the BMHCII archive remediation path, and [[00-Meta/decisions/2026-09-03-vault-migration-rulings]]. |
| [[00-Meta/log]] | The Brain's history. Every ingest, filing run and review. Narrative, never a source for a number. |
| [[00-Meta/audit-log]] | **Every change to this Brain, with the reason for it and what it affects. Append-only.** |
| `00-Meta/daily-close/` | The weekday closes, one file per day, 22 dated closes on file as of 2026-09-26 (2026-08-30 to 09-25, Saturday 09-19 included; 18 on 2026-09-22) plus the README; the superseded 2026-09-16 first run sits in `99-Archive/`. [[00-Meta/daily-close/README]] says how the page is used. **Austin types answers under the questions in here, so the current one gets re-read before anything else.** |
| `00-Meta/analysis/` | One-off workbooks and write-ups: the unit-count reconciliation, the tracker-versus-board read, and the master org chart find. |
| `00-Meta/analysis/board-triage-2026-09-03/` | **The four-part triage of all 1,183 board rows**, proposing a priority, owner and agent-ability call for every one without editing any. The distilled version is [[00-Meta/board-health]]. |
| `00-Meta/analysis/vault-reconciliation-2026-09-03/` | **The four-part reconciliation of the retired Claude Code vault**, plus Austin's five governing rulings. Ruled version: [[00-Meta/decisions/2026-09-03-vault-migration-rulings]]. |
| `00-Meta/drafts/` | Unsent drafts owned by no other folder. One open: the Corner IQ decline, 2026-09-04. |
| `00-Meta/board-data/` | The board builder, its 34 build files, the pre-pull snapshots and the stale set. [[00-Meta/board-data/builder/README]] says how to re-run it. |
| [[00-Meta/budget-week-2026]] | The 17 rows Austin flagged `BW` on the board, and why 13 of them are promises to named staff. **Budget week ran 2026-09-16 to 09-18 after three routines carried it as cancelled; corrected 2026-09-22, both readings kept. Whether the list reached the room is not recorded.** |
| [[00-Meta/owner-list-for-review]] | The 33 owner values the board offers, set by Austin 2026-09-01. Read before assigning anything. |
| [[00-Meta/austin-operating-manual]] | How to work with Austin. Style, cadence, what a good deliverable looks like. |
| [[00-Meta/team-rules]] | Folder owners and the working rules for more than one person. |
| [[00-Meta/template-version]] | Which template generation this Brain was built from. |
| **05-Inbox** | |
| [[05-Inbox/README]] | The drop zone. Anything new lands here; Claude files it. |
| [[05-Inbox/_needs-sorting]] | **What is flagged and not guessed. One item is Austin's call.** Inbox emptied 2026-09-15. |
| **10-Business** | |
| [[10-Business/MOC-Business]] | The folder hub. |
| [[10-Business/business-model]] | **How the business makes money, end to end. The day-one page.** |
| [[10-Business/competitors]] | The institutional MHC operators, and the total-payment argument against them. |
| [[10-Business/tools-and-systems]] | Every system that runs the business, one line each. |
| [[10-Business/outlook-folder-map]] | **What a mail sweep reads. 36 folders, the Inbox is the emptiest one.** Folder IDs included, because the connector cannot find most of them by name. |
| [[10-Business/a2z-mailbox-map]] | **The second mailbox, added 2026-09-03.** The a2zcp and Bedrock stream through the Google connector, including `ir@thebedrockgrp.com`, where the Fund II LP base actually writes. Label IDs, and the connector traps. |
| [[10-Business/systems-architecture]] | **The undecided single source of truth across MAV, Rent Manager, the warehouse and Camp Spot. It governs real spend.** |
| `10-Business/systems-architecture/` | Two documents filed 2026-09-15: a canonical key standard and crosswalk DDL, labelled approved, author unknown. The page says how to read them. |
| [[10-Business/connector-status]] | What Claude can actually reach, tested rather than assumed. |
| [[10-Business/data-lineage]] | What reports live on what connector, what feeds each dashboard, and what is broken or unowned. |
| [[10-Business/storage-inventory/known-problems]] | **The eight defects in the file estate. Cheap to fix during the migration, expensive after.** |
| `10-Business/storage-inventory/` | Seven inventories: SharePoint main and satellites, Birdcage, OneDrive, Dropbox, Google Drive, and the 2023 design spec. |
| [[10-Business/sharepoint/migration-risks]] | What breaks if Albert's migration runs before the eight defects are resolved. |
| [[10-Business/sharepoint/target-structure]] | The target Birdcage SharePoint tree, and the permissions model beside it. |
| [[10-Business/sharepoint/community-naming-standard]] | The canonical community naming rule and the live 21-rename list. **Read before any folder rename.** |
| [[10-Business/sharepoint/a2z-utility-logins-exposure]] | **Eleven credentials on a legacy domain, and a departed employee still the login of record on two live utility portals.** |
| [[10-Business/entity-structure/berk-inc-umbrella]] | The three identity domains, and how the pre-Parakeet layer still reaches live billing. |
| [[10-Business/entity-structure/entity-map]] | The readable map over 430 entity documents. **Superseded in part by the master org chart found 2026-09-02.** Since 2026-09-22 also the page for registered agents and entity compliance, the function with four lapses in eighteen days and no owner. |
| [[10-Business/people/how-we-work-together]] | **The routing map. Where things go, who decides what.** |
| [[10-Business/people/field-roster]] | The 28 on-site managers by region. |
| [[10-Business/people/staff-roster]] | ~135 provisioned accounts with emails and access. The most complete staff list. |
| [[10-Business/vendors/uniti-agent-mailbox]] | **`PD-23`: a shared mailbox cannot be put on litigation hold, and every message the agent sends a resident is discoverable.** |
| [[10-Business/eos/rocks-2026]] | Every 2026 rock verbatim, with evidence for and against. |
| [[10-Business/eos/scorecard]] | What is measured, and why it cannot currently be scored. |
| [[10-Business/eos/to-dos]] | **The to-do register, `TD-0001` to `TD-0717`, grouped by owner.** Ceiling re-read 2026-09-26 (`TD-0691` on 2026-09-22); `TD-0666` to `TD-0670` are voided in place and `TD-0678` to `TD-0680` each anchor two rows (`KP-0120`), so quote the row text with the ID. Where a one-on-one agenda comes from. **42% of it is noise and 150 rows are one road trip**, see [[00-Meta/board-health]]. |
| [[10-Business/hr/employee-handbook]] | Mission, core values, leave, spend authority. |
| **15-Projects** | |
| [[15-Projects/MOC-Projects]] | The folder hub. Time-bound builds only; standing work stays in its department folder. |
| [[15-Projects/quickbase-build/overview]] | **The operating system itself: 91 SOPs mapped to 46 workflows across 9 waves, 5 shared tables blocking everything, 11 blocking decisions unrouted.** **Wave 0 is in build with QuickBase's vendor team**, assisting rather than turnkey. FastField Phase I is its front end. |
| [[15-Projects/quickbase-build/workflow-register]] | **Per-workflow status, `WF001` to `WF046`. 3 in build, 2 draft, 41 not started.** In build, not built; the distinction is on the page. |
| [[15-Projects/fastfield-phase-i/overview]] | **13 forms into FastField with live workflows, 3 to 5 a week, before QuickBase launches.** The audit says 6 of 13 go to FastField; Austin says all 13. Unsettled. |
| [[15-Projects/fastfield-phase-i/build-register]] | **Per-form build status, `FF-01` to `FF-13`. 1 of 13 built, 0 with a live workflow.** Where Austin closes a form by ID. |
| **20-Brand-Marketing** | |
| [[20-Brand-Marketing/MOC-Brand-Marketing]] | The folder hub. |
| [[20-Brand-Marketing/voice]] | How Parakeet sounds. One voice, adapted per audience. |
| [[20-Brand-Marketing/online-presence]] | The website, the channels, how new work arrives. |
| **30-Customers** | |
| [[30-Customers/MOC-Customers]] | The folder hub. |
| [[30-Customers/customers]] | Residents: homeowners, renters, snowbirds, and the landlord problem. |
| [[30-Customers/capital-partners/jadian]] | The forward-looking equity partner. |
| [[30-Customers/capital-partners/bedrock-fund-ii-lps]] | The wind-down LP base. Careful handling required. **Now carries the 2025 K-1 delivery record, LP by LP.** |
| [[30-Customers/capital-partners/ridaa-murad]] | **The 33% Bedrock Group partner, on a page for the first time. 30 September is his date for counsel to take over.** Guardrail 6. |
| **50-Products-Sales** | |
| [[50-Products-Sales/MOC-Products-Sales]] | The folder hub. |
| [[50-Products-Sales/the-community]] | **The core product. The land we rent.** |
| [[50-Products-Sales/home-sales]] | The homes we sell, and the total-payment model behind the pricing. |
| [[50-Products-Sales/pipeline]] | Enquiry to resident, with owners and clocks. |
| [[50-Products-Sales/sales-org-buildout]] | The permanent sales org, and the call-routing leak that is the most fixable revenue problem in the portfolio. |
| **60-Communities** | |
| [[60-Communities/MOC-Communities]] | **The folder hub, and the portfolio watch list: occupancy gaps, sub-85% properties, widest loss to lease, payroll overruns.** |
| [[60-Communities/portfolio]] | **The 67-row portfolio table, plus every defect in the source data.** |
| [[60-Communities/regions]] | The three regions, who runs them, and the roll-up for each. |
| [[60-Communities/portfolio-baseline-warehouse]] | **The portfolio as the warehouse actually reports it, unfiltered: $54,813,442 TTM revenue, 48.43% NOI margin.** The filtered figures under Austin's inclusion rules, $44.4M and 62.75%, are in [[80-Finance/portfolio-reporting-rules]]. Same query, two populations. |
| [[60-Communities/open-items]] | **The property follow-up register, `PF-0001` to `PF-0496`, oldest first.** Ceiling re-read 2026-09-26 (`PF-0494` on 2026-09-22). |
| [[60-Communities/projects]] | **Capex and infill projects, one row each.** Kickoffs are projects starting, closeouts are projects finished; the doc number joins the two. |
| [[60-Communities/asset-inventory]] | **The homes we own, and the five lists that disagree.** No reconciled count exists yet. |
| [[60-Communities/_model]] | The Community to Lot to Asset model and the tag vocabulary. **Read before adding anything to this folder.** |
| [[60-Communities/activity/2026-08-stream]] | Every property-level item, newest first. The raw pulse. |
| `60-Communities/lots/` | 99 lot pages where a lot has real activity, plus 57 in `_superseded/`. Bulk; a lot earns a link when a page cites it. |
| `60-Communities/assets/` | 10 asset pages for homes with an identity that outlives their lot and something in dispute. Bulk. |
| **70-Operations** | |
| [[70-Operations/MOC-Operations]] | The folder hub. |
| [[70-Operations/sops/sop-library]] | **The process library: nine bands, 109 processes, 1 approved, 19 open conflicts.** |
| [[70-Operations/sops/year-end-push]] | **The SOP program: one plan, phased to year-end, five decisions blocking everything.** |
| [[70-Operations/sops/400-capex-kickoff-and-closeout]] | **How a capital project gets approved and closed.** Six signatories, one number, eight places the template breaks. |
| [[70-Operations/sops/200-demo-and-lot-prep]] | The only approved SOP. The model for what done looks like. |
| [[70-Operations/sops/folder-and-file-intake]] | The single-drop intake design Austin asked for. Not an approved SOP until six decisions land. |
| `70-Operations/sops/` | 37 process pages over 242 source files in four zones. Bulk; the library page is the way in. |
| [[70-Operations/rehab-program/overview]] | **The rehab program: 219 units, nine analysis angles, five that work and four that do not.** One program with one owner, because every gap on it sits in a seam between two departments. |
| [[70-Operations/rehab-program/wip-and-invoice-model]] | **How a rehab dollar moves. Seven steps from approved scope to balance sheet; this company can see three.** The $989,786 booked against finished homes, the WIP roll-forward that does not exist, and since 2026-09-22 Jon's own figure for the open WIP balance and the three mechanics faults behind it. |
| [[70-Operations/rehab-program/weekly-call]] | **The cadence, and the argument for two forums instead of one.** The vendor is in the room and accounting is not. |
| [[70-Operations/rehab-program/reconciliation-2026-08-28]] | Every flagged unit, listed so a name can go against it. **A point-in-time read, not a live figure.** |
| `70-Operations/rehab-program/pre-call-*` | One pre-call pack per weekly call, three on file (09-08, 09-15, 09-22; the third added to the maps 2026-09-26). The first two are built on the 2026-08-28 export and say so. `ledger-cost-analysis-2026-09-16` is the addendum to the second: the warehouse cannot see rehab capital. |
| [[70-Operations/delivery-bottleneck]] | **Set-crew capacity binds, permits do not, and nobody owns the capacity number.** |
| [[70-Operations/supply-chain-model]] | Order to occupancy: seven stages, the diagnostic order, the failures that keep recurring. |
| [[70-Operations/license-and-permit-ownership]] | Permits have no owner. The plan to take the function back. |
| [[70-Operations/meetings/2026-08-31-settlement-strategy-and-auburn-rent-control]] | **The Monday settlement call. Two paths, and the Massachusetts-versus-Clearwater question.** |
| [[70-Operations/meetings/2026-08-31-kippy-dispute-legal-strategy]] | **The Kippy dispute: defaulted note, ~$1M of fees, three portfolio communities.** |
| [[70-Operations/meetings/2026-08-31-listings-pipeline-and-ai-cost-consultation]] | **The listings pipeline end to end, and where the AI cost went.** |
| [[70-Operations/meetings/2026-08-31-bedrock-fund-ii-lp-call]] | **The Fund II LP call.** An admitted statement error, an untraced 2021 wire, and the first fund IRR recorded anywhere here. |
| [[70-Operations/meetings/2026-08-31-accounting-platform-intro-rillet]] | The AI accounting platform intro, and the clearest description of the expense-side stack in this vault. |
| `70-Operations/meetings/2026-08-southeast-tour/` | **59 pages and 188 documents**: 28 filed notes from the August tour, 31 raw Plaud exports behind them, 29 field photos and the 128 per-community one-pagers. 157 decisions came out of this set. **The trip is recorded three times over**, so read the filed note, not the export. |
| **80-Finance** | |
| [[80-Finance/MOC-Finance]] | The folder hub. |
| [[80-Finance/money-flow]] | How cash moves, and the monthly calendar that is the real rhythm. |
| [[80-Finance/capex-plan]] | The $11.6M 2026 plan. |
| [[80-Finance/payroll-model]] | Payroll at 5% of property revenue, and where it breaks. |
| [[80-Finance/board-reporting]] | The March 2026 board deck: thesis, misses, asks. **Carries per-person compensation; point at it, reproduce nothing.** |
| [[80-Finance/portfolio-reporting-rules]] | **Austin's own rules for what counts as an operating property. Do not re-derive, do not re-ask.** |
| [[80-Finance/intercompany-arap-recon]] | Eight years unreconciled, why the packet failed, and the quarterly process that replaces it. |
| [[80-Finance/fund-reporting/bedrock-fund-ii-winddown]] | The wind-down record and the path to dissolution. |
| [[80-Finance/fund-reporting/wp36-38-integrity-reaudit]] | **Why `WP-36-M3` was not signed. 37 figures held, 12 refuted, and the ordered fix.** |
| [[80-Finance/fund-reporting/esg-reporting]] | What the funds report on ESG, and to whom. |
| [[80-Finance/planning/2027-budget/overview]] | **How the 2027 budgets get built: the absorption cap that replaces per-unit overrides, the cash-flow roll-up, the JREF I pricing module.** The first description of this process anywhere here. |
| **85-Personal** | |
| [[85-Personal/README]] | **The private personal section, built 2026-09-03.** Its own rules, stricter than the vault's. Read it before adding a line to any page below it. `PD-39` holds whether it stays. |
| [[85-Personal/belmart]] | The house. A live construction project run like a job: budget tracker, change orders, draws, lead times. **Jamie is the day-to-day decision maker.** |
| [[85-Personal/household]] | The standing cast on the personal side outside the Belmart build: the people who work on the house, the cars and the property. |
| [[85-Personal/key-dates]] | The recurring personal calendar spine and the lead-time clocks on the house. **Absolute dates only, each with where it came from.** |
| [[85-Personal/personal-admin]] | The advisors and recurring services. **Pointers only: no account numbers, no balances, no policy or claim numbers, no credentials.** |
| [[85-Personal/school-and-sports]] | The schools, teams and clubs in the family calendar. **Logistics only.** |
| [[85-Personal/family/jamie]] | Relationship and logistics context, not a file on a person. |
| [[85-Personal/family/the-girls]] | Logistics only. **No ages, no dates of birth, no grade or school year.** |
| **90-Skills** | |
| [[90-Skills/end-of-day]] | **Weekday 6pm: sweep the day, file what moved, and ask about what probably got settled on a call.** Output in `00-Meta/daily-close/`. |
| [[90-Skills/page-update]] | Push what is new onto the pages that own it, and keep the maps honest. |
| [[90-Skills/transcript-filing]] | Recording in, filed decisions and routed tasks out. |
| [[90-Skills/community-hot-sheet-refresh]] | How the live block on every community page gets filled from the RentViewer warehouse. |
| [[90-Skills/community-pulse-refresh]] | **Weekly: harvest email, Teams and transcripts into the lot sheets and the follow-up register.** |
| [[90-Skills/index-rebuild]] | Rebuild this index and the MOCs from what is actually on disk. |
| [[90-Skills/weekly-brain-review]] | The weekly pass over the Brain itself. |
| [[90-Skills/data-lineage-probe]] | Weekly: rewrite the source layer of the data lineage register from live connector calls, never from memory. Step 7 of the weekly review. |
| [[90-Skills/structure-interview]] | The one-time interview that built this Brain. Run once; already run. |
| **95-Agents** | |
| [[95-Agents/answer-from-the-vault]] | Job 1: answer business questions without Austin digging. |
| [[95-Agents/transcript-to-action]] | Job 2: recording in, filed decisions and routed tasks out. |
| [[95-Agents/finish-the-sop-library]] | Job 3: work 109 processes to approved. |
| [[95-Agents/sharepoint-migration]] | Job 4: support Albert's move to the Birdcage structure. |
| [[95-Agents/morning-brief]] | **The weekday brief. What it sweeps, in what order, and what it is not allowed to re-raise.** |
| [[95-Agents/weekend-pulse]] | The Friday evening pulse. List everything, filter nothing. |
| [[95-Agents/ramp-charge-coding-agent]] | The agent that codes Ramp charges, and the arrears problem it exists to attack. |
| [[95-Agents/_example-agent-brief]] | The shape a new agent brief takes. |
| **99-Archive** | |
| [[99-Archive/README]] | What has retired, and what should retire next. **Every archive set has a line as of 2026-09-26: 49 pages, 107 documents** (47 and 101 on 2026-09-16). |

## Drafts, and where they sit

Unsent drafts live in the `drafts/` folder of whichever folder owns the subject, never in a central pile. **Fourteen are open**, counted 2026-09-08: eight in `10-Business/eos/drafts/`, two in `10-Business/sharepoint/drafts/`, one each in `10-Business/hr/drafts/`, `60-Communities/drafts/`, `80-Finance/drafts/` and `00-Meta/drafts/`. Every one is listed in its own folder's MOC. **A draft is Claude's work, not a sent thing** - guardrails 5 through 8 mean most of these will never be sent by anyone but Austin.
