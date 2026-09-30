# WP-36-M3 signature review, 2026-09-03

**What this is:** a line by line read of the memo Austin signs on 2026-09-04, checked against what WP-38 can actually support. Written because he is signing an assertion of fact rather than a document request, so the wording carries the risk.

**Status: SUPERSEDED IN PART, same day. DO NOT SIGN M3 AS DRAFTED.** The earlier recommendation on this page was to sign once the arithmetic re proof confirmed there was no Class A exception. **The re proof found one, and found a second defect the review had not anticipated.** The conditional did its job and the condition failed. **The revised recommendation is at the top of the section headed "REVISED 2026-09-03 after the re audit returned" below.** Everything above that section is the original review, left unedited, because the reasoning that produced the condition is worth keeping.

**Original status line, kept for the record:** current, recommendation sign with one figure to confirm first.

**Decision it implements.** Austin, 2026-09-03: sign M3 on 09-04, hold `WP-36-M1 v2` and `WP-36-M2 v2` until the re-audit lands. Reasoning: M3 asserts a fact and rests on three tie-outs; the other two are document requests, so holding them costs nothing and signing them early gains nothing. The 09-04 date is self-imposed weekly Friday cadence, not external. The only external anchor is Citrin fieldwork around 2026-10-01.

## What the memo actually asserts

Five claims, in its own order.

1. **The Fund was funded in full at subscription.** The Subscription Booklet directs each accepted subscriber to remit the entire Capital Commitment by ACH after acceptance, so no installment or drawdown schedule was established.
2. **The Fund carries no unfunded commitment.** Contributed capital equals position value for **every Class A limited partner position**, aggregating **$12,589,708**.
3. **No drawdown transaction exists.** Activity records for 2017-01-01 through 2026-12-31 contain investment, distribution and transfer transactions only. The 66 investment transactions aggregate $12,589,708 and reconcile without variance to the position schedule.
4. **The mechanic existed and was not used.** The PPM contemplates a Commitment Period with drawdowns on at least seven days notice and a default remedy. The General Partner never exercised it and no capital call notice was ever issued.
5. **Reclassification.** The 2019 Closing Letter has been refiled from 2.3 to 2.5 as the offering document behind the second tranche subscriptions.

It closes by making itself self superseding: if capital call documentation is later identified it goes in 2.3 and this memo is replaced. That is good drafting and it lowers the risk of signing.

## Three findings

### 1. The memo's third leg is weaker than the memo states. HIGH, and it does not overturn the conclusion.

**Claim 3 proves a negative from the completeness of the investor activity ledger.** The memo says no transaction is recorded as a capital call, drawdown or contribution notice, and treats the ledger's silence as proof.

**WP-38 Finding 4 proves that same ledger is incomplete.** Its own words on the activity ledger: it holds 66 investment, 2,043 distribution and 14 transfer rows, and *"The 2020 Khodara-to-WCO transfer is not among them."* A transfer that demonstrably occurred, and that the partnership returns have reported correctly every year since 2020, is missing from the ledger.

**So the document supplying leg 3 is proven to omit at least one real transaction.** A ledger that can omit a transfer can in principle omit a call, which makes its silence corroboration rather than proof.

**Why this does not stop the signature.** Legs 1 and 2 do not depend on ledger completeness at all. Leg 1 comes from the Subscription Booklet's payment mechanics and leg 2 from the position schedule. Either alone supports the conclusion and the two together are the substance of it. **Leg 3 should be read as consistent with the other two rather than as independent proof.** WP-38 calls its three tests independent while elsewhere documenting the gap in one of them, and both statements cannot be fully true at once.

### 2. One scope word may be wrong, and it is checkable before signature. MEDIUM.

**The memo says contributed capital equals position value for "every Class A limited partner position."** WP-38 names exactly one exception and it is a **Class B** position: Bedrock I Group's 100 Class B units at $100 position value against $0 contributed, tracked separately as register 5.05. **On that reading the memo is deliberately and correctly scoped**, because it says Class A and the exception is Class B.

