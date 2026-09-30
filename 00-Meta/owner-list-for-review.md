# Owner list — set by Austin 2026-09-01

**What this is:** the 31 values the board's Owner dropdown offers, set by Austin on 2026-09-01. **The list is data, not code** — it lives at `00-Meta/board-data/builder/owner-canon.json` and can be edited without touching the builder.

**Status:** current — 2026-09-01, closed out the same evening. 815 rows, **zero carry an owner that is not on the list.** Austin ruled on all 20 strays: Chris Pitzer added to the list, everything else to Unassigned.

## The list

`AB/JW` · **`Accounting`** · `Acquisitions` · `Albert Gano` · `Alex Fals` · `Alex Pontes` · `Alex Stuart` · `Ashlyne Godinez` · `Asset Management` · `Austin Berk` · `Auzzi Dixon` · **`Chris Pitzer`** · `Construction` · `David Berman` · `Demetria Loukas` · `Executive Team` · `Fernando Godinez` · `Jadian` · `John Clark` · `Jon Wyss` · `Justin Minkoff` · `Leslie Croft` · `Liz Santiago` · `Mark Anthony Vido` · `Mark Doucette` · `MAV Consulting` · `Melanie Sanchez` · `Moe Mehmood` · `Natalie Magurne` · `Operations` · `Sales & Marketing` · `Unassigned` · `Zach Schwartz`

**33 values.** Chris Pitzer added 2026-09-01 for the four Vantage Oaks rows; **Accounting added the same evening** once enforcing the list showed the department had no entry.

**Nine of the 31 currently own nothing** — Acquisitions, Alex Fals, Alex Pontes, Alex Stuart, Ashlyne Godinez, Asset Management, Executive Team, Jadian, Liz Santiago. **They still appear in the dropdown at zero**, because you cannot assign work to somebody the list refuses to show.

**Austin kept department owners and named them properly**, against the recommendation to drop them: Acquisitions, Asset Management, Construction, Executive Team, Operations, Sales & Marketing. He dropped the ones that named nothing — Team, Group, Vendor.

## The one correction that moved real numbers

**Mark Doucette owns 64 rows, not 3. Natalie Magurne owns 89, not 141.**

The old matcher checked names in list order, so `Natalie` was found before `Mark` no matter where each appeared in the string. **54 property rows read `owner: Mark Doucette / Natalie Magurne` and every one of them was being counted as Natalie's.** The rule is now first-named-wins by position in the string, which is what a `/` means.

**This is worth a sanity check from Austin.** If those 54 rows are genuinely joint and Natalie is the one who reports on them, the register should say her name first, not the matcher should guess.

## The twenty strays, closed 2026-09-01

Austin's ruling: **Chris becomes Chris Pitzer; everything else becomes Unassigned.**

| Value | Rows | Now |
|---|---:|---|
| `Team` | 8 | Unassigned |
| `Chris` | 4 | **Chris Pitzer**, added to the list |
| `Vendor` | 3 | Unassigned |
| `Heidi` | 1 | Unassigned |
| `Joe` | 1 | Unassigned |
| `Alex` | 1 | Unassigned |
| `Regional Manager` | 1 | Unassigned |
| `Group` | 1 | Unassigned |

**The unowned count went UP, from 251 to 285, and that is the ruling working rather than failing.** A row owned by "Team" or "Vendor" was never owned; it was an unowned row wearing a name, and it was not being counted. **Eighteen rows just became visible as work nobody has.**

### The gap enforcing the list found, and closed

**`KP-0011` and `KP-0012` fell to Unassigned**, because both read `Accounting team — proposed lead: Moe Mehmood` and the list had **Acquisitions, Asset Management, Construction, Executive Team, Operations and Sales & Marketing but no Accounting** — the one department Austin had named by hand that same morning when he assigned the Responsible Contractor block to *"the accounting team"*.

**`Accounting` added 2026-09-01 on Austin's word.** Three rows moved to it: `KP-0011`, `KP-0012` and `TD-0274`, which read `Accounting (Berman, Bennett, Moe)` and had been resolving to David Berman on the strength of his name appearing in the bracket. **That third one is the useful catch** — the row names a department and a roster, and it was being counted against a man who is on his way out.

Unowned settled at **267**, down from 285. `Moe Mehmood` was still not substituted anywhere: the registers say *proposed lead*, and that is not the same as accepted.

## Fixed in the registers, not just mapped

Five bare names were rewritten in the source files rather than aliased, because the register was wrong and an alias would have hidden that.

- `TD-0278`, `TD-0279` — `Zach` → **Zach Schwartz**. Both are RentViewer warehouse and Rent Manager API failures, which is his rollout. Not Zach Wallack, who is Massachusetts litigation.
- `TD-0247`, `PF-0277` — `Justin` → **Justin Minkoff**. Both are Rent Manager data, which he owns.
- `PR-0005` — `Mark` → **Mark Doucette**. *"Mark's rehab crew"*, and rehab is his.
- `PR-0033` — `Regional manager` → **Alex Pontes**, the Belle Haven regional per the portfolio sheet.

## Names to watch

- **`Melanie Sanchez` is your spelling; the staff roster says the same and the vault pages say `Melanie Sanchez-Soto`.** The alias maps all three. `Hesler Sanchez-Soto` is a different person.
- **`Liz Santiago` is your spelling; the portfolio sheet says `Liznette Santiago` and the roster says `Lizinette Santiago`.** All three map to Liz Santiago. **The roster and the portfolio sheet disagree with each other on her name**, which is a `KP-0023` problem, not a dropdown problem.
- **`Zach` alone is now ambiguous** — Zach Schwartz internal, Zach Wallack outside counsel. Surnames on anything Massachusetts.

## Related

- `00-Meta/board-data/builder/owner-canon.json` — the list and the alias map. Edit here.
- [[10-Business/people/staff-roster]] — the 209 provisioned accounts.
- [[00-Meta/open-board]]
