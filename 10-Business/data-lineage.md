# Data Lineage — what reports exist, on what MCP, and what consumes them

**What this is:** the one register that answers three questions without opening anything else. What reports and models each connector actually exposes. What each dashboard, report and vault surface is fed by. And which of those feeds is broken, unowned or fed by nobody.

**Status:** created 2026-09-09; feed map added 2026-09-29 (Phase 3 of the One Brain plan); rows 7 and 8 of the breaks table added 2026-09-15 by the Page Update from the daily closes. **Source layer probed live this session.** Consumer layer built from the refresh skills and the vault; the parts nobody has ever written down are marked as such rather than guessed.

**This page owns the report catalog.** [[10-Business/connector-status]] keeps connector identity, authentication and the blocked list. Two pages, one fact each — do not restate a report list over there.

**The rule that makes this page worth having, borrowed from the [[00-Meta/id-conventions]] near-miss:** a page describing live state goes stale by construction. So the source table below is never edited by hand. It is rewritten by [[90-Skills/data-lineage-probe]], which calls each connector and stamps the result. **A row with an old probe date is a row you do not trust.**

---

## The finding that changes what is possible today

**The warehouse has eleven models. This Brain has been working from five since 2026-08-26.** Six models nobody here knew about, and two of them dissolve blockers that are written down elsewhere as hard walls.

| New model | What it unblocks |
|---|---|
| **`VW_General_Ledger`** | Transaction-level GL detail by property, account and date. **This is the workaround for Rent Manager report 51 `GeneralLedger` returning HTTP 500**, which [[10-Business/connector-status]] records as the blocker on per-project capex analysis and `KP-0087`, the capex committed-versus-paid gap. Cash basis and transaction-dated, so it will not tie to `VW_Budget_Comparison` — that one stays the budgeting source of record. |
| **`VW_Reservation_Activity_Feed`** and **`VW_Short_Term_Rentals`** | **The six RV parks, with live reservation data.** connector-status says Camp Spot is blocked and "6 RV communities / ~400 sites invisible to Rent Manager." The booking system is still not connected — the reservation data is not invisible. Queried this session: Great Oak 157 reservations, Paradise Lakes 179, River Oaks 125, Whispering Pines 78, Northgate 70, Silver Breeze 34. **643 reservations, 87,095 occupied days, 524 sites.** No time filter was applied, so that is every period in the feed, not 2026 alone. |
| **`VW_Service_Manager_Issues`** | Work orders open and closed, April 2018 to date, by property, unit, category, assignee and age. Service Manager is the join between an Adobe Sign capex approval and Rent Manager, per [[10-Business/tools-and-systems]]. **Caveat to state in any answer: ~1,542 issues, about 10%, carry no Property ID, so a per-property breakdown will not sum to the unrestricted total.** |
| **`VW_Infill_Make_Ready`** | Infill and make-ready projects with checklist completion, by property and unit. **This is a live feed for the infill initiative and the rehab program** ([[70-Operations/rehab-program/weekly-call]], [[70-Operations/sops/200a-demo-to-infill]]), both of which currently run off point-in-time workbook exports of a shared sheet nobody tracks. Dates run to 2029 — it includes planned work, not only completed. |
| **`VW_Properties`** | The property reference list with active flags, address, state, short name. The clean join key the other models need. |

**Nothing here has been used in a decision yet.** It is capability, not a conclusion. `KP-0104`.

---

## Source layer — what each connector exposes

**Probed live 2026-09-09.** A connector not probed this run says so; it is not claimed either way.

### Rent Manager reporting API — `RentView_Rent_Manager_API`

**21 reports enabled, verified by `list_reports` 2026-09-09.** Unchanged in count from 2026-08-26.

