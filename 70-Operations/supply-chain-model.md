# Supply Chain — Manufactured Housing

> **Source-state paths, 2026-08-31.** The numbered `1. …` through `8. …` community subfolders quoted on this page describe `/sites/main/Shared Documents/` **as it exists today**. They are deliberately left as written: that estate is read-only (see [[CLAUDE]]) and a Brain page that renumbered them would misdescribe live reality and send people to folders that do not exist. The **Birdcage** template is unnumbered per Austin's 2026-08-31 ruling — see [[10-Business/sharepoint/target-structure]].

**What this is:** The operating model for order to occupancy - the seven stages, the diagnostic order, and the sequencing failures that keep recurring.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

The operating model the `supply-chain-analyst` agent reasons from. Kept here so the logic is auditable and improvable, not buried in a prompt.

## The core physics

A manufactured home generates zero revenue until it is delivered, set, finished, and occupied. Capital is committed at order and idle until certificate of occupancy. Compressing order-to-occupancy cycle time is the whole game.

## The chain

1. **Order** — plant slot allocation, model and spec, deposit. Lead times roughly 8–20 weeks, plant-dependent and seasonal. Plant-level variance exceeds manufacturer-level variance.
2. **Pad readiness** — site prep, utilities stubbed, pad or piers set. Must lead delivery. Frequently does not.
3. **Transport** — toter availability, escorts, route permits, weather.
4. **Set** — crew blocks, levels, ties down, marries sections. **Usually the real bottleneck.** Scarce regional resource, booked weeks out; a missed window slips everything behind it.
5. **Permits and inspections** — AHJ timelines are exogenous and variable. Applications must be filed against the ORDER date, not the delivery date. Permit aging leads set-schedule failure.
6. **Finish-out** — skirting, steps, decks, AC, landscaping. Small dollars, enormous schedule leverage: a complete home missing skirting cannot get a CO and cannot be occupied.
7. **CO and occupancy** — revenue begins.

## Diagnostic order

Check in this sequence — it reflects the empirical frequency of the true constraint:

1. Set crew capacity and scheduling
2. Permit status and aging vs. order dates
3. Utility connections
4. Finish-out materials and trades
5. Pad and site readiness
6. Factory lead time

Factory lead time is what everyone blames and is rarely what binds. Verify before accepting it.

## Metrics

- Order-to-occupancy cycle time, by community and manufacturer
- WIP count by stage, with aging in each
- Set-crew throughput (homes/week) vs. committed pipeline
- Days-on-site-unset — purest measure of dead capital
- Permit aging distribution; permits filed vs. homes ordered
- Dollars of capital in unset or unfinished inventory
- Finish-out stall rate — homes complete except one blocking item

## Recurring sequencing failures

- Homes delivered before pads ready — storage cost, damage risk, double handling
- Permits filed at delivery instead of at order — guarantees set-crew slip
- Set crews booked past delivery dates — homes sit
- One missing finish-out item blocking CO on an otherwise complete home
- Orders placed without confirmed downstream set-crew capacity
- Capex pacing decoupled from occupancy ramp — spending ahead of revenue

## Parakeet-specific context

**Manufacturer relationship**: Cavco is significant enough to have its own SharePoint site collection (`/sites/ParakeetHomes-ParakeetHomesxCavco`) and a manufacturer tree at `/sites/main/Shared Documents/Parakeet Homes/Manufacturers/Cavco Homes/`. Champion also appears in the tooling. Both have import skills configured.

**Where the data lives** (as of 2026-08-26, pending full inventory):
- Construction and development by community — SharePoint `/sites/main/Shared Documents/Construction/<COMMUNITY>/DEVELOPMENT/`
- Park-owned assets — `/sites/main/Shared Documents/Parakeet Homes/Park owned assets/`
- Site plans — duplicated across four locations, authority unresolved
- Project and service orders — `/sites/main/Shared Documents/Operations/<Community>/3. Facilities/Project & Service Orders/`
- Capex tracking — several spreadsheets unfiled at OneDrive root: `Cap Ex Project Tracker_AB Version.xlsx`, `capex pacing.xlsx`, `Consolidated Jadian CapEx Summary.xlsx`, `2024 Capex Budget Tracker - Jadian Properties v2ab.xlsx`
- Occupancy — `Occupancy Report.xlsx`, `Portfolio Vacancy.xlsx`, both unfiled at OneDrive root
- Rent Manager exports — OneDrive `Rent Manager Exports/`

**Known gap**: no single place shows homes in WIP by stage across the portfolio. Until that exists, cycle time cannot be measured and the bottleneck cannot be proven. Building that view is the highest-value supply chain task available.

## This week's numbers — 2026-08-19–24 road-trip review

**Source**: `C:\Users\AustinBerk\Desktop\Parakeet Week in Review.docx`, compiled 2026-08-25 from Plaud recordings of a property road trip. **This is a single AI-compiled source from audio — treat every claim below as SINGLE-SOURCE unless separately corroborated**, per the document's own diarization caveat.

- **Home-set average: 37 days, against a 45-day target.** The first actual cycle-time number this domain file has ever recorded. It partially answers the "known gap" above but only for the set stage — it is not a WIP-by-stage view, and no other stage (order, pad-readiness, permits, finish-out) has a comparable number yet.
- **Infill program: 130 homes delivered, 40 listed and ready** — finishing above an aggressive plan, ahead of snowbird season. Described in the source as "an act of god."
- **Champion and Cavco are storing homes free**, with **24 more slotted for Lucky Clover and River Oaks**. Free storage is masking the delivered-but-unset problem below rather than solving it — it removes the carrying-cost signal without removing the dead capital.
- **Champion — confirmed portfolio-level vendor failure**, and a direct, named instance of the delivered-but-unset dead-capital pattern this file already predicted under "Recurring sequencing failures" (*"Homes delivered before pads ready"*) and "Metrics" (*"Days-on-site-unset — purest measure of dead capital"*):
  - Two no-shows at Applegate.
  - Homes delivered 7/22 and 7/23 **still unset** as of the review — over a month on-site with zero revenue.
  - Defective stairs, treads, doors, and concrete across **all** Riverwalk lots.
  - One Applegate home has **no cribbing** and is "about to fall over" — a safety item, not just a schedule one.
  - The source is explicit this has moved from three site-level complaints to **one consolidated corporate-level escalation**. See `99-Archive/2026-08-catchup/entity-pages/applegate.md`, `99-Archive/2026-08-catchup/entity-pages/riverwalk.md`.
- **Paving rebid: $1.8M → $683K**, roughly **$1.1M saved** — verify scope before signing; a bid drop this large on identical scope is itself worth a second look.
- **Vantage Oaks: all change orders signed; flood-elevation risk resolved** — no $100K/home elevation requirement after all. See `99-Archive/2026-08-catchup/entity-pages/vantage-oaks.md`.
- **Vantage permits must be collected in person, inside a 72-hour window**, the moment Champion says issued — then 2 NCS + 2 park models set immediately. This makes Parakeet's own permit clock partly hostage to a vendor (Champion) already failing on set schedules elsewhere in this same review — worth folding into the portfolio-level Champion escalation above rather than treating as a separate permit problem. Cross-ref: `70-Operations/license-and-permit-ownership.md`.
