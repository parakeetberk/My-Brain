# Agent brief: Morning Brief

**The job in one sentence:** Every weekday at 6am, sweep Austin's calendar, mail, Teams and Plaud recordings, diff everything against what is already closed, and publish one phone readable artifact telling him what needs him today.

**Runs when:** Monday to Friday, 6am. Cadence set by Austin 2026-08-29, recorded in `00-Meta/decisions/2026-08-29-brief-delivery-artifact-only.md`. Also runs on request ("run the morning brief", "catch me up").

**Ported into this Brain 2026-08-31** from the Claude Code vault at `Documents/Claude/Code/brain/.claude/skills/morning-brief/`. Paths and house rules rewritten for this vault. The original still runs on its own schedule in the other vault, so expect both to write until one is retired.

Run `date "+%Y-%m-%d %H:%M %Z (%A)"` first. Never assume the date. Hard rule 3 and the CLAUDE.md datestamp warning both apply.

## Inputs

Read all of these before gathering anything. This step is not optional.

- `CLAUDE.md` at the vault root, the hard rules and the guardrails
- `00-Meta/commitments.md`, the commitment ledger, and the "Last reviewed" line at the top which carries yesterday's artifact URL
- `00-Meta/open-items.md`, ranked open items
- `00-Meta/parked-decisions.md` and `00-Meta/decisions/`, so a settled question is not reopened
- `99-Archive/`, including `99-Archive/2026-08-closed/`. List the directory and read every file.
- `00-Meta/numbers-ledger.md`, if the brief touches any figure

Then the live sources: `outlook_calendar_search`, `outlook_email_search`, `chat_message_search`, and the Plaud tools (`mcp__plaud__list_files`, `get_note`, `get_transcript`).

**Two mailboxes, added 2026-09-03.** `outlook_email_search` reaches `austin@parakeetcommunities.com` only. The second mailbox is the legacy holding company stream, read with the **Gmail tools** (`search_threads`, `get_thread`), carrying `austin@a2zcp.com`, `austin@thebedrockgrp.com`, **`ir@thebedrockgrp.com`** and the billing addresses. **Scope, label IDs and the connector traps are on [[10-Business/a2z-mailbox-map]]. Read it before the first call.** Three things that will otherwise cost a wrong brief: the Microsoft 365 connector cannot reach that mailbox and returns `ErrorInvalidUser`, its Inbox is the primary surface rather than the emptiest one, and **a Gmail search preview shows only the oldest messages in a thread**, so `get_thread` runs before anything is called open.

**Priority weighting, 2026-09-03.** Austin: *"nothing in personal and need more hands and eyes on the a2zcp and bedrock account."* **This mailbox is not the one that gets read if there is time left.** Per [[CLAUDE]] rule 14, it gets first class attention here, and **where this run has to be cut short, Outlook is what gets cut**, because Outlook has weeks of prior coverage under it and this one has days. Read `in:inbox` to exhaustion before extending Outlook past Inbox, Sent Items and For Signature. **The personal Google account is not a content source and nothing is harvested from it.**

**The brief states both mailboxes and their surfaces in one line**, per [[CLAUDE]] rule 14 as extended 2026-09-03. "Second mailbox not reachable" is a complete answer.

## Steps

1. **Diff against what is closed.** Hard rule 11. Absence of a written reply is not evidence something is open. Austin resolves things on calls, in cars and in person, and the archive is the only record. Any candidate finding gets checked against `99-Archive/` and `00-Meta/commitments.md` before it goes in the brief.

2. **Pick up dispositions on yesterday's brief.** The channel is artifact comments, not email. Read them with the Artifact tool, `action: "comments"`, using the URL on the "Last reviewed" line of `00-Meta/commitments.md`. Act on anything he left: update the ledger, move closed items to `99-Archive/2026-08-closed/` with the close date and his reason, and open today's brief with a short "Closed on your reply" block. Where a thread is activated for Claude, reply saying what you did, then resolve it.

3. **Sweep his own outbound, always.** Austin's Sent Items and Teams messages since the last brief, looking for actions that silently close a ledger item: a payment released, a question answered, an appointment booked. Most closures arrive this way rather than as an explicit disposition. His own outbound action is primary source evidence of closure. If both channels are empty, say so in one line. Never manufacture a closure.

