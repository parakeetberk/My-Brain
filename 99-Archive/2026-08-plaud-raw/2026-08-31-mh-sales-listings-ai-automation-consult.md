# 2026-08-31, Consultation on MH sales operations, listings data and AI automation

**Status:** RAW. Pulled from Plaud into the Inbox, not yet filed. `90-Skills/transcript-filing.md` has not been run against it, so nothing here has reached a page, the numbers ledger, the decisions log or any register.

**Source:** Plaud recording `16db0fb3adb2bc134f01689b578afb46`. Plaud's own title: "08-31 Consultation: Mobile Home Sales Operations and AI Automation". Device serial `8811B30274091547`.

**Recorded:** 2026-08-31, 09:03:21 to 10:13:31 ET. 70 min 10 sec, 210 utterances. The longest of the five recordings today by a wide margin.

**Pulled:** 2026-08-31 by Claude via the Plaud connector. Transcript block `transaction_polish`, Plaud's cleaned-up transcript, which keeps speaker labels and timestamps and tidies filler. The raw `transaction` block was not used here because the polished block returned complete and readable; if a verbatim quote ever matters for this call, re-pull `transaction` against the file ID above.

**Who was there:** four diarised speakers, none named by Plaud, and the identities do **not** resolve cleanly. Laid out here with the evidence rather than guessed:

- **Speaker 2** is the outside consultant. 5,056 words, the most of anyone. He is being shown the systems rather than showing them, asks the mapping questions, proposes moving production work onto Parakeet's own server, and describes himself as "not a business analyst from McKinsey" and "on Twitter all the time because of the nature of my business, the social media stuff." **Very likely the "Robert" named in the final utterance of the call.** INFERRED.
- **Speaker 4** is the internal builder. 4,850 words. He shares the screen, demos the listings dashboard, the listings audit, the prospect funnel build and the Cowork workspace, and says he will send copies over. He refers to Austin in the third person once ("it's notifying Austin and I") and appears to address Austin directly twice ("just like Austin talked about on the front end", "I had it scrape all our board decks, Austin, last night").
- **Speaker 3** speaks about the team's reporting needs and twice pairs himself with John ("what John has built here as the template", "help John and I versus helping the team").
- **Speaker 1** contributes 17 words across six segments and speaks the last word of the call, "Robert."

**The contradiction, stated rather than smoothed over:** Speaker 4 both refers to Austin in the third person and appears to address him, while Speaker 3 is the one who speaks as an owner. On a four-way call with a shared screen and heavy overlap, Plaud's diarisation drifts and merges turns, and at least one of those three attributions is wrong. Do not assign a quote from this transcript to a named person without listening to the audio at that timestamp.

**Handling flag:** this is a prospective paid engagement. The consultant proposes a value-based fee rather than hourly, a Railway server at roughly $5 a month to start, and asks for a Pro account plus API and MCP credentials for Rent Manager, the data warehouse and the CRM. CLAUDE.md rule 8 applies: analysis yes, action no. **Nothing in the to-do list below is authorised**, and the credential handover in particular is a real decision with real exposure, not a task.

**Why this one matters beyond the engagement question:** it is the clearest running description anywhere in this Brain of how the listings pipeline actually works end to end. Rent Manager to My State MLS, mandatory because of licensing, then syndicated out to Realtor.com, Zillow and Trulia, alongside MH Village. It also names the audit coverage gap (Zillow and Realtor.com are not audited), the roughly 15 sources feeding the prospect funnel build, the 100 to 120 day home preparation window before a home is listed, and the nightly crawler checking around 6,000 MH Village listings. Those are facts about the business, not about the vendor, and they are worth filing whatever happens with the engagement. Numbers stated on a call still need a primary source before they go in the ledger, per rule 3.

## Plaud's AI summary

Plaud generated the summary below. It is Plaud's output, not a verified reading of the source. Treat as SINGLE-SOURCE and check against the transcript underneath before relying on it. The to-do list is Plaud's construction, split between "Customer" and "Consultant", and **none of it has been agreed, scoped or approved by anyone.**

> Date & Time: 2026-08-31 09:03:21

### Overview
The series of consultations focuses on streamlining and enhancing the client's manufactured/mobile home listing and sales operations through automation, AI, and improved data pipelines. The client's business involves acquiring and preparing mobile homes, listing them for sale, and renting sites to residents. A central theme is the migration from fragmented, inefficient workflows, such as reliance on daily CSV drops from their property management system (Rent Manager), manual data entry, and costly, ad-hoc AI usage (Claude), towards a robust, centralized, and cost-effective operational infrastructure.

Key objectives include ensuring data consistency across multiple systems (Rent Manager, a SQL data warehouse, CRM, website) and third-party listing platforms (MH Village, My State MLS, Zillow, Realtor.com); developing live, permission-controlled dashboards that serve as a single source of truth; reducing human data entry errors through form-driven intake (QuickBase/FastField); controlling AI costs by moving to server-based solutions with model-agnostic routing; and improving the quality and SEO of listing descriptions to gain a competitive edge. The ultimate goal is to build an independent, scalable, and powerful internal toolset, starting with an MVP for a listings monitoring dashboard, and to prevent discrepancies rather than just reactively auditing them.

### Background
- The customer operates in real estate, exclusively selling and listing mobile homes. Their core data system is Rent Manager, supplemented by a Microsoft SQL-based third-party data warehouse, a CRM ("Nav"/Math Consulting), and QuickBase/FastField for data entry.
- The listing data flow is: Rent Manager to My State MLS (mandatory due to licensing) to syndicated portals (Realtor.com, Zillow, Trulia).
- The home preparation process takes "hundred" to "one hundred and twenty" days before listing.
- Previously, operations relied on daily CSV reports from Rent Manager, scheduled tasks, and browser-based automation to build and distribute dashboards, which proved unreliable. This has evolved to using Claude for daily tasks like email generation and audits, but this approach has led to high token usage and occasional "hallucinations."
- A web listing audit tool has been running for 60 days, successfully reducing audit flags from fifty to a few per day, but it requires an AI reasoning layer to explain discrepancies caused by data lags.
- A complex prospect/sales funnel dashboard is in development, aggregating data from ~15 sources (CRM, warehouse CSVs, property management system, Microsoft Bookings, Google Analytics, RingCentral, etc.).
- An internal "cowork" workspace (Claude-based) is used as a scratchpad for numerous projects, including data audits, description rewrites, board deck automation, and dashboards. Key components are now ready to be migrated to standalone servers and domains to improve stability and control costs.
- Recent technical progress includes enabling MCP/API connections to Rent Manager and the data warehouse to facilitate direct data access for live dashboards and historical analytics.

### Pain Points

**Data Discrepancies, Normalization, and Synchronization Risk**
The primary challenge is maintaining data consistency across a complex pipeline involving multiple systems and manual entry points. Discrepancies originate from human error during intake, propagate through Rent Manager to My State MLS and other portals, and are exacerbated by fragmented workflows (CSV drops vs. APIs). This creates synchronization risks, stale data, and inconsistent listings.
- Impact: **Inaccurate listings reduce conversion and SEO performance**, cause confusion for sales/marketing, and require manual reconciliation. High AI token usage is incurred for reactive audits and corrections.
- Current Situation: A "big listing audit" has corrected many issues, and a nightly crawler checks "six thousand listings" on MH Village. The team is rolling out QuickBase/FastField forms to standardize data entry and automate daily updates to Rent Manager. However, audits are incomplete (Zillow/Realtor.com coverage is missing), and scheduled tasks still occasionally misfire.
- Examples: Mismatched pricing, incorrect statuses, misordered images, and misformatted descriptions across websites. A "wrong version that misfired this morning" led to missing dashboard output.
- Stakeholders: Sales and marketing, listing submission staff, operations/C-level, and the website developer.

**High Cost and Rigidity of AI-Driven Workflows**
The current heavy reliance on a single AI system (Claude) for daily operational tasks (audits, crawling, email generation) creates significant and unpredictable costs, reliability issues, and a lack of flexibility. The "cowork" environment has led to spending spikes (e.g., using expensive models like "Fable"), and limited visibility from Anthropic's console makes task-level cost auditing difficult.
- Impact: **Budget strain, uncertainty about AI spending, and operational friction from AI "hallucinations."** The dependency prevents the adoption of more cost-effective or specialized models (e.g., GLM 5.2, cited as 40x cheaper).
- Current Situation: Model selector skills and context window monitoring have been implemented to reduce waste. The plan is to migrate production components (dashboards, crawlers) to standalone servers to reduce daily LLM runs and enable model-agnostic routing (e.g., OpenRouter, Token Router).
- Examples: Heavy document work (board decks, legal memos) and web scraping within chats driving up costs.
- Stakeholders: The internal builder, finance/ops, and corporate leadership.