**But WP-38's Lamberton thread describes a possible Class A exception that it never connects to this memo.** Register 5.05 establishes that **Bedrock I Group's $137,500 Class A position is the Lamberton Lake investment, funded by J315 on 2017-11-02 for $160,000** against a payable to A2ZI. **A $137,500 position against $160,000 of funding is a mismatch on a Class A position**, and the memo asserts there are none.

**Flagged as a question rather than a defect.** The $160,000 may be the property cost rather than a capital contribution, and the two figures may not be a position-to-contribution pair at all. **It is being independently tested as item 10 of the arithmetic re proof.** If it resolves as a genuine Class A exception the memo needs one clause acknowledging it before signature. If it resolves as a cost figure the memo is correct as drafted.

### 3. Leg 1's source document sits in the folder whose names were proven unreliable. MEDIUM.

WP-38 cites the **Subscription Booklet exemplar in folder 1.8** for the single payment mechanic. **The 2026-09-03 archive audit proved that names in 1.8 do not reliably match contents**, with roughly two dozen files confirmed wrong about the investor, the document type, or both, and some copies truncated to the point of extracting zero text. See [[80-Finance/fund-reporting/bmhcii-archive-audit-2026-09-03]].

**So the citation may not point at the document the conclusion rests on.** Being tested by the source integrity pass. **The exposure is low, because the subscription mechanic is a feature of the offering rather than of any one investor's booklet**, and the PPM independently describes the same structure. But a signed memo citing a booklet that turns out to be a different investor's document is an avoidable problem.

## Two smaller notes

- **The date line is blank**, reading `Date ____________, 2026`. Austin fills it on signature.
- **The memo says it responds to the Murad diligence request.** WP-36's own Murad Request Ref column is **blank** for item D-03, the capital call item, so it is not tied to a numbered Murad line. Not a defect, since the memo's framing is broader than the numbered list, but worth knowing if the memo is ever read beside the request it cites.

## REVISED 2026-09-03 after the re audit returned. DO NOT SIGN M3 AS DRAFTED.

**The condition failed. M3 asserts a dollar figure that the Fund's own general ledger contradicts, and it asserts it twice.**

### The finding that stops the signature. VERIFIED independently, twice, from primary records.

**Maria Forster's $4,798 is not a subscription. It is a distribution going the other way.** InvestNext records it as her second subscription dated 2020-07-15. The Fund's general ledger records the same amount as an outbound ACH:

- `10_Source_Data\GL_Exports\R-46_GL_FUNDIILP_fulllife_pull20260902.csv` **line 1157**: `CHECK`, reference `ach`, payee `Mariya Forester`, dated **2020-07-22**, credit to bank `10008 BAML - BEDROCK Fund II LP - 3502` of **$4,798.00**.
- **Line 9949**: the same item posted as a **debit to `36000 LP Distributions`** of $4,798.00.
- **Corroboration from her own payment history.** Her recurring quarterly distribution is **$4,798.20**, visible at lines 1008, 1206 and 1329 for Q4 2019, Q3 2020 and December 2020, each with the matching `36000 LP Distributions` leg. **The disputed item is twenty cents off her standing quarterly, to the same payee, out of the same account, with the same accounting treatment.**
- **No $4,798 deposit exists anywhere in the GL.** Reported by the arithmetic re proof and consistent with the above.

**Consequence for the memo, which is the point.** M3 states contributed capital aggregating **$12,589,708** and **66 investment transactions**. If the Forster item is an outbound distribution mis-keyed as an inbound subscription, the true figures are **$12,584,910 across 65 transactions**. **The memo asserts $12,589,708 twice and reconciles it "without variance."** A signed memorandum to the file asserting a figure the general ledger contradicts is the one outcome this review existed to prevent.

### The second defect, which is larger but less certain

**$137,500 of Bedrock I Group's Class A contribution has no capital-contribution credit in the GL.** The arithmetic re proof reconciles it exactly: GL `35000` credits of $13,140,903, less a reversed $500,000 Forster deposit and a $193,493 Tarheel journal, gives **$12,447,410**, which equals $12,589,708 less $137,500 less $4,798 **to the dollar**. A to-the-dollar reconciliation across three independent adjustments is strong evidence.

