# Tools and systems

**What this is:** every system that runs the business, what each one actually runs, and who uses it. One line per tool, with the detail on each vendor page.

**For what data each connected system actually exposes, and which dashboard eats it, see [[10-Business/data-lineage]].** This page is the tool inventory; that one is the report and feed register.

**Status:** current, 2026-09-15. The *What moved in September* section was added by the Page Update from the daily closes of 2026-09-08 to 09-15; every other line is as of 2026-08-30 or 08-31 as marked.

## The facts

### The system of record

- **Rent Manager** — everything. Asset records and user-defined fields, the Make Ready Board, the Prospect module, History & Notes (the universal documentation target every SOP writes to), the AR report, the TBD list, the Evictions tab and workflow including account locking, the Asset Transfer tab, work orders, recurring charges, billing schedules, the GL Total Cost field, the notice template library, and Tenant Web Access for resident auto-pay. **Rent Manager Express** handles lease generation, renewal and e-signature publishing with per-property templates. Owned in practice by Justin Minkoff. There is no documented fallback for any process. See [[10-Business/vendors/rent-manager]].
- Two known system gaps: Accounting receives **no system notification** when a lease is activated, so the billing schedule update is manual; and the August 2026 Rellit conversation concluded Rent Manager keeps the resident ledgers while the general ledger is replaceable.

### Where enquiries and customer records live

- **Rent Manager Prospects** is the record of a prospect. **MAV Consulting** is the CRM — the owner confirmed on 2026-08-30 that the CRM referenced throughout the SOP library but never named is MAV. The same relationship covers the **RentViewer** data warehouse, with a daily sync into the warehouse and everything reachable through Claude via the warehouse. See [[10-Business/vendors/mav-consulting]].
- The practical consequence: prospect data currently lives in two places, and the duplicate/merge rules were only being written in late August 2026.

### Forms — and the unresolved overlap

- **JotForm** — PSA and offer submission with Offer Valid/Invalid buttons, Move-in Request, Home Drop Confirm, Rehab Punchlist, Home Market, the month-end checklist due noon on the 27th, Home Listing, the Phase 1 and Phase 2 readiness gates, the Community Incident Log, the weekly manager recap and utility activation. The deck's position: "no more paper forms. Period."
- **FastField** — Home Delivery Confirmation, the home listing form, the weekly PPE inspection checklist.
- **These two overlap and nobody has picked one.** SOP 105 names the FastField punchlist in one task and the JotForm punchlist four lines later. SOP 001 uses FastField for delivery confirmation while SOP 201 uses JotForm for the same form. The tracker has an unstarted "Jotform Process (Form Ecosystem)" row to consolidate it. This is a live open item.

### Money and approvals

- **Avid Exchange** — AP invoice processing and approval routing, three workflows: CapEx to John Clark, POH over $1,000 to Leslie Croft, Standard Regional for everything else. NET 30 on all vendor invoices.
- **Ramp** — company cards for field and internal rehab spend, GL code required in the memo on every charge.
- **Paychex** — payroll and the benefits portal. Biweekly, every other Friday.
- **SignEasy** — e-signature for closing packages and lease-with-option. Not DocuSign; DocuSign appears nowhere in the process library.

### Screening, title and legal

- **AmRent** — resident screening, accessed only through Rent Manager, up to 72 hours, no preliminary decisions.
- **Florida Fast Title** — every title transfer, post-eviction package and abandoned-home auction. 7 to 10 business days. Single-sourced with no documented alternative.
- **Vector Law** — the auction when a lien exists on the home.
- **Triad** and other consumer lenders — financed home purchases. Lender registration per community is a prerequisite and at least one community had failed registration as of August 2026.

### The corporate stack

- **Microsoft 365** — Outlook, Teams, and **SharePoint** as the document system: Sales agreements and closing docs, Operations evictions and the Main Eviction Cases Sheet, incident reports, legal notices, prospectus documents, training SOPs, and the ParakeetBirdcage corporate library. **A migration from the Parakeet Communities SharePoint to the Parakeet Birdcage SharePoint in a new structure is in progress, run by Albert.** OneDrive syncs property folders and site visit records.
- **Power Automate** — Rent Manager CSV exports into SharePoint and the flows behind the portfolio dashboard. A decision in August 2026 moved it onto dedicated server accounts.
- **Make.com** — automation orchestration, run by Jhosua. Besides Austin he is the only person who can touch it.
- **ClickUp** — task and project execution; the deck names it as an already-in-place tool for reducing email volume. The Flight Plan 2026 execution lives there.
- **Claude** — invoice extraction by the Operations Coordinator in SOP 001, the SOP Builder in the wiki standards, and named in the deck for sales and marketing, SEO and sales contract review. This Brain is the newest piece.
- **Lucid** — every swim-lane flowchart is authored here; the shared Lucid folder is the live source and the PDFs in the wiki are exports. **Microsoft Stream** (Loom acceptable) for 3 to 8 minute task walkthrough videos — of which zero have been recorded against a schedule that completes 2026-09-28.
- **Campspot** — RV site booking. **Toast** — the Geiger Key restaurant POS. **GoPro** — 360 community video at regional site visits.

