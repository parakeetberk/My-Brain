import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, numbers
from openpyxl.utils import get_column_letter
from copy import copy

wb = openpyxl.Workbook()

# === STYLE DEFINITIONS ===
NAVY = "2F4E65"
GREEN = "4ABA81"
RED = "F16262"
YELLOW = "FFCC3B"
LIGHT_GRAY = "F2F2F2"
WHITE = "FFFFFF"

header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
header_fill = PatternFill(start_color=NAVY, end_color=NAVY, fill_type="solid")
data_font = Font(name="Calibri", size=10)
data_font_blue = Font(name="Calibri", size=10, color="0000FF")
bold_font = Font(name="Calibri", size=10, bold=True)
title_font = Font(name="Calibri", size=14, bold=True, color=NAVY)
subtitle_font = Font(name="Calibri", size=11, color="666666")
green_fill = PatternFill(start_color=GREEN, end_color=GREEN, fill_type="solid")
red_fill = PatternFill(start_color=RED, end_color=RED, fill_type="solid")
yellow_fill = PatternFill(start_color=YELLOW, end_color=YELLOW, fill_type="solid")
gray_fill = PatternFill(start_color=LIGHT_GRAY, end_color=LIGHT_GRAY, fill_type="solid")
white_fill = PatternFill(start_color=WHITE, end_color=WHITE, fill_type="solid")
thin_border = Border(
    left=Side(style="thin", color="D0D0D0"),
    right=Side(style="thin", color="D0D0D0"),
    top=Side(style="thin", color="D0D0D0"),
    bottom=Side(style="thin", color="D0D0D0"),
)
wrap_align = Alignment(wrap_text=True, vertical="top")
center_align = Alignment(horizontal="center", vertical="top", wrap_text=True)

