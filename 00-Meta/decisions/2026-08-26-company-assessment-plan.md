# Company Assessment & Automation Plan

**Date**: 2026-08-26
**Requested by**: Austin — a full read of the company, an honest people and org assessment, and a roadmap for the agent machine.
**Status**: Plan for approval. Nothing below has been executed.

---

## What you asked for, restated

1. Understand who actually does what across Parakeet — from email and Teams.
2. Assess each person: who can be trusted with important work, who is on the chopping block.
3. Review whether the organization is structured correctly.
4. Build agents that take administrative work off your plate — permit renewal monitoring, MH portal lookups, and more.
5. Stop losing work to agent failures.
6. Find things on the personal side that make your life easier.

All of it is doable. One piece I want to change the method on, and I will explain why in terms of accuracy rather than principle.

---

## The one thing I would do differently

You asked me to read every employee's mailbox and Teams chats and produce individual assessments including who to let go.

**I can do that. I think the output would be wrong, and wrong in a specific and expensive direction.**

Three days of evidence from your own operation:

| Person | What the written record showed | What was actually true |
|---|---|---|
| **Zach Schwartz** | 16 days silent on a direct $40k governance question | Discussed and resolved on the weekly call |
| **David Berman** | 30 days unresponsive on the journal entries | Replied **four times in 48 hours** — 1h41m, 4min, 10h06m, 18min — raised a legitimate objection that **you** still owe an answer to |
| **Toby Nelson** | 6 days ignored on a deadlined ask | Handled directly with Joe at Jadian, off-channel |

**Three for three.** In every case the written record made someone look unresponsive and the resolution had happened somewhere no sweep can reach. Teams transcripts are blocked tenant-wide. Plaud is not connected. Phone calls and site visits leave no trace at all.

Now apply that instrument to 29 people and rank them. The bias is not random — it is **structural and it runs exactly backwards**:

- **Community managers** work by phone, radio, and walking lots. Rose, Vicky, Julie, Angel — the people your own road trip singled out as your best — generate almost no written trail. They would rank at the bottom.
- **Corporate staff** who live in Outlook would rank at the top regardless of output.
- **Anyone whose good work happens in a meeting** — which is most decisions here — becomes invisible.

You would systematically penalize your field organization for doing the job correctly.

There is also a plain legal fact worth one sentence: an AI-generated dossier assessing a named employee's trustworthiness, built from their private messages, is a discoverable document. If any of these people are later terminated, that file is the first thing opposing counsel asks for. It does not matter that the monitoring is lawful — what matters is what the document says and how it was made. The road-trip review already warns that its own speaker attribution is best-effort AI diarization and names Ozzie, Berman, and Ashlyn as needing verification before action.

**None of this means you cannot get what you actually want.** It means the evidence should be outcomes, not correspondence.

### What I propose instead

Assess **roles and work**, not inboxes.

| Signal | Source | What it tells you |
|---|---|---|
| Commitments made vs. met | ClickUp task history, email threads **you** are party to, meeting follow-ups | Reliability, measured on delivery |
| Response latency to *you* and to peers | Threads already in your own mailbox | Responsiveness, without reading anyone's private mail |
| Work product | Actual deliverables — reports filed, permits pulled, homes set, occupancy moved | Output, not activity |
| Escalation behavior | Do problems surface early or arrive as surprises? | Judgment |
| Single-point-of-failure exposure | Function mapping | Structural risk regardless of the person |
| Your own direct observation | The road-trip review already contains detailed, named, first-hand assessments you made yourself | The highest-quality evidence you have |

That last row matters more than anything I could scrape. **You already did this assessment.** The road-trip document names Rose, Liz, Alex, Vicky, Julie, Angel, Janine, Travis, Brandon, Fernando, Leslie, Demetria, Stewie, Charles, Melanie, Justin — with specifics, from standing in front of them. That is better evidence than any inbox sweep, and it is already written down.

**If, having read this, you still want the full mailbox sweep — say so and I will run it.** It is your company and your call. I would want HR or counsel to sign off on scope first, and I would label every finding by evidence quality so you can see which conclusions rest on silence.

---

## The assessment — five workstreams

### WS1 — Org structure and function map
**Question: is the company structured correctly, and what is unowned?**

