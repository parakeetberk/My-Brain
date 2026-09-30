# Portfolio Baseline: RentViewer Warehouse

**What this is:** The portfolio as the RentViewer warehouse actually reports it - occupancy, rent, AR and TTM financials, every figure labelled.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

**Built:** 2026-08-26 · **Source:** RentViewer semantic warehouse (Rent Manager-derived), read-only MCP queries
**Cross-check source:** Rent Manager connector, `list_entities(Properties)`

## How to read this file

Every figure is labeled:

- **VERIFIED**: returned directly by a query run against the warehouse during this build
- **SINGLE-SOURCE**: appears in exactly one system, no cross-check available
- **INFERRED**: derived or reasoned from VERIFIED values, not returned directly

**Two periods are used throughout, and they are not the same period.**

| Period label | Meaning | Which models |
|---|---|---|
| **Snapshot 2026-08** | The most recent point-in-time snapshot (August 2026) | `VW_Rental_Unit_Listing`, `VW_Aged_Receivables`, `VW_Summary_Rent_Roll` |
| **TTM Aug-25 → Jul-26** | Trailing twelve months ended 31 Jul 2026 (last complete GL month) | `VW_Budget_Comparison` |

`VW_Budget_Comparison` is **not** period-restricted by default. Every financial query below explicitly sets
`timeRange { dimension: VW_Budget_Comparison.endDate, from: 2025-08-01, to: 2026-07-31 }`.
Warehouse GL data spans **2025-01-31 through 2026-08-22** (2026-08 is a partial month and is excluded from TTM).
Snapshot models span **2025-01 through 2026-08** (20 monthly periods).

---

## 1. Portfolio at a glance

**Occupancy / rent, as of snapshot 2026-08.** Model `VW_Rental_Unit_Listing`.
**Financials, TTM Aug-25 → Jul-26.** Model `VW_Budget_Comparison`.
**AR, as of snapshot 2026-08.** Model `VW_Aged_Receivables`.

| Metric | Value | Label | Measure |
|---|---|---|---|
| Total units, **raw as the warehouse returns it** | **9,355** | VERIFIED | `unitCount` |
| Total units, **de-duplicated** (archived/shadow records removed) | **8,020** | VERIFIED (filtered query) | `unitCount` |
| Occupancy rate, raw | **67.62%** | VERIFIED | `occupancyRate` |
| Occupancy rate, de-duplicated | **77.67%** | VERIFIED (filtered query) | `occupancyRate` |
| Days vacant / days available (de-dup) | 39,397 / 176,440 | VERIFIED | `daysVacant`, `daysAvailable` |
| Total actual (in-place) rent, raw | **$2,314,990** /mo | VERIFIED | `totalActualRent` |
| Total market rent, raw | **$2,715,297** /mo | VERIFIED | `totalMarketRent` |
| Total actual rent, de-duplicated | $2,182,350 /mo | VERIFIED | `totalActualRent` |
| Total market rent, de-duplicated | $2,375,815 /mo | VERIFIED | `totalMarketRent` |
| Total revenue (TTM) | **$54,813,442** | VERIFIED | `totalRevenue` |
| Total operating expenses (TTM) | **$28,268,197** | VERIFIED | `totalOperatingExpenses` |
| **Portfolio NOI (TTM)** | **$26,545,245** | VERIFIED | `noi` |
| **Portfolio NOI margin (TTM)** | **48.43%** | VERIFIED | `noiMargin` |
| Operating expense ratio (TTM) | **51.57%** | VERIFIED | `operatingExpenseRatio` |
| Utilities expense (TTM) | $5,403,916 | VERIFIED | `utilitiesExpense` |
| Repairs & maintenance (TTM) | $2,136,876 | VERIFIED | `repairsMaintenanceExpense` |
| **Total AR outstanding** | **$1,908,202** | VERIFIED | `agedReceivablesTotal` |
| AR over 90 days | $1,295,089 (**67.87%**) | VERIFIED | `over90Days`, `percentOver90` |
| Customers with a balance | 1,099 | VERIFIED | `customersWithBalance` |

**The portfolio misses its own stated NOI-margin target.** The warehouse documents a target above 50% for stabilized
assets and an operating expense ratio below 45 to 50%. Portfolio TTM margin is **48.43%** and OER is **51.57%**.
Both are on the wrong side of the line. (VERIFIED figures; the target itself is SINGLE-SOURCE, from the
`noiMargin` / `operatingExpenseRatio` measure definitions in `get_schema`.)

**Why two unit counts.** The raw 9,355 double-counts properties that exist twice in the warehouse under an
archived and an active name (see §6). The de-duplicated 8,020 excludes 20 named records identified as
archived (`x`-prefixed) or zero-occupancy shadow duplicates. **Use 8,020 / 77.67%.** The raw 67.62%
occupancy figure is an artifact of counting ~1,335 archived units at 0% occupancy.

**Portfolio scale is not stable across the snapshot history** (VERIFIED, `unitCount` by `reportMonth`):
2025-01→2025-07 = 8,823 · 2025-08→2025-11 ≈ 8,012 to 8,027 · 2025-12→2026-02 ≈ 8,517 to 8,522 ·
2026-03 = 8,942 · 2026-04 = 9,174 · 2026-05 = 9,216 · 2026-06 = 9,217 · 2026-07/08 = 9,355.
The step changes track record-keeping events (renames, archive flags), not acquisitions. Do not read
unit-count growth off this series without reconciling names first.

---

## 2. By property

**Sorted by TTM NOI, descending.** All properties with GL activity in the TTM window.

- Units / Occ % / Actual rent / Market rent / Loss-to-lease: `VW_Rental_Unit_Listing`, **snapshot 2026-08**
  (`unitCount`, `occupancyRate`, `totalActualRent`, `totalMarketRent`, `rentVsMarketVariance`)
- NOI / Margin: `VW_Budget_Comparison`, **TTM Aug-25 → Jul-26** (`noi`, `noiMargin`)
- AR / %>90: `VW_Aged_Receivables`, **snapshot 2026-08** (`agedReceivablesTotal`, `percentOver90`)
- Dimension throughout: `propertyName`

Loss-to-lease column = `rentVsMarketVariance` (actual minus market; **negative = in-place rent below market**).
`n/d` means the property has actual rent or market rent recorded as zero, so the variance is not meaningful.
This is a data gap, not a zero. `n/a` = no value returned. All figures **VERIFIED** unless the row says otherwise.

