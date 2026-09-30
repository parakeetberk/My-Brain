
with open('/home/ubuntu/parakeet_rollout_overview_v1.0.html', 'r') as f:
    html = f.read()

# --- NEW CSS ---
new_css = """
  /* =========================================================
     WAVE 0 — ALREADY BUILT SECTION
     ========================================================= */
  .w0-intro-box { background: var(--white); border: 1px solid var(--border); border-radius: 10px; padding: 20px 26px; margin-bottom: 24px; }
  .w0-intro-box p { font-size: 14px; color: var(--text); line-height: 1.75; }

  .w0-card { background: var(--white); border: 1px solid var(--border); border-radius: 12px; margin-bottom: 18px; overflow: hidden; }
  .w0-locked { border-left: 5px solid var(--green); }
  .w0-draft   { border-left: 5px solid var(--yellow); }

  .w0-card-header { display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 16px 22px; border-bottom: 1px solid var(--border); flex-wrap: wrap; }
  .w0-id-block { display: flex; align-items: center; gap: 12px; flex: 1; min-width: 240px; }
  .w0-wfid  { font-size: 13px; font-weight: 900; color: var(--navy); background: var(--navy-light); border-radius: 6px; padding: 4px 10px; white-space: nowrap; }
  .w0-name  { font-size: 15px; font-weight: 800; color: var(--navy); }
  .w0-badge { display: inline-block; font-size: 11px; font-weight: 800; padding: 4px 12px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.05em; white-space: nowrap; }
  .badge-locked { background: var(--green-light); color: #1a7a52; }
  .badge-draft  { background: #fffbeb; color: #92400e; border: 1px solid #fde68a; }

  .w0-arch-stats { display: flex; gap: 20px; flex-shrink: 0; }
  .w0-stat { display: flex; flex-direction: column; align-items: center; text-align: center; }
  .w0-stat-num { font-size: 20px; font-weight: 900; color: var(--navy); line-height: 1; }
  .w0-stat-lbl { font-size: 10px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); font-weight: 600; margin-top: 3px; }

  .w0-card-body { padding: 18px 22px; }
  .w0-decisions-title { font-size: 11px; font-weight: 800; color: var(--navy); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px; }
  .w0-decisions ul { padding-left: 18px; }
  .w0-decisions ul li { font-size: 13.5px; color: var(--text); line-height: 1.65; margin-bottom: 8px; }
  .w0-decisions ul li:last-child { margin-bottom: 0; }
  .w0-decisions ul li strong { color: var(--navy); }

  .w0-open-items { margin-top: 16px; background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 14px 16px; }
  .w0-open-title { font-size: 11px; font-weight: 800; color: #92400e; text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 10px; }
  .w0-open-list { display: flex; flex-direction: column; gap: 7px; }
  .w0-open-item { font-size: 13px; color: var(--text); display: flex; align-items: flex-start; gap: 10px; }
  .open-id { font-size: 10px; font-weight: 800; color: #92400e; background: #fde68a; border-radius: 4px; padding: 2px 8px; white-space: nowrap; flex-shrink: 0; margin-top: 2px; }

  /* WHAT'S NEXT CALLOUT */
  .next-callout { background: var(--navy); color: white; border-radius: 12px; padding: 26px 30px; margin-top: 22px; margin-bottom: 44px; }
  .next-callout-header { display: flex; align-items: center; gap: 12px; margin-bottom: 10px; }
  .next-callout-flag { font-size: 20px; color: var(--yellow); }
  .next-callout-title { font-size: 16px; font-weight: 800; color: white; }
  .next-callout-desc { font-size: 13.5px; color: rgba(255,255,255,0.75); line-height: 1.7; margin-bottom: 20px; }
  .next-items-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 22px; }
  .next-items-block-title { font-size: 11px; font-weight: 800; color: var(--yellow); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px; }
  .next-item-row { display: flex; align-items: flex-start; gap: 10px; font-size: 13px; color: rgba(255,255,255,0.85); margin-bottom: 7px; }
  .ni-id { font-size: 10px; font-weight: 800; background: rgba(255,255,255,0.12); border-radius: 4px; padding: 2px 7px; white-space: nowrap; flex-shrink: 0; margin-top: 2px; color: var(--yellow); }
"""

