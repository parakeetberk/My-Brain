# Skill: the Page Update

Based on Andrej Karpathy's LLM Wiki pattern: instead of re-reading raw files every session, Claude maintains one page per durable topic and reads those. The pages are the memory; raw files are where memories come from. In this Brain the pages live *inside the business folders*: a pricing page in `50-Products-Sales/`, a key-account page in `30-Customers/`. They never sit in a separate wiki pile.

To run it: tell Claude "run the Page Update", or paste everything below the line.

---

You are updating the knowledge pages of this AI Brain.

## The rules

1. **One page per durable topic, in the folder that owns it.** A topic earns a page when it will still matter in three months. No pages for one-off trivia.
2. **Update, don't re-read.** When new information arrives (a filed transcript, a new document, something the user tells you), push the durable facts onto the relevant page. Future sessions read the page, not the raw source.
3. **Format follows the example.** Every page matches the shape of `10-Business/_example-page.md`: what this is, the facts, decisions with dates, related links, sources.
4. **Numbers go to the ledger first.** A money figure belongs in `00-Meta/numbers-ledger.md` with a source and as-of date; pages cite the ledger, they don't carry their own copies. Dates, terms and decision thresholds may sit on a page as long as the ledger has them too.
5. **The MOC does the linking; the page barely links.** A page is connected because its folder's MOC lists it. On the page, wikilink only the one or two documents it was actually built from, plus at most one Related page that genuinely explains it. Never link the ledger, the business-model page, the index, or siblings out of habit. Hubs with spokes are readable; everything-links-everything is not.
6. **Cite the ledger by name, don't link it.** "Figures in `00-Meta/numbers-ledger.md`" in plain text. A wikilink from every page turns the ledger into a false hub.
7. **Cite pages when answering.** Answers about the business name the page they came from.
8. **Keep the maps current.** Page added, renamed, or retired → its row in `00-Meta/index.md` and its folder's MOC file list change in the same session, both as `[[wikilinks]]`.
9. **Hard rules apply.** Never delete a page without asking. Never put a number on a page without the ledger behind it.

## The job, this run

1. Look at what's new since the pages were last touched: `05-Inbox/`, recent filed transcripts, new documents.
2. List the pages you'd update or create because of it, one line each, and ask before proceeding. Durable topics usually include: each client or key account · each person on the team and each outside supplier · each offer or service line · each process or SOP · each meeting on file · each live proposal or project · the tools the business runs on · the business itself. Thin topics share a page; nothing that will matter in three months goes without one.
3. On the yes: make the updates, add the wikilinks, update the index and the MOCs, add a `00-Meta/log.md` line, and report back: pages touched, one line on what changed in each.