| Property | Units | Occ % | Actual rent | Market rent | Loss to lease | NOI (TTM) | Margin | AR | %>90 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Triple S Marina | 245 | 89.4% | n/a | 175,749 | n/d | 1,732,236 | 78.5% | 2,097 | 0% |
| Riviera | 163 | 100.0% | 166,645 | 153,900 | 12,745 | 1,547,992 | 71.9% | 1,424 | 0% |
| Riverwalk | 201 | 84.4% | n/a | n/a | n/d | 1,360,873 | 62.2% | 28,209 | 19% |
| The Oaks | 190 | 68.2% | n/a | n/a | n/d | 1,259,929 | 61.8% | 5,878 | 0% |
| J Bar J Estates | 100 | 100.0% | 115,500 | 98,665 | 16,835 | 1,148,605 | 73.8% | 2,559 | 0% |
| Auburn Ridge | 160 | 91.3% | n/a | n/a | n/d | 935,506 | 69.2% | 3,367 | 0% |
| Windward Knoll | 168 | 81.6% | n/a | n/a | n/d | 881,039 | 59.9% | 14,400 | 58% |
| Fox Creek | 129 | 78.9% | 67,080 | n/a | n/d | 880,767 | 70.0% | 0 | n/a |
| Whispering Pines MH FL | 202 | 62.9% | 75,140 | 135,820 | **-60,680** | 879,933 | 62.2% | 0 | n/a |
| Northgate MH | 222 | 85.6% | n/a | n/a | n/d | 861,666 | 66.5% | 2,124 | 0% |
| Geiger Key RV Resort | 63 | 71.2% | n/a | n/a | n/d | 841,628 | 55.7% | 34,326 | 32% |
| Lucky Clover | 128 | 66.4% | 41,085 | 141,570 | **-100,485** | 827,799 | 62.3% | 14,173 | 0% |
| Shady Acres MHC | 219 | 73.1% | n/a | n/a | n/d | 778,695 | 71.1% | 13,075 | 50% |
| Silver Hill MHC | 126 | 84.1% | 69,300 | n/a | n/d | 724,541 | 73.7% | 13,284 | 54% |
| Vantage Oaks | 253 | 65.6% | 31,550 | 125,300 | **-93,750** | 704,200 | 59.2% | 6,073 | 0% |
| Parkwood Mobile Home Park | 90 | 66.2% | n/a | n/a | n/d | 657,829 | 63.9% | 4,312 | 0% |
| Carley's Mobile Home Park | 76 | 100.0% | 87,020 | 84,540 | 2,480 | 614,902 | 54.5% | 0 | n/a |
| Sea Shells MHC | 100 | 85.0% | 79,500 | 80,240 | -740 | 591,142 | 62.9% | 911 | 0% |
| Terrace Crossings | 65 | 92.3% | n/a | n/a | n/d | 532,721 | 68.1% | 1,222 | 0% |
| Greene Pointe | 95 | 94.7% | 65,550 | 600 | n/d ⚠ | 514,936 | 76.5% | 12,015 | 74% |
| Redlands | 81 | 100.0% | 68,445 | 59,600 | 8,845 | 504,824 | 65.7% | 0 | n/a |
| Applegate MHC | 88 | 82.9% | 62,920 | 53,165 | 9,755 | 475,059 | 63.3% | 3,494 | 0% |
| Southgate | 102 | 73.5% | 69,360 | 62,130 | 7,230 | 463,805 | 63.0% | 1,715 | 0% |
| Regency I & II | 424 | 92.9% | n/a | n/a | n/d | 460,395 | 77.1% | 8,646 | 14% |
| Paradise Lakes | 200 | 79.5% | n/a | 139,300 | n/d | 427,028 | 51.0% | 0 | n/a |
| Hendersons MHC | 66 | 93.9% | 32,010 | n/a | n/d | 401,816 | 98.1% ⚠ | 4,400 | 55% |
| Druid Oaks MHC | 127 | 75.6% | n/a | n/a | n/d | 379,631 | 62.9% | 8,670 | 57% |
| Tradewinds MHC | 73 | 76.7% | 48,545 | 47,365 | 1,180 | 372,254 | 67.8% | 8,357 | 18% |
| Oakside MHP | 93 | 93.6% | n/a | n/a | n/d | 366,691 | 57.7% | 0 | n/a |
| Su-Rene | 80 | 82.5% | 58,000 | n/a | n/d | 361,258 | 60.4% | 780 | 0% |
| Hershey Park | 76 | 98.7% | 41,800 | n/a | n/d | 354,858 | 73.3% | 4,717 | 27% |
| Central Mobile Home Park | 64 | 87.5% | 43,520 | 35,200 | 8,320 | 351,651 | 62.0% | 0 | n/a |
| Shady Oaks MHP | 37 | 100.0% | 41,070 | 33,115 | 7,955 | 347,232 | 73.4% | 0 | n/a |
| Great Oak RV Resort | 231 | 58.4% | n/a | n/a | n/d | 312,217 | **33.4%** | 21,688 | **100%** |
| Belle Haven | 93 | 57.3% | n/a | 89,650 | n/d | 307,829 | 51.0% | 3,750 | 40% |
| Congress Mobile Home Park | 31 | 100.0% | 30,845 | 28,500 | 2,345 | 284,460 | 70.0% | 45,968 | 8% |
| Meadow Woods MHP | 69 | 95.7% | 44,850 | 44,850 | 0 | 265,177 | 54.4% | 40,336 | 24% |
| Brunswick Estates | 65 | 73.4% | 32,825 | n/a | n/d | 264,991 | 63.1% | 8,334 | 0% |
| Northgate RV | 117 | **34.2%** | n/a | n/a | n/d | 243,718 | 71.2% | 0 | n/a |
| McGregor Downs | 232 | 87.1% | n/a | n/a | n/d | 223,160 | 65.5% | 32,834 | 35% |
| Whispering Pines MA | 53 | 100.0% | 32,595 | 33,656 | -1,061 | 220,935 | 55.6% | 5,258 | 0% |
| Royal Palm Trailer Park | 51 | 98.0% | 22,950 | 20,910 | 2,040 | 218,718 | 83.7% | 0 | n/a |
| Everglades MHP | 55 | 96.4% | 24,750 | 22,550 | 2,200 | 212,944 | 76.7% | 0 | n/a |
| Lake Saunders | 48 | 87.5% | 29,760 | 26,805 | 2,955 | 209,159 | 60.1% | 6,331 | 0% |
| Oceanaire MHC | 50 | 90.0% | 33,250 | n/a | n/d | 205,281 | 80.5% | 3,033 | 23% |
| Monson | 61 | 96.7% | 39,640 | 42,314 | -2,674 | 198,295 | **44.0%** | 53,702 | 64% |
| Harbour Mobile Home Park | 46 | 78.3% | 31,280 | 26,330 | 4,950 | 190,763 | 55.8% | 0 | n/a |
| Paradise Palms | 50 | 76.0% | n/a | n/a | n/d | 190,685 | 62.8% | 1,295 | 0% |
| Shell Pointe MHC | 74 | 77.0% | n/a | n/a | n/d | 176,465 | **44.0%** | **125,620** | 37% |
| Palm Haven Estates | 60 | 67.6% | 33,300 | 44,505 | **-11,205** | 171,941 | 58.1% | 1,924 | 0% |
| Mayflower Hills | 50 | 98.0% | 37,000 | 39,500 | -2,500 | 153,772 | **37.9%** | 58,262 | 69% |
| Town & Country MHC | 36 | 100.0% | 20,340 | n/a | n/d | 142,088 | 63.8% | 868 | 0% |
| Bay Oaks Village I | 87 | 52.9% | n/a | n/a | n/d | 140,786 | 64.6% | 14,061 | 28% |
| Westwood MHC | 44 | 90.9% | 27,500 | n/a | n/d | 139,136 | 69.3% | 708 | 0% |
| Ormond Beach Oasis | 62 | 62.9% | 39,370 | n/a | n/d | 135,238 | 51.6% | 2,537 | 0% |
| Royal Oaks MHC | 39 | 76.9% | 23,985 | 23,725 | 260 | 130,870 | **46.4%** | 0 | n/a |
| Wolf Bay MHC | 45 | 88.9% | 24,750 | n/a | n/d | 114,529 | 62.7% | 21,574 | 76% |
| Palm Spring Estates | 45 | 71.1% | 29,250 | n/a | n/d | 111,512 | 50.7% | 29,710 | 64% |
| Gulf Breeze MHC | 39 | 74.4% | 22,230 | n/a | n/d | 94,059 | 63.4% | 3,565 | 0% |
| Hunter Springs MHP | 25 | 52.0% | 14,625 | n/a | n/d | 90,782 | 64.0% | 1,856 | 0% |
| American | 41 | 97.6% | 23,575 | 34,057 | **-10,482** | 83,144 | **22.6%** | **85,940** | **77%** |
| Bay Oaks Village II | 34 | 52.9% | n/a | n/a | n/d | 59,044 | 59.7% | 0 | n/a |
| Lake Wales MHC | 48 | **47.9%** | 28,320 | n/a | n/d | 38,636 | **32.6%** | 14,993 | 33% |
| Vantage Oaks Utility | 119 | 86.6% | n/a | n/a | n/d | 28,171 | 95.0% | 2,339 | 65% |
| Applegate Water | 57 | 93.0% | n/a | n/a | n/d | 15,869 | 71.5% | 9,444 | 86% |
| Crystal Acres | 51 | **45.1%** | 24,480 | 29,650 | -5,170 | 15,252 | **8.4%** | 2,115 | 91% |
| Silver Breeze | 57 | **8.8%** | 20,930 | 52,920 | **-31,990** | 12,479 | **9.4%** | 0 | n/a |
| Hunter Springs MHC ⚠dup | 25* | 0.0%* | n/a | n/a | n/d | -6,442 | **-18.4%** | 0 | n/a |
| River Oaks RV Resort | 113 | **38.9%** | 98,875 | 98,000 | 875 | **-10,941** | **-4.0%** | 2,725 | **100%** |
| Cambridge MHC | 149 | 61.1% | 75,990 | 73,115 | 2,875 | **-14,360** | **-8.4%** | **311,260** | **85%** |
| Lamberton Lake MHC | 53 | 67.9% | 28,620 | 26,633 | 1,987 | **-20,402** | **-7.5%** | 5,284 | 35% |
| Northgate Utility | 70 | 100.0% | n/a | n/a | n/d | -30,315 | **-236.7%** | 0 | n/a |

⚠ **Greene Pointe** market rent of $600 against $65,550 actual is an obvious data error, not a $65K rent premium. Its loss-to-lease is unusable.
⚠ **Hendersons MHC** 98.1% margin reflects only $7,975 of TTM operating expense against $409,791 of revenue. Expenses are almost certainly booked elsewhere. Treat as unreliable, not as the portfolio's best performer.
\* Hunter Springs MHC is a shadow duplicate of Hunter Springs MHP (see §6); its unit row shows 25 units at 0%.

**Non-property entity records excluded from the table above** (holding companies, funds, opcos, which carry GL
activity but no units). All VERIFIED, TTM Aug-25 → Jul-26 `noi`:

