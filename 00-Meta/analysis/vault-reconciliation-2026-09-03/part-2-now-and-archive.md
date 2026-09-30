# Vault reconciliation, part 2: `01-now/` and `99-archive/`

**What this is:** the disposition of every file in `C:\Users\AustinBerk\Documents\Claude\Code\brain\01-now\` and `\99-archive\`, plus the two scheduled-job skills and the eight published brief renders, checked row by row against this Brain's six registers and `99-Archive/`.

**Status:** current, 2026-09-03. Analysis only. Nothing was moved, edited or deleted. Governed by `05-Inbox/vault-reconciliation/00-rulings.md` and `CLAUDE.md` rules 10, 11 and 15.

**The one thing to read if you read nothing else.** `Claude\Code\brain\01-now\open-loops.md` is not a source that needs migrating. It is the **direct ancestor of `00-Meta/commitments.md`**, which was forked out of it on 2026-08-31 and has been maintained here ever since. Both files kept running for four more days, so they diverged in both directions. **Sixty-six of its sixty-nine rows are already tracked here with IDs.** Three are not, and one archive entry is genuinely missing.

---

## Summary table

### `01-now/` (17 files)

| File | Size | Disposition | One-line reason |
|---|---|---|---|
| `open-loops.md` | 141 KB | **SUPERSEDED** | Direct ancestor of `00-Meta/commitments.md`. 66 of 69 rows already carry `CM`/`KP`/`TD`/`PD` IDs here. Three row-level exceptions broken out below. |
| `albert-migration-risks.md` | 14 KB | **SUPERSEDED** | `10-Business/sharepoint/migration-risks.md` is the same document plus a provenance header plus a 2026-08-31 live-SharePoint correction. |
| `berman-function-extraction.md` | 8 KB | **SUPERSEDED** | `10-Business/people/_private-berman-function-extraction.md` is a strict superset. Rule 7 satisfied only by the NEW copy. |
| `catchup/PRIORITY-LIST.md` | 39 KB | **ALREADY THERE** | `99-Archive/2026-08-catchup/PRIORITY-LIST.md`. One substantive line newer in OLD, and that line is already live here as `TD-0389`. |
| `catchup/berman-journal-entries-thread.md` | 31 KB | **ALREADY THERE** | Byte-identical to `99-Archive/2026-08-catchup/berman-journal-entries-thread.md`. |
| `catchup/clickup.md` | 26 KB | **ALREADY THERE** | Byte-identical to `99-Archive/2026-08-catchup/clickup.md`. |
| `catchup/email-2026-07-26-to-08-10.md` | 26 KB | **ALREADY THERE** | Byte-identical to `99-Archive/2026-08-catchup/email-2026-07-26-to-08-10.md`. |
| `catchup/email-2026-08-11-to-08-25.md` | 34 KB | **ALREADY THERE** | Byte-identical to `99-Archive/2026-08-catchup/email-2026-08-11-to-08-25.md`. |
| `catchup/eod-2026-08-26.md` | 44 KB | **ALREADY THERE** | Byte-identical to `99-Archive/2026-08-catchup/eod-2026-08-26.md`. |
| `catchup/meetings-and-transcripts.md` | 43 KB | **ALREADY THERE** | Byte-identical to `99-Archive/2026-08-catchup/meetings-and-transcripts.md`. |
| `drafts/draft-zach-capex-reply.md` | 2.6 KB | **ALREADY THERE** | Byte-identical to `80-Finance/drafts/draft-zach-capex-reply.md`. Never sent, item closed, and the archive record says so. |
| `drafts/draft-dustin-lamberton.md` | 6.0 KB | **SUPERSEDED** | `60-Communities/drafts/draft-dustin-lamberton.md` is larger and was touched 2026-09-02. |
| `drafts/draft-it-credential-rotation.md` | 2.3 KB | **SUPERSEDED** | `10-Business/sharepoint/drafts/draft-it-credential-rotation.md` is larger and was touched 2026-09-01. |
| `drafts/draft-jon-clearing-agenda.md` | 9.2 KB | **ALREADY THERE** | `10-Business/eos/drafts/draft-jon-clearing-agenda.md`, same content plus header. |
| `drafts/drafts-today.md` | 6.5 KB | **ALREADY THERE** | Filed here as `10-Business/eos/drafts/2026-08-29-drafts-index.md`, byte-for-byte the same size. |
| `drafts/draft-albert-migration-handoff.md` | 6.7 KB | **ALREADY THERE** | `10-Business/sharepoint/drafts/draft-albert-migration-handoff.md`, same content plus header. |
| `drafts/jon-decision-items-extracted.md` | 30 KB | **ALREADY THERE** | `10-Business/eos/drafts/jon-decision-items-extracted.md`, same content plus header. |

### `99-archive/` (7 files)

| File | Size | Disposition | One-line reason |
|---|---|---|---|
| `american-ma-settlement-option-1.md` | 6.1 KB | **MIGRATE** | **The one genuine archive gap.** No counterpart anywhere in `My Brain/99-Archive/`. It is the record of Austin's own 2026-09-03 ruling. |
| `berman-boa-jpm-wire-62325.md` | 2.0 KB | **ALREADY THERE** | `99-Archive/2026-08-closed/`. Differs only in rewritten internal paths. |
| `boa-six-account-closures.md` | 2.5 KB | **ALREADY THERE** | `99-Archive/2026-08-closed/`. Paths rewritten, including the `_private-` Berman link. |
| `email-george-about-skills.md` | 2.3 KB | **ALREADY THERE** | `99-Archive/2026-08-closed/`. Paths rewritten. |
| `high-pace-chase-14400-monson-lot19.md` | 2.0 KB | **ALREADY THERE** | `99-Archive/2026-08-closed/`. One path line differs. |
| `jadian-jref1-litigation-update.md` | 2.2 KB | **ALREADY THERE** | `99-Archive/2026-08-closed/`. Paths rewritten. This is the rule 11 precedent file. |
| `zach-retaining-wall-40k-capex.md` | 3.2 KB | **ALREADY THERE** | `99-Archive/2026-08-closed/`. Paths rewritten. |

### Added scope: skills and published briefs

| File | Size | Disposition | One-line reason |
|---|---|---|---|
| `.claude/skills/morning-brief/SKILL.md` | 9.1 KB | **SUPERSEDED** | `95-Agents/morning-brief.md` is the ported, vault-native version and says so on its face. **But see the live-job warning below.** |
| `.claude/skills/weekend-pulse/SKILL.md` | 16 KB | **SUPERSEDED** | `95-Agents/weekend-pulse.md`. Same. |
| `06-reference/brief-2026-09-03.html` | 36 KB | **MIGRATE** | Only render with no counterpart here, and it carries four of Austin's own dispositions. Three landed here independently; one did not. |
| `06-reference/brief-2026-08-31.html` | 35 KB | **DISCARD** | This Brain rendered its own 08-31 brief. Two divergent published artefacts for one day; keep the one built against the system of record. |
| `06-reference/brief-2026-09-01.html` | 27 KB | **DISCARD** | Same. `99-Archive/2026-09-briefs/brief-2026-09-01.html` differs and is the vault-native render. |
| `06-reference/brief-2026-09-02.html` | 27 KB | **DISCARD** | Same. |
| `06-reference/brief-2026-08-27.html` | 26 KB | **ALREADY THERE** | Byte-identical to `99-Archive/2026-08-briefs/brief-2026-08-27.html`. |
| `06-reference/brief-2026-08-28.html` | 27 KB | **ALREADY THERE** | Byte-identical. |
| `06-reference/brief-2026-08-29.html` | 30 KB | **ALREADY THERE** | Byte-identical. |
| `06-reference/weekend-pulse-2026-08-28.html` | 78 KB | **ALREADY THERE** | Byte-identical to `99-Archive/2026-08-briefs/weekend-pulse-2026-08-28.html`. |
| `06-reference/daily-readout-2026-08-26.html` | 15 KB | **ALREADY THERE** | Byte-identical. |

**Counts.** ALREADY THERE 20 · SUPERSEDED 6 · MIGRATE 2 · DISCARD 3 · CONFLICT 0 at file level, 4 at row level. **No file in scope is DISCARD on grounds of having no value; the three DISCARDs are duplicate published renders.**

---

## `open-loops.md`, row by row

**VERIFIED.** `Claude\Code\brain\01-now\open-loops.md` holds **69 rows**: 25 numbered Active items, 12 Held bullets, 32 Recently closed entries.

### The provenance, because it changes what the file is

`My Brain\00-Meta\commitments.md` opens `# Open Loops`, carries the same **Rules** paragraph verbatim, the same **"Note on items 7 and 8, added 2026-08-26 evening"** block, and this line at the top:

