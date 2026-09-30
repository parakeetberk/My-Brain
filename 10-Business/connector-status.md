# Connector Status

**What this is:** Which systems Claude can actually reach from this Brain, tested rather than assumed, and what each one gives us.

**The report catalog moved, 2026-09-09.** **[[10-Business/data-lineage]] now owns what each connector exposes and what consumes it.** This page keeps connector identity, authentication, and the blocked list. **Two corrections that page carries against this one, both verified 2026-09-09 by direct call:** the warehouse has **eleven models, not five**, and the Camp Spot entry below is wrong in one direction - the booking system is still unconnected but **the six RV parks' reservation data is in the warehouse**, 643 reservations and 87,095 occupied days. Both readings are kept rather than smoothed over. `KP-0104`, `TD-0618`.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

**Verified**: 2026-08-26, by direct test of each connector rather than assumption.
**Why this file exists**: several capabilities recorded earlier this week as blocked turned out to be live, and one recorded as live was not. Test before asserting.

---

## LIVE: confirmed by successful call

| System | Identity / scope | What it gives us |
|---|---|---|
| **Microsoft 365** | austin@parakeetcommunities.com | SharePoint (12+ sites), OneDrive, Outlook mail, Teams **messages**, calendar. **READ ONLY on mail: it cannot create, edit or send drafts.** Tested 2026-09-03 by attempting `outlook_create_draft`; Graph returned `403 ErrorAccessDenied`, `graphErrorCode: ErrorAccessDenied`, with the tool reporting the app registration is missing the **`Mail.ReadWrite`** delegated permission. **So every drafted email is delivered as a file for Austin to paste, not saved into his Drafts folder.** Fixing it needs admin consent for `Mail.ReadWrite` on the confidential client app registration. |
| **Dropbox** | austin@a2zcp.com, A2Z MHC team, ns `11855305057` | Full team space, 445.2 GB |
| **Google Drive** | **still `austinrberk@gmail.com`, re-tested 2026-09-03** | Personal Drive plus three corporate Shared Drives. **The Drive identity did NOT move when the mail identity did.** See the split connector note at the bottom of this page |
| **Google mail, added 2026-09-03** | **the a2zcp mailbox**: `austin@a2zcp.com`, `austin@thebedrockgrp.com`, **`ir@thebedrockgrp.com`**, `bills@a2zcp.com` | **The second mailbox, and the only route to the Fund II LP base.** Gmail tools, not Microsoft 365. Scope, label IDs and traps: [[10-Business/a2z-mailbox-map]]. **WRITE CONFIRMED 2026-09-03: `create_draft` succeeded and returned a draft id.** So this connector can compose drafts where Microsoft 365 cannot. **It is the only working draft path in the estate today, and it is the wrong mailbox for Parakeet property and operations correspondence**, which needs the Parakeet address. Correct for Bedrock, A2Z and fund matters. **Reading drafts back was refused by the session permission classifier**, so composition is available and verification of the composed draft is not; check it in Gmail. |
| **ClickUp** | Parakeet workspace | Tasks, comments, hierarchy. Control plane for the SharePoint restructure |
| **Rent Manager** | Reporting API | **21 enabled reports** + entity lists |

**Re-tested 2026-08-31 evening, after a full day of failures.** Earlier today every RentViewer warehouse query timed out at 60 seconds and the Rent Manager report API returned HTTP 500 on `FilteredIssueList` and `UnitAvailability`. **The reporting API is back**: `list_reports`, `list_entities` (GLAccounts, 1,000 returned and that looks like a cap) and `BudgetCompare` all returned live data. **`GeneralLedger`, report 51, still returns HTTP 500** on both a single GL account and a list of them, so transaction-level detail remains unreachable. That one report is the blocker for per-project capex analysis, see [[60-Communities/projects]]. VERIFIED, all calls made this session.
| **RentViewer warehouse** | Semantic layer | **5 models**; see below |
| **Plaud** | Authenticated 2026-08-26 | **283 recordings**: transcripts, AI notes, highlights |

### Rent Manager: 21 reports enabled

`AgedReceivables` (78) · `AssetListing` (244) · **`BalanceSheet` (38)** · `BudgetCompare` (56) · `ChargeDetail` (30) · `Delinquency` (85) · `FilteredIssueList` (112) · **`GeneralLedger` (51)** · `LeaseExpiration` (76) · `MarketRent` (72) · `MoveInMoveOut` (77) · `ProspectBoxScore` (21) · `ProspectStageListing` (676) · `RentRoll` (67) · `RentRollCompare` (68) · `SummaryRentRoll` (69) · `UnitAvailability` (10) · `UnitList` (6) · `UnitTypeVacancy` (75) · `UtilCustomerConsumption` (102) · `Vacancy` (74)