### Confirmed on 2026-08-31, from a recording read in full

Source: [[70-Operations/meetings/2026-08-31-listings-pipeline-and-ai-cost-consultation]].

- **The Nav CRM stays, and the reason is integration rather than features.** Nav, from Math Consulting. *"One of the reasons we chose it is it talks back and forth to the property management system, so it allows us to keep things up to date."* An MCP is expected and there was a vendor follow-up call the same day. The CRM is mid-cleanup and was explicitly ruled out of scope for the consultant on that basis.
- **The QuickBase build has its own project page as of 2026-09-02: [[15-Projects/quickbase-build/overview]].** 91 SOPs mapped to 46 workflows across 9 dependency waves, with FastField as capture, QB as the workflow engine and Rent Manager staying the system of record. **The daily CSV described below is that architecture's Principle 4**, now written down in a spec rather than only in a recording: the batch runs at 18:00 ET and **QB never writes financial records to RM directly.** Read the project page before quoting any QuickBase scope, count or date from this one.
- **QuickBase with FastField forms: scope and sequence are now on the record.** First project is the **home order**, chosen because it is where the data errors originate and because Sales & Marketing owns buying the home. The mechanism is not a live link: QuickBase collects the form, and **at the end of each day it exports a CSV shaped as a Rent Manager import file**. Austin's framing of the goal is broader than forms: *"No one to send emails anymore. None of this, like Teams messages. If everybody just fills out the form by doing their job, everybody else will get notified cross department."* Planned next: inspections, move-ins and move-outs, and lease generation, with the lease questions driven by the specific community so the wrong figure cannot be typed into a field and signed. **Nothing is relied on yet** — Austin: *"we're not relying on it for anything yet."*
- **Unity is treated as locked in.** AI voice agent and call centre, mobile-home-park specific, integrates with Rent Manager by API, *"the major operators in the space use it, so we're kind of locked into using them."* It is also a future data source, since call reports come back through an API. Note the spelling question against **Uniti** in [[10-Business/systems-architecture]].
- **The AI cost spike has a stated cause and a stated fix.** John traced daily spend against his own usage and found it coincided with *"running everything on Fable at the exact time that Fable took away its free credits and price increases."* He has since built a context-window monitor that tells him when to start a new chat, and an **AI model selector skill** that advises which model to use before a large piece of work begins, and expects usage *"to come in line within the next month."* Recorded because it is the baseline any savings-based fee would be measured against — see `00-Meta/parked-decisions.md` row 20.
- **Put on the table by the consultant, none of it adopted:** **Railway** for hosting, roughly $5 a month to start; **Firecrawl**, open source, for crawling and for parsing PDFs, CSVs and spreadsheets, offered as a cheaper and more reliable substitute for having a model browse; **OpenRouter** or "Token Router" for model-agnostic routing with automatic fallback when a model is down or expensive; and **GLM 5.2**, which he claims is 40 times cheaper per token at Opus 4.8 level, sourced to Twitter and unverified. **Analysis only. CLAUDE.md rule 8.**
- **The consultant advised against Obsidian for company data.** *"Mostly, it's just a beautiful graph, but it adds a lot of extra context… it's going to overload your AI context window and waste more tokens. Not for corporate. Not for company data for sure."* Recorded here rather than omitted, because Obsidian is the tool this Brain runs in and a Brain that filters out criticism of itself is worth less than one that does not. It is one outside opinion, offered before he had seen the vault, and it is not a finding.

### Under evaluation or unresolved

- **QuickBase and FastField** as a BPM platform, with the operating thesis that the process should live inside the tool people use rather than in a document nobody reads. The August 2026 alignment meeting was blunt about the implementation: the launch date had slipped from July into September with nothing live.
- **Corner IQ** — a one-month trial with a small executive group was agreed on 2026-08-18. **It is not moving forward.** Austin ruled on 2026-08-31. Both facts are kept, per the contradictions rule: the trial was agreed and then not taken up, and a later reader needs to see that sequence rather than a page that reads as if it never happened.
- **Adobe Acrobat Sign** routes **every capex and infill approval in the company**. Vladimir Baga originates each document from a fixed template; it routes Controller, then Zach Schwartz, then Director of Construction, then Director of Property Operations, then Austin, then Jon last. Nothing about it was written down in this Brain until 2026-08-31. The document number doubles as the project ID and as the Rent Manager Service Manager issue ID. See [[60-Communities/projects]].
- **Rent Manager's Service Manager module** is where a capex project actually lives: every signed document links to `bedg.rmx.rentmanager.com/#/servicemanagerissues/<number>/details`. This is the join between the approval paperwork and Rent Manager, and it is a service issue rather than a GL account.
- The **600–699 Systems, IT and Reporting SOP band is empty**, which is why most of what is on this page is documented nowhere else in the company.