| Entity | TTM NOI | Note |
|---|---:|---|
| Triple-counted corporate: **Parakeet Communities** | **-3,636,103** | Corporate overhead pool; $6.12M opex against $2.48M revenue |
| Geiger Key Fish Camp Opco | -672,789 | $3.28M opex on $2.61M revenue; margin -25.8% |
| A2Z Community Partners | -385,883 | $563,784 opex, $177,902 revenue |
| Parakeet MHC Hold Co I | +1,044,836 | Management/holding income |
| BEDROCK I GROUP | +350,369 | |
| Grove Banyan | +195,044 | |
| Parakeet MHC Hold Co II | +113,566 | |
| xLake Saunders RV | -12,038 | Archived record still accruing expense |
| Nalls Court MHC | -17,100 | Expense only, no revenue, no units |
| Cambridge MHP Investment | -12,796 | |

**These corporate entities are inside the $26.5M portfolio NOI figure.** Property-level NOI alone sums materially
higher; the -$3.6M Parakeet Communities overhead pool is the single largest drag in the warehouse.

---

## 3. Outliers, and why they matter

### 3a. Occupancy: worst five

`VW_Rental_Unit_Listing.occupancyRate` by `propertyName`, **snapshot 2026-08**. VERIFIED.
Excludes records returning exactly 0.0% with no rent and no GL activity (those are listed in §6 as dead records,
not as vacancy).

| Rank | Property | Occupancy | Units | TTM NOI | Why it matters |
|---|---|---:|---:|---:|---|
| 1 | **Silver Breeze** | **8.77%** | 57 | 12,479 | 9.4% NOI margin, 90.7% OER, 15 move-outs vs 1 move-in in 6 months. Functionally emptying. |
| 2 | **Northgate RV** | **34.19%** | 117 | 243,718 | Still profitable (71.2% margin) but net -22 residents in 6 months. The NOI is running off. |
| 3 | **River Oaks RV Resort** | **38.94%** | 113 | **-10,941** | Only sizable property with negative TTM NOI. See 3a-i. |
| 4 | **Crystal Acres** | **45.10%** | 51 | 15,252 | 8.4% margin, 91.6% OER, 91% of AR over 90 days. |
| 5 | **Lake Wales MHC** | **47.92%** | 48 | 38,636 | 32.6% margin, 67.4% OER, net -3 residents. |

Runners-up: Hunter Springs MHP 52.0%, Bay Oaks Village I 52.87%, Bay Oaks Village II 52.94%,
Belle Haven 57.33%, Great Oak RV Resort 58.44%.

#### 3a-i. Testing the claim: "River Oaks is at roughly 60% actual occupancy despite looking full"

**Verdict: the headline number does not hold, but the claim's underlying instinct is right, and there is a
specific reason the two numbers differ.**

River Oaks RV Resort, snapshot 2026-08 (VERIFIED, `VW_Rental_Unit_Listing`, dimensions `propertyName` + `unitTypeName`):

| Unit type | Units | Occupancy | Days vacant / available |
|---|---:|---:|---:|
| Lot-RV | 60 | **65.0%** | 462 / 1,320 |
| Lot-RV (Transient) | 13 | 15.4% | 242 / 286 |
| Lot-Pending (POH) | 12 | 8.3% | 242 / 264 |
| Lot-Unusable | 10 | 0.0% | 220 / 220 |
| Lot-RV (Seasonal) | 7 | 14.3% | 132 / 154 |
| Lot-Avail (POH) | 6 | 0.0% | 132 / 132 |
| STOR | 2 | 0.0% | 44 / 44 |
| Lot | 1 | 0.0% | 22 / 22 |
| Lot-Demo | 1 | 0.0% | 22 / 22 |
| Office | 1 | 100.0% | 0 / 22 |
| **Total** | **113** | **38.94%** | **1,518 / 2,464** |

- **Blended occupancy is 38.94%, not ~60%.** The claim understates the problem.
- **But the core rentable RV inventory (Lot-RV, 60 units) is at 65.0%**, within a few points of "roughly 60%".
  The claim is almost certainly describing the *primary lot stock*, and on that basis it is broadly correct.
- The gap between 38.94% and 65.0% is entirely structural: 10 `Lot-Unusable`, 6 `Lot-Avail(POH)`,
  12 `Lot-Pending(POH)`, 1 `Lot-Demo`, 2 `STOR` and 1 bare `Lot`, **32 units, 28% of the property**,
  sit in the occupancy denominator at 0%.
- **Both readings support the "looks full but isn't" observation.** River Oaks is the only property of
  meaningful size in the portfolio with **negative TTM NOI (-$10,941, margin -4.0%, OER 104.0%)**, it missed
  budgeted revenue by **-$407,682**, and **100% of its AR is over 90 days**. Whatever the right occupancy
  denominator, the asset is not performing. (All VERIFIED.)

Label: unit-type breakdown and all percentages **VERIFIED**. The judgment that the ~60% claim refers to Lot-RV
stock is **INFERRED**.

### 3b. NOI margin and operating expense ratio: properties failing target

Targets are documented in the warehouse measure definitions (SINGLE-SOURCE, from `get_schema`):
**NOI margin above 50%** for stabilized assets; **operating expense ratio below 45 to 50%**.
All property figures below are **VERIFIED**, `VW_Budget_Comparison`, **TTM Aug-25 → Jul-26**,
measures `noiMargin` / `operatingExpenseRatio`, dimension `propertyName`.

**Failing BOTH tests (margin below 50% and OER above 50%):**

| Property | NOI margin | OER | TTM NOI |
|---|---:|---:|---:|
| Northgate Utility | -236.71% | 336.71% | -30,315 |
| Hunter Springs MHC ⚠dup | -18.38% | 118.38% | -6,442 |
| Cambridge MHC | -8.41% | 108.41% | -14,360 |
| Lamberton Lake MHC | -7.47% | 107.47% | -20,402 |
| **River Oaks RV Resort** | **-3.98%** | **103.98%** | **-10,941** |
| Crystal Acres | 8.40% | 91.60% | 15,252 |
| Silver Breeze | 9.35% | 90.65% | 12,479 |
| American | 22.59% | 77.41% | 83,144 |
| Lake Wales MHC | 32.63% | 67.37% | 38,636 |
| Great Oak RV Resort | 33.38% | 66.62% | 312,217 |
| Mayflower Hills | 37.88% | 62.12% | 153,772 |
| Monson | 43.97% | 56.03% | 198,295 |
| Shell Pointe MHC | 44.02% | 55.98% | 176,465 |
| Royal Oaks MHC | 46.39% | 53.61% | 130,870 |

**Corporate / opco entities also failing both** (not properties, listed for completeness):
A2Z Community Partners (-216.91% / 316.91%), Parakeet Communities (-146.63% / 246.63%),
BEDROCK MHC Fund II LP, Geiger Key Fish Camp Opco (-25.78% / 125.78%), Geiger RV (-10.62% / 110.62%).

**Passing margin but sitting inside the 45 to 50% OER caution band** (margin above 50, OER 45 to 50, so no headroom):
Belle Haven (50.95% / 49.05%), Paradise Lakes (50.96% / 49.04%), Palm Spring Estates (50.65% / 49.35%),
Ormond Beach Oasis (51.56% / 48.44%), Meadow Woods MHP (54.40% / 45.60%),
Carley's Mobile Home Park (54.46% / 45.54%). All VERIFIED.

**No property fails only one of the two tests.** Because NOI margin and OER are algebraic complements
(margin + OER = 100% when both are defined), a property below 50% margin is above 50% OER by construction.
The 45 to 50% OER band is therefore the binding test, and it catches the six additional properties listed above.

#### 3b-i. Testing the claim: "one property's margin fell from ~65% to low 50s pending a city-water pass-through"

**Verdict: supported. The property is almost certainly Riverwalk.**

I compared NOI margin for Aug-25→Jan-26 against Feb-26→Jul-26 across the portfolio (VERIFIED,
`VW_Budget_Comparison.noiMargin`, two explicit `timeRange` queries). Riverwalk is the only property whose
decline matches the described shape *and* carries the utilities signature.

Riverwalk, monthly (VERIFIED: measures `noiMargin`, `utilitiesExpense`, `utilityReimbursements`, `noi`;
dimensions `propertyName` + `endDate`):

| Month | NOI margin | Utilities expense | Utility reimbursements |
|---|---:|---:|---:|
| Aug-25 | 74.87% | n/a | 6,717 |
| Sep-25 | 79.19% | 1,476 | 15,359 |
| Oct-25 | 80.04% | 20,051 | 19,715 |
| Nov-25 | 45.90% | 20,431 | 18,150 |
| Dec-25 | 68.96% | 7,531 | 22,917 |
| Jan-26 | 59.70% | 6,710 | 21,484 |
| Feb-26 | 21.75% | **92,841** | 20,073 |
| Mar-26 | 78.25% | 7,336 | 46,635 |
| Apr-26 | 67.81% | 19,686 | 24,267 |
| May-26 | 48.81% | **40,776** | 18,880 |
| Jun-26 | 66.36% | 6,650 | 18,754 |
| **Jul-26** | **52.15%** | **41,775** | 20,462 |

