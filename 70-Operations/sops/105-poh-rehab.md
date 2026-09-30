# 105 — POH rehab

**What this is:** rehabbing a park-owned home from the TBD "Rehab" decision to an active listing — one page covering the vendor path (105/105a) and the internal path (105b), which are documented as separate SOPs with different clocks and owners.

**Status:** in review (Tier 1 Critical). The vendor SOP is v1.0 July 9 2026; the internal SOP is v1.0 Aug 1 2026, revised Aug 26. Read 2026-08-30.

## The facts

- **Owner:** Operations / Director of Operations — Natalie Magurne (vendor path); **Regional Manager** (internal path). **Executes:** Operations, Director of Operations, Regional Manager, Community/District Manager, Maintenance, contracted vendor, Sales, Accounting. **Trigger:** the TBD Call disposition is recorded as "Rehab." **Ends when (vendor):** the vendor invoice is with Accounting and the home is live on market. **Ends when (internal):** rehab is marked complete in Rent Manager and the CM/DM submits the Home Market Jotform.
- **Vendor path (105 / 105a) — five phases:** vendor assignment & kickoff → execution & weekly review → punchlist walkthrough & re-walk loop → listing activation → invoice & payment.
- **Gate: nothing proceeds until the vendor assignment and kickoff date are recorded in Rent Manager. "No Rent Manager record = no work starts."** The vendor must send scope or level status for approval before starting.
- The Director of Operations runs **a weekly review call with the vendor, every week, no weeks skipped**, and updates scope notes in Rent Manager after each call. Delays are reported by the vendor directly on that call; Operations then notifies the Regional Manager.
- **The one-week clock:** when the vendor reports completion, the Regional Manager notifies the Community Manager and Maintenance and **records the notification date in Rent Manager — that recorded date, not the vendor's finish date, starts a one-week turnaround for the whole punchlist phase.** Operations is the sole authority to approve and record an extension.
- **A completed punchlist form is required for every walkthrough and every re-walk, no exceptions — no verbal walkthrough substitutes.** Findings cover overall condition, deficiencies, cleaning, incomplete work, safety and cosmetic concerns; the form auto-routes to Regional Manager, Operations and Director of Operations.
- Three walkthrough outcomes: **Ready to List/Show** (install the Parakeet "P" plaque in the window, submit the Home Market form with all listing photos, Operations closes the Rent Manager rehab issue); **Not Ready — Maintenance scope** (work orders in Rent Manager, then re-walk); **Needs Additional Work — Vendor scope** (Regional Manager coordinates the vendor's return, updates Rent Manager notes, then re-walk).
- **Home Market Jotform submission is the formal Operations → Sales handoff.** Sales must activate the listing — or initiate photography — **within 24 hours** of receiving it.
- **Invoices without after photos are not forwarded to Accounting.** Operations reviews invoice plus after photos against approved scope, then forwards.
- **Internal path (105b) — six phases:** initiation → scope & GL setup → active rehab → punchlist & re-walk → completion & close-out → handoff to Sales.
- Internal gates: **no charges may be booked until a valid Rent Manager issue number exists**; **the Director of Operations must enter GL codes in the issue's "GL — Total Cost" UDF before any charges are booked**; **every Ramp card charge carries the GL code in the memo field, entered immediately, in the format `GL [XXXX] — [vendor or description]`**; **the rehab is not marked complete until Accounting confirms GL coding.** Expected internal duration **14–30 days**.
- Internal rehab is always Rehab Tier = Minor Rehab, with all four component flags (HVAC, water heater, roof, siding) defaulting to N — if any is needed, the job is not internal (per the 104 data-entry standard).
- **Systems used:** Rent Manager (issues, work orders, scope notes, UDF "GL — Total Cost", asset status), Jotform (punchlist, Home Market), FastField (named for the same punchlist), Ramp company credit card.
- **Known problems:**
  - **105a is a byte-for-byte duplicate of 105.** `105a-POH  External(vendor)rehab process. final draft.docx` has the identical body text to `105-POH rehab process. final draft.docx` — while the tracker assigns 105a to a **completely different process: "Rehab Handoff Checklist (Jotform)," Tier 1, partial draft.** So 105a is simultaneously a duplicate of 105 and a placeholder for an unwritten process.
  - **JotForm vs FastField is unresolved inside a single task.** Phase 3 Task 2 instructs the Community Manager to use "the Rehab Punchlist **Fastfield** form," then four lines later: "A completed Rehab Punchlist **Jotform** is required for every walkthrough." The forms table and every FAQ say Jotform. 105b calls the same artifact the "**Rehab Walkthrough Jotform**" — a third name.
  - **Two roles are named sole authority for the same extension.** Phase 3 body and role table: "**Operations** … Sole authority to approve and record extensions." Phase 2 role table: "**Operations Coordinator** … Approves and records any extensions in Rent Manager."
  - A truncated role: "**Director of**  records the vendor assignment and confirms kickoff date in Rent Manager" — the title is unfinished.
  - Open item stated in the document itself: **"Formal 1-week extension documentation process [TBD — Operations to define]."**
  - **105b has placeholder GL codes.** Every GL code is `[GL-XXXX]` / `GL [XXXX]`, and all three forms it depends on — Unit Turn Sheet, Rehab Walkthrough Form, Home Market Jotform — are "[Link TBD]".
  - The two paths have **different process owners** (Director of Operations vs Regional Manager) and **different clocks** (a one-week punchlist turnaround vs a 14–30 day duration with a deadline set ad hoc by the Regional Manager) for what is one decision on one TBD Call.
  - The 105 wiki folder holds **five artifacts and no version marker**: the final draft, the Lucid PDF, an SVG swimlane, a fillable punchlist PDF, and the Rehab Data Entry SOP (labelled v1.1 in the filename, v1.0 DRAFT in the content). Two further superseded rehab drafts (`105- Parakeet_Rehab_Workflow_draft V1.docx`, `105- SOP - Rehab Jotform.pdf`) and two near-identical "Weekly Rehab & New Home Inspection Checklist" PDFs (spelled "editable" and "editeble") sit in the drafting room.
  - `_Video Links.txt` is an empty template; **three** 105 videos were scheduled for the week of Sep 28, 2026 — the last slot in the schedule.

## Related

- [[70-Operations/sops/104-tbd-unit-review-and-allocate]] — the disposition call that routes homes into these two paths.

## Decisions

- None recorded yet. Whether 105a is a duplicate to archive or the number reserved for the Rehab Handoff Checklist is unresolved; so is JotForm vs FastField.

## Sources

- [[70-Operations/sops/Process Wiki/100-199 Operations/105 POH Rehab Process/105-POH rehab process. final draft.docx]] — the vendor path (Path A Rehab), five phases and the one-week clock.
- [[70-Operations/sops/105b-Internal_Rehab_SOP_2.docx]] — the internal path; drafting room only, not in the wiki.