Entity types resolvable: `GLAccounts`, `Properties`, `PropertyGroups`, `Units`.

**Balance Sheet and General Ledger are both enabled.** Berman stated on 2026-08-26 that a consolidated balance sheet has *never been produced*. It can be run on demand.

### RentViewer warehouse: 5 models

| Model | Covers |
|---|---|
| `VW_Budget_Comparison` | NOI, revenue, opex, budget variance by property / GL account / month. Has NOI margin and operating expense ratio with stated targets (NOI margin >50%, OER <45 to 50% for stabilized MH) |
| `VW_Aged_Receivables` | AR aging buckets, percent over 90, customers with balance |
| `VW_Rental_Unit_Listing` | Occupancy, vacancy, unit counts, market vs actual rent, loss to lease |
| `VW_Summary_Rent_Roll` | Collections, collection rate, vacancy loss, deposits |
| `VW_MoveIns_MoveOuts` | Turnover, net movement |

Four of five are **point-in-time snapshots** restricted to the most recent period unless grouped by `reportMonth`. Always state the "as of" period. All access is read-only, row-level-security filtered, and audited. `run_query` requires the `question` parameter.

---

## BLOCKED: needs someone to act

| Blocked | Who fixes it | Cost of leaving it |
|---|---|---|
| **Teams meeting transcripts**: `GraphAccessToTranscriptsDisabled`, tenant-wide, confirmed across two tenants | **Tenant admin** | Partly mitigated now that Plaud is connected, but Teams-only meetings with no Plaud recording remain invisible |
| **AvidXchange** | No connector exists | AP exceptions invisible; the $108,919 A&A invoice sat unassigned since April |
| **AHJ permit portals** | Per-jurisdiction credentials | Blocks the permit-renewal monitor. Recommend starting with the 5 to 6 jurisdictions covering the most communities |
| **State MH title / VIN portals** | State-by-state access | Blocks title lookups; needed for the Gulf Breeze FEMA sell-vs-scrap call and the PSE title cleanup |
| **MAV CRM**, **Camp Spot** | Vendor connectors | Camp Spot holds 6 RV communities / ~400 sites invisible to Rent Manager |
| **QuickBooks / accounting platform** | Unknown | Rent Manager GL is reachable; the accounting-side books are not |
| **Lender portals** (21st Mortgage, Triad) | Credentials | Registration status invisible; this is exactly how a financing channel went dark unnoticed |

---

## NOT PERMISSIONS: structural API limits, cannot be granted away

These constrain method regardless of access level. Design around them.

- **Graph `read_resource` caps at ~200 children** with no pagination parameter. Long folder listings truncate mid-alphabet. Recover tails with targeted `sharepoint_search`.
- **SharePoint library sync shortcuts are invisible to the Graph file API.** Three of the most current libraries on Austin's OneDrive (`Parakeet Communities`, `Parakeet Birdcage - Corporate`, `Parakeet Birdcage - Data & Analytics`) were found only via the local sync folder. Assume the same gap on other drives.
- **Google Shared Drive memberships cannot be enumerated.** Three corporate Shared Drives were found under Austin's personal Gmail only by walking `parentId` chains upward. Three is a floor.
- **Graph rate limits (429)** throttle deep sweeps. Repeatedly cut short chat coverage this week. Stagger and checkpoint rather than brute-forcing.
- **openpyxl drops embedded images on load/save round-trip.** Rebuild branded workbooks from the generator; never append in place.
- **Rent Manager returns `IsActive: false` on all 82 properties.** Near-certainly a maintenance artifact, not reality. **Do not filter on it.**

---

## Corrections to earlier records

| Previously recorded | Actually |
|---|---|
| "Plaud is unauthenticated and unreachable" | **Live.** A `login` tool existed and was never tried. 283 recordings. |
| "Rent Manager is not connected" | **Live**, 21 reports including Balance Sheet and General Ledger. |
| "The RentViewer warehouse is a future dependency" | **Live**, 5 semantic models. |
| "The definitive entity list must come from Berman" | **82 entities are already enumerable** from Rent Manager. This was the gating prerequisite for the intercompany AR/AP programme. See `80-Finance/intercompany-arap-recon.md`. Berman's sign-off still matters for *treatment*; the *list* no longer blocks anything. |

