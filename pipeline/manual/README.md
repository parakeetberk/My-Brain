# Refreshing a source by hand

When a connector is down, not yet enabled, or has gone stale, any dataset can be
refreshed by dropping a file. The manual path and the automated path use the
same landing zone and the same normaliser, so the fallback cannot drift from the
primary.

## How

1. Export the report from Rent Manager or the warehouse as CSV.
2. Name it with its as-of date. The date in the filename **is** the as-of; the
   normaliser reads it and the history keys on it.
   - `asset_listing_2026-09-08.csv`
   - `Asset Listing_260908.csv` also works, that being what SharePoint drops
3. Put it in `pipeline/incoming/<dataset>/` — create the folder if it is not
   there. `pipeline/manual/` is for anything you want kept but not read.
4. `python3 pipeline/sources.py status` to confirm it will be picked up.
5. `python3 pipeline/sources.py build` to normalise it.

## Rules

**Never rename a file to today's date to make it look fresh.** The as-of is what
every baseline is computed against. A file re-dated forward fabricates a day of
history, and nothing downstream can tell it from a real one. If a source is
stale, let it be stale — the dashboard says so and the day is skipped.

**Keep the export's own header row.** The reader is header-driven, never
positional, because the asset listing archive changes column layout across
dates. An export with the header stripped will produce nonsense rather than
an error.

**Do not hand-edit values.** Fix the source system, re-export, re-drop.
