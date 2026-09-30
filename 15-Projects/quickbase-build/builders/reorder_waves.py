"""
Reorder waves in parakeet_master_build_gameplan_v1.0.html
New order: Wave 2 (Revenue Protection) moves AFTER Wave 5 (Compliance)

Old:  Wave 1 | Wave 2 (Collections) | Wave 3 (Asset Sales) | Wave 4 (Field Ops) | Wave 5 (Compliance)
New:  Wave 1 | Wave 2 (Asset Sales) | Wave 3 (Field Ops)   | Wave 4 (Compliance) | Wave 5 (Collections)

Waves 6, 7, 8 unchanged.
"""

with open('/home/ubuntu/parakeet_master_build_gameplan_v1.0.html', 'r') as f:
    html = f.read()

# ─── STEP 1: Extract & reorder the wave card sections ────────────────────────
# Boundaries are the <!-- WAVE N --> comments

w2_start = html.index('<!-- WAVE 2 -->')
w3_start = html.index('<!-- WAVE 3 -->')
w4_start = html.index('<!-- WAVE 4 -->')
w5_start = html.index('<!-- WAVE 5 -->')
w6_start = html.index('<!-- WAVE 6 -->')

before_w2 = html[:w2_start]
wave2_raw  = html[w2_start:w3_start]   # Revenue Protection → becomes Wave 5
wave3_raw  = html[w3_start:w4_start]   # Asset Sales        → becomes Wave 2
wave4_raw  = html[w4_start:w5_start]   # Field Ops          → becomes Wave 3
wave5_raw  = html[w5_start:w6_start]   # Compliance         → becomes Wave 4
after_w5   = html[w6_start:]

# Helper: update the wave-card class, badge number, and comment label inside a section
def rebadge(section, old_n, new_n):
    s = old_n; t = new_n
    section = section.replace(f'<!-- WAVE {s} -->', f'<!-- WAVE {t} -->', 1)
    section = section.replace(f'wave-card wave-{s}', f'wave-card wave-{t}', 1)
    section = section.replace(f'<span class="wlabel">{s}</span>', f'<span class="wlabel">{t}</span>', 1)
    return section

# Update the W-meta "Can run in parallel with Wave 4" (inside old Wave 5, now Wave 4)
# Old Wave 5 meta references "Wave 4" (which is now Wave 3)
wave5_raw = wave5_raw.replace(
    'Can run in parallel with Wave 4',
    'Can run in parallel with Wave 3'
)
# Old Wave 5 rationale: "making them a natural parallel track to Wave 4"
wave5_raw = wave5_raw.replace(
    'natural parallel track to Wave 4.',
    'natural parallel track to Wave 3.'
)
# Old Wave 5 rationale: "can be designed in Wave 5 once Wave 1"
wave5_raw = wave5_raw.replace(
    'can be designed in Wave 5 once Wave 1',
    'can be designed in Wave 4 once Wave 1'
)

wave2_new = rebadge(wave2_raw, '2', '5')   # Revenue Protection → Wave 5
wave3_new = rebadge(wave3_raw, '3', '2')   # Asset Sales        → Wave 2
wave4_new = rebadge(wave4_raw, '4', '3')   # Field Ops          → Wave 3
wave5_new = rebadge(wave5_raw, '5', '4')   # Compliance         → Wave 4

# Assemble reordered HTML
html = before_w2 + wave3_new + wave4_new + wave5_new + wave2_new + after_w5

# ─── STEP 2: Update wave-label classes + text in tables ──────────────────────
# Use temp tokens to avoid collision during multi-step replace
# Old wave-label-2 → new wave-label-5  (Revenue Protection rows)
# Old wave-label-3 → new wave-label-2  (Asset Sales rows)
# Old wave-label-4 → new wave-label-3  (Field Ops rows)
# Old wave-label-5 → new wave-label-4  (Compliance rows)

html = html.replace('class="wave-label-2">Wave 2<', 'class="wave-label-TMP2">Wave TMP2<')
html = html.replace('class="wave-label-3">Wave 3<', 'class="wave-label-TMP3">Wave TMP3<')
html = html.replace('class="wave-label-4">Wave 4<', 'class="wave-label-TMP4">Wave TMP4<')
html = html.replace('class="wave-label-5">Wave 5<', 'class="wave-label-TMP5">Wave TMP5<')

