# The a2zcp mailbox map, what a sweep reads in the second mailbox

**What this is:** the scope definition for Austin's **second** mailbox, the legacy holding company stream, read through the **Google connector**. It is the companion to [[10-Business/outlook-folder-map]], which does the same job for `austin@parakeetcommunities.com`. Between them they define every mailbox this Brain reads.

**Status:** current, 2026-09-15. One connector trap added by the Page Update, the Sent folder blind spot. Otherwise 2026-09-03. Mailbox connected and read live this session. **Amended 2026-09-03 evening, twice, and both amendments are corrections to this page rather than new facts about the mailbox.** A **fourth** Bedrock address, `info@thebedrockgrp.com`, was found receiving live LP mail and has been added to the table below; `KP-0077` holds the fact that its history has still never been read. And the Google **Drive** correction at the foot of this page is **superseded**: Drive was moved to `austin@a2zcp.com` later the same day and all four Shared Drive roots returned, per [[00-Meta/log]]. The paragraph is left standing because it was true when written and the reasoning in it is still the record. **VERIFIED**, every count below came back from the connector rather than from a page.

## The change that made this page necessary

Austin, 2026-09-02: *"I will change my google connection to a2zcp.com which has bedrock emails forwarded to."* Austin, 2026-09-03: *"you now have access to a2zcp.com email which also receives bedrock group and fund ii email. run a full sweep on the mail box and add it to all routines, skills and scripts."*

**He made the change. The Google connector no longer points at a Drive-only personal account; it is this mailbox.** That closes `TD-0477`, which had four unknowns on it and guessed at none of them. All four are now answered:

- **Reachable how:** the Google connector, not Microsoft 365. `outlook_email_search` with `mailboxOwnerEmail: "austin@a2zcp.com"` returns `ErrorInvalidUser` because the address lives in a different tenant from Parakeet's. **Do not retry that call.** Use the Gmail tools.
- **Separate mailbox or forward:** separate. Nothing from this stream appears in the Parakeet inbox.
- **Structure:** Gmail labels, not Outlook folders. Mapped below.
- **What lands here:** five addresses plus two legacy ones, listed next.

## Addresses that deliver into this one mailbox

| Address | What arrives on it | Confidence |
| --- | --- | --- |
| `austin@a2zcp.com` | the holding company address, general business, banking alerts, vendors, personal | VERIFIED |
| `austin@thebedrockgrp.com` | Bedrock fund correspondence addressed to him personally, LP replies | VERIFIED |
| `ir@thebedrockgrp.com` | **the Fund II investor relations line.** LP questions, K-1 chases, capital account disputes | VERIFIED |
| `bills@a2zcp.com` | utility and vendor billing, forwards on to the per property gmail addresses below | VERIFIED |
| `accounting@a2zcp.com` | seen forwarding utility verification traffic, June 2026 | SINGLE-SOURCE |
| `info@thebedrockgrp.com` | **added 2026-09-03.** LP mail addressed to the fund generally, found carrying Steven Posborne's 2026-09-01 K-1 escalation | VERIFIED |
| `lambertonlakebills@gmail.com` | Lamberton Lake utilities, Consumers Energy and City of Grand Rapids | VERIFIED |
| `cambridgemhcbills@gmail.com` | Cambridge MHC vendor receipts, nothing since August 2024 | VERIFIED |

**`winnie@a2zcp.com` and `winnie@thebedrockgrp.com` are still live recipients on system notices**, most recently a Gusto payroll notice dated 2026-07-28. That is the same departed employee identity problem [[10-Business/outlook-folder-map]] and the A2Z credential work already carry. `KP-0063`.

## This mailbox is the opposite of the Outlook one, and that inverts the reading rule

[[10-Business/outlook-folder-map]] exists because Austin files his Parakeet inbox to zero, so a sweep that reads only the Inbox reads the folder he has already cleared. **Here the discipline is reversed.** The Inbox holds **4,803 messages across 3,051 threads with 11 unread**, and the archive label holds 12,244. He does not clear this one.

**So in this mailbox the Inbox is the primary surface, not the emptiest one.** A sweep reads `in:inbox` first and the labels second. That is not a contradiction of the Outlook rule, it is the same rule applied to a different habit: **read where the mail actually sits, and say which surface you read.**

**Read state is noise here too.** 2,124 unread across the mailbox against 11 unread in the Inbox means unread tracks age and bulk mail, not pending work. The Outlook rule carries over unchanged: read every message in scope, never only the unread ones, and never infer disposition from read state.

## Label map

**Read on every sweep.** These are where a human is waiting on Austin.

