# Online presence

**What this is:** the website, the channels and the phone number — how a prospect finds Parakeet, and what the company promises them before anyone speaks to them.

**Status:** current — 2026-08-30

## The facts

### The website

- **www.parakeetcommunities.com**, tagline **"Live Simply. Live Well. Live Parakeet."**
- **The promise, verbatim:** "vibrant neighborhoods where quality, comfort, and a friendly atmosphere make life a little brighter."
- **Navigation:** Homes · Communities · About · Help · Contact Us · FAQs · Current Residents · Future Residents · Home Improvements · Sell Your Mobile Home · Vendors · Deal Incentive.
- **Phone: (656) 260-8800.** Careers run through **jobs.appone.com/parakeetcommunities**.
- **States listed on the site:** FL, GA, SC, AL, NC, MA and MI. The Michigan property, Lamberton Lake, is being sold ([[60-Communities/portfolio]]).
- **Residents are addressed as "the flock"** — "Join the Flock", "friendly flock of residents". That ties directly to the Employee Handbook's own definition: "Our team includes our residents, employees, vendors, and stakeholders—together we are a 'flock,' working together and soaring together to new heights," with "Fly as a Flock" as a named value. **The word means the same thing internally and externally**, which is unusual and worth protecting.
- **Programmes promoted on the site:** homes for sale · homes for rent · residency applications · a **"Pick Your Perk" event with upgrades valued up to $3,500** · the resident portal · home improvement requests · Sell Your Mobile Home · a vendor programme · a deal incentive programme.
- **The site was rebuilt in 2025 from an information site into a sales platform.** The board deck names it as the main reason advertising and marketing expense ran nearly 6× budget in 2025 — $23,865 against $4,080: "Complete overhaul of our website to go from a general info site to a sales-focused platform was the main reason for increased expenses, along with uniforms for field employees."
- **Two website items remain open on Leslie Croft's Q1 rock list:** "Finalize and tweak website for little glitches & quirks", and the standalone RV websites and the Parakeet Retreats page. **Neither has evidence of completion in the vault.**

### The channels

- **A nightly crawler runs against MH Village**, built in code rather than in chat, covering *"all six thousand listings"* across Parakeet's states and pulling the data down. **It runs from a command prompt on one person's machine and only while that machine is open and running.** Added 2026-08-31 from [[70-Operations/meetings/2026-08-31-listings-pipeline-and-ai-cost-consultation]].

- **From the March deck:** MLS · MH Village · the Parakeet website · Google Ads · social · grassroots · SEO · referral · brokers · flyers · events.
- **An MH Village integration already exists** and was cited on 2026-08-24 as the model for a similar CRM/warehouse integration.
- **Google Ads had not launched as of the August 2026 tour**, and the capacity problem arrived before it did: "We haven't even launched Google Ads and the team's infrastructure is already overwhelmed with the amount of calls."
- **Google Ads already has a data rule attached.** In the CRM duplicate-and-merge workflow launched 2026-08-25, **if Google Ads is the ad source that value is retained; otherwise the oldest lead source wins** ([[10-Business/vendors/mav-consulting]]).
- **Listings sit with Tonya Thompson** — listings, listing data, marketing and branding ([[10-Business/people/tonya-thompson]]).
- **Campspot is the RV channel** — the only system that takes an RV booking, and treated in the 2026 plan as a revenue line: "in-fill RV sites with park models and generate incremental revenues from Campspot" ([[10-Business/vendors/campspot]]).

### How new work actually arrives

- **Referrals and walk-ins at the community** — the community manager is a lead source, which is why lead logging is a field responsibility.
- **Inbound calls through a central number, routed so every prospect is tracked.** Jhoiner Perez runs the offshore call centre, managed by Auzzi Dixon.
- **Web and MLS / MH Village listings.**
- **Google Ads — not yet launched as of the tour.**
- **Local outreach and grassroots.** The full path from any of these to a signed resident is on [[50-Products-Sales/pipeline]].

### Grassroots plays recorded in August 2026

