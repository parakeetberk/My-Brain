# Memory registry

**What this is:** every file in Claude's cross-chat memory, what it is for, and which vault page holds the real content. It exists so memory cannot quietly grow into a second copy of this Brain. **Status:** built 2026-09-29 from the live memory listing. Rebuilt by the `brain-audit` skill; a row here that disagrees with the live listing means the listing wins and this page is stale.

**The rule it enforces** (`00-Meta/brain-architecture.md`): memory holds who Austin is, how he works, and short pointer cards. **Business facts live in the vault.** A memory file over about 2 KB, or one with no vault page to point at, is a candidate to move.

## Counts, 2026-09-29

- **59 memory files.** 7 are pointer cards already moved into the vault. 11 are personal and stay in memory by design. 12 are program files not yet moved. 11 are scoped to one project. The rest are short people files.
- **Doubles:** 3 subjects exist twice (Moe, the camera rollout, Ramp booking). Marked below.

## Pointer cards, done

| Memory file | Vault page it points to |
|---|---|
| `/areas/bedrock-fund-ii-winddown.md` | `80-Finance/fund-reporting/bedrock-fund-ii-winddown.md`, `80-Finance/fund-reporting/bedrock-fund-ii-operating-rules.md` |
| `/areas/intercompany-reconciliation.md` | `80-Finance/intercompany-arap-recon.md`, `80-Finance/intercompany-operating-rules.md` |
| `/areas/jrefi-cashflow-model.md` | `80-Finance/jrefi-cashflow-model.md` |
| `/areas/payroll-recon-model.md` | `80-Finance/payroll-model.md` |
| `/areas/permit-license-tracker.md` | `70-Operations/license-and-permit-ownership.md` |
| `/people/tim-cpa.md` | `10-Business/outside-help/citrin-cooperman.md` |
| `/people/lisa-cpa.md` | `10-Business/outside-help/citrin-cooperman.md` |

## Program files not yet moved

| Memory file | Likely vault home | Note |
|---|---|---|
| `/areas/automation-stack.md` | `10-Business/` tools and systems | |
| `/areas/bay-oaks-rebrand.md` | `60-Communities/` Bay Oaks pages | |
| `/areas/camera-network-rollout.md` | `15-Projects/` or `70-Operations/` | **Double**, see project copy below |
| `/areas/construction-defect-oakside-hershey.md` | `60-Communities/` Oakside, Hershey | |
| `/areas/hunter-springs-note.md` | `60-Communities/` Hunter Springs | |
| `/areas/infill-initiative.md` | `70-Operations/` | |
| `/areas/parakeet-os.md` | `00-Meta/brain-architecture.md` | About this Brain itself |
| `/areas/quickbase-fastfield.md` | `15-Projects/fastfield-phase-i`, `15-Projects/quickbase-build` | |
| `/areas/ramp-booking-program.md` | `80-Finance/` | **Double**, see project copy below |
| `/areas/rehab-program.md` | `70-Operations/rehab-program/` | |
| `/areas/rentviewer-mcp.md` | `10-Business/data-lineage.md` | |
| `/topics/recent-work.md`, `/topics/tooling.md` | this page's review | Short; check if still true |

## Scoped to one project

These are visible only inside one Cowork project, which is what made work feel project bound. Parked by Austin 2026-09-29 ("leave for now").

| Memory file | Subject |
|---|---|
| `/projects/01a0890f…/areas/reporting-data-sources.md` | Which data source wins for reporting |
| `/projects/01a0890f…/people/melanie.md` | Melanie |
| `/projects/01a0a814…/areas/engie-utility-bills.md` | ENGIE utility bills |
| `/projects/01a0b15c…/people/demetria.md` | Demetria |
| `/projects/01a0b20a…/areas/camera-network-rollout.md` | **Double** of the shared camera file |
| `/projects/01a0ba3f…/people/erica-rocush.md` | Erica Rocush |
| `/projects/01a0c15f…/areas/ramp-booking-program.md` | **Double** of the shared Ramp file |
| `/projects/01a0c15f…/people/moe.md` | **Double** of `/people/moe.md` |
| `/projects/01a0c15f…/preferences.md` | Rollout sequencing preference |
| `/projects/01a0e981…/areas/accounting-daily-audit.md` | Accounting daily audit |
| `/projects/01a0edc0…/areas/lamberton-lake-sale.md` | Lamberton Lake sale |

## Personal, stays in memory by design

`/profile.md`, `/preferences.md`, `/people/jamie.md`, `/people/daughters.md`, `/areas/belmart-renovation.md`, `/people/rick-sullivan.md`, `/people/molly-menton.md`, `/topics/cooking.md`, `/topics/fitness.md`, `/topics/travel.md`, `/topics/schedule.md`. These are about Austin, not the business, and do not belong in a vault the team may one day read.

## Short people files

Work contacts with a line or two each: Albert, Alexis, Chris Hoke, David Berman, Derek, Jhosua, John Clark, Jon Wyss, Justin, Kippy, Leslie Croft, Lynn Rathjen, Moe, Natalie Magurne, Ridaa Murad, Sarah Kwiatkowski, Tom Gallagher, Zach. Fine as they are while short. Where `10-Business/people/` has a page for the same person, the vault page wins.
