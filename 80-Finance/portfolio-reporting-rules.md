# Portfolio Reporting Rules: Canonical

**What this is:** Austin's own rules for what counts as an operating property. Any report producing portfolio numbers follows these - do not re-derive, do not re-ask.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

**Established**: 2026-08-26, direct from Austin.
**Status**: Authoritative. Any agent or report producing portfolio numbers follows these. Do not re-derive, do not re-ask.
**Applies to**: RentViewer warehouse queries, Rent Manager reports, and anything downstream of them.

---

## Rule 0: Never filter on `IsActive`

All 82 Rent Manager property entities return `IsActive: false`, including Riviera ($2.15M revenue, 100% occupied) and Triple S Marina ($1.73M NOI). **The field is a maintenance artifact. Filtering on it returns nothing.**

Define inclusion by the rules below, not by that flag.

---

## Rule 1: What counts as an operating property

**IN: 67 communities**, plus Triple S Marina, plus 3 utility entities. Austin confirmed 2026-08-26: *"The other properties that are on here, all locally, they should be included, and nothing has been left out."*

**OUT is everything below:**

| Excluded | Count | Reason |
|---|---|---|
| **`Parakeet Communities`** | 1 | Corporate management entity. Carries **−$3,636,103 NOI on $2,479,722 revenue**, pure overhead. Including it drags portfolio margin ~8 points and makes a healthy book look broken. **Never include in property reporting.** |
| **Geiger Key** (all records) | 4 | *"Always been excluded as it is a different animal since it has a restaurant, RV, boat slips."* Covers Fish Camp Opco, Resort Propco, RV Resort, Geiger RV. |
| Funds, holdcos, GPs, LPs | 16 | A2Z entities, BEDROCK entities, Parakeet MHC Hold Co I & II, Origins Portfolio/GP, Grove Banyan entities, ND Communities, Parakeet Home Sales, Founders Group |
| Zero-activity records | 24 | No revenue and no NOI for the full period |
| **Shell Pointe MHC** | 1 | Excluded by Austin's instruction, 2026-08-26 |
| **Cambridge** (all records) | 3 | Excluded by Austin's instruction. Cambridge MHC, Cambridge Homes, Cambridge MHP Investment |

**Triple S Marina is IN.** *"Actually an RV park with boat slips and should be counted or included with everything else."* Do not classify it as non-MH. That was an error corrected on 2026-08-26.

---

## Rule 2: Utilities roll up into their community

Keep them, but **never report them as standalone properties**. Austin: *"Just make sure to lump those in with the actual community it's related to."*

| Utility entity | Rolls into |
|---|---|
| `Applegate Water` | Applegate MHC |
| `Vantage Oaks Utility` | Vantage Oaks |
| `Northgate Utility` | Northgate (MH + RV) |

Combined utility revenue is small ($64,642 TTM) but the **rollup matters for per-community margin**: utility expense sits in one record and the reimbursement revenue in another.

---

## Rule 3: Properties with special treatment

### Southgate: INCLUDE, fully

**Correction to an earlier misreading.** The road-trip review's "Southgate sale closed" referred to **the sale of a home at the property, not the community**. Parakeet still owns Southgate. $736,257 TTM revenue. It belongs in every report.

### Lamberton Lake: INCLUDE, fully

Pending sale, but *"we need to keep this still on the reports."* $273,191 TTM revenue, **−$20,402 NOI**. Do not exclude for being under contract.

### Congress Mobile Home Park: SPLIT TREATMENT

**Sold.** Austin: *"Keep for historical purposes, however, for any up-to-date financial, lot count, occupancy information should be ignored."*

| Report type | Congress? |
|---|---|
| Historical revenue, NOI, trailing-twelve financials | **Include** |
| Current occupancy, lot count, vacancy | **Exclude** |
| Current AR, delinquency, collections | **Exclude** |
| Anything forward-looking | **Exclude** |

$406,477 TTM revenue, $284,460 NOI. It has no Rent Manager counterpart, which is consistent with disposal.

### Hunter Springs MHC / MHP: TWO LEGS OF ONE TRANSACTION, NOT A DUPLICATE

Austin: *"Hunter Springs MHC should not have any activity, whereas MHP should, as that is the second leg of the transaction since we sold it from one investor to the next."*

- **`Hunter Springs MHP`**: current leg. Should carry the activity. $141,872 revenue, $90,782 NOI.
- **`Hunter Springs MHC`**: prior leg. **Should be dormant.**

**⚠ OPEN DISCREPANCY**: `Hunter Springs MHC` currently shows **$35,056 revenue and −$6,442 NOI** for the trailing twelve. That contradicts "should not have any activity." Either revenue is mis-booked to the legacy record, or it is the tail of the transaction period. **Worth one look from accounting**. Until resolved, reporting both records risks double-counting roughly $35K.

### Shirleys Trailer Park I & II: NEW, BASELINE FROM HERE

*"Brand new. So all the initial information is there, and we could start tracking historically."*

$8,125 and $3,250 TTM. **The 32 move-ins / 0 move-outs at Shirleys I is a new-property load, not churn**. Exclude it from absorption and turnover analysis, but treat the property itself as a legitimate baseline going forward.

---

## Rule 4: The x-prefixed records are renames, not duplicates

Thirteen `x`-prefixed records hold **$1,322,550 of real TTM revenue**, the front half of the year under a pre-rename name. Examples: `xOceanaire MHC` $180,722, `xPalm Spring Estates` $157,177, `xTown & Country MHC` $145,338.

**Merge them with their live twin. Do not exclude them**: dropping them silently understates trailing revenue. Including them changes portfolio margin by only 0.24 points, which confirms the merge is safe.

---

## The resulting portfolio: TTM Aug 2025 → Jul 2026

| | |
|---|---|
| Records | **71** (67 communities + 3 utilities + Triple S Marina) |
| Revenue | **$44,412,071** |
| NOI | **$27,870,728** |
| **NOI margin** | **62.75%**, comfortably above the >50% target |
| Operating expense ratio | **37.25%**, well inside the 45 to 50% target |

**Compare: 48.43% margin when corporate overhead and Geiger Key were blended in.** The portfolio was never underperforming. The arithmetic was.

---

## Still open

1. **Hunter Springs MHC's $35,056**: should be zero per Austin. Needs accounting to confirm mis-booking vs. transaction tail.
2. **How many communities is the right count?** Several assets span multiple records: Northgate (MH + RV + Utility), Bay Oaks Village I & II, Whispering Pines MA & MH FL, Shirleys I & II, Hunter Springs MHC & MHP. **Record count ≠ community count.** One decision on how to roll these up would settle every "how many communities do we have" question permanently.
3. **Congress split treatment needs enforcing in queries**, not just documented. Currently no filter implements it.
