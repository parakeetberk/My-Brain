# Target structure — Parakeet Birdcage SharePoint

**What this is:** the target folder tree for the new Parakeet Birdcage SharePoint — the destination Albert Gano is migrating everything into, and the reference everyone else works from.

**Status:** current — 2026-08-31

## The facts

- Source is one workbook, `Data Storage Security Direction.xlsx`, filed 2026-08-31. It contains **two different folder trees that do not match**, plus a per-community template and a file inventory of one existing community.
- **The tree rendered below is the `Folder Structure` sheet.** It is the fuller and newer of the two: 9 top-level areas, four folder levels plus a named-files column, a per-folder build **status** column (Done / To Do / Pending / Pending Review), a named owner initial on some rows, and permission columns for 16 security groups plus 68 per-community groups.
- **The `Structure` sheet is an earlier, six-area draft.** It is a hidden sheet. Its areas are CORPORATE, HUMAN RESOURCES, PROPERTY OPERATIONS, ACCOUNTING & FINANCE, ACQUISITIONS & ASSET MANAGEMENT and PROPERTY REFERENCE HUB. It carries folder descriptions the newer sheet does not, and it fills permissions for only the first 21 of its 163 folder rows. Both are recorded here; the newer one is the one to build.
- **The two trees disagree on the shape of the whole thing**, not on details. The older draft puts communities under `PROPERTY OPERATIONS > Communities > [Property Name] (City, ST)` with 7 unnumbered subfolders. The newer one puts them directly under `Operations > [Community Name] (City, ST)` with 8 subfolders — **numbered in the source workbook, unnumbered as built, per Austin 2026-08-31.** The newer one has no PROPERTY REFERENCE HUB and no ACCOUNTING & FINANCE; it has `Finance`, `Sales & Inventory`, `Asset Management`, `Acquisitions`, `Marketing` and `Data & Analytics` instead.
- **Depth:** four folder levels in both trees. The newer sheet records a fifth column of named files sitting inside the deepest folder (for example `Operating Manual` is marked "Live Document", and `Construction > [Issue #] [WIP] [Project Name]` holds Permits, Bids, Contracts and Photos).
- **Acquisitions is deliberately not built here.** Its two rows read `_Archive` and "Separate SharePoint Site Generated Based on Teams" — a separate site, not a folder in this one.
- **Only one community is built out in the newer tree:** American (Auburn, MA). The `Community Operations Folder` sheet builds out five — American, Applegate (Deland, FL), Auburn Ridge (Auburn, GA), Bay Oaks Village I & II (Panama City, FL) and Belle Haven (Clearwater, FL) — from the same 8-folder template. The remaining ~63 communities exist only as the template.
- **A copy/paste error to fix before building:** in `Community Operations Folder`, the American (Auburn, MA) block lists three Applegate rent-increase notices under `Communications > Rent Increases`.

## The target tree (rendered from `Folder Structure`)

Nine top-level areas: **00-Corporate, Human Resources, Operations, Finance, Sales & Inventory, Asset Management, Acquisitions, Marketing, Data & Analytics.**

### 00-Corporate

- Legal
  - Corporate Legal Matters *(status: Done)*
  - Compliance *(status: To Do)*
  - Entity Structure *(status: Done)*
    - Formation Docs *(owner: AG)*
    - PMAs *(owner: AG)*
    - Filings
- Investor Relations
  - Fund Docs
  - Board Materials
  - AGM
  - ESG
- Strategy
  - Corporate Models
  - EOS
  - Meeting Minutes
- Birdcage Files — four named live files, not folders
  - Payroll Calendar *(owner: DL)*
  - Org Chart *(owner: AB)*
  - Company Newsletter — spelled "Copany Newsletter" in the sheet
  - Property Data Sheet *(owner: ZS)*
- Administration

### Human Resources

- Employee Files
- Payroll
- Benefits
- Recruiting

### Operations

- `_Shared`
- `[Community Name] [City, State]` — the per-community template, below
- American (Auburn, MA) — the only community built out in this sheet

### Finance

- Bank Accounts
  - Bank of America
  - JPM Access
  - JPM Private
- Budgets
  - Internal Budgets
  - Lender Budgets
- Monthly Close
  - 2026-01
  - 2026-02
  - 2026-03
- Payroll
- Tax
  - Property Tax
  - Sales Tax
  - Filings *(status: Pending — DB discussion)*
    - 2024 — holds "To Discuss"
    - 2025 — holds "Cost Segs"
    - 2026 — holds "Filings"
    - 2027 — holds "Work Papers"
- Audit
  - 2025 — Work Papers & Final
  - 2026 — Work Papers & Final
  - 2027 — Work Papers & Final
- Insurance (Accounting)
  - Pre Paid Schedules
  - Premium Allocations
- Reference
  - Chart of Accounts
  - Check Lists
  - Accounting SOPs
- Vendor Packages

### Sales & Inventory *(status: Pending — LC discussion)*

- Inventory *(status: Pending)*
  - Manufacturer
    - Floorplans
    - Orders
  - Titles *(owner: AB)*
  - Home Info Packets
  - Quotes & Invoices
- Sales *(status: To Do)*
  - Agreements
  - Commissions
  - Marketing
- Lending *(status: To Do)*
- Dealership Information *(status: Pending Review)*
- Administrative *(status: To Do)*

### Asset Management

- Asset Management
  - Portfolio Performance
  - Business Plans
  - Valuations & Appraisals
- Investor & Lender Relations
  - Investor Packages
  - Lender Packages
  - Capital Calls & Distributions
- Market Research & Analytics
  - Market Reports
  - Comp Analysis
  - Data Models & Templates