### What moved in September 2026, added 2026-09-15

Figures in `00-Meta/numbers-ledger.md` under *Organisation*. Each line names the register row where the live state is.

- **ClickUp renewed: 18 seats, $4,104, renewing 2026-11-09**, on the platform the Microsoft build was meant to replace. Closed as renewed on 2026-09-11, `TD-0630`. Nobody recorded a decision to keep it; the renewal simply happened.
- **Rent Manager, two things.** The account is moving from **A2Z Community Partners to Parakeet** as the named owner: John Hemelgarn, the RM account manager, asked on 2026-09-14 whether Austin wants the name moved, which unblocks `TD-0645` and is the last piece of the A2Z Community Partners cleanup on the Parakeet domain. And **several Rent Manager controls were switched off on 2026-09-09** with Moe named as monitor in a chat he is not in; nothing in this Brain says what those controls are, who may change them or who is told. `KP-0108`, `TD-0623`, `TD-0624`. The close asked twice and dropped it.
- **Quickbase provisioned a Parakeet app on 2026-09-10 with admin access shared to the whole team.** Recorded, not judged; the build itself is on `15-Projects/quickbase-build/overview`. A Quickbase discovery session ran 2026-09-15 10:00 ET against a Lucky Clover entitlement meeting in the same slot.
- **InvestNext, `mhcportal.investnext.com`, is the Fund II investor portal and it locked five LPs out of their K-1s inside three days of the 2026-09-10 broadcast.** *"Can't get into the portal. Should consider changing vendors!!"* `KP-0110`, Critical, three paths on the row. The fallback that worked was a password protected PDF.
- **SafeSend is Citrin's return signing portal.** It issues the signature request and access code; it sends no completion notice to the signer, and what releases a K-1 after signature is unknown. On `10-Business/outside-help/citrin-cooperman`.
- **SharePoint Online is over its storage entitlement: 6,567.38 GB against 2,394 GB on 2026-09-11**, up from 6,550.52 GB four days earlier, with four migration tasks going overdue the same day and HR unable to upload resumes that evening. `KP-0111`. The restructure that would address it is on hold, `KP-0100`, and Albert is still owed the note saying so, `TD-0580`.
- **Plaud is recording and not transcribing.** Three recordings totalling about 1h45m are unreadable across every retrieval path, a 53 minute recording on 2026-09-15 came back as three words, and nothing readable exists after 2026-09-05 for eleven meetings. `KP-0112`. Connector detail on `10-Business/connector-status`.
- **Adobe Sign, seen from the queue side:** the For Signature folder went 0 items for eight runs, then 6, then 19 messages on 2026-09-14, then 0 on 2026-09-15. Fourteen documents in the fortnight, listed on `60-Communities/projects`.

## Who decides, established 2026-08-31

**Austin, asked directly who decides what accounting system the company runs on:** *"Jon and I will ultimately decide. It is very difficult to pivot from Rent Manager."*

**Two facts, and this vault held neither.**

- **Decision rights on core systems sit with the two founders.** Not with the accounting function, and not with the incoming controller. On the 2026-08-31 vendor call Jon framed the why and Austin answered every systems question, and the note filed from it recorded three plausible owners because nothing on the page said. **A vendor evaluation that routes its output to the controller seat routes it to the wrong place.** The controller candidate is an input to the decision, and needs to be in the room for that reason, not because it is theirs to make.
- **Switching cost off Rent Manager is the governing constraint**, in his own words. **This also settles a question left open on [[70-Operations/meetings/2026-08-31-accounting-platform-intro-rillet]]**, where Austin's aside about looking at QuickBooks *"overall"* went unanswered by everyone on the call and was flagged as the largest thing that call opened. **It is not a live direction.** Anything proposed on top of Rent Manager starts with a strong presumption in favour of staying, which is the right lens for the 2026-09-04 demo: the question is what integrates, not what replaces.

## Decisions

- 2026-08-31 — Corner IQ is not moving forward. The positioning is deliberate and Austin was specific about it: the message is that Parakeet is not ready for the system, **not** that there is a problem with the system. He asked for a draft on that footing. Supersedes the 2026-08-18 trial decision below, which stays visible. (Source: Austin, on the delegation board)
- 2026-08-30 — MAV Consulting is the CRM. (Source: Austin, in the Structure Interview)
- 2026-08-20 — Power Automate moves onto dedicated server accounts. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-lucky-clover-site-visit]])
- 2026-08-18 — Corner IQ one-month trial with a small executive group. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-18-property-management-and-strategic-ai-integration-review]])

## Sources

- [[70-Operations/sops/sop-library]] — where each system is used, process by process.
- Austin, in the Structure Interview, 2026-08-30.
- [[00-Meta/daily-close/2026-09-14]] — Rent Manager account ownership, SharePoint storage and the signature queue; `00-Meta/daily-close/2026-09-09.md`, `2026-09-10.md`, `2026-09-11.md` and `2026-09-15.md` for the rest. Added 2026-09-15.
