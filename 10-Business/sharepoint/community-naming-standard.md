# Community naming standard

**What this is:** the governing rule set for how a community is named in Birdcage, and the mapping table that gets it there. Adopted by Austin 2026-08-31 against a live read of both source trees.

**Status:** current - 2026-09-04. **The project is ON HOLD** ([[15-Projects/sharepoint-restructure/overview]]); the rulings on this page stand. **LOCKED on the seven rules below** - they are Austin's own rulings, recorded verbatim in intent. The mapping table is working material and may be corrected.

**Artifact:** `https://claude.ai/code/artifact/2d7225e8-a4f1-48ec-b91b-aebbb4f550d2`

---

## THE CONSTRAINT — read this before touching anything

**Austin, 2026-08-31: "Do not touch the construction folder."** And: **"nothing in the parakeet communities sharepoint should be edited rename etc without permission."**

`/sites/main/Shared Documents/` — the whole Parakeet Communities SharePoint — is **read-only** for this Brain and for anyone acting on it. No renames, no moves, no deletions, no edits, not even the obvious typo fixes, without Austin's explicit permission per action.

**Every rule below is a rule about Birdcage.** Normalisation happens on the **write into `/sites/ParakeetBirdcage`**, never as an in-place edit of the source. That means:

- The 21 name mismatches are a **mapping table**, not a rename list. Source name on the left, canonical Birdcage name on the right. Nothing is renamed where it sits.
- The three city misspellings are corrected **in the destination name only**. `Nalls Ct (Celwiston, FL)` keeps its name at source forever.
- The two 0-byte Construction folders are **not migrated**. They are not deleted.
- `INLAND VILLAGE - POSSIBLE` **lands under Acquisitions in Birdcage**. It is not moved at source.
- `__SITE ELVATION CERTIFICATES` is written to Birdcage spelled correctly, once, deduplicated against the byte-identical Asset Management copy. Neither source copy is touched.

This supersedes the earlier framing of this work as a rename pass. **It is lower risk and it is the right call**: renaming live folders breaks saved links, Power Query paths and Teams tabs on a system 125 people are working in today, and a migration write breaks nothing.

---

## The seven rules — Austin's rulings, 2026-08-31

1. **Folders: `Community Name (City, ST)`.** One canonical string per asset, byte for byte identical across every branch of Birdcage. *Austin: agree for folder names.*
2. **Title case. Never ALL CAPS.** *Austin: agree.* Caps hid the `WHSIPERING PINES MA` typo for months and defeat case-sensitive matching.
3. **City and state do the disambiguating, never a bare state suffix.** *Austin: OK.* `WHISPERING PINES FL` and `WHSIPERING PINES MA` are two different properties in two different states; a suffix is not enough to keep them apart and a fuzzy match will merge them.
4. **Files carry the community name alone. Folders carry the community name with city and state.** *Austin, verbatim intent: "Always go by community name for files and community name with city and state for folders."* This replaces the earlier draft rule about asset-type suffixes. The consequence: there is exactly **one** canonical community name per asset, it is what a file is named by, and the folder is that same name plus ` (City, ST)`. Whether `MHP`, `MHC` or `RV Resort` is part of a given community's name is therefore a question about the canonical name itself, decided once per asset on the canonical list, not a folder-naming choice.
5. **Single spaces, no trailing spaces, city spelling verified.** *Austin: agree.* `GEIGER KEY MARINA  RV` carries a double space at source - invisible to a reader, fatal to an exact match, and the reason the 2026-08-26 survey recorded Geiger Key as having no Construction folder.
6. **No leading underscores anywhere. One naming convention plus metadata for everything.** *Austin, verbatim intent: "remove all underscores at the front. everything needs the same naming convention and meta data."* This **reverses** the earlier draft rule, which would have kept underscore prefixes on non-community folders. Sort order and classification move from the folder name into SharePoint library metadata. **See the sequencing risk below - this rule has a prerequisite.**
7. **The canonical list lives in one governed place and changes only at migration.** *Austin: OK.* After cutover, renaming a live Birdcage folder breaks every saved link and query path pointed at it.

