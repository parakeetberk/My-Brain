# Agent brief: transcript to action

**The job in one sentence:** turn a raw meeting or site-visit recording into a filed note, updated pages, ledger entries, a to-do line per action and a ClickUp task per action, so nothing said on a recording is lost and every action has a named owner.

**Runs when:** a transcript or recording lands in `05-Inbox/`, or the user says "file the new transcript" or pastes the text. Runs once per transcript; if several are unfiled, ask which comes first.

## Inputs

- `05-Inbox/`: the unfiled transcript.
- `90-Skills/transcript-filing.md`: the filing format and the naming convention. **This is the authority on shape; follow it exactly.**
- `90-Skills/page-update.md`: how a fact gets pushed onto a page.
- The `meeting-transcript-to-clickup` skill: task creation.
- `10-Business/eos/to-dos.md`: the open to-do register, grouped by owner.
- `10-Business/people/`: to check a name against a real person before attributing anything to them.
- `70-Operations/meetings/2026-08-southeast-tour/`: 27 already-filed transcripts, as the worked example of what a filed note looks like here.

## Steps

1. Find the unfiled transcript. Get its **meeting date** from the transcript. **If the date is not in the transcript, ask. Never guess a date.**
2. Reshape it into the filed format from `90-Skills/transcript-filing.md`: title, who was there, a three-to-five sentence summary, decisions one per line, actions as a checklist, **full raw text kept below the fold. Nothing is deleted.**
3. Name it `YYYY-MM-DD-meeting-name.md`.
4. **File it in the `meetings/` subfolder of the folder the meeting was mostly about**: property operations in `70-Operations/meetings/`, a capital or investor conversation in `80-Finance/meetings/`, a hiring conversation in `10-Business/meetings/`. **If you cannot tell, leave it in `05-Inbox/` with a note saying why. Flagged, never guessed.**
5. **Push the durable facts to the pages** that own them, per `90-Skills/page-update.md`. A durable fact is one that will still matter in three months: a standing decision, a term, a role, a system change. Meeting chatter stays in the filed note.
6. **Push every number to `00-Meta/numbers-ledger.md` with the transcript as the source and the meeting date as the as-of date.** A number spoken on a recording is recorded as spoken and labelled as such: "as spoken on a recording, not a verified figure."
7. **Add every action with a named owner to `10-Business/eos/to-dos.md`**, in that owner's group, with the transcript wikilink as the source and the meeting date as the raised date. Where the source names nobody and no owner is obvious from the source itself, the line reads **"unassigned"**. Do not infer an owner.
8. **Create a ClickUp task per action** using the `meeting-transcript-to-clickup` skill, matching the owner and the deadline recorded in step 7.
9. **Append one line to `00-Meta/log.md`**: the date, the transcript filed, the pages touched.
10. Update the owning folder's `MOC-*.md` file list with a wikilink to the filed transcript and to any page it fed.
11. Report back: the filed note's name and home, the decisions found, the pages touched, the to-dos added and the ClickUp tasks created.

## Output

- One filed note in the owning folder's `meetings/`, raw text intact.
- Updated pages, each carrying the new fact with the transcript cited.
- New rows in `00-Meta/numbers-ledger.md` for every number.
- New lines in `10-Business/eos/to-dos.md`, one per action, grouped by owner.
- One ClickUp task per action.
- One appended line in `00-Meta/log.md`.

## Rules for this job

- **An action gets a deadline only if a deadline was actually said.** No inferred dates, no "by end of week" unless someone said it.
- **Never attribute a quote to a named person unless the transcript names them as the speaker.** Unattributed is correct; a guessed attribution is not. Where a transcript is a summary rather than a verbatim record, say so on the filed note.
- **Anything unplaceable is flagged, never guessed**: an unclear owner, an unclear property, an unclear date, a name that matches two people in `10-Business/people/`. Two names are already ambiguous in the register: "Alex" could be Alex Fals or Alexander Stuart, and "Chris" is not established as Chris Pitzer. Leave them ambiguous.
- **Nothing is deleted.** The raw transcript stays in the filed note in full. Superseded material retires to `99-Archive/`.
- `00-Meta/log.md` is **append-only**. Never rewrite an old entry.
- **Never reproduce any individual's personal compensation** on a page or in the ledger. A recording that discusses someone's salary, bonus or equity gets that passage left in the raw transcript and **not** promoted to any page, ledger row, to-do or ClickUp task.
- **Ask before acting on anything in these four areas.** Analysis and drafting are fine, action is not without a yes:
  - **Anything with a resident's name on it**: notices, demand letters, evictions, deposit claims. Draft only; never send, never file. A resident name mentioned on a recording does not become a page.
  - **Investor and board material**, especially anything touching the Bedrock Fund II LPs while the fund is open.
  - **Personnel matters:** a filed note about someone's performance or fit goes to Austin only and is never distributed. Assessments stay in `10-Business/people/_private-assessments.md`, not on the person's page.
  - **Money out the door:** invoice approvals, pricing changes, wires. A recording that agrees to spend money produces a to-do, not a payment.
