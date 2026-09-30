# WP-38 / WP-36 source integrity re-audit, 2026-09-03

**What this is:** a re-audit of whether the sources WP-38 v3 cites are the documents it says they are. Arithmetic is owned by another agent. Written incrementally; sections are marked IN PROGRESS until closed.

**Why it exists:** the 2026-09-03 fourteen agent audit of Dropbox `/Austin Berk/BMHCII` proved that filenames in `1.8 Subscription Agreements` do not match file contents, that roughly two dozen files are wrong about the investor or the document type or both, and that some copies are truncated to the point of holding no text layer. Source at `C:\Users\AustinBerk\Documents\My Brain\80-Finance\fund-reporting\bmhcii-archive-audit-2026-09-03.md`. WP-38 cites folder 1.8.

**Label key:** VERIFIED = I opened the file and read the content. SINGLE-SOURCE = one document says it and nothing corroborates. INFERRED = reasoning, not observation. UNREACHABLE = the source lives somewhere I cannot read from here. ABSENT = I searched and it is not there.

## The answer, in one paragraph

**WP-38's sources are not what it says they are, but not in the way the brief anticipated.** WP-38 names no file anywhere in its six pages, while its own Standard line promises that every assertion is tied to a named source file. That makes its citation to folder 1.8 untestable rather than wrong, which is a worse position: a wrong citation can be corrected, an untestable one cannot be audited at all. Separately, and independently of 1.8, **the name-does-not-match-content defect is live in the local working folder and lands on the two years Finding 4 turns on**: `10_Source_Data\2019.xls` holds the 2020 distribution report and `2020.xls` holds the 2019 one. Where WP-38's sources can actually be reached, eight of eight check out against what WP-38 says about them, so this is not a fabrication problem. All seven of its header sources are unreachable from here, and the three memos due for signature on 2026-09-04 exist only as prose assertions written by one session on one day.

## Priority order

| # | Finding | Label | Consequence before 2026-09-04 |
| --- | --- | --- | --- |
| 1 | The three memos due for signature cannot be confirmed to exist or be read from this project. WP-38 says WP-36-M3 is attached to it; nothing is attached | UNREACHABLE plus VERIFIED on the attachment | **Open the three files in Dropbox before the gate.** Do not sign on the tracker's word |
| 2 | WP-38 names no file in six pages, against its own stated standard. The 1.8 citation is therefore untestable | VERIFIED | Every source citation in WP-38 needs a filename added before it goes to counsel, Citrin or Murad |
| 3 | `2019.xls` and `2020.xls` have their contents swapped, in the folder holding the distribution files Finding 4 cites | VERIFIED | Rename both. Then re-check any conclusion drawn from either |
| 4 | The 06/30/2026 LP statement set, which WP-38 certifies as "Correct", disagrees with the distribution files by $32,005.48 and seven distributions on account 1034 | VERIFIED | WP-38 tells the reader to correct the register toward the statements. That propagates the gap |
| 5 | `pdftotext -layout` scrambles WP-38's tables. A re-audit run that way will report false errors | VERIFIED | Tell the arithmetic agent to use `-table` |
| 6 | Unreconciled off-by-one in the partner count between v1's 2022 math and v3's 2024 table. One partner must have left the fund and nobody has written it down | INFERRED | Needs the 2021, 2022 and 2024 K-1 sets |
| 7 | Register 5.05 is described as a Class B item in WP-38 Finding 3 and a Class A item in Finding 5. Finding 3 is one of the three tie-outs holding up WP-36-M3 | VERIFIED | Fix the wording in the memo before signature |
| 8 | Three claims changed between v1 and v3 with no revision note | VERIFIED | Add them to the revision history if v3 is circulated |
| 9 | Unredacted taxpayer identification numbers in all nine distribution reports in the working folder | VERIFIED | Same exposure class as the 1.8 ACH forms, second location |
| 10 | WP-36 calls the same memos both WP-33-M1/M2 and WP-36-M1/M2 | VERIFIED | Search Dropbox for both prefixes |

## Files under audit

| File | Path | Size | Extract method |
| --- | --- | --- | --- |
| WP-38 v3 | `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\12_Document_Archive\WP-38_Investor_Records_Integrity_Review_v3_20260830.pdf` | 99,219 bytes, 6 pages | `pdftotext -layout`, 310 lines, clean text layer |
| WP-36 | `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\12_Document_Archive\WP-36_Document Archive Needed Items + Timeline.xlsx` | 13,758 bytes, 3 sheets | unzip + parse `xl/worksheets/sheet1-3.xml`, inline strings |
| WP-38 v1 SUPERSEDED | `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\_archive\WP-38_superseded\WP-38_v1_SUPERSEDED_20260830.pdf` | 93,482 bytes | `pdftotext -layout`, 227 lines |
| WP-38 v2 SUPERSEDED | `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\_archive\WP-38_superseded\WP-38_v2_SUPERSEDED_20260830.pdf` | 97,692 bytes | `pdftotext -layout`, 279 lines |

