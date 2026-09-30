# Delivery Bottleneck Diagnosis — 43 Homes, Aug 31 – Sep 14, 2026

**What this is:** The diagnosis of the 43-home delivery window: set-crew capacity binds, permits do not, and nobody owns the capacity number.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

**Prepared:** 2026-08-26 | **Analyst:** supply-chain-analyst
**Labels:** **VERIFIED** (read the primary source) · **SINGLE-SOURCE** · **INFERRED**

---

## 1. The Binding Constraint

**Set-crew capacity — specifically Champion's set crew. It is not permits, and it is not factory lead time.**

Nobody stated a set-crew capacity number in a two-hour status meeting covering fourteen properties
and forty-three homes. That number does not exist in any system I can query. It is the only input
that determines whether the next two weeks work, and it is the one input nobody owns.

**The arithmetic that settles it.** Current average from delivery to set-complete is **37 days**,
against a 45–60 day target — reported as a success (**VERIFIED**, Lucky Clover Site Visit,
Plaud `9532e6eba522ac6125b40946762a628d`, 08-20). Apply it:

| Delivered | + 37 days | Set-complete |
|---|---|---|
| Aug 31 (first) | | **~Oct 7** |
| Sep 14 (last) | | **~Oct 21** |

**At the historical average, with unlimited crew, zero of the 43 are set-complete before October 1.**
CO comes after that — the 8/26 meeting puts CO at "mid-September" for homes *already being set*,
so CO lags set-complete by additional weeks (**VERIFIED**, Plaud `c27bbc61324143a8e9dcb744a85a4ea6`).

And 37 days was achieved at a *much lower run rate*. 43 homes in 14 days is **3.07 deliveries per
day** against a pipeline that has never demonstrated anything close to that in CO conversion.

**The failure mode is already running at Applegate.** Champion delivered homes on 7/22 and 7/23.
As of the 8/19 site visit they were still unset, with the cause named explicitly: Champion was
"a no-show for a second time, directly blocking progress on at least two homes"
(**VERIFIED**, Applegate Site Visit, Plaud `26975b73a3b820c0b579d23cfd75d7bf`). As of today that is
**34–35 days on site, unset**. Nothing in the 8/26 meeting indicates it has been resolved.

**Effective capacity is lower than nominal, because one of the two crews produces rework.**
Field review found "night and day" differences between crews — stairs built against door swings,
exposed wood, missing caps, mismatched concrete — with the verdict: *"We are paying for the same job
twice"* (**VERIFIED**, Paradise Palms Visit, Plaud `8c0634fc8d6f29965cdc5178106a8ed7`, 08-22;
corroborated at Riverwalk in the 08-25 meeting, `9d97fab1d8c2edad1e900a2cfbaf9ba1`).

**Champion is simultaneously the set contractor, the transport constraint, and the QC problem.**
The 8/25 meeting flags "the transportation issue for moving homes out of storage" as significant and
unresolved, pending a Champion/Bennett meeting (**VERIFIED**). Single vendor, three chokepoints,
no committed capacity figure.

---

## 2. Permit Gating Table — Permits Are Noisy, Not Binding

Permits were the most-cited blocker in the 8/26 meeting. They are **not** the constraint on these 43.
Where permits are pending, the homes are mostly *not in the 14-day window*. Where homes *are* in the
window, permits are largely in hand — or the team has decided to proceed regardless.

| Property | Permit status | What it blocks | In-window homes | Binding? |
|---|---|---|---|---|
| **Great Oaks** | In hand; only lot F-15 site plan pending | F-15 only | 4 ready mid-week | **No** — homes already set/blocked |
| **Harbor** | Submitted, completeness review w/ COCO | **Pads cannot start** | Absorbing Tradewinds lot 46 order | Yes, but few in-window |
| **Lucky** | **17 of 22 received** | Little — septic is the gate | 5 shifted from Northgate | **No** — septic abandonment binds |
| **Northgate** | In hand | — | 3280 + 4 on 9/3 | **No** |
| **Paradise Palms** | In hand | — | 2 done by 8/28 | **No** — septic + meters bind |
| **Paradise Lakes** | Site plans approved; permits submitted by 8/28 | Everything | ~0 in window | Yes, but out of window |
| **River Oaks** | Soft-set permissible for park models | Some lots too tight | 9/2 and 9/3 | **No** |
| **Seashells** | Pads in process | 3 demos first | First delivery 9/4 | **No** — demo/pad sequence binds |
| **Silver Breeze** | **Filing, not approved** — decision to file rather than wait | Everything | ~0 in window | Yes, but out of window |
| **The Oaks** | Remaining by 8/28; lots 11 & 39 site plans pending | Lots 11, 39 | Lot 37 on 9/8 | Partial |
| **Trade Winds** | **Lot 46 DENIED** (never-developed lot); order pivoted to Harbor | That one home | 9/4 | Resolved by pivot |
| **Vantage Oaks** | **ALL in plan review**; city ANSI amperage comment answered | 12 homes | **12 next week + remainder** | **YES — the one real permit risk** |
| **Whispering Pines** | Site plans early next week; permits end of that week | Everything | 0 in window | No homes in window |
| **Windward Knoll** | In hand | — | Arrive 9/8, set on arrival | **No** |

