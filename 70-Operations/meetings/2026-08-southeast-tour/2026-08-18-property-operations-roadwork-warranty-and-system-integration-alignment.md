# 2026-08-18 — Property operations, roadwork warranty, and system integration alignment

**Who was there:** Ten speakers on the recording, not individually identified (Speaker 1-10 in the diarized transcript). No participant is named or self-identified in the raw text.
**Filed:** 2026-08-30, by Claude.
**Source:** [[70-Operations/meetings/2026-08-southeast-tour/08-18 Meeting_ Property Operations, Roadwork Warranty, and System Integration Alignment-Summary]], [[70-Operations/meetings/2026-08-southeast-tour/08-18 Meeting_ Property Operations, Roadwork Warranty, and System Integration Alignment-transcript.docx]]
**Flagged:** The transcript never names the community this walk took place at. It is the first recording of 2026-08-18, before the Auburn Ridge stop that afternoon, and Parkwood is mentioned only as a comparison. Filed against the department pages only rather than guessing a community.
**Flagged:** Home titles were reportedly registered in the prior manager in her own name, blocking residents from getting insurance. The prior manager is not named on the recording and no owner was assigned to chase the title fix.

## Summary
A long morning working session that ran from a walk of the community into a vendor dispute and then into the systems project. On the property side the group went through the closed pool (permit in hand, but it cannot open until the surrounding fence is replaced to compliant height), illegal dumping that is blocking the haulers from the dumpsters, security incidents including break-ins and a car theft, drainage running into backyards off a single rolled curb, and homes whose titles the prior manager had reportedly put in her own name. A recent road project has produced significant flooding and plugged storm drains, one of them covered only with two-by-fours and metal sheathing, so the team decided to pursue the warranty and to price the repair independently. On systems, the group reset the Rent Manager / QuickBase / FastField project after the July launch target slipped and a communication gap between the vendor sales team and the implementation team came to light. The agreed architecture is QuickBase as the governing layer over data Rent Manager exports daily, with FastField as the field entry layer, and a walkthrough of Rent Manager was set for 2026-08-25.

## Decisions
- Pursue the warranty claim against the roadwork vendor: gather every prior communication, confirm warranty terms, send a firm response, and treat legal action as live if the vendor does not respond.
- Get independent quotes from national paving vendors (Rose Paving named) to document the scope and cost of the drainage repairs.
- Move the community off shared dumpsters to individual cans with a chargeback, and use escalating fines for illegal dumping (75 dollars, then 150 dollars).
- Keep the pool closed until the surrounding fence is replaced to compliant height; pick one of the three pending service plans (3, 5 or 7 day) and get staff certified for water management.
- List the vacant home to gauge market interest before spending anything on rehab; the pricing frame discussed was 1,100 dollars lot rent against a 30,000 dollar purchase.
- QuickBase becomes the system that governs data and enforces the workflows Rent Manager does not: a daily Power Automate export from Rent Manager into SharePoint, read by QuickBase, whose metadata drives the dynamic dropdowns in FastField (for example, only vacant lots offered on a move-in).
- Field staff enter data in FastField; corporate uses QuickBase for analytics, process monitoring and bottleneck spotting.
- Approvals run community manager, then regional or district manager, then Natalie for final approval, enforced in QuickBase.
- Phase one runs on file exports; the two-way Rent Manager API integration is a later phase.
- Ship the physical archives (maps, photos, water system documents) to the office to be scanned and backed up digitally.
- Contact prospective applicants who start but do not finish an application, before they pay the non-refundable fee, to deal with whatever concern stopped them.

## Actions
- [ ] Unassigned — hold the walkthrough of Rent Manager with the implementation team — 2026-08-25 (date stated in the meeting; no owner named).
- [ ] Unassigned — draft and send the firm response to the roadwork vendor, with prior emails, photos and the contract attached.
- [ ] Unassigned — make the compromised storm drain safe; it is an immediate hazard.
- [ ] Unassigned — provide the implementation team with the Rent Manager metadata exports: community list, property IDs, lot numbers, occupancy status.
- [ ] Unassigned — contact the county about the deemed-real-property status and what it requires.
- [ ] Unassigned — inventory the newly found maintenance shed, including the zero-turn mower.
- [ ] Unassigned — secure and clarify the title for the pending sale, and identify the right contact for the resident home title problem.
- [ ] Unassigned — scope and budget fence renewal and removal of the chain link sections.

## Pages updated
- [[10-Business/departments/property-operations]] — pool compliance and service plan, the move from dumpsters to individual cans with escalating dumping fines, camera coverage at the office, clubhouse rental policy, and the resident home title problem left by the prior manager.
- [[10-Business/departments/construction]] — roadwork warranty claim, the plugged storm drains and the rolled-curb drainage issue, and independent repair pricing from national paving vendors.
- [[10-Business/departments/sales-and-marketing]] — list-before-rehab pricing test, and the practice of calling back applicants who stall before the non-refundable fee.
- [[10-Business/departments/accounting-and-finance]] — the warranty claim as a potential recovery, and the pool and fence spend that has to be budgeted before the pool can open.

