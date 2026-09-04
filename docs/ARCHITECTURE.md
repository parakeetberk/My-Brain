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
of Austin's 9am meeting floor. It re-runs the six queries, rebuilds, republishes
to the same artifact URL, and pushes to this branch.

It is bound to the session that built the dashboard rather than spawning a fresh
one, because the warehouse connector lives on that session. The trigger record
itself stores no connector grant, so if a run ever reports the
`mcp__RentViewer_Data_Warehouse__run_query` tool as missing, attach the
RentViewer connector to the Routine in claude.ai Routines settings.

The warehouse is a monthly snapshot, so a weekday cadence is not about the
closed-month figures changing daily. It keeps the open-month reading current,
catches newly onboarded properties in the registry audit, and means the numbers
are already fresh at the Friday 2pm EOS call and the Monday Jon catch-up.

Every run reports what moved and re-reads the flags. A run that cannot reach the
warehouse stops rather than republishing a stale payload to the live URL.

## Running it by hand

```bash
# 1. refresh pipeline/raw/*.json  (warehouse connector + the PDS roster from
#    SharePoint; both are specified in pipeline/queries.json)
# 2. build the payload
python3 pipeline/build.py

# 3. assemble the standalone page
python3 pipeline/publish.py

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
| `pipeline/queries.json` | The six warehouse queries, with row-limit warnings |
| `pipeline/raw/pds_reportable.json` | The Reportable = Yes roster — the gate |
| `pipeline/registry.json` | Sold overrides, roll-ups, segments, unit types, thresholds |
| `pipeline/build.py` | Raw pulls → `data/dashboard.json` |
| `pipeline/publish.py` | Payload + UI → one standalone HTML |
| `pipeline/raw/` | Committed raw query results |
| `data/dashboard.json` | The payload the UI reads |
| `data/registry_audit.json` | Every property name and its disposition |
| `dashboard/app.js` | The UI (plain-JS React, no build step) |
| `dashboard/styles.css` | Parakeet brand tokens, light and dark |
| `dashboard/index.html` | Local dev shell, fetches the payload over HTTP |
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
