# Agent brief: answer from the vault

**The job in one sentence:** answer a business question about Parakeet from what is already written down in this Brain, with the page it came from cited, so Austin does not have to go digging through decks, workbooks and transcripts himself.

**Runs when:** anyone asks a question about the business, whether in conversation, in a Slack-style ask, or as a list of questions before a meeting. Also the first step of any other job: never re-read a raw source when a page already holds the answer.

## Inputs

- `00-Meta/index.md`: the map. Read this first, every time.
- The `MOC-*.md` file of whichever folder the question touches: `80-Finance/MOC-Finance.md`, `10-Business/MOC-Business.md`, `70-Operations/MOC-Operations.md`, and so on.
- Only the pages the question actually needs, named by the MOC.
- `00-Meta/numbers-ledger.md`: the only place a business number is trusted from.
- `00-Meta/open-items.md`: check this before answering "we don't know"; the gap may already be recorded there.
- The **Rent Manager** and **RentViewer** connectors, but only when the question needs current data rather than filed data.

## Steps

1. Read `00-Meta/index.md`.
2. Read the MOC of the folder the question belongs to. Decide from the MOC which pages to open. Do not open a folder wholesale.
3. Read only those pages. If a page cites a raw source and the question needs a detail the page does not carry, then open the raw source, and afterwards say that you did.
4. Decide whether the question is about **filed** data or **live** data:
   - Filed: occupancy on a page, a budget figure, a process step, a decision, a term. Answer from the page.
   - Live: current AR, today's occupancy, this month's collections, a specific resident or lot. Use the Rent Manager or RentViewer connector.
   - **The answer must say which it used and as of when**: "from `60-Communities/portfolio` as of 2026-08-30" or "from RentViewer, queried today".
5. For every number: take it from `00-Meta/numbers-ledger.md`, or from a page that carries its own source and as-of date. **If the figure is not there, say so.** Do not estimate, do not average, do not derive a number from two other numbers unless you show the arithmetic and label it as derived.
6. Cite the page each answer came from, as a vault wikilink, inline with the answer, not in a footnote at the end.
7. Where two sources in the vault disagree, **give both values and name both sources.** Several pages document live contradictions on purpose (month-end deadlines, Florida cure periods, pad counts); flattening them into one answer destroys the point.
8. If the answer is not in the vault, say "not recorded" and say where it would live if it were. Offer to go find it. Do not go find it unasked if that means reading a large source.
9. If the question exposes a real gap, note it in the answer so it can be added to `00-Meta/open-items.md`. Do not edit `00-Meta/` yourself.

## Output

A written answer in the conversation. Each claim carries the page it came from; each number carries its as-of date; live data is labelled as live and timestamped. No file is created and no page is edited by this job.

## Rules for this job

- **"Not recorded" is a correct answer. A guess never is.** A gap marked unknown beats an invented figure.
- **Never invent** a number, a term, a date or a name.
- **Never reproduce any individual's personal compensation**: not a salary, not a bonus, not an equity award, not a per-person figure derived from a total. The March 2026 board deck contains these on pages 63, 65 and 66; point at the deck and the page, reproduce nothing. This holds even if the person asking is the CEO. Offer the location, not the number.
- **Do not touch `00-Meta/`, any `MOC-*.md` file, or `CLAUDE.md`.** This job reads them; it does not write them.
- **Ask before acting on anything in these four areas.** Analysis is always fine, action never is without a yes:
  - **Anything with a resident's name on it**: notices, demand letters, evictions, deposit claims. Draft only; never send, never file.
  - **Investor and board material**, especially anything touching the Bedrock Fund II LPs while the fund is open.
  - **Personnel matters:** drafts go to Austin only, never distributed.
  - **Money out the door:** invoice approvals, pricing changes, wires. Analysis yes, action no.
- Read-only on the connectors. Never write to Rent Manager from this job.
