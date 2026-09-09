# Ops platform: what it shows, what it alerts on, what happens next

Decided 2026-09-08 with Austin. This is the design the rebuild follows. Nothing
here is built yet except the two ledgers noted below.

## The problem that forced this

Nobody keeps intra-month history. Not Rent Manager, and not the warehouse.

`VW_Summary_Rent_Roll` holds exactly two snapshots for Aug–Sep 2026: `2026-08-31`
and `2026-09-05`. `VW_Aged_Receivables` holds 21 monthly snapshots, all month-end
except a handful of scattered partials. So the question "is 60% collections at
J Bar J normal for the 3rd of the month" **cannot be answered from any existing
data**. There is no history of what the 3rd looks like.

That is the whole reason for a snapshot store, and it is why capture starts
before design finishes. Every day we do not capture is a day of baseline that
can never be recovered.

## Where the history lives

**Git is the system of record.** `data/daily_facts.json`, append-only, one row
per community per day.

Not the raw pulls — those are 24MB a day, 8.7GB a year. The derived fact row is
~20 metrics × 64 communities × 365 days ≈ 23,000 rows and about 6MB a year.

Git rather than SharePoint for three reasons. It is already proven for exactly
this: `data/flag_history.json` and `data/source_reconciliation.json` both live
there because the container is reclaimed between runs. It is versioned, which
matters more here than anywhere else in the project, because this store cannot
be rebuilt if a write corrupts it. And there is no auth round-trip mid-run, so a
SharePoint outage cannot silently cost a day.

**SharePoint gets a published CSV copy** so Power Automate, Excel and the
analysts can reach it. Write-through, never read-from. Git is truth, SharePoint
is distribution.

**Retention.** Daily rows for 24 months, then rolled to month-end only.

## Freshness: the capture keys on the snapshot, not the run

Austin's concern, and it is the load-bearing rule of the whole store. The
warehouse models are live queries whose content depends on when the upstream
refresh last ran. A stale feed does not fail. It returns the previous answer
with no indication that it is old.

**This already happened, on the day the store was designed.** On 2026-09-08 the
latest `VW_Aged_Receivables` snapshot was `asOfDate 2026-09-05` and the rent
roll's was the same. Three days behind. The query results said nothing about it;
the staleness only surfaced because the `asOfDate` dimension was queried on a
hunch, and it accounts for a large part of the $513K AR discrepancy in
[SOURCE_CONSOLIDATION.md](SOURCE_CONSOLIDATION.md).

Three rules follow.

**1. Every pull records its own as-of date.** Read the snapshot date in the same
call as the measures and store it beside them. Never infer freshness from the
run date. `compare_sources.py` already does this via `WH_AR_AS_OF` and
`drift_days`.

> **CORRECTION, 2026-09-09.** This rule cannot be satisfied from the warehouse
> as it stands, and the paragraph above overstated what `asOfDate` is.
>
> `VW_Aged_Receivables.asOfDate` is not a snapshot calendar. It is a per-charge
> attribute. Complete portfolio snapshots appear only at month-end and at the
> current live read — 1,001 customers on 2026-07-31, 949 on 2026-08-31, 1,328
> on 2026-09-05 — while every other date in it holds one to sixteen customers.
> Reading it as a snapshot calendar would have filed a $2,669 portfolio for
> 2026-07-11 and a $20,505 one for 2026-09-03.
>
> The other ten models have no snapshot dimension at all. `reportMonth` and
> `endDate` are the period the data *describes*, not when it was captured; they
> read `2026-09` all month while the live figures underneath them change daily.
>
> So the as-of has to be **stamped by whoever ran the pull**
> (`data/warehouse_asof.json`, written by `capture.py stamp <date>`), and
> `capture.py` refuses to append without it. A fact row carrying a guessed date
> is worse than a missing day, because nothing later can tell it from a real
> one. Idempotency is decided by a **content hash** of the normalised rows,
> which is exact and, unlike a date, also catches a restatement inside an
> existing month.
>
> Getting a real refresh timestamp published on the semantic layer is the fix,
> and it belongs on the same list as exposing `dw_prospects`.

