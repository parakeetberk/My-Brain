# Decision queue and the 479 unowned items

**What this is:** two pieces of work on one board. Job 1 turns the 39 open rows of [[00-Meta/parked-decisions]] into briefs each answerable in a sentence. Job 2 explains why 479 of 1,183 board rows carry no owner and what that says about the shape of the company.

**Status:** built 2026-09-03. Nothing in any register was edited. Everything below is a proposal.

**Sources.** Job 1 reads `C:\Users\AustinBerk\Documents\My Brain\00-Meta\parked-decisions.md` in full. Job 2 reads the prebuilt parse of all 1,183 board rows at `C:\Users\AUSTIN~1\AppData\Local\Temp\claude\C--Users-AustinBerk-Documents-Claude-Code\ce06657f-114b-4631-af3f-1d35a438f537\scratchpad\board.json`, analysed with node rather than read by eye. Supporting reads: `10-Business/departments/accounting-and-finance.md`, `10-Business/people/staff-roster.md`, `00-Meta/austin-operating-manual.md`, `CLAUDE.md`.

**Confidence labels.** VERIFIED means the primary source was read here. SINGLE-SOURCE means it appears in one place with nothing to check it against. INFERRED means it was reasoned from other facts and is stated nowhere.

**Two rules bind this file and are worth stating up front.** No individual's compensation appears anywhere, per CLAUDE.md rule 9. Where a decision turns on a personnel matter, the file says so and moves on, per rule 7; the substance lives only in `10-Business/people/_private-assessments.md`.

**One note on the register itself.** The count is 41 `PD-nn` rows, of which `PD-37` and `PD-38` are in the Resolved table, ruled 2026-09-03. That leaves 39 in the Open tables. VERIFIED, file read in full. Per CLAUDE.md rule 15 no ID below is renumbered and none is reused.

---

## Job 1. The 39 decision briefs

Read in register order. The stakes ranking is the section after this one; the five to answer first are at the top of that ranking.

Each brief carries seven fields. **Blocked** names the people and the register IDs waiting. Where nothing is actually blocked, the brief says so, because that row is a candidate for closing rather than deciding.

---

### `PD-01` Ozzie evaluation

**Question.** Nothing to rule on. Do you want this row off your queue and onto Jon's, with a report back by the 2026-09-30 due date already on it?

**Blocked.** Nothing of yours. The row says **RULED 2026-08-31, owner moved to Jon Wyss**, in your own words: *"This is on Jon's plate as Auzzi is in his office."* The CRM findings surfaced inside the evaluation window (700 stale prospects, 84 miscategorised tours, 7 flow errors) are real work but they belong to the CRM cleanup, not to this decision.

**Options.** Move it to Resolved with the delegation recorded. Keep it open as a tracked delegation with a 09-30 check. Take the call back yourself.

**Recommendation.** Move it to Resolved and open a dated follow-up on Jon, because a decision you have already delegated is a commitment to track and not a decision to make.

**Cost of being wrong.** One missed check-in on a date already set.

**Reversible.** Yes, entirely.

**Staleness.** **Moot as a decision.** Ruled three days ago and the register never moved the row. Personnel matter as to the substance, see the private assessment file.

---

### `PD-02` Controller situation

**Question.** Personnel matter, and the personnel half is not addressed here. The half that is not: do you want a written extraction of what the Controller seat actually holds before the seat empties?

**Blocked.** Accounting leadership continuity, the live intercompany journal-entry negotiation (`99-Archive/2026-08-catchup/berman-journal-entries-thread.md`), and **eleven board rows that still route to that seat**: `KP-0003`, `TD-0005`, `TD-0192`, `TD-0193`, `TD-0194`, `TD-0205`, `TD-0372`, `TD-0461`, `PF-0015`, `PF-0024`, `PF-0030`. VERIFIED from board.json.

**Options.** Commission the function extraction now and keep the personnel track separate. Do both in one conversation. Wait until a transition date is fixed.

**Recommendation.** Commission the extraction now, because those eleven rows go dark the day the seat empties whatever the personnel track does, and `10-Business/people/_private-berman-function-extraction.md` already exists as the place to put it.

**Cost of being wrong.** A few hours of writing time if the transition never happens.

**Reversible.** The extraction is. The personnel track is not, and it is out of scope here.

**Staleness.** **Overtaken.** The register itself now describes the seat as in transition (`PD-24`, citing `00-Meta/commitments` item 16). The row as written asks whether to act; that question has moved past it.

---

### `PD-03` Who owns accounting, and in what order

**Question.** Do you fix the accounting function by naming a person first, or by buying a platform first?

**Blocked.** `PD-05` Rellit is explicitly gated on this. So is `PD-24` rehab program ownership, which names the Controller seat as the money side. So is the 30-to-45-day close lag, `KP-0003`, one of the three problems you named yourself. Waiting: you, Moe Mehmood, Derek Flynn, the seven offshore accountants named in `10-Business/departments/accounting-and-finance.md`, and Jon on anything that reaches a lender or an LP.

**Options.** Name the seat first and let whoever fills it choose the platform. Buy the platform first and hire into a defined system. Neither, and run the function on the existing team under a named interim.

**Recommendation.** Name the seat first, because the source's own line is that buying a platform under the current department *"just automates the mess"*, and a platform chosen by someone who will not live with it is the choice most likely to be reversed.

**Cost of being wrong.** Wrong sequencing costs a hiring cycle, call it a quarter, on a function already 30 to 45 days behind.

**Reversible.** The sequencing is reversible. The hire is slow to reverse.

**Staleness.** Live and getting more urgent. The Controller departure turns this from a strategy question into a coverage question.

---

### `PD-04` MAV MCP or warehouse only

**Question.** Does the RentViewer warehouse become the single source of truth, making the MAV MCP work redundant, or does MAV MCP continue?

**Blocked.** Continued spend on a system that may be abandoned, against a five-week runway to October snowbird season. Jon Wyss holds the stated position: *"warehouse-first may make the MAV MCP redundant."* See `10-Business/systems-architecture.md`.

**Options.** Warehouse only, stop MAV MCP now. Keep both through snowbird season and decide in November. Continue MAV MCP and make the warehouse reporting only.

**Recommendation.** Warehouse only, because Jon holds the position, nothing in the register argues the other side, and an unargued position that keeps costing money is a decision already made informally.

**Cost of being wrong.** Rebuilding a CRM integration inside a peak-season window.

**Reversible.** Partly. Stopping is cheap; restarting inside the runway is not.

**Staleness.** The five-week runway was stated as of 2026-08-26, so it has about one week left. That converts this from a strategy call into a deadline.

---

### `PD-05` Rellit adoption

**Question.** Do you proceed past the CPA-led technical demo with Rellit, or park it until the accounting seat is settled?

**Blocked.** Nothing operational. You offered to introduce Rellit to Rent Manager's API team and that has not happened. The row's own text ties it directly to `PD-03`.

**Options.** Proceed to demo now. Park it and tell Rellit why. Decline outright.

**Recommendation.** Park it and say so to Rellit, because this row cannot be answered before `PD-03` and a vendor left in silence is a relationship being spent for nothing.

**Cost of being wrong.** A few weeks of vendor goodwill.

**Reversible.** Yes.

**Staleness.** **Candidate for closing rather than deciding.** It is a dependent of `PD-03` with no independent content. Folding it into `PD-03` as a sub-question takes a row off the queue.

---

### `PD-06` Corner IQ trial

**Question.** Nothing to rule on. Do you want the drafted decline email to Zayv sent today?

**Blocked.** `TD-0015`. Zayv and Luke are waiting on an answer taken on 2026-08-31 that has not left the building. The draft is on the row's comment thread in your own words: *"We're not moving forward at the moment. It isn't the product. It's us. Our own processes aren't settled enough right now for me to evaluate what you've built fairly."*

**Options.** Send as written. Send with a date attached for revisiting. Leave it.

**Recommendation.** Send as written, because the reasoning is honest and the only thing between the decision and the vendor is a send.

**Cost of being wrong.** None material. The positioning is deliberately non-final.

**Reversible.** Yes.

**Staleness.** **Moot as a decision, taken 2026-08-31.** It is a task sitting in a decision register, three days old. Note the guardrail: outbound mail does not leave these sessions, so this needs you or someone with send rights.

---

### `PD-07` Referral fees to outside managers

**Question.** May Parakeet pay a referral fee to managers of other communities for sending prospects, yes or no, as a standing policy?

**Blocked.** Vicky's grassroots marketing plan at River Oaks, which is otherwise ready to execute. Waiting: Vicky, and Natalie Magurne as the operations line above her.

**Options.** Yes, with a written cap and a disclosure line. No, referrals stay unpaid and goodwill-based. Yes but resident referrals only, never outside managers.

**Recommendation.** Yes with a written cap, because the row frames this as ethics rather than law, and an ethics question is answered by writing the rule down rather than leaving each manager to guess it.

**Cost of being wrong.** Reputational with peer operators, plus a small uncontrolled spend line if the cap is missing.

**Reversible.** Yes, though a fee already paid cannot be unpaid.

**Staleness.** Live. The plan has been ready to execute since 2026-08-26, so this is 8 days of a marketing plan not running.

---

### `PD-08` Centralised landscaping at Regency I and II

**Question.** Do you bundle mowing and trimming into rent at the Regencies and run one crew, or keep it property by property?

**Blocked.** Nothing is blocked by the decision. What blocks the decision is the landscaping spend pull, and that is the finding: **the row has been waiting on it since 2026-08-26 and nobody has been named to do it.** Waiting: Natalie Magurne, plus the Gulf Breeze and Crystal Acres managers who both asked for lawn care to be included going forward.

