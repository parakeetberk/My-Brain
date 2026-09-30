# Jon Wyss — 13 Standardization Decisions, Extracted for a Single Clearing Meeting

**Source of record:** `RCM_Standardization_Decision_Sheet_2026-08-15_001.md` (7,853 B), at
`https://parakeetcommunities.sharepoint.com/sites/ParakeetBirdcage/Data  Analytics/Claude Cowork/Corporate/Replacement Cost Model/`
**Supporting:** `SKILL.md` (22,396 B), `workstreams\WS1..WS8_*.md`, `RCM_Divergence_Register_2026-08-15_001.md`, `Corporate_Project_Instructions_2026-08-17_001.md`, `MEMORY_index_rebuilt_2026-08-15_001.md`, `Parakeet Brain\_GOVERNANCE.md`, `Parakeet Brain\_HANDOFF_TO_CORPORATE_WORKSTREAM.md`, sibling-branch `Acquisitions\UW Model Engine\Roadmap & Completion Status.docx`.
**Extracted:** 2026-08-26. Read-only pass. No file was modified; the four `.eml` drafts named "DRAFT - open and hit send" were not opened.

---

## Summary

The JREF II Replacement Cost Model (RCM) is a valuation framework that has now shipped three institutional-grade reports to Jadian Capital (Regency FINAL_v2, RC $51,617,512; Riverwalk FINAL_v1, RC $30,118,418; McGregor Downs FINAL_v1, RC $27,911,781). Because each report was seeded from the one before it, the three disagree with each other in 91 catalogued places, tracked in a standing Divergence Register; 53 of those are marked "FRAMEWORK: silent," meaning nobody has ever ruled which version is correct. The Standardization Decision Sheet bundles the silent ones into **13 numbered groups and asks Jon to pick a house standard for each**. Every group already carries a written recommendation and a one-line rationale, so the meeting is a set of confirm-or-override calls, not open-ended design. Each ruling then flows to four places: it is written into `SKILL.md` (the runbook) and the affected workstream files; the matching register entries flip from "silent" to "ruled"; Riverwalk and Regency get next-touch queue items (their shipped files are never edited); and McGregor Downs applies the whole set at its next touch. **Nothing about the framework can be finalized until these land** — the sheet states the rulings are the gate, and the register's own Rule 2 is that it "rules on nothing." One material discrepancy to surface at the top of the meeting: `SKILL.md` section 13 already contains all 13 recommendations verbatim, headed "Presentation standards (Jon rulings 2026-08-15, from the standardization decision sheet)," while the decision sheet itself still lists them as "Decisions needed." Either the rulings were given and the sheet is stale, or the runbook was written ahead of the ruling. **I could not determine which from the files; both were last modified 2026-08-15, the sheet at 07:43 and SKILL.md at 07:50.**

---

## The 13, in unblock order

Ordering rationale: the sheet does not rank them. I ordered by (a) how many Divergence Register entries each group retires, (b) how many of the eight workstream files must change, and (c) whether the group sits on a hard gate in the ten-step build order (the land gate at step 4, FINAL packaging at step 10). **No ordering is stated in the source; this ranking is mine.**

---

### 1. GROUP 8: Audit Trail standard kit
*(DR-005, 059, 060, 064, 066, 067 — six register entries, the most of any group)*

**The decision, plainly.** The Audit Trail tab is the "show your work" page of every report. Right now each of the three shipped reports built that page differently. Jon is being asked to freeze one version: which explanatory boxes appear, in what words, and how the page signals whether a report is still a draft or finished.

**Options on the table.** The sheet states one recommendation with five parts, not competing alternatives:
(a) an "AUDIT TRAIL BASIS" box opens the tab on every report;
(b) the four-layer wording uses the neutral phrase "the evidence sample sizes, the city cost index, and the fee jurisdiction";
(c) draft-versus-final language is codified — a DRAFT says "on the build so far," a FINAL says "before this report was finalized," flipped at packaging;
(d) status-chip vocabulary is codified — red "PENDING REVIEW" chips allowed in DRAFT, none allowed at FINAL unless Jon rules an item ships red;
(e) the derivation-notes box set is fixed as Land Comps + the land-basis box matching that asset's ruling + a Documents & Exhibits register, with a Vendor Invoice Data Set box returning when the invoice database refresh lands.

