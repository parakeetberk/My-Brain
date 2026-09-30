# Austin Berk — Second Brain

The single source of state for Austin Berk's professional and personal operation. If it is not in here, it does not exist.

**Owner**: Austin Berk — austin@parakeetcommunities.com
**Kept by**: `chief-of-staff` agent, maintained by `second-brain-librarian`
**Established**: 2026-08-26

## Why this exists

Austin runs Parakeet Communities and affiliated entities, a multi-billion-dollar manufactured-housing operation, and has ADD. The constraint is not effort — it is that state is scattered across three clouds, multiple SharePoint site collections, departed employees' archives, and his head. Every decision costs a search. This vault eliminates that search cost.

Design constraint: **this vault must not require discipline to maintain.** Anything depending on Austin remembering to file something will fail. Agents maintain it.

## Structure

| Folder | Holds | Lifetime |
|---|---|---|
| `00-inbox/` | Raw capture, unprocessed. Dump zone. | Emptied weekly |
| `01-now/` | Live commitments, this week's priorities, open loops | Days to weeks |
| `99-Archive/2026-08-catchup/entity-pages/` | Companies, communities, properties, people, vendors, lenders | Durable |
| `03-domains/` | Functional knowledge: supply chain, capital, ops, sales, legal, personal | Durable |
| `10-Business/storage-inventory/` | Cloud storage inventories — where everything actually lives | Refreshed quarterly |
| `00-Meta/decisions/` | Decisions made, with date and rationale | Permanent |
| `99-Archive/2026-08-briefs/` | Durable reference material, templates, playbooks | Durable |
| `99-Archive/2026-08-closed/` | Dead, closed, superseded. Kept for provenance. | Permanent |

## Conventions

- **Filenames**: `kebab-case.md`. Entities get their own file. No dated filenames except in `00-Meta/decisions/`, which uses `YYYY-MM-DD-slug.md`.
- **Verify the current date from the system clock before datestamping anything.** A full-vault off-by-one occurred on 2026-08-26 from assuming the date instead of checking it.
- **Absolute dates always.** Never "next week" or "last month" — write the real date. Today is meaningless in six months.
- **Provenance on every substantive fact.** Cite the file path, message ID, or quote it came from. Unsourced claims cost more than they save.
- **Label confidence on every claim**: *Verified* (primary source read), *Single-source* (one place, unconfirmed), *Inferred* (reasoning from names, sizes, patterns). Verify against the primary artifact, never an index or summary — indexes go stale. Precedent: a "18 reds pending" claim from one index line reached a decision record before the shipped report was found to say the opposite.
- **Link with `[[wiki-links]]`.** Link liberally; a link to a note that does not exist yet marks work worth doing.
- **Contradictions stay visible.** When new information conflicts with an existing note, keep both with dates and flag it. Do not smooth it over — conflicts are signals.
- **Three-item ceiling.** Anything in `01-now/` presented to Austin tops out at three items. If there are more, they are ranked and held, not shown.
- **Never surface an item without checking `99-Archive/2026-08-closed/` and `00-Meta/commitments.md` first.** Any brief, sweep, or report built from a fresh data pull MUST diff its findings against what is already closed before showing Austin anything. **Absence of a written reply is not evidence an item is open** — resolutions happen in calls, in cars, and in person, and the archive is the only record of them. Precedent: on 2026-08-27 the morning brief re-raised the Toby Nelson litigation update as urgent, four hours before a meeting, when Austin had told us the previous morning it was handled directly with Joe at Jadian and it had been archived the same day. Re-raising a closed item costs more trust than missing an open one.

## The organizations

Austin operates across three distinct identity and storage domains. This separation is the root of the fragmentation problem:

| Org | Primary storage | Identity |
|---|---|---|
| **Parakeet Communities** | Microsoft 365 — SharePoint + OneDrive | austin@parakeetcommunities.com |
| **A2Z MHC** | Dropbox (team) | austin@a2zcp.com |
| **Personal** | Google Drive | austinrberk@gmail.com |

"Berk Inc" is the informal umbrella across all three. Establishing the actual legal and operational relationship between these entities is an open task — see `99-Archive/2026-08-catchup/entity-pages/`.

## Target state — decided 2026-08-26

This is where everything is going. Migration in flight, owned by **Albert**.

| Content | Destination |
|---|---|
| **Everything manufactured-housing** — Parakeet, A2Z, Bedrock | **SharePoint Birdcage** (`/sites/ParakeetBirdcage`) — system of record |
| **Personal** — Belmart, Winterset, Get Real, other investments, financials | **Dropbox** |
| A2Z Dropbox tenant | Archive / sandbox in the interim; end state holds no MH content |

Two clean domains replacing three fragmented ones. Full decision at `00-Meta/decisions/2026-08-26-storage-target-state.md`; operational landmines at `10-Business/sharepoint/migration-risks.md`.

**When filing anything from here on: MH goes to Birdcage, personal goes to Dropbox.** Do not add to the legacy locations.

## Cloud storage — known surfaces

Discovered 2026-08-26. Full inventories in `10-Business/storage-inventory/`.

**Microsoft 365 / SharePoint** (`parakeetcommunities.sharepoint.com`) — **at least 12 sites across 14 drives**, plus two tenant root-site libraries and 6 personal OneDrives. Corrected 2026-08-26 after survey; the original estimate of 5 sites was wrong by more than half.

