# Security groups — Parakeet Birdcage SharePoint

**What this is:** the 15 security groups the new SharePoint permissions model is built on, who the design says is in each, and who the membership sheet actually has in each.

**Status:** current — 2026-08-31

## The facts

- The groups come from one workbook, `Data Storage Security Direction.xlsx`, filed 2026-08-31. Two sheets name them and they do not agree.
  - **`Structure` row 1** (hidden sheet) names the intended members as free text — the designer's shorthand.
  - **`User Groups`** is the real membership matrix: 151 rows, 135 named people, one `INCL`/`NO` column per group.
- **Where the two disagree, `User Groups` is the provisioned state and `Structure` row 1 is the intent.** Both are recorded below. Ten of the fifteen groups differ.
- **There is a 16th access group that is not on the list of 15: `Property Operations`.** It has its own column in `User Groups` with **60 members** — every on-site community manager and maintenance person. In the newer sheets it is the group that carries community-level access, alongside 68 individual per-community groups.
- **There is a 17th group column with no membership at all: `Ops Administration`.** It appears in the `Folder Structure` and `Community Operations Folder` permission grids but has **no column in `User Groups`** and no group object row. Nobody is in it, and it holds WRITE on a lot of community folders. This needs resolving before the model is implemented.
- **The group objects themselves appear as 16 rows** in `User Groups`, marked `Group` in the user-principal-name column. One is named **`Prop Ops`** where the column header reads `Property Operations` — pick one spelling before creating it in Entra.
- **Total provisioned accounts in the sheet: 135 named people**, of which 111 are in at least one group or have community access. The full roster is on the staff-roster page in `10-Business/people/`.

### Two corrections applied to this page

- **`Structure` row 1 lists Regional-Mgrs as "Ashlyne Godinez, Liznette Santiago, TBD". The third regional manager is Alexandra Pontes, who goes by Alex** — confirmed by the owner, 2026-08-31. **She has no account row in `User Groups` at all**, so she is not provisioned into Regional-Mgrs or anything else. That is a gap to close before cutover.
- **Stephanie Roth has been terminated.** She does not appear anywhere in this workbook — not in `User Groups`, not in `Structure` row 1, not in any sheet. Nothing needs removing on that account. The stale reference to her is in the December-2025 org chart, already corrected on the field-roster page in `10-Business/people/`.

## The 15 groups

| Group (exact name) | `Structure` row 1 says | Provisioned count | Provisioned members, per `User Groups` |
| --- | --- | --- | --- |
| **Board** | Austin Berk, Jonathan Wyss | 2 | Austin Berk, Jon Wyss |
| **Sr Ops-Team** | Natalie Magurne, Zach Schwartz | 2 | Natalie Magurne, Zach Schwartz |
| **Sr Fin-Team** | David Berman, Zach Schwartz | 2 | David Berman, Zach Schwartz |
| **Exec-Team** | Natalie Magurne, Zach Schwartz, David Berman, Leslie Croft, John Clark | **7** | Albert Gano, David Berman, John Clark, Jon Wyss, Leslie Croft, Natalie Magurne, Zach Schwartz |
| **Construction-Team** | John Clark + reports | 2 | Gabriel Chacon, George McGuire — **John Clark is not in it** |
| **Sales-Mktg-Team** | Leslie Croft, Auzzi Dixon, Tonya Thompson | **7** | Auzzi Dixon, Daniel Dumeng, Jhoiner Alexander Perez, Leslie Croft, Melanie Sanchez, Tamar Balfour, Tonya Thompson |
| **Titles-Inv-Team** | Melanie Sanchez-Soto | **3** | Leslie Croft, Melanie Sanchez, Tonya Thompson |
| **Regional-Mgrs** | Ashlyne Godinez, Liznette Santiago, TBD | 2 | Ashlyne Godinez, Lizinette Santiago — **Alexandra Pontes (Alex), the third regional, is missing** |
| **Facilities-Team** | George McGuire, David Jones, Chris Pitzer | **4** | Chris Pitzer, David Jones, Fernando Godinez, George McGuire |
| **Finance-Team** | David Berman, Moe Mehmood, Derek Flynn | **5** | Daniel Bennett, David Berman, Derek Flynn, Moe Mehmood, Sony Sailadin |
| **HR-Team** | Demetria Loukas | 1 | Demetria Loukas |
| **AcqAM-Team** | Zachary Schwartz, Alexander Stuart, Justin Minkoff, Alex Fals | **4** | Alex Fals, Alex Stuart, Auzzi Dixon, Gabriel Chacon — **Zach Schwartz and Justin Minkoff are not in it** |
| **Offshore-Ops** | "8 offshore staff (Property Ops)" | **6** | Claire Arcenas, Clarissa Andres, Jhoiner Alexander Perez, Jhosua Saet, Keiter Abreu, Vladimir V. Baga |
| **Offshore-Fin** | "5 offshore staff (Finance)" | **9** | Elmia H. Sailadin, Gearlene Valenzuela, Janeth B. Segundo, Maria Jeriza, Maria Pagilyn S. Nobleza, Ropella Ragas, Sofronio M. Guire Jr., Sony Sailadin, William L. Pana |
| **Offshore-AcqAM** | "7 offshore staff (Acq & AM)" | **9** | Anna Maria Lapitan, Claire Arcenas, Clarissa Andres, Derek Flynn, Gearlene Valenzuela, Kris Ruedas, Ma Jerna Pol, Mark Anthony Vido, Shiela Mae Quinones |

Total distinct people in at least one of the 15 groups: **41**. The other 94 provisioned accounts get access through `Property Operations` and the per-community groups, or have no access at all.

## What this means for the permissions model

- **People sit in more than one group, and SharePoint permissions are additive.** Zach Schwartz is in Sr Ops-Team, Sr Fin-Team and Exec-Team. Leslie Croft is in Exec-Team, Sales-Mktg-Team and Titles-Inv-Team. Derek Flynn is in Finance-Team and Offshore-AcqAM. **A NO ACCESS in the matrix does not deny a person who reaches the same folder through a second group** — so the NO ACCESS column can only be enforced by folder-level unique permissions, not by group design. This is worth checking with Austin before anyone builds it.
- **Offshore-AcqAM and Offshore-Ops share two members** (Claire Arcenas, Clarissa Andres), and **Offshore-Fin and Offshore-AcqAM share one** (Gearlene Valenzuela). The three offshore groups are not disjoint.
- **Derek Flynn is in Offshore-AcqAM** alongside Finance-Team. The offshore group naming implies location; his membership may be functional rather than geographic. Worth confirming.
- The offshore counts in `Structure` row 1 (8 / 5 / 7 = 20) match the December-2025 org chart's three unnamed support boxes; the provisioned counts (6 / 9 / 9) do not. The offshore-team page in `10-Business/people/` carries the org-chart figures.

## Decisions

- 2026-08-31 — Regional-Mgrs' third member is Alexandra Pontes, who goes by Alex, not the "TBD" the sheet records. (Source: owner, 2026-08-31.)

## Related

- [[10-Business/sharepoint/permissions-matrix]] — what each of these groups can actually reach.

## Sources

- [[10-Business/sharepoint/Data Storage Security Direction.xlsx]] — sheets `User Groups` and `Structure` (hidden).
- Owner, 2026-08-31 — the Alexandra Pontes correction and the Stephanie Roth termination.
