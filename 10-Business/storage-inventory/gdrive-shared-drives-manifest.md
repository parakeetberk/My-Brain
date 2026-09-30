# The four Google Shared Drives, pre-switch manifest

**What this is:** the top level of every Google Shared Drive reachable on 2026-09-03, captured **before** Austin moved the Drive connector from `austinrberk@gmail.com` to `austin@a2zcp.com`. It exists so that after the switch there is a checklist to test against rather than a memory.

**Status:** VERIFIED, every row returned by `search_files` on `parentId` this session. Captured 2026-09-03.

**Why this page exists in one sentence.** Austin, 2026-09-03: *"i am going to change the drive account to a2zcp. its important for document clean up and more."* **Shared Drive membership belongs to an account, not to a person**, so the switch does not automatically carry these four memberships across, and there is no way to enumerate memberships through the API to find out what was lost. **Without this page, a drive that goes dark after the switch is invisible rather than missing.**

## The test after the switch

Run `search_files` with `parentId` set to each root below. **Four roots return contents, nothing was lost. Any root that returns empty means `austin@a2zcp.com` is not a member of it** and either it gets added from the Drive UI or the connector goes back.

| Root ID | What it is | Top level count |
| --- | --- | --- |
| `0ANSvtCpaQmhVUk9PVA` | the community property drive | 32 |
| `0AHN7ilIBrGJRUk9PVA` | the Parakeet corporate and ops drive | 24 |
| `0AFtyceEG0HhKUk9PVA` | the A2Z fund, entity and investor drive | 7 |
| `0AJ8dOob9gR0HUk9PVA` | the A2Z and Bedrock entity layer | 8 |

**Four is a floor, not a total.** Memberships cannot be enumerated, so a fifth drive would be found the same way the fourth was, by accident. The pre-switch state is four.

## `0ANSvtCpaQmhVUk9PVA`: community property, 32 folders

`_Archive` · `Administrative` · `_Property Name (City, State)_Template`

Nine still carry the `____UPLOADED____` prefix, which is a migration marker left in place: **Mayflower (Plymouth, MA)** · **J Bar J Estates (Miami, FL) - Property Files** · **Bay Oaks I & II (Panama City, FL)** · **Mobile Manor (Rosedale, MD)** · **Royal Oaks (Vero Beach, FL)** · **Apple Creek (Bismarck, ND)** · **Westwood (Ormond Beach, FL)** · **Gulf Breeze (Hudson, FL)** · **Wolf Bay (Elberta, AL)**

The rest: Hunter Springs (Crystal River, FL) · Lake Wales (Lake Wales, FL) · Ormond Beach Oasis (Ormond Beach, FL) · Palm Spring Estates (Tarpon Springs, FL) · Cambridge (Charles Town, WV) · Journey's End (Okeechobee, FL) · Lambeth (Winston Salem, NC) · Cedar Grove (Kernersville, NC) · Colonial (New Bern, NC) · Parkwood (Winston Salem, NC) · Vandemere (Greenville, NC) · Royal Palm (Clewiston, FL) · Oceanaire (New Smyrna Beach, FL) · Everglades (Clewiston, FL) · Town and Country (Jacksonville, FL) · Countryside (Mandan, ND) · Lamberton Lake (Grand Rapids, MI) · Valley View (Roseburg, OR) · Shasta Glen (Klamath Falls, OR) · Parktown (Mandan, ND)

**Mayflower was touched 2026-04-07.** Every other folder here last moved in 2021 or 2022, so this drive is an archive with one live corner rather than a working surface.

## `0AHN7ilIBrGJRUk9PVA`: Parakeet corporate and ops, 24 items

Folders: `Community Maps` · `Mileage Logs` · `Admin Files` · `Strategy` · `Training` · `Communication` · `Corporate Files` · `Meetings & Check Ins` · `Properties` · `Human Resources` · `Investment Vehicles` · `Tollett Intro Info` · `Marketing` · `Investor Relations`

Loose files: `Bank Register_20211206122750750.pdf` · `AR Report for Ops Call.csv` · `Aged Receivables_20211206083818672.csv` · `omesite Violation Checklist (2).xls` · `Waiver and Release of Lien.pdf` · `Parakeet Directory.xlsx` · `Support Staff Duties-Parakeet[73] (1).docx` · `File & Folder Organization Outline.xlsx` · `Agreement to Demo Home_FL.docx` · `Business_Cap Ex Budget.xlsx`

**Nothing here has moved since December 2021.** `File & Folder Organization Outline.xlsx` is worth a look before the cleanup starts, since it is a prior attempt at the same job.

## `0AFtyceEG0HhKUk9PVA`: A2Z fund, entity and investor, 7 items

`Cap Tables` · `Investor Relations` · `BMHCII - InvestorsRelations` · `A2Z Fund I - Subscriptions` · `RealPage_IMS` · `Violet Smears` · loose `Investnext Investor Distribution Schedule.xlsx`

**This is the securities drive.** Beneath it, per the 2026-08-26 survey: subscription agreements naming individual trusts, K-1s, an LPA, certificates and articles of merger, and executed signature pages. `KP-0008`.

