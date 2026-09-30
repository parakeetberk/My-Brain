# Agent brief: finish the SOP library

**The job in one sentence:** work the SOP library from 1 approved process to a library that can actually be followed, resolving the conflicts that block approval first, then the [TBD] markers, then the empty bands, and routing every finding to the rock owner with her name on it.

**Runs when:** the user asks to work the SOP library, or a session picks up the process-documentation rock. Runs one work item at a time, not the whole library at once.

## Inputs

- The `parakeet-sop-builder` skill: the authority on how a Parakeet SOP is built, numbered and formatted. Load it before touching any SOP.
- `70-Operations/sops/sop-library.md`: the state of play, the nine-band numbering scheme, and all nineteen documented conflicts stated in full.
- The 34 process pages in `70-Operations/sops/`: each carries its own conflicts and open [TBD] markers.
- `70-Operations/sops/_SOP Drafts & Master Tracker/SOP_Master_Tracker_v3.xlsx`: the scoreboard. **v3 is current; three older versions exist and are not.**
- `10-Business/eos/rocks-2026.md`: the rock this work serves.
- `10-Business/eos/to-dos.md`: where every finding lands as a line.
- `10-Business/outside-help/counsel.md`: who the compliance questions go to.

## State of play: read this before starting

- **109 processes tracked. 1 approved** (200 Demo & Lot Prep, whose own revision history still says "Initial draft" and names no approver).
- **Bands 400 to 700 are empty scaffolds**: Asset Management, Acquisitions/Dispositions, Systems/IT/Reporting, HR & Training (except orphan 704).
- **19 documented conflicts**, unresolved.
- **27 empty `_Video Links.txt` files**: zero training videos recorded against a schedule that had every populated process covered by the week of 2026-09-28.

## Steps: the order is the point

1. **Resolve the blocking conflicts first, starting with the Florida cure period.** It has four live values across four documents: 5 business days in SOP 100, 7 days plus a 5-day mailbox rule in 802/803, 10 business days in SOP 107, 5 days in SOP 800. **It blocks SOP 100, SOP 107 and the whole FL 800-block simultaneously**, and field staff are currently following the operating SOPs. Then the other statutory contradictions: South Carolina's rent increase notice (90 days in SOP 101 vs 30 days with a 60-day company standard in SOP 821, both citing SC Code 27-47-420) and Georgia's 60-day notice (44-7-60 in SOP 101 vs 44-7-7 in SOP 811).
2. **Then the [TBD] markers that make their own documents unapprovable.** SOP 201 states it "cannot be marked Approved until all three are resolved": the JotForm link, the SharePoint folder link and the Bill of Lading retention period. Then 203's manufacturer warranty reporting window, 302's missed-lender-deadline consequence and Repo Tracker, 108's HR email, 105's one-week extension process, 105b's placeholder `[GL-XXXX]` codes, and 001's empty "PENDING DECISIONS" heading.
3. **Then the empty bands, starting with 400 Asset Management and 600 Systems**: the two bands whose absence is doing the most damage, since four of the seven Tier 1 Critical processes with nothing started are utility processes that belong in those bands.
4. **Then MA and NC compliance.** The owner confirmed on 2026-08-30 that Massachusetts and North Carolina are live operating states, and the 800s block covers only FL, GA and SC. SOPs 100 and 101 already carry the statutory detail, including the MA 72-hour pre-signing disclosure package and the bona fide five-year lease offer, with no compliance SOP behind it.
5. **Then an RV / Chapter 513 process.** SOPs 801, 802 and 804 explicitly exclude or route RV parks: "RV parks are Chapter 513 — no prospectus applies; route to Legal". No Chapter 513 SOP exists anywhere, despite RV being a large part of the portfolio.
6. **For each item, produce the resolution as a draft, not a change.** Show the conflicting values side by side, say which one the evidence supports and why, and name the document that has to change.
7. **Get sign-off before anything is marked resolved.** **Every conflict resolution needs the process owner's sign-off. Every compliance one additionally needs counsel**: the statutory numbers, the MA and NC blocks, the Chapter 513 work and the deposit clocks.
8. **Route the findings to the rock owner.** Process documentation is **Natalie Magurne's** rock. Produce **a drafted email to Natalie** setting out what was found, what the recommendation is and what needs her sign-off, and **a to-do line in `10-Business/eos/to-dos.md` with her name on it** for each item. The draft email is not sent.
9. **Update the tracker only where a file genuinely exists.** The tracker is stale on at least seven processes and has no row at all for 122, 123, 202, 203 or 704. Correcting a stale row is fine; marking anything "Approved" is not, without a real approver and date.
10. Append one line to `00-Meta/log.md` per work session.

## Output

- One resolution draft per conflict or [TBD] worked, in the drafting folder or as a proposed edit to the relevant process page.
- A drafted email to Natalie Magurne, unsent, in the session or in `10-Business/eos/drafts/`.
- A to-do line per finding in `10-Business/eos/to-dos.md`, owner Natalie Magurne, with the source and the date raised.
- Tracker corrections where a file genuinely exists.
- One appended line in `00-Meta/log.md`.

## Rules for this job

- **Never mark a process Approved.** Approval requires a named human approver and a date. The one approved SOP in the library does not have either, which is exactly the mistake not to repeat.
- **Never resolve a statutory number without counsel.** A cure period, a notice period or a deposit clock is a legal question, not a documentation question. Present the options; do not pick.
- **Never delete a superseded document.** The standards doc requires them to move to an `_Archive` subfolder inside each process folder: "never deleted, never left beside the current version". **No `_Archive` subfolder exists anywhere in the library yet.** Creating them and moving files is a proposal to be approved, not an action to take.
- **Leave the 107-vs-800 eviction numbering alone.** The owner was asked on 2026-08-30 and deferred. Both files stay on disk, unmarked, until he decides.
- **The 96 duplicate files are a real problem but not this job's to fix by deletion.** Flag the set; propose one authoritative copy per process; wait.
- **Nothing goes to a resident.** Eviction, collections and deposit SOPs describe letters and notices with resident names on them. **Draft only, never send, never file.**
- **Personnel material is Austin-only.** SOP 704 is the disciplinary-action process; anything drafted around it goes to Austin, not distributed.
- **No pricing or spend change.** SOPs carry approval thresholds and GL codes; proposing a change to one is analysis, changing it is not this job.
- **Never reproduce any individual's personal compensation**, including anything implied by a commission or bonus structure discussed in a sales SOP.
