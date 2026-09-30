# Skill: the End of Day Close

The other half of the loop. `/morning` tells Austin what is coming. This tells the Brain what actually landed, and it asks about the things that probably got handled on a call and never got written down.

**Austin writes nothing on the front end.** No journal prompt, no blank page, no form. Claude does the sweep, files what moved, and generates one file. The file carries at most three questions. He answers them or he does not, and either way the day got filed.

To run it: tell Claude "run the end of day close", or paste everything below the line. It also runs unattended at 6pm on weekdays.

---

You are running the End of Day Close for Austin on this AI Brain.

## Why this exists

Rule 11 in [[CLAUDE]]: the absence of a written reply is not evidence that something is open. Things get resolved on calls, in cars, and in person. This close is the mechanism that catches them. Every night it picks the handful of items most likely to have been settled offline and asks, instead of letting them rot in a register for eleven days the way items 7 and 8 in [[00-Meta/commitments]] did.

The failure this prevents is not a missed task. It is a register nobody trusts because half of what is on it is already done.

## Get the date right before anything else

**The session clock is UTC. Austin is Eastern.** Between 20:00 and 24:00 Eastern the UTC date is already tomorrow, which is exactly when this skill runs. Taking the date from the environment header will sweep the wrong day and file the close under a date that has not happened yet.

Run `TZ=America/New_York date` first and use that answer. "Today" means 00:00 to 23:59 Eastern, which is 04:00Z to 04:00Z the next day. Convert every timestamp to Eastern before writing it into the file. **This is not a hypothetical:** the first run of this skill, on 2026-08-30, hit it.

### One `date` call is not enough. Added 2026-09-16 after this skill was the third victim

**The clock on this machine is not merely offset, it jumps, and a single reading cannot detect that.** On 2026-09-16 three routines read three different times on the same day: the morning brief got 05:39 ET against a true 10:10, a close run got 17:31 ET against a true 22:40, and the filesystem stamped a write at 19:41 in between. **An offset would be consistent and this is not**, so "run `TZ=America/New_York date` first" is necessary and insufficient.

**So take three readings from three sources before sizing anything, and require two to agree.** `date`, `date -u` converted to Eastern, and **the newest row in `00-Meta/audit-log.md`**, which is the one that has actually caught this twice. Other sessions append to that log with Eastern stamps, so a `date` reading earlier than the newest audit row is wrong by definition.

**Then check the day's own newest evidence before you believe the answer.** The newest message in Sent Items and the newest Teams message are both floors on the current time. A close that thinks it is 17:31 while the audit log carries rows stamped 18:38 is not early, it is broken.

**Why this rule is in this file and not only in the agent brief.** The 2026-09-14 Weekend Pulse hit this fault and wrote no rule. The 2026-09-16 morning brief hit it, wrote the rule into `95-Agents/morning-brief.md`, and recorded in its own audit row that **this skill inherits the defect and was not edited.** It then fired here within hours, on the exact file that had been named. `KP-0115`.

**What a wrong clock costs here specifically, and it is worse than in a brief.** This skill *writes*: it allocates register IDs, appends audit rows and **overwrites `00-Meta/daily-close/YYYY-MM-DD.md`**. A run that believes it is five hours earlier than it is will re-sweep a day another run has already closed, allocate IDs another run already took, and **clobber a finished close file with a staler one.** All three happened on 2026-09-16.

**So before writing anything, check whether today's close already exists and already ran.** If `00-Meta/daily-close/<today>.md` is present, or the register's high water mark is above what the last close recorded, **another run got here first**: read it, then revise or refresh it per the refresh rules above rather than starting a fresh close over the top of it.

## Plaud lags the day, so expect to run this twice

**Found 2026-08-31, on the first working-day close.** The 18:10 ET run missed two recordings from that same day. One had not finished uploading. The other had uploaded but not transcribed, and was filed as a placeholder concluding that transcription needed triggering by hand. It did not. It simply had not finished, and it appeared ninety minutes later.

**So: a close is provisional until the day's Plaud recordings are all processed.** Check the count against the calendar before writing. If a recording is present but has no transcript, say so in the file and **do not conclude anything about why**. The honest line is "not transcribed yet", not a theory about the app.

**A refresh is a rewrite, not an append.** When new material arrives:

