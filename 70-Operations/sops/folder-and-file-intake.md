# Folder and file intake — design, not yet an SOP

**What this is:** the design for the "drop it in one place and describe it" intake Austin asked for on 2026-08-31, so that nobody at Parakeet ever creates a folder or names a file again. **This is a design spec with open decisions, not an approved SOP.** See *Why this is not an SOP yet* at the bottom.

**Status:** draft - 2026-08-31. Six open [TBD] items, each with a recommendation.

**Source:** Austin, 2026-08-31, verbatim intent: *"should have a SOP on creating folders. Something like the brain that they can just send to one place only describe it and then you can file it away to the appropriate place with naming conventions and meta data. this would keep everything clean."*

## The idea, and why it is the right one

Every naming standard ever written fails the same way: it asks 125 people to remember a convention while they are trying to do something else. [[10-Business/sharepoint/community-naming-standard]] will drift back to 21 mismatches within a year if compliance depends on people reading it.

Austin's answer removes the requirement. **Nobody names anything and nobody chooses a folder.** They drop a file in one place, say what it is in plain language, and the filing — canonical name, correct folder, metadata columns — happens downstream. It is exactly the pattern this Brain already runs on: humans drop things in `05-Inbox/` and talk; Claude does the filing and the writing. That pattern is already proven inside the Brain, which is the strongest argument for it.

The convention stops being a rule people follow and becomes a property of the system.

## The flow

1. **Drop.** An employee puts the file in the single intake location and answers a short prompt: what is this, which community, what kind of record.
2. **Classify.** The description plus the file itself determine the community, the department, the record type and the date.
3. **Name.** Applied from the standard, not from what the file was called: **files get the community name alone, folders get the community name with city and state** (rule 4).
4. **File.** Written to the correct Birdcage path, with the metadata columns populated.
5. **Confirm.** The submitter is told where it landed, so they learn the structure by seeing it rather than by reading it.
6. **Escalate.** Anything the classifier is not confident about goes to a review queue rather than being filed on a guess. **A wrong confident filing is worse than a queue.**

## Open decisions — six, each with a recommendation

| # | Decision | Recommendation | Why it matters |
|---|---|---|---|
| 1 | **[TBD] Where is the one drop location?** | A single Birdcage document library named `Intake`, not email and not a Teams channel. A library gives metadata columns, version history and per-item permissions; a channel gives none of those. | Everything downstream keys off this. Get it wrong and the intake becomes a second unstructured dump, which is the problem it exists to solve. |
| 2 | **[TBD] How is the description captured?** | A Jotform or SharePoint column set with four required fields — community, record type, date, one free-text line — not a free-text filename. Parakeet already runs Jotform, and the open Jotform-or-FastField decision is one of the five Phase 1 SOP decisions. | A free-text description is unclassifiable at volume. Four structured fields plus one free line is the least the classifier needs. |
| 3 | **[TBD] Who files it, and on what cadence?** | Claude on a schedule, with a human reviewing the escalation queue. Not a person filing every item — that is the bottleneck this design removes. | Decides whether this is automation or a new job. |
| 4 | **[TBD] What is the SLA from drop to filed?** | Same business day, with the escalation queue reviewed daily. | Without an SLA people stop trusting the intake and go back to creating their own folders, and the whole thing unwinds. |
| 5 | **[TBD] Who may drop, and who may bypass?** | Everyone drops. **Nobody bypasses**, including Austin and Jon. One exemption reintroduces the drift. | An intake with exceptions is not an intake. |
| 6 | **[TBD] Which metadata columns exist?** | At minimum `Community`, `Status` (active / archived / prospect), `Department`, `Record Type`, `Effective Date`. | **This is a hard prerequisite, not a detail.** Rule 6 of the standard removes all leading underscores, and these columns are what has to be carrying the classification before the prefixes come off. See the sequencing note on that page. |

## What this does not do

- **It does not touch the Parakeet Communities SharePoint.** Per Austin, 2026-08-31, that estate is read-only without permission. This intake is a Birdcage mechanism only.
- **It does not retroactively fix existing files.** Intake governs new material. The existing estate is normalised by the migration mapping, which is a separate piece of work.
- **It does not replace the standard.** [[10-Business/sharepoint/community-naming-standard]] stays governing; intake is what makes compliance automatic instead of voluntary.

## Why this is not an SOP yet

The house SOP process requires a named owner on every phase, a named receiver on every handoff, and a deadline pinned to a triggering event, and it will not mark an SOP Approved while a `[TBD]` is open. Six are open above, and four of them — the drop location, the capture method, the filer and the metadata columns — are architecture decisions rather than process steps. **Writing the SOP before they are settled would produce a document that reads complete and cannot be executed.**

The path is: Austin rules on the six, then the SOP gets written properly against the settled design, with the swim-lane flowchart and the intake form built as part of the package.

## Related

- [[10-Business/sharepoint/community-naming-standard]] — the conventions this intake applies
- [[10-Business/sharepoint/target-structure]] — the Birdcage tree things get filed into
- [[CLAUDE]] — the `05-Inbox/` pattern this is modelled on
