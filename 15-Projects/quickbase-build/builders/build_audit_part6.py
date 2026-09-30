import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.load_workbook("/home/ubuntu/parakeet_jotform_audit.xlsx")

NAVY = "2F4E65"; GREEN = "4ABA81"; LIGHT_GRAY = "F2F2F2"; WHITE = "FFFFFF"; GRAY_TAB = "999999"; RED_TAB = "F16262"
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
header_fill = PatternFill(start_color=NAVY, end_color=NAVY, fill_type="solid")
data_font = Font(name="Calibri", size=10)
bold_font = Font(name="Calibri", size=10, bold=True)
green_fill = PatternFill(start_color=GREEN, end_color=GREEN, fill_type="solid")
gray_fill = PatternFill(start_color=LIGHT_GRAY, end_color=LIGHT_GRAY, fill_type="solid")
white_fill = PatternFill(start_color=WHITE, end_color=WHITE, fill_type="solid")
section_fill = PatternFill(start_color="E8E8E8", end_color="E8E8E8", fill_type="solid")
thin_border = Border(left=Side(style="thin", color="D0D0D0"), right=Side(style="thin", color="D0D0D0"),
                     top=Side(style="thin", color="D0D0D0"), bottom=Side(style="thin", color="D0D0D0"))
wrap = Alignment(wrap_text=True, vertical="top")
FORM_HEADERS = ["Section Name", "Field Name", "Field Type", "Required", "Options/Values",
                "Conditional Logic", "QB Target Field", "FastField?", "Migration Notes"]

def add_form_tab(wb, tab_name, fields, tab_color=GRAY_TAB):
    ws = wb.create_sheet(title=tab_name[:31])
    ws.sheet_properties.tabColor = tab_color
    for c, h in enumerate(FORM_HEADERS, 1):
        cell = ws.cell(row=1, column=c, value=h)
        cell.font = header_font; cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    ws.freeze_panes = "A2"
    row_idx = 2; dc = 0
    for f in fields:
        is_sec = (f[1] is None)
        for c, val in enumerate(f, 1):
            cell = ws.cell(row=row_idx, column=c, value=val if val is not None else "")
            cell.border = thin_border; cell.alignment = wrap
            if is_sec: cell.font = bold_font; cell.fill = section_fill
            else:
                cell.font = data_font; cell.fill = gray_fill if dc % 2 == 0 else white_fill
                if c == 4 and str(val).strip().lower() == "yes": cell.fill = green_fill
        if not is_sec: dc += 1
        row_idx += 1
    for c in range(1, 10):
        mx = 12
        for row in ws.iter_rows(min_col=c, max_col=c):
            for cell in row:
                if cell.value: mx = max(mx, min(len(str(cell.value)), 42))
        ws.column_dimensions[get_column_letter(c)].width = mx + 2
    ws.column_dimensions["E"].width = 45; ws.column_dimensions["F"].width = 35
    ws.column_dimensions["G"].width = 30; ws.column_dimensions["I"].width = 30

# FORM 11: Community Site Visit Inspection
def sv(sec, name):
    return (sec, name, "Dropdown", "No", "GOOD / MONITOR / REPAIR / N/A", "None", f"Site Visits > {name}", "Yes", "")

