# Skill: Transcript Filing

Turns a raw meeting transcript into a filed, useful note: summary on top, decisions pulled out, pages updated, nothing deleted.

To run it: drop the raw transcript into `05-Inbox/` and tell Claude "file the new transcript", or paste everything below the line.

---

You are filing a raw meeting transcript from `05-Inbox/` of this AI Brain.

## The job

1. **Find the raw transcript:** the unfiled file in `05-Inbox/` (or the text the user just gave you). If more than one is unfiled, ask which to do first.
2. **Reshape it** into the filed format below: date and meeting name as the title, who was there, a three-to-five sentence summary, decisions pulled out one per line, actions as a checklist. Keep the full raw text at the bottom. The summary sits on top of the source and never replaces it.
3. **Name it** `YYYY-MM-DD-meeting-name.md`, using the meeting date. If the date isn't in the transcript, ask. Never guess a date.
4. **File it** in a `meetings/` subfolder of the folder the meeting was mostly about: a sales call lands in `50-Products-Sales/meetings/`, a job debrief in `70-Operations/meetings/`. Can't tell? It stays in `05-Inbox/` with a note. Flagged, never guessed.
5. **Push to the pages.** Decisions and durable facts go onto the relevant pages per `90-Skills/page-update.md`; numbers go to `00-Meta/numbers-ledger.md` with the transcript as source. The filed note lists which pages were updated.
6. **Log it:** one line in `00-Meta/log.md`. Update the owning folder's MOC file list (a `[[wikilink]]` to the filed transcript and to the page it fed).
7. **Report back**: the filed note's name and home, the decisions found, the pages touched.

## The filed format

```
# YYYY-MM-DD: [meeting name]

**Who was there:** names, comma-separated.
**Filed:** YYYY-MM-DD, by Claude.

## Summary
Three to five plain sentences: what the meeting was about and where it landed.

## Decisions
- The decision, one line each. These also get pushed to the relevant page.

## Actions
- [ ] **Owner:** does what, by when (only if a date was actually said; never invent one).

## Pages updated
- [[page-name]]: what changed on it because of this meeting.

## Full transcript
The raw text, kept in full below the fold. Nothing deleted.
```

## The rules

- Never delete the raw text. Filing reshapes; it doesn't remove.
- Actions only get a deadline if one was said in the meeting. Never invent a date or an owner.
- Anything in the transcript you can't place (an unfamiliar name, a job that has no folder) gets flagged in the filed note, not guessed.
