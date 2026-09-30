---
name: asset-inventory
type: register
status: open
---

# Home asset inventory and the tie-out

**What this is:** the analysis page for the homes Parakeet owns. Five systems each hold a list of them and no two agree. This page holds the reconciliation, leg by leg, and the count of what disagrees. The insurance schedule is one leg of it, not a separate errand.

**Status:** current, 2026-08-31. Built to hold work that had been running as four disconnected email threads since 2026-08-27.

**Why it exists.** Austin, 2026-08-31: the insurance tie-out belongs with the analysis on the asset inventory, and all of it should match each other. Before this page the insurance leg sat alone in `00-Meta/commitments.md` item 15 while the floor line leg, the manufacturer leg and the Rent Manager leg sat in three other places. Read apart they look like four chores. Read together they are one question with one answer: **there is no single home inventory, so every system is authoritative and none of them is.**

Confidence labels below are per [[CLAUDE]] rule 10. Money figures are in `00-Meta/numbers-ledger.md` under "Home asset inventory and floor line" and are not restated here.

## The five lists

| System | What it claims to hold | Who owns it |
| --- | --- | --- |
| Rent Manager master | every home as an asset record with a serial | Daniel Bennett, Moe Mehmood |
| Floor line lenders | CountryPlace, 21st Mortgage, Triad, each with their own funded and pending list | David Berman, lender-facing |
| Insurance schedule | the carrier's list of what is covered | assigned 2026-08-27, unaccepted twice, stays with accounting |
| Manufacturer orders and invoices | Cavco and Champion order sheets, and what has been invoiced | Leslie Croft on the order side |
| `60-Communities/assets/` | 10 sheets, homes with an identity that is in dispute or in motion | this Brain |

**The Property Data Sheet's park-owned-home counts are a sixth list** and are not reconciled to any of the five. Flagged, not counted.

## What disagrees, leg by leg

All figures below are counts of serials, VERIFIED from Jon Wyss's "Floor Line Tie-Out" email of 2026-08-27 11:55 ET with the `Floor Line Tie-Out_2026-08-27_001.xlsx` attachment, and from Berman's rebuild of 2026-08-31 02:13 ET. Both email bodies were read in full.

**Floor line against Rent Manager**

- **59 serials appear on more than one row. 46 are full duplicate submissions**: the home is already funded at one lender, mostly CountryPlace, and is also sitting as a roughly full-balance pending approval at a second, mostly 21st.
- **13 small add-on approvals** ride serials that are already funded.
- **29 homes have no floor line row at all**, marked "Cash, verify."
- **16 homes** carry a noted lender that disagrees with the floor line.
- **SS-284, SS-304 and SS-342** are floored at CountryPlace and absent from the Rent Manager master.
- **Five serials exist in no system of Parakeet's**: 71825, 71826, 71827, 71829, 72012.

**Rent Manager against itself**

- **RO-2704 and RO-2706 share a serial.** NGRV-99 carries a typo. **BELL-23 and RO-2732 share a Tiny Heirloom serial.**

**Lenders against what we actually ordered**

- **28 homes of orders the lenders were never told about**, and **32 homes carrying an address the lender was given wrong.** Berman, 2026-08-31.

**Insurance schedule against the corrected master**

- Not started. Austin's framing when he added the leg on 2026-08-27 12:52 ET is the whole case for it: *"A home we own that is not on the schedule is sitting uninsured. A home on the schedule we no longer own is premium we are burning every month."* SS-284, SS-304 and SS-342 are the first three checks, because they are already known to be in one list and not the other.

**Manufacturer against invoices**

- At Lucky Clover, **eleven homes are struck through on the Cavco sheet** with no live order and shared order numbers, and **invoices are logged against all eleven.** Leslie Croft asked what is actually owned. Open as of 2026-08-27. Source: the Pulse block on `60-Communities/lucky-clover.md`.

## Why it matters beyond the accounting

**This is the explanation for the claim that there was no floor line capacity to buy homes.** The line looked full because homes were counted twice. That single sentence is the reason this page is an analysis page and not a filing cabinet: the inventory defect was reading as a capital constraint, and it changed what the company thought it could afford to do.

The facility position as Berman rebuilt it on 2026-08-31 is in the ledger. It is a decision tagged AB/JW, so it needs Austin and Jon together.

## Root cause, as stated by the people closest to it

- **Austin, 2026-08-27:** *"Every issue Jon flagged below traces back to a step in that document being skipped."* He re-issued the Home Ordering SOP to the full thread.
- **Berman, 2026-08-27 22:00 ET, naming the same step from the other side:** **Step 2, Point 12 of the Home Ordering SOP.** *"Nobody is communicating to Accounting/Finance before an order is placed so we can direct how to finance the home and handle everything that rolls downstream from there."*

Two people on opposite sides of a dispute independently named the same missing step. That is the strongest signal on this page. VERIFIED, both emails read in full.

**Jon also flagged the Cavco call as the place to fix the manufacturer to lender comms flow** so it stops recurring. Fixing the flow and cleaning the list are two jobs, and only the second one has ever been assigned.

## Decisions

- **2026-08-31 - The serial-by-serial insurance tie-out stays with accounting.** Austin declined to reassign it after two non-acceptances. It keeps its owner and needs a **date** instead of a new name. (Source: Austin, on the delegation board.)
- **2026-08-31 - The insurance leg is filed with the asset inventory analysis, not on its own.** Austin: it should sit with the analysis on the asset inventory and all of it should match each other. This page is that instruction. (Source: Austin, in session.)
- **2026-08-27 - Insurance costs added as a leg of the reconciliation.** Austin, 12:52 ET, on Jon's tie-out thread.

## Open, and who has it

- **The insurance tie-out has an owner and no date.** Berman, Daniel Bennett and Moe. Answered around twice, on 2026-08-27 and again on 2026-08-31, both times with the mechanics of lender reporting rather than the schedule. `00-Meta/commitments.md` item 15.
- **Jon's three proposed assignments still have no named owners.** He wrote them as open questions, not instructions, and nobody converted them. No owner is invented here.
- **Berman's capacity list is the one live deliverable** anyone has accepted: he said he will circulate legitimate capacities so the lenders can remove pending orders from the lines. Track that.
- **This page has no reconciled count of homes owned.** That number does not exist anywhere yet, which is the point. Do not quote one until the tie-out produces it.

## Related

- [[70-Operations/sops/001-home-ordering-delivery-and-set]] - the process whose skipped Step 2, Point 12 both sides name as the cause.

## Sources

- Jon Wyss, "Floorplan Line Tie-Out, Floor Line Inventory vs RM Infill Invoices," 2026-08-27 11:55 ET, attachment `Floor Line Tie-Out_2026-08-27_001.xlsx`. Email body read in full.
- David Berman, floor line rebuild and facility position, 2026-08-31 02:13 ET. Email body read in full.
- `00-Meta/commitments.md` item 15, where this ran before it had a page.