**Limited Live, Centralized Dashboard Access and Permissions**
Dashboards are currently generated and distributed as files via email/SharePoint links rather than being hosted as live, permission-controlled views tied directly to the source of truth (Rent Manager API). This limits ease of access and increases the risk of teams acting on outdated information.
- Impact: Users rely on emails and saved files, creating friction and risk. Manual filtering and sorting are required across scattered sources.
- Current Situation: A SharePoint homepage redesign is underway to centralize report access. MCP/API access to Rent Manager and the data warehouse has recently been enabled, creating an opportunity to build live dashboards.
- Stakeholders: All employees, sales/marketing, C-level, and IT/SharePoint admins.

**Incomplete Automation and Tracking**
Several key processes remain manual or untracked. Listing price adjustments are not automated due to incomplete CRM data integration and the need for human judgment. Social media postings (especially to Facebook groups) are done separately and are difficult to track, limiting performance analytics.
- Impact: Manual workload remains high for sales/marketing, and there is a lack of performance insight for social channels.
- Current Situation: Rules exist for listing revisions (e.g., at "sixty to ninety days"), but actions are manual. Integration with an AI calling agent (Unity) is planned to improve CRM data integrity. The Meta API is seen as "tough, but possible" for tracking social posts.
- Stakeholders: Sales/marketing, C-level, and data/IT.

### Expectations

**Build Live, Server-Based Dashboards and Offload AI Workflows**
The primary expectation is to migrate from Claude-dependent, file-based reporting to a persistent, server-based dashboard system. This system will connect directly to data sources (Rent Manager API, SQL warehouse), provide live visualizations with role-based permissions, and include built-in reasoning to explain data discrepancies. The first step is to build an MVP of the listings monitoring dashboard on a dedicated server (Railway).
- Specific Goals: **Build once, operate without daily LLM runs.** Replace email-distributed files with a live, centralized dashboard integrated into SharePoint. Reduce or eliminate daily Claude token usage while providing explanatory outputs.
- Success Metrics: **Near-zero daily LLM token usage**, reduced failures/misfires, consistent real-time data, and successful live publication with daily HTML snapshots for auditing.

**Standardize and Automate Data Intake and Listing Generation**
Implement a robust, form-driven data intake process using QuickBase/FastField to eliminate human error at the source. Complement this with an AI-assisted listings generator that enforces templates, tone of voice, and SEO best practices to create error-free, high-quality descriptions before publication.
- Specific Goals: Standardize data entry to ensure clean data from the start. AI to generate and validate every listing against standardized templates and data from internal reports.
- Success Metrics: Fewer discrepancies in audits, automated and accurate daily data imports into Rent Manager, and consistent, templated listings with improved SEO and conversion.

**Expand Audit Coverage and Move from Detection to Prevention**
Expand automated audits to cover all syndication channels, including Zillow and Realtor.com. Shift the overall strategy from reactively detecting discrepancies to proactively preventing them through validation rules in the data pipeline.
- Specific Goals: Implement comprehensive cross-platform audits. Introduce a gated "listing intake validator" to block bad data at the source.
- Success Metrics: Audit findings approaching zero, reduced mismatches across all platforms, and a faster detection-to-fix cycle.

**Enhance Analytics and Cautiously Automate Actions**
Integrate CRM data (e.g., tour counts) and analytics from the data warehouse to better inform pricing strategies. Introduce AI-driven recommendations (e.g., morning signal emails for listings at 90 days) before moving to fully automated actions like price drops.
- Specific Goals: Combine CRM signals with listing data to guide price changes. Automate and track social media postings to provide unified performance analytics.
- Success Metrics: Documented outcomes of pricing strategies (e.g., impact of a "ten percent" price drop), improved days-to-sale, and trackable reach and engagement for social channels.

### Other Information Summary
- The client exclusively sells mobile homes, and My State MLS is a mandatory part of the syndication pipeline due to licensing constraints.
- A data warehouse captures daily/weekly/monthly snapshots to preserve historical changes (e.g., listing price changes) and enable analysis.
- The consultant advocates for model-agnostic, low-cost solutions hosted on the client's own server (e.g., Railway, with initial costs of ~$5/month). The proposed compensation model is value-based, not hourly.
- Open-source tools like Firecrawl are suggested to improve web crawling/parsing and further reduce reliance on expensive LLMs.
- An AI calling agent (Unity) is being integrated to improve CRM data quality due to its niche focus and existing integrations with Rent Manager.
- Production-ready components (dashboards, crawlers) currently in a "cowork" workspace will be migrated to standalone servers for stability and monitoring.

### To-Do List (Plaud's construction, nothing here is agreed or approved)
- [ ] [Customer] Compile a consolidated list of all system names and listing websites (CRM, data warehouse vendor, ~15 data sources, Zillow, Realtor.com, MH Village, etc.).
- [ ] [Customer] Provide API/MCP access credentials and documentation for Rent Manager, the data warehouse, and the CRM.
- [ ] [Customer] Set up a Pro account on Railway and provide the consultant with access.
- [ ] [Consultant] Design and deploy the MVP of the live, role-based listing dashboard on Railway, integrated with Rent Manager API and the data warehouse, with daily HTML snapshot publishing.
- [ ] [Consultant & Customer] Interview the listing submission employee to document the exact workflow and identify automation points.
- [ ] [Consultant] Evaluate and integrate Firecrawl (or similar) into the web listing audit pipeline.
- [ ] [Consultant & Marketing/IT] Design the AI listings generator: finalize templates, tone, validation rules, and data sources, aligning with QuickBase/FastField schemas.
- [ ] [IT/Consultant] Implement comprehensive audits for Zillow/Realtor.com syndication and harden scheduled tasks (logging, alerts, retry logic).
- [ ] [Marketing/IT] Scope Meta API integration for Facebook group posting and tracking, defining UTM standards and analytics requirements.
- [ ] [IT/Finance] Establish API key segregation and usage logging for major AI tasks to improve cost visibility.

### AI Suggestions (Plaud's own, unreviewed)
The AI has identified the client's biggest pain points as **data discrepancies from fragmented, multi-source pipelines** and **heavy reliance on costly, rigid AI workflows**. Here are some possible solutions for consideration:
1. **Implement a Gated Intake & Syndication Pipeline:** Architect a data-first workflow starting with a "listing intake validator" integrated with QuickBase/FastField to enforce schema and business rules at the origin. This feed would power an AI-driven listings generator with deterministic templates and an SEO-aware validation layer. The final, validated data would then be pushed through a single, monitored syndication pipeline to Rent Manager, My State MLS, and other channels.
2. **Deploy a Server-Based, Model-Agnostic "Optimization Engine":** Build the proposed solution as an independent, server-based platform on Railway, not just a dashboard. This engine would integrate a "Model Router" (like OpenRouter) to dynamically select the most cost-effective AI model for each task (e.g., cheap model for classification, powerful model for generation). This immediately demonstrates the value of independence through tangible cost savings.
3. **Create a Unified Admin Dashboard with Built-in Reasoning:** The engine's frontend should be a persistent admin dashboard connected directly to APIs (Rent Manager, data warehouse). It should surface not just issues but also data-driven explanations (e.g., "Price mismatch due to 12-hour syndication lag") and provide historical views via data warehouse snapshots. Publish daily HTML snapshots for auditability.
4. **Centralize Auditing and Social Posting:** Integrate a robust crawler (like Firecrawl) for nightly reconciliation across all portals (including Zillow/Realtor.com) and automate ticket creation for discrepancies. Add a social posting scheduler that integrates the Meta API and enforces UTM standards, unifying analytics across all web and social channels.
5. **Introduce Lightweight Inference and Task-Specific API Keys:** For simple tasks like data classification or routing, use smaller, specialized models or rule engines to cut token usage. Implement task-level API keys and lightweight telemetry to correlate AI jobs with costs, enabling continuous optimization of model selection and prompt engineering.

---

## Full transcript

Verbatim from Plaud. Nothing removed, nothing tidied, nothing summarised away. Timestamps are offsets from the start of the recording, so they map straight back onto the audio in Plaud under the file ID in the header. Speaker labels are Plaud's own diarisation and are **not** resolved to people. Read the speaker note above before attributing any line to anyone.

**[00:09] Speaker 1**

All right.

**[00:11] Speaker 2**

Hey! Good to see you guys.

**[00:19] Speaker 3**

Good to see you. Not driving in the car.

**[00:22] Speaker 2**

Finally back in office. Are you happier on the road? Yeah.