f11 = [
    ("Header", None, None, None, None, None, None, None, None),
    ("Header", "Date", "Date", "No", "", "None", "Site Visits > Date", "Yes", ""),
    ("Header", "Community", "Dropdown", "No", "65-community dropdown", "None", "Site Visits > Community", "Yes", ""),
    ("Header", "Email", "Email", "No", "", "None", "Site Visits > Inspector Email", "Yes", ""),
    ("Entrance & Curb Appeal", None, None, None, None, None, None, None, None),
    sv("Entrance & Curb Appeal", "Entry Signs"), sv("Entrance & Curb Appeal", "Fencing"),
    sv("Entrance & Curb Appeal", "Landscaping"), sv("Entrance & Curb Appeal", "Front Gates"),
    sv("Entrance & Curb Appeal", "Overall Feeling"),
    ("Roads", None, None, None, None, None, None, None, None),
    sv("Roads", "Streets Condition"), sv("Roads", "Curbs/Gutters/Shoulders"),
    sv("Roads", "Parking Areas"), sv("Roads", "Parking Lot Striping"),
    sv("Roads", "Road Striping"), sv("Roads", "Sidewalks & Patios"),
    ("Common Areas", None, None, None, None, None, None, None, None),
    sv("Common Areas", "Other Common Areas"), sv("Common Areas", "Landscaping Office/Clubhouse"),
    sv("Common Areas", "Trees Trim/Safety"), sv("Common Areas", "Ponds/Lake"),
    sv("Common Areas", "Fireplugs"), sv("Common Areas", "Mailbox Area"),
    sv("Common Areas", "In-Park Signage"), sv("Common Areas", "Perimeter Fencing"),
    sv("Common Areas", "Trash Area"), sv("Common Areas", "RV Storage Area"),
    sv("Common Areas", "Flagpole & Flags"),
    ("Other Common Areas", None, None, None, None, None, None, None, None),
    sv("Other Common Areas", "Clubhouse Exterior"), sv("Other Common Areas", "Clubhouse Interior"),
    sv("Other Common Areas", "Bathrooms Cleanliness"), sv("Other Common Areas", "Office"),
    sv("Other Common Areas", "Utility Storage"), sv("Other Common Areas", "Maintenance Yard Outside"),
    sv("Other Common Areas", "Maintenance Building Inside"),
    ("Vacant Lots", None, None, None, None, None, None, None, None),
    sv("Vacant Lots", "Cleaned/Filled/Graded/Crowned"),
    sv("Vacant Lots", "Utility Panels Secured"),
    sv("Vacant Lots", "Utilities Properly Painted (B/G/O/R)"),
    ("Amenities", None, None, None, None, None, None, None, None),
    sv("Amenities", "Swimming Pool"), sv("Amenities", "Pool Area"),
    sv("Amenities", "Playground"), sv("Amenities", "Other Recreational Facilities"),
    sv("Amenities", "Golf Cart"),
    ("Resident Homes & Home Sites", None, None, None, None, None, None, None, None),
    sv("Resident Homes", "Home Exterior Surfaces"), sv("Resident Homes", "Skirting"),
    sv("Resident Homes", "Steps & Decks"), sv("Resident Homes", "Carports/Additions/Parking"),
    sv("Resident Homes", "Home Sites Cleanliness"), sv("Resident Homes", "Home Sites Landscaping"),
    sv("Resident Homes", "Home Sites Grass"), sv("Resident Homes", "Storage Sheds"),
    sv("Resident Homes", "Pets"), sv("Resident Homes", "Inoperative Vehicles"),
    sv("Resident Homes", "House Numbering"), sv("Resident Homes", "Parking Pads"),
    sv("Resident Homes", "Sidewalks & Walkways"),
    ("Sales/Rental Appearance", None, None, None, None, None, None, None, None),
    sv("Sales/Rental", "Banners/Signs at Entrance"), sv("Sales/Rental", "Sales Brochures in Box"),
    sv("Sales/Rental", "Home Exterior"), sv("Sales/Rental", "Skirting"),
    sv("Sales/Rental", "Steps & Deck"), sv("Sales/Rental", "Vacant Rental Interiors"),
    sv("Sales/Rental", "Vacant Rental Landscaping"), sv("Sales/Rental", "Vacant Rental Grass"),
    sv("Sales/Rental", "Vacant Rental Storage Sheds"), sv("Sales/Rental", "Occupied Rentals Cleanliness"),
    sv("Sales/Rental", "Occupied Rentals Landscaping"), sv("Sales/Rental", "Occupied Rentals Grass"),
]
add_form_tab(wb, "11-Site Visit Insp", f11)

# FORM 12: Rehab Walkthrough Punchlist
def rehab(sec, name, ftype="Checkbox", opts="Yes / No"):
    return (sec, name, ftype, "No", opts, "None", f"Rehab > {name}", "Yes", "")

