# Property Operations Dashboard — how it works

The dashboard the team opens is a private Claude Artifact at a stable URL. This
repo is the source of truth for the code that builds it and the data it shows.

```
RentViewer warehouse (Rent Manager)
        │  6 queries, declared in pipeline/queries.json
        ▼
pipeline/raw/*.json          raw query results, committed so every build is reproducible
        │  pipeline/build.py  — registry, rollups, exclusions, trends, flags
        ▼
data/dashboard.json          the payload the UI reads (+ registry_audit.json)
        │  pipeline/publish.py — inlines CSS + JS + logo + data
        ▼
build/parakeet_ops_dashboard.html   one self-contained file
        │  Artifact tool, same URL every time
        ▼
Live dashboard for the team
```

## Why the live URL is an Artifact, not GitHub Pages

`parakeetberk/My-Brain` is a **private** repo on a personal account. GitHub Pages
for a private repo needs GitHub Enterprise Cloud; on this plan the only way to
get a Pages URL is to make the repo public. This dashboard carries per-community
receivables, delinquency and NOI, so publishing it to a public URL is not an
option. A Claude Artifact is private by default and shareable with named people,
which is the right fit.

The Pages route stays available if Parakeet ever moves this to an Enterprise org:
`dashboard/index.html` already fetches `data/dashboard.json` at runtime and
refreshes every 15 minutes, so it works as a static site with no changes.

## Why the refresh runs through Claude, not GitHub Actions

The warehouse is only reachable through an authenticated MCP connector held by
Austin's Claude account. There is no API key this repo could hold, so a plain
cron job in Actions has nothing to call. The refresh therefore runs as a
**scheduled Claude session** that has the connector, executes the queries, runs
the build, commits, and republishes the artifact.

If Parakeet later provisions direct REST credentials for the warehouse, the only
piece that changes is how `pipeline/raw/*.json` gets written — `build.py` and
everything downstream stays as is.

## The scheduled refresh

A Claude Routine, `Ops dashboard refresh (weekday 7am ET)`
(`trig_01CAF7XT9fnnH67xFe2JBS1D`), fires weekdays at 11:00 UTC / 7am ET, ahead
of Austin's 9am meeting floor. It re-runs the six queries, re-reads the PDS
roster and the eviction tracker, rebuilds, republishes to the same artifact URL,
and pushes to this branch.

It is bound to the session that built the dashboard rather than spawning a fresh
one, because the warehouse connector lives on that session. The trigger record
itself stores no connector grant, so if a run ever reports the
`mcp__RentViewer_Data_Warehouse__run_query` tool as missing, attach the
RentViewer connector to the Routine in claude.ai Routines settings.

The eviction tracker is the one source that genuinely changes daily, and it is
the reason a weekday cadence earns its keep. If the export stops landing, the
in-eviction bucket silently drains into needs-action, so `build.py` raises a
flag once the tracker's as-of date is more than two days old rather than
reporting a quietly wrong split.

The warehouse is a monthly snapshot, so a weekday cadence is not about the
closed-month figures changing daily. It keeps the open-month reading current,
catches newly onboarded properties in the registry audit, and means the numbers
are already fresh at the Friday 2pm EOS call and the Monday Jon catch-up.

Every run reports what moved and re-reads the flags. A run that cannot reach the
warehouse stops rather than republishing a stale payload to the live URL.

## Sending it to someone who is not in this session

Two routes, and they answer different questions.

**A file, for anyone.** `python3 pipeline/publish.py --standalone` writes
`build/Parakeet_Ops_Dashboard.html`, a complete document with React inlined from
`dashboard/vendor/` and the web font dropped in favour of the brand's Calibri
fallback. It opens by double-click in any browser with **no account, no login
and no network at all** — verified with every external request blocked. About
2MB, so it emails fine. This is the route to use when you are not sure what the
recipient has.