**[00:27] Speaker 4**

Maybe on the road.

**[00:29] Speaker 3**

Oh yeah, that's true.

**[00:31] Speaker 4**

These days. How's it going?

**[00:36] Speaker 2**

All good. Busy, but happy to be here. You've been thinking about your case. I think it's a very interesting puzzle. So I would say so.

**[00:46] Speaker 3**

Puzzle, very.

**[00:50] Speaker 2**

Have you been expanding your AI operations, or is it running as it is?

**[00:58] Speaker 3**

Knowledge base

**[00:58] Speaker 2**

I would say continuing.

**[01:03] Speaker 3**

To expand. Obsidian. I actually just over the weekend connected it to see how the brain is looking and how it would work and how to use it, but nothing permanent.

**[01:16] Speaker 4**

Yeah, Obsidian confuses the shit out of me. Because he knows. Yeah, I originally downloaded it to like actually just be able to view MD files, not in Notebook. And I haven't done anything, and then I haven't done anything else with it.

**[01:32] Speaker 2**

That's exactly the case, guys. Maybe once a month, a user looks into it. Mostly, it's just a beautiful graph, but it adds a lot of extra context. It's against what I'm trying to to help you with. Like, it's it's going to overload your AI context window and waste more tokens. Got it. I'm not a any subsidiary per se.

**[01:53] Speaker 4**

I'm saying we'll just overload it and waste more tokens.

**[01:55] Speaker 2**

Got it. It's not that I'm against it per se, but not for corporate. Not for company data for sure. It looks beautiful, though. The cloud of the notes. But today I wanted to actually be hands on mapping certain things as you speak. I have my board open, and again, not to overpromise, not to go way too wide. I would pick one case that needs to be sold, that is already being sold.

**[02:32] Speaker 2**

That is the most wasteful and also the the highest return, right for your company. Like you're actually saving man hours, you know, not not suffering with redundant work, right? And and do that. Like I will show you that as a blueprint how it can run on your own server, how it can be fully model agnostic, close to free in terms of API usage, right? Not paying cloud thousands. And and also functional, right? It should not decrease in quality. That's another criteria that that I'm after, right? But only one one thing at a time, right? Like invoices, let's say, or certain reports, processing the data into into your other systems. Something simple, right? And yeah, I'm ready to start mapping it hands on instead of yeah, just open so I'm.

**[03:25] Speaker 4**

I'm not sure what the best thing to go into. Maybe I'll just jump into a handful of things that are going on a scheduled basis, and then a handful of things that I've been working on as ongoing projects.

**[03:45] Speaker 2**

Yeah. We're just mapping them. Yeah. I'm not asking you to name one immediately. Of course not. Let's let's map them and then we'll see. Okay. So is it helpful if.

**[03:52] Speaker 4**

I share my screen in God. It's much better.

**[03:55] Speaker 2**

Actually. Right.

**[03:57] Speaker 4**

So how big, how wide of a screen do you have? I have one of these giant triple monitors.

**[04:05] Speaker 2**

I'm an intro.

**[04:07] Speaker 4**

So I'm gonna do that because I'll be able to show you three things at once, which I think would probably be beneficial.

**[04:34] Speaker 2**

You see this? I'm able to zoom in and see your GitHub.

**[04:41] Speaker 4**

Yeah, it's not that. That's just nothing. I haven't done anything in GitHub. I haven't downloaded anything or put anything there. No, no, is that? So, so here's I'm going to show you two examples of things. Three examples, maybe, of things that fire off daily, which have changed actually a little bit. From when the last time we spoke, I think I optimized it a little bit. Here we go. Okay, so we'll start with this one. Mm-hmm. Because it's all kind of the same. So this is a listings dashboard. We told you a little bit about our business. We have, but we we own the land. We rent the sites out to residents. In order for us to sell homes and bring new residents in.

**[05:32] Speaker 4**

We effectively buy the home, get it all set up, then we list it online and we sell it to someone else. So, like for example, I think this context is helpful. Tell me if it's not. Here's our website. You can go on here, homes for sale, and you can see, you know, this home we bought, we set it up, we're selling it, right? So part of this whole process, our information lives in.

**[06:02] Speaker 4**

Rent Manager, a property management system. In Rent Manager, every single home that we buy has an asset record associated with that home. That asset record includes a ton of different information. This is just a snapshot of it. Some of it being listing related, and also I think this is the one that didn't fire off right. By the way, so I don't have it right now.

**[06:34] Speaker 2**

Each row is a listing item.

**[06:37] Speaker 4**

Each each row is an asset. This asset listing is actually like six thousand deep, because it pulls from the system. The ones that do, it's not gonna. This is the wrong version that misfired this morning. But an example of something that happens is right now, rent manager drops the report as a CSV into a folder. Claud knows to look to the folder to get the asset listing. The information that it has on the asset listing is directly feeds our website. So it feeds the beds, the bath, the price, the description, all this stuff. It then also feeds MH Village, and I'll show you why all this matters. It also feeds MH Village.

**[07:26] Speaker 4**

Not gonna find it, but the same listing on here, right? Which is a broader, like Zillow type thing. Yeah, yeah. So the listing dashboard is. I have it as a scheduled task. It runs at six o'clock or whatever every morning. It goes in and it creates the dashboard. So now I have the dashboard. I used to have clogged Chrome, like. Creating the email, then attaching the dashboard to the email, then sending it to everybody. It was always breaking with the attachment because it has issues attaching and sending and stuff.

**[08:02] Speaker 2**

The browser is not reliable.

**[08:06] Speaker 4**

Yes. So now I have it doing it. I think with the Outlook connector, and it creates a SharePoint link to the file that people then open. Right, so they have access to it. They can open it. So this is the output of what it creates. It takes all the data from the system. It looks and populates it with like the date that it's listed, the price that it's listed at. It it goes into our website and it checks all listings on our website, provides a link. So if someone wanted to come in here, and like review a listing, they could tap it. It then also goes and scrapes and looks at the MH Village listing.

**[08:48] Speaker 4**

So that they can tap it and see it, and that's kind of that's kind of it. It allows for good sortings by portfolio, all these things. It then runs audits and checks. It looks for things missing from our website, things stale on our website, things missing on other websites, and then it does a data check where this is more of like a system issue where something. Is in one status, but it's just mismatching data.

**[09:23] Speaker 2**

Mismatching exactly. Yeah, I was about to say that. So it works for you. So that the the goal is to have unified data on every listing aggregator. Let's say on every website where your property is listed. Correct. But I have a quick question. You said the your website. Is the one dropping the data? So the input comes from the website, but who who uploads it on the website? No,

**[09:49] Speaker 4**

Your operator on the website comes from that Excel file. It comes from our system, so it automatically feeds our website.

**[09:56] Speaker 2**

Then there is a missing step: the admin of the website, the CMS, the content management system of your website. I'm not sure if you're using WordPress or your own one.

**[10:08] Speaker 4**

But we don't do it. We have a third. Party managing the website, and they have an API into the system that pulls the data out. And that and that seems.

**[10:17] Speaker 3**

Hold on, that seems like there's not a verification of information.

**[10:20] Speaker 2**

Is that what you're saying? Just curious about the data structures. Because the CSV structure you showed me matches entirely your own website. But whenever you list on other people's websites, there is already normalization and mapping needed.

**[10:39] Speaker 4**

And they have that set up, that like that set up and seems to be working. Like for today, for example, if you look, like both our website and MH Village are fully clean and matching.

**[10:50] Speaker 2**

That's great. That's but how often do you let's say add and populate more listing websites? Like, would you be interested personally to expand? Like, it's also an interesting.

**[11:05] Speaker 4**

We have. You mean other listing websites? Yes. We have them populating through. There's another layer of audit that I haven't built now, where we have it feeding another system, which puts it on like Zillow and Realtor. com. I haven't built the the checks to that yet. Um,

**[11:25] Speaker 2**

We'll focus on that system. Just what what what what I was gonna say is that using AI and those custom automations is perfect for normalizing data, like remapping it basically. Like if the website wants a, You know, twenty columns of data with those names, remapping them from your original one is going to be, like a good task to do, right? It's a it's a it's very much doable.

**[11:50] Speaker 4**

And I think that's taken care of. I'm like Austin, our website developer who manages the website. That doesn't seem to be an issue. They might be using AI for it.

**[12:10] Speaker 2**

But no, because it's a. You're right. And the one - time Python script that remaps the fields, it's instant and it's free. There is no need to use AI. Just saying. Okay, but that. Just a point of one thing.

**[12:22] Speaker 4**

I don't really know how that works. Like we're not doing that, but it seems to be working.

