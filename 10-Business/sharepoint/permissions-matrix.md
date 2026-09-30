# Permissions matrix — Parakeet Birdcage SharePoint

**What this is:** who gets WRITE, READ or NO ACCESS to each area of the new SharePoint — the patterns, the exceptions, and the rows where nothing has been decided yet.

**Status:** current — 2026-08-31

## The facts

- Source is `Data Storage Security Direction.xlsx`, filed 2026-08-31. **Two sheets carry permissions and they use different vocabularies and different group sets.**
  - **`Folder Structure`** — the newer grid. **165 folder rows fully filled** across **16 group columns** (the 15 named groups plus `Ops Administration`), then a `Property Operations` column, then 68 per-community columns. Values are `WRITE` / `READ` / `NO`.
  - **`Structure`** (hidden) — the earlier draft. 163 folder rows, 15 group columns, values `WRITE` / `READ` / `NO ACCESS`. **Only the first 21 rows have any permissions at all.**
- **The summary below is built from `Folder Structure`**, because it is complete and it matches the tree that is actually being built.
- **The permission model is additive in SharePoint and the matrix is not.** Several people are in two or three groups. A `NO` for one group does not deny someone who reaches the same folder through another. Enforcing the `NO` column requires unique permissions on the folder, not just group design.

## The patterns

Nine patterns account for almost every row.

| Pattern | Applies to | Shape |
| --- | --- | --- |
| **Board is WRITE everywhere** | all 165 rows | Board = WRITE on every single row, with no exception. |
| **Everyone reads the shared reference** | 00-Corporate top level, Birdcage Files, Administration, all of Marketing | READ for all 16 groups; Board WRITE; the owning team WRITE. |
| **Corporate detail is locked to Board plus one team** | Investor Relations children, Strategy children | Board + Sr Fin-Team + AcqAM-Team WRITE; everyone else NO. |
| **HR is HR-Team and Board only** | all four Human Resources folders | Board + HR-Team WRITE; everyone else NO, except Finance-Team READ on Payroll and Benefits. |
| **Finance is Sr Fin-Team plus Finance-Team** | all of Finance | Board + Sr Fin-Team + Finance-Team WRITE; Property Operations and all 68 community groups NO throughout. |
| **Communities are READ by default, WRITE where the field works** | the per-community template | The whole community folder is READ to all 16 groups; the field-writable folders are Facilities, Legal (Evictions, Violations, Leases, Inspections) and Operations (Site Visits, Photos, Incident Reports). |
| **Community groups are scoped to their own community** | 68 community columns | Each community's group gets READ across the community template and WRITE on the field-writable folders. NO on every corporate, HR and Finance folder. |
| **Sales & Inventory is Sales-Mktg-Team plus Titles-Inv-Team** | all of Sales & Inventory | Those two WRITE; most others READ; HR-Team NO throughout except Commissions. |
| **Asset Management is Sr Fin + Finance + AcqAM** | all of Asset Management | Those WRITE; Sr Ops-Team and Exec-Team READ; everyone else NO. |

## Locked down to almost everyone

Folders where **13 or more of the 16 groups are NO**, and who the exceptions are.