f12 = [
    ("Personal Information", None, None, None, None, None, None, None, None),
    ("Personal Information", "Community", "Dropdown", "No", "65-community dropdown", "None", "Rehab > Community", "Yes", ""),
    ("Personal Information", "Unit", "Text", "No", "", "None", "Rehab > Unit", "Yes", ""),
    ("Personal Information", "Email", "Email", "No", "", "None", "Rehab > Email", "Yes", ""),
    ("Personal Information", "Manager Name", "Text", "No", "", "None", "Rehab > Manager", "Yes", ""),
    ("Personal Information", "Manager Email", "Email", "No", "", "None", "Rehab > Manager Email", "Yes", ""),
    ("Personal Information", "Date of Walkthrough", "Date", "No", "", "None", "Rehab > Date", "Yes", ""),
    ("Interior Condition", None, None, None, None, None, None, None, None),
    rehab("Interior", "Home Smells Clean"), rehab("Interior", "No Trash/Debris"),
    rehab("Interior", "Floors Swept/Mopped/Vacuumed"), rehab("Interior", "Cabinets/Counters/Appliances Cleaned"),
    rehab("Interior", "Blinds Installed/Clean/Working"), rehab("Interior", "Outlet/Switch Covers Installed"),
    rehab("Interior", "Interior Bulbs Working"), rehab("Interior", "Smoke Detectors Working"),
    rehab("Interior", "Bath/Toilets/Sinks Cleaned"), rehab("Interior", "Windows Cleaned"),
    ("Doors/Hardware/Safety", None, None, None, None, None, None, None, None),
    rehab("Doors/Hardware", "Front Door Handle/Lock Good or Replaced"),
    rehab("Doors/Hardware", "Deadbolt Works/Keys Labeled"),
    rehab("Doors/Hardware", "Interior/Closet Doors Work"),
    rehab("Doors/Hardware", "Windows Open/Close/Lock"),
    rehab("Doors/Hardware", "Steps/Porch/Handrails Safe"),
    ("Kitchen/Appliances", None, None, None, None, None, None, None, None),
    rehab("Kitchen", "Refrigerator Clean/Working"), rehab("Kitchen", "Stove/Oven Clean/Working"),
    rehab("Kitchen", "Dishwasher/Range Hood Works"), rehab("Kitchen", "Sink/Faucet Works"),
    rehab("Kitchen", "No Leaks Under Sink"), rehab("Kitchen", "Cabinets/Drawers Work"),
    ("Bathrooms/Plumbing", None, None, None, None, None, None, None, None),
    rehab("Bathrooms", "New Toilet Seat Installed"), rehab("Bathrooms", "Toilet Flushes"),
    rehab("Bathrooms", "Sink/Shower/Tub Work"), rehab("Bathrooms", "No Leaks"),
    rehab("Bathrooms", "Mirror/Vanity/Towel Bar Secure"), rehab("Bathrooms", "Caulking Clean/Complete"),
    ("Utilities/Vacant Home Check", None, None, None, None, None, None, None, None),
    rehab("Utilities", "Electric On/Staying On"), rehab("Utilities", "Water On/Staying On"),
    rehab("Utilities", "Heat/AC Works"), rehab("Utilities", "Toilets Flushed/Water Run in Sinks"),
    rehab("Utilities", "Checked for Leaks/Odors/Pests/Vandalism"),
    ("Exterior/Landscaping", None, None, None, None, None, None, None, None),
    rehab("Exterior", "Exterior Clean/Power Washed"), rehab("Exterior", "Skirting Secure/Presentable"),
    rehab("Exterior", "Yard Cleaned/Grass Cut/Weeds Handled"), rehab("Exterior", "Landscaping Complete or Assigned"),
    ("Exterior/Landscaping", "Landscaping Owner", "Dropdown", "No", "Maintenance / Manager / Vendor", "None", "Rehab > Landscaping Owner", "Yes", ""),
    ("Post Walk Through Status", None, None, None, None, None, None, None, None),
    ("Post Walk Through Status", "Status", "Dropdown", "No", "Approved as Ready to Market / Needs Additional Items / Not Ready / Vendor Needs to Finish", "None", "Rehab > Status", "Yes", "OPEN ITEM: Separate workflow from Home Ordering"),
    ("Post Walk Through Status", "Manager/Inspector Signature", "Signature", "No", "", "None", "Rehab > Signature", "Yes", ""),
]
add_form_tab(wb, "12-Rehab Punchlist", f12)