**[12:28] Speaker 2**

That should be an integr. It's an important step, so I'm asking so that it's also integrated in the overall flow. We can follow this.

**[12:36] Speaker 3**

Park web and make sure that they're doing something like that.

**[12:40] Speaker 2**

Sure. Also, I would prefer to list every website that you are interested in having your listings on. Later, I will send the questions. The rent management system that you are currently using is the one for updates, right?

**[13:00] Speaker 4**

Because that is like the source of truth. So when that is updated in that system, it populates everywhere else. That is where all the listing data lives. So it's all in one place.

**[13:14] Speaker 2**

I see. I see. I see. So the the source of truth is super important. And what you did is you visualized it, right? Correct. You visualized it in your own way. Also, I assume because I did not catch the goal of, Sharing what it is? No. Why do you need to share it via email, right? If you have already a system that probably has the user interface, right? Not everyone can log in and and see that data, right? And also, it's not updated. Um. Or or or why? Why why do you need to share the the listing data?

**[13:49] Speaker 4**

I would say the reason is that we lost him. The reason for sharing it is putting it all in one place so that it's filterable and sortable. If you just pulled it from our property management system, it would be in a gross format.

**[14:25] Speaker 4**

I wouldn't be able to filter through different things. I wouldn't be able to click through to the different listings to look at them. I wouldn't. In in the end, the goal of this is to have it be a actionable sheet for our sales and marketing department to go through and say, okay, this has been listed for sixty to ninety days. We also will probably integrate some data from our CRM into this eventually that can show how many. Tours they've had at that home. How many other things? So it pulls in the data from a bunch of different places, and allows them to make decisions on, okay, this has been listed for sixty days. We should probably drop the price, or so that we can get more traffic or whatever.

**[15:08] Speaker 2**

So those advisory things, right? They could actually come from a smart AI agent. That is an amazing case. What do you think?

**[15:17] Speaker 4**

The are all built in up here in terms of the listing revision strategy for them. Now I would say we're not handing off the automated listing changes to AI yet because we don't have all the CRM data fully built out, and because that's kind of the job of our sales and marketing department. Like I don't really, I don't really want them automating it. There's some art to this versus just keeping it truly mathematical. At least at this point, till we know what's working and have real data on.

**[15:51] Speaker 4**

Okay, we drop price ten percent. It sold in X days. You know what I mean?

**[15:55] Speaker 2**

So like that's analytics already. That's both, yeah, sale analytics. There's something else, but insights could be an interesting like just signals, right? Like so he doesn't have to scroll as you just did, right? Or or filter by hand. He just get the morning email, like by by the time that like these are the ones that listing reached ninety days with no sale. Boom, you get it in the list. Like oh. Listing 57 is there already for a while. Go look at it, kind of like a just a heads up kind of thing. Man, this is amazing! This what you did with Cloud Code, Cloud Code Work is amazing. This deserves it's own website, right? A stable thing, like it cannot live on the Cloud Code Work link, right? It's a perfect blueprint, right? For a small solution to to be rebuilt into your own admin dashboard for listing management.

**[16:49] Speaker 2**

And it can even be a product. I think it's great. You can even distribute it to other companies doing the same thing.

**[16:58] Speaker 4**

So that, so yeah, and I think in the end it would be most ideal if this was just something live, and the email, to your point, was like, hey, look at these audits, fix these things in the system. Here's the new. It's also informational to us because it will say this day there didn't happen to be any changes, but if we listed four new homes. It's catching it, and it's notifying Austin and I, versus me having to like I don't otherwise I don't get a report from anybody. Unlike yeah, we listed four more things, or we did this, just to go off of. There's another one that's built. It's a home sales and rental tracker. Same concept, running off similar data, but it basically shows, again, more for us. Like, homes that we've sold year to date.

**[17:49] Speaker 4**

Percentage of sale price, days that they were on the market. There's some gaps because we weren't tracking data before. It flags data issues for the team to fix. But basically, this is just a report of all our ongoing sales and rentals that are happening. So, same sort of thing. I can sort. I can look at new homes, old homes, whatever. I can see my different audits and checks and the things in the system that people need to fix. And that's kind of it. Should this live?

**[18:18] Speaker 2**

I'm also coming. So sorry to interrupt. Just to clarify, the the data is coming from the listing, the rent management system, from the main source of truth. This is not a separate data structure. Right.

**[18:28] Speaker 4**

Same system runs off the same CSV.

**[18:32] Speaker 1**

-

**[18:33] Speaker 4**

Now, so like, so the yeah, so there's little improvements, right? Like, could this be published live somewhere that just updates every day? That would be cool, as opposed to me having to send an email out or save an attachment. I do like saving the daily versions of it, so I could go back and look and see how things changed if I needed to, or if I catch an error. The other thing that I would say is like the CSV thing is clunky, but we have a way to MCP or API into it. We just haven't set it up yet. Mm - hmm. Um.

**[19:08] Speaker 2**

But there's a trigger. There are almost daily triggers to the updates.

**[19:17] Speaker 4**

They're daily. They're weekdays. They fire off every morning at six in the morning.

**[19:20] Speaker 2**

But it saves a separate file on your desktop.

**[19:26] Speaker 4**

On SharePoint, it actually saves a separate file in a folder where everyone can see. It's got all the updates, so it saves everyone. Just move it over.

**[19:45] Speaker 2**

And they would prefer to because what the dashboard does is it basically visualizes that very same data in a more convenient way, so people won't even have to use those daily files.

**[19:57] Speaker 4**

Exactly. They can just open the email, pop it open, see it, or go directly to the folder it's in and open it and see it.

**[20:06] Speaker 3**

I think would if it was. I think what you're saying also is it would be like a dashboard. They don't even need the emails. They just know it's there. Which would then, which would then parlay into what we are also working on. You know, I would say outside of AI, but kind of brings this connection, which is we're re kind of doing our entire SharePoint, you know, storage system for the company, which we're gonna make everybody's home screen kind of be our company page. Which then that would be like a button to click to get this report, or, you know, a tab on that.

**[20:40] Speaker 3**

Which everybody can access right away is what you're saying. So instead of these coming from an email, it's just here's your morning home inventory, or here's your age listings, or whatever it is.

**[20:51] Speaker 2**

Why I also ask is because that seems like basically if there is one source of truth, like one backend database. Whatever you build on top should be only visualizing that very same data, because the moment that you report it, re-format it, save it somewhere else, there is always a risk of desynchronization.

**[21:14] Speaker 4**

Which is what happens every once in a while with the CSV thing, which is annoying. It's taking the data and putting it one place.

**[21:21] Speaker 2**

Whatever. If I was to build something like that, it would be pulling data live from the API of your red management system, only, only, just. Revisualizing it, right? Would never save it somewhere else. Would never make sense to build a separate DB, mirroring it or something, just because it's risky. Like even the best data scientist, you know, or data engineer, that I'm not, right, would probably be struggling with, with this issue, right? So it's better to just use one source, right? Publish it, and and also, yeah, the other item that I'm listing here is the users, right? Like what.

**[22:01] Speaker 2**

Who are your users? There is a marketing team, right? There is you guys, the C level, that because you have different degrees of permissions of the data that you want to see, which is that should be implemented, right?

**[22:16] Speaker 4**

So we're going through a bunch with regards to like the SharePoint thing, but I mean there are permissions and everything are kind of in place. The other thing that I would mention is important. I am starting to understand this more. Austin's a little bit. Raton, more. We have that rent manager source of truth. We also have a data warehouse that takes us a basically a snapshot of all the data. What Austin daily?

**[22:43] Speaker 3**

Depending on which report, we have it pull on certain timing. If it's updating daily, or if it's something more stable, it's weekly or monthly.

**[22:56] Speaker 4**

Because. Reason being, if something changes in the system, we want the historical record. So, if we wanted to see, you know, what a list is right now, this is a perfect example for our listings. Right, there's only one field that is the listing price. That listing price feeds the websites and feeds this and everything. It's one place. If they decided to change it by lowering the price to try and sell the home faster. We're not adding a second listing price column, so the data warehouse captures every day, so that we would be able to say what date did the that we drop the price? How many days has it been since we drop the price? What's the traffic and the volume look like since we drop the price? So there's that layer on top of it, which is the versioning.

**[23:47] Speaker 2**

Yeah, and there's the logins, right? Like the the the very event of the price change is getting logged. You could look look it up. It's not an issue for sure. And this is all handled by your property management system, correct? This is already it's a backend.

**[24:00] Speaker 4**

The data warehouse is outside of the property management system.

**[24:04] Speaker 2**

Ah, okay.

**[24:05] Speaker 3**