| Folder | Groups denied | Who gets in |
| --- | --- | --- |
| 00-Corporate > Strategy > EOS | 15 of 16 | Board (WRITE) only |
| 00-Corporate > Strategy > Meeting Minutes | 14 of 16 | Board, Sr Fin-Team (WRITE) |
| 00-Corporate > Investor Relations > Fund Docs | 13 of 16 | Board, Sr Fin-Team, AcqAM-Team (WRITE) |
| 00-Corporate > Investor Relations > Board Materials | 13 of 16 | Board, Sr Fin-Team, AcqAM-Team (WRITE) |
| 00-Corporate > Investor Relations > AGM | 13 of 16 | Board, Sr Fin-Team, AcqAM-Team (WRITE) |
| 00-Corporate > Investor Relations > ESG | 13 of 16 | Board, Sr Fin-Team, AcqAM-Team (WRITE) |
| 00-Corporate > Strategy > Corporate Models | 13 of 16 | Board, Sr Fin-Team, AcqAM-Team (WRITE) |
| **Human Resources > Employee Files** | 14 of 16 | Board, HR-Team (WRITE) |
| **Human Resources > Payroll** | 13 of 16 | Board, HR-Team (WRITE); Finance-Team (READ) |
| Human Resources > Benefits | 13 of 16 | Board, HR-Team (WRITE); Finance-Team (READ) |
| Human Resources > Recruiting | 14 of 16 | Board, HR-Team (WRITE) |
| **Finance > Payroll** | 14 of 16 | Board, Finance-Team (WRITE) |
| Finance > Tax, and Property Tax / Sales Tax / Filings / Filings 2024–2027 | 13 of 16 each | Board, Sr Fin-Team, Finance-Team (WRITE) |
| Finance > Audit, and 2025 / 2026 / 2027 Work Papers & Final | 13 of 16 each | Board, Sr Fin-Team, Finance-Team (WRITE) |
| Finance > Reference, Chart of Accounts, Check Lists | 14 of 16 each | Board, Finance-Team (WRITE) |
| Asset Management > Investor & Lender Relations > Capital Calls & Distributions | 14 of 16 | Board, Sr Fin-Team (WRITE) |

**Legal and litigation is the exception to the pattern — it is not locked down in the newer sheet.** `00-Corporate > Legal` is READ for all 16 groups, and inside it `Corporate Legal Matters` and `Compliance` are NO for 11 of 16, with Board, Sr Ops-Team, Sr Fin-Team and HR-Team on WRITE and Exec-Team on READ. There is no litigation folder in the newer tree at all. The earlier `Structure` draft did have one — `CORPORATE > Legal & Entity > Litigation & Claims`, NO ACCESS to 11 of 15 groups, WRITE for Board, READ for Sr Ops-Team, Sr Fin-Team and Finance-Team. **If litigation material is coming across, it needs a folder and a permission line; right now it has neither.**

## READ to everyone

Every group READs these, nobody is denied. This is the "everyone can see it" layer.

- `00-Corporate > Legal` (parent), `Investor Relations` (parent), `Strategy` (parent), `Administration`
- `00-Corporate > Birdcage Files` — Payroll Calendar, Org Chart, Company Newsletter, Property Data Sheet. Also READ for `Property Operations` and all 68 community groups: **these four files are the only things in 00-Corporate the field can see.**
- All four Marketing folders — Brand Assets, Photography, Digital Marketing, Print Materials
- The whole per-community template, including every community's own folder
- `Sales & Inventory > Sales > Commissions`

**Company policies and SOPs are READ to everyone in the earlier draft, and have no home in the newer one.** In `Structure`, `CORPORATE > Company Policies & SOPs` and all three children (Employee Handbook & Policies, Operational SOPs, Technology & Security Policies) are READ for all 15 groups with Board and HR-Team on WRITE, and Sr Ops-Team on WRITE for Operational SOPs. **The newer tree has no equivalent folder.** The closest thing is `Finance > Reference > Accounting SOPs`, which is READ to 14 groups but NO for Facilities-Team and NO for Property Operations and all 68 community groups — so under the newer model the field cannot read the SOPs. That is very likely not the intent.

## Where offshore groups have WRITE

**Note, 2026-08-31:** the per-community subfolders below are written **unnumbered** — Austin removed the `1-` through `8-` prefixes on 2026-08-31, and this section is the evidence for why. Offshore-Ops holds WRITE on the 1st, 2nd, 7th and 8th folders of the old sequence and Offshore-AcqAM on the 1st, 2nd and 3rd. Under permission trimming those users saw `1, 2, 7, 8` and `1, 2, 3` — a numbered list with holes, which reads as missing folders rather than scoped access.


