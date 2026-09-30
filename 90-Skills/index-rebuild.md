# Skill: the Index Rebuild

Claude rebuilds the Brain's maps, the master index and every folder's MOC file list, so future sessions read the map first and open only the notes they need. Fewer tokens than reading the whole vault every time.

To run it: tell Claude "rebuild the index", or paste everything below the line.

---

You are rebuilding the maps of this AI Brain.

## What you rebuild

1. **`00-Meta/index.md`**: a row for each folder's MOC plus the pages that matter at business level: where it lives (as a `[[wikilink]]`) and a one-line summary. Grouped by folder, in folder order. Not every page, because the MOCs list those.
2. **Every folder's `MOC-*.md` Files list**: every page and document the folder owns as a `[[wikilink]]`, one line each; bulk material as one unlinked line per set, naming it and its count.

## The rules

1. Cover every page in the vault. No page left out. A map with holes is worse than no map.
2. Summaries are one line and factual. Written from what the page says, never from a guess about what it probably says.
3. Rebuilding the index and the MOC file lists is this skill's job and needs no permission. Touching anything *else* does.
4. When done, report: how many pages and documents mapped, how many files sit in bulk sets, and any **page** with zero links in or out (a page should always be listed in its MOC; bulk raw files are meant to be unlinked). Add one line to `00-Meta/log.md`.

## When to run it

After a batch of new content lands: a stack of filed transcripts, a new job folder, a growth spurt. If Claude notices the maps are stale mid-session, it says so and offers this skill; it doesn't run it unasked.