It's an API that pulls pulls from it, and what we now have, which we're testing, and you know, hopefully get it turned on more, is MCPs directly to the rent manager API, and then one to the data warehouse, because some of the we keep the data warehouse, for instance, prospects. Prospects it overwrites their stage status and and you know certain things that you can't pull out by do by pulling it into the data warehouse daily, we're able to see the you know actual days in previous processes like how in in previous stages how long it's taking for people to get through things so you know that's one aspect or just the overall historical like John saving the report, the data warehouse is saving the data behind it.

**[24:50] Speaker 2**

What is the solution for the data warehouse? Is it a third-party thing, or did you build it?

**[24:54] Speaker 3**

Or it's a Microsoft SQL through a third party that was doing before AI came out, that was really doing it to then get us Tableau and Power BI dashboards on everything going on. They even started to pivot their business, but you know, we have the data warehouse with them and and keep it updated, and it's been going great. So anything that we could use for that, like we've been. Testing just certain questions for the team in the field, like what's my AR, who's my delinquent residents, things like that, that would just pop up. But again, it's you know, ideally, it would be best to go straight to rent manager through the API for most of us.

**[25:36] Speaker 2**

Now I'm thinking, and thanks for clarifying that. Now I'm thinking that maybe using the data warehouse as a primary source of data for this dashboard is actually beneficial. Yep. Because at some point, you might want to also look up. Historical data, right? You would might want to use analytics. Maybe then, if there is already the second step, right? The second source of truth, yeah. The warehouse, then, and also it's more. I assume that since you're working with the team as an operator, right? They would be much more flexible in providing us accesses, like right, like you mentioned MCP. I'm not sure if it exists or it has to be.

**[26:13] Speaker 3**

It does now. In the last two weeks

**[26:16] Speaker 2**

It does. I again presume that the rent management system is way more rigid, in these terms. They won't move their ass for the AI advancement as fast as those guys processing your data. So let's work with them. For sure, with the MCP that they've set up, and visualize it. I see a quite straightforward task. You need an admin dashboard. You have multi-level, multi cohorts of users.

**[26:47] Speaker 2**

This is a perfect blueprint for it. There are some redundancies that Claude did or hallucinated, and I'm sure you fixed many already. But it should not run on daily token usage at all. You build it once, boom, no use it for Claude.

**[27:03] Speaker 4**

Like zero. That's part of the issue. This is firing out of Claude every single day, creating emails this and that. It should have been built there, but it should be able to just speak to the data. Although there is some element of analysis on it. That's the thing I struggle with because it has to actually go through and look at the websites. So it actually goes and looks through to see if there are glitches that don't match on the websites for whatever reason.

**[27:45] Speaker 4**

On the data, it has to be smart enough to understand where you know current status is this, listing status is this, why, and provide an explanation. Like I don't want to provide our team just like, hey, these are three issues, fix them without giving them some explanation of what the issue is. People always do that to us, and I hate it. Right? Like, hey, don't just give me a problem; give me a problem and a solution. Which is what we try and do, even though no one. That means it's been working good for you, right? Like, it's been working good. This thing, when it first got rolled out, had fifty audit flags and everything, and now, quite frankly, the team keeps it to a few a day. And there's some natural data lag and things, so like it's running.

**[28:32] Speaker 2**

And it's not just a pricing mismatch. There could be images that are not in order. Some other descriptions are messed up.

**[28:40] Speaker 4**

Descriptions. Things that are showing up on one website and not another, like there is some reasoning that needs to happen to it, which is an AI overlay. It's just a way it can API. There's some way to connect. There are some sources.

**[29:03] Speaker 2**

Sources, yeah, and that are actually optimized for scraping. Right and crawling websites way more than even a quad skill could do, right? And and they're free. They're they're yeah, fully open source. Right? Like you should be the open GitHub thing. There would be a repo. I don't know. I I use it for my own tool right now. There's a thing called Firecrawl, which is a global like it's a very well known thing that that open source that even keyless. Like you can you don't even need an API to to give your agent.

**[29:38] Speaker 2**

An insane crawling capability for web, and also parsing PDFs, CSVs, Excel's, whatever files. A hundred percent faster, a hundred times faster than than usual. All AI optimized. Those guys are just giving it away, and it's all about plugging it in in your system and and saving it a bunch of a bunch of usage, basically. Yeah, because regular Claude does it, right? But sometimes it struggles, sometimes it hallucinates. And as I understand, the submissions to those websites, right, this data discrepancy, could also be minimized, right? Because like reporting issues is is is a great thing, but preventing issues should be right primary. Because you provided data, right?

**[30:24] Speaker 4**

And then I'm going to show you one other example, which is in the process of getting built out, which is I would say highly more complex. This is like. This is so we have a CRM. The CRM has a bunch of data going into it. There's all sorts of things that we're working on with the CRM in terms of getting the data in the CRM cleaned up. That's like first step, just because it had a bunch of old data in it. A bunch of prospects weren't getting sent automations. So there's a big cleanup process that I've mapped out. You know, with the help of Claude through this that we're going through. Once it's all cleaned up.

**[31:05] Speaker 4**

I've built a dashboard across a bunch of different items to essentially totally inform the sales and marketing process, like the prospect funnel. I'm just flipping it very quickly so you can see.

**[31:20] Speaker 2**

I'm looking. Was it Salesforce, HubSpot, or what are you guys using?

**[31:25] Speaker 3**

No

**[31:25] Speaker 2**

Math consulting. Yeah, that's awesome. You'll send me. Okay, I'll send you the list of questions, and you'll send me the exact name of it. But you you all stick with that CRM, right? You cannot just move.

**[31:37] Speaker 4**

Right now, one of the reasons we chose it is it it talks back and forth to the property management system, so it allows us to keep things up to date. So this sheet, like this dashboard, which is what makes it way more complex, is it's pulling data in from a ton of different places. So right now, it's pulling in exports from the Nav, which is the CRM. That will eventually have an MCP. We have a follow-up call with them today, on that. It's pulling info from a CSV from the data warehouse for now because it's not, it's not fully connected. So it's pulling data from MAB. It's pulling data from our property management system through the data warehouse. It's pulling data from the property management system itself. CSV drops like the asset listing. There's.

**[32:32] Speaker 4**

It's pulling data from a Microsoft bookings tool that we use for booking tours. It's pulling information from an RV website that we have bookings on. It's pulling information from Google Analytics, from Ring Central, which is where our phone calls run through. That's it. It's pulling in from like 15 different things, aggregating it all, and putting it all together in a bunch of analytics on this dashboard. So this is one that's like fairly complex. It might become a little less complex as we get it finished, but there's a ton of different data sources flowing into this. I'm not updating this and sending this live every day. Obviously, the angle for this, just like the rest of them, should be living on our website as a published thing with probably a daily HTML save down, just as a timestamp on it.

**[33:30] Speaker 4**

But this is not to the point of being live and circulated right now. We're using it as a, like a tracker to essentially track the progress of getting everything fresh, getting everything working,

**[33:43] Speaker 2**

Etc. And how much would you say the accuracy is? Is is there? Like, how much do you trust the data right now? Is there a way to verify it?

**[33:53] Speaker 4**

Is is I trust the data as much as the data like. The data issue, let's just say, is not with AI; it's with internal, and we're fixing it. Like the data issue is caused by humans. It's like people not keying in the right thing when they talk to somebody. Whatever we're integrating an AI calling agent and call center that should cut most of that out. So that all the data integrity would be totally self-inflicted, as opposed to like.

**[34:27] Speaker 4**

Something to do with you found.

**[34:28] Speaker 2**

You found one already. The the guys who provide the AI calls. Ah, yeah, I know a couple. Also, if you need recommendations, I could look them up. It's called Unity.

**[34:40] Speaker 4**

Um, they do it. They have a specific mobile home parks. Ah, business AI voice agents for real estate. Sounds so. It's ah. They integrate with their rent manager system via API. Like it's basically need for it. And the major operators in the space use it, so we're we're kind of locked into using them.

**[35:08] Speaker 2**

No, that's for sure. That's for sure. Because I personally value those kind of products that niche down. They know you know exactly the the industry they're tackling, and they're doing it except exactly for for for for them for you. Everything's perfect. Okay, and they'll be. Also providing an API with the reports of each call, so that's another data source as well. Okay, let's not touch the CRM for now, right? Because since it's dynamic and is be is changing, like as I said in the beginning of the call, just let's take tackle one one element of your dashboard, right? And I just wanted to show you how it could look when it's published live on a website that is not.

**[35:50] Speaker 2**