- **Half-over-half: 68.16% → 56.64%.** Most recent complete month (Jul-26): **52.15%, "low 50s".** VERIFIED.
- **Utilities expense H1 $56,199 → H2 $209,064 (+272%)**, while **utility reimbursements stayed flat at
  ~$18 to 24K/month.** That is precisely the signature of a utility cost landing on the property without a
  resident pass-through in place. VERIFIED.
- Riverwalk also carries the **portfolio's single largest utilities budget overrun: +$134,112** against a
  budget of $131,152 (actual $265,264). VERIFIED.

Label: all Riverwalk figures **VERIFIED**. The attribution to a *city-water* pass-through specifically is
**INFERRED**: the warehouse's `utilitiesExpense` measure aggregates electric, gas, sewer, water, WWTP,
garbage and stormwater into one 518xx bucket and does not break out a water line item, so the data confirms
the pattern but cannot name the utility.

**Runners-up on the same test** (VERIFIED): Lucky Clover 66.69% → 57.00%; Brunswick Estates 65.81% → 59.92%;
Central Mobile Home Park 64.22% → 59.90%; Oakside MHP 59.76% → 55.77%. And separately,
**Paradise Lakes collapsed from 64.83% to 9.66%** half-over-half (H2 NOI just $20,346 on $210,712 revenue),
a far larger deterioration than the one described, with utilities of $66,575 in H2. That is a bigger problem
than the one the road-trip review flagged and it is not the same property.

### 3c. Loss to lease: where in-place rent trails market

Measure `VW_Rental_Unit_Listing.rentVsMarketVariance` (actual minus market), dimension `propertyName`,
**snapshot 2026-08**. VERIFIED. Negative = in-place rent below market = recoverable revenue.

**Only properties with BOTH actual and market rent populated are shown.** This is a hard constraint:
of 104 property records, only 35 have both fields non-zero. The rest return 0 for one side and produce
meaningless variances.

| Property | Actual rent | Market rent | **Monthly gap** | Annualized | Occupancy |
|---|---:|---:|---:|---:|---:|
| **Lucky Clover** | 41,085 | 141,570 | **-100,485** | **-1,205,820** | 66.4% |
| **Vantage Oaks** | 31,550 | 125,300 | **-93,750** | **-1,125,000** | 65.6% |
| **Whispering Pines MH FL** | 75,140 | 135,820 | **-60,680** | **-728,160** | 62.9% |
| **Silver Breeze** | 20,930 | 52,920 | **-31,990** | **-383,880** | 8.8% |
| **Palm Haven Estates** | 33,300 | 44,505 | **-11,205** | **-134,460** | 67.6% |
| **American** | 23,575 | 34,057 | **-10,482** | **-125,784** | 97.6% |
| Crystal Acres | 24,480 | 29,650 | -5,170 | -62,040 | 45.1% |
| Monson | 39,640 | 42,314 | -2,674 | -32,088 | 96.7% |
| Mayflower Hills | 37,000 | 39,500 | -2,500 | -30,000 | 98.0% |
| Whispering Pines MA | 32,595 | 33,656 | -1,061 | -12,732 | 100.0% |
| Sea Shells MHC | 79,500 | 80,240 | -740 | -8,880 | 85.0% |

**Total identified loss to lease: -$320,737/month, -$3,848,844 annualized** (INFERRED, the sum of the
VERIFIED rows above).

**Read this carefully.** The top four rows are dominated by *vacancy*, not by under-priced leases:
Lucky Clover (66% occupied), Vantage Oaks (66%), Whispering Pines MH FL (63%) and Silver Breeze (9%) each
carry market rent on units that have no in-place rent at all because nobody lives there. The gap at those
four is a **lease-up** number, not a **rent-raise** number.

**The genuinely fast money is the bottom of the list, not the top.** American (97.6% occupied, -$10,482/mo),
Monson (96.7%, -$2,674), Mayflower Hills (98.0%, -$2,500) and Whispering Pines MA (100%, -$1,061) are
full properties renting below market. That is **-$16,717/month, -$200,604/year recoverable by renewal
pricing alone**, with no lease-up required. (INFERRED from VERIFIED rows.)

**Properties where loss to lease CANNOT be measured** (market rent or actual rent returns zero):
Riverwalk, The Oaks, Auburn Ridge, Windward Knoll, Northgate MH, Regency I & II, Shady Acres MHC,
McGregor Downs, Terrace Crossings, Druid Oaks MHC, Oakside MHP, Great Oak RV Resort, Geiger Key RV Resort,
Parkwood MHP, Silver Hill MHC, Su-Rene, Fox Creek, Hendersons MHC, Hershey Park, Oceanaire MHC,
Ormond Beach Oasis, Palm Spring Estates, Westwood MHC, Wolf Bay MHC, Gulf Breeze MHC, Town & Country MHC,
Brunswick Estates, Lake Wales MHC, Hunter Springs MHP, Lambeth MHC, Bay Oaks Village I & II,
Colonial MHC, Shell Pointe MHC, Paradise Palms, Shirleys I & II, Nalls Court, Highlands, Trailerama,
Vantage Oaks Utility, Northgate Utility, Applegate Water. **That is ~44 properties, more than half the
portfolio, including six of the ten largest NOI producers.** Loss to lease cannot be stated at portfolio
level until market rents are loaded. See §6.

**Note on `VW_Summary_Rent_Roll.lossToLease`:** that measure returns large *negative* values for most
properties (e.g. Regency I & II -103,575, Riverwalk -83,799, Northgate MH -78,398, Windward Knoll -76,549),
which would imply in-place rent far *above* market. Cross-referencing the unit listing shows those same
properties have market rent recorded as **zero**. The measure is being driven by the missing-market-rent gap,
not by real rent premiums. **Do not use `VW_Summary_Rent_Roll.lossToLease` until market rents are populated.**
(VERIFIED that the values are returned; the diagnosis is INFERRED.)

### 3d. AR: worst concentrations and disproportionate aging

`VW_Aged_Receivables`, **snapshot 2026-08**, dimension `propertyName`, measures `agedReceivablesTotal`,
`over90Days`, `percentOver90`, `customersWithBalance`. All VERIFIED.

**Largest balances:**

| Property | AR total | Over 90 days | % over 90 | Customers | Share of portfolio AR |
|---|---:|---:|---:|---:|---:|
| **Cambridge MHC** | **311,260** | 265,265 | **85.2%** | 90 | **16.3%** |
| **Cedar Grove MHC** ⚠ | **178,871** | 178,871 | **100%** | 123 | 9.4% |
| **xParkwood MHC** ⚠arch | **137,340** | 137,340 | **100%** | 97 | 7.2% |
| **Shell Pointe MHC** | **125,620** | 46,317 | 36.9% | 54 | 6.6% |
| **Colonial MHC** ⚠ | **111,839** | 111,839 | **100%** | 103 | 5.9% |
| **Lambeth MHC** ⚠ | **87,407** | 87,407 | **100%** | 62 | 4.6% |
| **Parakeet Communities** | **85,975** | 76,215 | 88.6% | 0 ⚠ | 4.5% |
| **American** | **85,940** | 66,120 | **76.9%** | 7 | 4.5% |
| Mayflower Hills | 58,262 | 39,908 | 68.5% | 13 | 3.1% |
| Monson | 53,702 | 34,274 | 63.8% | 12 | 2.8% |
| Congress Mobile Home Park | 45,968 | 3,585 | 7.8% | 31 | 2.4% |
| Meadow Woods MHP | 40,336 | 9,764 | 24.2% | 20 | 2.1% |
| Geiger Key RV Resort | 34,326 | 11,116 | 32.4% | 12 | 1.8% |
| McGregor Downs | 32,834 | 11,485 | 35.0% | 15 | 1.7% |
| Palm Spring Estates | 29,710 | 18,979 | 63.9% | 4 | 1.6% |
| Riverwalk | 28,209 | 5,391 | 19.1% | 10 | 1.5% |
| Cedar Grove Homes | 25,817 | 25,817 | **100%** | 2 | 1.4% |
| Colonial Homes | 23,657 | 22,412 | 94.7% | 1 | 1.2% |
| Apple Creek | 21,828 | 21,828 | **100%** | 29 | 1.1% |
| Great Oak RV Resort | 21,688 | 21,688 | **100%** | 102 | 1.1% |
| Wolf Bay MHC | 21,574 | 16,296 | 75.5% | 3 | 1.1% |

