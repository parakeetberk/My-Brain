# DRAFT — Migration handoff to Albert

**Status**: Not sent. Review and send from your own mail client. Attach or link `brain/10-Business/sharepoint/migration-risks.md`.
**Drafted**: 2026-08-26

---

**To**: Albert
**Subject**: Before you get to site plans — findings from the storage audit

---

Albert,

I had a full audit run across SharePoint, Dropbox, OneDrive, and Google Drive this week — about 3.3 TB, every surface. It turned up several things that will bite the Birdcage migration if you hit them cold. Full brief is attached; this is the short version.

**Three things not to touch until you've read the brief**

1. **`/sites/ParakeetHome` and `/sites/ParakeetHomes` are both real sites, one letter apart, and neither is a superset of the other.** Singular has 29 communities, plural has 24. Of the 19 that overlap, five differ materially — Northgate is 219.8 MB larger on singular, Harbour 105.4 MB larger, Lucky Clover 244.9 MB smaller. Ten communities exist only on singular, five only on plural. If either one gets collapsed into the other, we lose data. They have to be merged community by community.

2. **Construction folders are not duplicate site plans.** `main/Construction/BAY OAKS VILLAGE I` looks like a fourth copy of the Bay Oaks plans. It isn't — it's the construction record: contracts, development, projects. Same for other communities.

3. **`_Archive Communities` contains five currently-owned assets.** 46.5 GB, and they're distinguished from the live folders only by a leading underscore.

**What is safe to collapse**

The actual site-plan duplication is a verified three-way byte-identical clone across ParakeetHomes, the Cavco satellite, and `main/.../Cavco Homes/Plans for Sites` — 27 Bay Oaks lot folders at exactly 812,391,202 bytes each. **Keep `/sites/ParakeetHomes`**; it's the source of the copy chain and the only complete tree. The pattern holds for 22 of 23 shared communities, about 16.6 GB. Lake Saunders is the one exception — check it by hand.

There's also a clean 4.71 GB win: the flood elevation certificate folders under `Asset Management & Finance` and `Construction` report identical byte totals.

**Don't build a new taxonomy — one already exists and is half-built**

`Folder Structure Tracker_Outline.xlsx` in my OneDrive root is a 6,051-row, 9-level structure: 12 departments, 224 level-4 folders, 79 distinct filename conventions, and 45 communities — 43 of them structurally identical. Reconcile against it rather than starting over; it answers the folder question and the naming question together.

Four things about it before you build from it:

- **Build from `APPLE CREEK`, not the blank `PROPERTY NAME (CITY, STATE)` template.** The template is stale — it's the only block missing `ASSET MANAGEMENT/CLOSING DOCUMENTS/LOAN DOCUMENTS`.
- **Ignore the status column entirely.** Only 54 cells are filled — about 2% — covering three communities, and it's three years stale. There's a second worksheet with a different, incompatible scheme that also stops at "Applegate." Re-audit against live SharePoint instead of trusting either.
- **There are nine typos that will propagate into real folder names**, including `SITE VISTS & INSPECTIONS` in all 46 blocks. Fix them at build time — renaming live folders later is much worse. One filename convention also contains a slash (`Property Name_Violation/Inspection_...`), which is illegal in SharePoint and has to be rewritten.
- **2,210 of the 2,323 folder nodes are the same 47 folders repeated 46 times.** Worth deciding whether that should be a metadata-driven library — one library, community as a column — instead of physical duplication. Physical duplication is what produced the mess we're cleaning up.

Fair warning on provenance: I wrote this thing in three days in September 2023 and never touched it again. No sign-off, no version. There's a larger copy in Teams Chat Files, so it was circulated — worth diffing before you commit to the version in my OneDrive.

**Two things that will get missed if scope is set from the connectors**

- **Three SharePoint library sync shortcuts don't show up in the Graph file API** — `Parakeet Communities`, `Parakeet Birdcage - Corporate`, and `Parakeet Birdcage - Data & Analytics`. They're the most current and most structured branches on the drive, and we only found them through the local sync folder. Assume the same blind spot on other people's drives.
- **Three corporate Google Shared Drives sit under my personal Gmail** and are invisible to standard audit queries — Shared Drive files carry no owner field. They hold about 30 community folders, Parakeet ops material, and A2Z fund records. All MH content, all needs to come to Birdcage. There's no way to enumerate Shared Drive memberships, so treat three as a floor.

**One thing worth doing while we're moving anyway**

Operations and Construction each have 71 community folders, and they are not the same 71. Six exist in one and not the other, four the reverse, and eight are spelled differently — including a typo, `WHSIPERING PINES MA`. Any report that joins on community name is silently mismatching about 18 assets right now.

Migration is the only moment renaming is free. If we normalize to one canonical community list as part of the move, that defect goes away. If we don't, it follows us into Birdcage and we live with it for years.

**Also flagged**

- Dropbox has what may be the only copy of the Lamberton Lake LP syndication records, filed under `Business Lines/Bedrock Group/Entities/Bedrock EM Holdings/Holdings/Lamberton Lake/`. Lamberton is under active sale. Please confirm those exist elsewhere before anything decommissions Dropbox. (The Dropbox folder actually *named* `Lamberton Lake DD Files` is empty — ignore it.)
- Permissions: sensitive material is currently co-located with broadly-shared folders — HR and payroll, a cap table and §83(b) files in `Executive/`, buyer PII in closing files. Migration is the moment to re-point permissions rather than replicate what exists. No permission audit has been run yet.
- Birdcage already holds 23 GB of prior analytics work under `Claude Cowork`. Worth deciding whether incoming volume merges into that structure or sits alongside it before bulk volume lands on top of it.

**Caveats on all of the above**

Duplication was established from folder byte-totals, not content hashes — strong evidence, not proof. Nothing was opened; sensitivity is inferred from names and paths. The `External/` listing is truncated past "S" because the API caps at 200 children with no pagination.

Everything was read-only. Nothing has been moved.

Shout if you want to walk through any of it before you keep going.

Austin
