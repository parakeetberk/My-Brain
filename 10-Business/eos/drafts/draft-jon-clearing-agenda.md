# DRAFT — Jon Wyss clearing meeting agenda

**Status**: Not sent. Working agenda for a single meeting to clear the standing decision queue.
**Drafted**: 2026-08-26
**Backing detail**: `10-Business/eos/drafts/jon-decision-items-extracted.md` — all 13 groups characterized, with register entries, downstream effects, and the sheet's own recommendation for each.

**Framing**: every one of the 13 already carries a written recommendation and a one-line rationale. This is a confirm-or-override session, not a design session. Budget 45 minutes.

---

## 0. Ask this first — it may collapse the whole agenda

**"Did you already rule these on August 15th?"**

`SKILL.md` section 13 contains all 13 recommendations verbatim, headed **"Presentation standards (Jon rulings 2026-08-15, from the standardization decision sheet)."** The decision sheet itself still lists them as "Decisions needed."

Both files were modified 2026-08-15 — the sheet at 07:43, `SKILL.md` at 07:50, seven minutes apart.

So either the rulings were given and the sheet was never updated, or the runbook was written ahead of the ruling. **The files cannot tell us which.** If Jon says he ruled them, the entire standardization block is a stale document rather than a real dependency, and the meeting is over in five minutes.

---

## 1. The 13, in unblock order

Ordered by how much each retires — register entries closed, workstream files touched, and whether it sits on a hard gate. **The sheet applies no priority markers of its own; this ordering is inferred.**

| # | Group | Retires | Blocks |
|---|---|---|---|
| 1 | **G8 — Audit Trail standard kit** | 6 entries | WS4, WS6, WS8. Parts (c) and (d) literally define "this report is finished." Packaging cannot be finalized without it. |
| 2 | **G2 — Land tab presentation kit** | 5 entries | WS5, WS3, WS4. Sits on the hard land gate at build step 4 — nothing wires until land basis is ruled. |
| 3 | **G1 — Subject corroboration device** | 3 entries | Widest per-line reach; every empirical line on every tab. Also the anonymization rule for named sister assets. |
| 4 | **G5 — Entitlement card format** | 5 entries | WS3, WS4 |
| 5 | **G3 — Land-value levers table** | 3 entries | WS5, WS3. Note: deliberately standardizes the *table*, not the *basis* — basis stays a per-asset call. |
| 6 | **G9 — Internal pane standards** | 3 entries | WS8, internal/external split at packaging |
| 7 | **G12 — Foot-fault carry behavior** | 2 entries | Doctrine. Resolves the DR-084 post-ship accrual anomaly. |
| 8 | **G7 — Log-row citations** | 1 entry | Adds a standing WS6 check |
| 9 | **G13 — Growth model citation form** | 1 entry | WS3 |
| 10 | **G4 — Survey sheets at FINAL** | 1 entry | WS8 packaging; file weight |
| 11 | **G10 — Pool and deck granularity** | 1 entry | WS7, KML workflow |
| 12 | **G6 — Provenance tags** | 1 entry | WS3, WS4 |
| 13 | **G11 — Aside punctuation** | 1 entry | Style only. Promotion of an existing "prefer" to a standard. |

**Two worth a second look rather than a rubber stamp:**

- **G3** is the only group whose recommendation explicitly declines to fully standardize — "the basis itself should not be hard-standardized because the assets genuinely differ." Confirm that carve-out is intentional.
- **G12** is already written into `SKILL.md` section 12, and the sheet says so plainly: it "needs your ruling to be doctrine." It also resolves DR-084, which records that Regency's supposedly frozen foot-fault pane carries a Georgia-versus-Florida comparison that could only have been written after the Florida build started. Text appears to have been added to a shipped report after it shipped. That anomaly stays open until G12 rules.

---

## 2. The Parakeet Brain — and two of the three gates are Austin's

**Document**: `Corporate\Parakeet Brain\_GOVERNANCE.md`, created 2026-07-04.
**Header**: *"Brain version: 0.1 (DRAFT — pending Jon's sign-off; becomes 1.0 on approval)."*

**What the Brain is**: a cross-project knowledge base — governed markdown on SharePoint, one file per domain (Acquisitions, Market Intelligence, Sales & Marketing, Operations, Construction & Infill), plus a founder-only company file and a decisions log. Seeded from the Acquisitions chat on 2026-07-02.

**What the gate does**: Section 5, "Activation control" — *"Projects are activated one at a time, by Jon, using `_ACTIVATE_IN_OTHER_PROJECTS.md`. No self-service activation."* The handoff file adds: *"HOLD rollout until controls are defined."* **No department beyond Acquisitions can read from or write to the Brain until v1.0 exists.**

