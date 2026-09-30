# Open Commitments — Meetings, Calendar, Teams & Recordings
**Window:** 2026-07-26 → 2026-08-25 · **Compiled:** 2026-08-26 · **Subject:** Austin Berk

---

## Summary

**What I could reach:**
- **Outlook calendar — FULLY REACHED.** 107 events enumerated across the full window.
- **Teams chats — PARTIALLY REACHED.** Heavy Microsoft Graph 429 throttling. Deep message-level coverage of 2026-08-25; keyword-targeted coverage of the rest of the window.

**What I could not reach:**
- **Teams meeting transcripts — HARD BLOCKED.** Every request returns HTTP 403 `GraphAccessToTranscriptsDisabled`: *"Graph API access to transcripts is disabled for this tenant."* This is a tenant policy, not a per-meeting permission.
- **Plaud recordings — UNAUTHENTICATED.** `list_files` returns *"Not authenticated. Please login first."* Per instruction, I did not attempt to authenticate.

**Total items: 30 verified + 5 under `Needs verification`.**
*(First pass: 22 verified. Second pass added 8 new items, closed 2 gaps, and confirmed 2 items as already resolved. Second-pass content is in its own section below and is marked **[2P]**.)*

**The three most consequential:**

1. **A deliverable Jon Wyss requested "by EOD today" (2026-08-25) is due right now and is blocked** — Austin's own words: *"this directly impacts the deliverable that @Jon Wyss requested by EOD today."* The blocker is that per-unit rehab cost data appears never to have been tracked. Age: 1 day, already past deadline.
2. **David Berman asked Austin to move $62,325.06 and close six bank accounts "this week"** (2026-08-25). Money movement plus six account closures, with no confirmation Austin has acknowledged.
3. **Austin proposed a joint Champion + Cavco improvement call on 2026-08-03 and it was never scheduled** — 23 days old, and no such meeting exists anywhere on the calendar through 2026-08-26.

> **Confidence tags:** `VERIFIED` = I read the message body or event record myself · `SINGLE-SOURCE` = appears in exactly one place, unconfirmed · `INFERRED` = reasoned from a meeting title, attendee list, or absence pattern.

> **Important caveat on all calendar items:** Outlook shows what was *scheduled*, not what *happened*. I have no transcripts and no attendance records, so no calendar item below should be read as evidence a meeting occurred or that anything was said in it.

---

# SOURCE 1 — Teams Chats

## OWED-BY-AUSTIN

### 1. Rehab cost deliverable for Jon Wyss — due EOD 2026-08-25
- **Confidence:** `VERIFIED`
- **Who:** Jon Wyss → Austin. Austin acknowledged the deadline in writing.
- **Source:** THE OG CHAT (Jon Wyss, Zach Schwartz, Austin), 2026-08-25 18:53 UTC. Austin, in a draft email he posted to the chat:
  > "Since this directly impacts the deliverable that @Jon Wyss requested by EOD today, I'm including him here because it appears this information has either not been tracked or has not been communicated."
  > "I have a number of follow-up questions, including how we're expected to produce the report Jon requested if these costs are not readily available…"
- **Age:** 1 day — 1 day past deadline.
- **Stakes:** The report cannot be produced because per-unit rehab cost data does not exist in usable form. Austin states the purpose is "to establish a reliable cost basis so we know where we can price and sell homes, and how much we are effectively investing to achieve our occupancy goals." Missing this blocks home pricing decisions.
- **Next action:** Tell Jon explicitly what can and cannot be produced tonight, and propose a dated recovery plan for the missing cost basis.
- **Owner:** Austin
- **Urgency:** `ACUTE`
- **[2P] Searched for Jon's original request — not found in Teams.** I ran a dedicated search for the ask itself and it does not exist in any Teams chat. **The request therefore came by email or verbally, and its exact scope and timing are not recoverable from my sources.** Everything known about it comes from Austin's one-line reference above. What that reference does establish: it is a *report*, it is due **EOD 2026-08-25**, and it depends on per-unit rehab cost data. What it does **not** establish: the report's format, its audience, or when Jon asked. **Check Austin's email for the original request before acting** — and note the second pass found Jon pushing a separate related thread the same week (items 27–28), so this may be one deliverable among several.

### 2. Wire $62,325.06 BOA → JPM, then close six bank accounts
- **Confidence:** `VERIFIED`
- **Who:** David Berman → Austin.
- **Source:** "Finance" group chat (Berman, Moe Mehmood, Austin), 2026-08-25 17:42 UTC:
  > "hey Austin, can you set up a wire for the full balance in the BOA Parakeet Communities bank account to go over to the JPM Parakeet Communities bank account? Should be for $62,325.06. Then hoping you might be able to take a field trip this week to BOA to officially shut down the Parakeet Communities bank account, the Parakeet MHC account, Town & Country, Wolf Bay, Wolf Bay II, and the 'NA 5000' account."
