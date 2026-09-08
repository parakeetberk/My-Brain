# Moving the unit-grain pulls from the Rent Manager API to the warehouse

Status as of 2026-09-08: **rent roll passes, receivables does not, moves untested.**
Nothing has been cut over. The candidate pulls live in `pipeline/raw/candidate/`
and `build.py` still reads the Rent Manager files.

## Why this was tried

The pipeline reads two sources for the same five reports. The warehouse gives
twenty months of history at property grain; the Rent Manager API gives today at
unit grain. That looked like a hard split until the schema was actually read:
four of the five cubes carry a `unitName` dimension, so the warehouse can serve
unit grain too. A portfolio-wide unit-level rent roll returns 10,285 rows,
inside the 15,000 limit, on a two-measure batch.

Consolidating would drop the pipeline from two sources plus SharePoint to one
source plus SharePoint plus a single API call, and would fix the fact that the
five Rent Manager files were never in the refresh runbook and had gone four
days stale while everything around them was same-day.

## What replaces what

| Rent Manager | Warehouse | Verdict |
|---|---|---|
| 69 Summary Rent Roll | `VW_Summary_Rent_Roll` @ unitName | **Cut over.** Matches. |
| 78 Aged Receivables | `VW_Aged_Receivables` @ unitName | **Do not cut over.** $513K apart. |
| 77 Move In / Move Out | `VW_MoveIns_MoveOuts` @ unitName | Untested. |
| 244 Asset Listing | — no assets cube — | **Stays on the API.** |

## Rent roll: matches

`compare_sources.py rentroll`, warehouse August 2026 snapshot against the
Rent Manager pull, joined on (roster property, unit) through the same alias map
`build.py` uses:

```
keys: 7,440 warehouse / 7,344 rent manager / 7,343 shared
only in warehouse: 97      only in rent manager: 1

FIELD               WAREHOUSE   RENT MANAGER         DIFF   MATCH%
rent charges       $2,920,712     $2,920,712           $0   100.0%
misc charges       $1,248,379     $1,247,779         $600   100.0%
total charged      $4,069,166     $4,071,307      -$2,141   100.0%
total paid         $4,057,381     $4,057,381           $0   100.0%
```

Rent charges and total paid agree to the dollar. The two residuals are three
units: Auburn Ridge 131A (+$600 misc) and two Gulf Breeze lots where the
warehouse carries a credit the Rent Manager row does not. Both worth a look,
neither a reason to hold the cutover.

The 97 warehouse-only keys are **Shell Pointe (65) and Congress (32)** — the
two sold properties excluded by registry override rather than by the PDS. They
still resolve through the alias map, so the warehouse returns them and the
scoped Rent Manager pull did not. Expected, not a defect.

## Receivables: half a million dollars apart

```
warehouse unit pull   $2,144,770 total   $1,012,231 inside the reportable roster
rent manager 78                          $1,525,120 inside the reportable roster
                                           -$512,889
879 unit keys rent manager has and the warehouse does not, worth $648,439
```

Three explanations tested and ruled out:

- **Not zero balances.** All 879 keys carry a non-zero remaining balance.
- **Not prospects.** None of the 879 carries a prospect charge row.
- **Not credits.** None has a negative balance.
- **Not an aging as-of shift.** Only 3 units disagree on the 0–30 bucket, so
  the two are aged as of the same date. (An earlier read of this as a
  systematic $75 bucket shift was wrong; it was three data points.)

The cause is unknown. `VW_Aged_Receivables` holds 21 monthly snapshots and its
most recent is 2026-09 at $2,165,275 across 1,362 customers with a balance, so
the pull did capture the current snapshot — the gap is inside it, not a period
mismatch. This is a question for whoever owns the RentViewer model, not
something to paper over: half a million dollars of receivables that one source
sees and the other does not.

Until it is answered, AR stays on report 78.

## Two things the comparison turned up that are worth more than the refactor

### The RV revenue is already in the warehouse

The dashboard flags three RV resorts as showing expenses and almost no revenue,
and says connecting the Campspot rent roll is what fixes it. `VW_Reservation_Activity_Feed`
covers six parks including all three. August 2026:

| Park | Reservations | Allocated rent | Sites | Occupied days |
|---|---|---|---|---|
| Great Oak RV Resort | 146 | $92,643 | 141 | 4,127 |
| Paradise Lakes | 172 | $106,282 | 160 | 4,588 |
| River Oaks RV Resort | 120 | $71,112 | 74 | 2,474 |
| **the three flagged** | | **$270,037** | | |
| Northgate | 68 | $31,831 | 61 | 1,224 |
| Whispering Pines | 75 | $35,533 | 52 | 1,394 |
| Silver Breeze | 23 | $11,793 | 19 | 503 |

The rent roll corroborates it from the other side. The RV lots exist in Rent
Manager as their own property records and bill nothing at all:

```
Great Oak RV Resort   215 units   $0 rent   $0 charged
Paradise Lakes RV     175 units   $0        $0
River Oaks RV Resort  132 units   $0        $0
Northgate RV          126 units   $0        $0
Lucky Clover RV        59 units   $0        $0
Geiger RV              41 units   $0        $0
Geiger Key RV Resort   93 units   $67,638   $87,927   <-- this one does bill
```

So the two halves of the P&L are in the same warehouse: the lots in the rent
roll, the stays in the reservation feed. Before a dollar of it lands on the
page, two caveats. `allocatedRent` spreads a reservation across the months it
covers, which is the right shape for a monthly view but is not the general
ledger and will not tie to it. And Northgate, Whispering Pines and Silver
Breeze also bill recurring rent in Rent Manager, so adding the feed wholesale
would double count — each park needs reconciling on its own.

### The roster drops the RV side of communities it otherwise keeps

The PDS lists `NGMH = Northgate MH` but there is no NGRV row, and `PL = Paradise
Lakes` but nothing for `Paradise Lakes RV`. Rent Manager splits those
communities into separate MH and RV property records, so the roster gate keeps
the MH side and silently drops the RV side: 126 sites at Northgate, 175 at
Paradise Lakes. That is a roster problem, not a Campspot problem, and it is the
more precise diagnosis of the same symptom.

`Apple Creek` (209 lots, billing $0) is a separate question — the roster has
`APPLE = Applegate MHC`, which the warehouse carries separately at 105 units and
$52,860 of rent. Apple Creek is some other record. It bills nothing, so nothing
is lost by dropping it, but nobody has said what it is.

Correctly dropped, for the record: Cedar Grove, Colonial, Lambeth, Valley View,
Parktown, Countryside and `xParkwood` (the `x` prefix is Rent Manager's retired
marker; the live `Parkwood Mobile Home Park` is in the roster and resolves),
plus `Vantage Oaks Utility` and `Applegate Water`, which are utility
sub-entities of communities already counted.

## How to re-run it

```
python3 pipeline/compare_sources.py rentroll
python3 pipeline/compare_sources.py ar
```

The harness separates three failure modes that a row-count summary hides: a
unit only one source knows (coverage), a unit both know with different values
(definition or as-of), and a unit both know that agrees (evidence). Only the
third kind is evidence, and a source is not swapped until the first two are
explained rather than merely small.
