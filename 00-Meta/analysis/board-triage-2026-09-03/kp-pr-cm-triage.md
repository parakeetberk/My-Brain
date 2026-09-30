# Triage: known problems, promises, commitments

**Scope.** The last three of the six registers, triaged 2026-09-03. 74 `KP-nnnn` from `C:\Users\AustinBerk\Documents\My Brain\00-Meta\open-items.md`, 40 `PR-nnnn` from `C:\Users\AustinBerk\Documents\My Brain\00-Meta\promises.md`, 30 `CM-nn` from `C:\Users\AustinBerk\Documents\My Brain\00-Meta\commitments.md`. 144 items. **All three markdown files were read in full and are the authority for every claim below.** `board.json` was used only for cross register duplicate detection and for the Berman sweep, and where the two disagree the markdown wins and the disagreement is reported.

**No register was edited.** This file proposes; Austin disposes. No ID was renumbered or recycled, per [[CLAUDE]] rule 15.

**Personnel.** `CM-16`, `PD-02` and the severance and equity terms inside them are a personnel matter, see the private assessment file. No individual's compensation is reproduced here, per hard rule 9.

---

## Counts

### By tier

| Tier | Known problems | Promises | Commitments | Total |
|---|---|---|---|---|
| **P0 Exposure** | 29 | 2 | 12 | **43** |
| **P1 Dated** | 2 | 1 | 2 | **5** |
| **P2 Blocking** | 20 | 19 | 3 | **42** |
| **P3 Value** | 14 | 13 | 1 | **28** |
| **P4 Noise** | 9 | 5 | 12 | **26** |
| Total | 74 | 40 | 30 | **144** |

**Read the P0 column before anything else, because 43 of 144 is not a credible tier distribution and the reason it is not is the finding.** 29 of the 43 sit in `KP`, and 21 of those 29 fall into just two clusters: **eleven on Bedrock Fund II, A2Z and the legacy tenant** (`KP-0008`, `KP-0038`, `KP-0058`, `KP-0062`, `KP-0063`, `KP-0064`, `KP-0067`, `KP-0068`, `KP-0072`, `KP-0073`, `KP-0074`), and **eight on compliance and SOP text** (`KP-0001`, `KP-0002`, `KP-0005`, `KP-0011`, `KP-0013`, `KP-0017`, `KP-0018`, `KP-0022`). The remaining ten split across the rehab and WIP money (`KP-0003`, `KP-0041`, `KP-0044`, `KP-0047`, `KP-0057`), the Kippy and Massachusetts counterparties (`KP-0033`, `KP-0034`, `KP-0055`) and two credential and insurance rows (`KP-0059`, `KP-0065`). **This is one wind down and one unfinished process library wearing 21 badges, not 21 independent fires.** Treating them as 21 is what makes the register unreadable.

**P1 is only 5 items, and that is the most useful number on this page.** A real external date is rare here. Almost every date on the board is one Austin set himself on 2026-09-02, which by the tier definition is not P1. The five genuine outside clocks are `KP-0012`, `KP-0036`, `PR-0040`, `CM-22` and `CM-23`, and the hardest of them is not on any of those rows: it is **2026-09-15**, Onyx Holdings' own corporate filing deadline, recorded inside `CM-25`.

### By agent-ability

| Verdict | Known problems | Promises | Commitments | Total |
|---|---|---|---|---|
| `AGENT NOW` | 7 | 5 | 8 | **20** |
| `AGENT WITH A HUMAN CHECK` | 38 | 12 | 9 | **59** |
| `HUMAN ONLY` | 29 | 23 | 13 | **65** |

**Every `AGENT NOW` is a closure, a retirement or a self contained sweep.** Nothing that reaches a counterparty, a resident, a lender or an LP is agent-able at all, because guardrails 5, 6, 7 and 8 forbid the action rather than the analysis. **The promises register is the least agent-able of the three**, 23 of 40 `HUMAN ONLY`, and that is correct: a promise closes when a named person is told, and an agent cannot be the one who tells them.

---

## The David Berman list, settled

**The two prior triages said eleven and twelve. Both are wrong, and both are wrong for the same mechanical reason.** They counted `board.json`'s `owner_short` field. That field is an exact match on the string `David Berman`, and it returns exactly **eleven** rows: `KP-0003`, `TD-0005`, `TD-0192`, `TD-0193`, `TD-0194`, `TD-0205`, `TD-0372`, `TD-0461`, `PF-0015`, `PF-0024`, `PF-0030`. **VERIFIED** by query against `board.json`. The twelfth in the other count is one of the joint ownership rows below or `KP-0001`, which is closed; the count cannot be reproduced exactly because the field does not carry joint owners.

**Two defects in that field make eleven an undercount.**

1. **`owner_short` drops the second name on a joint ownership row.** `TD-0198` reads `Natalie Magurne with David Berman (GL codes)` and resolves to Natalie. `TD-0327` reads `Austin with David Berman` and resolves to Austin. `TD-0274` reads `Accounting (Berman, Bennett, Moe)` and resolves to Accounting. Work is still routed to him on all three.
2. **`board.json` has a column shift on the eighteen newest to-dos.** `TD-0497`, `TD-0498`, `TD-0503` to `TD-0512` and `TD-0524` to `TD-0529` all carry the priority token in the `desc` field and their real owner string in `extra`. **VERIFIED**: `TD-0528`'s owner is `David Berman with Albert` in the markdown and `Albert Gano` in `board.json`. **So any Berman count taken from the board's owner field is blind to precisely the rows written on 2026-09-03**, which are the ones that matter most, because they are the new ones.

### Definitive list: 17 open rows across all six registers route work to David Berman

Owner strings are quoted from the markdown, which is authoritative. **VERIFIED**, each row read in place.

| # | ID | Register | Owner string as written | Note |
|---|---|---|---|---|
| 1 | `KP-0003` | Known problems | `David Berman` | Accounting 30 to 45 days in arrears. **Sole owner of a Critical finding.** |
| 2 | `TD-0005` | EOS to-dos | `David Berman - the source itself says this needs one look from accounting` | Hunter Springs MHC double count. |
| 3 | `TD-0192` | EOS to-dos | `David Berman with Austin Berk` | SOP 302 lender deadline consequence. |
| 4 | `TD-0193` | EOS to-dos | `David Berman` | Build the Repo Tracker named in SOP 302. |
| 5 | `TD-0194` | EOS to-dos | `David Berman with Leslie Croft` | SOP 302 Data Pack Template. |
| 6 | `TD-0198` | EOS to-dos | `Natalie Magurne with David Berman (GL codes)` | Missed by the board field. |
| 7 | `TD-0205` | EOS to-dos | `David Berman with Natalie Magurne` | **Remove the lender's wire instructions from SOP 302. See the contradiction section: `KP-0001` says this is done.** |
| 8 | `TD-0274` | EOS to-dos | `Accounting (Berman, Bennett, Moe)` | Missed by the board field. |
| 9 | `TD-0327` | EOS to-dos | `Austin with David Berman` | Ramp charge coding agent. Missed by the board field. |
| 10 | `TD-0372` | EOS to-dos | `David Berman with Citrin Cooperman` | The Oregon notice on Bedrock MHC Fund II. |
| 11 | `TD-0461` | EOS to-dos | `David Berman owns the thread` | 21st Mortgage inventory confirmation. |
| 12 | `TD-0504` | EOS to-dos | `Austin with Berman` | **Raised 2026-09-03.** Missed by the board field. |
| 13 | `TD-0527` | EOS to-dos | `Austin Berk with David Berman` | **Raised 2026-09-03.** Missed by the board field. |
| 14 | `TD-0528` | EOS to-dos | `David Berman with Albert` | **Raised 2026-09-03. He is the named primary.** Missed by the board field. |
| 15 | `PF-0015` | Property follow-ups | `David Berman` | Journal entries lacking descriptions. |
| 16 | `PF-0024` | Property follow-ups | `David Berman` | **Duplicate of `KP-0003`.** |
| 17 | `PF-0030` | Property follow-ups | `David Berman` | Utilities and permits described as a black box. |

**Three rows name him without routing work to him and are correctly excluded**: `TD-0253` and `CM-21` (owner Austin, he set the deadline), and `PF-0332` (unassigned, he is the sender of the question). **Two rows that name him are closed**: `KP-0001` and `CM-21`. **One row is about him rather than for him**: `PD-02`, owner Austin, which is a personnel matter, see the private assessment file.

### The finding inside the finding

**Three of the seventeen were created on 2026-09-03, today.** `TD-0504`, `TD-0527` and `TD-0528` all came out of the BMHCII archive audit, and `TD-0528` names him as the primary owner of opening and classifying 179 subscription files. **The instruction is to route nothing new to him, and the board did exactly that three times today**, in the same pass that produced this triage series. **INFERRED** as to cause, and the likely cause is benign: the audit needed a controller and he is the controller of record. **The consequence is not benign.** `TD-0528`'s output is the per investor completeness matrix that a securities examiner and Ridaa Murad both ask for (`KP-0072`, `KP-0073`), so it is the single worst piece of work to hand to someone who will not be here to finish it.

**`TD-0372` is the one to move first regardless of the exit.** An Oregon state notice on a fund in wind down, received in the mail by the departing controller, attachment never read, contents unknown. If it carries a date, nobody knows what the date is.

---

## Cross register contradictions and duplicates

`TD-0225` against `PF-0297` was already known. **There are more, and two of them are consequential rather than cosmetic.**

### 1. `KP-0001` says the lender's wire instructions are removed. `TD-0205` says they are not. P0.

`KP-0001` is **CLOSED 2026-09-01** on Austin's word: *"Updated and information removed."* Its own text records what the closure does not establish, that nobody said which artefact was edited or whether the wiki copy and circulated PDFs were re-issued. **`TD-0205` is the exact same work**, worded *"Remove the lender's account name, account number, beneficiary bank and ABA routing number from SOP 302 and take payment instructions from each notice instead"*, and it is **open**, owner `David Berman with Natalie Magurne`, dated 2026-08-30. **VERIFIED**, both rows read in place.

**Two registers disagree about whether a live fraud exposure has been remediated, and the open one is assigned to a man who is leaving.** This is the highest value contradiction on the board because the cost of the registers being wrong in the optimistic direction is a wire to a fraudster.

### 2. `CM-30` says the registered agent was paid. `TD-0492` says pay or dispute it.

`CM-30` is **CLOSED 2026-09-03**, Austin's own words, *"CM-30 completed. confirm number 1599693."* `TD-0492` reads *"Pay or dispute the CT Corporation registered agent balance on A2Z Community Partners, account 9750574"* and is **open, unassigned**. **VERIFIED.** Harmless today, and it is the mechanism that produced the nine month arrears in the first place: a row closes in one register and its twin keeps standing in another.

### 3. `KP-0010` and `KP-0025` are the same finding with two IDs, and only one has a task.

`KP-0010`: *"The portfolio disagrees with itself on how many units it has. 6,379 from the Property Data Sheet against 8,020 from the warehouse."* `KP-0025` C1: *"Unit count"*, 6,379 against 8,020, *"1,641 apart and both are described as the portfolio."* **Same two numbers, same source pair, two rows.** `KP-0010` has `TD-0402` and a comparison workbook built 2026-09-01; `KP-0025` has no task anywhere. **Retire `KP-0025` into `KP-0010`.** Its ID retires with it, per rule 15.

### 4. `KP-0019` has absorbed `KP-0020`'s text, and the two rows now disagree about ownership.

`KP-0019`'s row body carries both findings and both closures, including *"2026-09-01: assigned to Albert by Austin"* twice and both `TD-0337` and `TD-0338`. `KP-0020`'s own row still reads owner blank, status `open`. **So the permissions matrix item is assigned to Albert on one row and unassigned on the next row down.** Cosmetic, and it is how a real assignment gets lost.

### 5. `KP-0003` and `PF-0024` are the same finding in two registers, both owned by the departing controller.