def style_header_row(ws, num_cols, row=1):
    for c in range(1, num_cols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border

def style_data_row(ws, row, num_cols, is_odd, section_row=False):
    fill = gray_fill if is_odd else white_fill
    for c in range(1, num_cols + 1):
        cell = ws.cell(row=row, column=c)
        if section_row:
            cell.font = bold_font
            cell.fill = PatternFill(start_color="E8E8E8", end_color="E8E8E8", fill_type="solid")
        else:
            cell.font = data_font
            cell.fill = fill
        cell.alignment = wrap_align
        cell.border = thin_border

def auto_width(ws, num_cols, max_width=45, min_width=12):
    for c in range(1, num_cols + 1):
        max_len = min_width
        for row in ws.iter_rows(min_col=c, max_col=c):
            for cell in row:
                if cell.value:
                    max_len = max(max_len, min(len(str(cell.value)), max_width))
        ws.column_dimensions[get_column_letter(c)].width = max_len + 2

# ============================================================
# TAB 1: MASTER INVENTORY
# ============================================================
ws = wb.active
ws.title = "MASTER INVENTORY"
ws.sheet_properties.tabColor = NAVY

# Title area
ws.merge_cells("A1:M1")
ws["A1"] = "Parakeet Communities"
ws["A1"].font = title_font
ws["A1"].alignment = Alignment(vertical="center")
ws.merge_cells("A2:M2")
ws["A2"] = "JotForm Audit — Build Reference v1.0 | August 2026"
ws["A2"].font = subtitle_font
ws["A2"].alignment = Alignment(vertical="center")
ws.row_dimensions[1].height = 28
ws.row_dimensions[2].height = 20

headers = [
    "Form #", "Form Name", "JotForm URL", "Category", "Primary User",
    "Frequency", "Total Field Count", "Has Conditional Logic",
    "Has File Uploads", "Has Signatures", "Migration Target",
    "Migration Notes", "Priority"
]
for c, h in enumerate(headers, 1):
    ws.cell(row=4, column=c, value=h)
style_header_row(ws, len(headers), row=4)
ws.freeze_panes = "A5"

forms = [
    [1, "Home Listing Confirmation", "https://form.jotform.com/260284900083049",
     "Sales / Listings", "Community Manager", "Per Event", 4, "No", "No", "No",
     "QB Only", "Maps to Listing Records table — already in spec", "High"],
    [2, "Home Listing Request Form", "https://form.jotform.com/260254036219047",
     "Sales / Listings", "Community Manager", "Per Event", 30, "No", "Yes", "No",
     "QB + FastField", "Listing workflow — already in spec; field capture for photos", "High"],
    [3, "Offer to Purchase / Rent", "https://form.jotform.com/260429031747052",
     "Sales / Offers", "Community Manager / Agent", "Per Event", 15, "No", "Yes", "No",
     "QB Only", "New Offers table needed in QB", "High"],
    [4, "Utility Request Application", "https://form.jotform.com/260408100295044",
     "Operations / Utilities", "Community Manager", "Per Event", 12, "No", "No", "No",
     "QB Only", "New Utility Requests table in QB", "High"],
    [5, "Weekly Maintenance Checklist", "https://form.jotform.com/261368473481060",
     "Maintenance / Operations", "Facility Manager", "Weekly", 40, "No", "Yes", "No",
     "FastField + QB", "New Maintenance table; photo-heavy — FastField primary", "Low"],
    [6, "Incident Report", "https://form.jotform.com/261375661615056",
     "Operations / Risk Management", "Community Manager", "Per Event", 45, "Yes", "Yes", "No",
     "QB Only", "New Incidents table in QB; complex conditional logic", "Medium"],
    [7, "Monthly Equipment & Inventory", "https://form.jotform.com/261374648754064",
     "Maintenance / Operations", "Technician", "Monthly", 50, "No", "Yes", "Yes",
     "FastField + QB", "New Equipment table; field-heavy — FastField primary", "Low"],
    [8, "Month End Checklist", "https://form.jotform.com/261374362462053",
     "Operations / Management", "Community Manager", "Monthly", 25, "No", "No", "Yes",
     "QB Only", "New Month End table; several items reference Rent Manager", "Medium"],
    [9, "Move Out Inspection", "https://form.jotform.com/260264216018045",
     "Operations / Resident Mgmt", "Community Manager / Inspector", "Per Event", 95, "Yes", "No", "Yes",
     "FastField + QB", "New Inspections table; room-level conditional logic", "Medium"],
    [10, "Resident Information Sheet", "https://form.jotform.com/260355458038056",
     "Operations / Resident Mgmt", "Community Manager", "One-time", 20, "No", "Yes", "No",
     "QB Only", "New or synced with Rent Manager; intake form", "Medium"],
    [11, "Community Site Visit Inspection", "https://form.jotform.com/261053925624052",
     "Operations / Management", "Regional Manager / Director", "Per Visit", 55, "No", "No", "No",
     "FastField + QB", "New Site Visit table; field inspection — FastField primary", "Medium"],
    [12, "Rehab Walkthrough Punchlist", "https://form.jotform.com/261234541071043",
     "Construction / Operations", "Community Manager / Inspector", "Per Event", 35, "No", "No", "Yes",
     "FastField + QB", "Rehab workflow — separate from Home Ordering (Workflow #002?)", "High"],
    [13, "Move In / Move Out Request", "https://form.jotform.com/260116744407049",
     "Operations / Resident Mgmt", "Community Manager", "Per Event", 30, "Yes", "Yes", "Yes",
     "QB Only", "New Move In/Out table — triggers Rent Manager entries", "High"],
]

for i, row_data in enumerate(forms):
    r = i + 5
    for c, val in enumerate(row_data, 1):
        ws.cell(row=r, column=c, value=val)
    is_odd = i % 2 == 0
    style_data_row(ws, r, len(headers), is_odd)
    # Color-code Migration Target (col 11)
    mt_cell = ws.cell(row=r, column=11)
    if mt_cell.value and "Retire" in str(mt_cell.value):
        mt_cell.fill = red_fill
    elif mt_cell.value and "TBD" in str(mt_cell.value):
        mt_cell.fill = yellow_fill
    # Color-code Required = Yes would be in form tabs
    # Color-code Priority
    # Green fill for Required=Yes is for form tabs; here highlight URL as blue
    url_cell = ws.cell(row=r, column=3)
    url_cell.font = data_font_blue

auto_width(ws, len(headers))
ws.column_dimensions["C"].width = 45
ws.column_dimensions["L"].width = 50

# Save intermediate
wb.save("/home/ubuntu/parakeet_jotform_audit.xlsx")
print("Part 1 done — Master Inventory created")