- **Age:** 1 day.
- **Stakes:** Six legal-entity accounts stay open and reconcilable if not closed; Berman scoped it to "this week."
- **Next action:** Confirm receipt with Berman and book the BOA branch visit before Friday 2026-08-28.
- **Owner:** Austin (execution of the transfer itself is Austin's to perform, not to delegate to an assistant)
- **Urgency:** `SOON` — Berman's stated window is the week of 2026-08-24.

### 3. Schedule a joint Champion + Cavco improvement call
- **Confidence:** `VERIFIED` (commitment) + `VERIFIED` (non-completion, by calendar cross-check)
- **Who:** Austin → Jon Wyss. **This is Austin volunteering, not someone asking him.**
- **Source:** THE OG CHAT, 2026-08-03 13:00 UTC:
  > "Jon, I would like to schedule a call with Champion and Cavco with the two of us to ask how we can improve"
  >
  > Message carries a ❤️ reaction (assenting, but no verbal reply captured).
- **Cross-check:** I enumerated all 107 calendar events through 2026-08-26. The only Champion or Cavco meetings are the pre-existing standing series ("Parakeet - Construction Update" weekly, "Cavco x Parakeet - Weekly Update" weekly). **No joint improvement call was ever created.**
- **Age:** 23 days.
- **Stakes:** Both manufacturer relationships showed friction in-window (see FYI item 21). The corrective conversation Austin himself proposed has not happened.
- **Next action:** Send the invite, or consciously drop it.
- **Owner:** Austin
- **Urgency:** `SOON`

### 4. Send Charles Cimaglia a list of all property addresses
- **Confidence:** `VERIFIED`
- **Who:** Charles Cimaglia (OHmazing — external IT/MSP) → Austin.
- **Source:** 1:1 chat, 2026-08-25 20:40 UTC:
  > "also do you have a list of all the property addresses?"
  >
  > Followed at 20:41 by: *"i thought there was one in sharepoint?"*
- **Age:** 1 day. **Appears unanswered** — these are the last two messages in the thread.
- **Stakes:** Blocks the phone-systems work (extensions, transfers) that had a dedicated meeting the same day.
- **Next action:** Point Charles at the SharePoint list or export a current one.
- **Owner:** Austin (delegable to Natalie or Leslie)
- **Urgency:** `SOON`

### 5. Decide whether to send the rehab-cost escalation email
- **Confidence:** `VERIFIED`
- **Who:** Austin, self-imposed deadline, to Jon Wyss and Zach Schwartz.
- **Source:** THE OG CHAT, 2026-08-25 18:53 UTC:
  > "this is my email response I am going to send. Stop me by 3:00 if you don't want me to send."
- **Age:** 1 day — **the self-imposed 3:00 deadline has passed.**
- **Stakes:** The draft is pointed. It names a colleague ("what Daniel's ongoing tracking process has been since this is exactly the type of information he was brought on to manage down to the penny") and questions the accounting function directly. Sending vs. not sending is a real relationship decision.
- **Note:** At 19:02 UTC — *after* the 3:00 deadline — Austin was still asking Jon 1:1: *"please let me know if I can send that email i can't let you be the only one to call out this bull shit."* So as of the last captured message it was **still unsent and still awaiting Jon**. See item 7.
- **Next action:** Get a yes/no from Jon, then send or formally drop it.
- **Owner:** Austin
- **Urgency:** `ACUTE`

---

## AWAITING-FROM-OTHERS

### 6. Jon Wyss's sign-off on the rehab-cost email
- **Confidence:** `VERIFIED`
- **Who:** Austin → Jon Wyss.
- **Source:** Austin ↔ Jon 1:1, 2026-08-25 19:02 UTC:
  > "please let me know if I can send that email i can't let you be the only one to call out this bull shit"
- **Age:** 1 day. No reply captured.
- **Stakes:** Item 5 is blocked on this.
- **Next action:** Ping Jon for a direct yes/no.
- **Owner:** Jon Wyss
- **Urgency:** `ACUTE`

### 7. Natalie Magurne — Royal Oaks capex list, last 5 years
- **Confidence:** `VERIFIED`
- **Who:** Austin → Natalie Magurne.
- **Source:** Austin ↔ Natalie 1:1, 2026-08-25 17:42 UTC:
  > "any chance you have an easy list of cap ex done at royal oaks in the last 5 years"
- **Age:** 1 day. No reply captured.
- **Stakes:** Unstated in chat. Timing alongside the Newmark BOV and Jadian portfolio work suggests diligence support, but **I could not verify the purpose** — do not assume.
- **Next action:** Follow up; state the deadline and what it feeds.
- **Owner:** Natalie Magurne
- **Urgency:** `SOON`

### 8. John Clark — site measurements and numbers
- **Confidence:** `VERIFIED`
- **Who:** John Clark → Jon Wyss (Austin present in the chat).
- **Source:** "Parakeet Dream Team" group chat, 2026-08-25 13:44 UTC:
  > "Jon, we are getting measurements and will update once we have the numbers for you."
- **Age:** 1 day.
- **Stakes:** Feeds a paving/parking/drainage scope. Jon in the same thread: *"i'd quote full paving up to the main road. in front of office. everything"*; Natalie flagged: *"there is currently no drainage on the roads because it is sand so will need to make sure we have that engineered and quoted as well."* **The community is not named in the captured messages — flagging rather than guessing.**
- **Next action:** Confirm the measurement date, and ensure drainage engineering is scoped into the same quote rather than discovered later.
- **Owner:** John Clark
- **Urgency:** `SOON`

### 9. Albert Gano — SharePoint Full Control access request (Birdcage migration)
- **Confidence:** `VERIFIED` (the request) · `SINGLE-SOURCE` (whether it was granted)
- **Who:** Cedrick Arnigo (OHmazing) posted the request; Austin and Jon Wyss are the approvers in the chat.
- **Source:** "Parakeet Management" group chat, 2026-08-18 15:42 UTC:
  > "**Access request** **User:** Albert Gano **Location:** Parakeet Birdcage site **Access Level:** Full Control **Sponsor:** **Justification:** restructure sharepoint"
  >
  > A second identical block requests Full Control on the **Parakeet Communities Site**.
- **Age:** 8 days. **The `Sponsor:` field is blank in both blocks.**
- **Stakes:** Full Control on two SharePoint sites, including the Birdcage site, in order to restructure it. This is the Birdcage migration's blocking dependency — and it is also a broad permission grant that nobody has visibly sponsored.
- **I could not confirm whether this was approved.** There is no tool to enumerate a chat's full history, and no later message on it surfaced in search.
- **[2P] Re-investigated. Still unconfirmed, but the picture is sharper — and it leans open.** A completed search of the access-request queue shows this chat is where OHmazing transacts approvals, and that **at least three in-window requests show no approval**: Albert's (8/18, sponsor blank), Auzzi Dixon's GA4 Full Control (8/18, sponsor blank), and Alex's mailbox write access. Cedrick Arnigo demonstrably chases unanswered requests — *"Just following up on this"* (8/19), *"Sorry for putting this again but, giving access on auzzi to just specific folder didn't work, and the power automate is asking for the full site access. is that okay with you guys?"* (8/20) — yet **no grant and no chase appeared for Albert's**. Cross-reference item 25: Zach has also been waiting 12 days on Albert's to-do list. **Consistent with Albert being blocked; still not proof, since grants can be made silently in the admin console.**
- **Next action:** Ask Cedrick directly whether the 8/18 grant was executed — one message settles it. If granting, name a sponsor and consider time-boxing Full Control. Clear the other two pending requests at the same time.
- **Owner:** Austin or Jon Wyss
- **Urgency:** `SOON` — raise to `ACUTE` if Albert confirms he is blocked

---

## DECISION-NEEDED

### 10. Whispering — 30-day security contract, $9,800
- **Confidence:** `VERIFIED`
- **Who:** Natalie Magurne → Austin.
- **Source:** Austin ↔ Natalie 1:1, 2026-08-25 17:10 UTC:
  > "Security company we used in Whispering. 30 days 8 hour shift 9pm to 5am and they will have 24/7 cameras on the property while we have the contract. I think if we do it for 30 days we should be good to go. $9800"
- **Age:** 1 day.
- **Stakes:** $9,800 committed spend; Natalie has already formed a recommendation ("I think… we should be good to go"). Delay leaves the property uncovered overnight.
- **Next action:** Approve, decline, or ask for one competing quote.
- **Owner:** Austin
- **Urgency:** `SOON`

### 11. Asset Management Agreement — what sits inside the 4% construction fee base
- **Confidence:** `VERIFIED` (that Jon stated this) · **NOT verified that it was ratified or documented**
- **Who:** Jon Wyss → Austin.
- **Source:** Austin ↔ Jon 1:1, 2026-08-06 02:36 UTC:
  > "The **Asset Management Agreement** (Parakeet HoldCo II ↔ Parakeet MHC, effective 10/11/2024, signed by Austin and Bryan LaPlant) §6.2 charges 4% of *'the total cost of the **Construction Project**… including all hard costs and soft costs, but excluding any financing costs.'* And §6.8 defines a Construction Project as *'any tenant improvement work or other construction projects.'* A Cavco purchase order isn't construction. So: **home purchases are OUT of the fee base; homeset/installation and home rehab stay IN** (those are the construction services §2.2(b) actually lists)."
- **Age:** 20 days.
- **Stakes:** Directly sets fee revenue between two Parakeet entities on an agreement **Austin personally signed**. If home purchases have been billed into the fee base historically, this is a restatement, not just a go-forward policy.
- **Next action:** Decide whether this reading is adopted, then get it in writing (counsel or a memo to file) rather than leaving it in a 1:1 chat. Check whether prior billings need correcting.
- **Owner:** Austin + Jon Wyss, with counsel
- **Urgency:** `SOON`

### 12. SAM 2-hour call on 2026-08-26 — tight group or wider?
- **Confidence:** `VERIFIED`
- **Who:** Jon Wyss → Austin, Leslie Croft, Natalie Magurne, Zach Schwartz.
- **Source:** "SAM: Juices Flowing Prep Call" meeting chat, 2026-08-25 14:30 UTC:
  > "guys - i am thinking after writing that email that maybe we should reserve the 2hrs tomorrow for just us"
  > "theres a lot to talk through"
  > "if we need to rope tanya and auzzi in we can, but LC - thoughts on just this tighter group first so that we can all make sure we are on the same page first"
- **Age:** 1 day. Jon explicitly put the question to Leslie Croft; no reply captured.
- **Stakes:** The "SAM Hands On Organizational Call" is confirmed on the calendar for 2026-08-26 19:00–21:00 UTC. Attendee list needs settling before it starts.
- **Next action:** Leslie to answer; then confirm or adjust the invite.
- **Owner:** Leslie Croft (decision), Jon Wyss (invite)
- **Urgency:** `ACUTE` — meeting is today.

---

## DELEGATE

### 13. Carmen's housing program — coordinate outreach and a companywide note
- **Confidence:** `VERIFIED` (the asks) · `INFERRED` (that Austin is the intended owner)
- **Who:** Jon Wyss, in the "Parakeet Dream Team" group chat (Austin, John Clark, Leslie Croft, Natalie Magurne, Zach Schwartz, Jon).
- **Source:** 2026-08-25, sequence from 15:28–15:40 UTC:
  > "should send to her and have her call on the 6 other apps in the community"
  > "we should def press the other 6 apps into them in the community"
  > "worthwhile austin and i and you getting in touch with the people at the program to personally thank them and discuss the program more broadly?"
  > "can you coordinate with the help of carmen?"
  > "I also think we should put out a companywide email including this congratulating carmen on doing this and encouraging all managers to look for similar programs in their area with local governments"
- **Age:** 1 day.
- **⚠️ Ambiguity flagged:** *"can you coordinate with the help of carmen?"* was posted in a six-person group chat with **no @-mention**. The "you" is not identifiable from the transcript. Do not assume it is Austin. The separate line — *"worthwhile austin and i and you getting in touch…"* — does name Austin, but as a participant, not the coordinator.
- **Stakes:** Natalie noted *"I didn't realize it was literally the first home for this program!"* — a first-of-program placement with six more applications live in the same community. Real upside if pressed, and a genuine recognition moment for Carmen.
- **Next action:** Clarify who owns coordination, then run the outreach and the companywide email.
- **Owner:** Unassigned — needs naming
- **Urgency:** `SOON`

### 14. Rehab and new-home cost tracking is not producing usable data
- **Confidence:** `VERIFIED` (Austin's account) · `SINGLE-SOURCE` (only Austin's characterization; I have no counter-view from the person named)
- **Who:** Austin's assessment; concerns a colleague he names as "Daniel."
- **Source:** Austin's draft email, THE OG CHAT, 2026-08-25 18:53 UTC:
  > "We hired someone specifically to maintain up-to-date cost tracking for new homes and rehabs so we would have accurate financials on every project."
  > "…what Daniel's ongoing tracking process has been since this is exactly the type of information he was brought on to manage down to the penny."
  > "At a minimum, every rehab should have a simple summary: Home: / Rehab Level: / Estimated Cost: / Completed Cost: / Variance:"
- **Age:** 1 day as raised; the underlying gap is "months" per Austin (*"for months from an accounting perspective, and this is only now coming up?"*).
- **Stakes:** Root cause of item 1. Until fixed, no reliable cost basis for pricing or occupancy investment decisions.
- **Next action:** Set the five-field summary as the required standard, name an owner, and set a date for a first full back-fill.
- **Owner:** Austin to assign
- **Urgency:** `SOON`

---

## FOLLOW-UP-NEEDED

### 15. Zach Schwartz asked whether Austin was joining the Quickbase call
- **Confidence:** `VERIFIED`
- **Source:** Group chat (Zach, Austin, Natalie), 2026-08-25 14:02 UTC:
  > "Austin you still planning to join the Quickbase call?"
- **Age:** 1 day. No reply captured. The "Parakeet | Quickbase Discovery Session" was on the calendar for 2026-08-25 14:00–15:00 UTC — **the message arrived two minutes after start time.**
- **Stakes:** Fifth Quickbase session in the window (8/4, 8/6, 8/12, 8/18, 8/25) with a large vendor team. Austin's invite response was `tentative` on the 8/12, 8/18 and 8/25 occurrences.
- **Next action:** Reply to Zach; decide whether Austin needs to be in this series at all or can hand it to Zach.
- **Owner:** Austin
- **Urgency:** `SOON`

### 16. Champion items — call with John Clark
- **Confidence:** `VERIFIED`
- **Source:** Austin ↔ Jon 1:1, 2026-08-25 15:28 UTC:
  > "are we doing our call with John Clark today. If not I want to reach out to him to discuss the champion items"
- **Age:** 1 day. The JC/AB/JW Weekly Check-in was scheduled 2026-08-25 19:15–20:00 UTC. **I cannot confirm it happened.**
- **Stakes:** Austin conditioned direct outreach on whether the standing call ran. If it did not, the outreach is owed.
- **Next action:** Confirm whether the check-in ran; if not, contact John Clark directly.
- **Owner:** Austin
- **Urgency:** `SOON`

---

## REMINDER-FUTURE

### 17. Massachusetts / Auburn rent control meeting — ~2026-09-14
- **Confidence:** `VERIFIED` (as a possibility, not a confirmed booking)
- **Source:** Austin ↔ Natalie 1:1, 2026-08-25 18:26 UTC:
  > Natalie: "We might need to go up to MASS Sept 14th for the rent control meeting in Auburn. Stelmock called"
  > Austin: "we can go the beginning of the week and then go to Miami the end"
  > Natalie: "I asked if we could move budgets to the week after"
- **Age:** 1 day. **Note the hedge — "might need to." Not a confirmed trip.** Name "Stelmock" is as written.
- **Stakes:** Rent control proceeding. Austin has already floated restructuring that week's travel and Natalie has asked to move budget sessions.
- **Next action:** Confirm the meeting date with Stelmock, then lock travel and the budget reschedule.
- **Owner:** Natalie Magurne (confirm), Austin (travel)
- **Urgency:** `SCHEDULED` — 2026-09-14

---

# SOURCE 2 — Outlook Calendar

*(Scheduling facts only. No attendance or content verification is possible without transcripts.)*

## REMINDER-FUTURE

### 18. River Oaks home deliveries — 7 homes across 2026-08-24 and 2026-08-25
- **Confidence:** `VERIFIED` (event records)
- **Source:** Two all-day events from `construction@parakeetcommunities.com`, with Champion Homes staff on the invite (chamiller, jvandenburg, jlockwood, tcooper, tandros):
  - **2026-08-24 "RIVER OAKS - HOME DELIVERIES":** 2702 Dancing Mullet / 28650 · 2710 / 28651 · 2712 / **28632** · 2714 / 28653
  - **2026-08-25 "RIVER OAKS - HOME DELIVERIS" [sic]:** 2716 / 28655 · 2726 / 28659 · 2728 / 28657
- **⚠️ Data anomaly flagged:** serials run 28650, 28651, **28632**, 28653, 28655, 28657, 28659. The **28632** breaks an otherwise consecutive odd/even sequence and may be a typo for 28652. Verify against the Champion order before relying on it.
- **Stakes:** Seven homes landing across two days drives set crews, utility connections, and certificates of occupancy.
- **Next action:** Confirm all seven were delivered; confirm serial 28632; confirm set-crew and CO scheduling downstream.
- **Owner:** Construction (John Clark / Leslie Croft)
- **Urgency:** `ACUTE` — deliveries are landing now.

### 19. Uniti — kickoff 2026-08-26
- **Confidence:** `VERIFIED`
- **Source:** Three events in 10 days with Uniti (external): Intro Call 2026-08-17, "Parakeet <> Uniti Call" 2026-08-24, **"Parakeet <> Uniti Kickoff Call" 2026-08-26 21:00–22:00 UTC** (Uniti brings Allison, Alex, Catherine; Parakeet brings Austin, Jon, Leslie).
- **Stakes:** Intro → kickoff in nine days. A new vendor relationship is being stood up quickly.
- **Next action:** Confirm what is actually being committed to at kickoff and whether anything is signed.
- **Owner:** Austin / Leslie Croft
- **Urgency:** `SCHEDULED` — 2026-08-26

---

## FOLLOW-UP-NEEDED

### 20. Governance cadence broke down in the week of 2026-08-17
- **Confidence:** `VERIFIED` (the absences) · `INFERRED` (that it signals anything)
- **Source:** Full enumeration of all 107 events in the window:
  - **L10 EOS call** (Natalie organizer, 8 attendees): held **7/31, 8/7, 8/14** — **absent the week of 8/17–8/21**, and not on the calendar again through 8/26.
  - **Finance & Accounting EOS Meeting** (Berman organizer): **7/30** held, **8/6 absent**, **8/13** held, **8/20 explicitly `Canceled`** (flagged `importance: high`).
- **Stakes:** Both standing accountability forums lapsed in the same week. Notably, the rehab-cost-tracking failure surfaced on 8/25 — the first business week after both forums went dark. That adjacency is suggestive, **not proven**.
- **Next action:** Confirm whether L10 was deliberately paused or just dropped, and get both back on the calendar.
- **Owner:** Natalie Magurne (L10), David Berman (Finance EOS)
- **Urgency:** `SOON`

### 21. RentViewer weekly sync — never RSVP'd, five occurrences running
- **Confidence:** `VERIFIED` (RSVP state) · `INFERRED` (that Austin disengaged)
- **Source:** "RentViewer | Parakeet Weekly Sync" (dan@rentviewer.com, external, 10 attendees) on 7/27, 8/3, 8/10, 8/17, 8/24. **Every single occurrence** shows `showAs: tentative` and carries Austin's own Outlook category **"Awaiting Reply."**
- **⚠️ Read this carefully:** this proves Austin never accepted the invitation. It does **not** prove he skipped the calls. No attendance data is available.
- **Stakes:** An external vendor's standing weekly with a large internal group, flagged by Austin's own system as awaiting his response for five straight weeks. Note he *did* separately take a "RentViewer | Parakeet - Claude MCP Setup" 1:1 with Dan Keller on 8/24 — so the relationship is active even if the series RSVP is not.
- **Next action:** Accept, decline, or delegate the seat to Zach.
- **Owner:** Austin
- **Urgency:** `SOON`

---

## FYI

### 22. External counterparties Austin was scheduled with in-window
- **Confidence:** `VERIFIED` (attendee lists)
- **Legal:** Eckert Seamans (Wallack, Dym — "Parakeet Next Steps," 8/10) · Gunster + Vector Law (WPMH increase call, 7/30) · King & Spalding (Rocky Creek Final Apportionment, 7/31) · Woods Oviatt + Adam Steinberg Law + Laurence Brokaw ("RE: Hunter Extension," 8/19 — **Austin organized this one**)
- **Capital / brokerage:** Jadian Capital (Hennessy, Nelson, Cridge) — Pipeline Review 8/6, Weekly Catch-up 8/14 · **Newmark — "Jadian Capital x Newmark - Parakeet Portfolio BOV" ran four times in ten days: 8/11, 8/13, 8/14, 8/20**, with up to 9 Newmark staff incl. Adam Doneger (Executive Vice Chairman) · JLL + Marcus & Millichap (Geiger Key Resort, 8/5)
- **Manufacturers:** Champion Homes (weekly Construction Update, 14 Champion attendees) · Cavco (weekly, incl. Ross Mueller, Jason Calvert)
- **Vendors / other:** Quickbase (×5) · RentViewer · Global Payments/Zego · Uniti · Corridor-IQ + Bonaventure · Nutrient · High Pace Construction · OHmazing · Hensdale Club · Robert Youssef (8/16, a **Sunday**, with Jon Wyss)
- **Worth noting:** a four-session Newmark BOV sprint on the Parakeet portfolio, driven by Jadian, is the single densest external engagement in the window. Whatever came out of it lives in transcripts I cannot reach.

### 23. Champion "Construction Update" series is running past its stated end date
- **Confidence:** `VERIFIED` (the discrepancy) · `INFERRED` (that it matters)
- **Source:** The recurring "Parakeet - Construction Update" event body reads:
  > "This meeting series will begin Wednesday January 7th, 2026 and end Wednesday July 1st, 2026."
  >
  > Yet occurrences are scheduled 7/29, 8/5, 8/12, 8/19 and 8/26 — nearly two months past the stated end.
- **Stakes:** Low on its own; likely just a stale invite body. Flagged only because it is the primary Champion coordination forum and nobody appears to have re-chartered it.
- **Next action:** Have Champion reissue the series with correct dates.
- **Owner:** Leslie Croft
- **Urgency:** `SCHEDULED` — next occurrence 2026-08-26

---

# SECOND PASS — added 2026-08-26

*Run after the first pass to close the 7/26–8/24 coverage hole. All items below are marked **[2P]**. Same evidence standard. Each was checked for a later message that already closed it.*

## OWED-BY-AUSTIN

### 24. [2P] Confirm Justin's file is the complete population of infill home orders
- **Confidence:** `VERIFIED`
- **Who:** David Berman → the group (Jon Wyss, Leslie Croft, Zach Schwartz, Austin).
- **Source:** Group chat, 2026-08-24 19:29 UTC:
  > "Not sure whose looked it over yet but can we confirm that the file Justin sent around is the full population of all homes we believe have been ordered associated with the infill initiative?"
- **Age:** 2 days. Berman's own "Not sure whose looked it over yet" indicates it was unaddressed at the time of writing; no reply surfaced.
- **Stakes:** This is an order-integrity question across the whole infill initiative — the same Cavco/Champion order set that produced the River Oaks delivery discrepancy in item 18. If the file is incomplete, both the delivery schedule and the capital plan are built on a short list.
- **Next action:** Someone must actually reconcile Justin's file against the Cavco and Champion order books and answer Berman.
- **Owner:** Unassigned — Berman addressed the group, not a person
- **Urgency:** `SOON`

## AWAITING-FROM-OTHERS

### 25. [2P] Zach Schwartz is waiting on Albert Gano's to-do list — 12 days
- **Confidence:** `VERIFIED`
- **Who:** Zach Schwartz → Albert Gano.
- **Source:** L10 EOS call meeting chat, 2026-08-14 19:02 UTC:
  > "Albert - Pls send me list of to do's by EOD. we covered a lot today I don't want anything to fall through the cracks"
- **Age:** 12 days past an EOD deadline. No reply surfaced.
- **Stakes:** Directly relevant to the Albert question. Zach asked for exactly the artifact that would show what Albert is working on and blocked by — and it appears never to have arrived. Note the date: 2026-08-14 was the **last L10 EOS call that took place** (see item 20), so this ask was made in the final session before that forum went dark, with nothing to carry it forward.
- **Next action:** Get the list from Albert; use it to confirm whether the SharePoint access in item 9 is the actual blocker.
- **Owner:** Albert Gano
- **Urgency:** `SOON`

## DECISION-NEEDED

### 26. [2P] Financing/lender hire — Austin must appoint who selects candidates
- **Confidence:** `VERIFIED`
- **Who:** Demetria Loukas → Austin (and Jon Wyss).
- **Source:** Group chat (Demetria, Jon, Austin), 2026-08-24:
  > Austin, 19:44: "Spoke to Melanie about the financing/lender hire to work with her and have her involved in the interview process. she is super excited and relieved as that topic is a hurdle for eveyone"
  > Demetria, 20:27: "Just let Melanie know my ideas for the interview process. I will find candidates and procure/ rank and then allow Leslie (or whomever you appoint) to choose who they want to speak with and then I will have panel interviews with Leslie, Melanie, and maybe Auzzi(?)."
  > Demetria, 20:28: "You guys will have 2 people to speak to - after which the final call is made."
- **Age:** 2 days.
- **Stakes:** Demetria has committed to sourcing and ranking candidates, but the process is explicitly gated on Austin naming who chooses the shortlist ("or whomever you appoint") and confirming whether Auzzi is on the panel. Her pipeline stalls without that.
- **Next action:** Name the selector and confirm the panel composition.
- **Owner:** Austin
- **Urgency:** `SOON`

## FOLLOW-UP-NEEDED

### 27. [2P] Permits — Natalie committed to raising them again on the 9am call
- **Confidence:** `VERIFIED`
- **Who:** Natalie Magurne → Jon Wyss and Austin.
- **Source:** Group chat (Austin, Jon, Natalie), 2026-08-23 17:13 UTC:
  > "I'll bring up the permits again on our call at 9 tomorrow"
- **Age:** 3 days. The word **"again"** signals this is a repeat escalation that has not resolved.
- **Stakes:** Permits gate home placement, which gates the delivery schedule and certificates of occupancy. **This directly contradicts the first pass's finding that no permit activity surfaced** — see the Gaps revision.
- **Next action:** Confirm the 8/24 9am call happened and what was decided.
- **Owner:** Natalie Magurne
- **Urgency:** `SOON`

### 28. [2P] Jon Wyss wants demo/build permits pushed through as the priority
- **Confidence:** `VERIFIED`
- **Who:** Jon Wyss → Austin and Natalie.
- **Source:** Same chat, 2026-08-23 17:15 UTC, two minutes after Natalie's message:
  > "honestly those things are such garbage - i think we need to really focus on pushing the demo/build permits thru"
- **Age:** 3 days.
- **Stakes:** A stated reprioritization from the CIO toward demo/build permits. No owner or date was attached to it in the thread — which is how this kind of directive evaporates.
- **Next action:** Convert into an owned, dated workstream rather than a chat remark.
- **Owner:** Needs naming — likely John Clark or Natalie Magurne
- **Urgency:** `SOON`

## FYI

### 29. [2P] SAM prep agenda for the 2026-08-26 two-hour call
- **Confidence:** `VERIFIED`
- **Source:** Jon Wyss → Austin, 2026-08-24 18:22 UTC:
  > "SAM pre-Wednesday call juices flowing prep call — CRM Flows / Org build-out / responsibilities of the funnel top to bottom / Loan coordinator / Sales & Leasing Coordinators – not so much PT assistant managers"
  > and: "i just want them thinking ahead of the wednesday call"
- **Stakes:** Sets the scope for the 8/26 19:00–21:00 session, and connects to item 26 (the loan coordinator hire) and item 12 (who attends).
- **Urgency:** `SCHEDULED` — 2026-08-26

### 30. [2P] Two items that closed inside the window — logged so they are not re-raised
- **Confidence:** `VERIFIED`
- **Contract execution, closed in 2 minutes.** Austin, 2026-08-24 19:57 UTC: *"Leslie just got the contract so let me know when you approve and ill execute"* → Leslie Croft, 19:59 UTC: *"looks good"* / *"i will forward him the new vendor docs"*. **Approved. Not an open item.**
- **Permit obtained for PL.** Austin, 2026-07-28 19:14 UTC: *"Got the permit for PL"*. **Closed.**

---

# Needs verification

These surfaced as signals but **do not meet the evidentiary bar**. Do not act on them without checking first.

### V1. Lamberton Lake sale — no in-window activity found anywhere reachable
Every Teams hit for "Lamberton" predates the window (2025-09-04 through 2026-01-30). Zero calendar events in the window. **This is a genuine absence in the sources I could reach — but it is not evidence the sale is dormant.** Lamberton is most likely progressing over email and through counsel, neither of which was in my scope. Check email and the deal counsel directly.

### V2. Cambridge SCH 2025 — ✅ **RESOLVED IN SECOND PASS**
~~No in-window chat hits before the rate limit truncated the scan at 25 of 47 chats.~~ **The Cambridge search completed on the second pass.** Result: **all Cambridge chat activity runs 2026-07-09 → 2026-07-15 and then stops — eleven days before the window opens.** There is genuinely no in-window Cambridge chat traffic. Calendar likewise shows only pre-window events (Interco Balance Discussion 7/14; Citrin Cooperman 7/22).

**But the pre-window state was left unresolved, and it is significant.** Verbatim, all from David Berman in his 1:1 with Austin:
> 2026-07-14 16:50 UTC: *"A2Z Community Partners will be inheriting the outstanding payables to Parakeet Communities and Parakeet MHC, LLC from all Cambridge entities that currently total $242,942.16"*
> 2026-07-14 17:12 UTC: *"We'll have to draft a contract between A2Z and Cambridge noting the inheritance of the payables to be signed by representatives of both parties"*
> 2026-07-13 16:56 UTC: *"One of two things needs to happen, either Parakeet needs to formally write off receivables and take a P&L hit on the books at MHC for revenue it didn't collect or Cambridge needs to not file a final return so that it can pay the money back in 2026"*
> 2026-07-15 21:41 UTC: *"if there was a distribution recorded on the Cambridge books, you would have to give all the LPs taxable income that never happened to facilitate a final return"*

**Why this matters:** a $242,942.16 inter-entity payable, an unsigned A2Z↔Cambridge contract, and a binary tax decision (write off vs. don't file a final return) were all live on 7/15 and then went silent. Silence is not resolution. **Confirm status with Berman and Citrin Cooperman.**

### V3. Walton Street Capital / WSRED — zero hits
No calendar events and no chat messages matched "Walton" in any period searched. Either the work is not represented in calendar/Teams, or it travels under a name I did not search. **Absence here is weak evidence.**

### V4. Belle Haven legal — last activity predates the window
One event only: "Belle Haven + Silver Breeze Call" with Gunster counsel (cspake, mdportilla) on **2026-06-22**, five weeks before the window opened. A related "Silver Breeze MHP Monthly Payment Due" reminder appears 2026-08-01. No in-window Belle Haven legal activity found. Confirm status with Gunster.

### V5. [2P] DOH water permit expired 2026-06-30 — no resolution found
- **Confidence:** `SINGLE-SOURCE` — one message, pre-window, uncorroborated.
- **Source:** Jon Wyss, group chat, 2026-07-12 14:13 UTC, during a licenses-and-permits folder audit:
  > "also licenses and permits folder audit for DOH… Its misc water permit also just expired 6/30/2026…— no certificate for any year; the 'permit' file is a Feb 2024 change-of-ownership inspection report saying the reissued permit (13-54-2855268…"
- **Why flagged:** An expired Department of Health water permit with **no certificate on file for any year** is a regulatory exposure, not a filing-hygiene issue. It surfaced pre-window and **nothing in the window shows it resolved.** The community is not named in the captured message.
- **Also unresolved — who owns renewals.** On the same day Jon asked *"Who is responsible for license and permit renewals now do either of you know?"* and Natalie Magurne answered *"Berman took over all license and permit renewals."* That handoff is `SINGLE-SOURCE` and was never confirmed by Berman in anything I could reach.
- **Next action:** Confirm the permit's current status and confirm with Berman that he owns renewals.

### V6. [2P] River Oaks serial `28632` — **still unresolved, deliberately not inferred**
Searched Champion and Cavco chat history for order or serial data that would confirm or correct the out-of-sequence serial flagged in item 18. **No order confirmation surfaced.** Per instruction I am leaving this flagged rather than resolving it by inference — a serial number is exactly the kind of field where a plausible guess (28652) is worse than an open question. **Verify against the Champion order document directly.**

---

# Gaps

**Be precise about what these mean — an unauthenticated connector reporting "nothing found" is a false negative, not a clean result.**

| Source | Status | Detail |
|---|---|---|
| **Outlook calendar** | ✅ **Fully reached** | All 107 events in window enumerated via 5 paginated calls, plus 6 targeted keyword searches. High confidence in coverage. |
| **Teams meeting transcripts** | ❌ **Hard blocked — zero transcripts read** | HTTP 403 `GraphAccessToTranscriptsDisabled` on every attempt. Confirmed against 4 meetings spanning **two different tenants** (Parakeet `8a338c82…` and Eckert Seamans `6fbe60a2…`), so this is tenant policy, not a per-meeting or per-organizer issue. **`meetingTranscriptUrl` is populated on the event records — the transcripts exist and are simply not retrievable through this connector.** Requires a tenant admin to enable Graph transcript access. |
| **Plaud recordings** | ❌ **Unauthenticated — zero recordings read** | `list_files` → *"Not authenticated. Please login first."* Per instruction I did not attempt to authenticate. **This is the single largest gap.** Plaud is where Austin's own site visits and in-person conversations live — exactly the commitments that exist nowhere else. Nothing in this report reflects any Plaud content. |
| **Teams chats** | ⚠️ **Partially reached — improved on second pass** | Persistent Graph 429 throttling (`retryAfterSeconds: 62`) throughout, despite fully serialized calls and backoffs up to 10 minutes. Full message-level depth achieved for **2026-08-24 and 2026-08-25**. The rest of the window is covered by **six completed keyword searches** (Lamberton, Birdcage, Cambridge, Cavco, Champion, Access request, permit, EOD), each of which ran to completion. **2026-07-26 → 2026-08-23 still has no day-by-day sweep** and is covered only where a keyword search happened to surface it. |

**Structural limits worth stating plainly:**

1. **The richest source produced nothing.** The task correctly identified meeting transcripts and Plaud as the most likely home for forgotten verbal promises. Both were unreachable. Every commitment in this report came from written Teams messages or calendar records.
2. **No verbal commitments are captured.** Nothing here reflects anything anyone *said* in a meeting. Zero coverage of the L10 EOS call, the Flock in Focus all-hands (last occurrence 2026-07-02, outside the window), the four Newmark BOV sessions, the Jadian pipeline reviews, or the Eckert Seamans legal call.
3. **The date distribution is still skewed, but less than before.** *(Revised after second pass.)* Chat-derived items now cluster on **2026-08-23 → 2026-08-25** rather than 8/25 alone, and targeted searches pulled in items from 8/3, 8/6, 8/14 and 8/18. **2026-07-26 → 2026-08-22 remains thinly sampled** — the day-by-day sweep never reached it, because each date-filtered call rescans all 47 chats and exhausted the Graph quota after two attempts. Routine commitments made in that first month are still likely uncaptured. Treat the age figures as reliable and the *coverage* of early August as partial.
4. **Several "unanswered" calls are provisional.** Where I note a message appears unanswered, that reflects what surfaced in search — not a full thread read. There is no tool to enumerate a chat's complete history. This is the specific reason item 9 (Albert's access) could not be closed either way.
5. **What the second pass changed.** Two first-pass gaps closed: **Cambridge** (search completed — genuine in-window silence, but a live $242,942.16 pre-window exposure surfaced) and **permits** (the first pass wrongly reported nothing on supply-chain sequencing; in-window permit activity does exist, items 27–28). Two remained open by design: **serial 28632** and **Albert's access grant**.

**On Albert's SharePoint access (item 9) — what the second pass established.** I could not confirm whether it was granted, but the surrounding evidence is now much clearer. The "Parakeet Management" chat is the standing queue where OHmazing posts access requests for Austin and Jon to approve. Within the window it holds **at least three requests that show no approval**: Albert's Full Control on two sites (8/18, `Sponsor:` blank), Auzzi Dixon's Full Control on GA4 (8/18, `Sponsor:` blank), and Alex's mailbox write access. Cedrick Arnigo visibly chases unanswered ones — *"Just following up on this"* (8/19) and *"Sorry for putting this again…"* (8/20). No such follow-up or grant appeared for Albert's request. **This is consistent with it still being open and gating him, but it is not proof** — grants may be executed silently in the admin console without a chat reply. Combined with item 25 (Zach's 11-day-old unanswered request for Albert's to-do list), the fastest way to settle it is to ask Cedrick directly.

**To close the remaining gaps:** authenticate Plaud, have a tenant admin enable Graph transcript access, ask Cedrick whether Albert's access was granted, verify serial 28632 against the Champion order, and re-run a day-by-day chat sweep across 7/26–8/22 when Graph quota allows.
