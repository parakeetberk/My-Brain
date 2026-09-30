---
name: projects
type: register
status: open
---

# Capex and infill projects, the ledger

**What this is:** every capex and infill project that has been kicked off or closed out, one row each, with the dates. Austin's instruction, 2026-08-31: kickoffs are projects getting started, closeouts are projects completed, and in time a completed project carries an analysis of whether it landed in or out of budget and on or off timeline.

**Status:** opened 2026-08-31. Seeded, not backfilled. Coverage and its limits are stated below, honestly. **Updated 2026-09-22 by the Page Update: nine more documents pending in For Signature since 2026-09-18, listed under the ledger with the closes' community expansions corrected against the hot sheet codes.** **Updated 2026-09-15 by the Page Update: fourteen documents moved through For Signature between 2026-09-09 and 09-15 and none had reached this ledger**; they are listed under *Not yet extracted* with their community resolved where a register states it. No PDF has been opened, so no row has been added to the table.

## This is a ledger, not a sixth register

The five registers in [[CLAUDE]] hold **open items**: things owed, things waiting, things unowned. A project that finished on budget is not an open item, it is a **record**, and records belong in a ledger the way decisions belong in the decisions log and figures belong in the numbers ledger. Nothing here competes with the five. A project that goes wrong produces a row in whichever register owns the problem; the project itself stays here either way.

**It is also the project-level extension of `00-Meta/numbers-ledger.md`**, on the same precedent that page already sets for `60-Communities/portfolio`: project costs live here with their source and date, and are not restated elsewhere.

## The join key, and why this works at all

**A kickoff and its closeout share the document number.** `LUCK_CAPEX_KICKOFF_17178` and `LUCK_CAPEX_CLOSEOUT_17178` are the same project at two ends of its life. That number is the project ID, and it is what makes budget-versus-actual and planned-versus-actual possible without anyone keying anything in.

**INFERRED**, from one confirmed pair: Lucky Clover 17178, kickoff requested 2026-08-25 and closeout completed 2026-08-31. Every other document seen so far has only one end of the pair in the last 90 days of mail. Confirm on the next matched pair and upgrade this to VERIFIED.

**Naming:** `CODE_TYPE_NUMBER`. TYPE is `CAPEX_KICKOFF`, `CAPEX_CLOSEOUT`, `INFILL_KICKOFF`, `INFILL_CLOSEOUT` or `CHANGEORDER`. One exception already exists: `VO_INFILL_KICKOFF_MULTI` carries `MULTI` instead of a number, so it has no join key and no closeout can ever be matched to it.

## The ledger

**All eight documents from the 2026-08-31 batch extracted in full from their signed PDFs. VERIFIED**, every field read off the document.

| Project | Community | Doc | Project name | Lead | Contractor | Budget allocation | Estimate | Final invoice | Target completion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **11055** | [[60-Communities/lake-saunders]] | CAPEX KICKOFF | Retaining wall, 120 LF vinyl seawall | John Clark | All American Site Services | **$30,000.00** | **$48,000.00** | - | 2026-11-24 |
| **17011** | [[60-Communities/su-rene]] | CAPEX KICKOFF | Retaining wall | John Clark | All American Site Services | none, UNPLANNED | **$40,700.00** | - | 2026-11-05 |
| **16996** | [[60-Communities/sea-shells]] | INFILL KICKOFF | Lot 284 demo, 7521 N. Atlantic Ave | John Clark | Champion Home Builders, Chris Miller | none, INFILL | **$9,351.42** | - | 2026-11-26 |
| **17386** | [[60-Communities/palm-haven-estates]] | CAPEX KICKOFF | Lot S, 200 amp electrical service | John Clark | Hiller LLC, Jason Bratcher | none, UNPLANNED | **$7,546.50** | - | 2026-11-29 |
| **17285** | [[60-Communities/royal-oaks-mhc]] | CAPEX KICKOFF | Lift station motor and pump replacement | Natalie Magurne | U.S. Water Services, Chad Hughes | none, UNPLANNED | **$6,648.49** | - | 2026-11-28 |
| **15603** | [[60-Communities/whispering-pines-mh-fl]] | CAPEX CLOSEOUT | Lot 5015 and 5025 electrical pedestal | John Clark | Michaels Lighting and Electric | none, UNPLANNED | **$9,901.90** | **$4,950.95** plus **$4,950.95** deposit | - |
| **17021** | [[60-Communities/applegate-mhc]] | CAPEX CLOSEOUT | Meter box replacement | Natalie Magurne | High Pace Construction FL | none, UNPLANNED | **$3,789.00** | **field left blank** | - |
| **17178** | [[60-Communities/lucky-clover]] | CAPEX CLOSEOUT | Underground water leak | Natalie Magurne | 1 Tom Plumber | none, UNPLANNED | **$3,120.00** | **$3,120.00** | - |