**Why permits look binding but aren't:** permits are the one thing everyone can *report a status on*,
so they dominate the meeting. Set-crew capacity generates no status line because no one measures it.
Reported blockers are a poor proxy for real blockers.

**Aggravating detail (Okeechobee/Vantage):** permit packets require two copies of the install manual,
and permits must be **paid for and physically collected within 72 hours of issuance or they cancel**.
Permit processing is running **three weeks behind**. (**VERIFIED**, Vantage Oaks Site Visit,
Plaud `4c03ae6cda8fe18d717cdc77afd67911`, 08-21.)

---

## 3. Set-Crew Capacity — The Unstated Number

**I cannot compute set-crew capacity. The data does not exist.** That is the most important finding
in this document, because it explains why the problem persists.

**What I could establish as a ceiling.** August 1–26, 2026, portfolio-wide, across ~31 properties:
**82 total move events** (Rent Manager `MoveInMoveOut` report 77, run 2026-08-26 — **VERIFIED**).
At the thirteen delivery-window properties, roughly **25 move-ins in 26 days** — and those include
ordinary resident turnover on existing lots, not new-home COs. **Seven of the thirteen
delivery-window properties recorded zero move-ins in August**: Paradise Palms, Paradise Lakes,
Sea Shells, Silver Breeze, Tradewinds, Harbour, Great Oak.

Warehouse corroborates the plateau — move-ins have run 86–165/month portfolio-wide all year
(`VW_MoveIns_MoveOuts`, Sep 2025 – Aug 2026, **VERIFIED**), with no upward trend that would suggest
absorption capacity is expanding to meet a 43-home surge.

**So: true new-home CO throughput is demonstrably below 1 per day portfolio-wide, against a plan
requiring 3.07 deliveries per day into one two-week window.**

### What is missing, and exactly where it would live

1. **Set-crew count and weekly slot capacity.** Exists nowhere. Would live in a Champion contract or
   scheduling commitment. *Not a system gap — a vendor-management gap.*
2. **Home delivery dates.** Known only because someone said "July 22nd" on a recording. There is no
   delivery-date field anywhere queryable. **Days-on-site-unset therefore cannot be computed
   systematically** — the purest measure of dead capital is unmeasurable.
3. **WIP by stage.** No system tracks a home between order and CO. Rent Manager only knows a unit
   once it is leasable; the warehouse only sees occupancy after move-in.
4. **Capital deployed into homes.** `VW_Budget_Comparison.capexExpense` and `.nonOperatingIncome`
   return **null for every property for all of 2026** (**VERIFIED** — confirmed against the
   `capexAccounts` segment for July 2026). Home capital and home-sale revenue live in Rent Manager
   GL (93xxx–94xxx CapEx, 81xxx home sales) and in the inventory entities **Parakeet Homes (221),
   Parakeet Home Sales (341), Parakeet Origins I Homes (277)** — none of which the enabled reports
   expose. The 8/25 meeting confirms CapEx review is happening *manually in Rent Manager*.
5. **Per-property vacancy via this connector is currently broken.** `UnitAvailability` (10),
   `Vacancy` (74), and `UnitTypeVacancy` (75) all returned HTTP 500 when scoped to a property.

**The connection worth making:** the QuickBase/FastField build discussed on 8/18 was explicitly
scoped to give corporate staff "analytics, process monitoring, and identifying bottlenecks." Its
July launch target was missed and the project was described with significant frustration
(**VERIFIED**, Plaud `e9006917b555cb88ad3dc2a47705f2ed`). **The bottleneck is invisible because the
system built to show it is not live.**

---

## 4. Dead Capital