---

## The hole in rule 6, and it has to be closed first

Rule 6 is the right end state and it cannot be applied first. The leading underscores are currently doing real work that nothing else is doing:

- **`_Archive Communities` is 114.4 GB** and the only thing separating 36 disposed assets from 71 live ones is a leading underscore. Five assets — Congress, Central, Crystal Acres, Everglades, Wolf Bay — exist in **both**, distinguished only by a run of 4 to 5 underscores.
- The Operations root holds 71 community folders plus roughly 24 operational folders. Strip the prefixes and it is a flat list of ~95 undifferentiated folders in alphabetical order.
- ~~The numbered community subfolder template is an open question.~~ **ANSWERED 2026-08-31: the numbers come off too.** Rule 6 extends to numeric prefixes, on Austin's reasoning: **permissions trim the view**, so a group with WRITE on only part of the template sees a numbered sequence with holes in it. Offshore-Ops sees `1, 2, 7, 8`; Offshore-AcqAM sees `1, 2, 3`. Missing numbers read as missing folders. The cost is near zero — alphabetical order reproduces the numbered order exactly except that Construction and Facilities swap third and fourth.

**So the sequence is: define the metadata columns in Birdcage first, then drop the prefixes.** At minimum a document library needs `Community`, `Status` (active / archived / prospect), `Department` and `Record Type` as real columns with default views built on them, before any name loses its prefix. Dropping prefixes before the columns exist trades a working sort hack for no organisation at all.

**Answered 2026-08-31: rule 6 covers numeric prefixes as well as underscores**, for the community subfolder template. Austin's reason is permission trimming rather than tidiness, and it is the stronger argument: scoped access makes a numbered list look broken. The Birdcage template is now unnumbered at [[10-Business/sharepoint/target-structure]] and in [[10-Business/sharepoint/permissions-matrix]].

**The prerequisite still stands for the underscores.** Numbers were safe to drop immediately because alphabetical order preserves the sequence. Underscores are not — they are still the only thing separating 114.4 GB of archived communities from live ones, and they come off only once the metadata columns exist.

---

## The facts, verified live 2026-08-31

- **Operations 71 community folders, Construction 71.** Not the same 71; the matching counts are a coincidence.
- **66 assets exist in both branches.** 46 already match once case and city/state are set aside. **21 do not** and need a mapping row.
- **5 assets exist only in Operations**: Apple Creek (Bismarck, ND), Countryside (Mandan, ND), Parktown (Mandan, ND), Shell Pointe (Ruskin, FL), Shirley's.
- **4 folders exist only in Construction**: `AVALON MHP` (0 B), `CREEK WOOD` (0 B), `INLAND VILLAGE - POSSIBLE` (8.3 MB), `LAKESIDE ESTATES` (6.7 MB).
- **30 of 142 community folders fail an exact-name join.** The earlier recorded figure of ~18 was wrong - see the correction on [[10-Business/sharepoint/migration-risks]].
- `Shirley's` is the only community folder in either branch with **no city or state**.
- Three Operations folders misspell their own city: `Celwiston`, `Canavaral`, `Symrna`.
- Two non-community folders sit unprefixed among the 71 communities in the Operations root: `Invoice Gathering` and `October 26 strom damage`, the latter a 0-byte duplicate of `_October 26 strom damage` (91 MB).

## What this does not settle

Canonical **spelling** and canonical **membership** are different questions. 66 assets exist in both branches, [[60-Communities/portfolio]] carries 67 rows, and Austin's 2026-08-26 reporting rules exclude three of those. Membership is the open P3 ruling, not something this page decides. Nine folders also cannot be resolved from a folder tree at all and are owed by Austin — the three North Dakota assets, Shell Pointe's status, what `Shirley's` is, whether `LAKESIDE ESTATES` is an asset, and whether Bay Oaks I and II are one asset or two.

## Decisions