> **Status:** needs review - content is as of 2026-08-29; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`.

**VERIFIED.** So `commitments.md` is `open-loops.md`, forked here on 2026-08-31 and maintained since. Then both halves kept running: OLD's header says *"Last reviewed: 2026-09-03"*, NEW's says *"Last reviewed: 2026-09-02"* with 2026-09-03 additions on individual rows. **Neither is a subset of the other.**

### Active items 1 to 25

| OLD item | Where it lives in this Brain | Status here |
|---|---|---|
| 1. Jadian known-wrong text, DR-035 | `CM-01` | **CLOSED 2026-09-01** |
| 2. Security exposure on corporate storage | `CM-02`, plus `10-Business/sharepoint/a2z-utility-logins-exposure.md` | **RISK ACCEPTED 2026-09-01** |
| 3. Jon Wyss binding constraint | `CM-03` | **UNBLOCKED 2026-09-01, CLOSED 2026-09-02** |
| 4. Migration risk brief to Albert | `CM-04` | **CLOSED 2026-09-01** |
| 5. Lamberton Lake LP syndication records | `CM-05`, and `KP-0067`, `CM-29`, `PD-38` | **CLOSED 2026-09-02** |
| 6. Berk Inc entity map | `CM-06`, `TD-0398` | Open, reframed 2026-09-01 |
| 7. Lucky Clover armed resident | `CM-07`, `KP-0006`, `TD-0329` | **CLOSED 2026-09-01** on Austin's word |
| 8. Great Oaks boil water | `CM-08`, `KP-0007`, `TD-0330` | **CLOSED 2026-09-01** on Austin's word |
| 9. Email George about skills | `CM-09` | **CLOSED 2026-08-27** |
| 10. Belmart bank package | `CM-10`, `TD-0489`, `TD-0499`, `TD-0500` | Open |
| 11. Hensdale Club application | `CM-11` | Open |
| 12. Road-trip Excel tracker | `CM-12` | **CLOSED 2026-09-01** |
| 13. Intercompany AR/AP reconciliation | `CM-13` | Open, **reopened 2026-09-01, due 2026-09-30** |
| 14. License and Permit transition | `CM-14`, `KP-0011` | Open |
| 15. Floorplan double-counting | `CM-15`, `TD-0308`, `TD-0343` | Open |
| 16. Berman exit | `CM-16`, `PD-02`, `TD-0327` | **CLOSED 2026-09-02** |
| 17. E&O / D&O binder $43,090.21 | `CM-17`, `TD-0480` | Open |
| 18. A2Z ND Portfolio Partners equity | `CM-18`, `TD-0312` | Open |
| 19. Royal Oaks nine missing titles | `CM-19`, `TD-0263`, `KP-0033` | Open |
| 20. American MA settlement | `CM-20` | **Open here, CLOSED in OLD. See CONFLICT 1.** |
| 21. Fund II wind-down documents, Woods Oviatt | **Nowhere.** `KP-0070`/`KP-0071` are adjacent but different. | **See MIGRATE 1.** |
| 22. SharePoint out of storage | Folded into `CM-04` by an explicit note | **See CONFLICT 2.** |
| 23. Kippy Brokaw approximately $961K | `CM-24`, `KP-0055`, `TD-0368`, `TD-0436` | Open. Renumbered. |
| 24. Uniti / SAM leasing agent | `TD-0376` (closed), `TD-0377`, `TD-0392` to `TD-0394`, `TD-0472`, `PD-23`, `KP-0059`, and the page `10-Business/vendors/uniti-agent-mailbox.md` | Open, distributed |
| 25. "Rita" voicemails | `CM-26` | **See CONFLICT 3. This Brain is ahead.** |

**Read the numbering carefully, because it is a trap.** `CM-01` to `CM-20` correspond exactly to OLD items 1 to 20. **From 21 the two files diverge and the numbers no longer mean the same thing.** `CM-21` here is August payroll allocations, `CM-22` is the Geiger House PSA, `CM-23` is the Auburn MA rent-control meeting, `CM-25` is Bedrock Fund II LP obligations. None of those exist in OLD at all. Anyone reading a cross-reference like *"item 22"* across the two vaults will land on the wrong row.

### Held, 12 bullets

**ALL 12 ALREADY THERE or resolved.** Sampled and checked:

- The standing rule about the `.eml` "DRAFT, open and hit send" files, set by Austin 2026-09-03. Present in OLD only as a Held bullet. **INFERRED that this belongs in `CLAUDE.md` rather than a register**, since it is a sweep rule, not an item. Worth Austin's eye.
- The Belle Haven permitted-site-count correction, 91 against the county's 87. **ALREADY THERE** as `PF-0069`, and on `60-Communities/belle-haven.md` line 65, both dated 2026-08-26.
- `/sites/ParakeetHome` against `/sites/ParakeetHomes`. **ALREADY THERE** as `KP-0009`.
- Community name reconciliation, approximately 18 mismatched assets. **ALREADY THERE** in `10-Business/sharepoint/migration-risks.md` section 7, with a 2026-08-31 live correction OLD does not have.
- The 17.56 GB of redundant PCA dumps, the taxonomy tracker figures, the three invisible sync libraries, `/sites/UserArchive`, the two undistinguished legal sites, the empty-shell inventory and the unbuilt usage tracker are all reproduced verbatim in `00-Meta/commitments.md` lines 395 to 402 and in the storage-inventory pages.

### Recently closed, 32 entries

**31 of 32 ALREADY THERE.** The Recently closed section of `00-Meta/commitments.md` carries the same entries with the same dates, including the 2026-08-29 retraction of the Jadian check-in closure and the A&A Development upgrade to VERIFIED. **The one exception is the 2026-09-03 American Option 1 closure**, which is CONFLICT 1 and MIGRATE 2 below.

---

## CONFLICTS

### CONFLICT 1: American MA settlement. Closed in OLD, open here, and both are partly right.

**OLD**, `Claude\Code\brain\01-now\open-loops.md` line 284:

> `### 20. American (Massachusetts) rent-increase settlement — **CLOSED 2026-09-03: Option 1, agreed**`

