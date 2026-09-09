# Proposed prompt: Rehab call pre-read, Tuesday 5pm ET

**Status: waiting on Austin. Not applied.** Drafted 2026-09-09.

`trig_01MDcyYXyogo9xgQqWAxkTNq` runs on Claude Desktop (Windows) with access to
that computer, so its prompt can only change with Austin's approval given in a
conversation connected to that machine. `update_trigger` was called and returned
`needs_device_approval`; **nothing was changed**. The live routine still runs its
seven-item prompt with no slip section.

To apply it: in a Claude conversation on the Windows desktop, ask for this
routine's prompt to be replaced with the text below, or edit the task there
directly. Do **not** delete and recreate the routine — that discards its run
history and its binding to the computer.

The only differences from the live prompt are a new item 8, and one clause in the
delivery paragraph allowing that section its own page. Items 1 to 7, the three
hard rules and the tracker-export paragraph are untouched.

---

Build the pre-call pack for Austin's Weekly Rehabs Call (Wednesday 10:00–10:30 ET, organised by Jon Wyss, with Mark Doucette of High Pace, John Clark, Natalie Magurne and Leslie Croft).

Read `70-Operations/rehab-program/weekly-call.md` in the "My Brain" folder first — it carries the standing agenda, the order the items go in, and the two rules on that agenda. Then read `overview.md` and `wip-and-invoice-model.md` in the same folder for the data contract.

Build the pack in agenda order off the newest CSV in `70-Operations/rehab-program/data/`:
1. The two board numbers — rehabs completed YTD against 100+, and the 60-day turn rate.
2. Every open unit past 60 days, unit by unit, each needing a date or an escalation rather than a status.
3. Approvals sitting, oldest first.
4. Open units with no start date, with the modelled scope attached.
5. Open units with no vendor.
6. Completions to hand off to Leslie or Natalie.
7. Decisions Austin owes, read off `00-Meta/parked-decisions.md` — `PD-24`, `PD-25` and `PD-26` are the rehab ones.

8. Dates that moved later. Append this as the LAST section, after the seven agenda items. It is new and is not in `weekly-call.md`, so do not renumber or reorder anything above it, and if it cannot be produced in time ship the pack without it and say so — the seven agenda items come first.

   Generate it fresh. Do not read a committed copy: a week-old slip file is exactly the thing this is meant to catch. The code is in the `parakeetberk/My-Brain` repo, branch `claude/property-ops-dashboard-ad8eyk` — attach with `add_repo`, then `git clone --depth 1`. Read the "Pushed dates: the slip watcher" section of `docs/PLATFORM_SPEC.md` before running anything. **Do all of this in the session container, not on the desktop** — this routine has device access for the vault, but the pipeline, the clone and the Python runs belong container-side. Nothing in this section touches `C:\Users\AustinBerk`.

   - Pull every `Asset Listing_YYMMDD.csv` from SharePoint dated after the newest `observed` date already in `data/date_slips.json`. They are in Birdcage → Data Analytics → Rent Manager → Historical Asset Listing; find them with `sharepoint_search` (query "Asset Listing", fileType csv) and read each with `read_resource` on `file:///b!xyOQz3MDX0KO4DwwD8HVIt10RnZ14ehEpxBSsCZX7QBJfg0Odv_GQ7Z2fmJye92a/<itemId>`. Each is ~1.4MB and spills to a VM file the tool result names; copy those into `pipeline/incoming/asset_listing/` under their real `Asset Listing_YYMMDD.csv` filenames and parse from disk, never by pasting rows. Use a subagent if context is tight.
   - Run `python3 pipeline/slip_watch.py scan`, then `python3 pipeline/slip_pack.py`. Paste `data/pre_read_slips.md` into the pack as it stands. It is already written to length and carries its own caveats; do not summarise it or rebuild the tables by hand.
   - Commit the updated `data/date_slips.json` and push to `claude/property-ops-dashboard-ad8eyk`. No pull request. The ledger is append-only and cumulative drift per home only accumulates if each week's scan is committed.
   - If SharePoint is unreachable, or no new file has landed, say so in one line and print the section off the existing ledger — it will correctly report the older window. Never re-date a file forward to make it look fresh, and never treat a byte-identical snapshot as a failed pull; weekends and holidays produce them legitimately.

   Two things this section must never say. **It is not a vendor scorecard.** `UDF: Req Delivery Date` is written only by the Cavco import, so every requested-delivery slip is Cavco by construction, and Cavco's zero-day median slip is Cavco measured against itself rather than evidence it beats anyone. **And do not ask Mark Doucette about delivery slip.** Champion Construction preps sites and sets homes; it does not deliver them. Its measurable work is the fifteen setup stages, and of 1,745 assets only 50 carry a single real setup-stage date, which is a data-capture conversation before it is a performance one.

Three hard rules. **Never present `expected` or `remaining` as budget** — they are tier averages off as few as six comps and the pack labels them `model`. **Never show an unresolved community code as a real community** — `NGMH`, `LS` and `PPH` render as UNRESOLVED, never guessed. **Diff every item against `99-Archive/` and `00-Meta/commitments.md` before Austin sees it**, per CLAUDE rule 11 — the absence of a written reply is not evidence something is open.

Also check whether a fresh tracker export has arrived in `05-Inbox` or by email since the last pull. If one has, file it into `data/` under its own as-of date without overwriting the previous export, rebuild with `build/make_data.py` then `build/assemble.py`, republish the dashboard to https://claude.ai/code/artifact/34a291f1-59a7-4d4b-952c-3bf5404eaa87, and say in the pack which gaps closed and which widened since the prior export. If no new export has arrived, say so plainly and note that the pack is running on data that is now N days old.

Deliver the pack as a message in the chat plus a markdown file in `70-Operations/rehab-program/`, named `pre-call-YYYY-MM-DD.md`. Keep the seven agenda items to one page; the pushed-dates section sits after them and is allowed its own. Log the run in `00-Meta/log.md`.