**Blocked downstream.** The widest blast radius of the thirteen. It rewrites `SKILL.md` section 13, and it is checked by WS4 (conformance), WS6 (deep sweep, review-state drift), and WS8 (assembly and packaging). Part (c) and part (d) are literally the definition of "this report is finished" — WS8's packaging checklist cannot be finalized without them. Part (e) is additionally waiting on the invoice database refresh, which is a separate open item (DR-067).

**Flags.** Not marked high priority or contested in the sheet. Carries a recommendation. Rationale given: "the boxes are framework furniture; naming the set once ends the per-build improvisation."

---

### 2. GROUP 2: Land tab presentation kit
*(DR-019, 021, 022, 028, 029 — five register entries)*

**The decision, plainly.** Land value is the single largest input to a replacement cost number, and the three reports each presented the land evidence differently — different table columns, different closing paragraph, different place to put the working file. Jon is being asked to fix one layout for the land page.

**Options on the table.** One recommendation, four parts:
(a) a labeled "Land-basis check." paragraph closes the Land Comps card on every report;
(b) one canonical comps-table schema, taken as the superset of all three builds: COMPARABLE SALE | BUYER OF RECORD | ACRES | PRICE | $/ACRE | DIST. (MI) | SALE DATE | QUAL/ZONING;
(c) the "cover-mix" mechanic is named by that exact phrase wherever it applies;
(d) the full land working file and the detail on which comparable sales were excluded move into the standalone research Library, with the land tab linking out to it — retiring the old Internal-tab pointer along with the g3 pane.

**Blocked downstream.** Sits on the build's hard gate. Per the runbook's ten-step build order, the land comp set "goes in front of Jon BEFORE anything wires" (step 4 of 10); nothing in the model is populated until the land basis is ruled. This group defines the format of that gate memo, so it changes WS5 (land comp screen), WS3 (prose substitution) and WS4 (conformance). Part (d) also depends on the already-settled ruling that the Library is a standalone file.

**Flags.** Not marked high priority or contested. Carries a recommendation. Rationale: "three reports built three kits; the superset loses nothing and the library is now the natural home for working files."

---

### 3. GROUP 1: Subject corroboration device
*(DR-041, 051, 056 — three register entries, but the widest per-line reach in the report)*

**The decision, plainly.** When the model prices something using outside evidence (a published rate, a vendor invoice from another community), should the report always add a sentence saying whether there is any evidence from *this specific property* backing it up — including explicitly saying so when there is none? And separately: can the report name other Parakeet communities as supporting evidence, or must those references be anonymized?

**Options on the table.** One recommendation: every empirical line carries a "Subject-property check:" sentence, *including* an explicit statement when no subject evidence exists; scale and track-record claims stay in the report but are anonymized — no named sister assets, no cross-market figures.

**Blocked downstream.** Applies to every empirical line on every tab, so it is the broadest single change in prose terms. Feeds WS3 (prose substitution card format), WS4 (conformance check), WS6 (deep sweep). The anonymization half also interacts with a standing non-negotiable already in the runbook: "no cross-market comparisons and no named cross-asset references in external prose," since these reports go to Jadian Capital.

**Flags.** Not marked high priority or contested. Carries a recommendation. Rationale: "the explicit-absence form (McGregor) is the honest version of the device and reads identically across assets."

---

### 4. GROUP 5: Entitlement card format kit
*(DR-042, 043, 046, 048, 050 — five register entries)*

**The decision, plainly.** The Entitlement tab explains how hard it will be to get a property approved and permitted, and what the fees are. Each of the three reports wrote those cards with different headings, different closing sentences, and different ways of listing caveats. Jon is being asked to pick one house format.

**Options on the table.** One recommendation, five parts:
(a) the tier card closes with "RECOMMENDATION: Tier X (multiplier, clock). Basis: ...";
(b) the sub-headline reads "«County» local-facts read: zoning path, process and supply evidence" — colon, not hyphen;
(c) the fee card opens "One line, N cited components.";
(d) caveats appear as an enumerated (1)(2)(3) paragraph when there are two or more, and as a single "Open item:" sentence when there is one;
(e) carried-forward conventions close with "Standing convention, unchanged: ...".

**Blocked downstream.** WS3 (prose substitution — this is the template it substitutes into) and WS4 (convention-text conformance). Also `SKILL.md` section 13.

**Flags.** Not marked high priority or contested. Carries a recommendation. Rationale: "each is the clearest of the three shipped variants; picking one ends the drift."

---

### 5. GROUP 3: Land-value levers table
*(DR-023, 033, 034 — three register entries)*