All eight created by Vladimir Baga. All eight approved by Austin between **11:29 and 11:32 ET on 2026-08-31**, and by Jon between 11:32 and 11:41.

### Facts from the documents

**1. Lake Saunders 11055 was approved at $48,000 against a $30,000 budget allocation.** It is the only one of the eight carrying a real budget allocation, and it is the only one marked **PLANNED**. The estimate exceeds the allocation by **$18,000, sixty percent over**, on the face of the document. Every signatory including Austin and Jon approved it. The document states both numbers on the same page.

**2. The other seven carry no budget allocation at all.** Six read `UNPLANNED, NO BUDGET ALLOCATION` and one reads `INFILL, NO BUDGET ALLOCATION`. Seven of eight capex approvals in one batch had nothing to be measured against.

**3. The document number is the Rent Manager Service Manager issue ID.** Every document links to `https://bedg.rmx.rentmanager.com/#/servicemanagerissues/<number>/details`. **This is the join into Rent Manager, and it is a service issue, not a GL account.**

**4. Variance needs neither Rent Manager nor the kickoff.** The closeout form carries ESTIMATED QUOTATION and FINAL INVOICE on the same page.

**5. The final-invoice field is the last payment, not the project total.** Whispering Pines 15603: estimate $9,901.90, deposit invoice $4,950.95, final invoice $4,950.95. The two invoices sum to the estimate exactly. Read naively that project reports as fifty percent under budget when it landed on it.

**6. Applegate 17021 was signed as a closeout by all six signatories with the final invoice amount blank**, while its own document checklist lists `final Invoice - Invoice Detail.pdf`.

**7. Two of the three closeouts show Project Implementation as "In progress"**: 17021 and 15603.

**8. The Assigned GL Code field is empty on all five kickoffs.** Four are blank, one reads `---`. But a five-digit number in the same range as the closeout GL codes appears elsewhere in each kickoff's text, adjacent to the estimate or the project links: **17386 carries 16987, 17011 carries 16954, 17285 carries 16986, 16996 carries 16858, 11055 carries 16976.** The three closeouts print theirs in the field properly: 16971, 16961, 16741. **Whether the stray kickoff number is the same field rendering out of position is unresolved and should not be assumed.** Separately, none of those codes appears in the Rent Manager chart of accounts pulled live the same day, where the 16xxx band runs 16000 to 16304.

**9. Two of the five kickoffs are the same project type from the same contractor.** Su Rene 17011 and Lake Saunders 11055 are both named RETAINING WALL, both from All American Site Services, and both describe seawall work. Su Rene is UNPLANNED at $40,700 with no allocation; Lake Saunders is PLANNED at $48,000 against $30,000. Su Rene's exclusions list "Retaining walls or screen walls" while the project is named Retaining Wall; Lake Saunders words the same exclusion as "No Retaining Walls or Screen Walls (other than the vinyl seawall)."

**10. Every kickoff sets target completion exactly three months after kickoff**, and every one reads Implementation: TBD. 11055 Aug 24 to Nov 24, 16996 Aug 26 to Nov 26, 17285 Aug 28 to Nov 28, 17386 Aug 29 to Nov 29, 17011 Aug 5 to Nov 5.

