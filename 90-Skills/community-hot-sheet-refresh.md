# Skill: refresh the community hot sheets

**What this is:** how the `## Live from Rent Manager` block on every community page gets filled. Run it on a cadence. Everything else on a community page comes from workbooks and only changes when a new workbook lands.

## When to run it

Monthly, after the Director of Operations approves the Month End Tracker on the 29th and Justin Minkoff has entered month end in Rent Manager (SOP 301). Running before that pulls a half-closed month.

## What fills the block

The RentViewer data warehouse connector. Five queries, all grouped by property, all point-in-time snapshots restricted to the latest period unless a `reportMonth` grouping is supplied.

| Field on the page | Model | Measures |
| --- | --- | --- |
| Occupancy (live) | `VW_Rental_Unit_Listing` | `occupancyRate`, `unitCount` |
| Collection rate | `VW_Summary_Rent_Roll` | `collectionRate`, `totalCharged`, `totalPaid` |
| AR outstanding | `VW_Aged_Receivables` | `agedReceivablesTotal`, `customersWithBalance` |
| AR over 90 days | `VW_Aged_Receivables` | `over90Days`, `percentOver90` |
| NOI YTD vs budget | `VW_Budget_Comparison` | `noiYTD`, `noiBudget`, `noiVariance`, `noiMargin` |
| Move-ins / move-outs | `VW_MoveIns_MoveOuts` | `moveIns`, `moveOuts`, `netMovement` |

Group every query by `propertyName`. Join to the community pages on the short code in `[[60-Communities/portfolio]]`, not on the name. Rent Manager property names and vault page names do not match exactly.

## Rules

1. **Stamp every value with the period it came from.** The warehouse reloads the whole population each period; a figure describes one period, not a running total. Write the "Pulled" column as the report month, not today's date.
2. **Never overwrite the Snapshot table with live data.** Snapshot is plan and workbook data with its own as-of dates. Live is live. Two blocks, on purpose. The whole point is being able to see the plan and the actual side by side.
3. **If a query times out, leave the block as it is and say so.** A stale value that looks current is worse than an empty cell. The warehouse timed out on every query on 2026-08-31, which is why the blocks are empty.
4. **Any number that lands on a page also lands in `00-Meta/numbers-ledger.md`** with its source and as-of date, per the hard rules.
5. **Re-derive the watch list after a refresh.** Live occupancy under 85%, collection rate under 95%, or AR over 90 days above 10% of the balance each earn a flag.

## After the run

Append a dated line to `00-Meta/log.md` saying which report month was pulled and how many properties came back. Route anything the refresh surfaces: draft the email to whoever owns it, add it to the community page, and put a named task in `10-Business/eos/to-dos.md`.