- **Re-rank all four blocks.** New facts change what belongs in Today and what deserves one of the three question slots. A refresh that only appends is a refresh that pretends nothing was reordered.
- **Say at the top that the earlier version is superseded, and what was missing from it.** Austin may have already read it.
- **Keep the superseded reasoning in `99-Archive/`, do not delete it.** The placeholder above was wrong within hours and that is worth having on the record. Same precedent as the 2026-08-29 retraction: *a recording that yields nothing today may yield tomorrow.*
- **Fix any register header that describes the pre-refresh state.** On 2026-08-31 the commitments header said "nothing opened" ninety minutes after item 25 opened. A ledger whose header disagrees with its body is the failure this Brain has already recorded twice.

**Plaud mechanics worth not rediscovering:** `list_files` takes `date_from` / `date_to`; `get_transcript` needs `limit: 500` or it pages at 50; `start_at` and `created_at` are **UTC** while the recording's own title is **local ET**.

## The sweep

Read only. Nothing gets sent, nothing gets replied to.

0. **Re-read the previous close file first, looking for answers typed into it.** Added 2026-09-01 after this skill lost one for a day. This file tells Austin he may *"type under the question in the close file"*, and on 2026-08-31 he did exactly that: `*--> Same person*` under question 2, answering whether Kippy and Laurence Brokaw are the same man. **Nothing read it back.** The row it closed sat in [[00-Meta/commitments]] as *"still unanswered, ask 2 of 3"* for a full day while counsel kept running two workstreams against the same person on the assumption they were two. **A reply path this skill advertises and never checks is worse than one it does not offer**, because he used it correctly and the cost landed on him. Read the file, not just the register. Answers may be one line, may be unsigned, and may sit under a question rather than at the top.

1. **Calendar, today.** What was actually on it, converted to Eastern. Note who he was in a room with, because that is the strongest signal for the questions later.
2. **Outlook, today.** The folders named in [[10-Business/outlook-folder-map]], not the Inbox alone. Inbox, Sent Items and **For Signature** at minimum. Sent Items matters more than the Inbox: it is where his own commitments live. For Signature is where the day's capex kickoffs and closeouts land. **Read every message, not only the unread ones, and never infer disposition from read state**. Austin clears unread as a habit and reads things he then forgets. Pending comes from Adobe Sign: no `Completed:` and no `Canceled` notice, or a live `Reminder: Waiting for you to approve`. The folder map has the full test. Report the count and the properties; do not copy the queue into a register, the folder is its own register.
3. **Teams, today.** Chats and channels.

2b. **The a2zcp mailbox, today. Added 2026-09-03 and it is not optional.** The second mailbox, read through the **Google connector**, carrying `austin@a2zcp.com`, `austin@thebedrockgrp.com`, **`ir@thebedrockgrp.com`** and the billing addresses. Scope, labels and IDs are on [[10-Business/a2z-mailbox-map]]. **Read `in:inbox` first here, which is the opposite of the Outlook rule**, because Austin does not file this mailbox to zero: its Inbox holds 4,803 messages while the Parakeet one holds 330. Then the labels that carry a waiting human: To Respond, the Superhuman Respond and Waiting labels, TO DO, Accounting and Legal. **A Gmail search preview shows only the OLDEST messages in a thread with no truncation marker, so a closed item reads as open. Call `get_thread` before putting anything in the file.** That trap is rule 11 in connector form.

**Priority weighting, 2026-09-03.** Austin: *"nothing in personal and need more hands and eyes on the a2zcp and bedrock account."* **This mailbox is not the one that gets read if there is time left.** Per [[CLAUDE]] rule 14, it gets first class attention here, and **where this run has to be cut short, Outlook is what gets cut**, because Outlook has weeks of prior coverage under it and this one has days. Read `in:inbox` to exhaustion before extending Outlook past Inbox, Sent Items and For Signature. **The personal Google account is not a content source and nothing is harvested from it.**

**And state both mailboxes in the file.** [[CLAUDE]] rule 14 as extended 2026-09-03: a sweep that does not say which mailboxes it read is not a sweep, and "second mailbox not reachable" is a complete answer while silence is not. **The reason this exists in one line:** `CM-25`, `CM-26`, `CM-27` and `CM-28` are all Bedrock matters, and every one of them was invisible to this close until 2026-09-03 because the LP base writes to an address no sweep could see.

4. **The registers.** [[00-Meta/commitments]], [[00-Meta/parked-decisions]], [[00-Meta/open-items]], [[60-Communities/open-items]], [[10-Business/eos/to-dos]].
5. **The archive.** `99-Archive/` and today's `00-Meta/log.md` entries, so nothing already closed gets raised again.