The published Artifact deliberately keeps the pinned cdnjs script tags instead:
cdnjs is on the Artifact CSP allowlist, and leaving React external keeps the
page smaller. Both builds come from the same `app.js` and the same payload.

**The Artifact URL,** for anyone inside the Claude workspace. Private by
default; sharing is done from the share menu on the page itself, which is a UI
action rather than something the pipeline can do. It has the advantage of
updating itself every weekday refresh, where a mailed file is a snapshot.

Note that this session cannot mail it for you. The Microsoft 365 connector is
read-only here: `Mail.ReadWrite` and `People.Read` are not admin-consented on
the app registration, so drafting an email or looking someone up in the
directory both return 403. Reading mail and SharePoint works.

## Running it by hand

```bash
# 1. refresh pipeline/raw/*.json  (warehouse connector, the PDS roster and the
#    eviction tracker from SharePoint; all specified in pipeline/queries.json)

# 1b. the tracker is a CSV and must go through the staging script, which strips
#     resident names and case numbers. Never hand-write pipeline/raw/eviction_tracker.json.
python3 pipeline/stage_eviction.py <the-downloaded-csv>

# 2. build the payload
python3 pipeline/build.py

# 3. assemble the page for the Artifact
python3 pipeline/publish.py

# 3b. or a self-contained file to send to someone
python3 pipeline/publish.py --standalone

# 4. local preview — must be served over HTTP, not opened as a file://
python3 -m http.server 8000    # then open http://localhost:8000/dashboard/
```

`build.py` prints a portfolio summary and every data-quality flag it raised.
Read those before shipping a refresh.

## The two-period model

Every period-sensitive figure is built twice, and the dashboard has a toggle in
the masthead to switch between them. Both are real; neither is hidden.

| | **Closed** | **Live** |
|---|---|---|
| Period | Last completed month | Current month through today |
| Use it for | Comparing like with like, trends, board numbers | What is actually owed right now |
| Occupancy | 80.0% (Aug) | 79.8% (Sep 4) |
| Receivables | $928K | $2.09M |
| Past due 30+ | $711K | $800K |
| Collections | 99.2% for the full month | 44.5% month to date |

The warehouse reloads a full snapshot each month, so the open month is partial.
Rent bills on the 1st, which means an open-month snapshot carries a full month of
fresh charges against only a few days of collection. That makes the live
collection *rate* structurally low and not comparable to a closed month, but it
does **not** make live receivables wrong: past the grace day (`grace_day` in
registry.json, currently the 5th) that money is late, and the live view is the
actionable one. It is what the collections team should be working from.

Consequences that are wired in rather than left to the reader:

- The toggle **defaults to Live once the month is past the grace day**, and to
  Closed before it. Opening the page on the 12th shows what is late.
- **Charts always show the full history including the open month**, drawn as a
  dashed hop to a hollow marker (`○` on the axis). The y-scale comes from closed
  months only, because a live receivables reading roughly doubles the axis and
  would flatten twenty months of history. A live bar that exceeds the scale is
  capped with a break mark and labelled with its true total.
- **`Past due 30+` is a headline tile in both modes.** Everything outside the
  0–30 bucket, which is the number that survives the month-start distortion.
- **Financials always read the closed month**, in both modes. The general ledger
  does not post intra-month, so a live NOI would read as a collapse to zero. The
  tab and the NOI tile both say so.
- Live collection rates are **not colour-banded** against the full-month
  threshold. A 44% month-to-date rate on day 4 is not a red flag.

## Two data sources, and why

The warehouse tops out at **property grain**. Adding `unitName` or
`glAccountName` as a dimension times out at 60 seconds even scoped to a single
property, so unit-level and account-level detail cannot come from there.

Rent Manager report exports fill that gap:

| Need | Source | Why |
|---|---|---|
| Portfolio and per-community aggregates, all trends | Warehouse, 6 queries | Fast and consistent at property grain |
| Expense and income categories | Warehouse, 2 queries | Pre-aggregated measures, property grain |
| Per-unit rent roll and vacant unit names | RM `SummaryRentRoll` (69) | The only source with unit rows |
| Accounts owing, by aging bucket | RM `AgedReceivables` (78) detail | Charge-level, collapsed to one row per account |

Resident names come back **redacted** by the RM connector, so a unit number
plus an account id is the whole identity in the drill-ins.

Several RM reports are simply broken server-side and return HTTP 500 for every
parameter combination, including with no parameters and scoped to one property:
`Vacancy` (74), `RentRoll` (67), `UnitAvailability` (10), `UnitTypeVacancy` (75)
and `UnitList` (6). Do not spend time on them; `SummaryRentRoll` carries the
same fields.

The two systems also name properties differently. The rent roll carries
`EntitiesName` plus `EntitiesEntityID`; aged receivables carries
`EntitiesShortName`. `rm_community()` resolves on any of the three rather than
betting on one.

### Vacancy: counts from one source, names from the other

**The warehouse owns the vacant counts. Rent Manager only supplies the names.**

This is not arbitrary. RM computes vacancy loss only where a market rent is set,
so Great Oak — an RV resort that bills transient stays rather than recurring lot
rent — reported 2 vacant sites against an actual 74. The warehouse computes
vacancy from unit-days and reconciles to portfolio occupancy, so it counts;
RM names.

The two will never tie exactly, and the page says so rather than implying
otherwise. The count is unit-day weighted, so a lot empty for half the month
counts as half. The named list is units with no active lease **today**. Roughly
1,313 counted against 1,820 named, and the Vacancy tab carries a `Units listed`
column so a community where RM can name few of them is visible.

Vacancy reasons are mapped in `registry.json` under `vacancy_reasons`, across
**both** vocabularies: the warehouse uses `POH-Need Rehab` and `SFH`, while the
RM rent roll uses `Single Wide`, `Double Wide`, `Park Model`. Anything unmapped
falls to "vacant lot" and is named in a flag.

## Natalie's review, and what each ask needed

| Ask | Delivered | Source |
|---|---|---|
| Vacancy aging | Yes, for 30% of vacant units | `MoveInMoveOut` (77) — days since last move-out |
| Move-ins/outs and net occupancy by property | Yes | Warehouse moves, already held |
| 90+ AR split by eviction / former / plan / action | Yes, three of four | Eviction Tracker `CurrentStage` |
| Utility metered vs flat and by type | Yes | PDS utility columns |
| Ready to Market / rehab visibility | Yes, no punch stage | `AssetListing` (244) status + `udf_551` |

Austin closed the two open ones on 2026-09-04: Ready to Market is a UDF on the
Asset Listing, and the Eviction Tracker is a scripted report that also lands in
SharePoint daily. Both are now wired in. What remains incomplete is narrower
and named below.

**Vacancy aging** is anchored on a unit's last move-out, because an asset's
service start date is when it entered the fleet, not when it went empty. The
move history pulled starts January 2025, so a lot empty longer than that has no
anchor and shows as Unknown — 1,269 of 1,820 named units. The 551 that do
resolve tell a sharp story: 322 empty more than 90 days, 113 more than a year.
Pulling move history further back closes the gap.

**AR segmentation** now comes from the eviction tracker rather than from
guessing at charge names, and the buckets are real:

| Bucket | Accounts past due 30+ | Amount | How it is determined |
|---|---|---|---|
| In eviction | 50 | $169K | An open case on the unit in the tracker |
| Former resident | 17 | $27K | Lease ended in the move history, or a closed case with money left |
| On a payment plan | 0 | — | A payment plan charge type on the ledger |
| Needs action | 176 | $258K | None of the above — somebody has to call |

Note what the bar counts: accounts carrying something **30 days old**, not every
account with a balance. Rent bills on the 1st, so on day four of a month all
1,427 accounts with a balance would read as a portfolio in crisis. Only 243 are
actually behind.