**Path correction, VERIFIED.** The brief located the superseded versions at `12_Document_Archive\_archive\WP-38_superseded\`. They are not there. They are at project root: `Close It Down\_archive\WP-38_superseded\`. `find` over the whole project returns exactly those two PDFs and no others matching WP-38.

## FINDING A. The name-does-not-match-content defect is present in the local working folder too, and it lands on 2019 and 2020. VERIFIED.

`10_Source_Data\2019.xls` and `10_Source_Data\2020.xls` have their contents swapped. Three independent fields inside each file agree with each other and disagree with the filename.

| File on disk | Worksheet name | Cell A3 | Payment-date years actually present in column F | Rows |
| --- | --- | --- | --- | --- |
| `2018.xls` | 2018 Distribution Report | Year: 2018 | 2018 | 208 |
| **`2019.xls`** | **2020 Distribution Report** | **Year: 2020** | **2020 only** | 357 |
| **`2020.xls`** | **2019 Distribution Report** | **Year: 2019** | **2019 only** | 346 |
| `2021.xls` | 2021 Distribution Report | Year: 2021 | 2021 | 311 |
| `2022.xls` | 2022 Distribution Report | Year: 2022 | 2022 | 588 |
| `2023.xls` | 2023 Distribution Report | Year: 2023 | 2023 | 403 |
| `2024.xls` | 2024 Distribution Report | Year: 2024 | 2024 | 336 |
| `2025.xls` | 2025 Distribution Report | Year: 2025 | 2025 | 402 |
| `2026.xls` | 2026 Distribution Report | Year: 2026 | 2026 | 332 |

Full paths: `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\10_Source_Data\<year>.xls`. All nine are genuine OLE2/BIFF8 workbooks (`d0cf 11e0 a1b1 1ae1` signature), read with `xlrd` 2.0.2. None is empty and none is truncated. Exactly two are misnamed, and the content years 2018 through 2026 are each present exactly once, so **this is a naming swap with no data loss**.

**Why it matters more than a two-file typo.** These are the "Distribution files 2018-2026 (2.2)" that WP-38 Finding 4 cites, and 2020 is the single year Finding 4 turns on: the year the Khodara interest moved to WCO Capital. Anyone testing "the 2020 distribution file" by filename reads 2019 data. Sample of the divergence, VERIFIED by opening both:

- `2020.xls`, account 1034 Maria Yvonne Khodara: three preferred distributions of $3,000.00 on 07/15/2019, 10/15/2019 and 12/31/2019.
- `2019.xls`, account 1034 Maria Yvonne Khodara: four preferred distributions of $7,000.00 on 07/15/2020, 10/01/2020, 12/25/2020 and 12/31/2020.

A reviewer who opened the file named `2020.xls` would see the $3,000 quarterly run and no step-up, and would miss the fact that the quarterly rate more than doubles in 2020. Same defect class as folder 1.8, different folder, and nobody had flagged it.

**Also present in these files: unredacted taxpayer identification numbers.** Column C of every one of the nine reports is headed `Tax ID #` and is populated with individual Social Security numbers and entity EINs in the clear, in a working folder with no access restriction. No value is transcribed anywhere in this page. This is the same exposure class the 2026-09-03 audit raised for the ACH forms in folder 1.8, in a second location, and it is a live item rather than a historical one.

## FINDING B. WP-38 names not one file, anywhere, in six pages. VERIFIED.

WP-38 v3's own Standard line reads, verbatim from the header block:

> Every assertion below is tied to a named source file. No conclusion rests on a single source.

A regex sweep of the full extracted text for any token ending in `.pdf`, `.xlsx`, `.xls`, `.docx`, `.csv` or `.txt` returns **zero matches**. WP-38 cites document types and archive section numbers. It never cites a file.

That is the answer to the central question the brief poses. The 2026-09-03 audit proved that in folder `1.8 Subscription Agreements`, 179 files, the filename does not predict the contents, and that **every file opened specifically to test name against content failed**. WP-38's citation to that folder is `Subscription Booklet exemplar (1.8)`. There is no way to establish which of the 179 files was read, so:

- **The 1.8 citation cannot be re-performed at all.** Not "it points at the wrong document" and not "it points at the right one". It is untestable as written. That is a worse position than a wrong citation, because a wrong citation can be corrected and an untestable one cannot be audited.
- The same applies to `PPM (1.2)`, `2019 Closing Letter (2.3)`, `K-1 sets 2018-2025 and filed 2024 Form 1065 (4.5)`, `Investor position schedule (2.1)` and `InvestNext Activity List Report (2.2)`.

The `Sources tested` header block is **byte-identical across v1, v2 and v3** (md5 of the six header lines is the same in all three files). WP-38 restated two of its seven findings on 2026-08-30 without changing its source list once.

The header also understates v3's actual source base. Sources cited in the v3 body but absent from the header: Bedrock I Group's own 2024 Form 1065; the Fund's Schedule M-2; Item M and Item N of the A2Z Schedule K-1; the Distribution files 2018-2026; the 06/30/2026 LP statement set; register items 5.05, 4.09, 4.38 and 2.19; WP-12a; Bedrock I Group's balance sheet; fund ledger account 14211; Issue Register v56.

## FINDING C. WP-38 v3 says WP-36-M3 is attached to it. Nothing is attached. VERIFIED.

WP-38 v3, section 1, action column for folder 2.3: `SIGN WP-36-M3 (attached).`

The PDF contains zero `/EmbeddedFile` objects. Metadata read directly from the file trailer:

| | v1 | v2 | v3 |
| --- | --- | --- | --- |
| Producer | ReportLab PDF Library | ReportLab PDF Library | ReportLab PDF Library |
| Title | WP-38 | WP-38 v2 | WP-38 v3 |
| CreationDate | D:20260830195137+00'00' | D:20260830201055+00'00' | D:20260830201453+00'00' |
| Pages | 5 | 6 | 6 |
| EmbeddedFile objects | 0 | 0 | 0 |

All three are machine-generated by ReportLab, so the text layer is authoritative and there is no scan or OCR uncertainty anywhere in this audit of them. **v1 to v2 took 19 minutes 18 seconds. v2 to v3 took 3 minutes 58 seconds.** The whole three-version chain closed inside 23 minutes 16 seconds on 2026-08-30.

## FINDING D. The three memos due for signature on 2026-09-04 are not in the local project, and their existence rests on a single unverifiable assertion. UNREACHABLE, not ABSENT.

