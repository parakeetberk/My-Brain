# Open board builder

Rebuilds `https://claude.ai/code/artifact/de27b6c8-cbac-4342-a5cc-32e0598f6144`
from the five registers.

## Rebuild

    cd 00-Meta/board-data/builder
    VAULT="$HOME/mnt/My Brain" python3 build_board.py
    # -> open-board.html, publish it to the artifact URL above

## Never lose a comment, a correction or a flag

Austin works three things directly on the published page, and **all three live
in the page, not in the vault**:

| What | Where it lands | Copied to chat as |
|---|---|---|
| Comments | `comments.json` | `KP-0010: text` |
| Field corrections (priority, category, community, owner) | `edits.json` | `TD-0044: Community -> Riverwalk (was blank)` |
| Budget-week flags | `flags.json` | `TD-0044: FLAG Budget week` |

`pull_comments.py` writes all three in one go and `build_board.py` reads all
three automatically. **Every rebuild must run the pull first:**

    # 1. save the LIVE artifact HTML to live.html (Claude reads it with the Artifact tool)
    python3 pull_comments.py live.html comments.json
    # 2. after writing a row's comments into its register, mark them done:
    python3 pull_comments.py live.html comments.json --action KP-0010 TD-0004
    # 3. rebuild - build_board.py picks up comments.json automatically
    VAULT="$HOME/mnt/My Brain" python3 build_board.py

Skipping step 1 wipes the history, the corrections and the flags. **There is
no other copy of any of them.**

A correction changes what the BOARD shows. It does not change the register -
that is a real edit, made by hand, and only then is the correction marked
`--action`. The board is a proposal surface; the markdown is the record.

## Files

| File | What it is |
|---|---|
| `parse_registers.py` | reads the five registers. **Header-driven**: every markdown table is mapped by its own header row, never by column position. The 2026-09-01 defect came from assuming a fixed order. |
| `build_board.py` | assembles the page: template + data block. |
| `template_head.html` | `<title>`, fonts, and the CSS (`__BOARD_CSS__` is filled from `board.css`). |
| `board.css` | the board's styles. |
| `template_app.js` | renders rows from the data block, filters, the comment popup, save. |
| `pull_comments.py` | extracts comments, corrections and flags out of a published page. |

## How the page republishes itself

The published page carries a base64 copy of its own template with two
markers, `__TPL_B64__` and `__DATA_JSON__`. Saving decodes the template,
puts the same base64 back in the first marker and the new data in the
second, and calls `artifact.publish`. The template is therefore a fixed
point: only the data block ever changes. `template_app.js` builds those
marker strings at runtime (`"__TPL" + "_B64__"`) so the builder's own
literal replacement does not corrupt the app source.

## One format the parser depends on

A commitment heading that closes must end with its own bold span:

    ### `CM-03` 3. Some title — **UNBLOCKED 2026-09-01** — **CLOSED 2026-09-02**

**Not** `— **UNBLOCKED 2026-09-01, CLOSED 2026-09-02**`. `parse_commitments()` looks for
`**CLOSED...**` as a span that *starts* with CLOSED, so a second status folded into the
same bold span makes it `None` and the build dies on an `AttributeError`. It crashed
loudly on 2026-09-02 rather than dropping rows, which is the good failure, but the fix
is to write the heading in the form above.

## Two more traps in the registers themselves

**The word "unassigned" anywhere in an owner cell forces the row to Unassigned.** `owner_short()`
short-circuits on `unassigned|no owner|nobody` before it ever looks at the alias table, so
`Austin Berk - set by Austin on the open board, up from unassigned` came back as Unassigned and
sat in the no-owner count. The guard is right for `unassigned - the Controller seat`. Keep owner
history on its own bullet, never in the Owner line. Found 2026-09-02 on `CM-05`, the only row
affected across all six registers.

**A commitment's `- **Priority**:` line beats its heading.** The chip reads `_prio` from that
bullet; the meta line reads `state` from the heading. If the heading says CLOSED and the bullet
says Open, the board shows both and contradicts itself. Change them together.
