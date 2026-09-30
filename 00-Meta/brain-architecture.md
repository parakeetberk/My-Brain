# One Brain, the architecture

**What this is:** the contract for how every agent, model and skill gets its knowledge, so there is one source of truth and not four copies drifting apart. **Status:** DRAFT 2026-09-29, written at Austin's instruction. The routing rules below go into `CLAUDE.md` only on his sign-off (CLAUDE.md team rule).

**His words, 2026-09-29:** *"My Brain is where every agent and model goes first. The knowledge of the communities and the vehicles and our overall company from emails and teams and the rent manager api and mcp to the data warehouse... build out a team of agents to all be run off one brain."*

## The four places knowledge lives today

| Layer | What it should hold | What it actually holds, measured 2026-09-29 |
|---|---|---|
| **This vault** | Every business fact, number, decision, register row, with source and date | The right content. 616+ pages. Canonical homes already exist for the big programs |
| **Claude's cross-chat memory** | Who Austin is, how he works, and a pointer to the vault page for each program | **Full working notebooks.** Fund II wind-down 37 KB, Intercompany three files at 20 KB + 24 KB + 2 KB, BMHCII Financials 17 KB, JREFI model 11.5 KB, Payroll 9.5 KB. Each one parallels a vault page and drifts from it |
| **Project memory** (per Cowork project) | Tool quirks only: what broke, what works, gotchas | Mostly right. Some project facts that belong in the vault |
| **Skills** | Procedure only: how to do a job | Mostly right. Must read facts from the vault, never carry their own copy |

**The duplication, VERIFIED 2026-09-29 by reading both sides:**
- **Close It Down and BMHCII Financials:** one program since 2026-09-19 on disk, confirmed by Austin 2026-09-22 and again 2026-09-29. Still two memory files (37 KB and 17 KB) plus the vault page `80-Finance/fund-reporting/bedrock-fund-ii-winddown.md` (37 KB). Three copies of one program.
- **Intercompany:** three memory files plus `80-Finance/intercompany-arap-recon.md`. Four copies.
- **The CPAs:** Tim and Lisa sat in one project's memory only. Austin ruled 2026-09-29 their email matters to everything. **Fixed tonight:** global memory cards `tim-cpa` and `lisa-cpa` point at `10-Business/outside-help/citrin-cooperman.md`. The old project copies are removed on his go.
- Moe, the camera rollout and Ramp booking each have two memory copies.

## The routing contract (proposed for CLAUDE.md)

1. **Brain first.** Any agent, model or skill starts at `CLAUDE.md`, then `00-Meta/index.md`, then the folder MOC, then only the pages it needs. No agent answers from a raw source when a page exists.
2. **Facts land in the vault first.** Anything learned from mail, Teams, Plaud, Rent Manager, the warehouse or Ramp is written to its vault page or register, with its source link and date, before it is used anywhere else.
3. **Memory is a pointer card.** One card per program or person: what it is, the vault path, aliases, and at most five rules Austin stated that must never be broken. Target under 2 KB. Everything else lives on the page.
4. **Skills are procedure.** A skill says how. It reads what from the vault.
5. **Git is the proof.** Every write to this vault is committed and pushed within 15 minutes (`KP-0132`, closed 2026-09-29), so every change any agent makes can be checked line by line.

## The feed map, what the agent team is built on

Owned by [[10-Business/data-lineage]], which is extended rather than duplicated. One row per source: which agent harvests it, how often, and which page or register it writes to.

| Source | Harvest agent (brief in `95-Agents/`) | Writes to |
|---|---|---|
| Outlook, all folders | morning brief, daily close | registers, community pages |
| a2zcp / Bedrock Gmail | morning brief, daily close (first class, CLAUDE.md rule 14) | Fund II page, LP page, registers |
| Tim and Lisa (Citrin) mail, both mailboxes | **every sweep, flagged first** (Austin 2026-09-29) | `10-Business/outside-help/citrin-cooperman.md`, commitments |
| Teams | transcript to action, daily close | registers, meetings |
| Plaud recordings | transcript to action | `70-Operations/meetings/`, decisions |
| Rent Manager API and warehouse | hot sheet refresh, dashboard refresh | community hot sheets, `60-Communities/portfolio.md` |
| Ramp | charge coding agent | `80-Finance`, Ramp booking program |

