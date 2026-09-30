# Asset Management

**What this is:** the department that tracks every other department — the scorecard, the capex tracker, the asset records and the portfolio reporting — and the one with no documented process of its own. SOP band 400–499 is empty.

**Status:** current — 2026-08-30

## The facts

- **Director: Zach Schwartz**, Director of Asset Management & Acquisitions. **Employee number one.** Jon Wyss's right hand in the Miami office — Austin's words: Zach is "Jon's Natalie." See [[10-Business/people/zach-schwartz]].
- **The team.** Alex Fals (Acquisitions Analyst), Alexander Stuart (Acquisitions & Asset Management Analyst — reporting, financial analysis, data management, and the issue-level data entry in the rehab flows), and Justin Minkoff (Asset Management & Data Analyst — the Rent Manager gate). Auzzi Dixon dual-reports here from Sales. Offshore back-end support from Anna Marie Lapitan and Gearlene Valenzuela. See [[10-Business/people/alex-fals]], [[10-Business/people/alexander-stuart]], [[10-Business/people/justin-minkoff]].
- **Justin Minkoff's reporting line is not what the chart says.** The December-2025 org chart puts him under Zach; in practice he reports to Austin with Zach as the backstop.
- **The March deck's framing of the department, verbatim:** "MAJOR WORKFLOWS SPAN ALL DEPARTMENTS — **AM + ACCTG & FINANCE ARE CENTRAL HUB.**" On all five cross-departmental workflows — Home Sale, Home Demo, Vacant Lot In-fill, Capex Project, Home Rehab — "Asset Management sets the tone and is tracking projects to budget, reporting on progress and holding departments accountable."
- **What it owns:** the EOS scorecard, CapEx Tracker 2.0, the asset records in Rent Manager, the infill plan, the Make Ready Board, and portfolio reporting.
- **SOP band 400–499 is EMPTY** — a scaffold folder holding only a `_README.txt` marked "coming soon". The queued processes named in that README are **Corporate Model, Debt Overview, Insurance Policy Inventory and Compliance Calendar.** Bands 500–599 (Acquisitions / Dispositions) and 600–699 (Systems / IT / Reporting) are empty too, and both sit in this department's remit ([[70-Operations/sops/sop-library]]).
- **Where it appears in other departments' processes instead.** Asset Management moves Prospect to Resident and marks the asset inactive once funds are confirmed and the floorplan loan is paid off (SOP 003a, 004). Justin updates Rent Manager within 24 hours of any date change from Sales (SOP 001), and enters all month-end updates after the Director of Operations approves the tracker on the 29th (SOP 301). Alexander Stuart opens the rehab issues and checklists — **no rehab charge may be booked until a valid Rent Manager issue number exists** (SOP 105).
- **2026 year-end goals, verbatim from the March deck:** "SALES & MARKETING REPORTING – Once CRM built out, we will roll out more detailed reports around prospects, home sales, etc." · "UTILITY OPTIMIZATION – Analytics in tandem with Acctg team" · "SERVICE CONTRACTS – Optimize process & find savings" · "INTERNAL REPORTING – Enhance KPI reporting for Ops Team" · "FINALIZE CAPEX TRACKING – Working on improved tracker 2.0" · "TECH – Explore use of AI for budgeting, reporting & analytics."
- **2026 rocks (Zach Schwartz):** Q1 — Internal KPI Reporting (EOS Scorecard) · Cap Ex Tracker 2.0. **Q2 — none on file. Q3 — none on file.** Jointly with David Berman: timely monthly financial reporting across all entities (Q1), payroll and utility recapture analysis (Q1), real-time cash flow reporting and future cash projections (Q2), service contract optimisation (Q3). Evidence on [[10-Business/eos/rocks-2026]].
- **KPIs on the scorecard: none.** Zach Schwartz's KPI cells are blank, as is the joint David & Zach row ([[10-Business/eos/scorecard]]).
- **Weekly reporting to Jadian on occupancy, infill and capex KPIs is a stated 2026 corporate priority:** "Enhanced reporting – Weekly internal and Jadian reporting rollout across occupancy/infill, capex and operations KPIs" (board deck, 2026 Goals & Objectives). See [[30-Customers/capital-partners/jadian]].
- **The trackers it owns and the numbers in them:** the 2026 infill plan covers 51 properties, 925 recorded vacancies against a 661-occupant gain goal (Sheet2, per-property view, 51 properties); the 2026 capex plan carries $9,954,600 across the 169 line items still marked "Existing" (53 properties); the payroll model shows $54,487,005 of 2026 budgeted revenue across 65 properties with 16 running a payroll deficit against the 5%-of-revenue allocation ([[60-Communities/portfolio]]).
- **Systems it runs on:** Rent Manager as the system of record ([[10-Business/vendors/rent-manager]]); the CapEx Overview and Infill Strategy workbooks; QuickBase; SharePoint; Power Automate exports into SharePoint with Make.com orchestration on top, run by Jhosua ([[10-Business/people/jhosua]]); the RentViewer data warehouse and the MAV CRM ([[10-Business/vendors/mav-consulting]]); Campspot analytics on the RV side ([[10-Business/vendors/campspot]]).