**1b. There is twenty months of month-end AR history already in the warehouse.**
`VW_Aged_Receivables` holds complete month-end snapshots back to at least
2025-01. Nobody has been reading them. Consequence: AR is **not** starting from
zero — only its intra-month shape is. Month-over-month and year-over-year on
receivables are available today, without waiting for the capture to accumulate.

**2. The capture is idempotent on the as-of date, not the run date.** One row
per *snapshot*, not one per *run*. If today's pull returns Friday's snapshot,
the store gains nothing and, crucially, invents nothing.

This is the rule that protects the whole platform. Appending a run-dated row
from an unrefreshed feed would fabricate a flat line, and every day-of-month
baseline built on top of it would be quietly wrong while looking perfectly
healthy. A missing day is recoverable. A fabricated day is not, because nothing
downstream can tell it from a real one.

**3. Staleness is itself an alert.** If a source's as-of has not advanced in the
expected interval, that is a flag. The eviction tracker already works this way
(`eviction-tracker-stale`); the rule generalises to every source, warehouse and
SharePoint alike.

`capture.py` stores `drift_days` on every fact row and prints a STALE line above
`STALE_DAYS = 1`. It fired on the first run: the warehouse snapshot was
2026-09-05 against a read of 2026-09-09, four days behind.

Net: a stale feed costs a day of baseline. It never corrupts the history.

### Consequence for prospects

`dw_prospects` is **not exposed to the MCP connector** as of 2026-09-08 — the
schema returns 11 models and none mentions prospects. It exists warehouse-side
but has not been published to the semantic layer, so someone with RentViewer
admin has to surface it before anything can read it.

Once it is exposed, the open question is whether its refresh can be **triggered**
as step zero of the daily routine, or whether we can only read whatever it last
produced. Rule 2 makes us safe either way; triggering it just means we stop
losing days.

## The analytical idea: compare like to like

A raw number is nearly meaningless here and the JBJ question is the proof. 60%
collected is alarming on the 25th and unremarkable on the 3rd. Four
normalisations, in order of how much they matter:

**1. Day of month.** The only honest comparison for anything cash-related is the
same day of month in prior periods. Rent bills on the 1st, is late after the
5th, and the collection curve is steep and non-linear through the first week.
This is the primary axis and the reason the store is daily rather than monthly.

**2. Same-store.** Congress and Shell Pointe are sold; Cambridge and Geiger Key
were removed. Any year-over-year total that includes them compares different
portfolios and will read as growth or decline that is really just composition.
Every trend needs a same-store cut alongside the all-store one, on the set of
communities present in **both** periods. This is not currently done anywhere and
it is the most likely source of a wrong conclusion in the existing dashboard.

**3. Seasonality.** The RV parks are snowbird businesses. August against January
is not a comparison, it is two different products. For anything touching RV,
year-over-year same-month is the only valid read, and month-over-month should
be suppressed rather than shown misleadingly.

**4. Rate versus volume.** A revenue rise is either more lots occupied or more
rent per lot, and the action is completely different. Decompose it rather than
reporting the total.

Plus the two already handled: onboarding months excluded from move trailing
averages, and the financials as-of stamp for GL posting lag.

## Three views, one pipeline

Austin's call: all three, off the same data.

| View | Opens on | Cadence |
|---|---|---|
| **Exception scan** (Austin) | What broke against its own baseline, ranked by dollars. Everything else is a drill-in. | Daily, read in five minutes |
| **Regional manager worklist** | My communities, my overdue items, sorted by what is actionable today | Daily |
| **Founders / board** | Portfolio trend, same-store, budget variance | Monthly |

## Alerts

**What earns one: breaking its own baseline.** A community outside its own
day-of-month range. Self-calibrating, no thresholds to maintain, and a park that
has always run 70% occupancy does not alert forever for being itself.

Deliberately **not** absolute thresholds, and deliberately not the current
behaviour, where every true statement becomes a flag and nothing becomes a task.
The 22 flags on the board today are mostly data-quality findings — real, but they
are IT tickets, not operating decisions. Those stay, in their own tray, separate
from operating alerts.

**Confidence gate.** No alert fires until 60 days of baseline exist for that
community and metric, and every alert is labelled provisional until 12 months
exist. A thin baseline produces confident nonsense.

