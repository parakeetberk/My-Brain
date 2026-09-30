# Paychex

**What this is:** payroll and the benefits portal — how roughly 125 people get paid and where they view and change their benefits.

**Status:** current, 2026-09-22. September control findings added by the Page Update; the operating facts above them are as of 2026-08-30. Extended 2026-09-26: a dated block from the closes of 2026-09-22 to 09-25 was added by the Page Update; nothing above it was changed.

## The facts
- **What they supply:** payroll processing, direct deposit administration, and the self-service portal that carries benefits enrolment and company policies.
- **Who uses it:** every employee (pay, direct deposit, benefits, policies), Human Resources and Payroll (administration and changes), and Accounting, whose rebuilt payroll model allocates payroll and healthcare expense by property and geography.
- **The workweek for payroll purposes begins on Monday and ends on Sunday.** Team members are **paid biweekly, on every other Friday**; if a scheduled payday falls on a holiday the date shifts.
- **Direct deposit is administered through Paychex.** Employees receive the information during onboarding, and the first deposit of payroll follows **within 30 calendar days** after the employee submits the completed form. Existing employees change their account through HR or by logging into their Paychex account directly.
- **Medical, dental and vision plan options are all viewed on Paychex**, per the Employee Handbook — so it is the benefits window, not only the pay engine. The dress code policy is also published there.
- Overtime is paid at one and a half times the regular rate for hours worked over 40 in a workweek, with holidays, vacation and sick days excluded from the 40-hour calculation. Mileage reimbursement forms are submitted for payroll **weekly**.
- **How critical: high — 125 people get paid through it.** There is no shadow payroll, no alternative provider and no manual pay run documented anywhere. A Paychex outage across a pay cycle is a direct employment and compliance problem in five states, and it simultaneously takes out the benefits portal every employee uses to view their plans.
- The dependency is wider than pay: Accounting's payroll allocation by property and geography, and the fiscal-year compliance calendar that carries **payroll, debt, tax and property tax deadlines**, both run off payroll data.
- Payroll is also a live budget item, not a fixed one: 2025 payroll came in **$219k under budget (-8%)** but was over-budgeted by more than 5% because **lot rent credits to managers now run through payroll**.
- **Restructuring benefits was a 2026 goal with a July renewal** — "RESTRUCTURE HEALTHCARE BENEFITS – Renewal in July" — which is a Paychex-portal change as much as a plan change.
- **Known problems — payroll and HR have almost no documented process.** The **700–799 HR & Training SOP band is empty except an orphan**, SOP 704 on disciplinary action forms, which is a PDF with no number inside it, no owner and no timeline. There is no onboarding SOP, no payroll SOP, no benefits SOP and no offboarding SOP.
- HR itself has no contact route in the library: SOP 108 requires same-day written notification to HR for any incident involving Parakeet personnel and its **HR email is literally [TBD]**, and SOP 704 requires HR consultation before any written discipline and gives no route to reach them.
- SOP 704 also warns that "certain states have different laws that must be factored into disciplinary action" against five operating states — and there is **no state-specific employment guidance anywhere in the library**; the 800s compliance block is tenancy law only.

**September 2026, added 2026-09-22 by the Page Update, from the daily closes 2026-09-18 to 09-21.**

- **HR has told both founders in writing that employee records are changing in Paychex without her making the changes, and she raised it with Paychex before either founder heard.** Demetria Loukas in the leadership Teams chat, 2026-09-18 12:04 ET: *"this is not an isolated episode. I contacted Paychex this past week because I told them that people's information has been changing in the system without my having implemented those changes and I was supposed to have a meeting set up"*. The trigger was Zach Schwartz at 12:00 ET reporting that some employees' medical insurance deductions came out lower, with his own sizing of it: *"if employees are paying less money my concern was that the company would be paying more."* **Three separate things, kept apart on the register**: records changing without HR's action is a system access and control problem; deductions not matching elections is a payroll accuracy problem; and the mechanism runs through a **Master Deduction Log Demetria generates monthly and hands to a payroll specialist**, a manual handoff with no stated check on the other side. Austin: *"Let's discuss Tuesday I'll be in"*, meeting 2026-09-22. **Who pulls the Paychex audit trail was asked on three closes and not answered**; the reports Demetria is running show whether a number is wrong, not who changed the record, and the person running them is the person whose access is in question, which is why a control test is not self administered. No employee, election, deduction or premium figure is recorded, guardrails 7 and 9. `KP-0119`, `TD-0679`.
- **The same morning, Toast locked Demetria's account overnight and Justin Hults had to be provisioned to submit payroll at all**, so a pay run depended on a second person being set up the same morning. Her words, 12:10 ET. What Toast is in this stack, and how it relates to the Paychex submission, is not recorded anywhere in this Brain and is not guessed here.
- **Where the workers comp view went** is on `10-Business/outside-help/baldwin.md`: since the Baldwin handover HR can no longer see the Parakeet workers compensation breakdown (`TD-0652`, 2026-09-14).

## Payroll held, 2026-09-23 to 09-25

*Added 2026-09-26 by the Page Update from the daily closes of 2026-09-22 to 09-25 (`00-Meta/daily-close/2026-09-22.md` to `2026-09-25.md`). Confidence labels are the closes' own; the primary messages were not re-opened this run. Figures in `00-Meta/numbers-ledger.md`.*

- **Payroll for Parakeet Communities LLC stopped rather than slipped on 2026-09-23.** Paychex came back on the deductions log at 17:02 ET and Demetria wrote at 17:04 ET, *"Austin I will have to wait to have payroll submitted."* Paychex is researching. `TD-0679`.
- **David Berman, 2026-09-24 17:21 ET: *"We can talk it through on Monday."*** Demetria has a Paychex appointment Monday 2026-09-28 at 10:00 and an unanswered question to Austin, Kelly Benefits instead or quotes from both. `TD-0715`.
- **Underneath it:** Paychex, Wise and Rent Manager disagree about who works here, and no roster exists. See [[10-Business/people/offshore-team]].

## Decisions
- None recorded yet.

## Sources
- [[10-Business/hr/Parakeet Communities Employee Handbook.pdf]] — the Monday-to-Sunday workweek, biweekly Friday pay, direct deposit through Paychex and the benefits plan options on Paychex.
- [[80-Finance/board/Parakeet - Board Presentation 2026-03 vFINAL.pdf]] — the rebuilt payroll allocation model, the 2025 payroll variance and the July benefits renewal.
- Austin, in the Structure Interview, 2026-08-30.
- [[00-Meta/daily-close/2026-09-18]] — the five Teams messages as read at the close; `00-Meta/daily-close/2026-09-19.md` question 3 and `2026-09-21.md` question 3 for the unanswered audit trail question. Added 2026-09-22.

