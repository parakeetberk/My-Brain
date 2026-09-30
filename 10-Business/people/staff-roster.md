# Staff roster — from the SharePoint user-groups sheet

**What this is:** every named account in the new SharePoint's membership sheet — 135 rows, the most complete staff list in this vault — reconciled against the field roster and the people pages.

**Status:** current — 2026-08-31

## The facts

- Source is the `User Groups` sheet of `Data Storage Security Direction.xlsx`, filed 2026-08-31. It is a membership matrix: display name, user principal name, then one `INCL`/`NO` column per security group (15), one for `Property Operations`, and one per community (68).
- **151 rows. 135 are named accounts; 16 are the group objects themselves** (marked `Group` in the email column: AcqAM-Team, Board, Construction-Team, Exec-Team, Facilities-Team, Finance-Team, HR-Team, Offshore-AcqAM, Offshore-Fin, Offshore-Ops, Prop Ops, Regional-Mgrs, Sales-Mktg-Team, Sr Fin-Team, Sr Ops-Team, Titles-Inv-Team).
- **`DMARC` (dmarc@parakeetcommunities.com) is a service account, not a person.** It has no group and no community access, which is correct for what it is.
- **3 of the 135 are external guest accounts** — Matthew Hennessy and Philip Heller (both `_jadiancapital.com#EXT#`) and Montie Miller (`_fourstarhomes.com#EXT#`). All three have no group and no community access.
- So: **131 internal named accounts.** Of those, 41 are in at least one of the 15 security groups, 60 are in `Property Operations`, and 23 have no group and no community access at all.
- **This is the most complete staff list in the vault.** The December-2025 org chart named about 60 people. **77 named people in this sheet appear nowhere else in the vault at all.**
- **Three email namespaces, and one of them is a different company.** 129 accounts are `@parakeetcommunities.com`, 2 are `@parakeetcommunities.onmicrosoft.com` (both external guests), and **4 are `@geigerkeymarina.com`** — Bonnie Kern, Edouard Jean, Justin Hults and Pedro Mederos. That is a separate mail domain for the Geiger Key restaurant OpCo, and it means the tenant carries a second identity namespace the migration has to account for. (The earlier note that there were two such addresses undercounted: there are four.)
- **Three stray cell values** break the `INCL`/`NO` convention and need cleaning before this is used to provision anything: Anthony Prater has an `NN`, and Kenneth Gregorio and Marina Vega each have an `X`.
- **Four community columns have nobody in them:** Brunswick Estates, Cambridge, Congress and Shelle Pointe MHC. Two of those four have named on-site managers on the field roster (Brunswick Estates — Meghan Vaughn; Congress — Erica Romero), so this is a provisioning gap, not an empty community.

## Headcount reconciliation

Three sources count three different things. None is wrong; none is a total.

| Source | Count | What it is counting |
| --- | --- | --- |
| `User Groups`, 2026-08-31 | **135 named accounts** (131 internal, 3 external guests, 1 service account) | Microsoft 365 accounts that exist, whether or not the person is currently working |
| Owner, in the Structure Interview, 2026-08-30 | **~125 total employees** | People on payroll, corporate and field together |
| March-2026 board deck | **42 corporate employees** | Corporate only — excludes the on-site field entirely |

The gap between 131 and ~125 is roughly the size of the 23 accounts with no group and no community access. That is consistent with those being either unprovisioned new starters or accounts left standing after departure — but the sheet does not say which, so this is an observation, not a conclusion.

## The roster

Security groups shown as the sheet records them. `Property Operations` is the 16th access group and is listed alongside the 15. "—" means no group, or no community access.