and on the same row:

> **CLOSED 2026-09-03 — Option 1.** Austin's disposition, direct: **American is agreed to move forward with Option 1** [...] and ends a path decision the ledger had carried as open since 2026-08-29.

**NEW**, `My Brain\00-Meta\commitments.md` line 186:

> `### `CM-20` 20. Massachusetts class settlement, American and Whispering Pines MA — $400,000 agreed, the rent schedule is the only open issue`

and on the same row, line 188:

> **2026-09-02, ADVANCED, and the path question is now answered in practice rather than by ruling.**

and line 190:

> **Path 1 is being executed without a recorded ruling from Austin, and that is worth naming rather than smoothing.**

**What I believe, and it is a split.** **The two vaults are describing different questions and each has a fact the other lacks.**

- **OLD is right that the path decision is closed.** Austin ruled directly on 2026-09-03. `CM-20` still says *"without a recorded ruling from Austin"*, and that sentence became false the next morning. **This Brain is one day stale on the ruling.**
- **NEW is right that the matter is open, and it holds far more of the substance.** OLD has no `$400,000`, no Whispering Pines MA, no `$575`/`$615`/`$1,315` lease rates, and nothing about the 2028-12-01 credit expiry that `CM-20` calls *"the entire remaining gap"*. OLD's version of this item is thinner by a wide margin.

