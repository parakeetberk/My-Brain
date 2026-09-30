# 2026-08-24 — MAV and Parakeet

**Who was there:** The MAV representative leading the call, plus Ozzy, John and Austin, who are addressed by name. Speakers are not individually mapped to the diarization.
**Filed:** 2026-08-30, by Claude.
**Source:** [[70-Operations/meetings/2026-08-southeast-tour/MAV & Parakeet-Summary]], [[70-Operations/meetings/2026-08-southeast-tour/MAV & Parakeet-transcript.docx]]
**Attachments:** [[70-Operations/meetings/2026-08-southeast-tour/MAV & Parakeet-Discussion Summary]]
**Flagged:** The unresolved edge case: two people with the same name but different contact details, such as roommates, would be merged under the oldest-value rule. Flagged on the call, not solved.
**Flagged:** Claude audit log visibility was described as limited, which is a governance gap if agents can delete or overwrite records. No mitigation plan or timeline was set.
**Flagged:** Which system is the single source of truth for prospecting and lead data — Mav or Rent Manager — was agreed as necessary but not chosen.

## Summary
A CRM vendor call covering three things. First, the duplicate and merge workflow goes live on the Parakeet account on 2026-08-25: if Google Ads is the ad source that value is retained, otherwise the oldest lead source wins, and it applies only to new prospects created after launch, not to the existing duplicates. A written rules and testing document goes over before launch, with a walkthrough call on 2026-08-26. Second, a trial MCP sandbox is due by Friday 2026-08-29, covering Prospects, Tenants, Units, Properties and Tours/Meetings, loaded with Parakeet real CRM data but deliberately not connected to the live Rent Manager account, with roughly 900 tools available; the Friday 3:00 PM EST call will connect it to the team Claude account and run initial test prompts. Historical timelines will not come across in the first export. Third, reporting: today someone manually pulls backups and pushes them to the cloud, which is slow and sometimes wrong, and the preferred design is Rent Viewer syncing daily into the data warehouse, likely Microsoft SQL, with an introduction to the Rent Viewer team after Friday. Governance got real attention — token and API cost, thin audit logs, and the risk of round-tripping data between MCP, the warehouse and the CRM without a routing plan — and everyone agreed to a wider call with internal teams and Rent Viewer before the integration design is fixed.

## Decisions
- Launch the duplicate and merge workflow on the Parakeet account on 2026-08-25, for new prospects only: Google Ads source is retained, otherwise the oldest lead source is used.
- Send the written rules and testing document before launch, and walk it through together on 2026-08-26.
- Build the MCP sandbox on Parakeet real CRM data — Prospects, Tenants, Units, Properties, Tours/Meetings — but keep it disconnected from the live Rent Manager account.
- Prioritize Meetings and Tours second or third in the migration order, after converted prospects.
- Use Rent Viewer to sync data daily into the data warehouse instead of manual backup pulls, and centralize reporting there.
- Engage the Rent Viewer team before building anything, to avoid duplicate flows between Mav, Rent Manager, the warehouse and the CRM.
- Everything should be reachable through Claude via the data warehouse, so field and corporate users get information in digestible form through agents.
- Assess cost, governance and workflow capability before any full deployment: token and API consumption, data privileges and audit logs, and which agents and scheduled functions push or pull CRM data.

## Actions
- [ ] MAV — send the duplicate and merge testing document — 2026-08-25.
- [ ] MAV and Parakeet — review the testing document and the workflow rules together — 2026-08-26.
- [ ] MAV — complete the MCP sandbox setup (Prospects, Tenants, Units, Properties, Tours/Meetings) — 2026-08-29.
- [ ] MAV — send details on the 900-plus MCP tools and example use cases before the Friday call.
- [ ] Team — MCP review call: connect the sandbox to the Claude account and run test prompts — 2026-08-29 at 3:00 PM EST.
- [ ] Austin — connect MAV with Saad and Dan on the Rent Viewer team — after 2026-08-29.
- [ ] Unassigned — schedule the broader call with internal teams and the Rent Viewer team on the data warehouse integration.

## Pages updated
- [[10-Business/departments/sales-and-marketing]] — duplicate and merge rules and launch date, the MCP sandbox scope and Friday test, replacing manual data pulls with a daily Rent Viewer sync, and the unresolved source-of-truth question for lead data.
- [[10-Business/departments/asset-management]] — the data warehouse as the reporting centre, the Claude access layer over it, and the governance items — cost, audit logs, and data routing between systems.