Searched `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\` in full: 3,851 files, 438 directories.

- Filename search for `*M1*`, `*M2*`, `*M3*`, `*no*activity*`, `*36-M*`, `*33-M*` returns five hits, none of them a memo: three unrelated workpapers (`WP-1_Item110_Murad_Tag_Review_v2.xlsx`, `WP-2g_Item210_Parakeet_Transfer_Support_Memo.docx`, `_archive/WP-1_Item110_Murad_Tag_Review.xlsx`) and two PNG screenshots in `_to_delete\_qc_tmp_20260830\` (`m1-1.png`, `m3-1.png`).
- `12_Document_Archive\` contains exactly two files: WP-36 and WP-38 v3. No memos.
- Content search inside every `.docx` and `.xlsx` in the project for the strings `WP-36-M1`, `WP-36-M2`, `WP-36-M3` and `no-activity memo` returns **references to the memos in four workpapers and the memos themselves in none**: `00_Governance\WP-37_Workstream_Tracker_BMHCII_20260830.xlsx`, `08_Communications\WP-00b_Weekly_Internal_Digest_BMHCII_20260831.docx`, `09_Issue_Register\WP-Issue_Register_BMHCII_v57.xlsx` and `..._v58.xlsx`.

**Report absence correctly:** WP-36 sheet 3 and the register both place these memos in the Dropbox tree (`BMHCII\2. Investor Records\2.4\`, `\2.5\`, `\2.3`). Dropbox is not reachable from this session, so **this is UNREACHABLE, not ABSENT.** I cannot say the memos do not exist. I can say the following, which is worse in one specific way.

**Every local record of WP-36-M3, WP-36-M1 v2 and WP-36-M2 v2 traces back to the same author on the same day, and none of them is a record of the memo being created.** WP-36 sheet 3 is titled `Cleanup Pass Move Log -- executed 2026-08-30 by Claude (session), authorized by Austin Berk`. It has 14 numbered actions. Row 11 records `CREATE ... WP-33-M1/M2 DRAFT memos committed to 2.4 and 2.5`. Rows 12 and 13 then record MOVING `WP-36-M1_No Activity Memo_2.4 Transfers_DRAFT.pdf` and `WP-36-M2_No Activity Memo_2.5 Additional Subscriptions_DRAFT.pdf` out to `Archive_Superseded`. **There is no CREATE row for WP-36-M3, none for WP-36-M1 v2, and none for WP-36-M2 v2.** The move log that documents the creation and withdrawal of the two memos that must NOT be signed does not document the creation of the three that must be.

The only assertions that they exist are prose: WP-36 sheet 1 cell H7 (`WP-36-M3 drafted and filed in 2.3 for signature`), register 2.32 (`Replaced by WP-36-M1 v2 (transfer register + document request), filed in 2.4 for signature`), register 2.33 (`Replaced by WP-36-M2 v2 (schedule + document request), filed in 2.5`), and WP-38 v3 section 1 (`SIGN WP-36-M3 (attached)`, which Finding C shows is false as to attachment). SINGLE-SOURCE, all four written the same day by the same session.

**Consequence.** The 2026-09-04 gate is `WP-36-M3 signed (2.3, no capital calls) + WP-36-M1 v2 and M2 v2 signed` (WP-36 sheet 2, row 6, cell C6). Nobody in this project can currently confirm that the three documents Austin is being asked to sign tomorrow exist, or read what they say. **Verify by opening the three files in Dropbox before the gate, not by trusting the tracker.** The specific text to check is whether WP-36-M3 says what WP-38 section 4 says it says: that the capital-call mechanic existed in the PPM, that the General Partner never exercised it, and that the books show no unfunded commitment, rather than the weaker claim that folder 2.3 is empty.

**One piece of indirect evidence cuts the other way, see the cross-check section below.** The 2026-09-03 audit's own Dropbox listing reports that folder 2.4 "contains nothing but a draft and zero final documents". Folder 2.4 is where WP-36-M1 v2 is supposed to be. That is SINGLE-SOURCE and indirect, since the audit did not name or open the file, but it is the best available sign that at least one of the three memos is really there.

**Naming inconsistency inside WP-36, VERIFIED.** WP-36 calls the same two memos both `WP-33-M1`/`WP-33-M2` and `WP-36-M1`/`WP-36-M2`. Sheet 1 cell C5 reads `Signed no-activity memo -- LP transfers/assignments (WP-33-M1 draft delivered 8/30)` while cell H5 of the same row reads `WP-36-M1 no-activity memo WITHDRAWN 8/30`. Sheet 3 row 11 says `WP-33-M1/M2 DRAFT memos` and sheet 3 rows 12 and 13 give the actual filenames as `WP-36-M1_...` and `WP-36-M2_...`. Sheet 3 row 10 also refers to `_FOLDER STATUS.txt` notes `pointing to WP-33 open items`. Anyone searching Dropbox for these memos must search both prefixes.

## FINDING E. `pdftotext -layout` silently scrambles WP-38's tables. Anyone re-auditing its arithmetic that way will read wrong numbers. VERIFIED.

The brief instructed `pdftotext -layout`. On this file that mode misassigns table cells across rows. The installed binary is xpdf 4.00, not poppler, and `-table` and `-lineprinter` modes both give the correct alignment. Worked example, WP-38 v3 Finding 2:

| Acct | Partner | Second amount, `-layout` | Second amount, `-table` and `-lineprinter` |
| --- | --- | --- | --- |
| 1034 | Maria Yvonne Khodara | (blank) | **200,000.00** |
| 1045 | Slab Holdings, LLC | 200,000.00 | **75,000.00** |
| 1049 | Stuart Taub | 75,000.00 | **125,000.00** |
| | Total | 125,000.00 then 498,548.00 | 498,548.00 |

`-layout` shifts the amount column up one row from Khodara onward and strands the last value on the Total line. **The `-table` reading is the correct one, and WP-38 v3's Finding 2 table is right.** Confirmed three ways: `pdftotext -lineprinter` character-grid output places `2 0 0 , 0 0 0 . 0 0` on the Khodara row; register 2.33 in the live v58 register reads `1034 Khodara (+200,000 1/13/20), 1045 Slab Holdings (+75,000 12/30/19), 1049 Taub (+125,000 12/31/19)`; and the WCO limited partner statement's own distribution schedule shows the remaining capital balance stepping from `$150,000.00` to `$350,000.00` at the 01/31/2020 row, which is the $200,000 second subscription landing (`02_Investor_Capital\LP_Statements_06302026\Bedrock_FundII_Statement_WCO.pdf`, page 2, rows 4 and 5).

The header block and the Finding 5 percentage table are scrambled the same way under `-layout`. **Tell the arithmetic agent to re-extract with `-table` before checking a single figure.** A tie-out run off the `-layout` text will report three false errors in Finding 2 alone.

## FINDING F. WP-38 v3 calls the 06/30/2026 LP statement set "Correct". Opening it shows it disagrees with the distribution files cited in the row directly above, by $32,005.48 and seven distributions. VERIFIED.

WP-38 v3 Finding 4, the "What is actually wrong" table, has two adjacent rows:

> `Distribution files 2018-2026 (2.2)` -- Every distribution on this interest is paid under Maria Yvonne Khodara, including $312,026.55 return of capital on 03/16/2026 and $53,029.70 preferred on 06/30/2026. WCO Capital appears in no distribution file in any year.

> `LP statement set 06/30/2026` -- Already names WCO as Partner of Record on the $350,000 position, initial funding 04/20/2018, capital returned in full. ... **Correct** -- and therefore inconsistent with the register it was built beside.

**What is confirmed, VERIFIED.** `02_Investor_Capital\LP_Statements_06302026\` holds exactly 62 PDFs, matching WP-38's "the 62 limited partner statements issued 06/30/2026". `Bedrock_FundII_Statement_WCO.pdf` opened: `Partner of Record: WCO`, `Total Capital Commitment $350,000`, `Initial Funding Date 04/20/2018`, `Position Status: Capital Returned in Full`. There is a WCO statement and no Khodara statement in the set. Every field WP-38 asserts about that statement is accurate.

**What WP-38 did not test.** Account 1034 in the nine distribution reports, against the WCO statement's own page 2 distribution schedule:

| Year | Distribution reports, acct 1034 | WCO statement schedule | Difference |
| --- | --- | --- | --- |
| 2018 | 5,333.33 | 2,333.33 | 3,000.00 |
| 2019 | 9,000.00 | 9,000.00 | 0.00 |
| 2020 | 28,000.00 | 17,000.00 | 11,000.00 |
| 2021 | 21,000.00 | 28,000.00 | (7,000.00) |
| 2022 | 70,797.62 | 63,797.62 | 7,000.00 |
| 2023 | 24,245.86 | 12,480.91 | 11,764.95 |
| 2024 | 18,721.59 | 18,721.59 | 0.00 |
| 2025 | 24,962.13 | 18,721.60 | 6,240.53 |
| 2026 | 371,296.78 | 371,296.78 | 0.00 |
| **Total** | **573,357.31** | **541,351.83** | **32,005.48** |

**33 distribution rows in the reports against 26 on the statement.** The statement's dates are all month-end normalized (10/31/2018, 02/28/2019, 01/31/2020) while the reports carry actual payment dates (10/16/2018, 07/15/2019), so the statement is not built from the distribution reports; it is built from a different dataset. Year-boundary timing explains the 2020 and 2021 rows offsetting each other, but it does not explain the $32,005.48 total, which is timing-independent, nor the seven missing rows.

Extraction method for both sides: `pdftotext -table -f 2` on the statement, filtered to numbered schedule rows; `xlrd` walk of account 1034 with forward-fill on the merged account and name columns, summing column G by the column F payment-date year.

**The finding is not that WP-38 is wrong. It is that WP-38 certified a document as "Correct" on the strength of four header fields and did not open page 2.** That endorsement is now load-bearing: WP-38 tells the reader to correct the register to agree with the statement set. If the statement set's own distribution history is off by $32,005.48 against the distribution reports, correcting the register toward the statements propagates the gap. Reconciliation is the arithmetic agent's; the source-integrity point is that the endorsement was not earned.


## Task 1 and 2. Complete source inventory, with existence, content and completeness tested per source

Six sources are named in the WP-38 header. Thirteen more are cited only in the body. Twenty in total.

Local root searched: `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\`, 3,851 files, 438 directories, walked in full. "Dropbox only" below means I found no local file matching the description and the workpapers place the document in the Dropbox tree, which this session cannot reach.

### Header sources

| # | Source as WP-38 cites it | Section refs | Exists locally | Content opened | Label |
| --- | --- | --- | --- | --- | --- |
| 1 | InvestNext Activity List Report 01/01/2017-12/31/2026 (2.2) | header; s2; s4 test 3; s5 | **No.** `10_Source_Data\InvestNext\` **is an empty directory.** No file anywhere in the project matches an activity list report | Not opened. Nothing to open | UNREACHABLE |
| 2 | Investor position schedule (2.1) | header; s4 test 2; s5 | No standalone file found | Not opened | UNREACHABLE |
| 3 | K-1 sets 2018-2025 (4.5) | header; s2; s5; s8 | No. No K-1 PDF or workbook anywhere in the project | Not opened | UNREACHABLE |
| 4 | Filed 2024 Form 1065, Client Copy, 3,229 pages (4.5) | header; s6 | No | Not opened | UNREACHABLE |
| 5 | Subscription Booklet exemplar, Class A and Class B, Item 6 (1.8) | header; s4 test 1 | No | Not opened | **UNREACHABLE and, per Finding B, untestable even with Dropbox access** |
| 6 | PPM (1.2) | header; s4 caveat | No | Not opened | UNREACHABLE |
| 7 | 2019 Closing Letter (2.3, being refiled to 2.5) | header; s3; s4 housekeeping | No | Not opened | UNREACHABLE |

### Body-only sources

| # | Source | Section refs | Result |
| --- | --- | --- | --- |
| 8 | Distribution files 2018-2026 (2.2) | s5 | **FOUND and VERIFIED.** `10_Source_Data\2018.xls` through `2026.xls`. Opened all nine. Two are misnamed, see Finding A. Cited figures confirmed exactly: account 1034 Maria Yvonne Khodara, $312,026.55 Return of Capital 03/16/2026 and $53,029.70 Preferred 06/30/2026, both in `2026.xls`. WCO Capital appears in none of the nine years; Khodara appears in all nine. WP-38's assertion here is right |
| 9 | LP statement set 06/30/2026 | s5 twice | **FOUND and VERIFIED, with a disagreement WP-38 missed.** `02_Investor_Capital\LP_Statements_06302026\`, exactly 62 PDFs. `Bedrock_FundII_Statement_WCO.pdf` opened. See Finding F |
| 10 | Archive folder 2.4, asserted empty | s2; s5 | Dropbox only. Cannot confirm or refute emptiness. The 2026-09-03 audit independently reports `2.4 Transfer-Assignment Documentation` as holding nothing but a draft and zero final documents, which agrees in substance but is second-hand rather than an opened folder |
| 11 | Bedrock I Group's own 2024 Form 1065, Lamberton passthrough 100% disposed | s6 | Dropbox only. Not in the project |
| 12 | Fund Schedule M-2, no capital contributed in 2024 | s6 revision note | Dropbox only. **This is the load-bearing evidence for the v2-to-v3 correction and it cannot be re-performed here** |
| 13 | A2Z Schedule K-1, Item M (No to contributed property) and Item N (704(c) allocation) | s6 revision note | Dropbox only. Same as above |
| 14 | Register 5.05, Bedrock I Group $137,500 Lamberton position, J315 11/02/2017 $160,000 against a payable to A2ZI | s6 | **FOUND and VERIFIED twice.** `09_Issue_Register\WP-Issue_Register_BMHCII_v58.xlsx`, sheet `Issue Register`, row 90, ID 5.05, reads exactly that. Independently confirmed in the ledger itself: `10_Source_Data\GL_Exports\R-46_GL_FUNDIILP_fulllife_pull20260902.csv` carries 27 rows on account `14211 Lamberton Lake`, including a J315 row dated 11/2/2017 for 160000.00 and a J316 row dated 12/27/2017 crediting 22970.55, described as Lamberton Wire Overage |
| 15 | Fund ledger account 14211 | s6 | **FOUND and VERIFIED.** Same GL export, account exists and is named `14211 Lamberton Lake` |
| 16 | WP-12a, draft confirmatory assignment, reciting the interest held since on or about November 2, 2017 | s6 | **FOUND and VERIFIED.** Both `07_Legal_Dissolution\WP-12a_Confirmatory_Assignment_Lamberton_DRAFT_20260826.docx` and `..._DRAFT_v2_Austin_20260827.docx` contain at recital C the words WP-38 quotes. Quotation is accurate and the characterisation as a draft is accurate. Both are unexecuted drafts |
| 17 | Register 4.09 and 4.38, A2Z counterparty | s6 | **FOUND and VERIFIED.** v58 register: 4.09 reads `21101 Payable to A2ZCP ends $1,440,631.32 DEBIT`, OPEN; 4.38 reads `A2ZCP net position: fund is owed 1,364,979.16`, IN PROGRESS. WP-38 v1 quoted the $1,440,631.32 figure and it matches to the cent |
| 18 | Bedrock I Group's balance sheet, $46,535 receivable from A2Z and $155,311 of payables to the A2Z family | s6 | **NOT CORROBORATED, and not refuted.** The source WP-38 means is the 2024 return balance sheet, which is Dropbox only. The nearest local source is `10_Source_Data\GL_Exports\R-19_TB_BEDROCKGRP_asof_08312026.xlsx`, a trial balance for BEDROCK I GROUP as of 08/31/2026, which carries `12101 Receivable from A2Z Community Partners 59,284.95` and A2Z-family payables of `21101 Payable to A2ZCP 8,139.00` plus `21102 Payable to A2ZI 40,000.00`, totalling 48,139.00. Different figures, different date, different system, so this neither confirms nor contradicts. Recorded as untested rather than as agreement |
| 19 | Register 2.19, final 2025/2026 K-1 zero-out | s5 | **FOUND and VERIFIED.** v58 register row 43: `Final 2025/2026 K-1 zero-out`, status WAITING, owner CPA. WP-38's characterisation is accurate |
| 20 | Issue Register v56, carrying the five items with columns L and M populated per the WP-37 sync rule | s9 | **FOUND and VERIFIED as stated, but the pointer is now stale.** `_archive\register_superseded\WP-Issue_Register_BMHCII_v56_SUPERSEDED_missing_6.16.xlsx`, rows 131 to 135, holds IDs 2.31 through 2.35 with columns L and M populated in all five. WP-38's claim is literally true. But v56 has since been superseded twice, by v57 at 16:20 and v58 at 16:37, both in `09_Issue_Register\`, and its own filename records that it was missing item 6.16, which v57 adds at row 131. WP-38 v3 was written at 16:14, so this is not an error by WP-38. It is a pointer that went stale 23 minutes after publication and before the 9/4 gate |

### Aggregate: all seven header sources are unreachable from here. Zero were opened.

**Nothing in the WP-38 header block can be verified from this session.** The InvestNext folder that should hold sources 1 and 2 exists and is empty. There is no K-1, no Form 1065, no PPM, no subscription booklet and no closing letter anywhere in 3,851 files.

Of the thirteen body-only sources, **eight are locally present and all eight checked out against what WP-38 says about them**, one is not corroborated either way, and four are Dropbox only.

That matters for how to read this re-audit. **Where WP-38's sources can be reached, WP-38 reports them accurately.** Its problem is not fabrication. Its problem is that the sources carrying its two highest-severity findings are precisely the ones nobody can reach, and that it cites every one of them in a form that names no file.

### A stale pointer inside the live register, VERIFIED

Register item 2.31, the item WP-38 says stops the final distribution if it is not answered, carries `Evidence: WP-38 v2; ...` in v56, v57 and v58 alike. It was never updated to v3. WP-38 v2 now sits in `_archive\WP-38_superseded\` under a filename containing SUPERSEDED. Substantively this is harmless: diffing section 5 of v2 against section 5 of v3 line by line, **the only difference in the entire Finding 4 section is the heading of the section that follows it.** Finding 4 is identical in v2 and v3. But the live register's evidence trail for its own gating item points at an archived, superseded file, while item 2.34 three rows below correctly points at v3.

## Task 4. Testing WP-38's two self-corrections, and looking for the third error

### The two disclosed corrections are genuine and complete. VERIFIED.

**Correction 1, Finding 4, v1 to v2.** v1's heading was `Finding 4 -- A 2.78% limited partner has received no K-1 since 2021 (NEW, HIGH)`, subtitled `MARIA YVONNE KHODARA -- ACTIVE $350,000 POSITION, DISTRIBUTED TO THROUGH MARCH 2026, OMITTED FROM FOUR YEARS OF PARTNERSHIP RETURNS.` Its conclusion: `Four tax years of income, loss and distribution allocations for a 2.78% partner have been reported to the IRS without her ... This is not an archive gap -- it is a live reporting exposure.` Its remedy: `the 2021 Final K-1 marking was in error and 2022-2024 returns require amendment`.

v3 reverses the direction of the error entirely: `THE PARTNERSHIP RETURNS ARE RIGHT. THE INVESTOR REGISTER IS WRONG`.

This is a real correction, not a re-wording, and **nothing of v1's version survives the text of v3.** Grep of the v3 extraction for each of v1's load-bearing phrases returns zero hits in every case: `omitted from` (v1: 2 hits), `require amendment` (1), `Citrin handoff` (3), `reported to the IRS` (1), `no K-1 since` (1), `3,229 pages` (1), `Number of Schedules K-1` (1). The whole four-step v1 recommended sequence is replaced by a different four-step sequence.

**Correction 2, Finding 5, v2 to v3.** v2 asserted `The K-1 reports net unrecognized Section 704(c) gain of $372,729 beginning / $574,362 ending, which is the signature of contributed property carrying built-in gain, not a cash subscription`, and asked the file for `the property description, the valuation supporting the $574,362 built-in gain`. v3 retracts it: `Item M of that K-1 answers No to contributed property, and the partnership's own Schedule M-2 shows no capital contributed in 2024 at all, cash or property. Item N reports the partner's share of fund-level Section 704(c) gain, which is an allocation, not evidence of a contribution.`

Also complete at the text level. Grep of v3 for v2's load-bearing figures and phrases returns zero in every case: `574,362` (v2: 3 hits), `372,729` (1), `14,909` (1), `built-in gain` (3), `property description` (1), `valuation` (2). The document request is rebuilt around a reallocation rather than a contribution.

**But the evidence for correction 2 is entirely unreachable.** Schedule M-2, Item M and Item N of the A2Z Schedule K-1 all live in the filed 2024 Form 1065, in Dropbox folder 4.5. I cannot open any of them. **The correction that makes v3 the signing version rests on three source documents that no one in this session can see, cited without a filename.** That is not a reason to doubt it. It is a reason not to describe v3 as verified.

### Three claims from v1 that v3 changed without disclosing. VERIFIED that the change is undisclosed.

v3 carries exactly two revision notes. Both are honest about what they cover. Neither covers the following.

**1. v1's Finding 5 was a different finding, and v3 does not say so.** v1 section 6 was headed `Finding 6 -- Two K-1 recipients are not on the limited partner register (NEW)` (numbered as Finding 5 in the body) and covered **WCO Capital and A2Z Community Partners together**, concluding `Both need a source document establishing when and on what terms the interest was admitted.` v3's revision note for Finding 5 mentions only v2. A reader of v3 alone cannot tell that v1's Finding 5 existed or what it claimed. Substantively it is superseded: WCO is now explained by Finding 4 and A2Z by Finding 5. But the disclosure is incomplete.

**2. v1 and v3 disagree about whether WCO Capital has a 2024 K-1.** v1: `WCO Capital -- Partner 62 in 2020, 2021, 2022 and 2023; in the 2025 draft letter set.` That enumeration skips 2024. v3 Finding 4: `Partner of record every year through the 2025 draft set.` That includes 2024. **Both cannot be right, and v3 does not record a change.** Unresolvable from here: the K-1 sets are in Dropbox 4.5.

**3. v1 and v2/v3 disagree about whether A2Z appears on the filed 2024 return.** v1: `A2Z Community Partners, LLC -- In the 2025 draft letter set only; absent 2020-2023.` v3 Finding 5 is built entirely on A2Z holding its own Schedule K-1 in the filed 2024 return at 1.7332920% of capital. v1's framing, that A2Z surfaces only in the 2025 draft, is refuted by the 2024 return, and v1 said it after reporting that it had read that return (`Filed return -- 2024 Form 1065 Client Copy, 3,229 pages`). Again not disclosed as a correction.

### The candidate third error: an unreconciled off-by-one in the partner count, carried from v1 into v3. INFERRED, and it needs the K-1 sets to close.

Two statements in the version chain, taken together, do not add up.

- **v1 Finding 4, partner-count math row:** `2021 = 62 partners. 2022 = 62 + 7 transferees - 1 (partner slot 7 retired) = 68. The removal was carried through deliberately, not lost in a filing.` So the 2022 return has 68 partners, and per v1 A2Z is not one of them.
- **v3 Finding 5, 2024 return table:** rows are `BEDROCK I GROUP, LLC`, `A2Z COMMUNITY PARTNERS, LLC` and `All 66 other partners`, with the Total row reading `100.0000000%` and `Ties exactly across all 68 partners`. So the 2024 return has 68 partners and A2Z is one of them. Register item 2.34 in the live v58 register states this came from a direct read: `Parsed all 68 partner K-1s in the filed 2024 1065`.

If 2022 had 68 partners without A2Z, and 2024 has 68 partners with A2Z, **exactly one partner must have left the fund between the 2022 and 2024 returns.** No version of WP-38 identifies such a departure, and no version flags the tension. The alternatives are that v1's 2022 arithmetic is wrong, or that A2Z was already a partner in 2022 and v1's `absent 2020-2023` row is wrong, or that a partner did leave and nobody has written it down. All three are material to the final K-1 zero-out at register 2.19.

**Labelled INFERRED because it is arithmetic over two of WP-38's own assertions, not an opened document.** It cannot be closed without the 2021, 2022 and 2024 K-1 sets, which are unreachable from here. It is the strongest candidate for the third error, and it is the kind of thing a document that revised twice in twenty-three minutes would be expected to have.

### Two smaller consistency defects found in v3, both VERIFIED

**Register 5.05 is misattributed.** WP-38 v3 Finding 3, test 2: `In the investor position schedule, Position Value equals Contribution Amount for all 68 Class A positions, totalling $12,589,708. The only exception is Bedrock I Group's 100 Class B units, carried at $100 position value with $0 contribution -- a separate item already tracked as register 5.05.`

