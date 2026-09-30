# Skill: the Weekly Brain Review

The maintenance habit that keeps the Brain alive: once a week, Claude sweeps the vault, clears the Inbox, catches stale pages, and tells you what it did. This is also the standard second scheduled agent. Set it to run weekly and it becomes a habit you don't have to keep.

To run it: tell Claude "run the weekly brain review", or paste everything below the line.

---

You are running the Weekly Brain Review on this AI Brain.

## The sweep, in order

1. **Inbox:** go through `05-Inbox/`. For each item, say where you'd file it and why. File on the yes; anything still uncertain stays put with a note. The goal is an empty Inbox, never a guessed one.
2. **Unfiled transcripts:** any raw transcripts sitting in the Inbox? Offer to file them per `90-Skills/transcript-filing.md`.
3. **Stale pages:** any page contradicted by newer decisions, marked "needs review", or carrying an as-of date that's aged badly? List them and offer the update per `90-Skills/page-update.md`.
4. **Ledger check:** any number in `00-Meta/numbers-ledger.md` that's clearly out of date? Flag it; ask for the current figure rather than guessing.
5. **Map check:** does `00-Meta/index.md` match the actual pages? Does every folder's MOC list match its files? Stale → offer `90-Skills/index-rebuild.md`.
6. **Delivery:** any job folder in `70-Operations/` that looks finished? Suggest retiring it to `99-Archive/` (never delete, per rule 2).
7. **Data lineage probe:** run [[90-Skills/data-lineage-probe]]. It calls each connector and rewrites the source layer of [[10-Business/data-lineage]] with this run's date. A report or model that appeared or disappeared is a finding — the 2026-09-09 build found six warehouse models the vault had never recorded.

## The report

End with a short plain-English summary: what was filed, what was updated, what's still open, and the one thing most worth doing next week. Five lines or fewer. This is a health check, not an essay. Add one line to `00-Meta/log.md`.

## The rules

- Every move and every change gets asked about before it happens. The review proposes; the user approves.
- If the week added nothing, say so in one line and stop. A quiet week doesn't need a padded report.
