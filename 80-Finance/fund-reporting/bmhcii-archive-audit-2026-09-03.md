# BMHCII archive audit, 2026-09-03

**What this is:** the full audit of whether the Bedrock MHC Fund II memorialization archive at Dropbox `/Austin Berk/BMHCII` is accurate and complete, and the three remediation paths with the recommendation. Run by a fourteen agent team: five lead auditors each spawning sub agents, an adversarial challenge pass per lane, three independent solution architects, one judge. 509 tool calls.

**Status:** current, 2026-09-03. Every count below is from a listing or an opened file. **Counts are floors where the audit says so.**

**The standard being measured against:** Austin, 2026-09-03, *"the dropbox one is the one we will post the final, approved documents for memorialization."*

## The answer

**Not accurate. Completeness not established, and unproven in both directions.** Those are different failures and they need different fixes.

**The container is sound.** 181 folders, 1,513 files, 1.29 GB, walked to full depth with every listing confirmed complete. Section 1 holds 192 files across 8 sub folders, 267.1 MB, of which `1.8 Subscription Agreements` alone is 179 files and 204,703,717 bytes. Section 2 holds 64 files, 158.0 MB. `4.5 Tax Returns` holds 989 files.

**What fails is the link between a filename and the document behind it.** Fewer than 150 of the 1,513 files were opened, under 10%, and **every file opened in 1.8 specifically to test whether its name matched its contents failed the test.**

## Accuracy: fails. VERIFIED, by independent passes that opened the same files and agreed.

**Files that assert one investor and contain another.** All confirmed by opening:

| Filename | What it actually is |
| --- | --- |
| `Thien_Quach_-_Bedrock_MHC_Fund_II.pdf` | Michael Mitchell's Letter of Accreditation |
| `MIchael Mitchell_Accreditation.pdf` | Khodara's subscription package |
| `BEDROCK_..._Batzer(1).pdf` | Bernard Schachter's countersigned booklet |
| `B Batzer Sub Docs.pdf` | Jim Folliard's executed side letter, byte identical to `Side Letter_Folliard.pdf` |
| `Marie_Yvonne_Khodara_-_Bedrock_MHC_Fund_II.pdf` | John G Christian's side letter |
| `BEDROCK_..._Folliard.pdf` | Triangle Ventures LLC's booklet |
| `VerifyInvestor-inari-llc_cF3Qycz.pdf` | Bernard Schachter's executed subscription package |
| `Taub_Sub Docs_LPA.pdf` and `CAROL L LEE.pdf` | byte identical to each other, and **neither is an LPA nor a Carol Lee document**: an unsigned, undated side letter template naming Matt Aven and Slab Holdings |
| `BEDROCK_..._Osborne.pdf` | no Osborne content at all. The genuine completed Osborne package is `Osborne(1).pdf`, from a different e signature platform |

**Roughly two dozen files are now confirmed wrong about the investor, the document type, or both.**

**Extension and type are also unreliable.** `Quad G ACH Form.pdf` is a 64 byte Windows Internet Shortcut containing a mailto link, not a document at all. `#.url` is a 2,156,407 byte executed DocuSign PDF carrying Michael Loveland's side letter, under a filename no human or extension based tool would open. `Committments.xlsx` is a DocuSign Certificate of Completion, envelope 54B0843F, 80 pages, signers Brian Mikalis, Tifanie Mikalis and Austin Berk, completed 2018-11-28. **Not one of the fifteen readable `Signed_Side_Letter_*` files is a side letter**, and the `fw9_` prefix is wrong at least a third of the time. `Bedrock MHC Fund II LP Limited Partnership A&R.pdf` is not an A&R: it is the **unexecuted, undated First Amendment with all four signature lines blank.**