**11. Su Rene 17011 sat 26 days between creation and completion**, created 2026-08-05 and finished 2026-08-31. Jon queried the $40k on 2026-08-11. It was approved at $40,700.00.

### Not yet extracted

Ten documents are known from mail metadata but their PDFs have not been read: closeouts 15073 Shady Acres and 8760 Riverwalk, kickoffs 6681 and 16881 Belle Haven, 15063 Sea Shells and MULTI Vantage Oaks infill, all completed 2026-07-29; 17188 Vantage Oaks, approved 2026-08-21; and the three closeouts with no completion notice, 15026 Gulf Breeze, 11127 Southgate and 15040 Royal Palm, which have no signed PDF to read.

**September 2026, added 2026-09-15 by the Page Update, fourteen more.** All known from For Signature folder metadata read by the daily closes and the morning briefs; **no PDF opened, so no amount, contractor or project name is asserted for any of them**, per the open-the-file rule. Two are complete: `PPH_CAPEX_CLOSEOUT_15706` and `VO_INFILL_CHANGEORDER_MULTI`, both `Completed:` notices at 16:34 and 16:36 ET on 2026-09-09 (Vantage Oaks VERIFIED for VO; PPH unresolved). Twelve were approval requests that sat in Austin's queue, 19 messages and 18 unread at the 2026-09-14 close, and the folder read **0 items at 17:36 ET on 2026-09-15**, which says they cleared his row and nothing about Jon's, who signs last. Kickoffs: `DO_CAPEX_KICKOFF_17482` Druid Oaks (VERIFIED, `TD-0649`), `RO_CAPEX_KICKOFF_6675` Royal Oaks (VERIFIED, `TD-0646`), `OBOPO_CAPEX_KICKOFF_17483` Ormond Beach Oasis (INFERRED from the prefix), `SO_CAPEX_KICKOFF_15043` (prefix unresolved; Southgate uses `SOUTH`). Closeouts: `BELL_CAPEX_CLOSEOUT_13824` Belle Haven (INFERRED), `TRADE_CAPEX_CLOSEOUT_15047` Tradewinds (INFERRED), `CARL_CAPEX_CLOSEOUT_15020` Carley's (INFERRED), `RW_CAPEX_CLOSEOUT_15778` Riverwalk (INFERRED), `GO_CAPEX_CLOSEOUT_11181` and `GO_CAPEX_CLOSEOUT_16518` (prefix unresolved between Great Oak and Greene Pointe), `OAK_CAPEX_CLOSEOUT_15033` (prefix unresolved between Oakside and The Oaks). **A prefix table would turn nine INFERRED or unresolved readings into VERIFIED ones**; the community naming standard on `10-Business/sharepoint/community-naming-standard` does not carry the Adobe Sign codes. Also seen: `PL_INFILL_CHANGEORDER_MULTI` on 2026-09-09 and, at Hunter Springs, a High Pace rehab kickoff Jon said would go out 2026-09-15 that had not reached the folder by 18:05 ET (`TD-0662`).
**September 2026, second batch, added 2026-09-22 by the Page Update: nine more, all still pending.** The folder went from zero for three straight days to nine documents on 2026-09-18 between 12:08 and 14:31 ET, and by the 2026-09-21 close stood at **34 items, all unread, the same nine documents on day four of daily Adobe reminders, not one with a `Completed:` or `Canceled` notice.** Jon signs last and was at sea until midweek. **No PDF opened, so no amount, contractor or project name is asserted for any of them**, same rule as the batch above. The codes, with the community each prefix resolves to on this vault's own hot sheet codes (`60-Communities/*.md` header lines), every reading INFERRED from the prefix: `SS_CAPEX_KICKOFF_11132` Sea Shells (`SS`); `SSS_CAPEX_CLOSEOUT_16839` prefix unresolved, Sea Shells is `SS`; `WIND_CAPEX_KICKOFF_17607` Windward Knoll (`WIND`); `VO_CAPEX_CLOSEOUT_6935` Vantage Oaks (`VO`, the one prefix VERIFIED in the batch above); `OBOPO_CAPEX_CLOSEOUT_15035` Ormond Beach Oasis, as the batch above read `OBOPO`, though the hot sheet code is `POOBO`; `RW_INFILL_KICKOFF_16161` and `RW_INFILL_KICKOFF_16829` Riverwalk (`RW`, the code the lot sheets `60-Communities/lots/RW-*.md` carry); `TRADE_INFILL_KICKOFF_16823` Tradewinds (`TRADE`); and `FDEP Wastewater Clearance Brevard`, an environmental clearance rather than a capex document, Gunster on the Brevard thread. **A correction to the closes, kept with dates rather than smoothed over:** the 2026-09-18, 09-19 and 09-21 closes expanded these prefixes as *Windmill*, *Valley Oaks*, *Orange Blossom* and *Rolling Wood*. **No community by any of those names exists in this vault**; the codes are what the folder carries and this page reads them against the hot sheet codes instead. The prefix table asked for on 2026-09-15 is still the fix, and it is still not built.