## `0AJ8dOob9gR0HUk9PVA`: A2Z and Bedrock entity layer, 8 folders

`Parakeet Companies` · `Mobile Management` (described as A2ZMHC) · `A2Z Community Partners` · **`Bedrock MHC Fund II`** · **`BEDROCK I GROUP`** · `A2Z MH Fund I` · `MoMa Lending` · `NewCo`

`Bedrock MHC Fund II` opens into `Accounting`, `Analysis`, `Entities`, `Holdings` and `Verivest Track Record_Bedrock MHC II.xlsx`. **Found 2026-09-03 and not in the 2026-08-26 survey.** `KP-0068`.

## Do this before the switch, not after

**Add `austin@a2zcp.com` as a Manager on all four drives from the Drive UI.** Membership is granted per drive and cannot be granted through this connector. **Done first, the switch loses nothing.** Done after, there is a window where nothing here can see any of it, and the only way back is to switch the connector again.

**A Shared Drive cannot be created by a consumer Gmail account**, so a Google Workspace owns each of these four. **Which Workspace is not known and was not assumed.** If it is the a2zcp.com Workspace, `austin@a2zcp.com` may already reach all four and the switch is a straight upgrade that also answers `KP-0008`. If it is a legacy or third party Workspace, membership has to be granted by whoever administers it. **INFERRED, and the four queries above settle it in one minute.**

## POST-SWITCH RESULT, 2026-09-03: all four pass, nothing lost

Austin switched the connector the same day. **The four query test was run immediately and every root returned contents.** VERIFIED.

| Root | Post-switch | Sample returned |
| --- | --- | --- |
| `0ANSvtCpaQmhVUk9PVA` | **PASS** | Everglades, Mayflower, Mobile Manor, Administrative, Gulf Breeze |
| `0AHN7ilIBrGJRUk9PVA` | **PASS** | Admin Files, Corporate Files, Properties, Human Resources, Communication |
| `0AFtyceEG0HhKUk9PVA` | **PASS** | all 7: `BMHCII - InvestorsRelations`, `Cap Tables`, `Investor Relations`, `Violet Smears`, `RealPage_IMS`, `A2Z Fund I - Subscriptions`, the Investnext schedule |
| `0AJ8dOob9gR0HUk9PVA` | **PASS** | all 8: `Bedrock MHC Fund II`, `Parakeet Companies`, `BEDROCK I GROUP`, `A2Z Community Partners`, `A2Z MH Fund I`, `Mobile Management`, `MoMa Lending`, `NewCo` |

**New identity:** `austin@a2zcp.com`, My Drive root `0ANBjF5CmkPsBUk9PVA`, ouid `115194717785561895747`.

### The result changes what `KP-0008` says, and it is worth reading carefully

**`austin@a2zcp.com` had access to these drives before today.** The rows come back carrying a `viewedByMeTime` for that account going back well before the switch: 2026-08-25 on the community drive and the ops drive, 2026-08-29 on `Bedrock MHC Fund II`, 2026-04-14 on `BMHCII - InvestorsRelations`, 2025 dates on several more. **A connector switch cannot create a view history.** So both accounts have been members all along.

**That falsifies one half of `KP-0008` and leaves the other half standing.**

- **False now: the continuity claim.** The row said that if the personal Gmail were lost or compromised, continuity would sit outside company control. **It would not. The corporate account reaches every one of these drives and always did.**
- **Still true, and now the whole of it: a consumer Gmail account holds standing membership in corporate Shared Drives** containing cap tables, fund subscriptions, K-1s, an LPA and executed signature pages. **That is a removal, not a migration**, which makes it a much cheaper fix than the row implied for two days.

**What this Brain got wrong and why.** The original survey walked in from the personal account, found the drives, and recorded them as reachable *only* that way. **Reachable from here was written down as reachable only from here.** Nothing ever tested the corporate account against them, because the corporate account was not connected. **This is rule 15's failure mode in connector form: a claim about the world made from the limits of one vantage point.**

### One thing did go dark, stated so nobody assumes coverage

**The personal My Drive is no longer visible.** A search for `Belmart` now returns zero, where before the switch it returned the full 9100 Belmart Road closing set: the ratified contract, the final disclosures, the EMD, the assignment and `Belmart Docs.zip`. Also gone from view: the Amex statement folder, the JLB Group financials at personal root, the Gilchrist financials, the 2015 investor contact list.

**This is consistent with Austin's *"nothing in personal"* ruling and is not a defect.** It is recorded because `KP-0066` and `TD-0489` are about where personal documents live, and **the answer for Belmart was "the personal Google Drive" right up until today.** `PD-40` and the personal section work both inherit this.

`Parakeet Brand guide.pdf` survives in three places, one of them owned by `austin@a2zcp.com` at My Drive root, so the brand asset is not affected.

## Related

- [[10-Business/connector-status]]
- [[10-Business/storage-inventory/gdrive-personal]]

## Sources

- Google Drive connector, `search_files` on each `parentId`, 2026-09-03, authenticated as `austinrberk@gmail.com`.
- Austin, in session 2026-09-03, quoted above.