**Options.** Bundle into rent portfolio-wide for rental properties. Bundle at the Regencies only, as a pilot. Keep it per property and issue homeowners the trim-it-or-we-remove-it notice alone.

**Recommendation.** Pilot the bundle at the Regencies, because Jon's field report reframes this from an enforcement problem into a service one (landlord negligence plus older owners who physically cannot do the work), and a service problem does not respond to enforcement.

**Cost of being wrong.** One season of landscaping cost at two properties, recoverable at the next rent cycle.

**Reversible.** Slow. Bundling into rent is hard to unwind without a rent decrease.

**Staleness.** Live, blocker unchanged for 8 days. The useful action is not a ruling, it is putting a name on the spend pull.

---

### `PD-09` Regency landlord strategy

**Question.** What is the standing position on third-party landlords at Regency I and II, starting with Larry and his roughly 20 units?

**Blocked.** The broader landlord-relations approach at both Regencies. Waiting: Natalie Magurne and the on-site manager, Charlie Sapp III per `10-Business/people/staff-roster.md`.

**Options.** Buy the units out over time. Impose a landlord addendum with maintenance standards and enforce it. Leave the rents alone and compete on the company's own inventory.

**Recommendation.** Landlord addendum first, because the roster is incomplete (roughly 10 of an estimated 20 to 30 landlords are known) and you cannot buy out or negotiate with a population nobody has counted.

**Cost of being wrong.** A round of landlord friction at two properties.

**Reversible.** Yes.

**Staleness.** Live. The incomplete roster is the same gap it was on 2026-08-26.

---

### `PD-10` FEMA homes at Gulf Breeze

**Question.** Nothing to rule on yet. Do you want a return date on Rose and Natalie bringing back the disposition options?

**Blocked.** Disposition of the FEMA home inventory at Gulf Breeze. Waiting: Rose and Natalie Magurne, delegated 2026-08-31.

**Options.** Set a return date. Take the call now on what you have. Wait for the test permit application to reveal the county's post-hurricane stance.

**Recommendation.** Set a return date, because the delegation is already made and what is missing is a clock, not an answer.

**Cost of being wrong.** Carrying cost on unsellable inventory for another month.

**Reversible.** Yes until a home is scrapped, which is not.

**Staleness.** **Partly moot.** Delegated 2026-08-31 with no date attached. As written it reads as your decision; in substance it is a delegation missing a deadline.

---

### `PD-11` Well relocation at River Oaks

**Question.** Do you fund a feasibility study on relocating the River Oaks well, given it could reclaim 6 to 8 lots?

**Blocked.** The River Oaks site plan and lot capacity. Waiting: John Clark, who is the named owner on the row.

**Options.** Fund the feasibility study now. Fold it into the River Oaks clubhouse scope now that `PD-13` says the building is repairable. Drop it and keep the current lot count.

**Recommendation.** Fold it into the clubhouse scope, because River Oaks now has one live capital conversation rather than four and 6 to 8 lots is the largest revenue item in any of them.

**Cost of being wrong.** A feasibility fee, and a delay of one budget cycle on 6 to 8 lots of lot rent.

**Reversible.** Yes at the study stage. Not once the well moves.

**Staleness.** Live, and improved. It was raised alongside a clubhouse question that has since been answered, which removes its main uncertainty.

---

### `PD-12` Amenity preference survey before building

**Question.** Do residents get surveyed on amenities before any amenity capex is approved, as a standing rule across the portfolio?

**Blocked.** Every amenity line in the 2027 budget, and `PR-0028` on [[00-Meta/promises]], which is a promise to residents that a survey happens before anything is built. Waiting: Natalie Magurne, Vikki at River Oaks, and every manager with an amenity ask (`PR-0008`, `PR-0009`, `PR-0023`, `PR-0024`).

**Options.** Yes, survey first, portfolio-wide, no exceptions. Survey only above a dollar threshold. Keep it River Oaks only, as already scoped.

**Recommendation.** Survey first above a threshold, because the River Oaks scoping already proved the mechanism works and The Oaks and Terrace Crossings already decided basketball over pickleball without one, so a blanket rule would relitigate a settled call.

**Cost of being wrong.** An amenity nobody uses, at one property.

**Reversible.** Yes.

**Staleness.** **Partly moot for River Oaks**, scoped and delegated 2026-08-31 to Vikki via Natalie. The open half is the portfolio rule, which is what this brief asks.

---

### `PD-13` River Oaks clubhouse

**Question.** The repair-or-replace binary is answered. The live question: why did the funded `Amenities - Clubhouse Reno, $75,000` line, scheduled 2026-01-31 to 2026-03-31, never run, and do you re-release it for budget week?

**Blocked.** `PD-12`, `PD-14`, `PR-0023`, `PR-0024`, `PR-0028`, `TD-0366`, `TD-0367`, and `PF-0179`, which is the inspection report that has still never been read. Waiting: John Clark on the structural work, Natalie Magurne on the resident-facing side.

**Options.** Re-release the existing $75,000 line and require the inspection report read first. Rescope from scratch at budget week. Defer to 2027.

**Recommendation.** Re-release the existing line with the inspection report as a precondition, because the building still leans and still leaks after a roof replacement that money was already spent on, which means the scope was wrong rather than the budget.

**Cost of being wrong.** A second wasted spend on a building whose actual defect has never been diagnosed. The first one is already sunk.

**Reversible.** The re-release is. The spend is not.

**Staleness.** **The binary is moot, decided 2026-09-01 in your words: "River Oaks is Repairable."** The row should move to Resolved and the scope question should become its own row. Note the budget window closed five months ago.

---

### `PD-14` River Oaks bathroom conversion

**Question.** The bathroom quote came back above the funded number. Do you want the variance explained before budget week, or do you kill the line?

**Blocked.** River Oaks amenity allocation alongside `PD-12` and `PD-13`. Waiting: John Clark.

**Options.** Get the variance explained against the existing `Amenities - RV Bathrooms, $20,000` line and then decide. Kill the line and reallocate to the clubhouse. Rebid it.

**Recommendation.** Get the variance explained first, because a quote that comes in above a number set eight months ago and never spent is either a stale budget or a bad quote, and those two have opposite fixes.

**Cost of being wrong.** Either an overpay or a cancelled amenity that was affordable.

**Reversible.** Yes.

**Staleness.** **Twice overtaken.** Decided 2026-08-31 as bathroom over dog wash, then reopened 2026-09-01 by your own *"Price out but not realistic."* The dog-wash half is settled; only the pricing half is live.

---

### `PD-15` Lucky Clover shuffleboard roof

**Question.** Nothing to rule on. Do you want the lighting walkthrough you promised Angel and the maintenance lead scheduled this week?

**Blocked.** Nothing of yours. Delegated 2026-08-31 to Angel and Jason Davis via Natalie. What is still open is `PR-0011` on [[00-Meta/promises]], the design decision promised to Angel and the maintenance lead, and the lighting walkthrough promised alongside it.

**Options.** Schedule the walkthrough. Fold it into the next Natalie one-on-one. Leave it with the delegates.

**Recommendation.** Schedule the walkthrough, because the promise register records it as a promise to two named people and a promise closes when the person is told, not when the work is done.

**Cost of being wrong.** Negligible on the design. Real on the promise, which is the part that keeps a new manager engaged.

**Reversible.** Yes.

**Staleness.** **Moot as a decision, delegated 2026-08-31.** What remains is a promise, not a decision, and it belongs in `00-Meta/promises.md` rather than here.

---

### `PD-16` May investor residents rent out their units at Gulf Breeze

**Question.** May an investor who buys a home at Gulf Breeze rent it out, yes or no, as a carve-out to the company-wide investor-application policy?

**Blocked.** The company-wide investor-application policy standardisation, which is moving forward with this one carve-out unruled. Waiting: Natalie Magurne, who is the named owner, and Rose at Gulf Breeze. Due 2026-09-11.

**Options.** No, owner-occupied only. Yes, with the $50 application fee and a rental addendum. Yes but capped at a percentage of the community.

**Recommendation.** No, owner-occupied only at Gulf Breeze, because at 74.4% occupancy against a de-duplicated portfolio average of 77.67% there is vacancy the company could be leasing itself, and an investor renting a unit out competes directly for the same tenant.

**Cost of being wrong.** A few home sales lost to investors who wanted rental rights, against rental income the company would otherwise capture.

**Reversible.** Yes, but only prospectively. Rights granted in a purchase are hard to withdraw.

**Staleness.** Live and the urgency went up, not down. Gulf Breeze is one of the named real-absorption properties at +5 units, so the community is filling and the carve-out matters more each month. One caveat carried from the row: an archived `xGulf Breeze MHP` record also carries 39 units, so any occupancy figure pulled without de-duplicating will be wrong.

---

### `PD-17` New-home pricing at The Oaks

**Question.** What is the price band for the incoming new homes at The Oaks and Terrace Crossings?

**Blocked.** The launch of new-home sales at The Oaks and Terrace Crossings. The row records "price the incoming new homes" as an open to-do gated on this. Waiting: Leslie Croft, the named owner, and Carmin Horner, who holds both communities on the staff roster.

**Options.** Price it yourself now. Have Leslie bring a band with comparables and approve it. Hold launch until the pricing SOP exists.

**Recommendation.** Have Leslie bring a band with comparables, because pricing is her function and the row has sat unpriced since 2026-08-26 waiting for a decision that was never actually hers to wait on.

