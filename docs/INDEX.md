# Where things live, and which thread owns them

Read this first. It exists because the work is split across three sessions and
each one has to pick up cold without re-deriving what is already settled.

Updated 2026-09-09.

## The three threads

| Thread | Owns | Cadence | Audience |
|---|---|---|---|
| **Daily Ops** | the weekday refresh, the live dashboard, source freshness | every weekday morning | Austin, five minutes |
| **Platform Build** | capture layer, baselines, alerts, the three views, data integrity | weeks | nobody yet; it is plumbing |
| **Home Pipeline** | date slips, rehab and demo throughput, Cavco and Champion | Tuesday pre-read, Wednesday call | Jon, Mark Doucette, Natalie, Leslie |

The split is by **cadence, not subject**, on purpose. Subject splits leak: the
asset-listing work is where the Campspot revenue answer came from, and the
routing work is where naming mismatches turned out to be systemic rather than
three coincidences. Cadence splits hold because they match when the work
actually happens.

## Which document owns which decision

| Document | Owns |
|---|---|
| `ARCHITECTURE.md` | why the live URL is an Artifact, the two-period model, the reportable gate, the financials as-of stamp, the candlestick, scope filters, the flag ledger |
| `PLATFORM_SPEC.md` | the four platform decisions, the snapshot store, day-of-month and same-store normalisation, the alert model, routing, the throughput tab, freshness rules |
| `SOURCE_CONSOLIDATION.md` | warehouse against Rent Manager, the $513K AR gap, the RV revenue found in the reservation feed, the roster dropping RV-side records |
| `pipeline/queries.json` | every pull, its row limits, and the two truncation hazards |
| `pipeline/sources.json` | which provider serves which dataset, and the switch to flip when a connector comes online |
| `pipeline/community_emails.json` | the 64 community mailboxes, the shared inboxes, the Silver Breeze rename |

## Live surfaces

- **Ops dashboard** (the team reads this as fact) —
  `https://claude.ai/code/artifact/253e4ada-1234-4ff5-94f1-979099ed2dc1`
- **Home pipeline sandbox** (static preview, not wired) —
  `https://claude.ai/code/artifact/61931de0-56e2-45a4-94c1-1602a8faad9a`

Never publish a stale or partial payload to the first one.

## Open items, and who owns them

**Austin**
- Verify the 64 community addresses actually deliver. Nothing has been mailed.
- Get `dw_prospects` exposed to the warehouse connector. It is the only thing
  blocking the funnel work.
- Explain nothing further about Space Coast Village — answered: it is the
  Silver Breeze rename.
- Decide whether the disposition bottleneck is pricing, marketing or staffing.
  The data says where the constraint is, not why.

**Daily Ops thread**
- Rebuild the weekday routine as fresh-session-per-fire. It is currently bound
  to the session that created it and will die with it, exactly as
  `trig_01UXCQEFF7Hj3CQHouDz9oss` already did. Corrected 15-file pull list,
  push and email notifications.
- The roster on disk was built 2026-09-04; the PDS changed 2026-09-08. Rebuild
  and diff it, do not build on it silently.

**Platform Build thread**
- Backfill the 387-file asset archive for real slip and duration history.
- Build the capture step. `daily_facts.json`, keyed on snapshot date.
- Same-store cut on every trend. Nothing does this today and it is the most
  likely source of a wrong conclusion on the current page.
- Watch the AR reconciliation ledger for whether the gap tracks drift.

**Home Pipeline thread** — all three closed 2026-09-09, see `PLATFORM_SPEC.md`
- ~~The 71 assets with no community~~ → 59 recovered from `Financial Property`,
  a column the map never read. 12 left, all disposed sales history. The 45 demos
  were not idle: 41 have a replacement home already ordered or delivered.
- ~~Feed the slip report into the Tuesday pre-read~~ → `slip_pack.py` renders the
  section; the Tuesday routine regenerates it weekly.
- ~~Champion delivery performance is unmeasurable~~ → wrong question. Champion
  Construction is the site-prep contractor, not a manufacturer, and
  `Req Delivery Date` is written only by the Cavco import. **Skyline** is the
  manufacturer that is actually unmeasured.

Now open instead:
- **Someone owns telling Rent Manager to stop blanking `Property`.** The pipeline
  works around it; the field is still wrong at source, and Vantage Oaks alone
  accounts for 20 of the 45.
- **Build a Skyline import** for `Req Delivery Date`. Same shape as the Cavco
  one, 30 homes in the pipeline with no commitment date to measure against.
- **Recut the demo pace against 91, not 136.** 45 of the 136 have a home coming;
  the stalled backlog is the 91 with nothing coming.
- **Austin: the Cavco zero-day median is Cavco measured against itself.** It is
  not a vendor win and should not be presented as one on the call.

## Things that will bite whoever touches them

**The alias map is load-bearing and silent.** Three mismatches surfaced in one
week: `Hunter Springs MHC` against `MHP` dropped seven live assets,
the roster has no RV-side rows so 301 sites at Northgate and Paradise Lakes fall
out, and Silver Breeze is mid-rename. A typo here removes a park from the
numbers with no error anywhere.

**`whisperingpines@` is Florida and `whisperingpinesma@` is Massachusetts.**
Reads backwards. Do not tidy it.

**Three inboxes serve two parks each** — Bay Oaks 1 and 2, Regency 1 and 2,
Northgate MH and RV. Any message must name the community in its subject.

**The capture keys on the snapshot date, never the run date.** An unrefreshed
feed must cost a day of history rather than fabricate one. A missing day is
recoverable; a fabricated day cannot be told from a real one.

**Never re-date a file forward to make it look fresh.** Same reason.

**Assets carry three kinds of community**, not two: `current`, `historical`
(sold or an `x`-prefixed retired duplicate — sales history only) and
`unattributed`. Counting historical inflates every current-inventory figure;
filtering it erases real sales.

**`Property` goes blank when a record is superseded; `Financial Property` does
not.** That one column was hiding 59 assets, 45 of them demos. Anything reading
`Property` alone undercounts. `community_source` says which field answered.
