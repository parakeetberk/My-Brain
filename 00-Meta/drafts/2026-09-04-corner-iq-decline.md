---
type: draft
tags: [type/draft, status/awaiting-address]
---

# Draft: Corner IQ decline, to Zayv and Luke

**Status:** approved wording, **not sent. Two blockers: there is no email address for Zayv or Luke anywhere, and this Brain cannot currently write drafts into Outlook at all.**

**Why this file exists.** Austin asked on 2026-09-04: *"Need to send this, where is draft located?"* **The honest answer was that it was not located anywhere a person could send it from.** It existed only as a comment record inside `00-Meta/board-data/builder/comments.json`, under key `PD-06`, second entry, timestamped 2026-09-02 07:40. **A draft parked in a board data file is a draft nobody can send**, which is why this sat for three days after being ruled. Filed here as a document 2026-09-04. **It could not be staged in Outlook Drafts: the mail connector is read-only on this tenant** - `outlook_create_draft` returns `ErrorAccessDenied` because `Mail.ReadWrite` is not consented on the app registration. **That is a second finding and it is bigger than this email**, since it means no run in this Brain can put a draft into Austin's Outlook at all, only into a file. `KP-0092`.

**The decision behind it. VERIFIED**, Austin's own words on the delegation board 2026-09-01: *"Send a draft letting Zave know that we are not moving forward more because we aren't set on our ways yet."* Decision taken 2026-08-31. **Positioning is deliberate and it is the honest reason, which is why it is worth keeping**: Parakeet is not ready to evaluate it fairly, not that there is a problem with the product.

**The blocker.** No address for either contact exists in this vault, and a search of the Parakeet mailbox for `Zayv`, `Corner IQ` and `CornerIQ` returns nothing. **The whole relationship appears to have run by phone or through somebody else's inbox.** `TD-0566` asks Austin for the address or for who has it.

**Wording is Austin's, approved 2026-09-02. Do not reword it.**

---

**To:** Zayv, copy Luke
**Subject:** Corner IQ - not moving forward right now

Zayv,

Thanks for the time on this, and for the trial batch. I want to be straight with you rather than let it drift.

We're not moving forward at the moment. It isn't the product. It's us. Our own processes aren't settled enough right now for me to evaluate what you've built fairly, and if we brought it in on top of what we're currently sorting out internally I don't think either of us would learn much from it.

I'd rather come back to you when we've got our side in order and give it a real look than string this out and waste your time.

Appreciate you and Luke both being easy to deal with through this. I'll reach back out.

Austin

---

## Related

- [[00-Meta/parked-decisions]] `PD-06`
- `10-Business/eos/to-dos.md` `TD-0258`, `TD-0566`