**Disproportionate over-90 concentration.** Portfolio-wide, 67.87% of AR is over 90 days. These properties
are materially worse, and several are 100%:

- **100% over 90, no current billing at all**: Cedar Grove MHC ($178,871 / 123 customers),
  xParkwood MHC ($137,340 / 97), Colonial MHC ($111,839 / 103), Lambeth MHC ($87,407 / 62),
  Cedar Grove Homes ($25,817), Apple Creek ($21,828 / 29), Great Oak RV Resort ($21,688 / 102),
  Countryside MHC ($4,155), Parktown MHC ($9,181), River Oaks RV Resort ($2,725), Vandemere Homes ($318).
  **These are frozen ledgers, not active delinquency.** Zero dollars in every bucket except 90+, which means
  no charges have posted in 90+ days. Combined: **$601,769, 31.5% of portfolio AR.** They are either written-off
  populations, migrated-away properties, or a stopped billing feed. This is the single largest thing to
  investigate in the AR book.
- **Crystal Acres 91.5%**, Applegate Water 86.5%, **Cambridge MHC 85.2%**, Wolf Bay MHC 75.5%,
  **American 76.9%**, Greene Pointe 73.9%, Mayflower Hills 68.5%, Vantage Oaks Utility 65.4%,
  Palm Spring Estates 63.9%, Monson 63.8%.
- **Cambridge MHC is the worst live concentration**: $311,260 across 90 customers, 85.2% over 90 days,
  **16.3% of all portfolio AR at a property with negative TTM NOI (-$14,360)**. Note the rent roll shows
  `rentCharges` = $0 for Cambridge MHC in the current snapshot, so this balance is also not being added to.
- **Parakeet Communities carries $85,975 of AR against 0 customers with a balance**, a measure conflict
  that indicates the balance is not attributable to a tenant record.

**Best-behaved AR** (nonzero balance, 0% over 90): Applegate MHC, Auburn Ridge, Brunswick Estates,
Gulf Breeze MHC, Hunter Springs MHP, J Bar J Estates, Lake Saunders, Lucky Clover, Northgate MH,
Ormond Beach Oasis, Palm Haven Estates, Paradise Palms, Parkwood MHP, Riviera, Sea Shells, Shirleys I,
Southgate, Su-Rene, Terrace Crossings, The Oaks, Town & Country, Triple S Marina, Vantage Oaks,
Westwood MHC, Whispering Pines MA.

#### 3d-i. Testing the claim: "77% of AR at Windward Knolls, about $84.1K"

**Verdict: WRONG. Both the property and the framing are incorrect. Do not carry this figure forward.**

Windward Knoll aged receivables, every period in the warehouse (VERIFIED, `agedReceivablesTotal`,
`over90Days`, `percentOver90` by `reportMonth`, filtered `propertyName contains "Windward"`):

| Period | AR total | Over 90 | % over 90 |
|---|---:|---:|---:|
| 2025-08 | 6,616 | 0 | 0% |
| 2025-09 | 1,578 | 0 | 0% |
| 2025-10 | 2,367 | 789 | 33.3% |
| 2025-11 | 4,021 | 789 | 19.6% |
| 2025-12 | 4,926 | 2,367 | 48.1% |
| 2026-01 | 5,903 | 3,156 | 53.5% |
| 2026-02 | 6,658 | 3,156 | 47.4% |
| 2026-03 | 8,562 | 3,945 | 46.1% |
| 2026-04 | 7,491 | 4,734 | 63.2% |
| 2026-05 | 8,410 | 6,537 | **77.7%** |
| 2026-06 | 9,329 | 6,572 | 70.4% |
| 2026-07 | 15,298 | 8,375 | 54.7% |
| **2026-08** | **14,400** | **8,410** | **58.4%** |

Three separate errors in the claim:

1. **Windward Knoll's AR has never exceeded $15,298 in any period the warehouse holds.** $84.1K is off by
   roughly 5.5x. Its current balance is **$14,400**, or **0.75% of portfolio AR**, not 77%.
2. **"77% of AR" cannot mean share of portfolio AR.** No single property holds anywhere near 77% of the
   $1.91M book; the largest, Cambridge MHC, holds 16.3%.
3. **The 77% is a real number, but it is the over-90 share, not the portfolio share**. Windward Knoll hit
   **77.73% over 90 days in 2026-05**. Someone read `percentOver90` as a portfolio-concentration figure.

**Where the $84.1K probably came from.** The closest match anywhere in the current snapshot is
**American: $85,940.04 total AR at 76.94% over 90 days**, a property whose two numbers line up almost
exactly with "77% ... about $84.1K". Also close: Lambeth MHC at $87,407 (100% over 90).
This identification is **INFERRED**, not proven. But American, not Windward Knoll, is the property that
actually matches the reported figures, and American is genuinely a problem (22.6% NOI margin, 77.4% OER).

**Corrected statement:** *77% of American's $85,940 receivable balance is over 90 days old, as of 2026-08.*

---

## 4. Turnover

`VW_MoveIns_MoveOuts`, dimension `propertyName`, measures `moveIns`, `moveOuts`, `netMovement`,
`timeRange { dimension: month, from: 2026-02-01, to: 2026-08-31 }`, **the last seven months**. VERIFIED.
67 properties returned move activity; the remaining warehouse property records returned no rows.

### Net-losing residents (worst first)

| Property | Move-ins | Move-outs | **Net** | Occupancy (2026-08) | Cross-read |
|---|---:|---:|---:|---:|---|
| **Lucky Clover** | 12 | 34 | **-22** | 66.4% | Already only two-thirds full and still bleeding. -$100K/mo loss to lease. |
| **Northgate RV** | 9 | 31 | **-22** | 34.2% | Worst combination in the portfolio: lowest-but-one occupancy, largest outflow. |
| **Silver Breeze** | 1 | 15 | **-14** | 8.8% | Effectively closing. Only 1 move-in in 7 months. |
| **The Oaks** | 7 | 20 | **-13** | 68.2% | ⚠ **$1.26M NOI at risk**, 4th largest NOI in the portfolio. |
| **Parkwood MHP** | 10 | 22 | **-12** | 66.2% | $658K NOI. |
| **Shell Pointe MHC** | 4 | 16 | **-12** | 77.0% | 44% margin, $125.6K AR. Compounding. |
| **Great Oak RV Resort** | 8 | 17 | **-9** | 58.4% | 33.4% margin, 100% of AR over 90. |
| **Vantage Oaks** | 11 | 19 | **-8** | 65.6% | -$93.7K/mo loss to lease already. |
| **Riverwalk** | 12 | 19 | **-7** | 84.4% | ⚠ **See below. This is the one to watch.** |
| **Sea Shells MHC** | 13 | 20 | **-7** | 85.0% | ⚠ **See below.** |
| **Brunswick Estates** | 0 | 7 | **-7** | 73.4% | Zero move-ins in seven months. |
| Triple S Marina | 33 | 39 | -6 | 89.4% | ⚠ Largest NOI in the portfolio ($1.73M). |
| Tradewinds MHC | 7 | 12 | -5 | 76.7% | |
| Bay Oaks Village I | 9 | 13 | -4 | 52.9% | |
| Fox Creek | 8 | 12 | -4 | 78.9% | $881K NOI. |
| Southgate | 7 | 11 | -4 | 73.5% | |
| Paradise Palms | 0 | 4 | -4 | 76.0% | Zero move-ins. |
| Druid Oaks MHC | 0 | 3 | -3 | 75.6% | Zero move-ins. |
| Lake Wales MHC | 1 | 4 | -3 | 47.9% | |
| Ormond Beach Oasis | 1 | 4 | -3 | 62.9% | |
| Silver Hill MHC | 1 | 4 | -3 | 84.1% | ⚠ $725K NOI. |
| Su-Rene | 3 | 6 | -3 | 82.5% | |
| Applegate Water, Bay Oaks II, Belle Haven, Central MHP, Geiger Key RV, Oakside MHP, Oceanaire MHC, Palm Spring Estates, River Oaks RV, Shady Acres MHC, Wolf Bay MHC | | | **-2 each** | | |
| Crystal Acres, Lake Saunders | | | -1 each | | |

### Net-gaining

Shirleys Trailer Park I **+32** (32 move-ins, 0 move-outs; see §6, likely a bulk record load rather than
real absorption), Shirleys Trailer Park II **+8**, Gulf Breeze MHC **+5**, Palm Haven Estates **+5**,
McGregor Downs **+4**, Lamberton Lake MHC **+3**, Regency I & II **+3**, Auburn Ridge **+2**,
Paradise Lakes **+2**, and +1 each at American, Cambridge MHC, Carley's, Greene Pointe, Harbour,
Hershey Park, Hunter Springs MHP, Terrace Crossings, Whispering Pines MH FL, Windward Knoll.

