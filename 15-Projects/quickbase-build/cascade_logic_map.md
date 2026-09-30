# Cascading Dropdown Logic Map — All Form Contexts

## Master Hierarchy
Community → Lot → Asset

## Filter Rules by Form

| Form | Community Filter | Lot Filter | Asset Filter | Notes |
|---|---|---|---|---|
| Home Listing Request | All communities | All lots in community | All assets on lot | Standard cascade |
| Home Listing Confirmation | All communities | All lots in community | Assets with status = Listed | Confirming an already-listed asset |
| Offer to Purchase/Rent | All communities | Lots where asset status = Listed (Active for sale/rent) | Listed assets on that lot | Buyer/renter sees only what's for sale/rent |
| Utility Request | All communities | All lots in community | No asset field needed | Utility is lot-level |
| Weekly Maintenance | Community only | N/A | N/A | Community-level form |
| Incident Report | Community only | Optional lot (free text ok) | No asset | Location is community or lot — not asset-specific |
| Monthly Equipment | Community only | N/A | N/A | Community-level |
| Month End Checklist | Community only | N/A | N/A | Community-level |
| Move Out Inspection | All communities | OCCUPIED lots only | Assets on that lot | Only lots where Lot Status = Occupied |
| Resident Info Sheet | All communities | All lots in community | No asset field | Data entry — all lots visible |
| Community Site Visit | Community only | N/A | N/A | Community-level inspection |
| Rehab Walkthrough | All communities | Lots with assets where asset status = Rehab/In Progress | Assets on that lot in rehab | Only rehab-stage assets |
| Move In / Move Out Request | All communities | STATUS-DEPENDENT (see below) | STATUS-DEPENDENT | Most complex cascade |

## Move In / Move Out — Detailed Cascade Logic

### When Move In is selected:
- Community → Lot: Show ONLY lots where Lot Status = Available (vacant, no active resident)
- Lot → Asset: 
  - If "Was this a sale of Community Owned Home?" = YES → show assets on that lot with status = Listed or Active
  - If "Was this a sale of Community Owned Home?" = NO (lot-only move-in) → no asset selection needed

### When Move Out is selected:
- Community → Lot: Show ONLY lots where Lot Status = Occupied (has active resident)
- Lot → Asset: Show asset(s) on that lot (the home being vacated/moved out)

## Lot Status Values (drives filter behavior)
- Available — vacant, no active resident → show in Move In filter
- Occupied — has active resident → show in Move Out filter  
- Reserved — lot committed but not yet moved in → NEITHER Move In nor Move Out
- Demo — demolition/clearance → exclude from all resident-facing forms

## Asset Status Values (drives filter behavior)
- Ordered → show only in Home Ordering workflow forms
- In Production → show only in Home Ordering workflow forms
- Delivered → show only in Construction Inspection / Ops Readiness
- Listed → show in Offer to Purchase form, Home Listing Confirmation
- Active/Occupied → show in Move Out, Inspections, Rehab
- In Storage → show in Home Ordering workflow, storage tracking
- In Rehab → show in Rehab Walkthrough form

## QB Implementation Notes
- All Community, Lot, Asset fields on QB forms MUST be relationship fields (not free-text)
- Community → Lots: one-to-many relationship (1 Community : many Lots)
- Lots → Assets: one-to-many relationship (1 Lot : many Assets; usually 1 active asset per lot at a time)
- QB form field setting: "Filter related records" by matching Community field + status field as needed
- Lot Status and Asset Status are the two key filter fields — must be maintained in real time
- Gate rule: Lot Status and Asset Status must be updated at every stage transition in QB automations

## FastField Implementation Notes
- FastField cascading dropdowns require a synced data source (QB data via API or exported CSV)
- Community → Lot: supported via FastField cascading dropdown linked to QB Lots table
- Status-based filtering in FastField: requires pre-configured form templates per use case
  (e.g., Delivery Confirmation form is pre-filtered to show only "Delivery Scheduled" stage lots)
- Full real-time status filtering in FastField requires FastField Enterprise API integration
- Fallback: Pre-populate Community and Lot on FastField form from QB (QR code or link launch) so field staff don't hand-select — eliminates filtering problem for most field forms

## New Fields Needed on Lots Table (additions to spec)
- Has Active Asset [Formula-Checkbox]: True if count of linked assets > 0 and asset status ≠ Archived
- Active Asset Status [Lookup]: Pulls status of the active asset on this lot
- Current Resident Name [Lookup or Text]: Who is currently occupying (for Move Out filter UX)
- Lot Status [already in spec]: Available / Occupied / Reserved / Demo — MUST be kept current by automations

## Automation Updates Needed
- Any time an asset reaches "Listed — Complete" stage → set Lot Status = Reserved (in-sale limbo) 
- Any time Move In is processed → set Lot Status = Occupied
- Any time Move Out is processed → set Lot Status = Available (reset)
- Any time a new Home Order is created for a lot → set Lot Status = Reserved
- Any time Delivery is confirmed → no Lot Status change (home is there but lot status stays Reserved until resident moves in)
