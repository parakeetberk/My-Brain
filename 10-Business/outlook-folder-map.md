# Outlook folder map — what a mail sweep actually reads

**What this is:** Austin's mailbox is 36 folders, and the Inbox is the emptiest one in it. This page defines the mail scope every sweep uses, folder by folder, with the folder IDs, because the connector cannot look most of them up by name.

**Status:** current - 2026-08-31. Folder list read live from the Microsoft 365 connector on 2026-08-31. **VERIFIED.** Extended 2026-09-26: `KP-0127` note added to the For Signature section by the Page Update.

## Why this page exists

Austin, 2026-08-31: *"when processing my inbox in outlook, make sure to look into folders not just the inbox as the For Signature folder holds the kick offs and close outs that are requesting signature which is a great notification to know what projects are going on at what property along with all the necessary information."*

He is right, and the mailbox proves it harder than the instruction does. **The Inbox holds 330 messages and zero unread.** He files to zero. Every sweep this Brain has ever run read the Inbox and Sent Items, which means every sweep read the folder he had already cleared and the folder of things he had already sent. The signal is in the folders he moved things into.

## The rule

**A mail sweep reads a defined set of folders, not the Inbox.** Which set depends on the sweep, and the table below says which. Folder scope is part of the sweep definition, the same way the register grain is part of the routing definition. A sweep that does not say which folders it read is not a sweep.

**The connector cannot find most of these folders by name.** `outlook_email_search` with `folderName: "For Signature"` returns NOT_FOUND; the ID works. Read a folder with `read_resource` on `mail:///folders/{id}`. The IDs below are current as of 2026-08-31 and survive as long as the folder is not recreated. If one 404s, re-list with `read_resource` on `mail:///folders/` and update this page in the same session.

## Read on every sweep

| Folder | Holds | Why it is in scope | ID |
| --- | --- | --- | --- |
| **For Signature** | Adobe Sign capex kickoff, closeout and infill approval requests routed by Vladimir Baga | Austin's own words: it tells you what project is running at what property with the detail attached. Unread means pending his approval. | ID below |
| Inbox | whatever has not been filed yet | Still read it. It is just never the whole picture. | resolves by name |
| Sent Items | his own commitments | The strongest source for what he personally promised. | resolves by name |

## Read on the community pulse and the asset work

| Folder | Holds | Why |
| --- | --- | --- |
| **For Signature** | as above | Every kickoff and closeout is property-level project activity. This is a structured feed of exactly what `90-Skills/community-pulse-refresh.md` harvests out of unstructured email. |
| **EOW: Vlad** | 27 items, Vlad's end-of-week reports | Weekly construction status in one place. |
| **CountryPlace**, **Triad**, **Reliable Premium** | floorplan lender correspondence, filed by lender | Directly feeds [[60-Communities/asset-inventory]]. The tie-out is reconstructing from email what these three folders already separate by lender. |
| **RM Notifications** | 949 items, Rent Manager alerts | Data feed, not conversation. Sample it, never harvest it whole. |
| **JotForm** | 1,190 items, form submissions | Same. High volume, low signal per item. |

## Do not harvest

`Archive` (73,117 items), `Deleted Items`, `Junk Email`, `Conversation History`, `Sync Issues` and its three children, and the empty folders. **Archive is the exception that matters:** it is not harvested, but rule 11 requires it to be *searched* before anything is called open. Searching a folder for a specific thing and harvesting it wholesale are different operations.

`Belmart` is out of scope for this Brain entirely while the Belmart question in `05-Inbox/_needs-sorting.md` is unanswered.

## What the For Signature folder is, and is not

**Read state means nothing here. CORRECTED 2026-08-31, hours after this page was written.** The first version of this page said unread means pending, read means dealt with, and that the folder maintains itself. That was wrong, and Austin said so: *"I read emails and forget some times, i can't stand looking at unread emails."* He clears the unread badge as a habit, so read state tracks his tolerance for a bold number, not whether anything happened. Both directions fail: a read item can be untouched, and an unread item can be long since done.

**The proof, same day.** This page's first version reported six unread items in For Signature as six pending approvals. All eight items in the folder had been signed by 11:44 ET, roughly forty minutes after they arrived, and their `Completed:` notices were themselves sitting **unread**. A naive unread rule would have counted those eight completions as eight new pending items on the next pass. The wrong reading is kept here because it is the clearest available illustration of why the rule changed.

**Disposition comes from Adobe Sign, never from Outlook.** For any `CODE_TYPE_NUMBER` document:

