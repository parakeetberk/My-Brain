> **DO NOT SEND AS WRITTEN. Superseded 2026-08-31.** This draft's central caveat — *"Its contents were not opened"* — is no longer true and was never the right frame. The file has been read: **38 rows, three reused password roots covering 21 of them, four shared service mailboxes as the identity layer, and a live password returned by SharePoint search without the file being opened at all.** Ask 1 below ("rotate the credentials for every A2Z utility account") treats 38 unrelated secrets as the unit of work when the real unit is three. **Rewrite from [[10-Business/sharepoint/a2z-utility-logins-exposure]] before sending.** Kept unaltered because it stood from 2026-08-26 and is the record of what was believed for five days.

# DRAFT — Credential rotation request to IT

**Status**: Not sent. Review, fill the recipient, send from your own mail client.
**Drafted**: 2026-08-26

---

**To**: [IT lead / MSP]
**Subject**: Credential rotation needed — plaintext login file on OneDrive

---

We ran a full audit of our cloud storage this week and it turned up a file that needs immediate attention.

**The file**

`A2Z Utility Logins.xlsx`, in the `Attachments` folder of my OneDrive (austin@parakeetcommunities.com).

To be precise about what we know: the file was identified by name and location during an automated inventory. **Its contents were not opened.** But the name is explicit enough that I want it treated as a live exposure rather than investigated first.

**What I need**

1. Rotate the credentials for every A2Z utility account. Assume all of them are in that file until you can confirm otherwise.
2. Once rotation is confirmed, delete the file — not to the recycle bin, permanently.
3. Check whether it was ever shared, synced to a personal device, or copied elsewhere. The `Attachments` folder is an auto-capture location for email attachments, so there may be duplicates.
4. Tell me what the right storage is going forward. We should be in a password manager, not a spreadsheet.

**Separate but related**

The same audit found other material on the corporate tenant that shouldn't be there. Lower urgency than the credentials, but I want it on your radar as a remediation list:

- Government ID and passport images (`Teams Chat Files/Berk_ID.pdf`, `Desktop/berk passport.jpg`)
- A third party's wage-garnishment record
- Nine resident and employee PII screenshots scattered across an auto-capture folder
- Individually-named K-1s in five separate locations
- Two confidentiality-marked legal documents loose in a downloads folder
- Family medical records, including a Cleveland Clinic PDF and a vaccination card

Same caveat: these were identified by filename and location during inventory. Nothing was opened.

We're mid-migration to SharePoint Birdcage, and the personal items are moving to Dropbox as part of that. But I'd rather not wait on the migration to get the sensitive material off corporate storage.

Can you start on the credentials today and come back to me with a plan for the rest?

Thanks,
Austin
