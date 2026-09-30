# Rent Manager

**What this is:** the system of record for every asset, resident, ledger, issue and document at Parakeet — the one system every documented process routes through.

**Status:** current — 2026-08-30

## The facts
- **What they supply:** Rent Manager, plus **Rent Manager Express** for leases. Between them they hold asset records and the UDF fields carrying lot due diligence (buildable envelope, door swing, electrical, water/sewer, placement notes); Issues and **the make ready board**; the **Prospect module**; **History & Notes** — the universal documentation target every SOP writes to; the AR report; the **TBD list**; the **Evictions tab** and the eviction workflow including account locking; the **Asset Transfer tab**; work orders; recurring charges and billing schedules; the **"GL — Total Cost" UDF** on rehab issues; the state notice template library; and **Tenant Web Access**, where residents run auto-pay.
- Rent Manager Express does lease generation and renewal: **click "Renew Lease," never "New Lease"** — New Lease duplicates the record and breaks tenancy history, named as one of the most common errors in the company. Each property has **its own lease template**; the digital path is Generate Lease Document → review merge fields → Publish → assign signers → track Published / Pending Approval / Signed (SOP 101).
- **Who uses it:** everyone. Community and District Managers (AR report, notices, work orders, History & Notes), Asset Management (asset status, rent amounts, TBD list, Issue creation), Operations, Construction (UDF due diligence, Issues > Infill), Sales (Prospect records and listing-feed UDFs), Accounting, the Evictions Team, and the Screening Coordinator — **AmRent screening runs only inside Rent Manager, never outside it** (SOP 006).
- **How critical: total.** It is named in nearly every one of the 24 documented processes, and the March board deck calls it "our **single source of truth** for all project-related and home inventory/home ordering information." **There is no documented fallback for any process** — no manual path, no secondary system, nothing. If it vanished tomorrow the company stops the same day.
- **Four hard gates are literally Rent Manager records:** "No Rent Manager issue = no work starts" after the TBD Call (SOP 104) · "No Rent Manager record = no work starts" at vendor rehab kickoff (SOP 105) · no internal rehab charge may be booked until a valid issue number exists and the Director of Operations has entered GL codes in the "GL — Total Cost" UDF (SOP 105b) · the home's serial number must be in Rent Manager before delivery day (SOP 001, Gate 2).
- Asset status path on a new home: ORDERED → In Storage → DELIVERED → Active → LOT–Avail (SOP 001). **Statuses flip off dates entered in the system — never hand-set a status** (SOP 104). Asset Management updates Rent Manager **within 24 hours** of any home date change (SOP 001).
- Regional site-visit action items are entered as Rent Manager tasks tagged **"30-Day Site Visit Follow-Up"** with due dates, before the end of the week of the visit (SOP 106).
- **Account locking:** the Evictions Team places a resident under the Eviction workflow and locks the account so no online payments can be made. Only the Evictions Team and the Director of Operations may unlock it (SOP 107) — the legacy `800-eviction_sop.docx` says Asset Management can, and that conflict is unresolved.
- The Asset Transfer tab is where every title outcome lands — POH sale (SOP 005), post-eviction auction and resident turn-in — alongside the resident profile and the Assets tab.
- **Known system gap 1:** Accounting receives **no system notification when a lease is activated**, so Asset Management updates the billing schedule manually and the Community Manager must confirm with them that it happened (SOP 101).
- **Known system gap 2 — the GL is the replaceable half.** The 2026-08-21 Rellit conversation concluded that resident ledgers, payments and records must stay in Rent Manager — "the majority of residents pay online and it attaches to all their records, so that can't be changed" — while **the general ledger sitting inside Rent Manager is open to replacement**, pulled out by API, to reach a live close.
- The same call put a number on the pain: books close **30 to 45 days in arrears**, so Ramp card spend that was once reviewed weekly is now booked once a month.
- Internal rehab cost tracking is blocked on an **unconfigured accounting GL pull**: SOP 104's data-entry standard instructs staff to leave build cost blank indefinitely and rely on the Home Depot / Lowe's memo convention instead, and 105b's GL codes are all placeholder `[GL-XXXX]`.
- The 2026-08-24 MAV session left open **which system is the single source of truth for prospecting and lead data — the CRM or Rent Manager** — and agreed the MCP sandbox would be built on real CRM data but deliberately **not connected to the live Rent Manager account**.
- **The 600–699 Systems / IT / Reporting SOP band is empty.** The system every process depends on has no SOP of its own — no access control, no permissions, no data standards, no admin procedure anywhere in 242 process files.

## Decisions
- 2026-08-21 — Rent Manager stays for resident ledgers, payments and records; the general ledger is the piece open to replacement, pulled by API, with a live close as the standard. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-rellit-conversation]])
- 2026-08-24 — Reporting moves to a daily RentViewer sync into the data warehouse instead of manual backup pulls, with everything reachable through Claude over the warehouse. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-mav-and-parakeet]])

## Sources
- [[70-Operations/sops/sop-library]] — the process library; Rent Manager and Rent Manager Express are named as the system of record in nearly every documented process.
- [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-rellit-conversation]] — the resident-ledger / general-ledger split and the 30-to-45-day close lag.
- Austin, in the Structure Interview, 2026-08-30.
