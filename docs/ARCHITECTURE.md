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
# 1. refresh pipeline/raw/*.json  (needs the warehouse connector; see queries.json)
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

This is the single most important thing to understand about the numbers.

The warehouse reloads a full snapshot each month, so the **open month is
partial**. Rent bills on the 1st and collects through the month, which means an
open-month snapshot taken on the 4th shows:

- AR roughly **80% higher** than reality (everything just billed, nothing paid)
- open accounts jumping from ~900 to ~2,250
- a collection rate around **45%** instead of ~99%

So every headline figure, table and chart uses the **last closed month**. The
open month appears in the masthead and in the data notes, and nowhere else.
Ignoring this distinction is the easiest way to produce a badly wrong number
from this warehouse.

## The property registry

`pipeline/registry.json` decides what each `propertyName` in the warehouse
actually is. Rent Manager carries several parallel record types under that one
field, and about half the names are not communities:

| Kind | Example | Treatment |
|---|---|---|
| Live community | `Riverwalk` | `keep` — its own row |
| Retired record | `xGulf Breeze MHP` | dropped by the `^x[A-Z]` rule |
| Duplicate ledger | `Colonial MHC` beside `Colonial Manufactured Housing Community` | `alias` — money merges, **lots do not** |
| Utility sub-ledger | `Northgate Utility` | `roll_up` — money to parent, no lots |
| Home-sales ledger | `Cedar Grove Homes` | `roll_up` — money to parent, no lots |
| Fund / holdco / GP | `Parakeet MHC Hold Co I`, `A2Z Fund I, LLC` | dropped, not a community |
| Sold | `Congress Mobile Home Park` | dropped, per the standing July 2026 rule |
| Stale | no snapshot in 4+ periods | dropped, and flagged for confirmation |

**Money and lots do not merge the same way.** This caused a real bug worth
remembering: merging an alias's unit count as well as its money gave Colonial
230 lots instead of 115 and reported its occupancy as 45% instead of 90%. A
duplicate ledger describes lots that are already counted once, so only a `keep`
record contributes lots. `target()` routes money; `target_units()` routes lots.

Every name the pipeline sees lands in `data/registry_audit.json` with its
disposition and the reason, so a new or reclassified property shows up there
instead of quietly changing a total.

### When Austin sells a property

Add it to `sold` in `registry.json` with every name variant the warehouse uses
(full RM name, community name, short code), then rebuild. Do not edit `build.py`.

Historical AR snapshots are **not** scrubbed when a property is sold — that is
Austin's standing instruction from 2026-07-27. History stays as recorded; new
snapshots simply exclude the sold community.

## Data-quality flags

`build.py` raises flags rather than papering over problems, and the UI shows
them above the numbers they qualify. Current standing ones:

- **90+ receivables have nearly doubled** in eight months ($625K → $1.18M) while
  monthly collections still read ~99%. Collections is a flow and AR is a stock;
  1–3% monthly leakage on $4.2M compounds. This is the real story in the data.
- **Three communities hold 100% of their AR in the 90+ bucket** with nothing
  current — a signature of a migrated or frozen ledger, not live delinquency.
- **Five records report exactly 0% occupancy on 457 lots.** They stay in the
  portfolio denominator (the conservative reading) and are held out of the
  "lowest occupancy" ranking so they don't crowd out real leasing problems.
  Confirm each in Rent Manager, then either fix the ledger or classify it.
- **Nine communities post revenue with no budget loaded**, so their variance is
  blank.

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
| `pipeline/registry.json` | Property classification, exclusions, thresholds |
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