# Insert new CSS before closing </style>
html = html.replace('</style>', new_css + '\n</style>', 1)

# --- NEW SECTION HTML ---
new_section = """
  <!-- ======================================================
       WAVE 0 DETAIL — WHAT WE'VE ALREADY BUILT
       ====================================================== -->
  <div class="section-title" style="margin-top: 44px;">What We&rsquo;ve Already Built &mdash; Wave 0</div>

  <div class="w0-intro-box">
    <p>Before the proposed wave plan kicks off, the team has already put in significant design and architecture work. The five workflows below form the operational core of the system. Three are fully <strong>LOCKED</strong> — design is complete, spec is signed off, ready to build — and two are in active <strong>DRAFT</strong> — architecture is designed and well-defined, with a handful of specific decisions still needed before they can lock. Here&rsquo;s exactly where each one stands.</p>
  </div>

  <!-- WF001 -->
  <div class="w0-card w0-locked">
    <div class="w0-card-header">
      <div class="w0-id-block">
        <div class="w0-wfid">WF001</div>
        <div class="w0-name">Home Ordering, Delivery &amp; Set</div>
        <div class="w0-badge badge-locked">&#10003; LOCKED v1.2</div>
      </div>
      <div class="w0-arch-stats">
        <div class="w0-stat"><span class="w0-stat-num">12</span><span class="w0-stat-lbl">Stages</span></div>
        <div class="w0-stat"><span class="w0-stat-num">7</span><span class="w0-stat-lbl">QB Tables</span></div>
        <div class="w0-stat"><span class="w0-stat-num">4</span><span class="w0-stat-lbl">FF Forms</span></div>
        <div class="w0-stat"><span class="w0-stat-num">14</span><span class="w0-stat-lbl">Automations</span></div>
        <div class="w0-stat"><span class="w0-stat-num">9</span><span class="w0-stat-lbl">Gate Rules</span></div>
      </div>
    </div>
    <div class="w0-card-body">
      <div class="w0-decisions">
        <div class="w0-decisions-title">&#10003;&nbsp; What&rsquo;s Built &amp; Locked</div>
        <ul>
          <li><strong>Two-stage sequential FastField inspection</strong> is fully specced: Construction Inspection (89 items across 7 sections) must be completed and submitted before the Ops/Sales Readiness Inspection (71 items, 10 sections) can even open. There&rsquo;s no way to skip or reorder this in the system.</li>
          <li><strong>Hard gate rules enforced by QB automation</strong> — CMs cannot manually advance a home to the next stage. Every status change is triggered by the system when all gate conditions are met. No manual overrides.</li>
          <li><strong>Lot Prep gate</strong>: WF026 (Lot Prep) must pass its inspection before a new home order can be placed. The system blocks ordering if the lot hasn&rsquo;t cleared.</li>
          <li><strong>Automatic downstream handoffs</strong>: on set completion, WF027 (Utility Activation) is triggered automatically. Any punch-list failures during inspection auto-generate a WF002 Rehab record.</li>
          <li>WF001 is the most upstream workflow in the entire OS &mdash; it creates the Asset record every other workflow reads from. It goes first for a reason.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- WF002 -->
  <div class="w0-card w0-locked">
    <div class="w0-card-header">
      <div class="w0-id-block">
        <div class="w0-wfid">WF002</div>
        <div class="w0-name">Rehab Management</div>
        <div class="w0-badge badge-locked">&#10003; LOCKED v1.3</div>
      </div>
      <div class="w0-arch-stats">
        <div class="w0-stat"><span class="w0-stat-num">9</span><span class="w0-stat-lbl">Stages</span></div>
        <div class="w0-stat"><span class="w0-stat-num">5</span><span class="w0-stat-lbl">QB Tables</span></div>
        <div class="w0-stat"><span class="w0-stat-num">1</span><span class="w0-stat-lbl">FF Form</span></div>
        <div class="w0-stat"><span class="w0-stat-num">12</span><span class="w0-stat-lbl">Automations</span></div>
        <div class="w0-stat"><span class="w0-stat-num">8</span><span class="w0-stat-lbl">Gate Rules</span></div>
      </div>
    </div>
    <div class="w0-card-body">
      <div class="w0-decisions">
        <div class="w0-decisions-title">&#10003;&nbsp; What&rsquo;s Built &amp; Locked</div>
        <ul>
          <li><strong>Tiered bid approval is fully locked</strong>: under $2,500 = no approval needed; $2,500&ndash;$5,000 = Regional Manager must approve in QB; over $5,000 = Austin signs off. No contractor starts work without the right approval in the system.</li>
          <li><strong>Full financial tracking</strong> across 7 budget categories with actual cost rollup and variance tracking. Budget vs. actual is visible in QB in real time throughout the rehab.</li>
          <li><strong>SLAs are enforced</strong>: 3-business-day walkthrough from trigger, 5-business-day task completion, 30-calendar-day cap for the full project. SLA breaches auto-escalate to the Regional Manager.</li>
          <li><strong>Photo documentation</strong>: before, during, and after photos are stored as QB attachments and pushed to SharePoint automatically. No manual uploads.</li>
          <li><strong>Listing team auto-notification</strong>: the moment Rehab Status = Complete, Leslie and Tanya receive an automatic notification to begin the WF006 listing process. No one has to remember to tell them.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- WF003 -->
  <div class="w0-card w0-locked">
    <div class="w0-card-header">
      <div class="w0-id-block">
        <div class="w0-wfid">WF003</div>
        <div class="w0-name">TBD Process</div>
        <div class="w0-badge badge-locked">&#10003; LOCKED v1.1</div>
      </div>
      <div class="w0-arch-stats">
        <div class="w0-stat"><span class="w0-stat-num">2</span><span class="w0-stat-lbl">QB Tables</span></div>
        <div class="w0-stat"><span class="w0-stat-num">5</span><span class="w0-stat-lbl">Automations</span></div>
        <div class="w0-stat"><span class="w0-stat-num">3</span><span class="w0-stat-lbl">Gate Rules</span></div>
      </div>
    </div>
    <div class="w0-card-body">
      <div class="w0-decisions">
        <div class="w0-decisions-title">&#10003;&nbsp; What&rsquo;s Built &amp; Locked</div>
        <ul>
          <li><strong>Weekly Monday meeting trigger</strong>: QB automatically surfaces all homes eligible for the decision meeting each week. No one has to manually pull a list or remember which homes are pending.</li>
          <li><strong>Three disposition paths are fully mapped</strong>: Rehab (triggers WF002), Demo (triggers WF025 Demo to Infill), Turn for Sale (triggers WF006 Listings). Each downstream workflow kicks off automatically on decision.</li>
          <li><strong>Hold is a hard block</strong>: placing a home on Hold requires Disposition Notes (minimum 10 characters). No automation fires, no next step runs, until the Hold is cleared. This prevents decisions from falling through the cracks.</li>
          <li><strong>Single leadership recap email</strong> is sent automatically when the meeting is closed &mdash; no one has to write or distribute a manual summary.</li>
          <li>QB record IDs: Decision Meetings use <em>DM-YYYY-###</em> format; Decision Items use <em>DI-YYYY-###</em>.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- WF004 -->
  <div class="w0-card w0-draft">
    <div class="w0-card-header">
      <div class="w0-id-block">
        <div class="w0-wfid">WF004</div>
        <div class="w0-name">Move Out</div>
        <div class="w0-badge badge-draft">&#9997; DRAFT v1.0</div>
      </div>
      <div class="w0-arch-stats">
        <div class="w0-stat"><span class="w0-stat-num">2</span><span class="w0-stat-lbl">QB Tables</span></div>
        <div class="w0-stat"><span class="w0-stat-num">1</span><span class="w0-stat-lbl">FF Form</span></div>
        <div class="w0-stat"><span class="w0-stat-num">3</span><span class="w0-stat-lbl">Triggers</span></div>
        <div class="w0-stat"><span class="w0-stat-num">5</span><span class="w0-stat-lbl">Open Items</span></div>
      </div>
    </div>
    <div class="w0-card-body">
      <div class="w0-decisions">
        <div class="w0-decisions-title">&#10003;&nbsp; What&rsquo;s Designed &amp; Locked In</div>
        <ul>
          <li><strong>Three move-out triggers</strong> all feed the same workflow path: voluntary resident notice, lease non-renewal, and eviction outcome. One process, three clean entry points &mdash; no separate workflows for each.</li>
          <li><strong>FastField Move Out Inspection Form</strong>: completed by the CM on-site. Regional Manager approves or rejects inside FastField (not in QB). The <strong>48-hour inspection SLA</strong> from move-out date is locked &mdash; that&rsquo;s not one of the open items.</li>
          <li><strong>Inspection storage</strong>: results save directly to SharePoint; QB stores the SharePoint link and inspection date. QB is not the document store here &mdash; SharePoint is.</li>
          <li><strong>RM sync</strong>: Move Out records come from RM to QB via a daily 6 PM ET batch CSV import. QB reads from RM; it never writes financial data back.</li>
          <li>QB record IDs: Move Out Records use <em>MO-YYYY-###</em> format, linked to the Move Out Inspections table.</li>
        </ul>
      </div>
      <div class="w0-open-items">
        <div class="w0-open-title">&#9888;&nbsp; 5 Open Items &mdash; Need Answers Before This Can Lock</div>
        <div class="w0-open-list">
          <div class="w0-open-item"><span class="open-id">O-WF004-001</span>RM column mapping &mdash; which RM columns feed which QB fields in the daily sync</div>
          <div class="w0-open-item"><span class="open-id">O-WF004-002</span>Inspection checklist items &mdash; full line-item list for the FastField Move Out form</div>
          <div class="w0-open-item"><span class="open-id">O-WF004-003</span>FastField approval routing detail &mdash; exact approval-chain configuration inside FastField</div>
          <div class="w0-open-item"><span class="open-id">O-WF004-004</span>SharePoint destination path &mdash; which folder/site inspection results are saved to</div>
          <div class="w0-open-item"><span class="open-id">O-WF004-005</span>Rejected form correction flow &mdash; what happens when the Regional rejects the FastField form</div>
        </div>
      </div>
    </div>
  </div>

  <!-- WF006 -->
  <div class="w0-card w0-draft">
    <div class="w0-card-header">
      <div class="w0-id-block">
        <div class="w0-wfid">WF006</div>
        <div class="w0-name">Listings</div>
        <div class="w0-badge badge-draft">&#9997; DRAFT v1.0</div>
      </div>
      <div class="w0-arch-stats">
        <div class="w0-stat"><span class="w0-stat-num">2</span><span class="w0-stat-lbl">QB Tables</span></div>
        <div class="w0-stat"><span class="w0-stat-num">1</span><span class="w0-stat-lbl">FF Form</span></div>
        <div class="w0-stat"><span class="w0-stat-num">6</span><span class="w0-stat-lbl">Automations</span></div>
        <div class="w0-stat"><span class="w0-stat-num">4</span><span class="w0-stat-lbl">Gate Rules</span></div>
        <div class="w0-stat"><span class="w0-stat-num">5</span><span class="w0-stat-lbl">Open Items</span></div>
      </div>
    </div>
    <div class="w0-card-body">
      <div class="w0-decisions">
        <div class="w0-decisions-title">&#10003;&nbsp; What&rsquo;s Designed &amp; Locked In</div>
        <ul>
          <li><strong>Full listing lifecycle mapped</strong>: Request Submitted &rarr; Under Review &rarr; Active &rarr; Price Reduced &rarr; Pending Offer &rarr; Closed. Six stages, each with defined gate requirements before status can advance.</li>
          <li><strong>FastField Listing Request Form</strong>: CM-completed (15 fields across 5 sections). This fires when WF002 Rehab is complete or when WF003 TBD Process sets disposition = Turn for Sale.</li>
          <li><strong>Leslie and Tanya own the review step</strong> and set Official Price, Listing Date, and Listed By directly in QB. A gate rule enforces this: no status change to Active is allowed until both Official Price and Listing Date are entered.</li>
          <li><strong>Price is frozen while Pending Offer</strong>: gate rule blocks any listing changes while an offer is in review. Protects the offer process from mid-review edits.</li>
          <li><strong>RM sync</strong>: active listing data pushes daily at 6 PM ET to RM via batch CSV to RM User Defined Fields (UDFs).</li>
          <li>QB record IDs: Listing Records use <em>LST-YYYY-###</em>; Price History records use <em>PH-YYYY-###</em>.</li>
        </ul>
      </div>
      <div class="w0-open-items">
        <div class="w0-open-title">&#9888;&nbsp; 5 Open Items &mdash; Need Answers Before This Can Lock</div>
        <div class="w0-open-list">
          <div class="w0-open-item"><span class="open-id">O-WF006-001</span>Listing platforms &mdash; which platforms listings go live on (MHVillage, Zillow, Craigslist, etc.)</div>
          <div class="w0-open-item"><span class="open-id">O-WF006-002</span>RM UDF field names &mdash; exact names of the RM User Defined Fields that receive the daily sync</div>
          <div class="w0-open-item"><span class="open-id">O-WF006-003</span>RM Listing Status allowed values &mdash; what values RM accepts in the Listing Status field</div>
          <div class="w0-open-item"><span class="open-id">O-WF006-004</span>SharePoint folder structure &mdash; where photos and marketing materials are stored per listing</div>
          <div class="w0-open-item"><span class="open-id">O-WF006-005</span>Listing review SLA &mdash; how long Leslie / Tanya have to act on a new request before escalation</div>
        </div>
      </div>
    </div>
  </div>

  <!-- WHAT'S NEXT CALLOUT -->
  <div class="next-callout">
    <div class="next-callout-header">
      <div class="next-callout-flag">&#9650;</div>
      <div class="next-callout-title">What We Need to Resolve Before Wave 1 Can Begin</div>
    </div>
    <p class="next-callout-desc">WF004 (Move Out) and WF006 (Listings) each have 5 open items &mdash; 10 total. These are not design problems, they&rsquo;re information gaps: specific decisions that need answers from the team. <strong>WF004 must lock before Wave 1</strong> (Resident Lifecycle) can be built, because WF005 Move In is triggered directly by a completed Move Out. <strong>WF006 needs to lock before Wave 2</strong> (Asset Sales Pipeline) begins, since Wave 2 picks up exactly where Listings hands off.</p>
    <div class="next-items-grid">
      <div>
        <div class="next-items-block-title">WF004 &mdash; Move Out (5 items)</div>
        <div class="next-item-row"><span class="ni-id">O-WF004-001</span>RM column mapping for daily sync</div>
        <div class="next-item-row"><span class="ni-id">O-WF004-002</span>Move-out inspection checklist line items</div>
        <div class="next-item-row"><span class="ni-id">O-WF004-003</span>FastField approval chain configuration</div>
        <div class="next-item-row"><span class="ni-id">O-WF004-004</span>SharePoint destination folder path</div>
        <div class="next-item-row"><span class="ni-id">O-WF004-005</span>Rejected form correction / resubmission flow</div>
      </div>
      <div>
        <div class="next-items-block-title">WF006 &mdash; Listings (5 items)</div>
        <div class="next-item-row"><span class="ni-id">O-WF006-001</span>Listing platform destinations</div>
        <div class="next-item-row"><span class="ni-id">O-WF006-002</span>RM UDF field names for daily sync</div>
        <div class="next-item-row"><span class="ni-id">O-WF006-003</span>RM Listing Status allowed values</div>
        <div class="next-item-row"><span class="ni-id">O-WF006-004</span>SharePoint marketing folder structure</div>
        <div class="next-item-row"><span class="ni-id">O-WF006-005</span>Listing review SLA (Leslie / Tanya)</div>
      </div>
    </div>
  </div>

"""

# Insert before the GUIDING PRINCIPLES comment
insertion_target = '  <!-- GUIDING PRINCIPLES -->'
if insertion_target in html:
    html = html.replace(insertion_target, new_section + insertion_target, 1)
    print("Section inserted successfully.")
else:
    print("ERROR: insertion target not found!")

with open('/home/ubuntu/parakeet_rollout_overview_v1.1.html', 'w') as f:
    f.write(html)

print("File written: parakeet_rollout_overview_v1.1.html")

# Quick sanity check
with open('/home/ubuntu/parakeet_rollout_overview_v1.1.html', 'r') as f:
    content = f.read()
print(f"File length: {len(content)} chars")
print(f"WF001 card present: {'w0-locked' in content}")
print(f"WF004 open items present: {'O-WF004-001' in content}")
print(f"WF006 open items present: {'O-WF006-001' in content}")
print(f"Next callout present: {'next-callout' in content}")
