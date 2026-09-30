	# Skill: refresh the community pulse

**What this is:** how the Pulse block, the lot pages, the asset pages and [[60-Communities/open-items]] get rebuilt from what came in since the last run. The hot sheet's Snapshot comes from workbooks and the Live block comes from Rent Manager; this is the third feed, the one made of what people actually said.

## When to run it

Weekly, Monday morning, before the Jon and Austin catch-up at 8:30. Also before any EOS session, because the open-items register is where to-dos should come from.

## The four sources, in order of signal

1. **Outlook, For Signature folder first.** Read `mail:///folders/{id}` for **For Signature** (ID in [[10-Business/outlook-folder-map]]) before any keyword search. Every item is a `CODE_TYPE_NUMBER` Adobe Sign kickoff or closeout, which means it already carries the community, the project, the vendor, the budget and the GL code with no inference. This is the only structured property-activity feed in the mailbox: harvest it first, then let the keyword search below fill the gaps around it.

   **Every one of these also gets a row in [[60-Communities/projects]].** Parse `CODE_TYPE_NUMBER`, resolve the code to a community, and add or update the row on that project number: a kickoff opens it, a closeout closes it, and the `Completed:` notice is what dates either end. The number is the join key between the two, so never drop it.

2. **Outlook, keyword search.** Search the last 7 days across: lot prep, punch list, make ready, home delivery, set, trim out, skirting, infill, demo, title, boil water, well, septic, sewer, lift station, roof, sinkhole, code violation, inspection, permit, eviction, landlord, vacant, listing, closing, walkthrough, work order, complete, resolved, approved, escalate. Also by sender for natalie@, jon@, zach@, leslie@, john@ and any @highpaceconstruction.com address. **Exclude donotreply@rentmanager.com and no-reply@sharepointonline.com** - those are data feeds, not activity, and they will drown the harvest.
3. **Teams.** Same terms plus the community names directly. Note that date-filtered searches only scan the 50 most recent messages per chat; run the searches unfiltered and filter by date afterwards, which gives much deeper recall. Graph rate-limits hard at around two searches per minute, so pace them.
4. **Filed transcripts** in `70-Operations/meetings/`. Look for items raised and never closed: a problem with no owner, a decision deferred, a promise made, a question never answered.
5. **Rent Manager**, when it is working. See [[90-Skills/community-hot-sheet-refresh]].

## The extraction format

One line per item, and never more than one line per item:

`COMMUNITY | LOT | DATE | TYPE | STATUS | what happened in one sentence | owner | source`

TYPE and STATUS come from the vocabulary in [[60-Communities/_model]]. Drop anything that names no community. Never invent a community name; resolve it against the page filenames in `60-Communities/`.

Write the raw harvest to `60-Communities/activity/_sources/<date>-<source>-raw.md` and keep it. The generated pages are disposable; the harvest is the record.

## Rules

1. **Nothing is deleted.** An item that closes changes state; it does not disappear from the lot page timeline.
2. **A lot page is created only when a lot has activity.** Never pre-create lots.
3. **An asset page is created only for a home with a real identifier that is in dispute or in motion.** Never for every home.
4. **`decided-not-actioned` is a real state.** Use it. It is the whole reason this exists.
5. **Route what you find.** Per CLAUDE.md: draft the email to the person who owns it, add it to the community page, and put a named task in `10-Business/eos/to-dos.md`. Never report and stop.
6. Append a dated line to `00-Meta/log.md` with the item count and the date window covered.

## What to escalate without being asked

- Anything `blocked` with a statutory or county deadline attached.
- Anything open more than 60 days with no owner.
- Any `decided-not-actioned` item where the decision was Austin's or Jon's.
- Any lot where the same issue appears from two different sources with two different answers. That is a data conflict, and those have been expensive.


## The second mailbox, added 2026-09-03

**Legacy asset mail does not arrive in the Parakeet mailbox.** Lamberton Lake's utilities, its Capital One loan servicing, its insurance renewals and its Fannie certifications all land in the a2zcp mailbox, read through the Google connector. So do Cambridge MHC's vendor receipts and the Bismarck and Onyx joint venture traffic. **A pulse that harvests only Outlook will report a clean sheet on those properties while four dated items sit unread**, which is exactly what happened until the first sweep on 2026-09-03 opened `PF-0459` to `PF-0462`.

**Priority weighting, 2026-09-03.** Austin: *"nothing in personal and need more hands and eyes on the a2zcp and bedrock account."* **This mailbox is not the one that gets read if there is time left.** Per [[CLAUDE]] rule 14, it gets first class attention here, and **where this run has to be cut short, Outlook is what gets cut**, because Outlook has weeks of prior coverage under it and this one has days. Read `in:inbox` to exhaustion before extending Outlook past Inbox, Sent Items and For Signature. **The personal Google account is not a content source and nothing is harvested from it.**

**Scope and label IDs: [[10-Business/a2z-mailbox-map]]. State both mailboxes in the output**, per [[CLAUDE]] rule 14 as extended 2026-09-03.