### Confirmed and measurable

**Applegate: 2+ homes, 34–35 days on site unset** (delivered 7/22 and 7/23; unset at the 8/19 visit;
no resolution recorded through 8/26). Cause: Champion no-show, twice.

Forgone lot rent, shown as arithmetic:
- Applegate average actual rent **$715/month** (**VERIFIED**, `VW_Rental_Unit_Listing`, most recent
  snapshot period) → $715 ÷ 30.4 = **$23.52/day**
- 2 homes × 34.5 days × $23.52 = **≈ $1,620 forgone lot rent** *(ESTIMATE)*

### Scaled to the 43

Delivery-window properties with a rent basis (**VERIFIED**, same source): Sea Shells $795,
Applegate $715, Tradewinds $665, Palm Spring $650, River Oaks RV $875, Whispering Pines FL $372,
Silver Breeze $367, Lucky Clover $321, Vantage Oaks $125. The low figures are RV/undeveloped-heavy
communities; new MH lots should price at or above the MH-community averages. **Using $700/month as
the new-home lot-rent basis (INFERRED from the $650–$795 MH cluster):**

- $700 ÷ 30.4 = **$23/day per home**
- 43 homes × 37 days (baseline set cycle) = 1,591 home-days → **≈ $36,600 forgone lot rent**
- **Each additional week of slip across all 43: 43 × 7 × $23 ≈ $6,900/week** *(ESTIMATE)*

### The number I cannot compute — and it is the big one

**Lot rent is not where the money is.** These are homes to be *sold*; the revenue event is the home
sale, not the lot lease. Vantage Oaks is preparing for **twenty new home sales per month**
(**VERIFIED**, Plaud `4c03ae6cda8fe18d717cdc77afd67911`). At that rate, 43 homes is roughly **two
months of the entire sales plan**, and every week of slip defers a corresponding share of sale
proceeds plus carry on the homes' invoice cost.

**I cannot size it.** Home invoice cost is not in the warehouse (capex null) and not in any enabled
Rent Manager report. Give me home invoice cost and delivery dates and this becomes a real number
within an hour. **Until then, treat the $36,600 lot-rent figure as a floor that understates true
dead capital by roughly an order of magnitude.**

---

## 5. Slip Risk Stack Rank

| # | Property | Homes | Reason |
|---|---|---|---|
| 1 | **Vantage Oaks** | **12** | Largest block in the window on permits **still in plan review**. Okeechobee: 72-hour pickup-or-cancel, processing 3 weeks behind. Inspector requires 200-amp pedestals to match 200-amp homes — no deviation. Team plans to set "even if electrical hookups are pending," which sets without CO. |
| 2 | **Paradise Palms** | 3 lots | **Septic issue awaiting county response** — exogenous, no committed date, direct CO blocker. Also awaiting electric meters; homes risk being set, surveyed and trimmed with no meter. |
| 3 | **Lucky** | 5 | Homes shifted from Northgate to lots 28/27/29/58/97. Pads only where septic abandonment complete; **sewer not done until Labor Day (9/7)**. Entire sequence compressed into the back half of the window. |
| 4 | **Harbor** | absorbing Tradewinds 46 | Permits in completeness review; **pads cannot start until permits received**. No pad, no set. |
| 5 | **Applegate** | 2+ already failed | Homes unset 34+ days with the vendor named as cause. Adding volume here repeats the failure. |
| 6 | **The Oaks** | lot 37 (9/8) + 11, 39 | Lots 11 and 39 site plans still pending; remaining permits due 8/28. |
| 7 | **River Oaks** | 9/2, 9/3 | Some lots may be **too tight to build on** — flagged 8/26, unresolved. Walkways await seals. |
| 8 | **Seashells** | first 9/4 | 3 demos must finish by 8/28 before pads. Tight but properly sequenced. |
| 9 | **Northgate** | 3280 + 4 on 9/3 | 3280 not delivered; 3306/3311 mid-set. Moderate. |
| 10 | **Windward Knoll** | 9/8 | "Set on arrival" — low risk *if* a crew is actually booked. Nobody confirmed one. |
| 11 | **Great Oaks** | 4 | Lowest risk. Homes set, blocked, ready. Only F-15 pending. |

**Three most at risk: Vantage Oaks (12 homes, 28% of the window), Paradise Palms (3 septic lots),
Lucky (5 shifted homes).**

---

## 6. The October Question

