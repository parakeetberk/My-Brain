# Uniti agent mailbox: shared mailbox or its own account

**What this is:** the provisioning decision for the AI sales agent's Microsoft inbox, which Uniti asked for and never specified. Written 2026-09-02 on Austin's question.

**Status:** decision open. **Recommendation: provision a licensed user account, not a shared mailbox**, and the reason is discovery rather than anything Uniti asked for. Updated 2026-09-28: the agent ran its first live weekend with no recorded feedback, and the routing column is owed Monday, `TD-0714`.

## What Uniti actually asked for, verbatim

Alex Edwards, Uniti, 2026-08-27 12:21 ET, *Parakeet Implementation Kick-Off Next Steps*, item 3 of five:

> Finalize the agent name and set up the agent's Microsoft inbox

**That is the whole specification.** VERIFIED, primary email read. No mailbox type, no authentication method, no permission scope, no mention of whether they sign in or connect through an app registration. Jon's 2026-09-02 01:06 email adds only the address recommendation, `sam@parakeetcommunities.com`, with the surname kept out so a later name change costs nothing. That part is right and is not in question.

**So the reason this decision is hard is that the vendor has not said how they connect**, and the connection method is the only thing that rules a shared mailbox in or out. This is the same shape as the FAQ spec they committed to on 8/27 and never sent.

## The three shapes, and what each one can and cannot do

### 1. Shared mailbox, no licence

Free. No credentials of its own, and interactive sign-in is blocked by design, which Microsoft recommends you leave blocked. Reachable two ways only: **delegated access**, where named users are granted Full Access and Send As, or an **Entra app registration with Graph application permissions and admin consent**, which should then be scoped with an ApplicationAccessPolicy so the app can reach that one mailbox and nothing else in the tenant.

- Works if Uniti connects through their own app registration. This is the cheapest and tightest answer if that is what they do.
- **Fails outright if Uniti's connector is a "sign in with Microsoft" consent screen or IMAP with a password.** A shared mailbox cannot complete an interactive sign-in.
- 50 GB cap. Cannot be a Teams member. **No per-mailbox archive and no litigation hold unless you licence it anyway.**

### 2. Licensed user account

A real seat. Own credentials, so it can do interactive OAuth, can be MFA'd or better yet given a conditional access policy, can be a Teams member, can be put on litigation hold, and appears in the address book as a person.

- Works with every connection method Uniti could plausibly use.
- Costs a seat.
- **It appears in the GAL as a person, which cuts both ways.** Residents and staff will read Sam as an employee. That is the product working as designed and it is also a thing to be deliberate about.
- If Uniti wants IMAP or SMTP with a username and password, note that basic auth is off by default and turning SMTP AUTH on for this mailbox is its own security decision, not a checkbox.

### 3. Licensed account with the mailbox delegated to the team

The hybrid, and operationally the one that matches how this will actually get used. Sam has a real identity for Uniti to authenticate as, and Leslie, Auzzi and whoever covers sales get **Full Access and Send As** so a human can read the thread and take a conversation over mid-stream without asking Uniti for anything.

**The agent needs an identity to act as. Humans need to see what it said and be able to step in.** Those are two different requirements and only this shape covers both.

## The use cases, and which shape each one forces

| Use case | Shared mailbox | Own account |
|---|---|---|
| Receive inbound lead email at `sam@` | yes | yes |
| Send outbound as Sam | yes, via Graph app permission or Send As | yes, natively |
| Uniti connects via their own app registration and admin consent | **yes, and this is the right answer if so** | yes |
| Uniti connects via "sign in with Microsoft" OAuth consent | **no** | **required** |
| Uniti connects via IMAP or SMTP with a password | **no** | **required**, plus SMTP AUTH enabled |
| A human reads the thread and takes over | via delegation | via delegation, and cleaner |
| Sam is a Teams member, or gets a calendar residents can book | **no** | yes |
| Litigation hold and per-mailbox archive on everything Sam ever sent | **no, not without licensing it** | yes |
| Conditional access policy restricting where the identity can be used from | limited | yes |

## The argument that settles it regardless of what Uniti needs

**An AI agent emailing residents, while a Massachusetts class action about rent increases is live, produces discoverable records from day one.** Every message Sam sends is a company communication with a resident. A shared mailbox with no licence has no per-mailbox archive and cannot be placed on litigation hold, so the cheap option is the one that cannot preserve the thing most likely to be asked for.

