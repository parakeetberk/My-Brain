---
name: utility-cost-per-lot
description: Sewer, WWTP and trash cost per occupied lot by community, 2026 year to date. Read before any utility budget, trash contract or sewer reimbursement question.
sources: [RentViewer Data Warehouse]
---

# Sewer, WWTP and trash cost per occupied lot, 2026 YTD

**As of 2026-08-31. Pulled 2026-09-04 from the RentViewer Data Warehouse** - `VW_Budget_Comparison` for expense, `VW_Rental_Unit_Listing` for occupied units. Workbook: `80-Finance/planning/Sewer-Trash-Per-Lot-2026-YTD.xlsx`.

**Account definitions, and they matter more than they look.** Sewer is `51804 Sewer` plus `51810 Sewer Base Rate`. **WWTP is `51821 Dumping Fee`, `51822 Maintenance` and `51823 Service Call`, and it is shown as its own column rather than folded into sewer**, because at the properties that run their own plant it substitutes for a municipal sewer bill entirely. Trash is `51811 Garbage Base`, `51812 Garbage Overage` and `51813 Roll Offs`. Water, electric, chlorine, water testing, private water and stormwater are excluded.

**The denominator is occupied lots, not people.** Rent Manager holds no reliable occupant head count, so every per-lot figure here is cost per occupied lot per month, computed as the YTD account total divided by occupied lot-months.

## Portfolio, 62 property records with both expense and occupancy

| | YTD | Per occupied lot / mo |
| --- | --- | --- |
| Sewer | $512,306 | $12.90 |
| WWTP | $347,979 | $8.76 |
| Trash | $967,838 | $24.37 |
| **All three** | **$1,828,124** | **$46.03** |

Occupied lot-months: 39,712.

## By community, ranked by all-in cost per occupied lot