| Label | ID | Holds | Why it is in scope |
| --- | --- | --- | --- |
| `INBOX` | `INBOX` | 4,803 messages, 3,051 threads | the working surface in this mailbox |
| To Respond | `Label_46` | 236 messages, 74 threads | his own triage of what needs an answer |
| [Superhuman]/AI/Respond | `Label_44` | 133 messages | machine triage, overlaps the above, catches what he did not label |
| [Superhuman]/AI/Waiting | `Label_38` | 88 messages | things he is waiting on somebody else for |
| Awaiting Reply | `Label_48` | empty today, kept in scope | same grain, his own hand |
| TO DO | `Label_6828196491080464622` | 41 messages | his own |
| Email Response Needed | `Label_2944530270452383990` | 1 message | his own |
| Accounting | `Label_13838010255879549` | 850 messages, 73 unread | Citrin, invoices, the K-1 pipeline |
| Legal | `Label_3972695125781275896` | 5 messages | thin, but every row on it matters |
| Deals | `Label_8719823625459333532` | 59 messages | acquisitions and dispositions on the legacy side |
| Capital Intro | `Label_10` | 6 messages | capital raising history |
| DocSend | `Label_1032504313536762726` | 314 messages | who opened which fund document and when |
| Property Reporting | `Label_4687921847476065467` | 38 messages, 37 unread | plus its three children, AR Report, General Ledgers, Trending AR |
| Bedrock Email | `Label_1314686734266673844` | **empty** | a label he made for this stream and never used. Do not read it as coverage |

**Read on the finance and asset sweeps only.**

| Label | ID | Holds |
| --- | --- | --- |
| Capital One CC Notifications | `Label_5274678360787696446` | 179 messages |
| To Upload in RM | `Label_6966275158318989293` | 8 messages |
| Report Files | `Label_6047238291230123645` | 4 messages |
| ClickUp | `Label_8463714022064060497` | 44 messages |
| TreVista | `Label_2596851721940127154` | 1,183 messages, a whole prior relationship |

**Do not harvest.** Sample if a specific question needs them, never whole: `[Imap]/Archive` (`Label_22`, 12,244), AppSheet (`Label_5945738047030316823`, 6,888), Paylease (`Label_7031957186281026520`, 3,712), Grasshopper (`Label_7966625726742743102`, 1,148), Google Text Message (`Label_1698061196569841096`, 554), Marketing (`Label_53`), Notification (`Label_52`), Cold Email (`Label_51`), the `[Superhuman]/AI/News`, `Pitch`, `Social` and `Marketing` labels, `SPAM` and `TRASH`.

**The same archive exception applies as in Outlook.** `[Imap]/Archive` is never harvested wholesale and must still be **searched** before anything is called open, per [[CLAUDE]] rule 11.

## Connector quirks, learned the hard way rather than assumed

- **`search_threads` returns a preview of roughly the five OLDEST messages in a thread, and shows no truncation marker.** A thread whose newest message closes the item will look open in the preview. **Never call something open from a search preview. Call `get_thread` first.** This is the single most expensive trap in this mailbox and it is the exact shape of rule 11.

  **Second recorded instance, 2026-09-04, and it is worse than the first because the bait was better.** A `in:inbox newer_than:2d` search returned the Grant, Tani, Barash & Altman thread on the Q2 2026 distribution to Gink Bastian Enterprises. The subject line reads **"IMMEDIATE RESPONSE NEEDED"**, the preview's newest visible message was Corey Barash on **2026-07-31** saying *"Please advise no payment YET"*, and the thread had appeared in a two-day window, which is itself the tell: **Gmail matches the thread on a recent message and then shows you the oldest ones.** `get_thread` returned four later messages. Austin answered James Perkins at 2026-09-03 13:24 ET and Perkins replied *"Perfect. Thank you."* **Unchecked, that would have reached the morning brief as a five-week-old unanswered law-firm escalation, highlighted, on a Friday.** The useful residue is `KP-0086`: this is a **seventh** party on the Fund II K-1 clock where the register counted six.

  **The operational rule that follows: if a thread surfaces in a `newer_than:` window but its newest previewed message is older than that window, the preview is definitionally truncated.** That is a free truncation detector and it costs one call to act on.
- ~~Labels are addressed by **ID**, not display name, in a `label:` query. The IDs are in the tables above.~~ **WRONG, and corrected 2026-09-04. This is the reverse of the truth and it silently blanked the label half of every sweep that has ever run against this mailbox.**

  **`label:<ID>` returns nothing at all. `label:"<Display Name>"` returns the label.** Tested both ways in the same minute on 2026-09-04: `label:Label_46` returned `{}`, and `label:"To Respond"` returned 74 threads. **`{}` is a legitimate empty result, not an error**, so a sweep using the documented form reports a clean label and moves on. That is the worst possible failure shape for a scope page: it looks like coverage.

  **What it cost.** `To Respond` holds **236 messages across 74 threads, zero unread**, and is Austin's own hand-marked needs-a-reply pile. **No sweep had ever read it.** The first read, on 2026-09-04, found an unanswered CrowdStreet ownership-transfer request six months old on an LP who is currently chasing his K-1, a five-times-asked LP capital account discrepancy escalated by Bedrock's own co-founder, an LP threatening to involve attorneys, a bond premium six months unpaid, and documented entity-attribution evidence bearing on the Citrin $217,787.93 reconciliation. `KP-0088`, `KP-0089`, `KP-0090`.

  **Use the display name for every label in the tables above**, quoted where it contains a space. **The IDs are still correct and still worth keeping** - they are what `label_thread` and `unlabel_thread` take, and they are how a renamed label stays findable. They are simply not what `search_threads` matches on.