Second argument, smaller and pointed at a known failure in this company: **`winnie@a2zcp.com` is a departed employee who is still the login of record on two live utility portals**, per [[00-Meta/commitments]] item 2. An unlicensed, unowned shared mailbox with a vendor's app connected to it is that pattern being started deliberately. Whichever shape gets picked, **a named human owns the mailbox and it goes on the compliance calendar** (`KP-0022`).

## Recommended sequence

1. **Provision a licensed user account today** once the name lands. Licensed to shared is a supported one-way conversion in the admin centre that keeps the data, so starting licensed costs one seat and keeps every option open. Starting shared and discovering Uniti needs an interactive sign-in costs a day at the wrong end of the October 1 go-live.
2. **Grant Full Access and Send As** to Leslie Croft and Auzzi Dixon so humans have visibility from the first message rather than after the first complaint.
3. **Ask Catherine on the 2pm call, in these words:** does your integration authenticate as the mailbox through an interactive Microsoft sign-in, through an app registration with admin-consented Graph permissions, or through IMAP and SMTP credentials. **The answer is the only thing that would change the recommendation**, and it also tells you what consent you are being asked to grant in your own tenant.
4. **Put the identity behind a conditional access policy** before it goes live, and no MFA-exempt service account without a written reason.
5. **Do not enable SMTP AUTH** unless Uniti confirms they need it, and if they do, treat it as a decision rather than a setting.

## What is not decided here

- **Whether Sam gets a Teams presence or a bookable calendar.** Not asked for, and it is a different conversation about how human the agent is meant to appear.
- **Whether the address should be `sam@` or something that reads as a role rather than a person.** Jon's reasoning for keeping the surname out is sound. Whether an AI agent should have a first-name mailbox at all is a brand and disclosure question for Leslie, not a provisioning one.

## The agent goes live, 2026-09-25

*Added 2026-09-26 by the Page Update from `00-Meta/daily-close/2026-09-25.md`. Confidence labels are the close's own.*

- **The voice agent goes into a weekend test on a live RingCentral routing path** (`TD-0714`). Uniti says the fault where the agent texted a caller the application link is fixed. **Three content faults are not**: the RV park list, the Campspot links and the missing home detail.
- **It is running an unresolved age designation reading**, 55+ for the affected communities and 50+ for Vantage, per Jon on 2026-09-25. An age answer from an automated agent is a statement to a prospect. `KP-0128`, Critical; path one on that row is to take the age question out of the agent's scope before the test.
- **This page's mailbox decision is still recorded as open above**; nothing in the closes says it was settled.

## The first live weekend, 2026-09-26

- **Sam has been live on (386) 202-1662 since Friday afternoon and no test feedback is recorded in any channel.** Jon Wyss's Uniti Rollout Board, 18:27 ET.
- **The per scenario transfer column is owed to Uniti Monday morning by Leslie Croft and Austin.** All twenty scenarios read TBC, health and safety emergency included, and Uniti has stopped work on scenario transfers until it arrives.
- **Zillow leads will not reach Sam at go live**: Sam matches lead emails on exact sender addresses only, so the email lead channel goes into 1 October untested.
- **The age designation wording Sam is using at Belle Haven, Lake Saunders, Southgate and Vantage Oaks is still unapproved.** `KP-0128`.
- `TD-0714`. **SINGLE-SOURCE**: the board is Jon's own summary and Uniti's sheet was not readable. Source: `00-Meta/daily-close/2026-09-26.md`, which read the primary messages; **the primaries were not re-opened this run.**

## Sources

- Alex Edwards, Uniti, *Parakeet Implementation Kick-Off Next Steps*, 2026-08-27 12:21 ET. **VERIFIED**, primary email read. The only vendor statement of the requirement.
- Jon Wyss, *Uniti call 2pm today: 3 decisions we need before then*, 2026-09-02 01:06 ET, and Teams SAM Masters chat 00:36 ET. **VERIFIED**.
- [[10-Business/vendors/vendor-status-2026-08]] — Uniti row, kickoff inputs.
- Microsoft 365 shared mailbox and licensing behaviour is stated here from general platform knowledge, **not from a tenant read**. Confirm the archive and hold behaviour against your own licence SKUs before relying on it in a compliance answer.
