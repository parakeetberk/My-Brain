#!/usr/bin/env python3
"""
Build WF006 Listings Spec v1.0
Parakeet Communities — QB + FastField OS
"""

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>WF006 Listings — Build Spec v1.0</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@400;500;600;700;800;900&display=swap');

  :root {
    --green:  #4ABA81;
    --red:    #F16262;
    --yellow: #FFCC3B;
    --navy:   #2F4E65;
    --navy-lt:#3a6280;
    --gray:   #f5f6f8;
    --border: #dce1e7;
    --text:   #1a2530;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: 'Red Hat Display', sans-serif;
    font-size: 13px;
    color: var(--text);
    background: #fff;
    line-height: 1.55;
  }

  /* ── COVER ────────────────────────────────────────────── */
  .cover {
    background: var(--navy);
    color: #fff;
    padding: 64px 56px 52px;
    page-break-after: always;
  }
  .cover .logo-bar {
    display: flex; align-items: center; gap: 14px; margin-bottom: 48px;
  }
  .cover .logo-mark {
    width: 48px; height: 48px;
    background: var(--green);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 22px; font-weight: 900; color: #fff; letter-spacing: -1px;
  }
  .cover .co-name { font-size: 17px; font-weight: 700; letter-spacing: .3px; }
  .cover .wf-badge {
    display: inline-block;
    background: var(--green);
    color: #fff;
    font-size: 11px; font-weight: 700;
    padding: 4px 12px; border-radius: 20px;
    letter-spacing: .5px; margin-bottom: 20px;
  }
  .cover h1 {
    font-size: 44px; font-weight: 900; line-height: 1.1;
    margin-bottom: 10px; letter-spacing: -1px;
  }
  .cover .sub {
    font-size: 19px; font-weight: 500; opacity: .75; margin-bottom: 36px;
  }
  .cover .meta-grid {
    display: grid; grid-template-columns: 1fr 1fr; gap: 10px 40px;
    border-top: 1px solid rgba(255,255,255,.15); padding-top: 28px;
  }
  .cover .meta-item { }
  .cover .meta-label { font-size: 10px; font-weight: 700; opacity: .5; letter-spacing: 1px; text-transform: uppercase; }
  .cover .meta-val   { font-size: 14px; font-weight: 600; margin-top: 2px; }
  .cover .status-badge {
    display: inline-block;
    background: var(--yellow); color: var(--navy);
    font-size: 11px; font-weight: 800; padding: 3px 10px; border-radius: 20px;
    margin-top: 4px;
  }

  /* ── SECTION BLOCKS ───────────────────────────────────── */
  .section-block {
    padding: 36px 48px;
    border-bottom: 1px solid var(--border);
    page-break-inside: avoid;
  }
  .sec-hdr {
    display: flex; align-items: baseline; gap: 14px;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid var(--navy);
  }
  .sec-hdr .num {
    font-size: 10px; font-weight: 800; letter-spacing: 1px;
    text-transform: uppercase; color: var(--green); white-space: nowrap;
  }
  .sec-hdr .ttl {
    font-size: 20px; font-weight: 800; color: var(--navy);
  }

  h3 {
    font-size: 14px; font-weight: 700; color: var(--navy);
    margin: 20px 0 10px;
  }
  h4 {
    font-size: 12px; font-weight: 700; color: #444;
    margin: 14px 0 6px;
  }
  p { margin-bottom: 8px; }

  /* ── TABLES ───────────────────────────────────────────── */
  table {
    width: 100%; border-collapse: collapse;
    margin-bottom: 20px; font-size: 12px;
  }
  th {
    background: var(--navy); color: #fff;
    font-size: 10px; font-weight: 700; letter-spacing: .5px;
    text-transform: uppercase; padding: 7px 10px; text-align: left;
  }
  td { padding: 7px 10px; border-bottom: 1px solid var(--border); vertical-align: top; }
  tr:nth-child(even) td { background: var(--gray); }
  tr:last-child td { border-bottom: none; }

  /* ── BADGES ───────────────────────────────────────────── */
  .b {
    display: inline-block;
    font-size: 10px; font-weight: 700; letter-spacing: .4px;
    padding: 2px 8px; border-radius: 20px;
  }
  .b-green  { background: #d4f2e3; color: #1a6b43; }
  .b-yellow { background: #fff3c4; color: #7a5e00; }
  .b-red    { background: #fde4e4; color: #8b1e1e; }
  .b-blue   { background: #dceffe; color: #1a4a6b; }
  .b-navy   { background: var(--navy); color: #fff; }
  .b-gray   { background: #e8eaed; color: #444; }
  .b-purple { background: #ede0ff; color: #4a1a7a; }

  /* ── FLOW DIAGRAM ─────────────────────────────────────── */
  .flow-wrap {
    display: flex; flex-wrap: wrap; gap: 0;
    align-items: center; margin: 16px 0;
  }
  .flow-step {
    background: var(--navy); color: #fff;
    padding: 8px 14px; border-radius: 6px;
    font-size: 11px; font-weight: 700; text-align: center;
    min-width: 100px;
  }
  .flow-step .step-num {
    font-size: 9px; opacity: .6; display: block; margin-bottom: 2px;
  }
  .flow-arrow {
    font-size: 18px; color: var(--green); padding: 0 6px; font-weight: 900;
  }
  .flow-step.active { background: var(--green); }
  .flow-step.warn   { background: var(--yellow); color: var(--navy); }

  /* ── CALLOUT BOXES ────────────────────────────────────── */
  .callout {
    border-left: 4px solid var(--green);
    background: #f0faf5;
    padding: 12px 16px; margin: 14px 0; border-radius: 0 6px 6px 0;
  }
  .callout.warn {
    border-left-color: var(--yellow); background: #fffbea;
  }
  .callout.alert {
    border-left-color: var(--red); background: #fff5f5;
  }
  .callout strong { font-weight: 700; }

  /* ── OPEN ITEMS ───────────────────────────────────────── */
  .open-item {
    border: 1px solid var(--yellow);
    background: #fffbea;
    border-radius: 6px; padding: 10px 14px; margin: 8px 0;
  }
  .open-item .oi-id {
    font-size: 10px; font-weight: 800; color: #7a5e00;
    letter-spacing: .5px; text-transform: uppercase;
  }
  .open-item .oi-q { font-weight: 600; font-size: 12px; margin: 3px 0; }
  .open-item .oi-owner { font-size: 11px; color: #666; }

  /* ── FIELD BLOCKS ─────────────────────────────────────── */
  .field-grid {
    display: grid; grid-template-columns: 1fr 1fr; gap: 10px;
    margin: 10px 0;
  }
  .field-card {
    border: 1px solid var(--border); border-radius: 6px;
    padding: 10px 12px; background: var(--gray);
  }
  .field-card .fn { font-weight: 700; font-size: 12px; }
  .field-card .ft { font-size: 10px; color: #666; }
  .field-card .fd { font-size: 11px; margin-top: 3px; color: #333; }

  /* ── VERSION TABLE ────────────────────────────────────── */
  .version-table th { background: #555; }

  /* ── PRINT ────────────────────────────────────────────── */
  @media print {
    .section-block { page-break-inside: avoid; }
    .cover { page-break-after: always; }
  }
</style>
</head>
<body>

<!-- ═══════════════════════════════════════════════════════════
     COVER
═══════════════════════════════════════════════════════════ -->
<div class="cover">
  <div class="logo-bar">
    <div class="logo-mark">PC</div>
    <div class="co-name">Parakeet Communities</div>
  </div>
  <div class="wf-badge">WORKFLOW 006 — LISTINGS</div>
  <h1>Listings<br>Build Spec</h1>
  <div class="sub">QB + FastField Operational OS — Design Phase</div>
  <div class="meta-grid">
    <div class="meta-item">
      <div class="meta-label">Version</div>
      <div class="meta-val">v1.0</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Status</div>
      <div class="status-badge">DRAFT — OPEN ITEMS PENDING</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Date</div>
      <div class="meta-val">08/19/26</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Prepared By</div>
      <div class="meta-val">Parakeet OS Design Team</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Workflow</div>
      <div class="meta-val">WF006 — Listings</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Replaces JotForms</div>
      <div class="meta-val">#2 Home Listing Request Form</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Open Items</div>
      <div class="meta-val">5 (O-WF006-001 through -005)</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Decisions Logged</div>
      <div class="meta-val">D-046 through D-050</div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 1 — OVERVIEW
═══════════════════════════════════════════════════════════ -->
<div class="section-block">
  <div class="sec-hdr">
    <span class="num">Section 01</span>
    <span class="ttl">Workflow Overview</span>
  </div>

  <p>WF006 manages the full listing lifecycle for Parakeet Communities assets — from the Community Manager's listing request through active marketing, price adjustments, and listing close. It is the primary pathway for getting a vacant or newly rehabbed home onto the market.</p>

  <div class="callout">
    <strong>WF006 is independent.</strong> Any Community Manager can submit a listing request for any eligible asset at any time — it does not require WF002 (Rehab) completion as a prerequisite, though WF002's handoff notification to the listing team (Leslie and Tanya) commonly precedes it. When an offer is received, WF007 (Offer to Purchase/Rent) is initiated as a separate workflow.
  </div>

  <h3>Summary Statistics</h3>
  <table>
    <colgroup><col style="width:33%"><col style="width:33%"><col style="width:34%"></colgroup>
    <tbody>
      <tr>
        <td><strong>QB Tables</strong></td>
        <td><strong>FastField Forms</strong></td>
        <td><strong>Automations</strong></td>
      </tr>
      <tr>
        <td>2 (Listing Records + Price History)</td>
        <td>1 (Listing Request Form)</td>
        <td>6 (A-LS-01 through A-LS-06)</td>
      </tr>
      <tr>
        <td><strong>Gate Rules</strong></td>
        <td><strong>Listing Team</strong></td>
        <td><strong>RM Sync</strong></td>
      </tr>
      <tr>
        <td>4 (G-LS-01 through G-LS-04)</td>
        <td>Leslie + Tanya</td>
        <td>Daily batch CSV — 6 PM ET</td>
      </tr>
    </tbody>
  </table>

  <h3>System Roles</h3>
  <table>
    <colgroup><col style="width:22%"><col style="width:25%"><col style="width:53%"></colgroup>
    <thead><tr><th>System</th><th>Role in WF006</th><th>Notes</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>Quickbase (QB)</strong></td>
        <td>Workflow engine</td>
        <td>Listing Records, Price History, automations, gate rules, dashboards. All status tracking lives here.</td>
      </tr>
      <tr>
        <td><strong>FastField</strong></td>
        <td>Field form capture</td>
        <td>Community Manager completes Listing Request Form in FastField. Submission triggers QB record creation.</td>
      </tr>
      <tr>
        <td><strong>Rent Manager (RM)</strong></td>
        <td>System of record</td>
        <td>RM user-defined fields (Listing Status, Listed By, Listing Date, Listing Price) are updated via daily 6 PM ET batch CSV export from QB. RM is the financial and legal source of truth.</td>
      </tr>
      <tr>
        <td><strong>SharePoint</strong></td>
        <td>Document storage</td>
        <td>Marketing materials, photos, listing packages stored in SharePoint. QB stores the link. SharePoint path TBD (O-WF006-004).</td>
      </tr>
    </tbody>
  </table>

  <h3>Listing Team</h3>
  <table>
    <colgroup><col style="width:25%"><col style="width:25%"><col style="width:50%"></colgroup>
    <thead><tr><th>Person</th><th>Role</th><th>Responsibilities in WF006</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>Leslie</strong></td>
        <td>Listing Team Lead</td>
        <td>Reviews and approves/rejects listing requests. Sets Listing Price, Listing Date, Listed By. Manages active listings. Full email to be confirmed at build phase.</td>
      </tr>
      <tr>
        <td><strong>Tanya</strong></td>
        <td>Listing Team Member</td>
        <td>Co-notified on all listing requests. Supports listing management. Full email to be confirmed at build phase.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 2 — TRIGGER
═══════════════════════════════════════════════════════════ -->
<div class="section-block">
  <div class="sec-hdr">
    <span class="num">Section 02</span>
    <span class="ttl">Trigger</span>
  </div>

  <div class="callout">
    <strong>Single trigger:</strong> Community Manager submits the FastField Listing Request Form. Submission creates a QB Listing Record and notifies Leslie and Tanya.
  </div>

  <table>
    <colgroup><col style="width:20%"><col style="width:30%"><col style="width:50%"></colgroup>
    <thead><tr><th>Trigger Type</th><th>Event</th><th>Detail</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>FastField Form Submission</strong></td>
        <td>CM submits Listing Request Form</td>
        <td>Community Manager completes and submits the FastField Listing Request Form for an eligible asset. Replaces JotForm #2 (Home Listing Request Form). QB automation A-LS-01 fires on submission.</td>
      </tr>
    </tbody>
  </table>

  <h3>What Commonly Precedes This Trigger</h3>
  <table>
    <colgroup><col style="width:30%"><col style="width:70%"></colgroup>
    <thead><tr><th>Upstream Event</th><th>Relationship to WF006</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>WF002 Rehab Complete</strong></td>
        <td>When Rehab Status = Complete, A-RH-11 notifies Leslie and Tanya that the home is ready to list. The CM then submits the FastField Listing Request Form to formally initiate WF006. This is the most common path.</td>
      </tr>
      <tr>
        <td><strong>WF003 Disposition = Turn for Sale</strong></td>
        <td>When the Asset Disposition Review assigns Turn for Sale, A-DR-03 updates the asset status. CM may then submit a listing request independently.</td>
      </tr>
      <tr>
        <td><strong>Direct / Acquisition Listing</strong></td>
        <td>New acquisitions, community-owned inventory, or management decisions may prompt a listing request without a preceding WF002 or WF003 event. WF006 is always available as a standalone trigger.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 3 — WORKFLOW STAGES
═══════════════════════════════════════════════════════════ -->
<div class="section-block">
  <div class="sec-hdr">
    <span class="num">Section 03</span>
    <span class="ttl">Workflow Stages</span>
  </div>

  <div class="flow-wrap">
    <div class="flow-step"><span class="step-num">STAGE 1</span>Request Submitted</div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><span class="step-num">STAGE 2</span>Under Review</div>
    <div class="flow-arrow">→</div>
    <div class="flow-step active"><span class="step-num">STAGE 3</span>Active Listing</div>
    <div class="flow-arrow">→</div>
    <div class="flow-step warn"><span class="step-num">STAGE 4</span>Price Reduced</div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><span class="step-num">STAGE 5</span>Pending Offer</div>
    <div class="flow-arrow">→</div>
    <div class="flow-step"><span class="step-num">STAGE 6</span>Closed</div>
  </div>

  <div class="callout warn">
    <strong>Stage 4 (Price Reduced)</strong> is a modifier stage, not a linear block. An active listing moves to Price Reduced when a price change is recorded and returns to Active after the change is applied. It does not interrupt the progression to Pending Offer or Closed.
  </div>

  <table>
    <colgroup><col style="width:5%"><col style="width:18%"><col style="width:25%"><col style="width:25%"><col style="width:27%"></colgroup>
    <thead><tr><th>#</th><th>Stage</th><th>Who Acts</th><th>What Happens</th><th>Exit Condition</th></tr></thead>
    <tbody>
      <tr>
        <td>1</td>
        <td><strong>Request Submitted</strong></td>
        <td>Community Manager (via FastField)</td>
        <td>CM submits Listing Request Form. QB Listing Record created (LST-YYYY-###). Leslie and Tanya notified via A-LS-01.</td>
        <td>Leslie or Tanya reviews the request → advances to Stage 2</td>
      </tr>
      <tr>
        <td>2</td>
        <td><strong>Under Review</strong></td>
        <td>Leslie / Tanya (in QB)</td>
        <td>Listing team reviews the request, confirms asset eligibility, sets Listing Price and Listing Type. May reject and return to CM with notes.</td>
        <td>Approval → Stage 3 (Active). Rejection → CM notified, record status = Rejected.</td>
      </tr>
      <tr>
        <td>3</td>
        <td><strong>Active Listing</strong></td>
        <td>Leslie / Tanya</td>
        <td>Listing Date stamped. Listed By set. Listing distributed to platforms (O-WF006-001 — TBD). RM UDFs updated via daily batch. SharePoint marketing folder linked.</td>
        <td>Price change → Stage 4. Offer received → Stage 5. Withdrawn/expired → Stage 6.</td>
      </tr>
      <tr>
        <td>4</td>
        <td><strong>Price Reduced</strong></td>
        <td>Leslie / Tanya</td>
        <td>New price recorded. Price History entry created (PH-YYYY-###). RM batch sync queued. Status returns to Active after price is updated.</td>
        <td>Price update confirmed → returns to Stage 3 (Active)</td>
      </tr>
      <tr>
        <td>5</td>
        <td><strong>Pending Offer</strong></td>
        <td>WF007 (Offer to Purchase/Rent)</td>
        <td>Offer received. WF007 initiated as a separate workflow. Listing record locked — no price changes, no withdrawals while offer is pending.</td>
        <td>WF007 offer accepted → Stage 6 (Closed — Sold). WF007 offer rejected → returns to Stage 3 (Active).</td>
      </tr>
      <tr>
        <td>6</td>
        <td><strong>Closed</strong></td>
        <td>Leslie / Tanya (or automation)</td>
        <td>Listing closed. Close reason recorded: Sold / Withdrawn / Expired. Asset Status updated in QB. RM final sync triggered. CM notified.</td>
        <td>Terminal stage — record is locked after close.</td>
      </tr>
    </tbody>
  </table>

  <h3>Rejection Path</h3>
  <div class="callout alert">
    <strong>Rejected listings</strong> are closed records — they do not proceed to Stage 3. If the CM needs to re-submit after a rejection, they submit a new Listing Request Form, which creates a new Listing Record (new LST-YYYY-### ID). The rejected record is retained for audit purposes with Status = Rejected and the rejection reason noted.
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 4 — QB ARCHITECTURE
═══════════════════════════════════════════════════════════ -->
<div class="section-block">
  <div class="sec-hdr">
    <span class="num">Section 04</span>
    <span class="ttl">Quickbase Architecture</span>
  </div>

  <h3>4.1 QB Tables</h3>
  <table>
    <colgroup><col style="width:5%"><col style="width:22%"><col style="width:15%"><col style="width:28%"><col style="width:30%"></colgroup>
    <thead><tr><th>#</th><th>Table Name</th><th>Record ID Format</th><th>Purpose</th><th>Key Relationships</th></tr></thead>
    <tbody>
      <tr>
        <td>1</td>
        <td><strong>Listing Records</strong></td>
        <td>LST-YYYY-###</td>
        <td>One record per listing. Captures all listing data from request through close. Primary WF006 table.</td>
        <td>→ Communities, Lots, Assets/Homes, Price History</td>
      </tr>
      <tr>
        <td>2</td>
        <td><strong>Price History</strong></td>
        <td>PH-YYYY-###</td>
        <td>One record per price change event. Tracks original price, new price, change date, and who changed it. Enables audit trail for all price movements.</td>
        <td>→ Listing Records (parent), Communities</td>
      </tr>
    </tbody>
  </table>

  <div class="callout">
    <strong>Shared reference tables</strong> — Communities, Lots, and Assets/Homes are pre-existing reference tables shared across all workflows (WF001–WF006). WF006 reads from them via QB relationship fields; it does not own them.
  </div>

  <h3>4.2 Listing Records — Field Specification</h3>

  <h4>Identification &amp; Cascading Location</h4>
  <table>
    <colgroup><col style="width:26%"><col style="width:14%"><col style="width:10%"><col style="width:50%"></colgroup>
    <thead><tr><th>Field Name</th><th>Type</th><th>Required</th><th>Notes</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>Listing ID</strong></td>
        <td>Auto-generated</td>
        <td><span class="b b-red">Required</span></td>
        <td>Format: LST-YYYY-### (e.g., LST-2026-001). System-generated on record creation.</td>
      </tr>
      <tr>
        <td><strong>Community</strong></td>
        <td>QB Relationship</td>
        <td><span class="b b-red">Required</span></td>
        <td>Cascading dropdown → Communities table. Populated from FastField form submission. Filters available Lots to selected community.</td>
      </tr>
      <tr>
        <td><strong>Lot</strong></td>
        <td>QB Relationship</td>
        <td><span class="b b-red">Required</span></td>
        <td>Cascading dropdown → Lots table. Filtered by Community. Filters available Assets to selected Lot.</td>
      </tr>
      <tr>
        <td><strong>Asset / Home</strong></td>
        <td>QB Relationship</td>
        <td><span class="b b-red">Required</span></td>
        <td>Cascading dropdown → Assets/Homes table. Filtered by Lot. The specific asset being listed.</td>
      </tr>
      <tr>
        <td><strong>Listing Status</strong></td>
        <td>Dropdown</td>
        <td><span class="b b-red">Required</span></td>
        <td>Values: Request Submitted / Under Review / Active / Price Reduced / Pending Offer / Closed — Sold / Closed — Withdrawn / Closed — Expired / Rejected. Set by automation; listing team does not manually change status except to close or reject. Synced to RM UDF daily.</td>
      </tr>
    </tbody>
  </table>

  <h4>Request Fields (populated by FastField form submission)</h4>
  <table>
    <colgroup><col style="width:26%"><col style="width:14%"><col style="width:10%"><col style="width:50%"></colgroup>
    <thead><tr><th>Field Name</th><th>Type</th><th>Required</th><th>Notes</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>Request Date</strong></td>
        <td>Date</td>
        <td><span class="b b-red">Required</span></td>
        <td>Date CM submitted the FastField form. Auto-stamped on record creation.</td>
      </tr>
      <tr>
        <td><strong>Requesting CM</strong></td>
        <td>Text</td>
        <td><span class="b b-red">Required</span></td>
        <td>Community Manager who submitted the request. Pulled from FastField form submission metadata.</td>
      </tr>
      <tr>
        <td><strong>Listing Type</strong></td>
        <td>Dropdown</td>
        <td><span class="b b-red">Required</span></td>
        <td>Values: For Sale / Rent to Own / Lease Option. CM selects on form.</td>
      </tr>
      <tr>
        <td><strong>Proposed Listing Price</strong></td>
        <td>Currency</td>
        <td><span class="b b-red">Required</span></td>
        <td>CM's proposed listing price. Format: $XX,XXX.XX. Listing team may modify during review before setting the Official Listing Price.</td>
      </tr>
      <tr>
        <td><strong>Asset Condition Notes</strong></td>
        <td>Text (multiline)</td>
        <td>Optional</td>
        <td>CM's observations on current asset condition. Informational for the listing team.</td>
      </tr>
      <tr>
        <td><strong>Marketing Notes</strong></td>
        <td>Text (multiline)</td>
        <td>Optional</td>
        <td>Any special features, recent upgrades, or selling points the CM wants to highlight.</td>
      </tr>
    </tbody>
  </table>

  <h4>Listing Team Fields (populated by Leslie / Tanya in QB)</h4>
  <table>
    <colgroup><col style="width:26%"><col style="width:14%"><col style="width:10%"><col style="width:50%"></colgroup>
    <thead><tr><th>Field Name</th><th>Type</th><th>Required</th><th>Notes</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>Official Listing Price</strong></td>
        <td>Currency</td>
        <td><span class="b b-red">Required</span></td>
        <td>Final approved listing price set by Leslie/Tanya. Format: $XX,XXX.XX. G-LS-01: hard block — required before listing can go Active. Synced to RM UDF "Listing Price."</td>
      </tr>
      <tr>
        <td><strong>Listing Date</strong></td>
        <td>Date</td>
        <td><span class="b b-red">Required</span></td>
        <td>Date listing goes live. Format: mm/dd/yy. G-LS-02: hard block — required before listing can go Active. Synced to RM UDF "Listing Date."</td>
      </tr>
      <tr>
        <td><strong>Listed By</strong></td>
        <td>Dropdown</td>
        <td><span class="b b-red">Required</span></td>
        <td>Values: Leslie / Tanya. Who is managing this listing. Synced to RM UDF "Listed By."</td>
      </tr>
      <tr>
        <td><strong>Approved By</strong></td>
        <td>Dropdown</td>
        <td><span class="b b-red">Required</span></td>
        <td>Values: Leslie / Tanya. Who approved the listing request.</td>
      </tr>
      <tr>
        <td><strong>Approval Date</strong></td>
        <td>Date</td>
        <td><span class="b b-red">Required</span></td>
        <td>Date listing team approved the request. Auto-stamped by A-LS-02.</td>
      </tr>
      <tr>
        <td><strong>Listing Platform(s)</strong></td>
        <td>Checkbox (multi-select)</td>
        <td>Optional</td>
        <td>Where this listing is posted. Values TBD (O-WF006-001 — need Leslie). e.g., MHVillage / Zillow / Internal Site / Other.</td>
      </tr>
      <tr>
        <td><strong>Platform Listing URL(s)</strong></td>
        <td>Text</td>
        <td>Optional</td>
        <td>Direct URL(s) to the live listing(s) on each platform. Leslie/Tanya enter after going live.</td>
      </tr>
      <tr>
        <td><strong>Rejection Reason</strong></td>
        <td>Text (multiline)</td>
        <td>Conditional</td>
        <td>Required if listing is rejected. Minimum 10 characters. CM notified via A-LS-03.</td>
      </tr>
    </tbody>
  </table>

  <h4>SharePoint &amp; RM Sync Fields</h4>
  <table>
    <colgroup><col style="width:26%"><col style="width:14%"><col style="width:10%"><col style="width:50%"></colgroup>
    <thead><tr><th>Field Name</th><th>Type</th><th>Required</th><th>Notes</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>SharePoint Marketing Folder Link</strong></td>
        <td>URL</td>
        <td>Optional</td>
        <td>Link to the SharePoint folder for this listing's marketing materials (photos, PDFs, etc.). Folder path TBD (O-WF006-004).</td>
      </tr>
      <tr>
        <td><strong>RM Last Synced</strong></td>
        <td>Date/Time</td>
        <td>Auto</td>
        <td>Timestamp of last successful RM batch export update. Auto-stamped by A-LS-05. Read-only.</td>
      </tr>
      <tr>
        <td><strong>RM Sync Status</strong></td>
        <td>Dropdown</td>
        <td>Auto</td>
        <td>Values: Pending / Synced / Error. Updated by A-LS-05. Read-only. Error triggers alert to listing team.</td>
      </tr>
    </tbody>
  </table>

  <h4>Close Fields</h4>
  <table>
    <colgroup><col style="width:26%"><col style="width:14%"><col style="width:10%"><col style="width:50%"></colgroup>
    <thead><tr><th>Field Name</th><th>Type</th><th>Required</th><th>Notes</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>Close Date</strong></td>
        <td>Date</td>
        <td>Conditional</td>
        <td>Required when Listing Status = any Closed value. Format: mm/dd/yy. Auto-stamped on close.</td>
      </tr>
      <tr>
        <td><strong>Close Reason</strong></td>
        <td>Dropdown</td>
        <td>Conditional</td>
        <td>Required when closing. Values: Sold / Withdrawn / Expired. "Sold" is auto-set when WF007 offer is accepted.</td>
      </tr>
      <tr>
        <td><strong>Days on Market</strong></td>
        <td>Calculated (numeric)</td>
        <td>Auto</td>
        <td>Calculated: Close Date − Listing Date. Auto-populated on close. Read-only.</td>
      </tr>
      <tr>
        <td><strong>Close Notes</strong></td>
        <td>Text (multiline)</td>
        <td>Optional</td>
        <td>Any relevant notes at close (buyer details if sold, reason for withdrawal, etc.).</td>
      </tr>
    </tbody>
  </table>

  <h3>4.3 Price History — Field Specification</h3>
  <table>
    <colgroup><col style="width:26%"><col style="width:14%"><col style="width:10%"><col style="width:50%"></colgroup>
    <thead><tr><th>Field Name</th><th>Type</th><th>Required</th><th>Notes</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>Price History ID</strong></td>
        <td>Auto-generated</td>
        <td><span class="b b-red">Required</span></td>
        <td>Format: PH-YYYY-###</td>
      </tr>
      <tr>
        <td><strong>Parent Listing Record</strong></td>
        <td>QB Relationship</td>
        <td><span class="b b-red">Required</span></td>
        <td>Links to LST-YYYY-### parent record.</td>
      </tr>
      <tr>
        <td><strong>Previous Price</strong></td>
        <td>Currency</td>
        <td><span class="b b-red">Required</span></td>
        <td>Price before the change. Auto-populated from parent Listing Record on creation.</td>
      </tr>
      <tr>
        <td><strong>New Price</strong></td>
        <td>Currency</td>
        <td><span class="b b-red">Required</span></td>
        <td>Price after the change.</td>
      </tr>
      <tr>
        <td><strong>Price Change Date</strong></td>
        <td>Date</td>
        <td><span class="b b-red">Required</span></td>
        <td>Date the price change was recorded. Auto-stamped.</td>
      </tr>
      <tr>
        <td><strong>Changed By</strong></td>
        <td>Dropdown</td>
        <td><span class="b b-red">Required</span></td>
        <td>Values: Leslie / Tanya.</td>
      </tr>
      <tr>
        <td><strong>Reason for Change</strong></td>
        <td>Text</td>
        <td>Optional</td>
        <td>Brief note on why the price was changed.</td>
      </tr>
      <tr>
        <td><strong>Price Change Amount</strong></td>
        <td>Calculated (currency)</td>
        <td>Auto</td>
        <td>Calculated: New Price − Previous Price. Negative value = reduction.</td>
      </tr>
      <tr>
        <td><strong>Price Change %</strong></td>
        <td>Calculated (percentage)</td>
        <td>Auto</td>
        <td>Calculated: (New Price − Previous Price) / Previous Price × 100. Displayed to 1 decimal.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 5 — FASTFIELD FORM
═══════════════════════════════════════════════════════════ -->
<div class="section-block">
  <div class="sec-hdr">
    <span class="num">Section 05</span>
    <span class="ttl">FastField Form</span>
  </div>

  <h3>Form 1 — Listing Request Form</h3>
  <p><strong>FastField Form Name:</strong> PARAKEET — WF006 — Listing Request Form</p>
  <p><strong>Completed By:</strong> Community Manager</p>
  <p><strong>Replaces:</strong> JotForm #2 — Home Listing Request Form</p>
  <p><strong>Submission Trigger:</strong> Fires A-LS-01 — creates QB Listing Record + notifies Leslie and Tanya</p>

  <div class="callout">
    <strong>CM completes this form, not the listing team.</strong> The CM provides asset location, proposed price, condition notes, and marketing highlights. Leslie and Tanya review, modify if needed, and approve or reject inside QB — they do not have a separate FastField form.
  </div>

  <table>
    <colgroup><col style="width:5%"><col style="width:28%"><col style="width:15%"><col style="width:12%"><col style="width:40%"></colgroup>
    <thead><tr><th>#</th><th>Field Label</th><th>Field Type</th><th>Required</th><th>Notes / Logic</th></tr></thead>
    <tbody>
      <tr>
        <td colspan="5" style="background:#2F4E65; color:#fff; font-weight:700; font-size:11px; letter-spacing:.5px;">SECTION A — PROPERTY LOCATION</td>
      </tr>
      <tr>
        <td>1</td>
        <td>Community</td>
        <td>Dropdown</td>
        <td><span class="b b-red">Required</span></td>
        <td>68-community list from QB. Cascades to Lot field.</td>
      </tr>
      <tr>
        <td>2</td>
        <td>Lot Number / Site</td>
        <td>Dropdown</td>
        <td><span class="b b-red">Required</span></td>
        <td>Filtered by Community. Cascades to Asset field.</td>
      </tr>
      <tr>
        <td>3</td>
        <td>Asset / Home</td>
        <td>Dropdown</td>
        <td><span class="b b-red">Required</span></td>
        <td>Filtered by Lot. Links to QB Asset record.</td>
      </tr>
      <tr>
        <td colspan="5" style="background:#2F4E65; color:#fff; font-weight:700; font-size:11px; letter-spacing:.5px;">SECTION B — LISTING DETAILS</td>
      </tr>
      <tr>
        <td>4</td>
        <td>Listing Type</td>
        <td>Dropdown</td>
        <td><span class="b b-red">Required</span></td>
        <td>Values: For Sale / Rent to Own / Lease Option.</td>
      </tr>
      <tr>
        <td>5</td>
        <td>Proposed Listing Price</td>
        <td>Currency</td>
        <td><span class="b b-red">Required</span></td>
        <td>CM's suggested listing price. Format: $XX,XXX.XX. Listing team confirms or modifies during review.</td>
      </tr>
      <tr>
        <td>6</td>
        <td>Desired Listing Date</td>
        <td>Date</td>
        <td>Optional</td>
        <td>CM's preferred go-live date. Informational for Leslie/Tanya — not a binding commitment.</td>
      </tr>
      <tr>
        <td colspan="5" style="background:#2F4E65; color:#fff; font-weight:700; font-size:11px; letter-spacing:.5px;">SECTION C — ASSET CONDITION</td>
      </tr>
      <tr>
        <td>7</td>
        <td>Asset Condition</td>
        <td>Dropdown</td>
        <td><span class="b b-red">Required</span></td>
        <td>Values: Excellent / Good / Fair / Poor. CM's assessment of current asset condition.</td>
      </tr>
      <tr>
        <td>8</td>
        <td>Rehab Completed?</td>
        <td>Yes / No</td>
        <td><span class="b b-red">Required</span></td>
        <td>Was a WF002 Rehab completed on this asset prior to this listing request?</td>
      </tr>
      <tr>
        <td>9</td>
        <td>Condition Notes</td>
        <td>Text (multiline)</td>
        <td>Optional</td>
        <td>Additional condition details, known issues, recent repairs not captured in WF002.</td>
      </tr>
      <tr>
        <td colspan="5" style="background:#2F4E65; color:#fff; font-weight:700; font-size:11px; letter-spacing:.5px;">SECTION D — MARKETING HIGHLIGHTS</td>
      </tr>
      <tr>
        <td>10</td>
        <td>Key Selling Points</td>
        <td>Text (multiline)</td>
        <td>Optional</td>
        <td>Features, upgrades, community amenities worth highlighting in the listing. Used by Leslie/Tanya when drafting listing copy.</td>
      </tr>
      <tr>
        <td>11</td>
        <td>Photos Available?</td>
        <td>Yes / No</td>
        <td><span class="b b-red">Required</span></td>
        <td>Are photos ready to upload for the listing?</td>
      </tr>
      <tr>
        <td>12</td>
        <td>Photo Upload</td>
        <td>File Attachment (multi)</td>
        <td>Conditional</td>
        <td>Required if Photos Available = Yes. Up to 10 photos. JPG/PNG. FastField delivers photo URLs to QB.</td>
      </tr>
      <tr>
        <td colspan="5" style="background:#2F4E65; color:#fff; font-weight:700; font-size:11px; letter-spacing:.5px;">SECTION E — SUBMISSION</td>
      </tr>
      <tr>
        <td>13</td>
        <td>Requesting CM Name</td>
        <td>Text</td>
        <td><span class="b b-red">Required</span></td>
        <td>Full name of the Community Manager submitting this request.</td>
      </tr>
      <tr>
        <td>14</td>
        <td>Submission Date</td>
        <td>Date</td>
        <td><span class="b b-red">Required</span></td>
        <td>Auto-populated to today's date. CM can confirm or correct.</td>
      </tr>
      <tr>
        <td>15</td>
        <td>Additional Notes</td>
        <td>Text (multiline)</td>
        <td>Optional</td>
        <td>Any other information the CM wants the listing team to know.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 6 — AUTOMATIONS
═══════════════════════════════════════════════════════════ -->
<div class="section-block">
  <div class="sec-hdr">
    <span class="num">Section 06</span>
    <span class="ttl">Automations</span>
  </div>

  <div class="callout">
    <strong>Community Manager does not manually set any QB status fields.</strong> All Listing Status changes are driven by Leslie/Tanya actions in QB or by automation. The CM's role in QB is read-only after the FastField form is submitted.
  </div>

  <table>
    <colgroup><col style="width:8%"><col style="width:22%"><col style="width:20%"><col style="width:50%"></colgroup>
    <thead><tr><th>ID</th><th>Name</th><th>Trigger</th><th>Action</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>A-LS-01</strong></td>
        <td>Listing Request Received</td>
        <td>FastField Listing Request Form submitted</td>
        <td>
          1. Create QB Listing Record (LST-YYYY-###), Status = Request Submitted.<br>
          2. Populate all fields from FastField submission (Community, Lot, Asset, Listing Type, Proposed Price, Condition, CM Name, Submission Date, photos).<br>
          3. Send notification to Leslie and Tanya: <em>"New Listing Request submitted by [CM Name] for [Community] — [Lot/Asset]. Proposed price: $[X]. Review in QB: [link]."</em>
        </td>
      </tr>
      <tr>
        <td><strong>A-LS-02</strong></td>
        <td>Listing Approved</td>
        <td>Leslie/Tanya sets Listing Status = Active in QB</td>
        <td>
          1. Stamp Approval Date = today.<br>
          2. Stamp Listing Date = today (if not already set by team).<br>
          3. Set RM Sync Status = Pending.<br>
          4. Send notification to requesting CM: <em>"Your listing request for [Community — Lot/Asset] has been approved and is now active. Listing Price: $[X]. Listed By: [Leslie/Tanya]."</em>
        </td>
      </tr>
      <tr>
        <td><strong>A-LS-03</strong></td>
        <td>Listing Rejected</td>
        <td>Leslie/Tanya sets Listing Status = Rejected in QB</td>
        <td>
          1. Require Rejection Reason (hard block via G-LS-03 if empty).<br>
          2. Send notification to requesting CM: <em>"Your listing request for [Community — Lot/Asset] was not approved. Reason: [Rejection Reason]. Contact Leslie or Tanya with questions."</em><br>
          3. Lock record — no further edits by CM. Record retained for audit.
        </td>
      </tr>
      <tr>
        <td><strong>A-LS-04</strong></td>
        <td>Price Change Recorded</td>
        <td>Official Listing Price updated on an Active or Price Reduced listing record</td>
        <td>
          1. Create Price History record (PH-YYYY-###): Previous Price = old value, New Price = new value, Price Change Date = today, Changed By = Leslie/Tanya.<br>
          2. Set Listing Status = Price Reduced.<br>
          3. Set RM Sync Status = Pending.<br>
          4. Send notification to requesting CM: <em>"Listing price for [Community — Lot/Asset] has been updated from $[old] to $[new]."</em>
        </td>
      </tr>
      <tr>
        <td><strong>A-LS-05</strong></td>
        <td>Daily RM Batch Export</td>
        <td>Daily — 6 PM ET</td>
        <td>
          Export CSV of all Listing Records where RM Sync Status = Pending or last sync &gt; 24 hours ago.<br>
          CSV columns: Listing ID, Community Short Name, Lot Number, Asset ID, Listing Status, Listed By, Listing Date, Official Listing Price, Last Update Date.<br>
          Delivered to Justin / RM admin team for import into RM user-defined fields.<br>
          On successful export: Set RM Sync Status = Synced, RM Last Synced = current timestamp.<br>
          Column mapping to exact RM UDF field names to be confirmed at build phase (O-WF006-002).
        </td>
      </tr>
      <tr>
        <td><strong>A-LS-06</strong></td>
        <td>Listing Closed</td>
        <td>Leslie/Tanya sets Listing Status = any Closed value</td>
        <td>
          1. Stamp Close Date = today.<br>
          2. Calculate Days on Market = Close Date − Listing Date.<br>
          3. If Close Reason = Sold: update Asset Status in QB to reflect sold (RM-exact value to confirm).<br>
          4. Set RM Sync Status = Pending (final sync).<br>
          5. Lock Listing Record — no further edits.<br>
          6. Send notification to requesting CM: <em>"Listing for [Community — Lot/Asset] has been closed. Close Reason: [Sold/Withdrawn/Expired]. Days on Market: [X]."</em>
        </td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 7 — GATE RULES
═══════════════════════════════════════════════════════════ -->
<div class="section-block">
  <div class="sec-hdr">
    <span class="num">Section 07</span>
    <span class="ttl">Gate Rules</span>
  </div>

  <div class="callout alert">
    <strong>All gate rules are hard blocks.</strong> QB will not allow the record to advance until the condition is met. No exceptions, no overrides.
  </div>

  <table>
    <colgroup><col style="width:8%"><col style="width:22%"><col style="width:25%"><col style="width:25%"><col style="width:20%"></colgroup>
    <thead><tr><th>ID</th><th>Gate Name</th><th>Condition</th><th>Block Message</th><th>Resolves When</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>G-LS-01</strong></td>
        <td>Official Price Required Before Active</td>
        <td>Official Listing Price is blank when attempting to set Status = Active</td>
        <td><em>"Official Listing Price is required before a listing can go Active. Enter a confirmed listing price to proceed."</em></td>
        <td>Official Listing Price is entered.</td>
      </tr>
      <tr>
        <td><strong>G-LS-02</strong></td>
        <td>Listing Date Required Before Active</td>
        <td>Listing Date is blank when attempting to set Status = Active</td>
        <td><em>"Listing Date is required before a listing can go Active. Enter the go-live date to proceed."</em></td>
        <td>Listing Date is entered.</td>
      </tr>
      <tr>
        <td><strong>G-LS-03</strong></td>
        <td>Rejection Reason Required</td>
        <td>Rejection Reason is blank or fewer than 10 characters when attempting to set Status = Rejected</td>
        <td><em>"A rejection reason is required when rejecting a listing request. Enter at least 10 characters to proceed."</em></td>
        <td>Rejection Reason field contains ≥ 10 characters.</td>
      </tr>
      <tr>
        <td><strong>G-LS-04</strong></td>
        <td>No Changes While Offer Pending</td>
        <td>Listing Status = Pending Offer and user attempts to change Official Listing Price or set Status = any Closed value (except Closed — Sold via WF007)</td>
        <td><em>"This listing has a pending offer and cannot be modified or closed until the offer is resolved in WF007."</em></td>
        <td>WF007 offer is accepted (→ auto-close Sold) or rejected (→ returns to Active).</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 8 — RM ALIGNMENT
═══════════════════════════════════════════════════════════ -->
<div class="section-block">
  <div class="sec-hdr">
    <span class="num">Section 08</span>
    <span class="ttl">Rent Manager Alignment</span>
  </div>

  <p>Rent Manager is the system of record for all listing financial and status data. QB captures and manages the listing workflow; RM UDFs are updated via the daily 6 PM ET batch CSV export (A-LS-05). RM does not drive QB — data flows QB → RM only.</p>

  <div class="callout warn">
    <strong>RM user-defined fields</strong> — Austin confirmed that RM has user-defined fields for Listing Status, Listed By, Listing Date, Listing Price, and related data. The exact RM UDF field names and allowed values must be confirmed by Justin / RM admin before the build phase to ensure the batch CSV export maps correctly. See O-WF006-002 and O-WF006-003.
  </div>

  <h3>QB → RM Field Mapping (pending confirmation)</h3>
  <table>
    <colgroup><col style="width:32%"><col style="width:32%"><col style="width:36%"></colgroup>
    <thead><tr><th>QB Field (Listing Record)</th><th>RM UDF (name TBD)</th><th>Notes</th></tr></thead>
    <tbody>
      <tr>
        <td>Listing Status</td>
        <td><em>TBD — O-WF006-002</em></td>
        <td>Exact RM UDF name and allowed values to confirm. QB values: Active / Price Reduced / Pending Offer / Closed — Sold, etc.</td>
      </tr>
      <tr>
        <td>Listed By</td>
        <td><em>TBD — O-WF006-002</em></td>
        <td>QB values: Leslie / Tanya. RM UDF may use different labels — confirm.</td>
      </tr>
      <tr>
        <td>Listing Date</td>
        <td><em>TBD — O-WF006-002</em></td>
        <td>Date format: mm/dd/yy in QB. RM may require different format — confirm.</td>
      </tr>
      <tr>
        <td>Official Listing Price</td>
        <td><em>TBD — O-WF006-002</em></td>
        <td>Currency — $XX,XXX.XX. RM UDF type (numeric/text/currency) to confirm.</td>
      </tr>
      <tr>
        <td>Listing Type</td>
        <td><em>TBD — O-WF006-003</em></td>
        <td>QB values: For Sale / Rent to Own / Lease Option. RM equivalent to confirm.</td>
      </tr>
      <tr>
        <td>Close Date</td>
        <td><em>TBD — O-WF006-002</em></td>
        <td>Populated when listing closes. RM may have a separate "Date Sold" field.</td>
      </tr>
    </tbody>
  </table>

  <h3>Batch Export Cadence</h3>
  <table>
    <colgroup><col style="width:25%"><col style="width:75%"></colgroup>
    <tbody>
      <tr>
        <td><strong>Export Time</strong></td>
        <td>Daily at 6 PM ET (same export as WF004 Move Out batch — may be consolidated into a single daily Parakeet → RM export file at build phase)</td>
      </tr>
      <tr>
        <td><strong>Scope</strong></td>
        <td>All Listing Records where RM Sync Status = Pending or last sync &gt; 24 hours ago with any status change</td>
      </tr>
      <tr>
        <td><strong>Recipient</strong></td>
        <td>Justin / RM admin team — imports into RM user-defined fields</td>
      </tr>
      <tr>
        <td><strong>Format</strong></td>
        <td>CSV. Column mapping to RM UDF field names confirmed at build phase (O-WF006-002).</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 9 — WORKFLOW CONNECTIONS
═══════════════════════════════════════════════════════════ -->
<div class="section-block">
  <div class="sec-hdr">
    <span class="num">Section 09</span>
    <span class="ttl">Workflow Connections</span>
  </div>

  <table>
    <colgroup><col style="width:15%"><col style="width:15%"><col style="width:20%"><col style="width:50%"></colgroup>
    <thead><tr><th>Connected Workflow</th><th>Direction</th><th>Connection Type</th><th>Detail</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>WF002 — Rehab</strong></td>
        <td>WF002 → WF006</td>
        <td>Notification handoff</td>
        <td>When Rehab Status = Complete, A-RH-11 notifies Leslie and Tanya. The CM then initiates WF006 independently by submitting the FastField Listing Request Form. WF002 does not auto-create a WF006 record.</td>
      </tr>
      <tr>
        <td><strong>WF003 — Asset Disposition</strong></td>
        <td>WF003 → WF006</td>
        <td>Status signal</td>
        <td>When Disposition = Turn for Sale, A-DR-03 updates Asset Status to "For Sale." This signals readiness to list. The CM then independently initiates WF006. WF003 does not auto-create a WF006 record.</td>
      </tr>
      <tr>
        <td><strong>WF007 — Offer to Purchase/Rent</strong></td>
        <td>WF006 → WF007</td>
        <td>Offer trigger (separate workflow)</td>
        <td>When an offer is received on an Active listing, WF007 is initiated independently. WF006 Listing Status is set to Pending Offer (G-LS-04 blocks changes). If WF007 offer is accepted → WF006 auto-closes as Sold. If rejected → WF006 returns to Active.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 10 — OPEN ITEMS
═══════════════════════════════════════════════════════════ -->
<div class="section-block">
  <div class="sec-hdr">
    <span class="num">Section 10</span>
    <span class="ttl">Open Items</span>
  </div>

  <p>The following items require input before WF006 can be finalized and locked. This spec reflects the confirmed architecture; these open items affect specific field values, platform integrations, and RM field mapping.</p>

  <div class="open-item">
    <div class="oi-id">O-WF006-001 — Listing Platforms</div>
    <div class="oi-q">Where does Parakeet post listings? (e.g., MHVillage, Zillow, internal website, Realtor.com, other?) Austin has indicated this needs to come from Leslie.</div>
    <div class="oi-owner"><strong>Owner:</strong> Leslie | <strong>Impact:</strong> Listing Platform(s) field values in QB; integration scope if any platforms have APIs or direct submission tools.</div>
  </div>

  <div class="open-item">
    <div class="oi-id">O-WF006-002 — RM UDF Field Names</div>
    <div class="oi-q">What are the exact RM user-defined field names for Listing Status, Listed By, Listing Date, Listing Price, and any additional listing UDFs? Required to build the batch CSV export column mapping for A-LS-05.</div>
    <div class="oi-owner"><strong>Owner:</strong> Justin / RM Admin | <strong>Impact:</strong> A-LS-05 batch CSV column headers; RM import template.</div>
  </div>

  <div class="open-item">
    <div class="oi-id">O-WF006-003 — RM Listing Status Allowed Values</div>
    <div class="oi-q">What are the allowed values for the RM Listing Status user-defined field? QB Listing Status values (Active / Price Reduced / Pending Offer / Closed — Sold, etc.) need to map 1:1 to RM's existing UDF values, or RM values need to be established.</div>
    <div class="oi-owner"><strong>Owner:</strong> Justin / RM Admin | <strong>Impact:</strong> QB Listing Status dropdown values; RM UDF dropdown values; batch export mapping.</div>
  </div>

  <div class="open-item">
    <div class="oi-id">O-WF006-004 — SharePoint Folder Structure</div>
    <div class="oi-q">What is the SharePoint folder path and naming convention for listing marketing materials? (e.g., /Communities/[Community Name]/Listings/[LST-YYYY-###]/) Required to configure the SharePoint Marketing Folder Link field and any Power Automate auto-folder-creation automation.</div>
    <div class="oi-owner"><strong>Owner:</strong> Austin / IT | <strong>Impact:</strong> SharePoint Marketing Folder Link field; optional A-LS-02 enhancement to auto-create SharePoint folder on listing approval.</div>
  </div>

  <div class="open-item">
    <div class="oi-id">O-WF006-005 — Listing SLA / Review Timeline</div>
    <div class="oi-q">Is there a target SLA for Leslie/Tanya to review and approve/reject a listing request after it is submitted? (e.g., within 2 business days of submission?) If yes, should QB trigger a reminder or escalation if the request sits in "Under Review" past the SLA?</div>
    <div class="oi-owner"><strong>Owner:</strong> Austin | <strong>Impact:</strong> May add A-LS-07 (review SLA reminder) to the automation set.</div>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════════
     SECTION 11 — VERSION HISTORY
═══════════════════════════════════════════════════════════ -->
<div class="section-block">
  <div class="sec-hdr">
    <span class="num">Section 11</span>
    <span class="ttl">Version History</span>
  </div>

  <table class="version-table">
    <colgroup><col style="width:10%"><col style="width:12%"><col style="width:18%"><col style="width:60%"></colgroup>
    <thead><tr><th>Version</th><th>Date</th><th>Status</th><th>Changes</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>v1.0</strong></td>
        <td>08/19/26</td>
        <td><span class="b b-yellow">Draft</span></td>
        <td>Initial spec. Decisions D-046–D-050 incorporated. Architecture confirmed: FastField Listing Request Form (CM trigger), 2 QB tables, 6 automations, 4 gate rules, daily RM batch sync. 5 open items remain (O-WF006-001 through -005). Locks after open items resolved.</td>
      </tr>
    </tbody>
  </table>
</div>

</body>
</html>"""

with open("/home/ubuntu/parakeet_listings_spec_v1.0.html", "w") as f:
    f.write(html)

print("Written successfully")