**Duplicates are not what they looked like, and that cuts both ways.** 39 duplicate byte size groups cover 80 files, 45% of 1.8. **But the four Ebert files are four genuinely different documents, not copies**, and the fully countersigned booklet is `Ebert(1).pdf` rather than `Ebert.pdf`. **A near identical name hiding a different document is worse than a duplicate**, and both are present here.

**The mechanism is known, and it is the most useful finding in the audit.** The upstream per investor tree at `ns:5655481408` is the intact index: Loveland's W-9 under Michael Loveland, Kahn's accreditation under Maria Kahn. **Every one of the 40 opaque vault files has a same size counterpart under a named investor folder there.** The name permutation was introduced when material was bulk copied into 1.8. **Some copies are also truncated**: Quach at 35,732 bytes against 463,119 intact upstream; CS Partners IV at 44,267 against 670,054. **Files in that band extract to zero text.** That is data loss, not naming.

**The opaque set is smaller and better than first reported.** 40 files, not 52. They resolve to only **11 distinct investors, and 14 of the 40 are one investor, Bernard Schachter.** So it is largely a redundancy artefact rather than 40 lost records. **The exception is the Langley cluster: 1.8 holds no Langley named subscription agreement, so three opaque files are the sole identifiable copy of the Langley executed package in that folder.** Ten files could not be attributed at all and eight of those have no text layer.

**Five files are artefacts of a VOIDED DocuSign envelope** and must not be memorialized as executed documents.

## Live data exposure, and this is the one to act on today

**Three ACH authorization forms carrying bank routing and account credentials are filed in `1. Governing Documents` under names that give no warning of their contents.** 1.8 is the folder handed to LPs and counsel for subscription review. **A books and records production from that folder as it stands hands a hostile partner other investors' banking details.** No field values were transcribed anywhere in this audit or into this page.

## Completeness: not established, and the gap list is the least reliable part of the audit

**Treat every "missing" finding as a floor from an unfinished search.** The challenge pass killed roughly a dozen of them, including two that matter: **`4.1 General Ledger` exists with 72 files and 46.9 MB**, and **an entire `4.5 Tax Returns` section holds 989 files** that the estate brief omitted outright. **Section 4 had been undercounted by about 95% of its file count.** Also found after being reported missing: Quach's intact booklet, Batzer's package, Khodara's countersigned RealCrowd package, Inari and Langley's subscription agreement and accreditation letter correctly named in 1.8, W-9s and ACH authorizations present in quantity, LP counterpart signature pages bound inside the combined booklets as Exhibit B, and six of the ten files declared functionally lost.

### Genuinely absent, on the GP's own work papers rather than inference

- **The seven executed transfer instruments and the General Partner's written consent** for the CS Partners IV admissions of accounts 1063 to 1069 effective 2022-01-01. **Those seven limited partners have no subscription agreement, joinder, LP counterpart, accreditation or transfer instrument anywhere reachable.**
- **The five additional subscription agreements and GP acceptances totalling $498,548** between 01/2019 and 07/2020.
- **The 2020 assignment instrument and GP consent for the account 1034 interest transferred to WCO Capital.** The investor register was never corrected and **distributions have been paid under the transferor's name from 2020 forward.**
- **Twelve investors have no subscription agreement anywhere**, vault or older tree. Five of those are not transferees, so they are primary subscriptions with no executed evidence on file.

### Self declared absent by the vault's own placeholder notes, owner named as Austin

`3.6` mortgage payoff statements. `4.4` fund organizational documents. **Section 6's GP, Investment Manager and PM fee schedules, collections support, banking, tax and use of proceeds support, which are precisely the sections Murad's request names.** `2.4 Transfer-Assignment Documentation` contains nothing but a draft and **zero final documents.** Twelve sub folders are completely empty: eleven entity folders in `3.1` and one property bank account folder in `4.2`.

### Structurally absent, no folder exists at all