- Build the real org chart from `Parakeet & Affiliates Org Chart.vsdx`, `corporate org.csv`, `Org Chart Overview_122023.xlsx`, ClickUp assignments, and observed reporting in threads you are on.
- Map **every function** to an owner. The unowned list is the deliverable — today it already includes permits, the Regency sinkholes, the Brunswick sewer pipe, D-4 EKEET ($1,147,531), and utilities/licenses inside accounting.
- Identify **single points of failure** — functions where one departure loses institutional knowledge. Known already: Berman (accounting, entity history), Melanie (prior permit knowledge), Sam at Paradise Lakes (retiring, date keeps moving), the departing Regency I maintenance man.
- Span-of-control and layer analysis: regionals, community managers, corporate.
- **Output**: `99-Archive/2026-08-catchup/entity-pages/org-map.md` plus a function-to-owner matrix with gaps highlighted.

### WS2 — Role and reliability assessment
**Question: who can carry important work?**

- Per the method above — outcomes, commitments, and your own recorded observations.
- **Output**: a role assessment per function, with named incumbents, rated on *demonstrated delivery*. Written to be defensible if read aloud.
- Explicit separation of three different problems that get conflated: **capability** (can they do it), **capacity** (do they have room), and **clarity** (do they know it is theirs). Most "performance problems" in this operation look like clarity problems from here — 134 of 159 road-trip items have no owner at all.

### WS3 — Operating rhythm
**Question: does the management system work?**

- EOS/L10 health. **The L10 forum went dark after 8/14** — that is a finding, not a detail. Your accountability ceremony stopped and nobody restarted it.
- Which meetings produce decisions and which produce discussion.
- Where decisions queue: 13 standardization decisions on Jon, ~19 parked decisions from the road trip, DECISION 0 blocking Albert.
- **Output**: `70-Operations/ (page not built)`.

### WS4 — Systems and data architecture
**Question: what is the machine actually running on?**

- Resolve the single-source-of-truth question across MAV CRM, Rent Manager, RentViewer warehouse, and Camp Spot. **Five-week runway to October snowbird season.** Jon's position: warehouse-first may make the MAV MCP redundant.
- Map every system, its owner, its cost, and what depends on it.
- Identify what is buildable with agents versus what needs a platform.
- **Output**: extend the existing `10-Business/systems-architecture.md` — do **not** create a second file. That note was written the same evening from the road-trip review and already covers the MAV / Rent Manager / RentViewer / Camp Spot question. WS4 deepens it rather than duplicating it.

### WS5 — Personal
**Question: what is taking your time that should not be?**

Detailed below.

---

## The machine — agent roadmap

You are right that this should be built. Here is what is actually buildable, in order of value over effort.

### Tier 1 — buildable now, no new access required

| Agent | What it does | Cadence |
|---|---|---|
| **Morning brief** | Overnight email/Teams sweep, today's calendar, three things that matter, one decision block | Daily, 06:00 |
| **Commitment tracker** | Watches your sent mail and chats for promises you make, files them, chases them | Continuous |
| **EOD close** | What moved, what slipped, tomorrow's prep | Daily, 18:00 |
| **Meeting prep** | For each meeting: attendees, open items with them, last commitments both ways | 30 min before each |
| **Weekly review** | Re-rank open loops, kill dead items, surface slipped-twice items | Weekly |
| **Vendor scorecard** | Champion first — no-shows, delivered-not-set days, defect reports, by property | Weekly |

### Tier 2 — needs credentials or portal access

| Agent | What it needs | Value |
|---|---|---|
| **Permit renewal monitor** | AHJ portal logins per jurisdiction | Exactly what you described. Watches filing status and renewal dates, alerts at 120/90/30 days. **Directly prevents the 21st Mortgage failure** — a financing channel went dark because registrations lapsed and nobody noticed until a mystery shop was denied. |
| **MH title / VIN lookup** | State portal access | Pull home info, title status, lienholder. Feeds the FEMA sell-vs-scrap decision at Gulf Breeze and the PSE title cleanup. |
| **Rent Manager reporter** | API access — already exists in your stack | Occupancy, delinquency, WIP by stage. **Would close the biggest measurement gap you have**: nothing currently shows homes in WIP by stage across the portfolio. |
| **AP exception monitor** | AvidXchange access | Invoices unassigned past N days. The $108,919 A&A invoice sat since April. |
| **Compliance calendar** | Consolidated license/registration list | Every renewal, every jurisdiction, one calendar with automated alerts. |

