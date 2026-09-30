# Vault reconciliation, part 3: entities, domains, decisions

**What this is:** the file by file disposition of 26 files from the retired Claude Code vault (`C:\Users\AustinBerk\Documents\Claude\Code\brain\`) against this Brain (`C:\Users\AustinBerk\Documents\My Brain\`). Scope is `02-entities/` (14 files), `03-domains/` (6 files), `05-decisions/` (5 files) and the old root `CLAUDE.md`.

**Status:** analysis only. Nothing was moved, edited or deleted. Written 2026-09-03.

**Governed by** `05-Inbox\vault-reconciliation\00-rulings.md`, Austin's five rulings of 2026-09-03. Rulings 2, 3 and 5 bear on this scope directly and are applied rather than re-opened.

**Confidence labels** are on every substantive claim, per rule 10. VERIFIED means both files were read end to end in this session. SINGLE-SOURCE means one file says it and nothing here contradicts it. INFERRED means it was reasoned from what was read.

**One note on quoted text.** This Brain forbids em dashes and en dashes. Every file in the old vault is full of them. Where a quote below carries one it is the source's character, kept so the quote stays exact. None of this report's own prose uses them, and no file in the old vault can migrate without the rewrite ruling 4 requires.

---

## The headline finding

**The 2026-08-31 fold already happened, and it was more complete than the brief assumed. VERIFIED.**

Twelve of the 26 files in this scope are already inside this Brain, byte for byte apart from mechanical path and wikilink rewrites. Ten sit in `99-Archive\2026-08-catchup\entity-pages\`, one in `10-Business\people\road-trip-roster-2026-08.md`, one in `10-Business\vendors\vendor-status-2026-08.md`. The old root `CLAUDE.md` is also already archived, at `99-Archive\2026-08-catchup\superseded-brain-CLAUDE.md`, though the copy there is four rules behind the live old file.

**So the reconciliation question is not "what should move" for most of this scope. It is "what got dropped on the way in."** Three things did, and they are set out under CONFLICT and MIGRATE below.

---

## Summary table

| OLD file | Size | Disposition | Reason |
|---|---|---|---|
| **`02-entities/`** | | | |
| `berk-inc.md` | 4.8KB | ALREADY THERE | `10-Business\entity-structure\berk-inc-umbrella.md` carries it whole plus Austin's 2026-08-31 verification of A2Z. |
| `communities.md` | 6.3KB | ALREADY THERE | `99-Archive\2026-08-catchup\entity-pages\communities.md`, identical but for path rewrites. |
| `applegate.md` | 1.4KB | ALREADY THERE | Archived copy plus a live four-block page at `60-Communities\applegate-mhc.md`. |
| `belle-haven.md` | 1.9KB | ALREADY THERE | Archived copy plus `60-Communities\belle-haven.md`. |
| `belmart.md` | 1.5KB | ALREADY THERE | Archived copy plus a live page at `85-Personal\belmart.md`. |
| `great-oaks.md` | 1.2KB | ALREADY THERE | Archived copy plus `60-Communities\great-oak-rv-resort.md`. |
| `lucky-clover.md` | 2.0KB | ALREADY THERE | Archived copy plus `60-Communities\lucky-clover.md`. |
| `regency.md` | 2.6KB | ALREADY THERE | Archived copy plus `60-Communities\regency-i-and-ii.md`. |
| `river-oaks.md` | 2.7KB | ALREADY THERE | Archived copy plus `60-Communities\river-oaks-rv-resort.md`. |
| `riverwalk.md` | 1.5KB | ALREADY THERE | Archived copy plus `60-Communities\riverwalk.md`. |
| `vantage-oaks.md` | 2.1KB | ALREADY THERE | Archived copy plus `60-Communities\vantage-oaks.md`. |
| `people-roster.md` | 8.5KB | CONFLICT | Body is at `10-Business\people\road-trip-roster-2026-08.md`, but its External counsel table was dropped in the fold. |
| `vendors-platforms.md` | 5.6KB | ALREADY THERE | `10-Business\vendors\vendor-status-2026-08.md`, identical but for path rewrites. |
| `karen-doner.md` | 5.4KB | MIGRATE | Per ruling 5 she is outside counsel. No page exists in `10-Business\outside-help\`. |
| **`03-domains/`** | | | |
| `supply-chain.md` | 6.9KB | ALREADY THERE | `70-Operations\supply-chain-model.md`, a superset. Its 37-day figure is not in the ledger. |
| `delivery-bottleneck-2026-09.md` | 17KB | ALREADY THERE | `70-Operations\delivery-bottleneck.md`, identical body, headers added. |
| `license-permit-transition-plan.md` | 14KB | ALREADY THERE | `70-Operations\license-and-permit-ownership.md`, identical body. |
| `intercompany-arap-recon-plan.md` | 25KB | ALREADY THERE | `80-Finance\intercompany-arap-recon.md`, plus the 2026-08-31 sequencing ruling. |
| `sales-org.md` | 2.5KB | ALREADY THERE | `50-Products-Sales\sales-org-buildout.md`, a superset. |
| `systems-data-architecture.md` | 3.9KB | ALREADY THERE | `10-Business\systems-architecture.md` is the same page renamed, plus a 2026-08-31 VERIFIED block. |
| **`05-decisions/`** | | | |
| `2026-08-26-storage-target-state.md` | 2.7KB | ALREADY THERE | `00-Meta\decisions\` plus spine line 42 of `decisions-log.md`. |
| `2026-08-26-dr035-no-action.md` | 1.9KB | ALREADY THERE | `00-Meta\decisions\` plus spine line 43. The 52-divergence caveat survived. |
| `2026-08-26-company-assessment-plan.md` | 15KB | ALREADY THERE | `00-Meta\decisions\` plus spine line 45. Two output paths were rewritten into nonsense. |
| `2026-08-29-brief-delivery-artifact-only.md` | 3.3KB | ALREADY THERE | `00-Meta\decisions\` plus spine line 46. |
| `parked-decisions-register.md` | 7.8KB | ALREADY THERE | `00-Meta\parked-decisions.md`. All 19 rows map one to one onto `PD-01` to `PD-19`, same numbers. |
| **root** | | | |
| `CLAUDE.md` | 12.6KB | SUPERSEDED | `My Brain\CLAUDE.md`, per ruling 2. The archived copy is four rules behind the live old file. |

---

## Section 1: `02-entities/`, 14 files

### 1.1 `berk-inc.md`, 4.8KB. ALREADY THERE.

**NEW path:** `C:\Users\AustinBerk\Documents\My Brain\10-Business\entity-structure\berk-inc-umbrella.md`

**VERIFIED by direct diff.** Exactly one line of the old file does not appear verbatim in the new one, and that is because the new page expanded it in place rather than dropping it. The old line reads:

> `- **A2Z Community Partners** — the Maryland hold-co, top of the structure`

The new page keeps that text and appends Austin's own confirmation of 2026-08-31, *"a2zcp.com is my entity that ran everything prior to parakeet. both bedrock and a2zfund i. a2z is my holding company"*, then the eleven live utility logins that run through `accounting@a2zcp.com` and `winnie@a2zcp.com`. **The new page is a strict superset. Nothing in the old file is lost.**

**Relationship to `entity-map.md`.** `10-Business\entity-structure\entity-map.md` is not a version of this file. It is a different document built from a different source: 430 filed entity documents, organised in five tiers, dated 2026-08-30. **The two do not conflict; they answer different questions.** The umbrella page asks how the three identity domains relate and says the answer is unknown. The entity map says what paperwork exists. **INFERRED, and worth saying out loud: the old file's Next action is stale.** It asks someone to read `Org Chart Overview.xlsx` (2020, Dropbox) against `Org Chart Overview_122023.xlsx` (2023, OneDrive) to produce a governed structure. `00-Meta\analysis\2026-09-02-entity-map-found.md` exists and `00-Meta\index.md` records the entity map as *"Superseded in part by the master org chart found 2026-09-02."* **That next action may already be done or partly done. Do not re-run it without reading that analysis file first.**

**No action.** The old file can retire.

### 1.2 `communities.md` and the nine community pages. ALREADY THERE, all ten.

**NEW paths:** `C:\Users\AustinBerk\Documents\My Brain\99-Archive\2026-08-catchup\entity-pages\` holds `communities.md`, `applegate.md`, `belle-haven.md`, `belmart.md`, `great-oaks.md`, `lucky-clover.md`, `regency.md`, `river-oaks.md`, `riverwalk.md`, `vantage-oaks.md`.

**VERIFIED by direct diff on all ten.** Every difference is a mechanical path or wikilink rewrite done during the fold. Representative examples from `applegate.md`:

| OLD text | NEW text |
|---|---|
| `` `03-domains/supply-chain.md` `` | `` `70-Operations/supply-chain-model.md` `` |
| `[[communities]]` | `[[60-Communities/portfolio]]` |
| `` `02-entities/vendors-platforms.md` `` | `` `10-Business/vendors/vendor-status-2026-08.md` `` |

**No substantive text was changed, added or removed in any of the ten. VERIFIED.**

#### Does the old page hold anything the new hot sheet does not?

Each old page now has a live counterpart in `60-Communities\` carrying the mandated four blocks. The mapping, and it is not one for one on names:

| OLD page | NEW live page | Old-only content? |
|---|---|---|
| `applegate.md` | `60-Communities\applegate-mhc.md` | No. "about to fall over" and the cribbing item are on the live page, in `60-Communities\open-items.md` and in `10-Business\eos\to-dos.md`. |
| `belle-haven.md` | `60-Communities\belle-haven.md` | No. "block and blast" is on the live page and in the tour transcript. |
| `belmart.md` | `85-Personal\belmart.md` | No. |
| `great-oaks.md` | `60-Communities\great-oak-rv-resort.md` | No. Boil water and the aerator are on the live page. |
| `lucky-clover.md` | `60-Communities\lucky-clover.md` | No. The armed-resident item is on the live page and in four registers. |
| `regency.md` | `60-Communities\regency-i-and-ii.md` | No. Savannah, the sinkholes, Larry and Green Oak are all on the live page. |
| `river-oaks.md` | `60-Communities\river-oaks-rv-resort.md` | **Yes, two items. See CONFLICT 1 and CONFLICT 2.** |
| `riverwalk.md` | `60-Communities\riverwalk.md` | No. |
| `vantage-oaks.md` | `60-Communities\vantage-oaks.md` | No. The 72 hour permit window and the paving rebid are carried. |

**The old name to new name drift is worth recording on its own. VERIFIED.** Four of nine changed name in the fold: `applegate` to `applegate-mhc`, `great-oaks` to `great-oak-rv-resort` (singular, and RV rather than MH), `regency` to `regency-i-and-ii`, `river-oaks` to `river-oaks-rv-resort`. **This is exactly the community naming drift `10-Business\storage-inventory\known-problems.md` documents in the file estate, appearing inside the vault itself.** Anyone searching the new vault for "great oaks" or "applegate" by the old slug finds nothing.

#### CONFLICT 1: River Oaks occupancy. Two numbers, and the new vault has already tested the old one.

**OLD**, `C:\Users\AustinBerk\Documents\Claude\Code\brain\02-entities\river-oaks.md`:

> "River Oaks is running at **roughly 60% actual occupancy despite looking full**."

**NEW**, `C:\Users\AustinBerk\Documents\My Brain\60-Communities\river-oaks-rv-resort.md`, Snapshot block:

> "**Occupancy** | **Unknown** — sheet shows 0%, confirmed a data gap"

and in the same page's facts: "December-2025 occupancy is **not reliably captured** for this property. The Property Data Sheet shows 0%, which the owner confirmed on 2026-08-30 is a data gap and not an actual figure."

**But this one is already adjudicated, and the adjudication is the useful part. VERIFIED.** `C:\Users\AustinBerk\Documents\My Brain\60-Communities\portfolio-baseline-warehouse.md` line 883 tests the old claim by name:

> "| River Oaks ~60% actual occupancy despite looking full | **Partly holds** | Blended **38.94%**; core Lot-RV stock **65.0%**. 32 of 113 units are unusable/POH/demo and sit at 0% in the denominator. The "looks full but isn't" instinct is correct; the asset has **negative TTM NOI**. |"

**So there are three figures on this property, not two: 60% road-trip estimate, 38.94% blended warehouse, 65.0% core stock, against an "unknown" on the hot sheet.** The hot sheet says unknown while a page two doors down carries two computed numbers with a method. **That is the conflict that actually matters, and it is internal to this Brain rather than between the vaults.** Recommend the hot sheet Snapshot cite the warehouse figures with their as-of and method rather than reading "Unknown", and that `00-Meta\numbers-ledger.md` carry them. **Do not use the 60% figure as a number; it is a road-trip impression and the warehouse has superseded it.**

#### CONFLICT 2: River Oaks new home price. Present in OLD, absent from every live page in NEW.

**OLD**, `02-entities\river-oaks.md`:

> "**HOLD on new homes until sales move.** Price at $49,900. 15% RV-resident discount, terms TBD."

**NEW.** The string `49,900` appears **nowhere** in this Brain outside the archived copy of that same old file. VERIFIED by full-vault grep. What did survive is the surrounding decision, stripped of the number. `60-Communities\river-oaks-rv-resort.md` Pulse block:

> "| **9d** | - | sales | open | Whether to pause new home deliveries until current inventory sells was disputed on the recording and left open. | Zach Schwartz |"
> "| **9d** | - | sales | open | The terms of a proposed 15 percent discount for current RV residents were never defined. | Leslie Croft |"

**So the two open items are tracked and the price point is not.** INFERRED as to cause: `$49,900` is a money figure, and rule "Money figures live in the ledger only" would have kept it off the community page, but it is not in `00-Meta\numbers-ledger.md` either. **This is a genuine loss of one fact in the fold.** It is SINGLE-SOURCE (one road-trip document) and should not be asserted as the current list price, but it is the only price point anywhere for River Oaks new homes and the pause decision is meaningless without it.

**Recommend:** one line in `00-Meta\numbers-ledger.md`, labelled SINGLE-SOURCE, as-of 2026-08-25, sourced to `Parakeet Week in Review.docx`, and referenced from the two open Pulse rows. **Not asserted as current.**

### 1.3 `people-roster.md`, 8.5KB. CONFLICT.

**NEW path:** `C:\Users\AustinBerk\Documents\My Brain\10-Business\people\road-trip-roster-2026-08.md`

**The body migrated intact. VERIFIED by diff.** The Field and Corporate tables are identical apart from path rewrites, and the new page added a Status header, a confidence-label header and a What this is line. The diarization caveat survived verbatim, including the four names it says to double check, Ozzie, Berman, Ashlyn and accounting personnel.

**Rule 7 compliance: the new page is clean. VERIFIED.** The candid material about David Berman, and about a second person in the same function, sits in `10-Business\people\_private-assessments.md` and `10-Business\people\_private-2026-08-31-controller-performance-and-transition.md`, not on the roster. `00-Meta\audit-log.md` line 150 records that separation being made deliberately, and `_private-assessments.md` line 68 states *"No compensation figures are recorded here or anywhere in this Brain"*, per guardrail 9. **The old roster page itself carries no compensation and no candid assessment, so it would not have violated rule 7 on migration.**

#### The conflict: the External counsel table was dropped in the fold.

**OLD**, `02-entities\people-roster.md`, a five row section titled `## External counsel`. **NEW**, `10-Business\people\road-trip-roster-2026-08.md`, **has no such section. VERIFIED by diff and by grep for "External counsel" in that file, which returns nothing.**

The five rows, and where each one landed:

| OLD row | Is the fact in this Brain? | Where |
|---|---|---|
| **Karen Doner**, Doner Law PLC, employment counsel | Yes, but not on a counsel page | `00-Meta\commitments.md` CM-16, `10-Business\people\_private-assessments.md`, `10-Business\hr\employee-handbook.md` |
| **Zach Wallack**, G. Dym, Eckert Seamans, WPMH / Mark Raymond litigation | Yes, and better | `60-Communities\american.md` line 69 and `00-Meta\commitments.md` line 202 both name **"Zachary M. Wallack with Gabriel Dym, Eckert Seamans"** |
| **C. Spake**, E.R. Portilla, Gunster, Belle Haven and Silver Breeze | **Firm yes, attorneys no** | Gunster is on `60-Communities\belle-haven.md`. "Portilla" appears **nowhere** in this Brain; "Spake" only in two archived email digests. VERIFIED. |
| **Chris Hoke**, Woods Oviatt, Hunter Springs / Hunter Extension | **Firm and person yes, this matter no** | Hoke is on `10-Business\outside-help\counsel.md` as deal counsel. The **Hunter Springs / Hunter Extension** attribution survives only in `99-Archive\2026-08-catchup\` files and a passing line in `00-Meta\daily-close\2026-08-30.md`. VERIFIED. |
| **Lowenstein**, MIP legal work | Yes | `10-Business\outside-help\counsel.md`, as Lowenstein Sandler LLP |

**What this actually costs, and it is more than five rows. VERIFIED.** `C:\Users\AustinBerk\Documents\My Brain\10-Business\outside-help\counsel.md` is the page that owns the counsel roster. It lists five relationships: Woods Oviatt Gilman, Lowenstein Sandler, Vector Law, Closing USA and Zach Wallack. **It does not list Karen Doner at all**, and on Wallack it says:

> "**Zach Wallack — litigation, Massachusetts.** ... **Firm not recorded.**"

**The firm is recorded, twice, on two other pages in the same vault.** `60-Communities\american.md` and `00-Meta\commitments.md` both say Eckert Seamans. **This is a rule 15 failure of exactly the shape rule 15 was written for: a page asserting a gap while the fact sits on another page.** The old roster's table would have caught it, and so would reading the Brain against itself.

**Disposition detail.** The old file is CONFLICT rather than MIGRATE because its body is already filed and only one section is missing. **The fix is not to migrate the old file. It is to complete `10-Business\outside-help\counsel.md`** from what this Brain already knows, plus the two facts only the old table holds: the Gunster attorney names, and Hoke on Hunter Springs / Hunter Extension. Both are SINGLE-SOURCE and both need the dash pass.

#### A defect found while checking this, worth its own line

`C:\Users\AustinBerk\Documents\My Brain\00-Meta\commitments.md` line 579 ends: *"One line to Demetria settles it; then record in `99-Archive/2026-08-catchup/entity-pages/`."* **That is a live instruction pointing at an archive folder.** VERIFIED. It is a mechanical artefact of the fold, where every `02-entities/` reference was rewritten to the archive path, including ones that were instructions about where to file future work. **The same rewrite hit `10-Business\people\road-trip-roster-2026-08.md`, which now tells readers to see `99-Archive\2026-08-catchup\entity-pages\belle-haven.md` when `60-Communities\belle-haven.md` is the live page.** Grep for `99-Archive/2026-08-catchup/entity-pages` across live folders to find the rest.

### 1.4 `vendors-platforms.md`, 5.6KB. ALREADY THERE.

**NEW path:** `C:\Users\AustinBerk\Documents\My Brain\10-Business\vendors\vendor-status-2026-08.md`

**VERIFIED by diff.** All 19 vendor rows present and identical. The only non-path difference is the dropped `[[communities]]` link in Related. The new page added the standard Status and confidence headers. Every vendor named in the old file also has a live page in `10-Business\vendors\` or a live mention: Champion, Cavco, Camp Spot, Rent Manager, Ramp, Triad, Uniti, MAV, FastField and the rest.

#### CONFLICT 3: Rellit or Rillet. This Brain spells the same vendor two ways.

**OLD**, `02-entities\vendors-platforms.md`: **"Rellit"**, described as an accounting and fintech platform, gated on the CFO decision.

**NEW**, and both spellings are live:

- `C:\Users\AustinBerk\Documents\My Brain\00-Meta\parked-decisions.md` line 30, `PD-03`: *"Whether to adopt **Rellit**"*. Line 32, `PD-05`: *"**Rellit** adoption"*.
- `C:\Users\AustinBerk\Documents\My Brain\10-Business\tools-and-systems.md` line 12: *"the August 2026 **Rellit** conversation"*.
- `C:\Users\AustinBerk\Documents\My Brain\70-Operations\meetings\2026-08-31-accounting-platform-intro-rillet.md`, a filed meeting record, spells it **Rillet** in the filename and throughout.

**VERIFIED.** INFERRED, at high confidence: **Rillet is correct and Rellit is a diarization error** carried out of the Plaud recording into the old vendor page, then inherited by two parked decisions and the tools page. The meeting record is the primary artefact and the later one; `00-Meta\index.md` describes it as *"The AI accounting platform intro, and the clearest description of the expense-side stack in this vault."*

**Why this one is not cosmetic.** `PD-03` and `PD-05` are two of the 29 parked decisions waiting on Austin's ruling, and one of them gates the other. **A search of this Brain for "Rillet" does not return either decision.** Anyone preparing that ruling from the meeting record would not find the parked rows, and anyone working the parked rows would not find the meeting record.

**Recommend:** correct `PD-03`, `PD-05` and `10-Business\tools-and-systems.md` to Rillet, keep Rellit as a noted alias on the vendor page per the contradictions rule, and log it in `00-Meta\audit-log.md` with the reason. **Do not silently overwrite.** The archived `vendor-status-2026-08.md` keeps Rellit as the historical record of what the recording said.

### 1.5 `karen-doner.md`, 5.4KB. MIGRATE.

**What the file is.** A page on **Karen Doner of Doner Law PLC**, `kdoner@donerlawplc.com`, engaged 2026-08-28 as outside employment counsel on the David Berman separation. It reconstructs that day hour by hour from Sent Items, Teams, the calendar and a Plaud recording, then summarises what she is advising on, then carries a five row table of other counsel and a naming caution.

**Ruling 5 governs the disposition. Austin, 2026-09-03:** *"Karen Doner is Parakeet and affiliates employment attorney."* **She is a vendor relationship. Rule 7 does not apply to the page about her.**

**Does NEW have it? No page, yes facts. VERIFIED.**

- `C:\Users\AustinBerk\Documents\My Brain\10-Business\outside-help\` contains `baldwin.md`, `citrin-cooperman.md`, `counsel.md`, `lenders.md`. **No `karen-doner.md`.** Checked per instruction.
- `10-Business\outside-help\counsel.md` does not mention her.
- Her role is well established elsewhere: `00-Meta\commitments.md` CM-16 tracks her across 2026-08-29, 08-30 and 08-31, upgrading her from INFERRED to VERIFIED and quoting her instruction *"I'd stop emailing him at this point"*; `00-Meta\audit-log.md` line 53 logs that upgrade with its reason; `10-Business\people\_private-assessments.md` line 63 records it.

**NEW folder and page shape.** `C:\Users\AustinBerk\Documents\My Brain\10-Business\outside-help\karen-doner.md`, following `10-Business\_example-page.md` and the shape of the sibling `baldwin.md` and `citrin-cooperman.md`: What this is, Status, The facts, Related, Decisions, Sources. **One `[[wikilink]]` line in `10-Business\MOC-Business.md`**, per the MOC rule, and one Related link at most.

**What must be stripped before it can be written, and this is not optional.**

1. **Rule 9, personal compensation. Four figures on the old page violate it outright.** The severance working plan of *"six months salary and benefits continuation plus a prorated bonus (~25% of salary)"*; the benchmarks *"Janine (~6 months + $50,000), Stacy (~$38,000 ≈ 4 months)"*; the MIP valuation *"~$1,500"*; and the Rose Consulting hire at *"$20K above approved range"*. **Rule 9 says never record any individual's personal compensation anywhere in this Brain.** `_private-assessments.md` line 68 already states these were deliberately not restated when CM-16 was written. **They must not arrive now through a different door.**
2. **Rule 7, the nuance in ruling 5.** Everything specific to the Berman matter, the termination grounds, the age-over-40 review, the forfeiture mechanics, the legal hold and the IT forensics, is a personnel matter. It stays in `00-Meta\commitments.md` CM-16 and the `_private-` files. **Her page records the relationship, the firm, the contact, the scope and the engagement date. Not the matter.**
3. **The unresolved-name paragraph.** The old page flags that the Plaud summary renders a new hire as *"Dimitri"* and INFERS **Daniel Bennett**. That is personnel and it is unconfirmed. Off her page.
4. **The dash pass, ruling 4.** The old file uses em dashes throughout, including inside the table cells.

**What is genuinely worth carrying, beyond the identity block.** The five row other-counsel table and the naming caution that Doner Law is not transactional counsel, with the note that deal attorney **Brian Action moved to Paul Hastings, the same office as Berman's brother**, flagged as a conflict concern. That last one is SINGLE-SOURCE in the old file, and it is corroborated in this Brain: **Paul Hastings and Brian Action both appear in `00-Meta\commitments.md`.** VERIFIED. **It belongs on `counsel.md` as a conflict note, not on her page.**

**Two open items on the old page to check before writing, not to copy forward.** The surname spelling is INFERRED from the email address rather than a signature block. And Demetria's unanswered 2026-08-31 question about what she owed Karen. **Rule 11 applies: check `99-Archive\` and `00-Meta\commitments.md` before surfacing either as open.** CM-16 has moved several times since 2026-08-31 and the daily closes through 2026-09-02 mention Doner, so both may already be settled.

---

## Section 2: `03-domains/`, 6 files

**All six are ALREADY THERE. VERIFIED by direct diff on every one.** This is the cleanest part of the fold. Every difference in all six files is either a mechanical path rewrite or the three standard headers this Brain adds to a folded page: a What this is line, a Status line reading *"needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`"*, and a confidence-labels line. **No substantive sentence was dropped from any of the six.**

| OLD file | Size | NEW path | Relationship |
|---|---|---|---|
| `supply-chain.md` | 6.9KB | `70-Operations\supply-chain-model.md` | Superset. Adds a source-state paths callout about the read-only estate. |
| `delivery-bottleneck-2026-09.md` | 17KB | `70-Operations\delivery-bottleneck.md` | Identical body. Headers only. |
| `license-permit-transition-plan.md` | 14KB | `70-Operations\license-and-permit-ownership.md` | Identical body. Headers only. |
| `intercompany-arap-recon-plan.md` | 25KB | `80-Finance\intercompany-arap-recon.md` | Superset. Adds the 2026-08-31 sequencing ruling. |
| `sales-org.md` | 2.5KB | `50-Products-Sales\sales-org-buildout.md` | Superset. |
| `systems-data-architecture.md` | 3.9KB | `10-Business\systems-architecture.md` | Superset. Adds a large 2026-08-31 VERIFIED block. |

**All six are linked from their folder MOC. VERIFIED**, checked line by line in `70-Operations\MOC-Operations.md` lines 53 to 55, `80-Finance\MOC-Finance.md` line 22, `50-Products-Sales\MOC-Products-Sales.md` line 25, and `10-Business\MOC-Business.md` lines 86 and 93.

### 2.1 On the brief's question about `systems-data-architecture.md` versus `systems-architecture.md`

**They are the same page. VERIFIED by diff: zero old lines are absent from the new one.** `10-Business\systems-architecture.md` is the folded old file, renamed, plus a section headed "What the 2026-08-31 consultation established" that is the first VERIFIED material on the page. The old file's own naming flag survived the fold and now reads as resolved rather than open, because it warned:

> "`00-Meta/decisions/2026-08-26-company-assessment-plan.md` ... proposes a WS4 output at `10-Business/systems-architecture.md` covering this exact question ... **Before building that WS4 output, reconcile it with this file rather than creating a second one**"

**The path in that warning is now this page's own path.** INFERRED: the rewrite pass resolved the risk it was warning about by putting the old file at the destination the plan wanted. **Worth confirming with one read of the assessment plan before anyone builds a WS4 output, because a session reading that sentence today could conclude the work is still to do.**

### 2.2 Two things the fold carried forward that need attention on their own

#### Rule 3 gap: the 37-day cycle figure is not in the ledger, and money is derived from it.

**VERIFIED.** `C:\Users\AustinBerk\Documents\My Brain\70-Operations\supply-chain-model.md` line 78:

> "**Home-set average: 37 days, against a 45-day target.** The first actual cycle-time number this domain file has ever recorded."

**Neither 37 days nor the 45-day target appears in `C:\Users\AustinBerk\Documents\My Brain\00-Meta\numbers-ledger.md`.** Grep across all 312 lines returns nothing on either. The ledger has a "Home and infill economics" section that would be its home, and it carries cost and financing assumptions but no cycle time at all.

**Why that is not a filing nicety.** `C:\Users\AustinBerk\Documents\My Brain\70-Operations\delivery-bottleneck.md` computes off it:

> line 157: "- 43 homes × 37 days (baseline set cycle) = 1,591 home-days → **≈ $36,600 forgone lot rent**"

**So a dollar figure in an operations analysis rests on an input that the ledger does not carry and cannot date.** CLAUDE.md rule 3 says numbers live in the ledger with a source and an as-of. **Recommend two ledger rows, 37-day home-set average and 45-day target, both sourced to the road-trip document with an as-of of 2026-08-25 and labelled SINGLE-SOURCE, and the $36,600 marked as derived.**

#### Three vendor names are spelled two ways each, and all three came through the fold.

**VERIFIED, and this is one pattern rather than three coincidences.** All three originate in AI transcription of the same road-trip recordings.

| Vendor | Spelling A, and where | Spelling B, and where | Which is right |
|---|---|---|---|
| Rillet | **Rellit** in `00-Meta\parked-decisions.md` `PD-03` and `PD-05`, and `10-Business\tools-and-systems.md` line 12 | **Rillet** in `70-Operations\meetings\2026-08-31-accounting-platform-intro-rillet.md` | Rillet, INFERRED at high confidence. The meeting record is the primary artefact and the later one. |
| Uniti | **Uniti** in `10-Business\systems-architecture.md` and `10-Business\vendors\vendor-status-2026-08.md` | **Unity** on the 2026-08-31 recording, flagged on `10-Business\systems-architecture.md` itself | Undetermined. This Brain already flags it and says *"Worth one look before either name reaches a contract or a report."* |
| Jon Wyss | **Jon** everywhere in this Brain | **John** throughout the road-trip source, and left as written on the folded pages | Jon. Already flagged on `10-Business\people\road-trip-roster-2026-08.md`. |

**The Rillet one is the only one that is not already flagged, and it is the one that costs something.** `PD-03` and `PD-05` are two of the 29 parked decisions, and `PD-03` gates `PD-05`. **A search of this Brain for "Rillet" returns the meeting record and not the two decisions it governs.** See CONFLICT 3 in section 1.4.

---

## Section 3: `05-decisions/`, 5 files

### 3.1 The four decision records. ALREADY THERE, all four.

**VERIFIED by direct diff on every one.** Each is in `C:\Users\AustinBerk\Documents\My Brain\00-Meta\decisions\` under the same filename, and each also has its line on the spine at `C:\Users\AustinBerk\Documents\My Brain\00-Meta\decisions-log.md`. **Both halves of the arrangement CLAUDE.md describes are satisfied: the log line and the full record.**

| OLD file | NEW full record | Spine line | Diff |
|---|---|---|---|
| `2026-08-26-storage-target-state.md` | `00-Meta\decisions\2026-08-26-storage-target-state.md` | `decisions-log.md` line 42 | 1 line, a path rewrite |
| `2026-08-26-dr035-no-action.md` | `00-Meta\decisions\2026-08-26-dr035-no-action.md` | `decisions-log.md` line 43 | 1 line, a path rewrite |
| `2026-08-26-company-assessment-plan.md` | `00-Meta\decisions\2026-08-26-company-assessment-plan.md` | `decisions-log.md` line 45 | 3 lines, all path rewrites |
| `2026-08-29-brief-delivery-artifact-only.md` | `00-Meta\decisions\2026-08-29-brief-delivery-artifact-only.md` | `decisions-log.md` line 46 | 3 lines, all path rewrites |

**On the brief's question about the storage decision and `10-Business\sharepoint\`.** The decision record is filed in `00-Meta\decisions\`, which is correct per the folder map. Its operational detail sits where the record now points, `10-Business\sharepoint\migration-risks.md`, and that page is listed in `00-Meta\index.md`. **The Birdcage as system of record ruling is also restated in CLAUDE.md itself**, under the heading "The Parakeet Communities SharePoint is read-only". **Nothing to move. VERIFIED.**

**On `2026-08-26-dr035-no-action.md`.** This is Austin's documented no-action on a known-wrong hard-costs subtotal in two replacement-cost FINALs already delivered to Jadian Capital. It is intact, and `decisions-log.md` line 43 carries the important qualifier verbatim: *"The other 52 unresolved divergences are not covered by this decision."* **The old file's pointer to the Jon Wyss decision queue was rewritten to `00-Meta\commitments.md` item 3, and that item exists. VERIFIED. Nothing lost.**

### 3.2 Two rewrite defects inside the assessment plan, and they are the same defect class as the one in section 1.3

**VERIFIED.** `C:\Users\AustinBerk\Documents\My Brain\00-Meta\decisions\2026-08-26-company-assessment-plan.md` describes workstream outputs. Two of those output paths were rewritten into something that no longer reads as an instruction.

| Line | OLD text | NEW text | The problem |
|---|---|---|---|
| 78 | Output: `02-entities/org-map.md` plus a function-to-owner matrix | Output: `99-Archive/2026-08-catchup/entity-pages/org-map.md` plus a function-to-owner matrix | **WS1 is now told to write its output into the archive.** No `org-map.md` exists there or anywhere. |
| 93 | Output: `03-domains/operating-rhythm.md` | Output: `70-Operations/ (page not built)` | **An instruction was converted into a status.** A session reading this cannot tell what page it was asked to build. |

**Neither is a business problem and both are cheap to fix now.** They matter because this plan is not executed yet, so these lines are live instructions rather than history. **Recommend WS1's output be redirected to `10-Business\entity-structure\` and WS3's named as `70-Operations\operating-rhythm.md`, with a row in `00-Meta\audit-log.md` giving the reason.** Both need Austin's nod, since the plan is a filed decision record.

### 3.3 `parked-decisions-register.md`, 7.8KB. ALREADY THERE, and the mapping is exact.

**NEW path:** `C:\Users\AustinBerk\Documents\My Brain\00-Meta\parked-decisions.md`

**Ruling 3 asked for a mapping table before anything else. Here it is, and the answer is simpler than expected: the 19 old rows are `PD-01` to `PD-19`, in the same order, with the same numbers. VERIFIED.**

The old register numbered its rows 1 to 19. The new register kept those numbers as the ID and prints both, in the form of a code span followed by the original number. `C:\Users\AustinBerk\Documents\My Brain\00-Meta\id-conventions.md` confirms the method: *"`PD-nn` ... the page's own row numbers."* **No row was renumbered, dropped, merged or split.**

| OLD row | OLD decision | NEW ID | Status in NEW | Owner in NEW |
|---|---|---|---|---|
| 1 | Ozzie's future, 2-week evaluation window | `PD-01` | Open | **Jon Wyss** |
| 2 | Berman, no decision despite frustration | `PD-02` | Open | **Austin** |
| 3 | CFO and accounting ownership | `PD-03` | Open | unassigned |
| 4 | MAV MCP versus warehouse-only | `PD-04` | Open | unassigned |
| 5 | Rellit adoption | `PD-05` | Open | unassigned |
| 6 | Corner IQ trial scope | `PD-06` | Open | **Austin** |
| 7 | Referral-fee ethics for outside managers | `PD-07` | Open | unassigned |
| 8 | Centralized landscaping business case | `PD-08` | Open | unassigned |
| 9 | Regency landlord strategy, Larry | `PD-09` | Open | unassigned |
| 10 | FEMA homes, sell cheap versus scrap | `PD-10` | Open | **Team** |
| 11 | Well relocation feasibility, River Oaks | `PD-11` | Open | **John Clark** |
| 12 | Pickleball versus residents' preferences | `PD-12` | **RULED 2026-08-31.** Scoped and delegated: River Oaks only, Vikki via Natalie | unassigned |
| 13 | Clubhouse repair versus sinking foundation | `PD-13` | **RULED 2026-09-01.** *"River Oaks is Repairable."* Repair, not replace | **John Clark** |
| 14 | Dog wash versus bathroom conversion | `PD-14` | **RULED.** Bathroom conversion, no dog wash | **John Clark** |
| 15 | Shuffleboard roof design, Lucky Clover | `PD-15` | Open | **John Clark** |
| 16 | Whether Rose's investor residents may rent out | `PD-16` | Open | **Natalie Magurne** |
| 17 | New-home pricing at The Oaks | `PD-17` | Open | **Leslie Croft** |
| 18 | Office space solution at Vantage Oaks | `PD-18` | Open | **Zach Schwartz** |
| 19 | I-4 corridor exposure at Windward Knoll | `PD-19` | Open | **Zach Schwartz** |

**No old row is without a PD equivalent. Nothing is a candidate for a new number. VERIFIED.**

**Three of the 19 have been ruled since. Ruling 3 predicted this and it is right, though "already closed" is not quite what happened.** `PD-12`, `PD-13` and `PD-14` all carry Austin's ruling in their Status cell **and all three are still sitting in the Open table.** `PD-13`'s own cell contains the words *"Move to Resolved"* and it has not been moved. **The Resolved section of that page holds only `PD-37` and `PD-38`.** That is a housekeeping gap in this Brain rather than a migration question, and it means the page's own open count runs three high.

#### Three enrichments the new register added, and one small repair

1. **An Owner column that did not exist.** The page says why: *"This register had none: every row was implicitly Austin's because the page is decisions waiting on his ruling. **Five of them are not his**, and he said so on the board."* Eleven of the 19 now carry a named owner. **Eight are still unassigned**, which is the useful number.
2. **Community wikilinks on eight rows**, pointing at the live `60-Communities\` pages.
3. **The register grew from 19 rows to 38 IDs.** `PD-20` onward came from later sources: the delegation board, Jon's August field report, the rehab tracker ingest, the End of Day close, and the 2026-09-03 a2zcp mailbox sweep.
4. **A malformed-table repair. VERIFIED.** Old rows 16, 17 and 18 carry only four cells where every other row carries five: **the Context column is missing entirely on all three.** The new register supplies the missing cell on each. **But it fills the empty Context with an em dash as the placeholder**, which the voice rule forbids. Cosmetic, and worth catching in the same pass as anything else on that page.

#### One stale count, flagged not fixed

`C:\Users\AustinBerk\Documents\My Brain\00-Meta\index.md` says: *"**29 decisions waiting on Austin's ruling, `PD-01` to `PD-29`.**"* `C:\Users\AustinBerk\Documents\My Brain\00-Meta\id-conventions.md` gives the same range. **The file itself carries IDs through `PD-38`. VERIFIED by grep.** So the map undercounts by nine, and `index.md` already records that undercounting maps are the specific failure it was rebuilt to fix on 2026-09-02: *"A map that undercounts is worse than one that is missing, because a session reads it and stops looking."* **The same thing has happened again in the same place.**

---

## Section 4: the old root `CLAUDE.md`, 12.6KB. SUPERSEDED.

**NEW version:** `C:\Users\AustinBerk\Documents\My Brain\CLAUDE.md`, with the old file archived at `C:\Users\AustinBerk\Documents\My Brain\99-Archive\2026-08-catchup\superseded-brain-CLAUDE.md`.

**Ruling 2 governs and is applied: the old constitution does not merge.** What follows is the full comparison the brief asked for, reported as findings rather than as a merge plan. **It is worth doing precisely because it is the only way to tell whether the 2026-08-31 fold lost anything, and it did.**

### 4.0 First, a fact about the archived copy that changes how to read it

**The archived copy is four rules behind the live old file. VERIFIED by diff.** `99-Archive\2026-08-catchup\superseded-brain-CLAUDE.md` was taken on 2026-08-31. The old `CLAUDE.md` was then edited on 2026-09-03 and gained three new rules, and one rule was rewritten. **So the archive does not contain the newest thinking in the old vault, and anyone treating the archived copy as the complete old constitution will miss the three most recent rules in it.** Those three are items 7, 8 and 9 in the list below, and they are the ones most likely to be worth adopting, because they are the only rules in the old file that postdate the fold.

### 4.1 What the two constitutions agree on

**Three of the old file's rules are in this Brain, credited, and stronger. VERIFIED.** `My Brain\CLAUDE.md` says so itself, under the heading "The evidence rules — adopted 2026-08-31, Austin's sign-off": *"These three came from the Claude Code vault that was folded into this Brain on 2026-08-31."*

| OLD rule | NEW rule | What changed |
|---|---|---|
| Label confidence on every claim, three labels, verify against the primary artefact | **Rule 10** | Same rule, same precedent (the "18 reds pending" failure), extended from numbers to every claim. |
| Never surface an item without checking the archive and the open-loops file first | **Rule 11** | Same rule, same precedent (the Toby Nelson re-raise of 2026-08-27), retargeted at `99-Archive\` and `00-Meta\commitments.md`. |
| Contradictions stay visible | **Page rules**, under "Contradictions stay visible" | Same rule, plus a named register for them, `00-Meta\open-items.md`. |

**Rule 15 is not from the old file.** It was proposed by Claude on 2026-08-31 and endorsed by Austin the same evening, and it exists because of failures the old vault's own pages caused. **It is the rule that would have caught the counsel gap in section 1.3.**

### 4.2 Every rule in OLD that NEW does not carry

**Seventeen items. Each was checked by grep across every live folder in this Brain, excluding `99-Archive\` and this report. VERIFIED.**

#### Group A: dropped conventions

**1. Verify the current date from the system clock before datestamping anything.** OLD: *"A full-vault off-by-one occurred on 2026-08-26 from assuming the date instead of checking it."* **The phrase "system clock" appears nowhere in this Brain. NOT CARRIED.** This is the cheapest rule in the old file and it has a named failure behind it. **Recommend adopting it.** Everything in this Brain is datestamped, `00-Meta\log.md` and `00-Meta\audit-log.md` are append-only and dated, and a repeat of that off-by-one would corrupt both.

**2. Filenames are `kebab-case.md`, entities get their own file, no dated filenames except in the decisions folder.** **"kebab-case" appears nowhere in this Brain. NOT CARRIED as a written rule**, although it is followed in practice on every page, and `00-Meta\decisions\` does use the `YYYY-MM-DD-slug.md` form. INFERRED: the convention survived as habit rather than as a rule. **Low stakes, but a new page written by a session that has not seen this will not know it.**

**3. Absolute dates always. Never "next week" or "last month".** **PARTIALLY CARRIED, and demoted.** It exists in `95-Agents\morning-brief.md`, `95-Agents\weekend-pulse.md`, `00-Meta\commitments.md` and `85-Personal\key-dates.md`, so it governs some routines. **It is not in `My Brain\CLAUDE.md`, so it does not govern anything outside those four.**

**4. Provenance on every substantive fact: cite the file path, message ID, or quote.** **SUBSTANTIALLY CARRIED and improved.** Rule 3's "always name the file" clause is stronger on documents than the old rule was. Rule 15's source-links clause covers deep links for mail and Teams. **The one part that thinned is the message ID and the quote as acceptable provenance for something that is not a file.**

**5. Link liberally.** OLD: *"Link with `[[wiki-links]]`. **Link liberally**; a link to a note that does not exist yet marks work worth doing."* **NOT CARRIED, and reversed. See CONTRADICTION 2.**

**6. The three-item ceiling.** OLD: *"Anything in `01-now/` presented to Austin tops out at three items. If there are more, they are ranked and held, not shown."* **REPLACED by rule 12 on 2026-09-01. See CONTRADICTION 1.** Ruling 2 settles it and it is not re-opened here.

#### Group B: the three rules added to OLD on 2026-09-03, all absent from NEW

**These three are the substance of what the comparison was for. All three postdate the fold, none is in this Brain, and each has a named failure behind it. VERIFIED by grep.**

**7. A matter's name and its character come from a primary document, never from a thread subject, never from a folder name.** The phrase "primary document" appears nowhere in this Brain outside the archived copy. **The two failures the old file records are both live concerns here:**

> "(1) The Eckert Seamans settlement was labelled "Belle Haven" for five consecutive briefs; it is **American**, in Massachusetts, and Belle Haven is an unrelated Clearwater FL asset. No message in the thread names a property, so every sweep keyed the matter to the subject line and nothing written could contradict it. (2) A Cowork folder named *"Belle Haven & Silver Breeze Site Plan Dispute"* was read as evidence of an "active Belle Haven legal matter"; the memo inside frames it as *"a records correction rather than an appeal"*, and the county's 98-record permit history shows *"no site plan case, no lot-count violation, ever."*"

**This Brain has already absorbed the corrections without absorbing the rule.** `60-Communities\american.md` correctly names the Eckert Seamans matter as American, and `60-Communities\belle-haven.md` correctly frames the Gunster work as a records correction with the 98-record permit history. **So the outputs were fixed and the mechanism that produced them was not.** The old file's closing line is the reusable part: *"when a detail sits oddly against a label, test the label."* **Strongest candidate for adoption of anything in the old file.**

**8. Generated `.eml` "DRAFT - open and hit send" files are corpus output, not commitments. Do not mine them.** With Austin's words, 2026-09-03: *"the drafts are always a mess. Will need to review manually."* **NOT CARRIED as a rule.** The phrase "open and hit send" appears on three live pages, `00-Meta\commitments.md`, `10-Business\eos\drafts\jon-decision-items-extracted.md` and `10-Business\storage-inventory\birdcage-corporate.md`, but as descriptive content about what is in the Birdcage corpus, not as a prohibition on mining it. **This Brain also has thirteen of its own drafts in `drafts/` folders, and `00-Meta\index.md` correctly says a draft is Claude's work and not a sent thing.** So half the rule is present in a different form. **The half that is missing is the instruction not to take a matter's name, its character or a commitment out of a generated draft**, and that is the half with Austin's quote behind it.

**9. Route by owner, not by discovery.** OLD: *"A finding surfacing in Austin's mail does not make it Austin's action. Gunster/land-use items are **Jon's** (Austin, 2026-09-03: 'more FYI as those are in Jon's purview to run down'). Record the durable substance in the vault; put only Austin's own actions in front of him."* **NOT CARRIED.** This Brain has the machinery for it: `00-Meta\owner-list-for-review.md` holds the 33 owner values Austin set, `00-Meta\delegation-board.md` exists, and `CLAUDE.md`'s "How findings get delivered" says to route a finding to the person who owns it. **What is missing is the negative half: that appearing in Austin's mailbox is not evidence of ownership.** Given rule 14's 2026-09-03 weighting of the a2zcp mailbox as the highest-concentration unrouted surface in the Brain, **this rule is about to matter more rather than less.**

#### Group C: dropped from OLD's "Working with Austin" block

**10. One next action per response. Never a menu.** **NOT CARRIED, and this one is worse than a gap: this Brain's constitution depends on it and points at a page that does not contain it. VERIFIED.**

`My Brain\CLAUDE.md` cites it twice as the limit on two of its own rules:

> line 38: "**This does not loosen the one-next-action rule** in [[00-Meta/austin-operating-manual]]. Three paths is what he sees; one action is what he is asked to take."
> line 93: "**This does not loosen "one next action per response"** in [[00-Meta/austin-operating-manual]]. That governs what he is asked to *do* in a reply. This governs what he is allowed to *see*."

**`C:\Users\AustinBerk\Documents\My Brain\00-Meta\austin-operating-manual.md` contains no such rule.** The string "next action" does not appear in it at all. Nor does "menu" appear anywhere in any live folder. **The rule exists only in the old vault's `CLAUDE.md`.**

**Why this is the most consequential finding in section 4.** Rule 12 says show everything and highlight three, and the three-paths rule says every issue arrives with three options. **Both are explicitly bounded by the one-next-action rule, and that bound is currently unwritten.** So the two rules that expand what Austin sees are in force and the rule that limits what he is asked to do is not. **Recommend it be written into `00-Meta\austin-operating-manual.md` verbatim from the old file, so the two citations in `CLAUDE.md` resolve.** Needs Austin's sign-off only because it lands in a page his manual owns; the rule itself is his.

**11. Never say "you are behind." Say what is un-indexed, un-decided, or un-delegated.** **NOT CARRIED.** The phrase appears nowhere in this Brain. INFERRED: this is a voice rule about a person with a specific working style, and `00-Meta\austin-operating-manual.md` is where it belongs. **It is also the rule most directly at risk from rule 12, because a 943-row board and a growing tail are exactly the shape of a page that reads as "you are behind" without ever using the words.**

**12. Make completed work visible.** **NOT CARRIED, and the omission looks deliberate but incomplete.** `00-Meta\austin-operating-manual.md` ends with a comment block listing what was consciously dropped from the original knowledge file, including *"family names and a clinical label, where the operational instruction ... carries the full value without the exposure."* **So the clinical framing was removed on purpose and correctly. The operational instruction went with it.** Recommend the instruction be restored without the framing: make completed work visible.

**13. Decide reversible things and report; ask only about money, third parties, and irreversibility.** **NOT CARRIED as a rule, and superseded in substance.** This Brain's guardrails 5 through 9 are far more specific and far more restrictive: resident-facing documents, investor and board material, personnel, money out the door, and no individual compensation anywhere. **The old rule's permissive half, decide reversible things and report, is the part that did not survive**, and nothing in this Brain grants that latitude explicitly. INFERRED: not a problem, because the guardrails enumerate what to ask about and everything else is regular. **Worth one line in the operating manual so a session does not over-ask.**

**14. Delegate anything mechanical to an agent.** **NOT CARRIED.** See item 16 below; the agent model changed underneath it.

#### Group D: dropped structure and framing

**15. The design constraint.** OLD: *"this vault must not require discipline to maintain. Anything depending on Austin remembering to file something will fail. Agents maintain it."* **NOT CARRIED.** This Brain says the operational half in its page rules, *"Claude writes the pages. Humans drop things in `05-Inbox/` and talk"*, but not the constraint itself. **The constraint is the reason for the design, and a session that has the mechanism without the reason will eventually propose something that needs Austin to remember to file it.**

**16. The four-agent roster.** OLD names `chief-of-staff`, `cloud-archivist`, `supply-chain-analyst` and `second-brain-librarian`. **This Brain's `95-Agents\` holds eight briefs and none of them is one of those four.** The model changed on purpose: OLD's agents were personas, NEW's briefs are jobs, and `CLAUDE.md` says *"One file = one job Claude does on repeat."* **Not a loss, but note that all four old agent names are still live agent types in the Claude Code environment**, so a session can invoke `cloud-archivist` while this Brain has no brief describing what that agent is for here. **Worth one line in `95-Agents\` mapping the four environment agents to the eight jobs, or saying explicitly that they are not used.**

**17. Known problem 7, "Three identities, no bridge."** **DROPPED FROM THE EIGHT. See CONTRADICTION 4.**

### 4.3 Every place the two constitutions contradict each other

**Seven contradictions. Each quoted from both sides with its path.**

#### CONTRADICTION 1: the three-item ceiling. Settled by ruling 2.

**OLD**, `C:\Users\AustinBerk\Documents\Claude\Code\brain\CLAUDE.md`:

> "**Three-item ceiling.** Anything in `01-now/` presented to Austin tops out at three items. If there are more, they are ranked and held, not shown."

and again: "Three-item ceiling on any list."

**NEW**, `C:\Users\AustinBerk\Documents\My Brain\CLAUDE.md` rule 12:

> "**Show everything, highlight three.** Adopted 2026-09-01 at Austin's instruction, **replacing the three-item ceiling** that ran from 2026-08-31. His words: *"I think the rule should be to include everything but highlight or have an important topics of 3."*"

**NEW wins, and it records what the ceiling cost:** *"In one day it held back an AB/JW decision on a $250,000 lender reserve, a direct question from Leslie on a new vendor partnership, a one-word yes Jon was waiting on, and an overdue month-end task."* **Not re-opened. Ruling 2 is explicit.**

#### CONTRADICTION 2: how much to link. Direct opposites, and nobody has adjudicated it.

**OLD:**

> "**Link with `[[wiki-links]]`.** Link liberally; a link to a note that does not exist yet marks work worth doing."

**NEW**, `My Brain\CLAUDE.md`, Page rules:

> "**The MOCs do the linking; pages barely link at all.** A page is connected because its folder's MOC lists it — that is its one guaranteed link. On the page itself, add a `[[wikilink]]` only where it genuinely earns its place ... Most pages carry two links or fewer. Never link the ledger, the business-model page, the index, or sibling pages out of habit — that is what turns a readable Brain into an unreadable mesh."

**These are not reconcilable and NEW is clearly the current rule.** **The reason to record it rather than just note it: every one of the twelve already-folded files was written under the old rule**, and it shows. The archived entity pages carry four and five link Related blocks. `10-Business\vendors\vendor-status-2026-08.md` and `10-Business\people\road-trip-roster-2026-08.md` are live pages that still carry old-rule Related blocks. **Anything migrating from the old vault needs a link trim in the same pass as the dash pass.**

#### CONTRADICTION 3: the folder map. Eight folders against thirteen.

**OLD** defines eight: `00-inbox/`, `01-now/`, `02-entities/`, `03-domains/`, `04-index/`, `05-decisions/`, `06-reference/`, `99-archive/`. **NEW** defines thirteen, and `CLAUDE.md` says they *"follow the org chart rather than a generic template."*

**Not a real conflict, because the fold already mapped every old folder onto a new one, and the archived copy of the old constitution has that mapping written into it. VERIFIED.** Recorded for one reason: **the old file also carries the mapping inside a table that now describes this Brain rather than the old vault**, so the archived copy reads as a partly-rewritten document rather than as a faithful artefact. Ruling 2 wants it archived *"as the artefact that rules 10, 11 and 15 came out of"*, and the copy in `99-Archive\` is not quite that artefact. **The unrewritten original is the file at `C:\Users\AustinBerk\Documents\Claude\Code\brain\CLAUDE.md`.**

#### CONTRADICTION 4: the eight known problems are not the same eight.

**OLD** problem 7: *"**Three identities, no bridge.** Nothing links Parakeet, A2Z, and personal records."*

**NEW**, `10-Business\storage-inventory\known-problems.md` problem 7: *"**Two legal sites exist with no documented distinction.** `/sites/Corporate-Legal` and `/sites/LegalParakeet`."*

**Both files say "eight". Seven of the eight match. The seventh slot is a substitution. VERIFIED by reading both lists end to end.** The two-legal-sites item was unnumbered prose in the old file, and it was promoted into the numbered eight while "three identities, no bridge" came out. **"Three identities" survives only in the archived old constitution.**

**This is not a loss of the fact.** The three-identity question is the whole subject of `10-Business\entity-structure\berk-inc-umbrella.md`, and `00-Meta\commitments.md` item 6 owns it with Austin named as the non-delegable owner. **It is a loss of the framing that it is a defect in the storage estate as well as an open entity question**, which is what made it cheap to fix during Albert's migration. **Recommend one line in `known-problems.md` cross-referencing the umbrella page, so the migration window is not missed on it.**

#### CONTRADICTION 5: where a decision lives.

**OLD:** a single folder, `05-decisions/`, holding both the log and the records, with the convention *"No dated filenames except in `05-decisions/`, which uses `YYYY-MM-DD-slug.md`."*

**NEW:** a spine and a records folder, `00-Meta\decisions-log.md` append-only plus `00-Meta\decisions\` for full records, and `CLAUDE.md` adds a third destination: *"A decision also goes on the page it affects, in that page's own Decisions section."*

**NEW wins and the fold already implemented it. VERIFIED**, per section 3.1: all four old records are in both places. **Recorded because the old file's convention line is the only place the `YYYY-MM-DD-slug.md` filename rule is written down**, and this Brain follows it without stating it.

#### CONTRADICTION 6: one register against six.

**OLD** routes everything through `01-now/open-loops.md` and says a stalled parked decision *"belongs in `01-now/open-loops.md` as a slipped commitment instead."*

**NEW** has six registers with a stated non-overlap rule, permanent reference IDs per rule 15, and the equivalent line pointing at `00-Meta\commitments.md`.

**NEW wins decisively, and it is the single largest structural improvement in the fold.** Recorded for one reason: **the old vault's `01-now/open-loops.md` item numbers are still cited by number across this Brain's migrated pages.** `99-Archive\2026-08-catchup\entity-pages\river-oaks.md` and its live siblings point at *"`00-Meta/commitments.md` item 2"*, *"item 9"* and so on, because the rewrite changed the path and kept the number. **Those numbers now resolve against `CM-nn`, which is the same numbering, so they happen to be right.** VERIFIED against the register for eight of them: `CM-02` security exposure on corporate storage, `CM-03` Jon Wyss as the analytics constraint, `CM-06` the Berk Inc entity map, `CM-07` Lucky Clover, `CM-08` Great Oaks, `CM-09` email George about skills, `CM-10` the Belmart bank package, `CM-16` the Berman exit. **Every one matches what the old page cited at that number.** This held by design rather than by luck: `00-Meta\id-conventions.md` says `CM` used *"the page's own item numbers."*

**But six of those eight are now CLOSED, and the old pages still read as urgent. This is a rule 11 trap sitting in the retired vault. VERIFIED.**

| Item | Old vault's framing | Status in `00-Meta\commitments.md` |
|---|---|---|
| `CM-07` Lucky Clover, resident pointed a gun at contractors | *"this week's most urgent safety item"*, owner unassigned | **CLOSED 2026-09-01** |
| `CM-08` Great Oaks, active boil water notice | *"the most urgent property item on the entire list"* | **CLOSED 2026-09-01** |
| `CM-01` known-wrong text in two Jadian reports | open | **CLOSED 2026-09-01** |
| `CM-02` security exposure, the Visa number and gate code 8518 | *"Next action: trim/delete that recording"* | **RISK ACCEPTED 2026-09-01** |
| `CM-03` Jon Wyss as the binding constraint | open | **UNBLOCKED 2026-09-01, CLOSED 2026-09-02** |
| `CM-09` email George about skills | *"unresolved"* | **CLOSED 2026-08-27** |
| `CM-16` Berman exit | open | **CLOSED 2026-09-02** |

**So the two items the old vault ranks as the most urgent things in the portfolio are both closed.** Rule 11 exists for exactly this. **Anyone working from the retired vault, or from the archived copies of its pages in `99-Archive\2026-08-catchup\entity-pages\`, will re-raise closed items unless they diff against `00-Meta\commitments.md` first.** Recommend a one-line banner on `99-Archive\2026-08-catchup\entity-pages\` saying every open item on those pages is superseded by the six registers, because those files are still reachable by search and read as live.

#### CONTRADICTION 7: the dashes. The old file violates the new rule in every paragraph.

**OLD** has no rule about dashes and uses em dashes and en dashes throughout, including in its own rule text.

**NEW**, `My Brain\CLAUDE.md`: *"**No em dashes or en dashes, ever.**"*

**This is ruling 4 and it applies to every file in scope, not just this one.** It is listed here as a contradiction because **the old constitution is the one file where the dashes are inside the rules themselves**, so a dash pass on it would be rewriting rules rather than prose. **That is another argument for archiving it unchanged rather than migrating it**, which is what ruling 2 already says.

### 4.4 What NEW carries that OLD never had

**Recorded briefly, because it is the answer to whether the fold was a net gain. VERIFIED, all from `My Brain\CLAUDE.md`.** Guardrails 5 through 9 (resident-facing, investor and board, personnel, money out the door, no individual compensation). Rule 13, the audit log with a reason on every row. Rule 14, mail sweeps read folders and now two mailboxes, with the a2zcp mailbox weighted first. Rule 15, read the Brain against itself, and the reference-ID scheme. The three-paths-and-a-recommendation rule of 2026-09-03. The read-only SharePoint rule. The LOCKED convention. The community hot sheet. The vocabulary section. **The old file has none of these.**

---

## Section 5: counts, and what needs Austin

### 5.1 Counts by disposition

| Disposition | Count | Files |
|---|---|---|
| **ALREADY THERE** | 23 | `berk-inc`, `communities`, `applegate`, `belle-haven`, `belmart`, `great-oaks`, `lucky-clover`, `regency`, `river-oaks`, `riverwalk`, `vantage-oaks`, `vendors-platforms`, all six of `03-domains/`, and the four decision records plus `parked-decisions-register` |
| **MIGRATE** | 1 | `karen-doner.md` |
| **CONFLICT** | 1 | `people-roster.md` |
| **SUPERSEDED** | 1 | `CLAUDE.md` |
| **DISCARD** | 0 | none |
| **Total** | **26** | |

**Nothing is DISCARD.** Every file in this scope either landed already or holds something worth keeping. **INFERRED, and it is the honest read of the fold: the 2026-08-31 pass was thorough. What it lost, it lost in three specific places, and all three are named above.**

### 5.2 The complete list of things lost or unresolved in the fold

**Ranked by what it costs to leave alone.**

1. **The one-next-action rule.** `My Brain\CLAUDE.md` cites it twice as the bound on rule 12 and the three-paths rule. `00-Meta\austin-operating-manual.md` does not contain it. Section 4.2 item 10.
2. **The External counsel table.** Dropped from `people-roster.md` in the fold. `10-Business\outside-help\counsel.md` says *"Firm not recorded"* about Zach Wallack while two other pages in the same vault say Eckert Seamans. Section 1.3.
3. **The three rules added to the old vault on 2026-09-03**, all absent here: matters get their name from a primary document, generated `.eml` drafts are not commitments, route by owner not by discovery. Section 4.2 items 7, 8 and 9.
4. **Karen Doner has no page**, and ruling 5 says she should. Section 1.5.
5. **Rellit versus Rillet**, splitting two parked decisions from the meeting record that governs them. Section 1.4 and 2.2.
6. **The 37-day cycle figure is outside the ledger** while a dollar figure is derived from it. Section 2.2.
7. **The River Oaks $49,900 price point** exists nowhere in this Brain, and two open items depend on it. Section 1.2.
8. **`PD-12`, `PD-13` and `PD-14` are ruled and still sitting in the Open table.** Section 3.3.
9. **`00-Meta\index.md` and `00-Meta\id-conventions.md` both say `PD-01` to `PD-29`. The file goes to `PD-38`.** Section 3.3.
10. **Rewrite defects: instructions rewritten to point into `99-Archive\`.** Three found, in `00-Meta\commitments.md` line 579, `00-Meta\decisions\2026-08-26-company-assessment-plan.md` lines 78 and 93. Sections 1.3 and 3.2.
11. **Verify the date from the system clock, and the absolute-dates rule at constitution level.** Section 4.2 items 1 and 3.
12. **"Three identities, no bridge" came out of the eight known problems.** Section 4.3, CONTRADICTION 4.
13. **The archived old constitution is four rules behind the live old file**, and its folder table was rewritten, so it is not a faithful artefact. Section 4.0 and CONTRADICTION 3.
14. **The archived entity pages read as live and present closed items as urgent.** Section 4.3, CONTRADICTION 6.

### 5.3 What migration work would actually involve, if it is authorised

**Only one file migrates: `karen-doner.md`.** Per ruling 5, to `10-Business\outside-help\karen-doner.md`, linked once from `10-Business\MOC-Business.md`.

**Three things have to happen to it first, and none of them is a find and replace.**

1. **Strip four compensation figures.** Rule 9. Listed in section 1.5.
2. **Strip the Berman matter detail.** Rule 7 and the nuance in ruling 5. Her page carries the relationship; `00-Meta\commitments.md` `CM-16` and the `_private-` files carry the matter.
3. **Rewrite the dashes rather than swapping them.** Ruling 4. **The old page uses em dashes inside table cells as well as in prose**, and a table cell dash usually wants to become a comma or a full stop with the cell resplit. A hyphen swap would leave prose that reads wrong, which is the outcome the rule exists to prevent.

**A fourth, from CONTRADICTION 2: trim the links.** The old page carries a three-link Related block and an inline `[[people-roster]]`. Under the current page rules it gets two links at most.

**Everything else in this scope needs editing in place, not migrating.** The work is on this Brain's own pages: complete `counsel.md`, write the one-next-action rule into the operating manual, correct the Rillet spelling, add two ledger rows, move three PD rows to Resolved, refresh two stale counts, and fix three archive-pointing instructions.

### 5.4 The three files that most need Austin's decision

**1. `C:\Users\AustinBerk\Documents\Claude\Code\brain\CLAUDE.md`, and specifically its three rules of 2026-09-03.**

Ruling 2 already says the constitution does not merge, and that is not being re-opened. **But ruling 2 was made about the three-item ceiling, and the three rules added on 2026-09-03 are newer than the archived copy Austin's ruling was reasoning about.** Each has a named failure behind it, each is about how findings get built rather than how they get presented, and none conflicts with anything in this Brain. **This is the one place where "do not merge it" and "check what was lost" point in different directions, and only he can settle it.** The specific ask is one word on whether the three get written into `My Brain\CLAUDE.md`, and CLAUDE.md changes need his sign-off anyway.

**2. `C:\Users\AustinBerk\Documents\Claude\Code\brain\02-entities\people-roster.md`, for the counsel roster underneath it.**

Not the roster itself, which is already filed. **The question is `10-Business\outside-help\counsel.md`, which is missing Karen Doner entirely and asserts a gap on Zach Wallack's firm that two other pages in this Brain fill.** Completing it means writing four facts onto a page about outside legal relationships: Doner as employment counsel, Eckert Seamans as Wallack's firm, the Gunster attorneys on Belle Haven and Silver Breeze, and Hoke on Hunter Springs. **Three of the four are SINGLE-SOURCE from a road-trip document, and one of them is a conflict note about deal counsel sharing an office with a departing controller's brother.** That last one is not a filing decision.

**3. `C:\Users\AustinBerk\Documents\Claude\Code\brain\02-entities\karen-doner.md`.**

Ruling 5 settled where it goes. **What is not settled is how much of it goes.** The page is 5.4KB and roughly half of it is the Berman separation, hour by hour, including counsel's advice, the forensic review, the retaliation exposure and the severance benchmarks. **Rule 9 forbids the figures outright, so those are decided. The rest is a judgement about how much of a live personnel matter belongs on an outside-counsel page even in summary**, and `CM-16` closed on 2026-09-02, which changes the calculus. **The ask is whether her page names the Berman engagement at all, or only says employment counsel, engaged 2026-08-28.**

---

## Related

- `05-Inbox\vault-reconciliation\00-rulings.md`, Austin's five rulings that govern this reconciliation.