## Full transcript
08-18 Meeting: Property Operations, Roadwork Warranty, and System Integration Alignment
2026-08-18 08:46:34
00:01:48 Speaker 1
Good morning. Good morning. You’re so welcome. You got it
00:02:00 Speaker 2
You got it. This was done by former maintenance staff. Has it been mostly air?
00:02:15 Speaker 2
Oh nice, oh fantastic.
00:02:51 Speaker 2
Yes.
00:04:16 Speaker 3
Oh really. That’s not a good thing.
00:04:29 Speaker 4
But that’s why we come so that we can help with it.
00:04:34 Speaker 2
Do people use the lawn area at all? There’s like soccer nets or something there for the kids.
00:04:39 Speaker 3
A lot of people walk their dogs there.
00:04:41 Speaker 2
Got it.
00:04:43 Speaker 3
Um, I would suggest maybe a dog park, but I wouldn’t do that here.
00:04:47 Speaker 5
Dog park?
00:04:48 Speaker 3
It would take care of that. Yeah.
00:04:51 Speaker 3
But maybe a park?
00:04:53 Speaker 2
Something playground? Maybe a little playground? Playground could be nice to have something there actually,
00:05:01 Speaker 1
Yeah, I’m saying sure, The first is the most important.
00:06:49 Speaker 1
So, Hopefully, they will be moving in at the end of this month or the end of September. I think with financing, you know.
00:08:55 Speaker 2
Now I was questioning this morning because I saw that one sale. Which sale fell apart because he couldn’t sell it or something? Yeah. Which one was that? That one. I think.
00:09:18 Speaker 3
They’re states without a council.
00:09:20 Speaker 2
That’s what Natalie was saying. Can we just get a title for it? The title.
00:09:32 Speaker 5
Of property is the next thing that’s going to be discussed.
00:09:57 Speaker 2
Should we have been? Fifteen ceiling. Or wait, what about when we put this on the market? Eleven hundred. It’s eleven hundred rental. Eleven hundred to thirty thousand purchase.
00:10:17 Speaker 1
Thirteen minutes. Pulling all those out. We should do that. That’s the difference.
00:10:50 Speaker 5
Five Dollars. Let’s.
00:10:57 Speaker 2
See what happens with it. See what happens. It doesn’t sell. Get someone in here to do a little bit more rehab or whatever kind.
00:11:06 Speaker 1
Of thing. I don’t think carry stuff all the time.
00:12:02 Speaker 4
This Is deemed real property.
00:12:56 Speaker 2
Yeah, We should reach out to the county and see.
00:13:15 Speaker 1
So, The.
00:13:24 Speaker 3
Person that’s put the same for preventative application with this one is a herbicide. So, we can sell this one. So,
00:13:30 Speaker 2
They can do it too. Oh, so we could have even done that one? Oh, nice. That’s good.
00:14:21 Speaker 4
How Long did this take for the third operator?
00:14:32 Speaker 1
Yeah. A Lot of times when we’re doing these tours,
00:14:42 Speaker 5
Most of the tours that we do put an application out.
00:14:47 Speaker 4
They just don’t pay attention to it.
00:14:48 Speaker 5
They just don’t submit it. So we’re reaching out to them, seeing if you know. Yeah. Especially in Hawaii because if you get. Are we still doing that? If you get approved, buy it with credit card applications. So if you don’t have a concern, we have a lot of stuff. Yeah, which is basically okay. You know what is that? Not so they bounce back today fifty dollars out of state.
00:15:19 Speaker 2
That’s like after they’ve had conversations and you submit your application.
00:15:23 Speaker 3
Not submitting an application.
00:15:40 Speaker 2
What else? What else is going on? Anything else that we should think about to help push the free bags. We’re done with mailboxes. That’d be a good thing.
00:15:54 Speaker 3
I think budgeting to renew some of the fencing would be great.
00:16:05 Speaker 2
Other what? The white, the white we should just fix something. I hate chain. If anything, we should remove the chain link. You know because it’s such an estimation.
00:16:33 Speaker 5
That would be.
00:18:20 Speaker 1
And they came up.
00:20:32 Speaker 1
We have one rolled curb in the entire.
00:21:08 Speaker 4
And that’s so it flows right through the backyard.
00:21:39 Speaker 2
There might be a curve on the other side.
00:22:13 Speaker 4
Do we bill for utilities or is it included?
00:22:22 Speaker 1
You know?
00:22:56 Speaker 1
Okay.
00:25:39 Speaker 4
Leave their cans or do they pull them to the back.
00:25:46 Speaker 1
Have a lot of.
00:25:59 Speaker 4
Questions where mailboxes, fencing, and uniformed mini blinds in all the homes are being marketed. Trash cans.
00:26:14 Speaker 1
It’s actually a trash can that’s just.’cause.
00:26:34 Speaker 4
It’s resident care, if that’s. do we know that this is back in the.
00:27:41 Speaker 1
Two of thirty two.
00:28:16 Speaker 1
Sorry. Sorry. Sorry. Should.
00:28:27 Speaker 2
Keep that concrete sign just to have to like do that. That’s.
00:28:33 Speaker 1
True. Don’t pass it up. That’s the front of it.
00:28:46 Speaker 4
Cause people feed them. And cats fuck like rabbits and there’s kittens everywhere, and they’re impossible to get rid of. I don’t give a fuck if this is abandoned or not, clean it up. You should have seen in Parkwood, it was the same thing.
00:29:23 Speaker 1
Marcus. Just. That’s just a little bit. Probably not. Probably not. It’s about.
00:30:05 Speaker 4
Still lower quality residents. Is it worth putting the money into turning it more to try to get the higher quality residents or, like, is the demand there to fill that stuff?
00:30:27 Speaker 1
It’s just a little blood.
00:31:17 Speaker 1
Yesterday at 8:00 a. M. It was, and it was cooking.
00:31:46 Speaker 1
Probably a pet. That way they get eggs and then they chop it up later.
00:33:36 Speaker 3
Oops. Is that a work in progress?
00:33:38 Speaker 4
Work in progress or war zone?
00:33:40 Speaker 3
Both. It’s not like that.
00:33:45 Speaker 4
Seriously? I expected to walk into something much worse.
00:33:51 Speaker 6
It’s always been planned, but it doesn’t ever look that bad. Not at all because the pictures are on the pan.
00:34:00 Speaker 4
And there’s no um covers. Let’s see what happens, then I can’t help you
00:34:20 Speaker 4
Then I can’t help you.
00:34:27 Speaker 3
Question. Do you know if anyone has access to the cameras that are recording?
00:34:50 Speaker 7
I think everybody who got it does ask for it.
00:34:54 Speaker 7
Everybody got it? If I can get orange to be straight like that, sure, why not? As soon as they came on the orange, I don’t see nobody.
00:35:08 Speaker 5
The best.
00:35:18 Speaker 4
So do you want to use this as a clubhouse as well?
00:35:22 Speaker 4
But we’re just going to keep this closed. When we use this as a clubhouse for people who rent it out or just always keep it closed.
00:35:29 Speaker 3
I think we should have already asked.
00:35:31 Speaker 4
They have.
00:35:32 Speaker 3
We just had a resident event. We grilled hot dogs and served the hot dogs and gave out backpacks for back to school. I think it’s mostly needs a little. And then the pool.
00:35:52 Speaker 3
The pool. Figure out, kind of taking care of it or I’ll purchase some chlorine and go out there and put it in.
00:36:01 Speaker 2
Do we have regular pool maintenance?
00:36:04 Speaker 3
We do not. I sent three different estimates for three day, five day and seven day. Just waiting to hear back on that but I feel like we got it looking really good right now. So I’m not too worried about it.
00:36:18 Speaker 4
We get the permits and everything for it?
00:36:20 Speaker 3
We got the permit, but we can’t open it because the fence has to be replaced. It’s too short. That’s what happens. You guys want some water or anything?
00:36:48 Speaker 2
You need to get a break point.
00:36:52 Speaker 4
I don’t think you guys should be doing it.
00:37:03 Speaker 2
That’s true. I think it’s great what they do because there’s a process to doing it. I wouldn’t want you guys to have to just guess.
00:37:16 Speaker 3
But once you start.
00:37:23 Speaker 4
Testing all the water levels.
00:37:28 Speaker 2
I’m sure there’s like a training course. I’m sure. But.
00:37:44 Speaker 4
We should put something in the budget to clean this up a little bit.
00:37:48 Speaker 2
Would people use this?
00:37:50 Speaker 4
Yeah, they’ve already gotten requests. Yeah.
00:37:53 Speaker 3
They wanted to host a baby shower in here. That’s when we first took over, and I was like,“ Oh,
00:37:59 Speaker 2
I don’t know.“ I mean, how would we do it? Is there just like a little rental fee?
00:38:05 Speaker 4
Yeah, you do look at deposit. You either do a deposit or or a fee for it.
00:38:09 Speaker 7
Did I have place where I was at my club’s women. They got a building that she can hang out for parties and stuff, birthday parties and stuff like that.
00:38:18 Speaker 3
This this door right here, locks, too. So we would just have to give them access to get in.
00:38:23 Speaker 4
Yep, and I guess we probably would have. I’m guessing we’re gonna have to open the pool to be able to do it because otherwise you’re giving them access to the pool to get to here. It’s like a waterfall. Got it,
00:38:38 Speaker 3
But I believe we definitely need cameras in the office, outside of the office, and around the parks and definitely in front of here. Yes, yes. Okay, I’ve purchased a little doorbell one for. The front door because we’re having a lot of kind of incidents with people coming in. So once we put that there, they’ve kind of calmed down when they’re entering the office.
00:39:00 Speaker 4
Just but okay, so when they’re coming in, they’re coming in hot and heavy.
00:39:04 Speaker 3
Sometimes. Yeah. Really? Sometimes sometimes more with me than anyone else.
00:39:12 Speaker 4
Interesting And that’s calmed down though?
00:39:16 Speaker 3
Yeah definitely since we put the camera on the door and I see that we’re recording them in. Enter the office. They kind of come in a little easier, but we have children going around breaking into houses, breaking windows. We had someone steal a car last Friday and a lot of other things, so I think that cameras would be helpful.
00:39:52 Speaker 3
I work with there people that are there kind of just stealing our items, our signs.
00:39:57 Speaker 4
Yeah, just to be a pain.
00:39:59 Speaker 3
Flags and flowers. And flowers.
00:40:05 Speaker 4
Basically dig them up and plant them in their yard?
00:40:10 Speaker 7
That’s what they were saying when we have angel pictures inside, they just steal the flowers.
00:40:16 Speaker 4
It’s unbelievable. It’s just the hatred. That’s all it is.
00:40:23 Speaker 4
Correct, You have a put you have a choice.
00:40:48 Speaker 3
Yeah, The trail.
00:40:49 Speaker 7
Yeah.
00:41:18 Speaker 4
You can’t get.
00:41:19 Speaker 1
And just leave it there. They will sit in front of the trash cans. It’ll be empty when they don’t care. They sit right in front of the trash and walk away. You’d have to move all those bags, put a trash bag, open the doors.
00:41:43 Speaker 3
That’s another thing we have a hard time with having a regular dumping because when they come to dump the bins, there’s so much stuff there that they can’t get in there.
00:41:52 Speaker 2
Can we do cans here?
00:42:00 Speaker 4
Just because there’s so many, it still might be worth it than putting all the money into. The probably biggest thing is unless we’re gonna sit there
00:42:14 Speaker 2
I don’t even think you.
00:42:16 Speaker 4
But I don’t think you can actually enforce the dumping fees. You’re going to put it on somebody’s license plate. It’s always just an empty threat.
00:42:25 Speaker 2
People don’t correct.
00:42:28 Speaker 4
So it’s almost one of those just put up a fake one because you’re not going after the person, like you’re not going after their license plate. There is one and they don’t give a shit.
00:42:41 Speaker 7
They don’t care.
00:42:42 Speaker 4
Because they know what you are. We should look into the cans just to get rid of it.
00:42:52 Speaker 3
I was thinking about the cans or removing them in general, making people take their own trash to the dump.
00:43:02 Speaker 4
I think that’s a fantastic idea for about two weeks. And then Marcus is going to hate you because now it’s going to be on the side of everybody’s house just lined up.
00:43:18 Speaker 4
They’ll just leave it there waiting for you to pick it up.
00:43:21 Speaker 7
But see, the thing is too, If I have to pick it up and find them, and you won’t do a small fine because that’s what the thing is. If I if we have to come and pick that trash up, that’s every time that’s seventy five dollars sometimes going back go look. That’s a hundred fifty dollars each time that, You Have to come snatch. Your trash is not going to be the regular price. It’s the second time you came. Yeah, that’s hundred fifty.
00:43:54 Speaker 7
It’s the
00:44:14 Speaker 4
Only Way. Hit them where it hurts, the pocketbook.
00:44:16 Speaker 2
We do the cans, we can charge back. Just make a bad charge of traffic.
00:44:22 Speaker 4
I think that’s what you do. I think we should just because then you’re not worried about dumpsters.
00:44:30 Speaker 7
Dumpsters are the worst because I know in my neighborhood, I have to take my own trash cans like that. We don’t pay for that.
00:44:38 Speaker 4
And
00:44:39 Speaker 7
Yeah, yeah.
00:44:42 Speaker 4
I think that’s definitely the better.
00:44:45 Speaker 2
How’s the issue with the people saying that they didn’t have the titles for their homes?
00:44:54 Speaker 3
Um, yeah, there’s still a lot of so basically what was happening is previous management, The manager that was in office was going to the DMV and putting the title in her personal name.
00:45:08 Speaker 2
When it comes to
00:45:11 Speaker 3
And telling them that they couldn’t get it back for ten years.
00:45:19 Speaker 2
That’s crazy. Are we, is the seller working on this side? Do you have, are you guys getting resolution on that front at all?
00:45:26 Speaker 3
I have not heard from the seller since we grabbed keys. We also have a maintenance shed here that we did not know about until like two weeks ago. No way. Yeah, So we got in there, and there’s like a zero turn and all kinds of stuff. So Oh, that’s fun.
00:45:41 Speaker 4
Let’s go driving.
00:45:43 Speaker 2
It’s like shed wars.
00:45:45 Speaker 4
Storage Wars, shed wars. Um, yeah, let’s follow up with whoever on the title stuff. That does it.
00:45:53 Speaker 2
Because they should know we’re within the contract period to need to fix that shit. You know,
00:45:59 Speaker 3
I can’t say for sure if that’s what she did, but that’s what her residents told me.
00:46:04 Speaker 2
And they’re saying that just the title. Well, have you seen the title? They didn’t tell us the title if it was in her name.
00:46:09 Speaker 4
Well, we’d have to you’d have to look up the registration and everything.
00:46:18 Speaker 4
Yeah, no records of a title. So, then that means that she basically probably has fifteen homes or whatever in her name, Which would be the dumbest thing you could do, because why are you saying they were? Why would you? You literally here is a paper trail right to me of what I did.
00:46:29 Speaker 2
And you have to pay taxes.
00:46:32 Speaker 4
It’s people. Um But overall they’ve been nice about it. They’re not giving you a hard time about it. They just want the title of their home. Because they also can’t get insurance for it. Yeah.
00:47:21 Speaker 4
How many wells are there? Two.
00:47:32 Speaker 1
I’ve heard about.
00:47:43 Speaker 2
Fence raising, but we haven’t broke ground on it yet.
00:47:48 Speaker 4
Well, you want to, you can see why. What? It’s gonna cost an arm and a leg.
00:47:57 Speaker 2
I remember it potentially about being only like it’s all concrete.
00:48:02 Speaker 4
It’s all concrete and it also connects to the foundation of the hall.
00:48:07 Speaker 2
Well, That’s what I think John was saying we could add.
00:48:10 Speaker 4
Just add up add up.
00:48:22 Speaker 2
Higher fence surrounding it. Yeah, but needs to be higher? The whole perimeter. If you come over here and take a look,
00:48:37 Speaker 1
The house is in back.
00:49:01 Speaker 4
This Has to come up all the way. This is the one big side because that one drops off.
00:49:32 Speaker 1
No, it’s all the way around.
00:50:02 Speaker 1
Which one? Awful. But.
00:50:16 Speaker 4
Here’s the thing, You don’t you can take it up on the back side to leave this side open. It’s just how much higher this side has to go, which isn’t as bad as over there.
00:50:29 Speaker 2
I mean, it’s kind of what they did with my top deck. Like you can actually stucco it and it doesn’t.
00:50:33 Speaker 4
You won’t see the difference. Only if you need a couple inches, but if you need like feet, it’s going to be you’re basically swimming in a concrete box. So you’d have to do stuff like this.
00:50:45 Speaker 2
So you do something that matches this on that side up. Yep And then same way, extend the concrete, and you extend this up Yep Or arguably replace it to make it.
00:50:58 Speaker 4
They look like it better just shellacked over or whatever. Yeah, because that’s what the whole all those tiny walls are. Yeah, But that’s yeah,
00:51:07 Speaker 2
We should be able to come up with. We should talk to Mark about it. Because.
00:51:12 Speaker 4
If that’s all that’s holding it up, at least they could get it done.
00:51:16 Speaker 2
But also the the concrete pool dock needs to be sealed. It needs grinded down and.
00:51:29 Speaker 2
Is the integrity of the pool pond?
00:51:34 Speaker 5
Jump in, tell us.
00:51:35 Speaker 3
Um, did you see all of these spots? Those were all packed. So we drained it, cleaned it, washed it, filled it back up. But since we can’t really. we don’t really know what we’re doing as far as cleaning it, it’s kind of looking like this again.
00:51:56 Speaker 2
We should get Marcus the certification.
00:52:05 Speaker 1
It’s a daily. Ooh.
00:52:11 Speaker 2
What? Of the water? Yeah. Um, let’s go around the park. Where’s the, The old playground is down there.
00:52:48 Speaker 2
I feel like doing something like that, along with pushing the trash back on them. Cared well.
00:53:04 Speaker 1
That’s all they got.
00:53:10 Speaker 4
I didn’t even hear me there. What’d you say? We’re not paying attention to you.
00:53:14 Speaker 3
Oh, oh, I think those are.
00:53:19 Speaker 3
I have the entire. Oh, right.
00:53:25 Speaker 2
Yes, Should we have her send all that? Yeah,
00:53:27 Speaker 4
What we could do is somebody get your office or office. We could send it to one of the offices and have them basically get them scanned in. Yeah, because that actually will.
00:53:38 Speaker 2
Yeah and.
00:53:39 Speaker 4
Have his life.
00:53:50 Speaker 1
That’s that’s from a water system. Yeah.
00:54:00 Speaker 2
Yeah, we should we should well, we’ll send you a label. We’ll just ask Melanie for a label. Yeah, and then like go ahead and send it now.
00:54:08 Speaker 4
And, we’ll get all this shipped up to put it, put all of it in tubes or a box. And because that’s actually helpful, because if anything happens, then we have it like digital. But that way, it’s also it’s all. We’re going to need all this. This is all your photography. We’re going to send this down. Actually, here’s the question: Is P.B. Harrison Jr still alive and kicking?
00:55:15 Speaker 2
Music With all the modern conveniences, designs. Once we can have the beauty of the land and freedom. I do not believe that there’s a right way to run. Interesting.
00:55:34 Speaker 2
I mean, there is that is there is an area down there that’s plugged up. So I wonder like back and get it. That’s probably.
00:55:48 Speaker 1
Little tools dated.
00:55:54 Speaker 3
I can send them, but I also can scan them and send them as well if you want.
00:55:58 Speaker 4
There’s a place I, We did it before because we took a whole bunch of stuff that they’ll take our friends and be able to scan them in versus like trying to do it.
00:56:07 Speaker 2
I guess the question is if we figure out that place,
00:56:18 Speaker 1
Most of those places won’t keep back your stuff.
00:57:05 Speaker 8
Before I am sorry to interrupt you guys, but like this this road email that John was sent out. I want to make sure I am addressing properly.
00:57:14 Speaker 4
Oh, it’s legal. It’s so bad.
00:57:17 Speaker 8
It, shouldn’t it should it should not be legal like we should be warranted and I am going to write that back to you guys. I am trying to write something not to throw John Clark under the bus, but at the same time, give him direction and ask him if we re engage the comp, the vendor after. The initial conversations, I’ve been screaming from the rooftops since these were done that we had an issue. He’s known about it. We have all the documentation about it. So, I am asking you, do you because John Wiss addressed it to the both of us, which gives me the inclination he wants me to step in to fix? Yes, and I am fine with that.
00:57:56 Speaker 4
Yes, Because well, part of it, yes. And also on part of it on the fact of finally. Like realizes that if you want something done, you need to be connected to it. Um, I am going to respond either way before you do and probably say something else. And be like, “This is i the fact that we’ve known about this for this long. “ The fact that it has not been an ongoing topic of conversation, and we would run out of warranty period legal. We should be all over this guy. We should be figuring out everything.
00:58:29 Speaker 4
Every way to ding his license. I mean, the whole dream t here is massive issues with it. Like, This is not this is not a small. This is not a small game to play.
00:58:43 Speaker 8
So so if you don’t want me to respond, I won’t. My response was going to be obviously that we had concerns right from the completion of the project. John was the vendor reengaged after those conversations. We should still be within warranty periods, so I think that’s the first place to start. Has anything been sent back to them specifically regarding the flooding and drainage? I would suggest that we confirm a couple of things: what has already been communicated with the vendor, what warranty coverage is listed in the contract.
00:59:16 Speaker 4
I am going to let me be the hard one first, and you can follow up. I am not even going to play nice; I am going to say it. Yeah, let me.
00:59:24 Speaker 8
I know, but when you are doing it because it’s written to the two of us, it looks like it looks like I did something wrong. And I am fine with that. I just want to make sure.
00:59:32 Speaker 4
That you are clear on my.
00:59:34 Speaker 8
Thing up wherever I need to.
00:59:35 Speaker 4
Yes, and let’s put it this way: you don’t. It might be might look like it’s coming from both of you, but at least for your sake, At least it’s a way for you to say let’s work together to get this fixed. But don’t take it.
00:59:49 Speaker 8
No, I’m not taking it personally at all. I just, I want to know again, my, my, my call is more for how how deeply involved do you want me to get? Do you want me to direct him? Do, you want me picking up the phone and calling the fucking vendor because I have no problem doing that. I just haven’t because I didn’t want to step on somebody’s toes.
01:00:12 Speaker 4
Let’s see where this goes.
01:00:15 Speaker 8
He Responded and his response was basically, yeah, I agree legal legal should get involved. Like that was I can’t see any resolution outside of trying to get legal involved. That’s what he said.
01:00:31 Speaker 4
Let me see if I can write something real quick, and if it makes sense and go from there.
01:00:38 Speaker 8
Do you want me to send you what I started writing?
01:00:42 Speaker 4
No, I don’t want to get confused. Give me two seconds and try to see if I can get something out. And then yeah, I’ll send you some. I’ll send it to you first. The i’m deleting it out of mine. The only other thing is is i’m not going to get on this call with clickbase just because i’m on site, and it’s not going to do any good, and i’m just going to sit there and end up yelling at them. Um.
01:01:11 Speaker 4
And I would, even though, yeah, I’ll explain. Is it more than.
01:01:15 Speaker 3
You want us to just reschedule it?
01:01:17 Speaker 4
No, I mean, I think we could get they need to start doing something. Um, I mean, I can get on. Yeah, I’ll get off. Let me see if let me see if I can write this. Yeah, Let me see if I can just run this by you, real quick for this response to this email. And then one thing at a time. Still like it’s hot my brain’s not working.
01:01:40 Speaker 4
Well, it’s hot. My brain’s not working, And I was we were basically up in the hotel till like three, three thirty in the morning. Fucking I was building out quick base, But it’s just so um okay, uh, give me two seconds and I’m gonna see if I can just diarrhea them out this to you. I agree we need to pull out. All stops. However, before we go that route, I need to understand every step and every detail that has been taken from conversations, emails, etc. with this vendor. As, this is not the first time this has been brought up ;. It’s almost been brought up since day one when the project was completed.
01:02:40 Speaker 4
We need to get all of our ducks in a row before going forward. John, I don’t know where your relationship stands with this vendor. If it’s worth making a phone call, having Natalie reach out or having just an initial letter sent letting them know, especially with the warranty factor.
01:03:08 Speaker 4
Before making an educated decision, because this is going to not be a pretty conversation. We need to make sure that we have our t’s crossed, i’s dotted and ducks in a row.
01:03:48 Speaker 4
Draft a follow- up email to John Wiss’s construction email and John Clark’s response. Below are some thoughts.
01:04:01 Speaker 5
On what I would like to say.
01:11:15 Speaker 4
We Also need a mailbox and closure. We’ll drag her down.
01:11:33 Speaker 1
Um, drain that’s plugged up. She said. I’m.
01:11:50 Speaker 4
Really curious if this recognizes house or not.
01:11:52 Speaker 2
Be amazing. Um, so look right here. The roads don’t need repaved, but there’s I guess there’s steam marks over here that drains. Coming down in so like it’s just people’s cars. So we should raise the trees. We.
01:12:11 Speaker 4
Didn’t do the roads here yet. Okay,
01:12:14 Speaker 2
But they also don’t need to be down there. No, but if we cut out the sections where the drains are, above with drains, I guess that’s our just.
01:12:43 Speaker 1
I’m sorry.
01:13:16 Speaker 4
Same thing the other storm drain.
01:13:22 Speaker 1
I’m inclined to tell them. She can come if she wants, but I feel like.
01:13:30 Speaker 4
Is there something that we should be looking at, otherwise we’re going to drive through it?
01:13:34 Speaker 2
Yeah, just to tell her or we could just face time her. Just so she doesn’t have to like go around.
01:13:45 Speaker 1
Watch out.
01:14:18 Speaker 4
Go away. It’s it’s absolutely ridiculous. Why, do you think you know why when I pulled out the paintball gun from the trunk? Yeah, I did it for the deer in my neighborhood, So now I’m thinking about doing it here for cats, and you can just tag them with a different color.
01:15:07 Speaker 4
Also, Add to the email. That I want to get. Quotes. From. National vendors. Like Rose Paving. To have something in the file to be able to hand to this guy or legal. To understand the impact of what, needs to be done. For. The document delivery.
01:15:49 Speaker 4
Let’s make sure we can clarify a timeline, of when that could be delivered by. Is next Monday. A fair. Window.
01:17:44 Speaker 1
Thirty minutes there for the store.
01:18:14 Speaker 1
Oh. Tour.
01:18:19 Speaker 5
They have another home tour there.
01:18:20 Speaker 2
No, they’re touring someone right now. Oh.
01:21:37 Speaker 1
Um.
01:22:33 Speaker 4
I Can. Paraphrase my email if you want.
01:22:43 Speaker 1
If you want, I can paraphrase my email response.
01:23:20 Speaker 4
Basically, we’ve known this for a while. Super disappointed. Where does the relationship stand? I need all documentation that you have, all email communications, All times that you’ve reached out. So we can basically evaluate the situation if we take it to legal, what our warranty is and how hard we can press this. In the meantime, having a storm drain with two by fours and a metal sheath, For get about the half a million dollar project as a much greater liability, if something happens. Get somebody out there now to figure it out and get national paving companies out there to give us a quote. So we have something to hand over of this is what it’s going to take to repair all the work that you did.
01:24:02 Speaker 2
Uh, quick baseball.
01:24:09 Speaker 1
I was letting them handle it but on the line.
01:24:17 Speaker 1
Asynchronous processes.
01:24:18 Speaker 9
Using the same kind of suggestion, using pipelines to pull data. Those are the options most likely that a solution architect would devise for you to pull data from from the application rent manager, and then possibly if you need to push back from QuickBase as well. It would hopefully be in an event driven thing, rather than a CSV push on a timely event.
01:24:48 Speaker 6
Um, I guess every time though, A at a minimum, somebody will be uh at a minimum, somebody will be triggering that with a fill out of the QuickBase form. Correct Natalie? Mhm.
01:25:08 Speaker 4
All right, so that’s. Sorry I’m coming on late but happy to clarify anything here.
01:25:15 Speaker 6
Yes. Okay. We’re just talking through the move-in, move-out process which the team over there has reviewed. And we’re trying to understand or articulate, I guess, the trigger for them to start the process in QuickBase. And, while the process for on our side starts prior to now, let me know if I get this right : The process on our side starts prior to a form being submitted. It wouldn’t technically enter quick basis uh per two until that form is filled out. Is that correct? That we’re at so far.
01:25:55 Speaker 8
That would be correct for me because just because an application or prospect is approved, doesn’t mean they’re actually moving forward with something. So the trigger would be like them moving in. Whoa.
01:26:13 Speaker 4
Quickbase and Fast Forms would be involved way before that from the initial offer of sale or rental. And that’s going to kick off the process. The application submission is part of a checklist that would be a barrier or a gate for someone to be able to move in and to be able to do that. So if there was an offer, to purchase or rent, it would come in to be approved. There, is your next kind of decision tree or or you know whatever you want to call it node in the. Decision tree: Are they approved? Like that offer, yes no. Great, they are submit an application. That should also have some sort of branch that turns around and and um constructs the questioning for a lease to be filled out and signed. So for someone to be able to move moved into the system, to be handed keys or whatever the case may be, there is a sign approved application. There is a signed lease. There is an offer there is.
01:27:11 Speaker 4
A whole list of checkboxes that have gone through to get to this point that we’re not able to circumvent in the system to move somebody in or whatever the case may be keeps us in compliant. And the system does what it’s supposed to be doing. Um, I guess you know part of looking at it from there, you know, uh, I guess where.
01:27:41 Speaker 4
Where do you see that QuickBase would be involved, not be involved? Am I missing something?
01:27:49 Speaker 6
I mean all those real quick before you guys chime in. All those data points just to reiterate would be very helpful. We don’t want to just have the data being captured once an application is approved. We want to go as far back as possible to be able to understand. These are the ones that potentially expressed interest. These submitted an application. These got an approved application. These actually led to a closing and a moving. Like that ball off from that top of the funnel down would be important to capture. To the extent that all of that is capturable data, which it seems like it should be if it’s running through the form, would just be helpful.
01:28:32 Speaker 10
So I have a question here. As per what we are discussing initially, your customers fill out a form when you are telling that you want to use Fast Fields.
01:28:44 Speaker 4
No, no, no. Initially the manager fills out the form that is submitting an offer, or you know, up to corporate to say, I have a purchase or rental offer that I would like to submit et cetera, et cetera. And then that comes in. That would be based in their Fast Fields app or whatever front end UI. If we continue going down this route or notum and it would basically say, I need to submit an offer. Okay, great. That’s what they do now. Whether, there is branches off of that that we get to in phase six or seven where it gets pushed through, but this is an internal app; there is no customer- facing aspects to it.
01:29:31 Speaker 10
And for approval, once the manager has filled in the form in Tosti’s, does it? They also attach the document of the client, which is used for the verification process.
01:29:47 Speaker 4
So, again, The whole thing is, is that all this information is going to update our system. Where that’s when it comes back out and updates QuickBase, Those checkboxes or filters or whatever the case may be that are needed are going to be filled out. We don’t want to have five document depositories. I mean, if we can collect documents when it comes through through, You know, inspections or checklists or things like that, And they would end up, you know, having a link in the database as well as file storage in our SharePoint. Great, but I don’t that aspect here is not you know is is not used. We would still send it, maybe we haven’t even gotten to the fact if we can create seventy leases and have it decide and run a decision tree if it’s a rental or purchase in which community for which lot and what to fill out.
01:30:39 Speaker 4
But that would be the only customer-facing aspect of it from the start.
01:30:48 Speaker 9
Yeah, and also having hearing you describe like an integrated system totally here. And, we are trying to focus on the move- inm ove- out process and where and when the data actually exists in QuickBase and where we’re pulling the data. So when we started this discussion. You talk about when the rent manager has a specific status when the records are approved in rent manager, that’s when this can kick off the move- in process. But, it does sound like you want to collect more data in ClickBase prior to the move- in process. Yeah,
01:31:30 Speaker 4
Whether it’ll be another process, a different process or something along those lines. That’s a great, Question, I mean, We were talking about one very limited scope here to see if it can do what it’s supposed to do. Um. But I think what the biggest issue that we’re finding or at least that I’m finding now is you’re focusing on something, but you don’t understand the business. So if you don’t understand the business and where it’s coming from, we’re going to end up rebuilding this stuff over and over and over again. And that I have zero tolerance for.
01:32:22 Speaker 4
Guys, My disappointment has been so massive in how this has gone. We have gone out and looked at other competitors. Going out looking at other competitors, the line of questioning to understand things. And really try to make sure that their software or systems can handle what we want to do is night and day. So, I am, it’s starting to concern me on the knowledge factor or anything that you guys are have put together.
01:33:03 Speaker 5
Austin, what are you experiencing from the other vendors?
01:33:10 Speaker 5
Taking things
01:33:12 Speaker 4
Showing us what they can do with it, how it would work. Asking questions like, ‘Oh okay, you want somebody to move in? How do you even get them into your system?’ What is your full life cycle of a resident?
01:33:26 Speaker 5
Are they off-the-shelf companies or are they whiteboards and click-based? Plenty of all.
01:33:38 Speaker 4
We are exhausting this because again, the launch date for this was July seventh or seventeenth. We are now almost in September and we can’t even get to one happening. Wouldn’t it be helpful for us to write a scope and just be all the discovery documents and really take you guys out of discovery and just say, build this?
01:34:11 Speaker 9
I would disagree. We typically do not build in a vacuum. We typically build alongside you, and it’s maybe the process is a bit slower. We don’t typically just turn around an end-to-end, you know, Fully lifecycle application. That’s customized like to the extent of what you are asking for without your heavy. Um, buy in and discussion and discovery up front, Austin. So, we are trying to do exactly what I heard you asking for, you know, discover your end end process here. We’ve conquered this document up. I’ve reviewed your field forms, And we’ve even discussed internally how to interpret this into QuickBase as far as schema.
01:35:06 Speaker 9
And we’re prepared to talk about this process with you today. Is that how we can expect it us to do today?
01:35:15 Speaker 4
That’s great. So are we? I guess it is the system capable. Do we start building something?
01:35:32 Speaker 9
We are in discovery here. We did see the application that was shared with you prior to us meeting with you. We had some meetings with those folks as well. Rika, we do have that simple ERD where we were reviewing together. What we do believe your schema in QuickBase would require, Austin. This is what we’re putting together as far as our thoughts so far on what’s required.
01:35:59 Speaker 9
Well, we’re thinking, you know, where does your process start? You know, Like when do we get a resident in here or a prospect or a buyer? What do you call these folks? Um, put together from your documentation and schema. And, there’s quite a bit of this as you’re embedded with your community community managers, the properties, the regions, your agents. Um uh We imagine that for every. The type of community you have a set of template tasks that’s required for each residency. And when we’re talking move in and move out, it’s pretty defined through that documentation that we’re reviewing what’s required for that. And I think you guys know your business enough to talk if you can determine what templates are or what are required. But one of the things, in Rent Manager and.
01:36:58 Speaker 9
We wouldn’t want you to duplicate your data entry and pull it in multiple places, like you were discussing. If you are pulling in the documents in Round Manager, then you just need to notify QuickBase that those documents have been collected. So, this is as far as we’ve gotten internally thinking ahead, what we would take review that application. I decided so we have a bunch of questions for the meeting about flow, but that’s what we are focused on is the meeting. And move out flow and building that out. So, is that not your expectation? I just want to level expectations.
01:37:34 Speaker 4
That’s fine. Trying to understand where we’re going with it. We can start all the way back at day zero or pick up a certain aspect of the move-in process.
01:37:57 Speaker 9
So that’s what we were hearing today. The application starts off with somebody sitting down in the rental office and starting to fill out an application and beginning the background and financial check. I imagine that’s not a same day process.
01:38:18 Speaker 4
Twenty four to forty eight hours is usually the turnaround time for an application.
01:38:30 Speaker 9
Is that just getting that background financial check application entered and confirmed? How long before that? And you notify the folks for move-in because I assume there’s a lot more steps in between that and the move-in process.
01:38:52 Speaker 4
Yes. So I think you know somebody’s app approved whether they accept it. They sign a lease. They pick a move-in date. They put a deposit down, whatever the case may be. And then there’s like a closing day process. So I think it also depends on the type of move-in. If we were moving in a resident that bought another resident’s home versus somebody that’s buying a home from us versus somebody that’s renting versus an RV resident.
01:39:30 Speaker 9
And that type of sale triggers the different things that are required in order to get to the point where these elements have been checked off, and all these things can move forward so that the person can even trigger the move-in form for them. You don’t send it to the individual; you’re sending a move-in form or like the property? Or what do you call it? The community manager.
01:39:59 Speaker 4
So, if you look at the move in form and the decision flow tree that we sent over from the jot form system, basically the community manager sends the move in form with the required information. It then makes its way to their regional manager or district manager, that next tier up. They will either approve it, deny it, request more information. That will then and don’t remember each, Detail, but let’s just say that that makes it to Natalie. She will approve it once that is done. And everything else is completed with it. It will make it to the corporate office where the system will be updated. As of today, Ideally, this would be something that we could just have an export for and take data entry out of it, But then that’s when the system would be updated and then Quickbase would be refreshed the following morning.
01:40:56 Speaker 9
So again, it does sound like a lot of this work is handled outside of QuickBase.
01:41:04 Speaker 4
Yeah, everybody’s job still needs to be done, But the communication and the workflow and the guardrails on the workflow and the audit of the data in the workflow to make sure that, you know, it’s not a self reporting saying, hey, I took an application. Okay well you took an application. We know that because we actually see the application and that’s been processed and the checkbox is done. Um, so there will still be you know our applications are run through Amren. Uh, you know somebody still has to hand them the keys. You know, we still have to get the signed leases, things like that. So yes, there is still a lot that is outside of Quick Base. Quick Base is kind of you know coming in as the communication and guardrails.
01:41:50 Speaker 4
Around it all, the auditor around it all.
01:41:55 Speaker 9
Okay, And so where we come from is just looking from the perspective of when does that data get to QuickBase, right? Like when when does it get there? You have a lot of metadata. Like I said, like we could start pulling that in in QuickBase. You do have these fast build forms. So right now, you know I see that they’re you know where they’re being sent to. Um we could start, Pushing that to QuickBase, but if it’s not really you know, if we don’t set up QuickBase correctly, it’s just going to be a repository to collect data. Um, I think there is a few things that I saw in your forms that we would have to, you know, adapt a little bit to work with QuickBase. It’s not not really a big deal. Um, But like your your data that you are pulling into the move in move out forms, if you start pulling it from QuickBase like I think you can start to.
01:42:47 Speaker 9
Isolate the records that are available for selection for folks. You know, wouldn’t be every community, every property. So we could start with, like I said, with bringing data into QuickBase your metadata. We could start looking at your FASFO forms and how they communicate, and we can bring that data into QuickBase. We don’t have a connection with Rent Manager to know what we’d be pulling in from there, right? But, if folks are just currently working outside of QuickBase, and they’re working and collecting all this data and everything, then that’s where my curiosity is. Like, Are we just going to piggyback off of the Rent Manager data and pull that into QuickBase? And, are we going to use the Fast Field Data Entry to pull that data into QuickBase? So it sounds like that’s our two options, right now.
01:43:42 Speaker 4
Both of those options are correct. It is a two way flow, so you are going to use rent manager data. Rent manager is our single source of truth. Everything runs through there and has to be updated in there. That is basically the base, the community listing, unit listing, resident information, occupied, not whatever we need to create the checks and balances and the data entry side of everything. We will pull that out of rent manager.
01:44:13 Speaker 4
Create the dynamic drop-down lists, all the other you know field necessary items. The data then would be captured from the field, whether it’s the move-in form or a checklist, whatever it is, Would come back into Quick Base and Quick Base would then provide an output or report or something that then we could put back into Rent Manager. That would be phase one. Phase two of that aspect would hopefully have an API or something to be able to write direct. But, it is taking the information as like the database side from my manager to be able to control the forms, Understand and provide the team what they need to be able to do what they’re doing, Create the checks and balances to make sure that the data is correct and enforce the workflow. And then take the data that it got to get it back into the system. Okay.
01:45:11 Speaker 9
This is heavily dependent on the rent manager connection. Our entire business is dependent on rent manager, okay? So we’re tagging that back in. And regardless of this process, like if you guys are managing this process within, like I said, within FastField, People are doing this data entry, and they’re already why try to reinvent the wheel? We have to understand what data we can collect from FastField to QuickBase. And I guess that’s where I lean in heavily. Uh, to help Britika, right? Uh, but honestly, I mean before until we get some data outputs from our metadata from Rent Manager. I don’t think we should try to build the Quickbase schema out. So that’s that’s kind of my conundrum right now.
01:45:58 Speaker 4
Do we want to give you the data or do you want to request the data? For instance, you’re going to need community listing. You’re going to need the property IDs and the short names as the reference numbers. You can actually reference that in the back end of the system, all the unit numbers, roles, things like that. I can give you a whole bunch of data.
01:46:17 Speaker 9
Do you already have that?
01:46:18 Speaker 4
We have all of it.
01:46:20 Speaker 9
Do you have outputs from the firmware manager in CSV format like that?
01:46:25 Speaker 4
Or do you already have HTML? Whatever you want in any format. We have an SQL database. We have all these files that get downloaded every day to a SharePoint folder.
01:46:36 Speaker 9
Beautiful. Have you played with any kind of API? So then if you’re able to output this data from Rent Manager, is it event driven? Or is it asynchronous and a CSV?
01:46:53 Speaker 4
Right now how we do it is run it through a Power Automate function from a webhook email because it has report batching that sends out reports via email. We have an API that goes to a data warehouse, but that we’re you know again, We don’t want to go the API API route yet until we know that it’s working. But once you know, we kind of get there. You know, look, we were even looking at the API route already ourselves. You can have an MCP from an AI agent go into it. You know, We have a custom A P uh MCP that’s built in to pull out reports from Rent Manager. So right now, they’re sent four AM every morning Power Automate saves them in a SharePoint folder.
01:47:30 Speaker 4
Those reference lists are there. Each unit has its unit ID, each resident has a resident ID, and each prospect has a prospect ID. It gets back and forth throughout the way.
01:47:43 Speaker 9
I am a data guy and smiling. I want to see the data. Austin, I am sure that’s a number of tables. You might have to send it in a zip file like that. Are you able to send that to my team?
01:47:55 Speaker 4
Sure, real quick.
01:47:59 Speaker 6
Are we not getting ahead of ourselves with this type of request? It feels like we haven’t perfected a single process. Why are we trying to look at one type of one aspect of our business for one property? Why are we turning around to zoom back out and look at everything? I just want to understand that.
01:48:26 Speaker 9
Yeah, yeah. I mean, Honestly, I mean, Austin is is uh, you know he’s voicing his concerns, right? We’re not looking at the holistically at the whole business and how this works out, if we were just to focus on the move in move out, you know, Riddika and I may be shooting ourselves in the foot painting ourselves in a corner because we’re not looking at this holistically. We’re thinking about this. Like, okay, you have this form in FastField. You are collecting your move- inm ove- out data. What do we do in Quick Base? What are we collecting? If it were just that myopic, We would just pull the data in a Quick Base, and it would just be a repository for it. There’d be, you know, roles permissions in a Quick Base application. We could build that within a day or within the week. I want to be is not as it is time but.
01:49:14 Speaker 9
That’s not all we’re trying to do here. A lot of this data, like I said, exists already. Your metadata exists and you’re pulling it into FastField already. People are selecting it from dropdowns. What my goal is is that we can tile that data in QuickBase, Like not like pull all your metadata in a QuickBase and then control the list that you’re pushing out to FastField from your QuickBase data. That way, you guys have control over what is shared in a fast field. Then, Your users are using your moving for form and fast field that’s pushing its quick base related to all the data that it needs to be so that you have this full view from the community from a property perspective. You know, its history of residents and applicants and everything that’s going on with it. Otherwise, so.
01:50:11 Speaker 6
You’re viewing the big value add here as. Not building out an interface for us to view our data, which we arguably can do very easily in an extremely customizable fashion, But you are viewing it as housing rehousing that data to then drive our forms, correct?
01:50:35 Speaker 9
I mean i mean if that’s not your goal, I just want to understand what is you know so I mean.
01:50:45 Speaker 6
I just want to make sure that we’re on the same page in terms of like what we’re actually trying to accomplish here. So, that is the purpose of the request, right? So that you can take that data, understand it, comprehend it, And then load it back up with a bunch of if-, then statements into our forms in real time. Correct? That’s like what we’re trying to accomplish here.
01:51:10 Speaker 9
Yeah, I mean we, That if it’s just a matter of pushing data from FastField that you are collecting into QuickBase, you know, um,
01:51:21 Speaker 6
I just don’t see how providing that data is really nothing. Is like yes, there are certainly community dependent things, But getting that information on a macro scale, just this isn’t what I do for a lot. I don’t build out the system so may I am. I am not. I am potentially speaking out of turn here. It doesn’t feel to me like the right place to start, but if that’s what you think is right, and maybe I am misunderstanding the goal of this project, then so be it.
01:51:57 Speaker 4
So, I think maybe one thing to help Zach or maybe everybody is here.: is a move in move out. You have a form manager. Basically opens it up and says, “Yay, I got to move somebody in.” Whatever the case, wherever it starts, whatever ground zero is. But they’re opening up whatever form we come up with for move in move out. They select their community. The next selection is lot or unit. That lot or unit selection should only show lot or units at that community. Let’s take it one step further because it’s a move in form that lot unit selector should only show units that are vacant.
01:52:39 Speaker 4
Meaning, you can’t move somebody by accident into a unit that already has a resident. Both Natalie and Zach, I guarantee you could think of six examples in five seconds where that’s happened. Or the vice versa of moving out—you know, a move out—you can’t move out somebody that doesn’t live there. So the vacant unit should not show up in that dynamic field. Assets and things like that when they’re attached to lots, and we need to be selling a home, it’s attached to the lot. Got it? Yeah, I totally. That’s, where they need to see all of this, because all of this needs to talk in the back end of Quick Base. Quick Base is basically our police, our security everything for our data so no one can make a bad.
01:53:27 Speaker 4
Basically, Data requests or get something, so Justin doesn’t have to ask sixteen different follow up questions. And hopefully one day we can get the API to read and write itself, and it’s a lot more efficient.
01:53:39 Speaker 6
Okay, But my I guess, a follow up question to that would be if we are not capable of showing that we can build out a process for a hypothetical scenario eating in all the data, it feels like we’re trying to run before we can walk.
01:53:58 Speaker 6
But if that’s the recommended path and you feel strongly otherwise, then let’s go. Let’s do it.
01:54:12 Speaker 9
Well, the other options are guys. I mean, if you are really. Visual wants us to start building QuickBase out. We can try to confirm that model and start building proof concept stuff. It’s going to be just basics, but the idea would be solid. That’s where you know whether or not we pull the data from any sources now or later ; any consequential to proof concept.
01:54:45 Speaker 9
So, I just don’t want. It’s not really our style. Our style is to pretty much, you know, Do the ERDs to do this lucid work to do this understanding with you to kind of get a document that understands what we’re agreeing to building. Um, Just want to make sure that you know that is our goal is to create a solution design document that we can agree to building. Um.
01:55:15 Speaker 10
I mean, uh, just to add to Kevin’s point, you know, like how Austin was describing like you have a list of community. Then, you know, in this particular community, you have lots of units, which are like vacant. So, this is the process which we want to understand in order to help you build the flow. I mean the flow, which is shared with us. It talks through your process, but it does not explain the nitty gritty of it, like how now we at least understand that community data is in rent manager. It’s going to come to QuickBooks from rent manager. Then from there, we can also get the lot and unit data. So, that’s what we are trying to actually understand in order to help you how to, you know, move forward.
01:55:53 Speaker 4
I am going to go back, Kevin Lewis, everybody, the whole QuickBase team. Here is the frustration, And I want you to take this to as high up in your company that you possibly can. This was all, Before we even decided to go with you guys, this was all discussed and all talked about and all gone through. This is why it’s like such a just mind blowing conversation that we’re none of it made it over to you guys. This whole sales team, The whole trial period team that was being worked with left you guys out to dry.
01:56:35 Speaker 4
So, you are getting the reactions from us in the way that we are because the fact that you are saying,“ Oh my god, rent manager has this information.“ It’s, no,
01:56:49 Speaker 9
That you are able to pull the information or that you have it already. If you are able to pull it out,
01:56:56 Speaker 4
I guess my point is, is all of this was actually discussed and talked about with them; otherwise, we wouldn’t have moved forward.
01:57:05 Speaker 4
So, taking a step back, I really would like you guys to discuss with whoever you need to that create a form that goes through Quick Base that notifies you guys that the sales team has this information or whatever it is. Kind of the same thing that we’re trying to do, to expedite and make sure that the communication is bulletproof. Because, this what happens when when not. And this why it’s like an email didn’t come through that somebody. Or, they jumped in their car because they had to run out and they didn’t send an email that something was done or something was broken, and then it’s forgotten about and goes away. We try to make it as easy as humanly possible for someone just to click a few buttons, Get the proper notifications out to where it needs to go without having to worry about sending an email. And making sure that the data is correct. Kevin, I’d love to take some time and go through all the data.
01:58:02 Speaker 4
All the exports, anything you can. I am happy to take the time and walk you guys through the system, show you Rent Manager, you know, so you fully understand and are aware of what’s going on. If, maybe then you match up some of where the jot form or other workflows were and have a full understanding. Um, before we try to, you know, We took it one way where we had this really big process. That was maybe twelve stages to now trying to bring it all the way back down to a move- in form. But again, you guys are really flying blind here. You have no idea where any of this stuff is coming from or our ideas are coming from. So, maybe the better step is to start from scratch and go through Rep Manager and say,“ This is what happens. This is what the form looks like. This is what the fields are.“ And, this is what we’re trying to put guardrails around. So we don’t have.
01:58:56 Speaker 9
Yeah, I mean, I would love like I can we can, I could be a resident in applying for this whole process, And you could push me through it and show me what that looks like end to end. I mean, I don’t think that there is any loss of merit for doing that. I think that’s a great way to look at your business holistically. If, you wanted to just do a video of that and send it to me and say, “Watch this,” like I am okay with that, Austin. I mean, I’ve applied to live places.
01:59:29 Speaker 9
I understand. I understand the uh the business model that you have, you know, for manufactured homes and and those communities and such. Um, you know, I was curious if this was, you know, More customer facing or you know as this is clearly defined as a community manager. This isn’t your Fastbuild forms aren’t external facing? They’re to these community managers for inputting the data. Um You know I just I want you to, Have a good taste for QuickBase because I definitely drink the Kool Aid every day. So, How do I get you into a position where you see the value of QuickBase collecting this data? You already have Rent Manager doing the work, you already have Fast Field collecting that data. What what how can I make QuickBase collect this data or show this? Or what can the guardrails do to make this better for you? I am really interested in that.
02:00:25 Speaker 9
Because I can build any application you want to collect this data, and like you said, if the data is in here, we have your communities, we have your properties, and we know that they’re not vacant. Then we send a vacant list to your FAS field form for selections. You know that’s the sort of stuff that I wanted to do for you or that I know I can do for you. Um.
02:00:50 Speaker 9
But that’s just a small piece, you know. That’s just such a small piece. So I want to build something that.
02:00:56 Speaker 4
Small piece and one variable or option in how to get to the end goal. I mean, I think it’s you might have better ideas or best practices on how to actually get to only, you know, vacant lots would show for a move in and vice versa. The biggest at your fast fields.
02:01:19 Speaker 4
You know, was pushing that what we wanted to do had to be done through QuickBase. In a lot of this our taking our workflows, Making sure things can’t move forward around over under through, unless certain things are done. Maybe a very detail, but you know, somebody does an inspection. I am inspecting something. Everything looks good. I am checking off good, but if anybody says needs repair or replace or something like that, it’s going to then trigger to say I need a photo, I need this, I need that. Um, those are the the rule engagement, the workflow, The guardrails that we’re trying to put in place because rent manager doesn’t have it. There is no way to.
02:02:14 Speaker 4
You know, Verify something or or have approval on something before it gets put into the system. That’s why we defaulted to forms. That way there is also a paper trail and a, you know, historical log of who approved when when it was submitted. That we can see those things. That’s going to help us become better operators more efficient in what we do. So it’s kind of looking at it that way if that’s helpful. And that’s where we think, or where we were guided to, That QuickBase and the combination of QuickBase and FastFields can really help you know, set us apart there.
02:02:55 Speaker 9
So, The same folks who are digging through Rent Manager to make sure the data is there, checking on forms, checking on stuff they’re submitting things to their. Are they the same folks that are going to be in in QuickBase, or is that really going to be, you know, your folks? It’s, not the community managers who are going to be looking at the data in QuickBase. That’s going to be your folks, correct?
02:03:17 Speaker 4
Correct. So I kind of the way that we’ve structured it from the original conversation and and the user base, the user base is very heavy on the fast field side. It’s very heavy on the data entryum you know, the forms, The The I guess things to make, The whole process run and get it out there for the team in the easiest way possible. Back end, The smaller user base and the quick base side is really for your corporate where data entry is going into, the analytics are being done. You know, Somebody submits a a form. Or let’s just say anything they’re part of the process and they fill it out.
02:03:58 Speaker 4
And, this one person is taking three days to approve or take it to the next step. Somebody from the corporate level is going into QuickBase and understanding that and using the QuickBase dashboards and the data and the AI to say, “Hey, You have an inefficiency in this region because this person might be overwhelmed or whatever the case may be.” We’re going to say that everything’s positive; there’s no one’s malicious, but you know they it takes them three days to approve move outs. But maybe that’s because they have too many things on their plate. Maybe look at taking it off, but that we can see those funnels, that we can see the things that are going through on the back end, you know, through Quick Base. And that is because everything is very specific: dropdown lists, checkboxes. Everything could be analyzed and seen from timestamps: where is it? What does it look like? You know I can go crazy with hopes and dreams. You take.
02:04:57 Speaker 4
A community inspection picture or video or something like that. Use fast fields, you dispatch a task out to the maintenance or community manager and say, hey, on this part of the property there was overgrowth. Can you go take pictures of that? Make sure that it was cleaned up. They go and they take pictures. And now we can look at them either manually side by side AI. Some technology wherever the world ends up going and says, yes, that was actually done.
02:05:28 Speaker 4
Maybe it’s something where we don’t even have to dispatch the task out, But they’re so proud to get that work done that they go and they update their task or or something through all of this. And they say, “Great, I did it. I trimmed the overgrowth. Here is my picture,” and send it in. And you know now the regional manager knows, director of operations, owners, accounting whatever the case may be everybody knows it is done. Bills can be paid. You know, task items could be closed. Liability issues can be closed. You know, All these things that if that one manager maintenance took a picture and text messaged it, It gets lost in translation or won’t end up to where it needs to get to for two three weeks later or five follow up questions. Okay.
02:06:27 Speaker 9
Austin, you’re a bit of firehose for me. Little bit good.
02:06:32 Speaker 4
Welcome to the game. That’s what she says. It’s like drinking from a firehose here.
02:06:39 Speaker 5
Hey Austin, I have a quick question for you and for the Parakeet team. I am in the background; I’ve been pretty quiet on this call, just absorbing all the information that you guys are giving us, and I got to admit. Sad, Sad to hear about the sales process and the gap of information that that made it to us. I am in currently in the background chasing the account team right now. Any chance, any chance you guys did a demo for the account team with Net Manager?
02:07:20 Speaker 4
If I say yes, I also want to give you the backup of the meeting with it and everything like that. Oh no, it’s okay. But we we don’t have to give you the data came from. Did I show the actual rep manager? I don’t, I can’t. I am going to say no for their benefit. Okay, I think it was more of was this going to be an API? It was more here are the CSV files that we would have exported and imported.
02:07:45 Speaker 5
Yeah okay.
02:07:46 Speaker 4
Okay no worries actually platform or something like that.
02:07:50 Speaker 5
Oh, that’s that’s good to know. No, thank you all so much.
02:07:54 Speaker 4
We also knew there was no integration chance, nothing in the near term, whether even in the long term. So that was our first kind of this would work, this would be great. We can get this to work how we do it is we have an output from QuickBase in. However, many files we need to be able to import into the system. And then an, you know, a way to have those same types of. Fi les come from rent manager through this power automate or whatever the case may be to be saved into SharePoint that QuickBase can read every morning.
02:08:27 Speaker 5
Oh, okay, okay. No, no, This is good to hear because yeah I am chasing Andrew right now in the background. It would be very valuable for you to walk us from step one to step one hundred, right much like what you and Kevin were talking about earlier. Um, when I typically work with customers, um, I like to see the whole data set. And, if a customer wants to itemize like a certain certain columns, if you will, or certain fields, uh, maybe uh, create a workflow based on that subset, right? Um but I’m certainly not going to derail derail the team here. Um I’d like to be on the next call as well. Kevin Rettica um just to go through.
02:09:18 Speaker 5
Go through the next test, or Austin. If you do send us a recording, Kevin, I’d like to be able to review it as well, just to get eyes on it. Mostly. But I think for the for this call on my end, I am just chasing in the background Austin, just to ensure that we do have all the information because we did meet yesterday with the team. But you’ve certainly identified a gap and I appreciate it.
02:09:47 Speaker 4
Thank you. I am even thinking one step further, hearing from both of you, it might be beneficial if we kind of create a guest, Maybe read only account and let you guys just dig around in Rep Manager and see what it is. See what reports come out, what they look like. Again, They have an API that we use that goes to a SQL database, but and there is a whole documentation because there is things that we pull out. You know, Zach uses the data warehouse as well, And we’ll have reports that have certain fields that can be pulled from the API. But if you tried pulling them or scripting them from Rent Manager and its interface, you can’t get them. It’s like you know the weird nuances that are out there. So if t here is something that we needed, you know maybe that’s an avenue to look at. But just kind of letting you guys kind of jump in, see how it goes, see what they have.
02:10:45 Speaker 4
It’s uh, it’s pretty customizable. It’s pretty nimble. It’s just more, I would say, and then this truly isn’t endearing in a nice way to say it. It’s kind of like QuickBase. It looks extremely archaic, Yet its functionality is so powerful. You can’t even see underneath this underneath the first layer of it.
02:11:12 Speaker 5
Okay, Now you make me want to just take off my manager hat and go jump in on the tech side and start digging into it as well. Like, come on, Andrew. Can you get perks from Rent Manager?
02:11:26 Speaker 4
Just Been fully connected and living it and everything for decades of my life, and I am stuck.
02:11:37 Speaker 10
Kevin, what I think. I mean, do you think we can schedule the next. For Thursday, where Austin can give us a walkthrough of Front Manager and how the data flows, would that be a good option? I mean, that’s what I’m thinking. It would help us at least.
02:11:52 Speaker 9
I’ve got the time for you, if if that’s if that’s the best way, often you want to do it. If you’d prefer to have a recording so you could say,“ No, I recorded it once so I’m not doing it again,“ kind of thing.
02:12:05 Speaker 4
That’s not something we don’t we don’t work like that. I’ll walk you through it. Eight million times, as long as it’s not the same question twice, that’s where I lose my patience. But with that so I am actually on the road this week. I am just trying to think T hurs day ;. It’s kind of a little bit up in the air on just where we’re going to be and things like that. So, I don’t want to have to cancel on anybody. Maybe like a Monday.
02:12:38 Speaker 4
Kick off, And I can get you a lot of this data over and share some of it just to start digging in. And maybe a sample just so we’re not slowing down or pausing. I am also happy if I can’t jump on, you know, Natalie, you know the system; Zach, You know the system to kind of bounce around and give just a quick overview. So.
02:13:05 Speaker 10
How about Tuesday at the same time? Next week, sure.
02:13:14 Speaker 1
Okay, okay.
02:13:17 Speaker 9
Yeah, feel free to send over whatever you feel is pertinent and you have available. Austin, don’t go on a goose chase. But I appreciate all the like I said, I am a data person. So, if you send me data like I probably can’t help myself and Rudica and I will build something around it. Soum. You’ll have.
02:13:36 Speaker 4
What we started doing when we started doing the trial and all the feeds that we started putting in. I mean, I think that might be helpful to to see what we were pulling, you know. From the fact of you know, you might only need two columns for this this set data set, But it needs the link, so you need the, you know IDs and all your reference IDs things like that.
02:13:57 Speaker 9
Okay i’d appreciate I’d appreciate that and I think, Like I said, I can make heads and tails of that and come to the table with more questions. Okay, so I appreciate your time today. Uh, I know discovery can be pretty tense, man. I am going to ask a lot of dumb questions. Uh, I am not in the real estate business, So I assume that there is some terms taxonomy ; I am just going to get wrong. Um i require you to be certain to let me know So, no no you are good. So i appreciate y’all um.
02:14:31 Speaker 9
Uh, I’m looking forward to whatever you sent our way. You all have an exceptional day and I look forward to talking to you next time, okay?
02:14:37 Speaker 4
You guys as well. Thank you very much.
02:14:39 Speaker 9
Thank you. All right, take care.
02:14:41 Speaker 1
Bye- bye. All right, so we’re here.
02:15:22 Speaker 1
Um. One really like. Back area. By the uh. Cell phone tower.
02:15:51 Speaker 1
Where we can.
02:15:51 Speaker 4
See that act doesn’t. Is that them driving around? Let’s see if we can find them. I guess. Yeah, we can see if we can find them. Dog machine, dog machine, dog machine.
02:16:21 Speaker 2
John, this is fantastic. It’s.
02:16:26 Speaker 4
All about. You should say you’re welcome for doing your job here. Yes, ready?
02:16:50 Speaker 2
I won’t sit. It’s.
02:16:54 Speaker 4
Not the six inch legs that are the issue. Trunks up. My problem is it’s going to be anything. Will you hand me that bag, my bag up there?
02:17:18 Speaker 4
You were probably half asleep, half listening. I set that up for that entire document. Like, ready? Fucking go!
02:18:49 Speaker 1
I just.
02:18:54 Speaker 6
Had to. It’s where he’s like, there’s no way I’m fitting on this thing.
02:18:57 Speaker 4
Damn, you still get off of there. Nothing like the metal slides we grew up With.
02:19:16 Speaker 3
Looks a lot better than it did at first.
02:19:18 Speaker 2
Yeah. Yeah, I saw the the Parkwood one is a little balancing.
02:19:25 Speaker 1
Are they branded? We’re good. Yeah, we’re really good so yeah. Oh nice.
02:19:35 Speaker 3
She’s put in an application too?
02:19:37 Speaker 4
Oh great. Great How how often you do that?
02:19:43 Speaker 6
Is it usually every time they throw it?
02:19:47 Speaker 6
A lot of people are, yeah. Most of them are putting applications in, But like I’ll get an email the next day that says so and so is uh submitted an application. But hasn’t or they filed an application, but they haven’t submitted it. You know, they haven’t saved it yet. Yeah. But uh, but we are like whenever we get those emails, We’ll reach out to that person and try to see, if like, hey, is there something wrong?
02:20:11 Speaker 4
Is there something that we can help with? You know something that why have you been asking for a lot of times? I’m, just trying to think about how to like about it is they’re worried about something that they’re not, they don’t want to say this. We don’t want to take your application money. Yeah. We don’t make money on it, goes straight to the third party company. That’s not what we’re trying to do. Right? Is there something that you like? Yeah. If there is, tell me, Let me I won’t even bring up your name, but let me find out if that’s going to have an issue or if there’s a way we can work around it before you spend the money. How much is the fine? Right because that’ll end their hesitation.
02:20:48 Speaker 4
Oh well, I have a. Then all of a sudden, yeah. And it was like, I’ve never been passed. Thank you very much for you know, sorry. I was arrested for X, Y and Z when I was a kid and turn my okay, great. Yeah yeah, everybody’s here to second. That’s not yet. So that help might help a little bit mhm cause I think that yeah or if there’s a document that they need cause it’s usually like.
02:21:18 Speaker 4
Social security card, license. You have to pay stuff today. Get your application in and approved. Yeah. If you don’t think there’s any other issues, get your application in, pay for it so we can get it approved. Right. Then we can at least hold on to it. Yeah, Or, at least we keep the process going, and then we can figure out the rest. Yeah, That just try to help get them. That’s the whole thing is like you can’t run without it, but then I know that’s usually what it is. They have a concern about something on it. Yeah. They don’t have a document and then. What do we do with the storm drain?
02:23:05 Speaker 1
Oh, you did?
02:23:43 Speaker 1
Thank you.
02:24:19 Speaker 2
The Panthers. Oh, we’re gonna make it home. Wrap.
02:24:34 Speaker 4
It all the way around to the mailbox.
02:24:49 Speaker 2
As well, yeah. At least some wrap it. I don’t know if you want to wrap it the whole way.
02:24:54 Speaker 3
I will say the only complaint I get about the fencing is that since the park or the playground is so close to the main road, and kids can just kind of cut through this pathway, yeah, everything across street. Uh, Sorry.
02:25:21 Speaker 3
That’sum. Yeah, that’s the only thing I can about. Yeah, I mean if my kids were playing there.
02:25:32 Speaker 5
Yeah, yeah. Um.
02:25:42 Speaker 4
So Brutal is it ours?
02:26:45 Speaker 2
We should rip it to Greenville.
02:26:48 Speaker 4
Get out of their hair.
02:26:49 Speaker 2
Yeah. Thank you. Thank you guys, thanks for taking the time. We got a note, we got we got notes and stuff so we’ll.
02:27:01 Speaker 3
Any feedback for us? Anything we need to work on? No, no violations. No,
02:27:08 Speaker 2
I mean the part they can hide,
02:27:09 Speaker 4
And we just took over my burger. It’s gonna. Yeah. I wouldn’t I wouldn’t get there. I’m just talking to you about the applications. That just. I talk to them most of the time. It’s something so stupid that they think is going to show up, and that’s what’s holding them back. They don’t want to pay the fifty dollars, which I get. And but I would say it doesn’t go to us; it’s a third party. We don’t want to take your money. Talk to us, tell us what it is, Let us find out to make sure because we want you to lose it either. And most of the time, it’s something so ridiculous that you’re like.
02:27:43 Speaker 4
Fill it out, or if they’re missing like their social security card, okay, great. Pay for the application so we can hold the home for you. Get you in there. And then we can basically have it pending to get your social security card or a copy of it. Or.
02:27:56 Speaker 3
If there is something we could do a higher security deposit.
02:27:59 Speaker 4
Right, maybe they had, you know, there’s a few things we won’t do because it’s family friendly kind of thing. But other than that. We could probably figure it out or it probably wouldn’t even show up but.
02:28:19 Speaker 2
You’ve seen occupants and pick up a bunch, which is great. So, you guys have did a great job pivoting off that and continuing to push even selling those back up and selling those homes like it’s great. But.
02:28:37 Speaker 4
Everybody’s doing a good job, yeah. She chose so Mike,
02:28:41 Speaker 3
All right? Yes,
02:28:44 Speaker 7
Go get lunch. Take a deep breath.
02:29:09 Speaker 1
Thank You so much, and if you think of anything, please let us know.
02:29:25 Speaker 1
Something. Yeah. Celsius and some food.
02:29:33 Speaker 4
John’s all about the the gas station eggs and jerky for. Eggs.
02:29:48 Speaker 2
And Jerky bites I buy but it’s kind of, For breakfast oh it was it was no.
02:30:12 Speaker 2
No Let’s get like a five guys or something. We could get C hick- fil- A I mean, we need we don’t unless we want to get Savannah at like eleven. I’m already thinking we should skip Auburn. We can talk, we can call him out of the way. Um. So.
02:30:30 Speaker 4
That sounds like a plan. No, no Auburn. I’ll fly to Auburn another day.
02:30:35 Speaker 2
But. I do feel bad actually About which part?
02:30:49 Speaker 2
Then we have somebody new there, and he like did the sign twice, but it’s really good.
02:30:53 Speaker 4
Oh yeah, but is he new? I don’t know.
02:31:06 Speaker 2
Ah! He’s gotta be something in the way. I’d fuck with Chick Fil A. Yeah. Easy. See if it’s on the route though.
02:32:56 Speaker 1
How do you want me to respond to that?
02:33:00 Speaker 4
Can I have a cloud account so it can import into SharePoint? Cloud doesn’t import into SharePoint. Yeah.
02:34:16 Speaker 5
That’s Fine.
02:34:54 Speaker 1
I don’t know what to do.
02:35:37 Speaker 4
Well, It’s his attorney that hasn’t got back to.
02:37:36 Speaker 1
No.
02:40:51 Speaker 1
Oh.
