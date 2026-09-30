# Agent brief: Weekend Pulse

**The job in one sentence:** Every Friday evening, review everything that moved across Parakeet and the affiliates over the last fourteen days and publish one deliberately exhaustive artifact, so Austin can read the whole company over a weekend instead of triaging it.

**Runs when:** Friday, 7pm. Cadence set by Austin 2026-08-29, recorded in `00-Meta/decisions/2026-08-29-brief-delivery-artifact-only.md`. Also runs on request ("weekend pulse", "what is going on everywhere", "give me the full picture").

**Ported into this Brain 2026-08-31** from the Claude Code vault at `Documents/Claude/Code/brain/.claude/skills/weekend-pulse/`. Paths and house rules rewritten for this vault.

Run `date "+%Y-%m-%d %H:%M %Z (%A)"` first. Never assume the date.

**Window: the 14 days ending today, inclusive.** Compute both endpoints from the verified date and state them in the report. Every date written is absolute.

## This job was the exception, and as of 2026-09-01 it is the norm

Rule 12 used to put a three item ceiling on anything presented to Austin, and this job was carved out of it by his own instruction. **On 2026-09-01 he generalised that instruction to everything**: show it all, highlight three. So this page is no longer an exception, it is the pattern - and the instruction below is worth keeping on the record, because it is the same preference stated three days earlier in narrower form. Verbatim, 2026-08-28:

> *"look back two weeks and include more than less. don't filter, list everything that might still be a to do but also list out all deliverables i am waiting on and what others are working on so that I can get a good pulse of everything going on around the company... this report should be a fullsome report that does not limit scope at all... er on the side of inclusion rather than limiting any type of scope."*

The morning brief triages. This one covers. Do not rank and hold, do not summarize away detail, and if you are unsure whether something belongs, put it in with a confidence label rather than dropping it. Only section 1 ranks. Anyone later "correcting" this brief back to three items has misread rule 12.

## Inputs

Read all of these before gathering anything.

- `CLAUDE.md`, the hard rules and the guardrails
- `00-Meta/commitments.md`, the commitment ledger
- `00-Meta/open-items.md`, ranked open items
- `00-Meta/parked-decisions.md`, `00-Meta/decisions/`, `00-Meta/decisions-log.md`
- `00-Meta/delegation-board.md`, for who owns what
- `99-Archive/`, including `99-Archive/2026-08-closed/`. List the directory and read every file.
- `00-Meta/numbers-ledger.md`, mandatory before any figure appears in the money section
- The two most recent daily closes in `00-Meta/daily-close/`, so you know what was already surfaced
- `10-Business/people/` for the roster, `60-Communities/` for property context, `30-Customers/capital-partners/` for Jadian and the LP base

## Steps

1. **Diff against what is closed.** Hard rule 11, and it still applies in an inclusive report. Never present a closed item as though it were open.

   **The twist for this job:** closed items are not dropped, they get their own section. Austin has ADD and completed work becomes invisible to him. A well populated "Closed in the last two weeks" section is one of the most valuable parts of this document. The rule is about labelling, not omission.

2. **Plaud, the richest source.** `mcp__plaud__list_files` with the window, then `get_note` on each substantive recording. Prefer `get_note` over `get_transcript`. `start_at` is UTC, `duration` is milliseconds. Cross check against the date line inside the note body, usually already ET. Recordings under about 60 seconds are usually accidental. Near identical `start_at` values usually mean a double tap, not two meetings.

   Site visit recordings are the best source of property level to-dos that exist nowhere in writing. Mine them hard. Every "we should", "tell so and so", "get that fixed" is a candidate.

   **Verify coverage, do not assume it.** A recording can exist and still return nothing. If `get_note` comes back empty, try `get_transcript` with `block: transaction` then `outline`. If both are empty the recording is unreadable and you name it in Blind Spots. A recording on a different device serial from the rest of the corpus is the likeliest to be unprocessed.

   **Attribution.** Do not infer a meeting's identity from its Plaud title alone, and do not infer it from a calendar slot alone. Auto generated titles describe topics, not attendees. Where title and calendar disagree, present both readings and flag the contradiction rather than picking one. Convert the calendar's UTC wall clock before comparing.