**Section 7 names three open decisions as blocking v1.0. Two of them are Austin's to answer, not Jon's:**

1. **Weekly review slot** — fold into the Monday catch-up with Austin, or a scheduled Claude task that emails the digest? *(Austin's call.)*
2. **Should Austin's Parakeet Pulse logs auto-feed the 00_COMPANY summaries**, or stay separate until he opts in? *(Austin's call.)*
3. **Rollout order** in `_ACTIVATE_IN_OTHER_PROJECTS.md` — approve or reorder? *(Jon's call.)*

**A fourth, added later and easy to miss**: the Agentic System architecture doc (`Corporate\Agentic System\parakeet_agentic_architecture_2026-08-16_001.md`, §11 item 6) flags that introducing a "Brain Service" as the single machine writer changes §1 write permissions and therefore *"requires Jon's explicit OK and a `_GOVERNANCE.md` version line."* The entire Railway / OpenRouter / Midbrain agent platform sits downstream of the same signature.

**So**: answer questions 1 and 2 before the meeting, and the Brain gate reduces to a rollout-order confirmation and a signature.

---

## 3. Reds — the real number is 21, and it is all McGregor

**Corrected 2026-08-26.** An earlier draft of this agenda said Riverwalk carried 18 open reds. It does not.

- **Riverwalk**: **zero.** The shipped `FINAL_v1.internal.html` states *"Reds — ALL CLEARED. The build peaked at 36… Zero remain."* Machine-checked: 103 CONFIRMED rows, 28 ADJUSTED, zero `PENDING REVIEW` chips. Register **DR-064** agrees — *"the FINALs shipped with reviews complete."*
- **Regency**: zero. Marked FINAL, shared with Jadian, read-only.
- **McGregor Downs**: **21 open reds** — the only asset carrying any, and still a DRAFT.

**Where the "18" came from**: one line in `MEMORY_index_rebuilt_2026-08-15_001.md` pointing at `project-riverwalk-kickoff-draft.md` — a file that exists nowhere reachable. Possibly a stale mid-build snapshot (the build peaked at 36), possibly a confusion with McGregor's 21. **Do not raise it with Jon as fact.**

**What does exist as an enumerated reviewer punch list**: `Riverwalk/Riverwalk comments 1.docx` and `Riverwalk comments 2.docx` — two rounds of Jon's own comments, both worked and closed before FINAL. Neither is labeled "reds" and neither has 18 items.

**Worth asking**: whether McGregor's 21 are enumerated anywhere, or exist only as red cells in the workbook.

---

## 4. Two numeric flags that are not covered by the DR-035 decision

Austin took a documented no-action decision on DR-035 on 2026-08-26. **These are separate items and remain open:**

- A **g5 paving statistic** cited as "SF-weighted $3.94" that does not reproduce from its stated inputs — roughly $4.01 observed.
- A **Framework Defaults fill-rate of ~3.8/month** that contradicts the subject's own tier math of 4.8/month — and **this one travels into every report.**

The fill-rate is the more consequential of the two. A wrong absorption assumption propagating portfolio-wide is a different class of problem from a mislabeled subtotal.

Separately, `_source_data\RCM_Library_Enrichment_Flags_2026-08-21_001.md` raises **12 unresolved pricing-library items** also awaiting Jon.

---

## 5. Zach — a different dependency entirely

There is **no Zach dependency in the RCM standardization work.** Targeted searches returned nothing; the Corporate project instructions state flatly that *"Jon Wyss: owner and sole decision-maker; all rulings come from him."*

The real Zach item is separate: **`Corporate\Zach_Mailbox_Extraction_Prompt.md`** — a fully drafted, self-contained prompt to be forwarded to Zach's own Claude, asking it to extract a **Walton Street Capital / WSRED lender paper trail** from his mailbox. Three email threads that exist only in Zach's mailbox, plus the vacancy-allowance question and the disputed DO/OAK/TO expense items.

It blocks the **Walton DSCR position work** — 12 memos and 11 briefs sitting at the Corporate root.

**Whether that prompt was ever sent, or answered, could not be determined from the files.** That is a one-line question worth asking, and if the answer is no, forwarding it costs nothing.

*(Separate branch note: the Acquisitions roadmap step 10.4 does wait on Zach — "89 JW + 80 AF answered, JW/AF/engine conflicts resolved; ZS pass + final ingestion pending.")*

---

## Close the meeting with

1. Who updates the decision sheet once ruled — it is the artifact that went stale.
2. Owner and date for the invoice database refresh, which blocks part of G8 (DR-067) and has no stated owner.
3. Whether `_framework_restructure\` (0 bytes) is unstarted scaffolding or emptied work.