**Routing: the community mailbox, not a named person.** Austin's call, and
better than the per-manager mapping originally proposed here. It survives
turnover with no roster to maintain, and the manager, the regional and the
director all see the same message land — which buys accountability without a
task system, and removes what was listed below as the project's one blocker.

**The addresses are stored, not derived, and that is the finding.** Austin
supplied the real list from the M365 groups on 2026-09-09 and it follows no rule
the roster can reproduce: `obo@` and `pse@` are initialisms, `triples@` drops a
word, `vantageoak@` is singular where the roster is plural, `GreenPointe@` spells
what the roster calls Greene Pointe, and one mailbox serves both Bay Oaks
villages. A generator would have got several wrong, and a wrong address means
mail about one park landing at another. So the mapping lives in
`pipeline/community_emails.json` as reviewed data; `pipeline/routing.py`
consumes it and reports anything unmatched in either direction.

Reconciled against the M365 group export (`pipeline/manual/m365_groups.csv`),
which supplies group *names* alongside the aliases and so settles every
ambiguity. **61 of 64 live communities routed.** The rest is the interesting
part:

| | |
|---|---|
| Two parks, one inbox | Bay Oaks Village 1 + 2 → `bayoaksvillage@`; Regency 1 + 2 → `Regency@`; Northgate MH + RV → `northgate@` |
| Excluded as sold | Congress, Shell Pointe (`shellpointe@` still exists) |
| Group, no live community | `geigerkey@` — removed from the roster at Austin's direction |
| Deliberately not an option | `regionalmgmt@` — a real mailbox, excluded per Austin. Every community has its own address, so no fallback case remains |

**All 64 live communities route.** Carley's, Hendersons and Nalls Court turned
out to have mailboxes (`carleys@`, `hendersons@`, `nalls@`) that simply were not
in the export.

**One mapping is counterintuitive and must not be "corrected".** The unsuffixed
`whisperingpines@` is the **Florida** park; `whisperingpinesma@` is
Massachusetts. The group names in the export say so explicitly. Swapping them
sends one state's numbers to the other state's team.

**A pending rename, recorded so it is not mistaken for a bug twice.**
`Spacecoastvillage@` looked like a mailbox with no community. It is the
successor: **Silver Breeze is being renamed to Space Coast Village**, and the
address already exists. Routing deliberately stays on `silverbreeze@` until the
rename lands in the Property Data Sheet — sending to the new address before the
team watches it loses the mail, and sending to both duplicates every alert.

When the PDS renames it, three things move together: flip the alias in
`community_emails.json`, delete the `_pending_rename` block, and add the old
spelling to the roster's alias map, because the warehouse and Rent Manager will
both keep saying Silver Breeze long after the PDS changes. That last step is the
one that would otherwise silently drop a community, exactly as the
`Hunter Springs MHC` / `MHP` mismatch did.

Three consequences worth building around. Communities with no mailbox must be
**surfaced, not silently skipped** — an alert with nowhere to go is worse than no
alert because everyone assumes it was sent. Anything mailed to a shared inbox
must **name the community in the subject**, or the recipient cannot tell which
park it concerns. And `shellpointe@` resolving to a park we sold in July is
exactly the bounce the `sold` override exists to prevent.

The remaining tradeoff, stated once: an email has no completion state, so nothing
records whether an alert was acted on. Three people seeing it mitigates that.
If it still bites, ClickUp goes on top later and the payload is unchanged.

## Cross-checks rather than consolidation

The Listings Dashboard and Prospects & Funnel Tracker already publish daily to
SharePoint under `Birdcage/Data Analytics/Claude Cowork/Sales-Marketing/` and,
duplicated, to `main/Sales/Dashboards/`. Austin's call: **leave them alone, read
their data, and compare results to check accuracy.**

That makes them a third reconciliation, the same discipline as
`compare_sources.py`. Where two independently built pipelines agree, confidence
is real. Where they disagree, one of them is wrong and we find out before the
team does.

## Assets come from SharePoint, not the API, and the history already exists

Austin's call, and it is a straight upgrade. A dated `Asset Listing_YYMMDD.csv`
lands in `Birdcage/Data Analytics/Rent Manager/Historical Asset Listing/` every
morning around 08:05. **387 files as of 2026-09-08**, so homes are the one thing
we do not have to start accumulating today — the daily history is already there.

