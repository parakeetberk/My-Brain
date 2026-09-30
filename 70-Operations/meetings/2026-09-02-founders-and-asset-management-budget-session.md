---
type: meeting
tags: [type/meeting, dept/finance, dept/asset-management, status/filed]
---

# 2026-09-02, founders and asset management, 09:21 ET

**What this is:** the Wednesday morning founders block with Zach and the analyst team, 38 minutes, filed 2026-09-02 from Plaud recording `852d56987176924d4746003f887fb58b`. **No AI title and no AI notes existed on this recording**, so this note is built from the raw transcript read in full rather than from a summary.

**Attribution caveat.** Plaud diarised five speakers and named none. Attribution below is by role and content, and **where a name is uncertain it is marked so.** Several proper nouns are unreliable in the raw text: *"Eastill" / "East Hill" / "Easton"* is almost certainly **Eastdil**, and *"Stewie" / "Stu"* is the analyst working the model. **Neither is asserted as fact.**

---

## The 2027 budget model, and it is the substance of the call

Zach walked the build. It is an Excel model with the formulas driven by Claude and code, rendered to an HTML dashboard so everyone can review on their own screen.

- **Shape:** organised by market, then property within market. Filters for regionals, markets and portfolios. **Regionals is the one they settled on** as the primary cut, so a regional can be sent their own slice and add input.
- **P&L ties to the actual GLs**, above and below the line. Separate infill tab that summarises the asset summary. Occupancy over time from January 2025 to December 2027 on an annual basis, plus ready spaces.
- **Infill is driven off Leslie's planned order sheet.** The order cadence drives occupancy; timelines come from agreed-upon timelines with the field based on what they have been and what they should be; **the sale timeline is 90 days.**
- **The design decision worth keeping.** The final version carries **no manual per-unit overrides.** Instead a **cap input per community per month** of homes sold: set Applegate at three a month and everything staged and ready gets absorbed at three a month until the plan is hit. Possibly driven off occupancy percentage rather than home count so it scales with community size, a 400-site community maybe eight a month against a 100-site community at two. Jon's reason: **"manual inputs by unit is what caused a lot of the pain last time,"** and the goal is **"not to be a hundred percent exact, but to have it roll in on a reasonable, defensible basis."** Austin's position is stronger, that the final should be entirely formulaic with no room for tweaking.
- **The HTML cannot save state**, so an override would be purely visual. The plan is to keep the source files in one place and have the dashboard pull off them, so a refresh reflects the change.
- **Cash flow is the layer after the properties.** Property-level items get pushed down where they can be; corporate-level capital events layer on top in a portfolio cash flows page, with escrows and the unplanned capex reserve pulled in. **The point of it is a live cash position**, so the question *"which capex project do we adjust"* has an answer in real time.
- **JREF I gets its own module**, pulling the cash flows, running the IRR and producing a price. **Not for distribution** - a back-of-envelope of what they are tracking to, to maximise price and achievability together. The reason is timing: **"if we're going to be under contract with someone in Jan, Feb, March."**
- **Applegate was built first**, with the analyst, the night before. **Thursday night 2026-09-03 is the session to finalise the mechanics and the template**, proven out by replicating it for Whispering Pines. After that it is replication.

**The distribution date is stated two ways in the same conversation and neither is unambiguous.** *"If we do get everything out by next Friday, that should give them plenty of time to review, they have two full days"* plus the weekend, and later *"if we're aiming to try to finalize and distribute by Friday."* **From a Wednesday, "next Friday" reads as 2026-09-11 and "Friday" as 2026-09-04**, and the two-full-days-plus-weekend arithmetic fits neither cleanly. Recorded as ambiguous rather than picked. `TD-0437`.

**What the budget review itself will cover**, per Jon: expenses are expenses across the properties at this point, infill comes straight off the order sheets which is Leslie's, then rent increases, then capex, with John Clark working on capex intel and managers having views. He expects the property reviews to be straightforward.

## Two gaps in how the money is booked, and one of them may be revenue

**Leslie asked how to think about marketing and sales-organisation expenses in her budget, and nobody on the call knew how those are booked.** Jon's words: *"I don't know how that stuff is getting booked. I'm guessing it's all going to Opco"* - flyers, flags, the state MLS subscription. He wants it broken out because **it flexes up and down with sales activity**, so the Opco run-rate burn should be readable with and without it. The frame they already use is **roughly a $5,000 internal budget per home to get it sold.** Leslie to be asked to inventory it; side conversation with her next week. `TD-0438`, `TD-0439`.

