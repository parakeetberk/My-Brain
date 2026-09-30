# WP-36 and WP-38 integrity re-audit

**What this is:** the three-agent re-audit of the two workpapers that drive the Bedrock Fund II wind-down document programme, run 2026-09-03 the evening before the memo they support was due for signature. It answers one question. **Can `WP-36-M3` be signed as drafted, and the answer is no.**

**Status:** current, 2026-09-08. **`WP-36-M3` was not signed on 2026-09-04 and is still open**, confirmed by Austin. The blocker below is what holds it. Nothing in the re-audit has been actioned yet.

## The finding that stops the signature

**`M3` asserts a dollar figure the Fund's own general ledger contradicts, and it asserts it twice.**

Maria Forster's $4,798, which InvestNext records as her second subscription dated 2020-07-15, is booked in the Fund's general ledger as an outbound ACH on 2020-07-22: credit to the Fund II bank account, debit to `36000 LP Distributions`. Her standing quarterly distribution in that period was $4,798.20, so **the disputed item is twenty cents off her regular payment, to the same payee, out of the same account, with the same accounting treatment.** No matching deposit exists anywhere in the GL.

`M3` states contributed capital aggregating a total across 66 investment transactions and says it reconciles "without variance." If the Forster item is a mis-key, both the total and the count are wrong. **A memo that asserts a reconciliation without variance, twice, over a figure the ledger disputes is the wrong document to sign.** Figures in `00-Meta/numbers-ledger.md`.

**The memo's conclusion is not what is in doubt.** Nothing in the re-audit challenges the finding that no capital call was ever issued. The four transaction types, their counts, the absence of any call or drawdown row, and the single-payment subscription mechanic all held unqualified. **`M3` is wrong in a supporting figure, not in its answer**, which is why the fix is a corrected figure rather than a withdrawn memo.

## The facts

- **The re-audit tested 49 figures. 37 held, 12 were refuted.** All twelve refutations touch numbers `WP-38` relies on for the signature gate.
- **`WP-38` names not one source file in six pages**, against its own header standard that "every assertion below is tied to a named source file." A regex sweep for any filename token returns zero matches. **Its citations are untestable rather than wrong**, which is a worse position, because a wrong citation can be corrected and an untestable one cannot be audited at all.
- **All seven of `WP-38`'s header sources are unreachable.** The InvestNext folder that should hold two of them exists and is empty. There is no K-1, no Form 1065, no PPM, no subscription booklet and no closing letter anywhere in the 3,851 files of the working folder. **Eight of the thirteen body-only sources were reachable and all eight checked out against what `WP-38` says about them.** The problem is not fabrication. It is that the sources carrying the two highest-severity findings are precisely the ones nobody can reach.
- **`WP-38` says `M3` is attached to it. Nothing is attached.** Zero embedded-file objects in the PDF. All three versions are ReportLab output generated inside a 23 minute window on 2026-08-30, so the text layer is authoritative and there is no OCR uncertainty.
- **Two distribution source files have their contents swapped.** `2019.xls` holds the 2020 report and `2020.xls` holds the 2019 report, agreeing on worksheet name, cell A3 and every payment date inside. **No data loss, and 2020 is the single year the Khodara-to-WCO finding turns on.** Anyone testing "the 2020 file" by filename reads 2019 data and misses that the quarterly rate more than doubles that year. Same defect class as the folder `1.8` naming failures, different folder, previously unflagged.
- **Unredacted taxpayer identification numbers sit in all nine distribution reports.** Column C is headed `Tax ID #` and is populated with individual Social Security numbers and entity EINs in the clear, in an unrestricted working folder. **This is the second location for the exposure the 2026-09-03 archive audit raised on the folder `1.8` ACH forms.** No value is transcribed in this Brain.
- **`pdftotext -layout` silently scrambles `WP-38`'s tables.** It shifts the amount column up one row and strands the last value on the total line, which produces three false errors in one finding alone. **Use `-table` or `-lineprinter`.** Read correctly, `WP-38`'s own table is right and the published version is the one that is displaced.
- **`WP-36` calls the same two memos both `WP-33-M1/M2` and `WP-36-M1/M2`**, in adjacent cells of the same row. Search both prefixes.
- **The near-miss risk is a naming one.** The memo to sign and the two memos that must never be signed differ by a `_v2` and a folder name. `WP-38` page 1 states in capitals that `WP-36-M1` and `WP-36-M2` are contradicted by the Fund's own books and by filed tax returns. **Do not sign either, in any circumstance.**
- **One pointer in the live issue register is stale.** Item `2.31`, the item that stops the final distribution if unanswered, still cites `WP-38 v2`, which now sits in the superseded archive. Substantively harmless, since the relevant section is unchanged between v2 and v3.

## What to do instead of signing

Ordered, and the order matters because the first item is small enough to settle in one email.

1. **Settle the Forster item.** One question to the CPA or to InvestNext: is the 2020-07-15 $4,798 on account 1033 a subscription or a mis-keyed distribution. **The GL answer is already unambiguous. What is needed is the correction to the investor register.**
2. **Get the CPA to rule on the $137,500** before a reissued memo repeats the "no unfunded commitment" sentence. If the Lamberton interest was contributed as property rather than cash, no bank deposit is the correct picture and the sentence is fine. If it was not, the sentence needs qualifying.
3. **Reissue `M3` with the corrected figures**, whatever they prove to be.
4. **Rename the two swapped distribution files**, then re-check anything drawn from either.
5. **Add a filename to every source citation in `WP-38`** before it goes to counsel, Citrin or Murad.
6. **Treat the taxpayer identification numbers as an exposure item**, not a formatting one.

**There is no external clock on any of this.** The 2026-09-04 date was self-imposed weekly Friday cadence. **The only external anchor is Citrin fieldwork around 2026-10-01**, so roughly three weeks of slack remain as of today.

## Decisions

- 2026-09-08. `WP-36-M3` was not signed on 2026-09-04 and stays open, blocked on the Forster item. (Source: Austin, in session)
- 2026-09-03. The recommendation reversed from sign-with-one-check to **do not sign as drafted**, on the re-audit returning a Class A exception the conditional was built to catch. (Source: [[80-Finance/fund-reporting/wp36-38-reaudit-2026-09-03/m3-signature-review]])
- 2026-09-03. Sign `M3` on 09-04, hold `WP-36-M1 v2` and `WP-36-M2 v2` until the re-audit lands. **Superseded the same day by the row above.** (Source: Austin, in session)

## Related

- [[80-Finance/fund-reporting/bmhcii-archive-audit-2026-09-03]]. The fourteen-agent audit that proved filenames do not predict contents in folder `1.8`, which is why this re-audit exists.

## Sources

- [[80-Finance/fund-reporting/wp36-38-reaudit-2026-09-03/source-integrity]]. Whether `WP-38`'s sources are the documents it says they are. Findings A through J.
- [[80-Finance/fund-reporting/wp36-38-reaudit-2026-09-03/arithmetic-reproof]]. Independent re-derivation of every material figure. 37 verified, 12 refuted.
- `80-Finance/fund-reporting/wp36-38-reaudit-2026-09-03/m3-signature-review.md`. The line-by-line read of the memo, original recommendation kept unedited beneath the reversal.
- `80-Finance/fund-reporting/wp36-38-reaudit-2026-09-03/status-and-sequencing.md`. Whether `WP-36`'s status picture is still true, and the true work order.
- Austin, in session 2026-09-03, for the original sign-and-hold instruction, and 2026-09-08 confirming `M3` is unsigned.