It carries **125 columns against the API's 30**, and the difference is not
padding. The whole home setup sequence is in it, each stage with its own date:
permit submitted and received, demo, footers and pads, spot units, set side and
tie down, interior trim out, water, sewer, electrical and AC connection,
skirting and gutter, steps and deck, **punch out**, certificate of occupancy.

Two consequences.

**It closes an open data note.** The dashboard says there is no punch stage in
Rent Manager, so the home pipeline jumps from rehab straight to ready. There is
a punch stage. `UDF: Punch Out Date` was simply never in the API pull.

**Time-in-stage for homes is answerable now, but not from these columns.** I
overclaimed this on first reading and the correction matters. The stage columns
are free text, not dates: of 1,745 assets on 2026-09-06 only 96 carry a
punch-out value, and of those 80 read `TBD`, 3 read `N/A`, 3 read
`WE 07/07/26` and 9 are an actual date. So the field is a hand-typed planning
cell with mixed conventions, not an event log, and durations cannot be computed
from it.

The route that does work is better anyway: **diff `status` across the 387 daily
snapshots** and observe when each home actually moved. That measures what
happened rather than what someone typed, and it needs no change in data-entry
habits to start working.

Worth keeping the columns regardless. They are the team's forward-looking target
dates, which is a different and useful thing — and `TBD` on 83% of the homes
that have any value at all is itself a finding for whoever owns home setup.

Three hazards before trusting the archive. The schema is **not stable across
dates** — some files carry a different header beginning with property name and
short code rather than the 125-column layout. The alternate layout is **more
widespread than first recorded**: 2026-07-28, 08-13, 08-17, 08-24 and **09-04**
all carry it, so it is not a one-week glitch around mid-August and there is no
safe date range to assume. Read every file's header; never assume column
positions. Column 101 is `UDF: Sewer Connection Date'` with a trailing apostrophe
in the source. And **consecutive files can be byte-identical** — 09-06 and 09-07
are, being a Sunday and Labor Day. That is correct behaviour, not a broken
export, and the slip watcher rightly emits nothing for such a pair. Do not treat
an unchanged file as a failed pull.

**`Financial Property` is the column that matters most and was the one not being
read.** It survives when `Property` is blanked on a superseded record, and it is
what recovered 59 of the 71 unattributed assets. It is now in the canonical map.
See the unattributed section under the throughput tab.

## Prospects

No daily prospect feed exists. Three one-off exports sit on SharePoint and none
of them repeats:

| File | Source | What it has |
|---|---|---|
| `JW Claude_*-1-Prospect Stage Listing.csv` | RM report 676 | Stage, Property, Unit, First Contact, Last Contact, **Stage Date** |
| `DW_Prospect Status Report_*.csv` | warehouse (`DW_` prefix) | ProspectStage, **Days In System**, **Application Days** |
| `Prospects_YYYY_MM_DD.csv` | Zoho CRM | Prospect Owner, Source, Status |

The `DW_` file is the closest match to what Austin described and suggests the
warehouse view he is enabling may be a revival of something that already ran.
Both it and the RM export carry Stage Date or a days-in-stage measure, which is
what the funnel question needs.

Until one of them lands daily, prospect history still has to be accumulated
forward, so prospects stay out of phase one.

**PII.** The RM stage listing carries prospect names and the Zoho export
carries names, email addresses and phone numbers. Any of these gets staged
through the same discipline as the eviction tracker: strip the identifying
columns, keep Property and Unit as the join key, and refuse to write a file
that still contains them. `pipeline/stage_eviction.py` is the pattern.

## No longer blocked on the manager mapping

Routing to the community mailbox removed it. Alerting needs no manager list at
all, and the addresses derive from the roster.

What is still open, smaller than it was:

- **Verify the 64 addresses actually deliver.** The mapping is reconciled against
  the group export, but no mail has been sent to any of them.
- **The regional manager view still needs scoping** — which communities each
  regional covers. But that is one of three views, not the alerting path, and it
  can be deferred without holding anything else up. It is also arguably less
  necessary now: if the regional is on the community distribution, the scoping
  happens in their inbox.
