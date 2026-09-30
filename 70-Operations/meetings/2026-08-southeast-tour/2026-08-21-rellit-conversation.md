# 2026-08-21 — Rellit conversation

**Who was there:** Austin, who self-identifies on the call ("This is Austin"), and John, who is addressed by name. The vendor side is represented by at least one person who is not named on the recording.
**Filed:** 2026-08-30, by Claude.
**Source:** [[70-Operations/meetings/2026-08-southeast-tour/Rellit Conversation-Summary]], [[70-Operations/meetings/2026-08-southeast-tour/Rellit Conversation-transcript.docx]]
**Flagged:** The vendor name is transcribed inconsistently across the source files — Rellit in the recording name, Realit in the summary. The recording name is kept.
**Flagged:** Remarks about the finance function are recorded here at role level only. The transcript does not name the person, so no individual is named in this note.
**Flagged:** The transcript says roughly 72 properties each in its own SPV plus five or six additional entities; the summary elsewhere says about 78 LLCs in total. Both figures are as spoken.

## Summary
A vendor call with an accounting platform about replacing the general ledger. Austin and John laid out the structure: two holding companies with two funds under them plus a property management company, roughly 72 properties each in its own SPV with its own LLC and bank arrangement, and another five or six entities handling home sales and title ownership; banking runs through J.P. Morgan Commercial Access with two physical accounts and virtual accounts per SPV. Rent Manager holds the resident ledgers and cannot be replaced, but it is also where the general ledger sits, and that is the piece in question. The pain is timing: books close 30 to 45 days in arrears, so Ramp card spend that used to be reviewed weekly is now booked once a month, which leaves leadership blind on expenses while many employees hold company cards. Austin said plainly that they are open to rebuilding how accounting is done — including pulling the ledger out of Rent Manager via API — to get to a live close. What they want from any new system is a native Ramp integration, a Rent Manager connector Parakeet will help broker, and for the new tool to sit as the nucleus of the finance stack with everything else feeding it.

## Decisions
- Rent Manager stays for resident ledgers, payments and records; the general ledger is the piece open to replacement.
- The standard to hit is a live close — expenses booked as they happen rather than at month end — measured by eliminating the 30 to 45 day lag.
- Any new system has to integrate natively with Ramp and pull Rent Manager ledger data by API; Parakeet will introduce the vendor to the Rent Manager team to help build the connector.
- NG stays for utility payables, and the new platform is scoped as the accounting and general ledger layer only, not an operational tool.

## Actions
- [ ] Vendor — email John and Austin a Calendly link to schedule a 30-minute intro call with an executive.
- [ ] Vendor — prepare for the intro call around the business model, with targeted follow-up questions.
- [ ] Vendor — plan and schedule the deep-dive technical demo of the end-to-end flow from the current finance stack.

## Pages updated
- [[10-Business/departments/accounting-and-finance]] — the 30 to 45 day close lag and the live-close target, Ramp spend booked monthly instead of reviewed weekly, the entity and banking structure as stated on the call, the position that Rent Manager keeps resident ledgers while the general ledger is replaceable, and the Ramp and Rent Manager integration requirements.
- [[10-Business/departments/asset-management]] — the reporting delay as a constraint on reacting and pivoting, which is the stated reason for looking at a new platform.

