# Ramp

**What this is:** the company credit card programme — how the field and the internal rehab crews buy anything.

**Status:** current — 2026-08-30

## The facts
- **What they supply:** company credit cards with per-charge memo and allocation fields. Cards are held widely across the company — the Rellit call describes "everybody running around with credit cards."
- **Who uses it:** internal rehab crews and field staff on the internal rehab path (SOP 105b), plus community and maintenance spend. The Director of Operations sets the GL codes the charges must carry; Accounting confirms the coding before a rehab can be closed.
- **The GL rule: every Ramp card charge carries the GL code in the memo field, entered immediately, in the format `GL [XXXX] — [vendor or description]`** (SOP 105b). No charges may be booked at all until a valid Rent Manager issue number exists and the Director of Operations has entered GL codes in the issue's **"GL — Total Cost" UDF**.
- **The rehab cannot be marked complete until Accounting confirms GL coding.** Expected internal rehab duration is 14–30 days, so the coding discipline has to hold across the whole job.
- **The Home Depot / Lowe's convention: every Home Depot and Lowe's transaction carries the rehab Issue number and the lot in the memo**, so internal costs can be pulled back out per home later (SOP 104 data-entry standard). This convention is **mandatory now** precisely because the accounting GL pull is not yet configured and the internal build cost field is left blank.
- **How critical: high — this is how the field buys anything.** There is no petty cash process, no purchase-order process and no company-card alternative documented anywhere in 242 process files. Pull Ramp and internal rehab stops the same day, along with routine maintenance purchasing across 67 communities.
- **Known problems — the issue is timing, not the cards.** From the 2026-08-21 Rellit conversation: Ramp spend "used to be [reviewed] once a week at least to give me an idea of what the spend was per week. Now they're doing it once a month so it's kind of like blind." Books close **30 to 45 days in arrears**, and the transactions are not booked until month end.
- The stated standard on the same call: "when people are booking things or putting their memos and allocations in Ramp, it should be booked right away. And therefore we know where we are." That is the definition of the live-close target.
- **A native Ramp integration is a named requirement of any replacement accounting platform**, alongside a Rent Manager API connector — and **Parakeet offered to broker the introduction to the Rent Manager team** to help build that connector.
- SOP 105b's GL codes are all placeholder `[GL-XXXX]`, so the memo format the process depends on currently has no real code list behind it.
- Ramp appears in only one SOP by name (105b) and in SOP 104's memo convention. There is **no card-issuance, card-limit, receipt or spend-policy SOP anywhere** — the 600s Systems band is empty and the AP Process row covering PO and coding compliance has nothing started.

## Decisions
- 2026-08-21 — Any replacement accounting platform must integrate natively with Ramp and pull Rent Manager ledger data by API; Parakeet will introduce the vendor to the Rent Manager team to help build the connector. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-rellit-conversation]])

## Sources
- [[70-Operations/sops/105-poh-rehab]] — the internal rehab gates: issue number, the "GL — Total Cost" UDF, and the Ramp memo format.
- [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-rellit-conversation]] — Ramp spend booked monthly instead of reviewed weekly, and the native-integration requirement.
- Austin, in the Structure Interview, 2026-08-30.