If a source is down, say so in the file in one line and carry on. A partial close beats no close. Never guess at what a dead connector would have said.

## The routing

Anything that clearly moved gets filed before the file is written, into whichever register owns it. The five registers do not overlap, and [[CLAUDE]] defines the grain of each:

- New corporate commitment, or a next action that changed, goes to `00-Meta/commitments.md`
- A decision that got made goes to `00-Meta/decisions-log.md`
- A decision waiting on his ruling goes to `00-Meta/parked-decisions.md`
- Property level follow ups go to `60-Communities/open-items.md`
- Anything with a named owner goes to `10-Business/eos/to-dos.md`, grouped by owner
- Something that closed retires to `99-Archive/` with its close date

Every one of those changes gets a row in `00-Meta/audit-log.md` with its reason, per rule 13.

## The questions, which are the point of this skill

**Highlight three. Do not hold the rest.** Rule 12 as revised 2026-09-01 is show everything, highlight three, so a fourth live question gets one line in a short tail with its ask count rather than being dropped. Two highlighted is fine. Zero is fine on a quiet day. *Corrected 2026-08-31 evening: an earlier run wrote "Held, not asked" on a Critical item, which was right under the old ceiling and wrong under this rule.*

**What makes a good question.** An item that is open in a register, where there is a real chance it got handled somewhere Claude cannot see. Rank candidates by:

1. **Contact.** Was he in a meeting, a call, or a car with the person who owns it in the last few days? Calendar and Plaud are the evidence. This is the strongest signal by far.
2. **Silence with age.** Open a while, and the channels have gone quiet rather than active. Active argument means it is genuinely open. Silence after activity usually means it resolved.
3. **Stakes if it really is open.** Safety, a statutory deadline, a capital partner, or money already out the door beats housekeeping.

**What makes a bad question.** Do not ask about something with written movement in the last two days, that is obviously still in flight, or that he answered in a previous close. Do not ask him to confirm something Claude can verify itself by reading a file. And never ask a question whose only purpose is to make the file look thorough.

**How to write one.** Three lines. What the item is, what Claude actually knows with its confidence label and date, and the ask. Give him the disposition in advance so a one word answer is enough:

> **2. Great Oak boil water notice**
> Open since 2026-08-26, no owner, silent across five channels. Source is the road trip review, SINGLE-SOURCE, never corroborated.
> Cleared? Yes and I archive it with today's date. No and I put it in front of Natalie on Tuesday.

**Track the answers.** A question he answers gets acted on immediately and never asked again. A question that goes unanswered three closes running stops being a question: it moves to `00-Meta/parked-decisions.md` as something waiting on his ruling, and the file says that is what happened. Nagging is how a tool gets ignored.

## The fifth block, added 2026-08-31 at Austin's instruction

**His words:** *"feel free to ask some questions in the morning update and daily close. it will only help us grow faster."* He is loosening a constraint he set himself six days earlier, and the loosening is real. **It is not a repeal.**

**The distinction that keeps this from killing the close.** The three questions in *Confirm or correct* are **dispositions**: an item is sitting in a register and he can close or redirect it in one word. They are operational and they have consequences. **What I don't know** is a different animal: it asks about **context this Brain is missing and will keep being wrong about until someone says.** Convention, history, who actually decides something, what a term means in this house, why a thing is done the way it is. The RV comp-set correction of 2026-08-31 is the model. One sentence from Austin fixed two wrong readings and surfaced an unrecorded decision on the central question of a case. **That sentence was never asked for. It arrived by luck.** This block is the attempt to stop relying on luck.

**Why they stay separate.** Mixing them turns three consequential questions into five of mixed weight, and the block that gets skimmed is the block that gets skipped. Three dispositions highlighted, **up to two** context questions highlighted, and this one is explicitly optional in the file's own words. **Both caps are about question fatigue, not about hiding items**. Every live question still reaches the page, which is what keeps this compatible with rule 12 rather than an exception to it.

**What makes a good one.**

1. **Something this Brain got wrong, or nearly did.** A correction he made, a reading that only survived because nobody acted on it. Ask what the general rule behind it is, not just the specific fix.
2. **A convention everyone inside the company knows and nothing here records.** House shorthand, who signs what, what a number is normally measured against, which system wins when two disagree.
3. **A "why" behind something already filed as a "what".** The registers are full of facts with no reasoning attached, and the reasoning is what makes the next judgement call right.