| Report | ID | Answers |
|---|---|---|
| `AgedReceivables` | 78 | AR by aging bucket, detail or summary |
| `AssetListing` | 244 | Homes and assets, active flag |
| `BalanceSheet` | 38 | **Consolidated balance sheet, cash or accrual.** Berman said this was never produced; it runs on demand |
| `BudgetCompare` | 56 | Budget vs actual, two date ranges side by side |
| `ChargeDetail` | 30 | Charges posted in a window |
| `Delinquency` | 85 | Delinquency as of a date |
| `FilteredIssueList` | 112 | Service issues in a window |
| `GeneralLedger` | 51 | **HTTP 500 as of 2026-08-31, not re-tested. Use `VW_General_Ledger` instead** |
| `LeaseExpiration` | 76 | Leases expiring in a range |
| `MarketRent` | 72 | Market rent analysis |
| `MoveInMoveOut` | 77 | Turnover in a window |
| `ProspectBoxScore` | 21 | Lead funnel counts |
| `ProspectStageListing` | 676 | Prospects by stage |
| `RentRoll` | 67 | Rent roll and recurring charges |
| `RentRollCompare` | 68 | Rent roll period over period |
| `SummaryRentRoll` | 69 | Per-community rollup, **VACANT rows drive vacancy composition** |
| `UnitAvailability` | 10 | Available units as of a date |
| `UnitList` | 6 | Rental unit listing |
| `UnitTypeVacancy` | 75 | Vacancy by unit type |
| `UtilCustomerConsumption` | 102 | Utility consumption by tenant |
| `Vacancy` | 74 | Vacancy, detail or summary |

Entity types resolvable: `GLAccounts` (1,000 returned, looks like a cap), `Properties`, `PropertyGroups`, `Units`.

**Standing trap:** Rent Manager returns `IsActive: false` on all 82 properties. Do not filter on it.

### RentViewer data warehouse — `RentViewer_Data_Warehouse`

**11 models, verified by `get_schema` 2026-09-09.** The five the vault knew about, plus six.

| Model | Measures | Covers | Known trap |
|---|---|---|---|
| `VW_Budget_Comparison` | 37 | NOI, revenue, opex, budget variance by property / GL account / month. 18 segments including `capexAccounts`, `utilitiesGroup`, `repairsMaintenanceGroup` | The budgeting source of record. Named measures are whole groups — list distinct GL accounts inside a segment before defining a category |
| `VW_Aged_Receivables` | 12 | AR aging buckets, percent over 90, customers with balance | — |
| `VW_Rental_Unit_Listing` | 11 | Occupancy, vacancy, unit counts, market vs actual rent, loss to lease | **Times out at 120s filtered on `propertyName` with `contains`. Filter on `propertyId` with `equals`.** The per-lot denominator |
| `VW_Summary_Rent_Roll` | 12 | Collections, collection rate, vacancy loss, deposits | — |
| `VW_MoveIns_MoveOuts` | 4 | Turnover, net movement | — |
| **`VW_Properties`** | 5 | Property reference list, active flag, address, state | Holds no financial or occupancy figures |
| **`VW_General_Ledger`** | 10 | Transaction-level postings, cash basis | **Will not agree with `VW_Budget_Comparison`** — different basis, different dating |
| **`VW_Service_Manager_Issues`** | 7 | Work orders open and closed, 2018 to date | ~10% of rows carry no Property ID |
| **`VW_Infill_Make_Ready`** | 8 | Infill and make-ready projects, checklist progress | Dates run to 2029, includes planned work |
| **`VW_Short_Term_Rentals`** | 9 | RV reservations and the charges against them | Reservation-level totals repeat per row — use `transactionAmount`, never sum a total |
| **`VW_Reservation_Activity_Feed`** | 5 | RV activity allocated by calendar month, six parks | **Carries no property identifier matching the Properties list — it cannot be joined to any other model or restricted by property** |

**Portfolio-wide rule that applies to every model here:** most are point-in-time snapshots restricted to the latest period unless grouped by `reportMonth`. Always state the as-of period. `run_query` requires the `question` parameter.

**Standing scope hole:** 22 property records carry occupied lots and zero utility expense of any kind in 2026, roughly 1,200 occupied lots, mostly the pre-Parakeet A2Z and Bedrock layer. `KP-0093`, `TD-0573`. Any portfolio per-lot figure states how many records it covers.

### Everything else

| Connector | What it exposes | Probed |
|---|---|---|
| **Plaud** | Recordings, transcripts, AI notes, highlights. Authenticated as `austin@parakeetcommunities.com`, workspace `ws_clEURiICSQ` | **2026-09-09, auth confirmed.** Recording count not pulled this run |
| **Microsoft 365** | SharePoint, OneDrive, Outlook mail and folders, Teams messages, calendar. **Mail is read-only — no drafts, `Mail.ReadWrite` not consented** | Not probed 2026-09-09. Live 2026-09-04 |
| **Gmail, a2zcp mailbox** | The Bedrock and A2Z mail estate. **The only working draft path in the estate** | Not probed 2026-09-09. Live 2026-09-04 |
| **Google Drive** | Four Shared Drive roots on `austin@a2zcp.com` | Not probed 2026-09-09. Live 2026-09-03 |
| **Dropbox** | A2Z MHC team space, ten mounts, 445 GB | Not probed 2026-09-09. **Dropped mid-session 2026-09-03** |
| **ClickUp** | Tasks, comments, hierarchy | Not probed 2026-09-09 |
| **Ramp** | Transactions, bills, cards, spend. See [[10-Business/vendors/ramp]] and [[95-Agents/ramp-charge-coding-agent]] | Not probed 2026-09-09 |
| **No connector exists** | AvidXchange · AHJ permit portals · state MH title and VIN portals · MAV/Nav CRM · Camp Spot booking · QuickBooks · lender portals (21st Mortgage, Triad) | — |

