# Road-trip tracker against the open board

**What this is:** the answer to Austin's question of 2026-09-01 — *"are the tasks on the tracker also within the board? if so we don't need the tracker. if not, we should look at the benefits of just adding it to the open board."*

**Status:** current — 2026-09-01. Analysis run against `parakeet-road-trip-tracker-2026-08.xlsx` (205 KB, last written 2026-08-26) and the 758 parsed board rows. **A decision is proposed at the bottom and not taken.**

## The short answer

**Mostly yes on topic, unprovably on items, and that is the wrong axis to decide on.** The tracker's *task* tabs are largely redundant. Its *other four tabs* hold three kinds of record that **no register in this Brain carries at all**, and that is the actual finding.

## What the tracker holds

| Tab | Rows | Columns |
|---|---:|---|
| Action Items | 159 | ID, Property, Category, Item, Detail, Owner, Urgency, Timing, **Est. Cost**, Source Section |
| Promises to Team | 36 | Property, **Person**, Promise, Owner, Status, Notes |
| Wins | 33 | Block, Who / What, Recognition, Suggested Action |
| Parked Decisions | 19 | Decision, Context, What It Blocks, Owner |
| Safety & Risk | 14 | Rank, Property, Risk, Detail, Owner, Urgency |
| This Week — Dated | 14 | **Date**, Item, Detail, Owner, Status, Notes |
| Vendor Accountability | 12 | **Vendor**, Property, Issue, Impact, **Escalation Status** |
| Dashboard | — | counts only |

254 substantive rows plus the Wins tab.

## What the overlap test actually showed, including where it failed

Three tests were run against all 758 board rows, and **they disagree by an order of magnitude, which is itself the answer.**

| Test | Result |
|---|---|
| Loose (token containment ≥ 0.60) | 96 of 254 look like duplicates |
| Strict (three rarest words must co-occur in one row) | 20 of 254 confirmed |
| Vocabulary (every distinctive word absent from the entire board) | **6 of 254 are provably absent** |

**The strict test is badly wrong and it was checked rather than trusted.** Ten of its "not found" rows were grepped by hand: **eight were on the board under different wording** — Camp Spot, Ozzie's exit path, pickleball, Lily Mora, speed bumps, the EPD pond violation, the resident memo. Only *lift station privacy fence* and *Auburn maintenance sign-off* were genuinely missing. **So a text-matching answer to "is this task already tracked" has roughly a 20% false-negative rate on this data, and no amount of tuning fixes that** — the two sources describe the same site walks in different words, one from `Parakeet Week in Review.docx` and one from the 27 filed transcripts.

**The six provably-absent action items**, vocabulary appearing nowhere on the board:

- Green Oak — parking lights
- Green Oak — rubber mulch beds out
- Regency I/II — set a mandatory weekly grass-cut day
- Paradise Lakes — orange mesh replaces caution tape
- Whispering Pines — relocate or refund the mis-booked transients
- Portfolio — job ads out now, seats filled in about 4 weeks

**Conclusion on the task tabs: redundant enough that keeping them as a second list is a liability, and not so redundant that deleting them is free.** Six rows have to be typed in.

## The real finding: three records with no home in this Brain

Confirmed by search across all five registers.

- **Promises to Team — 36 rows, and there is no promises register anywhere.** Property, **the named person**, the promise, the owner, a status. **This is the one that matters.** Turnover is a stated priority and a stated reason `KP-0022` is urgent; a list of 36 things the CEO told named employees he would do, with nothing tracking whether he did, is a retention artefact sitting in a spreadsheet nobody has opened in six days.
- **Vendor Accountability — 12 rows, no vendor register.** Vendor, issue, impact, **escalation status**. `KP-0011` to `KP-0014` are about contractor governance and this is live evidence for it.
- **Wins — 33 rows, no recognition register.** The road-trip review specifically recorded that the Lucky Clover maintenance lead *"deserves public recognition."* Nothing in this Brain tracks that, so it does not happen.

## Three fields the board schema cannot hold

The board's row has: id, reg, sec, desc, notes, owner, category, community, priority, state, lot, age, source. It has **no money, no date, and no person-owed**.

- **Est. Cost.** The tracker prices its action items. **The board has no money field at all**, so nothing on it can be sorted or filtered by what it costs.
- **Date** (the This Week tab). The board has `age` in days, not a due date. Nothing on the board can answer *"what is due this week."*
- **Person owed** (the Promises tab). `owner` is who does it. There is no field for who it was promised to.

## The proposal, for Austin to rule on

**Fold it in and archive the workbook, but the value is the four columns, not the 254 rows.**

1. Type the **6 provably-unique action items** into [[60-Communities/open-items]]. Ten minutes.
2. **Add Promises to Team as a sixth register**, `PR-0001` onwards, with a `person` field. This is the change that needs Austin's word, because [[CLAUDE]] says five registers and this makes six.
3. **Route the 12 vendor rows** into [[10-Business/eos/to-dos]] under a vendor category, linked to the Responsible Contractor block.
4. **Add `cost` and `due` to the board schema.** Optional on every row, shown when present, filterable. This is the single highest-value change on this list and it is independent of the tracker.
5. **Wins** become to-dos only where they imply an action; the rest are archived with the workbook.
6. **Archive `parakeet-road-trip-tracker-2026-08.xlsx`** to `99-Archive/` with a pointer here, so nobody works from a frozen list.

**What is deliberately not proposed: keeping both.** Two records of one tour, one live and one frozen, is the condition that produced this question.

## Sources

- `70-Operations/meetings/2026-08-southeast-tour/parakeet-road-trip-tracker-2026-08.xlsx` — read in full 2026-09-01, all eight tabs.
- `00-Meta/board-data/open-board-2026-09-01.json` — 758 parsed rows.
- Austin, 2026-09-01, on the board and in chat.