Right, my job here is to save you from the govt bill, in the end of the month, right? And also, my personal interest is is like I I don't want to charge you know per hour or something. I want to help you cut costs, right? And I want to make money, by you know evaluating this percentage of how much I was able to cut costs, right? So it's like all you know result result driven, and things like that. We can we can discuss this later. It's not the main thing now. Right, but for instance, listings and data that's more defined, right? And the more, more, more — it's not static, right? But still, I think.

**[36:29] Speaker 4**

This thing's been running for 60 days. It's pretty. It's doing its job right now, absent some improvements that could be made to it.

**[36:40] Speaker 2**

I don't think it needs improvements. I think it needs to be.

**[36:44] Speaker 4**

I don't need improvements. Additions to it.

**[36:49] Speaker 2**

Optimization is key, right? Taking it out of co-work and publishing it on your own domain. Again, just details. Like I can do it on a temporal thing, and just show you how much cheaper it can work with all the analytics in place and crawling, and maybe even scouting for new websites automatically, like offering you guys to like expand and share your listings elsewhere. I don't know. It's, Posting them on Facebook groups, maybe that way.

**[37:19] Speaker 3**

That is a place where we do post them and separate, and it is not as easy to track. So if there's a way to do that as well, absolutely.

**[37:28] Speaker 2**

Meta API is a bitch. It's tough, but it's possible. Things like that. Like I'm not trying to reinvent it here. Just optimize it, and then once it's optimized, you get room for expansion. Because if you keep complicating it and adding things, it can get so bulky.

**[37:51] Speaker 4**

Yeah, like I was gonna add, for example, so there's two things that I was gonna add. In near term, one, I was gonna do a further scrape of of Realtor. com, which apparently has all our listings. But then we also feed all this data into a website called My State MLS. My state MLS is like the gate for regular real estate listings websites, so Realtor. dot com, Zillow, Trulia, like all those different websites, it runs out of our data, which is in my state MLS. So our data takes a hop from rent manager to my state MLS, and then from my state MLS takes a hop into the websites. So there's actually an extra step there versus the two on here, which just goes straight to our website and straight to Image Village.

**[38:43] Speaker 4**

So that's a secondary audit I haven't built yet. I'm not even sure how to. I may have to have it look to my state MLS with our login to go in and see it, or I can scrape the end websites too. I'm not sure, but like that's an example of a.

**[39:01] Speaker 2**

But it's a multi - funnel, right? You cannot divert and not use my state MLS and submit straight to the website,

**[39:08] Speaker 4**

Right? You have to use my state MLS here.

**[39:11] Speaker 2**

It's licensing and things like that, right? It probably yeah. Yeah, I'm looking at it right now. So you basically you never go directly to those websites.

**[39:21] Speaker 4**

You only never go directly to the normal because here's the thing. I mean, I'm guessing it has something to do with the nature of mobile homes. Like we don't, we're not actually selling the real estate. We're selling the the vehicle. The vehicle. Yeah, the vehicle on the real estate. Right.

**[39:42] Speaker 4**

So it has to go through my state MLS to hop over and hit the other, the main real estate websites.

**[39:48] Speaker 2**

But not all your listings are mobile homes, correct? Like you, you have properties that are. Yeah,

**[39:54] Speaker 1**

They're all mobile. Yeah.

**[39:55] Speaker 2**

Oh, okay, okay, hundred percent of them. Okay, that was also an important thing to clarify. Okay. Um. I see. I see. The the the the the website looks like it will be not that easy to. To automate things with, it's a bit legacy, right? But so you log in, and someone manually does the the addition of the listing, right? The submission, right? Currently, my listings. Sorry, sorry,

**[40:28] Speaker 3**

I don't know how it's manually done, or if it's done by uploads or something like that. Not a hundred percent sure.

**[40:35] Speaker 2**

But you have an employee that does it on a daily basis? Yes. Because that pretty much is the main point of the funnel, right? All the discrepancies, all the other things, they potentially come from this very moment, of my listing submission, right? Because I was sure that you're going on a bunch of websites. You have an account everywhere, and you're

**[41:04] Speaker 4**

It's all it's all automated. I think.

**[41:08] Speaker 2**

Is it possible to talk to that guy? Like, if you guys want me to to to help you with this, and we proceed, right? Would it be okay if I,

**[41:16] Speaker 3**

You know, yeah, absolutely. Anybody will anybody will be at your disposal.

**[41:20] Speaker 2**

Uh huh. And all of them are in your office. Like, it's more often because you mentioned that some some teams are more like offshore, right? Outsource.

**[41:34] Speaker 4**

All of these people are U. S. based. Yeah. It might be like remote in different areas, but all, all, all the space.

**[41:44] Speaker 2**

Mm - hmm. So you acquire new homes weekly, right? New or.

**[41:50] Speaker 4**

Sure. There's a big pro. There's a big process to it. We have to like, that's a whole separate thing where we we order the homes, they get delivered, they get installed. There's a long like hundred hundred day process or a hundred and twenty day process before. For something is listed, and I've ah got trackers built for all that shit too.

**[42:15] Speaker 2**

Yeah, better because if if something goes south on the way, then you know it was money, right? But by the time that it's prepared, like I say on the day hundred twenty one, you get a listing preamble like ah you know the description of the home, photographs. The name. I can tell the whole process for that. But you have a templated solution, right? By the time that it's done, right, there is a template that gets filled up, and it becomes your listing. Correct.

**[42:49] Speaker 4**

Or correct. So I don't know what forum that template is in, but I built a big listing audit recently that we're going through. They're fixing a bunch of shit that was wrong in our listings. Um. And on the back end of it, I'm gonna create them a listings generator, which makes sure that shit doesn't happen like this again.

**[43:10] Speaker 2**

I see, I see. Yeah, that that that is where AI could be useful for verification, right? Like,

**[43:18] Speaker 4**

If which is exactly what this is doing. Like, if you look here, it went through every single detail of every listing, looked at the listing on the website, checked it versus our system, checked the general format that we tried to use. And then found the fixes, said the fixes, suggested the the rewriting of the description to match. And so, what I'm going to do once they get the system fixed now is I'll create a listings generator. Some this again, this could live on the website where it would be a thing where they could put in, or this would live in. We're building out a forms system internally. That.

**[44:00] Speaker 4**

Gets people out of emails where it would be able to look to that and basically create the input based on seven other different reports that we've created that have all the detail on the community, all the detail on the area, all the detail on the home. Like that's kind of the information that it can all pull together. There's no reason why every single listing shouldn't be written by AI. In the same cottage, but the house has no errors.

**[44:27] Speaker 2**

Mhm, mhm. I think that's where. Like I keep discovering, like as we speak, like those super central nodes, right, where where a lot of these discrepancies can originate, and I think tackling them first is even more important than you know calibrating the final listing, right? Because if you eliminate the original potential for discrepancy, then then you don't have to run poor Claude to to go to check every website, right? Like you have way more errors, way less. Sorry, the margin of errors will be way less.

**[44:58] Speaker 2**

Yeah, maybe we could tackle this final listing template together and build like a tiny app, where you upload non-normalized data, like whatever crap those people have. Because I assume that even after 120 days of preparations, right, there are still different operators, different employees, doing different things. The human error will be always there, but it can never leave this node without being, you know, perfectly templated, uh, perfectly described with your ton of voice because. It even matters for search engine optimization. I, I, I'm sure. Right, the way you describe your home, if it's some AI written, or too shitty written by a human, it's gonna damage the potential conversion rate, right? In marketing efforts. So we could tackle that first, and then see, you know, like as I promised in the beginning, let's pick something super niche, super tiny, make it.

**[45:55] Speaker 2**

As efficient as it gets, make it perfect, right? Have its own website, have its own uploads, have its own communication system, and then scale from there. Because, right? Like, if I prove to you that that thing can work, it can be your own IP, you know, belonging to you, also without me touching much corporate data, right? Because, like, I also see you guys won't really, you know, make me go through a huge compliance process. I hope so, because I tried to work with I don't know hedge funds in New York and. Corporate entities that like just such a bitch way. I would just rather not to like. I'm not a business analyst from McKinsey. You know, I don't. I don't work with reports and compliance audits and things like that. But as a maker, as a builder, like I would really happily show you a blueprint for a mini app that solves like a super important node in your business, saves you tokens, because it will run basically for free, right? But yeah, normalizes the data.

**[46:53] Speaker 2**

I say it's the biggest pain point here: discrepancies, mapping, normalization. You get input from multiple sources, it gets confused, gets lost somehow. We can fix that at the origin.

**[47:10] Speaker 4**