**Recommendation: do not close `CM-20`.** Add Austin's 2026-09-03 ruling to it as the path-decision closure, keep the row open on the rent schedule, and file `american-ma-settlement-option-1.md` as the archive record of the decision rather than of the matter. **Migrating OLD's row wholesale would delete the $400,000 settlement from this Brain**, which is the more expensive error of the two.

### CONFLICT 2: SharePoint out of storage. A live daily-escalating blocker in OLD, deliberately not surfaced here.

**OLD**, `open-loops.md` line 331, is a full Active item, item 22, with four consecutive daily notices tracked and the number climbing: 6,531 GB on 08-31, 6,533.22 on 09-01, 6,537.4 on 09-02, against a 2,394 GB quota. Next action: *"decide buy or purge and hand it to IT today."*

**NEW**, `My Brain\00-Meta\commitments.md` line 27:

> **Not re-raised, deliberately.** The SharePoint out-of-storage alert (6,537.4 GB against 2,394 GB) is the same wall as 2026-08-10 and is Albert's under item 4.

**And `CM-04` is CLOSED 2026-09-01.** So the item was folded into a commitment that then closed, and there is **no open row in any of the six registers carrying the storage quota**. A grep of all six for `6,531`, `2,394`, `quota` and `out of storage` returns the header note above and nothing else.