`KP-0003`: *"Accounting runs 30 to 45 days in arrears."* `PF-0024`: *"Books close 30 to 45 days in arrears so Ramp card spend is booked monthly instead of reviewed weekly."* Both owner `David Berman`. **The property follow-up register is carrying a corporate function finding.** Retire `PF-0024` into `KP-0003`.

### 6. `KP-0030` and `TD-0005` are the same $35,056, and the finding cites no task while the task cites the finding.

`KP-0030` C6: Hunter Springs MHC carrying $35,056 revenue on a leg that should be dormant. `TD-0005` is that item as a task, owner `David Berman`, and cites `[[00-Meta/open-items]] C6`. **The `KP` row does not cite `TD-0005`**, which is why the automated link check below reports `KP-0030` as having no task when it has one.

### 7. `KP-0008` is deferred and its two tasks are open.

Austin deferred `KP-0008` on 2026-09-03: *"Will leave for now as those will be deactivated in the future."* `TD-0008` is open at High and `TD-0508` is open at P2. **A deferred finding with two live tasks under it is a deferral that has not reached the work.**

### 8. `CM-07` and `KP-0006`, `CM-08` and `KP-0007`, are one incident each carried in two registers.

Both pairs are closed on the same disposition and both are correctly filed. Recorded so the pairing is not rediscovered: **a row count across registers is a count of rows, not of problems**, exactly as [[CLAUDE]] says.

### 9. Five promises are also to-dos, by design, and one of the pairs is an orphan on both sides.

`PR-0001` and `TD-0070`, `PR-0019` and both `TD-0363` and `TD-0354`, `PR-0028` and `TD-0260`, `PR-0031` and `TD-0181`, `PR-0033` and `TD-0364`. The register's own rule says a promise becomes a to-do when someone accepts it and the promise row stays open until the person is told, so four of these five are the intended shape. **`PR-0031` and `TD-0181` are the exception: both are unassigned.** A promise nobody owns, mirrored by a task nobody owns, is not a pair, it is the same nothing written down twice.

### 10. `PR-0013` is a duplicate of `PR-0012` on a community that does not exist.

`PR-0012` is the Lucky Clover maintenance lead's request for a bigger American flag and a Parakeet flag. `PR-0013` is *"Flagpole / flags"*, note *"Raised alongside the Lucky Clover flag request"*, community recorded as Muskegon Hill, **which Austin cleared on 2026-09-01 as not one of the 67**. Same request, one of the two rows has no place attached to it. **P4.**

### 11. Overlaps recorded rather than merged, because merging them would lose a fact.

- `KP-0008` and `KP-0068` are the same personal Gmail identity. `KP-0008` is deferred at High; `KP-0068` is Critical and open because the Fund II document base is reachable only through it. **The rows disagree on urgency about one account.**
- `KP-0021` and `KP-0051` are both the four Master Tracker versions. `KP-0021` names the two on Natalie's OneDrive; `KP-0051` names the two sharing a filename.
- `KP-0037`, `KP-0042` and `KP-0050` all reduce to one master community list and one authoritative state list.
- `KP-0070`, `KP-0071` and `KP-0072` are three rows about one BMHCII record base, written before anyone opened it. `KP-0071` says so in its own text.
- `CM-24`, `CM-19`, `KP-0033` and `KP-0055` are one counterparty, Kippy and Laurence Brokaw, confirmed by Austin as one person.
- `CM-25`, `CM-26`, `CM-27`, `CM-28` and `PR-0037` to `PR-0040` are one fund, Bedrock MHC Fund II, and five different people waiting on it.
- `CM-20`, `CM-23` and `KP-0036` may be one proceeding in Auburn, Massachusetts. Not merged, per the register's own instruction.

---

# Register 1: `CM` commitments, 30 rows

**What is different about this register.** It is the one Austin actually works from, and **twelve of the thirty are already closed and were moved to `## Recently closed` on 2026-09-03**, which is why the tier table shows twelve P4. The eighteen live rows carry **eleven named external counterparties**: Citrin Cooperman, Jadian, CountryPlace, 21st Mortgage, Triad, Capital One, Anderson and Kreiger, Cappello and Noel, First Title and Trust, Onyx Holdings, and the Fund II LP base. **My job here is less tiering and more saying which are moving.**

## The moving and not moving split, stated first

