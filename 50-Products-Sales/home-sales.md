# Home sales

**What this is:** selling homes — new infill homes and rehabbed park-owned homes — as the means of filling lots and shedding park-owned-home overhead. Not the end in itself.

**Status:** current, 2026-09-22. A second September block, 09-16 to 09-21, added by the Page Update to the lending lines and licensing entry; the first block is as of 2026-09-15 and the rest as of 2026-08-30.

## The facts

- **The logic, in the owner's words:** "We rent the land but sell the homes on it. We don't want the homes and the additional overhead and expenses that go along with them." The community is the product ([[50-Products-Sales/the-community]]); the home sale is how a lot gets filled and a park-owned home gets off the books.
- **Two kinds of home are sold.** **New (infill)** — ordered from a manufacturer, delivered, set and trimmed out on a vacant lot. **Used (rehabbed POH)** — an existing park-owned home taken through rehab and listed. The 2026 listing target is "inclusive of rehabs, ready homes & in-fill."
- **2026 targets, verbatim from the March deck:** "ORDER ~230 NEW HOMES – In-filling vacant lots is priority #1" · "LIST ~400 HOMES – Inclusive of rehabs, ready homes & in-fill" · "SELL ~400 HOMES @ MAX LOSS OF 30% – Discount = velocity."
- **The total-payment model, and it is the whole argument.** From the pricing workbook: home cost **$65,000** plus infill cost **$35,000** equals **$100,000**. Financed at **10% interest over 20 years with 5% down**, that is a **$929.89** monthly home payment. Add the model's **$640** market lot rent and the resident's **total payment is $1,569.89**.
- **The benchmark it is measured against:** a two-bedroom market rent of **$1,448**, less a **10%** park-owned-home discount, equals **$1,303.20**.
- **So at full cost the buyer pays about 20% more than renting**, and the total payment only drops below the benchmark somewhere between a 20% and a 30% discount — $1,383.91 at 20% off, $1,290.92 at 30% off.
- **Hence the policy: start at a 25% discount, and sell roughly 400 homes in 2026 at a maximum 30% loss. "Discount = velocity."**
- **The JREFI underwriting assumptions behind it** (board deck, NOI bridge): existing homes at $6k demo cost, $17k rehab cost and $33k sale price; **in-fill cost per lot/home $80k with a sale price per home of $57k — 30% below cost**, stated as such.
- **The sales process is SOPs 001 through 006.** Order and deliver ([[70-Operations/sops/001-home-ordering-delivery-and-set]]), list and take an offer ([[70-Operations/sops/002-home-sales]]), prepare the closing package ([[70-Operations/sops/003-closing-prep-and-documentation]]), close ([[70-Operations/sops/004-closing-day]]), transfer title ([[70-Operations/sops/005-poh-title-transfer]]), with lead intake and screening at the front ([[70-Operations/sops/006-lead-intake-tracking-application-and-screening]]).
- **The clocks.** Director of Sales approves or rejects an offer **within 24 hours** of receiving the PSA. Buyer e-sign window **24 hours** — miss it and the closing date does not move. Lender follow-up **every 48 hours** on financed deals. Rehab Addendum collected at offer or **within 3 business days** after.
- **Three deal paths, routed by the Closing Coordinator:** Cash, Financed, or Lease with Option to Purchase ([[50-Products-Sales/lease-with-option-to-purchase]]). Melanie Sanchez-Soto routes every one of them ([[10-Business/people/melanie-sanchez-soto]]).
- **The hard stop at the end:** the asset cannot be marked inactive in Rent Manager until payment is confirmed **AND** the floorplan loan is paid off. Keys are not handed over until Accounting confirms funds received.
- **Financed buyers go through consumer lenders, and lender registration per community is a prerequisite.** A mortgage approval was lost outright because a community was not registered with the lender: "that community isn't registered with twenty first. So I got denied from them." **There is no lender-registration process, tracker, owner or registration list anywhere in the library.** See [[10-Business/vendors/triad]].
- **The mix today is mostly cash.** As of 2026-08-20, recent rehab sales were cash, with three or four homes done through financing.
- **A Loan Coordinator role was created in August 2026** to hold financed buyers' hands, published immediately by HR.
- **Dealerships are in place with licensing cleared in FL, SC and GA**, onboarded with manufacturers and lenders; the South Carolina dealership was formed in February 2026, after which all vacant POH at Northgate were listed for sale.
- **Where the homes come from:** Champion ([[10-Business/vendors/champion]]) and Cavco ([[10-Business/vendors/cavco]]). Construction sets and trims them out and holds the readiness gate ([[10-Business/departments/construction]]).
- **Supply has run ahead of demand.** By 2026-08-24, 130 homes delivered and 40 listed and ready, ahead of plan — which moved the constraint to sales, five weeks before the October snowbird ramp.