### Acquisitions

- `_Archive`
- "Separate SharePoint Site Generated Based on Teams" — a note, not a folder. Acquisitions gets its own site.

### Marketing

- Brand Assets *(status: Done)*
- Photography *(status: Done)*
- Digital Marketing *(status: Done)*
- Print Materials *(status: Done)*

### Data & Analytics

- Dashboards
- JotForm
- Rent Manager
- Claude

## The per-community template

**Unnumbered as of 2026-08-31, by Austin's ruling.** The template previously ran `1-Asset Management` through `8-Templates`. The numbers came off because **permissions trim the view**: a group with WRITE on only some subfolders sees a sequence with holes in it — Offshore-Ops sees 1, 2, 7, 8 and Offshore-AcqAM sees 1, 2, 3 — which reads as missing folders rather than as scoped access. See [[10-Business/sharepoint/permissions-matrix]].

**The cost of dropping the numbers is almost nil**: alphabetical order reproduces the numbered order exactly except that Construction and Facilities swap third and fourth. The list below is now in the order it will actually render.

This is the folder set that repeats under `Operations` for every community. It appears three times in the workbook — as a template row in `Folder Structure`, as the `Community Operations Folder` sheet's template, and built out for five named communities — and is identical in all three. Folder name pattern: `[Community Name] [City, State]`, for example `American (Auburn, MA)`.

- **Asset Management**
  - Operating Manual — marked "Live Document"
  - PCAs
  - Survey
  - Site Maps (incl Utility Maps) — spelled "Utiltiy" in the sheet
- **Communications**
  - Notices
  - Rent Increases
  - Community Events
- **Construction**
  - `[Issue #] [WIP] [Project Name]` — holds Permits, Bids, Contracts, Photos
  - Inspections
- **Facilities**
  - Maintenance Logs
  - Service Contracts
  - Utility Readings
  - Work Orders
- **Insurance**
  - Active Policy
  - Claims
- **Legal**
  - Evictions
  - Violations
  - Lease Agreements
  - Inspections
  - License & Permits
  - Rules & Regulations (Prospectus)
- **Operations**
  - Site Visits
  - Photos
  - Incident Reports
- **Templates**
  - Property Specific Forms and Templates

For the five communities built out in `Community Operations Folder`, the four `Asset Management` subfolders are each flagged **"Need"** — the Operating Manual, PCAs, Survey and Site Maps do not exist yet for those communities.

### The earlier draft's community template, for the record

The hidden `Structure` sheet's version, under `PROPERTY OPERATIONS > Communities > [Property Name] (City, ST)`, with the descriptions it gives:

| Folder | Contents, per the sheet |
| --- | --- |
| Resident Files | Leases, applications, correspondence |
| Utilities | Electric, water, sewer, trash invoices |
| Vendor & Maintenance | Contracts, work orders, bids |
| Inspections & Compliance | State inspections, fire marshal, DEP |
| Capital Projects | Scope, permits, progress photos, close-out |
| Financial Reports | Monthly P&L, budget vs actual |
| Community Docs | Rules & regs, prospectus, site map |

The newer template covers all seven of these, split differently: Resident Files and Lease Agreements move into `Legal`, Utilities becomes `Facilities > Utility Readings`, Vendor & Maintenance splits across `Facilities`, Inspections & Compliance splits across `Construction`, `Legal` and `Operations`, Capital Projects becomes `Construction`, and Community Docs becomes `Asset Management` plus `Legal > Rules & Regulations (Prospectus)`. **There is no Financial Reports folder in the newer per-community template** — monthly close moves to `Finance > Monthly Close`.

## The earlier draft's tree, for the record

The hidden `Structure` sheet's six areas and their level-2 folders. It is the only place folder descriptions exist, so it is worth keeping until they are carried across.

| Area | Level-2 folders |
| --- | --- |
| CORPORATE | Legal & Entity; Insurance; Board & Governance; Company Policies & SOPs; Technology & IT |
| HUMAN RESOURCES | Employee Files; Payroll; Benefits; Recruiting & Onboarding; Training & Development; Compliance & Reporting |
| PROPERTY OPERATIONS | Communities; Construction Projects; Sales & Leasing; Marketing; Titles, Inventory & Licensing; Facilities & Maintenance; Regional Management |
| ACCOUNTING & FINANCE | General Ledger; Accounts Payable; Accounts Receivable; Financial Reporting; Budgets & Forecasts; Tax; Banking & Treasury; Audit & Compliance |
| ACQUISITIONS & ASSET MANAGEMENT | Deal Pipeline; Asset Management; Investor & Lender Relations; Dispositions; Market Research & Analytics |
| PROPERTY REFERENCE HUB | `[Property Name] (City, ST)` (one folder per community); Templates & Standards |

Folders that exist in the earlier draft and have **no home in the newer tree**: `CORPORATE > Company Policies & SOPs` (Employee Handbook & Policies, Operational SOPs, Technology & Security Policies), `CORPORATE > Technology & IT`, `CORPORATE > Insurance`, the whole `PROPERTY REFERENCE HUB`, `PROPERTY OPERATIONS > Regional Management`, `PROPERTY OPERATIONS > Titles, Inventory & Licensing > Vehicle & Equipment`, and most of `ACCOUNTING & FINANCE`'s ledger detail. **These are open questions for Albert, not omissions to assume away** — the SOP library in particular has 242 files in this vault and nowhere obvious to land in the newer tree.

## Decisions

- None recorded yet.

## Sources

- [[10-Business/sharepoint/Data Storage Security Direction.xlsx]] — the source workbook; sheets `Folder Structure`, `Structure` (hidden) and `Community Operations Folder`.
