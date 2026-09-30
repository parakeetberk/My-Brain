---
type: reference
tags: [type/reference, community/all]
---

# The Community to Lot to Asset model

**What this is:** the three levels this folder is built on, the tag vocabulary that makes them queryable, and the rule for when a page gets created. Read this before adding anything to `60-Communities/`.

**Status:** current - 2026-08-31

## The three levels

**Community** is the asset we own and hold. One page per community, always. 67 of them. The page opens with the hot sheet: snapshot, watch list, pulse, live block, then the detail. `60-Communities/<slug>.md`.

**Lot** is the rentable unit. A lot page is created **only when something is happening on that lot** - a rehab scoped, a home delivered, a set blocked, an issue raised. There are 6,379 lots in the portfolio and a page for every one of them would be a graveyard. 99 lots have a page today because 99 lots have real, lot-level activity. A source line whose lot column holds a count or a place, not a lot, files against the community instead. `60-Communities/lots/<CODE>-<lot>.md`.

**Asset** is the home. Homes move between lots, get sold, get demoed. An asset earns a page when it has an identity that outlives the lot - a serial number, a Cavco order or quote number, a Rent Manager asset ID - **and** something about it is in dispute or in motion. Ten have one today. `60-Communities/assets/<id>.md`.

The relationship is not a folder tree, it is a link. A lot page names its community. An asset page names its community and its current lot. That way a home moving from Northgate Lot 98 to Riverwalk Lot 130 is an edit to one page, not a file move.

**Project** is a funded piece of capex or infill work, identified by its Adobe Sign document number, which the kickoff and the closeout share. A project attaches to a community and sometimes to a lot. Projects are not created per community page; they all live in one ledger at [[60-Communities/projects]], because the questions asked of them are cross-portfolio ones: what is running, what finished, what came in over.

## The tag vocabulary

Every lot, asset and register page carries YAML frontmatter. These are Obsidian properties, so Dataview and Bases can query them directly.

| Property | Values |
| --- | --- |
| `type` | `community`, `lot`, `asset`, `project`, `activity-log`, `register`, `reference` |
| `community` | the community slug, e.g. `fox-creek` |
| `lot` | the lot number as a string, e.g. `"46A"` |
| `code` | the community short code, e.g. `FOX` |
| `status` | `open` or `closed` at page level; individual items carry `open`, `in-progress`, `complete`, `blocked`, `decided`, `decided-not-actioned` |
| `categories` | one or more of `rehab`, `infill`, `delivery`, `lot-prep`, `maintenance`, `utility`, `compliance`, `title`, `sales`, `resident`, `capex`, `demo`, `other` |
| `open_items` | count of items still open on that page |
| `last_activity` | date of the newest item |
| `asset_id`, `id_kind`, `asset_state` | asset pages only |

Tags mirror the properties so Graph View and tag search both work: `community/<slug>`, `type/<level>`, `status/<state>`, `category/<category>`, `asset/<id_kind>`.

## What `decided-not-actioned` means

It is the most valuable state on this page and it does not exist in Rent Manager. It marks something that was agreed in a meeting - a decision, out loud, with people nodding - and then nothing happened. No owner, no date, no budget. Those are the cheapest items to close and the ones that quietly rot. They are counted separately in [[60-Communities/open-items]].

## Market rent comparables

**MH & RV is one asset class, benchmarked against single-family homes and apartments.** Austin, 2026-08-31: *"as we discuss market rents, we usually just say MH & RV vs single family home or apartments."* This is the house convention for discussing market rents, so "MH & RV" in a transcript or a note is a comparable set and not a reference to RV inventory at a specific community.

**It is not cosmetic.** In the Massachusetts class settlement (`00-Meta/commitments.md` item 20) the whole case turns on whether a stated lot rent is a fair market rental rate, and the benchmark chosen decides the answer: MH & RV against apartments and single-family rentals reads very differently from MH & RV against other manufactured housing communities in the same market. Anyone instructing an appraiser or a valuation consultant is choosing that set.

## The rule for adding

Claude writes these pages, not humans. A new item arrives from email, Teams, a transcript or Rent Manager. It gets a community. If it names a lot, the lot page is created or appended. If it names a home with an identity and that home is in dispute, the asset page is created or appended. The community page's Pulse block and the open-items register are rebuilt from the whole set, never edited by hand.

The procedure is [[90-Skills/community-pulse-refresh]].

## Sources

- [[60-Communities/activity/2026-08-stream]] - the full activity stream all of this was built from.
