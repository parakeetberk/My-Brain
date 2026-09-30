# Rehab board builder

Rebuilds `https://claude.ai/code/artifact/34a291f1-59a7-4d4b-952c-3bf5404eaa87`
from the tracker export.

## Rebuild

    cd 70-Operations/rehab-program
    python3 build/make_data.py            # -> build/rehab-data.json
    python3 build/assemble.py             # -> build/rehab-board.html
    # publish rehab-board.html to the artifact URL above

**A dashboard that cannot be regenerated is a screenshot.** The 2026-09-01 open-board
rebuild proved the cost of hand-assembly: a fixed-column-order parser corrupted four
hundred rows and nobody noticed for a day. Same rule here.

## Files

| File | What it is |
|---|---|
| `make_data.py` | reads `data/rehab_tracker_all_data_*.csv`, writes `rehab-data.json`. All aggregation lives here so the page never computes a business figure. |
| `assemble.py` | `src/head.html` + `src/body.html` + the data block + `src/app.js` -> one self-contained page. |
| `src/head.html` | title, fonts, CSS. Parakeet surfaces and status colours; categorical series from the validated data-viz reference palette. |
| `src/body.html` | the page's prose and section shells. **The argument lives here** - the numbers are injected. |
| `src/app.js` | renders tiles, both charts, the rollups, the nine gap blocks and the filterable unit table. |

## When a fresh tracker export arrives

Drop it in `data/` with its own as-of date in the filename - **never overwrite the old
one.** These exports are point-in-time snapshots of a live vendor sheet, and the diff
between two of them is the only way to see whether a reconciliation gap is closing.
Then point `make_data.py` at the new file and rebuild.

## What the page must never do

- Present `expected` or `remaining` as budget. They are tier averages off as few as six
  comps, and the page labels them **model** in every place they appear.
- Show an unresolved community code as a real community. `NGMH`, `LS` and `PPH` render as
  `UNRESOLVED`, never guessed.
