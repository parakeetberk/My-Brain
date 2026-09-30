# The entity map already exists

**What this is:** the answer to Austin's question on `CM-06` — *"What is needed. Since this is important, tell me what I need to do to rectify this."*

**Status:** current — 2026-09-02. **The premise of `CM-06` was wrong and this page corrects it.**

## The short answer

**You do not need to build an entity map. One exists, it is a year newer than the file this Brain has been calling the only copy, and it already lists what is missing from it.**

`/sites/main/Shared Documents/Corporate/Formation Documents/Master Org Chart.xlsx` — last modified **2025-01-15**. Read in full 2026-09-02. **VERIFIED.**

It carries roughly **115 entities**, each with: status, type, name, short name, full street address, state, postal code, and a document checklist across **ORG CHART · LLC AGREEMENT · EIN LETTER · CLOSING BINDER**, marked ✓, MISSING, N/A or LINK. Behind that sit **per-community tabs with cap tables, ownership percentages, EINs and the fee schedule** (acquisition 1%, asset management 1%, capex 7%, disposition 1%).

**Every line already carries a status: `COMPLETE`, `WIP`, `MISSING DOCS` or `NOT STARTED`.** That column is the work list. Nobody has to invent one.

## What this Brain got wrong, and why it matters

`CM-06` said the only map was `Org Chart Overview.xlsx`, 2020, eleven tabs, broken formula columns, sitting in a personal OneDrive. That file is real. **It is not the only one and it is not the newest.** The 2023 version (`Org Chart Overview_122023.xlsx`) is also in a personal OneDrive, in Teams Chat Files. The 2025 master is in the company's own Formation Documents folder.

**This is [[CLAUDE]] rule 15 again, at the largest scale yet: a gap asserted from one file while the answer sat in the company's own corporate folder.** The row then sat for six days described as the highest-value unknown in the vault. **The unknown was a search away.**

## Three contradictions worth fixing first

These are not opinions. They are two documents in your own systems disagreeing.

**1. `PARAKEET MHC SENIOR, LLC` and `PARAKEET MHC MEZZ, LLC` both carry EIN `88-1479499`.** The same pair appears on roughly fifteen community tabs, so whichever is wrong has propagated everywhere. **Two entities cannot share an EIN.** This is the single most consequential data error in the file — an EIN on the wrong entity flows into filings.

**2. `A2Z Community Partners` is a Maryland LLC, EIN `47-5345819`.** The master says Maryland. **The 2023 org chart says Delaware.** [[10-Business/entity-structure/berk-inc-umbrella]] said Maryland, so the vault was right and the 2023 chart is wrong. Its cap table reads **Austin Rian Berk 95% Managing Member, and 5% to a "Trust to be formed FBO Julia and Hailey Berk."** *"To be formed"* on a 2025 document is worth one question: was it ever formed, and if not, who holds that 5%.

**3. There are two Northgates and this Brain has been treating them as one.** The master lists `Northgate MHP`, short name `N`, at **720 N Main Street, Mt Gilead, NC**. The 67-row Property Data Sheet has `Northgate MH` at **Mims, FL**. **That resolves an open question from the unit-count work** ([[00-Meta/analysis/2026-09-01-unit-count-reconciliation.xlsx]]): the warehouse's `Northgate MHP` record with GL activity and no units is a different asset in a different state, not a duplicate.

## The open questions its own author already wrote down

The `SK NOTES` and `AB Notes` columns carry live questions. **These are the fastest wins on the whole item because somebody already did the diagnosis.**

- *"Missing Parakeet MA Portfolio, LLC agreement"* — appears three times.
- *"Need to get from Larry"* — the same Larry as the Titan reinstatement on `CM-19`.
- *"SUPER CONFUSED ON THIS ONE"* — verbatim.
- *"Potentially outdated LLC agreement?"*
- **Crystal Acres**: *"the only one I found has PARAKEET MHC, LLC as the sole member, but it is not on most recent org chart."*
- **Hunter Springs**: *"only one I found has PARAKEET MHC I, LLC as the sole member vs PARAKEET MHC, LLC on most recent org chart"* — **three different members named for one asset across three documents.**
- **Gulf Breeze**: *"need LLC agreement to continue / is THIS CHART still accurate?"*
- **ND Communities**: *"Need operating agreement for ND Community Homes LLC. Need operating agreement for A2Z ND Portfolio Partners LLC signed by Evergreen and need Schedule A showing % ownership."* **A signed agreement with no ownership schedule is a live problem on a portfolio with outside investors.**

## What the map shows that changes other open items

**There are at least three distinct ownership families in here, and the Property Data Sheet only carries one.**

| Family | Examples | On the 67-row sheet? |
|---|---|---|
| **Parakeet MHC** (Senior → Mezz → MHC → asset LLC) | Applegate, Congress, Lucky Clover, Triple S, River Oaks | Yes |
| **Bedrock Fund II / Grove Banyan / Tarheel** | Cedar Grove, Colonial, Lambeth, Parkwood, Vandemere, Bay Oaks I & II, Westwood, Wolf Bay, Lake Wales, Town & Country, Oceanaire, Ormond Beach | **No** |
| **A2Z legacy and Post / PSP joint ventures** | ND Communities (Apple Creek, Countryside, Parktown — Bismarck ND), Cherrywoods (KS), Kimball Estates (MI), A2Z Fishin MHP (KS), Mayflower Hills, Valley View (OR), Mobile Manor (MD), Greenspot Village, Victoria Woods (MI), Collins and Underwood (NY) | **No** |