# FORM 13: Move In / Move Out Request
f13 = [
    ("General Information", None, None, None, None, None, None, None, None),
    ("General Information", "Community", "Dropdown", "No", "65-community dropdown", "None", "Move In/Out > Community", "No", ""),
    ("General Information", "Regional Manager", "Text", "No", "", "None", "Move In/Out > Regional Manager", "No", "Auto-populate from community"),
    ("General Information", "Lot/Unit Name", "Text", "No", "", "None", "Move In/Out > Lot/Unit", "No", ""),
    ("General Information", "Resident Name", "Text", "No", "", "None", "Move In/Out > Resident Name", "No", ""),
    ("General Information", "Move In or Move Out", "Radio", "No", "Move In / Move Out", "Drives conditional sections below", "Move In/Out > Type", "No", ""),
    ("Move In (conditional)", None, None, None, None, None, None, None, None),
    ("Move In", "Type", "Radio", "No", "Lot Only / Rental", "Visible if Move In selected", "Move In/Out > Move In Type", "No", ""),
    ("Move In", "Was This a Community Home Sale", "Radio", "No", "Yes / No", "Visible if Move In", "Move In/Out > Home Sale", "No", ""),
    ("Move In", "Sale Amount", "Currency", "No", "", "Visible if Home Sale = Yes", "Move In/Out > Sale Amount", "No", ""),
    ("Move In", "Upload Bill of Sale", "File Upload", "No", "", "Visible if Home Sale = Yes", "Move In/Out > Bill of Sale", "No", ""),
    ("Move In", "Length of Stay", "Radio", "No", "Short Term / Long Term", "Visible if Move In", "Move In/Out > Length of Stay", "No", ""),
    ("Move In", "Date of Move In", "Date", "No", "", "Visible if Move In", "Move In/Out > Move In Date", "No", ""),
    ("Move In", "Monthly Lot Rent", "Currency", "No", "", "Visible if Move In", "Move In/Out > Lot Rent", "No", ""),
    ("Move In", "Monthly Home Rent Portion", "Currency", "No", "", "Visible if Move In", "Move In/Out > Home Rent", "No", ""),
    ("Move In", "Security Deposit Amount", "Currency", "No", "", "Visible if Move In", "Move In/Out > Security Deposit", "No", ""),
    ("Move In", "Additional Recurring Fees", "Radio", "No", "Yes / No", "Visible if Move In", "Move In/Out > Has Add'l Fees", "No", ""),
    ("Move In", "List Additional Fees", "Textarea", "No", "", "Visible if Add'l Fees = Yes", "Move In/Out > Add'l Fees Detail", "No", ""),
    ("Move In", "First Month Pro-Rated", "Radio", "No", "Yes / No", "Visible if Move In", "Move In/Out > Pro-Rated", "No", ""),
    ("Move In", "Pro-Rated Rent Amount", "Currency", "No", "", "Visible if Pro-Rated = Yes", "Move In/Out > Pro-Rated Amt", "No", ""),
    ("Move In", "Lease Fully Executed", "Radio", "No", "Yes / No", "Visible if Move In", "Move In/Out > Lease Executed", "No", ""),
    ("Move In", "Upload Signed Lease", "File Upload", "No", "", "Visible if Lease = Yes", "Move In/Out > Lease Upload", "No", ""),
    ("Move Out (conditional)", None, None, None, None, None, None, None, None),
    ("Move Out", "Move Out Type", "Dropdown", "No", "Lot Only / Home / Rental / RV", "Visible if Move Out selected", "Move In/Out > Move Out Type", "No", ""),
    ("Move Out", "Date of Notice Given", "Date", "No", "", "Visible if Move Out", "Move In/Out > Notice Date", "No", ""),
    ("Move Out", "Move Out Date", "Date", "No", "", "Visible if Move Out", "Move In/Out > Move Out Date", "No", ""),
    ("Move Out", "Security Deposit on File", "Currency", "No", "", "Visible if Move Out", "Move In/Out > Deposit on File", "No", ""),
    ("Move Out", "Reason", "Dropdown", "No", "Sale to New Resident / Sale to Community / Rental Term Exp / Lease Exp / Eviction Post Auction / Broken Lease / Skip Out / Other", "Visible if Move Out", "Move In/Out > Move Out Reason", "No", ""),
    ("Move Out", "Bill of Sale Upload", "File Upload", "No", "", "Visible if reason = Sale", "Move In/Out > Move Out BOS", "No", ""),
    ("Move Out", "Auction Paperwork Upload", "File Upload", "No", "", "Visible if reason = Eviction", "Move In/Out > Auction Docs", "No", ""),
    ("Move Out", "Email of Inspector", "Email", "No", "", "Visible if Move Out", "Move In/Out > Inspector Email", "No", ""),
    ("Requestor Information", None, None, None, None, None, None, None, None),
    ("Requestor Information", "Name", "Text", "No", "", "None", "Move In/Out > Requestor Name", "No", ""),
    ("Requestor Information", "Email", "Email", "No", "", "None", "Move In/Out > Requestor Email", "No", ""),
    ("Requestor Information", "Phone", "Phone", "No", "", "None", "Move In/Out > Requestor Phone", "No", ""),
    ("Requestor Information", "Signature", "Signature", "No", "", "None", "Move In/Out > Signature", "No", ""),
]
add_form_tab(wb, "13-Move In Out", f13)