---

## Consumer layer — what feeds what

**Read the first line of this section before anything else. There are two disconnected worlds, and that is the whole answer to "why don't these stay linked."**

**The two dashboards the team actually looks at do not touch the MCPs at all.** The Ops Dashboard and the Founders Report read CSV exports off a synced SharePoint folder. The MCPs feed the vault's own surfaces and ad-hoc analysis. Nothing crosses. So a report can go stale on one side while the other side reads fine, and no single person sees both.

### Fed by CSV export off `Parakeet Birdcage - Data & Analytics` (OneDrive sync)

| Consumer | Fed by | Cadence | Owner |
|---|---|---|---|
| **Ops Dashboard** — `parakeet_dashboard.html` | Rent Manager CSV exports: `*_Rent_Roll`, `*_Receivables`, `Eviction_*`, `Asset_*`, `Prospects.csv`, `Summary Rent Roll.csv`, per-community `General Ledger - XXX.csv`, plus `2026 Budgets_All.csv` and `Property Data Sheet.xlsx`. Pipeline: `build_data` → `apply_data_fixes` → `build_financials` → `build_forecast` → assemble | On request, skill `parakeet-dashboard-refresh` | **none recorded** |
| **Founders Report** — `founders_report.html` | Same pipeline plus `build_founders_report.py`, injected into the founders shell in the Communication Dashboards folder | Scheduled Monday, skill `parakeet-founders-report-refresh` | **none recorded** |

Standing rules on both: sold properties are stripped via `excluded_properties.json` (Congress/CONG and Shelle Pointe/SP, sold July 2026) run against the **staged** copy, never the OneDrive originals. **Historical `ar_history.json` snapshots are never scrubbed** — Austin's instruction 2026-07-27. The founders build refuses to ship on fewer than 60 GL files or fewer than 60 properties. **Never pull GL, Summary Rent Roll or Issue History through the SharePoint connector** — transcription risk on financial data; read the synced files off disk.

**Naming discrepancy to settle:** the refresh skill writes `Parakeet_Ops_Dashboard_v2.html` in one place and `parakeet_dashboard.html` in another. One of those is wrong. `TD-0616`.

### Fed by the MCPs

| Consumer | Fed by | Cadence | Owner |
|---|---|---|---|
| **Community hot sheets** — the `## Live from Rent Manager` block on every community page | RentViewer, five queries: `VW_Rental_Unit_Listing` (occupancy, unit count) · `VW_Summary_Rent_Roll` (collection rate, charged, paid) · `VW_Aged_Receivables` (AR total, customers with balance) · `VW_Aged_Receivables` (over 90, percent over 90) | Monthly, after the Director of Ops approves the Month End Tracker on the 29th **and** month end is entered in Rent Manager per SOP 301. Running earlier pulls a half-closed month | Claude, via [[90-Skills/community-hot-sheet-refresh]] |
| **Community pulse** — lot pages, asset pages, [[60-Communities/open-items]] | Outlook **For Signature folder first** (Adobe Sign `CODE_TYPE_NUMBER` kickoffs and closeouts, the only structured property-activity feed in the mailbox), then Outlook keyword search, Teams, filed transcripts, Rent Manager | Weekly, Monday before the 8:30 Jon catch-up | Claude, via [[90-Skills/community-pulse-refresh]] |
| **Open board** — [[00-Meta/open-board]] and `00-Meta/board-data/` | Parsed from the six registers in the vault. **No external connector** | On demand | Claude |
| **Morning brief / daily close** | Outlook (all folders, read state means nothing), Gmail a2zcp, Teams, Plaud, calendar | Daily | Claude |

### Fed by nothing, or by nobody