Two caveats stay on the page. **Payment plans** are still detected by charge
name, and one account portfolio-wide is almost certainly under the truth — most
plans are agreed by email and never posted as a charge, so those read as needing
action. **Former resident** needs a lease the move history shows ended, and that
history only reaches back to January 2025; a closed eviction case recovers some,
but an account that moved out earlier still reads as needing action.

The tracker also surfaced something nobody was looking at: **15 cases have been
open more than a year**, the oldest 1,156 days. Seven of them sit at Declaratory
Judgement owing nothing, which reads like matters that resolved and were never
closed out rather than three-year evictions. Either way they inflate the funnel
until someone sets a close date, so that is a flag.

**Ready to Market** is `udf_551` on the Asset Listing — a user-defined field,
not a status, which is why a home can read For Sale and not-ready at the same
time. The field was identified by profiling every Yes/No UDF against
`AssetStatusesName`: `udf_551` Yes appears only against For Sale (111) and
Delivered (2) and never against Ordered, Needs Rehab or Rental, which is exactly
how an RTM flag behaves. `udf_325` looks similar at a glance and is **not** it —
its Yes spreads across Rental, Needs Rehab and Rent to Own alike.

That gives a real pipeline: 72 ordered, 99 awaiting setup, 147 in rehab, 110
listed and ready, 2 ready but not listed, 63 to demo, 18 with no status set. And
it exposes the gap the flag exists to find: **19 homes read For Sale without
Ready to Market set** — either not actually showable, or nobody flipped the flag.

**There is still no punch stage.** No punch status and no punch field exist on
the Asset Listing, so the funnel runs rehab straight to Ready to Market with
nothing in between. Someone has to add it before it can be reported. The panel
says so.

### Utility recapture, reframed

The headline rate alone was the wrong question. The PDS carries Water Service,
Water Paid By, Sewer Service, Sewer Paid By and Trash Paid By, and **16 of 64
communities pay their own utilities** — a low rate there is the design, not a
failure. Banding them red was misleading.

The Financials tab now separates the two. Across the 48 communities that do bill
residents the rate is 51%, and the table sorts by dollars absorbed so the
genuine failures surface: River Oaks, Paradise Lakes and Fox Creek each bill a
resident-paid utility and recover **$0** against $10K to $16K of monthly spend.
Communities that pay their own are shown greyed and unbanded.

### Resident names are stripped at ingest

`MoveInMoveOut` returns `AccountsFirstName` and `AccountsLastName` unredacted,
unlike the other reports. `pipeline/raw/rm_moves_detail.json` is written with
those and the street address removed before anything downstream reads it,
because the standalone build of this dashboard gets emailed around. Unit number
plus account id is the whole identity anywhere in the payload.

The Eviction Tracker arrives with names too, and worse: a `FullName` column and
a `CaseNumber`. `pipeline/stage_eviction.py` drops both before anything reads
the file. The name is obvious; the case number is a public court filing, but
printed next to a community and a unit it re-identifies the resident to anyone
holding the emailed file. The dashboard only ever needs whether a case exists,
so that is all that survives, as `has_case`. The script refuses to write a file
with either column in it. `Name` on the tracker is the unit number, not a
person, and is kept because it is the join key to the receivable.

## Controllable expense and utility recapture

Austin's split: **utilities, taxes and insurance are not controllable** by a
community manager; everything else in operating expense is.

Controllable is computed as total opex **minus** those three, not by summing
named categories. That way it reconciles to opex exactly and
`other_controllable` absorbs admin, travel and bad debt without needing a
warehouse measure for each.

Utility recapture is utility reimbursement income over utility expense, target
80%. The portfolio runs 45%, absorbing about $242K a month, and it varies
sharply by vehicle (JREFI 34%, JREFII 54%). It sits on its own rather than
inside controllable expense because it is a metering and pricing question, not
something a manager spends their way out of.

## Vehicle grouping