- **Referral fees** — send a manager into communities whose homes sell well over $100,000 and offer a referral fee for buyers looking for something cheaper.
- **RV park canvassing** — work the surrounding RV parks to learn where the snowbird traffic goes.
- **Flyers**, dropped in those parks.
- **Elks Lodge and American Legion outreach**, targeting retired veterans.
- **A billboard** — pricing the blank board on Bayshore Road at Route 41 to fix the visibility of a park that is tucked away.
- **"Flyer flags" on end lots, credited to Fox Creek** — negotiated with residents where the lot is not company-owned, using $100 Amazon gift cards. Deployed alongside fifty for-sale signs and twenty flags at Vantage Oaks.
- **A block-and-blast Facebook campaign** and a single test RV listing at Belle Haven.

### Named problems

- **A live data error was found on the site and in Rent Manager.** Brunswick Estates showed **21 Gressel**, which is an actual resident home inside the community; the correct address is **221 Robarts Road**, and the community signage was wrong too.
- **The listing-picture problem.** The March deck asks for "an accessible listing-picture database the sales team can pull from instantly" and for all photo libraries to be organised in SharePoint. Both are open.
- **A listing audit and creator tool was drafted for Tonya on 2026-08-24** and is unassigned on [[10-Business/eos/to-dos]]. **ADVANCED 2026-08-31: the audit half is built and has been running 60 days.** It checks every listing against the system and the website, flags the fixes and suggests description rewrites, and the flag count has fallen from **50 at rollout to a few a day**. The creator half, described on the recording as a *"listings generator"* that would compose every listing from seven internal reports on the community, the area and the home, is **not built** and is gated on the current data cleanup finishing. Source: [[70-Operations/meetings/2026-08-31-listings-pipeline-and-ai-cost-consultation]].
- **The audit does not reach Zillow or Realtor.com.** It covers the Parakeet website and MH Village. Those two portals are fed through My State MLS, which is a separate hop with no check on it, and the recording is explicit that nobody knows yet whether to reach them via the My State MLS login or by scraping the end sites. **This is the largest known blind spot in listing quality.**
- **Facebook group posting is done and not tracked.** Listings are posted to Facebook groups separately from every other channel, and Austin's own words are that it *"is not as easy to track."* The consultant's read on closing that gap: *"Meta API is a bitch. It's tough, but it's possible."*
- **Description quality is a ranking argument, not a tidiness one.** The consultant's case, unrebutted on the call: Parakeet's listings sit on portals with high domain authority, so a well-templated description ranks higher on those portals and is more likely to be surfaced by an AI assistant answering a question about mobile homes in Parakeet's states. Badly written or obviously machine-written descriptions cost conversion. Recorded as his argument, not as a measured effect.
- **"REDUCE EMAIL VOLUME – Leverage tools already in place"** is the deck's own marketing-adjacent complaint.
- **Nothing in this vault holds the website's own content, analytics, SEO position or ad spend.** The facts in this page's website section come from the owner rather than from a filed source.

## Decisions

- 2026-08-31 — Build the listings generator only after the current listing data cleanup is finished, so the generator is not enforcing a template over bad inputs. (Source: [[70-Operations/meetings/2026-08-31-listings-pipeline-and-ai-cost-consultation]])
- 2026-08-24 — Correct the Brunswick Estates address to 221 Robarts Road in Rent Manager, on the website and on the community signage. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-sam-brainstorming-session]])
- 2026-08-22 — Run the grassroots play for River Oaks: referral fees from higher-priced communities, canvass the RV parks, distribute flyers, target the Elks Lodge and American Legion, and price the Bayshore Road and Route 41 billboard. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-22-post-river-oaks-discussion]])
- 2026-08-21 — Deploy fifty for-sale signs and twenty flags at Vantage Oaks, with flyer flags on end lots negotiated with residents using $100 Amazon gift cards. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-vantage-oaks-site-visit]])

## Sources

- Owner, 2026-08-30 — the website content: tagline, navigation, phone number, careers URL, the flock language, the state list and the promoted programmes. **Nothing on the site itself is filed in this vault.**
- [[80-Finance/planning/2026-executive-strategy/Parakeet - Executive Strategy Meeting v1.pptx]] — the channel list and the listing-picture and email-volume items.
- [[80-Finance/board/Parakeet - Board Presentation 2026-03 vFINAL.pdf]] — the 2025 website overhaul and the advertising expense variance it caused.