**Lesson recorded**: three capabilities were logged as blocked on the strength of one failed call or an assumption, and stayed logged that way for a full day of planning. Test the connector before recording a limitation, and re-test before repeating it.

---

## What this unlocks immediately

1. **Portfolio analytics on demand**: occupancy, NOI, AR aging, loss to lease, turnover, budget variance. The vault had none of this before today.
2. **The spoken layer becomes searchable.** 283 Plaud recordings covering site visits, vendor calls, and internal meetings. This is what ends the false-silence problem that produced four wrong findings this week.
3. **The consolidated balance sheet** Berman says was never produced.
4. **The 82-entity list** that was gating the intercompany reconciliation.
5. **Supply-chain measurement becomes possible.** Occupancy, vacancy, and turnover data plus meeting transcripts means days-on-site-unset and permit aging can finally be quantified rather than inferred.


## Correction and addition, 2026-09-03

**The Google connection changed and it is no longer a Drive only account.** Austin, 2026-09-02: *"I will change my google connection to a2zcp.com which has bedrock emails forwarded to."* Confirmed live 2026-09-03 by direct call. **This page listed Google Drive under a personal Gmail and listed no mail connector at all**, which was true when written and is now half the picture.

**What was tested this session, and the result:**

- **Gmail tools against the a2zcp mailbox: LIVE.** `list_labels` returned the full label set with counts; `search_threads` and `get_thread` returned mail across the mailbox's whole history.
- **Microsoft 365 against the same mailbox: NOT REACHABLE, and do not retry.** `outlook_email_search` with `mailboxOwnerEmail: "austin@a2zcp.com"` returns `ErrorInvalidUser` with Graph status 404. **It is a different tenant and no delegate access exists**, which is consistent with what the A2Z credential work already recorded about a legacy tenant sitting outside Parakeet's.

**Why the distinction matters more than a row in a table.** Every sweep in this Brain resolves mail through the Microsoft 365 connector. **The Fund II LP base, the Bedrock tax stream and the legacy assets' operating mail are all unreachable that way**, and were unread until 2026-09-03. See [[CLAUDE]] rule 14 as extended the same day.

---

## The Google connection is split, and this page has been saying otherwise. Tested 2026-09-03

**Austin, 2026-09-03:** *"i updated the connection in gmail to a2zcp / bedrock email account from personal. nothing in personal and need more hands and eyes on the a2zcp and bedrock account."*

**The correction is one word: gmail, not Google.** The section above and [[10-Business/a2z-mailbox-map]] both read as though a single Google identity moved from personal to a2zcp. **Two connectors are involved and only one of them moved.**

| Connector | Authenticates as | Tested |
| --- | --- | --- |
| **Gmail tools** | **the a2zcp mailbox.** `in:inbox newer_than:3d` returned live threads addressed to `ir@thebedrockgrp.com`, `austin@thebedrockgrp.com` and `austin@a2zcp.com` | VERIFIED 2026-09-03, this session |
| **Google Drive tools** | **`austinrberk@gmail.com`, unchanged.** `list_recent_files` returned items owned by that address on the personal My Drive root `0AA-ebv6mPPW-Uk9PVA` | VERIFIED 2026-09-03, this session |

**Why the distinction is worth a section rather than a footnote.** `KP-0008` and `TD-0008` exist because three corporate Google Shared Drives holding cap tables, fund subscriptions, K-1s, an LPA and executed signature pages are reachable only through a consumer Gmail identity. **A reader of the 2026-09-02 correction above could reasonably conclude that switching the connection resolved that.** It did not. The securities exposure is unchanged, and the only thing that changed is which mailbox this Brain can read.

**The second half of the instruction is a weighting rule, not a scope one**, and it lives in [[CLAUDE]] rule 14: the a2zcp and Bedrock mailbox gets first class attention on every routine, and where a sweep has to be cut short, Outlook is what gets cut. **The personal Google account is not a content source.** Nothing is harvested from it and no register row is built out of it.

**One thing not decided here.** Whether "nothing in personal" means the personal Drive should be disconnected outright, or simply not read. It is still connected and still reachable as of this session. `PD-40`.

### Follow up, same day: two Google accounts are already connected at once, and the personal one is not empty

Austin, 2026-09-03: *"I can only connect one mailbox at a time through the connector unless you know another way."*

**There is another way and it is already in force. Gmail and Google Drive are separate connectors with separate authentication.** The one mailbox limit is real and applies to Gmail only. It says nothing about Drive.

**Verified this session, both live in the same minute:**