| Community | RM | Sewer YTD | WWTP YTD | Trash YTD | Lot-mos | Sewer /lot | WWTP /lot | Trash /lot | All-in /lot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Town & Country MHC | `TCMHCPO` | $10,629 | $0 | $38,330 | 288 | $36.91 | $0.00 | $133.09 | **$170.00** |
| Central Mobile Home Park | `CENT` | $21,374 | $658 | $39,073 | 459 | $46.57 | $1.43 | $85.13 | **$133.13** |
| Parkwood Mobile Home Park | `PARK` | $40,448 | $511 | $23,689 | 508 | $79.62 | $1.01 | $46.63 | **$127.26** |
| Palm Spring Estates | `PSEPO` | $17,526 | $209 | $10,992 | 265 | $66.14 | $0.79 | $41.48 | **$108.41** |
| Royal Oaks MHC | `ROYAL` | $0 | $25,193 | $825 | 242 | $0.00 | $104.10 | $3.41 | **$107.51** |
| Harbour Mobile Home Park | `HARB` | $9,259 | $0 | $19,977 | 284 | $32.60 | $0.00 | $70.34 | **$102.94** |
| Ormond Beach Oasis | `OBOPO` | $13,990 | $0 | $17,468 | 318 | $43.99 | $0.00 | $54.93 | **$98.93** |
| Riverwalk | `RW` | $92,825 | $4,485 | $35,038 | 1354 | $68.56 | $3.31 | $25.88 | **$97.75** |
| Silver Breeze | `SILVER` | $0 | $0 | $6,651 | 69 | $0.00 | $0.00 | $96.39 | **$96.39** |
| The Oaks | `TO` | $0 | $74,235 | $29,365 | 1110 | $0.00 | $66.88 | $26.45 | **$93.33** |
| Shady Oaks MHP | `SO` | $2,498 | $675 | $24,400 | 296 | $8.44 | $2.28 | $82.43 | **$93.15** |
| Lake Wales MHC | `LWPO` | $10,514 | $0 | $7,428 | 198 | $53.10 | $0.00 | $37.51 | **$90.62** |
| Carley's Mobile Home Park | `CARL` | $3,375 | $73 | $50,732 | 605 | $5.58 | $0.12 | $83.85 | **$89.55** |
| Wolf Bay MHC | `WOLFPO` | $15,129 | $942 | $11,802 | 326 | $46.41 | $2.89 | $36.20 | **$85.50** |
| Lamberton Lake MHC | `LLMHC` | $17,141 | $0 | $6,748 | 280 | $61.22 | $0.00 | $24.10 | **$85.32** |
| Geiger Key RV Resort | `GEIGRV` | $7,315 | $0 | $20,696 | 330 | $22.17 | $0.00 | $62.72 | **$84.88** |
| Sea Shells Manufactured Housing Community | `SS` | $42,272 | $0 | $14,955 | 723 | $58.47 | $0.00 | $20.68 | **$79.15** |
| Monson | `MON` | $25,156 | $0 | $11,596 | 472 | $53.30 | $0.00 | $24.57 | **$77.86** |
| Applegate MHC | `APPLE` | $0 | $24,963 | $18,566 | 590 | $0.00 | $42.31 | $31.47 | **$73.78** |
| Windward Knoll | `WIND` | $0 | $42,144 | $36,207 | 1092 | $0.00 | $38.59 | $33.16 | **$71.75** |
| Southgate | `SOUTH` | $32,346 | $0 | $11,866 | 618 | $52.34 | $0.00 | $19.20 | **$71.54** |
| Belle Haven | `BELL` | $21,707 | $0 | $8,815 | 439 | $49.45 | $0.00 | $20.08 | **$69.52** |
| J Bar J Estates | `JBJ` | $6,548 | $0 | $44,398 | 799 | $8.19 | $0.00 | $55.57 | **$63.76** |
| Oakside MHP | `OAK` | $33,447 | $575 | $10,851 | 707 | $47.31 | $0.81 | $15.35 | **$63.47** |
| Riviera | `RIV` | $3,690 | $0 | $78,571 | 1304 | $2.83 | $0.00 | $60.25 | **$63.08** |
| Meadow Woods Mobile Home Park | `MWMHP` | $13,829 | $0 | $17,988 | 528 | $26.19 | $0.00 | $34.07 | **$60.26** |
| Mayflower Hills | `MAY` | $0 | $0 | $22,258 | 392 | $0.00 | $0.00 | $56.78 | **$56.78** |
| Redlands | `RED` | $1,050 | $14,819 | $17,858 | 648 | $1.62 | $22.87 | $27.56 | **$52.05** |
| River Oaks RV Resort | `RO` | $0 | $1,950 | $14,885 | 350 | $0.00 | $5.57 | $42.53 | **$48.10** |
| Vantage Oaks | `VO` | $229 | $40,315 | $23,529 | 1355 | $0.17 | $29.75 | $17.36 | **$47.29** |
| Hershey Park | `HP` | $463 | $0 | $27,898 | 600 | $0.77 | $0.00 | $46.50 | **$47.27** |
| Great Oak RV Resort | `GO` | $0 | $29,863 | $20,214 | 1088 | $0.00 | $27.45 | $18.58 | **$46.03** |
| Silver Hill MHC | `SH` | $26,882 | $0 | $11,614 | 855 | $31.44 | $0.00 | $13.58 | **$45.02** |
| Whispering Pines MH FL | `WPMH` | $6,187 | $9,484 | $31,803 | 1057 | $5.85 | $8.97 | $30.09 | **$44.91** |
| Crystal Acres | `CA` | $0 | $0 | $7,287 | 187 | $0.00 | $0.00 | $38.97 | **$38.97** |
| Bay Oaks Village II | `BOVIIPO` | $0 | $0 | $5,731 | 151 | $0.00 | $0.00 | $37.96 | **$37.96** |
| Congress Mobile Home Park *(sold)* | `CONG` | $7,145 | $1,399 | $0 | 248 | $28.81 | $5.64 | $0.00 | **$34.45** |
| Northgate Utility | `NGU` | $0 | $18,278 | $0 | 560 | $0.00 | $32.64 | $0.00 | **$32.64** |
| Palm Haven Estates | `PPH` | $1,815 | $0 | $6,991 | 290 | $6.26 | $0.00 | $24.11 | **$30.36** |
| Su-Rene | `SUR` | $0 | $14,402 | $825 | 541 | $0.00 | $26.62 | $1.52 | **$28.15** |
| Fox Creek | `FOX` | $2,228 | $0 | $20,387 | 812 | $2.74 | $0.00 | $25.11 | **$27.85** |
| Westwood MHC | `WWPO` | $0 | $0 | $8,412 | 320 | $0.00 | $0.00 | $26.29 | **$26.29** |
| Lake Saunders | `LS` | $0 | $1,148 | $7,777 | 346 | $0.00 | $3.32 | $22.48 | **$25.79** |
| Shell Pointe MHC *(sold)* | `SP` | $8,364 | $0 | $4,360 | 494 | $16.93 | $0.00 | $8.82 | **$25.76** |
| Paradise Lakes | `PL` | $0 | $23,257 | $8,305 | 1255 | $0.00 | $18.53 | $6.62 | **$25.15** |
| Regency I & II | `REG` | $-165 | $0 | $48,796 | 2360 | $-0.07 | $0.00 | $20.68 | **$20.61** |
| Oceanaire MHC | `OCEANPO` | $7,447 | $0 | $0 | 363 | $20.51 | $0.00 | $0.00 | **$20.51** |
| Lucky Clover | `LUCK` | $0 | $0 | $14,726 | 728 | $0.00 | $0.00 | $20.23 | **$20.23** |
| Hunter Springs MHP | `HSMHC` | $705 | $0 | $1,400 | 105 | $6.71 | $0.00 | $13.33 | **$20.04** |
| Gulf Breeze MHC | `GULFPO` | $2,140 | $0 | $1,750 | 212 | $10.10 | $0.00 | $8.25 | **$18.35** |
| Paradise Palms | `PP` | $0 | $0 | $5,093 | 315 | $0.00 | $0.00 | $16.17 | **$16.17** |
| American | `AMER` | $0 | $0 | $4,740 | 316 | $0.00 | $0.00 | $15.00 | **$15.00** |
| Greene Pointe | `GPT` | $132 | $0 | $10,024 | 719 | $0.18 | $0.00 | $13.94 | **$14.13** |
| Triple S Marina | `SSS` | $4,464 | $407 | $18,869 | 1796 | $2.49 | $0.23 | $10.51 | **$13.22** |
| Shady Acres MHC | `SA` | $0 | $15,900 | $942 | 1285 | $0.00 | $12.37 | $0.73 | **$13.11** |
| Brunswick Estates | `BRUN` | $2,201 | $0 | $2,887 | 398 | $5.53 | $0.00 | $7.25 | **$12.78** |
| Whispering Pines MA | `WPMA` | $0 | $0 | $4,320 | 424 | $0.00 | $0.00 | $10.19 | **$10.19** |
| McGregor Downs | `MCG` | $0 | $0 | $10,006 | 1013 | $0.00 | $0.00 | $9.88 | **$9.88** |
| Northgate MH | `NGMH` | $0 | $2,094 | $2,448 | 1496 | $0.00 | $1.40 | $1.64 | **$3.04** |
| Auburn Ridge | `ARD` | $0 | $0 | $3,069 | 1170 | $0.00 | $0.00 | $2.62 | **$2.62** |
| Druid Oaks MHC | `DO` | $0 | $0 | $1,234 | 783 | $0.00 | $0.00 | $1.58 | **$1.58** |
| Terrace Crossings | `TC` | $0 | $0 | $373 | 476 | $0.00 | $0.00 | $0.78 | **$0.78** |