html = html.replace('class="wave-label-TMP2">Wave TMP2<', 'class="wave-label-5">Wave 5<')
html = html.replace('class="wave-label-TMP3">Wave TMP3<', 'class="wave-label-2">Wave 2<')
html = html.replace('class="wave-label-TMP4">Wave TMP4<', 'class="wave-label-3">Wave 3<')
html = html.replace('class="wave-label-TMP5">Wave TMP5<', 'class="wave-label-4">Wave 4<')

# ─── STEP 3: Update narrative text references ────────────────────────────────

# Foundation principles: "are Wave 2 — right after..."
html = html.replace(
    'the Eviction Pipeline are Wave 2 &mdash; right after the resident lifecycle workflows that create the data',
    'the Eviction Pipeline are Wave 5 &mdash; building on the field and compliance workflows the team already knows'
)

# "The system needs to protect revenue before it optimizes field operations."
# This no longer reflects the new priority reasoning — update to match new rationale
html = html.replace(
    'A single 30-day delay in an eviction pipeline due to missing documentation or missed cure period deadlines can cost $1,500&ndash;$3,000 in lost rent plus legal fees. The system needs to protect revenue before it optimizes field operations.',
    'Field-team adoption is highest when the system supports daily work first. Revenue protection workflows (collections, stipulations, evictions) are still built before Waves 6&ndash;8, giving the legal and accounting teams a fully integrated system once the field layer is established.'
)

# Wave 0 section: "WF006 (Listings) feeds into Wave 3 (Offer to Purchase / WF007)"
html = html.replace(
    'WF006 (Listings) feeds into Wave 3 (Offer to Purchase / WF007)',
    'WF006 (Listings) feeds into Wave 2 (Offer to Purchase / WF007)'
)

# Wave plan intro: "A workflow in Wave 3 cannot be specced until all Wave 1 and Wave 2 workflows"
html = html.replace(
    'A workflow in Wave 3 cannot be specced until all Wave 1 and Wave 2 workflows are at least in draft, because Wave 3 workflows reference records created by Wave 1&ndash;2.',
    'A workflow in Wave 2 cannot be specced until all Wave 1 workflows are at least in draft. Waves are not calendar weeks &mdash; they are logical dependency layers.'
)

# Wave 6 meta: "Depends on Wave 1 (resident data) & Wave 3 (sale data)"
html = html.replace(
    'Depends on Wave 1 (resident data) &amp; Wave 3 (sale data)',
    'Depends on Wave 1 (resident data) &amp; Wave 2 (sale data)'
)

# Wave 6 rationale: "Build Wave 6 once Wave 1 and Wave 3 are functional"
html = html.replace(
    'Build Wave 6 once Wave 1 and Wave 3 are functional.',
    'Build Wave 6 once Wave 1 and Wave 2 are functional.'
)

# Wave 7 meta: "Can begin speccing in parallel with Wave 5/6"
html = html.replace(
    'Can begin speccing in parallel with Wave 5/6',
    'Can begin speccing in parallel with Wave 4/6'
)

# Wave 7 rationale: "Waves 5–6"
html = html.replace(
    'Wave 7 can be designed in parallel with Waves 5&ndash;6',
    'Wave 7 can be designed in parallel with Waves 4&ndash;6'
)

# Open Items section header
html = html.replace('Wave 2 Design Inputs Needed', 'Wave 5 Design Inputs Needed')

# "Wave 3–8 Advisory Items" (keep as-is since it's a catch-all label — adjust to 2–8)
html = html.replace('Wave 3&ndash;8 Advisory Items', 'Wave 2&ndash;8 Advisory Items')

# ─── STEP 4: Update document version & title ─────────────────────────────────
html = html.replace(
    'Master QB + FastField Build Gameplan v1.0',
    'Master QB + FastField Build Gameplan v1.1'
)
html = html.replace(
    'Build Gameplan &mdash; v1.0',
    'Build Gameplan &mdash; v1.1'
)
# Date/version meta rows
html = html.replace('>v1.0<', '>v1.1<')
html = html.replace('"v1.0"', '"v1.1"')

# ─── STEP 5: Write output ────────────────────────────────────────────────────
out_path = '/home/ubuntu/parakeet_master_build_gameplan_v1.1.html'
with open(out_path, 'w') as f:
    f.write(html)

# Quick verification
import re
wave_labels = re.findall(r'wave-label-(\d+)">Wave (\d+)', html)
mismatch = [(c, t) for c, t in wave_labels if c != t]
print(f"Total wave-label references: {len(wave_labels)}")
print(f"Mismatches (class≠text): {mismatch}")
print(f"Output size: {len(html):,} bytes")
print(f"Written to: {out_path}")