## Full transcript
Rellit Conversation
2026-08-21 18:50:51
00:00:04 Speaker 1
So We have basically two holding companies. It’s kind of one main company, two funds under that, plus a property management company. And then with the seventy- two properties, each one’s in its own SPV, so they each have their own entity, their own bank— well, let’s not go there yet— their own LLCs and then a couple of. Additional ones, Let’s call it maybe five or six more that handle things like home sales and just ownership of titles. I guess to let you know, which could be important is we run through J P Morgan Commercial Access. So we have one. We actually have two main physical accounts, and then.
00:00:53 Speaker 1
Those are the ones that we’re going to be using for the funds, and then underneath each of those physical accounts are all the virtual accounts for each special purpose vehicle.
00:01:04 Speaker 2
Got it. That is helpful. So, I think we can keep the current format and just add a note about the bold text. I guess another question? I am not sure if that’s within our emails. But in terms of the ledger piece, were you looking to keep that tool or were you looking to roll it out as a replacement option?
00:01:39 Speaker 3
I think to some extent, it needs to live there because that’s where our payments and everything we can’t really disrupt or change the resident ledger, which is obviously a big driver on the revenue side. It comes through there automatically because the majority of residents pay online and it attaches to all their records, so that can’t be changed.
00:02:06 Speaker 1
I Am gonna shock John. This is Austin, and he’s probably gonna crash after I say this. We’re open to understanding how this could work and understand how it would flow because we can have an API with Rent Manager that pulls it out. And then, Maybe do we have to rebuild Because if we can get rid of the CFO and have accounting be live and really improve our accounting and finance department by changing the way that we do things, maybe a little uncomfortable at first, but you know get to where we need to be.
00:02:41 Speaker 1
We’re open to it. I am shocked. Right.
00:02:46 Speaker 3
But one of the things we’ve struggled with for five years since we started the company is that initially, Austin was doing all the work. We had to do a lot of research on this topic. Right? Okay, so I think it’s important to note that when you’re looking at something like this, you have to be careful about how you interpret the data. The thing is, we were trying to figure out what the best way was to handle our financials. Initially, Austin was doing all the accounting because we didn’t have a CFO or any finance and accounting infrastructure. And then we brought one person on; she was awful. Then, we brought a CFO on or the controller or whatever you want to call him. He’s definitely like gotten it off our plate, but it’s been a massive struggle still. Making sure that books are closed, making sure that everything is done on time. From our perspective, I guess what did catch my eye on you guys is it’s like a live close. And that was from a reporting standpoint, from a business management standpoint. We are getting to the point where we’re close to like, we can review, and we can look at stuff thirty to forty five days in arrears.
00:03:36 Speaker 3
Our business like being able to look at something and know it live asap. That’s the better we can react and change and pivot and solve problems. And so that is what actually caught me on.
00:03:51 Speaker 1
These guys, this thing. So maybe a couple other things that are helpful because I can’t believe I am as open as I am through this conversation.
00:04:03 Speaker 3
Which they integrate with.
00:04:04 Speaker 1
Which is great. So that’s a great example of not having live books. They are not because they’ve got whatever their excuse is, which I don’t think is a very good excuse. They’re not booking transactions until the end of the month. The fact that we can have a way when people are booking things or putting their memos and allocations in ramp, and it should be booked right away. And therefore we know where we are. We know if something was booked correctly. It should be super easy in our mind. The fact that it’s not. I used to do it once a week at least to give me an idea of what the spend was per week. Now they’re doing it once a month so it’s kind of like blind.
00:04:59 Speaker 1
Which is not very comforting with everybody running around with credit cards.
00:05:06 Speaker 2
I totally hear you on that part. It sounds like you guys have really done your research. You’re kind of taking all my talk tracks away from me. You’re kind of taking all my talk tracks away from me.
00:05:15 Speaker 1
We try to give you as much information and be as open a book as we can because we don’t want to waste your time or ours.
00:05:24 Speaker 2
Absolutely, I do want to note so insurance, The rent manager as a tool. I just wanted to like that. We currently don’t have any sort of like operational rent management, module within realit itself. We would still need that tool in terms of all the operational support. And then realit would be the accounting piece if you are open to.
00:05:52 Speaker 3
What I think is how we thought about it.
00:05:54 Speaker 2
Kind of makes sense.
00:05:56 Speaker 3
Which I think is how we thought about it. Quite frankly, the revenue side and the resident side is live all the time, so we can see you know as soon as a resident pays their rent, We know the day it comes in like that is more automatic than the expense side. And the accounting side of it. I guess.
00:06:17 Speaker 2
Definitely, and we don’t have a native partnership with them as of today. But we are built on an open API architecture, so it will be a build.
00:06:32 Speaker 1
We can make that introduction as well.
00:06:35 Speaker 2
Build a connector there.
00:06:36 Speaker 1
We can definitely make an introduction because I think it is one. It’s great that they have everything in one place;. They’re the only ones that really do that. But at the same time, it’s not as easy; it doesn’t have this functionality so they might be, Pretty open to having an.
00:06:54 Speaker 3
They have tons of APIs.
00:06:55 Speaker 1
We do a bunch of integration partners with them and make introductions so.
00:07:02 Speaker 2
Wonderful, awesome.
00:07:04 Speaker 1
And as we’re talking
00:07:05 Speaker 2
Do you mind just giving me a go ahead? Go ahead, sorry. Go ahead.
00:07:10 Speaker 1
Do you do utility payables or anything like that?
00:07:14 Speaker 2
So go ahead.
00:07:15 Speaker 1
Do you do utility payables?
00:07:17 Speaker 2
Sorry, I think we have a lag.
00:07:20 Speaker 1
Anything with utilities, like we use NG for our utility kind of billing AP.
00:07:30 Speaker 2
So in terms of utilities, we don’t either. We think we would just be the revenue recognition piece. We would just be anything that surrounds the general ledger. We don’t really have any sort of operational inventory. Manufacturing modules made in real health, so we would just be that a recapping piece.
00:07:59 Speaker 3
So it’s really just a live general ledger, essentially.
00:08:04 Speaker 2
Correct. So that’s our work huge plus there in terms of integrations as well. I would say Realit is almost kind of like the nucleus of the finance stack, if that kind of makes sense. We’re kind of built or our apps integrations as well. You mentioned Brand, we have a native partnership there, so that would flow kind of seamlessly to Rollit as well. In terms of real estate and the operations piece, that would have to be kind of outsourced.
00:08:43 Speaker 3
Okay, I think that’s fine. That makes totally fine.
00:08:49 Speaker 3
Maybe we schedule a demo.
00:09:01 Speaker 3
You’re Breaking up a little bit.
00:09:05 Speaker 2
I’m sorry about that. You hear me now?
00:09:07 Speaker 3
Here that’s better.
00:09:12 Speaker 2
I hope you don’t get into another rough patch. I just asked if you had any other questions before I will discuss the.
00:09:24 Speaker 2
No, I think we’re good. So eventually, the next steps here would be one of our executives for essentially a thirty minute intro call. You can chat through your company model, and they’ll ask some more follow up questions there. Then this would be the scheduled deep dive. Technical demo essentially, so that’s where Wolper Business Solutions is consulted. It’s CPK led, so any technical accounting questions and specific business they have, that’s what we’ll run through end to end, real to your current finance. How does that sound?
00:10:13 Speaker 3
That sounds good. If you’re in that, Wait. Wait. A little choppy, but we got it. So if you want to email me to set that up, I’ll loop Austin into the email too and then we can get it scheduled.
00:10:29 Speaker 2
Yes. Actually I’m just gonna go look at my calendar. Now if you wanna schedule a time, or do you not have access to calendars since you’re dropped?
00:10:39 Speaker 1
Maybe email us and then we could sit and look at a calendar.
00:10:44 Speaker 2
Got it.
00:10:46 Speaker 3
No. Or even if you send the cal if you send the link to the Calendly. We can just book a meeting and talk about it. We can look at it and just schedule away.
00:11:00 Speaker 2
Absolutely. I’ll have them do a follow up email to get all some about your today and excited they could help save. Awesome.
00:11:14 Speaker 3
We appreciate the time and look forward to continuing the conversation.
00:11:21 Speaker 2
Of course. Have a good week.
00:11:24 Speaker 3
You too, thanks a bunch.