**Cost of being wrong.** Mispriced inventory at one community, correctable at the next release.

**Reversible.** Yes, subject to not repricing homes already under contract.

**Staleness.** Live, and the row's context column is empty. The register itself notes the context for `PD-16`, `PD-17` and `PD-18` is genuinely not recorded anywhere, so this brief is built from the blocking column alone. SINGLE-SOURCE.

---

### `PD-18` Office space at Vantage Oaks

**Question.** Where does the Vantage Oaks back office go, given Lot 1 is unbuildable and the target is 20 sales a month?

**Blocked.** Back-office scaling at Vantage. Waiting: Zach Schwartz, the named owner.

**Options.** Modular office on an alternative lot. Convert an existing structure. Run it remote and keep only a sales desk on site.

**Recommendation.** Have Zach bring two costed sites before you choose, because the row names only the site that does not work and picking a replacement without a survey repeats the Lot 1 mistake.

**Cost of being wrong.** A building in the wrong place at a community targeting its highest sales volume.

**Reversible.** No. A structure placed is a structure placed.

**Staleness.** Live. Context column empty, same caveat as `PD-17`. SINGLE-SOURCE.

---

### `PD-19` I-4 corridor exposure at Windward Knoll

**Question.** Did anyone attend the 2026-08-27 I-4 corridor public meeting, and if not, who finds out what was said?

**Blocked.** Any disposition or mitigation call at Windward Knoll. Waiting: Zach Schwartz, the named owner, and Anita Rouse, who holds Windward Knoll on the staff roster.

**Options.** Pull the meeting minutes from the county and read them. Send someone to the next meeting. Do nothing until a taking notice arrives.

**Recommendation.** Pull the minutes, because the meeting is a week past and a corridor expansion that touches the property is a fact the county has already published rather than something to wait on.

**Cost of being wrong.** A disposition decision made without knowing whether the state is about to take frontage.

**Reversible.** The information gathering is. A missed comment period is not.

**Staleness.** **Overtaken by events.** The meeting was scheduled for Thursday 2026-08-27 and that date has passed. The row as written asks whether someone should attend; that question is dead and the replacement question is what was said. The register itself says the status of the meeting is not known to this vault.

---

### `PD-20` The outside AI consultant engagement

**Question.** Three things, and they can be answered together: what percentage of measured savings does he earn and against what baseline, does he get direct API credentials to Rent Manager, the warehouse and the CRM, and do you buy the Railway Pro seat?

**Blocked.** Whether the listings monitoring dashboard gets rebuilt on Parakeet's own server and whether the daily Claude run behind it goes away. Waiting: Jon Wyss, the named owner, and John on the model-selector work the baseline depends on.

**Options.** Fixed fee for the dashboard, no percentage and no credentials, warehouse read-only through an existing account. Percentage of savings against a baseline frozen at a stated date, credentials through the normal access process. Do not engage.

**Recommendation.** Fixed fee with no direct credentials, because he told you himself he is not a business analyst and does not do compliance audits, and a savings-percentage fee measured against the Fable price spike would pay him for a decline John's model-selector work is already producing.

**Cost of being wrong.** On the fee, you overpay for a decline that was happening anyway. On the credentials, a third party holds live write-capable access to the rent ledger and the CRM outside any compliance process, and that one does not have a ceiling.

**Reversible.** The fee is. Credentials issued and used are not, because you cannot un-see data.

**Staleness.** Live. **VERIFIED, the primary recording was read end to end**, which makes this the best-evidenced row on the register other than `PD-21` and `PD-22`.

---

### `PD-21` ClickUp renewal, 2026-11-09

**Question.** Does the ClickUp workspace renew on 2026-11-09, downgrade, or go away, and if it goes, where does what lives in it land?

**Blocked.** Nothing today. There is a date on it, 67 days out. Waiting: Zach Schwartz, who you named as the only other power user and who has already replied.

**Options.** Renew as is. Downgrade to the tier two power users actually need. Migrate the content out and cancel.

**Recommendation.** Downgrade rather than cancel, because your own note is that Claude works well with the ClickUp integrations, and a two-power-user workspace on a full tier is the shape that gets downgraded rather than the shape that gets killed.

**Cost of being wrong.** One renewal period of overspend, or a migration under time pressure in early November.

**Reversible.** Yes, up to the renewal date.

**Staleness.** Live with a real clock. **VERIFIED, thread read in full.** Note your own framing: *"I think we should just think it through"*, which is a think-it-through and not yet a decision, so the honest next step is a date to think it through rather than a ruling now.

---

### `PD-22` Triple S park model community lease

**Question.** Do you approve the Triple S community lease and its addendum, including Parakeet postponing Carolina C?

**Blocked.** Triple S going live on sales, events, marketing and advertising at the community. Waiting: Leslie Croft, who drafted it and sent it 2026-09-01 at 17:25 ET, Jon Wyss, and Natalie Magurne.

**Options.** Approve as drafted. Approve subject to counsel reading the addendum. Decline the lease structure and use a licence or a vendor agreement instead.

**Recommendation.** Approve subject to counsel reading the addendum, because a third party trading inside a community on a lease is a vendor-risk decision rather than a marketing one, and the Carolina C postponement is a concession whose downstream cost is not stated anywhere in the row.

**Cost of being wrong.** A third party with lease rights inside a community and a postponed Parakeet product line, both hard to unwind.

**Reversible.** No, once a lease is signed.

**Staleness.** Live, two days old, and it is the newest fully evidenced row on the register. **VERIFIED, email read.**

---

### `PD-23` Uniti agent mailbox: shared or licensed

**Question.** Does the Uniti AI agent get a licensed user account or a shared mailbox?

**Blocked.** The October 1 Uniti go-live. Blocked in turn on `TD-0392`, which is one vendor answer about how Uniti authenticates. Waiting: Albert Gano on the provisioning, and whoever holds the Uniti relationship.

**Options.** Licensed user account. Shared mailbox. Wait for the Uniti answer on `TD-0392` before choosing.

**Recommendation.** Licensed, per the page's own recommendation at `10-Business/vendors/uniti-agent-mailbox`, because an AI agent emailing residents while the Massachusetts rent-increase class action is live produces discoverable records from day one and a shared mailbox cannot be placed on litigation hold.

**Cost of being wrong.** One seat of licence cost if licensed turns out unnecessary. If shared turns out wrong, a day lost at the wrong end of an October 1 go-live plus a discovery gap on live litigation.

**Reversible.** One way. Licensed to shared is a supported conversion that keeps the data; shared to licensed is not the same trip.

**Staleness.** Live, raised 2026-09-02. The asymmetry means this is cheap to decide now and expensive to decide late.

---

### `PD-24` Who owns the rehab program

**Question.** Do you name a single rehab program owner, and who is it?

**Blocked.** Every gap on `70-Operations/rehab-program/overview`, and specifically `KP-0040` where three systems hold a rehab cost $274,178 apart, `KP-0041` where $989,786 of GL spend sits against 56 units marked Complete, `KP-0043` the unreconciled forecast, `KP-0046` vendor concentration, and `KP-0047`. Waiting: John Clark, Natalie Magurne, Zach Schwartz, Mark Doucette of High Pace, and the Controller seat that is in transition.

**Options.** One named program owner with the Controller seat supplying the money side. A committee of the four departments. Leave it split and reconcile quarterly.

**Recommendation.** One named program owner, per the page's own recommendation, because a program split four ways is four people each holding a quarter of a problem and that is exactly the arrangement that let three cost figures drift $274,178 apart without anyone catching it.

**Cost of being wrong.** The wrong person owns it and you swap them, which is cheap. Not naming anyone costs the drift continuing, which is the expensive branch.

**Reversible.** Yes.

**Staleness.** Live and hardening. The forum named on the row is the Friday 14:00 ET Executive EOS call, which means it can be settled this week without a new meeting.

---

### `PD-25` One rehab call or two

**Question.** Do you split the Wednesday 10:00 ET rehab call into an operational call with the vendor and a separate monthly internal money review?

**Blocked.** The three-way tie-out on WIP and invoices, which currently has no forum. Waiting: John Clark, Natalie Magurne, Mark Doucette, and whoever holds the money side.

**Options.** Split into two calls. Add Accounting to the existing 30-minute call. Leave as is.

**Recommendation.** Split, per the page's own recommendation, because you cannot run a general-ledger reconciliation with your largest contractor listening, and the nine units where his tracker sits $163,123 above the GL is a conversation to have with him while whether $989,786 is stuck in WIP is not.

**Cost of being wrong.** One extra monthly meeting on the calendar.

**Reversible.** Yes, trivially.

**Staleness.** Live. This is the cheapest row on the register to answer and it unblocks `PD-24` and `KP-0041` operationally.

---

### `PD-26` Whether the modelled rehab forecast may be used

**Question.** Do you bar the modelled rehab forecast from anything that leaves the company until it is reconciled to the approved capex plan?

**Blocked.** Jon's fund reporting, LP updates and lender packages. Blocked in turn on `TD-0415`. Waiting: Jon Wyss, Zach Schwartz, and anyone building an external pack.

**Options.** Bar it externally, label it `model` on every internal surface. Allow it with a caveat footnote. Allow it unrestricted.

**Recommendation.** Bar it externally, per the page's own recommendation, because the only rehab forecast that exists sits $5.8M below the approved $9,954,600 plan with no explanation, and 27 of its rows use a flat portfolio average because they carry no tier.