Flat (net 0): Applegate MHC, Hendersons MHC, J Bar J Estates, Monson, Northgate MH, Northgate Utility,
Redlands, Riviera, Royal Oaks MHC, Royal Palm, Vantage Oaks Utility, Westwood MHC, Whispering Pines MA.

### Cross-reference: good occupancy, negative net movement

**This is the list the brief asked for: properties that look fine today and will not look fine in two quarters.**
Criterion: occupancy at or above the de-duplicated portfolio average of 77.67%, **and** negative net movement.
(INFERRED grouping; all component figures VERIFIED.)

| Property | Occupancy | Net movement | TTM NOI | Exposure |
|---|---:|---:|---:|---|
| **Triple S Marina** | 89.4% | **-6** | **$1,732,236** | Largest NOI in the portfolio. High-churn asset (33 in / 39 out) so the net is small relative to flow, but it is negative. |
| **Sea Shells MHC** | 85.0% | **-7** | $591,142 | 13 in / 20 out. Steady erosion at a healthy-looking property. |
| **Riverwalk** | 84.4% | **-7** | **$1,360,873** | **The compound risk.** 3rd largest NOI, margin already fell 68% → 52% on utilities, and it is losing residents. |
| **Silver Hill MHC** | 84.1% | **-3** | $724,541 | 1 in / 4 out, a 4:1 outflow ratio, the worst on this list. |
| **Fox Creek** | 78.9% | **-4** | $880,767 | 8 in / 12 out. |
| **Shell Pointe MHC** | 77.0% | **-12** | $176,465 | Just below the threshold but the largest outflow of any above-average-occupancy property. 4 in / 16 out. |

**Riverwalk is the single most important name in this file.** It is the only asset that is simultaneously
(a) top-five NOI, (b) suffering a margin collapse from utilities, and (c) net-losing residents. Its occupancy
of 84.4% is why nobody is looking at it.

**Brunswick Estates, Paradise Palms and Druid Oaks recorded literally zero move-ins in seven months.**
Whatever leasing motion exists at those three is not reaching the system.

---

## 5. Budget variance

`VW_Budget_Comparison`, **TTM Aug-25 → Jul-26**, dimension `propertyName`, measures `revenueVariance`,
`expenseVariance`, `noiVariance`, `utilitiesVariance`, `repairsVariance`.

### ⚠ Read this before reading any number below

**Budget coverage is incomplete and the portfolio-level variance figures are unusable.**

| | Actual (TTM) | Budget (TTM) | Implied variance |
|---|---:|---:|---:|
| Total revenue | $54,813,442 | $37,066,664 | +$17,746,778 |
| Total operating expenses | $28,268,197 | $11,977,686 | **+$16,290,511** |
| NOI | $26,545,245 | $25,088,978 | +$1,456,267 |

Actual opex is **2.36x** budgeted opex portfolio-wide. That is not a $16.3M overrun. It is missing budget data.
**Only 61 of 134 property records carry a non-zero budget.** For the other 73 (including Parakeet Communities,
Geiger Key Fish Camp Opco, Geiger Key RV Resort, Parkwood MHP, Hendersons MHC, Regency I & II, McGregor Downs,
Northgate RV, Hunter Springs MHP, Cambridge MHC and every `x`-prefixed record), **variance = actual, because
budget = 0.** An unfiltered variance ranking puts Parakeet Communities at "+$6,115,825 over budget" when the
real statement is "no budget exists."

**Everything below is filtered to the 61 budgeted properties only.** All VERIFIED.

### Largest revenue misses

| Property | Revenue variance | Budget | Actual |
|---|---:|---:|---:|
| **xParkwood MHC** ⚠ | **-706,420** | 706,420 | **0** |
| **Paradise Lakes** | **-477,598** | 1,315,626 | 838,028 |
| **River Oaks RV Resort** | **-407,682** | 682,556 | 274,875 |
| **Silver Breeze** | **-230,124** | 363,591 | 133,468 |
| **Lucky Clover** | **-200,079** | 1,529,581 | 1,329,502 |
| Whispering Pines MH FL | -175,212 | 1,589,354 | 1,414,141 |
| Vantage Oaks | -153,362 | 1,343,324 | 1,189,962 |
| Palm Haven Estates | -120,239 | 416,341 | 296,102 |
| Belle Haven | -114,027 | 718,207 | 604,180 |
| Triple S Marina | -83,593 | 2,289,707 | 2,206,114 |
| Southgate | -63,681 | 799,938 | 736,257 |
| Applegate MHC | -57,238 | 808,039 | 750,801 |

⚠ **The xParkwood miss is not real. It is a rename break.** The $706,420 budget sits on the archived record
`xParkwood Manufactured Housing Community` (TTM actual: $0), while the $1,028,810 of actual revenue posts to
`Parkwood Mobile Home Park`, which carries **no budget at all**. Budget and actuals were split across the
rename. Netted, Parkwood is +$322,390 to budget, not -$706,420. (INFERRED netting; both components VERIFIED.)

**Real, and large: Paradise Lakes (-$477,598), River Oaks (-$407,682), Silver Breeze (-$230,124).**
All three also appear in the occupancy or margin outlier lists. These are the same three problems seen
from a different angle, not three new ones.

### Largest expense overruns

| Property | Expense variance | Budget | Actual |
|---|---:|---:|---:|
| **The Oaks** | **+407,563** | 373,024 | 780,587 |
| **Riverwalk** | **+390,757** | 437,048 | 827,805 |
| **Windward Knoll** | **+261,285** | 328,897 | 590,183 |
| **Great Oak RV Resort** | **+255,791** | 367,362 | 623,153 |
| **Fox Creek** | **+214,526** | 163,390 | 377,917 |
| Lamberton Lake MHC | +192,645 | 100,948 | 293,593 |
| Mayflower Hills | +172,509 | 79,676 | 252,185 |
| Auburn Ridge | +154,793 | 262,576 | 417,369 |
| Shady Acres MHC | +153,772 | 163,297 | 317,068 |
| American | +151,834 | 133,047 | 284,881 |
| Meadow Woods MHP | +151,057 | 71,198 | 222,255 |
| Su-Rene | +136,955 | 99,989 | 236,944 |

### Largest NOI misses

xParkwood MHC -506,677 (see rename note) · **Paradise Lakes -439,689** · **River Oaks RV Resort -399,538** ·
**Great Oak RV Resort -253,852** · Whispering Pines MH FL -199,814 · Silver Breeze -197,980 ·
Lucky Clover -167,430 · Palm Haven Estates -142,147 · Vantage Oaks -138,792 · Belle Haven -128,997 ·
Carley's MHP -121,115 · Riviera -109,639.

### Utilities: called out specifically

`utilitiesVariance` (actual minus budget) and `utilitiesExpense`. Portfolio TTM utilities: **$5,403,916**
against a much smaller budgeted base. VERIFIED.

| Property | Utilities variance | Utilities actual |
|---|---:|---:|
| **Riverwalk** | **+134,112** | 265,264 |
| **The Oaks** | **+115,526** | 178,036 |
| **Windward Knoll** | **+101,046** | 153,567 |
| **Great Oak RV Resort** | **+97,102** | 215,505 |
| **Monson** | **+79,077** | 115,985 |
| Oakside MHP | +71,668 | 151,577 |
| Lamberton Lake MHC | +61,925 | 103,032 |
| American | +55,690 | 126,188 |
| Carley's MHP | +53,282 | 161,416 |
| Auburn Ridge | +47,443 | 83,085 |
| Su-Rene | +46,920 | 72,711 |
| Fox Creek | +42,734 | 61,368 |

**Utilities is the dominant expense-overrun driver.** At Riverwalk, The Oaks, Windward Knoll and Great Oak,
the utilities variance alone accounts for **33%, 28%, 39% and 38%** of each property's total expense overrun
respectively (INFERRED from VERIFIED components). Riverwalk's is the pass-through gap documented in §3b-i;
the pattern at the other three is worth the same test.

Monson deserves a note: **$79,077 over budget on utilities at a 61-unit property**, the highest
utilities overrun per unit in the portfolio ($1,296/unit variance). Its NOI margin is 44.0% (failing target)
and 64% of its $53,702 AR is over 90 days.

### Repairs and maintenance: called out specifically

`repairsVariance` and `repairsMaintenanceExpense`. Portfolio TTM R&M: **$2,136,876**. VERIFIED.

| Property | Repairs variance | Repairs actual |
|---|---:|---:|
| **Mayflower Hills** | **+76,932** | 85,457 |
| **Meadow Woods MHP** | **+54,863** ⚠ | 43,983 |
| **Great Oak RV Resort** | **+48,737** | 88,087 |
| **Auburn Ridge** | **+44,511** | 84,661 |
| **Riverwalk** | **+42,722** | 60,362 |
| The Oaks | +34,272 | 93,772 |
| Su-Rene | +29,017 | 33,103 |
| American | +25,639 | 37,261 |
| Silver Hill MHC | +24,703 | 34,897 |
| Triple S Marina | +23,912 | 85,310 |
| Fox Creek | +22,809 | 47,941 |
| Monson | +22,664 | 31,483 |