4. **Today's calendar.** Every event with times, attendees, and whether anyone external is in the room. Flag conflicts, and flag any meeting where an open item involving an attendee will land. Calendar `start` and `end` come back as wall clock in the named `timeZone`, usually UTC even for meetings set in ET. Convert every one. Every timezone bug in this system has come from that field.

5. **New since the last brief.** Human correspondence only. Skip Rent Manager exports, AvidXchange queues, Paychex, Jotform, DocSend pings, Power Automate. Look for direct questions to Austin, deadlines, escalations, and anything where someone has now followed up more than once.

6. **Plaud recordings since yesterday.** Use `get_note` for the AI summary rather than full transcripts, cheaper and higher signal. This is where verbal commitments live and the only way to see them. `start_at` is UTC, `duration` is milliseconds. Confirm the note actually returns content: an empty result means the recording is unreadable, and you say so by name rather than assume it was covered. Do not infer a meeting's identity from its auto generated title alone, since titles describe topics and not attendees. Where title and calendar disagree, show both and flag it.

7. **Movement on the top ledger items.** State "no movement" explicitly where there was none.

8. **Ask before anything in the guardrails.** Hard rules 5 to 9 apply in full. Personnel matters are drafts to Austin only, never distributed. Nothing with a resident's name goes out. No money moves.

## His actual morning, and what it means for this brief

**Recorded 2026-09-04 from Austin, when the school year restarted:** he wakes at **06:15** and the car leaves at **07:25**. No meetings before 09:00.

**So the day has three windows and this brief serves the third.**

- **06:15 to 07:25 is reading time, on a phone, with two children getting ready.** He is not acting on anything here. The brief must be scannable in five minutes and legible one-handed.
- **07:25 to roughly 08:00 is the school run.** Nothing happens.
- **08:00 to 09:00 is the only uninterrupted hour he has all day.** **This is what the brief is actually for.** Every action it proposes must be sized to fit inside it, and the total of the easy wins should come to under thirty minutes so the hour has room for one real thing.

**Consequences that bind this job.** Publish by **06:00** so it is waiting when he wakes, never later. Put a minute estimate on every action. **If the easy wins total more than thirty minutes, cut the list rather than the estimates.** Lead with the single thing that would hurt most if the hour were spent elsewhere.

## Output

One artifact, published, and nothing else sent. Structure in this order:

1. **Emergencies.** Things that get worse on their own, or already have. **The test is not importance, it is whether waiting costs something.** Each carries the verbatim fact behind it and one action with a minute estimate. **If there are none, say so in one line and move on.** A quiet morning stated plainly builds more trust than a manufactured alarm.
2. **Easy wins.** Work that is already decided or already written and is waiting on a word, a send, or a signature. **Sized for the 08:00 hour, under thirty minutes in total.** Say what each one is waiting on, because that is usually the more useful fact than the task itself.
3. **Important projects.** Not for today. He needs the shape, not an action. Dated things inside two weeks, and the two or three programmes where the quarter is actually won.
4. **One delegation check.** Exactly one, every morning. Take one item from sections 1 or 2 and ask why it reached him: is it his by law or judgement, is it blocked on a missing person or a missing permission, or is it habit. **End it with a question he can answer in a sentence.** This is the section that compounds, and it is the input to the `business-coach` agent's monthly audit.
5. **Today's schedule**, with prep notes only on the meetings that need them.
6. **Everything else**, one line each. **Hard rule 12 lives here:** show everything found, and say how long the tail is, because its length is itself a finding.

**Anything that was closed by his reply since the last run goes at the very top, above emergencies, and only if there is something to report.**

Design: load the `artifact-design` skill first. Title `Morning Brief`, favicon a coffee cup. Fonts via Google Fonts: IBM Plex Sans Condensed for headings, IBM Plex Serif for body, IBM Plex Mono for times and data. Light tokens on bare `:root`, dark redefined under both `@media (prefers-color-scheme: dark)` guarded as `:root:not([data-theme="light"])` and `:root[data-theme="dark"]`. Palette light: paper `#F4F6F7`, card `#FFFFFF`, ink `#12171B`, muted `#5C666E`, rule `#D8DEE2`, signal `#B45309`, critical `#A32036`, ok `#16794A`, slate `#2F4858`. Dark: paper `#0E1317`, card `#161D23`, ink `#E6EAED`, muted `#94A0A8`, rule `#29333B`, signal `#E9A63F`, critical `#F2657C`, ok `#4FBF87`, slate `#9FC0D4`. Single column, `max-width: 640px`, 18px body. Left border stripes on cards, critical for urgent, signal for warning, ok for closed. Keep it identical day to day so it is instantly familiar. No horizontal scroll on the body.

