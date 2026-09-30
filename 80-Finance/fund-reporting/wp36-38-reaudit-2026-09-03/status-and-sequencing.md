# WP-36 status re-audit and true sequencing, as of 2026-09-03

**Scope.** Whether WP-36's status picture is still true four days after it was written, and what order the work actually has to happen in. Arithmetic and source-file naming are owned by other agents and are not re-checked here.

**Primary sources.**

- `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\12_Document_Archive\WP-36_Document Archive Needed Items + Timeline.xlsx`, sheets `Needed Items` (sheet1), `Timeline` (sheet2), `Move Log 2026-08-30` (sheet3). Strings inline, no sharedStrings part. Workbook `docProps/core.xml` shows created 2026-08-30T03:39:43Z, modified 2026-08-30T20:15:20Z, creator openpyxl.
- `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\12_Document_Archive\WP-38_Investor_Records_Integrity_Review_v3_20260830.pdf`, read with `pdftotext -layout`, 6 pages.
- `C:\Users\AustinBerk\Documents\My Brain\80-Finance\fund-reporting\bmhcii-archive-audit-2026-09-03.md`, the fourteen agent audit of 2026-09-03.
- Local working tree `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\`, 3,851 files across 438 directories, fully readable.

**Reachability, stated once so it is not restated per item.** The destination-folder column of WP-36 sheet1 points at the Dropbox archive `/Austin Berk/BMHCII`. **That namespace is not reachable from this session's tools.** So no item whose status turns on the contents of a Dropbox folder can be confirmed or refuted here. What is reachable and was tested: the local working tree above, the other wind-down workpapers and the issue register that sit in it, the Brain registers, and the fourteen agent audit's own dated listings of the Dropbox folders. The last of those is a secondary source and is labelled as such every time it is used.

**Evidence labels used below.** VERIFIED means two independent reachable sources agree. SINGLE-SOURCE means one reachable source. INFERRED means a conclusion drawn from reachable facts. UNTESTABLE FROM HERE means the evidence sits in Dropbox, InvestNext, Box, or a third party's hands.

---

## 0. The one thing most likely to go wrong tomorrow morning

**The 09-04 milestone says "sign three memos." All three exist, all three still carry `_DRAFT` in the filename, and the two memos that must never be signed sit two folders away under names that differ from the correct ones only by a `_v2` and a few words.**

The fourteen agent audit listed the Dropbox folders on 2026-09-03 and found, live inside the numbered sections, exactly three files (`bmhcii-archive-audit-2026-09-03.md` chain, recorded on `C:\Users\AustinBerk\Documents\My Brain\80-Finance\fund-reporting\bedrock-fund-ii-winddown.md` line 165):

- `2.3 Capital Call Notices/WP-36-M3_No Capital Call Activity_DRAFT.pdf`
- `2.4 Transfer-Assignment Documentation/WP-36-M1_v2_Transfer Register and Document Request_DRAFT.pdf`
- `2.5 Additional Subscription/WP-36-M2_v2_Additional Subscription Schedule and Document Request_DRAFT.pdf`

and, in `2. Investor Records/Archive_Superseded`, the two withdrawn memos whose own note reads *"Do not sign, circulate or rely on."* VERIFIED by that listing, which is a reachable secondary source dated today; the Dropbox namespace itself is UNTESTABLE FROM HERE.

So the failure mode is not a missing document. It is this: **an executor with no fund experience is being told to sign a document, in a folder that also contains a near-identically named document that WP-38 says in capital letters must never be signed**, and the only thing separating them is reading `_v2` and the folder name. WP-38 page 1: "DO NOT SIGN WP-36-M1 OR WP-36-M2 AS DRAFTED. BOTH ARE CONTRADICTED BY THE FUND'S OWN BOOKS AND BY FILED TAX RETURNS." That sentence is in a PDF the checklist never tells anyone to open. WP-36 sheet1 column E for D-01 and D-02 says only `Superseded - replaced`, which does not tell a novice that the superseded thing is a signature-ready-looking PDF sitting in the same section tree.

**Second, and it makes the first worse: all three are stamped DRAFT and none of them is a signature-ready instrument.** Signing a PDF whose filename and face say DRAFT produces an executed record of the fund's investor history that reads DRAFT forever. The step the checklist omits between "drafted" and "signed" is finalisation, and no row on WP-36 owns it.

**Third, the signature itself is not delegable.** WP-38's addressee block reads "Prepared for Austin Berk, Authorized Signatory, Bedrock MHC Fund II GP, LLC." These are General Partner representations about what the partnership did and did not do, going into a file that a 33% partner's counsel has subpoenaed and that is now inside active litigation. **No one but the authorized signatory can sign them, and no amount of written instruction changes that.** An inexperienced executor's correct action on D-01, D-02 and D-03 is to prepare and route, never to sign.

---
## 1. The full item table as written

All 31 D-items plus T-01, transcribed from `WP-36...xlsx` sheet `Needed Items` (sheet1), rows 5 to 36. Note the row order in the file is not the ID order: D-01 to D-27 occupy rows 5 to 31, **T-01 sits at row 32, and D-28 to D-31 sit at rows 33 to 36 after it.** An executor scrolling the sheet meets the timeline answer before the four highest-consequence document items. VERIFIED, read from the sheet XML.

| ID | Row | Murad ref | Needed item (abridged) | Destination | Status 8/30 | Owner | Due |
|---|---|---|---|---|---|---|---|
| D-01 | 5 | none | Signed no-activity memo, LP transfers/assignments | 2. Investor Records/2.4 | Superseded, replaced | Austin | 2026-09-04 |
| D-02 | 6 | none | Signed no-activity memo, additional subscriptions | 2. Investor Records/2.5 | Superseded, replaced | Austin | 2026-09-04 |
| D-03 | 7 | none | Capital call notices OR signed no-activity memo | 2. Investor Records/2.3 | Draft issued, SIGN | Austin | 2026-09-04 |
| D-04 | 8 | closing documents | Full closing sets for portfolio sale parks: deeds/assignments, escrow, title. MIPAs on file only for Tarheel, Mobile Manor, Royal Palm, Everglades | 5. Closings and Dispositions | Partial | Austin | 2026-09-11 |
| D-05 | 9 | escrow details | Escrow statements/ledgers for each sale | 5. Closings and Dispositions | Missing | Austin | 2026-09-11 |
| D-06 | 10 | mortgage statements | Loan payoff statements for each financed fund asset | 3. Property Level/3.6 Payoff Statements | Missing | Austin | 2026-09-11 |
| D-07 | 11 | bank statements | GreenSpot x2488, Valley View BAML, Cedar Grove (empty), Westwood (1 file) | 4. Fund Level/4.2 | Partial | Austin | 2026-09-25 |
| D-08 | 12 | tax documents | Verify fund-level 1065 returns present for every year 2018 to 2025 | 4. Fund Level/4.5 | Verify | Claude | 2026-09-11 |
| D-09 | 13 | remaining unsold assets | Schedule of remaining assets: Lamberton Lake, Tarheel interest, carried notes, POH/GP homes | 5. Closings and Dispositions | Open | Claude | 2026-09-11 |
| D-10 | 14 | IM AUM fee schedules | IM-side asset management fee schedules and collections support | 6. GP and Investment Manager | Missing | Austin | 2026-09-18 |
| D-11 | 15 | IM acq/dispo fees | Acquisition and disposition fee support | 6. GP and IM | Missing | Austin | 2026-09-18 |
| D-12 | 16 | IM financing fees | Financing fee support | 6. GP and IM | Missing | Austin | 2026-09-18 |
| D-13 | 17 | IM tax documents | Bedrock Group LLC tax returns for fund years | 6. GP and IM | Missing | Austin | 2026-09-18 |
| D-14 | 18 | IM bank statements | Bedrock Group LLC bank statements | 6. GP and IM | Missing | Austin | 2026-09-18 |
| D-15 | 19 | GP fees collected | GP fee collection support | 6. GP and IM | Missing | Austin | 2026-09-18 |
| D-16 | 20 | GP LP contributions from fee rollovers | Support for GP/sponsor LP positions funded by fee rollovers | 6. GP and IM | Missing | Austin | 2026-09-18 |
| D-17 | 21 | GP contributions from asset sales | Support for amounts contributed into LP from asset sales | 6. GP and IM | Missing | Austin | 2026-09-18 |
| D-18 | 22 | GP loans to BMHC2 | Instruments/support for GP-fund loans | 6. GP and IM | Missing | Austin | 2026-09-18 |
| D-19 | 23 | GP bank statements | GP entity bank statements | 6. GP and IM | Missing | Austin | 2026-09-18 |
| D-20 | 24 | PM 5% fees | PM fee support, 5% of revenue per asset | 6. GP and IM | Missing | Austin | 2026-09-18 |
| D-21 | 25 | PM use of proceeds | Use-of-proceeds support | 6. GP and IM | Missing | Austin | 2026-09-18 |
| D-22 | 26 | PM transactions | Transaction detail showing collections | 6. GP and IM | Missing | Austin | 2026-09-18 |
| D-23 | 27 | PM bank statements | PM entity bank statements | 6. GP and IM | Missing | Austin | 2026-09-18 |
| D-24 | 28 | PM tax documents | PM entity tax documents | 6. GP and IM | Missing | Austin | 2026-09-18 |
| D-25 | 29 | none | Fund-level organizational documents: certificates, EIN, good standing | 4. Fund Level/4.4 | Missing | Austin | 2026-09-18 |
| D-26 | 30 | none | Resolve 7 empty entity folders in 3.1 (POH entities) | 3. Property Level/3.1 | Open | Austin | 2026-09-18 |
| D-27 | 31 | none | Final QC sweep: map every Murad line to a filed document or signed memo; certify Murad-complete | All | Open | Claude | 2026-09-30 |
| T-01 | 32 | Distributions, dates | LP gain distribution date; K-1 delivery dates; GP proceeds/waterfall dates plus all calculations | n/a, an answer not a document | Timeline answer | Austin/CPA | 2026-12-12 |
| D-28 | 33 | BMHC2 / investor records | Assignment or transfer instrument, GP written consent, transferee joinder for each of the seven 1/1/2022 CS Partners IV transferees | 2. Investor Records/2.4 | Open | Austin | 2026-09-18 |
| D-29 | 34 | BMHC2 / investor records | Executed subscription agreements or supplements for the five second-tranche subscriptions ($498,548), plus character of Forster $239,910 / $4,798 | 2. Investor Records/2.5 | Open | Austin | 2026-09-18 |
| D-30 | 35 | Distributions / K-1s | 2020 assignment instrument and GP written consent for the Khodara to WCO Capital transfer, confirmatory assignment acceptable | 2. Investor Records/2.4 | Open | Austin | 2026-09-11 |
| D-31 | 36 | Bedrock GP / IM | A2Z 2024 admission package: admission or reallocation agreement, LP schedule amendment, consideration recital, Bedrock I Group consent to its 2.7461477% reduction, basis for the 1.0128557% redistributed | 6. GP and IM | Open | Austin / Counsel | 2026-09-18 |

**Owner distribution, counted cell by cell from column F.** Austin 27 rows (D-01 to D-07, D-10 to D-26, D-28, D-29, D-30), Claude 3 (D-08, D-09, D-27), Austin / Counsel 1 (D-31), Austin/CPA 1 (T-01). Total 32. VERIFIED. The Brain page `C:\Users\AustinBerk\Documents\My Brain\00-Meta\audit-log.md`, row dated 2026-09-03, states "Claude on 4"; the file says 3. Minor, recorded rather than smoothed.

**Notes carried on the rows, the ones that change the work.**

- D-01 (H5): "WP-36-M1 no-activity memo WITHDRAWN 8/30: seven transfers DID occur 1/1/2022 (CS Partners IV to 7 transferees). Sign WP-36-M1 v2 (transfer register + document request) instead. See WP-38 section 2. Register 2.32."
- D-02 (H6): "WP-36-M2 no-activity memo WITHDRAWN 8/30: five second-tranche subscriptions totalling $498,548 DID occur. Sign WP-36-M2 v2 instead. See WP-38 section 3. Register 2.33."
- D-03 (H7): "ANSWERED 8/30: no capital calls were ever issued. Three tie-outs. WP-36-M3 drafted and filed in 2.3 for signature. 2019 Closing Letter refiled 2.3 to 2.5."
- D-07 (H11): "Aug 2026 monthly and forward: file as issued."
- D-08 (H12): "Census counted K-1 folders; fund return presence not yet verified file-by-file."
- D-09 (H13): "Claude drafts from ledger + BOVs; Austin confirms."
- D-10 (H14): "4.3 Fee Workbook is fund-side; IM-side support needed."
- D-18 (H22): "Intercompany balances exist on ledger; instruments needed (see WP-32/T-011 work)."
- D-20 (H24): "No Bedrock PM docs anywhere in archive as of 8/30."
- D-25 (H29): "Entity-level formation docs are in 3.1; Section 1 holds agreements."
- D-26 (C30) names the seven entities: Cedar Grove Homes, Colonial Homes, Lambeth Homes, Wolf Bay Homes/MHC, Westwood MHP, Lamberton Lake Homes, Wolf Bay Holdings. H30: "Populate with formation docs or mark N/A with note."
- D-27 (H31): "Gate for Citrin fieldwork ~10/1."
- D-28 (H33): "NOTE: folder 2.4 must cover TWO transfer events, the 2020 Khodara to WCO transfer (D-30) and the 1/1/2022 CS Partners IV split."
- D-30 (H35): "Blocks the final distribution and the final statement rerun until the register is corrected."
- D-31 (H36): "Resolve with 5.05 and WP-12a as one Lamberton chain. Goes to counsel in the WP-12 pack."
- T-01 (H32): "Final distro ~12/12 after Lamberton 11/30; calcs = LP workbook + waterfall WP; K-1s per Citrin."

**Sheet 3, the Move Log, records 14 executed actions on 2026-08-30, all by Claude, authorized by Austin Berk.** Nine MOVEs: two BOVs from the archive root to `5. Closings and Dispositions/Valuations (BOVs)`; two refi settlement statements from the section 3 root to `3.5 Loan Documents`; the sell-side portfolio PSA and its Amendment 1 to `5. Closings and Dispositions`; three superseded bank recon versions (v1, v2, v3) to `4.2 Bank Statements/Archive_Superseded Recon Versions`, with v4 retained as current. Two CREATEs: `_FOLDER STATUS.txt` in 3.6, 4.4, section 6 and 2.3; and the M1/M2 draft memos committed to 2.4 and 2.5. Two withdrawal MOVEs of those same memos to `2. Investor Records/Archive_Superseded`. One refiling of `2019 Closing Letter.pdf` from `2.3 Capital Call Notices` to `2.5 Additional Subscription`.

**The move log contradicts itself and sheet1 on the memo names.** Sheet3 row 14 (item 11) calls the drafts "WP-33-M1/M2"; sheet3 rows 15 and 16 (items 12 and 13) call the same two files "WP-36-M1" and "WP-36-M2"; sheet1 C5 and C6 say "WP-33-M1 draft delivered 8/30" and "WP-33-M2 draft delivered 8/30" while H5 and H6 of the same rows say WP-36-M1 and WP-36-M2. **Six cells in one workbook, two different workpaper numbers, the same two documents.** Source-file naming is another agent's lane; the consequence is mine to report. A novice searching the archive for "WP-33-M1" will find nothing, and the file that actually exists is named `WP-36-M1_v2_Transfer Register and Document Request_DRAFT.pdf`.

**The move log does not record the creation of the three memos the 09-04 milestone says to sign.** It records only the v1 drafts being created and then withdrawn. All three of M3, M1 v2 and M2 v2 nonetheless exist on Dropbox per the 2026-09-03 listing. So the log is incomplete rather than wrong, which for a document-provenance workpaper is still a defect: **there is no recorded chain of custody for the three documents that are about to become executed General Partner representations inside a litigation file.**

---
## 2. Re-test of every status against reality, item by item

**What was reachable and used as the test bed.** The local working tree; the fourteen agent Dropbox listing of 2026-09-03 (a secondary source, but a dated listing rather than an inference); `WP-37_Workstream_Tracker_BMHCII_20260830.xlsx`; `WP-Issue_Register_BMHCII_v58.xlsx` of 2026-08-30; `WP-00b_Weekly_Internal_Digest_BMHCII_20260831.docx`; `WP-15b_LP_Note_2025_K1_Status_20260902.docx`; and the Brain registers `00-Meta/commitments.md`, `00-Meta/audit-log.md`, `80-Finance/fund-reporting/bedrock-fund-ii-winddown.md`.

**One test applies to all 32 items and is worth stating before the list.** Nothing in the local tree has moved on any WP-36 item since 2026-08-30. `find` over 3,851 files for anything modified on or after 2026-08-31 returns 20 files, all of them P2 fund-close and P5 tax work: `WP-39_August_2026_Close` (08-31), seven GL exports (08-31), `R-45_BankStmt_x3502_Aug2026_export.csv` (09-01), `WP-40_Aug_Close_Residue` (09-02), `WP-15b_LP_Note_2025_K1_Status` (09-02), `R-46` to `R-48` (09-02), `WP-41_Journal_Register_Crosswalk` (09-02), and `WP-00b` digest (08-31). **No memo, no signed instrument, no archive workpaper, no WP-36 revision.** VERIFIED. Corroborated independently by the 08-31 digest, which reports "Closed since last Monday: Zero. No task moved to DONE since last Monday," and by WP-37's own P1 line reading "0 complete as of 8/30."

### D-01 and D-02, the withdrawn no-activity memos

- **Tested?** Yes, twice removed. Against WP-36 sheet3 rows 15 and 16, and against the 2026-09-03 Dropbox listing.
- **Verdict: the 8/30 status is still literally true and materially misleading.** The v1 memos are indeed withdrawn to `2. Investor Records/Archive_Superseded`. But the cell says `Superseded - replaced`, which describes the state of the document nobody should touch and says nothing about the state of the document someone must act on. As of 2026-09-03 the replacements exist and are **unsigned and still filename-stamped `_DRAFT`**. SINGLE-SOURCE on the DRAFT stamp (the 09-03 listing); UNTESTABLE FROM HERE as to whether a signature has since been applied inside Dropbox.
- **What would test it:** open `/Austin Berk/BMHCII/2. Investor Records/2.4/` and `/2.5/` and read the signature block of the two `_v2_` PDFs.

### D-03, capital call notices or memo

- **Tested?** Yes. Against WP-37 Milestones row for 09-04, which reads status "Pending, packet ready 8/30"; the 08-31 digest, Austin's open actions item 7, "Sign WP-36-M3 packet, ready since 8/30, due 9/4"; and the 09-03 listing showing `WP-36-M3_No Capital Call Activity_DRAFT.pdf` live in `2.3`.
- **Verdict: unchanged. Still unsigned, three independent sources agreeing, and the finding underneath it is the strongest on the sheet.** WP-38 section 4 carries three independent tie-outs: the Subscription Booklet Item 6 funds the whole commitment on acceptance; Position Value equals Contribution Amount on all 68 Class A positions totalling $12,589,708; and the 2,128-row activity report 01/2017 to 12/2026 contains only Dividend (2,043), Investment (66), Transfer Out (7) and Transfer In (7), with the 66 Investment rows footing to $12,589,708 exactly. VERIFIED within WP-38 by three sources.
- The caveat WP-38 insists the memo carry, and which a novice would drop: the PPM does define a Commitment Period and a drawdown mechanic with seven days notice plus an Investor Default remedy. **The memo must say the power existed and was never exercised, not that the folder is empty.**

### D-04, full closing sets

- **Tested?** Yes, and **the status has changed since 8/30.** Austin, 2026-09-03, quoted on `bedrock-fund-ii-winddown.md`: *"Chris is getting the documents together. anything needed can be held until we get those and reassess."* The Brain records the consequence explicitly: "So nothing opens on these and nothing chases Hoke," and names what is held, including **the closing binders across the transactions.**
- **Verdict: D-04's 09-11 action, "requests out to counsel, title, lenders," was overtaken by an Austin hold three days after WP-36 was written.** SINGLE-SOURCE, Austin quoted, 2026-09-03. An executor who chases Woods Oviatt on 09-11 would be acting against a live instruction they have no way of seeing from the checklist.
- Also still true and untested from here: MIPAs on file only for Tarheel, Mobile Manor, Royal Palm and Everglades out of a nine-park seller-financed portfolio.

### D-05, escrow statements and ledgers

- **Tested?** Partly. Same hold covers **the Green Spot escrow release and lien clearance before the May 2020 sale.** The wider set of per-sale escrow statements is UNTESTABLE FROM HERE.
- **Verdict: still Missing, and now partly held.** Plus a prerequisite nobody wrote down: the 09-03 audit records that **"nobody currently knows who the fund's QI or insurance broker was"** and prescribes finding them by searching the bank statements and general ledger for payments to the QI, the administrator, title agents and the law firms. **You cannot request an escrow ledger from an escrow agent you have not identified.** D-05 has a step zero that is not on the sheet.

### D-06, loan payoff statements

- **Tested?** Yes, indirectly and consistently. WP-36 sheet3 item 10 records `_FOLDER STATUS.txt` being created in 3.6 on 08-30; the 09-03 audit records `3.6` mortgage payoff statements as **self-declared absent by the vault's own placeholder note, owner named as Austin.**
- **Verdict: unchanged. Still Missing as of 2026-09-03.** VERIFIED by two independent sources agreeing the folder is empty and flagged.

### D-07, bank statement completeness

- **Tested?** Yes, in three parts, with three different answers, which is why the single word "Partial" is not good enough.
  1. **The Aug 2026 monthly leg has moved and is nearly done.** `R-45_BankStmt_x3502_Aug2026_export.csv` landed 2026-09-01; `WP-39_August_2026_Close_BMHCII_20260831.xlsx`, `WP-40_Aug_Close_Residue_F3_F5_Footings` and `R-48_Bank_Register_Uncleared_x3502_09022026.xlsx` follow it. VERIFIED locally. The note "Aug 2026 monthly and forward: file as issued" is satisfiable now.
  2. **The Cedar Grove leg is confirmed still empty.** The 09-03 audit: `4.2/Property Accounts/Cedar Grove` zero files. VERIFIED as of 09-03.
  3. **GreenSpot x2488 and Valley View BAML are UNTESTABLE FROM HERE** and are third-party requests to closed-account banks.
- **A finding the audit adds that reframes the item:** the 09-03 audit also found **"All three Wolf Bay entity formation folders empty, for a property with 46 bank statements,"** and `NCHOMES, LBHOM and SC ledgers delivered as 109 byte header only CSVs.` So bank-statement completeness is uneven in ways the four named gaps do not capture.

### D-08, verify fund-level 1065 returns 2018 to 2025. The known instruction defect, and it is worse than reported

- **Tested?** Yes, against three sources, and the item fails on two separate grounds.
  1. **Scale.** The 09-03 audit: `4.5 Tax Returns` holds **989 files**, and `4.1 General Ledger` exists with 72 files and 46.9 MB, meaning Section 4 had been undercounted by roughly 95% of its file count. VERIFIED by listing. WP-36's note, "Census counted K-1 folders; fund return presence not yet verified file-by-file," tells a novice this is a hunt through a thin folder. It is a filtering job across a thousand files, most of which are per-investor K-1s.
  2. **The 2025 return cannot be present, because it does not exist yet.** `WP-15b_LP_Note_2025_K1_Status_20260902.docx`, prepared 09-02: the fund's 2025 partnership return is *"in final partner review with our accountants. That review is the last step before your Schedule K-1 can be released."* VERIFIED, local file. **So D-08 as written asks an executor to verify the presence of a document that has not been filed.** A conscientious novice would conclude the 2025 return is missing from the archive and raise it as a gap. It is not a gap; it is unfinished work at Citrin.
  3. **2024 is confirmed present.** WP-38's Sources block names "filed 2024 Form 1065 (4.5)" among the records tested, and WP-38 section 6 parses all 68 partner K-1s out of it. VERIFIED.
- **Verdict: the status word "Verify" is right and the instruction underneath it is wrong.** Rewrite in section 6 below.

### D-09, schedule of remaining assets

- **Tested?** Yes, and it has a hidden blocker and a duplicate ID.
- **The blocker.** Lamberton Lake is the largest remaining asset and register 3.09, opened 2026-08-30 by Austin, says the structure is unresolved: **CURE A gives the Fund a 51.00% look-through to the park, CURE B gives 45.90%, "5.1 points apart, different consents required,"** and the instruction is explicit: *"DO NOT redraft, execute or circulate WP-12a v2. DO NOT treat 11/30 as a closing date until the cure is chosen."* **A remaining-asset schedule drafted before 3.09 is answered will state the wrong interest in the fund's largest remaining holding.** VERIFIED from register v58.
- **The duplicate.** WP-37 Milestones has 09-05 "WP-12 legal pack" and the 08-31 digest lists "T-040 WP-12 remaining-assets workpaper (Claude, 9/5)". So the same deliverable carries a WP-36 ID (D-09, due 09-11) and a task-board ID (T-040, due 09-05) with different dates. VERIFIED across two files.
- **Verdict: status "Open" is still true; the date and the owner are not, and the item is not safely draftable yet.**

### D-10 through D-24, the fifteen Section 6 items

- **Tested?** As a block, yes. The 09-03 audit records Section 6's GP, Investment Manager and PM fee schedules, collections support, banking, tax and use-of-proceeds support as **self-declared absent by the vault's own placeholder note**, and adds the sentence that matters: **"which are precisely the sections Murad's request names."** WP-36 sheet3 item 10 corroborates the placeholder being planted in section 6 on 08-30.
- **Verdict: all fifteen unchanged, still Missing as of 2026-09-03.** VERIFIED as a block.
- **But five of the fifteen are not document-retrieval items at all, and the sheet hides it.** D-10, D-11, D-12, D-15 and D-20 ask for fee schedules and fee support. The 08-31 digest's first gating decision reads: **"Fee framework, charge / waive / recharacterize ~$1.6M (T-007). BLOCKED, 5 open blockers, target 9/15."** Register 4.17 lists the gates before the fee package can post, including *"(a) Austin+Jon confirm fee framework"* and *"(d) management agreements filed as rate exhibits."* Register v58 records the T-011 EXECUTION COPY v2 as awaiting **Jon countersignature.** **Producing a fee schedule into the archive before the charge/waive/recharacterize decision lands manufactures a document that the later decision contradicts, inside a file that is now discoverable.**
- **D-20 is worse than blocked, it is self-contradictory.** It asks for "PM fee support (5% of revenue per asset)" while the 08-31 digest carries gating decision 2 as **"Land the PM rate, 4% vs 5%, $221,934.48 swing (T-002), IN PROGRESS since 8/21."** The item states the answer to an open question in its own instruction.
- **D-18 has its instrument problem already scoped elsewhere.** Its note points at WP-32/T-011; register 1.23 shows the related sponsor draw series papering is FIX IDENTIFIED with "NO SEPTEMBER PAYMENT" and five sequenced next actions. So D-18 is a downstream consumer of that work, not an independent pull.

### D-25, fund-level organizational documents

- **Tested?** Yes. `_FOLDER STATUS.txt` planted in 4.4 on 08-30 (sheet3 item 10); the 09-03 audit lists `4.4` fund organizational documents as self-declared absent.
- **Verdict: unchanged, still Missing.** VERIFIED. This is one of the few items on the sheet whose sources are public registries and the IRS rather than a hostile or departed party.

### D-26, empty entity folders in 3.1. A quantified contradiction

- **Tested?** Yes, and **WP-36 undercounts it.** WP-36 C30 names **seven** POH entity folders. The 09-03 audit, by listing: **"Twelve sub folders are completely empty: eleven entity folders in `3.1` and one property bank account folder in `4.2`."**
- **Verdict: status "Open" still true; the scope is 11 folders, not 7.** VERIFIED contradiction between two dated sources, reported rather than reconciled. An executor working the seven named entities will close the item and leave four empty folders behind, and D-27 will certify the section complete.

### D-27, final QC sweep and certification. The instruction that would produce a false certificate

- **Tested?** Yes, against the 09-03 audit, and this is the most serious finding in this section after D-08.
- D-27 says: "map every Murad line to a filed document or signed memo; certify archive Murad-complete." **The 09-03 audit establishes that in the archive's most sensitive folder, filenames do not identify their contents.** Its own words: "every file opened in 1.8 specifically to test whether its name matched its contents failed the test," and "roughly two dozen files are now confirmed wrong about the investor, the document type, or both." Named examples: `Thien_Quach_-_Bedrock_MHC_Fund_II.pdf` is Michael Mitchell's Letter of Accreditation; `MIchael Mitchell_Accreditation.pdf` is Khodara's subscription package; `Bedrock MHC Fund II LP Limited Partnership A&R.pdf` is the unexecuted, undated First Amendment with all four signature lines blank; `Committments.xlsx` is an 80-page DocuSign Certificate of Completion; `Quad G ACH Form.pdf` is a 64-byte Windows Internet Shortcut.
- **Verdict: D-27 as written maps request lines to filenames, and the filenames are unreliable. Executed against a 1,513-file archive by someone who cannot open and recognise a subscription booklet, it certifies a false statement to a partner who has subpoenaed the file.** It also has to catch that **five files are artefacts of a VOIDED DocuSign envelope** and must not be memorialized as executed.
- One further impossibility on the same row: **the document that triggered Murad's demand, the 2026-05-08 "Bedrock MHC Fund II LP Summary", exists nowhere in Dropbox and survives only as a Gmail attachment.** A Murad-complete certification cannot be issued while a request line points at a document that is not in the archive.

### T-01, the distribution and K-1 dates

- **Tested?** Yes, and the answer moved a long way in four days. Four independent gates now sit under the single date 2026-12-12.
  1. **11/30 Lamberton is not a date.** WP-37 Milestones for 11-30: "Lamberton resolved, SEPARATE THREAD (3.09). Structure question answered and cure chosen BEFORE this is treated as a closing date," status **"Blocked on 3.09."** The 08-31 digest: "T-004 shows 11/30/2026, but that date now sits on top of NEW item 3.09 ... 3.09 carries no owner date. The 11/30 date is fictional until this is answered."
  2. **K-1 delivery has an earlier and harder clock than 12/12.** `CM-25`, VERIFIED from the mailbox: **Tabish Rizvi of Onyx Holdings, 2026-09-02, "We need to process our own corporate returns by 9/15."** Twelve days from that date. Six LPs are chasing in writing with no reply on file. 2025 finals are over four months behind the 2026-04-23 drafts.
  3. **The CPA-signed waterfall is promised for Q3 2026, which ends 09-30, not 12-12.** `CM-25`: an LP asked for a fund-level waterfall "prepared and signed off by the CPAs so they can make a representation," Austin agreed unconditionally, and the filed wind-down plan promises the final waterfall in Q3 2026.
  4. **The December distribution now needs counsel sign-off.** Register 6.16: *"effect on the December final distribution, distributing while an LP fraud-count suit is pending needs counsel sign-off."*
- **Verdict: T-01's status "Timeline answer" is the one status on the sheet that is actively wrong now.** It is not an answer waiting to be typed; it is four unresolved gates, one of which expires in twelve days.

### D-28, the seven CS Partners IV transfer instruments

- **Tested?** Indirectly. UNTESTABLE FROM HERE as to folder 2.4 contents. The 09-03 audit lists among items "Genuinely absent, on the GP's own work papers rather than inference": **"The seven executed transfer instruments and the General Partner's written consent for the CS Partners IV admissions of accounts 1063 to 1069 effective 2022-01-01."**
- **Verdict: unchanged, and the audit widens it.** The audit continues: **"Those seven limited partners have no subscription agreement, joinder, LP counterpart, accreditation or transfer instrument anywhere reachable."** WP-36 D-28 asks for three document types. The gap is five, and it covers seven partners who hold $287,500 of the fund with no executed evidence of anything.

### D-29, the five second-tranche subscriptions

- **Tested?** Indirectly, same basis. The 09-03 audit: **"The five additional subscription agreements and GP acceptances totalling $498,548 between 01/2019 and 07/2020"** genuinely absent.
- **Verdict: unchanged.** VERIFIED absent by two dated sources.
- **A coverage gap WP-36 does not carry.** The same audit section: **"Twelve investors have no subscription agreement anywhere, vault or older tree. Five of those are not transferees, so they are primary subscriptions with no executed evidence on file."** Those twelve are a superset of D-29's five and have no D-item.

### D-30, the 2020 Khodara to WCO Capital assignment. Reprioritise this one first

- **Tested?** Yes, and this is where the four days matter most.
- The 09-03 audit confirms it still absent: **"The 2020 assignment instrument and GP consent for the account 1034 interest transferred to WCO Capital. The investor register was never corrected and distributions have been paid under the transferor's name from 2020 forward."**
- **The new fact, and WP-36 does not carry it.** `CM-25`, VERIFIED, thread read in full: **the WCO Capital principal is Gregory Khodara**, and on 2026-08-24 he wrote *"I will need to see the fund level return calculation... escalate to the state securities regulator."* He is asking for three things: written confirmation the GP took no promote given a sub-8% IRR, the fund-level return calculation, and resolution of a $348.88 accrual variance. Austin promised on 2026-08-16 *"If your read holds up we will take care of it right away"* and **no written reconciliation appears in the mailbox afterwards.**
- **Verdict: status "Open" still true, priority understated by a wide margin.** D-30 is the one item on this sheet whose counterparty has threatened a securities regulator in writing, whose position the register names under the wrong partner, and through whose account $312,026.55 went out on 2026-03-16 under a name that stopped being the partner of record in 2020. WP-36 gives it 09-11 and a one-line note.
- **A second document defect on the same party, from the 09-03 audit:** *"Khodara (WCO), the LP who has threatened to escalate to a state securities regulator, has his subscription agreement in this folder under two different names."* And `MIchael Mitchell_Accreditation.pdf` is Khodara's subscription package.

### D-31, the A2Z 2024 admission package. A direct contradiction with the register of the same date

- **Tested?** Yes. WP-36 H36 says: "Resolve with 5.05 and WP-12a as one Lamberton chain. **Goes to counsel in the WP-12 pack.**"
- Register v58, cut the same day, 2026-08-30, says of register 3.09: **"Austin carved it out to its own thread; scoping brief in 07_Legal_Dissolution; removed from the WP-12 counsel ask,"** and in the action column: **"DO NOT redraft, execute or circulate WP-12a v2."**
- **Verdict: WP-36 D-31 routes work into a counsel pack from which the register removed it on the same day.** Reported, not reconciled. The reachable evidence favours the register, because it is the file WP-37 designates as owning status and because `WP-12a_SCOPING_Open_Questions_20260830.pdf` exists locally as the carve-out artefact. But WP-36 is what the executor will be handed.
- Substance unchanged and still absent: the admission or reallocation agreement, the LP schedule amendment, the consideration recital, Bedrock I Group's consent to its 2.7461477% reduction, and the basis for the 1.0128557% redistributed. VERIFIED from WP-38 section 6 and register 2.34.

### Three WP-38 findings that have no WP-36 item at all

1. **Register 2.35, the Reinisch $12,500 basis overstatement.** WP-38 section 7: 37,500 units against a $50,000 amount and $50,000 opening cost basis; aggregate transferred $287,500 against $275,000 contributed; the whole variance on one row, carried in her reported capital account since 2022. Register v58 status **FIX IDENTIFIED**, owner Claude, and it *"gates final K-1 + final statement run."* **No D-item.**
2. **Register 2.35's second half, name normalisation.** WP-38 section 8: Renisch / Reinisch, Stuart / Stewart Taub, Thein Quach / Quash. The final K-1 run, the final LP statements and the final distribution file all key off names. **No D-item.**
3. **Register 3.09, the Lamberton structure question.** Gates the 11/30 milestone, the final distribution and the final K-1, and is the prerequisite for D-09 and D-31. **No D-item**, and WP-36 sheet2 lists 11-30 as a plain "anchor" with no blocker.

### The thing WP-36 does not mention once, and it governs the whole sheet

**There is active litigation in which the Fund itself is a named client, and WP-36 contains no reference to it.** Register 6.16, opened 2026-08-28, two days before WP-36 was written: *"ACTIVE LP LITIGATION: Gallagher & Gordon, Trustees of The Don Levin Trust v. Bedrock MHC Fund II GP, LLC et al., OC Superior Court 30-2026-01582020-CU-FR-CJC."* Surfaced via the Cappello & Noel retainer executed 2026-08-20; **clients are three parties including the Fund**; $50,000 paid from fund cash 2026-08-10. Its action column: *"All papering work in WP-32/T-012 is now litigation-adjacent, signed, dated, complete files only,"* and *"assume full discovery of the wind-down file."*

WP-37 turns that into a rule that binds most of WP-36: **P7 Litigation and Privilege is "CROSS-CUTTING. Nothing external, to counsel, to the CPA, to any LP, moves without Austin plus the privilege answer at T-013 Q1."** `T-013_Counsel_Briefing_DRAFT_BMHCII_20260828.docx` exists locally and is still DRAFT; WP-37 says it is *"awaiting Austin review then send to Cousineau."*

**Every outbound item on WP-36 is an external communication.** D-04, D-05 and D-06 are requests to counsel, title and lenders. D-28 and D-29 are document requests to limited partners. D-30 needs a confirmatory assignment executed with an LP who has threatened a regulator. D-31 goes to counsel. T-01 goes to the CPA. **None of them can leave the building until T-013 Q1 is answered, and WP-36 does not say so anywhere.** VERIFIED from WP-37 Dashboard row P7 and register 6.16.

### Two smaller contradictions, recorded because the brief says not to smooth them

1. **WP-38 cites a superseded register version.** WP-38 section 9: "Register version v56 carries these five items with columns L and M populated, per the WP-37 sync rule." Register v58's own header: *"two v55 files diverged ... v56 was cut from the first and is SUPERSEDED because it lacked 6.16."* And `09_Issue_Register/` locally holds v55, v57 and v58 and **no v56 at all**. So WP-38's citation points at a version that was withdrawn the same day for omitting the litigation item. VERIFIED by directory listing plus the v58 header.
2. **Register v58's header text describes itself as v57.** *"This v57 is the merge."* Cosmetic, but it is the file WP-37 designates as the single source of truth for status, and a novice asked to check a register item's status will not know which file is current.

---
## 3. Every date problem

**Today is Thursday 2026-09-03.** WP-36 sheet2 rows 5 to 14 carry the milestone calendar. Weekdays computed, not assumed.

| Due | Milestone | Weekday | Status on the sheet | Where it actually stands 09-03 |
|---|---|---|---|---|
| 2026-08-30 | Cleanup pass and structure census | **Sunday** | DONE | Past. Defensible as to the 14 logged actions, overstated as a label. See below. |
| 2026-09-04 | Investor-record memos signed | Friday | Pending | **Tomorrow.** Three DRAFT-stamped PDFs, no signature, no finalisation step owned. |
| 2026-09-11 | Closing sets, escrow, payoffs, 1065 verification, asset schedule | Friday | Pending | 8 days out. D-04 and D-05 overtaken by an Austin hold of 09-03. D-08 partly impossible. D-09 blocked on register 3.09. |
| 2026-09-18 | Section 6 populated, D-10 to D-26 | Friday | Pending | 15 days out. 15 of 17 items blocked behind the fee framework decision. D-26 scope is 11 folders, not 7. |
| 2026-09-25 | Bank statement completeness | Friday | Pending | 22 days out. One of four legs satisfiable now, two are requests to third parties, one is confirmed still empty. |
| 2026-09-30 | ARCHIVE MURAD-COMPLETE | Wednesday | Pending, WP-37 marks it **GATE** | 27 days out. Assessed below. |
| 2026-10-01 | Citrin fieldwork begins | Thursday | Context / Anchor | 28 days out, and itself unconfirmed. See point 5 below. |
| 2026-11-30 | Lamberton disposition | Monday | Context / Anchor | WP-37 restates it as **"Blocked on 3.09"** with no owner date on the blocker. |
| 2026-12-12 | Final distribution | **Saturday** | Context / Anchor | A Saturday. And it now needs counsel sign-off per register 6.16. |
| 2026-12-31 | Certificate of cancellation | Thursday | Context / Anchor | 08-31 digest: "zero slack". Counsel task T-041 for roughly 30 entities has "weeks-to-months lead" and **has not started**. |

### Which due dates are already past

**On WP-36's own sheet, only one: 2026-08-30, and it is marked DONE.** VERIFIED. Two qualifications.

1. **It was written and marked DONE on the same Sunday by the same session that issued WP-36.** `docProps/core.xml` shows the workbook created 2026-08-30T03:39:43Z and last modified 2026-08-30T20:15:20Z. A milestone self-certified on the day it is authored is not independent evidence that it happened.
2. **It is defensible on the 14 logged actions and overstated as a label.** "Cleanup pass" implies the archive was cleaned. The 09-03 audit found the archive's most sensitive folder, `1.8 Subscription Agreements`, is a flat harvest of 179 files with 21 duplicate-suffixed names, 40 opaque machine-token filenames, five LPA candidates sitting outside the dedicated LPA folder, and roughly two dozen files that are wrong about the investor or the document type or both. **The cleanup pass moved nine files and created three placeholder notes. It did not reach 1.8 at all.**

**Past due dates that are not on WP-36's sheet but bind its items.** These matter more than the sheet's own, because the sheet's next date is tomorrow while these are already late.

- **WP-37 Milestones 2026-08-31**, post AJE-1c.1 and AJE-32.1, owner Austin, status Pending. **Three days past.** AJE-32.1 is separately ON HOLD per register 1.23, because the executed Cappello retainer named three clients rather than one.
- **WP-37 Milestones 2026-09-01**, August bank statements to Aug close pass, owner Claude, status Pending. **Two days past**, though the local files show the work substantially done on 08-31 and 09-02.
- **T-001, the CPA call.** 08-31 digest: "READY since 8/21 and is 10 days overdue," re-dated by WP-37 to 09-07. As of today that is **13 days late**, and the digest says it gates 2.20, 1.16, 4.03, T-010 and "every K-1 task."
- **T-042 Oregon POA at 24 days and T-043 Woods Oviatt / Valley View reconveyance at 18 days**, both counted as of 08-31, so 27 and 21 days as of today. **T-043 runs through the same Woods Oviatt relationship D-04 and D-05 depend on.**
- **19 tasks overdue on the board as of 08-31**, by owner Austin 8, Team 6, Claude 4, CPA 1. The board itself has not been edited since 08-26, and its own cover cell reports 11, which the digest calls stale.

### Which dates fall inside the next seven days, 09-03 through 09-10

**One WP-36 milestone: 2026-09-04, tomorrow.** D-01, D-02 and D-03. That is the only WP-36 date in the window; 09-11 is eight days out and falls just outside.

**Three dates from outside WP-36 land inside the window, and one of them is a scheduling error.**

- **Monday 2026-09-07, the CPA call, per WP-37 Milestones. 2026-09-07 is Labor Day**, the first Monday in September. A call with an outside accounting firm is scheduled on a US federal holiday. VERIFIED by date arithmetic. Nobody appears to have caught it: the 08-31 digest reports the re-date to 09-07 as "another week of slip" and says nothing about the holiday. **If that call does not happen, it moves to 09-08 at the earliest and every K-1, pref-character and final-distribution item moves with it.**
- **Saturday 2026-09-05**, WP-12 legal pack per WP-37 Milestones, owner Claude, and the same day's board task T-040 remaining-assets workpaper. A Saturday deliverable that feeds D-09.
- **Tuesday 2026-09-15** is twelve days out, so outside the window, but it belongs in this list because it is the hardest clock in the file: **Onyx Holdings needs the BMHCII K-1 to file its own corporate return.** `CM-25`, VERIFIED, Tabish Rizvi 2026-09-02: "We need to process our own corporate returns by 9/15." The 2025 partnership return was still in final partner review at the accountants on 09-02.

### Is the 09-30 "archive Murad-complete" target still achievable

**No, not as defined. The reason is structural, not a question of how hard anyone works.**

**The arithmetic first.** From tomorrow, 09-04, through 09-30 inclusive there are **19 weekdays, and one is Labor Day, leaving 18 working days.** Against that: 31 checklist items with **zero complete** as of 08-30 on WP-37's own P1 line, and nothing moved in the four days since. That is one item closed every 0.58 working days, from a standing start, by someone who has not worked on a fund before.

**But effort is not the binding constraint. Five things make 09-30 unreachable regardless of who is working.**

1. **Fifteen of the 31 items are requests to parties outside the company, and not one has gone out.** D-04 and D-05 to closing counsel and title, both now under an Austin hold whose lift condition is *"the documents arriving from Chris Hoke."* D-06 to lenders on loans already paid off. D-07 to two banks on accounts that are closed. D-13, D-14, D-19, D-23 and D-24 to banks and the CPA on entities other than the fund. D-28 and D-29 to limited partners who would have to locate and re-execute six to eight year old instruments. **A checklist cannot compress a third party's response time.**
2. **The fifteen Section 6 items due 09-18 sit behind a decision that is BLOCKED with five open blockers and a target of 09-15.** If the fee framework lands on 09-15 as targeted, the documents it authorises still cannot be drafted, reviewed, countersigned by Jon, character-read by the CPA and filed by 09-18. If it slips, 09-18 slips with it.
3. **Nothing external can leave the building until the privilege question is answered.** WP-37 P7: *"Nothing external, to counsel, to the CPA, to any LP, moves without Austin plus the privilege answer at T-013 Q1."* `T-013_Counsel_Briefing_DRAFT_BMHCII_20260828.docx` is still a draft in `07_Legal_Dissolution` and has not gone to Cousineau. **Until it does, the fifteen outbound items in point 1 are not merely unstarted, they are prohibited.**
4. **D-27 cannot honestly certify what 09-30 asks it to certify.** Per section 2: the archive's filenames do not identify their contents, five files are voided-envelope artefacts, and at least one document a Murad request line points at is not in Dropbox at all. **Certifying "Murad-complete" on 09-30 against the archive as it stands would be a false written statement by the General Partner into a discoverable file.**
5. **The target's own purpose is unconfirmed.** 09-30 exists because 10-01 is Citrin fieldwork. The 08-31 digest carries **T-036, Citrin past-due balances, in the 8/21 overdue wave**, noted as *"must happen before the final K-1 engagement,"* and the 2025 return is still open at Citrin as of 09-02. **The firm the archive is being readied for has an unpaid balance and unfinished prior-year work.**

### What could actually be delivered by 09-30, per day, if work started tomorrow

- **Friday 09-04.** Finalise the three memos: produce clean execution copies with the DRAFT stamp removed, and route them to Austin for signature. **The novice's deliverable is a signature packet, not a signature.** Same day, the only genuinely urgent Austin action: send T-013 to Cousineau, because everything outbound queues behind it.
- **Tuesday 09-08** (09-07 is Labor Day). Get the T-013 Q1 privilege answer in writing. Hold the CPA call if it can be rebooked off the holiday.
- **09-08 to 09-11.** With the privilege answer in hand, issue the outbound requests that are not under hold: D-06 to lenders, D-07 to the two banks, D-13, D-14, D-19, D-23, D-24 to the CPA and banks. **Issuing the request is the deliverable; receiving the document is not inside September.** In parallel, counsel drafts the D-30 confirmatory assignment.
- **Friday 09-11.** D-08 delivered as a filtered inventory of what 4.5 actually holds by year, with 2025 marked "not yet filed, at Citrin" rather than "missing". D-25 started, because state registries and the IRS answer in days.
- **Tuesday 09-15.** The Onyx K-1 clock, and the fee framework decision or a formal statement that it is late.
- **09-18 to 09-25.** D-26 against **eleven** empty folders, not seven. D-07's Aug 2026 and forward filing, already substantially done locally. Section 6 documents only to the extent the fee decision has landed.
- **Wednesday 09-30.** **Issue a Statement of Archive Contents and Known Gaps instead of a completeness certificate.** The 09-03 audit's own grafted recommendation says exactly this: issue the signed statement at the end of the pass so it reads "here is the matrix" rather than "we cannot produce one." That is a deliverable a novice can assemble, an accountant can review and the authorized signatory can sign without asserting something untrue.

**Restate the target.** Replace 09-30 "archive Murad-complete" with **09-30 "every Murad request line has either a filed document, a signed memo, or a named gap with an owner and a date."** The first is not achievable and would be false if declared. The second is achievable in 18 working days and is the thing that actually helps if Khodara escalates or Murad's counsel moves.

---
## 4. The true dependency order

The checklist is flat. The work is not. Below is the order the work has to happen in, then the parallel lanes, then the items that are dead ends until somebody outside the company replies.

### Tier 0. Three things that must happen before anything else, and only one of them is on WP-36

**0a. Answer the privilege question, T-013 Q1, and get Austin's routing decision.** Source: WP-37 Dashboard row P7, *"CROSS-CUTTING. Nothing external, to counsel, to the CPA, to any LP, moves without Austin plus the privilege answer at T-013 Q1"*; register 6.16. **Gates D-04, D-05, D-06, D-07's two bank legs, D-13, D-14, D-19, D-23, D-24, D-28, D-29, D-30's execution leg, D-31 and T-01.** That is 15 of 31 items plus T-01 behind one unanswered question. **Not on WP-36.**

**0b. Take the SHA-256 hash manifest and pre-remediation snapshot of the Dropbox archive, stored outside the working tree.** Source: the 09-03 audit, which calls it "action one" and **"non negotiable"**, and states the risk it answers: *"renaming roughly 1,500 files while under a books and records demand can read as a party editing its own records."* **Gates every item that files, moves, renames or deletes anything in the archive: D-26, D-27, and the filing leg of all 31.** Note that WP-36's own cleanup pass already moved nine files and created three placeholder notes on 08-30 **with no manifest taken first.** **Not on WP-36.**

**0c. Audit the existing Dropbox share links, and move the three ACH authorization forms out of `1. Governing Documents`.** Source: the 09-03 audit. Three ACH forms carrying bank routing and account credentials are filed in `1.8` under names that give no warning of their contents; `1.8` is the folder handed to LPs and counsel for subscription review; *"a books and records production from that folder as it stands hands a hostile partner other investors' banking details"*; and every link already issued still points at 1.8. **Gates any sharing of Section 1 with Murad's counsel, which is exactly what D-27 certifies the archive ready for.** **Not on WP-36.**

### Tier 1. The 09-04 signature block

**1a. Finalise the three memos.** Produce clean execution copies of `WP-36-M3`, `WP-36-M1_v2` and `WP-36-M2_v2` with the DRAFT stamp removed. **No WP-36 row owns this step.** Predecessor: none. Successor: 1b.

**1b. Austin signs all three, closing D-01, D-02, D-03.** Predecessor: 1a. **D-03 is genuinely independent and can be signed and closed on its own merits**, because WP-38 section 4 supports it with three tie-outs. **D-01 and D-02 are different: each of those memos contains a document request, and the request half cannot go out until 0a.** So D-01 and D-02 each split into a signature leg, available now, and an outbound leg, behind 0a. WP-36 shows them as single items.

**1c. Delete the `_FOLDER STATUS.txt` placeholder in 2.3 once signed M3 is filed.** The note says so itself: *"This note is a placeholder and should be deleted when documents are filed."* Predecessor: 1b. Trivial, and exactly the kind of step a novice will not know to take, leaving a "documents pending" placard beside the document that answers it.

### Tier 2. The WP-38 Finding 4 chain, D-30. Strictly ordered, no step can be reordered

WP-38 section 5, "Recommended sequence":

- **2a. Produce the 2020 assignment instrument and the General Partner's written consent, and file both in folder 2.4.** Predecessor: 0a, because it is executed with an outside LP. Requires **counsel to draft**, since it is a confirmatory assignment of a partnership interest, and **Austin to sign**.
- **2b. Book the transfer into the investor register with the correct 2020 effective date and close account 1034.** Predecessor: 2a. This is an InvestNext register change, not a document.
- **2c. Restate the payee of record on every distribution made from the transfer date forward**, so the investor records, the tax records and the statement set finally agree. Predecessor: 2b. It touches every distribution 2020 through 2026 on that interest, including $312,026.55 on 2026-03-16 and $53,029.70 on 2026-06-30.
- **2d. Rerun the final statements and the distribution model off the corrected register.** Predecessor: 2c **and** 2e below.

**What 2d gates**, per WP-38 and register 2.31: the **final distribution** (WP-36 sheet2, 2026-12-12), the **final K-1 zero-out** (register 2.19), and the **Murad diligence answer on distributions**. WP-36 carries this correctly in one note on D-30, then gives the item a 09-11 date as though it were a document pull. **It is a four-step chain with counsel in step one and a register migration in steps two and three.**

- **2e. Correct the Reinisch opening basis to $37,500, and normalise the three name variants.** Register 2.35, WP-38 sections 7 and 8: Renisch / Reinisch, Stuart / Stewart Taub, Thein Quach / Quash. Predecessor: none. Successor: 2d, the final K-1 run and the final statement run. Register v58 says it plainly: 2.35 *"gates final K-1 + final statement run."* **This has no D-item anywhere on WP-36, and it sits on the critical path to the December distribution.**

### Tier 3. The Lamberton chain. One question, then three instruments

- **3a. Answer register 3.09: which cure, or did both happen at different times.** CURE A gives the Fund a 51.00% look-through to the park, CURE B gives 45.90%, *"5.1 points apart, different consents required."* Register v58's standing instruction: **"DO NOT redraft, execute or circulate WP-12a v2. DO NOT treat 11/30 as a closing date until the cure is chosen."** Owner Austin / Counsel, and **it carries no date**, which the 08-31 digest calls out as making 11/30 fictional.
- **3b. Then, and only then, the three legs.** Register 2.34 calls them *"one Lamberton chain, three legs, zero instruments"*: register 5.05, the fund-side $137,500 Bedrock I Group Class A position as the Lamberton investment funded by J315 on 2017-11-02; WP-12a, the confirmatory assignment; and **D-31**, the A2Z sponsor-side admission package.
- **3c. What 3a gates downstream.** **D-09**, because a remaining-asset schedule cannot state the fund's interest in its largest remaining asset while that interest is 5.1 points ambiguous. **The 11/30 disposition. The 12/12 final distribution. The final K-1.**

**The routing contradiction from section 2 lands here: WP-36 D-31 says this goes to counsel in the WP-12 pack; register v58, cut the same day, says it was removed from the WP-12 counsel ask and carved out to its own thread. An executor following WP-36 will put it back into a pack Austin took it out of.**

### Tier 4. Section 6, which is three different kinds of work wearing one due date

WP-36 gives D-10 through D-24 one date, 09-18, and one owner. They split three ways.

**4a. Blocked on the fee framework decision, T-007 and T-011. Five items: D-10, D-11, D-12, D-15, D-20.** Predecessors: the charge, waive or recharacterize decision on roughly $1.6M, **BLOCKED with five open blockers and a target of 09-15**; **Jon Wyss's countersignature** on the T-011 EXECUTION COPY v2; and the CPA character read. For D-20 specifically, predecessor **T-002, the PM rate at 4% versus 5%, a $221,934.48 swing, IN PROGRESS since 08-21.** **Producing a fee schedule into the archive before the decision manufactures a document the decision will contradict, inside a discoverable file.**

**4b. Blocked on the sponsor-economics papering. Four items: D-16, D-17, D-21, D-22, and D-18 belongs here too.** Predecessor: register 1.23's five sequenced actions, which include Austin signing T-012, locating an **executed** Bedrock I Group Operating Agreement (the archive copy in 1.4 is **unexecuted, blank signature lines both members**), a unanimous member consent ratifying the draw series, and posting AJE-32.1, which is itself **ON HOLD** pending the defense-cost allocation among the three named clients. D-18's own note points at WP-32 and T-011.

**4c. Independent third-party record pulls. Five items: D-13, D-14, D-19, D-23, D-24.** Entity tax returns and bank statements for Bedrock Group, the GP and Bedrock PM. Predecessor: **0a only.** These can go out the moment privilege is answered, and they are the only part of Section 6 that can move in September.

### Tier 5. What has to happen before D-27, and it is not on the sheet

**5a. Resolve name to content in `1.8`, at minimum for every document a Murad request line touches.** The 09-03 audit supplies the mechanism and it is cheap: **the upstream per-investor tree at `ns:5655481408` is the intact index, and every one of the 40 opaque vault files has a same-size counterpart under a named investor folder there.** A byte-size join plus 179 file opens produces the per-investor completeness matrix as a byproduct. Predecessor: 0b, the manifest. **Not on WP-36.**

**5b. Then D-27**, which by definition comes last, and which should be reissued as a Statement of Archive Contents and Known Gaps rather than a completeness certificate. Predecessors: everything above, plus 5a.

### What can run in parallel, starting now, with no outside party and no blocked decision

Five lanes, and they are close to the whole honest September workload for an inexperienced executor.

1. **D-08**, the 4.5 filtering job. Needs Dropbox read access and nothing else.
2. **D-25**, fund organizational documents. State registries and the IRS answer in days, and nobody has to decide anything first.
3. **D-26**, the empty 3.1 folders, scoped at **eleven** rather than seven. Needs 0b first, because it creates and moves files.
4. **D-07's Aug 2026 and forward leg**, already substantially done in the local tree.
5. **2e**, the Reinisch basis correction and the name normalisation. Internal workbook, accountant review, no outside party, **and on the critical path to December.**

Tier 1's finalisation step, 1a, also runs in parallel and takes an afternoon.

### Dead ends until an outside party responds

Ranked by how little of the clock the company controls. **Nothing on this list should carry a company-set due date**, because a date that depends on somebody who has not been asked yet is not a plan.

| Item | Waiting on | Note |
|---|---|---|
| D-04, D-05 | **Chris Hoke, Woods Oviatt** | Under an explicit Austin hold of 2026-09-03. Lift condition stated: *"the documents arriving from Chris Hoke."* The test on arrival is whether the **Valley View recorded reconveyance** of the 2018 Cornerstone deed of trust is in the set. If it is not, that is a **title defect on a fund asset**, not a binder gap. |
| D-06 | Lenders on paid-off loans | Payoff statements on closed loans. Servicer retention is the constraint. |
| D-07, two legs | GreenSpot x2488, Valley View BAML | Closed accounts. Bank retention, not effort. |
| D-13, D-24 | The CPA and the tax preparer | The same firm whose 2025 fund return is still open and which carries a past-due balance, T-036. |
| D-14, D-19, D-23 | Banks, three sponsor entities | Same retention problem as D-07. |
| D-28 | **CS Partners IV plus seven individual transferees** | Instruments six to eight years old that the 09-03 audit says never existed in reachable form. Reconstruction means asking eight parties to execute confirmatory paper. |
| D-29 | Five limited partners | Same, for the second-tranche subscriptions. And twelve more investors have no subscription agreement at all. |
| D-30, step 2a | **Counsel, plus Gregory Khodara of WCO Capital** | The counterparty threatened a state securities regulator in writing on 2026-08-24. |
| D-31 | **Counsel, and possibly the 2024 return preparer** | Register 3.09: *"what actually occurred in 2024, transaction versus preparer reclassification, ask the preparer if nothing is internal."* Also needs the 10% holder of Lamberton MHC Partners identified and consenting, and the 49% EM Lamberton GP side's position. |
| T-01 | **Citrin, plus counsel** | K-1 delivery dates, the CPA-signed waterfall representation, and counsel sign-off on distributing while an LP fraud-count suit is pending. |
| The 2026-12-31 certificate | **Counsel, T-041** | State clearance and entity standing across roughly 30 entities, "weeks-to-months lead", **not started.** This, not the archive, sets the dissolution floor. |

### The critical path to 2026-12-12, drawn out

**0a privilege answer, then 2a counsel drafts the confirmatory assignment, then Austin and Khodara execute, then 2b register booked and 1034 closed, then 2c payees restated 2020 to 2026, then 2d rerun which also requires 2e, then the final K-1 zero-out at register 2.19, then the final distribution.**

**In parallel and equally binding: 3a which cure, then 3b the three Lamberton instruments, then the 11/30 disposition, then the December waterfall.**

**Gating both: the CPA call, 13 days late and currently booked on Labor Day, then pref character at register 2.20, then the final waterfall method, then T-051 collect versus waive on $1,152,837.94.**

**None of those three chains runs through the document archive.** WP-36 is a document-completeness workstream that has been handed the calendar of a critical path it does not sit on. Say that plainly to whoever inherits it: **finishing WP-36 perfectly on 09-30 does not move 12-12 by a single day, and missing the T-013 privilege answer, the CPA call, or register 3.09 moves it by weeks.**

---
## 5. Who can actually do each item

**First, a premise correction, because the brief carries an assumption the record does not support.**

The brief says "the person originally named on the register for part of it has left the company." **WP-36 and WP-38 name no individual other than Austin Berk.** I searched both extracted workpapers for Berman, Moe, Mehmood and Bennett: **zero hits in WP-38's six pages of text and zero hits across all three WP-36 sheets.** VERIFIED, my own search. The owner column of sheet1 contains exactly four distinct values: `Austin` on 27 rows, `Claude` on 3, `Austin / Counsel` on 1, `Austin/CPA` on 1.

**The Brain reached the same conclusion independently on 2026-09-03 and withdrew the row that had asserted otherwise.** `00-Meta/audit-log.md`, dated 2026-09-03: *"`TD-0525`'s core instruction was false and is withdrawn: WP-36 and WP-38 never named David Berman. VERIFIED by string search of both extracted workpapers, zero hits."* And the consequence it drew is the right one: *"the work was never delegable in the way the row implied, because the workpaper assigns it to the authorized signatory, and much of it is either a signature or a request to an outside party."*

**What is true, and it is the harder version of the same problem.** The staffing facts sit in `00-Meta/commitments.md` `CM-16`, closed 2026-09-02, and they are worse for this checklist than a misnamed owner would have been:

- **The controller is being exited.** Target date stated 2026-08-30 as "by end of next week"; severance aligned to work completed through 2026-09-30; employment counsel (Karen Doner) engaged 2026-08-28.
- **His access was revoked on 2026-08-31, and Austin widened it: "ALL BANK ACCOUNTS."**
- **A legal hold is in place** and IT opened a forensic review of six months of email.
- **A second person inside the same accounting function was raised to counsel on 2026-08-31.**
- **`80-Finance/intercompany-arap-recon.md` assigned that controller five non-delegable roles**, including signing the entity list with EINs, and `CM-16` records that plan was written without knowledge of the exit.

**So the correct statement of the staffing problem is not "one register owner left." It is: the accounting function that bucket (b) below depends on has no available in-house body, and the people who did have the institutional memory are either exiting under a legal hold or have been referred to counsel.** Every item in bucket (b) therefore routes to the CPA, which is bucket (e), which is a firm with a past-due balance and an unfinished 2025 return.

### The classification

Bucket key. **(a)** doable by an inexperienced person following written instructions. **(b)** needs an accountant. **(c)** needs counsel. **(d)** needs Austin personally, because it is a signature or a judgement only the authorized signatory can make. **(e)** blocked on a third party.

| ID | Bucket | Why, in one line |
|---|---|---|
| D-01 | **(d)**, prep is (a) | A General Partner representation about what the partnership did, signed by the authorized signatory into a discoverable file; only the packet assembly is delegable. |
| D-02 | **(d)**, prep is (a) | Same instrument type, same signatory, and the document request inside it also needs 0a cleared first. |
| D-03 | **(d)** | Same, and it additionally asserts a negative about ten years of fund history, which nobody but the signatory can attest. |
| D-04 | **(e)** | Under an explicit Austin hold whose lift condition is documents arriving from Chris Hoke at Woods Oviatt. |
| D-05 | **(e)**, with a (b) prerequisite | The escrow agent and the qualified intermediary are not currently known, and finding them means reading the bank statements and general ledger for payments to them. |
| D-06 | **(e)**, request drafting is (a) | Payoff statements exist only at the lenders and the loans are already paid off, so retention is the constraint. |
| D-07 | **split: (a) + (e)** | The Aug 2026 and forward filing is pure clerical work; GreenSpot x2488 and Valley View BAML are requests to closed accounts at two banks. |
| D-08 | **(a) with (b) sign-off** | Inventorying 989 files by year is delegable; deciding which document is a fund-level 1065 rather than a state return or a K-1 package is not. |
| D-09 | **(b)**, blocked on 3a | Carried notes, park-owned homes and a 5.1-point ambiguity in the fund's largest remaining interest require valuation and basis judgement. |
| D-10 | **(d)** decision, then **(b)** | The fee schedule cannot be written until the charge, waive or recharacterize decision on roughly $1.6M is made by the principals. |
| D-11 | **(d)** decision, then **(b)** | Same framework decision governs whether acquisition and disposition fees were earned, waived or recharacterized. |
| D-12 | **(d)** decision, then **(b)** | Financing fee support of $790,723.20 sits inside the same undecided Batch B package. |
| D-13 | **(e)** | Bedrock Group LLC tax returns are held by the tax preparer, not by the fund. |
| D-14 | **(e)** | Bank statements for another entity's accounts, obtainable only from that bank. |
| D-15 | **(d)** decision, then **(b)** | GP fee collection support is the collect-versus-waive question on $1,152,837.94 and is a principal's decision before it is a schedule. |
| D-16 | **(b)**, with a **(c)** blocker | Fee-rollover LP positions tie to register 5.05 and to a Bedrock I Group Operating Agreement whose only archive copy is unexecuted with blank signature lines. |
| D-17 | **(b)** | Tracing amounts contributed into the LP from asset sales is a ledger reconstruction across two sets of books. |
| D-18 | **(c)**, with **(b)** support | Instruments for GP-to-fund loans are legal documents that do not exist yet and have to be drafted, not retrieved. |
| D-19 | **(e)** | GP entity bank statements, held by the bank. |
| D-20 | **(d)** decision, then **(b)** | The item states a 5% rate as fact while the 4% versus 5% question, a $221,934.48 swing, is still open. |
| D-21 | **(b)** | Use-of-proceeds support is built by tracing proceeds through the ledger, not by finding a file. |
| D-22 | **(b)** | Collections transaction detail requires a ledger extract and a judgement about what counts as a collection. |
| D-23 | **(e)** | PM entity bank statements, held by the bank. |
| D-24 | **(e)** | PM entity tax documents, held by the tax preparer. |
| D-25 | **(a)** | **The only genuinely and wholly delegable item on the sheet:** certificates, the EIN letter and good standing come from state registries and the IRS on request. |
| D-26 | **(a) with (d) sign-off** | Filing formation documents into eleven empty folders is clerical; writing "N/A" against an entity that may never have been formed is an assertion about the fund's structure. |
| D-27 | **(b) then (d)** | It is a completeness opinion over 1,513 files whose names do not match their contents, and the certificate at the end of it is the signatory's statement. **Never (a).** |
| T-01 | **(e) + (c) + (d)** | Dates depend on Citrin finishing, on counsel clearing a distribution during an LP fraud suit, and on Austin setting the date. |
| D-28 | **(c) then (e)** | Confirmatory transfer instruments, GP consents and joinders for seven transferees must be drafted by counsel and then executed by eight outside parties. |
| D-29 | **(c) then (e)**, with **(b)** on one point | Same drafting-and-execution pattern, plus an accountant to settle the character of the Forster $239,910 and $4,798 amounts. |
| D-30 | **(c) + (d) + (b) + (e)**, in that order | Counsel drafts the confirmatory assignment, Austin signs it, an accountant restates the register and six years of payees, and the transferee has to countersign. |
| D-31 | **(c)**, blocked on 3a | An admission or reallocation agreement, a consent to a percentage reduction and a consideration recital are legal instruments about who owns what. |

### The count, which is the point of this section

- **(a) wholly: 1 item of 31.** D-25.
- **(a) as a substantial share of a split item: 4 more.** D-07's forward filing, D-08's inventory, D-26's filing, and the unnumbered finalisation step 1a. Call it **five things an inexperienced person can be handed and complete.**
- **(d) requiring Austin's signature or judgement: 9 items** (D-01, D-02, D-03, D-10, D-15, D-20, D-26 sign-off, D-27 certificate, D-30 signature, plus T-01's date), and every one of them is a place where a wrong answer becomes a written General Partner representation.
- **(b) needing an accountant: 10 items**, against an accounting function with no available in-house body.
- **(c) needing counsel: 6 items**, across at least four separate counsel relationships (Cousineau on litigation, Woods Oviatt on title, dissolution counsel on T-041 and T-053, and whoever drafts the confirmatory assignments). **T-008, the Bedrock I Group consent analysis, has been READY and untouched since it was raised.**
- **(e) blocked on a third party: 12 items** plus T-01.

**Read plainly: of 31 items on a checklist about to be handed to someone with no accounting or fund experience, one can be completed by that person start to finish.** Roughly a third are requests to outside parties that cannot even be sent until the privilege question is answered, a third need an accountant the company does not currently have available, and nine end in a signature nobody but Austin can supply.

### What the handoff should actually be

The useful version of this reassignment is not "own the checklist." It is a **coordinator role with three deliverables and no authority to sign or send.**

1. **Assemble packets.** Finalise documents, build the request letters, prepare the signature packet. Never sign, never send.
2. **Maintain the status board.** Chase inside the company, record what came back, keep the eleven-folder count and the 989-file inventory honest. This is real value and it is genuinely delegable.
3. **Escalate on a fixed rule.** Anything that would go outside the company, anything that asserts a fact about the partnership, and anything where two source documents disagree goes to Austin or to counsel, not to a judgement call.

**Write that boundary down before the checklist is handed over,** because WP-36's owner column says "Austin" on 27 rows, and a reassignment that does not say which half of each row moved is a reassignment of the signature too.

---
## 6. Every instruction that would mislead a novice, and what it should say instead

Ordered by how much damage the misreading does. Each entry gives the cell, the words as written, the failure, and replacement text.

### 1. D-08 (C12, E12, H12). The known example, and it has two defects rather than one

**As written:** needed item "Verify fund-level 1065 returns present for every year 2018 to 2025 (K-1 sets confirmed present 8/30)"; status "Verify"; note "Census counted K-1 folders; fund return presence not yet verified file-by-file."

**Why it misleads.** (i) "Verify present" against a folder the reader will assume is small. `4.5 Tax Returns` holds **989 files**. This is a filtering job, not a hunt, and a novice who searches for eight files in a thousand-file folder and finds three will report five years missing. (ii) **The 2025 fund return does not exist yet.** It was still in final partner review at the accountants on 2026-09-02. The instruction asks for verification of a document that has not been filed, so the honest result of following it is a false gap report.

**Should say:** *"Inventory `4. Fund Level/4.5 Tax Returns` (989 files) and produce a one-row-per-year table for 2018 to 2025 showing, for each year: whether a complete fund-level Form 1065 is present, its filename, and its page count. Do not report a year as missing until an accountant has confirmed the document you found is a fund return and not a state return, a K-1 package, or a draft. **2025 is expected to be absent: the 2025 partnership return was still in final partner review at Citrin as of 2026-09-02. Record it as 'not yet filed, at Citrin' rather than 'missing'.** Deliverable is the table, not a yes or no."*

### 2. D-27 (C31). The instruction that would produce a false certificate

**As written:** "Final QC sweep: map every Murad line to a filed document or signed memo; certify archive Murad-complete."

**Why it misleads.** It presumes a filename identifies its contents. In the archive's most sensitive folder that presumption is false in roughly two dozen confirmed cases: `Thien_Quach_-_Bedrock_MHC_Fund_II.pdf` is Michael Mitchell's accreditation letter, `MIchael Mitchell_Accreditation.pdf` is Khodara's subscription package, `Bedrock MHC Fund II LP Limited Partnership A&R.pdf` is the unexecuted First Amendment with four blank signature lines. Five files are artefacts of a **voided** DocuSign envelope. And at least one document a Murad line points at, the 2026-05-08 LP Summary, is not in Dropbox at all. **A novice mapping request lines to filenames will produce a certificate that says the archive is complete when it is not, signed by the General Partner, into a file a partner's counsel has subpoenaed.**

**Should say:** *"Produce a Statement of Archive Contents and Known Gaps. One row per Murad request line, and for each row: the filed document by path, or the signed memo by path, or a named gap with an owner and a target date. **A row may only cite a document that has been opened and confirmed to be what its filename says.** Do not certify completeness. Do not cite any file from the voided-envelope set. Where a request line has no document, the row says so, with the owner. This statement is reviewed by an accountant and signed by Austin."*

### 3. D-01 and D-02 (E5, E6, H5, H6). "Superseded, replaced" describes the wrong document

**As written:** status "Superseded, replaced"; note "Sign WP-36-M1 v2 (transfer register + document request) instead."

**Why it misleads.** The status describes the document nobody may touch. It gives no location, no filename and no warning that the withdrawn versions are sitting two folders away in `Archive_Superseded` looking like signable PDFs, or that the replacement is still stamped DRAFT.

**Should say, for D-01:** *"SIGNATURE PACKET, Austin only. Sign `2. Investor Records/2.4 Transfer-Assignment Documentation/WP-36-M1_v2_Transfer Register and Document Request`. Before signature, produce a clean execution copy with the DRAFT stamp removed. **DO NOT sign anything in `2. Investor Records/Archive_Superseded`. The two files there assert that no transfers occurred, which the fund's own ledger and its filed 2022 K-1 set disprove, and their own cover note reads 'Do not sign, circulate or rely on'.** The document request inside this memo does not go out until the T-013 privilege question is answered."* Same pattern for D-02 against 2.5 and M2 v2.

### 4. D-04 and D-05 (H8, H9). Instructions to chase a party who is under a hold

**As written:** H8 "9-park seller-financed portfolio; pull from closing counsel/title co"; H9 "Request from title/escrow agent."

**Why it misleads.** Austin placed a hold on exactly these items on 2026-09-03 with the words *"Chris is getting the documents together. anything needed can be held until we get those and reassess,"* and the Brain records "nothing opens on these and nothing chases Hoke." A novice following H8 chases the counsel Austin told the company not to chase. Separately, H9 names an "escrow agent" that nobody has identified.

**Should say, D-04:** *"HELD by Austin, 2026-09-03. Do not contact Woods Oviatt or Chris Hoke. The hold lifts when Hoke delivers. On delivery, the first test is whether the **Valley View recorded reconveyance of the 2018 Cornerstone deed of trust** is in the set; if it is not, escalate immediately, because that is a possible unreleased 2018 deed of trust on a fund asset, not a binder gap."* **D-05:** *"Step zero: identify the escrow agent and the qualified intermediary by searching the fund bank statements and general ledger for payments to title agents and to a QI. Nobody currently knows who they were. You cannot request a ledger from an agent you have not named."*

### 5. D-20 (C24). The instruction contains the answer to an open question

**As written:** "PM fee support (5% of revenue per asset)."

**Why it misleads.** The 4% versus 5% question is open, worth $221,934.48, and in progress since 2026-08-21. A novice will build support for 5% and the archive will then hold a document contradicting whatever gets decided.

**Should say:** *"BLOCKED pending T-002, the property management rate decision, 4% versus 5%, a $221,934.48 swing. Do not produce fee support until the rate is decided and countersigned. When it is, the deliverable is the fee support at the decided rate, with the decision memo filed alongside it."* The same blocked-pending wording belongs on D-10, D-11, D-12 and D-15 against the T-007 fee framework.

### 6. D-26 (C30). The scope is understated by four folders

**As written:** "Resolve 7 empty entity folders in 3.1 (POH entities: ...)" with seven named.

**Why it misleads.** The 2026-09-03 listing found **eleven** empty entity folders in 3.1, plus one empty property bank account folder in 4.2. A novice will work the seven named, close the item, and D-27 will certify a section that still has four empty folders in it.

**Should say:** *"Resolve every empty sub-folder in `3. Property Level/3.1`. The 2026-09-03 listing counted **eleven**, not the seven named here; list them yourself before starting and reconcile your count to that listing. There is also one empty property bank account folder in `4.2`, Cedar Grove. For each folder, either file the formation documents or write a dated note explaining why none exist. **A note asserting that an entity was never formed needs Austin's sign-off, because it is a statement about the fund's structure.**"*

### 7. D-30 (H35). The priority and the counterparty are both understated

**As written:** the note is accurate on the mechanics and says "Blocks the final distribution and the final statement rerun until the register is corrected," with a due date of 2026-09-11 and a status of "Open" identical to fourteen other rows.

**Why it misleads.** Nothing on the row tells the reader that the counterparty is **Gregory Khodara of WCO Capital, who on 2026-08-24 threatened in writing to escalate to a state securities regulator**, that Austin promised him a written reconciliation on 2026-08-16 that has not been delivered, or that this is the highest-consequence single item on the entire sheet. It also presents a four-step sequence as a document pull.

**Should say:** *"HIGHEST PRIORITY ON THIS SHEET. Four steps, strictly in order, per WP-38 section 5: (a) counsel drafts the 2020 confirmatory assignment and the GP written consent, Austin signs, file both in 2.4; (b) book the transfer into the investor register at the 2020 effective date and close account 1034; (c) restate the payee of record on every distribution on this interest from the 2020 transfer date forward, including $312,026.55 on 2026-03-16; (d) rerun the final statements and distribution model off the corrected register, which also requires register 2.35 fixed first. **The transferee's principal has threatened a state securities regulator in writing (2026-08-24) and is owed a written reconciliation promised 2026-08-16. Everything touching this party goes through Austin and counsel.** This chain gates the 2026-12-12 final distribution, the final K-1 zero-out at register 2.19, and the Murad distributions answer."*

### 8. D-31 (H36). Routes work into a pack it was removed from

**As written:** "Resolve with 5.05 and WP-12a as one Lamberton chain. Goes to counsel in the WP-12 pack."

**Why it misleads.** Register v58, cut the same day, records the Lamberton structure question as carved out to its own thread and **"removed from the WP-12 counsel ask,"** with the standing instruction *"DO NOT redraft, execute or circulate WP-12a v2."*

**Should say:** *"BLOCKED on register 3.09. The Lamberton structure question must be answered first: CURE A gives the Fund 51.00% look-through, CURE B gives 45.90%, and they require different consents. This item was **removed from the WP-12 counsel pack** on 2026-08-30 and runs as its own thread; the scoping brief is `07_Legal_Dissolution/WP-12a_SCOPING_Open_Questions_20260830.pdf`. **Do not redraft, execute or circulate WP-12a v2.** When the cure is chosen, this item is the sponsor-side leg of three."*

### 9. D-03 (C7). The memo's supportable claim is narrower than the folder suggests

**As written:** "Capital call notices OR signed no-activity memo (folder holds only 2019 Closing Letter)."

**Why it misleads.** Two ways. The parenthetical is already stale: the 2019 Closing Letter was refiled out of 2.3 into 2.5 on 2026-08-30 by the same workbook's move log, so the folder no longer holds it. And a novice reading "no-activity memo" will draft or sign a memo saying the folder is empty. WP-38 is explicit that the memo must say the fund **had** the power to call capital, under a PPM Commitment Period with a seven day notice mechanic and an Investor Default remedy, and **never exercised it**.

**Should say:** *"Sign `2.3 Capital Call Notices/WP-36-M3`. The memo must state that the PPM provided a drawdown mechanic which the General Partner never exercised, supported by three tie-outs: the subscription booklet funds the entire commitment on acceptance; Position Value equals Contribution Amount on all 68 Class A positions totalling $12,589,708; and no call, drawdown or contribution-notice transaction appears in 2,128 rows of activity from 2017 to 2026. **It must not say the folder is simply empty.** The 2019 Closing Letter was moved out of 2.3 to 2.5 on 2026-08-30; that parenthetical is stale."*

### 10. D-28 (C33). Three document types named, five actually absent

**As written:** "Assignment or transfer instrument, GP written consent, and transferee joinder for each of the seven 1/1/2022 CS Partners IV transferees."

**Why it misleads.** The 2026-09-03 audit found the seven have **no subscription agreement, joinder, LP counterpart, accreditation or transfer instrument anywhere reachable.** A novice who collects three document types will close the item leaving two classes absent for seven partners holding $287,500.

**Should say:** *"For each of accounts 1063 through 1069, five document classes are absent and all five are needed: transfer or assignment instrument, GP written consent, transferee joinder or subscription, LP counterpart signature page, and accreditation. None exists in reachable form, so these must be drafted as confirmatory instruments by counsel and executed by CS Partners IV plus seven individuals. This is a drafting-and-execution project across eight outside parties, not a retrieval."*

### 11. The memo names, across six cells

**As written:** sheet1 C5 and C6 say "WP-33-M1" and "WP-33-M2"; sheet1 H5 and H6 and sheet3 rows 15 and 16 say "WP-36-M1" and "WP-36-M2"; sheet3 row 14 says "WP-33-M1/M2".

**Why it misleads.** A novice searching the archive for WP-33-M1 finds nothing. The files that exist are named `WP-36-M1_v2_Transfer Register and Document Request_DRAFT.pdf` and `WP-36-M2_v2_Additional Subscription Schedule and Document Request_DRAFT.pdf`.

**Should say:** use WP-36-M1, WP-36-M2 and WP-36-M3 throughout, and add the full filename and folder path to each of D-01, D-02 and D-03. **Naming is another agent's lane; this entry records only the operational consequence.**

### 12. What is not written anywhere on WP-36 and should be, in one block at the top of the sheet

- **There is active litigation and the Fund is a named client.** Register 6.16, opened 2026-08-28. **Nothing external, to counsel, to the CPA, or to any limited partner, moves without Austin plus the answer to T-013 Q1.** Assume full discovery of the wind-down file.
- **Take the SHA-256 manifest before touching a file.** The archive is under a books and records demand. Renaming or moving files without a prior manifest is the single act most likely to be read as a party editing its own records.
- **Three ACH forms carrying bank routing and account numbers are filed in `1. Governing Documents`.** Do not share Section 1 with anyone until they have been moved to a restricted folder and the existing share links have been audited.
- **A filename in this archive is not evidence of what the file is.** Open it.
- **Register 2.35 and register 3.09 have no D-item and both gate December.** Add them.

---
## 7. Contradictions between the sources, recorded rather than reconciled

Nine, in descending order of consequence. None of these is smoothed over anywhere else in this note.

| # | The contradiction | Sources | Label |
|---|---|---|---|
| 1 | **WP-36 contains no reference to the litigation the Fund is a named client in**, though register 6.16 was opened 2026-08-28, two days before WP-36 was written, and WP-37 of the same date makes P7 cross-cutting over everything external. | WP-36 all three sheets, zero hits; register v58 item 6.16; WP-37 Dashboard row P7 | VERIFIED |
| 2 | **D-31 routes the A2Z item into the WP-12 counsel pack; register v58 of the same date says it was removed from that pack and carved to its own thread**, with "DO NOT redraft, execute or circulate WP-12a v2." | WP-36 sheet1 H36; register v58 header and items 2.34 and 3.09 | VERIFIED |
| 3 | **D-26 says seven empty entity folders in 3.1; the 2026-09-03 listing says eleven**, plus one empty property bank account folder in 4.2. | WP-36 sheet1 C30; `bmhcii-archive-audit-2026-09-03.md` | VERIFIED, two dated sources disagree |
| 4 | **D-04 and D-05 tell the executor to pull from closing counsel and title on 09-11; Austin placed those exact items on hold on 09-03** and instructed that nothing chases Hoke. | WP-36 sheet1 H8 and H9; Austin quoted 2026-09-03 on `bedrock-fund-ii-winddown.md` | SINGLE-SOURCE on the hold, Austin quoted |
| 5 | **D-08 asks for verification that the 2025 fund return is present; the 2025 return was still in final partner review at the accountants on 09-02** and therefore cannot be in the archive. | WP-36 sheet1 C12; `WP-15b_LP_Note_2025_K1_Status_20260902.docx` | VERIFIED |
| 6 | **WP-38 cites register v56 as carrying items 2.31 to 2.35; v56 was cut and superseded the same day for omitting the litigation item, and no v56 exists in `09_Issue_Register`** (v55, v57 and v58 are present). | WP-38 section 9; register v58 header; local directory listing | VERIFIED |
| 7 | **The same two memos are called WP-33-M1/M2 in three cells and WP-36-M1/M2 in three others, inside one workbook**, and the files that actually exist use the WP-36 form with a `_v2` suffix. | WP-36 sheet1 C5, C6, H5, H6; sheet3 rows 14, 15, 16; the 2026-09-03 Dropbox listing | VERIFIED |
| 8 | **WP-36's move log records the creation and withdrawal of the v1 memos but never records the creation of M3, M1 v2 or M2 v2**, which nonetheless exist on Dropbox. So the three documents about to become executed GP representations have no recorded chain of custody. | WP-36 sheet3 rows 14 to 16; the 2026-09-03 Dropbox listing | VERIFIED as an omission |
| 9 | **The Brain's audit-log row of 2026-09-03 states WP-36's owner column reads "Claude on 4"; the file says 3.** | `00-Meta/audit-log.md`; WP-36 sheet1 column F, counted cell by cell | VERIFIED, minor |

**A tenth, which is a labelling problem rather than a disagreement.** Register v58's own header text describes the file as "This v57 is the merge." WP-37 designates the register as the single source of truth for item status. An executor asked to check a register item will not know which file is current.

## What was tested, and what was not

**Tested and confirmed from reachable sources:** that nothing has moved on any WP-36 item since 2026-08-30 (local `find` over 3,851 files, corroborated by the 08-31 digest and WP-37's own P1 count); the full contents of all three WP-36 sheets; the full text of WP-38; the milestone weekday arithmetic including Labor Day; the absence of any named individual other than Austin in either workpaper; the absence of register v56 locally; the existence and dates of the WP-39 to WP-41 and WP-15b work products; the register v58 text of items 1.23, 2.31 to 2.35, 3.09, 4.17 and 6.16; and the WP-37 Dashboard and Milestones tabs in full.

**Tested only through a secondary source, and labelled as such throughout:** the contents of the Dropbox archive `/Austin Berk/BMHCII`, including the existence and DRAFT status of the three memos, the 989-file count in 4.5, the eleven empty folders in 3.1, the empty Cedar Grove folder, the filename-to-content failures in 1.8, and the three ACH forms. **The source is the fourteen agent audit's own listings of 2026-09-03**, which is a dated listing rather than an inference, but it is not this session opening the folder.

**Not tested at all, and not asserted:** whether any signature has been applied inside Dropbox since 2026-09-03; whether the T-013 privilege question has been answered since the WP-37 cut of 2026-08-30; whether the CPA call was rebooked off Labor Day; whether Citrin's 10-01 fieldwork date is still committed; and the contents of Box, InvestNext, the Murad Dropbox Space and the MickLaw DDQ tree, which the 09-03 audit records as never reached.

**What would test the untested.** Open `/Austin Berk/BMHCII/2. Investor Records/2.3`, `/2.4` and `/2.5` and read the signature blocks of the three memos. Open `/4. Fund Level/4.5` and list by year. Count the sub-folders of `/3. Property Level/3.1` and note which are empty. Ask Austin one question: has T-013 gone to Cousineau, and what is the answer to Q1.

## Sources

- `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\12_Document_Archive\WP-36_Document Archive Needed Items + Timeline.xlsx`, sheets 1, 2 and 3, cells cited inline.
- `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\12_Document_Archive\WP-38_Investor_Records_Integrity_Review_v3_20260830.pdf`, sections 1 to 9.
- `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\00_Governance\WP-37_Workstream_Tracker_BMHCII_20260830.xlsx`, Dashboard and Milestones tabs.
- `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\09_Issue_Register\WP-Issue_Register_BMHCII_v58.xlsx`, Issue Register tab, items 1.23, 2.31, 2.32, 2.33, 2.34, 2.35, 3.09, 4.17, 6.16 and the header note.
- `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\08_Communications\WP-00b_Weekly_Internal_Digest_BMHCII_20260831.docx`.
- `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\08_Communications\WP-15b_LP_Note_2025_K1_Status_20260902.docx`.
- `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\07_Legal_Dissolution\` directory listing, including `T-013_Counsel_Briefing_DRAFT_BMHCII_20260828.docx` and `WP-12a_SCOPING_Open_Questions_20260830.pdf`.
- `C:\Users\AustinBerk\Documents\Claude\Projects\Close It Down\` full recursive listing, 3,851 files across 438 directories, and a modification-time filter for 2026-08-31 onward.
- `C:\Users\AustinBerk\Documents\My Brain\80-Finance\fund-reporting\bmhcii-archive-audit-2026-09-03.md`.
- `C:\Users\AustinBerk\Documents\My Brain\80-Finance\fund-reporting\bedrock-fund-ii-winddown.md`, in particular the Hoke hold section and the `_DRAFT` file list.
- `C:\Users\AustinBerk\Documents\My Brain\00-Meta\commitments.md`, `CM-16`, `CM-25`, `CM-26`.
- `C:\Users\AustinBerk\Documents\My Brain\00-Meta\audit-log.md`, rows dated 2026-08-31 through 2026-09-03.
- `C:\Users\AustinBerk\Documents\My Brain\00-Meta\owner-list-for-review.md`.

**Not reachable from this session, named so the gap is explicit:** the Dropbox namespace `/Austin Berk/BMHCII` and namespace `ns:5655481408`; InvestNext; Box; the Murad Dropbox Space created 2026-05-13; and the MickLaw DDQ tree.