**Cost of being wrong.** Internally, some friction while people wait for the reconciliation. Externally, a number reaching an LP or a lender that cannot be defended, which is the branch with no ceiling.

**Reversible.** The bar is. A number already sent to an LP is not.

**Staleness.** Live. The asymmetry is extreme and this is a one-sentence ruling.

---

### `PD-27` Eastdil or Newmark on the JREF I recapitalisation

**Question.** Do you back Newmark, back Eastdil, or hold until Jadian weighs in, and either way do you get Eastdil the update you owe them?

**Blocked.** The JREF I recap process. Blocked in turn on `TD-0441`. Waiting: Jon Wyss, Jadian, and Eastdil, who are owed an update regardless.

**Options.** Newmark, single mandate. Eastdil, single mandate. Hold the mandate and give Jadian the business plan and timing update first.

**Recommendation.** Hold and update Jadian first, because the row says plainly *"in the end, it'll be more Jadian's decision than ours"*, and choosing a bank before the party who decides has been briefed is how the Geiger process went wrong.

**Cost of being wrong.** Picking the wrong bank costs the difference between the MH buyer pool and the new-entrant buyer pool on a recapitalisation. Splitting it across both costs more than either, and that is the branch the row records as already tried and regretted.

**Reversible.** No, in practice. A bank engaged is a bank you cannot unwind without cost to the relationship.

**Staleness.** Live, one day old. The Eastdil update is owed whichever way this goes, and that half is a task rather than a decision.

---

### `PD-28` Plaud team account

**Question.** Do you take the Plaud team account at the same price as today?

**Blocked.** Nothing operational. `TD-0442`. Waiting: nobody is blocked. Jon runs a different recorder and will not use two systems, and one founder does not have the current device.

**Options.** Take it and mandate the desktop app on Teams calls. Take it for your own use only. Decline.

**Recommendation.** Take it and mandate the desktop app on Teams calls, because the price is unchanged and the capability with the most leverage is not the sharing, it is the desktop app auto-recording every Teams call, which does not depend on anyone else carrying a device.

**Cost of being wrong.** Nothing. Price is flat.

**Reversible.** Yes.

**Staleness.** Live but weightless. **Nothing is blocked by it, which makes it a candidate for closing rather than deciding.** The adoption problem it names is real and belongs on the to-do register, not here.

---

### `PD-29` Buying materials through the rehab vendor's Home Depot Pro account

**Question.** Do you route company material spend through Mark Doucette's trade account at his cost, or ask him for the quote and place the order yourselves?

**Blocked.** Window unit purchasing on the rehab program. `TD-0453`. Waiting: Mark Doucette, who offered it unprompted, and John Clark.

**Options.** Accept the offer as made. Ask for the quote at his pricing and order on a company account. Decline and buy at list.

**Recommendation.** Ask for the quote and place it on a company account, because that captures most of the saving and none of the control problem, and company spend routed through a vendor's trade account puts approval, coding and the audit trail inside his account rather than yours.

**Cost of being wrong.** A slightly worse price on window units. The other branch risks an audit trail you do not own with your largest rehab contractor, who already has a tracker $163,123 above your GL on nine units.

**Reversible.** Yes, but every purchase already made through his account stays outside your controls.

**Staleness.** Live, one day old. Guardrail 8 applies, which is why it is yours and not an operational yes.

---

### `PD-30` Portfolio site standards: mailboxes, fencing, bus shelters

**Question.** Do you set one central spec for mailboxes, entrance fencing and bus shelters and buy in bulk, or leave it park by park?

**Blocked.** Every mailbox, fence and shelter line in the 2027 budget, and roughly 30 punch-list rows now sitting as separate community items on [[60-Communities/open-items]]. Waiting: John Clark, Natalie Magurne, the three regional managers, and the on-site managers at the fifteen communities that raised mailboxes.

**Options.** Central spec and bulk buy for all three. Central spec for mailboxes only, park by park on fencing and shelters. Leave all three local.

**Recommendation.** Central spec and bulk buy, because two regionals arrived at the identical white PVC mailbox spec independently at Shady Acres and Druid Oaks, and when two people who did not talk reach the same answer the answer is the standard.

**Cost of being wrong.** A bulk order of the wrong spec, capped at one product line, against roughly 30 punch-list rows that stay open otherwise.

**Reversible.** The spec is. A bulk purchase is not.

**Staleness.** Live, one day old. The row is deliberately filed as one decision rather than three because the ruling is the same for all three; the three specs are named separately inside it if you want to split them.

---

### `PD-31` Individual trash cans over dumpsters

**Question.** Do individual cans replace dumpsters as the portfolio direction, and does the McGregor Downs fine schedule of $75 then $150 become the standard?

**Blocked.** Vendor selection, distribution, chargeback billing, enforcement and resident communication at eight communities: McGregor Downs, Parkwood, The Oaks, Terrace Crossings, Riverwalk, Paradise Palms, Regency I and Brunswick Estates. Rollout timing ties to rent increases, which differ by park, July at Terrace Crossings and October at The Oaks. Waiting: Natalie Magurne and the three regionals.

**Options.** Portfolio-wide switch on one schedule. Park by park as each rent cycle comes round. Keep dumpsters and add cameras plus fines.

**Recommendation.** Portfolio-wide on one schedule, because removing Parkwood's dumpsters moved the dumping to McGregor Downs, which means a park-by-park rollout relocates the problem instead of solving it.

**Cost of being wrong.** Can distribution cost across eight communities, against $395 a month saved at Regency alone and four days a week of staff pickup time at Terrace Crossings on a $15,000 trash cost already charged in rent.

**Reversible.** Slow. Cancelled hauler contracts and distributed cans are hard to reverse mid-year.

**Staleness.** Live, one day old. The October rent cycle at The Oaks is the nearest natural start date, which puts a soft clock on it.

---

### `PD-32` One written home-installation spec, enforced at install

**Question.** Do you adopt one written installation spec, and who audits against it at install, a QA lead or a contractor?

**Blocked.** Remediation cost at Paradise Palms, Riverwalk and Vantage Oaks, and every future set. Vendor accountability for the same defects sits at `TD-0348`, with the consolidated corporate escalation at `TD-0359`. Waiting: John Clark, the set crews, and Champion. Flagged `SAFETY` in the field report.

**Options.** Write the spec and audit with an internal QA lead. Write the spec and make it a contractual condition of payment, audited by the vendor. Write the spec and rely on the on-site manager to sign off.

**Recommendation.** Spec plus payment condition, because the same faults appear at three communities and Paradise Palms attributes them to two crews working to different standards with no downstream alignment, which is a contract problem rather than a supervision problem, and there is no QA lead in the company to do the alternative.

**Cost of being wrong.** You pay twice again, once for the flawed install and again for the remediation, and Paradise Palms is 55+ where visible defects do more reputational damage.

**Reversible.** Yes. A spec can be rewritten.

**Staleness.** Live, one day old. Note that the QA-lead-or-contractor question inside this row has no owner anywhere and is one of the orphan functions in Job 2 below.

---

### `PD-33` Electrical capacity: central or park by park

**Question.** Does Parakeet take the electrical-capacity fight to the utilities centrally, and does it press the position that a utility enforcing a code change should bear part of its cost?

**Blocked.** Infill at five communities. Whispering Pines FL faces a full community upgrade moving all services underground, hitting roughly 64 of 100 sites. Vantage Oaks cannot deviate from matching 200-amp pedestals to 200-amp homes. Great Oak cannot get power to the target area without rerouting. Paradise Lakes has an unresolved overhead-versus-underground question, may need new transformers, and carries a roughly $30,000 utility locating and mapping prerequisite before further excavation. Waiting: John Clark, Zach Schwartz on the infill plan, and five on-site managers.

**Options.** Central position, one negotiator, three utilities. Park by park as each gate arrives. Central on cost-sharing only, local on engineering.

**Recommendation.** Central position, because five parks negotiating separately with three utilities have no leverage and no consistent answer, and the cost-sharing question was asked at Whispering Pines and never answered anywhere.

**Cost of being wrong.** A per-site cost across 64 sites at one property alone, and infill stalled at five communities while it is unresolved. This is the largest unpriced item on the register.

**Reversible.** The negotiating posture is. Concessions given to a utility are not.

**Staleness.** Live, one day old, and the most consequential of the five field-report rows. Note that no owner exists for a central utility negotiation, which is another orphan function in Job 2.

---

### `PD-34` The 2027 equipment bundle

**Question.** Do you buy the 2027 equipment bundle as one decision, and does that include cancelling the Crystal Acres and Hunter Springs landscaping contract?

**Blocked.** The 2027 capital budget at `80-Finance/planning/2027-budget/overview`, plus `PR-0006`, `PR-0020` and `PR-0032` on [[00-Meta/promises]], all already flagged for budget week. Also the Shady Acres maintenance hire, now on its fifth attempt, where equipment was raised as a retention argument. Waiting: Rose, Travis, the Regency II maintenance team, and Natalie Magurne.

**Options.** Buy the bundle in one approval at budget week. Approve the excavator and mowers only, defer the carts. Keep renting and contracting.

**Recommendation.** One bundle approval at budget week, because six carts and mowers approved separately is six negotiations at retail, and Regency II's outgoing maintenance team named the small excavator as the highest-leverage purchase available since it converts rental and contractor jobs into in-house work.

**Cost of being wrong.** Capital tied up in machines that sit idle, against rental and contractor spend that is currently invisible because nobody has totalled it.

**Reversible.** No, once bought. Equipment resells at a loss.

**Staleness.** Live, one day old, with a natural forum already scheduled. `BUDGET ITEM` in the field report.