| Name | Email | Security groups | Community access |
| --- | --- | --- | --- |
| Albert Gano | agano@parakeetcommunities.com | Exec-Team | — |
| Alex Fals | Alex@parakeetcommunities.com | AcqAM-Team | — |
| Alex Stuart | alex.s@parakeetcommunities.com | AcqAM-Team | — |
| Amanda Rice | arice@parakeetcommunities.com | Property Operations | Lake Wales, MHC, Vantage Oaks |
| Amy Furbush | afurbush@parakeetcommunities.com | Property Operations | Lake Saunders |
| Andrea Wasgatt | awasgatt@parakeetcommunities.com | — | — |
| Andrew Cooks | acooks@parakeetcommunities.com | Property Operations | Applegate, Oceanaire, Ormond Beach, Town & Country, Westwood |
| Anita Rouse | anita@parakeetcommunities.com | Property Operations | Paradise Palms, Windward Knoll |
| Anna Maria Lapitan | alapitan@parakeetcommunities.com | Offshore-AcqAM | — |
| Anthony Prater | aprater@parakeetcommunities.com | Property Operations | Northgate MH, Sea Shells, Southgate |
| Armando Rodriguez | armando@parakeetcommunities.com | Property Operations | Everglades Mobile Home Park, Hendersons, Nalls Court, Royal Palm |
| Ashlyne Godinez | ashlyne@parakeetcommunities.com | Regional-Mgrs | — |
| Austin Berk | austin@parakeetcommunities.com | Board | — |
| Auzzi Dixon | auzzi@parakeetcommunities.com | Sales-Mktg-Team, AcqAM-Team | — |
| Barb Eppley | barb@parakeetcommunities.com | Property Operations | Paradise Lakes |
| Barry Barker | bbarker@parakeetcommunities.com | Property Operations | Paradise Lakes |
| Bonnie Kern | bkern@geigerkeymarina.com | — | Geiger Key |
| Brandon Ramirez | bramirez@parakeetcommunities.com | Property Operations | Riverwalk |
| Brian Headdy | bheaddy@parakeetcommunities.com | Property Operations | Royal Oaks, Su-Rene |
| Carmin Horner | chorner@parakeetcommunities.com | Property Operations | Terrace Crossings, The Oaks |
| Charles Bailey | cbailey@parakeetcommunities.com | — | — |
| Charlie Sapp III | csapp@parakeetcommunities.com | Property Operations | Regency I & II |
| Chris Pitzer | cpitzer@parakeetcommunities.com | Facilities-Team | — |
| Christy Allen | callen@parakeetcommunities.com | Property Operations | Lamberton Lake |
| Claire Arcenas | carcenas@parakeetcommunities.com | Offshore-Ops, Offshore-AcqAM | — |
| Clarissa Andres | candres@parakeetcommunities.com | Offshore-Ops, Offshore-AcqAM | — |
| Colin Manor | cmanor@parakeetcommunities.com | — | Belle Haven, Druid Oaks, Shady Acres |
| Curtis Sterling | csterling@parakeetcommunities.com | Property Operations | Whispering Pines FL |
| Dale Myers | dmyers@parakeetcommunities.com | Property Operations | Lake Wales, MHC |
| Daniel Bennett | dbennett@parakeetcommunities.com | Finance-Team | — |
| Daniel Dumeng | ddumeng@parakeetcommunities.com | Sales-Mktg-Team | — |
| Danielle Taylor | danielle@parakeetcommunities.com | Property Operations | Fox Creek |
| David Berman | dberman@parakeetcommunities.com | Sr Fin-Team, Exec-Team, Finance-Team | — |
| David Jones | djones@parakeetcommunities.com | Facilities-Team | — |
| Demetria Loukas | Demetria@parakeetcommunities.com | HR-Team | — |
| Dennis White | dwhite@parakeetcommunities.com | Property Operations | Great Oak, Lake Saunders |
| Derek Flynn | dflynn@parakeetcommunities.com | Finance-Team, Offshore-AcqAM | — |
| DMARC | dmarc@parakeetcommunities.com | — | — |
| Donald Carter | dcarter@parakeetcommunities.com | Property Operations | Vantage Oaks |
| Dylan Lang | dlang@parakeetcommunities.com | — | — |
| Edouard Jean | ejean@geigerkeymarina.com | Property Operations | Geiger Key |
| Elmia H. Sailadin | ESailadin@parakeetcommunities.com | Offshore-Fin | — |
| Erica Romero | eromero@parakeetcommunities.com | Property Operations | Central, Harbour, Lucky Clover, Silver Breeze, Tradewinds |
| Fernando Godinez | Fernando@parakeetcommunities.com | Facilities-Team | — |
| Fredrick Motley | fmotley@parakeetcommunities.com | — | — |
| Gabriel Chacon | gchacon@parakeetcommunities.com | Construction-Team, AcqAM-Team | — |
| Gearlene Valenzuela | gvalenzuela@parakeetcommunities.com | Offshore-Fin, Offshore-AcqAM | — |
| Gena Smith | gena@parakeetcommunities.com | Property Operations | Triple S |
| George McGuire | gmcguire@parakeetcommunities.com | Construction-Team, Facilities-Team | — |
| Gigi Lendorf | glendorf@parakeetcommunities.com | Property Operations | Redlands |
| Harold Castro | hcastro@parakeetcommunities.com | Property Operations | Carley's, Riviera |
| Hesler Sanchez-Soto | hsanchez-soto@parakeetcommunities.com | — | — |
| Jade Rodriguez | jrodriguez@parakeetcommunities.com | — | — |
| Jalene Wilkes | jwilkes@parakeetcommunities.com | — | Parkwood Mobile Home Park, Silver Hill MHC, Mcgregor |
| Janeth B. Segundo | JSegundo@parakeetcommunities.com | Offshore-Fin | — |
| Jason Davis | jdavis@parakeetcommunities.com | Property Operations | Lucky Clover, Royal Oaks, Su-Rene |
| Jeremy Gray | jgray@parakeetcommunities.com | Property Operations | Greene Pointe MHC, Hershey Park, Oakside |
| Jeremy Laluzerne | jlaluzerne@parakeetcommunities.com | Property Operations | Terrace Crossings, The Oaks |
| Jhoiner Alexander Perez | jPerez@parakeetcommunities.com | Sales-Mktg-Team, Offshore-Ops | — |
| Jhosua Saet | jsaet@parakeetcommunities.com | Offshore-Ops | — |
| John Clark | jclark@parakeetcommunities.com | Exec-Team | — |
| Jon Wyss | jon@parakeetcommunities.com | Board, Exec-Team | — |
| Jordan Young | jyoung@parakeetcommunities.com | Property Operations | Central |
| Josh Flowers | jflowers@parakeetcommunities.com | Property Operations | Applegate, Oceanaire, Ormond Beach, Town & Country, Westwood |
| Juan Oliva | joliva@parakeetcommunities.com | — | Greene Pointe MHC, Hershey Park, Oakside |
| Judy Marcano | jmarcano@parakeetcommunities.com | Property Operations | Great Oak |
| Julie Emerson | jemerson@parakeetcommunities.com | Property Operations | Royal Oaks, Su-Rene |
| Julio Beltran | jbeltran@parakeetcommunities.com | — | — |
| Justin Hults | jhults@geigerkeymarina.com | Property Operations | Geiger Key |
| Justin Minkoff | justin@parakeetcommunities.com | — | — |
| Justin Robbins | JRobbins@parakeetcommunities.com | Property Operations | Auburn Ridge |
| Keiter Abreu | kabreu@parakeetcommunities.com | Offshore-Ops | — |
| Kelly Taylor | ktaylor@parakeetcommunities.com | Property Operations | Bay Oaks Village I, Bay Oaks Village II, Palm Haven Estates, Wolf Bay |
| Kenneth Gregorio | kenneth@parakeetcommunities.com | Property Operations | — |
| Koelton Keoster | kkeoster@parakeetcommunities.com | — | — |
| Kris Ruedas | kris@parakeetcommunities.com | Offshore-AcqAM | — |
| Larry Mizelle | lmizelle@parakeetcommunities.com | Property Operations | Triple S |
| Laurel McKay | lmckay@parakeetcommunities.com | Property Operations | Northgate MH |
| Leslie Croft | lcroft@parakeetcommunities.com | Exec-Team, Sales-Mktg-Team, Titles-Inv-Team | — |
| Lizinette Santiago | liz@parakeetcommunities.com | Regional-Mgrs | — |
| Lori Cornell | lcornell@parakeetcommunities.com | Property Operations | Geiger Key |
| Luis Corrales | lcorrales@parakeetcommunities.com | Property Operations | Redlands |
| Luis Mendietta | lmendietta@parakeetcommunities.com | Property Operations | Carley's, J Bar J Estates, Riviera, Shady Oaks |
| Lynette Jackson | ljackson@parakeetcommunities.com | Property Operations | Regency I & II |
| Ma Jerna Pol | majerna@parakeetcommunities.com | Offshore-AcqAM | — |
| Manny De Luna | mdeLuna@parakeetcommunities.com | — | — |
| Maria Jeriza | Maria.J@parakeetcommunities.com | Offshore-Fin | — |
| Maria Pagilyn S. Nobleza | MNobleza@parakeetcommunities.com | Offshore-Fin | — |
| Mariano Rivera | mrivera@parakeetcommunities.com | — | Belle Haven |
| Marina Vega | mvega@parakeetcommunities.com | — | — |
| Mark Anthony Vido | mark@parakeetcommunities.com | Offshore-AcqAM | — |
| Mark Rouanzion | mrouanzion@parakeetcommunities.com | Property Operations | Auburn Ridge |
| Matthew Hennessy | mhennessy_jadiancapital.com#EXT#@parakeetcommunities.com | — | — |
| Megan Vaughn | mvaughn@parakeetcommunities.com | Property Operations | Belle Haven, Druid Oaks, Shady Acres |
| Melanie Sanchez | Melanie@parakeetcommunities.com | Sales-Mktg-Team, Titles-Inv-Team | — |
| Michael Gerbasio | mgerbasio@parakeetcommunities.com | Property Operations | River Oaks |
| Michael Sablan | msablan@parakeetcommunities.com | — | — |
| Mitchell Cribbs | mcribbs@parakeetcommunities.com | Property Operations | Paradise Palms, Windward Knoll |
| Moe Mehmood | mmehmood@parakeetcommunities.com | Finance-Team | — |
| Montie Miller | MontieM_fourstarhomes.com#EXT#@parakeetcommunities.onmicrosoft.com | — | — |
| Nancy Matias | nmatias@parakeetcommunities.com | Property Operations | American, Mayflower, Meadow Woods, Monson, Whispering Pines |
| Natalie Magurne | natalie@parakeetcommunities.com | Sr Ops-Team, Exec-Team | — |
| Nicolas Sixtos Villalva | nsixtos@parakeetcommunities.com | Property Operations | Regency I & II |
| Olga Benitez | olga@parakeetcommunities.com | Property Operations | Carley's, J Bar J Estates, Shady Oaks |
| Parker Bennett | pbennett@parakeetcommunities.com | Property Operations | Riverwalk |
| Pedro Mederos | pmederos@geigerkeymarina.com | — | — |
| Philip Heller | pheller_jadiancapital.com#EXT#@parakeetcommunities.onmicrosoft.com | — | — |
| Rachael Bailey | rbailey@parakeetcommunities.com | Property Operations | Riverwalk |
| Rebekah Crowe | rcrowe@parakeetcommunities.com | Property Operations | Parkwood Mobile Home Park, Silver Hill MHC, Mcgregor |
| Rhonda Skelly | Rhonda@parakeetcommunities.com | Property Operations | Windward Knoll |
| Richard Skelly | richard@parakeetcommunities.com | Property Operations | Windward Knoll |
| Robert Dato | rdato@parakeetcommunities.com | — | — |
| Ropella Ragas | Ropella@parakeetcommunities.com | Offshore-Fin | — |
| Rose Hernandez | RHernandez@parakeetcommunities.com | Property Operations | Crystal Acres, Gulf Breeze, Hunter Springs, Palm Spring |
| Scott King | sking@parakeetcommunities.com | Property Operations | Sea Shells, Silver Breeze, Southgate |
| Shannon Novoselich | shannon.n@parakeetcommunities.com | Property Operations | — |
| Shannon Silveria | Shannon@parakeetcommunities.com | — | — |
| Sharon Wainwright | sharon@parakeetcommunities.com | Property Operations | — |
| Sheila Williams | swilliams@parakeetcommunities.com | — | — |
| Sherry Chesbrough | SChesbrough@parakeetcommunities.com | — | — |
| Shiela Mae Quinones | squinones@parakeetcommunities.com | Offshore-AcqAM | — |
| Sofronio M. Guire, Jr. | SGuire@parakeetcommunities.com | Offshore-Fin | — |
| Sony Sailadin | sony@parakeetcommunities.com | Finance-Team, Offshore-Fin | — |
| Stephanie Davenport | sdavenport@parakeetcommunities.com | Property Operations | Fox Creek |
| Tamar Balfour | tbalfour@parakeetcommunities.com | Sales-Mktg-Team | — |
| Tonya Thompson | tthompson@parakeetcommunities.com | Sales-Mktg-Team, Titles-Inv-Team | — |
| Travis Simmons | tsimmons@parakeetcommunities.com | Property Operations | Lamberton Lake |
| Travis Staley | tstaley@parakeetcommunities.com | Property Operations | Terrace Crossings, The Oaks |
| Vicki Buck | vbuck@parakeetcommunities.com | Property Operations | River Oaks |
| Vikki Nieciecki | Vikki@parakeetcommunities.com | — | — |
| Vladimir V. Baga | vbaga@parakeetcommunities.com | Offshore-Ops | — |
| William L. Pana | WPana@parakeetcommunities.com | Offshore-Fin | — |
| Zach Schwartz | zach@parakeetcommunities.com | Sr Ops-Team, Sr Fin-Team, Exec-Team | — |
| Zachary Goldberg | zgoldberg@parakeetcommunities.com | — | — |
| Zarah Mendez | zmendez@parakeetcommunities.com | — | — |## Reconciliation against the rest of the vault

