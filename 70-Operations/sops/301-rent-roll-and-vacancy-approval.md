# 301 — Rent roll & vacancy approval

**What this is:** the month-end sign-off chain that gets rent and occupancy data corrected in Rent Manager — Community Manager review, Regional consolidation, Director approval, then system entry.

**Migration note, 2026-08-31:** the save path this SOP gives Regional Managers — `Operations > [Property Name] > 8. Reports_Month End Closeout` — is **correct today and left unchanged on purpose.** Rewriting it now would send Regional Managers to a folder that does not exist yet. It **breaks at Birdcage cutover**, because the community template there is unnumbered ([[10-Business/sharepoint/target-structure]]); the destination becomes `Reports_Month End Closeout`. This SOP is on the cutover list of documents whose paths change on the same day, not before.

**Status:** in review (Tier 2 High). Signed "Reviewed and approved by: Natalie Magurne, Director of Operations" — but the tracker and wiki index both mark it a draft pending review. Read 2026-08-30.

## The facts

- **Owner:** Director of Operations (Natalie) approves; the document names no process owner in a header table. **Executes:** Community Managers (review and sign), Regional Managers (save, consolidate, record), Director of Operations (approve), Clarissa (distribute and final-check), Justin (enter updates in Rent Manager). **Trigger:** the 25th of the month. **Ends when:** Justin confirms all updates are entered in Rent Manager and Clarissa completes a final verification.
- **The calendar is the process:**
  - **25th** — the Rent Roll Summary Report (PDF) is sent to all Community Managers. Every CM reviews it and marks any needed updates **directly on the PDF**.
  - **27th–28th** — Regional Managers save the PDF reports to `Operations > [Property Name] > 8. Reports_Month End Closeout > [Month] [Year]`, gather updates from all their communities, and record them in the **Month End Tracker Report** (template at `Operations > _Weekly Reports > Month End Tracker > Team Name`).
  - **29th** — the Director of Operations reviews and approves the Month End Tracker Report. After approval **Clarissa sends the Excel summary to Justin**, copying the Regional Managers and the Director, for system updating.
  - **Final verification** — once Justin confirms all updates are entered in Rent Manager, Clarissa performs a final check that everything is correctly updated.
- **What the Community Manager reviews under Rent Roll Approval:** previous and current resident name, previous and current unit type, and previous and current charges — **lot rent, water, trash, MH rent.**
- **What the Community Manager reviews under Vacancy:** previous and current resident name, previous and current unit type.
- **No changes still requires a signature.** If nothing has changed, sign the Rent Roll Approval (and the Vacancy report) and email it to the assigned Regional Manager — silence is not an approval.
- **Systems used:** Rent Manager (destination system of record), the Rent Roll Summary Report PDF, the Month End Tracker Report (Excel), SharePoint/OneDrive Operations folders, email.
- **Known problems:**
  - **301 has no SOP document.** The only file in the wiki folder is `301 Rent Roll Summary Process.pdf` — a process-flow PDF filed in the SOP slot. There is no Word source, no header table, no version, no effective date, no revision history and no status field. The tracker's actual SOP source is "**ROCK: AR RR analytics SOP draft.docx**" — raw material that was never brought into the library.
  - **The calendar collides with SOP 110.** This process *sends* the rent roll to Community Managers on the **25th**. `110-Month_End_Close_SOP.docx` requires the CM to have completed and submitted the whole month-end close checklist by **12:00 PM on the 25th** — before the report they are supposed to reconcile has arrived. The 110 *checklist* says the 27th with DOO sign-off on the 29th, which does line up with this process. Two of Parakeet's month-end SOPs cannot both be followed.
  - **"Clarissa" is defined nowhere.** She distributes the approved summary and performs the final system verification — two control steps — and appears in no other SOP, no role table, and no org description in the library.
  - **Department attribution is wrong on its face:** the document reads "Department: **Operations**" and is filed in **300-399 Accounting**; the tracker assigns creation to Accounting / Finance.
  - **Approval is by email and PDF markup, not in a system.** Community Managers annotate a PDF; Regionals retype into an Excel tracker; Justin retypes into Rent Manager. Three transcriptions between the reviewer and the system of record, with no audit trail beyond saved files.
  - The vacancy half of the process reviews only names and unit types — there is no vacancy *count* reconciliation, no occupancy figure, and no tie to the occupancy rate SOP 106 requires Regional Managers to record on site visits.
  - No escalation path: nothing says what happens if a CM does not return a signed report, or if Justin's entries do not match the approved tracker.
  - `_Video Links.txt` is an empty template; a 301 video was scheduled for the week of Aug 17, 2026.

## Related

- [[70-Operations/sops/110-month-end-close]] — the community-level month-end close whose deadline collides with this calendar.

## Decisions

- None recorded yet.

## Sources

- [[70-Operations/sops/Process Wiki/300-399 Accounting/301 Rent Roll & Vacancy Approval/301 Rent Roll Summary Process.pdf]] — the process flow, the 25th/27th–28th/29th calendar, and the signature requirement.