3. **Email, both directions.** `outlook_email_search` across the window, Inbox and Sent Items, paginating with `offset` until exhausted. The mailbox runs 100 to 150 messages a day and is heavily automated. Skip the machine noise. Keep everything human. **Austin's Sent Items matter as much as his Inbox here**, because that is where his own open commitments live: "I'll get you that", "on my list today", "let me confirm in the morning". Harvest them systematically. Known gap: at least one additional mail folder holds live business threads (Gunster and Belle Haven, Walton Street, some payment replies) that prior sweeps reached only by keyword search, never by enumeration.

4. **Teams.** `chat_message_search` across the window, paginating. Date filtered searches scan up to 50 chats by 50 recent messages each, so coverage is good but not complete. Expect HTTP 429 on deep pagination, and report how many chats were actually scanned. Watch the Finance chat, the L10 chat, Parakeet Management, and the 1:1s with Jon, Zach, Natalie, Demetria and Leslie.

5. **Calendar, two weeks back and the week ahead.** Two purposes: reconstruct which meetings happened so recordings can be matched and gaps found, and look forward seven days so the report ends with what is coming. Convert every UTC wall clock. A recurring meeting can change both name and time between weeks, so check the instance and not a sibling week. Flag that **Teams transcripts are disabled tenant wide**, so a Teams meeting with no Plaud recording is invisible, and name the meetings in the window that fall in that hole.

6. **Optional, only if the sweep points there.** Ramp (`ramp_get_attention_feed`, `ramp_get_missing_items_by_user`) and SharePoint search. Do not go fishing.

7. **Route every finding, do not just report it.** Per CLAUDE.md "How findings get delivered": draft the email to whoever owns it, add it to the relevant page, put a named task in `10-Business/eos/to-dos.md`, and log the change with its reason in `00-Meta/audit-log.md`. Where no owner exists in any source, the task says **unassigned** and names the forum where Austin can settle it. Never a guessed name.

8. **Ask before anything in the guardrails.** Hard rules 5 to 9 in full, and two bite hard on this job specifically. See "Rules for this job" below.

## Output

One artifact, published, and nothing else sent. Eleven sections in this order, each a full list rather than a top three.

1. **Read this first.** Five to eight sentences: what moved, what is stuck, what is at risk, and the two or three things that would change most if he touched them this weekend. The only part that ranks.
2. **Corrections to what you were told earlier.** Anything this sweep changes about what previous briefs or the ledger asserted. Short and factual. Where a contradiction cannot be resolved, say so instead of picking a side.
3. **Deliverables Austin is waiting on.** Table sorted by days outstanding, longest first: What, Who owes it, Since (absolute date), Days, Last movement, Confidence. If nobody was ever actually asked, say so in the row. "No commitment ever made" is different from "committed and late".
4. **Austin's own open commitments.** The mirror image, and the one people forget. Same shape: What, Who is waiting, Promised on, Days, His words verbatim, Confidence.
5. **What everyone is working on.** One block per person: current workstreams, blockers, what they owe, what they are owed, and any capacity or performance signal from the fortnight. Cover everyone who appears substantively, plus key externals as their own short blocks: accountants, capital partners, manufacturers, brokers, counsel, active vendors.
6. **Everything that might still be a to-do.** Grouped by domain: Property and Operations, Construction and Supply Chain, Finance Tax and Accounting, Legal and Insurance, Systems and AI Build, People and HR, Capital Deals and Dispositions, Personal and Admin. One line per item with source and confidence. Do not filter for importance. Mark genuine uncertainty as `UNVERIFIED, worth a look`.
7. **Safety and compliance.** Its own section because of the stakes. Physical safety incidents, public health notices, injuries, code and permit exposure. For each: what it is, current owner or explicitly **NO OWNER**, days open, last evidence of movement.
8. **Money in motion.** Every figure with a decision or deadline attached: Amount, What, Owner, Status, Confidence. Every number reconciles to `00-Meta/numbers-ledger.md` or is marked as not in the ledger. Hard rule 3.
9. **Closed in the last two weeks.** Completed work made visible, with dates and who did it. Pull from `99-Archive/`, the ledger's recently closed section, and the sweep. Be generous and concrete, because this is the section that counters the sense of standing still.
10. **The week ahead.** Calendar through the next seven days with the commitments and deadlines that land in it. Flag any meeting whose attendee list collides with an open personnel or governance matter.
11. **Blind spots.** What this report cannot see and why: Teams transcripts disabled, meetings with no recording, recordings that returned nothing, incomplete pagination, the thinner older email window, anything unverified.