## What this cannot yet tell you, and what would fix it

**Superseded 2026-08-31 by the extraction above.** This section previously said no cost, vendor, scope or GL code had been extracted, and that no planned completion date existed anywhere. Both were true when written and both are now wrong: the signed PDF attached to every `Completed:` notice can be read directly through the mail connector, and it carries all of it including a target completion date. The kept lesson is the narrower one: **do not treat an empty cell as a zero.** Applegate 17021's blank final invoice is a document that was signed without the number, not a project that cost nothing.

**How to extract one.** Find the `Completed:` email, read the message to get its attachment URI, then read that URI with `startPage` 1 to 2. Pages 1 and 2 carry every field; the rest is photos and the Adobe audit trail.

**Three better sources exist than email archaeology:**

1. **Adobe Sign's own report.** Every agreement with its dates and status, which is what this ledger is rebuilding one email at a time. Email search is relevance-ranked and noisy; this run had Rent Manager CSVs outranking capex documents on a literal document-name query.
2. **`CapEx Overview - REDO OF CAPEX PLAN.xlsx`** in `80-Finance/planning/2026-executive-strategy`. The plan side.
3. **Rent Manager.** See the section below. Austin raised it and it is the right instinct, but the chart of accounts does not hold what the idea assumes.

## Rent Manager, tested live 2026-08-31

Austin, 2026-08-31: *"since they all have WIP accounts then we should be able to run the analysis when the MCP to Rent Manager is back up and running."*

**The connector is back up.** It returned HTTP 500 on every call earlier today; `list_reports`, `list_entities` and `BudgetCompare` all returned this evening. **VERIFIED.**

**There is no WIP account.** The chart of accounts has no account named WIP, work in progress, or construction in progress. What exists instead is two separate bands:

- **94xxx `Capital Expenditures`**, type NonOperatingExpense. Eleven live categories: Signage, MH Purchase, Lot Update Electrical, Lot Update Plumbing, Road Repairs, Water Meter Installation, Water Line Improvements, Electrical Pedestal Improvements, Other Structures, Tree Trimming, Lot Update Pad Repairs, Septic Pumping. **This band carries a capex budget of $715,976.07** for the tested period.
- **16xxx `Long Term Assets`**, type FixedAsset. Where capitalised work lands.

**VERIFIED** against `list_entities` GLAccounts, with one caveat: the call returned exactly 1,000 accounts, which looks like a cap, so an account beyond it would not have been seen.

**The problem this exposes, and it is the real one.** Actuals in the 94xxx band read **zero for August** while the budget sits at $715,976.07. Either capex spend is being capitalised straight into 16xxx rather than expensed through the budgeted accounts, or the test run's second period defaulted wrongly. **Not resolved. Needs one clean run with both period pairs set explicitly before anyone concludes anything.** Budget and actual sitting in different account bands would mean budget-versus-actual does not currently compute inside Rent Manager at all, which would be worth knowing.