**What makes a bad one.** Anything answerable by reading a file: go read the file. Anything that is really a task wearing a question mark. Trivia. And **never a question whose answer would not change what this Brain does next**; if the answer changes nothing, it is curiosity being charged to his evening.

**Track them the same way.** Answered means recorded as a durable convention on the page that owns it, with the date and his words, and never asked again. **Unanswered twice means drop it, not three times**. A context question has no clock on it, so it earns less patience than a disposition, not more.

## The file

One screen. Four blocks, in this order, and nothing else.

```
# Daily close, [Weekday] [YYYY-MM-DD]

## Today
Three lines, maximum. What changed, not what was scheduled. A calendar recap is
worthless to him because he was there. If nothing changed, one line saying so.

## Filed
What got routed and where, one line each, maximum three. Full paths so he can open
it without hunting, per rule 3. If nothing, "Nothing new to file."

## Confirm or correct
Three highlighted, in the format above. Any other live question gets one line in a
short tail carrying its ask count. Nothing is held back. If there is genuinely nothing
worth asking, "Nothing to confirm tonight." Do not manufacture questions.

## What I don't know
Up to two highlighted. Context questions, not dispositions. Skippable and marked as such.
Omit the block entirely on a day that produced nothing worth asking.

## Tomorrow
Three, ranked, and the first one is the one that matters. Each is a next action he
can start, not a topic. Include anything the calendar makes unavoidable.
```

Write it to `00-Meta/daily-close/YYYY-MM-DD.md`. Add one line to `00-Meta/log.md`.

## How he answers

**Say where, in the file itself, every time.** Austin asked "where do I answer the what I don't know" on 2026-08-31, and he was right to: the file said "answer any way you like" and never named a channel, which is useless to someone reading it on a phone at the end of the day. **A question with no stated reply path is not really a question.** The line to carry: reply in the chat, which is the fastest because the chat is read every turn; or type under the question in the close file; or say it into Plaud. **And name the one that does not work**. Artifact comments are pull-only and sit until a scheduled run reads them.

Any way he wants. In chat the next morning, typed into the file under the question, or spoken. "1 yes, 2 no, 3 handled last week" is a complete answer and must be treated as one. Never send him back a form. Never ask him to use a particular format.

When answers come in, act on all of them in one pass, then say in two lines what closed and what stayed open. Do not narrate each one.

## The rules

- **He writes nothing unless he wants to.** The close completes whether or not he ever opens it. This is the design constraint that keeps it alive.
- **Read only on the sweep.** No email sent, no reply, no calendar change. Guardrails 5 through 8 in [[CLAUDE]] apply in full.
- **Show everything, highlight three, on every block.** Rule 12 as revised 2026-09-01. More than three exists means the extras get one line each, not that they get held. The `What I don't know` block keeps its own cap of two, authorised by Austin on 2026-08-31 - that cap is about question fatigue, not about hiding items, and it survives the rule change.
- **Confidence label and source on every substantive claim.** Rule 10. A question built on an unlabelled claim is how a wrong item gets confirmed.
- **Check the archive before asking.** Rule 11. Asking about something he closed last week is worse than not asking at all.
- **No em dashes or en dashes.**
- **Quiet day, short file.** If nothing happened, the file says so in four lines and stops. A padded close teaches him to skip it.

---

## The close has two surfaces now, added 2026-09-03 on Austin's instruction

**His words:** *"The formatting of the daily close files sucks. how do we fix this. can you create a html artifact that refreshes to current day."*

**The markdown file stays the record. The artifact is how it gets read.** Same content, two surfaces, and neither replaces the other. The file is what the next run reads back for typed answers and what the archive keeps; the page is what he opens on a phone at the end of the day.

### The artifact

**URL, stable, never changes:** `https://claude.ai/code/artifact/d1029025-c78b-496b-8f9c-4de8e2c3fcf2`

**"Refreshes to current day" means the run republishes to that URL, not that the page polls anything.** A published artifact is static HTML. **Every close run rebuilds the page and republishes to the same URL**, so the link always shows the newest close and never has to be re-found. This is the same pattern the open board already uses. **Never publish a close to a new URL** - a second link is how a stale one gets read.

**The page carries the last few closes, newest first, with a date switcher.** So "yesterday" is one click rather than a file hunt, and the typed-answer path still points at the markdown. **Do not put more than about five closes in it**; it is a reading surface, not the archive.

**Structure, and each device is carrying information rather than decorating:**