**Actually moving, with evidence of movement inside the last 48 hours:** `CM-15` (21st cleared pending orders 2026-09-02 and corrected one address), `CM-19` (Titan reinstated, Melanie mid transfer, status updated by Austin today), `CM-20` (CBRE agreed to release the comparables 2026-09-02), `CM-23` (unblocked today, counsel has given his view), `CM-25` (the written record surfaced today and five chasing LPs are now named), `CM-26` (Murad's request found to have been driving a workpaper programme since April), `CM-30` (paid today).

**Look like they are moving and are not:** `CM-13`, where the plan has been complete since 2026-08-26 and **Moe still has not been asked**, so the only thing that has happened is a sequencing decision. `CM-17`, where the answer arrived today and it is the bad answer, and **nothing has been drafted or sent**. `CM-18`, where the reply Austin owes Citrin **already exists verbatim in his own 2026-08-27 message** and has now missed two sends. `CM-24`, where the last recorded event is silence from Adam and the row's own next action is to decide what silence means. `CM-27` and `CM-28`, both raised today and both with a specific unanswered item older than four months. `CM-06`, where Austin answered three of four questions on 2026-09-02 and **the fourth, Gulf Breeze ownership, is still open**, along with who holds the unformed trust's 5%.

**Not moving at all:** `CM-10`, `CM-11`, `CM-14`, `CM-22`, `CM-29`.

## Row by row

Format per row: tier with its justification, owner, agent-ability, who is waiting and since when, duplicate.

### P0 Exposure

**`CM-10` Belmart bank package, plus an injured employee and a budget review.** **P0**, because an open employee back injury with workers' compensation documentation still unconfirmed is an insurance and regulatory path that does not close by itself, and unsanded handrails portfolio wide is a physical safety item on the same property. Owner **Austin**. **HUMAN ONLY**: three unrelated things ride on one row, one of them a person's injury claim. **Waiting**: the lender, no date recorded; the injured employee since the 2026-08-19 to 08-24 tour; Rick on a budget meeting since Austin asked for one on 2026-08-31. Duplicate of: none. **The bank package half alone would be P3. The tier comes entirely from the cross note.**

**`CM-13` Intercompany AR and AP reconciliation.** **P0**, because the person who created the entries leaves inside the same thirty day window the reconciliation is due in, and a balance nobody can reconstruct later is money that does not come back. Owner **Austin to unblock, working owner proposed Moe Mehmood and not yet asked**. **HUMAN ONLY**: it needs a signed entity list with EINs from one specific person, and a capacity decision about Moe who was already live on Royal Oaks payables. **Waiting**: nobody outside; the internal gate is G1. Duplicate of: none, though `PF-0015` and `PF-0030` are the same function seen from the property register. **The row reads as sequenced and is actually stalled, because the sequencing decision got made and the ask did not.**

**`CM-15` Floorplan line double counting, 46 duplicate lender submissions.** **P0**, because 32 homes carry an address the lender was given wrong, 28 orders totalling $1,408,256.25 were never reported to the lenders at all, and misstated floorplan collateral is a lending consequence rather than a bookkeeping one. Owner **Austin and Jon Wyss**, reassigned 2026-09-01. **AGENT WITH A HUMAN CHECK**: the seven leg serial by serial tie out on [[60-Communities/asset-inventory]] is exactly agent work and every lender facing reply is not. **Waiting**: Korey Bateman at CountryPlace since 2026-09-01 with an inspector due the week of 2026-09-08, Merrick Snider at 21st since 2026-09-02 16:17 ET, Karen Smith since 2026-09-01 13:20 ET. Duplicate of: none. Related `PF-0332`, `TD-0274`, `TD-0461`. **Moving on the lender side, static on the tie out side.**

**`CM-17` Management liability binder $43,090.21 and the governance question under it.** **P0**, because Austin confirmed today that **Jadian was not consulted**, and a capital partner who was meant to be in a decision and was not is a governance breach that declining the binder does not reverse. Owner **Austin, not delegable**. **HUMAN ONLY**: guardrail 6 governs everything touching Jadian. **Waiting**: Jadian, unknowingly, since 2026-08-27; the broker Baldwin on the binder decision since 2026-08-27. Duplicate of: none. **Today's 10:00 ET Jadian Pipeline Review is the difference between a disclosure and a discovery, and nothing has been drafted.**

**`CM-18` A2Z ND Portfolio Partners equity schedule and the Business Extensions.** **P0**, because it blocks final 2025 returns for ND, Cambridge and Mayflower, and a blocked filing is a regulatory consequence on somebody else's clock. Owner **Austin**. **AGENT WITH A HUMAN CHECK**: the answer exists verbatim in his own 2026-08-27 21:35 ET message, so an agent can assemble the reply and he sends it. **Waiting**: Tim McNamara at Citrin Cooperman since 2026-08-27 19:54 ET on the contributions question and since **2026-03-23 on the schedule itself, 164 days**; Lisa Timbrook on the Business Extensions since Austin promised them on 2026-08-27 15:15 ET. Duplicate of: none. **Slipped twice, so by this register's own rule it escalates rather than being rescheduled a third time.**

**`CM-19` Royal Oaks, nine missing titles, $67,500, a seller alleging failure to retitle.** **P0**, because nine unretitled homes are a title defect a buyer's counsel will find, and **the cure runs through a voluntarily reinstated dissolved LLC whose expiry nobody has recorded**, so a lapse resets the cure to zero. Owner **Melanie Sanchez**, the reply still Austin's. **AGENT WITH A HUMAN CHECK**: verifying `ROYAL-4, 6, 7, 11, 14, 22, 25, 28, 37` against the lot records is agent work, and nothing reaches First Title and Trust or Brokaw without Austin. **Waiting**: Laurence Brokaw since 2026-08-28 18:55 ET, Enon Winkler and Stephanie McMahon at Sunstone since 2026-08-27, Melanie on lot verification since today. Duplicate of: none; same counterparty as `CM-24` per `KP-0033`. **Two drafts to Melanie are unsent and are correctly held until the lots are verified.**

**`CM-20` Massachusetts class settlement, American and Whispering Pines MA, $400,000 agreed.** **P0**, because it is live class litigation under the Manufactured Housing Act and Chapter 93A with plaintiffs seeking double and likely treble damages, and the only open term is the post 2028 rent schedule. Owner **Austin**. **HUMAN ONLY**: privileged settlement correspondence and the path decision is his. **Waiting**: Melissa Allison at Anderson and Kreiger since 2026-08-18; CBRE's report and comparables now due **around 2026-09-11**, moved out from the 2026-09-04 target. Duplicate of: none; possibly the same proceeding as `CM-23` per `KP-0036`. **Moving. What is not moving is the comp set instruction, `KP-0034`.** One deliverable on this row is pure arithmetic and is agent-able: the dollar value of a one time $50 step against $20 a year across both tenant populations at two communities from December 2028 onward, which **nobody owns and which is the number that says whether the appraiser risk is worth taking.**

**`CM-24` Kippy dispute, a defaulted note where Parakeet is the lender, roughly $1M of unpaid management fees.** **P0**, because Parakeet is the lender on a note that matured and sat in default, the management agreement behind the $1M is verbal and unwritten, and both levers on the table land on the man whose voluntary cooperation `CM-19` currently depends on. Owner **Austin**, counsel running communication. **HUMAN ONLY**: litigation strategy. **Waiting**: Adam, Kippy's litigator, silent since roughly 2026-08-21 after Parakeet answered his three asks the same day. Duplicate of: none. Related `CM-19`, `KP-0033`, `KP-0055`. **Not moving, and counsel has still not been told that Kippy and Brokaw are one man (`TD-0368`).**

**`CM-25` Bedrock Fund II LP obligations.** **P0**, because an LP has threatened in writing to escalate to a state securities regulator, an issued capital account statement carried an admitted error, a $7,000 wire from July 2021 has never been traced, and Citrin has a **$217,787.93** unreconciled difference on the LP distribution schedule. Owner **Austin, Managing Partner, not delegable**. **HUMAN ONLY**: guardrail 6 on every line including the K-1 replies. **Waiting**: Gregory Khodara of WCO Capital since 2026-08-07 and again 2026-08-24, Bernie Schachter 2026-09-02, Patrick Scruggs 2026-09-01, John Buckwalter 2026-09-01, Steven Posborne 2026-09-01, Jim Folliard 2026-08-07, Tim McNamara at Citrin since 2026-09-01 19:56 ET, and **Tabish Rizvi of Onyx Holdings, whose own corporate return is due 2026-09-15, twelve days.** Duplicate of: none; carries `PR-0037`, `PR-0039`, `PR-0040` and `KP-0064`. **The $217,787.93 reconciliation is agent-able with a human check; nothing that reaches an LP is.**

**`CM-26` Ridaa Murad, 33% partner in Bedrock Group.** **P0**, because a GP side partner holding a third of the entity issued a 48 hour ultimatum on 2026-08-26 saying he would file personally without receipt, and **the 48 hours expired 2026-08-28**. Owner **Austin, not delegable**. **HUMAN ONLY**: guardrail 6, and his consent and information rights have never been checked against any document. **Waiting**: Murad since 2026-04-25 on the sectioned document request, since 2026-08-26 on the BEDROCK I GROUP dataroom, and twice by voicemail on 2026-09-02. Duplicate of: `KP-0061` is the same person as a findings row. **Moving in a way nobody here could see: the request has been driving a workpaper programme since April. The BEDROCK I GROUP half is a different entity and nothing says it has been answered at all.**

**`CM-28` Gallagher v. Bedrock MHC Fund II GP, LLC.** **P0**, because it is live California litigation in the fraud category, case 30-2026-01582020-CU-FR-CJC in Orange County Superior Court, with a December hearing whose date **appears nowhere in the record**, and an acknowledgment counsel asked Austin to sign for the DL Trust and Levin Trust defendants on 2026-08-06 with no confirmation it was ever returned. Owner **Austin**. **HUMAN ONLY**: litigation, and the acknowledgment is a signature. **Waiting**: David Cousineau at Cappello and Noel since 2026-08-06; Shulman Rogers coordinating. Duplicate of: none. **Raised today. A pressing LP became a fraud styled suit against the GP and no live page recorded the transition.**

**`CM-29` Capital One and Lamberton Lake.** **P0**, because it is an agency loan with an **insurance policy expiring 2026-10-31** and a First Notice already served, Fannie Mae annual certifications requested in February, April, May, July and August 2026 with no completion confirmation anywhere, and a lender who has asked the same $52,000 question twice and had no answer. Owner **Austin**, with the insurance filing itself **unassigned**. **AGENT WITH A HUMAN CHECK**: the $52,000 variance answer is already computable from the Grand Rapids water bills of $4,356, $4,966 and $9,463.14 against the March 2026 leak, and the lender reply is Austin's. **Waiting**: George Ksenics at Capital One since February 2026 on the certifications and twice since on the utility variance. Duplicate of: none. Related `KP-0067`, `PF-0459` to `PF-0461`. **Not moving. Five unanswered requests to a lender is a relationship problem before it is a compliance problem.**

### P1 Dated

**`CM-22` Geiger House PSA.** **P1**, because the timing driver is the **buyer's 1031 clock**, an outside date, and Jon wrote that it needed signing this week on 2026-08-30, meaning the week now running. Owner **Jon Wyss 100%, FYI for Austin**, corrected by Austin 2026-08-31. **HUMAN ONLY**: the liability cap and survival period are a negotiating position only the founders can set. **Waiting**: buyer's counsel and John Lisy on the open issues list since Sunday 2026-08-30. Duplicate of: none. Community is Geiger Key RV Resort, which `KP-0010` records as carrying four warehouse records for one asset. **Not moving in this register, and it may be moving in Jon's hands where this Brain cannot see it.**

**`CM-23` Auburn, MA rent control meeting.** **P1**, because a municipal proceeding around **2026-09-14** is the town's date and not Austin's, and travel has to be booked against it. Owner **Natalie Magurne** on the call, **Austin** on the travel. **HUMAN ONLY**: Natalie owes Justin Stelmac a call in her own words. **Waiting**: Justin Stelmac since roughly 2026-08-25, and Zach Schwartz who asked to be on the call. Duplicate of: possibly `CM-20` per `KP-0036`, deliberately not merged. **Unblocked today: Wallack has a view. What the view says was not stated and is not guessed, and if it is do not attend then this is a travel decision rather than a phone call.**

### P2 Blocking

**`CM-06` Berk Inc entity map.** **P2**, because Ridaa Murad's entity record (`KP-0061`), the Kippy counsel brief (`TD-0436`) and any answer to an ownership question all wait on it. Owner **Austin, not delegable**. **AGENT WITH A HUMAN CHECK**: reconciling `Org Chart Overview.xlsx` against `Org Chart Overview_122023.xlsx` and against `/sites/main/Shared Documents/Corporate/Formation Documents/Master Org Chart.xlsx` is mechanical, and the open questions are only answerable by him. **Waiting**: nobody outside; internally Zach and counsel. Duplicate of: none. **Two of four questions still open: who holds the 5% assigned to a trust that was never formed, and whether the chart is accurate on Gulf Breeze ownership.**

**`CM-14` Licence and permit transition.** **P2**, because Phase 1 cannot start and Melanie Sanchez's week one interview cannot be scheduled until Austin answers one question, namely who the function is being taken back from. Owner **Austin on the prerequisite, otherwise unnamed**. **HUMAN ONLY**: one sentence from Austin, and the three possible answers change the plan materially. **Waiting**: nobody outside. Duplicate of: shares the Melanie interview with `CM-19`. **Not moving since 2026-08-26. The company holds dealership licences in Georgia and South Carolina, which is why this is not a filing chore.**

**`CM-27` John B. Davies, six wind down questions.** **P2**, because a Fund II LP and advisor asked six specific questions on **2026-04-30**, chased on 5/8, 5/9, 5/24, 5/25, 6/6 and 6/29, received three acknowledgements and no substance, and **the thread then stops. 126 days as of today.** Owner **Austin**. **AGENT WITH A HUMAN CHECK**: the six answers can be drafted from the IR letter and the wind down plan, and guardrail 6 governs the send. **Waiting**: John B. Davies since 2026-04-30. Duplicate of: `PR-0038` is the promise half, deliberately split. **Not moving. Not P0 because no escalation has been threatened, and it is the row most likely to become one.**

### P3 Value

**`CM-11` Hensdale Club membership application.** **P3**, nothing breaks if it waits a month, and the 2026-09-04 date is one Austin set himself on the board on 2026-09-02. Owner **Austin**. **HUMAN ONLY**: a personal membership application in his own name. **Waiting**: the club. Duplicate of: none.

### P4 Noise, twelve closed rows

All twelve sit in `## Recently closed` and are correctly filed. **The residue under each is named, because a closure is not a clearance.**

- **`CM-01`** Known wrong text in two delivered Jadian reports. Closed 2026-09-01. **AGENT NOW**, archive only. Residue: which report versions went out and when is not recorded and was deliberately not reconstructed.
- **`CM-02`** Security exposure on corporate storage. **Risk accepted 2026-09-01, not fixed.** **AGENT WITH A HUMAN CHECK** on what survives. Residue: `TD-0321`, `TD-0322` and `TD-0323` are all open, and the row's own text says **file permissions and a Keeper migration do not retroactively unindex a password that SharePoint search has been returning in a result preview since 2024.** If one closed row on this board deserves reopening, it is this one.
- **`CM-03`** Jon Wyss as the analytics constraint. Closed 2026-09-02; the gate was read off a draft that never governed. **AGENT NOW**.
- **`CM-04`** Migration risk brief to Albert. Closed 2026-09-01. **AGENT NOW**.
- **`CM-05`** Lamberton Lake LP syndication records. Closed 2026-09-02. **AGENT NOW**. Residue: `TD-0397`, put a second copy somewhere the sale cannot take it.
- **`CM-07`** Lucky Clover, a resident pointed a gun at contractors. Closed 2026-09-01 on Austin's word with no artefact behind it. **AGENT WITH A HUMAN CHECK** on the residue. Residue: **there is still no trespass, law enforcement or lone worker protocol**, `TD-0329`, so the next lone manager has nothing to follow. Duplicate of `KP-0006` and `TD-0001`.
- **`CM-08`** Great Oak boil water notice. Closed 2026-09-01 on Austin's word. **AGENT WITH A HUMAN CHECK** on the residue. Residue: **no lift order, vendor confirmation or clearing sample result is filed anywhere in this Brain**, `TD-0330`, so a regulator asking for the paper gets pointed at the property. Duplicate of `KP-0007` and `TD-0002`.
- **`CM-09`** Email George about skills. Closed 2026-08-27, sent by Austin himself. **AGENT NOW**.
- **`CM-12`** Road trip Excel tracker. Closed 2026-09-01 and folded in. **AGENT NOW**. Residue: **the Wins tab, 33 rows of recognition with no register to live in**, deliberately not invented as a seventh register.
- **`CM-16`** Berman exit. Closed 2026-09-02. **HUMAN ONLY**. Personnel matter, see the private assessment file. Recorded here only as a fact: **`TD-0324` and `TD-0325` are open**, because disabling a named account does not rotate a shared service password and a revocation scoped to Parakeet's tenant does not reach `a2zcp.com`.
- **`CM-21`** August payroll allocations. Closed 2026-08-31 by Austin's ruling, run as circulated and audit after. **AGENT NOW**. **`board.json` still carries this row at priority `Open` inside section `Recently closed`**, which is the heading versus priority bullet mismatch the register documents on `CM-03` and `CM-05`.
- **`CM-30`** A2Z Community Partners registered agent. Closed 2026-09-03, paid, confirmation `1599693`. **AGENT NOW**. Residue: **`TD-0492` is still open**, and **no owner exists anywhere in this Brain for entity compliance**, so this recurs.

---

# Register 2: `PR` promises, 40 rows

**What this register is for, restated because it changes the tiering.** Every row is something Austin personally told a named human he would do. **A promise closes when the person is told, not when the work is done**, so *"we decided not to"* closes one honestly and silence does not. Following the standing instruction, **a broken promise is P2 at minimum regardless of its operational size**, because the cost is trust with a named person and that cost appears nowhere else on this board.

**Provenance.** `PR-0001` to `PR-0036` come from the Promises to Team tab of `parakeet-road-trip-tracker-2026-08.xlsx`, read in full 2026-09-01, archived at `99-Archive/2026-08-southeast-tour/`. The tour ran **2026-08-19 to 2026-08-24**, so those promises are **10 to 15 days old today**. `PR-0037` to `PR-0040` came out of the first sweep of the a2zcp mailbox on 2026-09-03 and carry their own dates.

**The headline number.** **Twenty-four of the forty have no owner at all**, recorded as `unassigned` exactly as the tracker stated them, with no owner inferred. Austin took three himself; Demetria, Natalie, John Clark, Leslie, Mark Doucette, Chris, Alex Pontes and "Team" hold the rest. **Thirteen of the forty are amenity or equipment spend that went straight onto the budget week list**, which is the shape of this register: a third of what the CEO promised his staff costs money nobody has budgeted.

## Broken promises, named

**Broken** means the promise carried its own timing and that timing has passed, or the person was told something would happen and nothing since has told them anything. **Nineteen of the forty are broken by that test.** Ordered oldest first.

| ID | Promised to | The promise | Age today | Why it is broken |
|---|---|---|---|---|
| `PR-0038` | **John B. Davies**, Fund II LP and advisor | A substantive answer to six wind down questions, promised three times as *"received, will respond asap"* | **126 days** (asked 2026-04-30) | Chased 5/8, 5/9, 5/24, 5/25, 6/6, 6/29. Three acknowledgements, no substance, then the thread stops. |
| `PR-0037` | **Gregory Khodara**, WCO Capital, Fund II LP | A written explanation of the portal discrepancy and, if his read held up, resolution of the $348.88 accrual gap *"right away"* | **18 days** (2026-08-16) | **No written reconciliation appears in the mailbox afterwards.** He has since threatened to escalate to a state securities regulator. |
| `PR-0039` | **Masha Kahn**, Fund II LP | *"We will update you and others asap"* on the final K-1 | **17 days** (2026-08-17) | Arguably overtaken by the 2026-09-02 IR broadcast to the whole list. **She was told individually and has not been answered individually.** |
| `PR-0001` | **The Regency I manager** | Tree trimming coming soon, before hurricane season | 10 to 15 days | Hurricane season is already running, so the stated condition has passed. `TD-0070` is open and unassigned. |
| `PR-0005` | **The Brunswick manager** | Mark's rehab crew arriving in the next couple of days | 10 to 15 days | Status is `VERIFY`. **Nobody has confirmed the crew showed and nobody has told her either way.** |
| `PR-0010` | **The Whispering Pines manager** | Her phone number listed alongside the sales line on the two Daisy Bear listings, *"we've got to talk about that"* | 10 to 15 days | The conversation she was promised has not happened. She lives on site and loses walk ups to the call centre. |
| `PR-0011` | **Angel and the maintenance lead**, Lucky Clover | A design decision on the shuffleboard shade and the lighting walk through, *"we'll get together about lighting up the area"* | 10 to 15 days | The get together has not happened. The decision is also `PD-15`. |
| `PR-0016` | **Amanda and team**, Vantage Oaks | Chris on site next week for the kitchen and outlet fix | 10 to 15 days | Next week has passed and nothing records whether Chris went. |
| `PR-0017` | **The Paradise Palms staff** | Energized by the end of this week | 10 to 15 days | That week ended. **Staff repeated the timeline to residents**, so this one broke twice. |
| `PR-0019` | **Rose**, Gulf Breeze | Take the water company fight off her shoulders, *"the fact that you said you would help me"* | 10 to 15 days | Austin's own 2026-09-01 note says Rose has moved forward with traction herself. **Traction by Rose is not the promise being kept.** The promise was to take it off her. |
| `PR-0021` | **Rose**, Gulf Breeze | Leslie to paper the lot 2 as is and title pending sale | 10 to 15 days | Nothing records it being papered. |
| `PR-0025` | **Vicky**, River Oaks | Reimburse promptly for the cash bingo machine she bought | 10 to 15 days | **She fronted her own cash and is still out of pocket.** "Promptly" has passed. |
| `PR-0026` | **Vicky**, River Oaks | Approve the aerator quote she already has | 10 to 15 days | She holds the quote and has no answer. |
| `PR-0027` | **Mitch and a staffer**, River Oaks | Resolve pier power, George's quote against letting Mitch and the staffer do it | 10 to 15 days | Two named people are waiting on a choice nobody has made. |
| `PR-0030` | **The mom who moderates the community Facebook page**, The Oaks | A rent credit | 10 to 15 days | The tracker's own note: **you told her to reprocess the request if you forget. She should not have to.** |
| `PR-0031` | **The Oaks manager** | Connect her with the in house financing specialist | 10 to 15 days | Unassigned here and unassigned as `TD-0181`. **She is still handing prospects cold to external lenders.** |
| `PR-0032` | **Maintenance and Travis**, The Oaks | Tool package, shed on slab, gator | 10 to 15 days | **Eric left with the tools.** Maintenance has the list and no tools. |
| `PR-0033` | **Julie and an elderly resident**, Belle Haven | Monday water leak inspection at the elderly resident's unit | 10 to 15 days | Status `VERIFY`. Promised to her face on a Saturday. **`TD-0364` asks Alex Pontes how it was handled and there is no answer on file.** |
| `PR-0036` | **The Riverwalk manager** | Confirm receipt of his complete lot issues list and get Champion scheduled | 10 to 15 days | *"What lot?" "All of them."* He was told corporate carries it and nothing since has shown him that. |

**Two promises were quietly overtaken rather than broken, and the distinction matters.** `PR-0039`, Masha Kahn, was answered collectively by the 2026-09-02 IR broadcast but never individually; that is a judgement call and one sentence from Austin settles it. `PR-0004` was closed by events rather than by keeping it: Austin's own words, *"This was just a conversation with maintenance that is moving with girlfriend to Michigan"*, and **the man it was made to is leaving the state, so there is nobody left to call anybody out.** The note in the register says Ohio in one place and Michigan in Austin's own quote in the next; **both are on the row, neither is resolved, and it does not matter to the disposition.**

**One promise has simply been dropped and should be said plainly.** `PR-0003`, the payment plan and subsidy help with skirting offered to residents in good standing at Regency I. It is described in the register as a **stated policy commitment**, it is unassigned, and no task, budget line or process anywhere in this Brain implements it. **It was made to residents rather than to staff, which makes it the only promise on this register with Fair Housing consistency riding on it**, because a discretionary subsidy for "residents in good standing" administered by nobody is administered inconsistently by definition.

## Row by row

Format per row: tier with its justification, owner, agent-ability, duplicate.

### P0 Exposure

**`PR-0033` Monday water leak inspection at an elderly resident's unit, Belle Haven.** Promised to **Julie and the resident**, to their faces, on a Saturday. **Not kept, status VERIFY, 10 to 15 days old.** **P0**, because an unrepaired water leak in an occupied unit is a habitability and personal injury path, the resident is elderly and caring for a terminally ill brother, and **nobody has confirmed the inspection happened.** The tier is INFERRED from the nature of an unverified leak rather than from any recorded damage. Owner **Alex Pontes**, who is Alexandra Pontes, the Belle Haven regional manager. **HUMAN ONLY**: guardrail 5, and the tracker's own note is that this one is about dignity as much as plumbing. Duplicate of `TD-0364`, which is the follow up rather than the promise.

**`PR-0037` Gregory Khodara, WCO Capital.** Promised in writing 2026-08-16, **18 days, not kept**. **P0**, because the LP it was made to has since threatened in writing to escalate to a state securities regulator and the promised written reconciliation does not exist. Owner **Austin**. **HUMAN ONLY**: guardrail 6, and this is the LP `CM-25` was built around. Duplicate of: none; `CM-25` is the commitment half.

### P1 Dated

**`PR-0040` The whole Fund II LP list.** 2025 K-1s *"in the next several days"*, a confirmation email when they post to InvestNext, and an offer to update mailing details. Sent by IR **2026-09-02, one day old, so this is a live clock rather than a broken promise.** **P1**, because behind it sits **2026-09-15**, Onyx Holdings' own corporate filing deadline, which is not Parakeet's date. Owner **Austin**. **HUMAN ONLY**: guardrail 6 and it is a promise to a countable set of people. Duplicate of: none; recorded under `CM-25`. **A promise made to a list is still a promise, and this one has a countable set of people watching it.**

### P2 Blocking

Nineteen rows. All are broken promises, so all take the P2 floor, and each names who is blocked.

- **`PR-0001`** Tree trimming, Regency I manager, **Natalie Magurne**. P2: she asked directly and hurricane season has already started. **AGENT WITH A HUMAN CHECK**: scheduling a vendor. Duplicate of `TD-0070`, which is open and unassigned. **If any of those trees overhang an occupied home this is P0 and nothing in the record says either way.**
- **`PR-0002`** Mailbox replacement, seven stations, Regency I manager, **John Clark**. P2: she already got it approved, so this is execution, not authorisation. **AGENT WITH A HUMAN CHECK**. Budget week flagged.
- **`PR-0003`** Payment plan and subsidy help with skirting, residents in good standing, Regency I, **unassigned**. P2 as a dropped promise; see the Fair Housing note above. **HUMAN ONLY**: guardrail 5.
- **`PR-0005`** Mark's rehab crew, Brunswick manager, **Mark Doucette**. P2: status VERIFY and nobody has told her. **AGENT WITH A HUMAN CHECK**: confirm the crew showed.
- **`PR-0010`** Manager's phone number on the two Daisy Bear listings, Whispering Pines, **unassigned**. P2: she loses walk ups to the call centre every day it waits. **HUMAN ONLY**: she was promised a conversation. Ties to the RingCentral fix.
- **`PR-0011`** Shuffleboard shade design decision and the lighting walk through, Angel and the maintenance lead, Lucky Clover, **unassigned**. P2: a design decision is owed to two named people. **HUMAN ONLY**. Also `PD-15`. Budget week flagged.
- **`PR-0016`** Chris on site for the kitchen and outlet fix, Amanda and team, Vantage Oaks, **Chris**. P2: next week has passed. **AGENT WITH A HUMAN CHECK**: confirm he went.
- **`PR-0017`** Energized by end of week, Paradise Palms staff, **unassigned**. P2: **staff repeated the timeline to residents**, so the broken promise has propagated past the person it was made to. **AGENT WITH A HUMAN CHECK**: get the real power date and hand it to the staff.
- **`PR-0019`** Take the water company fight off Rose's shoulders, Gulf Breeze, **Austin**. P2: the promise was to take it off her and she is still carrying it. **HUMAN ONLY**: escalating to a named human at a utility on her behalf. Duplicate of `TD-0363` and `TD-0354`. Follow up due 2026-09-11.
- **`PR-0021`** Paper the lot 2 as is and title pending sale, Rose, **Leslie Croft**. P2: Rose is waiting. **HUMAN ONLY**: a title pending sale is papered by a person. **A second title pending item on a different asset, so read it alongside `CM-19`.**
- **`PR-0025`** Reimburse Vicky for the cash bingo machine, River Oaks, **Team**. P2 by the floor rule, and **it is the cheapest broken promise on the board: an employee is personally out of pocket.** **HUMAN ONLY**: guardrail 8, money out the door. Budget week flagged, which is itself the problem, because a reimbursement of an employee's own cash should not be waiting on a budget session.
- **`PR-0026`** Approve the aerator quote Vicky already has, River Oaks, **Natalie Magurne**. P2: she holds the quote. **HUMAN ONLY**: guardrail 8.
- **`PR-0027`** Resolve pier power, Mitch and a staffer, River Oaks, **John Clark**. P2: two named people are waiting on a choice. **HUMAN ONLY**.
- **`PR-0030`** Rent credit for the mom who moderates the community Facebook page, The Oaks, **Austin**. P2, and **this is the promise most likely to create a problem by being kept carelessly**: the register's own note says check first whether you can compensate her given she posts on the community's behalf, and nobody has answered that. **HUMAN ONLY**: guardrail 5, a named resident, and an unresolved question about compensating someone who speaks for the community.
- **`PR-0031`** Connect the manager with the in house financing specialist, The Oaks, **unassigned**. P2: she is handing prospects cold to external lenders. **AGENT WITH A HUMAN CHECK**: it is an introduction. **Duplicate of `TD-0181`, and both sides are unassigned**, so the promise and its task are the same nothing written twice.
- **`PR-0032`** Tool package, shed on slab, gator, maintenance and Travis, The Oaks, **unassigned**. P2 Blocking in the literal sense: **Eric left with the tools and maintenance cannot work without them.** **HUMAN ONLY**: guardrail 8. Budget week flagged.
- **`PR-0036`** Confirm receipt of the lot issues list and get Champion scheduled, Riverwalk manager, **unassigned**. P2: he gave a complete list and has heard nothing. **AGENT WITH A HUMAN CHECK**: consolidating the list is agent work, `TD-0359` is the consolidated Champion escalation.
- **`PR-0038`** John B. Davies, six wind down questions, **Austin**. P2, and **it is the oldest broken promise on this board at 126 days.** Not P0 because he has threatened nothing; that is exactly why it is easy to keep not answering. **AGENT WITH A HUMAN CHECK**: the six answers can be drafted, guardrail 6 governs the send. Duplicate of: `CM-27` is the commitment half.
- **`PR-0039`** Masha Kahn, individual update on the final K-1, **Austin**. P2: told individually, answered collectively. **HUMAN ONLY**: guardrail 6, and it is a judgement call worth one sentence from him.

### P3 Value

Thirteen rows. Nothing breaks if they wait a month, and **eleven of the thirteen are budget week spend**, which means the register is telling Austin that the honest close on most of them is a decision at budget week rather than a delivery.

- **`PR-0006`** Gator and equipment pricing support, new maintenance hire, Brunswick, **unassigned**, budget week. **HUMAN ONLY**, spend.
- **`PR-0007`** Benches at the 42s and the waterfront, Brunswick manager, **John**, budget week. **HUMAN ONLY**, spend. Agreed in concept.
- **`PR-0008`** Playground or basketball in the old pool area, Brunswick manager, **unassigned**, budget week. **HUMAN ONLY**. The register's own note is to pick and fund at least one visibly.
- **`PR-0009`** Bus stop shelter, Brunswick manager, **unassigned**, budget week. **HUMAN ONLY**.
- **`PR-0012`** Bigger American flag, Parakeet flag and the cable rigging, Lucky Clover maintenance lead, **unassigned**, budget week. **HUMAN ONLY**. **`PR-0013` is a duplicate of this row.**
- **`PR-0015`** Advance notice before walkway crews arrive, Amanda and team, Vantage Oaks, **unassigned**. **AGENT WITH A HUMAN CHECK**: it is a scheduling message, and it becomes broken the moment the next crew arrives unannounced.
- **`PR-0018`** Set and powered within a month, closing out late September, Vantage Oaks staff, **unassigned**. P3 because it is not yet due. **AGENT WITH A HUMAN CHECK**. **Staff repeated the timeline to residents, same as `PR-0017`, so it converts to P2 the day it slips.**
- **`PR-0020`** Zero turn mower and trailer so Rose's maintenance guy replaces the fired landscaper, Gulf Breeze, **unassigned**, budget week. **HUMAN ONLY**, spend.
- **`PR-0022`** Ship the remaining shirts and swag, Vicky, Mitch, Sam and team, River Oaks, **Demetria Loukas**. **AGENT WITH A HUMAN CHECK**: place the order, Demetria approves. They ran out.
- **`PR-0023`** Movie night projector, River Oaks team, **unassigned**, budget week. **HUMAN ONLY**, spend.
- **`PR-0024`** Clubhouse microwave, River Oaks team, **unassigned**, budget week. **HUMAN ONLY**, spend.
- **`PR-0028`** Resident survey on amenities before building, River Oaks residents, **unassigned**, budget week. **AGENT WITH A HUMAN CHECK**: draft only, guardrail 5 on anything resident facing. Duplicate of `TD-0260`, owner Natalie Magurne, scoped to River Oaks only.
- **`PR-0029`** Lunch or tea with the moms' community committee, The Oaks, **Austin**. **HUMAN ONLY**. Not broken: Austin's own note is that the timing belongs to the committee, so this closes when they set their calendar. Coordinate with Natalie.

### P4 Noise, five rows

- **`PR-0004`** Closed 2026-09-01. **AGENT NOW**, kept as a closed row per the ID convention. The person it was made to was never named and is leaving the state.
- **`PR-0013`** Flagpole and flags. **P4 Noise and a duplicate of `PR-0012`.** The tracker recorded the community as **Muskegon Hill, which Austin cleared on 2026-09-01 as not one of the 67**, and the original value was deliberately kept so nobody re-adds it. **AGENT NOW**: retire it into `PR-0012` and keep the ID.
- **`PR-0014`** Back Angel visibly after a resident threatened her with a gun. Closed 2026-09-01 on Austin's word, same disposition as the incident. **AGENT NOW** on the row. **What backing her looked like is recorded nowhere**, and the register says so rather than inventing it. The protocol gap survives as `TD-0329`.
- **`PR-0034`** Gift bags, umbrella and gift cards for Alex and Brandon at Belle Haven. Closed 2026-09-01, Austin: *"Completed."* **AGENT NOW**.
- **`PR-0035`** Applegate grab bag went out without the gift card. Closed 2026-09-01, Austin: *"Completed."* **AGENT NOW** on the row. **The standing part is not closed**: buy $10 to $25 gift cards in bulk so it does not happen again, and nothing records that being done.

## What this register says that no other register can

**Twenty-four unowned rows out of forty.** Every one is a thing the CEO said to a named employee, and for twenty-four of them the company's answer to *"who is doing this"* is nobody. **`KP-0022` says turnover is the reason the compliance calendar is urgent. This register is the same argument made from the other end**: thirty six things the CEO told named employees he would do, in a company whose stated retention risk is turnover, and the honest status on nineteen of them is broken.

---

# Register 3: `KP` known problems, 74 rows

**What is different about this register.** These are **findings, not tasks**, so the useful question is not what tier they take but **whether each one has an owner and a next action, or whether it is only recorded.** A known problem with no task attached is a problem the company has decided to live with without ever saying so.

## The coverage answer, first

**Every `KP` was checked against `10-Business/eos/to-dos.md` in both directions**: does the `KP` row name a `TD`, and does any `TD` row name the `KP`. **Sixty-two of the seventy-four have at least one task attached. Eighteen do not.** Two of those eighteen have a task that exists but is unlinked, which is a filing defect rather than a gap, and both are named below.

### The eighteen with no task attached

| ID | What it is | Gap or acceptance | Reasoning |
|---|---|---|---|
| `KP-0001` | SOP 302 publishes a lender's full wire instructions | **Neither. It has a task and the task disagrees with it.** | Closed 2026-09-01 on Austin's word, so no task is needed by its own account. **`TD-0205` is that task, it is open, and it is assigned to David Berman.** See the contradictions section. |
| `KP-0002` | Employee Handbook has no effective date and no Georgia or South Carolina addendum | **Not a gap. Unlinked task.** | **`TD-0221` is exactly this work, owner Demetria Loukas, open.** Neither row cites the other, which is why the automated link check reports a gap. **Fix the link, not the coverage.** |
| `KP-0016` | 14 state compliance SOPs sitting at counsel review with none signed off | **Gap** | **No task exists anywhere.** The largest block of finished work in the company is behind one gate and nobody owns pushing on it. Owner reads *"outside counsel, via Natalie"*, which is a route, not an owner. |
| `KP-0017` | Massachusetts and North Carolina are live operating states with no compliance SOPs | **Not a gap. Unlinked task.** | `TD-0207`, owner Natalie Magurne, open, *"Commission Massachusetts and North Carolina compliance SOPs."* Neither row cites the other. |
| `KP-0018` | No Chapter 513 or RV compliance process exists at all | **Not a gap. Unlinked task.** | `TD-0208`, owner Natalie Magurne, open. Neither row cites the other. |
| `KP-0024` | Justin Minkoff has no access to anything | **Deliberate acceptance** | Austin: *"This will come in due time."* Deferred, not closed, and the row is deliberately left standing as the only written record that this is a decision rather than an oversight. Re-surfaces with the permissions pass. |
| `KP-0025` | Unit count, 6,379 against 8,020 | **Neither. Duplicate.** | Same finding as `KP-0010`, which has `TD-0402` and a comparison workbook. **Retire it.** |
| `KP-0026` | What counts as a reporting property, Shell Pointe, Geiger Key, Congress | **Gap** | Two pages disagree on Austin's own stated instruction and **no task makes them agree.** Board reporting inherits whichever page someone opens. |
| `KP-0027` | Occupancy, 82.5% against 77.67% | **Gap, and a cheap one** | Different periods and different denominators. **One sentence saying which answers the question would close it and nobody has written it.** |
| `KP-0028` | No financial baseline in this Brain | **Deliberate acceptance, correctly** | Resolved by addition: the TTM figures were added to the numbers ledger 2026-08-31 with a source and a date. Done and never closed. |
| `KP-0029` | Lucky Clover's manager | **Deliberate acceptance with residue** | Resolved 2026-08-31, the manager is Angel. **The residue is real: the December 2025 org chart and the March 2026 infill sheet are both stale on this row and nothing corrects them.** |
| `KP-0030` | Hunter Springs MHC carrying $35,056 it should not | **Not a gap. Unlinked task.** | `TD-0005`, owner David Berman, open, cites the finding by its old label `C6` rather than by ID. |
| `KP-0031` | Southgate is a trap, not a conflict | **Deliberate acceptance, correctly** | Recorded so the original misreading does not resurface from the archived road trip pages. Nothing to do. |
| `KP-0032` | Is the settlement a Massachusetts or a Florida matter | **Deliberate acceptance, correctly** | Resolved 2026-08-31 by Austin and left in place because its resolution opened three other rows. |
| `KP-0035` | Is there a separate Belle Haven settlement | **Gap, and the most uncomfortable one** | Austin said Belle Haven is *"completely separate"*, which reads as a matter that exists. **If it is live it currently has zero recorded detail anywhere and no task to find any.** A gap to fill, not an item to invent. |
| `KP-0038` | Origins projected cash negative by February 2027 | **Gap** | **The only forward looking cash statement anywhere in this Brain has no owner and no task.** The two `TD` numbers on the row, `TD-0384` and `TD-0386`, are Jon's own overnight asks and are not tasks about this finding. |
| `KP-0058` | Origins distributions run on a calendar cadence the cash projection says breaks | **Gap** | Its only apparent task, `TD-0476`, mentions `KP-0058` solely as an artefact of the ID collision incident. **There is no task about the distribution gate.** |
| `KP-0069` | `austinrberk@gmail.com` stopped being readable and nothing recorded the trade | **Acceptance, and a sound one** | Austin says the things at the top of his mind are not in that account, so nothing is being chased. **The cost of not looking is bounded and the row exists so a later sweep does not report clean while assuming it covered a third mailbox.** |

**So the honest count is: five deliberate acceptances that are correct (`KP-0024`, `KP-0028`, `KP-0031`, `KP-0032`, `KP-0069`), one duplicate to retire (`KP-0025`), four unlinked tasks that only need a cross reference (`KP-0002`, `KP-0017`, `KP-0018`, `KP-0030`), one contradiction (`KP-0001`), one residue (`KP-0029`), and six genuine gaps: `KP-0016`, `KP-0026`, `KP-0027`, `KP-0035`, `KP-0038` and `KP-0058`.**

**Two of the six genuine gaps are about the same fund's cash.** `KP-0038` says Origins is projected cash negative by February 2027 if current distribution and infill plans continue. `KP-0058` says the monthly Origins distribution has a standing calendar marker with no gate on it, **and the marker fell today, 2026-09-03**. Neither has an owner, neither has a task, and **nobody has put them next to each other except the register itself.**

## Owner coverage

**Twenty-one of the seventy-four carry `unassigned` or a proposed owner rather than a real one.** The unowned set is concentrated exactly where the money is: `KP-0038`, `KP-0040`, `KP-0041`, `KP-0042`, `KP-0043`, `KP-0044`, `KP-0046`, `KP-0047`, `KP-0049`, `KP-0050`, `KP-0051`, `KP-0052`, `KP-0053`, `KP-0054`, `KP-0057`, `KP-0058`, `KP-0059`, `KP-0060`, `KP-0065`, `KP-0067`, plus `KP-0037` which says in its own text *"No owner in this Brain."* **Four of them name the Controller seat, which is the seat in transition.**

## Row by row

Columns: the tier clause, the owner as the register states it, the agent-ability clause, whether a task is attached, and the duplicate.

### P0 Exposure, 29 rows

| ID | Short label | Why P0 | Owner | Agent-ability | Task | Duplicate of |
|---|---|---|---|---|---|---|
| `KP-0001` | SOP 302 publishes a lender's full wire instructions | Direct wire fraud exposure, and **two registers disagree about whether it is fixed** | Austin, reassigned from Berman | `AGENT WITH A HUMAN CHECK`: searching every circulated copy is agent work, accepting the result is not | Yes, `TD-0205`, **open and contradicting the closure** | Contradicts `TD-0205` |
| `KP-0002` | Employee Handbook, no effective date, no GA or SC addendum | The company holds dealership licences in Georgia and South Carolina and the handbook covers neither | Demetria Loukas | `AGENT WITH A HUMAN CHECK`: the version request is drafted and ready, HR sends it | Yes, `TD-0221`, unlinked | Unlinked pair with `TD-0221` |
| `KP-0003` | Accounting runs 30 to 45 days in arrears | No live spend visibility means money leaves before anyone sees it, and **the sole owner is leaving** | David Berman | `HUMAN ONLY`: the Ramp agent scope is a controls decision, not a build decision | Yes, `TD-0327` | `PF-0024` is the same finding |
| `KP-0005` | Five Phase 1 SOP decisions waiting on people | Four live SOPs give four different Florida cure periods, and an eviction served on the wrong cure period is void | Austin with Natalie | `HUMAN ONLY`: five decisions need five people in a room | Yes, `TD-0381`, `TD-0206` | None |
| `KP-0008` | Corporate securities records under a personal Gmail | Cap tables, fund subscriptions, K-1s, an LPA and executed signature pages in a consumer account, and **`KP-0068` says it is the only route to the Fund II records** | Austin with Albert | `AGENT WITH A HUMAN CHECK`: enumerating the memberships from the corporate account is now possible, removal is not | Yes, `TD-0008` and `TD-0508`, **both open while the finding is deferred** | Overlaps `KP-0068` |
| `KP-0011` | No Responsible Contractor Review in contract approval | An explicit Jadian implementation requirement that no process page performs, due 2026-09-30 | Austin with Zach, Natalie, Melanie, Moe | `HUMAN ONLY`: a gate inside the AP approval workflow plus a handbook clause | Yes, `TD-0332` | None |
| `KP-0013` | The annual Responsible Contractor audit may not have happened | A missed LP mandated annual audit, and the one filed report is a compilation of certifications and news searches rather than an audit | Zach Schwartz proposed, Moe on the data | `HUMAN ONLY`: an audit of contractor pay practices is fieldwork | Yes, `TD-0334` | None |
| `KP-0017` | MA and NC live with no compliance SOPs | Massachusetts is the most tenant protective law in the portfolio **and there is an active Massachusetts class action** | Outside counsel via Natalie | `HUMAN ONLY`: counsel drafts state compliance | Yes, `TD-0207`, unlinked | Unlinked pair with `TD-0207` |
| `KP-0018` | No Chapter 513 or RV compliance process | RV is a large part of the portfolio and Chapter 513 is statutory | Outside counsel via Natalie | `HUMAN ONLY`: counsel | Yes, `TD-0208`, unlinked | Unlinked pair with `TD-0208` |
| `KP-0022` | No compliance calendar exists | It carries the Florida January 1 Division filing, the 7 year retention standards and the insurance renewals, and **`CM-30` is what its absence costs** | Austin with Zach, Natalie, Melanie, Moe | `AGENT WITH A HUMAN CHECK`: the obligations are already enumerated, the dates need a human | Yes, `TD-0340`, `TD-0395` | None |
| `KP-0033` | Kippy and Brokaw are one person | Counsel is running a hostile fee dispute against the man whose voluntary reinstatement `CM-19`'s title cure runs through, **and counsel has not been told** | Austin | `HUMAN ONLY`: telling counsel | Yes, `TD-0368`, open | The question is resolved; the consequence lives in `CM-19` and `CM-24` |
| `KP-0034` | The comparable set for the Massachusetts case is recorded nowhere | It decides the fair market rent number the whole case turns on, **CBRE is selecting comps now and they go straight to plaintiffs' counsel** | Austin | `HUMAN ONLY`: instructing CBRE is a privileged litigation act | Yes, `TD-0345`, `TD-0469` | Lives inside `CM-20` |
| `KP-0038` | Origins projected cash negative by February 2027 | A fund projected to run out of cash while distributions continue monthly, and it is the only forward looking cash statement in this Brain | **unassigned** | `HUMAN ONLY`: whether a model exists and who owns FP&A are both people questions | **No task** | Pairs with `KP-0058` |
| `KP-0041` | $989,786 of GL spend against 56 completed units | A roughly $1M prior period adjustment, an overstated WIP and an understated depreciable base, surfacing at the first reconciliation | **unassigned**, the Controller seat | `AGENT WITH A HUMAN CHECK`: a WIP trial balance query is agent work, the accounting answer is not | Yes, `TD-0405` | None |
| `KP-0044` | Origins and Kippy spending rehab capital outside the tracker | **$32,530 of GL spend booked against Kippy units for work Jon says is Kippy's responsibility**, on a counterparty in a live fee dispute | **unassigned**, Jon chairs the call | `AGENT WITH A HUMAN CHECK`: the reconciliation is agent work, the Kippy ledger question needs an accountant | Yes, `TD-0416`, `TD-0417`, `TD-0520` | Related `CM-24`, `KP-0055` |
| `KP-0047` | Nothing captures a rehab invoice | **No WIP roll forward can be produced at all**, on a program with roughly $1M in question and an audit obligation behind it | **unassigned**, the Controller seat | `AGENT WITH A HUMAN CHECK`: checking whether AvidXchange already holds the invoices is one query | Yes, `TD-0406`, `TD-0407` | None |
| `KP-0055` | The Kippy relationship is wider than `CM-24` records | Parakeet is lender and seller on more than one Kippy asset, **and the same call approved $20,000 of rehab spend at Hunter Springs, an asset Parakeet sold to and financed for this counterparty** | Austin | `HUMAN ONLY`: it belongs in the counsel brief | Yes, `TD-0436`, `TD-0401`, `TD-0446` | Extends `CM-24`, informed by `CM-06` |
| `KP-0057` | Nobody knows whether the budgeted admin fee is charged on home closings | Revenue that may simply not be billed, per closing, against a 2026 plan to sell roughly 400 homes | **unassigned** | `HUMAN ONLY`: an accountant has to answer whether the fee is charged | Yes, `TD-0438` to `TD-0440`, `TD-0474` | None |
| `KP-0058` | Origins distributions run on a cadence the cash projection says breaks | **No step anywhere tests a monthly distribution against the forward cash position before it goes, and the marker fell today** | **unassigned** | `HUMAN ONLY`: one sentence saying whether the check already happens and by whom | **No task**; `TD-0476` only mentions the ID from the collision incident | Pairs with `KP-0038` |
| `KP-0059` | A live password for the Uniti agent mailbox posted in plain text in Teams | An identity that can send mail as Parakeet, in a retained, searchable, exportable channel | **unassigned** | `HUMAN ONLY`: rotating a credential is an IT act | Yes, `TD-0472`, `TD-0473`, `TD-0532` | Explicitly **not** covered by `CM-02`'s risk acceptance |
| `KP-0062` | Live one time passcodes arriving in plain text in the a2zcp mailbox | Bank and utility verification codes keep arriving into a mailbox read by sessions and agents, and **MFA status on it is unknown** | Austin | `HUMAN ONLY`: MFA and mail routing on his own bank mailbox | Yes, `TD-0486` | Same class as `CM-02`'s `A2Z Utility Logins.xlsx` |
| `KP-0063` | Departed addresses still receiving payroll notices in the legacy tenant | A payroll cancellation and transition notice for ND MHC Management LLC delivered to a person who may no longer work here, **and whether she departed is not established** | Austin | `HUMAN ONLY`: confirming a departure and disabling an identity | Yes, `TD-0487` | Same finding as `CM-02`'s Winnie row at a different address; `TD-0323`, `TD-0324` |
| `KP-0064` | Two dated LP letters carry different gross MOIC, 1.89x and 1.87x | **A fund performance figure that contradicts itself in writing to LPs, with a regulator escalation already threatened** | Austin with Citrin | `AGENT WITH A HUMAN CHECK`: recompute and reconcile, guardrail 6 on anything that goes out | Yes, `TD-0491`, `TD-0496` | Recorded inside `CM-25` |
| `KP-0065` | Royal Oak Vero Beach general liability may have been uninsured since 2026-06-16 | An uninsured community is the cost of being wrong, and **one certificate settles it in a minute** | **unassigned** | `AGENT WITH A HUMAN CHECK`: one email to the broker | Yes, `TD-0488` | None |
| `KP-0067` | Lamberton Lake MHC in Impending Not in Good Standing | **Good standing is what a lender and a title company check**, on an agency financed asset with an insurance renewal in progress | **unassigned** | `AGENT WITH A HUMAN CHECK`: Michigan status is a public record lookup | Yes, `TD-0484` | Pairs with `CM-30` and `CM-29` |
| `KP-0068` | The Bedrock Fund II document base is reachable only through a personal Gmail | Five LPs and a joint venture partner are chasing the 2025 K-1 against **2026-09-15**, and the prior year set sits in a consumer account nobody but Austin can reach | Austin with Albert | `HUMAN ONLY`: only he can reach it, and the extraction has to precede any deactivation | Yes, `TD-0497` | Overlaps `KP-0008`, which is deferred |
| `KP-0072` | The BMHCII archive contains material that cannot be relied on | **Roughly two dozen files are confirmed wrong about the investor or the document type, some copies are truncated so this is data loss rather than naming**, and Khodara's subscription agreement sits under two different names | Austin | `AGENT WITH A HUMAN CHECK`: the hash join against `ns:5655481408` is exactly agent work and **nothing may be deleted**, hard rule 2 | Yes, `TD-0511`, `TD-0512`, `TD-0524`, `TD-0527`, `TD-0528`, `TD-0529` | Extends `KP-0070`, `KP-0071` |
| `KP-0073` | ACH forms with live bank credentials filed inside the folder handed to LPs and counsel | **A books and records production from that folder as it stands hands a hostile partner other investors' banking details**, and folder level share links are still live and unaudited | Austin with Albert | `HUMAN ONLY`: revoking links and moving credential bearing files | Yes, `TD-0524`, and Austin ruled it into the `TD-0511` promotion gate | Sits inside `KP-0072` |
| `KP-0074` | The document search space was never closed: Box, InvestNext, the Murad Dropbox Space | **The InvestNext access log is the only evidence of what each LP was actually sent and when**, which is the document that answers "you never sent me this" on evidence rather than recollection | Austin | `HUMAN ONLY`: three repositories need credentials and an account decision | Yes, `TD-0526` | None |

### P1 Dated, 2 rows

| ID | Short label | Why P1 | Owner | Agent-ability | Task | Duplicate of |
|---|---|---|---|---|---|---|
| `KP-0012` | No list of interested Responsible Contractors exists | **2026-09-30** is Jadian's own annual cycle date, not Austin's | Accounting team, Moe Mehmood proposed | `AGENT WITH A HUMAN CHECK`: the list comes out of the vendor master, keeping it current needs `KP-0011`'s gate | Yes, `TD-0333` | Same package as `KP-0011`, `KP-0013`, `KP-0014` |
| `KP-0036` | Is the Massachusetts settlement the same proceeding as the Auburn rent control matter | The municipal meeting sits around **2026-09-14**, which is the town's date | Natalie owns the call, Austin owns `CM-20` | `HUMAN ONLY`: Natalie already owes Stelmac the call that answers it | Yes, `TD-0344`, `TD-0286` | Lives across `CM-20` and `CM-23` |

### P2 Blocking, 20 rows

| ID | Short label | Who is blocked | Owner | Agent-ability | Task | Duplicate of |
|---|---|---|---|---|---|---|
| `KP-0009` | ParakeetHome against ParakeetHomes | **Albert**, who cannot safely de-duplicate without the copy-both-then-reconcile guardrail in the migration plan | Albert | `AGENT WITH A HUMAN CHECK`: a content diff of the two sites | Yes, `TD-0007`, `TD-0331` | `TD-0007` and `TD-0331` are two tasks for one problem |
| `KP-0010` | The portfolio disagrees with itself on unit count | **Every downstream number**, and the Geiger Key PSA in `CM-22` sits on an asset with four warehouse records | Austin to rule, Zach proposed | `AGENT WITH A HUMAN CHECK`: the comparison is built, the ruling is his | Yes, `TD-0402` | **`KP-0025` is the same finding** |
| `KP-0014` | Scope of the Responsible Contractor Policy is unconfirmed | **`KP-0011`, `KP-0012` and `KP-0013` all shrink by three quarters or vanish depending on the answer** | Zach Schwartz | `AGENT WITH A HUMAN CHECK`: read the filed copy and check the blank effective date and Fund name line | Yes, `TD-0335`, `TD-0417` | Sequence first in the `KP-0011` to `KP-0014` block |
| `KP-0015` | ESG reporting has an owner but no date, and 2H25 and 1H26 are missing | **Jadian**, who requires it and has not been told a cadence date | Zach Schwartz | `AGENT WITH A HUMAN CHECK`: find the two reports or confirm they do not exist | Yes, `TD-0336` | None |
| `KP-0016` | 14 state compliance SOPs at counsel with none signed off | **Natalie's whole Phase 2**, and it is the largest block of finished work in the company behind one gate | Outside counsel via Natalie | `HUMAN ONLY`: counsel sign off | **No task anywhere** | None |
| `KP-0026` | What counts as a reporting property | **Board and LP reporting**, which inherits whichever of two pages someone opens | Not stated | `HUMAN ONLY`: Austin's own reporting instruction governs | **No task** | Related `KP-0010` |
| `KP-0030` | Hunter Springs MHC carrying $35,056 it should not | **Reporting**, and the asset sits inside the live Kippy fee dispute | David Berman | `AGENT WITH A HUMAN CHECK`: one look from accounting | Yes, `TD-0005`, unlinked | Unlinked pair with `TD-0005` |
| `KP-0035` | Is there a separate Belle Haven settlement | **Anyone who needs to know whether a second matter is live**, and it has zero recorded detail | Not stated | `HUMAN ONLY`: one sentence from Austin | **No task** | Spun out of `KP-0032` |
| `KP-0037` | Community dropdown lists inconsistent across all 13 forms, four counts across four documents | **QuickBase wave design and FastField Phase I both**, because every relationship field keys off the community value | **No owner in this Brain** | `AGENT WITH A HUMAN CHECK`: building one master list from the 67 is agent work, ratifying it is not | Yes, `TD-0414`, `TD-0454` | Same root as `KP-0042` and `KP-0050` |
| `KP-0040` | Three systems hold a rehab cost, $274,178 apart | **Anyone quoting a rehab cost**, and the weekly rehabs call has no accountant in it | **unassigned**, Austin to name at the Friday Executive EOS | `AGENT WITH A HUMAN CHECK`: a three way reconciliation | Yes, `TD-0412`, `TD-0517`, `TD-0519` | None |
| `KP-0042` | 37 rehab rows entered through an intake path never onboarded | **Every by-community rollup**, which double counts as a result | **unassigned** | `AGENT WITH A HUMAN CHECK`: the intake standard and the code resolution | Yes, `TD-0411`, `TD-0413`, `TD-0414`, `TD-0517`, `TD-0520` | Same root as `KP-0037` |
| `KP-0043` | The rehab program has never been reconciled against approved capital | **Jon, an LP or a lender**, who must not be quoted the $4.2M or $2.8M as a forecast | **unassigned**, Zach proposed | `AGENT WITH A HUMAN CHECK`: put the two figures side by side | Yes, `TD-0415`, `TD-0521` | None |
| `KP-0046` | One vendor holds 165 of 219 rehab units | **The Responsible Contractor audit due 2026-09-30**, which has effectively one contractor to audit | **unassigned**, Zach proposed | `AGENT WITH A HUMAN CHECK`: the concentration analysis is done, the procurement response is human | Yes, `TD-0411` | Collides with `KP-0011` to `KP-0014` |
| `KP-0049` | Eleven BLOCKING QuickBase decisions never put to a person | **The QuickBase vendor team**, and one unassigned question holds eight of the nine waves | **unassigned**, `TD-0421` routes it to Austin | `HUMAN ONLY`: eleven decisions need people | Yes, `TD-0421`, `TD-0423`, `TD-0424` | None |
| `KP-0050` | The build encodes eight states and this Brain records seven | **The build's state compliance logic**, which cannot lock until West Virginia is settled | **unassigned** | `HUMAN ONLY`: one sentence from Austin | Yes, `TD-0425` | Same root as `KP-0037` |
| `KP-0053` | `WF001` depends on three FastField forms on no register | **`WF001`, in build with the vendor team right now**, with the FastField half most likely Parakeet's and nobody told | **unassigned**, `TD-0430` puts the split to Austin | `HUMAN ONLY`: the delivery split is Austin's | Yes, `TD-0430`, `TD-0431` | None |
| `KP-0054` | QuickBase has no vendor page | **The relationship being set up now**, with no contract, no named owner on either side and **no record of what company data the vendor holds** | **unassigned** | `HUMAN ONLY`: a vendor relationship and a contract | Yes, `TD-0432`, `TD-0433` | Same shape as `CM-02` |
| `KP-0056` | The rehab sheet's own owner says its formulas are blown up | **Four vault pages and the weekly call**, all reading from a source its owner says is broken | Zach Schwartz, asked for by name on the call | `HUMAN ONLY`: fixing the vendor's sheet, and **closed red rows are deliberately retained for deposit purposes**, so a tidy up destroys a reconciliation trail | Yes, `TD-0450` | None |
| `KP-0061` | A 33% partner in Bedrock Group appears in no page | **`CM-26`**, and his consent and information rights have never been checked | Austin | `AGENT WITH A HUMAN CHECK`: build the record from the signature blocks and the master org chart, guardrail 6 on anything that leaves | Yes, `TD-0478` | Same person as `CM-26` |
| `KP-0071` | A disciplined wind down programme has been running since April and this Brain had no record | **Every completeness count on the fund**, which stays a floor until `WP-36` is reconciled | Austin | `AGENT WITH A HUMAN CHECK`: read `WP-36` and `WP-38` and reconcile | Yes, `TD-0507`, `TD-0509`, `TD-0525` | Corrects `KP-0070` |

### P3 Value, 14 rows

| ID | Short label | Why P3 | Owner | Agent-ability | Task | Duplicate of |
|---|---|---|---|---|---|---|
| `KP-0004` | The scorecard cannot be scored | Nothing breaks in a month, and it is already Zach's own Q1 rock with a quarterly review cadence set | Zach Schwartz | `HUMAN ONLY`: targets, units and definitions are his judgement | Yes, `TD-0328`, `TD-0418`, `TD-0443` | None |
| `KP-0019` | The SharePoint permissions model is not additive-safe | A design defect with no evidence of a live breach | Albert | `AGENT WITH A HUMAN CHECK`: effective permissions can be computed from group membership | Yes, `TD-0337` | **Its row body has absorbed `KP-0020`'s text** |
| `KP-0020` | Blank permission rows on target structure folders | Same pass, same person, same absence of a live breach | Blank on this row, **Albert on `KP-0019`'s row** | `AGENT WITH A HUMAN CHECK` | Yes, `TD-0338` | Contradicts `KP-0019` on ownership |
| `KP-0021` | Two of four Master Tracker versions sit on a personal OneDrive | The scoreboard for a 109 process program is partly on one desktop, and nothing stops today | Not stated | `AGENT WITH A HUMAN CHECK`: locate, hash and propose which is current | Yes, `TD-0339` | Overlaps `KP-0051` |
| `KP-0023` | 135 provisioned accounts against 125 employees, 23 with no group | Worth automating, nothing breaks in a month, **and the important half is that a reconciliation report is not a system of record** | Austin with Albert and Demetria | `AGENT WITH A HUMAN CHECK`: the Entra against Paychex diff is a scheduled job, the exceptions need a person | Yes, `TD-0341`, `TD-0342`, `TD-0420` | None |
| `KP-0024` | Justin Minkoff has no access to anything | Deferred by Austin, and the row is the record that it is a decision | Deferred 2026-09-01 by Austin | `HUMAN ONLY`: an access grant decision | **No task, deliberately** | Re-surfaces with `KP-0019` and `KP-0020` |
| `KP-0027` | Occupancy, 82.5% against 77.67% | Different periods and denominators, so it is a labelling job rather than a data problem | Not stated | `AGENT WITH A HUMAN CHECK`: state which answers which question | **No task** | Related `KP-0010` |
| `KP-0045` | 18 open rehabs past the 60 day board goal | The 60 day goal is an internal board goal, and **the ten unit Silver Breeze batch now has a completion date of 2026-09-10** | John Clark | `AGENT WITH A HUMAN CHECK`: the aging is data, the chasing is not | Yes, `TD-0408` to `TD-0410`, `TD-0419` | None |
| `KP-0048` | `cwigfall@parakeetcommunities.com` appears nowhere in this Brain | One question, not a build | Austin | `AGENT WITH A HUMAN CHECK`: draft the question, Demetria answers it | Yes, `TD-0420` | Same class as `KP-0023` |
| `KP-0051` | Two files share `SOP_Master_Tracker_Combined_v2.xlsx`, md5 different | A filing defect, and the fourth master tracker on disk | **unassigned** | `AGENT WITH A HUMAN CHECK`: hash and propose, a human declares which is current | Yes, `TD-0426` | Overlaps `KP-0021` |
| `KP-0052` | 109 processes against 91 SOPs, and no page reconciles them | They are probably counting different things, and saying so costs a sentence | **unassigned** | `AGENT WITH A HUMAN CHECK`: reconcile by definition | Yes, `TD-0427` | Same shape as the FastField 3 against 13 gap |
| `KP-0060` | The ID scheme has no answer for two writers at once | Nothing breaks in a month, **and a surviving duplicate silently routes a close instruction to the wrong row, which nobody has checked for** | **unassigned**, Austin owns the builder | `AGENT NOW`: a collision sweep across the six registers is exactly agent work | Yes, `TD-0476` | None |
| `KP-0069` | `austinrberk@gmail.com` is no longer readable and nothing recorded the trade | Austin says nothing at the top of his mind is in it, and the cost of not looking is bounded | Austin | `AGENT WITH A HUMAN CHECK`: one look | **No task, accepted** | Related `KP-0008` |
| `KP-0070` | The wind down record base duplicates against seven other locations | **Premise corrected 2026-09-03**: the destination is populated and disciplined, and what survives is a reconciliation against `WP-36` | Austin | `AGENT WITH A HUMAN CHECK`: reconcile the duplicate copies | Yes, `TD-0503`, `TD-0504`, `TD-0506` | Corrected by `KP-0071` |

### P4 Noise, 9 rows

| ID | Short label | Why P4 | Agent-ability | Residue |
|---|---|---|---|---|
| `KP-0006` | Lucky Clover armed resident incident | Closed 2026-09-01 on Austin's word | `AGENT WITH A HUMAN CHECK` on the residue | **No trespass, law enforcement or lone worker protocol exists**, `TD-0329`. Duplicate of `CM-07` and `TD-0001`. |
| `KP-0007` | Great Oak boil water notice | Closed 2026-09-01 on Austin's word | `AGENT WITH A HUMAN CHECK` on the residue | **No lift order, vendor confirmation or clearing sample is filed anywhere**, `TD-0330`. Duplicate of `CM-08` and `TD-0002`. |
| `KP-0025` | Unit count conflict C1 | **Duplicate of `KP-0010`**, which has the task and the workbook | `AGENT NOW`: retire it, keep the ID | None |
| `KP-0028` | No financial baseline C4 | Done and never closed: the TTM figures went into the ledger 2026-08-31 | `AGENT NOW`: close it | None |
| `KP-0029` | Lucky Clover's manager C5 | Resolved 2026-08-31, the manager is Angel | `AGENT WITH A HUMAN CHECK` | **The December 2025 org chart and the March 2026 infill sheet are both stale and nothing corrects them** |
| `KP-0031` | Southgate C7 | Recorded so a misreading does not resurface, which is its whole job | `AGENT NOW` | None |
| `KP-0032` | Massachusetts or Florida T1 | Resolved 2026-08-31 within the hour, left in place because its resolution opened three rows | `AGENT NOW` | None |
| `KP-0039` | Board row count disagrees with itself | Closed 2026-09-02, and the fix is the rule rather than the number | `AGENT NOW` | Quote the count from the build output, never from a page that mentioned it earlier |
| `KP-0066` | Where the personal mail lives | Closed and corrected 2026-09-03 within the hour | `AGENT NOW` | The lesson stands: when a search comes back empty, ask which surface was searched |

---

# The ten to put in front of Austin first

**Each is phrased as the question he answers, not as the problem.** Eight of the ten are a disposition, meaning a yes, a no or a name, and they do not need three paths because there is nothing to choose between. **Two are genuine choices and carry three paths with a recommendation**, per the standing rule.

## 1. SOP 302, the lender's wire instructions

> **"`KP-0001` says the lender's wire details are out of SOP 302. `TD-0205` says they are still in it and is assigned to David Berman. Which is true, and who confirms every circulated copy?"**

`KP-0001` was closed 2026-09-01 on his word, *"Updated and information removed."* `TD-0205` is the same work in the to-dos register, still open, owner `David Berman with Natalie Magurne`. **VERIFIED**, both rows read in place. **This is first because it is the only place on the board where two registers disagree about whether a live fraud exposure has been remediated, and the register that says it is fixed is the one with no artefact behind it.**

## 2. Jadian and the management liability binder, and this one has hours on it

> **"Jadian was not consulted on the E and O and D and O package. Do I raise it in the 10:00 Pipeline Review today?"**

He answered *no* to question 2 of the 2026-09-02 close, so **the governance half is now a confirmed fact rather than a suspicion**, and it does not reverse by declining the $43,090.21 binder. `CM-17`. **Nothing has been drafted, guardrail 6 applies, and the difference between today and tomorrow is the difference between a disclosure and a discovery.**

## 3. Counsel still does not know Kippy and Laurence Brokaw are one man

> **"Do I tell counsel today that the man they are running a hostile fee dispute against is the same man who voluntarily reinstated his dissolved LLC so we could cure the Royal Oaks titles?"**

Austin himself answered *"Same person"* on 2026-09-01 (`KP-0033`). `CM-24` contemplates a lien on Royal Oaks and a thirty day termination notice; `CM-19`'s nine title transfers are running inside a reinstatement window that man opened voluntarily and that has no recorded expiry. **`TD-0368` has owned telling counsel since 2026-09-01 and there is no record it happened.** Either lever lands on the person whose cooperation the other row depends on.

## 4. Gregory Khodara

> **"I promised Khodara a written reconciliation on 16 August. Do I send it, or do I tell him why I cannot?"**

`PR-0037`, 18 days, **not kept**. He has since threatened in writing to escalate to a state securities regulator. **A promise closes when the person is told**, so either answer closes it and silence does not. `CM-25`, `KP-0064`. Guardrail 6.

## 5. The 15 September clock

> **"Onyx Holdings needs the BMHCII K-1 to file their own corporate return by 15 September. Do I put that date to Citrin as the deadline, or do I tell Tabish Rizvi now that it will not be met?"**

Twelve days. Five LPs plus a joint venture partner are chasing the same document, none with a reply on file (`CM-25`). **`KP-0068` is the reason it is not a scheduling problem: the prior year K-1 set for that fund sits in a Google Shared Drive reachable only through a personal Gmail identity.** This is the hardest genuine outside date on the whole board and it does not appear on any row's due field.

## 6. The share links on `1. Governing Documents/1.8 Subscription Agreements`

> **"Do I revoke the folder level share links on 1.8 and 4.5 today, before anything else in the wind down moves?"**

`KP-0073`. Three ACH authorization forms carrying live bank routing and account numbers, plus W-9s, are filed inside the folder that gets handed to LPs and counsel for subscription review. **Folder level links already issued still point at it and nobody has audited who holds them or for how long.** Austin has ruled it into the pre-memorialization cleanup gate, which is right and **means the exposure persists in the working folder by design until the gate runs**. Revoking the links is separable from the gate and costs nothing.

## 7. David Berman: seventeen open rows, three of them written today

> **"Seventeen open rows across the six registers still route work to David Berman, and `TD-0504`, `TD-0527` and `TD-0528` were created today. Who takes them?"**

The full list is in the Berman section above. **`TD-0528` is the sharpest: it names him as primary owner of opening and classifying 179 subscription files, and its output is the per investor completeness matrix that a securities examiner and Ridaa Murad both ask for.** This is a real choice, so it carries three paths.

- **Path A, stop the bleeding only.** Re-owner the three rows written today and leave the other fourteen where they are until the exit date is fixed. **Costs**: one hour. **Who**: Austin. **Still exposed when done**: fourteen rows including `TD-0372`, the unread Oregon notice on a fund in wind down, and `KP-0003`, a Critical finding whose only owner is leaving. **Wrong choice if** the exit date lands sooner than the fourteen can be worked.
- **Path B, fix the mechanism.** Add one rule to the board builder: **a row cannot be written with an owner on the departure list**, and make the builder report any existing row that names one. **Costs**: a builder change plus one sweep. **Who**: whoever owns `00-Meta/board-data/builder/`, which is Austin today. **Still exposed when done**: nothing new gets routed to him, and the fourteen existing rows still need a name each. **Wrong choice if** the answer is that some of them genuinely have to be extracted from him before he goes, in which case a block on his name is the opposite of what is wanted.
- **Path C, extract deliberately, then block.** Treat the seventeen as two piles. **Pile one is what only he can produce** and gets pulled forward inside the exit window: the G1 signed entity list behind `CM-13`, the Oregon notice `TD-0372`, the SOP 302 removal `TD-0205`, and the 21st inventory confirmation `TD-0461`. **Pile two is everything else** and gets re-owned now. Then apply Path B's builder rule. **Costs**: half a day of Austin's time to sort, then the builder change. **Who**: Austin, with Demetria on sequencing. **Still exposed when done**: nothing material. **Wrong choice if** the relationship has deteriorated to the point where asking him for four deliverables is not realistic, which is a personnel judgement and sits in the private assessment file.

**Recommended: Path C.** Path A loses `TD-0372` and `TD-0205`, which are the two rows on his list with an outside consequence attached, and Path A's own logic admits it. Path B is correct and incomplete on its own: **a rule that stops new rows reaching him does nothing about the fourteen already there, and `CM-13`'s whole design depends on getting one signed document out of him before he leaves**, so a blanket block would fight the plan Austin already sequenced on 2026-08-31. Path C keeps Path B's builder rule, which is the only part that stops this recurring, and adds the one thing both other paths miss: **deciding on purpose what has to come out of him rather than discovering it after he has gone.**

## 8. Royal Oak Vero Beach may have had no general liability cover since 16 June

> **"Can somebody get me the certificate for Royal Oak Vero Beach, or tell me it was never bound?"**

`KP-0065`. The broker wrote on 2026-06-23 that the policy expired 6/16 with no signed renewal documents; accounting replied the same day that nothing had been received for Royal Oak, only for Crystal Acres. **No later message in either mailbox confirms it was bound.** SINGLE-SOURCE, and stated as unconfirmed rather than lapsed. **One certificate settles it in a minute and the cost of being wrong is an uninsured community.**

## 9. The comparable set in the Massachusetts case

> **"Has anyone told CBRE which comparable set to use, and if not, do I tell them before the report lands?"**

`KP-0034`, `CM-20`. The case turns on whether the resulting rent is a fair market rate, **the comp set decides that number**, and under the path counsel is now executing the comparables go **straight to plaintiffs' counsel** alongside the report. Austin's own words are the only statement of house convention anywhere: *"as we discuss market rents, we usually just say MH and RV vs single family home or apartments."* **Whether that ever reached CBRE is unknown, not assumed, and the window closes when the report lands around 2026-09-11.**

## 10. Nineteen promises to named people are broken

> **"Do I want one sweep this week where every one of the nineteen people is told something, including where the answer is no?"**

This is the second genuine choice, so it carries three paths.

- **Path A, close the cheap ones.** Reimburse Vicky, approve the aerator quote, ship the swag, confirm the two `VERIFY` rows. **Costs**: an afternoon and a small amount of money. **Who**: Austin, Natalie, Demetria. **Still exposed when done**: the twelve that cost money and are parked for budget week are still silent, and **budget week is not a date anybody at a community has been given.**
- **Path B, tell everybody something.** One pass in which every one of the nineteen named people gets a sentence, and thirteen of those sentences are *"this is a budget week decision and here is the date."* **Costs**: half a day of message writing, and it forces a budget week date to exist. **Who**: Austin for the ones he made personally, the regionals for the rest. **Still exposed when done**: nothing is delivered, but nothing is silent either, which is what this register measures. **Wrong choice if** a promise that is answered with a date and then slips again costs more than one that was never answered.
- **Path C, retire the register into the budget.** Take the thirteen budget week rows off the promises register entirely, put them into the 2026 budget as line items with a decision date, and leave the promises register holding only the six that are not about money. **Costs**: a budget session. **Who**: Austin with Zach. **Still exposed when done**: **the person on the other end disappears**, which is the exact failure the register was created to stop, and the register's own founding note says so.

**Recommended: Path B.** Path A is real and should happen inside Path B rather than instead of it, because four kept promises against fifteen silences still reads as fifteen silences to the fifteen people. Path C loses the named person, which is the only field this register carries that no other register has, and it would undo Austin's own 2026-09-01 ruling that created it. Path B is the only one that satisfies the register's own definition of closure, **that a promise closes when the person is told and that "we decided not to" closes one honestly**, and its side effect is the useful one: **it makes budget week a date rather than a category.**

## Three more that are today, or nearly free

Not in the ten because they are smaller, and worth naming because two of them are today.

- **`KP-0058`, the Origins distribution.** The recurring marker *"Monthly Parakeet Origins Distributions Completed"* fell **today, 2026-09-03**, organiser David Berman, and `KP-0038` says the same portfolio is projected cash negative by February 2027 if the current distribution cadence continues. **Nothing anywhere tests a monthly distribution against the forward cash position before it goes.** INFERRED that the two connect; the question is one sentence, whether that check already happens and by whom.
- **`PR-0025`, Vicky at River Oaks.** She fronted her own cash for the bingo machine and has not been reimbursed. **It is the cheapest broken promise on the board and it is flagged for budget week, which is the wrong queue for an employee's own money.**
- **`CM-18`, Citrin.** The reply Austin owes Tim McNamara **already exists verbatim in his own 2026-08-27 21:35 ET message.** It has missed two sends, the schedule behind it has been chased since 2026-03-23, **164 days**, and it blocks final 2025 returns for ND, Cambridge and Mayflower.

---

## Method and confidence

- **VERIFIED**: every tier, owner, quote and date above was taken from the three register markdown files read in full on 2026-09-03, or from a named cross register row read in place. Where a row is quoted, the quote is the register's own text.
- **The Berman list is VERIFIED** against both the markdown owner strings and `board.json`, and the disagreement between the two is reported rather than resolved silently.
- **INFERRED and labelled as such**: the P0 tier on `KP-0033` (the consequence is live even though the question is closed), on `PR-0033` (an unverified leak in an occupied unit), and on `KP-0058` (the register itself labels the connection INFERRED).
- **SINGLE-SOURCE and carried forward as such**: `KP-0038`, `KP-0065`, `KP-0067`, `KP-0069` and everything in `CM-07` and `CM-08` that came out of the road trip review.
- **Not asserted**: what Wallack's view on the Auburn meeting actually says (`CM-23`), what Ridaa Murad's issues are (`CM-26`), what backing Angel looked like (`PR-0014`), and whether Winnie has departed (`KP-0063`). Each is one sentence from a person and none of them is guessed.
- **Nothing in any register was edited.** Every proposal above is a proposal.