**The join problem is separate and harder.** The general ledger is organised by **account and property**. Nothing in it carries an Adobe Sign document number. So even with the connector fully healthy, Rent Manager gives **category-level variance per property**, not per-project. Tying $12,658.25 of manhole repair to VO 17188 specifically needs the project number on the transaction, in a job code, a reference field or a memo. Whether that exists is untested, because `GeneralLedger` (report 51) still returns **HTTP 500** on both single and multiple GL accounts, so transaction detail is unreachable. That report is the blocker for per-project analysis.

**And the GL code on the kickoff documents does not resolve.** Jon queried VO 17188 on 2026-08-21 because its GL read 59014 against "the 16xxx pattern every other doc uses." **There is no 59xxx band in the chart of accounts.** The reference prefixes run 50, 51, 52, 53 and then jump to 60. So 59014 is not an unusual code, it is a code pointing at no account that appears in the chart. That escalates Jon's question and it is still unanswered as of today.

### What has to be true before variance analysis runs

1. `GeneralLedger` stops returning HTTP 500, so transactions can be read.
2. A transaction-level field is found that carries the project number, or the company accepts category-level variance per property instead of per-project.
3. The 94xxx zero-actuals question is resolved with a clean two-period run.
4. GL coding on the kickoff documents is standardised, starting with what 59014 was meant to be.

## Signals already visible in one month of documents

Recorded because they are the kind of thing this ledger exists to make visible, and all three came out of building it.

- **Approvals arrive in batches and clear in minutes.** Eight documents landed on 2026-08-31 between 10:52 and 11:01 ET and all eight were fully signed by 11:44. Jon's 2026-08-21 email is titled "Last night's 11 approvals, all signed." A control that clears eleven documents overnight is worth asking what it is actually catching.
- **The catch rate is not zero, which is the counterargument.** Jon pushed back on 17011 at Su Rene: *"am I alone in feeling the need to push back on a $40k unplanned expense."* Gulf Breeze 15026 was held because a sign was mounted too high and crooked. Southgate 11127 was held on consistency. Three catches visible in one month.
- **GL coding is not standardised.** VO 17188 came through with GL 59014 against a 16xxx pattern every other document uses, queried by Jon on 2026-08-21.

## How a project gets logged

In `90-Skills/community-pulse-refresh.md`, step 1. For each Adobe Sign document in the For Signature folder: parse `CODE_TYPE_NUMBER`, resolve the code to a community, and add or update the row on that project number. A kickoff opens the row, a closeout closes it, and a `Completed:` notice is what dates either one. Never date a row from read state, per [[CLAUDE]] rule 14.

## Related

- [[10-Business/outlook-folder-map]] - where these documents live and how their disposition is read.

## Sources

- Adobe Sign notification emails in Austin's For Signature folder and Archive, read 2026-08-31.
- Jon Wyss, "Last night's 11 approvals," 2026-08-21 17:49 ET, and the Vlad and John Clark replies on the same thread.
- Jon Wyss, "Gulf Breeze signage, install looks too high and crooked," 2026-08-03, and "Southgate signage closeout, hold my approval?," 2026-08-03.
- `00-Meta/daily-close/2026-09-09.md` item 17, `2026-09-14.md`, `2026-09-15.md` item 16 and `10-Business/eos/to-dos.md` rows `TD-0646` and `TD-0649`, for the fourteen September documents. Added 2026-09-15.
- `00-Meta/audit-log.md` row 2026-09-21 19:04 ET for the nine document codes; `00-Meta/daily-close/2026-09-18.md` item 4, `2026-09-19.md` item 9 and `2026-09-21.md` item 11 for the counts. Prefix readings against the `HOT SHEET` code in each `60-Communities/*.md` header. Added 2026-09-22.