| Consumer | Situation |
|---|---|
| **Listings dashboard** | Fires 06:00 weekdays. **No logging, no alerting, no retry, and no owner.** Misfired 2026-08-31 — John said on the call "this is the wrong version that misfired this morning" and the point went by unremarked. The earlier Chrome-driven version "was always breaking with the attachment." `TD-0619` |
| **Prospect funnel dashboard** | Aggregates roughly fifteen sources — Nav CRM exports, a warehouse CSV, Rent Manager CSV drops, Microsoft Bookings, an RV bookings site, Google Analytics, RingCentral. **Not live and not circulated** |
| **EOS scorecard** — [[10-Business/eos/scorecard]] | **Out of scope for this register.** No measure has a data feed today, and **Zach Schwartz is rebuilding the scorecard** as his Q1 rock. Feeds get mapped once the rebuild defines the measures — mapping them against the current names would be pre-work against a spec that does not exist. Withdrawn 2026-09-09 on Austin's instruction |

---

## Feed map: every source, which agent harvests it, where it lands

**Added 2026-09-29, Phase 3 of `00-Meta/brain-architecture.md`, under rule 20 in `CLAUDE.md` (facts land here first).** One row per source. *Schedule* is read from the live scheduled task list on 2026-09-29, not from a brief; a brief that names a time with no scheduled task behind it is marked **not scheduled**. Rows with no running harvester are the hiring list for the agent team.

| Source | Harvested by | Schedule, verified 2026-09-29 | Writes to | Status |
|---|---|---|---|---|
| **Outlook**, all folders, **For Signature first** | `95-Agents/morning-brief`, `90-Skills/end-of-day`, `90-Skills/community-pulse-refresh` | Close runs weekdays 6:00 PM. **Morning brief: not scheduled** (brief says 6 AM). Pulse: on request | The six registers, community pages, `00-Meta/daily-close/` | Partly running |
| **a2zcp / Bedrock Gmail** (first class, rule 14) | `90-Skills/end-of-day`, morning brief | Weekdays 6:00 PM through the close | `80-Finance/fund-reporting/bedrock-fund-ii-winddown.md`, `30-Customers/capital-partners/bedrock-fund-ii-lps.md`, registers | Running through the close |
| **Tim and Lisa (Citrin)**, both mailboxes | Nobody by name. The close sees their mail as part of the sweep | None of its own | `10-Business/outside-help/citrin-cooperman.md`, `00-Meta/commitments.md` | **Gap.** Austin ruled 2026-09-29 their mail matters to everything; no sweep flags it first yet |
| **Teams** chats and channels | `90-Skills/end-of-day`, community pulse | Weekdays 6:00 PM through the close | Registers, community pages | Running. Meeting transcripts blocked tenant wide (see [[10-Business/connector-status]]) |
| **Plaud** recordings | `95-Agents/transcript-to-action`, `90-Skills/transcript-filing` | On request only | `70-Operations/meetings/`, decisions, registers | **Gap.** 283+ recordings; nothing picks up a new one on its own |
| **Adobe Sign** kickoffs and closeouts (via For Signature) | Community pulse; skill `kickoff-closeout-review-sign` | On request | Community pages, lot pages, WIP bridge in `80-Finance/jrefi-cashflow-model.md` | On request |
| **Rent Manager API** | `90-Skills/community-hot-sheet-refresh`; *Accounting daily audit* task | Audit weekdays 6:00 PM. **Hot sheets: not scheduled** | Community hot sheets (Live block), `80-Finance/` | Partly running |
| **RentViewer warehouse** | Hot sheet refresh, *Rehab call pre-read* task, `90-Skills/data-lineage-probe` | Pre-read Tuesdays 5:00 PM. **Lineage probe: not scheduled** (page says weekly) | Hot sheets, `70-Operations/rehab-program/`, this page | Partly running |
| **Rent Manager CSV exports** (Birdcage Data & Analytics sync) | *Ops dashboard v3 daily refresh* task; skill `parakeet-founders-report-refresh` | Ops dashboard daily 6:50 AM. **Founders report: no scheduled task found** (this page says Mondays) | The two dashboards, outside the vault | Ops running; founders report to confirm |
| **Ramp** | *Weekly Ramp expense audit* task; `95-Agents/ramp-charge-coding-agent` | Audit Mondays 9:00 AM. **Bookkeeper agent paused, not built** | Ramp booking program, `80-Finance/` | Audit running; booking is a gap |
| **ClickUp** | *Month end close list* task; skill `meeting-transcript-to-clickup` | 1st of the month 6:00 AM | ClickUp (outbound), EOS to-dos | Running |
| **SharePoint Accounting & Finance folder** | *Accounting daily audit* task | Weekdays 6:00 PM | `projects` audit notes, registers | Running |
| **Paychex files** (Payroll Project folder) | Skill `payroll-tie-out` | On request, per check date | `80-Finance/payroll-model.md` | On request |
| **Dropbox and Google Drive** (Fund II and A2Z records) | Fund II program, by hand | None | `80-Finance/fund-reporting/` | On request |
| **No connector:** AvidXchange, AHJ permit portals, state title portals, MAV CRM, Camp Spot, QuickBooks, lender portals | Nobody | None | None | **Structural gap**, see connector-status |