---

### `PD-35` The 21st Mortgage consumer loan structure and the $250,000 reserve

**Question.** Nothing to rule on until one number exists. Do you want line capacity across CountryPlace, 21st and Triad stated once, sourced and dated, and a name put on the expired insurance policy record 21st holds?

**Blocked.** The 21st Mortgage consumer loan programme. Greg Valentine of 21st is chasing. `CM-15` and `60-Communities/asset-inventory` hold the capacity analysis. `TD-0471` and `TD-0461` sit under it. Waiting: Jon Wyss, Greg Valentine, Merrick Snider, and the Controller seat, whose holder is out of the office.

**Options.** Green light now on the terms already agreed and settle capacity after. Hold until the capacity analysis exists, per your own precondition. Withdraw and run the programme without 21st.

**Recommendation.** Put a name and a date on the capacity analysis today rather than re-asking the decision, because you set the precondition yourself on 2026-08-31 (*"would like understand where our capacity is on all three lines before making that decision"*) and that number still does not exist, so this is blocked on a deliverable and not stalled on a judgement.

**Cost of being wrong.** The commercial terms are settled, 21st holds the reserve, disburses interest quarterly and pays SOFR on it, confirmed by Valentine 2026-08-19. What is at risk is the counterparty's patience and, separately, an expired insurance policy record that is its own gate and has no owner.

**Reversible.** The green light is not easily reversible. The capacity analysis is free to produce and reversible in the sense that it costs nothing to have.

**Staleness.** **Confirmed still undecided by you on 2026-09-03.** Surfaced twice, decided zero times. The clock started 2026-09-02, so by CLAUDE.md this becomes a slipped commitment on 2026-10-02 if it does not move. **VERIFIED, thread read in full.**

---

### `PD-36` Is there a separate Belle Haven settlement

**Question.** Is there a Belle Haven settlement separate from the Massachusetts case, yes or no?

**Blocked.** `KP-0035` T4, and every Belle Haven row on [[60-Communities/open-items]] that cannot be sized without knowing. Nine Belle Haven items sit unowned on the board. Waiting: nobody outside this vault, which is exactly the point.

**Options.** Yes, and here is the counterparty. No, there is nothing there. Do not know, so route it to counsel.

**Recommendation.** Answer it in one sentence in either direction, because *"there is nothing there"* is a complete and useful answer and this Brain currently holds zero detail on it: no counterparty, no counsel, no amount, no status.

**Cost of being wrong.** If a live matter exists and nobody here knows, the first anyone learns of a deadline is when it passes.

**Reversible.** Yes. It is an information question.

**Staleness.** **Asked three times and unanswered**, on 2026-08-31, 2026-09-01 and 2026-09-02, which is why it moved out of the daily close and into this register. The origin is your own correction of 2026-08-31: *"Settlement was in regards to the Mass case, Bellehaven is completely separate."* Note CLAUDE.md rule 16: the matter's character should come from the primary document, not from a folder name, and the row records that a Belle Haven matter was already misread once because of the folder it sat in.

---

### `PD-39` Where Austin's private personal section lives

**Question.** Does `85-Personal/` stand as a fourteenth top-level folder in this vault, or does the personal material live in Dropbox instead?

**Blocked.** `KP-0066` and `TD-0489`. The skeleton at `85-Personal/` is built and deliberately empty. Waiting: nobody but you.

**Options.** Keep `85-Personal/` here as a signed-off exception to the folder rule. Put it in Dropbox under the 2026-09-02 routing rule and leave a pointer here. Split it, calendar and logistics here, anything sensitive in Dropbox.

**Recommendation.** Dropbox with a pointer here, because the 2026-09-02 routing rule already sends anything touching Belmart or Jamie to Dropbox and never the Parakeet estate, this vault sits inside the Parakeet estate, and a private folder inside a vault that gets shared is not private. That is the same problem `10-Business/people/_private-assessments.md` already carries.

**Cost of being wrong.** Personal material sitting inside an estate that gets shared with staff, counsel or a buyer.

**Reversible.** Yes, but only until it is shared.

**Staleness.** Live, raised today. The folder rule exception is a real question and it needs your sign-off rather than a self-granted one, per CLAUDE.md.

---

### `PD-40` Does the personal Google account get disconnected

**Question.** Nothing to rule on. Do you want `austin@a2zcp.com` added as Manager on all four Google Shared Drives before the connector switches?

**Blocked.** `TD-0505`. Waiting: Albert Gano or whoever holds Google admin.

**Options.** Add the memberships first, then switch. Switch now and repair access after. Hold the switch until the K-1 cycle closes on 2026-09-15.

**Recommendation.** Add the memberships first, because Shared Drive membership belongs to an account and does not travel with the switch, so switching first takes the only route to the Bedrock fund record base dark while five LPs chase the 2025 K-1 against a 2026-09-15 deadline. The pre-switch manifest is captured at `10-Business/storage-inventory/gdrive-shared-drives-manifest`.

**Cost of being wrong.** Losing sight of cap tables, fund subscriptions, K-1s, an LPA and executed signature pages with no inventory of what went missing. The manifest is the insurance against that and it already exists.

**Reversible.** The switch is. The lost access window is not, and it lands inside a filing deadline.

**Staleness.** **Moot as a decision. RULED by you on 2026-09-03: *"i am going to change the drive account to a2zcp."*** The row is still sitting in the Open table and should move to Resolved. What is live is sequencing, which is a task.

---

### `PD-41` Three policy calls on the BMHCII vault

**Question.** Three, and they can be answered in one sitting. Do the four `_FOLDER STATUS.txt` notes and two retained unsigned memos stay in a vault defined as final approved documents only? Will you sign `WP-36-M1 v2`, `M2 v2` and `M3`, or should they be relabelled as open item lists? Which of the eleven dated general ledger pulls in `4.1` governs?

**Blocked.** The integrity of the BMHCII document vault. No source names an owner for any of the three. Waiting: whoever receives that vault next, which on current form is counsel or an LP.

**Options.** Answer all three now. Answer the signature question only and defer the other two. Hand all three to counsel with the vault.

**Recommendation.** Answer all three now, because the signature question is the one that matters and the other two are ten seconds each once you are in the file. Keep the status notes, since removing them erases the only in-vault record that the gaps are known and owned. Name one governing GL pull and archive the other ten, because `_FINAL` is currently attached to files that later undecorated pulls supersede and two RegisterPrint workbooks sit one byte apart with neither archived.

**Cost of being wrong.** Three unsigned drafts are currently the sole content of sections `2.3`, `2.4` and `2.5`, and their withdrawn v1 predecessors in `Archive_Superseded` already show any reader that the fund's assertions in this area were wrong once and were corrected only after its own filed K-1s contradicted them. A reader who finds unsigned drafts next to that history draws the obvious conclusion.

**Reversible.** The filing calls are. A signature is not.

**Staleness.** Live, raised today by the 2026-09-03 audit. This is the newest row on the register and it sits inside a live dispute, which is an unusual combination.

---

## The ranking: all 39 by what it costs to keep them parked

Ranked by cost of delay, not by size of the decision. A large decision with no clock ranks below a small one with a counterparty waiting or a one-way door closing.