### The 77 people in this sheet who appear nowhere else in the vault

Not on the December-2025 org chart, not on the field roster, and with no people page. Name, email, and what access the sheet gives them.

| Name | Email | Access |
| --- | --- | --- |
| Andrea Wasgatt | awasgatt@parakeetcommunities.com | **no group, no community access** |
| Andrew Cooks | acooks@parakeetcommunities.com | Property Operations — Applegate, Oceanaire, Ormond Beach, Town & Country, Westwood |
| Anthony Prater | aprater@parakeetcommunities.com | Property Operations — Northgate MH, Sea Shells, Southgate |
| Barry Barker | bbarker@parakeetcommunities.com | Property Operations — Paradise Lakes |
| Bonnie Kern | bkern@geigerkeymarina.com | community access only — Geiger Key |
| Brandon Ramirez | bramirez@parakeetcommunities.com | Property Operations — Riverwalk |
| Brian Headdy | bheaddy@parakeetcommunities.com | Property Operations — Royal Oaks, Su-Rene |
| Charles Bailey | cbailey@parakeetcommunities.com | **no group, no community access** |
| Charlie Sapp III | csapp@parakeetcommunities.com | Property Operations — Regency I & II |
| Claire Arcenas | carcenas@parakeetcommunities.com | Offshore-Ops, Offshore-AcqAM |
| Colin Manor | cmanor@parakeetcommunities.com | community access only — Belle Haven, Druid Oaks, Shady Acres |
| Curtis Sterling | csterling@parakeetcommunities.com | Property Operations — Whispering Pines FL |
| Dale Myers | dmyers@parakeetcommunities.com | Property Operations — Lake Wales, MHC |
| Daniel Bennett | dbennett@parakeetcommunities.com | Finance-Team |
| Daniel Dumeng | ddumeng@parakeetcommunities.com | Sales-Mktg-Team |
| Danielle Taylor | danielle@parakeetcommunities.com | Property Operations — Fox Creek |
| Dennis White | dwhite@parakeetcommunities.com | Property Operations — Great Oak, Lake Saunders |
| Donald Carter | dcarter@parakeetcommunities.com | Property Operations — Vantage Oaks |
| Dylan Lang | dlang@parakeetcommunities.com | **no group, no community access** |
| Edouard Jean | ejean@geigerkeymarina.com | Property Operations — Geiger Key |
| Elmia H. Sailadin | ESailadin@parakeetcommunities.com | Offshore-Fin |
| Fernando Godinez | Fernando@parakeetcommunities.com | Facilities-Team |
| Fredrick Motley | fmotley@parakeetcommunities.com | **no group, no community access** |
| Gabriel Chacon | gchacon@parakeetcommunities.com | Construction-Team, AcqAM-Team |
| Hesler Sanchez-Soto | hsanchez-soto@parakeetcommunities.com | **no group, no community access** |
| Jade Rodriguez | jrodriguez@parakeetcommunities.com | **no group, no community access** |
| Jalene Wilkes | jwilkes@parakeetcommunities.com | community access only — Parkwood Mobile Home Park, Silver Hill MHC, Mcgregor |
| Janeth B. Segundo | JSegundo@parakeetcommunities.com | Offshore-Fin |
| Jason Davis | jdavis@parakeetcommunities.com | Property Operations — Lucky Clover, Royal Oaks, Su-Rene |
| Jeremy Laluzerne | jlaluzerne@parakeetcommunities.com | Property Operations — Terrace Crossings, The Oaks |
| Jhosua Saet | jsaet@parakeetcommunities.com | Offshore-Ops |
| Juan Oliva | joliva@parakeetcommunities.com | community access only — Greene Pointe MHC, Hershey Park, Oakside |
| Julio Beltran | jbeltran@parakeetcommunities.com | **no group, no community access** |
| Justin Hults | jhults@geigerkeymarina.com | Property Operations — Geiger Key |
| Kenneth Gregorio | kenneth@parakeetcommunities.com | Property Operations |
| Koelton Keoster | kkeoster@parakeetcommunities.com | **no group, no community access** |
| Kris Ruedas | kris@parakeetcommunities.com | Offshore-AcqAM |
| Larry Mizelle | lmizelle@parakeetcommunities.com | Property Operations — Triple S |
| Lori Cornell | lcornell@parakeetcommunities.com | Property Operations — Geiger Key |
| Luis Corrales | lcorrales@parakeetcommunities.com | Property Operations — Redlands |
| Luis Mendietta | lmendietta@parakeetcommunities.com | Property Operations — Carley's, J Bar J Estates, Riviera, Shady Oaks |
| Lynette Jackson | ljackson@parakeetcommunities.com | Property Operations — Regency I & II |
| Manny De Luna | mdeLuna@parakeetcommunities.com | **no group, no community access** |
| Maria Jeriza | Maria.J@parakeetcommunities.com | Offshore-Fin |
| Maria Pagilyn S. Nobleza | MNobleza@parakeetcommunities.com | Offshore-Fin |
| Mariano Rivera | mrivera@parakeetcommunities.com | community access only — Belle Haven |
| Marina Vega | mvega@parakeetcommunities.com | **no group, no community access** |
| Mark Anthony Vido | mark@parakeetcommunities.com | Offshore-AcqAM |
| Mark Rouanzion | mrouanzion@parakeetcommunities.com | Property Operations — Auburn Ridge |
| Matthew Hennessy | mhennessy_jadiancapital.com#EXT#@parakeetcommunities.com | **no group, no community access** |
| Michael Gerbasio | mgerbasio@parakeetcommunities.com | Property Operations — River Oaks |
| Michael Sablan | msablan@parakeetcommunities.com | **no group, no community access** |
| Mitchell Cribbs | mcribbs@parakeetcommunities.com | Property Operations — Paradise Palms, Windward Knoll |
| Montie Miller | MontieM_fourstarhomes.com#EXT#@parakeetcommunities.onmicrosoft.com | **no group, no community access** |
| Nicolas Sixtos Villalva | nsixtos@parakeetcommunities.com | Property Operations — Regency I & II |
| Parker Bennett | pbennett@parakeetcommunities.com | Property Operations — Riverwalk |
| Pedro Mederos | pmederos@geigerkeymarina.com | **no group, no community access** |
| Philip Heller | pheller_jadiancapital.com#EXT#@parakeetcommunities.onmicrosoft.com | **no group, no community access** |
| Richard Skelly | richard@parakeetcommunities.com | Property Operations — Windward Knoll |
| Robert Dato | rdato@parakeetcommunities.com | **no group, no community access** |
| Ropella Ragas | Ropella@parakeetcommunities.com | Offshore-Fin |
| Scott King | sking@parakeetcommunities.com | Property Operations — Sea Shells, Silver Breeze, Southgate |
| Shannon Novoselich | shannon.n@parakeetcommunities.com | Property Operations |
| Shannon Silveria | Shannon@parakeetcommunities.com | **no group, no community access** |
| Sharon Wainwright | sharon@parakeetcommunities.com | Property Operations |
| Sheila Williams | swilliams@parakeetcommunities.com | **no group, no community access** |
| Sherry Chesbrough | SChesbrough@parakeetcommunities.com | **no group, no community access** |
| Shiela Mae Quinones | squinones@parakeetcommunities.com | Offshore-AcqAM |
| Sofronio M. Guire, Jr. | SGuire@parakeetcommunities.com | Offshore-Fin |
| Tamar Balfour | tbalfour@parakeetcommunities.com | Sales-Mktg-Team |
| Travis Simmons | tsimmons@parakeetcommunities.com | Property Operations — Lamberton Lake |
| Travis Staley | tstaley@parakeetcommunities.com | Property Operations — Terrace Crossings, The Oaks |
| Vikki Nieciecki | Vikki@parakeetcommunities.com | **no group, no community access** |
| Vladimir V. Baga | vbaga@parakeetcommunities.com | Offshore-Ops |
| William L. Pana | WPana@parakeetcommunities.com | Offshore-Fin |
| Zachary Goldberg | zgoldberg@parakeetcommunities.com | **no group, no community access** |
| Zarah Mendez | zmendez@parakeetcommunities.com | **no group, no community access** |
### Spelling variants — the same person under two names