Yes, and we did actually. So, what's kind of funny? It's it's kind of cool. It makes me feel good. Almost everything you're asking, we've done some aspect of it. With the best knowledge that we've had, so in the beginning of all of this, there was a shitload of data in that asset listing in our system that wasn't let's just say wasn't like super scrubbed. So we went through a whole giant data audit to get everything right, number one. But then to also get everything, and maybe I'm just going to show you this too because this will give you a sense of how I'm running Claude, which is.

**[47:50] Speaker 4**

So like, this is a disaster, and it's just an acid. Like so, I have every single co work project running out of this folder, and I have every folder organized by department, right? So nice. Uh, so corporate has access to the entire folder, so it can look across departments, and some other departments have access to other departments that they intertwine with. But like. You know, if I were to look at this, like we went through and built this whole, and the data issues were happening at the entry of the home, right? So, here we go. So we did. So sales and marketing,

**[48:39] Speaker 2**

But is the entry coming from sales as well?

**[48:42] Speaker 4**

Sales and marketing is in charge of buying the home.

**[48:45] Speaker 2**

Ah, okay.

**[48:47] Speaker 4**

So like we created this whole thing of putting the data into the system right from the very beginning, which got a lot of the data correct in there from the very start on these helps. So like item by item, line by column by column in that asset listing.

**[49:06] Speaker 3**

So just to give you a caveat on that, so like this is something that we noticed was a big you know sticking point. So now we're using. You know, one of the big things we're trying to push through is forms across the entire company. No one to send emails anymore. None of this, like Teams messages. If everybody just fills out the form by doing their job, everybody else will get notified cross department. Things like that. So we are we're starting to roll out QuickBase with FastFields form. And QuickBase is kind of like a I don't even know how to explain it anymore. But you know, automations. You know.

**[49:44] Speaker 3**

Rule base, so things.

**[49:45] Speaker 1**

Okay,

**[49:46] Speaker 3**

So things like this, you know, ideally the person ordering the form, ordering the home, would enter enter everything into a form that would go into QuickBase. It would notify everybody else, and at the end of each day, because it's not a direct link, but at the end of each day, anything that goes through QuickBase would basically send out a CSV export in the form of an import file that we can put into Rent Manager. And update all this information. So, if new homes were ordered, instead of Claw doing it, Quickbase would do it. But this really the template that we are using to build out Quickbase, if that makes sense. And I can send you like the working papers that we've sent them. This process here has been such a big one for us and a headache that we're actually going straight into it with Quickbase and having making sure that they can build it out because this the big solution we need. Where.

**[50:41] Speaker 3**

You know, all of this flows through. All of this is tracked. We're not manually doing it. You know, the works. Where I think this, you know, again, Quickbase should take this over. But we are using what John has built here as the template of what happened.

**[50:58] Speaker 2**

I see. I see. So what I was just considering that you guys might want is this, like, upload the interface and things like that. That's then taken by Quickbase already by the Fastfields forum. That is not really needed.

**[51:11] Speaker 4**

It Cuts out the human error and the human entry error, and it has timestamps. It it cleanses the data even more from the very start across every process. Which then it's great, but then we snapshot into the data warehouse, which then we have daily, which then we can run whatever the fuck we want on it. There is the goal.

**[51:34] Speaker 2**

So, so then. But you will also rely on QuickBase with more than just listing submissions. Right. All internal communication.

**[51:40] Speaker 3**

We are we we are rolling it out. It's not there yet. Like we're not relying on it for anything yet. But we have. First project is this one. Ideally, every form from inspections to move in, move outs, lease generation, a lot of things that rent manager was hard to use for people. That this will basically do it to cut out the error. So if, Somebody fills out a move - in form. They're also getting the lease, and they're getting asked the questions for that specific community's lease, so it can be justified and verified before the lease goes out and gets signed. Versus them putting the wrong amount in the field or something like that,

**[52:20] Speaker 1**

And then we're stuck with it. Uh huh.

**[52:24] Speaker 4**

Yes, sir. So then, so and and so maybe just taking two steps back or two two steps up for a second. What I see is potentially being very helpful. Like, I think I'm pretty good at building. Yeah, yeah, that's for sure. I think it's building, like based, like through the system with Claude. That's fine. Um, the uh, the major I would say roadblocks, hurdles, whatever that I see are just like Austin talked about on the front end.

**[53:03] Speaker 4**

The data entry, which I think we're like slowly fixing, and we have solutions that are being implemented, whether it be the AI calling automation stuff or the the fast fields form stuff. And the other thing that I truly have no fucking clue about is how to get this shit. Like I build this, the whole like efficiency of connecting it all together to run live. To have that AI reasoning layer built in, because a lot of the stuff, like I don't want to, I don't want to get a raw numbers dashboard and have to think about what the conclusions are or what the to-dos are. Having AI do it and get it ninety percent right, and having our employees say, "Oh no, this is already correct," is a way better option than me having to think about it. We got too much other shit to do.

**[53:58] Speaker 4**

So get it. So having it published live with an AI reasoning layer, and then the third big thing, which we did talk about when we first spoke, was like, you see my workflow here? It's a fucking disaster. I'm living, I'm living in this little side area on legitimately every single project I'm working on, whether it's some of the things I showed you, or whether it's like. Like I had it scrape all our board decks, Austin, last night, and start to build a format out so that I can totally have it build it in HTML to push to PDF, which is amazing, and it got it fucking nailed it. Whether it's like legal documents where I'm basically doing an attorney's job for them, telling them going going through like.

**[54:53] Speaker 4**

A bunch of legal docs that we got, and putting together a full memo that I'm reading, that I'm like vetting, and making sure that it's telling the right, like that it's getting the info correct. Like there's one-off deep analysis we're doing, whether it's going in and looking at a fucking single property and issues that we have, and and helping us frame in an organized fashion how to fix it. Right? Like there's so much stuff that's.

**[55:23] Speaker 4**

Running out of this, whether it's let's see, putting into different on web,

**[55:31] Speaker 2**

It's still your workspace, and I think it should remain your workspace. I think it's really well organized. I think there's nothing wrong with being,

**[55:39] Speaker 4**

But I'm, but I'm, I'm not a model agnostic. That's the only thing. That's for sure.

**[55:45] Speaker 2**

Yeah. That that that's like I'm addicted to what called myself to. In a sense, that like moving all these chats out to to somewhere else, I think it was a lot of context.

**[55:59] Speaker 4**

But it's daunting. It's daunting. Like I can't imagine doing that.

**[56:03] Speaker 2**

Yeah, but slowly migrating the things that because I consider this your scratch pad, your your workspace, right? Like yeah, thing that doesn't have to be final, perfect. It's not. It's not the production level thing, right? For instance, you used it to build the dashboard. We're taking the dashboard out of it. Right, right. Touch.

**[56:22] Speaker 4**

That aspect of it.

**[56:23] Speaker 2**

It's also all lives in this. That's the issue. Yeah, and then let's just take those things out first, right? Like I cannot promise you that immediately we'll be able to have a new UI for all the legal things separate, right? It's possible, but you know, it's not the most pressing thing. This thing works, right? And. Like the moment that it's gonna start, stop wasting tokens on scraping websites, building interfaces, and things like that. You you might even fit in your two hundred dollar plan, right? The the club.

**[56:55] Speaker 4**

It doesn't even have to fit in a two hundred dollar plan. Like, just can't fit into a twenty five thousand dollar. Yeah,

**[57:02] Speaker 2**

Exactly. But if you're daily using documents and you know memos and things like that, is definitely not gonna consume as much tokens. Like I. The thing is that I cannot see the exact usage, and it will never show us the breakdown on what exactly it used it for, right? And I'm sorry, I cannot promise you the the audit of what exactly consumed the most. Anthropic is just not gonna show it. I'm pretty sure. So because you're not using APIs, separate API keys for separate tasks, right? There is a thing called Anthropic Console that you can see that.

**[57:35] Speaker 4**

So I can tell you. Not interrupt you again. I went through and did a big deep dive on this. Uh huh. Uh, and looked at this, which is when it spiked, based on uh effectively dollars spent a day. Mm hmm. It really did coincide. I was doing a lot of fucked up shit. I wasn't. I wasn't running on lower tier models. I had everything running on Fable at the exact time.

**[58:10] Speaker 4**

That Fable took away its free credits and price increases from my usage, and then I learned a whole lot about like how to. Oh, it's not even here. Like basically tearing down models where needed. So I have all these skills built into my cloud now, where it's going to tell me when my con it tells me when my context window fills up, so I switch into a new chat. I have an AI model selector skill, so when I tell it to do something, it tells me if I should tear down. Like I have a discussion at the beginning of any any bigger project with Claude about what model to use, and it's drastically cut it down, like drastically. So I think my usage and everything should come in line within the next month, even using it to the extent I'm using it.

