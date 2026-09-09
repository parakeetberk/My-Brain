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
| No mailbox at all | **Carley's, Hendersons MHC, Nalls Court MHC** |
| Two parks, one inbox | Bay Oaks Village 1 + 2 → `bayoaksvillage@`; Regency 1 + 2 → `Regency@`; Northgate MH + RV → `northgate@` |
| Excluded as sold | Congress, Shell Pointe (`shellpointe@` still exists) |
| Group, no live community | `Spacecoastvillage@` ("Space Coast Village"), `geigerkey@` |
| Not in the group export | `regionalmgmt@` — appeared in the pasted list but is absent from the CSV, so a shared mailbox rather than a group. Not a park; the natural escalation target |

**One mapping is counterintuitive and must not be "corrected".** The unsuffixed
`whisperingpines@` is the **Florida** park; `whisperingpinesma@` is
Massachusetts. The group names in the export say so explicitly. Swapping them
sends one state's numbers to the other state's team.

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

Two hazards before trusting the archive. The schema is **not stable across
dates** — files around 2026-08-13 to 08-17 and 08-31 carry a different header
beginning with property name and short code rather than the 125-column layout.
Read every file's header; never assume column positions. And column 101 is
`UDF: Sewer Connection Date'` with a trailing apostrophe in the source.

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

- **Three communities need a mailbox**, or a decision to route them elsewhere:
  Carley's, Hendersons MHC, Nalls Court MHC.
- **`Spacecoastvillage@` needs explaining** — a mailbox with no community, which
  is either a park we do not report on, a rename, or a leftover.
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
| `current` | 1,468 | live reportable community | piles and pace |
| `historical` | 205 | `x`-prefixed retired duplicate of a live park, or a disposed community. 98 Sold. | sales history only |
| `unattributed` | 71 | `UNASSIGNED` or a name nothing matches | nothing, and flagged |

The `x` prefix is Rent Manager's retired-record marker, and ten of them shadow
communities that are still live — `xLake Wales MHC`, `xBay Oaks Village I` and
`II`, `xOrmond Beach Oasis`, `xPalm Spring Estates`, `xGulf Breeze MHP`,
`xWolf Bay`, `xOceanaire MHC`, `xWestwood MHP`, `xTown & Country MHC`. Their
assets are the sales history of parks we still own.

The alias pass earns its keep too: **`Hunter Springs MHC` in the asset file
against `Hunter Springs MHP` in the roster** was silently dropping seven live
assets over a three-letter suffix. That is the class of bug this whole exercise
exists to catch.

**71 unattributed assets, 45 of them marked To Be Demoed with no community at
all.** Counted nowhere by design. That is a data-entry problem worth a flag, not
a pile worth reporting.

### The corrected numbers

Scoped to `current`, transitions only, 2026-08-03 to 2026-09-06:

| Stage | Pile | In | Out | Net/mo | |
|---|---|---|---|---|---|
| Needs Rehab | 147 | 17 | 11 | **+5.3** | backlog growing |
| To Be Demoed | 91 | 4 | 6 | −1.8 | 52 months to clear |
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

The demo pile is the quiet one: 91 units clearing at under 2 a month is 52
months, and every one is a lot carrying no rent.

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