**What I believe: this needs Austin's ruling, and it is the one row here I would not decide for him.** The disposition is defensible, it is his own framing, and rule 11 forbids me re-raising it. But the mechanism is worth naming: **a tenant at 273% of licensed capacity, still climbing, is now recorded only in a "not re-raised" note under a closed commitment.** If it was deliberately accepted, it belongs in `00-Meta/open-items.md` as an accepted risk with a `KP` ID, the way `CM-02` was handled. If it was folded into Albert's scope, `CM-04` closing took it with it.

### CONFLICT 3: "Rita". OLD says do not guess who she is. This Brain already knows.

**OLD**, `open-loops.md` line 382, item 25:

> **She has no email footprint.** [...] **Do not guess who she is or what entity this is.** [...] **Next action**: call her.

**NEW**, `My Brain\00-Meta\commitments.md` line 321:

> `### `CM-26` 26. Ridaa Murad, 33% partner in Bedrock Group, is chasing Austin for financial statements`

> **IDENTIFIED 2026-09-02 by Austin, hours after this row was opened as an unknown caller.** His words: *"Voicemail is from Ridaa Murad, 33% partner in Bedrock Group."*

**This Brain is right and it is a day and a half ahead.** `CM-26` also carries the written half that OLD never found: Murad's 2026-08-26 dataroom demand with a 48-hour deadline that expired 2026-08-28, sourced to the a2zcp mailbox, plus `TD-0479` and `TD-0478`. **OLD's item 25 is SUPERSEDED, and migrating it would re-open a resolved identity question against a 33% partner.** That is exactly the rule 11 failure mode.

### CONFLICT 4: 21st Mortgage consumer loans. Ruled in OLD, still parked here.

**OLD**, `open-loops.md` inside item 15, Austin's 2026-09-03 disposition:

> **Austin's disposition, 2026-09-03: *"21st, needs to be executed today."*** **VERIFIED (principal, direct).** Not a decision to weigh, a green light to send, today.

**NEW**, `My Brain\00-Meta\parked-decisions.md` line 103:

> `PD-35` | **Formal green light on the 21st Mortgage consumer loan structure, and whether the $250,000 reserve stays on 21st's side.**

**I believe OLD on the green light and NEW on the reserve.** Austin ruled the green light on 2026-09-03; `PD-35` should not still be waiting on it. **But `PD-35` bundles a second question OLD does not have at all**, the $250,000 reserve, and Austin's *"needs to be executed today"* does not obviously answer it. **Recommendation: split `PD-35`.** Close the green-light half on Austin's 2026-09-03 words, keep the reserve half parked, and give the survivor its own next `PD` number rather than reusing `PD-35` for a narrowed question.

### A fifth, minor: the Balocco withdrawal did not reach this Brain.

**OLD** records Austin withdrawing a reading on 2026-09-03: J. Balocco Jr. is Brokaw's **transaction** attorney, not his litigator, so Sunstone looping him onto the Royal Oaks thread is normal deal counsel and not the adverse matter bleeding into the warm channel.

**NEW** carries the un-withdrawn framing at `00-Meta/daily-close/2026-09-02.md` line 39 and nowhere else. **No register row asserts the risk**, so nothing here is wrong today. But if a future sweep reads that close file, the withdrawn reading is what it will find. **One line on `CM-19` or `CM-24` fixes it.**

---

## MIGRATE

