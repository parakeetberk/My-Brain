# Vault reconciliation, part 1: the old `04-index/` and `06-reference/portfolio-reporting-rules.md`

**What this is:** a file by file disposition for ten pages from the retiring Claude Code vault at `C:\Users\AustinBerk\Documents\Claude\Code\brain\`, judged against this Brain at `C:\Users\AustinBerk\Documents\My Brain\`. Analysis only. Nothing was moved, edited or deleted.

**Status:** current, 2026-09-03. Governed by [[CLAUDE]] rules 3, 10, 12 and 15.

**Method:** every pair was compared by direct byte level diff of the two files, not by reading a summary of either. Confidence labels below are this pass's own, per rule 10.

## Summary table

| OLD file | Size | Disposition | Why, in one line |
|---|---|---|---|
| `04-index/connector-status.md` | 6.9 KB | **SUPERSEDED** | `10-Business/connector-status.md` is a strict superset at 19.3 KB with four re-tests OLD never saw, the last on 2026-09-03. |
| `04-index/sharepoint-main.md` | 41.6 KB | **SUPERSEDED** | Byte identical to `10-Business/storage-inventory/sharepoint-main.md` except NEW adds an 8 line header block. |
| `04-index/sharepoint-satellites.md` | 48.4 KB | **SUPERSEDED** | Byte identical to `10-Business/storage-inventory/sharepoint-satellites.md` except NEW adds an 8 line header block. |
| `04-index/onedrive-austin.md` | 55.6 KB | **SUPERSEDED** | Byte identical to `10-Business/storage-inventory/onedrive-austin.md` except NEW adds a 6 line header block. |
| `04-index/dropbox-a2z.md` | 24.3 KB | **SUPERSEDED** | Byte identical to `10-Business/storage-inventory/dropbox-a2z.md` except NEW adds a 6 line header block. |
| `04-index/gdrive-personal.md` | 17.4 KB | **SUPERSEDED** | Identical to `10-Business/storage-inventory/gdrive-personal.md` except NEW adds a header block and the fourth Shared Drive root found 2026-09-03. |
| `04-index/parakeet-birdcage-corporate.md` | 22.1 KB | **SUPERSEDED** | Byte identical to `10-Business/storage-inventory/birdcage-corporate.md` except NEW adds an 8 line header block. Renamed on the way in. |
| `04-index/folder-structure-tracker.md` | 23.9 KB | **SUPERSEDED** | Byte identical to `10-Business/storage-inventory/folder-structure-tracker.md` except NEW adds a 6 line header block. |
| `04-index/portfolio-baseline.md` | 58.1 KB | **SUPERSEDED** | Byte identical to `60-Communities/portfolio-baseline-warehouse.md` except NEW adds a 6 line header block. Renamed on the way in. |
| `06-reference/portfolio-reporting-rules.md` | 6.6 KB | **SUPERSEDED** | Byte identical to `80-Finance/portfolio-reporting-rules.md` except NEW adds a 6 line header block. |

**Ten files, ten SUPERSEDED, and that is the headline.** Every file in scope was already migrated into this Brain in the 2026-08-31 filing pass, and in every single case the NEW copy is the OLD copy plus a rule 10 header block. **There is nothing to MIGRATE and nothing to DISCARD outright.** Two conflicts were found, and neither of them is between OLD and NEW: one is inside NEW, and the other is a figure in the brief for this task that does not appear in either vault.

---

## The seven storage inventories: SUPERSEDED, and the evidence is a clean diff

**VERIFIED.** All seven files were diffed directly. Six of the seven differ from their NEW counterpart by nothing but an inserted header block; the seventh, `gdrive-personal.md`, differs by that header plus one added table row.

| OLD | NEW | Diff |
|---|---|---|
| `Claude\Code\brain\04-index\sharepoint-main.md` | `My Brain\10-Business\storage-inventory\sharepoint-main.md` | 8 lines added at line 3, nothing changed, nothing removed |
| `Claude\Code\brain\04-index\sharepoint-satellites.md` | `My Brain\10-Business\storage-inventory\sharepoint-satellites.md` | 8 lines added at line 3 |
| `Claude\Code\brain\04-index\onedrive-austin.md` | `My Brain\10-Business\storage-inventory\onedrive-austin.md` | 6 lines added at line 3 |
| `Claude\Code\brain\04-index\dropbox-a2z.md` | `My Brain\10-Business\storage-inventory\dropbox-a2z.md` | 6 lines added at line 3 |
| `Claude\Code\brain\04-index\gdrive-personal.md` | `My Brain\10-Business\storage-inventory\gdrive-personal.md` | 6 lines added at line 3, plus one row at line 51 |
| `Claude\Code\brain\04-index\parakeet-birdcage-corporate.md` | `My Brain\10-Business\storage-inventory\birdcage-corporate.md` | 8 lines added at line 3, file renamed |
| `Claude\Code\brain\04-index\folder-structure-tracker.md` | `My Brain\10-Business\storage-inventory\folder-structure-tracker.md` | 6 lines added at line 3 |

**What the added header carries, and why it makes NEW better rather than merely different.** Each NEW page opens with three things OLD has none of: a `What this is` line, a `Status` line dating the content to 2026-08-26 and saying it has not been re-verified since, and a note that the confidence labels on the page are the source's own. That is rule 10 applied to an inherited page. **A reader of OLD cannot tell that the survey is a week stale; a reader of NEW cannot miss it.**

**The three SharePoint pages also carry a source-state caveat NEW added and OLD lacks**, saying the numbered `1.` through `8.` community subfolders describe the read-only `/sites/main/` estate as it exists today and are deliberately left unrenumbered. That is the read-only ruling in [[CLAUDE]] being defended at the page level.

**`gdrive-personal.md` is the one with a substantive addition, and it is a find rather than an edit.** NEW carries a fourth Shared Drive root that the 2026-08-26 survey missed. Quoted from `My Brain\10-Business\storage-inventory\gdrive-personal.md`, line 51:

> `0AJ8dOob9gR0HUk9PVA` | A2Z and Bedrock entity layer, one folder per vehicle: `Parakeet Companies`, `Mobile Management` (A2ZMHC), `A2Z Community Partners`, `Bedrock MHC Fund II`, `BEDROCK I GROUP`, `A2Z MH Fund I`, `MoMa Lending`, `NewCo` | 8 folders. FOUND 2026-09-03, not in this survey. Three was a floor and it held. VERIFIED by direct listing

OLD's table stops at three roots. **Nothing in OLD is absent from NEW on any of the seven.** No conflict on any number in any of the seven files: every figure in OLD appears unchanged in NEW.

**Recommendation:** discard all seven OLD copies. `10-Business/storage-inventory/` also holds `known-problems.md` and `gdrive-shared-drives-manifest.md`, neither of which exists in OLD, so the NEW folder is the larger set in file count as well as in content.

**One flag for whoever retires the old vault.** These pages are full of em dashes, inherited from the 2026-08-26 survey, and NEW inherited them too. That is a pre-existing condition in NEW rather than something a migration would introduce, so it is not a reason to hold OLD back. It is worth a separate cleanup pass on `10-Business/storage-inventory/` if the voice rule is to be true of the whole vault. SINGLE-SOURCE, from reading the files.

---

## `04-index/connector-status.md`: SUPERSEDED

**NEW file:** `My Brain\10-Business\connector-status.md`, 198 lines, 19,344 bytes.
**OLD file:** `Claude\Code\brain\04-index\connector-status.md`, 88 lines, 6,943 bytes.

**VERIFIED by direct diff. NEW is more current, and by a wide margin.** OLD is a strict subset with two exceptions, both of which are NEW correcting OLD rather than the reverse.

**NEW contains, and OLD does not:**

- The 2026-08-31 evening re-test of the Rent Manager reporting API, including that `GeneralLedger`, report 51, still returns HTTP 500 and is the blocker for per-project capex analysis.
- The whole 2026-09-03 Google correction: Gmail moved to the a2zcp mailbox, Microsoft 365 returns `ErrorInvalidUser` with Graph 404 against that mailbox and must not be retried, and Gmail and Google Drive are separate connectors with separate authentication.
- The finding that the personal Drive was not empty, with four Bedrock Fund II locations named by folder ID and labelled VERIFIED.
- The fourth Shared Drive root, and the Dropbox `who_am_i` result placing that connector on `austin@a2zcp.com`, team A2Z MHC, root namespace `11855305057`.
- The final switch of the Drive connector to `austin@a2zcp.com`, which closes the split the page spent a day documenting.
- Eight register IDs OLD has none of: `KP-0008`, `KP-0066`, `KP-0068`, `TD-0008`, `TD-0497`, `TD-0498`, `TD-0507`, `PD-40`.

**The two places OLD and NEW differ rather than NEW simply adding.** Neither is a conflict.

1. **The Google Drive identity row.** OLD, `Claude\Code\brain\04-index\connector-status.md` line 14: `| **Google Drive** | austinrberk@gmail.com | Personal Drive plus three corporate Shared Drives |`. NEW records the same starting state, the 2026-09-03 re-test confirming it had not moved, and then the switch to `austin@a2zcp.com` later the same day. **This is a fact that changed, not two sources disagreeing.** OLD was correct on 2026-08-26 and is now stale.
2. **A path reference that was rewritten on the way in.** OLD line 76 points at `03-domains/intercompany-arap-recon-plan.md`; NEW line 85 points at `80-Finance/intercompany-arap-recon.md`. Same claim, corrected link. **This is direct evidence that a deliberate migration pass already ran over this file**, rather than the two pages having been written independently.

**Which is more current: NEW, unambiguously.** OLD's content is frozen at 2026-08-26. NEW carries four dated re-tests after that, the most recent on 2026-09-03, each one saying what call was made and what came back.

**Recommendation:** discard OLD. Nothing in it is missing from NEW.

---

## `04-index/portfolio-baseline.md`: SUPERSEDED, and the unit-count conflict is not in this file

**NEW file:** `My Brain\60-Communities\portfolio-baseline-warehouse.md`, 58,558 bytes.
**OLD file:** `Claude\Code\brain\04-index\portfolio-baseline.md`, 58,050 bytes.

**VERIFIED by direct diff: the two files are byte identical except for a 6 line header block inserted at line 3 of NEW.** Same 12 sections, same tables, same figures, same confidence labels. It was renamed on the way in, from `portfolio-baseline` to `portfolio-baseline-warehouse`, and the rename is an improvement because the page is one system's read rather than the portfolio's baseline.

### Ruling 1 is applied, and one part of its premise does not hold

**The ruling stands and I am not reopening it.** `My Brain\CLAUDE.md` line 13 states **67 active communities, 6,379 core units** and that is authoritative. The warehouse figures survive as a dated snapshot with their as-of and their method, labelled SINGLE-SOURCE, never as a headline and never as the unit count in `00-Meta\numbers-ledger.md`.

**But the figure the ruling names is not in the file it names, and rule 15 says to check the vault before asserting a fact about it, so the same check is owed in the other direction.**

`00-Meta\vault-reconciliation\00-rulings.md`, ruling 1, states:

> **Conflict.** `Claude\Code\brain\04-index\portfolio-baseline.md` reports **6,635 units across 66 records**.

**VERIFIED, and stated plainly: neither figure appears in that file, or anywhere in the old vault.**

- `grep -rn "6635\|6,635\|6 635"` across the whole of `Claude\Code\brain\` returns **exactly one hit**, and it is a substring: `| Mar-26 | 78.25% | 7,336 | 46,635 |` at line 301 of `04-index/portfolio-baseline.md`. That table is headed `| Month | NOI margin | Utilities expense | Utility reimbursements |`. **The 6,635 is the tail of $46,635 of utility reimbursement revenue in March 2026.** It is a dollar figure, not a unit count.
- `grep -rni "66 records\|66 reporting\|across 66\|66 propert"` across the whole old vault returns **nothing**.

**What the file actually reports for units, quoted from `Claude\Code\brain\04-index\portfolio-baseline.md` section 1:**

> | Total units — **raw, as the warehouse returns it** | **9,355** | VERIFIED | `unitCount` |
> | Total units — **de-duplicated** (archived/shadow records removed) | **8,020** | VERIFIED (filtered query) | `unitCount` |

and its own instruction, same section: `**Use 8,020 / 77.67%.**`

**Its record counts, none of which is 66:** 82 Rent Manager property entities, 104 property records on the market-rent test, 134 property records on the budget test, 67 properties returning move activity, and 71 reporting records under Austin's inclusion rules. The largest per-property table, section 2 `By property`, carries **72 data rows summing to 7,181 units**, counted directly.

**Why this matters rather than being pedantry.** The ruling's disposition is right and its arithmetic reasoning is right in shape: the warehouse counts a different population, and utility entities and Congress are exactly two of the reasons. **But if `6,635 across 66 records` gets written into an archive note or a decision record as what the old vault said, this Brain acquires a sourced-looking number that no source ever produced**, which is the precise failure rule 3 exists to prevent. **The real gap is 6,379 against 8,020, it is 1,641 units wide, and it is already registered.**

### What the warehouse figure measured, and why it differs

Requested by the coordinator so the difference is documented rather than re-discovered. **All of this is already on file in NEW; none of it needs migrating.** Sources: `My Brain\60-Communities\portfolio-baseline-warehouse.md` and `My Brain\80-Finance\portfolio-reporting-rules.md`.

| | Property Data Sheet, the authoritative figure | RentViewer warehouse |
|---|---|---|
| Units | **6,379 core units** | 8,020 de-duplicated, 9,355 raw |
| Communities or records | **67 active communities** | 71 reporting records, or 82 to 134 raw records depending on the model |
| As of | December 2025 occupancy vintage, sheet as of 2026-08-30 | Snapshot 2026-08 for units, TTM to 2026-07-31 for financials |
| Grain | The community, one row each | The Rent Manager property record, which is not the community |
| Scope | Parakeet MHC ownership family | Every ownership family in the warehouse |

**The four reasons the two populations differ, each already VERIFIED in NEW:**

1. **The record is not the community.** `80-Finance\portfolio-reporting-rules.md` names the assets that span several records: Northgate as MH plus RV plus Utility, Bay Oaks Village I and II, Whispering Pines MA and MH FL, Shirleys I and II, Hunter Springs MHC and MHP. Its own words: `**Record count ≠ community count.**`
2. **Utility entities.** `Applegate Water`, `Vantage Oaks Utility` and `Northgate Utility` are separate records that roll into their community and carry units of their own. Rule 2 of the reporting-rules page says keep them but never report them standalone.
3. **Renames and shadow duplicates were never retired.** `00-Meta\audit-log.md` line 205 quantifies it: **690 units of archived `x`-prefix renames, roughly 645 of shadow duplicates, 246 of utility and sub-meter records.**
4. **The error runs both ways, and this is the half that is easy to miss.** Same audit-log row: **Cedar Grove, Colonial, Lambeth and Cambridge are 466 units of occupied, paying community that exist in the warehouse and not on the Property Data Sheet**, and **Nalls Court is 19 lots on the Data Sheet with no warehouse record at all.** `00-Meta\analysis\2026-09-02-entity-map-found.md` line 56 adds the reason the four are absent rather than missing: they sit in a different ownership family and the Data Sheet is a Parakeet MHC document. **The sheet is scoped, not incomplete.**

**So 6,379 and 8,020 are not a right answer and a wrong one. They are two populations, and the bridge between them closes to within 547 units in the workbook already on file** at `00-Meta\analysis\2026-09-01-unit-count-reconciliation.xlsx`. VERIFIED, from the audit-log row that records building it.

### Do `numbers-ledger.md` and `portfolio.md` agree with 6,379, and with each other

**Yes to both, and the whole vault is consistent on this. VERIFIED by reading each file.**

| File | What it says | Agrees with 6,379 |
|---|---|---|
| `My Brain\CLAUDE.md` line 13 | 67 active communities, 6,379 core units | yes, it is the source of the ruling |
| `My Brain\00-Meta\numbers-ledger.md` line 41 to 46 | `Active communities 67`, `Core units, active portfolio 6,379`, Dec 2025 vintage, source `Property Data Sheet, PDS Clean`, with MH lots 5,293, RV sites 950, other units 136 | yes |
| `My Brain\60-Communities\portfolio.md` line 3 and line 160 | `6,379 lots across 7 states`, and `6,379 Total Core Units across the 67 active communities: 5,293 MH lots, 950 RV lots and 136 other units` | yes |
| `My Brain\10-Business\business-model.md` line 19 | 67 active communities, 6,379 core units total | yes |
| `My Brain\50-Products-Sales\the-community.md` line 10 | 6,379 total core units across 67 active communities | yes |
| `My Brain\10-Business\departments\property-operations.md` line 27 | 67 active communities, 6,379 total core units | yes |

**Three independent checks that the figure is internally sound:**

- **The components add up.** 5,293 MH lots plus 950 RV sites plus 136 other units equals 6,379 exactly. Arithmetic on the ledger's own rows, so INFERRED from VERIFIED inputs rather than taken on trust.
- **The row count matches.** `60-Communities\portfolio.md` carries **exactly 67 data rows** in its community table, counted directly. The table and the aggregate describe the same set.
- **The ledger already carries the warehouse figure the way the ruling requires.** `numbers-ledger.md` has a separate `Portfolio actuals — RentViewer warehouse` section holding 9,355 raw and 8,020 de-duplicated as their own rows with `Snapshot 2026-08` as-of dates and the model named, under a heading that says `**They do not reconcile with the Property Data Sheet figures above — see conflicts C1 to C4 in [[00-Meta/open-items]].**` **The unit count row at line 42 is the Data Sheet's 6,379. The warehouse numbers are nowhere near it and are not labelled as the unit count.** Ruling 1's requirement is already satisfied and needs no edit.

### The conflict is already registered, with IDs, so nothing new is needed

**VERIFIED. Four register rows and two analysis artefacts already carry it**, which means a migration that filed this again would be duplicating live work:

- `KP-0010` in `00-Meta\open-items.md`: 6,379 against 8,020, with Austin's 2026-09-01 theory quoted and the reconciliation workbook named. Ranked High, awaiting his read.
- `KP-0025 C1` in the same file: the two figures side by side with their vintages and the note that they are 1,641 apart.
- `KP-0026 C2`: what counts as a reporting property, naming Shell Pointe, Geiger Key and Congress as in one place and out of the other.
- `TD-0004` and `TD-0003` in `10-Business\eos\to-dos.md`: reconcile the count, and rule once on what counts as an operating property. Both unassigned with Zach Schwartz proposed on the first and Austin owning the second.
- `00-Meta\analysis\2026-09-01-unit-count-reconciliation.xlsx` and `00-Meta\analysis\2026-09-02-entity-map-found.md`.

**Recommendation: discard OLD.** Nothing in it is absent from `60-Communities\portfolio-baseline-warehouse.md`, and the conflict it was thought to create is registered under `KP-0010` with a workbook against it.

**One thing worth Austin's eye, and it is inside NEW rather than in OLD.** See the CONFLICT section at the end of this page.

---

## `06-reference/portfolio-reporting-rules.md`: SUPERSEDED

**NEW file:** `My Brain\80-Finance\portfolio-reporting-rules.md`, 122 lines, 7,140 bytes.
**OLD file:** `Claude\Code\brain\06-reference\portfolio-reporting-rules.md`, 6,610 bytes.

**Yes, these landed, and they landed in the right folder.** [[CLAUDE]] line 123 lists the page in the folder map by name: *Austin's own rules for what counts as an operating property. Do not re-derive, do not re-ask.* `00-Meta\index.md` line 123 carries its row.

**VERIFIED by direct diff: byte identical except for the 6 line header block at line 3 of NEW.** Every one of Austin's rules came across intact. Rule 0 never filter on `IsActive`, rule 1 what counts as an operating property with the exclusion table, rule 2 utilities roll up, rule 3 the five special-treatment properties, rule 4 the `x`-prefixed records are renames. Both his verbatim quotes and the counts survive.

**This is the most consequential page in scope, and it is the one where a migration failure would have cost the most.** It is the only place in either vault that records Austin's own inclusion rules in his words, and rules 3 and 15 of this Brain both point at it as the thing not to re-derive. **It is fully present in NEW.**

**All three of its `Still open` items were routed into NEW registers with IDs.** VERIFIED by reading each register:

| OLD `Still open` item | Where it landed in NEW |
|---|---|
| Hunter Springs MHC's $35,056 should be zero | `KP-0030 C6` in `00-Meta\open-items.md` and `TD-0005` in `10-Business\eos\to-dos.md`, owner **David Berman** |
| Congress split treatment needs enforcing in queries | `KP-0026 C2` and `TD-0003`, owner **Austin**, alongside Shell Pointe and Geiger Key |
| How many communities is the right count, given assets spanning multiple records | partially: `KP-0026` covers which properties are in scope. **The roll-up question itself has no row of its own** |

**One genuine small gap, and it is the only unrouted content found anywhere in this pass.** The second `Still open` item is two questions, not one, and only the first was routed. The unrouted half is the roll-up rule:

> **How many communities is the right count?** Several assets span multiple records: Northgate (MH + RV + Utility), Bay Oaks Village I & II, Whispering Pines MA & MH FL, Shirleys I & II, Hunter Springs MHC & MHP. **Record count ≠ community count.** One decision on how to roll these up would settle every "how many communities do we have" question permanently.

**This is a decision waiting on Austin, so its register is `00-Meta\parked-decisions.md` and its prefix is `PD`, per rule 15 and `00-Meta\id-conventions.md`.** It is not a `KP` finding, because the problem is understood and what is missing is a ruling. **It is not urgent, because the ruling already fixed the number Austin cares about at 67 and 6,379.** It is worth a row because the sentence *one decision would settle every "how many communities do we have" question permanently* is still true, and because the reporting-rules page is marked authoritative and this is the one thing on it that nobody can act on.

**Recommendation:** discard OLD. **Separately, and independent of the migration, open one `PD` row for the multi-record roll-up rule**, taking the next number in sequence per rule 15. That is a recommendation, not an action; nothing was written.

---

## CONFLICT: `00-Meta/index.md` attributes two figures to a page that does not contain them

**This is the one genuine conflict this pass found, and both sides of it are inside NEW.** It is not an OLD versus NEW disagreement and it does not affect any disposition above. It is reported because rule 10 says to verify against the primary artefact rather than an index, and this is an index that has drifted from its artefact.

**Side one.** `My Brain\00-Meta\index.md`, line 88:

> | [[60-Communities/portfolio-baseline-warehouse]] | **The portfolio as the warehouse actually reports it. $44.4M TTM revenue, 62.75% NOI margin.** |

**Side two.** `My Brain\60-Communities\portfolio-baseline-warehouse.md`, section 1, the page that row points at:

> | Total revenue (TTM) | **$54,813,442** | VERIFIED | `totalRevenue` |
> | **Portfolio NOI margin (TTM)** | **48.43%** | VERIFIED | `noiMargin` |

**VERIFIED: the strings `44.4`, `$44,412,071` and `62.75` do not appear anywhere in `60-Communities\portfolio-baseline-warehouse.md`.** Checked by grep. And `54,813,442` appears in exactly one file in the vault, that page.

**Which I believe, and why: both figures are correct, and the index has put them on the wrong page.** This does not need Austin's ruling.

- **$44,412,071 and 62.75% are the right headline** and they belong to `My Brain\80-Finance\portfolio-reporting-rules.md`, which computes them across 71 records under Austin's own inclusion rules, and to `My Brain\00-Meta\numbers-ledger.md`, which carries them in its `Portfolio actuals` section with sources and as-of dates.
- **$54,813,442 and 48.43% are the same warehouse unfiltered**, with the corporate entity and Geiger Key blended in. The reporting-rules page says so directly: `**Compare: 48.43% margin when corporate overhead and Geiger Key were blended in.** The portfolio was never underperforming. The arithmetic was.` The ledger carries the 48.43% as its own labelled row for exactly this reason.

**So the two numbers measure different populations of the same query, which is the identical shape as the unit-count question, and the ledger already handles it correctly.** The defect is only that the index credits the filtered result to the unfiltered page.

**Why it is worth fixing rather than shrugging at.** `00-Meta\index.md` line 3 says a session reads the index first, then the folder MOC, then only the files it needs. **A session that trusts line 88 and quotes $44.4M as coming from the warehouse baseline page has cited a page that says $54.8M**, and anyone who opens the page to check finds a number eleven million dollars different. That is the "18 reds pending" failure in rule 10 with a bigger number on it.

**Recommendation, and no edit was made:** change the index row to describe what the page holds, the unfiltered warehouse read at $54.8M and 48.43%, and point the $44.4M and 62.75% headline at `80-Finance\portfolio-reporting-rules.md` where it is derived. One row, one audit-log entry per rule 13.

---

## Ruling 4, the dash pass, as it applies to this scope

**No file in this scope is recommended for MIGRATE, so no dash pass is triggered by anything above.** All ten are SUPERSEDED and stay behind. The single recommendation that would produce new text, the `PD` row for the multi-record roll-up rule, would be written fresh in this Brain's voice rather than carried over, so the dash rule is satisfied by writing it rather than by cleaning it.

**But ruling 4 has already been missed once, and this scope is where the evidence sits.** SINGLE-SOURCE, from reading the files.

**All ten NEW counterparts contain em dashes, inherited verbatim from the 2026-08-26 source when they were filed on 2026-08-31.** The header blocks that were added on the way in are clean and use hyphens; **the bodies were not touched.** Examples, quoted exactly:

- `My Brain\80-Finance\portfolio-reporting-rules.md`: `**IN — 67 communities**, plus Triple S Marina, plus 3 utility entities.`
- `My Brain\60-Communities\portfolio-baseline-warehouse.md`: `Portfolio TTM margin is **48.43%** and OER is **51.57%** —`
- `My Brain\10-Business\connector-status.md`: `**Google Drive** | Personal Drive plus three corporate Shared Drives. **The Drive identity did NOT move when the mail identity did.**`

**So the dash rule is currently untrue of pages already sitting in `10-Business/`, `60-Communities/` and `80-Finance/`, and holding OLD back does not fix that.** The material is already in.

**Stated as a separate finding rather than folded into a disposition, because it is not a migration decision.** It is a cleanup pass over pages that are already filed, it is a rewrite rather than a find and replace per ruling 4, and on `80-Finance\portfolio-reporting-rules.md` in particular it needs care: **that page quotes Austin verbatim and is marked authoritative, so a rewrite has to leave his quoted words alone and reshape only the surrounding prose.** Worth its own scoped task rather than a line in a reconciliation report.

