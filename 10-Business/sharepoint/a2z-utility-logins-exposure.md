# A2Z Utility Logins — what is actually in the file

**What this is:** the contents analysis of `A2Z Utility Logins.xlsx`, the plaintext credential store that has sat at the top of [[00-Meta/commitments]] item 2 since 2026-08-26. Austin asked on 2026-08-31 what credentials were in it. **Until now nobody knew** — every prior entry in this vault said the file was "identified by name and location" and "not opened", and the drafted email to IT at `10-Business/sharepoint/drafts/draft-it-credential-rotation.md` still says so.

**Status:** read in full 2026-08-31 via the Microsoft 365 connector. **VERIFIED.**

**No password, security code or security-question answer appears on this page, deliberately.** Copying secrets out of one badly-secured file into a second badly-secured file makes the exposure worse, not better. What follows is the inventory and the pattern. The secrets stay in the source file until it is destroyed.

## The file

- **Location:** `/Attachments/A2Z Utility Logins.xlsx` in Austin's OneDrive (`austin@parakeetcommunities.com`). One worksheet, 42 rows, 8 columns.
- **38 credential rows.** Columns are Property Name, Provider Name, Username, Password, Extra, URL, and a notes column headed `1/29 Notes:`.
- **Last modified 2024-01-31.** The notes column records a login test run around 29 January, presumably 2024.
- **Roughly 25 named properties**, some rows covering several at once (one Duke Energy row covers Applegate, Paradise Lakes, Lake Wales, Lake Saunders and Palm Springs Estates; one Waste Management row covers Cambridge, Crystal Acres and Mayflower Hills).
- **Providers are utilities, waste and telecom:** Duke Energy, FPL, TECO, Spectrum, CenturyLink, GFL, Republic Services, Waste Management, Waste Pro, Coastal Waste, Nates Sanitation, Midco, Montana-Dakota, Capital Electric Cooperative, Riviera Utilities, OUA, and eight municipal utility portals.

## The five findings, worst first

**1. Password reuse is the exposure, not the file.** Three password roots and their punctuation variants account for **21 of the 38 rows**. One root appears on **13** accounts in five spellings, a second on **6**, a third on **2**. **Rotating "every credential in this file" is the wrong instruction** — it treats 38 unrelated secrets as the unit of work when in fact three secrets are, and those three are almost certainly in use on systems that are not in this file and not utility portals. **The question to answer first is where else those roots are used.** Nothing in this vault can answer it.

**2. Four shared service accounts are the identity layer underneath all of it.** `accounting@a2zcp.com`, `accounting@parakeetcommunities.com`, `homeoffice@parakeetcommunities.com` and `winnie@a2zcp.com` are the usernames on most rows. **Two of the four are on `a2zcp.com`, Austin's own legacy holding company, and one of those two belongs to a departed employee** — see finding 5. **If any of those mailbox passwords is one of the reused roots, the mailboxes are the breach, not the trash bills.** The remaining rows use per-property usernames (`royaloaks`, `oceanaire`, `luckyclovermhc`, `countrysidemhc`, `whisperingpinesparakeet`, `triplesmarina2`, `paradiselakesrvpark`, `ndcommunities`, `parakeet`, `parakeetcommunities`).

**3. This is not a file at rest. SharePoint search returns the passwords without opening it.** A connector search for "A2Z Utility Logins" on 2026-08-31 came back with a **live password inside the result preview snippet**, before any read call was made. **So the exposure surface is everyone who can search that OneDrive, not everyone who can find and open that file**, and it means the file's contents have been reachable to indexing infrastructure since 2024. **The drafted IT email's central caveat, "its contents were not opened", is now both untrue and beside the point** and that draft needs rewriting before it is sent.

**4. One row is full account-takeover material, not just a login.** The Spectrum row for Triple S Marina carries the account number, **the account security code, and the answer to the account security question**, alongside the password. That combination defeats a phone-based identity check at the carrier. It is the only row with that much in it, and it is the one to treat as a discrete incident.

**5. CORRECTED 2026-08-31 by Austin, and the corrected version is worse than the original claim.** This page first said the `a2zcp.com` rows sat under "another company's domain" that Parakeet "may not control". **Wrong, and wrong against three pages already in this vault.** Austin: *"a2zcp.com is my entity that ran everything prior to parakeet. both bedrock and a2zfund i. a2z is my holding company."* [[10-Business/entity-structure/berk-inc-umbrella]] already recorded **A2Z Community Partners** as *"the Maryland hold-co, top of the structure"*, [[10-Business/entity-structure/entity-map]] already carried a whole **"Tier 4 — A2Z legacy"** section, and the same umbrella page already listed `austin@a2zcp.com` as the owner of the A2Z Dropbox tenant. **The original claim is kept visible because it stood for about an hour and because it is the third instance tonight of this vault contradicting a fact it already held.**