- **`dw_prospects` exposed to the connector.** Still the only thing standing
  between us and the funnel work.

## A note on the Property Data Sheet

The PDS was modified 2026-09-08 at 12:50, after the roster on disk was built on
2026-09-04, so **the roster may be stale**. An attempt to read the sheet on
2026-09-09 came back with truncation markers present and the `vwr VW_PDS_V2`
header could not be located, which is the same hazard that nearly wrecked the
roster on 2026-09-08 — so nothing was concluded from that read, and in
particular whether the PDS carries a community email column is still unknown.

The next refresh must rebuild the roster from the sheet and diff it, per the
runbook. It must not build on the roster on disk without saying it is stale.

## Phase one

1. `daily_facts.json` and the capture step, appending every run. Starts before
   anything else, because the baseline only accumulates forward.
2. The same-store cut, which is a correctness fix to trends already on the page.
3. Day-of-month curves rendered as soon as ~30 days exist, unlabelled and
   without alerts, so the shape can be sanity-checked by eye.
4. Alerts at 60 days, provisional, once the manager mapping exists.

## Pushed dates: the slip watcher

Austin's ask: catch it when a projected date moves later, and flag it so the
question gets asked on the call rather than discovered afterwards.

`pipeline/slip_watch.py` diffs consecutive daily asset snapshots per asset per
date field and appends every movement to `data/date_slips.json`. Twenty date
fields are watched — the three the Cavco and Champion imports write, plus all
fifteen setup stages. Movements are classified rather than lumped: **pushed** (a
real date moved later), **pulled** (earlier), **set** (a projection recorded for
the first time, which is not a slip), **cleared**, and **text** (a placeholder
edited). Only `pushed` reaches the call pack.

The ledger is append-only and committed, so cumulative drift per home
accumulates. A home that has slipped four times is a different conversation from
one that slipped once by the same total, and only a ledger can tell them apart.

**Not a new notification stream.** The output is shaped for the pack the
existing Tuesday 5pm rehab pre-read routine already builds. A second email
nobody asked for is how a good signal gets ignored.

`pipeline/slip_pack.py` renders the ledger as that section and writes
`data/pre_read_slips.md`. The Tuesday routine
(`trig_01MDcyYXyogo9xgQqWAxkTNq`) regenerates it each week rather than reading a
committed copy, because a week-old slip file is exactly the thing this is
supposed to catch.

Three judgements are baked into the renderer, and they are the difference between
a section people act on and a table they skim.

**Bulk moves collapse to one line.** The ten Lucky Clover homes are one decision.
Printed as ten rows they invite ten explanations of a thing that needs one, and
they crowd out the eight single-home pushes underneath. Three or more homes
landing on the same date in the same observation prints as one line with the
range. Two still print individually, because two can be coincidence.

**The observation gap is stated out loud.** A push is dated when we *saw* it, not
when it happened, and the archive has a 31-day hole between 2026-08-03 and
2026-09-03. Saying "20 pushes this week" off that ledger would be flatly wrong.
The header names the real window and flags any gap over three days, so the pack
says "has moved", never "moved on".

**No vendor league table.** See the Champion section below. `Req Delivery Date`
is written only by the Cavco import, so a by-manufacturer breakdown of
requested-delivery slips measures the import, not the vendor. The renderer prints
that caveat rather than the table.

Empty is a real answer and reads as one: with no pushes the section says nothing
moved later *in the window scanned*, which is different from nothing being
checked.

First run over four snapshots (8/3, 9/3, 9/5, 9/6) found 20 pushes, all Cavco,
+2,069 days in total. The headline is not the total, it is the shape: **ten
Lucky Clover homes all re-dated from February and April to 2026-08-24 in one
move**, +132 to +184 days each. Ten homes moving to an identical date on the
same day is a bulk re-order or a data correction, not ten separate delays, and
it is exactly the kind of thing that needs a sentence of explanation rather than
a chart.

Note the parser accepts what people actually type, including a `WE ` week-ending
prefix, and treats `TBD`, `N/A` and blanks as "no projection yet" rather than as
dates. A projection appearing for the first time is never counted as a slip.