**The decision, plainly.** The land section carries a small table listing the levers that move the land number. It has been four rows in some builds and six in others. Jon is being asked to standardize at six — and to confirm that one of those rows stays a per-property judgment call rather than a fixed rule.

**Options on the table.** One recommendation: the six-row levers table is standard, adding "Application basis" and "Land closing & due diligence" to the original four. The application-basis row states each asset's own ruling (flat-to-gross, or cover mix), which stays a per-asset call Jon makes at the land gate. Section subtitle and row labels then follow that ruling.

**Blocked downstream.** Pairs with GROUP 2 on the same land page; feeds WS5 and WS3. Note the deliberate carve-out: this group standardizes the *table*, not the *basis*.

**Flags.** Not marked high priority or contested, but this is the one group whose recommendation explicitly declines to fully standardize: "the basis itself should not be hard-standardized because the assets genuinely differ." Carries a recommendation.

---

### 6. GROUP 9: Internal pane standards
*(DR-006, 074, 078 — three register entries)*

**The decision, plainly.** The internal-only section of the report (stripped out of the version Jadian sees) has picked up new sub-panes over successive builds. Jon is being asked to confirm which of them are permanent, and to confirm that internal text never names a person.

**Options on the table.** One recommendation, three parts:
(a) the Subject Register table — every exhibit pulled during that build — is standard on the g2 pane;
(b) kickoff sequencing rulings are recorded as a standard preamble block before the internal exchange record;
(c) internal panes say "the reviewer," never a name.

**Blocked downstream.** WS8 (assembly, internal section) and the internal/external file split at packaging. Part (c) is a shareability rule: neutral naming keeps internal text safe to circulate.

**Flags.** Not marked high priority or contested. Carries a recommendation. Rationale: "all three are the newest build's additions and each earned its keep."

---

### 7. GROUP 12: Foot-fault carry behavior
*(DR-084, 085 — two register entries; the closest thing on the sheet to a contested item)*

**The decision, plainly.** Each report keeps a running list of mistakes caught during the build ("foot-faults"), and that list gets carried forward into the next report. Two questions: when a past mistake was specific to a different property, may it be reworded generically for the new report (with the original preserved where it happened)? And is a shipped FINAL frozen at ship, so that later lessons go to the register and the next build rather than back into the delivered file?

**Options on the table.** One recommendation: yes to both — carried foot-faults may be GENERALIZED when the asset specifics do not travel, the original stays preserved in its source report, and a FINAL's panes are frozen at ship, with post-ship lessons going to the register and the next build.

**Blocked downstream.** This is doctrine rather than layout, so it changes how WS8 and the register behave rather than how a page looks. Its practical significance: the sheet states it "directly answers the REG post-ship-text anomaly." That refers to Divergence Register entry DR-084, which records that Regency's supposedly frozen foot-fault pane "carries a GA-versus-FL comparison that could only be written after the RW (Florida) build started," logged as an "accrual anomaly. Not resolved." In plain terms, text appears to have been added to a shipped report after it shipped. Until this rules, that anomaly stays open.

**Flags.** Not marked high priority or contested on the sheet. Carries a recommendation, and the sheet notes it is *already written into* `SKILL.md` section 12 "from my read of the accrual model; it needs your ruling to be doctrine."

---

### 8. GROUP 7: Log-row citations in evidence prose
*(DR-049 — one register entry, but it adds a permanent item to the QC checklist)*

**The decision, plainly.** Now that each report has one numbered review log, may the body text of the report point at it by row number — "(log row 7)"? The catch is that removing a row renumbers everything below it, which would silently break every citation.

**Options on the table.** One recommendation: allowed and encouraged, cited as "(log row N)," with the rule that any renumbering sweep must update the citations — added to the deep-sweep C4 surface list.

**Blocked downstream.** Adds a standing check to WS6 (deep sweep, category C4 review-state drift) and to the surface checklist in `SKILL.md` section 11. Depends on the already-settled single-numbered-log ruling.

**Flags.** Not marked high priority or contested. Carries a recommendation. Rationale: "decision 1 made row numbers stable enough to cite; the sweep hook covers the renumber risk."

---

### 9. GROUP 13: Growth model citation form
*(DR-057 — one register entry)*

**The decision, plainly.** When the report cites the rent-growth assumption, it should name Parakeet's own internal rent model rather than the third-party index underneath it. The three reports cite it three different ways. Jon is being asked to lock one wording.

**Options on the table.** One recommendation, an exact string: "The 2BR Rents Analysis - ZORI model (ZORI = the Zillow observed rent index) (Market Intelligence), «subject tab/row», «base month» base", glossed once per tab.