### MIGRATE 1: OLD item 21, the Fund II wind-down documents. Genuinely absent, and it is the real find.

**VERIFIED absent.** A grep of the whole of `My Brain` for `Valley View`, `Green Spot`, `reconvey`, `closing binder` and `Cornerstone ALR` returns **only** two storage-inventory folder listings and one archived ClickUp row. **No register row, no page, no archive entry.** Christopher Hoke of Woods Oviatt Gilman appears nowhere. `TD-0495` is a Woods Oviatt **billing** reconciliation and is a different matter.

`KP-0070` and `KP-0071` are the nearest neighbours and they are **not** this item. They say the Fund II wind-down record base is being built as a new destination and that a wind-down programme has been running since April 2026 that this Brain did not know about. **Neither names the three missing releases.**

**What is missing, from `Claude\Code\brain\01-now\open-loops.md` line 316:**

1. **Green Spot**, recorded termination of the Cornerstone ALR. A draft circulated January 2020, no recorded copy ever received, property sold May 2020.
2. **Green Spot**, confirmation the escrow for the outstanding deeds of trust was released and the liens cleared before the May 2020 sale. Hoke answered that as seller Parakeet would not have received copies of releases recorded after closing.
3. **Valley View**, recorded reconveyance of the 2018 Cornerstone deed of trust. **Hoke flagged this one in red himself.** Chicago Title found it still of record in early 2021, had the original release in November 2021, and *"should have recorded it in connection with the closing."*

**Why this is the sharp one.** Item 3 is a **2018 deed of trust that may still sit unreleased of record** on an asset inside the fund being wound down. Austin's own words on 2026-08-30 15:51 ET: *"Think I dropped the ball here on the follow up."* Hoke answered all three on 2026-08-11; Austin acknowledged 08-14 and then went sixteen days quiet. A call was held 2026-09-01 11:00 to 11:30 ET with Hoke and David DiMarco.

> **SUPERSEDED BY AUSTIN, 2026-09-03. `CM-31` was not opened and should not be.** His ruling: *"Chris is getting the documents together. anything needed can be held until we get those and reassess."* **The items are held, not tracked.** The hold and its lift condition are recorded on [[80-Finance/fund-reporting/bedrock-fund-ii-winddown]] and noted on `CM-25`. **`CM-31` therefore remains unissued and is the next available commitment number.** The recommendation below is left in place unedited, per rule 5, because superseding a recommendation is not the same as pretending it was never made.

**Where it goes.** This is a commitment, not a finding. **`00-Meta/commitments.md` as a new row taking the next number, `CM-31`.** Guardrail 6 applies, since it touches the Fund II wind-down. Three to-dos come off it, taking the next three `TD` numbers in file order:

- Chase the Valley View reconveyance and establish whether the 2018 deed of trust is still of record.
- Confirm what the 2026-09-01 Hoke call actually settled. **Nothing in this Brain records its outcome.**
- Settle where a closing-binder library lives, which is where this collides with CONFLICT 2.

**It also has a cross-reference worth keeping**: `CM-05` (Lamberton LP syndication records) closed 2026-09-02, and this is the same class of possibly-single-copy wind-down record. `CM-05` closing does not close this.

**Why it fell through the crack, and the coordinator's read is right.** OLD's numbering put it at item 21. This Brain assigned `CM-21` to August payroll allocations on 2026-08-31, the same day the fork happened. **The row had no ID at fork time**, so there was nothing to collide, and the position it would have taken was filled by something else. That is rule 15's argument made by accident.

### MIGRATE 2: `99-archive/american-ma-settlement-option-1.md`. The only missing archive entry.