Then update the vault:

- The **"Last reviewed"** line at the top of `00-Meta/commitments.md`: today's date, one line on what moved, and **the artifact URL**. Tomorrow's run needs that URL to read comments, so it is not optional.
- Anything closed moves to `99-Archive/2026-08-closed/` with the close date and reason.
- Genuinely new open items get added to the ledger with absolute dates and sources.
- One line in `00-Meta/log.md`, and the change with its reason in `00-Meta/audit-log.md`.

## Rules for this job

Beyond the hard rules in CLAUDE.md, which always apply:

- **Send nothing.** Not to Austin, not to anyone. Decided 2026-08-29, verbatim: *"let's drop it. keep it here."* Do not call `outlook_send_mail`, do not create a draft, do not message on Teams, do not drive Outlook through a browser. The artifact URL is the entire delivery. **Never report the absence of an email as a failure** and never reopen the `Mail.Send` or Chrome permission thread. Both were tried across four days and deliberately abandoned. Full reasoning: `00-Meta/decisions/2026-08-29-brief-delivery-artifact-only.md`.
- **Show everything, highlight three**, per hard rule 12 as revised 2026-09-01. Eleven things found means eleven things shown: three get the full treatment under `Needs attention`, and the other eight get one line each in a terse tail below `Resolved`. Nothing is ranked and held any more. Say how long the tail is when it runs long - its length is a finding.
- **Confidence label and source on every substantive claim**, per hard rule 10.
- **Never say Austin is behind.** Say what is un-indexed, un-decided or un-delegated.
- **A task instruction is not a source.** If this brief, a prior brief, or the ledger says something is true and the primary data disagrees, the data wins. Report the disagreement rather than laundering the error forward.
- **Teams meeting transcripts are disabled tenant wide.** A Teams meeting with no Plaud recording is invisible. Say so when it matters.
- If nothing is urgent, say so plainly and keep the brief short. A two item brief on a quiet day builds more trust than a padded one.

## The brief has two surfaces now, added 2026-09-04 on Austin's instruction

**His words, in the session that built this:** he asked for the same stable-link-plus-buttons treatment the daily close got on 2026-09-03, then said "yes let's start it now."

**Every prior morning brief published to a brand new URL each day.** That was fine for a page read once and archived, but it meant there was nothing to bookmark: yesterday's link was already dead by the time Austin wanted to check it from his phone. **That is fixed. The brief now republishes to one fixed URL, the same pattern the close already proved out.**

**URL, stable, never changes:** `https://claude.ai/code/artifact/eb013536-70e4-47aa-bb2d-3831e0fcc6d0`

**Every brief run rebuilds the page and republishes to that same URL.** Never publish a new one — a second link is how a stale one gets read, same rule as the close. The page carries the last few briefs, newest first, with a date switcher (`BRIEFS` array in the page source). Do not let it grow past about five; this is a reading surface, not the archive. The archived `.html` snapshot per day still goes to `99-Archive/2026-09-briefs/brief-YYYY-MM-DD.html` as before.

### The reply mechanism, copied from the close because it works

**The artifact declares a `db` capability.** Every substantive item on the page — each card under *Needs you before your first meeting*, each row under *Decisions only you can make*, each row under *Still open, carried forward*, and each *What I don't know* item — carries three buttons (Yes / No / Other) plus an always-visible note box. The note box is never hidden behind the Other button; the close shipped that bug on 2026-09-03 (a click saved but the typed note underneath it silently didn't, because the box was hidden until Other was pressed) and this page was built after that fix, not before it, so it starts correct.

**Where answers land.** `answers` collection, one document per question, id `<date>__<qid>` (`2026-09-02__n01`, `2026-09-02__d2`, `2026-09-02__o3`, `2026-09-02__u1`). Free text from the bottom box lands in `notes`. Body: `date`, `qid`, `choice` (`yes` / `no` / `other`), `note`, `at`, `status` (starts `new`).

**Read them at the start of every run, before anything else.** This is the same discipline the close's own history forced: a reply path advertised and never checked is worse than one not offered at all, because the person used it correctly and the cost still landed on them.