38 rows. Grouped by what they are:

- **Offshore-Ops** — `Operations > _Shared`; and per community: `Asset Management > Site Maps`, all three `Communications` folders, all three `Operations` folders (Site Visits, Photos, Incident Reports), and `Templates > Property Specific Forms and Templates`.
- **Offshore-AcqAM** — `Operations > _Shared`; and per community: `Asset Management > Site Maps`, all three `Communications` folders, all four `Facilities` folders (Maintenance Logs, Service Contracts, Utility Readings, Work Orders). Plus `Finance > Budgets > Internal Budgets` and `Lender Budgets`, and all three `Asset Management > Market Research & Analytics` folders.
- **Offshore-Fin** — **all three `Finance > Bank Accounts` folders: Bank of America, JPM Access, JPM Private.** Plus `Finance > Insurance (Accounting)` and both its children, `Finance > Reference > Accounting SOPs`, `Finance > Vendor Packages`, and all three `Asset Management > Market Research & Analytics` folders.

**The Bank Accounts rows are the ones to look at first.** Offshore-Fin has WRITE on all three bank folders while Sr Ops-Team, Exec-Team, Regional-Mgrs and everyone else outside Board / Sr Fin-Team / Finance-Team has NO. That may be exactly right — Offshore-Fin is the AP and property-accounting team — but it is the highest-value WRITE in the model and it belongs to the group furthest from the office.

## Rows with blank or unspecified permissions

**Blank is not NO ACCESS. Blank is a decision nobody has made.** Every such row, in both sheets.

### `Folder Structure` — 20 rows

Ten of these are the `Files` header cells in column H and are not folders; the real gaps are the ten below them.

| Row | Folder | State |
| --- | --- | --- |
| 22 | `00-Corporate > Birdcage Files` | Board WRITE only; the other 15 groups and all 68 community columns blank |
| 156 | `Sales & Inventory > Inventory > Home Info Packets` | all 16 groups blank |
| 157 | `Sales & Inventory > Inventory > Quotes & Invoices` | all 16 groups blank |
| 170 | `Asset Management > Asset Management` (level-2 parent) | all blank |
| 174 | `Asset Management > Investor & Lender Relations` (parent) | all blank |
| 178 | `Asset Management > Market Research & Analytics` (parent) | all blank |
| 184 | `Acquisitions > _Archive` | all blank |
| 185 | `Acquisitions > "Separate SharePoint Site Generated Based on Teams"` | all blank — a note, not a folder, but Acquisitions has no permission line anywhere |
| 3, 33, 39, 116, 150, 169, 183, 187, 193 | the nine `Files` header cells under each top-level area | not folders |
| 162, 164, 166 | three fully-filled permission rows with **no folder name** in any column | orphan rows; 166 is the most permissive row in the sheet (WRITE for 10 of 16 groups and all 68 communities) and belongs to nothing |

The two that matter most: **`Home Info Packets` and `Quotes & Invoices` are the only two named, real folders in the newer sheet with no permission line at all.** Home Info Packets holds home paperwork; Quotes & Invoices holds pricing. Both sit under `Inventory`, whose own row grants Sales-Mktg-Team and Titles-Inv-Team WRITE and everyone else READ. If they inherit, they are readable by all 16 groups and all 68 community groups. **That is the unspecified permission on a sensitive folder to fix.**

And **`Acquisitions` has no permissions anywhere.** Deal material, LOIs and PSAs are the single most confidential category the company has, and the area is a two-row placeholder pointing at a separate site that has not been specified.

### `Structure` (hidden) — 142 rows

The earlier draft fills permissions for rows 4 through 31 only. Everything below is blank.