### The hiring list, cheapest first

1. **Schedule what is already written.** Morning brief (weekdays 6 AM) and weekend pulse (Fridays 7 PM) have finished briefs and no scheduled task. Same for the hot sheet refresh, community pulse and data lineage probe, which their pages call weekly.
2. **A Citrin watch.** Every sweep lists Tim and Lisa's mail first, in both mailboxes, with the ask and the deadline.
3. **A Plaud harvester.** Daily, picks up recordings since the last run and runs transcript-to-action on each.
4. **The Ramp bookkeeper.** Brief exists, agent not built, scheduled task paused.
5. **Confirm the founders report schedule.** This page says Mondays; no scheduled task exists.

### Three paths for building the team

- **A. Schedule the briefs that exist, one task each.** Items 1 and 5 above, about an hour of setup, no new agents. Leaves Citrin, Plaud and Ramp uncovered. Wrong if the goal is coverage of every source.
- **B. One daily harvester agent that sweeps every source in a single run** and writes to the registers. Fewest moving parts. Wrong because one failure blinds every feed at once, and a single run long enough to read everything is the kind that times out.
- **C (recommended). One agent per source, each with one brief, one schedule and one page it writes to,** built cheapest first from the list above. Starts with A's step, so the first win is the same hour of setup; adds Citrin, Plaud and Ramp one at a time. Wins over B because a broken feed breaks alone and shows up as one stale row here, and over A because it closes the gaps rather than stopping at what is already written.

## Breaks and unowned feeds

| # | What | Consequence | ID |
|---|---|---|---|
| 1 | Listings dashboard has no owner, no logging, no alerting, no retry | It has already silently shipped the wrong version once | `TD-0619` |
| 2 | Ops Dashboard and Founders Report have no recorded owner or last-refresh date | Nobody can say whether the number on screen is from today or from July | `TD-0616` |
| 3 | RM report 51 `GeneralLedger` HTTP 500, unresolved since 2026-08-31 | Blocks capex committed-vs-paid, `KP-0087`. **Now has a warehouse workaround to test** | `TD-0617` |
| 4 | connector-status records Camp Spot RV as invisible; the warehouse has six parks of live reservation data | The vault is telling itself it is blind where it is not | `TD-0618` |
| 5 | Warehouse `VW_Reservation_Activity_Feed` cannot be joined to any other model | RV occupancy can never be consolidated with MH occupancy in one query | `KP-0104` |
| 6 | Two dashboards run off CSV exports of the same data the MCPs serve live | Every re-save is a desync risk — the design rule accepted on the 2026-08-31 call was that anything built on the source of truth should visualise it, never re-save it | `KP-0105` |
| 7 | Home Sales tracker shipped to eleven people with **STALE SOURCE** in its own subject line, 2026-09-10 08:12 ET, third occurrence | Leadership is reading an operating report that announces its own data is old and nobody has stopped the send | `KP-0109` |
| 8 | The rehab tracker export in `70-Operations/rehab-program/data/` is still the 2026-08-28 pull; no fresh export arrived by mail or Inbox through 2026-09-15 | Two pre-call packs (09-08, 09-15) ran on 11 and 18 day old data and said so on their face; no gap can be said to have closed or widened | No register row; the packs record it. See `70-Operations/rehab-program/weekly-call` |

---

## Related

- [[10-Business/connector-status]] — connector identity, auth, what is blocked and who fixes it
- [[10-Business/systems-architecture]] — the undecided single-source-of-truth question that sits underneath all of this
- [[10-Business/tools-and-systems]] — every system that runs the business
- [[90-Skills/data-lineage-probe]] — the routine that rewrites the source layer above
- [[00-Meta/id-conventions]] — why a hand-maintained state page is not trusted here