1. **The artifact database** — read `answers` and `notes` for the last few dates.
2. **The chat** — fastest, read every turn.

There is no third path here the way the close has a markdown file with typed-under-question answers, because this skill never wrote a separate markdown record — the artifact was always the only output. **Artifact comments are not a reply path for this page and were never checked reliably; do not tell Austin to use them.**

**After acting on an answer, set its `status` to `applied` with the date**, so the next run does not re-file it and an unapplied answer stays visible as a gap. Never delete an answer to mark it handled.

**What the page cannot do, said plainly.** Clicking a button does not edit the vault by itself. It records the answer; the next run applies it. An answer given at 11am lands in the Brain at tomorrow's 6am brief, not immediately. If Austin wants something acted on right now, the chat is the path, same as the close.

**Security note that comes free.** Declaring `db` makes the artifact organization-internal, so it cannot be shared publicly at all — the right constraint given this page routinely carries a $200k+ LP shortfall, a personnel separation, and named capital partners, none of which clears guardrails 5 through 9 for outside eyes.

### What this change did not touch

**This was a delivery-mechanism upgrade only.** The fixed URL and the reply buttons are what it changed. It did not touch the section order.

**CORRECTED 2026-09-08. The paragraph that stood here was stale and it cost a run.** It said the content structure was untouched, still Closed / Needs you / Today / New since yesterday / Decisions / Still open / What I don't know, and that the 2026-09-03 hold on the prototype restructure stood: Austin's *"don't set these routines yet."*

**Both halves of this file were true when written and they stopped agreeing on 2026-09-04.** The hold was lifted that day on Austin's instruction and the **Output** section above was rewritten to the new order: emergencies, easy wins, important projects, exactly one delegation check, the schedule, then everything else as a one line tail. **This paragraph was not rewritten in the same pass**, so the file specified the new order in one place and forbade it in another.

**What it cost, recorded so the shape is recognisable next time.** The 2026-09-08 run read this paragraph, honoured the hold, and published at 08:04 in the old section order with no minute estimates and no delegation check, on the one morning of the week Austin had already asked for all three. The page was rebuilt into the correct order and republished at 08:20. **The reason it is recorded rather than quietly fixed is that a self contradicting brief fails silently**: the run did nothing wrong by its own reading, and nothing in the file flagged the conflict.

**Both dates stay visible per the contradictions rule.** The 2026-09-03 hold was real. It was lifted on 2026-09-04. **The Output section above is the authority on structure**, and if these two ever disagree again, Output wins and the disagreement is itself a finding for `00-Meta/open-items.md`.

## Take a second clock reading before sizing anything, added 2026-09-16

**The rule: call `date` twice, from two sources, and treat a disagreement as authoritative over the first reading.** `date`, then `date -u` or the Windows clock, before any action is sized against a time and before a sweep window is computed.

**Why, and it has happened twice in three days.** On 2026-09-16 this job's opening `date` call returned **05:39 EDT** when the true local time was about **10:10 ET**. A complete brief was built and published on that reading. It stated the 06:15 window and the 08:00 block were intact when both had gone, it made its recommended action *settle budget week at the 09:00 check-in* when that meeting was already over, and **its sweep window stopped six hours short**, hiding two closures, a counsel question about sexual misconduct allegations and a second chase from a lender.

**It was caught by a register rather than by a clock.** `00-Meta/audit-log.md` held rows stamped 08:05, 08:40 and 09:45 ET written by other sessions the same day, which is impossible if it is 06:00. **That is a usable backstop and it belongs in this rule**: if the audit log's newest row is stamped later than the time you think it is, the clock is wrong, not the log.

**The 2026-09-14 Weekend Pulse hit the identical fault** and recorded it on `00-Meta/commitments.md`, where `date` returned 2026-09-13 18:09 EDT and then 2026-09-14 09:26 EDT on a re-check. **It recomputed its own window and wrote no rule, so this job inherited nothing.** That is why this section exists rather than another incident note.

**What a wrong clock corrupts, all at once and none of it loudly.** Action sizing against his day, the publish time stated on the page's own face, the sweep window computed from *now*, and every audit and log stamp the run writes. **A brief that is merely late says so. A brief built on a false clock asserts that it is early**, which is worse, because it sends him to meetings that have finished.

**`KP-0115`.** The same opening applies to `90-Skills/end-of-day` and [[95-Agents/weekend-pulse]], which each open with a single `date` call.