| Rank | ID | The question in short | Why it ranks here | Reversible |
|---|---|---|---|---|
| 1 | `PD-26` | Bar the modelled rehab forecast from anything leaving the company? | One sentence to answer, and the downside has no ceiling: a $5.8M unexplained variance reaching an LP or a lender | Bar yes, sent number no |
| 2 | `PD-24` | Name one rehab program owner? | Unblocks `KP-0040`, `KP-0041`, `KP-0043`, `KP-0046`, `KP-0047`; the forum is Friday 14:00 ET this week | Yes |
| 3 | `PD-23` | Licensed account or shared mailbox for the Uniti agent? | October 1 go-live, one-way conversion, discoverable records against a live class action | One way only |
| 4 | `PD-22` | Approve the Triple S community lease and addendum? | Leslie, Jon and Natalie waiting since 2026-09-01; a signed lease cannot be unwound | No |
| 5 | `PD-35` | Put a name and date on the three-line capacity analysis? | Counterparty chasing, surfaced twice and decided zero times, clock to slipped commitment started 2026-09-02 | Analysis yes, green light no |
| 6 | `PD-03` | Person first or platform first on accounting? | The largest decision on the register, and the Controller departure removes the option of waiting | Sequencing yes, hire slowly |
| 7 | `PD-20` | Fee basis and credentials for the outside AI consultant? | Credentials to Rent Manager, the warehouse and the CRM outside any compliance process | Fee yes, credentials no |
| 8 | `PD-33` | Central or park-by-park on electrical capacity? | Infill stalled at five communities; 64 sites at Whispering Pines alone; largest unpriced item here | Posture yes, concessions no |
| 9 | `PD-02` | Commission the Controller function extraction? | Eleven board rows still route to that seat and go dark when it empties | Yes |
| 10 | `PD-13` | Re-release the funded $75,000 clubhouse line, inspection report first? | The building still leans after money was already spent; the funded window closed five months ago | Release yes, spend no |
| 11 | `PD-16` | May investor residents rent out at Gulf Breeze? | Due 2026-09-11; the community is filling at +5 units so the carve-out costs more each month | Prospectively only |
| 12 | `PD-41` | Three BMHCII vault policy calls, including three signatures | Live dispute, and unsigned drafts sit next to a documented prior correction | Filing yes, signature no |
| 13 | `PD-04` | Warehouse only, or continue MAV MCP? | The five-week runway to snowbird season has about one week left | Stopping yes, restarting no |
| 14 | `PD-25` | Split the rehab call into operational and money? | Cheapest row on the register to answer and it makes `PD-24` workable | Yes |
| 15 | `PD-40` | Add a2zcp as Manager on all four Shared Drives before switching? | K-1 deadline 2026-09-15; switching first takes the fund record base dark | Switch yes, lost window no |
| 16 | `PD-27` | Eastdil, Newmark, or brief Jadian first? | A bank engaged cannot be unwound; the split-mandate mistake is already on record | No |
| 17 | `PD-36` | Is there a separate Belle Haven settlement? | Asked three times, unanswered; if a live matter exists nobody here knows its deadlines | Yes |
| 18 | `PD-06` | Send the drafted Corner IQ decline? | Decided 2026-08-31 and the vendor still has not been told | Yes |
| 19 | `PD-32` | One installation spec, enforced how? | Paying twice at three communities and counting; `SAFETY` flagged | Yes |
| 20 | `PD-31` | Individual cans over dumpsters, portfolio-wide? | Park-by-park relocates the dumping rather than solving it; October rent cycle is the natural start | Slow |
| 21 | `PD-30` | Central spec and bulk buy on mailboxes, fencing, shelters? | Roughly 30 punch-list rows stay open until this is answered | Spec yes, bulk order no |
| 22 | `PD-34` | Buy the 2027 equipment bundle as one approval? | Budget week is the forum and it is coming; six separate approvals is six retail negotiations | No |
| 23 | `PD-29` | Route material spend through the vendor's trade account? | Audit trail sits outside company controls with the contractor already $163,123 above the GL on nine units | Prospectively only |
| 24 | `PD-21` | Renew, downgrade or drop ClickUp? | Real date, 2026-11-09, and 67 days of runway | Yes |
| 25 | `PD-08` | Bundle landscaping into rent at the Regencies? | Waiting 8 days on a spend pull nobody has been named to do | Slow |
| 26 | `PD-17` | Price band for new homes at The Oaks? | Sales launch gated on it since 2026-08-26 | Yes |
| 27 | `PD-07` | Referral fees to outside managers, yes or no? | Vicky's plan has been ready to execute for 8 days | Yes |
| 28 | `PD-09` | Landlord addendum at the Regencies? | Roughly half the landlord roster is still unknown | Yes |
| 29 | `PD-19` | Pull the I-4 corridor meeting minutes? | The meeting was 2026-08-27 and the outcome is unknown to this vault | Info yes, comment period no |
| 30 | `PD-18` | Where does the Vantage Oaks office go? | A structure placed is a structure placed, but nothing is waiting on it today | No |
| 31 | `PD-11` | Fund the River Oaks well feasibility? | 6 to 8 lots of lot rent, but the clubhouse ruling removed its main uncertainty | Study yes, move no |
| 32 | `PD-14` | Explain the bathroom quote variance or kill the line? | Reopened 2026-09-01; a stale budget and a bad quote have opposite fixes | Yes |
| 33 | `PD-12` | Survey residents before amenity capex, as a rule? | River Oaks is already scoped; only the portfolio rule is open | Yes |
| 34 | `PD-39` | Does `85-Personal/` stay in this vault? | Nothing else waits on it, but it is a one-way door once material is filed and the vault is shared | Until shared |
| 35 | `PD-10` | Return date on the Gulf Breeze FEMA options? | Delegated 2026-08-31 with no clock attached | Yes |
| 36 | `PD-05` | Park Rellit until `PD-03` is answered? | Fully dependent on `PD-03`; no independent content | Yes |
| 37 | `PD-01` | Move the Ozzie row to Jon and close it here? | Ruled 2026-08-31 and never moved | Yes |
| 38 | `PD-15` | Schedule the Lucky Clover lighting walkthrough? | Delegated; what is left is a promise, `PR-0011`, not a decision | Yes |
| 39 | `PD-28` | Take the Plaud team account? | Price is unchanged and nothing is blocked by it | Yes |

### The five to answer first

Each is answerable in a sentence, and each costs more tomorrow than today.

1. **`PD-26`.** Do you want the modelled rehab forecast barred from Jon's fund reporting, LP updates and lender packages until `TD-0415` reconciles it to the approved $9,954,600 plan?
2. **`PD-24`.** Who is the single owner of the rehab program, and do you want it named at the Friday 14:00 ET Executive EOS call this week?
3. **`PD-23`.** Does the Uniti agent get a licensed user account rather than a shared mailbox, so it can be placed on litigation hold before the October 1 go-live?
4. **`PD-22`.** Do you approve the Triple S community lease and addendum, and does counsel read the addendum before you do?
5. **`PD-35`.** Who produces the line-capacity number across CountryPlace, 21st and Triad, and by what date, so the $250,000 reserve decision stops being blocked on a deliverable nobody owns?

### The rows that should leave the register rather than be decided

**Nine of the 39 are not live decisions.** Leaving them in place is what makes the queue read as 39 when it is closer to 30.

| ID | Why it should leave | Where it belongs |
|---|---|---|
| `PD-01` | Ruled 2026-08-31, owner moved to Jon Wyss | Resolved, with a dated follow-up on Jon |
| `PD-06` | Decided 2026-08-31; only a send remains | `TD-0015` |
| `PD-10` | Delegated 2026-08-31 to Rose and Natalie | A dated delegation, not a decision |
| `PD-13` | The binary was ruled 2026-09-01; the scope question is a new row | Resolved plus a new capital row |
| `PD-15` | Delegated 2026-08-31 to Angel and Jason Davis | `PR-0011` on [[00-Meta/promises]] |
| `PD-19` | The 2026-08-27 meeting has passed; the question changed | A to-do to pull the minutes |
| `PD-28` | Nothing is blocked by it and the price is flat | A to-do |
| `PD-40` | Ruled 2026-09-03 in your own words | Resolved plus `TD-0505` on sequencing |
| `PD-05` | Fully dependent on `PD-03` | A sub-question inside `PD-03` |

**Two more are decisions that turned into deliverables**, which is a different failure and worth separating: `PD-08` is waiting on a landscaping spend pull nobody has been named to run, and `PD-35` is waiting on a capacity analysis nobody has been named to run. Neither needs a ruling. Both need a name and a date. INFERRED from the register text; no source states it this way.

**One process observation.** `PD-23` through `PD-29` are physically located below the `## Related` heading in `00-Meta/parked-decisions.md`, after the Resolved table. VERIFIED: the board parser reads them as section `Related` with an empty description, which is why seven live decisions, including the $989,786 rehab reconciliation questions, appear on the board as blank unowned rows. That is a filing defect rather than a content one, and it is one edit to fix.

---

## Job 2. The 479 unowned items

**Method.** `board.json` was loaded and analysed in node. Every count below is reproducible from that file. VERIFIED unless labelled otherwise. No row is listed individually except where the individual row is the finding.

### What the 479 actually is

**479 of 1,183 rows carry `unowned: true`, which is 40.5%.** VERIFIED. But three things inside that number are not unowned work, and stripping them changes the shape of the problem.

| Deduction | Count | What it is |
|---|---|---|
| Rows the board parser could not read | 45 | Blank or stub descriptions. See below. |
| Rows already closed | 13 | `CM-07`, `CM-08`, `CM-09`, `KP-0006`, `KP-0007`, `TD-0001`, `TD-0002`, `TD-0032`, `TD-0037`, `PR-0004`, `PR-0014`, `PR-0034`, `PR-0035`. A closed row does not need an owner. |
| Net genuinely unowned and open | **~421** | The number worth working. |

**The 45 unreadable rows are a parser defect, not a filing gap, and this matters because it is the cheapest thing on this page to fix.** VERIFIED by opening the source files. `TD-0376` through `TD-0396`, 21 consecutive rows, come back with empty descriptions on the board while `10-Business/eos/to-dos.md` line 642 onward carries full text on every one of them, including `TD-0392` (ask Uniti how their integration authenticates), `TD-0389` (an A and A Development invoice of $108,919.00 sitting five months in AvidXchange Pending Workflow Assignment) and `TD-0396`, which **already has a named owner in the source**, Austin with Zach Wallack, and is still counted in the 479. Likewise `KP-0025` through `KP-0036` render as `C1` to `C7` and `T1` to `T5`, and `TD-0497`, `TD-0498`, `TD-0503`, `TD-0510` and `TD-0529` as `P1`, `P4`, `P2`, `P2`, `P0`. And `PD-23` through `PD-29` come back blank because, as noted in Job 1, they sit physically below the `## Related` heading in `00-Meta/parked-decisions.md`.

**So the headline should read closer to 421 of 1,170, or 36%.** Still bad. But 45 rows of it is a table-shape problem in two files and a parser that gives up on them, and that is a morning of work rather than an org design question.

### Where the unowned sit

**By register.** VERIFIED.

| Register | Total rows | Unowned | Unowned share |
|---|---|---|---|
| `10-Business/eos/to-dos.md` | 533 | 263 | 49% |
| `60-Communities/open-items.md` | 465 | 127 | 27% |
| `00-Meta/open-items.md` | 74 | 41 | 55% |
| `00-Meta/parked-decisions.md` | 41 | 20 | 49% |
| `00-Meta/promises.md` | 40 | 23 | 58% |
| `00-Meta/commitments.md` | 30 | 5 | 17% |

**Read that column right to left and it says something specific.** Commitments, the register you personally curate, is 17% unowned. Promises, at 58%, is the worst on the board, and a promise with no owner is the one kind of row that cannot be silently dropped, because a named person is waiting to be told. The to-do register carries the volume, 263 rows, but the promise register carries the highest failure rate.

