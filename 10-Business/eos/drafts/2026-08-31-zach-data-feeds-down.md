# Draft email — Zach, both Rent Manager data paths are down

**Status:** draft, not sent. Austin's review only.
**To:** Zach Schwartz
**Cc:** Justin Minkoff
**Subject:** Both Rent Manager data paths are down

Zach,

Building the community sheets this weekend I tried to pull live numbers and got nothing from either route.

The RentViewer data warehouse timed out at 60 seconds on every query. Not a big query either. A single measure grouped by property timed out the same as a five measure one. Occupancy, aged receivables, rent roll, all of it.

The Rent Manager report API returned HTTP 500 on FilteredIssueList and on UnitAvailability. The metadata endpoints work fine, so I can list reports and pull the property IDs, but nothing that actually runs a report comes back.

The daily CSV exports still land in my inbox, Issues, UnitListing, AssetListing, Move In Move Out, SummaryRentRoll. Those are fine. But the attachments can't be read programmatically, so they're only useful to a human opening them.

That leaves us with a gap. Every community page now has a Live block sitting empty, and it stays empty until one of those paths works. I'd rather leave it blank than fill it with a stale number nobody trusts.

Two things I want to know. First, is the warehouse timing out for everyone or just for us over the connector. Second, is there a way to land those daily CSVs somewhere the systems can read them instead of only my inbox. SharePoint would do it.

The join key is already sorted, by the way. I have the Rent Manager PropertyID to ShortName map for all 84 properties and it lines up with the codes in the portfolio table.

Austin