- **Four labels carry live mail and are not in the tables above.** Found by `list_labels` on 2026-09-04 rather than by reading this page. `FYI` (`Label_47`, 278 messages, 78 threads), `Actioned` (`Label_50`, 50 messages), `Chrissy (Review/Respond)` (`Label_4992546068371164319`, 37 messages, 4 threads), `Northwest RA` (`Label_31`, 71 messages, **the registered agent stream, and nothing in it is newer than 120 days**), plus `info@` (`Label_2310423233296313409`, 285 messages) and `NorthMarq Multi Sales` (8 messages, **all 8 unread**). **`Chrissy (Review/Respond)` and `FYI` are the two that belong in the every-sweep set** on grain, because both are his own triage rather than machine sorting.

- **Counts on this page drift and should be re-read rather than cited.** As of 2026-09-04 the Inbox holds **4,813 messages / 3,069 threads / 23 unread** against the 4,803 / 3,051 / 11 recorded above, and `[Imap]/Archive` holds **12,262** against 12,244. The shape of the mailbox is stable; the numbers are not.
- `newer_than:`, `older_than:`, `after:YYYY/MM/DD`, `in:inbox`, `is:unread`, `has:attachment` all work. Drafts are excluded by default.
- The Microsoft 365 connector cannot see this mailbox at all. Cross tenant delegate access is not granted and asking for it returns `ErrorInvalidUser`.

**Sends from the Bedrock addresses never reach the Gmail Sent folder.** Learned 2026-09-11 to 09-15, four closes running: Austin's replies from `austin@thebedrockgrp.com` do not land in `in:sent` here at all, so **a served LP and an ignored one look identical from this mailbox**. Buckwalter, Brown and Scruggs only became visible as answered because each wrote back. **Consequence for a sweep:** never infer that an LP is unanswered from the absence of a Sent item; ask, or look for the reply in the thread. Recorded on `KP-0110` and on the 2026-09-14 close, question 1.

## What is NOT in this mailbox, stated so nobody assumes coverage

- **Belmart, and this is a correction rather than a gap.** A direct search for "Belmart" and "9100 Belmart" returns **zero threads here**, which is true and was briefly read as meaning the house had no mail anywhere. **It is all in the Parakeet Outlook mailbox**, along with Bullis School and lacrosse. Austin, 2026-09-03: *"jamie emails me at work."* **The personal routing rule lives on [[10-Business/outlook-folder-map]] where the mail actually is**, and the section it feeds is `85-Personal/`. `KP-0066`, closed.
- **`austinrberk@gmail.com`.** The Google connector used to serve that account and now serves this mailbox instead, so it is no longer readable. Austin says nothing top of mind is in it. `KP-0069`.
- **Parakeet operating traffic.** The 67 communities, the field, capex kickoffs and the For Signature queue are all in the Outlook mailbox. This mailbox is the pre Parakeet layer plus what still bills to it.

## How much attention this mailbox gets, ruled 2026-09-03

**Austin:** *"nothing in personal and need more hands and eyes on the a2zcp and bedrock account."*

**This is not the backup mailbox.** It gets first class attention on every routine that reads mail, on the same footing as Outlook and ahead of it when a run has to be cut short. The reasoning is on [[CLAUDE]] rule 14 and it is short: this mailbox holds the highest concentration of unrouted work in the Brain and the thinnest history of coverage behind it. **The first read of it, on 2026-09-03, opened four commitments, four promises, three parked decisions, six findings, sixteen to-dos and four property items in a single pass.** That rate is what an unswept surface looks like, and it will not settle until several full passes have run.

**Practical version for a run that is short on time:** read `in:inbox` here to exhaustion before reading anything in Outlook beyond Inbox, Sent Items and For Signature.

**One correction that belongs on this page.** The change Austin made was to the **Gmail** connection. **The Google Drive connector still authenticates as `austinrberk@gmail.com`**, tested 2026-09-03. Nothing about `KP-0008` moved. Detail on [[10-Business/connector-status]].

## The rule this page carries

**Every sweep states its mailbox, its surfaces and its dates.** One line, the same way folder scope is stated. Both mailboxes get read on the morning brief and the end of day close, and a sweep that read only one says which one and why. "Second mailbox not reachable" is a complete answer and a useful one. Saying nothing is what produced the gap this page closes.

## Related

- [[10-Business/outlook-folder-map]], the same definition for the Parakeet mailbox.
- [[10-Business/entity-structure/berk-inc-umbrella]], which already recorded `austin@a2zcp.com` as a tenant owner before this mailbox was ever readable.

## Sources

- Google connector, mailbox read live 2026-09-03. Label list, counts and IDs from `list_labels`.
- Austin, in session 2026-09-02 and 2026-09-03, quoted above.
- [[00-Meta/daily-close/2026-09-14]] — question 1, the Sent folder blind spot. Added 2026-09-15.