### Tier 3 — build after the assessment tells us what matters

Ops-specific agents for inspection routing, work-order aging, home-set scheduling, and the L10 scorecard. **Deliberately not specified yet** — the assessment should determine these rather than me guessing now.

### An honest note on the permit-scraping agent

You named it as the example, and it is the right idea, but AHJ portals are the hardest target in this list: dozens of jurisdictions, no APIs, inconsistent authentication, some with no online presence at all. **Recommended approach**: start with the five or six jurisdictions covering the most communities, prove the pattern, then expand. A partial monitor that reliably covers 60% of your permit volume beats a comprehensive one that never ships.

---

## Why agents failed today, and how to stop it

You noticed. Four of five died — two API errors, two stalls at the 600-second watchdog. **My fault, not the tooling's**: I launched five heavy agents at once and starved them.

Fixes, applied from here:

1. **Cap concurrency at three.** Today's failures all came from running five.
2. **Incremental saves.** Every agent writes its file early and fills it in, so a stall loses minutes rather than everything. The Excel and brain-update agents were re-briefed this way and both completed.
3. **Checkpoint long jobs.** Split anything over ~20 minutes into phases with a saved artifact per phase.
4. **Scheduled agents for recurring work**, not ad-hoc launches. Cron-based runs are more reliable than long interactive ones and they survive session ends.
5. **Idempotent briefs.** Every agent brief written so a re-run is safe.

---

## Personal — what would actually help

From what I have seen this week, in order of time returned:

1. **Plaud is your best instrument and it is disconnected.** The week-in-review document is the highest-value artifact in the vault and it came from Plaud. Connecting it would (a) end the false-silence problem that has already misled you three times, and (b) let an agent turn every site visit and call into filed commitments automatically. **This is the single highest-leverage thing on the list.**
2. **The Visa card in the Post River Oaks transcript.** Tonight.
3. **Personal filing has a home now** — Belmart, Winterset, Get Real, Hensdale, investments to Dropbox. An agent can maintain it so it stays true.
4. **A real personal loop tracker.** Hensdale membership, the Belmart bank package, health, family, travel — currently these live in your head next to the company.
5. **Protected deep-work blocks.** You had six meetings today, two of them conflicting, and one asked you to decide something two hours before the meeting that would inform it. A calendar agent can catch that class of error before the week starts.
6. **A decision queue.** ~19 parked decisions plus today's. Batched into one weekly sitting rather than ambushing you individually.

---

## What I need from you

**Blocking — I cannot start WS2 without these:**

1. **The mailbox question.** Accept the outcomes-based method, or direct me to run the full sweep anyway. Either is fine; I need to know which.
2. **Scope of "employees."** ~29 staff. All, or corporate only?

**Not blocking, but they shape the work:**

3. Do you want the org assessment shared with anyone — Jon, an HR lead — or is it yours alone? That changes how it is written.
4. Which portal credentials can realistically be provisioned, and who owns them?
5. Is there an existing HR file or review history I should be reading?

---

## Sequencing

| Phase | Work | Duration |
|---|---|---|
| **0** | Answer the blocking questions above | You |
| **1** | WS1 org map + WS3 operating rhythm — parallel, 3 agents max | ~1 session |
| **2** | WS4 systems architecture + Tier 1 agents built and scheduled | ~1 session |
| **3** | WS2 role assessment — after WS1, because roles must be mapped before people are assessed against them | ~1 session |
| **4** | Consolidated findings + implementation plan for your approval | ~1 session |
| **5** | Tier 2 agents, as access is provisioned | Ongoing |

**Tier 1 agents get built in Phase 2, not at the end.** They start returning your time immediately and they generate the operating data that makes the Phase 3 assessment better.

---

## One thing I want to name

You said we are creating a machine. The instinct is right, and most of what is in this plan is machine-building.

But the biggest constraint I have found this week is not missing automation. It is that **134 of 159 commitments from your own road trip have no owner**, the L10 forum stopped on 8/14, and two senior people escalated permits on the same day with nobody assigned.

Automation applied to an ownership vacuum produces faster confusion. The org and rhythm work in WS1 and WS3 is what makes the machine hold — so I have sequenced it first, ahead of the agents you asked for. If you would rather see agents shipping sooner, say so and I will flip Phase 1 and Phase 2. It is a real trade and it is your call.
