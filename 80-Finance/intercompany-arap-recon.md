# Intercompany AR/AP Reconciliation — Cleanup + Quarterly Process

**What this is:** Eight years of unreconciled intercompany AR/AP, why the one-shot packet failed, and the quarterly process that replaces it.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26. Extended 2026-09-26: a dated block from the closes of 2026-09-22 to 09-25 was added by the Page Update; nothing above it was changed. **Extended 2026-09-29: the section "Where the program actually stands" at the bottom is the current state, written at the Intercompany project's close-out; the plan above it (sections 1 to 8) was written before the reconciliation ran and several of its premises no longer hold, each named there. The operating manual for the live program is `80-Finance/intercompany-operating-rules.md`.**

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

**Created**: 2026-08-26
**Requested by**: Austin, 2026-08-26 — *"Add intercompany AR/AP recon. I need to bring this up to moe to help and create a plan to have this updated quarterly. this is going to be a big lift as we have to review 8 years of activity before getting things tied out."* VERIFIED (Austin's own words)
**Working owner (proposed)**: Moe Mehmood — **not yet asked**. Nothing in this file is agreed with Moe or Berman.

**SEQUENCING SETTLED 2026-08-31.** The extraction happens **before** the Berman exit, not after. Austin, on the delegation board: *"We are pushing on this now prior to the exit to avoid any risk."* VERIFIED (Austin's own words). This matters to this plan specifically: the unanswered elimination-ledger objection on JE-6 and JE-7, $2.7M of the $5.4M, is knowledge that walks out of the building with the controller. The board had raised the sequencing as an open recommendation; it was already decided, and the registers did not know. `00-Meta/commitments.md` items 13 and 16.
**Evidence tags**: VERIFIED = primary source read. SINGLE-SOURCE = one place, unconfirmed. INFERRED = reasoning. PROPOSED = a design choice in this plan, not a fact.

Related: [[99-Archive/2026-08-catchup/berman-journal-entries-thread]] · [[10-Business/entity-structure/berk-inc-umbrella]] · [[99-Archive/2026-08-catchup/PRIORITY-LIST]] · [[00-Meta/decisions/2026-08-26-storage-target-state]]

---

## 1. The problem, plainly

**Eight years accumulated because intercompany was never a step anyone owned on a recurring calendar.** Rent Manager carries the detail under **12100 Inter Company Receivable** and **21100 Inter Company Payable**, with child accounts named for the *counterparty*, not the booking entity, under naming conventions that are actively counterintuitive ("X" vs "X II" vs "PO X"). VERIFIED — memory note `intercompany-account-conventions.md`. Nothing forces the two sides to agree, so a one-sided entry costs nothing at the moment it is made and compounds forever.

**The one-shot attempt already ran, and it produced an argument rather than a reconciliation.** Full evidence in `99-Archive/2026-08-catchup/berman-journal-entries-thread.md` (12 messages, 7/27–7/29/2026, every message read). What happened:

- Austin sent a finished packet — `Accounting_Action_Packet_v3_FINAL_2026-07-27.xlsx`, **six** entry sets (JE-1, 2, 3, 5, 6, 7; JE-4 was a **$0.02** keying difference waived the same day), ~**$5.4M** — with the ask *"once these are posted, please let me know."* VERIFIED
- Berman replied every time, within 1h41m / 4min / 10h06m / 18min. This was never silence. VERIFIED
- He raised a **legitimate technical hold on 7/28**: the workbook touches the **elimination ledgers**, which he says are financial-reporting-only and *"should never have touched anything relating to entities outside"* the MHC consolidation. That objection lands on **JE-6 and JE-7 — $2.7M of the $5.4M — and is still unanswered in writing.** VERIFIED
- It then stalled on **sequencing**, not substance: Berman asked for a couple of hours and a walkthrough as a precondition; Austin answered *"Hours is a large ask… Let me know when you get those 7 or so Journals recorded."* Austin conceded on 7/29 and offered 2:00 PM; Berman accepted in 18 minutes. **The written trail ends there.** The outcome of that call is unknown — Teams transcripts are blocked tenant-wide, so a verbal resolution would be invisible. VERIFIED (the trail); INFERRED (that a verbal resolution is plausible)

**Three structural lessons this plan has to absorb:**

1. **A packet is not a process.** Delivered as a demand to post, a packet transfers risk to the controller with no shared basis. He correctly refused to take it.
2. **The claim outran the work.** *"These 7 entries should create a 100% confirmed reconciliation"* is stronger than the packet supports — **JE-1 and JE-5 are under-specified** (JE-5 is explicitly a *"target end state, accounting drafts mechanics"*), and **three residuals — $5,788.90, $14,845.11, $500 — survive posting.** VERIFIED. One overstated claim cost more credibility than the entries were worth.
3. **The entity count is a live factual dispute Austin loses on the record as written** — **288** in the request email, **235** in his own rebuttal two days later, and Berman: *"there aren't even that many active and inactive entities in RM."* VERIFIED. Three numbers, two of them Austin's.

**The design conclusion**: fix the process, and fix it so the sequencing standoff cannot recur. The same friction is still running 28 days later in a different thread — on 8/26 Austin declined a Berman invite titled *"AR/AP Continuation"* and wrote *"Please provide me with the AR/AP that I have been asking for."* VERIFIED. This is a repeating pattern, not a one-off.

---

## 2. Gating prerequisites — nothing starts until these are true

### G1. A definitive entity list with EINs — **the hard gate**

You cannot reconcile between entities nobody has definitively enumerated, and the 288/235/neither dispute is the direct symptom. The only consolidated map found anywhere is **`Org Chart Overview.xlsx`** in Dropbox `ns:11855305057//Austin Berk/` — **dated 2020, broken formula columns, ungoverned, sitting in a personal folder in a tenant that is otherwise cold storage.** It does carry domiciles, ownership percentages, EINs, and 58 named LP investors. VERIFIED — `10-Business/entity-structure/berk-inc-umbrella.md`.

**Deliverable**: one governed list, one row per entity — legal name, EIN, Rent Manager entity code, status (active / inactive / dissolved / final return filed), and **in-scope-for-recon Y/N with the reason**. Reconcile the 2020 workbook against `Org Chart Overview_122023.xlsx` (OneDrive root); treat anything after 2023 as unknown rather than assuming continuity. **Berman signs it** — he is the one disputing the count, so his signature ends the dispute permanently. PROPOSED

**Until G1 exists, every number produced is arguable.** Do not start Phase 1 without it.

### G2. A written ruling on the elimination ledgers

Berman's 7/28 objection is the single most important open item in the workstream. It must be answered in writing and settled as a **standing rule** — are elimination-ledger balances in scope for cash-relevant intercompany recon, yes or no — not re-litigated every quarter. Berman rules; Citrin confirms if it touches consolidation reporting. **Whatever the answer, it determines whether JE-6 and JE-7 are ever postable in their current form.** VERIFIED (the objection); PROPOSED (settling it as a standing rule)

### G3. A counterparty crosswalk for 12100 / 21100 children

Every child account under 12100 and 21100 mapped to the entity from G1. The naming conventions are non-obvious and have already been verified by reciprocal amount matching. This is mechanical, it is **Moe's first deliverable**, and it is the thing that makes every later wave fast. VERIFIED (the conventions); PROPOSED (the ownership)

### G4. Ground truth on what is already posted

Pull the Rent Manager journal register for memo **`IC cleanup — Action Packet 7/27/26`**. Nothing in email or Teams confirms any JE was posted, but **absence of a written confirmation is not proof nothing was posted** — Berman said on 7/29 he was "looking over those few spots this AM." VERIFIED (the absence); INFERRED (that the register settles it). Do not assert non-completion until this is run.

### G5. A stated close calendar

Books are described as closing **30–45 days in arrears**, and accounting is described internally as a "black box." SINGLE-SOURCE — from Austin's framing of this request; not corroborated in the vault. The quarterly cadence in §4 is built on that lag and **must be re-based if the real lag differs.** A ClickUp month-end close list already contains a step literally named *"Reconcile Intercompanies"* — VERIFIED, `99-Archive/2026-08-catchup/clickup.md`. That step is the hook to attach this to; it exists and is not being executed.

---

## 3. Phase 1 — the historical cleanup

### 3.1 Direction: newest to oldest

**Recommended, and it is not the intuitive order.** PROPOSED, with reasoning:

- Recent balances are **collectible, auditable, and still have live counterparties** — a 2025 or 2026 imbalance can be funded, netted, or distributed. A 2018 imbalance mostly cannot; it is a write-off with a tax question attached.
- Recent balances are what the **A2Z/Bedrock wind-down and the current audit actually need.** Old years gate nothing.
- The people who can explain a 2025 entry still work here. The people who can explain 2018 largely do not — institutional knowledge sits in `/sites/UserArchive` and departed employees' drives. VERIFIED — `99-Archive/2026-08-catchup/superseded-brain-CLAUDE.md` Known Problems #6.
- Oldest-first spends the most effort on the least recoverable dollars and delivers nothing usable until the very end. That is exactly how a project like this dies.

### 3.2 Waves

| Wave | Period | Disposition | Why |
|---|---|---|---|
| **W1** | FY2026 YTD + FY2025 | **Must tie.** Real balances, real settlement. | Feeds the wind-down and the current audit; counterparties live |
| **W2** | FY2024 + FY2023 | **Must tie.** | Audit-relevant; D-4 lives here (2023 CRZ cleanup) |
| **W3** | FY2022–FY2019 | **Mixed** — tie what has a live counterparty, write off the rest under §3.3 | Diminishing recoverability |
| **W4** | FY2018 and prior | **Write-off zone.** One schedule, one approval, one entry per entity pair. | Not worth line-by-line adjudication |

**Do not run W2 until W1 has actually closed with a posted entry and a signed package.** The point is proving the loop works before scaling it.

### 3.3 Materiality thresholds — standing rules, not case-by-case calls

**JE-4 was waived over $0.02 — as a same-day judgment call, on one item.** VERIFIED. That should never have required a decision. Make it a rule:

| Per entity-pair variance | Treatment | Approver |
|---|---|---|
| **< $100** | Auto-waived. One tolerance line, never itemized, never discussed. | None — standing rule |
| **$100 – $5,000** | Batched onto one write-off schedule per wave, one line each. | Berman, in bulk |
| **$5,000 – $50,000** | Documented reconciling item: source journal ID, both sides, proposed treatment. | Berman, individually |
| **> $50,000** | Full walkthrough per §4.3 + named owner. | Berman posts, **Austin approves** |
| **> $250,000, or crossing a filed tax year / final return** | As above **plus Citrin** on treatment before anything posts. | Berman + Austin + Citrin |

All thresholds **PROPOSED**. Basis: the $0.02 waiver precedent, and the three residuals the packet left alive ($500 / $5,788.90 / $14,845.11) — under these rules the $500 auto-waives and the other two batch, instead of each becoming a conversation. **Berman should set the final numbers.** He is the controller, he will enforce what he sets, and having him pick them is the cheapest available way to give him ownership of the process.

### 3.4 Separate "must tie" from "will be written off" — from day one

Two ledgers, maintained separately for the whole cleanup:

- **TIE list** — both entities active, balance real, cash or equity will actually move. Full adjudication. Success = both sides zero.
- **WRITE-OFF list** — one side dissolved, has filed or will file a final return, or the balance is below the adjudication threshold. One schedule, a tax-treatment ruling, one entry. Success = documented, approved, gone.

**Sorting an item into one list or the other is a decision, and it is Berman's, not Moe's.** The tax consequence of a write-off is real: Berman's own unresolved 7/13 Cambridge binary is the live example — *"either Parakeet needs to formally write off receivables and take a P&L hit on the books at MHC for revenue it didn't collect or Cambridge needs to not file a final return so that it can pay the money back in 2026."* VERIFIED. Cambridge also carries a **$242,942.16** inter-entity payable to be inherited by A2Z and an **unsigned A2Z↔Cambridge contract**. VERIFIED — `99-Archive/2026-08-catchup/meetings-and-transcripts.md`. **Cambridge is not a hypothetical; it is W1 scope and it has been silent six weeks.**

### 3.5 Effort — an estimate, labeled as one

**No effort figure here is a fact.** INFERRED throughout. Basis and the honest confidence level:

- The **extraction** side is fast and already demonstrated. Austin's 7/27 message describes reading every intercompany transaction across the entity population — *"all 67,000 of them going back to 2016"* — in an afternoon. VERIFIED as a claim Austin made; **not independently validated**, and Berman disputes the entity population it ran over. Call it hours per wave, not weeks.
- The **human adjudication** side is the entire cost, and it is unmeasured. The one data point available: the 7/27 packet produced **6 entry sets from a single 2026-06-30 cut**, and **four weeks later not one is confirmed posted.** VERIFIED. The bottleneck is review, ruling, and posting — not analysis.

**Recommended approach instead of a committed date**: **timebox W1 to six weeks** at roughly one dedicated day per week of Moe's time, then **re-forecast W2–W4 from W1 actuals.** Track hours on W1 specifically so the re-forecast is grounded. Anyone committing to an 8-year completion date before W1 closes is guessing.

**What the estimate depends on** — state these to Moe and Berman explicitly:
1. G1 landing. An unsettled entity list makes every wave re-runnable and therefore unbounded.
2. G2 landing. An unresolved elimination-ledger question re-blocks $2.7M-class entries every single wave.
3. Berman's actual review capacity — the true constraint, currently unquantified.
4. Whether the 2020 org chart's EINs survive contact with reality.

---

## 4. Phase 2 — the quarterly process

### 4.1 Calendar

Anchored to close finishing ~45 days after quarter end (G5 — **re-base if the real lag differs**). PROPOSED:

| Milestone | Day after quarter end | Q1 (3/31) | Q2 (6/30) | Q3 (9/30) | Q4 (12/31) |
|---|---|---|---|---|---|
| Close complete, data pull | +45 | May 15 | Aug 14 | Nov 14 | Feb 14 |
| **Package issued** (Moe → Berman, cc Austin, Jon) | +60 | May 30 | Aug 29 | Nov 29 | Mar 1 |
| Controller response due, in writing | +70 | Jun 9 | Sep 8 | Dec 9 | Mar 11 |
| Disputes resolved or escalated | +75 | Jun 14 | Sep 13 | Dec 14 | Mar 16 |
| **Entries posted, package signed** | +90 | Jun 29 | Sep 28 | Dec 29 | Mar 31 |

**First live cycle: Q3 2026 — package due 2026-11-29.** Phase 1 waves run in parallel; the quarterly loop does not wait for the backlog to finish. Use a standing 30-minute slot on the existing weekly **Finance & Accounting EOS Meeting** (Berman's recurring series — VERIFIED) during package weeks. No new recurring meeting. Austin attends only the escalation slot.

### 4.2 Inputs and outputs

**Inputs**: Rent Manager 12100/21100 detail by entity for the quarter · the G1 entity list · the G3 crosswalk · prior-quarter open reconciling-item log · prior-quarter residuals.

**Outputs**: the quarterly package (§6) · posted journal entries · an updated open-items log with **a named human owner on every line** · a signed sign-off page.

### 4.3 The anti-standoff rule — **the single most important design element**

> **No proposed entry ships without its walkthrough. Ever. No exceptions, including "it's obvious."**

Every proposed entry carries, in the package, before anyone is asked to post anything:

1. Both sides of the pair, with **source journal IDs**, so the controller can pull it himself in under a minute
2. The accounting rationale in plain sentences
3. **An explicit split of what is mechanical vs. what is accounting judgment** — exactly where JE-1 and JE-5 failed; they handed judgment back without saying so
4. Any residual that will survive posting, named and quantified up front
5. A **named 30-minute slot already offered** on the cover — asked for, not parked. Austin's own 8/26 note is the standard: *"Most people ask when someone is available instead of parking time."* VERIFIED

And the reciprocal rule, which is what actually ends the standoff:

> **"Post it first and I'll explain after" is not an available request.** If the controller says an entry is not specified well enough to post, that is a **valid, non-escalating response** and it returns to Moe for respecification. It is not a dispute, it is not obstruction, and it does not go to Austin.

### 4.4 Dispute escalation

| Step | Who | Clock |
|---|---|---|
| 1. Objection raised **in writing**, naming the entry and the reason | Berman | By +70 |
| 2. Written response | Moe | 5 business days |
| 3. Still open after one round → **30-minute call**: Moe + Berman + Austin. Austin decides. | Austin | Within 5 business days |
| 4. GAAP / tax / final-return questions bypass step 3 entirely | Citrin | As scheduled |

**Nothing reaches Austin until it has survived one full written round.** That is the mechanism keeping this from becoming his job again. Note that verbal resolutions are invisible in this tenant — **Teams transcripts are blocked tenant-wide** (VERIFIED), which is precisely why the 7/29 2:00 PM outcome is unknown today. **Every call resolution gets a same-day written confirmation into the package.** Non-negotiable.

---

## 5. Roles

| Person | Owns | Explicitly does not |
|---|---|---|
| **Moe Mehmood** — working owner | The crosswalk; the quarterly pull; building the package; the reconciling-item log; drafting entries with walkthroughs; chasing counterparty detail; tracking residuals; timing W1 for the re-forecast | Decide accounting treatment. Decide tie vs. write-off. Post entries. Negotiate with Berman without a written record. |
| **David Berman** — controller | Sets the materiality thresholds. Rules on elimination ledgers (G2). Signs the entity list (G1). Sorts tie vs. write-off. Approves and posts. Signs the quarterly package. | Build the package. Do the extraction. |
| **Austin** — **deliberately narrow** | Approvals above the $50K threshold. Disputes that survive one written round. Unblocking G1. That is the whole list. | Build files. Chase. Draft entries. Attend working sessions. Be the reconciler. |
| **Jon Wyss** — informed | Business context on where balances shake out and how funds move | Execute |
| **Citrin Cooperman** — advisory | Tax treatment on write-offs, final returns, D-3 | Own the recon |

**Sign-off**: **Berman signs every quarterly package as controller.** **Austin countersigns two things only** — the write-off schedule, and any single item above the $50K threshold. PROPOSED

**Why Austin's role is drawn this tightly**: he already tried to own this and it consumed him without producing a posted entry. His own words on 7/28 — *"Hours is a large ask"* — are a real constraint, not an attitude, and the design has to respect it rather than fight it. INFERRED

**Moe's capacity is a real question, not a formality.** He is already working adjacent ground — the *"Outstanding Payables Information"* thread (Berman → Jon/Moe 8/19; Moe filled it out 8/20 20:21) plus a Royal Oaks payables preview on 8/24. VERIFIED. **Ask what comes off his plate before assuming he has a day a week.**

---

## 6. The artifact

**One workbook plus a one-page cover, per quarter.** File: `IC_Recon_YYYY-Qn_vN.xlsx`. Journal memo convention: `IC recon YYYY-Qn` — consistent and greppable in the RM register, so "is it posted?" becomes a query and never an email.

| Tab | Contents |
|---|---|
| **Cover / READ ME** | What ties, what doesn't, what's proposed, what's disputed, the offered meeting slot, sign-off block. One page. |
| **Pair Tie-Out** | Every in-scope pair from G1: both sides, variance, status, tolerance flag |
| **Reconciling Items** | Above-threshold variances with source journal IDs and proposed treatment |
| **Entries to Book** | Proposed entries — **each with its §4.3 walkthrough, mechanical-vs-judgment split, and residuals** |
| **Write-Off Schedule** | Batched sub-threshold and dead-counterparty items, one approval |
| **Decisions Open** | **Every line carries a named person. A line without an owner is not a valid line.** |
| **Residual Log** | What survives posting and rolls to next quarter |
| **Sign-Off** | Berman; Austin where §5 requires it; date |

**Where it lives**: **SharePoint Birdcage** (`/sites/ParakeetBirdcage`) — the decided system of record for everything manufactured-housing as of 2026-08-26. VERIFIED — `00-Meta/decisions/2026-08-26-storage-target-state.md`. Proposed path `Accounting & Finance/Intercompany Recon/YYYY-Qn/`. **Do not file to the A2Z Dropbox tenant, to OneDrive root, or to a personal folder** — that is exactly how the 2020 org chart became ungoverned and how the packet's four reference files became unretrievable. PROPOSED (the path); VERIFIED (the destination decision)

**One hard rule, taken straight from the failure**: **no item is filed without a named human owner.** D-4 below is the counterexample, and it cost the largest open number in the packet a year of nobody looking at it.

---

## 7. Immediate next actions

**In order. The first three unblock everything else and none of them require this plan to be approved first.**

1. **Answer Berman's elimination-ledger objection in writing.** Unanswered since 7/28. It bears on **JE-6 and JE-7 — $2.7M of the $5.4M** — and until it is answered a careful controller should not post them. Answer it as a standing rule (G2), not a one-off rebuttal. **Owner: Austin, with Berman ruling.** Highest-value single action available.
2. **Find out what came out of the 7/29 2:00 PM call.** Berman accepted it in 18 minutes and the written record stops there; transcripts are blocked, so a resolution would be invisible. **Ask him directly — do not chase as though nothing happened.** In the same pass, pull the RM register for memo `IC cleanup — Action Packet 7/27/26` (G4) before asserting nothing was posted. **Owner: Austin.**
3. **Assign an owner to D-4 — EKEET, $1,147,531** ("2023 CRZ Cleanup," J17405, 12/31/23; one-sided receivable from Hold Co with no KEET mirror). The packet assigns it to *"whoever prepared the 2023 cleanup"* — which is nobody. **Largest open dollar figure in the packet and it has no owner.** Berman or Citrin should be able to name the preparer in one message. **Owner: Austin to ask; Berman to name.**
4. **Ask Moe.** He has not been asked. Bring him §5, §3.2, and the W1 timebox — and ask what comes off his plate.
5. **Settle the entity count before it is raised again** (G1). Say **six entries, not seven**, and one entity number, not two.
6. **Close D-3 while it is cheap** — Lucky Clover, $541,680, routed to Austin + Citrin, flagged non-blocking. Non-blocking items that sit become blocking items later.

---

## 8. Risks

**R1 — This stays Austin's to push. HIGHEST.** Every prior attempt was Austin building the file, Austin sending it, Austin chasing four times in 48 hours. The design mitigates it — Moe owns the build, disputes need one written round before reaching Austin, Berman sets the thresholds he will enforce — but **the mitigation only holds if Austin does not step back in when a quarter slips.** The tell will be the first missed package date. If Austin builds that package himself, the process is over and this document was theater. INFERRED

**R2 — The entity list never settles.** G1 depends on a **2020 workbook with broken formula columns in an ungoverned personal Dropbox folder** as the only consolidated map in existence. VERIFIED. If Berman won't sign a list, there is no denominator, no tie-out, and no way to say "done" — and the 288/235/neither argument reruns every quarter forever. **This is the gate; treat a stall here as a stop, not a delay.**

**R3 — The wind-down forces decisions before the history is clean.** The A2Z/Bedrock wind-down is in progress and final returns are the forcing function. **Cambridge is the live instance**: $242,942.16, an unsigned contract, and a binary silent since 7/13. VERIFIED. Related: the A2Z ND Portfolio Partners equity schedule blocks final 2025 returns for ND, Cambridge, and Mayflower, open since 2026-03-23. VERIFIED. **Some balances will have to be decided on incomplete history.** Mitigation: W1 runs newest-first precisely so wind-down-relevant years are clean first — and every forced decision gets logged in `00-Meta/decisions/` with what was and wasn't known at the time.

**R4 — Method trust.** *"Is this an AI bot you assigned to look this over?"* and *"Let's just generally agree to not have bots look at this coming up with nonsense."* VERIFIED. Whatever the merits, that is the environment. Mitigation: **Moe is the human face and the named preparer**; the walkthrough is the proof; tooling stays invisible in the package. Do not re-argue the method — ship a package that survives being checked.

**R5 — Moe's capacity is unverified.** He is live on the payables workstream. VERIFIED. Assigning him a day a week without removing something is the most common way a plan like this quietly fails.

**R6 — Verbal resolutions vanish.** Teams transcripts are blocked tenant-wide, and this workstream has already lost one resolution to it. VERIFIED. Mitigation is the §4.4 rule: same-day written confirmation of every call outcome, into the package. If that rule lapses, the process reverts to email archaeology — which is what produced this file.

---

## Proposal to Citrin, 2026-09-23

*Added 2026-09-26 by the Page Update from the daily closes of 2026-09-22 to 09-25 (`00-Meta/daily-close/2026-09-22.md` to `2026-09-25.md`). Confidence labels are the closes' own; the primary messages were not re-opened this run. Figures in `00-Meta/numbers-ledger.md`.*

**Austin's proposal is with Citrin: combine AR and AP intercompany into one GL per entity under 12000 as Due To / Due From**, so a net position gets reviewed instead of two accounts reconciled. Recorded at the 2026-09-23 close. This changes the account structure the plan above was written against, which is why it is recorded here rather than only in the register. Citrin's answer is not yet on record.

## Where the program actually stands, 2026-09-29 (Intercompany project close-out)

*Written 2026-09-29 evening ET at the close of the Intercompany Matrix project session. The project's own files carry a 9/30 date stamp (its clock is UTC); the book dates are 8/31/2026 (closed month) and 9/30/2026 (preliminary). Every figure named below is in `00-Meta/numbers-ledger.md`, section "Intercompany reconciliation, v21". Labels: VERIFIED = read from the Rent Manager general ledger exports on both books; STATED = Austin's own ruling; PROPOSED = a plan waiting on a decision.*

**How it ran, against the plan above.** The eight year cleanup did not run newest to oldest in waves with Moe building a quarterly package. It ran as one Claude project (Intercompany Matrix, 2026-09-14 to date) working every pair of books from inception: manual accrual GL exports of all 210 Rent Manager books into `C:\Users\AustinBerk\Documents\Claude\Projects\Intercompany\`, a pair engine that nets every intercompany receivable and payable per counterparty and compares each book's net to the counterparty's, one tab per broken pair with every line since inception, and import CSVs that **Austin posts himself** in Rent Manager, then re-exports the touched books so every leg is verified against the ledger. VERIFIED (the files); the method is Austin's rule of 2026-09-20 (`intercompany-operating-rules.md`). Entries 1 to 146 plus 168 and 169 are posted and verified leg by leg; 134 and 147 to 167 are held. The G1 entity list question is moot in practice: the test runs on every book with a general ledger, 210 of them, and the pair universe is 570 pairs at 8/31/2026. G2 is moot too: the three elimination books (EFII, EKEET, ETHC) are out of the test on Austin's 2026-09-28 ruling. STATED.

**Where the numbers are (8/31/2026, matrix v21).** 570 pairs, 234 still broken, gross difference 13.85 million, of which 11.82 million is outside book against outside book (A2Z, Bedrock, Grove Banyan, Kippy, legacy) and is not Parakeet's exposure. Parakeet against Parakeet has 51 broken pairs; **Parakeet against external is down to 6 broken pairs**, five of them Hunter Springs and the sixth the Meadow Woods 100,000 EMD (Austin and Jon). VERIFIED, engine ties the matrix to the cent on every pair. Files: `GL Compare 8-31-2026 v18.xlsx` (master) and its two carve outs, `Intercompany Matrix 8-31-2026 v21.xlsx`, `Intercompany Matrix 9-30-2026 prelim v17.xlsx`, `Intercompany Balance Map KEET PC 9-30-2026 v16.xlsx`, `Parakeet Exposure 9-30-2026 v17.xlsx`, `Outstanding List 9-28-2026.md` (start there), `README - Intercompany folder 9-28-2026.md` (index).

**The bridge Austin asked for on day one now exists.** `Parakeet vs External Settlement Plan 8-31-2026 v1.xlsx` (same folder; project doc `claude/settlement-plan-parakeet-vs-external-9-30-2026.md`) answers his 2026-09-29 question, clean up as much of Parakeet vs external as possible while moving as little cash as possible: 109 balances between Parakeet books and 44 outside books in 9 owner groups; paid as booked they move 5.19 million; netted inside each owner group they move 3.62 million with nothing paid out by Parakeet; after settling A2Z (Austin's own books) and Fund II (Close It Down waterfall) on paper, 2.11 million is left to collect from third parties (Baker, Kippy's Royal Oaks and Crystal Acres, POST's Mayflower, Grove Banyan, PO), each convertible to a note. The American example from the project brief is the mechanism: American's 536,914.07 receivable from Parakeet Homes sets off against what American owes KEET, PC and PFG. PROPOSED; eleven decisions on the workbook's Decisions tab, none answered, nothing posted from it.

**Held and handed off.** Hunter Springs (HSRC sold the park to Kippy's HSMHC 8/29/2024): the sale date cut is in `Workpapers\Hunter Springs Sale Date Cut 9-29-2026.xlsx`, entries 147 to 167 are held, and Austin ruled 2026-09-29 that it goes to internal resources for review; reviewer not yet named. STATED. KEET / Lucky Clover 541,680: proven by the 5517 August 2025 bank statement to be a classification break only (KEET booked equity, Lucky Clover booked a loan); loan or contribution is a decision for Austin and Jon with the CPAs, nothing sent to Citrin yet. VERIFIED (statement read), STATED (hold). KEET / Meadow Woods 100,000 EMD: Austin and Jon.

**What changed in the roles.** David Berman is no longer with the company (Austin, 2026-09-28). Sections 5 to 7 above name him as controller, approver and signer; those roles are unassigned. The two items that waited on his answer (J18190 insurance true ups, entry 134; J17446) now need paper: the premium invoice behind KEET J22052, the 5222 August 2025 statement, the Q3 2025 true up workpaper, Citrin's 2024 AJE list. Moe was never asked to own the package; the quarterly process in section 4 is not running. Austin's 2026-09-23 proposal to Citrin (one Due To / Due From account per counterparty under 12000) is still unanswered on the record.

**Update 2026-10-03, the 9/30 close pull (v22).** Austin re-pulled every book (230 files, 210 with lines) into `GL Exports\GL 10032026` through 9/30/2026; the set was rebuilt as v22 (`GL Compare 8-31-2026 v19.xlsx` and its carve outs, `Intercompany Matrix 8-31-2026 v22.xlsx`, `Intercompany Matrix 9-30-2026 v19.xlsx`, `Intercompany Balance Map KEET PC 9-30-2026 v17.xlsx`, `Parakeet Exposure 9-30-2026 v18.xlsx`). Figures in `00-Meta/numbers-ledger.md`, section "Intercompany reconciliation, v22". Three things worth knowing here. First, 8/31 is restated at 235 broken pairs, 13.83 million, because the Fund II session (10/1 to 10/2) rolled entry 78 back and replaced it with entry 170 dated 9/30, so KEET/Wolf Bay Holdings and KEET/Wolf Bay each show 8,211.81 at 8/31 and zero at 9/30; Bedrock Group / Valley View closed. VERIFIED. Second, 9/30 is now a full set, not a prelim: 235 broken, 14.29 million, **Parakeet against external still 6 pairs, 236,030.54** (the five Hunter Springs pairs and Meadow Woods); the only new breaks are September journals on outside books (two Fund II wind down journals for the Close It Down log, and a 50,000 PO Ocean to PO Bay Oaks I cash transfer booked to the pre PO account names, Outstanding List question 14, proposed reclass, nothing cut). Whether Accounting has locked September is not confirmed; until it is, 9/30 is "as pulled 10/3". Third, a process catch: four books (KEET, KEETII, JBJ, SOUTH) exported on cash basis the first time with the setting reading accrual, and the completeness check does not catch that; the Type mix does (no BILL or CHARGE lines). The check is now in the pull list. The Settlement Plan has not been re-run on 9/30 balances yet; it waits on the September lock. Nothing posted this round beyond entry 170 (Fund II session).

**Open on this page from the plan above, status at 2026-09-29:** 7/29 call outcome and G4 (was anything from the July packet posted): superseded, the project rebuilt every pair from the ledger and posted its own entries. Close lag (G5): unconfirmed. Moe's capacity: not asked. Entity count: 210 books with a ledger at 8/31/2026.

## Open questions

- What actually came out of 7/29 2:00 PM? (blocks knowing the true starting position)
- Is anything from the packet posted? (G4)
- Is the 30–45-day close lag accurate? (G5 — the entire §4.1 calendar rests on it)
- Does Moe have capacity, and what comes off his plate?
- Correct entity count and scope: how many entities are genuinely in scope for intercompany, as against merely existing in Rent Manager?