The vault and the workbook disagree on four spellings. These are the same people, not new ones. Pick the workbook spelling for provisioning and the vault spelling for reading, or reconcile them.

| In `User Groups` | In the vault |
| --- | --- |
| Carmin Horner | Carmen Horner |
| Gigi Lendorf | GiGi Lendhorf |
| Megan Vaughn | Meghan Vaughn |
| Rachael Bailey | Rachel Bailey |
| Lizinette Santiago | Liznette Santiago |
| Melanie Sanchez | Melanie Sanchez-Soto |
| Alex Stuart | Alexander Stuart |
| Jon Wyss | Jonathan Wyss (as `Structure` row 1 spells him) |

**Hesler Sanchez-Soto is a different person from Melanie Sanchez-Soto.** He has an account with no group and no community access and appears nowhere else in the vault. Whether they are related is not recorded anywhere; do not assume.

### People with a vault page who are absent from this sheet

- **Alexandra Pontes, who goes by Alex** — the SR region's regional manager. She has a page in `10-Business/people/` and **no account row in this sheet at all.** She is the one confirmed current employee the workbook is missing. `Structure` row 1 records Regional-Mgrs as "Ashlyne Godinez, Liznette Santiago, TBD"; the TBD is her.

Every other person page in `10-Business/people/` has a matching row here, and all 28 named on-site managers from the field roster appear.