Both the Communities and Collections tabs, and the Financials P&L, open
**collapsed to vehicle level** across the 8 vehicles in the PDS roster. A
66-park flat list is unreadable, and the vehicle is how ownership asks the
question.

Vehicle totals are pre-computed in the build so a collapsed row is a real
weighted figure, never an average of averages. When a filter narrows the set,
`groupByVehicle` recomputes rather than showing a vehicle's untouched totals
next to a partial list of its communities.

## Budgets are loaded per fiscal year

2025 budgets sit at 42–65% of actual because only some properties had one
loaded; 2026 runs 94–107%. Plotting them drew a budget line that looked like a
huge miss rather than an absent plan, so the build finds the first month from
which *every* later month clears 85% coverage and nulls everything before it.
`period.budget_from` records where the series starts, and the chart says so.

## The reportable gate

**A community appears only if the Property Data Sheet marks it Reportable = Yes.**
That single field, maintained by Austin, is the roster.

It lives in the `vwr VW_PDS_V2` sheet of the Property Data Sheet on SharePoint,
exported to `pipeline/raw/pds_reportable.json`. It is **not** in the warehouse:
the RentViewer MCP connector exposes five models and `VW_PDS_V2` is not among
them. If RentViewer enables it for AI analysis, the SharePoint read goes away and
it becomes a seventh query.

The gate matters because the warehouse's `propertyName` mixes about 150 values,
and roughly half are not communities: funds, holdcos, GPs, LP entities, utility
sub-ledgers, home-sales ledgers, `x`-prefixed retired records, and dead
duplicates of live parks. An earlier build inferred all of that from name
patterns and occupancy heuristics and got 81 communities. The Reportable flag
gives 68, joins to the warehouse on Property Name with zero fuzzy matching, and
resolves both data-quality problems the heuristic build had raised: the five
records reporting exactly 0% occupancy on 457 lots and the communities holding
100% of their receivables in the 90+ bucket all sit outside the reportable set.

The gate moved the portfolio numbers materially:

| | Inferred roster | Reportable = Yes |
|---|---|---|
| Communities | 81 | 66 |
| Lots | 7,812 | 6,516 |
| Occupancy | 75.2% | 80.0% |
| Receivables | $1.48M | $928K |

Reportable = Yes is a *necessary* condition, not the only rule. Two things still
sit on top of it:

- **`sold`** in registry.json excludes a disposition the PDS has not caught up
  with. Congress and Shell Pointe sit there, both confirmed sold by Austin on
  2026-09-04. The build raises an informational flag for any entry still marked
  Reportable, so the override stays visible and can be retired once the PDS
  catches up.
- **`roll_up`** attributes a non-reportable sub-ledger's money to its reportable
  parent. Northgate Utility bills against Northgate MH's lots, so its receivables
  belong to Northgate MH while its unit count does not.

**Money and lots do not merge the same way.** This caused a real bug worth
remembering: merging a duplicate ledger's unit count as well as its money gave
Colonial 230 lots instead of 115 and reported 45% occupancy against an actual
90%. A sub-ledger or duplicate describes lots already counted once, so only a
`keep` record contributes lots. `target()` routes money; `target_units()` routes
lots.

Every name the warehouse returns lands in `data/registry_audit.json` with its
disposition and reason, so anything newly reportable, newly missing, or newly
unclassified shows up there instead of quietly changing a total.

### When Austin sells a property

Flip Reportable to No in the Property Data Sheet and fill the Sale Date. That is
the whole change, and it is the preferred one, because the roster then carries
the truth on its own.

Add it to `sold` in registry.json only when it has to come out before the PDS is
updated. That override is a stopgap, not a home: the build keeps flagging it
until the PDS agrees, and the entry should be deleted once it does.

Historical receivables snapshots are **not** scrubbed when a property is sold —
Austin's standing instruction from 2026-07-27. History stays as recorded; new
snapshots simply exclude it.

## Data-quality flags