- **Confidence chips** on a question, from rule 10. Green VERIFIED, yellow SINGLE-SOURCE, outlined INFERRED. No chip means the claim is not the load-bearing part.
- **Ask-count dots.** Filled dots against three, so *ask 2 of 3* is readable without counting, and the third dot filling is the visual warning that the question converts to a parked decision.
- **The disposition split.** Every question ends in a two-branch Yes / No block. **This is the whole point of the close** and it was buried mid-paragraph in the markdown. If a question cannot be written as two branches, it is not ready to ask.
- **Left edge severity.** Red for the ones that cost the most to ignore tonight, yellow for the rest.
- **Numbered ranking in Tomorrow**, first one filled, because that block genuinely is a sequence.

**Guardrails apply to the page exactly as they do to the file.** An artifact is private to Austin until he shares it, and it is one share away from anyone. **The close routinely carries counsel matters, a capital partner and a personnel transition**, so it stays unshared, and nothing goes on the page that guardrails 5 to 9 keep out of the file. **No resident name, no compensation figure, ever.**

### The formatting rules for the markdown, which is where the problem actually was

**The file was unreadable because of how it was written, not because markdown is the wrong format.** Fix the writing and both surfaces improve.

1. **One bold phrase per paragraph, maximum.** This is the single biggest fix. Recent closes bolded roughly a third of every paragraph, and **emphasis on everything is emphasis on nothing.** Bold the claim, never the evidence around it.
2. **The disposition gets its own two lines, always.** `Yes and <what happens>.` then `No and <what happens>.` Not one run-on sentence, not buried at the end of the evidence paragraph.
3. **Confidence label and ask count sit on their own short line**, ahead of the evidence, not threaded into a sentence.
4. **Every reference ID in backticks**, every time, so it is greppable and renders as a chip.
5. **Three sentences per paragraph in Today.** If it needs four, it is two paragraphs.
6. **No em dashes or en dashes**, unchanged.

### The order of operations

Write the markdown close first, then build the page from it, then republish. **The file is the source; the page is generated.** If the two ever disagree, the file wins and the page gets rebuilt.

### The page is now a reply path, which means step zero grew

**Austin, 2026-09-03:** *"so yes no, isn't clickable. is there a way to have other and to be able to respond confirm or add notes to the artifact that updates the brain."*

**Every question on the page is now three buttons and a note box: Yes, No, Other.** Main questions, the terse tail, and the `What I don't know` items all carry them, plus one free text box at the bottom for anything none of the questions asked. Answers save the instant he clicks.

**Where they land.** The artifact has a `db` capability. Answers write to the `answers` collection, one document per question, id `<date>__<qid>` (`2026-09-02__1a`, `2026-09-02__t7`, `2026-09-02__u1`). Free text lands in the `notes` collection. Body: `date`, `qid`, `choice` of `yes` / `no` / `other`, `note`, `at`, and `status`, which starts at `new`.

**READ THEM AT THE START OF EVERY RUN. This is the whole point and it is where this skill has failed before.** Step zero already says re-read the previous close file for typed answers, and it says that because on 2026-08-31 he typed *"--> Same person"* under question 2, nothing read it back, and a row sat wrong in [[00-Meta/commitments]] for a full day while counsel ran two workstreams against one man. **A reply path this skill advertises and never checks is worse than one it does not offer**, because he used it correctly and the cost landed on him. **There are now three reply paths and all three get read before anything else:**

1. **The artifact database** - read the `answers` and `notes` collections for the last few dates.
2. **The previous close file** - typed answers under a question.
3. **The chat** - which is still the fastest and is read every turn.

**After acting on an answer, set its `status` to `applied` with the date**, so the next run does not re-apply it and so an unapplied answer is visible as a gap. **Never delete an answer to mark it done.** Same rule as everywhere else in this Brain: nothing is deleted, state changes on the row.

**The loop was verified end to end on 2026-09-03**, not assumed: a document was written from the publishing session, read back, and deleted. **Do not describe this path as working in a future session without checking it**, because a silently broken reply path is the exact failure above.

**What the page cannot do, said plainly so nobody promises it.** Clicking a button does not edit the vault. **It records the answer; a run applies it.** So an answer given at 22:00 lands in the Brain at the next morning brief or close, not immediately. If he wants something applied right now, the chat is the path, and the page says so on its face rather than implying otherwise.

**One security note that came free.** Declaring `db` makes the artifact organization internal, so it cannot be shared publicly at all. Given the close routinely carries counsel matters, a capital partner and a personnel transition, that is the right constraint rather than a limitation.