Design: load the `artifact-design` skill first. Title `Weekend Pulse`, favicon a parrot. Same design system as the morning brief so it reads as one product, with three deliberate departures because this is a long document rather than a phone glance:

1. Column widens to `max-width: 860px`. Body text stays 18px.
2. A **sticky table of contents** at the top linking all eleven sections, with `scroll-margin-top` on the anchors. He will jump around.
3. Tables get real styling: `font-variant-numeric: tabular-nums`, zebra rows, sticky headers on long tables. **Every table sits in its own `overflow-x: auto` container** so the body never scrolls sideways.

Then update the vault:

- Genuinely new open items into `00-Meta/commitments.md`, continuing the existing numbering, absolute dates, sources cited.
- Corrections filed where they belong: tooling and infrastructure findings to `00-Meta/open-items.md`, ledger items to `00-Meta/commitments.md`, newly identified people or counterparties to `10-Business/people/`.
- Note on the "Last reviewed" line of `00-Meta/commitments.md` that the pulse ran, with the artifact URL.
- One line in `00-Meta/log.md`, the change and its reason in `00-Meta/audit-log.md`.
- Nothing moves to `99-Archive/` without primary source evidence it closed.

## Rules for this job

Beyond the hard rules in CLAUDE.md, which always apply:

- **Send nothing.** Artifact only. Decided 2026-08-29. Do not call `outlook_send_mail`, do not create a draft, do not message on Teams. Never report the absence of an email as a failure, and never reopen the `Mail.Send` or Chrome permission thread.
- **Hard rule 9 constrains section 8 and section 5.** Never record any individual's personal compensation anywhere in this Brain. Severance figures, bonus percentages, per person equity and MIP unit values are compensation. Point at where they live, reproduce nothing. This applies to the artifact as well as the vault pages.
- **Hard rule 7 constrains section 5 and section 7.** Personnel matters are drafts to Austin only, never distributed. Candid assessments of a named employee live only in `10-Business/people/_private-assessments.md`. A performance signal in the roster section is a personnel matter.
- **Hard rule 6.** Anything touching the Bedrock Fund II LP base gets drafted and not sent.
- **A task instruction is not a source.** If this brief, a prior brief, or the ledger says something is true and the primary data disagrees, the data wins. Report the disagreement.
- **Absolute dates always.** Never "last week". Convert every UTC timestamp to ET.
- **Confidence label and source on every substantive claim**, per hard rule 10.
- **Never say Austin is behind.** Say what is un-indexed, un-decided, un-delegated or un-owned.
- **Contradictions stay visible.** Two sources disagreeing get both shown with dates and a flag, never smoothed over.
- Long is fine here. Padding is not. Length comes from coverage, never from restating.


## The second mailbox, added 2026-09-03

**Priority weighting, 2026-09-03.** Austin: *"nothing in personal and need more hands and eyes on the a2zcp and bedrock account."* **This mailbox is not the one that gets read if there is time left.** Per [[CLAUDE]] rule 14, it gets first class attention here, and **where this run has to be cut short, Outlook is what gets cut**, because Outlook has weeks of prior coverage under it and this one has days. Read `in:inbox` to exhaustion before extending Outlook past Inbox, Sent Items and For Signature. **The personal Google account is not a content source and nothing is harvested from it.**

**Sweep both.** The Parakeet mailbox through Microsoft 365, and the legacy holding company mailbox through the Gmail tools, scoped by [[10-Business/a2z-mailbox-map]]. The second one carries the Fund II LP base at `ir@thebedrockgrp.com`, the Bedrock and A2Z tax stream, and the legacy assets' operating mail. **State both mailboxes and their surfaces**, per [[CLAUDE]] rule 14 as extended 2026-09-03.

**Weekend relevance is higher here than it looks.** LPs and joint venture partners write at weekends and there is nobody else on that inbox: the first sweep found five LPs and a partner with a 9/15 filing deadline all chasing the same document, none of it in any register. `CM-25`, `CM-27`, `CM-28`.