- `search_files` with `owner = 'me'` returned files owned by `austinrberk@gmail.com` on My Drive root `0AA-ebv6mPPW-Uk9PVA`.
- `search_threads` with `in:inbox newer_than:3d` returned live threads addressed to `ir@thebedrockgrp.com` and `austin@a2zcp.com`.

**So the current configuration is not a compromise, it is the best available arrangement, and it should be kept.**

### And "nothing in personal" is not accurate. The Bedrock document base is in there

**This is the finding that matters and it was found by opening the drive rather than reasoning about it.** The personal Drive connection reaches Shared Drives holding, VERIFIED by direct query:

| What | Where | Evidence |
| --- | --- | --- |
| **`Bedrock MHC Fund II`**, a Shared Drive folder with `Accounting`, `Analysis`, `Entities` and `Holdings` beneath it | Shared Drive `0AJ8dOob9gR0HUk9PVA`, folder `1-usxQGKvSEz22Anl2wE18ROi7Zh8cqex` | enumerated 2026-09-03 |
| **`Bedrock MHC Fund II, LP`** | folder `1cMRHDosvDm62_Js3d7VLih8uBXn_Y6Qp` | enumerated 2026-09-03 |
| **A `K-1s` folder holding per LP K-1 PDFs**, 2020 tax year, one file per partner including `A2Z Community Partners, LLC` | folder `1N-Wm4yA1vU1U3Z_37hXSvPaqf0k_UEL1`, under the Cambridge MHP Investment return set | enumerated 2026-09-03 |
| `Verivest Track Record_Bedrock MHC II.xlsx`, `BEDROCK Fund Presentation.pptx` and v2, `32. Bedrock EM Holdings LLC Entity Documents.PDF` | same estate | returned by full text search |

**Read that against what is happening in the a2zcp mailbox right now.** Five LPs and a joint venture partner are chasing the 2025 Fund II K-1 against a 2026-09-15 filing deadline. **The prior year K-1 set, the entity documents and the fund accounting folder for that exact fund are sitting in the drive Austin just described as having nothing in it.**

**The instruction and the evidence point opposite ways, so the instruction was not applied to Drive.** "Nothing in personal" stays in force for mail, where it is correct: no personal mailbox is connected and nothing is harvested from one. **It is not applied to Drive**, because applying it there would cut the only route this Brain has to the Bedrock fund record base at the exact moment that base is needed. `KP-0068`, `TD-0497`, `PD-40`.

**The gap that does exist, stated so nobody assumes coverage: the a2zcp account's own Google Drive is not reachable.** The Drive connector is on the personal identity, so whatever `austin@a2zcp.com` holds in Drive is invisible from here. Nobody has checked whether that is a lot or nothing. `TD-0498`.

### Third pass, 2026-09-03: the identities line up better than described, and there is a fourth Shared Drive

Austin: *"the a2zcp drive has a lot. but it is in austinrberk shared drives so let me know if you can access from there."*

**Answer: yes.** The Shared Drives are reachable through the personal Google identity, which is the identity the Drive connector holds. Enumerated this session by walking `parentId`, the same method the original survey used.

**A fourth Shared Drive root, not in the 2026-08-26 inventory.** `[[10-Business/storage-inventory/gdrive-personal]]` recorded three roots and said three was a floor. It was.

| Root | Top level | Status |
| --- | --- | --- |
| `0ANSvtCpaQmhVUk9PVA` | ~30 community folders, `_Archive`, `Administrative` | in the 2026-08-26 inventory |
| `0AHN7ilIBrGJRUk9PVA` | Parakeet corporate and ops, 14 folders | in the 2026-08-26 inventory |
| `0AFtyceEG0HhKUk9PVA` | `Cap Tables`, `Investor Relations`, `BMHCII - InvestorsRelations`, `A2Z Fund I - Subscriptions`, `RealPage_IMS`, `Violet Smears` | in the 2026-08-26 inventory |
| **`0AJ8dOob9gR0HUk9PVA`** | **`Parakeet Companies`, `Mobile Management` (A2ZMHC), `A2Z Community Partners`, `Bedrock MHC Fund II`, `BEDROCK I GROUP`, `A2Z MH Fund I`, `MoMa Lending`, `NewCo`** | **NEW, found 2026-09-03** |

**That fourth drive is the entity and fund layer of the pre Parakeet company, one folder per vehicle.** VERIFIED by direct listing. Four remains a floor for the same reason three was: **Shared Drive memberships cannot be enumerated through the API**, so the only way to find one is to already have a file inside it.