Register 5.05, read directly from `09_Issue_Register\WP-Issue_Register_BMHCII_v58.xlsx` row 90, is not about Class B units. Its Issue field reads `Bedrock I Group $137,500 LP position has no contribution entry`, and its Found field reads `The position appears in the investor schedule and on the K-1 but nowhere in the general ledger -- all 63 entries in 35000 LP Contributions are bank deposits and no $137,500 exists in any account.` WP-38 v3 Finding 5 uses 5.05 correctly two sections later, calling it `Bedrock I Group's $137,500 Class A position`. So **the same workpaper describes register 5.05 as a Class B item in Finding 3 and a Class A item in Finding 5.** The Finding 5 reading is the one that matches the register.

This is not cosmetic. Test 2 is one of the three tie-outs holding up WP-36-M3, the memo Austin is being asked to sign on 2026-09-04. Its wording says the only Class A exception to Position Value equalling Contribution Amount is a Class B holding, while the register says a $137,500 Class A position has no contribution entry at all. Those may both be true of different books, the position schedule and the general ledger respectively, and WP-38 does not say which. **For the arithmetic agent:** test 2 counts 68 Class A positions totalling $12,589,708 and test 3 counts 66 Investment transactions totalling the same $12,589,708 and says they tie to the dollar. Reconcile that against register 5.05's claim that $137,500 of Class A position has no contribution entry in any account.

