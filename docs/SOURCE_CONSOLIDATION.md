# Moving the unit-grain pulls from the Rent Manager API to the warehouse

Status as of 2026-09-08: **rent roll passes, receivables is under daily observation, moves untested.**
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
| 78 Aged Receivables | `VW_Aged_Receivables` @ unitName | **Not yet.** $513K apart, probably a one-day snapshot drift across the grace day. Under daily observation. |
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

## Receivables: $513K apart, and the leading explanation is timing

```
warehouse unit pull   $1,012,231 inside the reportable roster   as of 2026-09-05
rent manager 78       $1,525,120 inside the reportable roster   as of 2026-09-04
                        -$512,889
879 unit keys rent manager has and the warehouse does not, worth $648,439
```

Austin's read, and the evidence supports it over mine. **The two snapshots are
one day apart and the day between them is the grace day.**

`VW_Aged_Receivables` holds 21 monthly snapshots; its latest real one is
`asOfDate = 2026-09-05` at $2,144,770 across 1,328 customers with a balance,
which the unit pull reproduces to the dollar. The Rent Manager file was pulled
2026-09-04. Rent bills on the 1st and is late after the 5th — `grace_day` in
registry.json is the 5th — so the 4th to the 5th is the heaviest payment-posting
window of the month. 879 accounts clearing in the last day before late fees is
ordinary behaviour, and it would drop them out of a Sep 5 snapshot while they
still sat on a Sep 4 report. $648,439 over 879 units averages $738 each, which
is about one month's charges per account rather than a partial balance —
consistent with paying off in full.

Four alternatives were tested and none holds:

- **Not zero balances.** All 879 keys carry a non-zero remaining balance.
- **Not prospects.** None carries a prospect charge row.
- **Not credits.** None has a negative balance.
- **Not a property-alias failure.** Every community the comparison called
  missing resolves cleanly — Regency I & II, Riverwalk, McGregor Downs, all of
  them. The shortfall is inside those communities, unit by unit: 35 units with
  a balance at Regency in the warehouse against 112 in Rent Manager.
- **Not an aging shift among the units both sources hold.** Only 3 units
  disagree on the 0–30 bucket. (An earlier reading of this as a systematic $75
  bucket shift was wrong — it was three data points.)

### Why the rent roll is immune to this and AR is not

The reconciliation ledger makes the mechanism obvious on its first two rows:

```
ar        wh 2026-09-05  rm 2026-09-04  drift +1 d  gap -$512,889  rm-only 879
rentroll  wh 2026-08-31  rm 2026-09-04  drift -4 d  gap        $0  rm-only   1
```

The rent roll drifts **four days** and the gap is exactly zero. AR drifts **one
day** and the gap is half a million dollars. That is not a contradiction, it is
the distinction between a flow and a stock — the same one that makes a 99.7%
monthly collection rate sit next to a 90+ bucket up 30%. August charges are
fixed once August closes, so a rent roll pulled on any later date returns the
same numbers. A receivable balance is an as-of reading that changes every time
a payment posts, so a single day of drift across the grace day moves it more
than four days of drift moves a closed month.

Which means the fix for AR is not to reconcile the two sources. It is to pin
both to the same `asOfDate` and stop comparing a Friday to a Saturday.

### How we find out

Austin's call: keep both running and let the data settle it. Both sources are
pulled, `compare_sources.py <source> --log` appends a dated row to
`data/source_reconciliation.json`, and that file is committed for the same
reason the flag ledger is — the container is reclaimed between runs, and one
day's reading of a snapshot difference says nothing about whether it is an
artefact.

Each row carries both as-of dates and the drift between them. The test is
simple and it falsifies cleanly:

- **If it is timing**, the gap tracks `drift_days` and collapses toward zero
  when both sources are pulled on the same day.
- **If it is not**, the gap survives at zero drift, and then it is a real
  question for whoever owns the RentViewer model.

This needs the Rent Manager files pulled daily, which today they are not — they
were absent from the refresh runbook and had gone four days stale. That is the
one change the experiment depends on.

Until it resolves, AR stays on report 78.

### A separate thing this turned up

`xParkwood Manufactured Housing Community` carries **97 units and $137,340 of
receivables** and is dropped as non-reportable. The `x` prefix is Rent Manager's
retired-record marker and the live `Parkwood Mobile Home Park` is in the roster
with 20 units and $16,698. So Parkwood's receivables sit on two records and the
dashboard reports the smaller one. Either that $137K was written off and the
record is genuinely dead, or Parkwood is understated by eight times its
reported balance. Nobody has said which.

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
python3 pipeline/compare_sources.py rentroll --log
python3 pipeline/compare_sources.py ar --log
```

`--log` appends to `data/source_reconciliation.json` and prints the run history
with the drift column. Re-running on the same day replaces that day's row
rather than stacking a second one, so a day checked twice does not read as a
trend. `WH_AR_AS_OF` and `WH_RENTROLL_AS_OF` at the top of the script are the
warehouse snapshot dates and **must be updated whenever the candidate files are
re-pulled** — a stale value there would make real drift look like zero, which
is the one way this experiment could lie to us.

The harness separates three failure modes that a row-count summary hides: a
unit only one source knows (coverage), a unit both know with different values
(definition or as-of), and a unit both know that agrees (evidence). Only the
third kind is evidence, and a source is not swapped until the first two are
explained rather than merely small.