## Rehab and demo pace: the throughput tab

Austin's requirement: the `Vacant, not leasable` tile should open a view
answering whether we are on pace to rehab homes and get them occupied, and get
demos infilled with new homes and sold, to meet occupancy goals.

That is a flow question, not a count question, and the daily archive answers it.

### Assets carry three kinds of community, not two

Austin's correction, and it moved the numbers materially. The asset listing
deliberately keeps disposed and inactive records so sales can still be tracked.
Filtering them out erases real history; counting them inflates every
current-inventory figure. So `classify_community()` in `sources.py` splits three
ways:

| Scope | Rows | What it is | Counts toward |
|---|---|---|---|
| `current` | 1,526 | live reportable community | piles and pace |
| `historical` | 207 | `x`-prefixed retired duplicate of a live park, or a disposed community. Mostly Sold. | sales history only |
| `unattributed` | 12 | `UNASSIGNED` with no `Financial Property` either | nothing, and flagged |

The `x` prefix is Rent Manager's retired-record marker, and ten of them shadow
communities that are still live — `xLake Wales MHC`, `xBay Oaks Village I` and
`II`, `xOrmond Beach Oasis`, `xPalm Spring Estates`, `xGulf Breeze MHP`,
`xWolf Bay`, `xOceanaire MHC`, `xWestwood MHP`, `xTown & Country MHC`. Their
assets are the sales history of parks we still own.

The alias pass earns its keep too: **`Hunter Springs MHC` in the asset file
against `Hunter Springs MHP` in the roster** was silently dropping seven live
assets over a three-letter suffix. That is the class of bug this whole exercise
exists to catch.

### The 71 unattributed were not orphans, and 59 of them are now attributed

Resolved 2026-09-09, and it moved the demo pile.

`Property` read `UNASSIGNED` on 71 assets, 45 of them To Be Demoed. They were
counted nowhere. The reading that they are a data-entry backlog was wrong on
both halves: the community was never missing, and the homes are not idle.

**The community is in the file already.** `Financial Property` is populated on
all 45 demos and names the park. That is a column the export has always carried
and the canonical map simply did not read. It is now mapped, and `normalise()`
falls back to it when `Property` classifies as unattributed.

It is a read, not a guess, and it was checked before being trusted. 41 of the 45
also carry a `-vN` sibling record, and the recovered park matches the sibling's
park 41 times out of 41, zero disagreements. Every recovered row carries
`community_source: financial_property`, so a recovered row can never be mistaken
for a clean one, and the underlying `Property` value is still wrong in Rent
Manager whether or not this pipeline works around it.

**The homes are mid-swap, not stalled.** 41 of the 45 have a sibling replacement
home already Ordered, Delivered or For Sale. `-v1` is the outgoing home, carrying
a purchase price around $5K; the base record is its ~$50K Cavco replacement. Rent
Manager blanks `Property` when a record is superseded, which is exactly why these
fell out.

So the demo pile is not one number, and reporting it as one is the mistake:

| | Homes | What it is |
|---|---|---|
| Attributed, no replacement | 87 | bare lots, nothing coming. **This is the 52-month backlog.** |
| Attributed, replacement in flight | 4 | mid-swap |
| Recovered, replacement in flight | 41 | mid-swap, previously invisible |
| Recovered, no replacement | 4 | bare lots, previously invisible |
| **Current To Be Demoed** | **136** | was reported as 91 |

Only 87 of the 91 previously reported demos were stalled lots. Adding the
recovered 45 raises the pile to 136 but does *not* raise the backlog: 41 of the
45 already have a home on the way. The pace figure has to be recut against the
91 lots with nothing coming, not against 136.

**Vantage Oaks is 20 of the 45**, against 32 Delivered and 11 Ordered in the same
park. One community running a large infill program had its entire demo leg
invisible. That concentration says the blanking follows a workflow, so it will
keep happening until whoever runs that program is told.

12 assets are still unattributed. All 12 are `Sold` with no `Financial Property`
at all — Twin Lakes, Fort Lauderdale, a few bare unit numbers. Old sales history
for parks we do not own. Correctly counted nowhere, and not worth chasing.

### The corrected numbers