## What is not in the table, and why the table is not the whole portfolio

**Twenty-two property records carry occupied lots in Rent Manager and no sewer, WWTP or trash expense at all in 2026.** Several are real communities of real size. This is the single largest thing this pull found and it is registered as `KP-0093`.

| Record | RM | Avg occupied lots |
| --- | --- | --- |
| Cambridge MHC | `CAMMHC` | 90.4 |
| BEDROCK MHC | `BMHC` | 1.0 |
| Valley View MHC | `VV` | 57.0 |
| Apple Creek | `ACMHC` | 166.0 |
| Parktown MHC | `PTMHC` | 41.0 |
| Countryside MHC | `CSMHC` | 29.0 |
| Cedar Grove Manufactured Housing Community | `CG` | 124.0 |
| Colonial Manufactured Housing Community | `C` | 104.0 |
| Lambeth Manufactured Housing Community | `LB` | 63.0 |
| xParkwood Manufactured Housing Community | `PW` | 97.0 |
| Everglades Mobile Home Park | `EG` | 53.0 |
| Royal Palm Trailer Park | `RP` | 50.0 |
| Tradewinds MHC | `TRADE` | 59.5 |
| Parakeet Communities | `PC` | 1.0 |
| Applegate Water | `AW` | 53.4 |
| Vantage Oaks Utility | `VOU` | 103.0 |
| Nalls Court MHC | `NALLS` | 19.0 |
| Hendersons MHC | `HENDS` | 61.4 |
| Northgate RV | `NGRV` | 46.9 |
| Bay Oaks Village I | `BOVIPO` | 48.1 |
| Shirleys Trailer Park I | `STPI` | 32.0 |
| Shirleys Trailer Park II | `STPII` | 8.0 |

**Two records carry the expense and no occupied lots**, so no per-lot figure is possible: Geiger Key Fish Camp Opco (`GKFC`, $48,291 trash and $9,700 sewer - the restaurant and marina operation, not lots) and the legacy Hunter Springs MHC record (`HSRC`, $1,400 trash and $956 sewer, which belongs with `HSMHC`).

**Ten legacy `x` records were folded into their current entity** to build this. Without the merge, January 2026 expense is missing from the current record: `TCMHC`, `OCEAN`, `WOLF`, `PSE`, `OBO`, `BOVI`, `BOVII`, `GULF`, `WW` and `LW` all migrated to their `...PO` successors in December 2025. Any single-entity pull on those ten gives a wrong year to date.

**Congress and Shell Pointe are sold** and are shown for completeness only. **Regency I & II shows occupancy from March and McGregor Downs from April**, so their per-lot figures cover those months only.

## Related

[[80-Finance/planning/Sewer-Trash-Per-Lot-2026-YTD.xlsx]]