- `/sites/main` — primary repository. **2.88 TB, 24 top-level branches** under Shared Documents (not the 6 originally assumed). 71 communities in Operations, 71 in Construction, 60 DD folders, 36 archived.
- `/sites/ParakeetHomes` (plural) — Property and Site Data / Site Plans. **Authoritative** for site plans.
- `/sites/ParakeetHome` (**singular — one letter apart**) — a fifth, genuinely divergent Site Plans tree. See Known Problems #1.
- `/sites/ParakeetHomes-ParakeetHomesxCavco` — Site Plans, byte-identical clone of ParakeetHomes
- `/sites/ParakeetBirdcage` — 3 libraries. Holds `Data  Analytics/Claude Cowork` (23.07 GB), a prior AI pass over the corpus
- `/sites/Corporate-Legal`
- `/sites/LegalParakeet`
- `/sites/SouthernaireNorthRidge`
- `/sites/ParakeetOriginsAcquisition`
- `/sites/ParakeetOperations9-Amsterdam-General`
- `/sites/Operations95` — Files / Property A...
- `/sites/UserArchive` — departed employees (Deborah Koester 2025-10-08, Amy Furbush 2026-06-12)
- Personal OneDrives across the team, holding meeting recordings

Two legal-adjacent sites exist (`Corporate-Legal`, `LegalParakeet`) with no documented distinction between them — resolve before filing anything legal.

**Austin's OneDrive** — notable folders: `Austin_Brain_Vault`, `BerkClaude`, `Command Center`, `Austin @ Work`, `Community Manuals`, `Rent Manager Exports`, `Reporting`. Root holds roughly 200 loose files.

**Dropbox** (A2Z MHC team, namespace `11855305057`) — clean ten-folder taxonomy: Business Lines, Reference, Team Paper Docs, Property Management, Austin Berk, Lamberton Lake DD Files, Pipeline, Corporate, Cambridge - SCH 2025, Accounting.

**Google Drive** — personal, mixed personal and shared-in files.

## Known problems

1. **`/sites/ParakeetHome` vs `/sites/ParakeetHomes` — one letter apart, and neither is a superset.** The singular site holds 29 communities, the plural 24. Of the 19 that overlap, 14 are byte-identical but **5 differ materially** (Northgate +219.8 MB and Harbour +105.4 MB on singular; Lucky Clover −244.9 MB on singular). Ten communities exist only on singular, five only on plural. Deleting either one loses data. **This is the most dangerous item in the estate** — resolve before any consolidation touches site plans.

2. **Site plan cloning — resolved, and it is a three-way, not a four-way.** `/sites/ParakeetHomes`, the Cavco satellite, and `/sites/main/.../Cavco Homes/Plans for Sites` hold byte-identical trees (27 Bay Oaks lot folders at exactly 812,391,202 bytes each), created in a copy chain 2026-02-02 → 02-03 → 02-05. **`/sites/ParakeetHomes` is authoritative** — it is the source of the chain and the only complete tree. The fourth path, `/sites/main/Shared Documents/Construction/BAY OAKS VILLAGE I`, is **NOT a duplicate** — it is the construction record (CONTRACTS / DEVELOPMENT / PROJECTS) and **must not be deduped**. Pattern extends to 22 of 23 shared communities, ~16.6 GB redundant.

3. **Community names do not reconcile across Operations and Construction.** Both hold 71 folders; not the same 71. Six Operations assets lack a Construction folder, four the reverse, eight are spelled differently including typos (`WHSIPERING PINES MA`). Any join on community name silently mismatches ~18 assets — this corrupts cross-system reporting.
4. **Securities and investor records sit under a personal Gmail account.** `austinrberk@gmail.com` holds membership in three corporate Google Shared Drives, one containing cap tables, fund subscriptions, K-1s, an LPA, and executed signature pages. Outside any Workspace admin lifecycle. Invisible to standard audit queries. Three is a floor — memberships cannot be enumerated.

5. **OneDrive root as dumping ground.** ~200 loose files, including `Book1.xlsx` through `Book8.xlsx`, `Drawing 1-8.vsdx`, `Copy of Copy of Copy of FMHA.xlsx`. Work was done here and lost.

6. **Institutional knowledge in archived user drives.** `/sites/UserArchive` holds departed employees' files nobody can find.

7. **Three identities, no bridge.** Nothing links Parakeet, A2Z, and personal records.

8. **Known narrative contamination inside the deal models.** `Claude Cowork/.../batch/kb/INDEX.md` documents prose from one deal ("Triple S") cloned into dozens of workbooks, tagged `do-not-quote`. **Any index or summary that quotes model narrative without honoring that flag will propagate known-wrong text.** Read that INDEX before building anything on top of the underwriting corpus.

## Working with Austin

- One next action per response. Never a menu.
- Three-item ceiling on any list.
- Never say "you are behind." Say what is un-indexed, un-decided, or un-delegated.
- Make completed work visible — ADD erases it.
- Decide reversible things and report; ask only about money, third parties, and irreversibility.
- Delegate anything mechanical to an agent.

## Agent roster

- `chief-of-staff` — orchestrator, decision-maker, keeper of this vault
- `cloud-archivist` — storage survey, indexing, duplicate detection
- `supply-chain-analyst` — home procurement, set-crew throughput, bottleneck diagnosis
- `second-brain-librarian` — filing, linking, vault maintenance