Rows with no agent yet are the hiring list for the agent team.

## Chats become disposable (added 2026-09-29, Austin's question)

**Austin asked whether this lets him archive chats daily or weekly and stop working project by project.** It does, on one condition: **nothing may live only in a chat.**

- **Close-out rule.** Before a chat ends, whatever it decided, built or learned is written to its vault page or register, logged, and pushed. Then the chat holds nothing the Brain lacks and can be archived without loss. The daily close lists which chats filed what that day, so a chat that filed nothing is visible before it is archived.
- **One home, not many projects.** Work starts in the My Brain folder by default. A separate Cowork project is only for a big isolated build, and its knowledge still lands here. Project scoped memory is what made work project focused; Phase 1 moves it into vault pages, after which those projects can be archived too.
- **Limit, stated plainly.** Claude cannot see or archive the chat list. Archiving is Austin's click; the close-out rule is what makes that click safe.

## Phase 1 progress

**As of 2026-09-29 21:54 ET.** Five programs moved from Claude memory into vault pages, every line checked by script, and their memory files shrunk to pointer cards of about 1 KB:
- Fund II wind-down, Close It Down plus BMHCII Financials: `80-Finance/fund-reporting/bedrock-fund-ii-operating-rules.md`
- Intercompany, three memory files into one: `80-Finance/intercompany-operating-rules.md` (the open Intercompany chat closed out to it first)
- JREFI cash flow model: `80-Finance/jrefi-cashflow-model.md`
- Payroll rebuild: section on `80-Finance/payroll-model.md`
- Permits rebuild: section on `70-Operations/license-and-permit-ownership.md`
- The CPAs, Tim and Lisa: one shared memory card each, project copies removed

**Memory went from about 150 KB of working notebooks to pointer cards.** Still to do in Phase 1: the smaller doubles (Moe, camera rollout, Ramp booking), the project scoped files that are left, and ledger rows for the dollar figures the moved records carry.

## Three paths

**A. Memory diet only.** Shrink every fat memory file to a pointer card after diffing its contents into the vault page. About two hours of Claude's work. Fixes the drift. **Still exposed:** no written contract, so the next agent built can recreate the mess. Wrong choice if the goal is a team of agents, which it is.

**B. Brain first contract, then the team (recommended).** A, plus the routing contract into `CLAUDE.md`, plus the feed map above, plus agents built one at a time on it, each with one job, one brief, one schedule, and writes that land in git. Phase 1 memory diet, Phase 2 contract, Phase 3 feed map, Phase 4 agents. **Still exposed:** scheduled agents need Austin's PC awake to reach the vault. Wrong choice if agents must run from outside Claude.

**C. Brain as a service.** Put the vault behind a server (the GitHub repo plus a search index or MCP) so any model, including non-Claude ones and cloud agents, can query it with the PC off. **Wrong now** because it would serve today's duplicates to more readers faster. **Grafted onto B as Phase 5**, since the GitHub backup now works and makes it possible.

**Why B:** A fixes today and leaves tomorrow open; C scales the problem before fixing it. B takes A as its first step and C as its last.

## Order of work
1. **Phase 1, memory diet, plus the chat close-out rule.** Wind-down merged (Close It Down plus BMHCII) first, then Intercompany, then JREFI, Payroll, permits. Anything in memory that the vault page lacks is added to the page with its date. Then the memory file becomes a pointer card. Old duplicates removed only on Austin's go.
2. **Phase 2, contract into CLAUDE.md.** On Austin's sign-off.
3. **Phase 3, feed map** into `10-Business/data-lineage.md`.
4. **Phase 4, agents,** one at a time from the feed map's empty rows.
5. **Phase 5, cloud read access** to the Brain through GitHub.