**By subject area.** These are keyword clusters over description, notes and section text, so they overlap and a row can appear in two. INFERRED classification, VERIFIED counts.

| Cluster | Unowned rows | Where they concentrate |
|---|---|---|
| Construction, QA and install defects | 149 | 115 in property follow-ups, 25 in to-dos |
| Systems, data and integrations | 77 | 26 to-dos, 28 property, 17 known problems |
| Resident, leasing and infill | 71 | 32 to-dos, 25 property |
| Vendor and contract management | 63 | 38 to-dos, 16 known problems |
| Utilities and permits | 46 | 29 to-dos, 8 property |
| Rehab money reconciliation | 30 | 16 to-dos, 7 known problems |
| SOP library and process docs | 18 | 10 to-dos, 7 known problems |
| Fund, LP and tax | 13 | 5 known problems, 4 to-dos |
| Insurance and risk | 11 | spread across four registers |
| HR, hiring and headcount | 7 | spread |
| Title and home registration | 6 | 3 property, 2 to-dos |
| Entity compliance and state filings | 5 | `CM-30`, `KP-0022`, `KP-0067`, `TD-0484`, `TD-0492` |

**The bottom four rows of that table are the interesting ones and this is the central finding of Job 2.** Insurance, titles, entity compliance and tax are the smallest clusters on the board and they are the ones with the highest per-row consequence. A missed mailbox spec costs a mailbox. A missed annual report puts an entity out of good standing, which is exactly what `KP-0067` records happening to Lamberton Lake MHC, LLC over a 2023 filing. **Small clusters are not evidence that a function is healthy. They are usually evidence that nobody is generating rows for it**, because there is nobody there to notice.

**By community.** 322 of the 479 carry no community at all, which is consistent with them being corporate rather than field work. Of the 157 that do, the spread is flat: River Oaks RV Resort 12, McGregor Downs 12, The Oaks 10, Belle Haven 9, Fox Creek 9, Brunswick Estates 9, Riverwalk 7, then a long tail. **There is no single problem community.** That is a useful negative: this is not one park in trouble, it is a portfolio-wide routing gap.

**By source date.** 286 of the 479 carry a date in their section or provenance text. VERIFIED.

| Source date | Unowned rows |
|---|---|
| 2026-08-18 to 2026-08-24, the southeast road trip | **162** |
| 2026-09-02 | 51 |
| 2026-08-31 | 35 |
| 2026-09-01 | 19 |
| 2026-09-03 | 14 |
| other single dates | 5 |
| no date in the section text | 193 |

**One week of one road trip produced 162 of the unowned rows, and the 150-row section of `10-Business/eos/to-dos.md` titled "Unassigned: no owner named in the source, and none obvious" is almost entirely the same trip.** Sampled: `TD-0039` paint three speed bumps, `TD-0043` price a Metron meter after the main city meter, `TD-0052` make the compromised storm drain safe, `TD-0062` deal with the home that has no wood under it and is about to fall over, `TD-0063` complete utility locating before further digging. VERIFIED from board.json.

### The structural reason

**The harvest captures the work and the place. It never captures the person, because the person was never in the room in a way the recording could record.**

Every large unowned block on this board comes from the same kind of event: a walk-through, a Plaud recording, a transcript filing, a mailbox sweep. In each case somebody observed a problem at a location. What got written down was the problem and the location. **Nothing in the capture step forces a name, and the register accepts a row without one, so the row lands unowned and stays that way.** That is why the largest cluster is construction and property work, at 149 rows, and why 162 of them trace to a single week of driving.

**Three things make this worse rather than self-correcting.**

**One, the safety valve became the default.** CLAUDE.md rule 18 says a task with no owner in any source says **unassigned** and names the forum where you can settle it, never a guessed name. That rule is correct and it exists because a guessed owner is worse than an honest gap. **But only 28 of the 479 name a forum.** VERIFIED. So the rule's first half, do not guess, is being followed universally and the second half, name the forum, is being followed 6% of the time. The result is an honest gap with no route out of it.

**Two, the field register already knows the answer and does not write it down.** **115 of the 127 unowned property follow-ups carry regional coverage in their owner text but no person**: 61 to Liz Santiago, 43 to Alex Pontes, 11 to Ashlyne Godinez. VERIFIED. **That is not 115 unowned items. That is three unowned items.** The board is one mapping decision away from routing 90% of the property register, and the mapping is already written on every row.

**Three, an unowned row generates no pressure, so the age field goes unfilled.** Only 127 of the 479 carry an age, and only 5 carry a due date. VERIFIED. A row with no owner and no date cannot be late, and something that cannot be late does not get worked. That is the accumulation mechanism in one sentence.

**One thing this is not.** It is not duplication. Only 2 of the 479 share the first sixty characters of their description with another unowned row. VERIFIED. These are 421 distinct pieces of work, not one problem counted many times.

### The orphan functions

**This is the part worth more than any individual row.** An orphan function is where a cluster of unowned items all need the same kind of person, and no such person exists in the company. Six of them are on this board. Each is a hiring or engagement finding.

**Note on the accounting function.** It is known to be thin and the Controller is departing, and that fact sits underneath four of the six below. It is stated once here rather than repeated: this is a function-level observation and not a judgement about any person, and nothing in this file records anyone's compensation.

---

**1. Corporate secretary and entity compliance. Nobody. Not one row on this board routes to this function.**

The evidence is small in row count and large in consequence. `CM-30`: A2Z Community Partners has been past due with its registered agent for three consecutive monthly statements. `KP-0067`: a 2024 Michigan notice put Lamberton Lake MHC, LLC in "Impending Not in Good Standing" over a 2023 annual filing. `TD-0372`: an Oregon notice on Bedrock MHC Fund II, received in the mail, and the only person it routes to is the departing Controller. `KP-0022`: **no compliance calendar exists anywhere**, and the Jadian obligations, the Florida January 1 Division filing and the 7-year retention requirements all sit on it. `TD-0484` and `TD-0492`.

**Why it reads as five rows rather than fifty:** nobody is generating rows for it. An entity falling out of good standing produces no ticket. It produces a letter, to an address, that somebody may or may not open. **The 5 is the count of the notices that happened to be seen.** INFERRED, and it is the most defensible inference on this page.

**What it needs.** Not a full seat. A named owner plus a calendar, and the calendar is buildable by an agent from the filed formation documents. Roughly 115 entities are listed on `Master Org Chart.xlsx` per `CM-06`, so this is a real recurring obligation and not a one-off cleanup.

---

**2. Insurance and risk. Currently a broker relationship with no internal counterpart.**

`10-Business/departments/accounting-and-finance.md` puts insurance inside Accounting and records the March 2026 move from IOA to Baldwin. **A broker sells and places cover. A broker does not notice that you stopped being covered.** `KP-0065`: Royal Oak Vero Beach general liability may have been uninsured since 2026-06-16 and nothing on file says otherwise. `PF-0461`: an insurance renewal binder owed to Capital One before the Lamberton policy expires 2026-10-31. `TD-0274`: the serial-by-serial insurance tie-out, where you declined to reassign it and it stays with accounting, unscheduled. And on `PD-35`, 21st Mortgage is holding an expired policy record and the row says plainly that **that gate has no owner**.

**What it needs.** Not a risk manager hire at this size. A named internal counterpart to Baldwin with a renewal calendar and a schedule of insured assets, which is the same calendar as orphan function 1 and should be one build.

---

**3. Utilities and permits. A function that was explicitly moved out of accounting to a destination that was never named.**

This is the clearest orphan on the board because the decision to orphan it is written down. `10-Business/departments/accounting-and-finance.md`, Decisions, **2026-08-22: "Move utilities and operating permits out of accounting to capable people outside it; the function was described as a black box with poor communication."** VERIFIED. No person, no team and no date was attached. `PF-0030` is the same finding from the property side.

**46 unowned rows sit in this cluster**, 29 of them in the to-do register. The same page records that **four of the seven Tier 1 Critical processes with nothing started are utility processes**: utility onboarding for current communities, utility onboarding at acquisitions, utility recapture reporting and utility recapture review. And `PD-33` needs somebody to hold a central negotiating position with three utilities across five communities, which is a job nobody has.

**What it needs.** A utilities and permits coordinator, and this is the strongest single hiring case on the board. The function has a named exit from its old home, a named set of broken processes, a 46-row backlog and a live negotiation waiting on it.

---

**4. Construction QA and install inspection. The largest cluster, and the audit role inside it is explicitly ownerless.**

149 unowned rows, 115 of them in the property register. `PD-32` names it directly: the proposed installation spec raises "the QA-lead-or-contractor audit question that `PF-0179`-era rows and the Riverwalk punch list both raise with no owner." The same defects appear at Paradise Palms, Riverwalk and Vantage Oaks, attributed to two crews working to different standards with no downstream alignment, and the company pays twice, once for the flawed install and again for the remediation.

**What it needs, and this is the one where the honest recommendation is not a hire.** Make it a contractual condition of payment audited by the vendor, per the `PD-32` recommendation, because a QA lead is a headcount decision that takes a quarter and the payment condition takes a contract amendment. **The hire becomes right if the payment condition is tried and the defects continue.** That is the condition to watch, and it should be written down when the amendment is made.

---

**5. Business systems analyst and data steward. The function exists and it is you.**