Scoped to `current`, transitions only, 2026-08-03 to 2026-09-06:

| Stage | Pile | In | Out | Net/mo | |
|---|---|---|---|---|---|
| Needs Rehab | 147 | 17 | 11 | **+5.3** | backlog growing |
| To Be Demoed | 136 | 4 | 6 | −1.8 | see below; only 91 of these are stalled |
| Ordered | 69 | 5 | 30 | −22.1 | draining into delivery |
| Delivered | 104 | 30 | 17 | +11.5 | |
| For Sale | 128 | 29 | 9 | **+17.6** | the bottleneck |

```
Ordered   -> Delivered   26.5/mo
Delivered -> For Sale    15.0/mo
For Sale  -> Sold         4.4/mo
For Sale  -> Rental       3.5/mo
```

**The constraint is disposition, not supply.** 128 homes for sale clearing at
7.9 a month is **16 months of inventory**. Delivery is not the problem — Cavco's
median slip is zero days and 26.5 homes a month arrive. Homes pile up after they
are ready.

The demo pile is the quiet one, and it got quieter once the unattributed 45 were
recovered. 136 homes carry the To Be Demoed status, but 45 of them already have a
replacement ordered or delivered. The pile that is genuinely stuck is the **91
lots with no home coming**, clearing at under 2 a month. Every one is a lot
carrying no rent, and at that pace it is decades, not months.

### What the tab has to say out loud

**The piles will not match the tile.** The tile reads 393 (199 rehab, 194 demo)
because it counts *lots* inside the 64 reportable communities. The asset listing
counts *homes*, and after scoping, 147 rehab and 91 demo. Both are right. The
view must name which it is showing rather than letting two numbers disagree in
silence.

**Never blend transitions with new records.** 25 new `current` asset records
appeared between the two snapshots and 196 new `historical` ones — the latter
almost certainly a backfill of sold homes rather than 196 events. Transition
rates are the headline; record creation is a separate line.

## Actual completion dates are coming from FastField

Recorded so nobody proposes the wrong fix later. The fifteen setup stages hold
*projections* from Cavco and Champion. The matching *actuals* — when the crew
finished each step — are coming from FastField forms feeding the Quickbase
project, which is moving slowly.

So: do **not** propose adding actual-date fields to Rent Manager. The capture is
already designed elsewhere. What this platform does in the meantime is derive
what it can from status transitions, and hold a slot for the real actuals: a
`asset_actuals` dataset in `sources.json` with a Quickbase provider, disabled
until it exists. Same switch as every other source.

## Champion cannot be compared to Cavco, because they do not do the same job

The open question was why all 62 homes carrying both a requested and an actual
delivery date are Cavco, and zero are Champion — read at the time as half the
supply having no measurable delivery performance. Checked against
`Asset Listing_260907.csv` on 2026-09-09. The premise does not hold, in three
separate ways.

**Champion Construction is the site-prep contractor, not a home manufacturer.**
Its customer report feeds the set-and-prep tracker and the `champion-import`
skill writes eighteen fields, all of them setup stages: permits, demo, footers,
spot, set and tie down, trim out, utilities, skirting, steps, punch out,
certificate of occupancy. Not one is a delivery date. The report *has* a Delivery
column and the skill explicitly does not import it. Champion Construction never
delivers a home; it preps the lot and sets what arrives. Measuring its delivery
slip is a category error.

**`Req Delivery Date` is a Cavco-only field by construction.** The `cavco-import`
skill writes exactly three fields — Online, Offline and Req Delivery Date, the
last from Cavco's "Req to Ship" column. Nothing else in the stack writes it. So
all 62 populated rows are Cavco not because Cavco is better documented but
because Cavco is the only source of the field. **Cavco's median slip of zero days
is Cavco measured against itself.** It is not evidence that Cavco outperforms
anyone, and it must not be presented on the call as though it were.

**Champion is not half the supply. It is 2%.** Of 316 homes in the live pipeline
(Ordered, Delivered, For Sale): Cavco 180, Skyline 30, Champion 6. Across the
whole 1,745-row file Champion appears 29 times, mostly as the maker of old rental
stock that came with an acquisition.

### Skyline is the real measurement gap