**The Dropbox connector is on the a2zcp identity, not a third one.** `who_am_i` returns `austin@a2zcp.com`, team **A2Z MHC**, root namespace `11855305057`, home namespace `4802313104`. **So two of the three Google era surfaces are already on a2zcp**: Gmail and Dropbox. Only Drive is on the personal identity, and that is the arrangement to keep, per `PD-40`.

**Ten team mounts at the Dropbox root:** `Business Lines`, `Property Management`, `Pipeline`, `Corporate`, `Accounting`, `Reference`, `Austin Berk`, `Team Paper Docs`, `Lamberton Lake DD Files`, `Cambridge - SCH 2025`.

### SWITCHED, 2026-09-03. The Drive connector is now `austin@a2zcp.com`

Austin: *"I also changed the account on the google drive connector."* **Tested immediately. All four Shared Drive roots return. Nothing was lost.** Full result and the four query checklist: [[10-Business/storage-inventory/gdrive-shared-drives-manifest]].

| Connector | Identity now | Root |
| --- | --- | --- |
| Gmail | `austin@a2zcp.com` and the Bedrock addresses | Gmail labels, see [[10-Business/a2z-mailbox-map]] |
| **Google Drive** | **`austin@a2zcp.com`** | My Drive `0ANBjF5CmkPsBUk9PVA`, ouid `115194717785561895747` |
| Dropbox | `austin@a2zcp.com`, team A2Z MHC | ns `11855305057` |

**All three surfaces are now one identity.** The split that this page spent a day documenting is closed.

**`KP-0008` shrank rather than closed, and the reason matters.** The corporate account's own view history on these drives predates the switch by weeks, which a switch cannot manufacture. **Both accounts were members all along**, so the continuity half of that finding was never true and this Brain wrote it down because it had only ever looked from one side. What remains is a consumer Gmail with standing membership in corporate Shared Drives holding securities records: **a removal, not a migration.**

**The personal My Drive is now out of view.** Belmart's closing set, the Amex folder and the loose JLB and Gilchrist financials went with it. Per Austin's *"nothing in personal"* that is intended, and it is recorded because `KP-0066` is about where personal documents live and Belmart's answer was that drive until today.

**Dropbox connector note:** the Dropbox MCP server disconnected from this session partway through 2026-09-03 and did not come back. Everything on this page about Dropbox was captured by calls that completed before it dropped. **`/Austin Berk/BMHCII`, the wind-down destination Austin named, has not been opened and is not described anywhere from observation.** `TD-0507`.


---

## Probe, 2026-09-04 morning brief. Everything this run needed answered

**Why this section exists:** the top of this page still carries a "needs review, as of 2026-08-26" status, and the standing instruction on volatile connectors is to test before relying and to say what could not be reached. **Tested live this run rather than assumed.**

| Connector | Result | Evidence |
| --- | --- | --- |
| **Microsoft 365 mail** | LIVE | Outlook Inbox returned all 64 messages since 17:00 ET 09-03; Sent Items 6 |
| **Microsoft 365 folders by ID** | LIVE | `read_resource` on `mail:///folders/{For Signature}` returned the folder, 0 items, 0 unread |
| **Microsoft 365 calendar** | LIVE | 8 events across the 09-04 window, `timeZone: UTC` on every one as always |
| **Microsoft 365 Teams** | LIVE, degraded | Per-chat scan path, 48 of 50 chats on page one, then **429 after 39 of 50 on page two**. Channel messages are never covered on that path |
| **Gmail, a2zcp mailbox** | LIVE | `in:inbox`, `in:sent` and three label queries all returned; `get_thread` returned full bodies |
| **Plaud** | **LIVE, recovered** | 311 recordings scanned, 9 matched for 09-02 to 09-04, `get_note` returned content on all three fetched. **This connector failed entirely on 2026-09-03**, which is why that close was provisional |
| **RentViewer warehouse** | **REACHABLE, not queried** | `run_query` returned a member-name validation error rather than a timeout or a connection failure, which is proof of a live semantic layer. Not queried for data because nothing on the brief turned on a portfolio figure |
| **Artifact `db`** | LIVE | `answers` and `notes` both read; both empty, which is expected on the page's first real run |

**The Plaud recovery is the entry that matters.** It was unreachable through the whole 2026-09-03 close, and the nine recordings that outage hid produced **two of this morning's eight findings** - `KP-0083`, A2Z Fund One's 2024-to-2025 trial balance break, and `KP-0084`, Evergreen's distribution appearing never to have been made. **Neither is visible in email at all.** That is the concrete cost of the spoken layer going dark for one day, and it is the argument for probing rather than assuming a connector is still down because it was down yesterday.

