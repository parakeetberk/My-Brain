# Decision: Storage target state

**Date**: 2026-08-26
**Decided by**: Austin Berk
**Status**: Active, migration in flight

## The decision

**SharePoint Birdcage (`/sites/ParakeetBirdcage`) becomes the system of record for everything manufactured-housing.** All Parakeet, A2Z, and Bedrock files consolidate there. **Albert** owns the migration and is executing now.

**Dropbox becomes the personal and non-MH home** — Belmart, Winterset, Get Real, other investments and financials.

**A2Z Dropbox** serves as archive/sandbox in the interim. End state: nothing MH-related remains in it.

## Resulting architecture

| Domain | Destination | Status |
|---|---|---|
| Parakeet Communities — all MH | SharePoint Birdcage | Migrating (Albert) |
| A2Z MHC — all MH | SharePoint Birdcage | Migrating (Albert) |
| Bedrock — all MH | SharePoint Birdcage | Migrating (Albert) |
| Personal: Belmart, Winterset, Get Real, other investments, financials | Dropbox | Target |
| A2Z Dropbox tenant | Archive / sandbox, then empty of MH | Interim |

## What this resolves

- **The three-identity fragmentation** (Parakeet M365 / A2Z Dropbox / personal Google) collapses to two clean domains: MH in Birdcage, personal in Dropbox.
- **The personal-Gmail governance exposure** — three corporate Google Shared Drives holding cap tables, fund subscriptions, K-1s, an LPA, and executed signature pages — resolves by migrating that MH content into Birdcage. These drives are invisible to standard audit queries and were found only by walking parent chains; they must be explicitly added to Albert's scope or they will be missed.
- **Lamberton Lake LP syndication records**, currently possibly single-copy in Dropbox, come under governed storage.

## What this does not resolve, and must be handled during migration

Consolidation is the one moment when these are cheap to fix. After the move they calcify.

1. Community name normalization — ~18 assets currently mismatch between Operations and Construction, including typos
2. The `/sites/ParakeetHome` vs `/sites/ParakeetHomes` divergence — must be merged by content, never collapsed by picking one
3. Permission hygiene on sensitive material currently co-located with broadly-shared folders
4. Distinguishing genuine duplicates from records that merely look like duplicates

See `brain/10-Business/sharepoint/migration-risks.md` for the operational detail.

## Open question

Birdcage already contains `Data  Analytics/Claude Cowork` (23.07 GB), including a `Corporate` branch of 19.04 GB that is under survey now. Whether the incoming migration should merge into that structure or sit alongside it is undecided, and worth deciding before bulk volume lands.