⚠ **Meadow Woods returns a repairs variance ($54,863) larger than its repairs actual ($43,983)**, which implies
a negative R&M budget. Flagging as returned; the figure is internally inconsistent and should not be used.

**R&M overruns are an order of magnitude smaller than utilities overruns** ($2.14M total R&M vs $5.40M total
utilities). Mayflower Hills is the standout: **$76,932 over budget on a $79,676 total expense budget**,
i.e. repairs alone nearly doubled the property's entire budgeted cost base. Its margin is 37.9%.

**Six properties appear in both the utilities and repairs overrun lists**: Riverwalk, The Oaks,
Great Oak RV Resort, Auburn Ridge, American, Su-Rene, Fox Creek, Monson. Those are cost-control problems,
not one-off line items.

---

## 6. Data quality notes

**This section matters as much as the numbers above.** Several headline figures in this file cannot be trusted
at face value, and the reasons are all structural.

### 6.1 Rent Manager: 82 property entities, every one flagged `IsActive: false` (CONFIRMED)

`list_entities(entityType: Properties)` returns **exactly 82 records, and all 82 have `IsActive: false`.**
VERIFIED. There is no active property in Rent Manager's property master.

This is a **maintenance artifact, not reality.** Proof: those same "inactive" properties are transacting.
Riviera (`IsActive: false`, PropertyID 222) produced $2.15M of TTM revenue and is 100% occupied.
Triple S Marina (`IsActive: false`, PropertyID 173) produced $1.73M of TTM NOI. **Do not filter on
`IsActive` in any Rent Manager query. It will return nothing, or it will silently return everything.**
Any downstream integration that respects the flag is broken by design.

### 6.2 Reconciliation: Rent Manager (82) vs warehouse unit listing (104)

**71 names match exactly.** VERIFIED by set comparison.

**In Rent Manager, absent from the warehouse unit listing: 11 records.** All are legal/holding entities with
no rental units, so their absence is expected and correct:

Lamberton Lake Homes · Parakeet Home Sales · Parakeet Home Sales SC, LLC · Parakeet Homes ·
Parakeet MHC Hold Co I · Parakeet MHC Hold Co II · Parakeet MHC Senior · Parakeet Origins I GP ·
Parakeet Origins I Homes · Parakeet Origins I LP · Parakeet Origins Portfolio I

**Not benign:** `Parakeet Origins I LP` and `Parakeet Origins I Homes` appear in **Rent Manager only**.
They return no rows from any of the five warehouse models. Two entities exist in the source system and
are entirely invisible to reporting.

**In the warehouse unit listing, absent from the Rent Manager property list: 33 records.** These split
three ways:

**(a) Archived `x`-prefixed duplicates: 12 records, 690 units.** Rent Manager convention: prefix `x` to
retire a record. All 12 show 0.0% occupancy in the current snapshot but still carry units, market rent,
GL history and, critically, budgets and AR:

| Archived record | Units | Still carries |
|---|---:|---|
| xParkwood Manufactured Housing Community | 100 | **$706,420 TTM budget, $137,340 AR (100% over 90)** |
| xParkwood MHC | 100 | second-order duplicate of the above |
| xBay Oaks Village I | 87 | $167,991 TTM revenue, $50,465 market rent |
| xOrmond Beach Oasis | 62 | $150,661 TTM revenue |
| xOceanaire MHC | 50 | $180,722 TTM revenue |
| xLake Wales MHC | 48 | $98,735 TTM revenue |
| xPalm Spring Estates | 45 | $157,177 TTM revenue |
| xWolf Bay Manufactured Housing Community | 45 | $113,815 TTM revenue |
| xWestwood MHP | 44 | $123,119 TTM revenue |
| xGulf Breeze MHP | 39 | $101,671 TTM revenue |
| xTown & Country MHC | 36 | $145,338 TTM revenue |
| xBay Oaks Village II | 34 | $82,300 TTM revenue |

**The renames happened partway through the TTM window, so financials are split across both names.**
Any single-name TTM figure for these twelve properties **understates the property.** Example:
Ormond Beach Oasis reports $262,271 TTM revenue, but `xOrmond Beach Oasis` holds another $150,661.
True combined TTM revenue is **$412,932**. The same split affects Oceanaire, Lake Wales, Palm Spring,
Wolf Bay, Westwood, Gulf Breeze, Town & Country, Bay Oaks I and Bay Oaks II. There are also two additional
`x` records in the GL that never appear in the unit listing: `xLake Saunders RV` (-$12,038 TTM NOI, still
accruing expense) and `XRiver Oaks` (capital X: $1,021 revenue, -$3,888 expense).

**(b) Shadow duplicate pairs: same community, two spellings, one active and one dead.** In every pair
below, one record holds the occupancy and the other holds the AR or the units, so **neither record alone
describes the property**:

| Pair | Active record | Dead record | The problem |
|---|---|---|---|
| Cedar Grove | Cedar Grove Manufactured Housing Community, 133 units, 93.2% occ | Cedar Grove MHC, 136 units, **0.0% occ** | **$178,871 AR / 123 customers sits on the LIVE record at 100% over 90.** 269 units counted for a ~133-unit property. |
| Colonial | Colonial Manufactured Housing Community, 115 units, 90.4% occ | Colonial MHC, 115 units, **0.0% occ** | $111,839 AR / 103 customers, 100% over 90. 230 units counted. |
| Lambeth | Lambeth Manufactured Housing Community, 69 units, 91.3% occ | Lambeth MHC, 69 units, **0.0% occ** | $87,407 AR / 62 customers, 100% over 90. 138 units counted. |
| Hunter Springs | Hunter Springs MHP, 25 units, 52.0% occ, +$90,782 NOI | Hunter Springs MHC, 25 units, **0.0% occ**, **-$6,442 NOI** | 50 units counted for a 25-unit park. The MHC record drags a real negative into the margin-failure list. |
| Geiger Key | Geiger Key RV Resort, 63 units, 71.2% occ | Geiger RV, 41 units, **0.0% occ** | Plus two more GL-only entities: Geiger Key Fish Camp Opco (-$672,789 NOI) and Geiger Key Resort Propco. **Four records for one asset.** |
| Paradise Lakes | Paradise Lakes, 200 units, 79.5% occ | Paradise Lakes RV, 193 units, **0.0% occ** | 393 units counted. |
| Lucky Clover | Lucky Clover, 128 units, 66.4% occ | Lucky Clover RV, 65 units, **0.0% occ** | 193 units counted. |
| Parkwood | Parkwood Mobile Home Park, 90 units, 66.2% occ | xParkwood MHC + xParkwood MHC (100 each) | **Three records.** Budget on one, actuals on another, AR on a third. |
| Cambridge | Cambridge MHC, 149 units, 61.1% occ | Cambridge Homes, 1 unit, 0.0% occ | Plus `Cambridge MHP Investment` in the GL. |
| Northgate | Northgate MH (222) / Northgate RV (117) / Northgate Utility (70) | `Northgate MHP`, GL only, no units | Utility record has -236.7% margin. |
| Bay Oaks | Bay Oaks Village I & II | xBay Oaks Village I & II | Both live and archived carry TTM revenue. |
| Whispering Pines | Whispering Pines MA / Whispering Pines MH FL | `Whispering Pines RV FL`, $0 everything | |
| Vandemere | n/a | `Vandemere Manufactured Housing Community` (GL, $0 TTM) + `Vandemere Homes` ($318 AR) | No unit record at all. |

**(c) Real communities present in the warehouse but ABSENT from Rent Manager's property list: 12 records.**
Rent Manager's master is incomplete, not just stale:

Apple Creek (209 units, 79.4% occ, $21,828 AR) · **Congress Mobile Home Park (31 units, 100% occ,
$284,460 TTM NOI, $45,968 AR)** · **Geiger Key RV Resort (63 units, $841,628 TTM NOI)** ·
**Shell Pointe MHC (74 units, $176,465 TTM NOI, $125,620 AR)** · **Cambridge MHC (149 units, $311,260 AR)** ·
Countryside MHC (44 units) · Parktown MHC (49 units, $9,181 AR) · Highlands (61 units) ·
Trailerama MHP (121 units) · BEDROCK MHC (1 unit) · plus the Cedar Grove / Colonial / Lambeth
"Manufactured Housing Community" long-form names.

**Congress Mobile Home Park and Geiger Key RV Resort together produce $1.13M of TTM NOI and do not exist
in the Rent Manager property master.** That is the most serious reconciliation gap in this file.

### 6.3 Properties returning no data at all

