# 2026-08-29 — Briefs deliver as artifacts only. No email, ever.

**Decided by**: Austin, 2026-08-29, in session. Verbatim: *"let's drop it. keep it here."*
**Scope**: both scheduled tasks — `morning-brief` and the Weekend Pulse.
**Status**: closed. Not a blocker, not a workaround, not pending.

## What was decided

The daily brief no longer emails anything. It publishes an artifact and stops. The Weekend Pulse already worked this way by Austin's 2026-08-28 instruction — *"don't email i will open and look at the artifact"* — and this extends the same rule to the daily.

Cadence, confirmed the same day: **morning brief Monday–Friday 6am; Weekend Pulse Friday 7pm.**

## Why — and why this is not a capitulation

Both available fixes were attempted with Austin present, and both failed on things he could see:

1. **`Mail.Send` admin consent.** `outlook_send_mail` returned HTTP 403 `ErrorAccessDenied` on four consecutive days (8/26, 8/27, 8/28, 8/29), tenant `8a338c82-657d-4604-b4b3-9b929ccd7abe`, client `07c030f6-5743-41b7-ba00-0a6e85f37c17`. Austin is the tenant admin and was given the exact blade, the delegated-vs-application distinction, and the consent URL. He tried; the error stayed byte-identical.
2. **Sending via Outlook Web in his own Chrome.** The Claude for Chrome extension permits navigation to `outlook.office.com` but denies `read_page` and `screenshot` on that domain, and denies navigation to `outlook.cloud.microsoft` and `outlook.office365.com` outright. No permission prompt could surface. Logging in was never the issue — he was already signed in.

Neither is worth more of his time for a delivery convenience. **The artifact was always the deliverable; the email was only a notification.**

## What this costs, stated honestly

The original design used email replies as the disposition channel — Austin replies "done" or "not now", the next morning's brief closes those items. **That loop never once ran**, because no brief ever reached the mailbox. Every closure across four briefs was inferred from his own outbound actions or from a Plaud recording, never from a disposition he gave.

## What replaces it

- **Disposition channel**: comments on the brief artifact. The URL is recorded on the "Last reviewed" line of `00-Meta/commitments.md`; each run reads the previous day's comments as step 2. This needs no admin consent and no browser permission.
- **Second channel, unchanged and still primary in practice**: sweep Austin's own Sent Items and Teams for actions that silently close a ledger item. This is how closures have actually arrived.

## Standing instruction

**Do not re-raise `Mail.Send`, admin consent, or Chrome site permissions as an open blocker.** Do not report the absence of an email as a failure. Do not attempt `outlook_send_mail`, drafts, Teams messages, or browser-driven Outlook in any brief. Austin closed this with full knowledge of the trade-off.

## Related

- `99-Archive/2026-08-catchup/PRIORITY-LIST.md` item 11a — the historical failure record, now closed by this decision
- `00-Meta/commitments.md` — "Last reviewed" line carries the current artifact URL
- Task files: `.claude/scheduled-tasks/morning-brief/SKILL.md`, `.claude/scheduled-tasks/weekend-pulse-2026-08-28/SKILL.md`
