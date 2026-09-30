# Berk Inc — Entity Map

**What this is:** The three identity and storage domains Austin operates across, and the open question of how they legally relate.

**Status:** needs review - content is as of 2026-08-26; filed into this Brain 2026-08-31 from the second vault dropped in `05-Inbox/`. Nothing here has been re-verified since 2026-08-26.

**Confidence labels on this page are the source's own:** VERIFIED (primary source read), SINGLE-SOURCE (one place, unconfirmed), INFERRED (reasoned, not returned directly).

**Status**: OPEN QUESTION. This is the highest-value unknown in the vault.
**Created**: 2026-08-26
**Owner, set 2026-08-31**: **Austin, and it is not delegable.** He said so on the delegation board, which had listed it as a candidate to hand off. Only he holds how the three domains relate, so anyone else building this map would be guessing at the answer rather than recording it. `00-Meta/commitments.md` item 6 moves from unowned to Austin.

## What we know

Austin operates across three distinct identity and storage domains. Nothing currently maps how they legally or operationally relate.

| Org | Storage | Identity | Evidence |
|---|---|---|---|
| Parakeet Communities | Microsoft 365 (SharePoint + OneDrive) | austin@parakeetcommunities.com | Primary operating tenant, `/sites/main` |
| A2Z MHC | Dropbox team, namespace `11855305057` | austin@a2zcp.com | Team space with Corporate, Pipeline, Accounting mounts |
| Personal | Google Drive | austinrberk@gmail.com | Mixed personal and shared-in |

"Berk Inc" is Austin's informal umbrella term across all three. Whether it corresponds to a real holding entity is unconfirmed.

## Affiliates and related names seen in the wild

Surfaced while surveying storage on 2026-08-26 — each needs to be placed in the structure:

- **Parakeet Communities** — operating company, community ownership and management
- **Parakeet Homes** — home sales arm; buys from manufacturers, sells to residents
- **A2Z MHC** — separate Dropbox tenant, purpose unconfirmed
- **Jadian** — appears in `Parakeet - Jadian Quarterly Valuation Figures - 06302023.xlsx` and `2024 Capex Budget Tracker - Jadian Properties v2ab.xlsx`. Likely a capital partner or co-investment vehicle.
- **BMHC II** — appears in `BMHCII_General Ledger Analysis_01172022.xlsx`, `BMHCII_Payment Analysis_01172022.xlsx`, `BMHCIIQ32021 Letter.docx`. Fund entity, roman-numeral suffix suggests a series.
- **Fund II / KEY Fund II** — `FUNDIICSV.csv`, `KEY FundII June.csv`
- **GKFC / GKRV** — `GKFC Aloha Daily Sales Journal Workbook.xlsx`, `GKFC Deposits.csv`, `GKRV_02282024.csv`. Possibly an RV or separate asset class.
- **Fox Creek Inc / A S C Corp** — SharePoint `Accounting & Finance/Monthly Close/07212026 SCANS/FOX CREEK INC A S C CORP`
- **Cambridge (SCH 2025)** — Dropbox mount, active 2025-08
- **Varian** — OneDrive `2.0 Varian Expense`

## Known communities and properties

Confirmed from storage paths as of 2026-08-26. Not exhaustive — the `sharepoint-main` inventory will complete this.

- Bay Oaks Village I and II (BOVI / BOVII)
- Auburn Ridge (Auburn, GA)
- Terrace Crossing (Thonotosassa, FL)
- Palm Haven Estates (Panama City, FL)
- Harbour
- Crystal Acres
- Lamberton Lake — **active sale, 2026**
- Great Oaks
- Lake Saunders
- Oceanaire
- Lake Wales
- River Oaks

## Counterparties and advisors seen

- **Cavco Homes** — manufacturer, dedicated SharePoint site `/sites/ParakeetHomes-ParakeetHomesxCavco`
- **Gray Robinson P.A.** — legal, invoices under Parakeet Audit 2024
- **KeyBank** — `KeyBank Update_102021.docx`
- **StepStone** — `StepStone Real Estate House Views Report - Fall 2024.PDF`
- **Kippy** — diligence counterparty, `External/Kippy DD/Crystal Acres`
- **Bedrock** — `VP Finance Search Bedrock.Parakeet.docx`, likely a search firm

## Source documents to reconcile

These exist and should resolve most of the above. All currently unfiled at OneDrive root:

- `Parakeet & Affiliates Org Chart.vsdx`
- `corporate org.csv`
- `Org Chart Overview_122023.xlsx`
- `Parakeet Cap Table 2023.xlsx`
- `comm structure.xlsx`
- `canva holdings.xlsx`
- Dropbox `ns:11855305057//Corporate` (contents pending inventory)

## The consolidated map exists — found 2026-08-26

**`ns:11855305057//Austin Berk/Org Chart Overview.xlsx`** (Dropbox) is the only consolidated entity map found anywhere across all surfaces. Eleven tabs covering:

- **A2Z Community Partners** — the Maryland hold-co, top of the structure. **Austin's own words, 2026-08-31:** *"a2zcp.com is my entity that ran everything prior to parakeet. both bedrock and a2zfund i. a2z is my holding company."* Confirmed again the same evening: *"a2zcp.com is the website and url for a2z community partners."* **So the domain-to-entity mapping is VERIFIED from Austin and no longer inferred from an email address.**

**What that confirmation does not settle, and it matters for the credential work:** he confirmed the domain belongs to the entity. **He did not say the mail tenant on it is actively administered.** `accounting@a2zcp.com` and `winnie@a2zcp.com` are still open questions on that count, and Winnie Bretz is a departed employee. Recorded per rule 15 in reverse: the answer to a narrower question is not evidence on a wider one. **So A2Z is not a legacy curiosity, it is the prior generation of this business**, and it sits above both Bedrock (including Bedrock MHC Fund II, which owned the Origins portfolio) and A2Z Mobile Home Fund I. **The operational consequence, found the same evening: the identity layer never migrated when the entities did.** `A2Z Utility Logins.xlsx` has **eleven live utility and telecom logins running through `accounting@a2zcp.com` and `winnie@a2zcp.com`**, and they are not confined to legacy assets — they cover Origins properties (Gulf Breeze, Westwood) and a Kippy-vehicle property (Crystal Acres) as well as Lamberton Lake, Apple Creek, Cambridge and Mayflower Hills. **`winnie@a2zcp.com` belongs to a departed employee.** Detail at [[10-Business/sharepoint/a2z-utility-logins-exposure]].
- **BEDROCK I GROUP**
- **Bedrock MHC Fund II LP / GP**
- Seven deal-level ownership charts
- Employee org chart
- The operating-company split
- Domiciles, ownership percentages, **EINs**, and **58 named LP investors**

**Caveats, and they are serious**: it is dated 2020 — six years stale. It has broken formula columns. And it sits ungoverned in a personal folder inside a Dropbox tenant that is otherwise cold storage.

Formation packets for five management LLCs sit separately at `ns:11855305057//Business Lines/A2ZMHC/Entities/`.

Related but distinct sources still unread: `Org Chart Overview_122023.xlsx` (OneDrive root, likely a 2023 refresh of the same workbook — reconcile the two), `Parakeet & Affiliates Org Chart.vsdx`, `Parakeet Cap Table 2023.xlsx`.

## Next action

Read `Org Chart Overview.xlsx` (2020, Dropbox) against `Org Chart Overview_122023.xlsx` (2023, OneDrive root) and produce a current, governed entity structure in this file. Treat the 2020 workbook as the skeleton and the 2023 file as the delta. Flag anything that changed after 2023 as unknown rather than assuming continuity.
