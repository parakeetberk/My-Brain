# Media move manifest, 20-Brand-Marketing to SharePoint

**Why this page exists.** On 2026-09-29 Austin ruled that the marketing media leaves this vault for SharePoint, **approved per file or per set, not in bulk**. The files are already out of git (see `.gitignore` and `KP-0132` in `00-Meta/open-items.md`), so nothing here blocks the GitHub backup. This page is the approval list. Sizes measured 2026-09-29, VERIFIED from disk.

**How to approve.** Reply with the set ID and a destination, e.g. *"M3 go, Birdcage Marketing"*. Claude confirms the exact folder against `10-Business/sharepoint/community-naming-standard` before anything moves. The Parakeet Communities SharePoint stays read-only; all writes land in Birdcage.

**Links.** No page in this vault embeds any of these files (searched 2026-09-29; only audit and register text mentions the folders), so moving them breaks nothing.

**Upload route.** Files over about 250 MB (the drone videos) are too large for the SharePoint connector. Those go through the OneDrive sync of the Birdcage library, or through Albert. The vault copy is removed only after the SharePoint copy is confirmed, and only with Austin's yes (hard rule 2).

| ID | Set | Size | Files | Note | Status |
|---|---|---|---|---|---|
| `M1` | `assets/community-photos/Applegate/` | 1,778 MB | 86 | **Six High Rez photos exist twice**, in `Applegate/High Rez/` and `Newmark Refi Photos (3.11.2024)/High Rez/`. Move one copy | awaiting Austin |
| `M2` | `assets/community-photos/Auburn Ridge/` | 3,188 MB | 41 | Five aerial videos, 265 to 669 MB each | awaiting Austin |
| `M3` | `assets/community-photos/Bay Oaks Village I/` | 1,969 MB | 183 | Rebrand in progress, check with Leslie which are current | awaiting Austin |
| `M4` | `assets/community-photos/Bay Oaks Village II/` | 1,797 MB | 152 | Same as M3 | awaiting Austin |
| `M5` | `assets/community-photos/Belle Haven/` | 1,229 MB | 1 | One file, `360 Orbit AD.MP4` | awaiting Austin |
| `M6` | `assets/community-photos/` loose files | 8 MB | 3 | | awaiting Austin |
| `M7` | `branding-assets/Parakeet/` | 270 MB | 87 | Brand guide PDF is stored twice (73 MB each) plus a 72 MB zip of it | awaiting Austin |
| `M8` | `branding-assets/Community/` | 93 MB | 7 | Space Coast Village and Vantage Oaks logo zips | awaiting Austin |
| `M9` | `branding-assets/Logo Files PNG (2026-09 quickbase drop)/` and 2 loose files | 1 MB | 21 | Small, could stay in the vault | awaiting Austin |
| `M10` | `brochures/` | 427 MB | 32 | | awaiting Austin |
| `M11` | `80-Finance/planning/2026-executive-strategy/Parakeet - Executive Strategy Meeting v1.pptx` | 73 MB | 1 | Not marketing; out of git only. Move or keep local | awaiting Austin |

**Total:** about 10.8 GB across 614 files.