- **2026-09-04 — the six unresolved canon rows are ruled. Austin.** These are the rows the migration tracker itself marked *"Austin rules at Gate 0"* or `UNRESOLVED`, and they close the judgment half of GATE 0 criterion 02.
    1. **`Bay Oaks Village I & II (Panama City, FL)`, code `BAYO`** — one folder, superseding the prior list's two codes `BOV1` and `BOV2`. *Austin: "Bay Oaks I & II should be combined for the folder but still separate as far as leases."* **The separate fillable leases for I and II stay separate inside `6-Legal / Lease Agreements`**, so that filing convention needs a I/II token. Knock-on: per-community groups `#20 Bay Oaks Village I` and `#21 Bay Oaks Village II` collapse to one, taking the group count from 68 to **67**.
    2. **`Great Oaks (Kissimmee, FL)`, code `GRTO`.** *Austin: "For Great Oaks its just Great Oaks."* One asset, one name. Retires rule 4's standing warning that *"Great Oak and Great Oaks are not the same thing"* — corroborated by [[60-Communities/great-oak-rv-resort]], same city, JREFII, 198 RV units. Knock-on: per-community group `#33` is named `Great Oak` and must become `Great Oaks`.
    3. **`Hendersons (South Bay, FL)`, code `HEND`.** Closing `EX-003` inside its 48 hours. Birdcage and the Property Data Sheet both say South Bay, and the row's own county field reads Palm Beach — South Bay's county, where Clewiston is in Hendry. The Clewiston reading most likely leaked from Royal Palm and Everglades, both genuinely Clewiston assets.
    4. **`Gulf Breeze (Hudson, FL)`.** *Austin: "Gulf Breeze (Hudson, FL) is the way to go."* The bare `Gulf` folder merges into it. The per-community group is already named `Gulf Breeze`, so no group rename here.
    5. **`Parkwood (Columbia, SC)`, code `PRKW`, and `Parkwood (Winston Salem, NC)` are two different communities and never merge.** *Austin: "two different communities. do NOT merge."* Hard-codes rule 4's own example. SC is live under Operations; the divested NC asset routes to `Archive / Divested Communities`. The group named `Parkwood Mobile Home Park` must be renamed to resolve unambiguously to SC.
    6. **`Riviera (Miami Gardens, FL)`, code `RIVI`.** *Austin: "Keep Riviera."* The Jadian tree's `Riviera Park (Miami, FL)` is an alias, not a second asset, and is aliased on the write rather than migrated as its own community.

- **2026-09-04 — three mechanical items still stand between this and a signed canon**, and all three change what gets provisioned. Not judgment calls. **(a)** The tracker's code-change count contradicts itself: the header says 17 codes differ from the prior ratified 64-property list, the sheet marks **25** rows `CHANGED`, and files already renamed in the American pilot carry `WPES-`, `MAYF-` and `MONS-` prefixes that are non-compliant against the new codes. **(b)** The per-community group count is **67**, not the 68 GATE 0 criterion 04 states. **(c)** **18 of the 68 per-community group names fail a character-for-character match against the canonical names** — mostly typos and suffixes, but three are genuinely ambiguous: `Silver Hill MHC` against canon `Silver Hills`, `Silver Breeze` against canon `Silverbreeze`, and a bare `Whispering Pines` that could be the Titusville FL or the Auburn MA asset. **This is a third cut of the same problem**, alongside the 21-row mapping table and the 30-of-142 join failure recorded above: those compare source trees to canonical, this compares group names to canonical. **The three should reconcile to one list.**

- **2026-09-04 — held.** Austin put the SharePoint Restructure on hold the same day: *"put this all on hold as it won't be covered on EOS today."* The rulings above stand; the canon signature does not. See [[15-Projects/sharepoint-restructure/overview]].

## Related

- [[10-Business/sharepoint/target-structure]] — the Birdcage tree these names land in
- [[10-Business/sharepoint/migration-risks]] — carries the corrected figures and the original understated claim
- [[70-Operations/sops/folder-and-file-intake]] — the SOP that keeps new material compliant
