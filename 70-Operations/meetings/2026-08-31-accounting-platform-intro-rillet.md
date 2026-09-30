# 2026-08-31 — AI accounting platform intro call, continuous close

**Who was there:** **Speaker 1 is Austin** and **Speaker 4 is Jon Wyss** — VERIFIED, both are addressed by name and Jon opens with the founder framing while Austin answers every systems question. **Speaker 2 is "JD", on the vendor's sales team** — he names himself. Speaker 3 is one line.
**When:** 2026-08-31, 14:01:14 to 14:25:07 ET. 23 min 53 sec. Ran on Teams; the first two minutes are Jon joining late and a dropped participant.
**Filed:** 2026-08-31, by Claude, on the end-of-day close refresh. **This replaces the placeholder** `05-Inbox/2026-08-31-plaud-1401-not-transcribed.md`, which was written earlier the same evening when the recording had no transcript. Plaud has since processed it. The placeholder is retired to `99-Archive/2026-08-plaud-raw/` with its wrong-at-the-time reading intact.
**Source:** Plaud recording `fbe01d6378c7f9bcbef3893f6e5e2a5d`, 72 utterances, `transaction` block, plus the Plaud AI summary.

**The vendor's name is not settled.** The transcript spells it **Realest**, **Relit**, **Rulit** and **Relet** in four places, and names an agent layer **Aura**. The Plaud summary calls the company Realest. **INFERRED that this is Rillet**, the AI-native accounting platform, on the description Jon gives — *"something about the big raise you did and the fact that it's AI accounting software that helps keep alive monthly close."* One look at the calendar invite settles it, and the name should be settled before it reaches a contract or a report. **Second independent spelling found 2026-08-31:** the Parakeet Brain vault already carries an active project page called **"Realit Live Close Evaluation"**, which means this evaluation predates this call and the name is spelled a fifth way there. **That page, not the transcript, is the place to settle it** — and its existence is the more useful find, because it means there is prior work on this vendor that this vault has never read. Same class of trap as the Unity/Uniti row already on [[10-Business/eos/to-dos]].

## Summary

A first real call with an AI accounting vendor, following an intro call with a colleague of theirs a week and a half earlier that Jon and Austin took from the road. Jon framed the why: five years of growth, books that have got progressively more current by month-end but are still not live, and *"some changes probably in our accounting department that's going to allow us to embrace a little bit more technology."* Austin then said it plainly to an outside salesperson: *"We're kind of parting ways with our controller slash CFO, totally adverse to technology."*

The bulk of the call is Austin describing the stack, and it is the cleanest description of the expense side anywhere in this Brain. Revenue is not the problem — 99% of cash in is resident payments through the property management system's payment provider, batched daily. Everything painful is on the expense side. Bills go to AvidXchange, batch into Rent Manager, pay out of Rent Manager and rebatch out. AvidXchange stays because it is a **preferred partner with a direct API into Rent Manager**, and removing it would add work rather than remove it. **Ramp is the gap.** It is the corporate card programme for field staff, it does not integrate to Rent Manager the way AvidXchange does, and Ramp has moved to **once-a-month journal entries**, which Austin says *"at the end of the month drives us crazy because we can't see what's going on inter month."* Add utility charges through NG and recurring charges needing electronic reconciliation, and that is the close.

The vendor was straight about the gap on their side: **no native Rent Manager integration today**, Ramp integration yes and one of their largest, AvidXchange unconfirmed. Their proposal is daily file drops or SFTP rather than a custom build, with a native integration possible if demand justifies it. Their product pitch is deterministic rules where accounting must be exact, AI only where judgement is involved, **nothing posted without a human approving it**, continuous control monitoring on variances, and forward booking of multi-year commitments across 2026, 2027 and 2028. They also have an MCP connector so the finance team and the founders can query the ledger through Claude with role-based access.

Jon's addition is the one worth keeping: live is not needed, daily is fine, *"daily is better than 45 days"* — and the constraint is that with 66 properties and varied charges there still has to be a human in the loop, and the company is actively acquiring, so the rule set is a moving target. He also confirmed there is **no automated booking reasoning layer today**, for Ramp or anything else.

## The facts, and what they change