**Not tested this run, and not claimed either way:** Rent Manager's report API, Dropbox, SharePoint and Google Drive. None was needed. `GeneralLedger` report 51 is recorded above as returning HTTP 500 and that was not re-tested, which is worth knowing because it is the blocker on `KP-0087`, the capex committed-versus-paid gap.

## Correction, 2026-09-10: the Gmail connector is intermittently absent, and the table above still calls it LIVE

**Tested this morning at the morning brief and it is not reachable.** The Gmail tools are **absent from the session entirely**, which is a different failure from the ones this page already records: they do not appear in the tool list at all, they do not error, and no authentication prompt is raised. A search of the deferred tool registry for `search_threads`, `get_thread` and `list_labels` returns nothing.

**This is now the third recorded loss and the second consecutive routine.** The 2026-09-04 Weekend Pulse lost it and Austin reconnected it the same evening. The 2026-09-09 end of day close lost it again. The 2026-09-10 morning brief lost it again. **The row in the LIVE table above is true when it is true and it is not durable**, so a sweep must probe rather than assume.

**What it costs, stated as a number rather than as a complaint.** `austin@a2zcp.com` carrying `austin@thebedrockgrp.com`, **`ir@thebedrockgrp.com`** and `info@thebedrockgrp.com` is the only route to the Fund II LP base and the Bedrock tax stream, and [[CLAUDE]] rule 14 ranks it **ahead of** Outlook when a run is cut short. `KP-0088`, the 74 thread `To Respond` backlog, is now unread for a **fourth consecutive routine**. The 2026-09-15 Fund II filing date is five days out and eleven parties are chasing K-1s through that mailbox.

**What this does not establish.** Whether the connection is revoked, expired, or simply not loaded into these sessions is **not known** and is not guessed. The distinction matters because only one of the three is fixable by Austin reconnecting it, which is what worked on 2026-09-04.

**Not re-tested on 2026-09-10 and not claimed either way:** Google Drive, Dropbox, ClickUp, Ramp. **Probed and up on 2026-09-10:** Microsoft 365 (mail, calendar, Teams, with a Graph 429 on the second page of the chat scan), Rent Manager (21 reports), the RentViewer warehouse (full `VW_Budget_Comparison` measure catalogue), and Plaud. **Plaud is a separate finding**: it authenticates and answers, and its newest recording is **2026-09-05 19:55 ET**, so the library has not grown across 09-07, 09-08 or 09-09 despite a full meeting schedule. **Reachable and empty is not the same as working**, and with Teams meeting transcripts disabled tenant wide, Plaud is the only spoken layer this Brain has.

### Fourth consecutive loss, 2026-09-10 end of day close

**Probed again at 17:32 ET and the Gmail tools are still absent from the session.** Same signature as the three losses recorded above: not toggled off, not erroring, not prompting for authentication, simply not present in the tool registry. A search for `search_threads`, `get_thread` and `list_labels` returns nothing.

**This is the fourth consecutive routine and the second loss on the same calendar day**, the 2026-09-10 morning brief being the third. **`KP-0088`, the 74 thread `To Respond` backlog, is now unread for a fifth routine**, and 2026-09-15 is five days out with eleven parties chasing Fund II K-1s through that mailbox. One of them, David K. Gustafson of DKG Print, set his own 2026-09-10 deadline and **whether he wrote again today cannot be established from here.**

**Probed and up on the same run:** Microsoft 365 mail, calendar and Teams, the last on the per chat scan path at 48 of 50 chats with no channel coverage. **Plaud authenticates and answers and its newest recording is still 2026-09-05 19:55 ET**, so the library has now not grown across five working days and roughly twenty meetings. **Not probed this run and not claimed either way:** Rent Manager, the RentViewer warehouse, Google Drive, Dropbox, ClickUp and Ramp. **The artifact `db` was read and written successfully**, `answers` returning twelve documents and `notes` none.

### Recovery, 2026-09-12: the Gmail run of losses ended and Plaud started growing again

**Both connectors this page last recorded as down are up, and both were probed rather than assumed.**

**Gmail is present.** The tools loaded into this session on the first request and answered on every call: `list_labels` returned the full label set with counts, `in:inbox after:2026/09/10` returned 35 threads, `in:sent` returned two, and `get_thread` returned full bodies on five threads. **That ends a run of four consecutive routines with the tools absent from the session entirely**, recorded above across 2026-09-09, both 2026-09-10 routines and the 2026-09-10 close. **Why it came back is not known and is not guessed**, exactly as the loss itself was not diagnosed.