### How a home actually reaches a listing — added 2026-08-31

Source: [[70-Operations/meetings/2026-08-31-listings-pipeline-and-ai-cost-consultation]], recording read in full. **This is the first end-to-end description of the syndication chain anywhere in this Brain.**

- **Rent Manager is the source of truth.** Every home Parakeet buys has an asset record carrying the listing fields: beds, baths, price, description. The asset listing report runs *"about six thousand deep."*
- **There are two paths out of it, not one, and only one of them is audited.**
    - **Path A, direct.** Rent Manager drops a CSV; it feeds the Parakeet website through a third party that holds an API into the system, and it feeds **MH Village**.
    - **Path B, through the gate.** Rent Manager feeds **My State MLS**, which then syndicates to **Realtor.com, Zillow and Trulia**. *"So our data takes a hop from rent manager to my state MLS, and then from my state MLS takes a hop into the websites."*
- **My State MLS is not optional.** The stated reason is the nature of the product: *"we're not actually selling the real estate. We're selling the vehicle… the vehicle on the real estate."* **100% of Parakeet's listings are mobile homes**, confirmed on the recording.
- **Path B has no audit.** The listing audit covers the website and MH Village only. Reaching Zillow and Realtor.com would mean either logging into My State MLS or scraping the end sites, and the recording is explicit that nobody knows which yet.
- **Preparation takes 100 to 120 days** from ordering the home to listing it, and Sales & Marketing owns buying the home.
- **The revision trigger sales and marketing work to is 60 to 90 days listed**, at which point a price drop is considered. Price changes are deliberately **not** automated: *"there's some art to this versus just keeping it truly mathematical."* The outcome of a 10% drop has not been measured because the CRM data behind it is not built out.
- **Nobody at Parakeet can currently describe what the website's third party does with the field mapping.** Twice on the recording: *"I don't really know how that works. Like we're not doing that, but it seems to be working."* It is the one link in the chain with no internal owner.

### Named problems

- **002 has no sales-process SOP document at all** — the file filed under it is the closing process. The core sales process exists only as Lucid flowcharts. Tier 1 Critical.
- **The rejected-offer response window has three values and a blank across four closing documents** — 3 days, 2 days, 2 days, and a missing number.
- **Two generations of the closing process are both live**, disagreeing on whether a Title Coordinator role and a Make Ready Board gate exist.
- **The Closing Walkthrough Checklist that gates key handover is [TBD — in development] in every version.**
- **The pieces that would make 002 a real process are unbuilt:** Home Listing Process, Offer Submission Process, Open House Process, Sales Rep Property Walk, Marketing Photography and "Rehab Home For-Sale As-Is Steps" are all tracker rows with partial or no drafts.