**Blocked downstream.** WS3 (prose substitution), plus the gloss list in `SKILL.md` section 8.

**Flags.** Not marked high priority or contested. Carries a recommendation. Rationale: "names the real internal model (framework-model-first), keeps the gloss, and ends the three-way citation drift."

---

### 10. GROUP 4: Survey sheets at FINAL
*(DR-026 — one register entry)*

**The decision, plainly.** Should scanned images of the signed land survey be embedded inside the final report file, or just cited to the closing binder?

**Options on the table.** One recommendation: survey sheet images are NOT embedded at FINAL; the signed survey is cited to the closing binder, and only measured exhibits (KML maps, flood geometry) embed.

**Blocked downstream.** WS8 packaging. Practical effect is file weight: the sheet notes 721 KB of the seed file was prior-asset survey images.

**Flags.** Not marked high priority or contested. Carries a recommendation. Rationale includes a stated demand signal: "no external reader has asked for the sheets."

---

### 11. GROUP 10: Pool and deck granularity
*(DR-008 — one register entry)*

**The decision, plainly.** When pricing a community pool, should the pool and its surrounding deck be one line item or two?

**Options on the table.** One recommendation: component-level lines — pool and its deck priced as two separate evidence lines, as Riverwalk and McGregor did.

**Blocked downstream.** WS7 (census reconciliation, component line assignment) and the Google Earth KML measurement workflow, which already measures them as separate polygons.

**Flags.** Not marked high priority or contested. Carries a recommendation. Rationale: "matches the component-total rounding convention and the KML polygon workflow, which measures them separately."

---

### 12. GROUP 6: Provenance tags
*(DR-047 — one register entry)*

**The decision, plainly.** When a rate was read straight off the actual governing document (a real utility bill, a published tariff) rather than computed or looked up second-hand, should the report say so with a fixed phrase?

**Options on the table.** One recommendation: any rate resolved from an actual governing document carries the tag "resolved from the actual bill" (or "...the actual schedule/tariff").

**Blocked downstream.** WS3 (prose substitution) and WS4 (convention check). Small surface.

**Flags.** Not marked high priority or contested. Carries a recommendation. Rationale: "it is the one-phrase difference between a computed rate and a looked-up one, and two of three reports already do it."

---

### 13. GROUP 11: Aside punctuation
*(DR-088 — one register entry; the smallest call on the sheet)*

**The decision, plainly.** House style question: use commas rather than spaced hyphens for parenthetical asides in new prose.

**Options on the table.** One recommendation: confirm the runbook's stated preference — commas over spaced-hyphen asides in new prose (McGregor style).

**Blocked downstream.** Language standard only; checked by WS4 and WS6. Nothing structural waits on it.

**Flags.** Not marked high priority or contested. Carries a recommendation, and the sheet is explicit that this is a promotion rather than a new decision: "already written into SKILL.md section 8 as 'prefer'; your confirm makes it a standard rather than a lean."

---

## WS1–WS8 pipeline

**Important caveat, stated first: the eight WS files are role and instruction definitions, not status trackers. None of them carries a status field, a percent-complete, or a blocked flag.** There is no numbered roadmap with completion states in the Corporate branch, unlike the sibling Acquisitions branch which has a 21-step roadmap document. What follows is the stage list as defined, plus the completion state that *is* recorded elsewhere (the project memory index and the shipped deliverables).

| Stage | File | Tier / model | Purpose | Recorded state |
|---|---|---|---|---|
| WS1 | Source-Document Extraction | Mid (Sonnet-class) | Pull fixed-schema facts from PSA, closing statement, ALTA survey, PCAs, appraisal, tax bill, rent roll into the asset FACTS file | Defined; exercised on all three shipped builds |
| WS2 | Jurisdiction Rate-Stack Research | Mid, with web access | Pull the jurisdiction's published impact, permit, utility, stormwater and transfer fees, with effective dates and URLs | Defined; exercised |
| WS3 | Prose Substitution Into Templated Cards | Mid | Substitute the new asset's values into the skeleton inherited from the prior FINAL, as old/new pairs only | Defined; exercised. **Pending edits from 8 of the 13 decision groups** |
| WS4 | Conformance Check | Mid | Compare the new build against the reference FINAL and against every register entry; flag only, fix nothing | Defined; exercised. **Pending edits from most decision groups** |
| WS5 | Land Comp Screen | Top (Fable-class), never decomposed | Produce the land-basis gate memo that goes in front of Jon before anything wires. HARD GATE | Defined; exercised (e.g. `McGregorDowns_LandComp_Gate_2026-08-14_001.html`). **Pending GROUPS 2 and 3** |
| WS6 | Deep Sweep QC | Top, fresh-eyes agent | Six-category pre-review sweep over rendered text: relics, stale values, display bugs, review-state drift, unglossed jargon, markup integrity | Defined; exercised. **Pending a new C4 check from GROUP 7** |
| WS7 | Census Reconciliation and Purchase-Price Sourcing | Top | Reconcile the physical census across four sources and source the purchase price across all deal-paper views | Defined; exercised. **Pending GROUP 10** |
| WS8 | Final Assembly and Packaging | Top, architect only, never delegated | Kickoff rulings, land gate, wiring, the review cycle, FINAL packaging | Defined; exercised three times. **Pending GROUPS 8, 4, 9 — including the definition of what "finished" means** |