**The one that is not just presentation: the admin fee on closings.** Austin asked whether the company charges an admin fee on every home closing. Jon: *"Are we? I don't know. I think we are. We budgeted to have an amount, but I don't know how any of that is being done."* And on the wider point, **nobody could say where gains and losses on home sales are landing** - *"it's all one bucket."* Also raised: an on-site sales and leasing person will push payroll over on overage, and if they are sales and leasing **they arguably book to the dealership rather than to Opco.** `KP-0057`, `TD-0440`.

**They also want a proper Opco review** covering non-payroll office expenses that are department responsibilities, and a proper look at payroll overage. Jon: **"we've ramped a lot up without really analysing the impact."** The Opco piece was renamed on the call from a future review to an **Opco 2027 budget on the same cadence as everything else.** One mechanical complaint recorded without figures: the current model nets rather than showing the build, **"all he does is net it, and there's no way to track back to understand it"**, and it was pulled from the GL rather than the payroll model.

## The recap banker, Eastdil against Newmark

Live and undecided, and the useful part is that the comparison is not like for like.

- **Eastdil has not actually pitched.** They provided a BOV and no presentation on how they would sell it, who to, or who the recap partners are. **They will not do the deep presentation without an engagement.** The conversations have been with the execution person rather than the relationship principal.
- **Newmark presented and was convincing**, naming large capital relationships.
- **The real distinction: Newmark is more connected to the non-MH buyer trying to get into MH, who may pay more; Eastdil is more tied into MH and operator circles.** So Newmark carries the possibility of an unknown moonshot bid and Eastdil carries the ability to sell the story to people who already understand the asset class.
- **It is a recapitalisation, not a purchase.**
- **Splitting the process across two banks was tried before and went badly.** *"We screwed Dustin by doing that. We didn't pick a horse on Geiger."* The concern is the banks overbidding each other and a muddy process.
- **"In the end, it'll be more Jadian's decision than ours."** So the founders' job is to get Jadian an update on the business plan and the timing, and to get help on the core-plus fee comps.
- **Austin owes Eastdil an update** covering the pushed-out timing, and needs to ask for core-plus fee comps at the same time. **Likely to be handled by Joe.** The relationship is worth keeping on good terms regardless of the outcome. `TD-0441`, `PD-27`.

## Rent comps, and an offer to trade data with competitors

Jon is running a market survey. The analyst consolidated the company's market comps into a single grid so the gaps are visible, then broker blasts go out. **The approach worth noting: he intends to ask other operators - Phillips, Three Pillars, Bedrock and others - to exchange what their rents are today, explicitly not where they are taking them, on a reciprocal basis to enrich both databases.** A handful of one-off Miami owners will need phone calls. **The Duval portfolio already covers Tampa and Orlando**, so most of that market is already held. Target was to get the ball rolling that day and finish by early the following week.

## Shorter items

- **Plaud team account.** The vendor has offered a team account **at the same price**, which would let recordings be bucketed and shared with the team - the August road trip is the example, where every recording could have been shared as one set. **Adoption is uneven and that is the real issue**: one founder does not have the current device, another uses a different recorder and does not want two systems. The desktop app auto-records Teams calls, which is the capability with the most leverage, and there is now a connector plus speaker auto-tagging if people are preloaded. `PD-28`, `TD-0442`.
- **The Uniti dashboard is live and self-updating**, scraping mail and the SAM master chat into Plaud and refreshing the to-do list daily.
- **Lake Wales:** an email went to Gunster the previous night with PZR takeaways. Confidence in the read is low - *"no idea if some of that stuff is correct"* - but better than nothing. Still needs a conversation internally.
- **KPIs are owed to Jon and Zach**, and Austin is to call Jim about them rather than email, because Jim also needs an approval. `TD-0443`.
- **PFFs are still owed to a counterparty who has not chased them** and has said they do not need them. Being done slowly in the background. **The counterparty's name is not clear in the transcript and is not guessed here.**
- **Geiger:** hoping to be under contract that week.
- **Road trip material:** Austin's notes and recordings are loaded and organised by property; Jon still to add his photos and notes, then a report gets generated and circulated.

## Personnel

**One conversation happened and is recorded in one sentence, per [[CLAUDE]] guardrail 7 and rule 9.** The separation discussion with the controller took place, ran long, and both founders considered it to have gone as well as it could have; an update goes to one outside party and a short note to another. **No terms, no figures and no characterisation of any individual are recorded here or anywhere in this Brain**, and the compensation content that came up elsewhere in the same call is likewise not recorded. Sequencing stays as `CM-16` has it.

## Sources

- Plaud recording `852d56987176924d4746003f887fb58b`, 2026-09-02 09:21:55 ET, 38m27s. Raw transcript read in full, 176 utterances. **No AI summary or notes existed on the recording.**