- A matching **`Completed: "<doc>"`** email means done. It arrives minutes to an hour after the last signature, so its absence on a document from the last hour proves nothing.
- A matching **`Agreement Exchange Canceled`** notice means void and superseded; a corrected resend arrives later as a new request.
- A **`Reminder: Waiting for you to approve <doc>`** means genuinely still open. Adobe sends these daily until completion, so a reminder is a far better pending signal than an unread flag will ever be.
- Neither a Completed nor a Canceled, and the request is more than a day old, means **check the thread before calling it open**, per rule 11. Some are held on purpose.

**It is still its own register and this Brain still does not copy it.** Mirroring rows into `00-Meta/commitments.md` would create a second copy that drifts. Sweeps report the count and the properties and leave the queue where it is. What changed is how the count is computed, not where the queue lives.

**Standing check: three closeouts have been carrying daily reminders since 2026-08-01** with no Completed notice found: `GULFPO_CAPEX_CLOSEOUT_15026`, `RP_CAPEX_CLOSEOUT_15040`, `SOUTH_CAPEX_CLOSEOUT_11127`. All three are marked read. **Two are held for cause, not forgotten** — Jon asked to hold Southgate, and Gulf Breeze has a thread about the sign being mounted too high and crooked, both from 2026-08-03. **`RP_CAPEX_CLOSEOUT_15040` has no such thread and is the one worth asking about.** SINGLE-SOURCE: the reminder emails. Verify against Adobe Sign before treating any of the three as open.

**What does get copied is the content.** A kickoff names a community, a project, a vendor, a budget, a quote and a GL code. That is durable property activity. It belongs on the community page, and **every document also gets a row in [[60-Communities/projects]]** keyed on its document number, which the kickoff and closeout share. That ledger is the record of what started and what finished; this folder is only where the paperwork passes through.

**Naming convention:** `CODE_TYPE_NUMBER`, where CODE is the community short code, TYPE is CAPEX_KICKOFF, CAPEX_CLOSEOUT, INFILL_KICKOFF, INFILL_CLOSEOUT or CHANGEORDER, and NUMBER is the Adobe Sign document number. The code maps to a community page: SUR is Su Rene, SS is Sea Shells, PPH is Palm Haven Estates, WPMH is Whispering Pines MH, LS is Lake Saunders, ROYAL is Royal Oaks, APPLE is Applegate, LUCK is Lucky Clover.

**Austin is an upstream approver, not the final one.** The routing runs Berman, Schwartz, Magurne and Austin, then Jon signs last. A doc sitting unread in Austin's For Signature folder is holding up Jon's queue behind it.
**`For Signature` has stopped working as a register, per `KP-0127` opened 2026-09-24.** Added 2026-09-26 by the Page Update. The count went 34, 29 (2026-09-22), 1 (2026-09-23), 6 (2026-09-24), 17 (2026-09-25), and documents leave with no Adobe completion or cancellation: the Lucky Clover change order left on 2026-09-24 and even its reminder vanished. **Adobe Sign reported three other documents correctly on 2026-09-25**, so the folder's count is no longer evidence of anything. Disposition comes from Adobe Sign, never from Outlook, as this page already says.

## Folder IDs for the ones the connector cannot resolve by name

Read with `read_resource` on `mail:///folders/{id}`. Prefix for all of them: `AAMkADM5NmY0ZmQ1LWI2ZDUtNGFjYy1hN2M3LTcxNGZmNjkxNDgwNwAuAAAAAAAdz1OD1IrqRaFRepAlyYk2AQCVkYasAQi2QqY2To5b8Obu` followed by the suffix below.

| Folder | Suffix |
| --- | --- |
| For Signature | `AAbJ9FySAAA=` |
| EOW: Vlad | `AAff7jhUAAA=` |
| CountryPlace | `AAfnNs3mAAA=` |
| Triad | `AAgSMSnJAAA=` |
| Reliable Premium | `AAfxc9HIAAA=` |
| RM Notifications | `AAPcLADzAAA=` |
| JotForm | `AAa5x3jcAAA=` |

Inbox, Sent Items, Drafts, Deleted Items, Archive and Junk Email resolve by name in `outlook_email_search`. Everything else does not: `folderName: "For Signature"` returns NOT_FOUND, which is how this gap stayed invisible.

## Related

- [[90-Skills/community-pulse-refresh]] - the harvest procedure this scope feeds.

## Sources

- Microsoft 365 connector, mailbox folder list read live 2026-08-31.
- Austin, in session 2026-08-31, quoted above.

## A second mailbox was coming into scope. It arrived 2026-09-03

**RESOLVED 2026-09-03.** Austin connected it and said so: *"you now have access to a2zcp.com email which also receives bedrock group and fund ii email."* **The mailbox is live, it is reached through the Google connector rather than Microsoft 365, and it has its own scope page: [[10-Business/a2z-mailbox-map]].** `TD-0477` closes on this.