**`KP-0088` is readable again and it has not moved.** The `To Respond` label holds **74 threads and 236 messages, 0 unread**, the same 74 threads recorded when it was last visible. **The backlog did not grow during the blackout and it did not shrink either.**

**Plaud has grown for the first time since 2026-09-05.** Four recordings uploaded on 2026-09-11 between 11:36 and 11:38 ET, covering two meetings from 2026-09-09 and two from 2026-09-11. **320 recordings scanned.** The previous two routines both recorded the newest recording as 2026-09-05 19:55 ET across five working days and roughly twenty meetings, and that gap is now partly filled rather than fully: **the 2026-09-09 pair arrived two days late, which is the upload lag this Brain already expects, and 09-07, 09-08 and 09-10 are still empty.**

**One recording is present and has no transcript.** The 2026-09-11 09:19 ET recording, 66 minutes, matching the 09:00 to 12:00 ET calendar block titled `Rick`, returns an empty array on `get_note`, on the `outline` block and on the `transaction` block. **It is not transcribed yet and no conclusion is drawn about why**, per the standing rule in [[90-Skills/end-of-day]] that a placeholder theory about the app was wrong within ninety minutes the first time it was written.

**Probed and up this run:** Microsoft 365 mail, calendar and Teams; Gmail on the a2zcp mailbox; Plaud; the artifact `db`, which returned 15 documents in `answers` and none in `notes`. **Not probed and not claimed either way:** Rent Manager, the RentViewer warehouse, Google Drive, Dropbox, ClickUp and Ramp. **`For Signature` could not be read by folder name this run**, returning `NOT_FOUND`; the folder map records that most folders need their IDs and this run did not fall back to the ID, so **the pending signature queue is unswept and nothing below speaks for it.**

### Outage, 2026-09-14: Microsoft Teams returned nothing on three attempts, and the mail and calendar halves of the same connector were fine

**Teams is the only thing down this morning and it is down hard.** `chat_message_search` was called three times at the morning brief: once with a date filter from 2026-09-12, once repeated, and once as a bare `*` with no filter to force the Graph Search path. **All three returned a Microsoft Graph 429 with `chatsScanned: 0` of 50 chats listed, `chatsFailed: 4`, and `stoppedBy: rate_limit`.** No channel coverage either way.

**Why this is recorded as an outage rather than as a quiet sweep.** Teams has been the primary source for two of the last week's emergencies, including the payroll allocation model exchange of 2026-09-10 that turned `CM-13` from a personnel timeline into a records question. **A Teams scan returning zero is not evidence that nothing was said**, and the 2026-09-14 brief states that on its face rather than absorbing the gap. Nothing Teams derived was called open or closed on that run.

**The rest of the Microsoft 365 connector was healthy on the same session**, which is the useful diagnostic: `outlook_email_search` paged the Inbox and Sent Items, `outlook_calendar_search` returned five events, and `read_resource` read the `For Signature` folder by ID. **So this is Graph throttling on the chat endpoints specifically, not an authentication or a tenant problem.** The prior pattern supports that reading: 48 of 50 chats on 2026-09-11, 47 then 35 of 50 on 2026-09-10, 40 of 50 then 0 of 50 on 2026-09-08. **The scan has been degrading for a week and this is the first run where it returned nothing at all.**

**Up and probed on 2026-09-14:** Microsoft 365 mail and calendar, including the `For Signature` folder by ID; Gmail on the a2zcp mailbox, 10 inbox threads and 2 sent, two pulled with `get_thread`; Plaud, 320 recordings scanned with nothing new since 2026-09-11 15:24 ET, which is an empty result rather than an outage; the artifact `db`, which returned 22 documents in `answers`, all of them already marked `applied`.

**Not probed and not claimed either way on 2026-09-14:** Rent Manager, the RentViewer warehouse, Google Drive. **Failed to connect:** `browser-use` (CONNECTION_CLOSED) and `desktop-commander` (CONNECT_TIMEOUT after 30s).

### Recovery, 2026-09-14 end of day close: Teams came back inside the same calendar day it failed hard

**The morning brief recorded Teams returning a Graph 429 with `chatsScanned: 0` on three separate attempts.** At 17:52 ET the same call with a date filter from 2026-09-12 returned the per chat scan path healthy: **48 of 50 chats listed, 2 failed, no rate limit stop**, 25 messages returned with more available. **So the outage lasted hours rather than days and was throttling rather than a permission or tenant fault**, which is what the morning brief inferred from mail and calendar being healthy on the same session. **Channel messages were not covered either way**, which is a property of the scan path and not of the outage.