**So rotation is entirely within Austin's control. That is the good news and it is the smaller half.** The real finding is what the domain being *legacy* means:

- **`winnie@a2zcp.com` is a departed employee's address.** [[10-Business/storage-inventory/dropbox-a2z]] lists **Winnie Bretz** among four departed-staff folders in the A2Z Dropbox tenant, hers containing an entire nested `BEDROCK I GROUP` corporate tree. She is on **two** rows here as the username of record — the City of Mandan smarthub portal and Riviera Utilities. **A departed employee's account on a wound-down entity's domain, still the login of record on live utility portals, is a worse position than a third party's mailbox**, because a third party at least has someone administering it.
- **The identity layer never migrated when Parakeet took over.** Eleven rows run through `a2zcp.com` and they are not confined to legacy assets. They cover **Lamberton Lake** (a Fund II remaining asset, consistent with A2Z Lamberton Lakes LLC existing), but also **Gulf Breeze and Westwood**, which are Origins, **Crystal Acres**, which sits under the Kippy vehicle, and **Apple Creek, Cambridge and Mayflower Hills**. **The entities changed and the logins did not follow.** That is the fact worth carrying off this page.
- **The question to ask is not who controls the domain, it is whether anyone is still administering it.** A holding-company tenant for wound-down structures, holding live credentials, with at least one orphaned named account on it. Nothing in this vault says who watches `a2zcp.com` today, whether it still has an admin, or whether Winnie's account was ever disabled.
- **This lands on the Berman revocation too**, for the same reason as the shared mailboxes: a revocation exercise scoped to Parakeet's tenant does not reach a legacy tenant that is still the identity of record on live billing portals.

## The collision with the Berman exit, and it is live

[[00-Meta/commitments]] item 16 revoked Berman's access on 2026-08-31, with Austin's own instruction *"ALL BANK ACCOUNTS."* **Disabling a named individual account does not rotate a shared service-account password.** If any of these four shared logins were known to him, or if the reused roots are also on systems he used, then the revocation is incomplete and nobody has looked. **This is not an accusation of anything.** It is the standard consequence of shared credentials meeting a departure, and it is the reason item 2 and item 16 should be worked in the same conversation rather than as two separate rows.

## What is actually stale

**15 of the 38 rows were marked "Invalid Login" at the January test**, one records a login that requires MFA, one an unresolved portal error, and one notes the username format is wrong. **So a little under half were already dead eighteen months ago and roughly 20 were confirmed working.** Staleness cuts both ways here: it means the rotation list is shorter than 38, and it means nobody has verified the file in eighteen months, so "invalid" is not evidence a credential is retired at the provider.

## What this changes on item 2

The next action was "rotate every credential in that spreadsheet, then delete it." **That is still right and it is no longer sufficient.** The sequence that follows from the contents:

1. **Find out where the three reused roots are used outside this file**, starting with the four shared mailboxes. This is the only step that addresses the actual exposure.
2. **Treat the Triple S Marina Spectrum account as its own item** — password plus security code plus security answer needs the carrier called, not a portal reset.
3. **Establish whether anyone still administers the `a2zcp.com` tenant, and whether Winnie Bretz's account was ever disabled.** Not who controls it — Austin does, it is his holding company. The question is whether a wound-down entity's tenant still has an admin, and whether a departed employee's account on it is still live and still the login of record on two utility portals.
4. **Rewrite the IT email** at `10-Business/sharepoint/drafts/draft-it-credential-rotation.md`, whose premise is that the contents are unknown.
5. **Then** rotate, then destroy the file, then check for copies — the `Attachments` folder is an email auto-capture location, so duplicates are likely and search indexing means copies may exist outside it.
6. **Confirm the shared-credential question against the Berman revocation** before item 16 is treated as closed on access.

## Sources

- `A2Z Utility Logins.xlsx`, `/Attachments/` in Austin's OneDrive, read in full 2026-08-31. Last modified 2024-01-31.
- Austin, 2026-08-31, asking what credentials the file held — which is what prompted the read.
- [[10-Business/storage-inventory/onedrive-austin]] finding 6, which named the file and did not open it.
- [[00-Meta/commitments]] items 2 and 16.