- **September 2026, added 2026-09-15.** The financing side moved and the licensing side stalled. **Triad's floor plan line went from $4.5M to $7.5M with a $2M CAP program approved (2026-09-10); 21st Mortgage's $250,000 reserve was decided and wired (2026-09-09 to 09-10)**; and the capacity number across CountryPlace, 21st and Triad that Austin wanted before deciding still does not exist, `KP-0107`. Detail and contacts on `10-Business/outside-help/lenders`, figures in `00-Meta/numbers-ledger.md`. **Georgia is blocking the dealer's license on an authorized agent requirement** (`TD-0614`), so *"licensing cleared in FL, SC and GA"* above is the March 2026 deck's claim and not the September state; and the Parakeet Home Sales renewal needs its surety bond continuation and garage liability (`TD-0615`). Two sales on 2026-09-09, TC A-11 and Fox 74, reported by Natalie. **Leslie is not on Triad's notification list**, so a denial on 09-11 reached Austin rather than Sales (`TD-0641`).
- **September 16 to 21, added 2026-09-22.** **Georgia sales tax registration is a cost decision sitting unanswered since 2026-09-16.** Melanie Sanchez-Soto to Leslie, Austin and Natalie 11:23 ET: Florida Fast Title needs *Parakeet Homes II GA LLC* and *Auburn Ridge MHC LLC* to hold Georgia sales tax numbers *"in order for us to avoid paying the taxes for the title transfers"*; the alternative is transfer tax on every Georgia title, volume not stated. Four asks on the close, no answer. `TD-0669`. **21st Mortgage funded its $250,000 escrow on 2026-09-17** (decided 09-10, released 09-17, both dates on `10-Business/outside-help/lenders.md`), **and on 2026-09-21 sent Licensing Acknowledgement Letters that have to be signed and returned before Parakeet's locations are added**; 21st cannot originate DocuSign. `TD-0686`. **21st's Applegate inspection found inventory homes still on wheels** and its set-up status request is unanswered. `TD-0668`. **Triad confirmed the inventory insurance premium method** for budgeting on 2026-09-18 and still owes the covered homes list. `TD-0677`. **The Home Sales bank accounts are moving to JPM Access** per Berman 2026-09-16, plan not confirmation. `TD-0651`. **Shirley's DBPR P2 prospectus was approved in early August and nobody here knew until Melanie asked on 2026-09-18**; recorded as a gap that closed itself. *Shirley* is Shirleys Trailer Park I and II in the warehouse (`60-Communities/portfolio-baseline-warehouse.md`), a property with no community page and an open question on the register about what and where it is (`TD-0272`); which of the two the prospectus covers is not established.

## Decisions

- 2026-08-31 — Keep listing price changes with sales and marketing rather than automating them, until the CRM data exists to show what a price drop actually does to days-to-sale. (Source: [[70-Operations/meetings/2026-08-31-listings-pipeline-and-ai-cost-consultation]])
- 2026-08-20 — Treat lender registration per community as a prerequisite; one denial has already been traced to it. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-20-car-convo-with-joe]])
- 2026-08-21 — Tell buyers to live in the home ninety days before closing out the homeowner warranty punch list, so everything surfaces through daily use. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-21-vantage-oaks-site-visit]])
- 2026-08-24 — Publish the Loan Coordinator job description immediately. (Source: [[70-Operations/meetings/2026-08-southeast-tour/2026-08-24-sam-brainstorming-session]])

## Sources

- [[80-Finance/planning/2026-executive-strategy/home pricing vs. market lot rent + loan payments.xlsx]] — the $65k/$35k cost stack, the 10%/20yr/5% terms, the $1,448 two-bedroom benchmark, the 10% POH discount and the full discount ladder to $1,569.89.
- [[70-Operations/sops/002-home-sales]] — the sales sequence, the approval clock and the missing SOP document.
- [[80-Finance/board/Parakeet - Board Presentation 2026-03 vFINAL.pdf]] — the ~400-home target at max 30% loss, the infill cost and sale price assumptions, and the dealership status.
- [[70-Operations/meetings/2026-08-31-listings-pipeline-and-ai-cost-consultation]] — the syndication chain, the My State MLS gate, the 100 to 120 day prep window and the 60 to 90 day revision trigger.
- [[00-Meta/daily-close/2026-09-10]] — the Triad change; `00-Meta/daily-close/2026-09-08.md`, `2026-09-09.md` and `2026-09-11.md` for 21st, the Georgia block and the sales. Added 2026-09-15.
- [[00-Meta/daily-close/2026-09-16]] — the Georgia sales tax ask and the 21st inventory note; `00-Meta/daily-close/2026-09-17.md` for the escrow, `2026-09-18.md` for Triad and the prospectus, `2026-09-21.md` for the licensing letters. Added 2026-09-22.

