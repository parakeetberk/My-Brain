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

**Routing: email to the regional manager.** Austin's call over a ClickUp task.
The tradeoff, stated once: an email has no completion state, so nothing will
record whether an alert was acted on. If that becomes a problem the fix is to
add ClickUp later; the alert payload is the same either way.

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

**Time-in-stage for homes is answerable now.** Fifteen dated stages across
months of daily files means we can compute how long each home sat at each step,
and what normal looks like, without waiting for a baseline to accumulate. That
is the analysis Austin wanted for prospects, available immediately for homes.

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

## Blocked on one thing

**The regional manager mapping is empty.** `pipeline/regional_managers.json` has
zero managers and zero email addresses, and the Property Data Sheet has 41
columns and no manager field.

Two of the four decisions above depend on it: the regional manager worklist has
no way to scope itself, and email routing has no addresses to send to. It is a
64-row spreadsheet — community, manager name, email — and it unblocks both.

Nothing else in phase one is blocked.

## Phase one

1. `daily_facts.json` and the capture step, appending every run. Starts before
   anything else, because the baseline only accumulates forward.
2. The same-store cut, which is a correctness fix to trends already on the page.
3. Day-of-month curves rendered as soon as ~30 days exist, unlabelled and
   without alerts, so the shape can be sanity-checked by eye.
4. Alerts at 60 days, provisional, once the manager mapping exists.