`build.py` raises flags rather than papering over problems, and the UI shows them
above the numbers they qualify. On the reportable roster the standing ones are:

- **The 90+ bucket is up 148% in seven months**, $254K in January to $630K in
  August, while the monthly collection rate still reads 99.2%. This is the real
  story in the data, and the reportable gate made it *clearer*, not smaller: the
  heuristic roster's frozen ledgers were masking the trend. Current billing
  collects fine; a growing pile ages through and never gets collected. Total
  receivables are up 62% year over year on the same roster.
- **Congress and Shell Pointe are excluded by override rather than by the
  roster.** Both are confirmed sold, so they are correctly out of every figure,
  but the PDS still reads Reportable = Yes with no Sale Date. Flipping Reportable
  to No and filling the Sale Date lets the `sold` entries be deleted.
- **One community's lot count disagrees with the PDS.** The PDS is authoritative,
  so a gap means the Rent Manager unit list is out of step and that community's
  occupancy sits on the wrong denominator.
- **September financials are not posted**, so the Financials tab and NOI tile
  stay on the closed month.
- **Six communities post revenue with no budget loaded**, so their variance is
  blank.
- **Receivables rolled in from sub-ledgers** are reported as a total with the
  ledgers named, so the attribution is visible.

## Occupancy, reported two ways

A lot marked `Lot-Unusable` or `Lot-Demo` is not a leasing failure — it is
inventory that does not exist yet. So the dashboard reports both:

- **Occupancy** — every lot in the denominator, computed from unit-days so a
  424-lot park outweighs a 19-lot one.
- **Occupancy (rentable)** — unusable and demo lots removed.

The Vacancy tab splits empty lots three ways: leasable now, needs work first,
not leasable. "Vacant" as a single number hides the difference between a lot you
can fill this week and one that needs a demo permit.

## Files

| Path | What it is |
|---|---|
| `pipeline/queries.json` | The six warehouse queries, the PDS roster and the eviction tracker, with row-limit warnings |
| `pipeline/raw/pds_reportable.json` | The Reportable = Yes roster — the gate |
| `pipeline/raw/eviction_tracker.json` | Case stages, de-identified — the AR work buckets |
| `pipeline/registry.json` | Sold overrides, roll-ups, segments, unit types, thresholds, home pipeline, eviction stages |
| `pipeline/stage_eviction.py` | Eviction Tracker CSV → de-identified JSON |
| `pipeline/build.py` | Raw pulls → `data/dashboard.json` |
| `pipeline/publish.py` | Payload + UI → one standalone HTML |
| `pipeline/raw/` | Committed raw query results |
| `data/dashboard.json` | The payload the UI reads |
| `data/registry_audit.json` | Every property name and its disposition |
| `dashboard/app.js` | The UI (plain-JS React, no build step) |
| `dashboard/styles.css` | Parakeet brand tokens, light and dark |
| `dashboard/index.html` | Local dev shell, fetches the payload over HTTP |
| `dashboard/vendor/` | React 18.2.0 UMD, inlined only into the standalone file |
| `scripts/refresh.sh` | Build + publish in one step |

## UI notes

- Plain-JS `React.createElement`, no JSX and no build step, so the same
  `app.js` runs locally and inlined in the artifact. React 18.2 UMD comes from
  cdnjs, which is what the artifact CSP allows.
- Charts are drawn in **measured pixels**, not a fixed user-unit viewBox. An
  earlier version used `viewBox="0 0 100 34"` with `preserveAspectRatio="none"`,
  which stretched labels horizontally and rendered 2.5px type at 35px in a
  full-width panel. `useWidth` measures the container so type, padding and
  stroke weight hold their stated sizes at any width.
- Palette and type are fixed by the `parakeet-brand` skill: four brand colors,
  `#8FA3B2` as the one muted neutral, Red Hat Display with a Calibri fallback.
  The dark theme's grounds are deeper tints of brand navy rather than a fifth hue.