# ============================================================
# TAB 15: OPEN ITEMS — Forms
# ============================================================
ws_open = wb.create_sheet(title="OPEN ITEMS — Forms")
ws_open.sheet_properties.tabColor = RED_TAB
open_headers = ["Item #", "Form Name", "Question / Issue", "Owner", "Status", "Notes"]
for c, h in enumerate(open_headers, 1):
    cell = ws_open.cell(row=1, column=c, value=h)
    cell.font = header_font; cell.fill = header_fill
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = thin_border
ws_open.freeze_panes = "A2"

open_items = [
    [1, "Home Listing Confirmation", "Only 4 fields. Is this intentionally minimal or is it a placeholder? Does it trigger any downstream action in QB?", "Product Owner", "Open", ""],
    [2, "Home Listing Request Form", "Suggested Monthly Rental Price AND Suggested Sale Price are both required fields. Logic: should one be hidden based on \"For Rent\" vs \"For Sale\" selection?", "Product Owner", "Open", "Likely conditional — needs confirmation"],
    [3, "Offer to Purchase/Rent", "\"Upload Signed PSA\" — where does this file go? QB attachment or SharePoint?", "IT / Product Owner", "Open", "Drives file storage architecture"],
    [4, "Utility Request Application", "References JotForm utility alert from Ops readiness form. This is likely the same form. Confirm: is this replacing the JotForm utility alert process?", "Operations", "Open", "May consolidate with Home Ordering utility step"],
    [5, "Weekly Maintenance Checklist", "Uses a different community list than other forms (appears to be a different dataset). Reconcile with master community dropdown.", "Operations", "Open", "Inconsistent community data"],
    [6, "Monthly Equipment & Inventory", "Community field shows \"Community 1, 2, 3, 4, Other\" — placeholder, not real data. Needs real community dropdown.", "Operations", "Open", "Placeholder values — not production-ready"],
    [7, "Month End Checklist", "References Rent Manager in several items (\"Notes in Rent Manager\", \"Prospects in Rent Manager\"). These will still route to RM. Confirm which items stay RM-only vs QB tracked.", "Product Owner", "Open", "Determines QB table scope"],
    [8, "Move Out Inspection", "Uses Excellent/Good/Fair/Poor rating scale. The Home Ordering spec uses Pass/Fail/N/A. Confirm: keep distinct rating scales per form type, or standardize?", "Product Owner", "Open", "Standardization decision"],
    [9, "Resident Information Sheet", "This is largely a data collection form. Most fields mirror Rent Manager fields. Confirm: is this form becoming QB intake → sync to RM, or staying as a standalone form?", "Product Owner / IT", "Open", "Drives integration architecture"],
    [10, "Community Site Visit Inspection", "Who owns this form (Regional Manager? Director?)? Frequency: weekly, monthly, per visit?", "Operations", "Open", "Determines workflow rules and notifications"],
    [11, "Rehab Walkthrough Punchlist", "Status field: \"Approved as Ready to Market / Needs Additional Items / Not Ready / Vendor Needs to Finish.\" This is a separate workflow from Home Ordering. Will Rehab be built as Workflow #002?", "Product Owner", "Open", "Scope decision — separate build phase"],
    [12, "Move In / Move Out Request", "This form triggers Rent Manager entries. Will QB be the submission layer that then notifies the RM admin, or will this be a direct RM workflow?", "Product Owner / IT", "Open", "Drives integration pattern"],
    [13, "ALL FORMS", "Community dropdown lists are inconsistent across forms (some have 65+, some have fewer, Weekly Maintenance has a completely different list). One master community list needs to be defined and applied to all forms.", "Operations / IT", "Open", "CRITICAL — foundational data issue"],
]

for i, row_data in enumerate(open_items):
    r = i + 2
    for c, val in enumerate(row_data, 1):
        cell = ws_open.cell(row=r, column=c, value=val)
        cell.font = data_font
        cell.fill = gray_fill if i % 2 == 0 else white_fill
        cell.alignment = wrap
        cell.border = thin_border

# Auto-width open items
ws_open.column_dimensions["A"].width = 10
ws_open.column_dimensions["B"].width = 30
ws_open.column_dimensions["C"].width = 70
ws_open.column_dimensions["D"].width = 20
ws_open.column_dimensions["E"].width = 12
ws_open.column_dimensions["F"].width = 40

wb.save("/home/ubuntu/parakeet_jotform_audit.xlsx")
print("Part 6 done — Forms 11-13 + Open Items")