## Full transcript
MAV & Parakeet
2026-08-24 15:05:09
00:00:01 Speaker 1
Previous value, and then unless it says Google ad as the ad source, it’s gonna take the oldest lead source. That’s what the merge and duplication will do. I can send all that data to you, so we can launch that tomorrow. On Thursday, we can get on a call. If there’s anything that you want to review, we can review it.
00:00:23 Speaker 2
Do you have a text file or some type of workflow that I can understand before launching it? If I could say, these are the rules we put in place. For example, if name and number are the same, because there are certain situations where they don’t have the same phone number or even the same email, but the names would be different. So I could tell they’re two different people possibly applying for the same home, like as a roommate or another person living there. So let’s totally get on a call to discuss those.
00:00:57 Speaker 2
I think tomorrow is good for it.
00:01:00 Speaker 1
In that scenario, it would take the oldest value. So we can discuss that. I have a testing document already created. I can share that with you, and then you can go through it tomorrow once it’s launched. You can see if all those checks are there.
00:01:16 Speaker 2
And will it do existing duplicates or only new ones moving forward?
00:01:22 Speaker 1
It will only do new ones moving forward. Whenever a new prospect is created in the account.
00:01:28 Speaker 2
Got it. Understood. Thank you so much.
00:01:30 Speaker 1
Absolutely. And then in terms of the MCP Aussie, I know we talked about that. I am looking to create a trial account within MCP connectionum by Friday. So I could probably have an account by Friday. You’ll be able to sync it with your cloud account and start testing out all those different tools. There’s about nine hundred tools available inside Zoho. The capabilities include workflows, updating fields, removing fields, cleaning data and even reporting. You’ll be able to sync it with your account. So we would need to get on a call just to set that up for you. But by Friday, we should have the MCP server launched and ready to go. That’s kind of the timeline that we have.
00:02:21 Speaker 2
And that would be for a sandbox version of a copy of what we currently have.
00:02:27 Speaker 1
What I am going to do is take prospects, tenants, units, and properties. If we have time, I will also take the tours or meetings module. Then I will copy all of the data and import all the records and data that we currently have into that sandbox account so that it’s using parakeet’s data. Then you can start to connect that with the cloud. It won’t be tied to your existing right manager CRM account, but it would be tied to a sandbox environment with your data.
00:03:03 Speaker 2
Just bump the priority for the meetings to almost second or third. It should be converted prospects meetings and tours, then properties, and thereafter.
00:03:17 Speaker 1
I will try to get meetings into that; it shouldn’t be too much of a task to migrate that data. There aren’t that many fields there, so we can go ahead and do that.
00:03:26 Speaker 2
Relative. Right.
00:03:27 Speaker 1
Yeah, yeah. Um.
00:03:40 Speaker 1
Sorry, Ozzy didn’t quite hear you there.
00:03:42 Speaker 2
John, we’re having a hard time hearing you. Could you try that again?
00:03:49 Speaker 3
Based on all the data that you’ve been uploading for me in terms of testing out the dashboards that we’re creating, is all of that data going to be running through the MCP? Or is anything going to be missing? Or do you actually get more? We’ll get more.
00:04:12 Speaker 2
Good.
00:04:13 Speaker 1
Aussie, if I may. It’s basically whatever is in the prospects, tenants, units, properties and tours modules in the CRM. That’s what we’re going to be migrating.
00:04:26 Speaker 3
Is there any um? Is that so? That’s like everything.
00:04:31 Speaker 1
From the again it’s not going to have timings. For example, if you wanted to pull up a report for prospects converted in the month of May, we won’t be able to do that because we’re just taking that data export and putting it into a sandbox. That capability isn’t there. But once we migrate the entire account into that version, you’ll be able to have the timeline and create reporting based off the timeline.
00:05:04 Speaker 3
But now I’m just going to have. We won’t have the past timelines. But going forward we’ll be able to say, ‘All right, Joe. Flow was a new prospect on this date. It was touched on this day. It moved into his application on it. We’ll be able to have the complete flow down the funnel by time. On new ones that start flowing through it, it just isn’t going to retroactively pull that up.’
00:05:33 Speaker 1
It’s not going to do it for this when we launch it on Friday. This is kind of just a sandbox to show you how it syncs with your cloud account. And then again, there’s about nine hundred tools available that you’ll be able to see. What are the actual privileges? That’s a big one, right? We talked about data privileges with rent manager. This is going to be a very similar route. What are the privileges available? What are the functionalities in terms of what we can update, create, delete workflows? Once that’s all tested out, we can launch and create a plan in order to get all the previous data and migration, all the timelines, all the existing.
00:06:13 Speaker 1
Information into that account as well, and then we could launch the full MCP. So this is just a preview of the capabilities. Perfect. And then in terms of I know, I did want to talk a little bit about Rent Viewer. I did see that Parakeet was using Rent Viewer. I am not sure if that’s still the case. Are you guys looking to have reporting done via Rent Viewer or kind of what’s the reporting process right now? Because I know Aussie is pulling data backups currently and that’s kind of a manual effort. Sometimes the accuracy can be off there. So if there’s a way that we can solve that problem, let us know and we can discuss a few integration capabilities.
00:06:59 Speaker 4
We could have it pulled into our data warehouse with all the data.
00:07:06 Speaker 4
Am I on mute? Sorry I was on mute. We could use Rent Viewer to pull the data or sync the data daily and have it integrated into our data warehouse. That would be helpful. And obviously, so Ozzy doesn’t have to pull data and we can connect it to everything else that we report off of.
00:07:33 Speaker 1
And Austin just wanted to understand more. The best and ideal version of reporting is Claude using Claude.
00:07:45 Speaker 4
All of our stuff comes, if you’re basically everything comes from Rent, Manager and other sources into our data warehouse over there. Timing on refreshes and things like that vary depending on the reports that we’re pulling. That’s kind of the Depository for a lot of our historical data and things like that.
00:08:12 Speaker 1
Got it. And it sounds like RentViewer has a real time sync directly with Rent Manager? Correct. And is that a data warehouse? Do you happen to know where that is stored? Is that in Snowflake or is that their own proprietary Microsoft SQL?
00:08:32 Speaker 1
Microsoft S so.
00:08:34 Speaker 4
I believe I would put you in contact with Saad and Dan over there just to make sure.
00:08:40 Speaker 1
I was curious because on their website, it did show that it pulls information and has a CRM integration. It could be where we just have to build that integration out. And now all of that is stored into the database there. It’s a capability to centralize the reporting. I know right now Ozzy did mention that he was pulling in data backups and pushing that into the cloud. So if there’s a way to put that all into one warehouse, we can discuss an integration there similar to what we’re doing with MH Village. Perfect. And then in terms of Rent Viewer, Austin, would you be able to share the advantages there of having the integration? I guess maybe we would need to connect with the Rent Viewer team.
00:09:34 Speaker 1
Because there could be some duplications of the data, it could cause some issues, especially with our integration with Rent Manager. If that is something that you guys are interested in, I would definitely like to get in touch with the Rent Viewer team or your dedicated partner there. So that we can understand what the integration would look like and make sure that there’s no gaps in terms of the workflows themselves.
00:10:00 Speaker 4
I would say that’s above my pay grade, so to speak, or knowledge on all of it. And Happy to get on a call with them to make sure that we’re in the nothing overwrites, nothing messes anything up.
00:10:16 Speaker 1
And I know you guys are using cloud, maybe building out some agents and some workflows there. I am curious to know if that is part of the roadmap. Specifically with the CRM and the MCP connection and reporting side, how does that play into everything? I’m not sure if you’re able to pull data directly from the data warehouse to Claude or what those AI capabilities are. So I was curious about that as well.
00:10:52 Speaker 4
We can pull data directly and it speaks directly to the data warehouse. I would say John and I both would like to have everything connected in some way, shape or form through Claude or whatever interface we would use for the multiple models or just sitting with Claude’s LLM. Having things run through the data warehouse to be able to provide easy access to everybody through these agents to get that information in digestible forms.
00:11:30 Speaker 3
Got it. And I would say too, I think we need to figure out data warehouse versus MCP, versus pulling it in from the like. I want to make sure we need to be a little thoughtful and think through and make sure we’re not round tripping data, multiple places. Because obviously we want to be efficient with the data too, so we’re kind of learning as we go as well. And I think we’ll find out the best way to route everything to the end dashboard products. I don’t know if we know that yet.
00:12:16 Speaker 4
A knee-jerk reaction or an uneducated comment would be to not pull both Mav and Rent Manager, and have them conflict from the prospecting and lead generation information. We would either choose one or the other as far as what the source of truth is. The data warehouse would allow us to link the information that is in Rent Manager, that might be synced over with Mav, as well as what’s being entered on that side, and then being able to attach.
00:12:52 Speaker 4
The additional information that doesn’t get brought over from Mav into Rent Manager, whether it’s the data that you guys still have in your system that doesn’t come over to be used as additional reports or views out of the data warehouse. So we can access it all from one point rather than having to get that from Mav, this from Rent Manager, and this from the data warehouse.
00:13:14 Speaker 1
So what I would say is there are a few points I would discuss here and just to give you a rundown on the capabilities. The first thing I’d like to mention is governance. You want to make sure that, whether that be through Red Manager’s data privileges, what does it have access to? When you know we’ve already shared with you our data privilege sheet. Things cannot be deleted. Here’s what we have access to in terms of Red. Manager has over two hundred and fifty API endpoints.
00:13:49 Speaker 1
What are we actually pulling data and pushing data? And what would you like it to be? What separates the MCP capabilities in Mav versus the status quo in Red Manager? Now you can probably build a lot of agents inside of Claude, push that into Mav to perform some actions. Now that can also get pushed into Red Manager. So now you can have a little bit more of an agent taking over some more tasks and scheduled workflows through Mav’s MCP. So that automation capability would be there. In terms of the cost and governance, you mentioned some duplication efforts that could happen when data is being pushed from Mav to Rent Manager. And then from Rent Manager to Rent Viewer’s data warehouse. And then how does the CRM connect to the data warehouse?
00:14:45 Speaker 1
That’s something that will take a little bit of time to scope out and understand, so there’s no duplications there from a reporting standpoint. But it’s not going to affect the actual end data inside a rep manager because those are going to be two separate integrations. It’s just what gets stored in the data warehouse, so there’s no duplications. So those are some of the things and variables that we’ll have to scope out and understand. But from the capability standpoint, those are the three things I would mention. One is going to be how will this affect your cost? Tokens being used, what APIs and for example, we have a bunch of agents that are running on our Zoho system. We have a bunch of lead generations and different workflows being created. It exhausts a lot of API. So that’s one thing that I would like to mention. Second thing is governance, making sure you understand exactly what the capabilities are. Because with cloud, something can go wrong, where if it deletes a bunch of records you want to be able to.
00:15:42 Speaker 1
Have pretty good visibility and audit logs on that. Right now, those audit logs are a little bit not as defined with cloud itself. The third thing is what are the workflow capabilities? Being able to identify here are the workflows we can generate or the agents or scheduled functions we can have that can push data into the CRM. Those are the three things I would assess, and we can scope that out as we continue. First, view what the MCP is, and then how we would migrate all of the data when the sandbox has been created.
00:16:24 Speaker 4
My reaction would be great love that we’re looking at that. And the flags are raised. Probably a better conversation to have with both teams on the call. Just so you know, it doesn’t get lost in translation and also talking above. My knowledge base, so but definitely can ask about everything that you said.
00:16:51 Speaker 1
So I would agree. Definitely, I think being in touch with the viewer team would be required, especially because we don’t understand how the integration would work from the CRM to the data warehouse. Any other questions on that? Hopefully by Friday, we can go ahead and get the MCP configured on that sandbox account. I will send over some more details. You guys will be able to see the nine hundred plus tools that are available and how that is being curated. I can share some examples. The goal will be at the end of the call on Friday to connect it to your cloud account and have some tests run.
00:17:40 Speaker 1
So you have a few prompts that you can throw into Claude. You can generate some information, request or pull data from the CRM in a reporting standpoint, maybe create a dashboard. Then from there, we can discuss the other use cases and more so the data privileges.
00:18:05 Speaker 2
Sounds good. You guys available on Friday? Where do you work.
00:18:14 Speaker 1
My schedule is pretty wide open anytime after one p.m. Eastern Aussie. I think we’re good to go.
00:18:24 Speaker 2
Got it, send around an invite for one p.m. Friday.
00:18:30 Speaker 1
And then in terms of the duplication workflows, tomorrow might be a little bit difficult, but we can connect on Wednesday and go through those tests together. If you flagged anything, let me know. I’m going to send you the testing document, and we should launch it tomorrow as well. It will be live on Parakeet’s account starting tomorrow.
00:18:58 Speaker 2
Awesome. I’m looking forward to that. That’ll be great.
00:19:01 Speaker 1
And then I think John mentioned twelve. Let me just check my schedule here and make sure I can.
00:19:10 Speaker 1
Or he mentioned three p m Friday.
00:19:13 Speaker 3
That’s EST. We could do four or EST too.
00:19:16 Speaker 1
Both of those work. Three p.m. EST is perfect. Alright, well I will send over some more information. And if you do have any questions, just let me know. And then Austin, if we can get in touch with the rent viewer team after Friday. Once we’ve seen the MCP and the capabilities, that would probably be a good next step there, just to make sure that we can sync it to the data warehouse. Great.
00:19:50 Speaker 1
Thank you everyone. That’s pretty much it. Thanks.
00:19:55 Speaker 3
Thank you so much for your time.
00:19:56 Speaker 1
Today Take care Bye- bye All right
00:19:58 Speaker 2
Take care.