**VERIFIED.** `My Brain\99-Archive\2026-08-closed\` holds six of the seven OLD archive files. **The seventh has no counterpart anywhere under `My Brain\99-Archive\`.** It was written 2026-09-03 at 10:53, after the folder here was last touched on 2026-08-30.

**This is load-bearing under rule 11.** It is the written record of Austin's own direct disposition. Without it, the next sweep that reads `CM-20` will find *"Path 1 is being executed without a recorded ruling from Austin"* and has a live route to re-raising a path decision he settled. **The rule 11 precedent, Toby Nelson, is one of the six files that did make it across.**

**Where it goes.** `99-Archive/2026-09-closed/` as a new dated folder, or `99-Archive/2026-08-closed/` if a single closed-items folder is preferred. **Not as a `CM-20` closure**, per CONFLICT 1: it archives the decision, not the matter.

### MIGRATE 3, conditional: `06-reference/brief-2026-09-03.html`.

Its four dispositions, checked one by one:

| Disposition in the 09-03 brief | Reached this Brain? |
|---|---|
| Item 20 was misnamed Belle Haven for five briefs; it is American in Massachusetts | **Yes.** `CM-20` was renamed here independently on 2026-08-31 and carries the full provenance. |
| Item 20 CLOSED, Option 1 agreed | **No.** CONFLICT 1. |
| Item 19 reading withdrawn: Balocco is transaction counsel | **No.** Minor, see above. |
| 21st consumer loans: *"needs to be executed today"* | **Partly.** `PD-35` exists but is still parked. CONFLICT 4. |

**Also in it and worth checking before the file is dropped**: two sweep rules Austin adopted the same morning, that a matter's name comes from a primary document and never from a subject line, and that names and characters come from documents and not containers. **The first is already in `CLAUDE.md`. INFERRED that the second is not**, and it is the rule that killed the "active Belle Haven legal matter" error. That belongs in front of Austin as a possible `CLAUDE.md` addition, which needs his sign-off.

**Disposition: MIGRATE the three dispositions as register edits, then DISCARD the render.** The HTML itself is a published artefact of a superseded pipeline. Keeping it invites a future sweep to read a brief built against the retired archive.

---

## What would violate this Brain's rules if migrated as-is

### The dash problem is worse than a find-and-replace, per ruling 4

`open-loops.md` alone carries **384 em dashes and 34 en dashes**. Ruling 4 is explicit: rewrite the sentence, do not swap the character.

**On the three rows that actually migrate, this is real work and not cosmetic.** Item 21's text is dash-heavy in exactly the way the rule targets. One example, the row's own heading:

> `### 21. Fund II wind-down documents — three missing releases, a closing-binder library that does not exist, and Austin flagged the lapse himself`

That em dash is doing the work of a colon in a heading, so the heading needs recasting rather than a hyphen dropped in. And inside the row:

> Hoke's answer: the Pacific Premier Bank DOT and ALR were paid off at closing and shown on the settlement statement; **as seller, Parakeet would not have received copies of releases recorded after closing.**

That one is already clean. The dashes are not evenly distributed, so **the pass has to be read line by line rather than run**. On a 141 KB file that is the argument for migrating three rows by hand rather than the file.

**Two notes on the same rule that cut the other way.** First, `My Brain\00-Meta\commitments.md` itself carries em dashes throughout, inherited from this same ancestor. Second, `My Brain\10-Business\people\_private-berman-function-extraction.md` line 33 carries an **en dash** in *"the 7/27–7/29 intercompany journal-entry exchange"*. **The rule is being broken inside this Brain already**, by files that came across on 2026-08-31 before ruling 4 existed. Worth Austin knowing, because a dash pass scoped only to incoming files leaves the existing breach in place.

### Register rows with no IDs

**Every row in `open-loops.md` is ID-less.** OLD used positional numbers 1 to 25, which is the exact anti-pattern `00-Meta/id-conventions.md` records as the reason IDs were written into the markdown on 2026-09-02. **The three rows that migrate take the next number in their register and nothing gets renumbered:**

- OLD item 21, the Fund II wind-down documents, becomes **`CM-31`**. `CM-30` is the highest in use, VERIFIED by scanning every code span in `00-Meta/`.
- Its three to-dos become **`TD-0529`, `TD-0530` and `TD-0531`**. `TD-0528` is the highest in use.
- The `PD-35` split in CONFLICT 4 needs a new `PD` number for the surviving reserve question, not a reused one. **`PD-42`**, since `PD-41` is the highest in use.

**The rest of the register high-water marks, recorded so a later pass does not have to recount them:** `KP-0074`, `PF-0465`, `PR-0040`. **Note that `00-Meta/id-conventions.md` is stale on every one of these**, since it still reports the 2026-09-01 ranges. That is a small finding of its own and it belongs on `00-Meta/open-items.md` if it is not already there.

