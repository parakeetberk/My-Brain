# Delegation board

**What this is:** the one page that reads all five registers at once and asks a different question from the morning brief. The brief asks what Austin does today. The board asks what leaves his desk. It holds no items of its own. It counts and reads the five registers that do, so it can never become a sixth one.

**Status:** current, 2026-08-31. First build. Rebuilt weekly, alongside the Brain review.

## Why it exists

Austin's challenge on 2026-08-31, off the back of that morning's brief: if this is his brain, it should help him decide what to **delegate**, not only what to do next.

**Updated 2026-09-01: he was right, and the half I defended has since been removed.** I argued the three-item ceiling was his own rule and the brief should keep it. He replaced the rule outright the next morning - show everything, highlight three ([[CLAUDE]] rule 12). This board was the first thing built on the new principle before the rule existed, which is part of why the rule changed. The original argument is left below as written.He was half right, and the half that was wrong is worth keeping. The three-item ceiling is his own rule ([[CLAUDE]] rule 12) and the brief should keep it, because a glance page that opens with 660 rows is a page he stops opening. But no page anywhere held the whole board. So the ceiling was doing triage with nothing behind it, ranking three items out of a pile nobody had ever measured. This page is what sits behind the ceiling.

## The 2026-08-31 baseline

First end-to-end count of the five registers. Any future claim about backlog size measures against these.

| Register | Open | Grain |
| --- | --- | --- |
| `00-Meta/commitments.md` | 21 | what Austin owes and is owed |
| `00-Meta/parked-decisions.md` | 19 | waiting on his ruling |
| `10-Business/eos/to-dos.md` | 258 | tasks with a named owner |
| `10-Business/storage-inventory/known-problems.md` | 31 | defects in the file estate |
| `60-Communities/open-items.md` | 331 | property follow-ups |
| **Total** | **660** | |

**173 have no owner.** Two of those splits are recorded: **163 of the 258** to-do rows and **1 of the 331** property rows. The remaining nine sit across commitments, parked decisions and known problems without a per-register split having been taken, so do not quote one.

These are counts of register rows, not business figures, which is why they are here and not in `00-Meta/numbers-ledger.md`. The ledger is for numbers about the company. This is a number about the Brain.

**As-of matters here.** The count was taken before Austin's 18 comments on the board were worked through the same afternoon. Six rulings, nine commitment amendments and twelve routed tasks came out of that pass, so the live totals have already moved. The baseline is the baseline, not the current position.

## The finding: most of the unowned pile is not corporate work

**150 of the 163 unowned to-do rows are field items.** Speed bumps, an entrance sign, a mailbox vendor, a utility golf cart. They came off the 27 road-trip transcripts and landed on the corporate register because that is where the harvest put them, not because they were ever Austin's.

That reframes the whole backlog. **63% of the corporate to-do register is misfiled rather than neglected**, and one handoff to property operations clears it.

The contrast next door is the proof. `60-Communities/open-items.md` carries 331 property items and exactly **one** is unowned, because somebody did an assignment pass on it once. The corporate register never got one.

**The recommendation, unactioned as of this build:** the tour register moves to property operations as a block, regionals taking their own communities.

## The second finding: dependencies are only visible across registers

**Four items route through David Berman, who is being exited.** Commitments 13, 15 and 21, and to-do P5, all sit under item 16.

Each of the four reads as independently delegable on its own line. That is how all four would have failed quietly. The dependency does not exist in any single register; it appears only when they are read together, which is the thing no page did before this one.

**Austin's answer, same day:** the extraction happens before the exit, not after. He had already decided it and the registers did not know. See `80-Finance/intercompany-arap-recon.md`.

## What the first build got wrong

Recorded on purpose. A board that only records its hits is a board nobody can calibrate against.

- **Geiger House.** The board put the PSA liability cap on Austin with Jon. It is Jon's, 100%, and Austin is FYI. Wrong within four hours of publishing. See `60-Communities/geiger-key-rv-resort.md`.
- **The Berman sequencing.** Raised as an open recommendation when it was already decided.
- **The insurance tie-out.** The board suggested reassigning it after two non-acceptances. Austin declined: it stays with accounting and needs a date instead.

Two of the three are the system working rather than failing, which is the argument for publishing the board at all. The third is the argument for asking before recommending.

## How it gets rebuilt

1. Count the five registers. Open rows and unowned rows for each.
2. Diff against `99-Archive/` and `00-Meta/commitments.md` before anything is called open. [[CLAUDE]] rule 11.
3. Mark a proposed owner on every delegable item, and mark it **proposed**. Never invent one. Where no source names an owner, the row says unassigned and names the forum where Austin can settle it.
4. Split the parked decisions into the ones a single sentence clears and the ones blocked on a document or a number somebody has to go and fetch. On 2026-08-31 that split was 11 and 8.
5. Publish as an artifact. Tell Austin in chat that it is up, because artifact comments are pull-only and a comment he leaves at 2pm sits untouched until the next scheduled run reads it.

## The comment channel, and its limit

The board is how the disposition channel finally carried a disposition. The 2026-08-29 brief drew zero comments; this one drew 18 and all 18 were worked through.

It worked because Austin was told to leave the comments **and then say so in chat**. That two-step is the pattern to keep. A comment on its own does not wake a cloud session, and an empty comment list is never agreement.

All 18 threads remain open on the artifact. None was sent to Claude, so none can be replied to or resolved from a session. They are addressed in the registers; it is the threads that cannot be closed. Do not read them as 18 unaddressed items.

## Related

- [[10-Business/eos/to-dos]] - the register the 150-row finding is about.

## Sources

- Delegation board, 2026-08-31: `https://claude.ai/code/artifact/2ef2ab84-c786-4044-897c-09a2b8897a96`
- `00-Meta/audit-log.md`, the 2026-08-31 rows, where the counts and both findings were first recorded.