**No. These 43 do not land before snowbird season, and the gap is not close.**

At the **verified** 37-day delivery-to-set-complete average — the team's own best-case number,
achieved at a fraction of this volume, with unlimited crew assumed — the first home delivered 8/31
is set-complete **~Oct 7** and the last delivered 9/14 is set-complete **~Oct 21**. CO follows set
by additional weeks. **Zero of the 43 reach CO before October 1.**

### What would have to be true for October to work

1. **Champion commits a set-crew count and weekly slot allocation in writing before 8/31** — and it
   is at least 3 homes/day sustained. No evidence such capacity exists.
2. **Soft-set is used wherever permitted.** Park models can be soft-set in **~15 days** versus 37
   (**VERIFIED**, Lucky Clover Site Visit) — permissible at River Oaks and similar jurisdictions.
   Every soft-set-eligible home given full-set treatment burns **22 unnecessary days**.
3. **Deliveries are re-sequenced to crew capacity**, not to plant availability. Any home delivered
   without a booked set slot becomes another Applegate.
4. **The Paradise Palms county septic response and the Lucky sewer completion both land on time**
   — both are exogenous.
5. **Vantage Oaks' 12 permits clear plan review this week** and are physically collected inside the
   72-hour window.

Items 1 and 3 are inside your control. Items 4 and 5 are not. **Plan for the 43 to land across
October and into early November, and set the snowbird sales expectation accordingly now** — rather
than discovering it in the second week of October.

---

## 7. Highest-Leverage Intervention

**Get Champion's committed set-crew count and weekly slot allocation in writing before the first
truck rolls on August 31 — then cancel or re-date every delivery that does not have a booked set
slot behind it.**

Delivering a home without a confirmed set slot does not accelerate anything. It converts a home
into stored inventory, adds storage and double-handling cost, adds damage risk, and — as Applegate
proves — burns 35 days. **Applegate is not an anomaly. It is the preview of what 43 homes into an
unmeasured crew looks like.**

Second lever, no new crew required: **audit the 43 for soft-set eligibility this week.** At 15 days
versus 37, every home moved to soft-set removes 22 days from the critical path. This is the only
compression available that costs nothing and needs no one's approval but yours.

---

## Sources

| Source | ID / Ref | Used for |
|---|---|---|
| Plaud 08-26 Project Status (2 hr) | `c27bbc61324143a8e9dcb744a85a4ea6` | 43-home count, property-by-property permit/pad status |
| Plaud 08-25 Construction QC & Budget | `9d97fab1d8c2edad1e900a2cfbaf9ba1` | Champion QC, Tradewinds 46 denial, Lucky 22-permit cap, storage/transport issue, CapEx in Rent Manager |
| Plaud 08-18 Ops / System Integration | `e9006917b555cb88ad3dc2a47705f2ed` | QuickBase/FastField delay, missed July launch |
| Plaud Lucky Clover Site Visit 08-20 | `9532e6eba522ac6125b40946762a628d` | **37-day set average vs 45–60 target; 15-day soft-set** |
| Plaud Vantage Oaks Site Visit 08-21 | `4c03ae6cda8fe18d717cdc77afd67911` | Okeechobee 72-hr rule, 3-week permit backlog, 200-amp pedestal rule, 20 sales/month target |
| Plaud Applegate Site Visit 08-19 | `26975b73a3b820c0b579d23cfd75d7bf` | **Homes delivered 7/22 & 7/23 still unset; Champion no-show ×2** |
| Plaud Paradise Palms Visit 08-22 | `8c0634fc8d6f29965cdc5178106a8ed7` | Two-crew quality divergence, "paying for the same job twice" |
| RentViewer `VW_Rental_Unit_Listing` | most recent snapshot | Avg actual rent by property (Applegate $715, etc.) |
| RentViewer `VW_MoveIns_MoveOuts` | Sep 2025 – Aug 2026 | Portfolio move-in trend, no absorption growth |
| RentViewer `VW_Budget_Comparison` | 2026 YTD + Jul 2026 | **CapEx / non-operating income null — capital invisible** |
| Rent Manager `MoveInMoveOut` (77) | run 2026-08-26, Aug 1–26 | 82 move events; 7 delivery-window properties at zero |
| Rent Manager reports 10 / 74 / 75 | — | **HTTP 500 when property-scoped — vacancy unqueryable** |

*Speakers in the 8/26 meeting summary are unattributed; no commitment in this document is assigned
to a named individual from that source.*