**Nothing else in scope becomes a register row.** The archive entry is an archive entry, the drafts are already filed as drafts, and the catchup sweeps are already archived.

### Personnel content outside `_private-` files

**Clean, with one caveat.** `berman-function-extraction.md` sits at `01-now/berman-function-extraction.md` in OLD with no `_private-` prefix and no rule 7 header. **This Brain fixed both**, which is the main reason NEW is the more current copy. **The caveat is that OLD item 16 in `open-loops.md` carries substantial personnel content in an unprotected file**: Demetria's *"Lets surprise him and make the HH a Farewell party"*, the note-to-file on a second employee, Moe's *"he is useless to me"* on a named new hire, and the compensation construction of four months' pay plus COBRA plus bonus. **`CM-16` closed 2026-09-02 so none of it needs migrating.** It is a reason not to file `open-loops.md` here as a page even for provenance, because doing so would put unguarded personnel material and a compensation figure into a folder that is not `_private-`. Rules 7 and 9 both bite.

---

## The operational finding that is not a file disposition

**The two scheduled jobs still point at the retired vault, and this is why item 21 was invisible.**

`My Brain\95-Agents\morning-brief.md` says so itself:

> **Ported into this Brain 2026-08-31** from the Claude Code vault at `Documents/Claude/Code/brain/.claude/skills/morning-brief/`. Paths and house rules rewritten for this vault. **The original still runs on its own schedule in the other vault, so expect both to w[rite]**

**VERIFIED, and the evidence is in the file listings.** `Claude\Code\brain\06-reference\brief-2026-09-03.html` was written at 11:05 on 2026-09-03. `Claude\Code\brain\01-now\open-loops.md` was written at 11:04 the same morning. **The retired vault was being written to today.** And this Brain has no 09-03 brief at all: `99-Archive\2026-09-briefs\` holds 09-01 and 09-02 only.

**The consequence, and it is the coordinator's read confirmed.** The OLD morning-brief skill diffs against `Claude\Code\brain\99-archive\`, not against `My Brain\99-Archive\` and `00-Meta\commitments.md`. So for four days there have been **two ledgers, two archives and two brief pipelines**, each blind to the other's closures. That is how item 21 stayed off every register here while appearing in an OLD brief, and how `CM-20` still says no ruling exists when one was published in an artefact the same morning.

**This is not fixed by filing anything.** Until the OLD `.claude/skills/` directory is retired or repointed, every day adds a fresh divergence to reconcile. **Three genuinely different paths, per `CLAUDE.md`:**

1. **Retire the two OLD skills outright and accept a gap.** Cheapest, one action. **What stays broken:** any scheduled trigger that fires them errors rather than falling through to `95-Agents/`, and Austin loses the brief on whichever day that happens. Wrong choice if the OLD skills are what the scheduler actually invokes.
2. **Repoint the two OLD `SKILL.md` files at this Brain's paths and registers, leaving them where the scheduler finds them.** Fixes the mechanism so the divergence stops recurring, and it is the smallest change to a working pipeline. **What stays broken:** the skill definition then lives in a retired vault, so the file map and the running job disagree, which is the same defect one layer down. Wrong choice if the OLD vault directory is about to be deleted.
3. **Move the skill definitions into `My Brain\90-Skills\` and point the scheduler at the new location.** Rebuilds from the system of record. **What stays broken:** nothing structurally, but it needs whoever owns the scheduler, and `90-Skills/` currently holds no brief skill at all, so `95-Agents/morning-brief.md` and a new `90-Skills` entry would need reconciling first.

**Recommended: 3, with 2 as the same-day stopgap.** 1 loses a brief on a day nobody will predict, and Austin reads the brief. 2 alone leaves the running definition inside a vault the whole project is retiring, which is the defect being fixed, restated. **3 grafts on what 2 gets right by doing the repoint first and the move second, so no morning is missed.** The condition that makes 3 wrong: if the scheduler cannot be edited by anyone available today, then 2 is not a stopgap, it is the answer.

---

## Related

- `05-Inbox/vault-reconciliation/00-rulings.md` - Austin's five rulings, applied throughout
- `00-Meta/id-conventions.md` - the ID scheme MIGRATE 1 depends on