77 unowned rows in the systems and data cluster, 17 of them in the known-problems register, which is the highest concentration of critical findings anywhere on this board. `KP-0049`: **eleven BLOCKING decisions in the QuickBase build have never been put to a person.** `KP-0050`: the QuickBase specs encode compliance logic for eight states and this Brain records seven. `KP-0053`: `WF001` depends on three FastField forms that appear on no build register. `KP-0054`: a vendor is building the company's operating system and QuickBase has no vendor page. `KP-0037`: community dropdown lists are inconsistent across all 13 forms in the JotForm audit.

`00-Meta/austin-operating-manual.md` states the diagnosis already, under what you named as the top problems: **"The systems and automation depend on him. Power Automate, Make, the dashboards, the SharePoint architecture, this Brain. Nobody else can extend them."** VERIFIED. The 77 rows are what that sentence looks like as a backlog.

**What it needs.** One person who owns forms, integrations and the data dictionary, distinct from Albert's storage migration and distinct from the reporting layer. This is the second strongest hiring case and it is the one with the largest opportunity cost, because the alternative is your calendar.

---

**6. Fund administration and investor relations. Sits on one person plus an outside accountant.**

13 unowned rows, and they are the ones with statutory dates on them. `TD-0378`: rebuild the Bedrock MHC Fund II LP distribution schedule so it reconciles to the trial balance and general ledger, where the GL says $1,108,555.65 and the schedule says something else. `TD-0379`: identify a 10/08/2025 entry of $145,837.52 that matches no LP on the schedule and that Citrin cannot explain. `TD-0380`: explain why one LP shows $10,698.05 in the GL against $7,132.03 on the schedule, which is six quarters of distributions rather than four, and check whether other LPs received catch-up payments the same way. All three are unassigned and all three are due 2026-09-30. VERIFIED from `10-Business/eos/to-dos.md`.

**These are not bookkeeping questions.** A distribution that ran six quarters where four were owed, on a fund with a fraud-styled suit running against the GP, is the kind of item that gets found by the other side rather than by you.

**What it needs.** A fund administrator, or the engagement of one at Citrin Cooperman with a defined scope, before 2026-09-30. Engagement is faster than hiring here and the deadline is 27 days out.

---

### Proposed owners for the largest clusters

Names from the vault only. **Nothing is routed to David Berman.** Where no owner exists, the row says so rather than taking the nearest name, per CLAUDE.md rule 18.

| Cluster | Rows | Proposed owner | Reasoning |
|---|---|---|---|
| Property follow-ups with regional coverage | 115 | **Natalie Magurne**, to publish the mapping | The rows already say which region covers them, 61 Liz Santiago, 43 Alex Pontes, 11 Ashlyne Godinez. She holds the regionals, so one mapping decision from her routes all 115. |
| Construction, QA and install defects, non-property | 34 | **John Clark**, with **Mark Doucette** on vendor-side spec compliance | Already the proposed owner on 12 rows in the register text. Doucette holds 165 of 219 rehab units per `KP-0046`, so spec compliance is his to accept or refuse. |
| Systems, data and integrations | 77 | **Split. Albert Gano** on storage and SharePoint, **Zach Schwartz** on reporting and the warehouse, **no owner exists** for forms and integrations | This is orphan function 5. Splitting it two ways is honest; pretending the third piece is covered is not. |
| Vendor and contract management | 63 | **John Clark** on site vendors, **Zach Schwartz** on Responsible Contractor reporting | This exact split already appears as a proposal on 12 rows and on `KP-0013`. It has never been ratified, which is why it keeps being re-proposed. |
| Utilities and permits | 46 | **No owner exists.** Interim: **Natalie Magurne** on site-level, **Moe Mehmood** on billing and recapture | Orphan function 3. The interim split should carry an explicit end date so it does not quietly become permanent. |
| Rehab money reconciliation | 30 | **Moe Mehmood** as the money side, pending `PD-24` | He runs monthly closings and corporate accounting per the department page, and `PD-24` is the decision that makes this permanent. |
| Unowned promises | 23 | **Natalie Magurne** on site promises, **Austin Berk** on the ones he made personally | A promise closes when the person is told. Nine of the 23 are flagged for budget week, which is the natural forum. |
| SOP library and process docs | 18 | **Austin Berk** as submitter via the SOP builder, **Demetria Loukas** on the 700 band | The register already proposes Austin as submitter since the process is his design. |
| Fund, LP and tax | 13 | **Jon Wyss** on LP-facing, **Moe Mehmood** on the schedule reconciliation | Both funds sit on Jon's side of the house per the register text. The three September 30 items are reconciliation work, not LP relations. |
| Insurance and risk | 11 | **No owner exists.** Interim: **Moe Mehmood**, except workers compensation to **Demetria Loukas** | Orphan function 2. HR owns workers compensation per the register text; the rest has no home. |
| HR, hiring and headcount | 7 | **Demetria Loukas** | Function match, no ambiguity. |
| Title and home registration | 6 | **Melanie Sanchez** | `TD-0047` already routes power of attorney documents to her for overnight shipping to the title company, and Maryland is the physical destination for all title paperwork per `CLAUDE.md`. |
| Entity compliance and state filings | 5 | **No owner exists.** Interim: **Austin Berk**, with the calendar built by an agent | Orphan function 1. Naming anyone else here would be a guess. |

**Flagged: eleven rows still route to David Berman and he is leaving.** VERIFIED from board.json, `owner_short == "David Berman"`. They need reassigning before the seat empties, and three of them have external counterparties on them.

| ID | Register | What it is |
|---|---|---|
| `KP-0003` | Known problems, Critical | Accounting runs 30 to 45 days in arrears with no live spend visibility |
| `TD-0005` | To-dos, High | Hunter Springs MHC carrying $35,056 revenue on a leg that should be dormant |
| `TD-0192` | To-dos | Confirm the missed-lender-deadline consequence and payment timing on SOP 302 |
| `TD-0193` | To-dos | Build the Repo Tracker named in SOP 302, which does not exist |
| `TD-0194` | To-dos | Build the Data Pack Template and supply the Prospect Report link, both `[TBD]` in SOP 302 |
| `TD-0205` | To-dos | Remove a lender's account number and ABA routing number from SOP 302. This is `KP-0001`, the highest-ranked finding on the open-items register |
| `TD-0372` | To-dos | Establish what the Oregon notice on Bedrock MHC Fund II requires and by when. **External deadline, unknown** |
| `TD-0461` | To-dos | Return 21st Mortgage's inventory confirmation. **External counterparty chasing** |
| `PF-0015` | Property | Journal entries lacking detailed descriptions still need researching |
| `PF-0024` | Property | Books close 30 to 45 days in arrears so Ramp card spend is booked monthly |
| `PF-0030` | Property | Utilities and operating permits at accounting described as a black box |

**Proposed reassignment, and it is deliberately conservative.** `TD-0205` and `KP-0001` to **Austin Berk** today, because publishing a lender's ABA routing number is fraud exposure and it should not wait on a transition. `TD-0192`, `TD-0193`, `TD-0194` to **Moe Mehmood**, since they are SOP 302 build items inside the monthly close function. `TD-0461` and `TD-0372` to **Austin Berk** with **Jon Wyss** on the fund half, because both have external counterparties who will not wait for an internal transition. `TD-0005`, `PF-0015`, `PF-0024`, `PF-0030` and `KP-0003` to **Moe Mehmood** as interim, pending `PD-03`.

---

### What an agent could own, and what it could not

**Strict test applied.** An agent owns a cluster only where the entire loop is read, compare, write and notify, with no judgement call, no money leaving, no signature, no physical presence and no third party on the other end. Anything failing one of those is a person's work with agent support, which is not the same thing and should not be counted as ownership.

**Six clusters pass.**

| Work | Rows it touches | Why it passes |
|---|---|---|
| Board hygiene: write the row count and unowned count into `00-Meta/open-board.md` on every rebuild | `TD-0391` | Pure mechanism. The header is hand-edited today, which is why the count goes stale. |
| Source-link resolution across all six registers | Most of the 479 | CLAUDE.md rule 15 says resolve on demand and write the result back. Mail and Teams both return deep links. No judgement in it. |
| Duplicate and collision detection across the SOP library and SharePoint | `KP-0051`, `KP-0052`, `KP-0060` | Two files sharing `SOP_Master_Tracker_Combined_v2.xlsx` with different md5 hashes is a comparison, not a decision. |
| Build and run the compliance calendar from filed formation documents | `KP-0022` and orphan function 1 | An agent can build the calendar and surface the deadline. It cannot file the return, which stays with a person. |
| The rehab three-way tie-out data pull | `KP-0040`, `KP-0041`, `KP-0043` | Pulling three systems into one comparison is mechanical. The $274,178 variance then goes to a person. |
| Mailbox sweep and routing into registers | Ongoing | Already the established pattern, and the a2zcp sweep proved its value on 2026-09-03. |

**And the boundary matters more than the list.** The 115 property rows do not pass, because somebody has to stand at the storm drain. The install QA cluster does not pass, because somebody has to look at the stairs. Insurance does not pass, because renewing cover is money and a third party. Vendor escalation does not pass. Anything in `PD-41` requiring a signature does not pass. **An agent that pulls the rehab variance is useful; an agent that decides which of the three numbers is right is a liability**, because the value of that reconciliation is that a person put their name on the answer.

---

## What to do first

One action, not a menu.

**Ask Natalie for the regional-to-name mapping and have it written onto the 115 property rows this week.** It is the single largest routing gain available, the answer is already on every row, and it costs her one message. Everything else on this page is a decision; that one is a transcription.