Audited or reviewed financial statements. Fund financial statements. **The fund demonstrably engaged RSM to audit FY2018 and the engagement letter plus a full PBC file exist only in the old tree, with no audit report found anywhere.** IRA custodian annual valuations. Property management agreements. Insurance. **GP written consents and resolutions.** E file authorizations. Litigation. The distribution waterfall calculation workbooks. **A W-9 home**, despite the fund having demanded one from every partner.

### Absent at file level

**2025 final Schedule K-1s do not exist.** 68 per investor draft letters dated 2026-08-06 stand in their place, and one carries a header reading CY ended 12/31/25 against body text reading tax year ended December 31, 2024. **Twelve days to the 2026-09-15 deadline.** All three Wolf Bay entity formation folders empty, for a property with 46 bank statements. `4.2/Property Accounts/Cedar Grove` zero files. NCHOMES, LBHOM and SC ledgers delivered as 109 byte header only CSVs. **No Q4 2024, Q4 2025 or Q1 2026 LP quarterly update exists in any Dropbox namespace.** `BMHCII Quarterly Update Q12020.pdf` and `March 2020 Coronavirus & Tax Update.pdf` are the same document stored twice, and its content is an ad hoc Coronavirus and K-1 letter rather than a quarterly update. **And the 2026-05-08 "Bedrock MHC Fund II LP Summary", the document that triggered Murad's demand, exists nowhere in Dropbox and survives only as a Gmail attachment.**

### The search space was never closed

**Box**, named in a 2021-01-03 message as holding *"Both Investor ALL docs including KYC"*, appears in no estate map anywhere. **InvestNext**, the actual delivery channel for K-1s, draft returns and capital account documents, was never reached and holds the per investor access log that is the only evidence of what each LP was actually sent and when. **The Dropbox Space created 2026-05-13 for the Murad production** was never enumerated. Nor was the MickLaw DDQ tree.

## The clock nobody had written down

**Murad's demand was served through counsel on 2026-05-10 with a subpoena mentioned in writing, and Donna Etemadi was still chasing the production link on 2026-06-04.** Austin stated an invite to the Dropbox Space was sent; both recipients said they never received it. **Four months of silence toward a 33% partner's counsel is the most sanctionable fact in this file, and it is cured by answering rather than by finishing the archive.** `CM-26`.

## The three paths

| | **Freeze and Attest** | **One Door, One Name** | **Order the Originals** |
| --- | --- | --- | --- |
| **The bet** | A hostile reader punishes concealment, not disorder | It is an intake problem, not a cleanup problem | Stop grading the photocopy, re request the originals |
| **What it does** | Freeze the vault, hash manifest it, issue a signed Statement of Archive Contents and Known Gaps naming every hole with an owner, and close the four items with legal consequence | One written promotion standard, one naming grammar, one physical `_INTAKE` door. Prove it on the 68 K-1 finals landing in twelve days, then push the backlog back through the same door | Re request every document class from whoever holds the original: DocuSign and RealCrowd, Citrin, the banks, the QI, title, counsel |
| **Effort** | ~2 weeks. Berman 5 to 7 days, Austin ~2 days, Albert ~1.5 days | Gate live in 5 days. 1.8 clean in 3 weeks. Full backlog 4 to 6 weeks. Standing cost ~1 hour a month | 10 to 16 weeks, schedule owned by third parties. Tax and register lanes usable in 4 to 6 |
| **Residual risk** | **The fund still cannot produce a per investor completeness matrix, and the signed statement says so** | Governs the vault only. Box, InvestNext, the Murad Space and the diligence trees stay outside the door, and a well named vault will look complete while they do | **If the 2018 envelope archive has been purged, three months buys the same corrupted files plus a better documented list of absences** |
| **Fails if** | Khodara actually files and an examiner opens a file. The signed statement inverts from shield to roadmap. **Its trigger is already partly live** | Austin does not personally use the door. Dated test: if the K-1 finals land anywhere but `_INTAKE`, it is decorative | The third party relationships are already dead. **It has no fallback by design** |

