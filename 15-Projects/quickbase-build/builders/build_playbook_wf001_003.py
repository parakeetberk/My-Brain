#!/usr/bin/env python3
"""Parakeet QB+FastField Build Playbook v1.0 — WF001+WF002+WF003"""

def step(n, title, body):
    return f"""<div class="step"><div class="step-num">Step {n}</div><div class="step-content"><div class="step-title">{title}</div>{body}</div></div>"""

def note(body):
    return f'<div class="callout note"><span class="callout-icon">ℹ</span><div>{body}</div></div>'

def warn(body):
    return f'<div class="callout warn"><span class="callout-icon">⚠</span><div>{body}</div></div>'

def crit(body):
    return f'<div class="callout crit"><span class="callout-icon">🔴</span><div>{body}</div></div>'

def phase_header(num, title, color, tag, sub=""):
    return f"""<div class="phase-header phase-{color}">
  <div class="phase-num">Phase {num}</div>
  <div class="phase-title">{title}</div>
  <div class="phase-tag">{tag}</div>
  {f'<div class="phase-sub">{sub}</div>' if sub else ''}
</div>"""

def section(title):
    return f'<h3 class="section-title">{title}</h3>'

def subsection(title):
    return f'<h4 class="subsection-title">{title}</h4>'

def field_table(headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="table-wrap"><table class="data-table"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

def auto_table(rows):
    return field_table(["ID", "Trigger", "Timing", "Action"], rows)

def gate_table(rows):
    return field_table(["Gate ID", "Gate Name", "Transition", "Condition / Error Message"], rows)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Parakeet QB+FastField Build Playbook v1.0 — WF001 · WF002 · WF003</title>
<link href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
:root {
  --green: #4ABA81; --red: #F16262; --yellow: #FFCC3B; --navy: #2F4E65;
  --green-lt: #E8F8F1; --red-lt: #FEF0F0; --yellow-lt: #FFFBEA; --navy-lt: #EAF0F5;
  --border: #D1D9E0; --bg: #F7F9FB; --text: #1A2B3C; --muted: #5A6878;
  --font: 'Red Hat Display', sans-serif;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
@page { size: letter; margin: 0.75in 0.75in 0.9in; }
body { font-family: var(--font); color: var(--text); background: #fff; font-size: 10pt; line-height: 1.55; }

/* COVER */
.cover { page-break-after: always; min-height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: flex-start; padding: 2.5in 1in 1in; background: var(--navy); color: #fff; }
.cover-logo { font-size: 11pt; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: var(--green); margin-bottom: 0.6in; }
.cover-title { font-size: 32pt; font-weight: 900; line-height: 1.1; margin-bottom: 0.15in; }
.cover-sub { font-size: 14pt; font-weight: 400; color: rgba(255,255,255,0.75); margin-bottom: 0.4in; }
.cover-wf-row { display: flex; gap: 12px; margin-bottom: 0.4in; }
.cover-wf-badge { padding: 4px 14px; border-radius: 20px; font-size: 9pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; }
.cover-wf-badge.wf1 { background: var(--green); color: #fff; }
.cover-wf-badge.wf2 { background: var(--yellow); color: var(--navy); }
.cover-wf-badge.wf3 { background: var(--red); color: #fff; }
.cover-meta { font-size: 9pt; color: rgba(255,255,255,0.6); line-height: 2; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 0.25in; }
.cover-meta span { color: #fff; font-weight: 600; }

/* TOC */
.toc-page { page-break-after: always; padding: 0.5in 0.75in; }
.toc-title { font-size: 16pt; font-weight: 800; color: var(--navy); margin-bottom: 0.3in; padding-bottom: 8px; border-bottom: 3px solid var(--navy); }
.toc-group { margin-bottom: 0.25in; }
.toc-phase { font-size: 10pt; font-weight: 700; color: var(--navy); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 6px; padding: 4px 10px; background: var(--navy-lt); border-left: 4px solid var(--navy); }
.toc-item { display: flex; justify-content: space-between; padding: 2px 10px; font-size: 9pt; }
.toc-item:nth-child(even) { background: var(--bg); }
.toc-item .toc-num { color: var(--muted); min-width: 40px; }

/* PHASE HEADERS */
.phase-header { padding: 0.3in 0.4in; margin: 0.35in 0 0.25in; border-radius: 10px; page-break-inside: avoid; }
.phase-header.phase-green { background: linear-gradient(135deg, #1E7B55, var(--green)); color: #fff; }
.phase-header.phase-yellow { background: linear-gradient(135deg, #C49A00, var(--yellow)); color: var(--navy); }
.phase-header.phase-red { background: linear-gradient(135deg, #B83636, var(--red)); color: #fff; }
.phase-header.phase-navy { background: linear-gradient(135deg, #1A3044, var(--navy)); color: #fff; }
.phase-header.phase-purple { background: linear-gradient(135deg, #5B2A8E, #8B5CF6); color: #fff; }
.phase-num { font-size: 9pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; opacity: 0.8; margin-bottom: 4px; }
.phase-title { font-size: 18pt; font-weight: 900; line-height: 1.1; }
.phase-tag { font-size: 8pt; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; opacity: 0.75; margin-top: 4px; }
.phase-sub { font-size: 9pt; margin-top: 8px; opacity: 0.9; max-width: 480px; }

/* SECTION TITLES */
.section-title { font-size: 13pt; font-weight: 800; color: var(--navy); margin: 0.25in 0 0.12in; padding-bottom: 5px; border-bottom: 2px solid var(--border); }
.subsection-title { font-size: 10.5pt; font-weight: 700; color: var(--navy); margin: 0.2in 0 0.1in; }
.sub2-title { font-size: 9.5pt; font-weight: 700; color: var(--muted); margin: 0.15in 0 0.08in; text-transform: uppercase; letter-spacing: 0.06em; }

/* STEPS */
.step { display: flex; gap: 14px; margin: 0.15in 0; padding: 14px 16px; background: var(--bg); border-radius: 8px; border-left: 4px solid var(--green); page-break-inside: avoid; }
.step-num { min-width: 52px; font-size: 8pt; font-weight: 800; color: var(--green); text-transform: uppercase; letter-spacing: 0.06em; padding-top: 2px; }
.step-content { flex: 1; }
.step-title { font-size: 10pt; font-weight: 700; color: var(--text); margin-bottom: 6px; }

/* CALLOUTS */
.callout { display: flex; gap: 10px; padding: 10px 14px; border-radius: 6px; margin: 10px 0; font-size: 9pt; page-break-inside: avoid; }
.callout.note { background: var(--navy-lt); border-left: 4px solid var(--navy); }
.callout.warn { background: var(--yellow-lt); border-left: 4px solid var(--yellow); }
.callout.crit { background: var(--red-lt); border-left: 4px solid var(--red); }
.callout-icon { font-size: 12pt; flex-shrink: 0; padding-top: 1px; }

/* TABLES */
.table-wrap { overflow: hidden; margin: 10px 0; border-radius: 6px; border: 1px solid var(--border); }
.data-table { width: 100%; border-collapse: collapse; font-size: 8.5pt; }
.data-table thead th { background: var(--navy); color: #fff; font-weight: 700; padding: 7px 10px; text-align: left; }
.data-table tbody td { padding: 6px 10px; border-bottom: 1px solid var(--border); vertical-align: top; }
.data-table tbody tr:nth-child(even) td { background: var(--bg); }
.data-table tbody tr:last-child td { border-bottom: none; }

/* INLINE LABELS */
.lbl { display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 7.5pt; font-weight: 700; letter-spacing: 0.04em; }
.lbl-green { background: var(--green-lt); color: #1a6641; }
.lbl-red { background: var(--red-lt); color: #8B2222; }
.lbl-yellow { background: var(--yellow-lt); color: #7A5C00; }
.lbl-navy { background: var(--navy-lt); color: var(--navy); }
.lbl-gray { background: #EEF2F5; color: var(--muted); }

/* WF BADGES in content */
.wf-badge { display: inline-block; padding: 1px 8px; border-radius: 10px; font-size: 7.5pt; font-weight: 700; }
.wf-badge.wf1 { background: var(--green); color: #fff; }
.wf-badge.wf2 { background: var(--yellow); color: var(--navy); }
.wf-badge.wf3 { background: var(--red); color: #fff; }

/* CONTENT BODY */
.content { padding: 0 0.25in; }
p { margin: 6px 0; font-size: 9.5pt; }
ul { margin: 6px 0 6px 18px; font-size: 9.5pt; }
li { margin-bottom: 3px; }
strong { font-weight: 700; }
code { font-family: monospace; font-size: 8.5pt; background: #EEF2F5; padding: 1px 5px; border-radius: 3px; }

/* PAGE BREAK */
.page-break { page-break-before: always; }
.no-break { page-break-inside: avoid; }

/* SUMMARY BAR */
.summary-bar { display: flex; gap: 12px; flex-wrap: wrap; margin: 0.15in 0; }
.summary-chip { padding: 6px 14px; border-radius: 6px; font-size: 8.5pt; font-weight: 600; background: var(--bg); border: 1px solid var(--border); }
.summary-chip strong { color: var(--navy); display: block; font-size: 13pt; font-weight: 900; }

/* DIVIDER */
.divider { border: none; border-top: 1px solid var(--border); margin: 0.2in 0; }

/* BUILD SEQ TABLE */
.seq-table { width: 100%; border-collapse: collapse; font-size: 8.5pt; margin: 10px 0; }
.seq-table th { background: var(--navy); color: #fff; padding: 7px 10px; text-align: left; font-weight: 700; }
.seq-table td { padding: 6px 10px; border-bottom: 1px solid var(--border); vertical-align: top; }
.seq-table tr:nth-child(even) td { background: var(--bg); }

/* SPEC REF STRIP */
.spec-ref { font-size: 7.5pt; color: var(--muted); font-weight: 500; margin-bottom: 6px; }
.spec-ref span { color: var(--navy); font-weight: 700; }
</style>
</head>
<body>

<!-- ===================== COVER ===================== -->
<div class="cover">
  <div class="cover-logo">Parakeet Communities · Internal Confidential</div>
  <div class="cover-title">QB + FastField<br>Build Playbook</div>
  <div class="cover-sub">Step-by-Step Configuration Guide — QuickBase & FastField</div>
  <div class="cover-wf-row">
    <span class="cover-wf-badge wf1">WF001 · Home Ordering v1.2</span>
    <span class="cover-wf-badge wf2">WF002 · Rehab v1.3</span>
    <span class="cover-wf-badge wf3">WF003 · Disposition Review v1.1</span>
  </div>
  <div class="cover-meta">
    Document ID <span>BUILD-PLAYBOOK-v1.0</span><br>
    Date <span>08/19/26</span><br>
    Status <span>Approved for Build</span><br>
    Prepared For <span>Parakeet Communities — QB/FastField Build Team</span><br>
    Confidentiality <span>Internal · Confidential · Do Not Distribute</span>
  </div>
</div>

<!-- ===================== HOW TO USE ===================== -->
<div class="toc-page">
<div class="toc-title">How to Use This Playbook</div>
<p>This playbook translates the three locked build specs (WF001 v1.2, WF002 v1.3, WF003 v1.1) into ordered, step-by-step QuickBase and FastField configuration instructions. It is a <strong>build guide</strong>, not a spec repeat — it tells you <em>how</em> to configure, not just <em>what</em> to configure.</p>
<br>
<p><strong>How to work through it:</strong></p>
<ul>
  <li><strong>Phase 0</strong> first — always. Pre-build setup must be complete before any table is created.</li>
  <li><strong>Phase 1</strong> second — shared reference tables are dependencies for all three workflows. Build them once.</li>
  <li><strong>Phase 2, 3, 4</strong> — build each workflow in order. WF003 can be built before WF002 if preferred (it is upstream), but WF001 is independent and can run in parallel.</li>
  <li><strong>Phase 5</strong> last — cross-workflow wiring and end-to-end testing.</li>
</ul>
<br>
<p><strong>Key conventions:</strong></p>
<ul>
  <li><span class="lbl lbl-green">Auto</span> fields are system-generated — never manual entry.</li>
  <li><span class="lbl lbl-red">Required</span> fields must be set before the form can save.</li>
  <li><span class="lbl lbl-yellow">Gate</span> fields are enforced by hard-stop validation — no bypass allowed.</li>
  <li><span class="lbl lbl-navy">Relationship</span> fields link to another table via QB relationship (never free-text for linked data).</li>
  <li>All field names, automation IDs, and gate IDs match the approved specs exactly. Do not rename.</li>
  <li>QB status fields (Workflow Stage, Lot Status, Asset Status, etc.) are <strong>set by automation only</strong> — Community Managers never manually set these fields.</li>
</ul>

<div class="toc-title" style="margin-top:0.3in;">Table of Contents</div>
<div class="toc-group">
  <div class="toc-phase">Phase 0 — Pre-Build Setup</div>
  <div class="toc-item"><div class="toc-num">P0-S1</div><div>Create QB Application</div></div>
  <div class="toc-item"><div class="toc-num">P0-S2</div><div>Provision User Accounts &amp; Role Permissions</div></div>
  <div class="toc-item"><div class="toc-num">P0-S3</div><div>Provision FastField Account &amp; Users</div></div>
  <div class="toc-item"><div class="toc-num">P0-S4</div><div>Naming Conventions &amp; Record ID Formats</div></div>
  <div class="toc-item"><div class="toc-num">P0-S5</div><div>Source Files Reference</div></div>
</div>
<div class="toc-group">
  <div class="toc-phase">Phase 1 — Shared Reference Tables</div>
  <div class="toc-item"><div class="toc-num">P1-S1</div><div>Communities Table (68 records)</div></div>
  <div class="toc-item"><div class="toc-num">P1-S2</div><div>Lot Status Reference Table (16 values)</div></div>
  <div class="toc-item"><div class="toc-num">P1-S3</div><div>Asset Status Reference Table (25 values)</div></div>
  <div class="toc-item"><div class="toc-num">P1-S4</div><div>Lots Table</div></div>
</div>
<div class="toc-group">
  <div class="toc-phase">Phase 2 — WF001: Home Ordering</div>
  <div class="toc-item"><div class="toc-num">P2-S1</div><div>Home Orders Table</div></div>
  <div class="toc-item"><div class="toc-num">P2-S2</div><div>Workflow Tasks Table</div></div>
  <div class="toc-item"><div class="toc-num">P2-S3</div><div>Delivery Records Table</div></div>
  <div class="toc-item"><div class="toc-num">P2-S4</div><div>Construction Inspection Records Table</div></div>
  <div class="toc-item"><div class="toc-num">P2-S5</div><div>Ops Readiness Records Table</div></div>
  <div class="toc-item"><div class="toc-num">P2-S6</div><div>Listing Records Table</div></div>
  <div class="toc-item"><div class="toc-num">P2-S7</div><div>Cascading Dropdown Configuration</div></div>
  <div class="toc-item"><div class="toc-num">P2-S8</div><div>QB Forms (10 forms)</div></div>
  <div class="toc-item"><div class="toc-num">P2-S9</div><div>FastField Form 1 — Home Delivery Confirmation</div></div>
  <div class="toc-item"><div class="toc-num">P2-S10</div><div>FastField Form 2 — Construction Inspection (89 Items)</div></div>
  <div class="toc-item"><div class="toc-num">P2-S11</div><div>FastField Form 3 — Ops &amp; Sales Readiness (71 Items)</div></div>
  <div class="toc-item"><div class="toc-num">P2-S12</div><div>FastField Form 4 — Listing Form</div></div>
  <div class="toc-item"><div class="toc-num">P2-S13</div><div>Automations A1–A14</div></div>
  <div class="toc-item"><div class="toc-num">P2-S14</div><div>Lot Status Automations LS-1 – LS-6</div></div>
  <div class="toc-item"><div class="toc-num">P2-S15</div><div>Gate Rules HO-G1 – OI-G3</div></div>
  <div class="toc-item"><div class="toc-num">P2-S16</div><div>Views &amp; Dashboards</div></div>
</div>
<div class="toc-group">
  <div class="toc-phase">Phase 3 — WF002: Rehab</div>
  <div class="toc-item"><div class="toc-num">P3-S1</div><div>Rehab Records Table (RH)</div></div>
  <div class="toc-item"><div class="toc-num">P3-S2</div><div>Rehab Tasks Table (TK-RH)</div></div>
  <div class="toc-item"><div class="toc-num">P3-S3</div><div>Rehab Walkthrough Records Table (RW)</div></div>
  <div class="toc-item"><div class="toc-num">P3-S4</div><div>Vendors QB Reference Table + Power Automate Integration</div></div>
  <div class="toc-item"><div class="toc-num">P3-S5</div><div>FastField Form — Rehab Walkthrough Punchlist (37 Items)</div></div>
  <div class="toc-item"><div class="toc-num">P3-S6</div><div>Cascading Dropdowns (WF002)</div></div>
  <div class="toc-item"><div class="toc-num">P3-S7</div><div>Automations A-RH-01 – A-RH-12</div></div>
  <div class="toc-item"><div class="toc-num">P3-S8</div><div>Gate Rules G-RH-01 – G-RH-08</div></div>
</div>
<div class="toc-group">
  <div class="toc-phase">Phase 4 — WF003: Asset Disposition Review</div>
  <div class="toc-item"><div class="toc-num">P4-S1</div><div>Disposition Meetings Table (DM)</div></div>
  <div class="toc-item"><div class="toc-num">P4-S2</div><div>Disposition Items Table (DI)</div></div>
  <div class="toc-item"><div class="toc-num">P4-S3</div><div>Automations A-DR-01 – A-DR-05</div></div>
  <div class="toc-item"><div class="toc-num">P4-S4</div><div>Gate Rules G-DR-01 – G-DR-03</div></div>
  <div class="toc-item"><div class="toc-num">P4-S5</div><div>Standard Reports (5 reports)</div></div>
</div>
<div class="toc-group">
  <div class="toc-phase">Phase 5 — Cross-Workflow Connections &amp; Testing</div>
  <div class="toc-item"><div class="toc-num">P5-S1</div><div>WF003 → WF002 Integration Wire-Up</div></div>
  <div class="toc-item"><div class="toc-num">P5-S2</div><div>Move Out Integration Points</div></div>
  <div class="toc-item"><div class="toc-num">P5-S3</div><div>Shared Reference Table Dependencies Map</div></div>
  <div class="toc-item"><div class="toc-num">P5-S4</div><div>End-to-End Testing Checklists</div></div>
</div>
</div>

<!-- ========================= PHASE 0 ========================= -->
<div class="page-break"></div>
""" + phase_header("0","Pre-Build Setup","navy","Must be completed before any table is created") + """
<div class="content">
""" + section("P0-S1 · Create QuickBase Application") + """
""" + step("1","Log in to QuickBase and create a new app","<p>Go to <strong>quickbase.com → My Apps → + New App</strong>. Select <em>Start from scratch</em>. Name the app exactly: <code>Parakeet Communities</code>. Leave the description blank or enter: <em>Operational workflow system — Home Ordering, Rehab, Asset Disposition Review.</em></p>") + """
""" + step("2","Set app icon and branding","<p>In App Settings → Branding: set the app color to <strong>#2F4E65</strong> (navy). Upload the Parakeet logo (parakeet-communities-Logo-RGB.png).</p>") + """
""" + step("3","Confirm app URL and share with build team","<p>Copy the app URL (format: <code>https://parakeetcommunities.quickbase.com/db/[AppID]</code>). Share with all QB admins and the build team.</p>") + """

""" + section("P0-S2 · Provision User Accounts & Role Permissions") + """
""" + note("QB roles drive form visibility, field edit access, and automation permissions. Set these before building any forms.") + """
""" + step("1","Create all named user accounts","<p>In App Settings → Users, invite each person below. Set role as indicated:</p>") + """
""" + field_table(
    ["Name / Role", "QB Role", "Access Level"],
    [
        ["Austin (Owner / CEO)", "System Admin", "Full admin — all tables, all fields, approve gates"],
        ["Justin (Asset Management / RM Admin)", "Asset Management", "Full Edit — all workflow tables"],
        ["Melanie (Operations Coordinator)", "Ops Coord", "Edit — assigned tasks; read-only otherwise"],
        ["John Clark (Director of Construction)", "Construction", "Full Edit — Construction Inspection, Delivery Records; read-only on financial fields"],
        ["Facility Manager", "Facility Manager", "Edit — Ops Readiness Records; read-only otherwise"],
        ["Sales / Community Managers", "Community Manager", "Edit — Home Orders (own records), Ops Readiness (own records)"],
        ["Accounting", "Accounting", "Edit — financial fields only; read-only on workflow fields"],
        ["Leslie (Listing Team)", "Listing", "Read-only — Home Orders, Listing Records only"],
        ["Tanya (Listing Team)", "Listing", "Read-only — Home Orders, Listing Records only"],
    ]
) + """

""" + section("P0-S3 · Provision FastField Account & Users") + """
""" + step("1","Create FastField organization account","<p>Log in to FastField (fastfieldforms.com). Create or confirm the Parakeet Communities organization account. Confirm license tier supports webhook/API integration (required for QB sync).</p>") + """
""" + step("2","Add FastField users","<p>Add all field staff who will complete forms: Director of Construction (John Clark), Facility Managers, Community Managers / Sales Reps, Operations Coordinators.</p>") + """
""" + step("3","Note the FastField webhook endpoint","<p>In FastField → Settings → Integrations, locate the webhook configuration panel. Note the webhook URL format — you will configure this per-form in Phase 2 (FastField → QB sync).</p>") + """

""" + section("P0-S4 · Naming Conventions & Record ID Formats") + """
""" + field_table(
    ["Record Type", "ID Format", "Example", "Auto-Generated By"],
    [
        ["Home Orders (WF001)", "HO-YYYY-###", "HO-2026-001", "QB formula field"],
        ["Workflow Tasks (WF001)", "TK-YYYY-#####", "TK-2026-00001", "QB formula field"],
        ["Rehab Records (WF002)", "RH-YYYY-###", "RH-2026-001", "QB formula on creation"],
        ["Rehab Tasks (WF002)", "TK-RH-YYYY-#####", "TK-RH-2026-00001", "QB formula field"],
        ["Walkthrough Records (WF002)", "RW-YYYY-###", "RW-2026-001", "QB formula on webhook receipt"],
        ["Disposition Meetings (WF003)", "DM-YYYY-###", "DM-2026-001", "QB formula field"],
        ["Disposition Items (WF003)", "DI-YYYY-###", "DI-2026-001", "QB formula field"],
        ["Lot Status (ref)", "LS-###", "LS-001", "QB formula field"],
        ["Asset Status (ref)", "AS-###", "AS-001", "QB formula field"],
    ]
) + """
""" + note("All auto-generated IDs use a QB formula field combining <code>\"PREFIX-\" & Text(Year(Today())) & \"-\" & Right(\"000\" & [Record ID#], 3)</code>. Adjust padding zeros to match the format above.") + """

""" + section("P0-S5 · Source Files Reference") + """
<p>The following files are the build-phase source of truth. Keep them accessible during the build.</p>
""" + field_table(
    ["File", "Contents", "Use During Build"],
    [
        ["dw_PDS.xlsx", "68 active communities (Reportable = Yes) — Short Name, Display Name, State, Vehicle, Type, Age Cat, Lots, Occupancy, Rent", "Phase 1 — Communities table seed data"],
        ["Unit Type Listing.xlsx", "16 Lot Status values (RM-aligned) — exact status names, categories", "Phase 1 — Lot Status reference table"],
        ["Asset Status.xlsx", "25 Asset Status values (RM-aligned) — exact status names, categories, descriptions", "Phase 1 — Asset Status reference table"],
        ["WF001 Spec v1.2", "Home Ordering complete spec — 7 tables, 4 FastField forms, 20 automations, 9 gate rules", "Phase 2 — all steps"],
        ["WF002 Spec v1.3", "Rehab complete spec — 5 tables, 1 FastField form, 12 automations, 8 gate rules", "Phase 3 — all steps"],
        ["WF003 Spec v1.1", "Asset Disposition Review spec — 2 tables, 5 automations, 3 gate rules", "Phase 4 — all steps"],
    ]
) + """
</div>

<!-- ========================= PHASE 1 ========================= -->
<div class="page-break"></div>
""" + phase_header("1","Shared Reference Tables","green","Build first — all three workflows depend on these","Communities · Lot Status · Asset Status · Lots — built once, shared across WF001, WF002, and WF003") + """
<div class="content">
""" + note("These four tables are shared infrastructure. Build them before any workflow-specific table. Do not duplicate — every workflow references the same records.") + """

""" + section("P1-S1 · Communities Table (68 records)") + """
<div class="spec-ref">Source: <span>dw_PDS.xlsx (Reportable = Yes)</span> · Referenced by: <span>WF001, WF002, WF003</span></div>
""" + step("1","Create the Communities table","<p>In QB → Tables → + New Table. Name: <code>Communities</code>. This is a reference/master table — no workflow stage field needed.</p>") + """
""" + step("2","Add all fields","<p>Add the following fields to the Communities table:</p>") + """
""" + field_table(
    ["Field Name", "Type", "Notes"],
    [
        ["Short Name", "Text", "Primary key — unique community code (e.g., APPLE, RIV). Used in all cascade dropdowns and cross-table relationships."],
        ["Community Display Name", "Text", "Human-readable full name shown in QB forms and reports."],
        ["State", "Text", "Two-letter state abbreviation. Used to filter vendors by state in WF002."],
        ["Vehicle / Fund", "Text", "Investment vehicle (Single Asset, Fund II, JREFI, JREFII, Kippy, Harpreet, Baker, Origins)."],
        ["Property Type", "Multi-select", "Values: ManufacturedHousing | RVCampground | Mixed"],
        ["Age Category", "Multi-select", "Values: All-Ages | 55+ | 50+"],
        ["MH Lots", "Numeric (integer)", "Total manufactured housing pad sites."],
        ["RV Lots", "Numeric (integer)", "Total RV/campground sites. 0 for MH-only communities."],
        ["Total Units", "Formula (numeric)", "= [MH Lots] + [RV Lots]. Auto-calculated."],
        ["Occupancy %", "Percent", "Current physical occupancy. Updated periodically from dw_PDS."],
        ["2026 MH Lot Rent", "Currency", "Gross monthly MH lot rent. $0 for RV-primary communities."],
        ["Active", "Checkbox (Yes/No)", "Controls whether community appears in all workflow dropdown lists. Default: Yes for all 68."],
    ]
) + """
""" + step("3","Import the 68 community records","<p>In QB → Communities table → Import → From CSV. Export the 68 communities from <code>dw_PDS.xlsx</code> (Reportable = Yes rows) and import. Map columns to field names above. Verify Active = Yes for all 68 after import.</p>") + """
""" + warn("Do not create community records manually — import from dw_PDS to ensure exact Short Name values match RM. Short Name is the key used for all cascades and cross-references.") + """

""" + section("P1-S2 · Lot Status Reference Table (16 values)") + """
<div class="spec-ref">Source: <span>Unit Type Listing.xlsx (RM-aligned)</span> · Referenced by: <span>WF001 cascade filters, WF002 automations, WF003 automations</span></div>
""" + step("1","Create the Lot Status table","<p>In QB → Tables → + New Table. Name: <code>Lot Status</code>. This is a standalone lookup table — it holds every valid Lot Status value system-wide.</p>") + """
""" + step("2","Add all fields","") + """
""" + field_table(
    ["Field Name", "Type", "Notes"],
    [
        ["Status ID", "Text (auto-generated formula)", "Format: LS-### (e.g., LS-001). Auto-generated formula: 'LS-' & Right('000' & [Record ID#], 3)"],
        ["Status Name", "Text", "Exact RM-aligned status label shown in all QB dropdowns and views."],
        ["Status Category", "Dropdown", "Values: Active | Inactive | Transitional"],
        ["Description", "Text (multi-line)", "Operational definition — what this status means in practice."],
        ["Allows New Home Order", "Checkbox (Yes/No)", "WF001 filter: only lots where this = Yes appear in new order dropdowns."],
        ["Allows Move In", "Checkbox (Yes/No)", "Move In form filter."],
        ["Allows Move Out", "Checkbox (Yes/No)", "Move Out form filter."],
        ["Allows Rehab", "Checkbox (Yes/No)", "WF002 filter: only lots where this = Yes are eligible for Rehab Records."],
        ["Allows Listing", "Checkbox (Yes/No)", "Listing workflow filter."],
    ]
) + """
""" + step("3","Create the 16 Lot Status records (enter manually)","<p>Create one record per row below. Match Status Name exactly — these are RM-aligned values.</p>") + """
""" + field_table(
    ["Status Name", "Category", "New HO", "Move In", "Move Out", "Rehab", "Listing"],
    [
        ["Lot", "Active", "Yes", "Yes", "No", "Yes", "Yes"],
        ["Lot-Avail(POH)", "Active", "No", "Yes", "No", "No", "Yes"],
        ["Lot-Rental", "Active", "No", "No", "Yes", "No", "No"],
        ["Lot-LTP", "Active", "No", "No", "Yes", "No", "No"],
        ["Lot-RV", "Active", "No", "No", "Yes", "No", "No"],
        ["Lot-RV(Transient)", "Active", "No", "No", "Yes", "No", "No"],
        ["Lot-RV(Seasonal)", "Active", "No", "No", "Yes", "No", "No"],
        ["Lot-In Rehab", "Transitional", "No", "No", "No", "Yes", "No"],
        ["Lot-Need Rehab", "Transitional", "No", "No", "No", "Yes", "No"],
        ["Lot-Pending(POH)", "Transitional", "No", "No", "No", "No", "No"],
        ["Lot-Evicted", "Transitional", "No", "No", "Yes", "No", "No"],
        ["Lot-Evicted (Rental)", "Transitional", "No", "No", "Yes", "No", "No"],
        ["Lot-Demo", "Inactive", "No", "No", "No", "No", "No"],
        ["Lot-Abandoned", "Inactive", "No", "No", "No", "No", "No"],
        ["Lot-Not Ready", "Inactive", "No", "No", "No", "No", "No"],
        ["Lot-Unusable", "Inactive", "No", "No", "No", "No", "No"],
    ]
) + """

""" + section("P1-S3 · Asset Status Reference Table (25 values)") + """
<div class="spec-ref">Source: <span>Asset Status.xlsx (RM-aligned)</span> · Referenced by: <span>WF002 cascade filters, WF003 automations</span></div>
""" + step("1","Create the Asset Status table","<p>In QB → Tables → + New Table. Name: <code>Asset Status</code>. Standalone lookup table for all valid Asset Status values system-wide.</p>") + """
""" + step("2","Add all fields","") + """
""" + field_table(
    ["Field Name", "Type", "Notes"],
    [
        ["Status ID", "Text (auto-formula)", "Format: AS-### (e.g., AS-001). Formula: 'AS-' & Right('000' & [Record ID#], 3)"],
        ["Status Name", "Text", "Exact RM-aligned status label."],
        ["Status Category", "Dropdown", "Values: Active | Inactive | Transitional"],
        ["Description", "Text (multi-line)", "Operational meaning."],
        ["Allows Rehab Walkthrough", "Checkbox (Yes/No)", "FastField form filter: only assets where this = Yes are eligible for walkthrough submission."],
        ["Allows Listing", "Checkbox (Yes/No)", "Listing workflow filter."],
    ]
) + """
""" + step("3","Create the 25 Asset Status records","<p>Enter one record per row. Status Name must match RM exactly.</p>") + """
""" + field_table(
    ["Status Name", "Category", "Rehab WT", "Listing"],
    [
        ["Rental", "Active", "No", "No"],
        ["In Use", "Active", "No", "No"],
        ["For Sale", "Active", "No", "Yes"],
        ["Lease Option (LOP)", "Active", "No", "No"],
        ["Rent to Own Agreement", "Active", "No", "No"],
        ["Promissory Note", "Active", "No", "No"],
        ["Needs Rehab", "Transitional", "No", "No"],
        ["Rehab in Process", "Transitional", "Yes", "No"],
        ["TBD", "Transitional", "No", "No"],
        ["Delivered", "Transitional", "No", "No"],
        ["Ordered", "Transitional", "No", "No"],
        ["Setting Needed", "Transitional", "No", "No"],
        ["Permit Pending", "Transitional", "No", "No"],
        ["Pending Sale", "Transitional", "No", "No"],
        ["Eviction Filed", "Transitional", "No", "No"],
        ["Title Pending Transfer to Buyer", "Transitional", "No", "No"],
        ["Title Pending Transfer to Parakeet", "Transitional", "No", "No"],
        ["Waiting on Title", "Transitional", "No", "No"],
        ["Abandoned", "Inactive", "No", "No"],
        ["To Be Demoed", "Inactive", "No", "No"],
        ["Sold", "Inactive", "No", "No"],
        ["In Storage", "Inactive", "No", "No"],
        ["Declaratory Judgement", "Inactive", "No", "No"],
        ["Title in Deceased Owners Name", "Inactive", "No", "No"],
        ["< UNASSIGNED >", "Inactive", "No", "No"],
    ]
) + """

""" + section("P1-S4 · Lots Table") + """
<div class="spec-ref">Source: <span>WF001 Spec §3.3</span> · Referenced by: <span>WF001, WF002, WF003 (cascade dropdowns)</span></div>
""" + step("1","Create the Lots table","<p>In QB → Tables → + New Table. Name: <code>Lots</code>. This is the system-wide lot reference. Every Home Order, Rehab Record, and Disposition Item links to a Lot record.</p>") + """
""" + step("2","Add all fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Lot ID", "Auto-number", "Auto", "System-generated primary key."],
        ["Community", "Relationship → Communities", "Yes", "Links to the Communities table. Drives the Community → Lot cascade."],
        ["Lot Number", "Text", "Yes", "Must be unique within community. Used in form display and cascade filters."],
        ["Lot Status", "Relationship → Lot Status", "Yes", "Links to Lot Status reference table. Set by automation only — never manually by CM. Drives all cascade filters system-wide."],
        ["Has Active Asset", "Formula (Checkbox)", "Auto", "True if count of linked assets > 0 and Status ≠ Archived."],
        ["Active Asset Status", "Lookup", "Auto", "Pulls status field from the active linked asset record."],
        ["Current Resident Name", "Text", "No", "Updated at move-in / move-out."],
        ["Buildable Envelope", "Text", "No", "Lot dimension constraints for home placement."],
        ["Door Swing", "Text", "No", "Entry door orientation relative to lot."],
        ["Electrical Details", "Text", "No", "Panel size, service type."],
        ["Water / Sewer Available", "Checkbox", "No", "Confirmed utilities present at lot."],
        ["Site Survey Completed", "Checkbox", "No", "Required for Gate HO-G2 (Home Order approval)."],
        ["Site Survey Upload", "File Attachment", "No", "Survey document."],
        ["Notes", "Text (multi-line)", "No", "Internal notes."],
    ]
) + """
""" + step("3","Import lot records from Rent Manager","<p>Export all lots from RM (all 68 communities) as CSV. Import into QB Lots table. Map Community to Community Short Name. After import, verify Lot Count matches RM totals per community. Set Lot Status = <code>Lot</code> (Available) as the default for all vacant lots.</p>") + """
""" + crit("Lot Status must be kept current at all times — it drives every cascade filter in the system. If Lot Status is wrong, wrong lots appear in forms. Automations LS-1 through LS-6 (Phase 2) maintain Lot Status automatically. Until those automations are live, Sys Admin is responsible for manual updates.") + """
</div>

<!-- ========================= PHASE 2 ========================= -->
<div class="page-break"></div>
""" + phase_header("2","WF001 — Home Ordering","green","Spec v1.2 · Approved","12 stages · 7 tables · 4 FastField forms · 20 automations (A1–A14, LS-1–LS-6) · 9 gate rules") + """
<div class="content">
<div class="summary-bar">
  <div class="summary-chip"><strong>7</strong> QB Tables</div>
  <div class="summary-chip"><strong>4</strong> FastField Forms</div>
  <div class="summary-chip"><strong>14</strong> Workflow Automations</div>
  <div class="summary-chip"><strong>6</strong> Lot Status Automations</div>
  <div class="summary-chip"><strong>9</strong> Gate Rules</div>
  <div class="summary-chip"><strong>12</strong> Workflow Stages</div>
</div>

""" + section("P2-S1 · Home Orders Table (Master)") + """
<div class="spec-ref">Source: <span>WF001 Spec §3.2</span></div>
""" + step("1","Create the Home Orders table","<p>In QB → Tables → + New Table. Name: <code>Home Orders</code>. This is the spine of WF001 — one record = one home order.</p>") + """
""" + step("2","Add identity & property fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Record ID#", "Auto-number", "Auto", "QB system field — leave as-is."],
        ["Home Order #", "Formula (Text)", "Auto", "Formula: 'HO-' & Text(Year([Date Created])) & '-' & Right('000' & [Record ID#], 3)"],
        ["Community / Property", "Relationship → Communities", "Yes", "Top of cascade chain. Drives Lot filter. Always selected first."],
        ["Lot Number", "Relationship → Lots", "Yes", "Filtered: only lots in selected Community where Lot Status = 'Lot' (Available). Cascades from Community selection."],
        ["Infill Reason", "Multi-select", "Yes", "Values: Occupied Lot Turnover | Vacant Lot | Demo Lot"],
        ["Date Created", "Date", "Auto", "Auto-set on record creation."],
        ["Created By", "User", "Auto", "Auto-set on record creation."],
    ]
) + """
""" + step("3","Add manufacturer & home detail fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Manufacturer", "Multi-select", "Yes", "Values: Cavco | Clayton | Skyline | Champion | Other"],
        ["Floor Plan Name", "Text", "Yes", "Free text — name as provided by manufacturer."],
        ["Model", "Text", "No", "Model number/name."],
        ["Production Line", "Text", "Yes", "Production line code from manufacturer."],
        ["Home Type", "Multi-select", "Yes", "Values: Single Wide | Double Wide | Triple Wide"],
        ["Setup Type", "Multi-select", "No", "Values: Piers | Runners | Full Slab | Stem Wall"],
        ["Dimensions", "Text", "No", "e.g., 16x76"],
        ["Square Footage", "Numeric", "No", "Calculated from dimensions or entered manually."],
        ["Bedrooms", "Numeric", "No", "Integer."],
        ["Bathrooms", "Numeric (decimal)", "No", "e.g., 2.0, 2.5"],
        ["Serial Number", "Text", "No*", "Required before advancing to Delivery Scheduled (enforced by Gate HO-G3). Enter when known."],
    ]
) + """
""" + step("4","Add dates & timeline fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Order Date", "Date", "Yes", "mm/dd/yy"],
        ["Online Date", "Date", "No", "When home enters factory production. Triggers A4 notification on change."],
        ["Offline Date", "Date", "No", "When home leaves factory. Triggers A4 notification on change."],
        ["Estimated Delivery Date", "Date", "Yes (at HO-G1)", "Triggers A4 notification on change."],
        ["Actual Delivery Date", "Date", "No", "Required before advancing to CI Ready (Gate HO-G4)."],
        ["Set Date", "Date", "No", "Date home is set on lot."],
        ["Construction Inspection Date", "Date", "Auto", "Auto-set when Construction Inspection Record created."],
        ["Ops Readiness Date", "Date", "Auto", "Auto-set when Ops Readiness Record created."],
        ["Listing Date", "Date", "Auto", "Auto-set at Stage 12 (Listed — Complete)."],
        ["Storage Start Date", "Date", "Conditional", "Set when Storage Required = Yes is checked."],
    ]
) + """
""" + step("5","Add financial fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Purchase Price", "Currency", "Yes", "$1,234.56 format. Required for Gate HO-G2."],
        ["Purchase Date", "Date", "Yes", "mm/dd/yy."],
        ["Floorplan Line", "Text", "No", "Accounting reference."],
        ["Loan Number", "Text", "No", "Lender loan number."],
        ["Loan Amount", "Currency", "No", "$1,234.56 format."],
        ["Lender", "Text", "No", "Lender name."],
        ["Insurance Carrier", "Text", "No", "Required before listing."],
        ["Insurance Policy #", "Text", "No", "Required before listing."],
    ]
) + """
""" + step("6","Add status & stage fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Workflow Stage", "Multi-select (locked)", "Yes", "12 values — see stage list below. Set by automations & gates ONLY. Never manually edited by Community Managers."],
        ["Status", "Multi-select", "Yes", "Values: Active | On Hold | Cancelled"],
        ["Storage Required?", "Checkbox", "No", "When checked, triggers Automation A5 and activates the Stage 7 (In Storage) path."],
        ["Storage Location", "Multi-select", "Conditional", "Values: On Lot | Manufacturer | Community | Other. Required when Storage Required = Yes."],
        ["Lot Fit Issue?", "Checkbox", "No", "Checked if delivered home does not fit lot. Triggers A9 (hard stop + escalation)."],
        ["RM Asset Record #", "Text", "No", "Manual cross-reference to Rent Manager asset record."],
        ["RM Unit #", "Text", "No", "Manual cross-reference to RM unit number."],
        ["Internal Notes", "Text (multi-line)", "No", ""],
        ["Last Updated", "Date/Time", "Auto", "QB auto-stamp."],
        ["Last Updated By", "User", "Auto", "QB auto-stamp."],
    ]
) + """
""" + step("7","Configure the Workflow Stage field values","<p>The Workflow Stage field must contain exactly these 12 values in this order:</p>") + """
""" + field_table(
    ["#", "Stage Name", "Notes"],
    [
        ["1", "Infill Need Identified", "Starting stage on new record creation."],
        ["2", "Lot Due Diligence", "Site survey and lot assessment."],
        ["3", "Home Selected", "Manufacturer and floor plan confirmed."],
        ["4", "Order Placed", "Order submitted to manufacturer."],
        ["5", "File & Asset Setup", "RM record creation, insurance, loan docs."],
        ["6", "In Production", "Home in factory."],
        ["7", "In Storage", "★ Conditional — activated only when Storage Required = Yes. Skip to Stage 8 if no storage."],
        ["8", "Delivery Scheduled", "Carrier and date confirmed."],
        ["9", "Delivered", "Home on lot — triggered by FastField Form 1 submission."],
        ["10", "Home Set & Construction Inspection", "Setup complete; FastField Form 2 underway."],
        ["11", "Ops & Sales Readiness", "FastField Form 3 underway."],
        ["12", "Listed — Complete", "All gates cleared; home listed."],
    ]
) + """
""" + warn("Stage 7 (In Storage) is conditional. The path is: Stage 6 → Stage 8 (no storage) OR Stage 6 → Stage 7 → Stage 8 (storage required). Configure Automation A5 (Phase 2, P2-S13) to handle this branching.") + """

""" + section("P2-S2 · Workflow Tasks Table") + """
<div class="spec-ref">Source: <span>WF001 Spec §3.4</span></div>
""" + step("1","Create the Workflow Tasks table","<p>In QB → Tables → + New Table. Name: <code>Workflow Tasks</code>. This is a child table of Home Orders — one record per task per home order.</p>") + """
""" + step("2","Add all fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Task ID", "Auto-number", "Auto", "System-generated."],
        ["Task #", "Formula (Text)", "Auto", "Formula: 'TK-' & Text(Year([Date Created])) & '-' & Right('00000' & [Record ID#], 5)"],
        ["Home Order", "Relationship → Home Orders", "Yes", "Parent record. Auto-linked by automations."],
        ["Task Name", "Text", "Yes", "Auto-populated by automation templates."],
        ["Task Category", "Multi-select", "Yes", "Values: Due Diligence | Order | Setup | Delivery | Inspection | Readiness | Listing"],
        ["Assigned To", "User", "No", "QB user account. Auto-set by automation."],
        ["Assigned Role", "Multi-select", "No", "Role from Roles Reference (§ P0-S2)."],
        ["Due Date", "Date", "No", "Auto-populated from Order Date offset by automation rule."],
        ["Status", "Multi-select", "Yes", "Values: Not Started | In Progress | Complete | Blocked"],
        ["Completed Date", "Date", "No", "Set when Status → Complete."],
        ["Completion Notes", "Text (multi-line)", "No", ""],
        ["Required Before Next Stage", "Checkbox", "No", "Gate enforcement flag — checked tasks must be Complete before stage advances."],
    ]
) + """

""" + section("P2-S3 · Delivery Records Table") + """
<div class="spec-ref">Source: <span>WF001 Spec §3.5 — Populated by FastField Form 1</span></div>
""" + step("1","Create the Delivery Records table","<p>In QB → Tables → + New Table. Name: <code>Delivery Records</code>. Child of Home Orders. One record per delivery per home. Populated via FastField Form 1 webhook.</p>") + """
""" + step("2","Add all fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Delivery Record ID", "Auto-number", "Auto", ""],
        ["Home Order", "Relationship → Home Orders", "Yes", "Matched via Home Order # from FastField payload."],
        ["Delivery Date", "Date", "Yes", "From FastField."],
        ["Received By", "User", "Yes", "From FastField."],
        ["Home Visually Confirmed", "Checkbox", "Yes", "From FastField."],
        ["Serial Number Photo", "File Attachment", "Yes", "Photo of VIN plate."],
        ["Serial Number Confirmed", "Text", "Yes", "Must match Home Orders.Serial Number."],
        ["Video Uploaded", "Checkbox", "Yes", "Walkaround video confirmed."],
        ["Photos Uploaded", "File Attachment", "Yes", "Minimum 5 exterior photos."],
        ["Photo Count", "Numeric", "Yes", "Minimum 5 required."],
        ["Exterior Checklist Completed", "Checkbox", "Yes", "Transportation damage check complete."],
        ["Lot Fit Confirmed", "Checkbox", "Yes", "If No → triggers Lot Fit Issue flag on Home Order + Automation A9."],
        ["Delivery Notes", "Text (multi-line)", "No", ""],
        ["Submitted Via", "Text (auto)", "Auto", "Always: FastField"],
        ["Submission Timestamp", "Date/Time (auto)", "Auto", "Auto-set on FastField submission."],
    ]
) + """

""" + section("P2-S4 · Construction Inspection Records Table") + """
<div class="spec-ref">Source: <span>WF001 Spec §3.6 — Populated by FastField Form 2 (89-item checklist)</span></div>
""" + step("1","Create the Construction Inspection Records table","<p>In QB → Tables → + New Table. Name: <code>Construction Inspection Records</code>. Child of Home Orders. Populated via FastField Form 2 webhook. Represents Director of Construction sign-off.</p>") + """
""" + step("2","Add header & identity fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Inspection Record ID", "Auto-number", "Auto", ""],
        ["Home Order", "Relationship → Home Orders", "Yes", "Matched via Home Order # from FastField payload."],
        ["Inspection Date", "Date", "Yes", "From FastField."],
        ["Inspected By", "User", "Yes", "Director of Construction or designee."],
        ["Setup Type", "Multi-select", "Yes", "Values: Piers | Runners | Full Slab | Stem Wall"],
        ["City / State", "Text", "Yes", "Community location."],
    ]
) + """
""" + step("3","Add section pass/fail count fields","<p>Add one numeric field per section for Pass counts and one for Fail counts (auto-calculated from FastField payload):</p>") + """
""" + field_table(
    ["Section", "Pass Count Field", "Fail Count Field", "N/A Count Field", "Item Count"],
    [
        ["A — Roof: Structural Integrity & Installation", "Roof — Pass Count", "Roof — Fail Count", "Roof — N/A Count", "10"],
        ["B — Underneath Home", "Underneath — Pass Count", "Underneath — Fail Count", "Underneath — N/A Count", "12"],
        ["C — Exterior", "Exterior — Pass Count", "Exterior — Fail Count", "Exterior — N/A Count", "5"],
        ["D — Home Interior", "Interior — Pass Count", "Interior — Fail Count", "Interior — N/A Count", "27"],
        ["E — Windows & Doors", "Win/Doors — Pass Count", "Win/Doors — Fail Count", "Win/Doors — N/A Count", "6"],
        ["F — Electrical", "Electrical — Pass Count", "Electrical — Fail Count", "Electrical — N/A Count", "13"],
        ["G — Plumbing", "Plumbing — Pass Count", "Plumbing — Fail Count", "Plumbing — N/A Count", "16"],
    ]
) + """
""" + step("4","Add calculated summary & sign-off fields","") + """
""" + field_table(
    ["Field Name", "Type", "Notes"],
    [
        ["Total Items Inspected", "Numeric", "89 total items possible."],
        ["Total Pass", "Numeric (formula)", "Sum of all Section Pass Count fields."],
        ["Total Fail", "Numeric (formula)", "Sum of all Section Fail Count fields. If > 0 → triggers A11 (remediation task)."],
        ["Total N/A", "Numeric (formula)", "Sum of all Section N/A Count fields."],
        ["All Items Pass or N/A", "Formula (Checkbox)", "True when Total Fail = 0. Triggers A10 (advance to Ops & Sales Readiness)."],
        ["Items Requiring Attention", "Text (multi-line)", "Description of any failed items. From FastField."],
        ["Construction Sign-Off", "Checkbox", "Final sign-off by Director of Construction. Must be checked before Form 3 can begin."],
        ["Sign-Off Date", "Date", "Date of construction sign-off."],
        ["Full Inspection PDF", "File Attachment", "FastField auto-generates and attaches."],
        ["Submitted Via", "Text (auto)", "Always: FastField"],
        ["FastField Submission ID", "Text", "UUID from FastField. Stored for audit traceability."],
    ]
) + """

""" + section("P2-S5 · Ops Readiness Records Table") + """
<div class="spec-ref">Source: <span>WF001 Spec §3.7 — Populated by FastField Form 3 (71-item checklist)</span></div>
""" + step("1","Create the Ops Readiness Records table","<p>In QB → Tables → + New Table. Name: <code>Ops Readiness Records</code>. Child of Home Orders. Populated via FastField Form 3 webhook. Requires Construction sign-off on file as prerequisite.</p>") + """
""" + step("2","Add header & identity fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Readiness Record ID", "Auto-number", "Auto", ""],
        ["Home Order", "Relationship → Home Orders", "Yes", "Matched via Home Order # from FastField."],
        ["Inspection Date", "Date", "Yes", "From FastField."],
        ["Home Type", "Multi-select", "Yes", "Values: New Delivery | Rehab | Turnover"],
        ["Inspection Type", "Multi-select", "Yes", "Values: Weekly | Pre-Listing | Pre-Move-In"],
        ["Construction Sign-Off On File", "Checkbox", "Yes", "Must be checked — prerequisite before form submits. Pulls from parent Home Order's Construction Inspection record."],
        ["Completed By — Facility Mgr", "User", "Yes", "Facility Manager sign-off."],
        ["Completed By — Comm Mgr / Sales Rep", "User", "Yes", "Community Manager or Sales Rep sign-off."],
    ]
) + """
""" + step("3","Add section fail count fields (10 sections)","") + """
""" + field_table(
    ["Section (from Form 3)", "Fail Count Field", "Item Count"],
    [
        ["A — Utility Verification", "Utility — Fail Count", "10"],
        ["B — Rehab-Specific Utility Verification", "Rehab Utility — Fail Count", "4"],
        ["C — Mechanical & Safety", "Mechanical Safety — Fail Count", "5"],
        ["D — Exterior & Curb Appeal", "Exterior — Fail Count", "8"],
        ["E — Entry, Windows & Doors", "Entry Win Doors — Fail Count", "6"],
        ["F — Kitchen", "Kitchen — Fail Count", "9"],
        ["G — Bathrooms", "Bathrooms — Fail Count", "7"],
        ["H — Interior Presentation & Living Spaces", "Interior — Fail Count", "8"],
        ["I — Cleanliness", "Cleanliness — Fail Count", "8"],
        ["J — Escalation & Follow-Up", "Escalation — Fail Count", "6"],
    ]
) + """
""" + step("4","Add calculated summary, escalation & sign-off fields","") + """
""" + field_table(
    ["Field Name", "Type", "Notes"],
    [
        ["Total Fail Count", "Numeric (formula)", "Sum of all 10 Section Fail Count fields. If > 0 → triggers A13 (remediation)."],
        ["Home Ready for Listing", "Formula (Checkbox)", "True when Total Fail Count = 0. Triggers A12 (advance to pre-listing)."],
        ["Issue Description / Escalation Notes", "Text (multi-line)", "Required if any fails."],
        ["Regional Mgr Notified", "Checkbox", "Escalation tracking."],
        ["Vendor Notified", "Checkbox", "Escalation tracking."],
        ["Work Order Submitted", "Checkbox", "Escalation tracking."],
        ["Follow-Up Date", "Date", "Escalation tracking."],
        ["Facility Mgr Sign-Off", "Checkbox", "Facility Manager final sign-off."],
        ["Comm Mgr / Sales Rep Sign-Off", "Checkbox", "Community Manager / Sales Rep final sign-off."],
        ["Full Readiness PDF", "File Attachment", "FastField auto-generated."],
        ["Submitted Via", "Text (auto)", "Always: FastField"],
    ]
) + """

""" + section("P2-S6 · Listing Records Table") + """
<div class="spec-ref">Source: <span>WF001 Spec §3.8 — Populated by FastField Form 4</span></div>
""" + step("1","Create the Listing Records table","<p>In QB → Tables → + New Table. Name: <code>Listing Records</code>. Child of Home Orders. Populated via FastField Form 4. Triggers Stage 12 (Listed — Complete) via Automation A14.</p>") + """
""" + step("2","Add all fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Listing Record ID", "Auto-number", "Auto", ""],
        ["Home Order", "Relationship → Home Orders", "Yes", "Matched via Home Order # from FastField."],
        ["Listed By", "User", "Yes", "Sales staff who completed the listing form."],
        ["Listing Date", "Date", "Yes", "mm/dd/yy."],
        ["Construction Inspection Approved", "Checkbox", "Yes", "Pre-listing verification item 1 of 7."],
        ["Ops & Sales Readiness Approved", "Checkbox", "Yes", "Pre-listing verification item 2 of 7."],
        ["Insurance Active in RM", "Checkbox", "Yes", "Pre-listing verification item 3 of 7."],
        ["Loan Documents Uploaded to RM", "Checkbox", "Yes", "Pre-listing verification item 4 of 7."],
        ["Serial Number Confirmed in RM", "Checkbox", "Yes", "Pre-listing verification item 5 of 7."],
        ["Asset Status Updated in RM", "Checkbox", "Yes", "Pre-listing verification item 6 of 7."],
        ["Manufacturer Packet Confirmed", "Checkbox", "Yes", "Pre-listing verification item 7 of 7."],
        ["All Pre-Listing Items Complete", "Formula (Checkbox)", "Auto", "True only when all 7 above = Yes. Formula: [Item1] AND [Item2] AND [Item3] AND [Item4] AND [Item5] AND [Item6] AND [Item7]. Triggers A14 when True."],
        ["Internal Notification Sent", "Checkbox (auto)", "Auto", "Auto-set by Automation A14."],
        ["Notes", "Text (multi-line)", "No", ""],
    ]
) + """

""" + section("P2-S7 · Cascading Dropdown Configuration") + """
<div class="spec-ref">Source: <span>WF001 Spec §3A — System-wide standard. Applies to all QB and FastField forms.</span></div>
""" + crit("SYSTEM-WIDE STANDARD — NO EXCEPTIONS. Every form that includes Community, Lot, or Asset selection MUST follow this configuration. Do not use free-text fields for these selections.") + """
""" + step("1","Configure Community → Lot relationship","<p>In QB → Relationships: confirm Communities → Lots relationship exists (one-to-many). In the Lots table's Community field settings, ensure it links to the Communities table.</p>") + """
""" + step("2","Configure Lot field filter on every form","<p>On every QB form that includes a Lot field: In the Lot field's form settings → enable <em>Filter related records</em> → add filter: <code>[Community on Lot record] = [Community on current form]</code>. Then add a second filter condition for Lot Status based on the form context (see table below).</p>") + """
""" + field_table(
    ["Form / Context", "Lot Status Filter", "Asset Filter"],
    [
        ["Home Order (new)", "Lot Status = Lot (Available only)", "No asset — new home being ordered"],
        ["Move In", "Lot Status = Lot OR Lot-Avail(POH) (Allows Move In = Yes)", "If community-owned home sale → listed assets on Lot"],
        ["Move Out", "Lot Status = any Active rental status (Allows Move Out = Yes)", "Assets on selected Lot"],
        ["Rehab Walkthrough (WF002)", "Lot Status = Lot-In Rehab (Allows Rehab = Yes)", "Rehab-in-Process assets on Lot"],
        ["Construction Inspection (FF Form 2)", "Pre-populated via launch link — do not filter manually", "Linked to QB Home Order record"],
        ["Ops & Sales Readiness (FF Form 3)", "Pre-populated via launch link — do not filter manually", "Linked to QB Home Order record"],
        ["WF003 Disposition Items", "No status restriction — any recently vacated unit may be reviewed", "No restriction — snapshot captured at review"],
    ]
) + """
""" + step("3","Configure FastField pre-populated launch links","<p>Field forms (Delivery Confirmation, Construction Inspection, Ops Readiness) use QB-generated launch links — field staff do not manually select Community, Lot, or Home Order. Configure as follows:</p><ul><li>In QB → Home Orders table → create a formula URL field: <code>\"https://app.fastfieldforms.com/form/[FORM_ID]?home_order=\" & [Home Order #] & \"&community=\" & URLEncode([Community]) & \"&lot=\" & URLEncode([Lot Number])</code></li><li>Add this launch link field to the QB Home Order record's view so managers can tap/click to open the pre-filled FastField form.</li><li>Confirm the link opens correctly on iOS and Android — test before go-live.</li></ul>") + """

""" + section("P2-S8 · QB Forms Configuration (10 forms)") + """
<div class="spec-ref">Source: <span>WF001 Spec §4.1</span></div>
""" + step("1","Create all 10 QB forms","<p>In QB → Home Orders table → Forms → + New Form. Create one form per row below:</p>") + """
""" + field_table(
    ["Form #", "Form Name", "Primary Users", "Key Behavior"],
    [
        ["Form 1", "New Home Order", "Sales", "Community, Lot (filtered: Available only), Infill Reason, Manufacturer, Floor Plan, Production Line, Order Date. Triggers LS-1 (Lot → Reserved) on save."],
        ["Form 2", "Lot Due Diligence Entry", "Operations / Construction", "All Lot table fields, pre-linked to the lot on the Home Order. Gate HO-G2 requires Site Survey Completed before stage advances."],
        ["Form 3", "Home Details & Asset Setup", "Asset Mgmt / Sales", "Model, Setup Type, Dimensions, Sq Ft, Bedrooms, Bathrooms, Home Type, RM Asset Record #, Purchase Price, Purchase Date. First RM cross-reference entry."],
        ["Form 4", "Date Management", "Sales", "Online Date, Offline Date, Estimated Delivery Date. Triggers A4 (date change notification) on every save where any date field changes."],
        ["Form 5", "Storage Entry", "Construction", "Storage Required (checkbox), Storage Location, Storage Start Date. Conditional — only shown when Storage Required = Yes. Triggers A5."],
        ["Form 6", "Delivery Coordination", "Construction", "Estimated Delivery Date update, delivery vendor notes, assigned receiver. Advances stage to Delivery Scheduled."],
        ["Form 7", "Post-Delivery Asset Update", "Asset Mgmt", "Actual Delivery Date, documentation status checklist, RM confirmation fields, Lot Fit Issue flag. Completed after FastField Form 1 is submitted."],
        ["Form 8", "Insurance & Loan Entry", "Accounting", "Floorplan Line, Loan Number, Loan Amount, Lender, Insurance Carrier, Insurance Policy #. Required for Gate HO-G2."],
        ["Form 9", "Set & Utility Coordination", "Construction", "Set Date, utility accounts live confirmation. Completed after home is set on the lot."],
        ["Form 10", "Pre-Listing Final Gate", "Sales", "All 7 pre-listing checklist items — hard validation: all must = Yes before form saves. Links to Listing Records table. Triggers A14."],
    ]
) + """

""" + section("P2-S9 · FastField Form 1 — Home Delivery Confirmation") + """
<div class="spec-ref">Source: <span>WF001 Spec §6.1 — QB target: Delivery Records table. Triggers: A7 (stage → Delivered).</span></div>
""" + step("1","Create Form 1 in FastField","<p>In FastField → Forms → + New Form. Name: <code>WF001 Form 1 — Home Delivery Confirmation</code>. Set QB target table: <code>Delivery Records</code>. Matching key: <code>Home Order #</code>.</p>") + """
""" + step("2","Build the form sections","") + """
""" + field_table(
    ["Section", "Fields", "Type", "Required"],
    [
        ["A — Home ID", "Home Order # (pre-populated); Community (pre-populated); Lot # (pre-populated); Delivery Date", "Text / Date", "All required"],
        ["B — Serial Number", "Serial Number (as shown on VIN plate); Serial Number Photo", "Text / Photo Capture", "Both required"],
        ["C — Photo & Video", "Walkaround Video uploaded (Yes/No); Exterior Photo Set (min 5 photos); Photo count verified", "Photo Capture / Checkbox", "All required"],
        ["D — Exterior Condition", "Transportation damage check: siding, eaves, windows, roof visual, foundation area. Pass / Fail / N/A + Notes per item.", "Dropdown + Notes", "All required"],
        ["E — Lot Fit", "Home fits lot as ordered (Yes/No). If No: description of fit issue (text field)", "Checkbox + Text", "Required"],
        ["F — Submission", "Received By (name); Inspector signature; Submission timestamp (auto)", "Text / Signature / Auto", "All required"],
    ]
) + """
""" + step("3","Configure FastField → QB webhook","<p>In FastField → Form 1 → Settings → Integrations → Webhook: enter the QB webhook URL for the Delivery Records table. Map FastField fields to QB fields (match names exactly as defined in P2-S3). Test with a sandbox submission.</p>") + """
""" + note("When Lot Fit Confirmed = No on the FastField submission, the webhook payload triggers A9 — the Lot Fit Issue flag is automatically set on the parent Home Order record and an escalation task is created. No manual action required from the field.") + """

""" + section("P2-S10 · FastField Form 2 — Construction Inspection (89 Items)") + """
<div class="spec-ref">Source: <span>WF001 Spec §6.2 — QB target: Construction Inspection Records. Completed by: Director of Construction. Triggers: A10 (all pass) or A11 (any fail).</span></div>
""" + step("1","Create Form 2 in FastField","<p>Name: <code>WF001 Form 2 — Construction Inspection</code>. QB target: <code>Construction Inspection Records</code>. Matching key: <code>Home Order #</code>. Pre-populated header fields from QB launch link: Property/Community, Lot #, Home Model, Serial Number.</p>") + """
""" + step("2","Build the 7 checklist sections (89 items total)","<p>Each item: Yes / No / N/A dropdown + Notes field. Set Hard Validation: form cannot submit if any item = No without documented reason override.</p>") + """
""" + field_table(
    ["Section", "Item Count", "Key Items"],
    [
        ["A — Roof: Structural Integrity & Installation", "10", "Shingles, ridge vent, debris-free, vents sealed, flashing"],
        ["B — Underneath Home: Structure, Blocking & Mechanical Runs", "12", "Blocking, marriage line seal, duct suspension, sewer/water crossovers, bottom board"],
        ["C — Exterior: Structural & Transportation Damage Check", "5", "Close-up boards, lap siding, transportation damage-free, GFI covers"],
        ["D — Home Interior: Installation Quality", "27", "Mate line doors, floors, trim, wall panels, appliances, cabinets, tubs, caulking, toilets, faucets, vinyl flooring"],
        ["E — Windows & Doors: Operation & Security", "6", "Interior/exterior doors, locks/keys, windows/screens/blinds"],
        ["F — Electrical Check", "13", "Switch plates, panel/breakers, GFI, receptacles, switches, appliances, smoke detectors, bath fans"],
        ["G — Plumbing Check", "16", "Pressure test, commodes, aerators, P-traps, sewer function test"],
    ]
) + """
""" + step("3","Add sign-off & submission fields","<p>Final section: <code>☐ APPROVED — All items confirmed</code> / <code>☐ ITEMS REQUIRING ATTENTION — See notes</code>. Director of Construction signature. Date. Submit button.</p>") + """
""" + step("4","Configure webhook to Construction Inspection Records","<p>Map all section pass/fail counts to the corresponding QB fields (Section A–G Pass/Fail Count fields). Map signature to Sign-Off field. Confirm <code>All Items Pass or N/A</code> formula evaluates correctly after webhook push.</p>") + """

""" + section("P2-S11 · FastField Form 3 — Ops & Sales Readiness (71 Items)") + """
<div class="spec-ref">Source: <span>WF001 Spec §6.3 — QB target: Ops Readiness Records. Completed by: Facility Manager + Comm Mgr/Sales Rep. Triggers: A12 (all pass) or A13 (any fail).</span></div>
""" + step("1","Create Form 3 in FastField","<p>Name: <code>WF001 Form 3 — Ops &amp; Sales Readiness</code>. QB target: <code>Ops Readiness Records</code>. Matching key: <code>Home Order #</code>. Pre-populated: Property/Community, Home/Unit #, from QB launch link.</p>") + """
""" + step("2","Add form header fields","<p>Home Type (New Delivery / Rehab / Turnover); Inspection Type (Weekly / Pre-Listing / Pre-Move-In); Construction Sign-Off on File? (Yes/No — <strong>must be Yes to submit</strong>); Completed By (auto from FastField login); Date (auto).</p>") + """
""" + step("3","Build the 10 checklist sections (71 items total)","") + """
""" + field_table(
    ["Section", "Item Count", "Who Completes"],
    [
        ["A — Utility Verification: Physically confirmed; no assumptions", "10", "Facility Manager"],
        ["B — Rehab-Specific Utility Verification (N/A if new delivery)", "4", "Facility Manager"],
        ["C — Mechanical & Safety", "5", "Facility Manager"],
        ["D — Exterior & Curb Appeal", "8", "Community Manager / Sales Rep"],
        ["E — Entry, Windows & Doors", "6", "Community Manager / Sales Rep"],
        ["F — Kitchen", "9", "Community Manager / Sales Rep"],
        ["G — Bathrooms", "7", "Community Manager / Sales Rep"],
        ["H — Interior Presentation & Living Spaces", "8", "Community Manager / Sales Rep"],
        ["I — Cleanliness: Turnover & Show Standard", "8", "Community Manager / Sales Rep"],
        ["J — Escalation & Follow-Up", "6", "Facility Manager"],
    ]
) + """
""" + step("4","Add two signature capture fields","<p>Signature 1: <em>Facility Manager — Utility &amp; Condition Verification</em>. Signature 2: <em>Community Manager / Sales Representative — Show-Readiness Sign-Off</em>. Both required for form submission.</p>") + """
""" + step("5","Configure webhook to Ops Readiness Records","<p>Map section fail counts to the corresponding QB fail count fields (P2-S5). Map Home Ready for Listing formula input fields. Confirm formula evaluates after webhook push.</p>") + """

""" + section("P2-S12 · FastField Form 4 — Listing Form") + """
<div class="spec-ref">Source: <span>WF001 Spec §6.4 — QB target: Listing Records. Completed by: Sales. Triggers: A14 (stage → Listed — Complete).</span></div>
""" + step("1","Create Form 4 in FastField","<p>Name: <code>WF001 Form 4 — Listing Form</code>. QB target: <code>Listing Records</code>. Matching key: <code>Home Order #</code>. Pre-populated: Home Order #, Community, Lot # from QB launch link.</p>") + """
""" + step("2","Build the verification section (7 items — ALL must be Yes)","<p>Create 7 Yes/No checkboxes. Hard validation: form <strong>cannot be submitted if any item = No</strong>. No override allowed.</p>") + """
""" + field_table(
    ["#", "Item", "Responsible Party"],
    [
        ["1", "Construction Inspection approved and sign-off on file", "Sales / Construction"],
        ["2", "Ops &amp; Sales Readiness approved and sign-off on file", "Sales / Ops"],
        ["3", "Insurance active in Rent Manager", "Accounting"],
        ["4", "Loan documents uploaded to Rent Manager", "Accounting"],
        ["5", "Serial number confirmed and recorded in Rent Manager", "Asset Management"],
        ["6", "Asset status updated in Rent Manager", "Asset Management"],
        ["7", "Manufacturer packet confirmed and on file", "Sales"],
    ]
) + """
""" + step("3","Add submission fields and configure webhook","<p>Submitted By (auto from FastField login); Submission Timestamp (auto). Configure webhook to Listing Records table in QB. After push, confirm <code>All Pre-Listing Items Complete</code> formula evaluates to True and triggers A14.</p>") + """

""" + section("P2-S13 · Automations A1–A14 (Workflow Automations)") + """
<div class="spec-ref">Source: <span>WF001 Spec §5 — All automations are QB-native Pipelines unless noted.</span></div>
""" + note("Build each automation in QB → Pipelines → + New Pipeline. Name each pipeline exactly as shown in the ID column. Set trigger and action as specified.") + """
""" + auto_table([
    ["A1", "New Home Order record created", "Immediate", "Create Stage 1–2 task set (lot due diligence tasks). Set Lot Status → Reserved via LS-1 automation. Assigned roles receive task notifications."],
    ["A2", "Workflow Stage changes to <em>Home Selected</em>", "Immediate", "Create Stage 3–4 task set (order confirmation, asset setup tasks). Notify Sales and Accounting."],
    ["A3", "Workflow Stage changes to <em>Order Placed</em>", "Immediate", "Create Stage 5 task set (file &amp; asset setup tasks). Notify Sales, Asset Mgmt, Ops Coord."],
    ["A4", "Online Date, Offline Date, or Estimated Delivery Date changes on a Home Order record", "On save", "Send date change notification email to all departments: Regional, Ops, Accounting, Asset Mgmt, Construction. Include new date values and Home Order # in email body."],
    ["A5", "Storage Required? = checked on Home Order record", "Immediate", "Create storage coordination task (assigned to Construction and Asset Mgmt). Set Stage path to include Stage 7 (In Storage). Flag record for Storage Aging view."],
    ["A6", "Scheduled daily at 6:00 AM ET", "Scheduled", "Check all Home Orders where Storage Required = Yes AND Storage Start Date populated. If (Today − Storage Start Date) > 30 days → send storage aging alert to Construction, Sales, Ops. Include community, lot, home details, and days in storage."],
    ["A7", "Delivery Records child record created (FastField Form 1 webhook received)", "On record creation", "Set Workflow Stage → Delivered. Create post-delivery task set (assigned to Asset Mgmt, Accounting, Sales). Send delivery confirmation notification."],
    ["A8", "Workflow Stage = Delivery Scheduled AND Serial Number is blank", "Immediate (on stage change)", "Send non-blocking warning notification to Sales and Asset Mgmt: 'Serial number is missing before delivery. Please update before the home arrives.' This is a warning only — does not block stage advancement."],
    ["A9", "Lot Fit Issue? = checked on Home Order record", "Immediate", "Send immediate alert to Sales, Asset Mgmt, and Accounting. Create escalation task (assigned to Construction). <strong>Hard stop: block Workflow Stage advancement until Lot Fit Issue = unchecked by authorized user.</strong>"],
    ["A10", "Construction Inspection Record created AND All Items Pass or N/A = True", "Immediate", "Set Workflow Stage → Ops &amp; Sales Readiness. Send notification to Facility Manager, Comm Mgr, Sales: 'Construction inspection passed. Home is ready for Ops &amp; Sales Readiness inspection.'"],
    ["A11", "Construction Inspection Record created AND Total Fail > 0", "Immediate", "Create remediation task assigned to Director of Construction. Block Workflow Stage advancement. Notification to Construction: 'Construction inspection has [N] failed items. Remediation required before advancing.'"],
    ["A12", "Ops Readiness Record created AND Home Ready for Listing = True", "Immediate", "Set Workflow Stage → pre-listing stage. Create listing task assigned to Sales and Asset Mgmt. Notification: 'Ops &amp; Sales Readiness passed. Home is ready for pre-listing verification.'"],
    ["A13", "Ops Readiness Record created AND Total Fail Count > 0", "Immediate", "Create remediation task assigned to Ops, Construction, Sales. Block Workflow Stage advancement. Notification: 'Ops &amp; Sales Readiness inspection has [N] failed items. Issues must be resolved before listing.'"],
    ["A14", "Listing Records created AND All Pre-Listing Items Complete = True", "Immediate", "Set Workflow Stage → Listed — Complete (Stage 12). Send team notification to all roles. Set Lot Status to stay Reserved (per LS-5 — do not change to Available until Move In)."],
]) + """

""" + section("P2-S14 · Lot Status Automations LS-1 – LS-6") + """
<div class="spec-ref">Source: <span>WF001 Spec §5 (LS rules) and §3A — Critical for cascade filter accuracy. These are not optional.</span></div>
""" + crit("These 6 automations maintain Lot Status accuracy in real time. Without them, cascade dropdown filters will show wrong lots to users. Build and test all 6 before go-live.") + """
""" + field_table(
    ["Rule", "Trigger", "Lot Status Change", "Notes"],
    [
        ["LS-1", "New Home Order record created (linked to a Lot)", "Available → Reserved (Lot → Reserved)", "Lot committed to this order. Immediately removed from new Home Order and Move In filters."],
        ["LS-2", "Home Order Status changes to Cancelled", "Reserved → Available (back to 'Lot')", "Lot freed. Immediately re-appears in applicable filters."],
        ["LS-3", "Move In request processed/approved in QB", "Reserved → Occupied (Lot-Rental or Lot-LTP)", "Resident has moved in. Lot now appears in Move Out filter only."],
        ["LS-4", "Move Out request processed/approved in QB", "Occupied → Available ('Lot')", "Lot is vacant again. Re-appears in Move In and new Home Order filters."],
        ["LS-5", "Workflow Stage changes to Listed — Complete (Stage 12)", "No change — stays Reserved", "Lot stays Reserved until Move In is processed (LS-3). Do not change to Available."],
        ["LS-6", "Home delisted with no active resident on lot", "Reserved → Available ('Lot')", "Listing cancelled before move-in. Lot freed back to available pool."],
    ]
) + """

""" + section("P2-S15 · Gate Rules — WF001") + """
<div class="spec-ref">Source: <span>WF001 Spec §8 — All gates are hard blocks. No soft warnings that allow continuation.</span></div>
""" + warn("Every gate must be implemented as a hard field-level validation block in QB — the stage field is locked until all conditions are met. Gates that can be bypassed are not compliant.") + """
<div class="sub2-title">Home Ordering Gates (§8.1)</div>
""" + gate_table([
    ["HO-G1", "Draft → Submitted for Approval", "Draft → Submitted", "ALL must be true: Community selected; Lot ID populated; Home Model selected; Floor Plan selected; Estimated Delivery Date populated; Purchase Price populated; Submitted By populated. <br>Error: <em>'Required fields are missing. Please complete all required fields before submitting.'</em>"],
    ["HO-G2", "Submitted → Approved / In Production", "Submitted → In Production", "Austin (Owner) has stamped Approved; Approval Timestamp auto-populated; Order Number assigned; Purchase Price populated; Site Survey Completed on linked Lot record.<br>Error: <em>'This order requires Austin's approval before advancing to In Production.'</em>"],
    ["HO-G3", "In Production → Delivered to Site", "In Production → Delivered", "Actual Delivery Date populated; Delivery Confirmation attachment uploaded (FastField Form 1 record exists); Lot ID confirmed match.<br>Error: <em>'Delivery cannot be confirmed until the Delivery Confirmation form (FastField Form 1) has been submitted.'</em>"],
    ["HO-G4", "Delivered → Ready for Construction Inspection", "Delivered → Home Set & CI", "Utility connections confirmed; Set-up complete flag = Yes (Set Date populated).<br>Error: <em>'Home must be set on the lot and utilities confirmed before starting Construction Inspection.'</em>"],
]) + """
<div class="sub2-title">Construction Inspection Gates (§8.2)</div>
""" + gate_table([
    ["CI-G1", "Ready for Inspection → Inspection In Progress", "Home Set & CI → CI In Progress", "FastField Form 2 launched with valid Home Order #; Inspector identity confirmed (Inspected By populated).<br>Error: <em>'Construction Inspection cannot begin without a valid Home Order # and confirmed inspector.'</em>"],
    ["CI-G2", "Inspection In Progress → Passed", "CI In Progress → Ops & Sales Readiness", "All 89 checklist items = Yes or N/A (Total Fail = 0); Form submitted via FastField; QB Construction Inspection Record created; Construction Sign-Off = checked.<br>Error: <em>'Construction Inspection cannot pass until all items are confirmed and the Director of Construction has signed off.'</em>"],
    ["CI-G3", "Inspection In Progress → Failed", "CI In Progress → Deficiency Resolution", "One or more checklist items = No/Fail; Deficiency/remediation records auto-created by A11; Re-inspection must be scheduled before re-advancing."],
    ["CI-G4", "Deficiency Resolution → Re-inspection", "Deficiency → Re-inspection", "All remediation tasks for this Home Order = Complete; Resolution notes populated; Resolved By and Resolved Date stamped.<br>Error: <em>'All [N] outstanding remediation tasks must be marked Complete before re-inspection can begin.'</em>"],
]) + """
<div class="sub2-title">Operations Inspection Gates (§8.3)</div>
""" + gate_table([
    ["OI-G1", "Ready for Ops Review → Ops Inspection In Progress", "Ops & Sales Readiness → Ops In Progress", "Construction Inspection CI-G2 passed (CI All Items Pass = True; CI Sign-Off = Yes); FastField Form 3 launched with valid Home Order #.<br>Error: <em>'Ops &amp; Sales Readiness inspection cannot begin until Construction Inspection is fully approved and signed off.'</em>"],
    ["OI-G2", "Ops Inspection In Progress → Passed", "Ops In Progress → Pre-Listing", "All 71 checklist items = Yes or N/A (Ops Total Fail = 0); Manufacturer packet confirmed on file; Asset status updated in RM; Both sign-offs (Facility Mgr + Comm Mgr) checked; Form submitted via FastField.<br>Error: <em>'Ops &amp; Sales Readiness cannot be approved until all items are confirmed and both signatures are on file.'</em>"],
    ["OI-G3", "Pending Final Approval → Listed — Complete", "Pre-Listing → Listed — Complete", "All 7 pre-listing items on Listing Record = Yes (All Pre-Listing Items Complete = True); FastField Form 4 submitted; Austin approval stamp present.<br>Error: <em>'All 7 pre-listing verification items must be confirmed before the home can be listed as Complete.'</em>"],
]) + """

""" + section("P2-S16 · Views & Dashboards") + """
<div class="spec-ref">Source: <span>WF001 Spec §4.2</span></div>
""" + step("1","Create all 6 standard views","<p>In QB → Reports → + New Report. Create one report per row below:</p>") + """
""" + field_table(
    ["View #", "Name", "Primary User", "Filter / Sort"],
    [
        ["View 1", "Pipeline Board", "All roles", "Kanban by Workflow Stage. Color-coded: Green = on track, Yellow = approaching deadline, Red = overdue or blocked."],
        ["View 2", "My Tasks", "All assigned users", "Filtered: Assigned To = [Current User]. Sorted by Due Date ascending. Shows only tasks assigned to the logged-in user."],
        ["View 3", "Sales Master Tracker", "Sales", "All active Home Orders. Key dates inline-editable. Sortable by stage, community, manufacturer, or date."],
        ["View 4", "Overdue / Blocked Alert", "Management", "Filtered: Status = Blocked OR (Due Date < today AND Status ≠ Complete). Management escalation view."],
        ["View 5", "Storage Aging Report", "Construction / Sales", "Filtered: Storage Required = Yes. Calculated field: Days in Storage = Today − Storage Start Date. Homes > 30 days flagged Red. Sorted by days descending."],
        ["View 6", "Accounting Tracker", "Accounting", "Financial fields only: Purchase Price, Loan Amount, Insurance. Filterable by 'action needed' flag. Inline editable for Accounting fields only."],
    ]
) + """
</div>

<!-- ========================= PHASE 3 ========================= -->
<div class="page-break"></div>
""" + phase_header("3","WF002 — Rehab","yellow","Spec v1.3 · Approved","9 stages · 5 tables (2 ref + 3 main) · 1 FastField form · 12 automations · 8 gate rules · SharePoint vendor integration") + """
<div class="content">
<div class="summary-bar">
  <div class="summary-chip"><strong>5</strong> QB Tables</div>
  <div class="summary-chip"><strong>1</strong> FastField Form</div>
  <div class="summary-chip"><strong>12</strong> Automations</div>
  <div class="summary-chip"><strong>8</strong> Gate Rules</div>
  <div class="summary-chip"><strong>9</strong> Workflow Stages</div>
  <div class="summary-chip"><strong>37</strong> Checklist Items</div>
</div>
""" + note("The Lot Status and Asset Status reference tables (Phase 1) are shared with WF002. Do not recreate them. WF002 automations write to these same tables.") + """

""" + section("P3-S1 · Rehab Records Table (RH) — Main Table") + """
<div class="spec-ref">Source: <span>WF002 Spec §4C — Parent table. One record per home rehab project.</span></div>
""" + step("1","Create the Rehab Records table","<p>In QB → Tables → + New Table. Name: <code>Rehab Records</code>. This is the parent/master table for WF002. One record = one rehab project.</p>") + """
""" + step("2","Add identity & location fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Rehab ID", "Formula (Text)", "Auto", "Format: RH-YYYY-###. Formula: 'RH-' & Text(Year([Date Created])) & '-' & Right('000' & [Record ID#], 3). Auto-generated on record creation."],
        ["Community", "Relationship → Communities", "Yes", "Top of cascade chain. Required."],
        ["Lot", "Relationship → Lots", "Yes", "Filtered to selected Community. Lot Status = Lot-In Rehab or Lot (any non-Occupied, Allows Rehab = Yes)."],
        ["Asset", "Relationship → Asset Status lookup", "Yes", "Filtered to selected Lot. Required."],
        ["RM Asset Record #", "Text", "No", "Manual cross-reference to RM asset record. Not auto-synced."],
        ["RM Unit #", "Text", "No", "Manual cross-reference to RM unit number."],
    ]
) + """
""" + step("3","Add workflow state fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Rehab Stage", "Multi-select (locked)", "Yes", "9 values: 1 Rehab Identified | 2 Scope Assessed | 3 Work Assigned | 4 Work In Progress | 5 Walkthrough Scheduled | 6 Walkthrough Complete | 7 Items To Resolve | 8 Approved — Ready to Market | 9 Closed. Locked by gate rules. Cannot skip stages."],
        ["Triggered By", "Multi-select", "Yes", "Values: TBD Report | Manual | Move Out | Acquisition. Determines source of rehab identification."],
        ["Source Report Reference", "Text", "Conditional", "If Triggered By = TBD Report — report ID or run date."],
        ["Source Move Out Record #", "Relationship → Move Out Records", "Conditional", "If Triggered By = Move Out — links to originating Move Out record."],
    ]
) + """
""" + step("4","Add dates fields","") + """
""" + field_table(
    ["Field Name", "Type", "Notes"],
    [
        ["Rehab Identified Date", "Date (auto)", "Auto-populated by A-RH-01 on record creation."],
        ["Scope Assessed Date", "Date (auto)", "Set by A-RH-02 when Stage advances to Scope Assessed."],
        ["Work Assigned Date", "Date (auto)", "Set by A-RH-03 when Stage advances to Work Assigned."],
        ["Work Started Date", "Date (auto)", "Set by A-RH-04 when Stage advances to Work In Progress."],
        ["Walkthrough Scheduled Date", "Date", "<strong>Gate field</strong> — must be populated before Stage 5 → 6 transition."],
        ["Walkthrough Completed Date", "Date (auto)", "Set by A-RH-06 on FastField webhook receipt."],
        ["Approved Date", "Date (auto)", "Set by A-RH-07 when Walkthrough Status = Approved as Ready to Market."],
        ["Closed Date", "Date (auto)", "Set by A-RH-10 on Stage 9 transition."],
        ["Days In Rehab", "Formula (Duration)", "Rehab Identified Date → Approved Date. Drives SLA alerts: 7+ days past SLA → Ops Director alert (A-RH-12); 30+ calendar days without Completion → Austin escalation."],
    ]
) + """
""" + step("5","Add scope, assignment & financial fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Scope Notes", "Text (multi-line)", "Yes", "<strong>Gate field</strong> — must not be blank before Stage 1 → Stage 2 transition."],
        ["Primary Assigned To", "Text", "No", "Lead vendor or staff name. Receives notification from A-RH-03."],
        ["Assignment Type", "Dropdown", "No", "Values: In-House | External Vendor | Mixed"],
        ["Estimated Total Cost", "Currency", "Yes*", "<strong>Gate field</strong> — must be > $0.00 before Stage 2 → Stage 3 transition (G-RH-02). Entered during scope assessment."],
        ["Budget — Interior", "Currency", "No", "Optional category-level budget allocation."],
        ["Budget — Doors & Hardware", "Currency", "No", ""],
        ["Budget — Kitchen", "Currency", "No", ""],
        ["Budget — Bathrooms", "Currency", "No", ""],
        ["Budget — Utilities", "Currency", "No", ""],
        ["Budget — Exterior & Landscaping", "Currency", "No", ""],
        ["Budget — Other", "Currency", "No", ""],
        ["Actual Cost", "Currency (formula)", "Auto", "Sum of Actual Cost across all linked Rehab Tasks. Auto-updates as tasks are completed."],
        ["Budget Variance", "Currency (formula)", "Auto", "= Estimated Total Cost − Actual Cost. Positive = under budget; Negative = over budget."],
        ["Over Budget", "Formula (Checkbox)", "Auto", "True if Actual Cost > Estimated Total Cost."],
    ]
) + """
""" + step("6","Add walkthrough & metadata fields","") + """
""" + field_table(
    ["Field Name", "Type", "Notes"],
    [
        ["Walkthrough Status", "Dropdown", "Values: Approved as Ready to Market | Needs Additional Items | Not Ready | Vendor Needs to Finish. Set automatically by A-RH-06 on webhook receipt."],
        ["FastField Launch Link", "URL (formula)", "Pre-populated link to Rehab Walkthrough Punchlist form. Auto-generated by A-RH-05 with Community, Lot, and Rehab Record ID as URL parameters."],
        ["Record Created By", "Text (auto)", "QB user who created the record."],
        ["Last Updated", "Date/Time (auto)", "QB auto-stamp."],
    ]
) + """

""" + section("P3-S2 · Rehab Tasks Table (TK-RH)") + """
<div class="spec-ref">Source: <span>WF002 Spec §4D — Child of Rehab Records. One record per work item.</span></div>
""" + step("1","Create the Rehab Tasks table","<p>In QB → Tables → + New Table. Name: <code>Rehab Tasks</code>. Child of Rehab Records — multiple tasks per rehab project.</p>") + """
""" + step("2","Add all fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Task ID", "Formula (Text)", "Auto", "Format: TK-RH-YYYY-#####. Auto on record creation."],
        ["Parent Rehab Record", "Relationship → Rehab Records", "Yes", "Links task to parent rehab project."],
        ["Task Name", "Text", "Yes", "Free-text description of the specific work item."],
        ["Category", "Dropdown", "Yes", "Values: Interior | Doors & Hardware | Kitchen | Bathrooms | Utilities | Exterior | Other. Used for budget-vs-actual reporting."],
        ["Assignment Type", "Dropdown", "Yes", "Values: In-House | External Vendor. Drives which assignment field is shown/required."],
        ["Assigned To (In-House)", "Text", "Conditional", "Staff name. Shown/required when Assignment Type = In-House."],
        ["Assigned Vendor", "Relationship → Vendors", "Conditional", "Shown/required when Assignment Type = External Vendor. Drawn from Vendors reference table. Filtered to Active vendors."],
        ["Vendor Contact", "Text (lookup)", "Auto", "Auto-populated from linked Vendor record (Primary Contact field). Read-only on task record."],
        ["Assigned Date", "Date", "No", "Date this task was assigned."],
        ["Due Date", "Date", "No", "Expected completion. Used in overdue reporting and A-RH-12 SLA checks."],
        ["Status", "Dropdown", "Yes", "<strong>Gate field</strong> — all tasks must be Complete before re-walkthrough scheduling (G-RH-05). Values: Not Started | In Progress | Complete | Blocked"],
        ["Completion Date", "Date", "No", "Set when Status changes to Complete."],
        ["Notes", "Text (multi-line)", "No", "Context, blockers, or completion notes."],
        ["Estimated Cost", "Currency", "No", "Per-task estimate at assignment. $1,234.56 format."],
        ["Actual Cost", "Currency", "No", "Actual spend on completion. Rolled up to parent Rehab Record Actual Cost."],
        ["Cost Variance", "Currency (formula)", "Auto", "= Estimated Cost − Actual Cost. Positive = under budget; Negative = over budget."],
    ]
) + """

""" + section("P3-S3 · Rehab Walkthrough Records Table (RW)") + """
<div class="spec-ref">Source: <span>WF002 Spec §4E — Child of Rehab Records. One record per FastField submission.</span></div>
""" + step("1","Create the Rehab Walkthrough Records table","<p>In QB → Tables → + New Table. Name: <code>Rehab Walkthrough Records</code>. Child of Rehab Records. One record created per FastField Rehab Walkthrough Punchlist submission (via webhook).</p>") + """
""" + step("2","Add header fields","") + """
""" + field_table(
    ["Field Name", "Type", "Notes"],
    [
        ["Walkthrough Record ID", "Formula (Text)", "RW-YYYY-###. Auto on webhook receipt."],
        ["Parent Rehab Record", "Relationship → Rehab Records", "Required. Matched by Rehab ID from FastField payload."],
        ["FastField Submission ID", "Text", "UUID from FastField webhook. Stored for audit traceability."],
        ["Community", "Relationship → Communities", "Pre-populated from form header. Cross-checks parent record."],
        ["Lot", "Relationship → Lots", "Pre-populated from form header."],
        ["Submitted By", "Text", "Manager name as entered on FastField form."],
        ["Manager Email", "Email", "From FastField form field."],
        ["Walkthrough Date", "Date", "Date entered on form."],
    ]
) + """
""" + step("3","Add the 6 checklist sections (37 items × 2 fields each = 74 fields)","<p>For each of the 37 checklist items, create TWO fields: <strong>(1)</strong> a Yes/No Checkbox field named <code>[Item Name]</code>, and <strong>(2)</strong> a File Attachment field named <code>[Item Name] — Photo</code> (optional). The exception: <em>Landscaping Owner</em> (Section F, item 5) has a Dropdown field instead of a Photo field.</p>") + """
""" + field_table(
    ["Section", "Items", "Fields Per Item"],
    [
        ["A — Interior", "Home Smells Clean; No Trash/Debris; Floors Swept/Mopped/Vacuumed; Cabinets/Counters/Appliances Cleaned; Blinds Installed/Clean/Working; Outlet/Switch Covers Installed; Interior Bulbs Working; Smoke Detectors Working; Bath/Toilets/Sinks Cleaned; Windows Cleaned", "10 Checkboxes + 10 Photo fields = 20 fields"],
        ["B — Doors, Hardware & Safety", "Front Door Handle/Lock Good or Replaced; Deadbolt Works/Keys Labeled; Interior/Closet Doors Work; Windows Open/Close/Lock; Steps/Porch/Handrails Safe", "5 Checkboxes + 5 Photo fields = 10 fields"],
        ["C — Kitchen & Appliances", "Refrigerator Clean/Working; Stove/Oven Clean/Working; Dishwasher/Range Hood Works; Sink/Faucet Works; No Leaks Under Sink; Cabinets/Drawers Work", "6 Checkboxes + 6 Photo fields = 12 fields"],
        ["D — Bathrooms & Plumbing", "New Toilet Seat Installed; Toilet Flushes; Sink/Shower/Tub Work; No Leaks; Mirror/Vanity/Towel Bar Secure; Caulking Clean/Complete", "6 Checkboxes + 6 Photo fields = 12 fields"],
        ["E — Utilities & Vacant Home Check", "Electric On/Staying On; Water On/Staying On; Heat/A/C Works; Toilets Flushed/Water Run in Sinks; Checked for Leaks/Odors/Pests/Vandalism", "5 Checkboxes + 5 Photo fields = 10 fields"],
        ["F — Exterior & Landscaping", "Exterior Clean/Power Washed; Skirting Secure/Presentable; Yard Cleaned/Grass Cut/Weeds Handled; Landscaping Complete or Assigned (4 items with photos); Landscaping Owner (Dropdown: Maintenance/Manager/Vendor — no photo)", "4 Checkboxes + 4 Photos + 1 Dropdown = 9 fields"],
    ]
) + """
""" + step("4","Add calculated summary fields","") + """
""" + field_table(
    ["Field Name", "Formula", "Display"],
    [
        ["Items Passed", "Count of Yes responses across all 37 items", "Numeric"],
        ["Items Failed", "Count of No responses across all 37 items", "Numeric"],
        ["Pass Rate", "= Items Passed ÷ 37 × 100", "Percentage — format: xx.x%"],
        ["Photos Submitted", "Count of photo attachment fields that are not null", "Numeric"],
    ]
) + """
""" + step("5","Add status & signature fields","") + """
""" + field_table(
    ["Field Name", "Type", "Notes"],
    [
        ["Walkthrough Status", "Dropdown (Required)", "Values: Approved as Ready to Market | Needs Additional Items | Not Ready | Vendor Needs to Finish. Copied to parent Rehab Record by A-RH-06."],
        ["Inspector Signature", "File Attachment (Signature)", "Captured in FastField. Stored as image in QB record."],
    ]
) + """

""" + section("P3-S4 · Vendors QB Reference Table & Power Automate Integration") + """
<div class="spec-ref">Source: <span>WF002 Spec §6 — SharePoint is the vendor master. QB consumes via Power Automate.</span></div>
""" + step("1","Create the Vendors QB reference table","<p>In QB → Tables → + New Table. Name: <code>Vendors</code>. This table is the QB-side of the SharePoint → QB sync. It is populated and kept current by Power Automate (not manual QB entry).</p>") + """
""" + step("2","Add all fields","") + """
""" + field_table(
    ["Field Name", "Type", "Notes"],
    [
        ["Vendor ID", "Text", "Primary key. Unique short code from SharePoint Vendor Master. Referenced in Rehab Tasks."],
        ["Vendor Name", "Text", "Legal or DBA name."],
        ["Trade Category", "Dropdown", "Values: Plumbing | Electrical | HVAC | Roofing | Flooring | Painting | General Contractor | Cleanup | Other. Drives vendor cascade filter on Rehab Tasks."],
        ["Primary Contact", "Text", "Contact name. Auto-populated via Power Automate from SharePoint."],
        ["Phone", "Phone", "Direct contact number."],
        ["Email", "Email", "Business email."],
        ["States Served", "Multi-select", "State codes (FL, GA, SC, NC, MA, WV, MI, AL). Used to filter vendor dropdown by community state."],
        ["Preferred Vendor", "Checkbox (Yes/No)", "Flags top-tier, pre-vetted vendors. Surfaced first in QB dropdown."],
        ["Active", "Checkbox (Yes/No)", "Inactive vendors hidden from QB dropdown cascades. Updated by Power Automate when SharePoint record is deactivated."],
        ["Insurance Expiry", "Date", "GL insurance expiration from SharePoint. Flagged when within 30 days."],
    ]
) + """
""" + step("3","Configure Power Automate flow (IT / QB Admin deliverable)","<p>Create a Power Automate flow in the Parakeet 365 tenant:</p><ul><li><strong>Trigger:</strong> SharePoint list item created or modified in: <code>Parakeet Communities → Operations → Vendor Master</code></li><li><strong>Action:</strong> Upsert the corresponding QB Vendors record (match on Vendor ID). If record exists → update all fields. If not exists → create new record.</li><li><strong>Deactivation:</strong> When SharePoint Active = No → set QB Vendors Active = No.</li><li><strong>Schedule:</strong> Also configure a daily full-sync run at 5:00 AM ET as a safety net.</li></ul>") + """
""" + note("SharePoint remains the source of truth. Never edit Vendor records directly in QB. All vendor master changes go through SharePoint and Power Automate syncs them to QB.") + """

""" + section("P3-S5 · FastField Form — Rehab Walkthrough Punchlist (37 Items)") + """
<div class="spec-ref">Source: <span>WF002 Spec §5 — QB target: Rehab Walkthrough Records. Completed by: Community Manager / Inspector in field.</span></div>
""" + step("1","Create the Rehab Walkthrough form in FastField","<p>Name: <code>WF002 — Rehab Walkthrough Punchlist</code>. QB target: <code>Rehab Walkthrough Records</code>. Matching key: <code>Rehab ID</code> (RH-YYYY-###). Pre-populated from QB launch link: Community, Lot Number, Rehab Record ID.</p>") + """
""" + step("2","Add header (metadata) section","") + """
""" + field_table(
    ["Field", "Type", "Notes"],
    [
        ["WF002 Form ID (Rehab ID)", "Text (auto)", "Auto-populated from QB; links submission back to QB record."],
        ["Community", "Text (auto)", "Pulled from QB; read-only in field."],
        ["Lot Number", "Text (auto)", "Pulled from QB; read-only in field."],
        ["Inspector Name", "Text (auto)", "FastField user display name; auto-populated from login."],
        ["Inspection Date", "Date", "Defaults to device date; editable by inspector."],
        ["Unit Make / Model / Year", "Text", "Free entry to confirm the correct unit."],
    ]
) + """
""" + step("3","Build the 37-item checklist (6 sections)","<p>Each item: Pass / Fail / N/A dropdown + optional Photo capture field + free-text Notes field. Items marked Fail automatically create Rehab Tasks in QB (via A-RH-05).</p>") + """
""" + field_table(
    ["Section", "Item Count", "Key Scope Hints"],
    [
        ["Exterior (Items 1–8)", "8", "Roof condition; skirting & foundation; steps/landing; exterior walls; windows (exterior); doors (exterior); tie-downs/anchors; utility connections (exterior)"],
        ["Interior — General (Items 9–18)", "10", "Floors living areas; walls & ceilings; windows (interior); doors (interior); light fixtures & switches; smoke/CO detectors; electrical panel; HVAC heating; HVAC cooling; water heater"],
        ["Kitchen (Items 19–23)", "5", "Cabinets & countertops; sink & faucet; appliances; range hood/ventilation; GFI outlets — kitchen"],
        ["Bathrooms (Items 24–28)", "5", "Tub/shower; toilet; vanity & sink; ventilation; flooring"],
        ["Plumbing & Mechanical (Items 29–32)", "4", "Under-floor plumbing; main water line/shut-off; drainage/sewer connection; gas system"],
        ["Safety & Cleanup (Items 33–37)", "5", "Hazardous materials observation; pest/rodent evidence; personal property/debris; lot cleanup required; overall cleanliness (1–5 estimate)"],
    ]
) + """
""" + step("4","Add calculated summary and submission fields","") + """
""" + field_table(
    ["Field", "Type", "Logic"],
    [
        ["Total Items Inspected", "Calculated", "COUNT of items where result ≠ N/A"],
        ["Total Fails", "Calculated", "COUNT of items where result = Fail"],
        ["Fail Rate %", "Calculated", "Total Fails ÷ Total Items Inspected × 100; display to one decimal"],
        ["Recommended Disposition", "Calculated", "If Fail Rate > 60% → 'Full Rehab Required'; 30–60% → 'Partial Rehab'; <30% → 'Minor Work Only'"],
        ["Photo Count", "Calculated", "COUNT of photo fields with an attachment"],
        ["Overall Walkthrough Status", "Dropdown (Required)", "Values: Approved as Ready to Market | Needs Additional Items | Not Ready | Vendor Needs to Finish. Inspector selects. Drives QB Walkthrough Status field."],
        ["Inspector Notes (General)", "Long Text", "Free-form summary; mapped to QB Walkthrough Notes."],
        ["Inspector Signature", "Signature", "Captured on-device; stored as image in FastField; URL pushed to QB."],
        ["Submission Timestamp", "DateTime (auto)", "Set by FastField on submit; mapped to QB Walkthrough Date."],
    ]
) + """
""" + step("5","Configure webhook to Rehab Walkthrough Records","<p>Map all 37 checklist result fields, 37 photo fields, Walkthrough Status, Inspector Signature URL, and all header fields to corresponding QB fields. Confirm Walkthrough Status is copied to parent Rehab Record by A-RH-06.</p>") + """

""" + section("P3-S6 · Cascading Dropdowns — WF002") + """
<div class="spec-ref">Source: <span>WF002 Spec §8</span></div>
""" + step("1","Primary cascade — Community → Lot (Rehab context)","<p>On the Rehab Record form, Lot dropdown filters to: <code>Community = [selected Community]</code> AND <code>Lot Status Allows Rehab = Yes</code> (i.e., Lot-In Rehab or Lot status with Allows Rehab = Yes). This prevents creating Rehab Records for occupied lots.</p>") + """
""" + step("2","Secondary cascade — Task Trade Category → Vendor","<p>On the Rehab Tasks form: (1) User selects Trade Category. (2) Vendor ID dropdown filters to vendors where: <code>Trade Category = [selected Trade]</code> AND <code>States Served includes [Community State]</code> AND <code>Active = Yes</code>. Preferred Vendors appear first. Vendor Name auto-populates from lookup after Vendor ID is set.</p>") + """
""" + step("3","Rehab Stage → Allowed Status cascade","<p>Configure form validation: available Rehab Stage values are constrained to forward movement only (Gate G-RH-01 blocks backward movement). Task completion is blocked if Rehab Status = Rehab Identified or Walkthrough Scheduled.</p>") + """

""" + section("P3-S7 · Automations A-RH-01 – A-RH-12") + """
<div class="spec-ref">Source: <span>WF002 Spec §9 — 12 QB Pipelines automations. Build in order.</span></div>
""" + auto_table([
    ["A-RH-01", "Manual (PM/CM creates record), TBD Report, or Move-Out event", "Immediate", "Creates new Rehab Record with Rehab Stage = Rehab Identified. Sets Rehab Identified Date = today. Validates Community and Lot are provided. Sets Lot Status → Lot-In Rehab on linked Lot record. Sets Asset Status → Rehab in Process on linked Asset record."],
    ["A-RH-02", "Rehab Stage changes to Scope Assessed", "Immediate", "Sets Scope Assessed Date = today. Sends notification to PM and Community Manager to complete scope assessment."],
    ["A-RH-03", "Rehab Stage changes to Work Assigned", "Immediate", "Sets Work Assigned Date = today. Sends notification to Primary Assigned To (vendor or staff) with work order details and QB Rehab Record link."],
    ["A-RH-04", "Rehab Stage changes to Work In Progress", "Immediate", "Sets Work Started Date = today. Notifies Ops team that active rehab has begun."],
    ["A-RH-05", "Rehab Stage changes to Walkthrough Scheduled", "Immediate", "Generates pre-populated FastField Rehab Walkthrough launch URL with Community, Lot, and Rehab Record ID as parameters. Writes URL to FastField Launch Link field on Rehab Record. Sets Walkthrough Scheduled Date = today (or date manually set). Sends launch link to assigned inspector."],
    ["A-RH-06", "FastField Rehab Walkthrough form submitted (webhook received)", "On webhook receipt", "Receives FastField webhook payload. Creates child Walkthrough Record in QB (Rehab Walkthrough Records table). Matches by Rehab ID. Sets Walkthrough Completed Date = today. Copies Walkthrough Status from form to Rehab Record. Routes: if Walkthrough Status = Approved as Ready to Market → triggers A-RH-07; otherwise → triggers A-RH-08."],
    ["A-RH-07", "Walkthrough Status = Approved as Ready to Market (set by A-RH-06)", "Immediate", "Sets Rehab Stage → Approved — Ready to Market. Sets Approved Date = today. Sets Asset Status → For Sale on linked Asset record. Sets Lot Status → Lot-Avail(POH) on linked Lot record (confirm exact value per asset type at build). Sends listing handoff notification to Leslie and Tanya: 'Home at [Community] Lot [Lot] has been approved. Please complete a Listing Request Form.' Notification includes link to Listing Request form."],
    ["A-RH-08", "Walkthrough Status ≠ Approved as Ready to Market (set by A-RH-06)", "Immediate", "Sets Rehab Stage → Items To Resolve. Creates follow-up Rehab Task records for each failed walkthrough item (one task per failed item). Assigns to Primary Assigned To. Notifies PM: 'Walkthrough for [Rehab ID] was not approved. [N] items require resolution.'"],
    ["A-RH-09", "All Rehab Tasks for a Rehab Record = Complete (checked by A-RH-08 monitor)", "Immediate", "When all tasks linked to the parent Rehab Record = Complete → notifies PM to re-schedule walkthrough. Sets Rehab Stage → Walkthrough Scheduled (triggers A-RH-05 to re-dispatch FastField form for re-inspection)."],
    ["A-RH-10", "Rehab Stage changes to Closed (Stage 9)", "Immediate", "Sets Closed Date = today. Confirms Final Actual Cost = sum of all linked Rehab Task Actual Cost fields. Record becomes read-only (lock all editable fields except admin override)."],
    ["A-RH-11", "Rehab Stage changes to Approved — Ready to Market", "Immediate", "Sends listing handoff notification email to Leslie and Tanya with unit details, rehab summary, and total actual cost. <strong>Does not auto-create a listing record</strong> — notification only. Listing team initiates listing manually."],
    ["A-RH-12", "Scheduled daily at 6:00 AM ET", "Scheduled", "<strong>SLA / Age Alert — 3 thresholds:</strong><br>(1) Walkthrough Scheduling SLA: if more than 3 business days have elapsed since Rehab Identified without Walkthrough Scheduled Date → alert Ops Director.<br>(2) Task Completion SLA: any Rehab Task with Due Date > 5 business days ago and Status ≠ Complete → alert assigned party and Ops Director.<br>(3) Full Project SLA: any Rehab Record open 30+ calendar days without Closed Date → escalate to Austin. Any SLA overdue by 7+ days → alert Ops Director. 30+ calendar days without Completion → escalate to Austin."],
]) + """

""" + section("P3-S8 · Gate Rules — WF002") + """
<div class="spec-ref">Source: <span>WF002 Spec §10 — 8 gate rules. All are hard stops.</span></div>
""" + gate_table([
    ["G-RH-01", "No Backward Status", "Any → earlier Stage", "Condition: New Rehab Stage has a lower stage sequence number than the current stage.<br>Error: <em>'Status cannot move backward. Contact your administrator to revert if needed.'</em>"],
    ["G-RH-02", "Scope Notes Required", "Rehab Identified → Scope Assessed", "Condition: Scope Notes field is blank.<br>Error: <em>'Scope Notes must be completed before advancing to Scope Assessed.'</em>"],
    ["G-RH-03", "Estimated Cost Required", "Scope Assessed → Work Assigned", "Condition: Estimated Total Cost is blank or $0.<br>Error: <em>'Estimated Total Cost must be greater than $0 before work can be assigned.'</em>"],
    ["G-RH-04", "At Least One Task Required", "Scope Assessed → Work Assigned", "Condition: COUNT of Rehab Tasks linked to this Rehab Record = 0.<br>Error: <em>'At least one Rehab Task must be created before advancing to Work Assigned.'</em>"],
    ["G-RH-05", "All Tasks Must Close", "Work In Progress → Walkthrough Scheduled", "Condition: COUNT of Rehab Tasks where Task Status ≠ Complete or Cancelled > 0.<br>Error: <em>'[N] task(s) are still open. All tasks must be closed before scheduling the walkthrough.'</em>"],
    ["G-RH-06", "Walkthrough Date Required", "Work In Progress → Walkthrough Scheduled", "Condition: Walkthrough Scheduled Date is blank.<br>Error: <em>'Walkthrough Scheduled Date must be populated before advancing to Walkthrough Scheduled.'</em>"],
    ["G-RH-07", "Walkthrough Required", "Walkthrough Scheduled → Approved — Ready to Market", "Condition: COUNT of Walkthrough Records linked to this Rehab Record = 0.<br>Error: <em>'A completed walkthrough is required before the rehab can be approved.'</em>"],
    ["G-RH-08", "Occupied Lot Block", "Record Creation", "Condition: Selected Lot's current Lot Status category = Occupied (Lot Status Allows Rehab = No) at time of Rehab Record creation.<br>Error: <em>'This lot is currently occupied. A rehab record cannot be created for an occupied lot.'</em>"],
]) + """
</div>

<!-- ========================= PHASE 4 ========================= -->
<div class="page-break"></div>
""" + phase_header("4","WF003 — Asset Disposition Review","red","Spec v1.1 · Draft for Review","6 stages · 2 QB tables · No FastField forms · 5 automations · 3 gate rules · 5 standard reports") + """
<div class="content">
<div class="summary-bar">
  <div class="summary-chip"><strong>2</strong> QB Tables</div>
  <div class="summary-chip"><strong>0</strong> FastField Forms</div>
  <div class="summary-chip"><strong>5</strong> Automations</div>
  <div class="summary-chip"><strong>3</strong> Gate Rules</div>
  <div class="summary-chip"><strong>5</strong> Standard Reports</div>
  <div class="summary-chip"><strong>5</strong> Disposition Values</div>
</div>
""" + note("WF003 is a QB-only workflow — no FastField forms. All data entry is in the QB web interface during or after the Monday meeting. The meeting recorder creates records in QB; automations fire immediately on save.") + """

""" + section("P4-S1 · Disposition Meetings Table (DM)") + """
<div class="spec-ref">Source: <span>WF003 Spec §5A — Parent table. One record per Monday meeting.</span></div>
""" + step("1","Create the Disposition Meetings table","<p>In QB → Tables → + New Table. Name: <code>Disposition Meetings</code>. One record = one weekly Monday meeting.</p>") + """
""" + step("2","Add all fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Meeting ID", "Formula (Text)", "Auto", "Format: DM-YYYY-###. Auto-generated: 'DM-' & Text(Year([Date Created])) & '-' & Right('000' & [Record ID#], 3)"],
        ["Meeting Date", "Date", "Yes", "Date of the Monday meeting. Format: mm/dd/yy. Soft warning (not hard block) fires if date selected is not a Monday: 'This date is not a Monday. Asset Disposition meetings are typically held on Mondays. Confirm to proceed.'"],
        ["Meeting Status", "Dropdown", "Auto/Yes", "Values: Open | Closed. Defaults to Open on creation. Auto-set to Closed by A-DR-04 when all linked Disposition Items = Actioned or Closed."],
        ["Facilitator", "User", "Yes", "QB user running the meeting — typically Asset Management lead."],
        ["Participants", "Text (multi-line)", "No", "Names or roles of attendees beyond the facilitator."],
        ["Meeting Notes", "Text (multi-line)", "No", "General meeting notes. Unit-specific notes go on individual Disposition Items."],
        ["Total Units Reviewed", "Count (rollup)", "Auto", "Count of all linked Disposition Items. Auto-calculated."],
        ["Rehab Count", "Count (rollup)", "Auto", "Count of linked Disposition Items where Disposition = Rehab."],
        ["Demo Count", "Count (rollup)", "Auto", "Count where Disposition = Demo."],
        ["Turn for Sale Count", "Count (rollup)", "Auto", "Count where Disposition = Turn for Sale."],
        ["Hold Count", "Count (rollup)", "Auto", "Count where Disposition = Hold."],
        ["Created By", "User (auto)", "Auto", "QB user who created the meeting record."],
        ["Created Date", "Date/Time (auto)", "Auto", "Auto-stamped on record creation."],
    ]
) + """
""" + step("3","Configure soft warning for non-Monday dates","<p>In QB → Disposition Meetings table → Forms → Meeting Date field settings: add a conditional warning rule: <code>IF DayOfWeek([Meeting Date]) ≠ 2 (Monday) THEN show warning: 'This date is not a Monday...'</code>. This is a warning only — allow save to proceed.</p>") + """

""" + section("P4-S2 · Disposition Items Table (DI)") + """
<div class="spec-ref">Source: <span>WF003 Spec §5B — Child of Disposition Meetings. One record per unit reviewed at a meeting.</span></div>
""" + step("1","Create the Disposition Items table","<p>In QB → Tables → + New Table. Name: <code>Disposition Items</code>. Child of Disposition Meetings (many items per meeting). This is where disposition decisions are recorded.</p>") + """
""" + step("2","Add all fields","") + """
""" + field_table(
    ["Field Name", "Type", "Required", "Notes"],
    [
        ["Item ID", "Formula (Text)", "Auto", "Format: DI-YYYY-###. Auto-generated."],
        ["Meeting", "Relationship → Disposition Meetings", "Yes", "Links this item to the parent Monday meeting record (DM-YYYY-###)."],
        ["Community", "Relationship → Communities", "Yes", "Top of cascade. Filtered to active communities."],
        ["Lot", "Relationship → Lots", "Yes", "Filtered dynamically to lots belonging to the selected Community. No status restriction — any recently vacated lot may be under review."],
        ["Asset", "Lookup / Relationship", "Yes", "Filtered dynamically to assets on the selected Lot."],
        ["Lot Status at Review", "Formula (Text)", "Auto", "Snapshot of the Lot's current Lot Status at time of review — pulled from linked Lot record. Read-only. Preserved even if Lot Status changes after the meeting."],
        ["Asset Status at Review", "Formula (Text)", "Auto", "Snapshot of the Asset's current Asset Status at time of review. Read-only."],
        ["Disposition", "Dropdown", "Yes*", "Values: (blank — Pending) | Rehab | Demo | Turn for Sale | Hold | No Action. Defaults to blank. Setting to a non-blank value triggers the appropriate automation. Required before advancing Item Status beyond Pending Review."],
        ["Disposition Notes", "Text (multi-line)", "Conditional", "<strong>REQUIRED when Disposition = Hold</strong> (Gate G-DR-01). Must include reason for hold and expected re-review date. Optional for all other dispositions."],
        ["Assigned To", "User", "No", "QB user responsible for following up (e.g., Ops rep who will initiate WF002)."],
        ["Item Status", "Dropdown (auto)", "Auto", "Values: Pending Review | Reviewed | Actioned | Closed. Defaults to Pending Review on creation. Set by automations — not manually."],
        ["Downstream Record ID", "Text (auto)", "Auto", "Auto-populated by automation with ID of downstream record created — e.g., RH-2026-004 for a Rehab disposition. Empty for Hold and No Action."],
        ["Reviewed Date", "Date (auto)", "Auto", "Auto-stamped when Item Status advances to Reviewed."],
        ["Actioned Date", "Date (auto)", "Auto", "Auto-stamped when Item Status advances to Actioned."],
        ["Created By", "User (auto)", "Auto", "QB user who created this Disposition Item."],
        ["Created Date", "Date/Time (auto)", "Auto", "Auto-stamped on record creation."],
    ]
) + """
""" + step("3","Configure cascade dropdowns (Community → Lot → Asset)","<p>Same cascade architecture as WF001 and WF002 (D-011). Community → Lot: filter to lots in selected Community. No status restriction on Lot or Asset for WF003 — any recently vacated unit may be reviewed. The Lot Status at Review and Asset Status at Review snapshot fields capture the current state automatically on record save.</p>") + """

""" + section("P4-S3 · Automations A-DR-01 – A-DR-05") + """
<div class="spec-ref">Source: <span>WF003 Spec §6 — 5 automations. All trigger immediately on save.</span></div>
""" + auto_table([
    ["A-DR-01", "Disposition Item saved with Disposition = Rehab", "Immediate on save", "<strong>Primary downstream automation — creates WF002 Rehab Record.</strong><br>Actions (in order):<br>1. Create new WF002 Rehab Record — pass Community, Lot, Asset, Meeting Date (from parent DM record), and Disposition Notes to the new Rehab Record. Triggered By = TBD Report (or set based on context). New Rehab Record ID auto-generated (RH-YYYY-###).<br>2. Update linked Lot record: Lot Status → Lot-In Rehab.<br>3. Update linked Asset record: Asset Status → Rehab in Process.<br>4. Update Disposition Item: Downstream Record ID = new RH-#### ; Item Status → Actioned; Actioned Date → today.<br><br>Note: WF002 automation A-RH-02 then fires automatically on the new Rehab Record — it dispatches the FastField form link to the assigned inspector. WF003 recorder does not need to open WF002 separately."],
    ["A-DR-02", "Disposition Item saved with Disposition = Demo", "Immediate on save", "Actions:<br>1. Update linked Lot record: Lot Status → Lot-Demo.<br>2. Update linked Asset record: Asset Status → To Be Demoed.<br>3. Update Disposition Item: Item Status → Actioned; Actioned Date → today.<br><br>Note: No individual notification on Demo. All disposition outcomes communicated via meeting recap email (A-DR-04) when full meeting closes."],
    ["A-DR-03", "Disposition Item saved with Disposition = Turn for Sale", "Immediate on save", "Actions:<br>1. Update linked Asset record: Asset Status → For Sale.<br>2. Update Disposition Item: Item Status → Actioned; Actioned Date → today.<br><br>Note: No individual notification on Turn for Sale. All outcomes communicated via meeting recap email (A-DR-04)."],
    ["A-DR-04", "All Disposition Items for a Disposition Meeting = Actioned or Closed", "Immediate (checked on each Item save)", "Actions:<br>1. Update Disposition Meeting record: Meeting Status → Closed.<br>2. Send meeting recap email to full leadership group: Austin, Jon, John, Zach, Natalie, Leslie, Justin.<br>Email subject: 'Asset Disposition Review — Meeting Recap — [Meeting Date]'<br>Email body includes: total units reviewed; itemized list of all Disposition Items with Community / Lot / Asset / Disposition / Disposition Notes / Downstream Record ID (where applicable); meeting facilitator name.<br><br><strong>Build phase action required:</strong> Collect full email addresses for all 7 recipients before configuring this automation (O-WF003-004)."],
    ["A-DR-05", "Disposition Item saved with Disposition = Hold or No Action", "Immediate on save", "Actions:<br>1. Update Disposition Item: Item Status → Closed.<br>2. No status changes to Lot or Asset record.<br>3. Record preserved for audit trail. Unit should be re-added to the next meeting agenda manually by the recorder."],
]) + """

""" + section("P4-S4 · Gate Rules — WF003") + """
<div class="spec-ref">Source: <span>WF003 Spec §7 — 3 hard stops. No exceptions.</span></div>
""" + gate_table([
    ["G-DR-01", "Disposition Required Before Reviewed Status", "Pending Review → Reviewed (or beyond)", "Condition 1: Item Status cannot be set to Reviewed or beyond unless Disposition is set to a non-blank value.<br>Error: <em>'A disposition decision must be recorded before marking this item as Reviewed.'</em><br><br>Condition 2 (additional rule): When Disposition = Hold, the Disposition Notes field is required.<br>Error: <em>'Disposition Notes are required when Disposition = Hold. Please enter the reason for the hold and the expected re-review date.'</em>"],
    ["G-DR-02", "All Items Must Be Actioned or Closed Before Meeting Can Close", "Open → Closed (on Meeting record)", "Condition: Disposition Meeting Status cannot be manually set to Closed if any linked Disposition Item = Pending Review or Reviewed. Meeting closure is auto-handled by A-DR-04 only.<br>Error: <em>'Meeting cannot be closed while [N] item(s) remain unactioned. All items must reach Actioned or Closed status first.'</em><br><br>Note: Disable the manual Meeting Status field edit for all roles except Sys Admin. Closure is automation-only."],
    ["G-DR-03", "Block Duplicate WF002 Rehab Record", "Record Creation (Disposition Item)", "Condition: If a recorder attempts to create a Disposition Item for a Lot/Asset that already has an active (non-Closed) WF002 Rehab Record, QB blocks the save.<br>Error: <em>'This unit already has an active Rehab record in progress ([RH-ID]). A new Disposition Item cannot be created until the existing Rehab record is closed. Contact Ops if an exception is required.'</em><br><br>Secondary rule: No duplicate non-Closed Disposition Items for the same Lot within the same meeting. Recorder must close or remove the existing item first.<br><br>Future build: Replace hard block with exception approval workflow (recorder requests override → Ops Director approves)."],
]) + """

""" + section("P4-S5 · Standard Reports (5 reports)") + """
<div class="spec-ref">Source: <span>WF003 Spec §9 — All QB-native reports.</span></div>
""" + step("1","Create all 5 standard reports in QB","") + """
""" + field_table(
    ["Report Name", "Filter / Scope", "Columns to Display", "Primary User"],
    [
        ["This Week's Meeting", "Disposition Meeting where Meeting Date = current week. Shows linked Disposition Items.", "Item ID, Community, Lot, Asset, Lot Status at Review, Asset Status at Review, Disposition, Disposition Notes, Item Status, Downstream Record ID", "Meeting Recorder — default view for Monday meeting"],
        ["All Open Meetings", "Disposition Meetings where Meeting Status = Open", "Meeting ID, Meeting Date, Facilitator, Total Units Reviewed, Rehab Count, Demo Count, Turn for Sale Count, Hold Count", "Ops — confirm no meeting has outstanding unactioned items"],
        ["Disposition History by Community", "All Disposition Items. Group by Community. Filter by date range and disposition type (user-selectable).", "Item ID, Meeting Date, Community, Lot, Asset, Disposition, Disposition Notes, Item Status, Downstream Record ID", "Asset Management — portfolio-level reporting"],
        ["Rehab Pipeline Source", "All Disposition Items where Disposition = Rehab. Links through to associated WF002 Rehab Records.", "Disposition Date, Community, Lot, Asset, Downstream Record ID (links to RH record), Current WF002 Stage", "Ops / Asset Management — track all rehab-originated items"],
        ["Pending Items (Unactioned)", "All Disposition Items where Item Status = Pending Review or Reviewed", "Item ID, Meeting Date, Community, Lot, Asset, Disposition, Item Status", "Ops — identify stalled items. Expected to be empty at end of each meeting week."],
    ]
) + """
</div>

<!-- ========================= PHASE 5 ========================= -->
<div class="page-break"></div>
""" + phase_header("5","Cross-Workflow Connections & Testing","purple","Build last — requires all three workflows to be complete","WF003 → WF002 wire-up · Shared reference dependencies · End-to-end testing checklists") + """
<div class="content">

""" + section("P5-S1 · WF003 → WF002 Integration Wire-Up") + """
<div class="spec-ref">Source: <span>WF003 Spec §6 A-DR-01 · WF002 Spec §2 Trigger Logic</span></div>
<p>The WF003 → WF002 integration is the critical cross-workflow connection. When a Disposition Item is saved with Disposition = Rehab, Automation A-DR-01 must create a fully formed WF002 Rehab Record at Stage 1 and trigger WF002's own notification chain (A-RH-02). The WF003 recorder never touches WF002 manually.</p>
""" + step("1","Verify A-DR-01 creates valid WF002 Rehab Records","<p>In QB Pipelines → A-DR-01: confirm the 'Create Record' action in the Rehab Records table. Verify all required fields are passed: Community (from Disposition Item), Lot (from Disposition Item), Asset (from Disposition Item), Rehab Stage = Stage 1 (Rehab Identified), Triggered By = TBD Report (or applicable value), Rehab Identified Date = today, Disposition Notes → Scope Notes (if applicable).</p>") + """
""" + step("2","Verify A-DR-01 triggers WF002's A-RH-01 chain","<p>After A-DR-01 creates the Rehab Record, WF002 automation A-RH-01 should fire automatically (triggered by the new Rehab Record creation event). Confirm: Lot Status updates to Lot-In Rehab; Asset Status updates to Rehab in Process; WF002 notification goes to the assigned inspector.</p>") + """
""" + step("3","Verify Downstream Record ID is populated on the Disposition Item","<p>After A-DR-01 fires, the Disposition Item's Downstream Record ID field should contain the new Rehab Record ID (e.g., RH-2026-004). Verify this is populated correctly. This is the audit link between WF003 and WF002.</p>") + """
""" + step("4","Test the full path: WF003 meeting → WF002 Rehab Record creation","<p>Test scenario: (1) Create a Disposition Meeting (DM-2026-001). (2) Add a Disposition Item for a known vacant lot. (3) Set Disposition = Rehab. (4) Save. Confirm: Disposition Item Item Status = Actioned; Downstream Record ID = RH-2026-XXX; Lot Status on linked Lot = Lot-In Rehab; Asset Status = Rehab in Process; New Rehab Record exists in WF002 at Stage 1; WF002 notification chain triggered.</p>") + """

""" + section("P5-S2 · Move Out Integration Points") + """
<div class="spec-ref">Source: <span>WF002 Spec §2 Trigger Logic · WF003 Spec §8</span></div>
""" + note("The Move Out workflow is not yet built. These are documented integration points for when it is built.") + """
""" + field_table(
    ["Integration Point", "Behavior When Built", "Current Workaround"],
    [
        ["Move Out → WF002 trigger", "A completed Move Out where disposition = Rehab auto-creates a WF002 Rehab Record. Move Out workflow passes Lot ID, Asset ID, and Community to the new Rehab Record.", "Ops team or Community Manager manually creates the Rehab Record in QB (Manual trigger). Set Triggered By = Move Out and enter Source Move Out Record # manually."],
        ["Move Out → WF003 agenda pre-population", "A completed Move Out sets Asset Status to TBD or Needs Rehab. WF003 recorder sees the status change and adds the unit to the next meeting's Disposition Items manually.", "Already the current process — Move Out sets status change; recorder adds to next meeting agenda manually. No automation change needed at this time."],
        ["Move Out → Lot Status", "LS-4 automation: Move Out processed → Lot Status: Occupied → Available ('Lot').", "LS-4 is already built (Phase 2, P2-S14). Confirm it fires correctly when Move Out record is processed in QB."],
    ]
) + """

""" + section("P5-S3 · Shared Reference Table Dependencies Map") + """
<p>This map shows which tables are shared and which automations write to them. Use this to avoid redundant configuration and identify points of potential conflict.</p>
""" + field_table(
    ["Shared Table", "Read By", "Written By (Automations)"],
    [
        ["Communities", "WF001 (cascade), WF002 (cascade), WF003 (cascade)", "None — read-only. Updated manually by Sys Admin when community data changes."],
        ["Lot Status Reference", "WF001 (cascade filters), WF002 (cascade filters)", "None — read-only lookup. Values are fixed (16 records created in Phase 1)."],
        ["Asset Status Reference", "WF002 (cascade filters), WF003 (cascade filters)", "None — read-only lookup. Values are fixed (25 records created in Phase 1)."],
        ["Lots (Lot Status field)", "WF001 cascade, WF002 cascade, WF003 cascade", "WF001: LS-1, LS-2, LS-3, LS-4, LS-5, LS-6; WF002: A-RH-01 (→ Lot-In Rehab), A-RH-07 (→ Lot-Avail(POH)); WF003: A-DR-01 (→ Lot-In Rehab), A-DR-02 (→ Lot-Demo)"],
        ["Asset records (Asset Status field)", "WF002 cascade, WF003 cascade", "WF002: A-RH-01 (→ Rehab in Process), A-RH-07 (→ For Sale); WF003: A-DR-01 (→ Rehab in Process), A-DR-02 (→ To Be Demoed), A-DR-03 (→ For Sale)"],
    ]
) + """
""" + crit("Multiple automations write to Lot Status and Asset Status on the same records. Confirm there are no conflicting pipelines writing to the same record at the same time. QB Pipelines run sequentially per record trigger — verify ordering is correct in the Pipeline configuration.") + """

""" + section("P5-S4 · End-to-End Testing Checklists") + """
<div class="subsection-title">WF001 — Home Ordering End-to-End Test</div>
""" + field_table(
    ["Test #", "Test Scenario", "Expected Result", "Pass / Fail"],
    [
        ["T1-01", "Create new Home Order for an Available lot", "Lot Status → Reserved (LS-1). Stage = Infill Need Identified. Stage 1-2 tasks created (A1).", "☐"],
        ["T1-02", "Advance stage to Home Selected", "Stage 3-4 tasks created (A2). Sales and Accounting notified.", "☐"],
        ["T1-03", "Advance stage to Order Placed", "Stage 5 tasks created (A3). Asset Mgmt and Ops Coord notified.", "☐"],
        ["T1-04", "Change Estimated Delivery Date", "Notification sent to all departments (A4).", "☐"],
        ["T1-05", "Check Storage Required = Yes", "Storage task created (A5). Stage 7 path activated.", "☐"],
        ["T1-06", "Submit FastField Form 1 (Delivery Confirmation)", "Delivery Record created. Stage → Delivered (A7). Post-delivery tasks created.", "☐"],
        ["T1-07", "Set Lot Fit Issue? = Yes", "Immediate alert sent (A9). Stage advancement blocked.", "☐"],
        ["T1-08", "Submit FastField Form 2 (all items pass)", "CI Record created. All Items Pass = True. Stage → Ops & Sales Readiness (A10).", "☐"],
        ["T1-09", "Submit FastField Form 2 (any item fails)", "CI Record created. Total Fail > 0. Remediation task created (A11). Stage blocked.", "☐"],
        ["T1-10", "Submit FastField Form 3 (all items pass, both signatures)", "OR Record created. Home Ready = True. Stage → pre-listing (A12).", "☐"],
        ["T1-11", "Submit FastField Form 4 (all 7 items Yes)", "Listing Record created. All Pre-Listing Complete = True. Stage → Listed — Complete (A14). Team notified.", "☐"],
        ["T1-12", "Attempt to advance without required gate fields", "Hard stop fires. Error message displays. Stage does not advance.", "☐"],
        ["T1-13", "Verify lot cascade filters on New Home Order form", "Only Available lots for selected Community appear in Lot dropdown.", "☐"],
        ["T1-14", "Cancel a Home Order", "Lot Status → Available (LS-2). Lot re-appears in New Home Order form.", "☐"],
        ["T1-15", "Verify Storage Aging alert at day 31", "Scheduled automation A6 sends alert. Storage record flagged in Storage Aging View.", "☐"],
    ]
) + """
<div class="subsection-title">WF002 — Rehab End-to-End Test</div>
""" + field_table(
    ["Test #", "Test Scenario", "Expected Result", "Pass / Fail"],
    [
        ["T2-01", "Create Rehab Record manually for an eligible lot", "Rehab Record created at Stage 1. Lot Status → Lot-In Rehab. Asset Status → Rehab in Process (A-RH-01).", "☐"],
        ["T2-02", "Attempt to create Rehab Record for an occupied lot", "Gate G-RH-08 fires. Hard block. Error message displays.", "☐"],
        ["T2-03", "Advance to Scope Assessed without Scope Notes", "Gate G-RH-02 fires. Stage does not advance.", "☐"],
        ["T2-04", "Advance to Work Assigned with Scope Notes and Estimated Cost", "Stage advances. Work Assigned Date auto-set. Primary Assigned To notified (A-RH-03).", "☐"],
        ["T2-05", "Submit FastField Rehab Walkthrough (Approved as Ready to Market)", "Walkthrough Record created. Walkthrough Status → Approved. A-RH-07 fires: Stage → Approved — Ready to Market. Asset Status → For Sale. Listing handoff notification to Leslie and Tanya.", "☐"],
        ["T2-06", "Submit FastField Rehab Walkthrough (Needs Additional Items)", "Walkthrough Record created. A-RH-08 fires. Stage → Items To Resolve. Follow-up Rehab Tasks created for each failed item.", "☐"],
        ["T2-07", "Resolve all tasks and re-schedule walkthrough", "A-RH-09 fires when all tasks = Complete. Stage → Walkthrough Scheduled. FastField form re-dispatched.", "☐"],
        ["T2-08", "Verify bid approval routing — amount < $2,500", "A-RH-06: no approval required. Work proceeds immediately.", "☐"],
        ["T2-09", "Verify bid approval routing — amount $2,500–$5,000", "A-RH-06: approval task created for Regional Manager.", "☐"],
        ["T2-10", "Verify bid approval routing — amount > $5,000", "A-RH-06: approval task created for Austin.", "☐"],
        ["T2-11", "Verify SLA alert at 7 days past walkthrough SLA", "A-RH-12 daily check: Ops Director receives alert.", "☐"],
        ["T2-12", "Verify SLA escalation at 30 calendar days without Close", "A-RH-12: Austin receives escalation email.", "☐"],
        ["T2-13", "Verify vendor cascade — select Trade, confirm vendor filter by state", "Vendor dropdown shows only vendors matching trade and community state.", "☐"],
        ["T2-14", "Advance Rehab to Stage 9 (Closed)", "Closed Date set. Final Actual Cost calculated. Record becomes read-only (A-RH-10).", "☐"],
    ]
) + """
<div class="subsection-title">WF003 — Asset Disposition Review End-to-End Test</div>
""" + field_table(
    ["Test #", "Test Scenario", "Expected Result", "Pass / Fail"],
    [
        ["T3-01", "Create Disposition Meeting for a Monday date", "DM record created with Meeting Status = Open. No warning fires.", "☐"],
        ["T3-02", "Create Disposition Meeting for a non-Monday date", "Soft warning displays: 'This date is not a Monday...' Recorder can proceed and save.", "☐"],
        ["T3-03", "Add Disposition Item for a lot. Set Disposition = Rehab. Save.", "A-DR-01 fires: new WF002 Rehab Record created. Lot Status → Lot-In Rehab. Asset Status → Rehab in Process. Item Status → Actioned. Downstream Record ID populated.", "☐"],
        ["T3-04", "Add Disposition Item. Set Disposition = Demo. Save.", "A-DR-02 fires: Lot Status → Lot-Demo. Asset Status → To Be Demoed. Item Status → Actioned.", "☐"],
        ["T3-05", "Add Disposition Item. Set Disposition = Turn for Sale. Save.", "A-DR-03 fires: Asset Status → For Sale. Item Status → Actioned.", "☐"],
        ["T3-06", "Add Disposition Item. Set Disposition = Hold. Attempt to save without Disposition Notes.", "Gate G-DR-01 fires. Hard block. Error: 'Disposition Notes are required when Disposition = Hold...'", "☐"],
        ["T3-07", "Add Disposition Item. Set Disposition = Hold WITH Disposition Notes. Save.", "A-DR-05 fires. Item Status → Closed. Lot and Asset unchanged.", "☐"],
        ["T3-08", "Add Disposition Item. Set Disposition = No Action. Save.", "A-DR-05 fires. Item Status → Closed. Lot and Asset unchanged.", "☐"],
        ["T3-09", "All Disposition Items for a meeting reach Actioned or Closed.", "A-DR-04 fires. Meeting Status → Closed. Recap email sent to full leadership group (Austin, Jon, John, Zach, Natalie, Leslie, Justin).", "☐"],
        ["T3-10", "Attempt to manually close a meeting while 1 item is still Pending Review.", "Gate G-DR-02 fires. Hard block. Meeting Status cannot be set to Closed manually.", "☐"],
        ["T3-11", "Attempt to create a Disposition Item for a Lot that already has an active WF002 Rehab Record.", "Gate G-DR-03 fires. Hard block. Error: 'This unit already has an active Rehab record in progress ([RH-ID])...'", "☐"],
        ["T3-12", "Verify Disposition History by Community report covers all 5 disposition types.", "Report shows correct counts per community per disposition type.", "☐"],
    ]
) + """
<div class="subsection-title">Cross-Workflow Integration Tests</div>
""" + field_table(
    ["Test #", "Test Scenario", "Expected Result", "Pass / Fail"],
    [
        ["TX-01", "WF003 Rehab disposition → WF002 record auto-creation chain", "WF003 Disposition Item (Rehab) → A-DR-01 creates WF002 Rehab Record → WF002 A-RH-01 fires → Lot-In Rehab status → Inspector notified. Full chain confirmed end-to-end.", "☐"],
        ["TX-02", "Shared Lot record — verify only one automation writes at a time", "Create WF001 Home Order AND a WF003 Disposition Item for the same Lot in quick succession. Confirm only one Lot Status value results and no race condition.", "☐"],
        ["TX-03", "Verify Communities cascade works identically in WF001, WF002, and WF003 forms", "Select same Community in all three workflow forms. Confirm identical lot list appears in each.", "☐"],
        ["TX-04", "Cancel a WF001 Home Order that has a Lot in Reserved status", "LS-2 fires. Lot Status → Available. Lot re-appears in WF001 New Home Order form AND in WF003 Disposition Item lot selector.", "☐"],
    ]
) + """

</div>

<!-- ========================= FOOTER ======================= -->
<div style="margin-top: 0.5in; padding: 0.2in 0.25in; background: var(--navy); color: rgba(255,255,255,0.7); font-size: 7.5pt; border-radius: 8px;">
  <strong style="color:#fff;">Parakeet Communities · QB + FastField Build Playbook v1.0</strong> &nbsp;·&nbsp; 
  WF001 (Home Ordering v1.2) + WF002 (Rehab v1.3) + WF003 (Asset Disposition Review v1.1) &nbsp;·&nbsp; 
  08/19/26 &nbsp;·&nbsp; Internal Confidential &nbsp;·&nbsp; Approved for Build
</div>

</body>
</html>
"""

with open('/home/ubuntu/parakeet_qb_build_playbook_v1.0.html', 'w', encoding='utf-8') as f:
    f.write(HTML)

print("Playbook HTML written successfully.")
import os
size = os.path.getsize('/home/ubuntu/parakeet_qb_build_playbook_v1.0.html')
print(f"File size: {size:,} bytes")
