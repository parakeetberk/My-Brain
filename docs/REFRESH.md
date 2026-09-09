# The refresh: what runs, in what order, and what "done" means

This is the operating definition the schedule executes. If a step is not written
down here it does not run, and if it is written down here it runs every time.

Austin's requirement, in his words: *get everything in one place and make it run
without me.* Two constraints fall out of that and shape everything below.

**Nobody is watching.** The refresh fires into a session with no human in it. So
every step either succeeds, or fails loudly and stops — it never half-writes.
There is no "ask the user" branch at 7am.

**The container is thrown away.** Nothing survives a run except what is committed
and pushed. Files written to disk and not committed are gone.

## Cadence

| | when | why that |
|---|---|---|
| **Daily refresh** | weekdays 07:00 ET (`0 11 * * 1-5`) | the asset listing lands ~08:05 ET, the warehouse refresh is irregular — see below |
| **Tuesday pre-read** | Tuesdays 17:00 ET (`0 21 * * 2`) | ahead of the Wednesday calls, late enough that Tuesday's one-on-ones are done |

**The daily job runs daily even though the warehouse does not refresh daily.**
That looks wasteful and is not. The warehouse's refresh cadence is irregular and
unannounced — on 2026-09-09 the newest data was from 2026-09-05, four days
behind — and `capture.py` decides whether anything moved by hashing the rows, not
by trusting the calendar. An unrefreshed source appends nothing. So running daily
costs one wasted pull and guarantees we never miss the day it does refresh. The
alternative, guessing the cadence, loses baseline permanently every time the
guess is wrong.

The 07:00 slot is before the asset listing lands at 08:05. That is deliberate for
now: the asset archive keeps every day's file in SharePoint, so a missed day is
recoverable from history, whereas the warehouse is not. Move the slot to 08:30 ET
once the routine is proven, and the asset step stops running a day behind.

## What runs, in order

Each step lists its gate — the condition that stops the run rather than
proceeding on bad data.

**1. Pull.** `sources.py build` walks each dataset's provider list and writes
`pipeline/raw/*.json` with the provider and as-of recorded. Warehouse queries come
from `pipeline/queries.json`, sent in measure batches of two or three because
every one of them times out at 60s with its full list, and joined by
`merge_pull.py`.
*Gate:* a part that disagrees with its siblings on row count or key set is
refused, not merged. A silent mismatch files a measure against the wrong
property-month and nothing downstream would catch it.

**2. Stamp the as-of.** `capture.py stamp <date>` records when the warehouse data
was actually current. This cannot be derived — see [PLATFORM_SPEC](PLATFORM_SPEC.md)
— so the pull step has to state it.
*Gate:* `capture.py` refuses to append without it. A fact row with a guessed date
is worse than a missing day, because nothing later can tell it from a real one.

**3. Build.** `build.py` emits `data/dashboard.json`: the reportable gate from the
Property Data Sheet, alias and roll-up resolution, the two-period model, flags.
*Gate:* build dies on a missing roster, an empty pull, or a reportable community
with no warehouse data.

**4. Capture.** `capture.py run` appends one row per community per snapshot to
`data/daily_facts.json`, per family, idempotent on the content hash.
*Gate:* a family whose hash is unchanged appends nothing. That is a correct
outcome and not a failure — do not "fix" it by forcing a write.

**5. Assets.** Fetch the day's `Asset Listing_YYMMDD.csv`, fold it via
`backfill.py fold`, then `backfill.py finish` to rewrite `data/asset_facts.json`,
`data/date_slips.json` and the committed snapshot store.
*Gate:* the shape guard. Three files in that folder are a different report wearing
the same filename; folding one would read as 1,600 assets vanishing and returning.
Refuse and record, never normalise into something plausible.

**6. Publish.** Republish the artifact from `data/dashboard.json`.
*Gate:* never publish a stale or partial payload. The team reads that page as
fact. If any step above failed, the previous version stands.

**7. Commit and push.** Everything under `data/` plus any refused-file records.
*Gate:* this is not optional. An unpushed run is a run that did not happen.

## The Tuesday pre-read

Same pull, then the call pack: `date_slips.json`'s revised projections and
late-entered actuals, the disposition funnel, the rehab and demo pace, and the
per-community items routed to the community mailbox rather than to a named
manager, so the manager, regional and director all see it and turnover does not
break the workflow.

Materiality rules live in `backfill.py` and exist because the raw output is mostly
noise: a push under three days is a weekly re-baseline, several assets moving the
same field to the same value on the same day is one edit and one question, and a
new date already in the past is an actual being recorded rather than a schedule
slip. Ninety-three raw pushes came to one projection worth raising.

## Failure posture

- **A source is stale.** Not a failure. Capture appends nothing, `drift_days` is
  recorded, and a STALE line prints above one day of drift.
- **A source is missing.** That family is skipped, the others still run. Families
  are grouped by source cube precisely so a stale AR feed cannot block occupancy.
- **A build gate fires.** Stop. Do not publish, do not capture. The previous
  dashboard stands and is correct as of its own timestamp.
- **A pull is truncated.** Treat as a failed run. A limit-capped pull once read
  $588K of portfolio AR against a true $1.41M, and nothing looked wrong.

## Open, and blocking nothing

- `dw_prospects` is not on the MCP connector. The prospect dataset reads a
  manually refreshed CSV until it is, and flipping over is a config flag in
  `sources.json`, not a rebuild.
- No warehouse model publishes a refresh timestamp. Until one does, step 2 is
  manual. Same ask, same person as `dw_prospects`.
- The daily slot is 07:00 ET, an hour before the asset listing lands. Move to
  08:30 once the routine has proven itself.