## Recommended: One Door, One Name

**It is the only path that produces the thing a partner with a grievance actually asks for, and the only one that leaves a system behind when Austin stops looking at it.**

**Murad's request is sectioned by party and entity. Khodara's grievance is about whose name a distribution was paid under for six years. Both are per party questions.** One Door's promotion register carries one row per file with party resolved through a canonical party register, document type, date, execution state, and the identity evidence that fixed it. **That register is a per investor completeness matrix as a byproduct.** Three weeks out, "which document does this investor have, and how do you know" gets answered with a citation.

**Freeze and Attest cannot, and concedes it in its own residual risk.** That is Austin signing a document, in front of the person most motivated to exploit it, conceding he cannot answer the central question, **while the answer is three weeks and one worksheet away.** Honest disclosure of an irreducible gap is a shield. A disclosed decision not to do cheap work is not.

**Order the Originals has the right instinct pointed at the wrong source.** The originals for the class that matters most are not at DocuSign. They are at `ns:5655481408`, inside Dropbox, intact, correctly named, reachable today. **It spends 10 to 16 weeks and a retention gamble to obtain what a byte join plus 179 file opens produces in three.** It also cannot meet the clock: its first output is a schedule of letters to other people.

**Three more specifics.** One Door has the correct theory of the defect and shuts off the mechanism, because the damage was introduced at bulk copy time and nothing enters a numbered section again except through `_INTAKE` opened by a human. **It is the only path that addresses the ACH and W-9 exposure**, creating a restricted `1.9` and moving them, where Freeze and Attest only revokes links. And it is **timed to the inflow**, so the 68 finals arrive compliant instead of adding 68 more bad filenames.

**The honest risk: renaming roughly 1,500 files while under a books and records demand can read as a party editing its own records.** That is not a reason to reject the path. It is why the hash manifest is action one and is not optional.

## Grafted onto the recommendation

From **Freeze and Attest**: the pre remediation snapshot and SHA-256 manifest before a single rename, stored outside the working tree, **non negotiable**; the signed Statement of Archive Contents and Known Gaps, but issued at the **end** of the 1.8 pass so it says here is the matrix rather than we cannot produce one; the share link audit on day one, because every link already issued still points at 1.8; saving the 2026-05-08 LP Summary out of Gmail with its send date, recipient list and message ID, plus version pinned exports of the `BMHCII Calcs` and `BEDROCK MHC FUND II CALCS` Sheets whose arithmetic the dispute turns on; retrieving WP-36 and WP-38 first; and **answering Murad section by section now, through counsel, without waiting for the archive to be finished.**

From **Order the Originals**: the **source of record register** as front matter to the promotion register, one line per document class naming the institution that holds the original; the **accounts payable method** for resolving unassigned owners, searching the bank statements and general ledger for payments to the QI, the administrator, title agents, the insurance broker and the law firms, because nobody currently knows who the fund's QI or insurance broker was and the AP trail names them; pulling the **Form D from EDGAR**, because Item 6 states the exemption actually claimed and settles whether third party accreditation verification was required of every investor; ordering **Citrin's filed return package** including the K-1 recipient population per year, which is the partner register as actually filed, scheduled after 9/15; requesting the **QI's complete exchange file** and the title closing files, oldest first, since title retention is the one clock running independently; and ordering **full bank account histories** account by account, naming Cedar Grove and Westwood explicitly.

## Related

- [[80-Finance/fund-reporting/bedrock-fund-ii-winddown]]
- [[00-Meta/commitments]] `CM-25`, `CM-26`

## Sources

- Fourteen agent audit, 2026-09-03, run against Dropbox namespace `15029193027` and the cross source locations on [[10-Business/connector-status]]. Five survey lanes, adversarial challenge per lane, three solution architects, one judge. 509 tool calls, 2.87M tokens.
- Austin, in session 2026-09-03, quoted above.