**Zero occupancy, zero rent, no meaningful GL activity.** These are dead records occupying 1,335 units
in the raw portfolio count (VERIFIED):

| Record | Units | Status |
|---|---:|---|
| Paradise Lakes RV | 193 | Shadow duplicate |
| Cedar Grove MHC | 136 | Shadow duplicate, holds $178,871 AR |
| Trailerama MHP | 121 | **No occupancy, no rent, no GL, not in Rent Manager. Unexplained.** |
| Colonial MHC | 115 | Shadow duplicate, holds $111,839 AR |
| xParkwood MHC | 100 | Archived |
| xParkwood Manufactured Housing Community | 100 | Archived, holds $706,420 budget + $137,340 AR |
| xBay Oaks Village I | 87 | Archived |
| Lambeth MHC | 69 | Shadow duplicate, holds $87,407 AR |
| Lucky Clover RV | 65 | Shadow duplicate |
| xOrmond Beach Oasis | 62 | Archived |
| **Highlands** | **61** | **No occupancy, no rent, no GL, no AR, not in Rent Manager. Unexplained.** |
| xOceanaire MHC | 50 | Archived |
| xLake Wales MHC | 48 | Archived |
| xPalm Spring Estates, xWolf Bay MHC | 45 each | Archived |
| xWestwood MHP | 44 | Archived |
| Geiger RV | 41 | Shadow duplicate |
| xGulf Breeze MHP | 39 | Archived |
| xTown & Country MHC | 36 | Archived |
| xBay Oaks Village II | 34 | Archived |
| Hunter Springs MHC | 25 | Shadow duplicate, -$6,442 NOI |
| Cambridge Homes, Nalls Court MHC (19 units, 100% occ but $0 rent, -$17,100 NOI) | | |

**Highlands (61 units) and Trailerama MHP (121 units) are the two records I cannot explain.** They carry
units in the warehouse, return zero on every measure in every model, and appear in no Rent Manager list.
They are either sold assets never removed, or communities that were never onboarded. **182 units of
unknown status.**

### 6.4 Market rent is missing for more than half the portfolio

`totalMarketRent` returns **0** for **~44 of 104 property records**, including six of the ten largest
NOI producers (Riverwalk, The Oaks, Auburn Ridge, Windward Knoll, Northgate MH, Regency I & II) and
Shady Acres, McGregor Downs, Terrace Crossings, Druid Oaks, Oakside, Great Oak, Geiger Key, Silver Hill,
Su-Rene, Fox Creek. VERIFIED.

**Consequences:**
- Portfolio loss to lease **cannot be stated.** §3c covers only the 35 properties with both fields populated.
- **`VW_Summary_Rent_Roll.lossToLease` is actively misleading** and returns large negative values that read
  as "renting above market" when they actually mean "no market rent on file." See the note in §3c.
- The portfolio market-rent total of $2,715,297/mo is an **undercount of unknown size.**

Conversely, **`totalActualRent` returns 0 for ~40 records** that clearly have occupied units: Riverwalk,
The Oaks, Auburn Ridge, Windward Knoll, Northgate MH, Regency I & II, Triple S Marina, Paradise Lakes,
Belle Haven, Apple Creek, Cedar Grove, Countryside, Parktown and others. **The two gaps do not overlap
cleanly**, which is why so many rows in §2 read `n/d`.

### 6.5 Budget data covers only 61 of 134 property records

Documented in §5. **Portfolio-level budget variance is unusable**: actual opex is 2.36x budgeted opex,
which reflects missing budget rather than overspending. Any variance ranking that is not filtered to
budgeted properties will rank Parakeet Communities and Geiger Key Fish Camp Opco at the top for the sole
reason that they have no budget. VERIFIED.

**The Parkwood rename break is the worst instance**: budget on the archived record, actuals on the live one,
producing a phantom -$706,420 revenue miss and a phantom -$506,677 NOI miss.

### 6.6 $102,501 of AR is not attributable to any property

Sum of the 67 per-property AR rows = **$1,805,700.39**. Portfolio total = **$1,908,201.57**.
**Gap: $102,501.18, so 5.4% of the AR book has no property attribution.** (INFERRED from VERIFIED components.)

Separately, **Parakeet Communities shows $85,975 of AR against `customersWithBalance` = 0**, an internal
contradiction within a single model.

### 6.7 Move-in data has at least one bulk-load artifact

**Shirleys Trailer Park I recorded 32 move-ins and 0 move-outs in seven months at a 32-unit property.**
Shirleys Trailer Park II recorded 8 move-ins, 0 move-outs, 10 units. Both are at 100%/80% occupancy.
This is a **records migration, not leasing absorption.** Treat as VERIFIED-but-artifactual and exclude from
any turnover rate calculation. (Artifact diagnosis is INFERRED.)

Contrast: Geiger Key RV Resort shows 367 move-ins / 369 move-outs in seven months on 63 units. That is
genuine transient RV churn and is fine.

### 6.8 Snapshot models return two `endDate` values in some months

`VW_Rental_Unit_Listing` reportMonth 2025-08 returns both `2025-08-02` (811 units) and `2025-08-31`
(8,012 units). `VW_Budget_Comparison` has stub `endDate` values at 2025-06-07, 2025-08-02 and 2026-07-18
carrying $0. **Always group or filter by month-end, not by raw `endDate`,** or partial-period rows will
double-count. VERIFIED.

### 6.9 Query reliability

One query timed out at 120,000ms (`unitCount` by `reportMonth`, first attempt) and succeeded on retry.
One query exceeded the response size cap (five variance measures × 134 properties) and had to be split.
**Neither affected results.** Both were re-run successfully. Noting for anyone rebuilding this file:
keep variance queries to ≤4 measures when grouping by `propertyName`.

---

## Summary of claims tested

| Claim | Verdict | Correct figure |
|---|---|---|
| River Oaks ~60% actual occupancy despite looking full | **Partly holds** | Blended **38.94%**; core Lot-RV stock **65.0%**. 32 of 113 units are unusable/POH/demo and sit at 0% in the denominator. The "looks full but isn't" instinct is correct; the asset has **negative TTM NOI**. |
| None of River Oaks is listed in Rent Manager at unit level | **FALSE** | River Oaks RV Resort is Rent Manager PropertyID **172**, and the warehouse holds **113 units across 10 unit types** with full occupancy and day-level detail. |
| A property's margin fell ~65% → low 50s pending a city-water pass-through | **Holds** | **Riverwalk**: 68.16% (H1) → 56.64% (H2) → **52.15%** (Jul-26). Utilities +272% H1→H2 while reimbursements stayed flat. Utility type is not separable in the data. |
| 77% of AR at Windward Knolls, ~$84.1K | **FALSE** | Windward Knoll AR is **$14,400** (0.75% of portfolio AR) and has never exceeded $15,298. The 77% is a misread `percentOver90` (Windward hit 77.7% in 2026-05). Closest actual match: **American, $85,940 at 76.9% over 90.** |
| 82 Rent Manager properties, all `IsActive: false` | **CONFIRMED** | All 82. A maintenance artifact. The flagged-inactive properties are transacting normally. Never filter on it. |

---

## Reproducing this file

Every table names its model, measures, dimensions and period. To re-derive:

1. `get_schema`: member names must be passed verbatim.
2. Snapshot models (`VW_Rental_Unit_Listing`, `VW_Aged_Receivables`, `VW_Summary_Rent_Roll`) auto-restrict
   to the most recent period. Group by `reportMonth` to see history. **Always state the as-of period.**
3. `VW_Budget_Comparison` does **NOT** auto-restrict. It returns all history unless you pass a `timeRange`
   on `endDate`. Every financial figure in this file uses `2025-08-01` → `2026-07-31`.
4. `VW_MoveIns_MoveOuts` uses `month` as its time dimension. This file uses `2026-02-01` → `2026-08-31`.
5. Pass `question` on every `run_query` call. It feeds the security audit trail.
6. De-duplicated portfolio totals use a `notEquals` filter on `propertyName` against the 20 archived and
   shadow records listed in §6.3.

**Next refresh:** re-run after the 2026-08 GL month closes to get a clean TTM Sep-25 → Aug-26.

---

## The three things to fix before this baseline can be trusted further

1. **Resolve the duplicate property records.** 33 warehouse records have no Rent Manager counterpart;
   12 are `x`-archived with live financials split across the rename, and ~9 more are shadow pairs holding
   $601,769 of frozen AR. Until this is merged, unit counts, occupancy and loss to lease are all wrong at
   the portfolio level.
2. **Load market rents.** 44 properties have none, including six of the ten largest NOI producers.
   Loss to lease, the fastest recoverable revenue in the portfolio, is unmeasurable for most of the book.
3. **Complete the budgets.** 73 of 134 records have no budget. Variance reporting currently ranks
   "no budget" above "over budget."