The manufacturer actually missing from delivery performance is **Skyline: 30
homes in the pipeline, 29 with an actual delivery date, zero with a requested
one.** There is no Skyline import. Nobody writes its commitment date, so there is
nothing to measure a slip against — 27 of those 30 are already For Sale, at
Southgate, Vantage Oaks and Palm Haven Estates.

That is a genuinely open question and it is small enough to fix: one import, one
field, the same shape as the Cavco one.

### Checked against the vendor reports themselves, 2026-09-09

Austin supplied both raw vendor files. They confirm who does what and **correct
one thing this section originally implied.**

Champion's report is a construction schedule keyed by lot, not by home: BT#,
community, lot, permits, demo, footers, spot, set and tie down, trim out,
utilities and their inspections, punch out, certificate of occupancy, project
completion. No manufacturer, no model, no serial, no order number. Champion
Construction is a contractor. That much holds.

**But the report does carry delivery, and the earlier reading that there was
nothing to get from it was wrong.** Column R on the FL sheet is `Delivery`, and
**108 of 256 lots have a real date in it.** The `champion-import` skill drops
that column deliberately. So the question is not whether Champion has delivery
data. It is which half of it matters.

| | Lots | Already in Rent Manager |
|---|---|---|
| Champion `Delivery`, on or before the snapshot (actuals) | 89 | mostly yes |
| Champion `Delivery`, after the snapshot (forward schedule) | 19 | no |

Matching Champion's 108 to Rent Manager on community and lot: 73 match, and of
those **55 already carry a delivery date and 18 do not**. Split the 18 by
whether the date has passed and the picture is specific:

- **2 are missing actuals.** Small, and worth a manual fix.
- **16 are forward delivery commitments that exist nowhere in Rent Manager.**
  Seventeen of the eighteen are Cavco-built homes sitting in `Ordered` status
  with a booked delivery week on Champion's schedule — Vantage Oaks 38, 39, 46,
  70, 96, 97, 102, 103, 31C, 31D; Lucky Clover 5, 47, 64, 105; Windward Knoll 16
  and 62.

**Cavco's actuals are landing, by hand.** Its sheet carries `Req to Ship` and
`Shipped`; 98 lines have a real `Shipped` date, 82 match an RM asset, and 81 of
those 82 already have the delivery date. The `cavco-import` skill treats Home
Delivery as audit-only and never imports it, so somebody is keying those off the
audit workbook every cycle. The process works. It is just manual, and it only
covers Cavco.

### So the real gap is a forward commitment nobody records

This is the part that matters for the slip watcher. Those 16 homes cannot slip in
our data, because their delivery week was never written down. A date that is not
recorded cannot be seen to move, and this is exactly the signal the watcher
exists to catch. 39 of the 108 use the `WE ` week-ending convention, which the
parser already accepts.

Two data notes from the same pass. Riverwalk lots 10 and 69 (BT#3817, BT#3819)
both read `2029-06-09`, three years out and almost certainly meant to be 2026.
And **the `champion-import` skill is out of date against this file**: it expects
one sheet named `Parakeet` with headers in row 2, while the report now ships two
region sheets — `REG 621-FL Parakeet - Report` with headers on row 5 and a
repeated header block per community, and `REG 645 -SC, GA, AL-Report` with 57
lots in a region the skill has never seen. Run it as written and it either fails
or silently reads the wrong rows.

### What this means for the call

Still do not ask Mark Doucette about delivery slip in the sense of "why was this
home late" — Champion does not deliver. Do ask why sixteen booked delivery weeks
live only on his spreadsheet. Champion's own measurable work is the fifteen setup
stages, and of 1,745 assets only **50 carry a single real setup-stage date**.
That is a data-capture conversation before it is a performance one. The actuals
are coming from FastField; until they land, status transitions are the only
observed measure.

One more consequence for the throughput tab: seventeen Cavco homes read `Ordered`
in Rent Manager while Champion has their delivery booked. The `Ordered` pile is
overstated and `Delivered` understated by up to that much, so the
Ordered-to-Delivered rate is measuring paperwork lag as well as real flow.

Restated plainly: **there is one measured manufacturer, one unmeasured
manufacturer, and one contractor who was never a manufacturer.**