**Completion state that is recorded:**
- Regency: FINAL_v2 shipped, RC $51,617,512.
- Riverwalk: FINAL_v1 shipped, RC $30,118,418, **18 reds pending Jon**.
- McGregor Downs: FINAL_v1 shipped 2026-08-17, RC $27,911,781. The decision sheet states McGregor "applies everything at the 21-reds touch," so McGregor carries **21 reds** of its own, pending the same meeting.
- `_framework_restructure\` is a 0-byte empty folder — a restructure scaffolded and never started. **Whether that is unstarted work or emptied work could not be determined from the connector.**

**So: the pipeline is not blocked stage-by-stage. All eight stages have run end-to-end three times. The block is that the pipeline's written standards are unresolved in 13 places, and three shipped reports disagree with each other in 91 catalogued ways, 53 of them unruled.**

---

## Dependency on Zach (ZS)

**The sibling branch's version, confirmed:** `Acquisitions\UW Model Engine\Roadmap & Completion Status.docx` (rev 2, 2026-07-05), step 10.4, status "In progress":

> "Questions — 89 JW + 80 AF answered, JW/AF/engine conflicts resolved; ZS pass + final ingestion pending"

ZS is Zach Schwartz. That step waits on Zach reviewing a question set before the answers can be ingested into the underwriting knowledge base.

**The Corporate equivalent: there is none in the RCM workstream.** Targeted searches for Zach / ZS across `Replacement Cost Model\` returned nothing, and no WS file, the decision sheet, the register or `SKILL.md` names Zach as a dependency. Everything in the RCM branch routes to Jon; the Corporate project instructions state flatly, "Jon Wyss: owner and sole decision-maker; all rulings come from him." The nearest structural analogue inside RCM is WS7's rule that "reviewer field confirmation is the FINAL GATE" on any single-source census item, and WS5/WS8's land gate — but the reviewer in both cases is Jon, not Zach.

**The one genuine Zach dependency in the Corporate branch is a different matter entirely.** `Corporate\Zach_Mailbox_Extraction_Prompt.md` (6,007 B) is a fully drafted, self-contained prompt to be forwarded to Zach's own Claude, asking him to extract a Walton Street Capital / WSRED lender paper trail out of *his* mailbox — three email threads that exist only in Zach's mailbox and that Jon cannot pull himself, plus the vacancy-allowance question and the disputed DO/OAK/TO expense items. That blocks the **Walton DSCR position work** (the 12 memos and 11 briefs sitting at the Corporate root), not the RCM standardization. **Whether that prompt was ever actually sent to Zach, or answered, could not be determined from the files.**

---

## "Parakeet Brain governance is gated on Jon's approval"

**What it means, concretely.** The Parakeet Brain is a cross-project knowledge base — a set of governed markdown files on SharePoint holding what the company has decided it knows, one file per domain (Acquisitions, Market Intelligence, Sales & Marketing, Operations, Construction & Infill, plus a founder-only company file and decisions log). It was seeded from the Acquisitions chat on 2026-07-02 and Jon directed the build-out to continue as its own workstream inside Corporate.

**The specific approval, on the specific document.** The document is `Corporate\Parakeet Brain\_GOVERNANCE.md` (5,541 B), created 2026-07-04. Its header reads: **"Brain version: 0.1 (DRAFT — pending Jon's sign-off; becomes 1.0 on approval)."** So the approval being waited on is Jon signing off on the governance protocol itself, which promotes it from v0.1 DRAFT to v1.0.

**What that unlocks.** Section 5 of that file, "Activation control," states: "Projects are activated **one at a time, by Jon**, using `_ACTIVATE_IN_OTHER_PROJECTS.md`. No self-service activation." The handoff file adds: "HOLD rollout until controls are defined." So no department beyond Acquisitions can start reading from or writing to the Brain until v1.0 exists.

**Section 7 of that file lists three open decisions Jon must answer, and names them as blocking v1.0:**
1. Weekly review slot — fold into the Monday catch-up with Austin, or a scheduled Claude task that emails the digest?
2. Should Austin's Parakeet Pulse logs auto-feed the 00_COMPANY summaries, or stay separate until he opts in?
3. Rollout order in `_ACTIVATE_IN_OTHER_PROJECTS.md` — approve or reorder?

**A fourth, added later and easy to miss.** The Agentic System architecture document (`Corporate\Agentic System\parakeet_agentic_architecture_2026-08-16_001.md`, §11 item 6) flags that introducing a "Brain Service" as the single machine writer is a change to §1 write permissions and therefore "requires Jon's explicit OK and a `_GOVERNANCE.md` version line." That whole architecture — the Railway/OpenRouter/Midbrain agent platform — is downstream of the same sign-off.

---

## The 18 reds pending on the Riverwalk report

**What "reds" are.** During an RCM build, any model input that is unresolved, unmeasured or awaiting Jon's word is displayed as a red cell and carries a red "PENDING REVIEW" chip. The runbook's review cycle is that Jon calls row numbers off a single numbered "Review & Adjustment Log" on the Audit Trail tab, and "only the reviewer's word clears a red." When a red clears, it must be cleared on every surface the input lives on: the model input, the source attribute and the visible cell, the evidence card, the numbered log row, the provenance row, the recipe, and the Excel cell and its note.

**The count and its source.** The figure comes from `MEMORY_index_rebuilt_2026-08-15_001.md`, which describes `project-riverwalk-kickoff-draft.md` as: "Riverwalk current-state file. Shipped FINAL_v1, RC $30,118,418. **18 reds pending Jon.**"

**Are they enumerated anywhere?** *[PENDING — see note below]*

**Known-adjacent items that are enumerated, and are not the 18:**
- The Divergence Register catalogues 91 numbered divergences (DR-001 … DR-091) across the three reports, 53 marked "FRAMEWORK: silent." Those are cross-report inconsistencies, a different thing from Riverwalk's open reds.
- `_source_data\RCM_Library_Enrichment_Flags_2026-08-21_001.md` raises 12 explicitly unresolved pricing-library items for Jon.
- McGregor carries a separate "21-reds touch" referenced in the decision sheet.

**A related integrity item, already decided — do not reopen it by accident.** Divergence Register entry **DR-035** records that the Section IV hard-costs subtotal in the shipped **Riverwalk and McGregor FINALs** describes itself as summing "sitework through amenities" when the last row it actually sums is personal property. That is known-wrong text inside two reports already delivered to Jadian Capital, and both files are read-only by the framework's own Rule 1. **Austin took a documented no-action decision on DR-035 specifically on 2026-08-26** (`00-Meta/decisions/2026-08-26-dr035-no-action.md`); the finding stays recorded in the register as the evidence of when it was identified. That decision covers DR-035 only — the other 52 unresolved divergences remain open and sit under this same Jon decision queue.

Two further unresolved numeric flags sit at the register tail and are *not* covered by that decision: a g5 paving statistic ("SF-weighted $3.94") that does not reproduce from its stated inputs (~$4.01 observed), and a Framework Defaults fill-rate figure (~3.8/month) that contradicts the subject's own tier math (4.8/month) while travelling into every report.

---

## Things I could not determine

1. **Whether the 13 groups have in fact already been ruled.** `SKILL.md` section 13 presents all thirteen recommendations as "Jon rulings 2026-08-15," while the decision sheet lists them as awaiting decision. Both files are dated 2026-08-15. This should be the first question in the meeting.
2. **Whether the 18 Riverwalk reds are enumerated as a list anywhere** — see the pending note in that section.
3. **No group is flagged high priority or contested in the source.** The sheet applies no priority markers at all. Every group carries a recommendation. My ordering above is inferred from dependency counts, not stated.
4. **Whether the Zach mailbox-extraction prompt was ever sent or answered.**
5. **Whether `_framework_restructure\` (0 bytes) is unstarted scaffolding or emptied work.**
6. **The invoice database refresh** blocks the Vendor Invoice Data Set box (part of GROUP 8, entry DR-067); its owner and timing are not stated in these files.