### Named problems

- **No SOPs at all, in the department that owns the tracking layer everything reports into.** Asset Management is named the central hub of all five cross-departmental workflows and has zero documented process. Three of the four empty bands are its remit, and two of the seven Tier 1 Critical processes with nothing started are its acquisitions transitions and utility onboarding at takeover.
- **The scorecard is still unscoreable, and fixing it is Zach's own Q1 rock.** The KPI names sit in the Rocks file with no targets, units, frequency or definitions; the numeric year-end targets sit only in the March deck; the two have never been reconciled. Six of twenty targets have no KPI name at all, and this department has no KPIs of its own ([[10-Business/eos/scorecard]]).
- **Justin Minkoff spends time cleaning up other departments' data problems, and Austin wants that stopped.** It is a symptom of missing data-entry standards, not of him being too helpful; the fix is standards at the point of entry, which is what the FastField and QuickBase work is for.
- **"CREATING ONE SOURCE OF TRUTH – DATA ACCURACY & MULTIPLE SPREADSHEETS"** is the deck's own heading, with "build a single dashboard that everyone trusts," "one space for teams to see status, ownership, and progress across all departments," and "SharePoint - finalize structure, assign ownership, and drive adoption across the org."
- **On the occupancy goals it publishes — JREFI 292 of 386, JREFII 263 of 401, ORIGINS 106 of 138 — the deck asks its own question:** "**Who owns these goals and what are the contingency plans when targets aren't met?**" and "Cadence of reporting & reviews – weekly? **Scorecard!**"
- **The capex tracker is marked "(needs iterated)"** on the department's own accomplishment slide.
- **The data behind the reporting has known defects that are not silently worked around:** the Property Data Sheet's "Total Units" column reads 40 on every row and is broken; five occupancy rows are a data gap, not 0%; short codes and portfolio labels differ between workbooks so any join needs an alias map ([[60-Communities/portfolio]]).
- **Which system is the single source of truth for prospecting and lead data — MAV or Rent Manager — was agreed as necessary but not chosen** on 2026-08-24.

### Handoffs

- **From every department.** Asset Management is the reporting destination for capex spend, project completion, infill completions, rehabs, delinquency, evictions, lease penetration and POH conversions.
- **To Accounting & Finance** — the other half of the central hub. Joint rocks on monthly financial reporting, real-time cash flow, payroll and utility recapture, and service contracts. See [[10-Business/departments/accounting-and-finance]].
- **To Property Operations** — the month-end chain lands here for entry, and the KPI reporting for the ops team is a stated 2026 goal.
- **To Construction** — CapEx Tracker 2.0 is the instrument; Asset Management holds Construction to budget.
- **To Sales & Marketing** — sales and prospect reporting sits behind the CRM build; the Prospect-to-Resident transition is an Asset Management step.
- **To the capital partners** — weekly occupancy, infill and capex reporting to Jadian, and the corporate model and quarterly valuations built with them.

## Acquisition in view, 2026-09-22 to 09-25

*Added 2026-09-26 by the Page Update from the daily closes of 2026-09-22 to 09-25 (`00-Meta/daily-close/2026-09-22.md` to `2026-09-25.md`). Confidence labels are the closes' own; the primary messages were not re-opened this run. Figures in `00-Meta/numbers-ledger.md`.*

- **Courtly Manor Park, Hialeah Gardens: 525 sites, fully occupied, zero park owned homes, call for offers 2026-10-07.** Jon put it in front of Austin at 01:31 ET on 2026-09-22; already in front of Jadian by 2026-09-24. `TD-0710`.
- **Geiger Key is selling** and a payroll allocation there is being corrected in 2026. `TD-0712`.

## Decisions

- 2026-08-24 — Use RentViewer to sync data daily into the data warehouse instead of manual backup pulls, engage the RentViewer team before building, and make everything reachable through Claude over the warehouse. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]])
- 2026-08-24 — Sales momentum over the next six months is the determinant of the recap; turnover runs more than 3% a year across around 7,000 units. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-sam-brainstorming-session]])
- 2026-08-20 — Power Automate runs under dedicated server accounts rather than individual drive access, centralising control and restricting broad data access. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-lucky-clover-site-visit]])

## Sources

- [[10-Business/eos/department-plans]] — the central-hub framing, the verbatim 2026 goals, the rocks and the March deck's named problems.
- [[70-Operations/sops/sop-library]] — the empty 400–499 band, its README queue, and the Tier 1 gaps in this remit.
- [[10-Business/eos/scorecard]] — the unreconciled KPI names and targets, and the blank KPI rows.