**But two of the re audit's own findings are in tension here and this page will not pick between them.** Its finding 2 says the $137,500 position has no GL entry at all. Its finding 7 says the $137,500 against $160,000 gap **is** explained, by `J316` dated 2017-12-27, "Lamberton Wire Overage", a credit of $22,970.55, leaving a residual of only $470.55. **Both cannot be true as stated.** The likely reconciliation is that `J315` and `J316` are journal entries rather than credits to the capital contribution account, so the cash moved but was never booked as a contribution. **That is a plausible reading and it is not verified, so it is labelled INFERRED and it is not the basis of the recommendation.**

**It also has an innocent explanation that has to be excluded before anyone calls it a defect.** The Bedrock I Group Class A position is the Lamberton contribution, and **a contribution of property rather than cash would correctly show no bank deposit.** Whether that is what happened is a question for the CPA, not for this page.

### What to do instead of signing

1. **Do not sign M3 on 2026-09-04.** The 09-04 date is self-imposed weekly Friday cadence. The only external anchor is Citrin fieldwork around 2026-10-01, so there are roughly four weeks of slack and nothing is gained by signing a memo with a wrong number in it.
2. **Settle the Forster item first, because it is small, clean and decisive.** One question to the CPA or to InvestNext: is the 2020-07-15 $4,798 on account 1033 a subscription or a mis-keyed distribution. The GL answer is already unambiguous; what is needed is the correction to the investor register.
3. **Then reissue M3 with the corrected figures**, whatever they prove to be. The memo's conclusion that no capital call was ever issued is **not** what is in doubt and is likely to survive intact. **What is in doubt is one supporting figure, and the fix is a corrected figure rather than a withdrawn memo.**
4. **Have the CPA rule on the $137,500 before the reissued memo repeats the "no unfunded commitment" sentence.** If the Lamberton interest was contributed as property, the sentence is fine and should say so. If it was not, the sentence needs qualifying.
5. **Do not sign `WP-36-M1` or `WP-36-M2`**, the originals, in any circumstance.

### What this does not change

**The conclusion of M3 still looks right.** Nothing in the re audit challenges the finding that no capital call was ever issued. The re audit **held unqualified**: the four transaction types and their counts, that nothing is classified as a call, drawdown or contribution notice, and the single-payment subscription mechanic. **The memo is wrong in a supporting figure, not in its answer.** That distinction matters, because withdrawing the memo would lose four days of correct work over one mis-keyed cell.

## Original recommendation, superseded above and kept unedited

**Sign M3 on 2026-09-04, once the arithmetic re proof confirms there is no Class A position-to-contribution exception.** That single check is the only thing between the current draft and a memo that is accurate as written. **If an exception exists, add one clause naming it rather than withdrawing the memo**, because the conclusion survives either way and a memo that names its own exception is stronger than one that is silent about it.

**Do not sign `WP-36-M1` or `WP-36-M2`**, the originals. WP-38 v3 opens in capitals stating both are contradicted by the fund's books and by filed tax returns. They were withdrawn unsigned on 2026-08-30 and are correctly retained in `Archive_Superseded` at under 3 KB each, against 54 to 57 KB for the three live drafts.

## Sources

- `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\12_Document_Archive\WP-36_Document Archive Needed Items + Timeline.xlsx`, sheet 1 items D-01 to D-03 and sheet 2 the 2026-09-04 milestone. VERIFIED, extracted and read in full.
- `...\12_Document_Archive\WP-38_Investor_Records_Integrity_Review_v3_20260830.pdf`, sections 1, 4 and 5. VERIFIED, extracted and read in full.
- `WP-36-M3_No Capital Call Activity_DRAFT.pdf`, pulled from Dropbox `ns:15029193027//2. Investor Records/2.3 Capital Call Notices/`, 54,128 bytes, opened and read in full. VERIFIED.
- [[80-Finance/fund-reporting/bmhcii-archive-audit-2026-09-03]] for the folder 1.8 naming failures.
- Austin, in session 2026-09-03, for the sign M3 and hold the other two decision. VERIFIED, his own instruction.