- **Partial rows (some groups set, most blank):**
  - `CORPORATE > Board & Governance` and all three children — Meeting Minutes, Resolutions & Consents, Investor Communications — **Board = WRITE, the other 14 groups blank.**
  - `CORPORATE > Technology & IT` and both children — Software & Licenses, System Documentation (described as "architecture, integrations, credentials vault ref") — **Board, Sr Ops-Team, Sr Fin-Team, Exec-Team set; the other 11 groups blank.** A folder whose description mentions a credentials vault reference, with 11 groups unspecified.
- **Entirely blank (no group set at all):** the area rows CORPORATE, HUMAN RESOURCES, PROPERTY OPERATIONS, ACCOUNTING & FINANCE, ACQUISITIONS & ASSET MANAGEMENT, PROPERTY REFERENCE HUB; and every folder from row 33 down. That is:
  - **HUMAN RESOURCES** — Benefits (Health & Dental Plans, 401k & Retirement, Workers Comp), Recruiting & Onboarding (Open Positions, Applications & Resumes, Onboarding Checklists & Templates), Training & Development (Training Materials, Certifications & Licenses, Performance Review Templates), Compliance & Reporting (EEO & Affirmative Action, Labor Law Posters & Notices, Audit Documentation) — **16 folders, all blank.** Benefits and 401k are as sensitive as the Employee Files folder above them, which is NO ACCESS to 13 of 15.
  - **PROPERTY OPERATIONS** — all 38 folders, including the whole `Communities > [Property Name] (City, ST)` template with Resident Files in it.
  - **ACCOUNTING & FINANCE** — all 34 folders, including Bank Statements, Loan Documents, Federal Returns and Rent Rolls.
  - **ACQUISITIONS & ASSET MANAGEMENT** — all 24 folders, including Due Diligence, Closed Deals and Capital Calls & Distributions.
  - **PROPERTY REFERENCE HUB** — all 13 folders.

## Questions, not accusations

Five things read oddly. Each is stated as a question for Albert and Austin.

1. **Is Exec-Team meant to be locked out of board and fund material?** Exec-Team is NO on Fund Docs, Board Materials, AGM, ESG, Corporate Models and Meeting Minutes, and NO on all of Human Resources and all of Finance — while Board, Sr Fin-Team and AcqAM-Team have WRITE. Exec-Team is Albert Gano, David Berman, John Clark, Jon Wyss, Leslie Croft, Natalie Magurne and Zach Schwartz. Four of those seven reach the same folders through Board, Sr Fin-Team or AcqAM-Team anyway, so the effect of the NO falls on Albert Gano, John Clark and Leslie Croft specifically. Is that the intent?
2. **Why is Facilities-Team the single group denied Entity Structure and the Accounting SOPs?** On `Entity Structure`, `Formation Docs`, `PMAs`, `Filings` and `Finance > Reference > Accounting SOPs`, every group gets READ except Facilities-Team, which gets NO. It is the only single-group exclusion in the sheet.
3. **Why does HR-Team have WRITE on Corporate Legal Matters, Compliance, and Sales Commissions?** HR-Team is one person, Demetria Loukas. She has WRITE on two corporate legal folders where Finance-Team has NO, and WRITE on `Sales & Inventory > Sales > Commissions` while being NO on every other row in that area. Commissions plausibly belongs to HR because it feeds payroll; the legal folders are less obvious.
4. **Are the two Payroll folders both real?** There is `Human Resources > Payroll` (HR-Team WRITE, Finance-Team READ) and `Finance > Payroll` (Finance-Team WRITE, HR-Team NO). Mirrored permissions on the same-named folder in two areas usually means one is canonical and one is a copy.
5. **Is Offshore-AcqAM meant to have WRITE on Internal Budgets and Lender Budgets while Offshore-Fin has NO?** The budget work sits with finance, so the two offshore columns may be swapped on those two rows.

## Decisions

- None recorded yet.

## Related

- [[10-Business/sharepoint/target-structure]] — the folder tree these permissions apply to.

## Sources

- [[10-Business/sharepoint/Data Storage Security Direction.xlsx]] — sheets `Folder Structure` and `Structure` (hidden).