**Why this is worth a section rather than a line.** The Teams scan has degraded for a week, 48 of 50 on 09-11, 47 then 35 on 09-10, 40 then 0 on 09-08, and 0 on the 09-14 morning brief. **A same day recovery to 48 breaks that trend line rather than continuing it**, so the right reading is intermittent throttling, not a connector dying by degrees. **Probe every run and do not carry yesterday's result forward.** This run's recovery produced `TD-0652`, the workers compensation policy visibility loss, which exists in no other channel.

**Probed and up on 2026-09-14 at the close:** Microsoft 365 mail, calendar and Teams, including `For Signature` by folder ID; Gmail on the a2zcp mailbox, 17 inbox threads, 3 sent, five pulled with `get_thread`, and the full label set; the artifact `db`, 15 documents in `answers` and all of them already marked `applied`. **Reachable and static:** Plaud, 320 recordings scanned, newest still 2026-09-11 15:24 ET across a five meeting day, which is an empty result rather than an outage.

**One Gmail behaviour worth recording because it shaped a question on tonight's close.** **Replies Austin sends from `austin@thebedrockgrp.com` do not appear under `in:sent` in this mailbox.** Four LP replies over the 09-12 to 09-13 weekend were visible only because each recipient wrote back, and they surfaced inside the inbound thread rather than in the Sent folder. **So `in:sent` is not a complete record of what he sent from the Bedrock addresses**, and an LP served without a reply is indistinguishable from one never served. Confirmed this run against the Buckwalter, Brown, Scruggs and Koretsky threads. `TD-0633` is the live case.

**Not probed and not claimed either way on 2026-09-14:** Rent Manager, the RentViewer warehouse, Google Drive, Dropbox, ClickUp and Ramp. **Failed to connect:** `browser-use` (CONNECTION_CLOSED).

## Correction, 2026-09-22: the a2zcp mailbox has been unreadable for fifteen routines, and the cause is on this side of the wire

**Added by the Page Update from the daily closes 2026-09-16 to 09-21 and the Weekend Pulse of 2026-09-20.** `KP-0116` on `00-Meta/open-items.md` is the register row; this page carries the connector fact.

- **Every close from 2026-09-16 to 2026-09-21 read one mailbox of two.** Parakeet Outlook was read to exhaustion each night, Inbox, Sent Items and `For Signature` by folder ID. **The a2zcp and Bedrock mailbox, `austin@a2zcp.com` carrying the Bedrock addresses, was not readable on any of them**, the tenth routine on 09-16 and the fifteenth on 09-21. Nine register rows cite that mailbox as their only source and none could be checked; `PD-53`, Ridaa Murad, parks partly on it.
- **The diagnosis moved twice and both readings are kept.** 2026-09-16 and 09-17: `ListConnectors` returned Gmail as connected and authenticated with `enabledInChat: false`, the same for Plaud and Google Drive, so a toggle in the chat's connector settings rather than an outage. 2026-09-20 and 09-21: the Gmail read tools were **absent from the session entirely**; on 09-21 one Gmail tool existed and it was `delete_draft`. Either way the fix is in this chat's connector settings, not at Google.
- **Plaud came and went.** Reachable on 2026-09-19 and genuinely empty, 321 files scanned with the scan complete and the newest recording dated 2026-09-15, which is an absence rather than the known upload lag; **absent from the session on 2026-09-21**, so that day has no spoken record.
- **Confirmed live on 2026-09-20 by the Weekend Pulse, by direct probe:** Rent Manager, the RentViewer warehouse and Google Drive all answered, the first live confirmation of the warehouse since `KP-0104` and of Drive since 2026-09-03.
- **The clock.** `KP-0115`, a `date` call returning a wrong wall clock, fired on 2026-09-16 (overwriting that day's close file, restored from the published page) and on 2026-09-19 (caught before anything was written, because the reading fell below the newest audit row). The two clock rule is now in `95-Agents/morning-brief.md` and `90-Skills/end-of-day.md`; the clock opened clean on 09-17, 09-18, 09-20 and 09-21.
- **The status line at the top of this page still says nothing has been re-verified since 2026-08-26.** That has been untrue since 2026-09-03 and this page has carried dated probe sections ever since; the line is left as written so the page's own history stays readable, and this note is the correction.