**This is a better answer to the unit-count gap than the one filed yesterday.** `KP-0010` asked why the warehouse reports 8,020 units against the Data Sheet's 6,379, and the conclusion was double-counted records. That still holds, **but the four communities found in the warehouse and not on the sheet — Cedar Grove, Colonial, Lambeth, Cambridge — are not missing. They are in a different ownership family**, and the Data Sheet is a Parakeet MHC document. **The sheet is not incomplete; it is scoped, and nothing said so.**

## What to actually do

**Four steps, and only the last one needs you.**

1. **Make the master the single source and say so in writing.** Retire the two personal-OneDrive copies to an archive folder so nobody reconciles against a 2020 file again. Task `TD-0398`.
2. **Fix the shared EIN.** `PARAKEET MHC SENIOR` versus `PARAKEET MHC MEZZ`, `88-1479499`. Pull both EIN letters and correct the fifteen tabs. Task `TD-0399`.
3. **Work the status column as the list.** Every `MISSING DOCS` and `NOT STARTED` line names what is absent. That is a document-chasing exercise, delegable, and it does not need you. Task `TD-0400`.
4. **Answer the questions only you can.** The Trust FBO Julia and Hailey Berk — formed or not. Whether Crystal Acres and Hunter Springs sit under `PARAKEET MHC` or `PARAKEET MHC SENIOR`. Whether the Gulf Breeze chart is still accurate. **These are the four that have kept this row open, and they are four sentences, not a project.** Task `TD-0401`.

**What this row is not, any more: a build.** It is a document chase with four questions for you at the front of it.

## Sources

- `/sites/main/Shared Documents/Corporate/Formation Documents/Master Org Chart.xlsx` — read in full 2026-09-02, **VERIFIED**.
- `.../Microsoft Teams Chat Files/Org Chart Overview_122023.xlsx` in Austin's OneDrive — read in full 2026-09-02, the Delaware-versus-Maryland conflict.
- Also present and not read: `Org Chart All Entities.xlsx` and `Org Chart.xlsx` on Austin's Desktop, `Master Org Chart_TO USE _Backup.xlsx` and `A2Z - Master Org Chart - 5-20-20 DRAFT.xlsx` in Formation Documents `_Archive`. **Six versions of one map is its own finding.**
- Austin, `CM-06` on the open board, 2026-09-01.

## Answered by Austin, 2026-09-02

**Three of the four questions this analysis put to him came back the same day, on the open board (`TD-0401`), verbatim:** *"1) No this was not formed and going to be formed at some point. 2) Crystal Acres - Kippy Single Asset. 3) HSRC was Parakeets property. Sold to HSMHC which is Kippy and has a seller note from HSRC"*

**1. The trust does not exist.** The chart's *"Trust to be formed FBO Julia and Hailey Berk"* holding 5% of A2Z Community Partners was **never formed**, and is intended to be at some point. **The half he did not answer is the one that matters: who holds that 5% today.** A 2025 governance document assigns a stake to an entity that does not exist, so the stake sits somewhere and the chart does not say where. `TD-0435`.

**2. Crystal Acres was a false choice.** The question offered `PARAKEET MHC` or `PARAKEET MHC SENIOR` and the answer is **neither** - it is a **Kippy single asset**. **Corroborated independently the same morning** on the rehab call, where the Crystal Acres rehabs were put on hold with *"honestly, that's Kippy's responsibility."* Two channels, one answer, and **it means this analysis framed the question wrongly rather than the chart being ambiguous.**

**3. Hunter Springs makes Parakeet a lender twice over.** HSRC was Parakeet's property, sold to **HSMHC, which is Kippy**, and **HSRC holds a seller note from the sale.** `CM-24` already describes a defaulted note where Parakeet is the lender, roughly $1M of unpaid management fees, and *"three portfolio communities inside it."* **This adds a second Parakeet-to-Kippy paper relationship and a second Kippy-linked asset, and whether either is among `CM-24`'s three is not stated anywhere and is not assumed here.** `KP-0055`, `TD-0436`.

**Why this is the most consequential thing on the page.** The entity map was opened as a filing problem. **Answering three of its questions surfaced a counterparty exposure**, and it collided with an operational decision within the hour: **the same 2026-09-02 rehab call approved $20,000 of rehab spend at Hunter Springs** to obtain a November sign-off, on an asset Parakeet sold to this counterparty and financed. **Who pays, and whose sign-off is being sought, are not obvious from either conversation.** Counsel is already being briefed on the Kippy and Brokaw single-identity finding under `TD-0368`; this belongs in the same brief.

**4. Gulf Breeze is still open.** The chart's own note asks *"is THIS CHART still accurate?"* about Gulf Breeze's ownership. `PD-16` answered the **occupancy** question on 2026-09-02; **this is the ownership question and it is a different one.** Still on `TD-0401`.