**Three things a sweep needs to carry over from that page.** The Microsoft 365 connector **cannot** reach it, and asking returns `ErrorInvalidUser`, so do not spend a call on it. Its Inbox is the **primary** surface rather than the emptiest one, which inverts the rule below, because Austin does not file this mailbox to zero. And a Gmail search preview shows only the **oldest** messages in a thread, so a closed item reads as open until `get_thread` is called.

**The section below is kept as written on 2026-09-02**, with its four unknowns, because it is the record of what was not known and what was deliberately not guessed. Nothing in it was true and is now false; it was a question and the question has an answer.

### What the 2026-09-02 version said



**Austin, 2026-09-02:** *"I will change my google connection to a2zcp.com which has bedrock emails forwarded to."*

**Why this page has to say so.** Everything above defines mail scope inside **one** mailbox, `austin@parakeetcommunities.com`, read through the Microsoft 365 connector. **Bedrock correspondence is forwarded to `a2zcp.com`, which no sweep in this Brain has ever read.** The end of day close, the morning brief and the community pulse all resolve folders against the Parakeet mailbox and would report a clean sweep while a whole counterparty stream sat somewhere else. **A sweep that does not say which folders it read is not a sweep**, and by the same rule a sweep that does not say which *mailbox* it read is not one either.

**The evidence that this matters is the same day it was written.** `CM-26` exists because a 33% partner in Bedrock Group left two voicemails chasing statements. **Those landed in the Parakeet mailbox only because they were phone calls.** Anything he sent in writing would have gone to the Bedrock address and no sweep would have seen it. **This is not hypothetical missed mail; it is the one channel that happened to leak into the swept mailbox.**

**What is not yet established, and none of it is guessed.** Whether the change has been made, whether `a2zcp.com` is reached through the same Microsoft 365 connector or a Google one, whether it is a separate mailbox or a forward that lands back in the Parakeet inbox, and what folder structure it has. **`austin@a2zcp.com` is already recorded in this Brain as a tenant owner** on [[10-Business/entity-structure/berk-inc-umbrella]], so the address is not new even though the mail scope is. `TD-0477`.

**Until it is settled, every sweep states its mailbox.** One line, the same way folder scope is stated: which mailbox, which folders, and whether the Bedrock stream was reachable. **Saying "not reachable" is a complete answer and a useful one.** Saying nothing is what produced this gap.

## Personal versus business, defined 2026-09-02

**Austin:** *"Personal items to connect with personal is belmart and jamie berk (wife)."*

**Two markers, and they are the test.** Anything touching **Belmart** (9100 Belmart Road) or **Jamie Berk** is personal and routes to the personal side, which under the 2026-08-26 storage target state means **Dropbox, never the Parakeet estate**. That is now a stated rule rather than an inference drawn from Belmart being a non-manufactured-housing asset.

**What this does not settle**, and it is left open on purpose per the standing rule at [[05-Inbox/_needs-sorting]]: **whether Austin's personal portfolio gets tracked in this Brain at all.** He named what personal *contains*; he did not say whether this vault follows it. `CM-10` stays live either way, because a lender package he owes is a commitment regardless of where its documents live. **Nothing is guessed into a resolution to clear a page.**

## The personal life is in this mailbox, established 2026-09-03

**Austin, asked where his personal mail actually lives:** *"All over. I really don't get personal mail. Some in the austinrberk email but not the things i need at the top of my mind. jamie emails me at work."*

**So the personal versus business rule written on 2026-09-02 has a second half now.** That rule said what counts as personal, Belmart and Jamie Berk, and where its documents go, Dropbox. **It did not say where the mail arrives, and the answer is here, mixed into the Parakeet flow.** A live construction project at the house, Bullis School billing, and lacrosse all land in this mailbox.

**How a sweep separates it, by sender, because Jamie never writes to Austin about Parakeet:**

| Bucket | Senders |
| --- | --- |
| **Family** | `jamie.jle@gmail.com`, anything `@bullis.org`, Veracross school billing, LeagueApps |
| **The house, its own bucket** | `randrcustomhomes.com`, `serajassociates.com`, `riversedgebuilders.com`, `outofsight.net`, `machricofloors.com`, `weaverhardware.com`, plus one off vendor addresses on those threads |
| Keyword backstop, weaker | Belmart, Bullis, tuition, lacrosse, Hailey, cast stone |

**The house gets its own bucket rather than being filed as "personal" because Austin runs it like a project**: budget tracker, change orders, draws, lead times. Treating it as soft personal noise is how a 12 to 14 week hardware lead sits unordered for seven weeks.

**Where it goes: `85-Personal/`, and nowhere else.** Personal items carry **no reference ID and never appear on the open board or in a published artifact**, because the board publishes to a URL. The daily close is a local file and may carry a short personal block. **Volume is a handful of messages a week**, so a sweep that is not looking for it will not trip over it.