### Accounts with no group and no community access

23 people plus the DMARC service account. Either not yet provisioned, or no longer staff — **the sheet does not distinguish, and that distinction is the whole point.** An account that exists with no access is harmless; an account that exists for someone who has left is not.

Andrea Wasgatt, Charles Bailey, Dylan Lang, Fredrick Motley, Hesler Sanchez-Soto, Jade Rodriguez, Julio Beltran, Justin Minkoff, Koelton Keoster, Manny De Luna, Marina Vega, Michael Sablan, Pedro Mederos, Robert Dato, Shannon Silveria, Sheila Williams, Sherry Chesbrough, Vikki Nieciecki, Zachary Goldberg, Zarah Mendez — plus the three external guests Matthew Hennessy, Montie Miller and Philip Heller.

**Justin Minkoff is the one to check first.** He has a people page, he is named in `Structure` row 1 as an intended member of AcqAM-Team, and Austin counts him as one of his own team — yet his account has `NO` in every one of the 84 columns.

Three more have `Property Operations` but no community at all: **Kenneth Gregorio, Shannon Novoselich and Sharon Wainwright.** They can reach the shared operations folders and no community.

### Community naming that will not match on migration

The sheet has **68 community columns**; the vault has **67 community pages**. They do not line up cleanly.

- **`Cambridge` is a column in the sheet with no community page in the vault and nobody assigned to it.** Either a community the vault does not know about, or a stale column.
- **`Shelle Pointe MHC`** — the vault spells it Shell Pointe (`shell-pointe-mhc`). One of the two is a typo.
- **`Whispering Pines` and `Whispering Pines FL` are two separate columns.** The vault has two pages, `whispering-pines-ma` and `whispering-pines-mh-fl`, so the split is real — but the unqualified column name will be ambiguous as a group name.
- Names that differ only in form, and will still need an explicit mapping row so the folder name and the group name match: `Mcgregor` (vault: McGregor Downs), `Lake Wales, MHC` (note the comma), `Triple S` (Triple S Marina), `Great Oak` (Great Oak RV Resort), `River Oaks` (River Oaks RV Resort), `Geiger Key` (Geiger Key RV Resort), `Nalls Court` (Nalls Court MHC), `Palm Spring` (Palm Spring Estates), `Town & Country` (Town & Country MHC), `Regency I & II`, `Wolf Bay` (Parakeet Origins Wolf Bay).

**Build the name-mapping table before creating 68 groups and 68 folders**, or the folder names and the group names will drift apart on day one.

## Decisions

- None recorded yet.

## Related

- [[10-Business/people/field-roster]] — the field half of the org chart, which this sheet extends.

## Sources

- [[10-Business/sharepoint/Data Storage Security Direction.xlsx]] — the `User Groups` sheet; all names, emails, groups and community access above.
- Owner, in the Structure Interview, 2026-08-30 — the ~125 total employee figure.
- [[80-Finance/board/Parakeet - Board Presentation 2026-03 vFINAL.pdf]] — the 42 corporate employee figure.