**[59:02] Speaker 4**

In a big way, and doing some of the stuff like taking it out once something's built. Well, Desbird's built only.

**[59:08] Speaker 2**

Desbird's beautiful already. You can share it with me. I can show you how it can be running on your own server with like representing data, and from there on, the crawling, right, and the analytics of the website listings will be also an independent process, right? And we just branch them out, you know. Prune them out of your your workshop, basically the co work workshop, into independent existence, right?

**[59:41] Speaker 4**

And so, right. So the other thing I have, and I built, is I do have one crawler. It scrapes MH Village every single night, goes across all six thousand listings on their website in in our states, and it pulls all the data from them down. I built that in code. And it runs out of command prompt, so I. It seems to be working efficiently, but I've only, as you can see by the usage of my Claude code side, like I don't do much in code. I do it all in chat and cowork. But I have built, I did build one scraper that seems to be working out of code.

**[60:27] Speaker 2**

Yeah, it's mostly running locally on your computer. It could be also running on the servers. It's running, but they also independent of you having your MacBook or stationary PC.

**[60:39] Speaker 4**

It has to be open and running.

**[60:42] Speaker 2**

Yeah, and it costs five bucks to to run a server. So I keep repeating that. I think you you should do that. Yeah, I can.

**[60:52] Speaker 2**

Yeah, I think. But still, I think we we need to pinpoint the the exact solution. Since you're moving with the fast field, should we try the the form submission as an independent, like less bulky solution, or do you think it makes no sense? Austin, probably you already are with in the conversation, right there. Yeah, we don't have a contract with them.

**[61:15] Speaker 3**

I think it's probably so far. I wouldn't want to pull it off of that. At least now, I think there's. So much other stuff that we could build out and and and kind of get for really John help John and I versus helping the team.

**[61:30] Speaker 2**

Yeah, it's it's about what you're building for your internal usage. Yeah, even the dashboard that will put life. At first, it should not be shared with anyone. But then, would would be possible? Is like I did it by myself for my own business, for like without using any external CRMs or anything like that. And the permissions, just like you give logs to a marketer, he can only see the product data, right? And and some CRM data. You have customer support that only can control the accesses to to products on the website, like things like that, right? Like tiers, permissions. It's all really doable, and it's all part of your own you know business intelligence, rather than right.

**[62:18] Speaker 2**

I think it's good to keep something like that flexible, without committing to one rigid system, right? Because you see how much it evolves, how many ideas you have. So that's just where I want to come in and help you offload it from the UI of Cloud, right? And not sharing it with Cloud links. It's a simple task, quick, and not saying that it's something groundbreaking. No, just making more independent in these terms, and also yeah, be able to plug in other models for those tasks. Like keep Cloud for building. Like I most probably will use Cloud. For for building that solution as well, right? But it doesn't mean that it should run on cloud, right? That's my whole approach here. Yes. Have you heard of the the Chinese model, the GLM 5.2? That it was released as a stealth, like a cognitive thing. No one knew what it was because it was supposed to be better. Better. Well, it's supposed to be 40 times cheaper per token.

**[63:14] Speaker 2**

On the level of Opus 4.8, and well, there are there are many breakthroughs going on. Like I'm I'm on Twitter all the time because of the nature of my my business, the social media stuff, and and it's every it's not even every week anymore. It's it's every day, another crazy thing that comes out. I don't know where are we all going. You shouldn't even try to to keep up. I think, and also don't let you distract. Don't let this distract you from what you have already built. Like it's it's never going to be like a perfect AI that just get released that will solve all your issues. It's not true. It's just using things like OpenRouter or there is a thing called Token Router, right? Just for optimizing the the costs. That's it. Like it will by itself fall back to the model that like if one of them is down, which happens, right?

**[64:11] Speaker 2**

It will fall back to another one. If one of them is too expensive, you can set it to you know to use another open source one, and things like that. And I will take care of it. I will prepare like a proposal. Like this, right? And I will be focusing on this listings monitoring part of your dashboard, like just the first step.

**[64:30] Speaker 4**

Just the first one I showed you.

**[64:32] Speaker 2**

Yeah, makes sense, no? Like it's like we're starting step by step. Yeah, I will prepare a set of questions with the listings websites because I only the Image Village and my my state MLS are the only ones I I noted. But I'm sure there are more that you want to be monitoring, right? And yeah, and I could help you also refine the this final listing template, right? Because I use some code skills and other solutions, and I work a lot with search engine optimization. We could.

**[65:06] Speaker 2**

Actually, like fine-tune the descriptions that you guys are generating. You know, the final output of them, so that they're good for actually for AI to be discoverable. Right? If I'm chatting with ChatGPT about a mobile home and in the states that you're active in, like that, it could potentially even suggest. It will actually suggest with very high probability because you guys are listed on websites with high domain authority, right? With high traffic. Like it's not about the AI optimization of your website. It's it's just so that from those websites, your listing ranks higher, which is easier to do. And I think you can beat your competitors with a good AI, you know, text generation solution, right? And I'll prepare the questions. I'll just use email, right? Like instead of WhatsApp, because generally don't use notifications, right? So.

**[66:03] Speaker 2**

I think emailing is is faster. I assume you have so much in your inbox anyway. Okay,

**[66:11] Speaker 4**

And what I suggest is using DrawWait. Is it helpful if I send you the listings dashboard so you can see?

**[66:20] Speaker 2**

Yeah, yeah, the plot one. It will be my main. Let's say I don't want to call it raw material because it's not raw. Like it's actually a functional thing. Is is something I will be building, rebuilding. The same thing, but on a server, and I will send you guys maybe directly here in the in the chat. I think I would suggest that you start on your company account, as because don't look at it as like a major business infrastructure thing. Like just let it be our playground, right? Like you don't have to commit. Like maybe you don't like what I built. Like we just scrape it, right? But it will cost you five dollars to start the server on Railway.

**[67:00] Speaker 2**

It's dirt cheap and it's super easy to set up.

**[67:04] Speaker 3**

I think I went and signed up after the last time we were talking. So I'll make sure, and if so, we'll we'll get you a login for it.

**[67:10] Speaker 2**

Yeah, you can just invite my email there, create the project, and nothing, do nothing. Like I'll deploy everything there, and you will have full ownership. You know, full. Like I could have done it on mine, but I don't think it makes sense to to transfer it after. It should be done on yours from the beginning, right? And. And we take a look at the MVP, and then we can decide if we want to go further from there. You could cover some of the costs, or we can discuss. Yeah, like I want to show you something of value, and then you tell me like you know how much you would rather pay for it, right? Because I I cannot tell you like I don't want to work hourly and report hours. Like I want to help you save money, and then we see.

**[67:58] Speaker 2**

If it works and if I like, what's my cut, basically? Okay. On this on this business, yes. Because it might not be useful. Like then I I don't think I I should be charging. Okay,

**[68:12] Speaker 4**

Is perfect. So I'm going to send you a copy of the listings dashboard. I'm also going to send you a copy of that listings audit.

**[68:19] Speaker 2**

Yeah, yeah, yeah. And the original listing, the the the input thing that you consider your template. But I will follow up right now. Do we have also a recording of this, please? That would be very helpful if it's shared with me as well. Yep. I will include the transcript and summary of it. Thank you so much. Thank you. Okay, you guys have a good week. I just have a call already fifteen minutes late with my biller.

**[68:50] Speaker 3**

We'll get all this over.

**[68:53] Speaker 2**

Thank you, thank you. It was a great talk. I think today we were very hands down, and I understand the issue, and I think you did an amazing job, honestly. So solving it, like you, you don't have like I don't know, like a senior, be a business analyst would be charging a lot of money for doing that project. They might not be much more, let's say, refined, but come on, and it's a, I have friends doing that, and I still consider it a bullshit job. You know, the big, the big four consultancy on making reports and and and things like that. I think it should die, especially with AI. Oh, I think so. Yeah. No. Anyway. Awesome.

**[69:37] Speaker 4**

Awesome. As soon as this, as soon as the transcripts done, I'll attach it to this with the listing stuff, and I'll put and it'll be ready.

**[69:43] Speaker 2**

And I'll just follow up with more questions, and then.

**[69:48] Speaker 2**

Don't let me access the railway. That's that's easy.

**[69:51] Speaker 3**

Yeah, and we'll get the pro account to be able to invite and everything.

**[69:54] Speaker 2**

Yeah, perfect. Thank you. Thank you. Have a good day. All right, bye. Thanks,

**[69:59] Speaker 1**

Robert.