**A verified figure was dropped between versions.** v1 and v2 both cited register 4.09 as `$1,440,631.32 intercompany balance`. I confirmed that figure to the cent in the live v58 register. v3 drops it and cites `register 4.09 and 4.38` bare. Similarly, v2's A2Z `Ending capital account $14,909` is dropped from v3 but is still carried in register item 2.34 in v58, so on this point **the register is more complete than the workpaper it cites.**

### A near-miss for the arithmetic agent

v1 Finding 4 reports Khodara's `Cash activity -- Activity List Report (2.2) -- 34 transactions`. My independent count of account 1034 rows carrying a real payment date across all nine distribution reports is **33**. Different sources, activity report versus distribution reports, so this is not a contradiction. It is a one-row gap worth closing, and it points the same way as Finding F.

## Cross-checking WP-38 against WP-36 and against the 2026-09-03 Dropbox audit

### The 2026-09-03 audit is not an independent check on WP-38's three main findings. Read the labels.

It is tempting to treat the fourteen-agent audit as corroboration. On three points it is not, and it says so itself.

The audit's section `Genuinely absent, on the GP's own work papers rather than inference` lists the seven CS Partners IV transfer instruments, the five additional subscription agreements totalling $498,548, and the 2020 Khodara-to-WCO assignment. All three are WP-38 findings, down to the exact $498,548. **The audit's own heading says these come from the GP's work papers.** The audit also lists, under what it grafted onto its recommendation, `retrieving WP-36 and WP-38 first`, which reads as WP-38 not yet having been read at the time. Either way, **these are the same assertions restated, not a second source.** Do not present the audit as confirming WP-38 on Findings 1, 2 or 4.

### Where the audit is a genuine second observation, it contradicts WP-38 on one point. Report the disagreement.

The audit walked the Dropbox tree and listed folders directly. It reports: `2.4 Transfer-Assignment Documentation contains nothing but a draft and zero final documents.`

WP-38 v3 says twice that `Folder 2.4 is empty` (Finding 1, and again in the Finding 4 table: `Archive folder 2.4 -- Empty.`).

Register item 2.32 in the live v58 register says `Replaced by WP-36-M1 v2 (transfer register + document request), filed in 2.4 for signature.`

Three sources, three states for one folder: empty, holds one draft, holds WP-36-M1 v2. **The reconciliation that fits all three is that 2.4 holds exactly one item, the WP-36-M1 v2 draft, and that WP-38's "empty" means empty of executed source documents rather than literally empty.** WP-38's own preceding sentence supports that reading: `The archive holds no assignment or transfer instrument, no GP consent to transfer, and no transferee subscription or joinder for any of the seven. Folder 2.4 is empty.` Taken literally, though, the sentence contradicts both other sources, and it is the sentence a hostile reader will quote.

**This is the single best available evidence that at least one of the three memos due for signature exists.** An independent Dropbox listing on 2026-09-03 saw a draft in folder 2.4, which is where WP-36-M1 v2 is supposed to be. Labelled SINGLE-SOURCE and indirect: the audit did not name the file or open it, so it corroborates that something is there, not what it says. Finding D stands, softened by exactly this much.

### WP-36 and WP-38 agree on everything I could test, VERIFIED, and WP-36 records one open risk WP-38 glosses

Points of agreement, checked line by line:

- WP-36 sheet 1, cell H7: `no drawdown transaction in 2,128 rows of activity 2017-2026` matches WP-38 Finding 3 test 3 exactly, `The 2,128-row activity report for 01/2017-12/2026`.
- WP-36 H7: `contributed = position value on all 68 Class A positions ($12,589,708)` matches WP-38 Finding 3 test 2 to the dollar.
- WP-36 H5, H6, H33, H34, H35, H36 restate WP-38's Findings 1, 2, 4 and 5 and cite them by section (`See WP-38 s2`, `s3`, `s4`) and by register ID (2.31 through 2.34). No divergence in any figure.
- WP-36 sheet 3 rows 15, 16 and 17 record the withdrawal of the two no-activity memos and the refile of the 2019 Closing Letter from 2.3 to 2.5, matching WP-38's housekeeping instruction.

**The open risk.** WP-36 item D-08, sheet 1 row 12: needed item `Verify fund-level 1065 returns present for every year 2018-2025 (K-1 sets confirmed present 8/30)`, status `Verify`, owner `Claude`, due `2026-09-11`, note `Census counted K-1 folders; fund return presence not yet verified file-by-file`.

Two problems with that as it stands, given what the 2026-09-03 audit later proved.

1. **`Census counted K-1 folders` is a name-level check.** After 2026-09-03, a name-level census of that archive establishes nothing about contents. `K-1 sets confirmed present 8/30` should be downgraded from confirmed to unverified until someone opens files.
2. **The 2025 set is not a K-1 set.** The 2026-09-03 audit found that `2025 final Schedule K-1s do not exist` and that `68 per investor draft letters dated 2026-08-06 stand in their place`, one of which carries a header reading CY ended 12/31/25 against body text reading tax year ended December 31, 2024. WP-38's body is careful and calls it `the 2025 draft set` in both Finding 4 and Finding 5. **WP-38's header is not**, listing `K-1 sets 2018-2025` without qualification. WP-36 D-08 likewise reads `every year 2018-2025`. The 2026-09-15 filing deadline is twelve days out on the audit's own count.

### What WP-36 sheet 3 proves about the move log, VERIFIED

The move log has 14 numbered rows. It records nine MOVEs, two CREATEs and, at rows 12 and 13, the withdrawal of the two bad memos with reasons quoted from WP-38. It is a careful document. That is what makes the absence of a CREATE row for WP-36-M3, WP-36-M1 v2 and WP-36-M2 v2 meaningful rather than merely incomplete: the author recorded the creation of the two memos that were withdrawn and did not record the creation of the three that replaced them.

## Method, and the limits of this re-audit

**What I did.** Extracted WP-38 v1, v2 and v3 with xpdf `pdftotext` in `-layout`, `-table` and `-lineprinter` modes and cross-checked the three against each other wherever a figure mattered. Read PDF trailer metadata directly for producer, title, timestamps and embedded-file objects. Unzipped WP-36 and parsed `xl/worksheets/sheet1-3.xml` cell by cell. Walked the whole local project, 3,851 files and 438 directories. Opened all nine distribution reports with `xlrd` 2.0.2 and walked account 1034 row by row with forward-fill on merged cells. Opened the WCO limited partner statement including page 2. Parsed Issue Register v55, v56, v57 and v58 with `openpyxl` and read items 2.19, 2.31 to 2.35, 4.09, 4.38 and 5.05 in full. Grepped the live general ledger export for account 14211 and read the J315 and J316 rows. Read the Bedrock I Group trial balance. Opened both WP-12a drafts by unzipping `word/document.xml`. Searched every `.docx` and `.xlsx` in the project for the memo names.

**What I did not do, and it is the largest limit here.** I could not reach Dropbox. Every one of WP-38's seven header sources lives there, and so do the three memos. **Nothing in this page verifies the InvestNext activity report, the investor position schedule, any K-1 set, either Form 1065, the Schedule M-2, Item M or Item N of the A2Z K-1, the PPM, the subscription booklet or the 2019 Closing Letter.** Those are UNREACHABLE, which is a different finding from ABSENT and must not be merged with it.

**What that leaves unanswered.** The brief's central question was whether WP-38's citation to folder 1.8 points at a different document than the one its conclusion rests on. Finding B answers it in the only way the evidence allows: the citation names no file, so the question cannot be answered from the workpaper. Whoever opens folder 1.8 next should look for a Class A and Class B subscription booklet containing, at Item 6, the sentence WP-38 quotes: `After Acceptance please send your Capital Commitment via ACH to: Bedrock MHC Fund II, LP, Account #: 4460 3474 3502.` That quoted string is the only handle WP-38 gives for identifying its own source, and it is the right search key. **Note that the quotation itself contains a fund bank account number, printed in the clear in a workpaper that is circulating for signature.** That is a third instance of the same exposure class as Finding A's taxpayer identification numbers and the 2026-09-03 audit's ACH forms.

**Two things worth saying in WP-38's favour, because a re-audit that only lists defects is not honest.** First, every one of the eight locally reachable body sources checked out. The $312,026.55 and $53,029.70 figures are exact. Register 5.05's J315 detail is confirmed in the general ledger itself. The WP-12a quotation is accurate and correctly labelled a draft. The 4.09 balance matches to the cent. Second, both disclosed corrections are complete: no erroneous v1 or v2 language survives into v3 anywhere in the text, tested phrase by phrase. **The problems in WP-38 are problems of citation discipline and of unreachable evidence, not of invention.**

## Related

- [[80-Finance/fund-reporting/bmhcii-archive-audit-2026-09-03]] the fourteen-agent Dropbox audit this re-audit was commissioned against
- [[80-Finance/fund-reporting/bedrock-fund-ii-winddown]]