- **The close is 45 days.** Austin: *"it's a loaded question right now. We believe forty-five days."* [[00-Meta/open-items]] already carries *"accounting runs 30 to 45 days in arrears"* as a Critical finding owned by David Berman. **This puts the number at the top of the range and puts it in front of an outside vendor.**
- **99% of revenue is resident payments, batched daily** through the property management system's payment provider. New to this Brain.
- **About 70 entities** — SPVs per property, management companies, a couple of holding companies, all US, multi-level roll-ups, and *"there could be multiple"* holding companies at the top. Bookings must land on the right entity. Consistent with the 11-tab entity workbook behind commitments item 6.
- **66 properties needing human review**, Jon's number. The portfolio table carries 67 rows and [[00-Meta/open-items]] conflict C2 is about exactly which of them count. **Nobody asked which 66.**
- **The expense-side stack, named in full: Ramp, AvidXchange, NG for utility billing, Rent Manager.** AvidXchange has the direct API; Ramp does not.
- **Ramp's move to monthly journal entries is the specific cause of no intra-month visibility.** This is a vendor behaviour change, not an internal process failure, and it is the first time that distinction is recorded here.
- **Offshore bookkeepers are in use**, Jon's word. Not previously recorded.
- **Accrual handling is unowned at founder level.** Austin: *"I'm sure there are things that we need to do that they do that. I guess in the nicest way, I have stepped away from it over the last year or so… neither one of us are in the day to day anymore."* Insurance, tax, utilities and closing-statement accruals all named.
- **QuickBooks is back on the table.** Austin floated looking at it *"overall"* rather than staying inside Rent Manager. Not a decision, an aside, but it is a direction nothing else in this Brain records.
- **AI use today: the two founders, the investment team and director level on acquisitions and finance. Not the day to day.** Jon: *"we would like it to be pervasive in the accounting department."*

## Decisions

- **A demo is booked for Friday 2026-09-04 at 3:00pm ET.** Austin proposed the time, Jon confirmed. The vendor sends the invite and a recording of this call. **This sits after the 14:00 Executive EOS call on the same day.**
- **The internal controller candidate will be brought into the demo.** Jon: *"we can get the kind of like internal person. It's likely going to be involved on for that."* **The candidate is not named on the recording.**
- **The demo agenda, as the vendor set it and neither founder amended:** high-level platform overview, then automations to drive down month-end close, then the Ramp integration specifically including what happens when cardholders do not fill in required fields, then accruals, then scoping the multi-entity setup.
- **Both founders want to understand the tooling themselves rather than hand it to accounting.** Austin: *"we want to know everything that we're using instead of just passing this off to the accounting team."* Not a purchasing decision, but it is a stated operating principle and it governs who sits in the next meeting.

## Actions

- [ ] **Austin and Jon** — attend the demo, Friday 2026-09-04, 15:00 ET.
- [ ] **Austin with Jon** — decide who the internal controller candidate is and get them into that meeting. This is the same person referenced in commitments item 16, and **naming them to a vendor before the exit is complete is a sequencing question, not just a scheduling one.**
- [ ] **Vendor** — send the calendar invite and the recording of this call.
- [ ] **unassigned** — confirm the vendor's actual name and whether they have an AvidXchange integration. JD did not know.

## Flags

- **The controller exit was described to an outside salesperson on a recorded call, on the same day access revocation was in flight.** Austin's *"I'll speak bluntly"* was answering a fair question about the compelling event, and there is a real commercial reason to answer it. But the recording is going back to the vendor by their own offer, the exit is not complete, and commitments item 16 is under guardrail 7. Recorded as a fact, not a criticism.
- **The strongest single argument for this platform is already a Critical finding with an owner who is leaving.** Berman owns *"accounting runs 30 to 45 days in arrears"* on [[00-Meta/open-items]]. The tool being evaluated to fix it will be selected by his replacement, who has not been named. **The gap between those two facts is the risk on this workstream**, not the software.
- **Nothing here is an agreement.** No pricing was discussed, no terms, no timeline beyond the demo. Parked at the same level as the listings consultation on [[00-Meta/parked-decisions]] — a demo is not a decision.
- **Not established: whether Rent Manager stays.** Austin raised QuickBooks; Jon did not respond to it; the vendor moved on. That is the largest question this call opened and it went unanswered by everyone on it.
