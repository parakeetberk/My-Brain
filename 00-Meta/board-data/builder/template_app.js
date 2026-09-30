"use strict";
/* The Open Board — rendered from data so the page can republish itself.
   Comment lifecycle: pending (this browser only) -> open (saved into the
   published page) -> actioned (Claude wrote it into the register). */

var BOARD = JSON.parse(document.getElementById("board").textContent);
var ROWS = BOARD.rows, META = BOARD.meta;
var COM = BOARD.comments || {};          /* id -> [{ts,text,state}] */
var DRAFT_KEY = "openboard.pending.v1";
var EDIT_KEY = "openboard.edits.v1";
var FLAG_KEY = "openboard.flags.v1";
var VIEW_KEY = "openboard.view.v1";

/* ---------- pending comments kept out of the published data ---------- */
var PEND = {};
try {
  var raw = localStorage.getItem(DRAFT_KEY);
  if (raw) PEND = JSON.parse(raw) || {};
} catch (e) { PEND = {}; }
function savePend() {
  try {
    if (Object.keys(PEND).length) localStorage.setItem(DRAFT_KEY, JSON.stringify(PEND));
    else localStorage.removeItem(DRAFT_KEY);
  } catch (e) {}
}
function pendCount() { var n = 0; for (var k in PEND) n += PEND[k].length; return n; }

/* ---- field corrections: same three states as comments ---- */
var EDITS = BOARD.edits || {};          /* id -> {field: {from,to,ts,state}} */
var PEDIT = {};                          /* pending, this browser only */
try { PEDIT = JSON.parse(localStorage.getItem(EDIT_KEY) || "{}") || {}; } catch (e) { PEDIT = {}; }
function saveEdits() {
  try {
    if (Object.keys(PEDIT).length) localStorage.setItem(EDIT_KEY, JSON.stringify(PEDIT));
    else localStorage.removeItem(EDIT_KEY);
  } catch (e) {}
}
/* ---- flags: a tick that puts a row on a named list ---- */
var FLAGS = BOARD.flags || {};           /* id -> {flag: {ts,state}} */
var PFLAG = {};
try { PFLAG = JSON.parse(localStorage.getItem(FLAG_KEY) || "{}") || {}; } catch (e) { PFLAG = {}; }
function saveFlags() {
  try {
    if (Object.keys(PFLAG).length) localStorage.setItem(FLAG_KEY, JSON.stringify(PFLAG));
    else localStorage.removeItem(FLAG_KEY);
  } catch (e) {}
}
var FLAGDEFS = (META.flags || [{ key: "budget", label: "Budget week", short: "BW" }]);
function flagOf(id, k) {
  var a = (PFLAG[id] || {})[k], b = (FLAGS[id] || {})[k];
  return a || b || null;
}
function flagOn(id, k) { var f = flagOf(id, k); return !!f && f.state !== "removed"; }
function flagCount() { var n = 0; for (var id in PFLAG) n += Object.keys(PFLAG[id]).length; return n; }
function setFlag(id, k, on) {
  var cur = flagOn(id, k);
  if (on === cur) return;
  var saved = (FLAGS[id] || {})[k];
  if (saved && (saved.state !== "removed") === on) { delete (PFLAG[id] || {})[k];
    if (PFLAG[id] && !Object.keys(PFLAG[id]).length) delete PFLAG[id]; }
  else (PFLAG[id] = PFLAG[id] || {})[k] = { ts: stamp(), state: on ? "pending" : "removed" };
  saveFlags(); refreshRow(id);
}
function openFlags() {
  var out = [];
  ROWS.forEach(function (r) {
    FLAGDEFS.forEach(function (d) {
      var f = flagOf(r.id, d.key);
      if (f && f.state === "pending") out.push([r.id, d.label, "on"]);
      else if (f && f.state === "removed" && (FLAGS[r.id] || {})[d.key]) out.push([r.id, d.label, "off"]);
    });
  });
  return out;
}
var FIELDS = [["priority", "Priority"], ["category", "Category"],
              ["community", "Community"], ["owner_short", "Owner"],
              ["due", "Due date"], ["cost", "Est. cost"]];
var FIELD_TYPE = { due: "date", cost: "text" };
function editOf(id, f) {
  var a = (PEDIT[id] || {})[f], b = (EDITS[id] || {})[f];
  return a || b || null;
}
function shown(r, f) {
  var e = editOf(r.id, f);
  return e && e.state !== "actioned" ? e.to : (r[f] || "");
}
function editCount() {
  var n = 0;
  for (var id in PEDIT) n += Object.keys(PEDIT[id]).length;
  return n;
}
function openEdits() {
  var out = [];
  ROWS.forEach(function (r) {
    FIELDS.forEach(function (f) {
      var e = editOf(r.id, f[0]);
      if (e && e.state !== "actioned") out.push([r.id, f[1], e.from || "(blank)", e.to || "(blank)"]);
    });
  });
  return out;
}
function setEdit(id, f, to) {
  var r = rowById(id); if (!r) return;
  var cur = shown(r, f);
  if (to === cur) return;
  (PEDIT[id] = PEDIT[id] || {})[f] = { from: r[f] || "", to: to, ts: stamp(), state: "pending" };
  saveEdits(); refreshRow(id);
}
function rowById(id) {
  for (var i = 0; i < ROWS.length; i++) if (ROWS[i].id === id) return ROWS[i];
  return null;
}
function allFor(id) { return (COM[id] || []).concat(PEND[id] || []); }
function openFor(id) {
  /* a Claude reply is not something Austin owes anyone, so it never counts as
     open and never lands on the clipboard. */
  return allFor(id).filter(function (c) {
    return c.state !== "actioned" && c.state !== "reply" && c.by !== "claude";
  });
}

function trim(s, n) {
  s = String(s || "");
  if (s.length <= n) return s;
  var cut = s.slice(0, n), sp = cut.lastIndexOf(" ");
  return (sp > n * 0.6 ? cut.slice(0, sp) : cut) + "\u2026";
}
function esc(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
  });
}
function stamp() {
  var d = new Date(), p = function (n) { return (n < 10 ? "0" : "") + n; };
  return d.getFullYear() + "-" + p(d.getMonth() + 1) + "-" + p(d.getDate()) +
         " " + p(d.getHours()) + ":" + p(d.getMinutes());
}

var PCLASS = { "Critical (stated)": "p-crit", "Awaiting your ruling": "p-rule",
  "High (stated)": "p-high", "High (ledger)": "p-high", "Blocked": "p-blok",
  "Decided, never actioned": "p-dna", "Open": "p-open", "Closed": "p-clos" };
var PLABEL = { "Critical (stated)": "Critical", "Awaiting your ruling": "Your ruling",
  "High (stated)": "High", "High (ledger)": "High", "Blocked": "Blocked",
  "Decided, never actioned": "Not done", "Open": "Open", "Closed": "Closed" };
var PORDER = ["Critical (stated)", "Awaiting your ruling", "High (stated)", "High (ledger)",
  "Blocked", "Decided, never actioned", "Open", "Closed"];

/* ---------------------------- render ---------------------------- */
function counts(field) {
  var c = {};
  ROWS.forEach(function (r) { var v = r[field]; if (v) c[v] = (c[v] || 0) + 1; });
  return c;
}
function ownerCounts() {
  /* every name on Austin's list appears even at zero rows, so a row can be
     assigned to someone who owns nothing yet. */
  var c = counts("owner_short");
  ((META.opts && META.opts.owner_short) || []).forEach(function (k) { if (!(k in c)) c[k] = 0; });
  return c;
}
function msel(id, label, c, order, keepZero) {
  var keys = (order || Object.keys(c).sort()).filter(function (k) { return keepZero || c[k]; });
  var boxes = keys.map(function (k) {
    return '<label><input type="checkbox" value="' + esc(k) + '"><span>' + esc(k) +
           "</span><i>" + c[k] + "</i></label>";
  }).join("");
  return '<div class="ms" id="' + id + '"><button type="button" class="ms__btn">' + esc(label) +
    ' <span class="ms__sel">all</span><span class="ms__car"></span></button>' +
    '<div class="ms__panel" hidden><div class="ms__tools">' +
    '<button type="button" class="ms__all">All</button>' +
    '<button type="button" class="ms__none">None</button></div>' + boxes + "</div></div>";
}
var TODAY = new Date().toISOString().slice(0, 10);
function chipCell(r, f, cls, render, empty) {
  var e = editOf(r.id, f), v = shown(r, f);
  var st = e ? (e.state === "actioned" ? " ed-done" : (e.state === "open" ? " ed-open" : " ed-pend")) : "";
  return '<span class="chip ef ' + cls + st + (v ? "" : " chip-empty") + '" data-ef="' + esc(r.id) +
         '" data-f="' + f + '" title="' + esc((f === "due" ? "Due date" : "Est. cost") + " - click to set") +
         '">' + (v ? render(v) : empty) + "</span>";
}
function chips(r) {
  var due = shown(r, "due");
  var out = chipCell(r, "due", (due && due < TODAY ? "over" : "due"),
                     function (v) { return "due " + esc(v); }, "+ due");
  out += chipCell(r, "cost", "cost", function (v) { return esc(v); }, "+ cost");
  if (r.person) out += '<span class="chip who">to ' + esc(r.person) + "</span>";
  return out;
}
function fieldCell(r, f, label, cls) {
  var e = editOf(r.id, f), v = shown(r, f);
  var st = e ? (e.state === "actioned" ? " ed-done" : (e.state === "open" ? " ed-open" : " ed-pend")) : "";
  return '<span class="ef' + st + " " + (cls || "") + '" data-ef="' + esc(r.id) + '" data-f="' + f +
         '" title="' + esc(label + (e ? ": was " + (e.from || "blank") : "") + " - click to change") + '">' +
         (v ? esc(v) : '<em class="blank">set ' + esc(label.toLowerCase()) + "</em>") + "</span>";
}
function flagCell(r) {
  return FLAGDEFS.map(function (d) {
    var f = flagOf(r.id, d.key), on = flagOn(r.id, d.key);
    var st = f ? (f.state === "pending" || f.state === "removed" ? " fl-pend" : " fl-set") : "";
    return '<label class="fl' + st + '" title="' + esc(d.label) + '"><input type="checkbox" data-fl="' +
      esc(r.id) + '" data-k="' + esc(d.key) + '"' + (on ? " checked" : "") + '><span>' + esc(d.short) + "</span></label>";
  }).join("");
}
function rowHTML(r, i) {
  var open = openFor(r.id), pend = (PEND[r.id] || []).length, tot = allFor(r.id).length;
  var cls = "row" + (pend ? " haspend" : (tot ? " hascom" : ""));
  var cb = '<button class="cbtn' + (pend ? " pend" : (tot ? " has" : "")) + '" data-c="' + esc(r.id) +
    '">Comment' + (tot ? " <i>" + tot + "</i>" : "") + "</button>";
  var src = '<button class="cpq" data-q="' + esc(r.q || "") + '">Copy search</button>' + cb;
  if (r.srcurl) src += '<a class="slink" href="' + esc(r.srcurl) + '" target="_blank" rel="noopener">source</a>';
  src += '<a class="sreg" href="' + esc(r.regurl) + '">register</a>';
  src += '<span class="age">' + (r.age ? r.age + "d" : "&mdash;") + "</span>";
  return '<div class="' + cls + '" data-i="' + i + '">' +
    '<div class="flg">' + flagCell(r) + "</div>" +
    '<div><span class="rid" title="Click to copy">' + esc(r.id) + "</span></div>" +
    '<div>' + (function () {
       var p = shown(r, "priority"), e = editOf(r.id, "priority");
       var st = e ? (e.state === "actioned" ? " ed-done" : (e.state === "open" ? " ed-open" : " ed-pend")) : "";
       return '<span class="pill ef' + st + " " + (PCLASS[p] || "p-open") + '" data-ef="' + esc(r.id) +
              '" data-f="priority" title="Priority - click to change">' + esc(PLABEL[p] || p) + "</span>";
     })() + "</div>" +
    '<div><div class="desc">' + esc(trim(r.desc, 230)) + '</div><div class="meta">' +
      fieldCell(r, "category", "Category") + " &middot; " + esc((r.state || "open").slice(0, 78)) +
      (r.lot ? " &middot; " + esc(r.lot) : "") + chips(r) + "</div></div>" +
    '<div class="com">' + fieldCell(r, "community", "Community") + "</div>" +
    '<div class="own">' + fieldCell(r, "owner_short", "Owner") + "</div>" +
    '<div class="srcs">' + src + "</div></div>";
}
function render() {
  var byReg = {}, regOrder = [];
  ROWS.forEach(function (r, i) {
    if (!byReg[r.reg]) { byReg[r.reg] = {}; regOrder.push(r.reg); }
    var s = r.sec || "Unfiled";
    (byReg[r.reg][s] = byReg[r.reg][s] || []).push(i);
  });
  var h = [];
  h.push('<p class="eyebrow">Parakeet Communities &middot; every open item &middot; ' + esc(META.built) + "</p>");
  h.push("<h1>" + META.total + " items, every one with an ID you can quote back to me.</h1>");
  h.push('<p class="lede">All six registers on one page. <b>' + META.open + " open, " + META.unowned +
    " with nobody's name on them.</b> Comment on any row, or correct its priority, category, community or owner in place. Everything you change is kept here, date stamped, until it lands in the register.</p>");
  h.push(META.how || "");
  h.push('<div class="stats">' +
    '<div class="stat"><b>' + META.open + "</b><span>Open right now</span></div>" +
    '<div class="stat"><b style="color:var(--red)">' + META.unowned + "</b><span>No owner</span></div>" +
    '<div class="stat"><b style="color:var(--red)">' + META.hot + "</b><span>Critical, or waiting on your ruling</span></div>" +
    '<div class="stat"><b style="color:var(--green)">' + META.closed + "</b><span>Closed and kept visible</span></div>" +
    '<div class="stat"><b id="bwtot">0</b><span>Flagged for budget week</span></div>' +
    '<div class="stat"><b id="cmtot">0</b><span>Comments and corrections</span></div></div>');
  h.push('<div class="bar"><div class="bar__row">' +
    '<input type="search" id="q" placeholder="Search text, owner, or an ID like PF-0324&hellip;" autocomplete="off">' +
    msel("fp", "Priority", counts("priority"), PORDER) +
    msel("fc", "Category", counts("category")) +
    msel("fm", "Community", counts("community")) +
    msel("fo", "Owner", ownerCounts(), (META.opts && META.opts.owner_short) || null, true) +
    '<label class="tog"><input type="checkbox" id="fu"> Unassigned only</label>' +
    '<label class="tog"><input type="checkbox" id="fk"> Commented only</label>' +
    '<label class="tog"><input type="checkbox" id="fdd"> Has a date</label>' +
    '<label class="tog"><input type="checkbox" id="fcc"> Has a cost</label>' +
    '<label class="tog"><input type="checkbox" id="fbw"> Budget week only</label>' +
    '<button class="btn" id="reset">Reset</button>' +
    '<button class="btn" id="expand">Expand all</button>' +
    '<span class="count" id="count"><b>' + ROWS.length + "</b> shown</span></div>" +
    '<p class="barnote">Every filter takes more than one value. Within a filter they are OR, across filters they are AND.</p></div>');
  h.push('<div id="warn"></div>');
  regOrder.forEach(function (reg) {
    var secs = byReg[reg], ids = [], n = 0;
    Object.keys(secs).forEach(function (s) { secs[s].forEach(function (i) { ids.push(ROWS[i].id); n++; }); });
    ids.sort();
    h.push('<details class="reg"' + (n <= 40 ? " open" : "") + '><summary><span class="caret"></span>' +
      '<span class="rtitle">' + esc(reg) + '</span><span class="rsub">' + esc(META.subs[reg] || "") +
      " &middot; IDs " + esc(ids[0]) + " to " + esc(ids[ids.length - 1]) +
      '</span><span class="rn" data-rn>' + n + "</span></summary>");
    var keys = Object.keys(secs), multi = keys.length > 1;
    keys.forEach(function (s) {
      if (multi) h.push('<details class="sub"><summary><span class="caret"></span><span class="stitle">' +
        esc(s) + '</span><span class="rn" data-rn>' + secs[s].length + "</span></summary>");
      secs[s].forEach(function (i) { h.push(rowHTML(ROWS[i], i)); });
      if (multi) h.push("</details>");
    });
    h.push("</details>");
  });
  h.push('<div class="empty" id="none" hidden>Nothing matches those filters.</div>');
  h.push("<footer><p>" + esc(META.footer) + "</p></footer>");
  h.push('<div class="savebar" id="savebar" hidden></div>');
  document.getElementById("app").innerHTML = h.join("");
}

/* ---------------------------- filters ---------------------------- */
var rowEls, hay, MS, q, fu, fk, fdd, fcc, fbw, cnt, none;
function wireFilters() {
  rowEls = [].slice.call(document.querySelectorAll(".row"));
  hay = ROWS.map(function (x) {
    return (x.id + " " + x.desc + " " + (x.notes || "") + " " + x.owner_full + " " + x.category + " " + x.community +
      " " + x.sec + " " + x.lot + " " + x.state + " " + x.srctype +
      " " + (x.person || "") + " " + (x.due || "") + " " + (x.cost || "")).toLowerCase();
  });
  q = document.getElementById("q"); fu = document.getElementById("fu");
  fk = document.getElementById("fk"); cnt = document.getElementById("count");
  fdd = document.getElementById("fdd"); fcc = document.getElementById("fcc");
  fbw = document.getElementById("fbw");
  none = document.getElementById("none");
  var FIELD = { fp: "priority", fc: "category", fm: "community", fo: "owner_short" };
  MS = [].slice.call(document.querySelectorAll(".ms")).map(function (el) {
    return { el: el, field: FIELD[el.id], btn: el.querySelector(".ms__btn"),
      panel: el.querySelector(".ms__panel"), sel: el.querySelector(".ms__sel"),
      boxes: [].slice.call(el.querySelectorAll("input[type=checkbox]")) };
  });
  function lab(m) {
    var c = m.boxes.filter(function (b) { return b.checked; });
    m.sel.textContent = c.length === 0 ? "all" : (c.length === 1 ? c[0].value : c.length + " selected");
    m.el.classList.toggle("on", c.length > 0);
  }
  function closeAll(x) { MS.forEach(function (m) { if (m !== x) m.panel.hidden = true; }); }
  MS.forEach(function (m) {
    m.btn.addEventListener("click", function (ev) {
      ev.stopPropagation(); var o = m.panel.hidden; closeAll(m); m.panel.hidden = !o;
    });
    m.panel.addEventListener("click", function (ev) { ev.stopPropagation(); });
    m.boxes.forEach(function (b) { b.addEventListener("change", function () { lab(m); apply(); }); });
    m.el.querySelector(".ms__all").addEventListener("click", function () {
      m.boxes.forEach(function (b) { b.checked = true; }); lab(m); apply(); });
    m.el.querySelector(".ms__none").addEventListener("click", function () {
      m.boxes.forEach(function (b) { b.checked = false; }); lab(m); apply(); });
    lab(m);
  });
  document.addEventListener("click", function () { closeAll(null); });
  [q, fu, fk, fdd, fcc, fbw].forEach(function (el) { el.addEventListener("input", apply); });
  document.getElementById("reset").onclick = function () {
    q.value = ""; fu.checked = false; fk.checked = false; fdd.checked = false; fcc.checked = false; fbw.checked = false;
    MS.forEach(function (m) { m.boxes.forEach(function (b) { b.checked = false; }); lab(m); m.panel.hidden = true; });
    document.querySelectorAll("details.sub").forEach(function (s) { s.open = false; });
    apply();
  };
  var exp = false;
  document.getElementById("expand").onclick = function (ev) {
    exp = !exp; document.querySelectorAll("details").forEach(function (s) { s.open = exp; });
    ev.target.textContent = exp ? "Collapse all" : "Expand all";
  };
}
function apply() {
  var t = q.value.trim().toLowerCase(), u = fu.checked, k = fk.checked,
      dd = fdd.checked, cc = fcc.checked, bw = fbw.checked;
  var sets = MS.map(function (m) {
    return [m.field, m.boxes.filter(function (b) { return b.checked; }).map(function (b) { return b.value; })];
  }).filter(function (p) { return p[1].length; });
  var n = 0;
  rowEls.forEach(function (r) {
    var i = +r.dataset.i, x = ROWS[i];
    var ok = (!t || hay[i].indexOf(t) >= 0) && (!u || x.owner_short === "Unassigned") &&
             (!k || allFor(x.id).length > 0) && (!dd || !!x.due) && (!cc || !!x.cost) &&
             (!u || shown(x, "owner_short") === "Unassigned") &&
             (!bw || flagOn(x.id, "budget"));
    if (ok) for (var j = 0; j < sets.length; j++) {
      if (sets[j][1].indexOf(shown(x, sets[j][0])) < 0) { ok = false; break; }
    }
    r.hidden = !ok; if (ok) n++;
  });
  var act = t || u || k || dd || cc || bw || sets.length > 0;
  document.querySelectorAll("details.sub").forEach(function (s) {
    var v = [].slice.call(s.querySelectorAll(".row")).filter(function (r) { return !r.hidden; }).length;
    s.hidden = v === 0; s.querySelector("[data-rn]").textContent = v; if (v && act) s.open = true;
  });
  document.querySelectorAll("details.reg").forEach(function (s) {
    var v = [].slice.call(s.querySelectorAll(".row")).filter(function (r) { return !r.hidden; }).length;
    s.hidden = v === 0; s.querySelector("summary [data-rn]").textContent = v; if (v && act) s.open = true;
  });
  cnt.innerHTML = "<b>" + n + "</b> shown"; none.hidden = n > 0;
}

/* ---------------------------- clipboard ---------------------------- */
function copy(s) {
  try { navigator.clipboard.writeText(s); } catch (e) {
    var t = document.createElement("textarea"); t.value = s;
    document.body.appendChild(t); t.select();
    try { document.execCommand("copy"); } catch (_) {} t.remove();
  }
}
function flash(el, txt) {
  var o = el.innerHTML; el.classList.add("copied"); el.textContent = txt;
  setTimeout(function () { el.classList.remove("copied"); el.innerHTML = o; }, 900);
}
var toastT;
function toast(msg) {
  var el = document.getElementById("toast");
  if (!el) { el = document.createElement("div"); el.id = "toast"; el.className = "toast"; document.body.appendChild(el); }
  el.textContent = msg; el.hidden = false;
  clearTimeout(toastT); toastT = setTimeout(function () { el.hidden = true; }, 3200);
}

/* ---------------------------- the modal ---------------------------- */
var openId = null;
var CBUF = [];
function commentHTML(c, id, idx, isPend) {
  var mine = c.by === "claude" || c.state === "reply";
  CBUF.push(c.text);
  return '<div class="cm st-' + esc(mine ? "reply" : c.state) + '"><div class="cmh">' +
    '<span class="cmt">' + esc(c.ts) + '</span>' +
    '<span class="cms">' + esc(mine ? "Claude" : c.state) + "</span>" +
    (mine ? '<button class="cmcopy" data-cc="' + (CBUF.length - 1) + '">copy</button>' : "") +
    (isPend ? '<button class="cmdel" data-del="' + idx + '">remove</button>' : "") +
    '</div><div class="cmb">' + esc(c.text) + "</div></div>";
}
function openModal(id) {
  var r = null;
  for (var i = 0; i < ROWS.length; i++) if (ROWS[i].id === id) { r = ROWS[i]; break; }
  if (!r) return;
  openId = id;
  CBUF = [];
  var saved = COM[id] || [], pend = PEND[id] || [];
  var log = saved.map(function (c) { return commentHTML(c, id, -1, false); }).join("") +
            pend.map(function (c, k) { return commentHTML(c, id, k, true); }).join("");
  if (!log) log = '<p class="nocm">No comments yet on this item.</p>';
  var m = document.createElement("div");
  m.className = "mask"; m.id = "mask";
  m.innerHTML = '<div class="modal" role="dialog" aria-modal="true">' +
    '<div class="mhead"><span class="rid">' + esc(r.id) + "</span>" +
    '<span class="pill ' + (PCLASS[r.priority] || "p-open") + '">' + esc(PLABEL[r.priority] || r.priority) + "</span>" +
    "<h3>" + esc(trim(r.desc, 320)) + "</h3>" +
    '<button class="mx" id="mclose" aria-label="Close">&times;</button></div>' +
    '<div class="mmeta"><dl>' +
      "<dt>Register</dt><dd>" + esc(r.reg) + " &middot; " + esc(r.sec) + "</dd>" +
      "<dt>Owner</dt><dd>" + esc(r.owner_full || r.owner_short) + "</dd>" +
      "<dt>Status</dt><dd>" + esc(r.state || "open") + "</dd>" +
      (r.person ? "<dt>Promised to</dt><dd>" + esc(r.person) + "</dd>" : "") +
      "<dt>Due</dt><dd>" + chipCell(r, "due", (shown(r, "due") && shown(r, "due") < TODAY ? "over" : "due"),
          function (v) { return esc(v) + (v < TODAY ? " &middot; overdue" : ""); }, "+ set a due date") + "</dd>" +
      "<dt>Est. cost</dt><dd>" + chipCell(r, "cost", "cost", function (v) { return esc(v); }, "+ set a cost") + "</dd>" +
      (r.community ? "<dt>Community</dt><dd>" + esc(r.community) + "</dd>" : "") +
    "</dl></div>" +
    (r.notes ? '<div class="mnotes"><h4>Register notes</h4><p>' + esc(r.notes) + "</p></div>" : "") +
    '<div class="mlog"><h4>Comment history</h4>' + log + "</div>" +
    '<div class="madd"><h4>Add a comment</h4>' +
    '<textarea id="cnew" placeholder="What changed, what you decided, who owns it&hellip;"></textarea>' +
    '<div class="mact"><button class="btn pri" id="cadd">Add comment</button>' +
    '<button class="btn" id="ccopy">Copy this item’s open comments</button>' +
    '<span class="hint">Ctrl or Cmd + Enter to add</span></div></div></div>';
  document.body.appendChild(m);
  var ta = document.getElementById("cnew");
  ta.focus();
  m.addEventListener("click", function (ev) { if (ev.target === m) closeModal(); });
  document.getElementById("mclose").onclick = closeModal;
  document.getElementById("cadd").onclick = addComment;
  document.getElementById("ccopy").onclick = function () {
    var o = openFor(id);
    if (!o.length) { toast("No open comments on " + id + "."); return; }
    copy(o.map(function (c) { return id + ": " + c.text; }).join("\n"));
    toast("Copied " + o.length + " comment" + (o.length > 1 ? "s" : "") + " for " + id + ".");
  };
  ta.addEventListener("keydown", function (ev) {
    if ((ev.metaKey || ev.ctrlKey) && ev.key === "Enter") { ev.preventDefault(); addComment(); }
  });
  m.querySelectorAll("[data-cc]").forEach(function (b) {
    b.onclick = function () { copy(CBUF[+b.dataset.cc] || ""); flash(b, "copied"); };
  });
  m.querySelectorAll("[data-del]").forEach(function (b) {
    b.onclick = function () {
      var k = +b.dataset.del;
      PEND[openId].splice(k, 1);
      if (!PEND[openId].length) delete PEND[openId];
      savePend(); var id2 = openId; closeModal(); refreshRow(id2); openModal(id2);
    };
  });
}
function addComment() {
  var ta = document.getElementById("cnew"), txt = ta.value.trim();
  if (!txt) { ta.focus(); return; }
  (PEND[openId] = PEND[openId] || []).push({ ts: stamp(), text: txt, state: "pending" });
  savePend();
  var id = openId; closeModal(); refreshRow(id); openModal(id);
  toast("Added. Not saved to the page until you hit Save.");
}
function closeModal() {
  var m = document.getElementById("mask");
  if (m) m.remove();
  openId = null;
}
function refreshRow(id) {
  var i = -1;
  for (var k = 0; k < ROWS.length; k++) if (ROWS[k].id === id) { i = k; break; }
  if (i < 0) return;
  var el = document.querySelector('.row[data-i="' + i + '"]');
  if (el) {
    var wrap = document.createElement("div");
    wrap.innerHTML = rowHTML(ROWS[i], i);
    var nu = wrap.firstChild;
    nu.hidden = el.hidden;
    el.parentNode.replaceChild(nu, el);
    rowEls = [].slice.call(document.querySelectorAll(".row"));
  }
  updateBar();
}

/* ---------------------------- save ---------------------------- */
var ART = null, READONLY = false;
function updateBar() {
  var n = pendCount() + editCount() + flagCount(), bar = document.getElementById("savebar");
  var tot = 0; for (var k in COM) tot += COM[k].length; tot += n;
  var el = document.getElementById("cmtot"); if (el) el.textContent = tot;
  var bw = 0; ROWS.forEach(function (r) { if (flagOn(r.id, "budget")) bw++; });
  var bwel = document.getElementById("bwtot"); if (bwel) bwel.textContent = bw;
  if (!n) { bar.hidden = true; bar.innerHTML = ""; return; }
  bar.hidden = false;
  var nc = pendCount(), ne = editCount(), nf = flagCount();
  var what = [];
  if (nc) what.push(nc + " comment" + (nc > 1 ? "s" : ""));
  if (ne) what.push(ne + " correction" + (ne > 1 ? "s" : ""));
  if (nf) what.push(nf + " flag" + (nf > 1 ? "s" : ""));
  bar.innerHTML = "<b>" + what.join(" and ") + " not saved yet</b>" +
    '<span class="sp"></span>' +
    '<button class="btn" id="bdiscard">Discard unsaved</button>' +
    '<button class="btn" id="bcopy">Copy open comments</button>' +
    '<button class="btn pri" id="bsave"' + (READONLY ? " disabled" : "") + ">Save to the page</button>";
  document.getElementById("bcopy").onclick = copyOpen;
  document.getElementById("bdiscard").onclick = function () {
    if (!confirm("Discard " + (pendCount() + editCount() + flagCount()) + " unsaved change(s)?")) return;
    var ids = Object.keys(PEND).concat(Object.keys(PEDIT)).concat(Object.keys(PFLAG));
    PEND = {}; savePend(); PEDIT = {}; saveEdits(); PFLAG = {}; saveFlags(); PFLAG = {}; saveFlags();
    ids.forEach(refreshRow); updateBar(); toast("Unsaved changes discarded.");
  };
  document.getElementById("bsave").onclick = doSave;
}
function copyOpen() {
  var lines = [];
  ROWS.forEach(function (r) {
    openFor(r.id).forEach(function (c) { lines.push(r.id + ": " + c.text); });
  });
  openEdits().forEach(function (e) {
    lines.push(e[0] + ": " + e[1] + " -> " + e[3] + "   (was " + e[2] + ")");
  });
  openFlags().forEach(function (f) {
    lines.push(f[0] + ": " + (f[2] === "on" ? "FLAG " : "UNFLAG ") + f[1]);
  });
  if (!lines.length) { toast("Nothing open to copy."); return; }
  copy(lines.join("\n"));
  toast("Copied " + lines.length + " line" + (lines.length > 1 ? "s" : "") + ". Paste into chat.");
}
function mergeEdits() {
  var out = {};
  for (var k in EDITS) { out[k] = {}; for (var f in EDITS[k]) out[k][f] = EDITS[k][f]; }
  for (var id in PEDIT) {
    out[id] = out[id] || {};
    for (var f2 in PEDIT[id]) {
      var e = PEDIT[id][f2];
      out[id][f2] = { from: e.from, to: e.to, ts: e.ts, state: "open" };
    }
  }
  return out;
}
function mergeFlags() {
  var out = {};
  for (var k in FLAGS) { out[k] = {}; for (var f in FLAGS[k]) out[k][f] = FLAGS[k][f]; }
  for (var id in PFLAG) {
    out[id] = out[id] || {};
    for (var f2 in PFLAG[id]) {
      var e = PFLAG[id][f2];
      if (e.state === "removed") delete out[id][f2];
      else out[id][f2] = { ts: e.ts, state: "open" };
    }
    if (!Object.keys(out[id]).length) delete out[id];
  }
  return out;
}
function mergePending() {
  var out = {};
  for (var k in COM) out[k] = COM[k].slice();
  for (var id in PEND) {
    out[id] = (out[id] || []).concat(PEND[id].map(function (c) {
      return { ts: c.ts, text: c.text, state: "open" };
    }));
  }
  return out;
}
function buildDoc(comments, edits, flags) {
  var b64 = document.getElementById("tpl").textContent.trim();
  var tpl = decodeURIComponent(escape(atob(b64)));
  var data = JSON.stringify({ meta: META, rows: ROWS, comments: comments, edits: edits, flags: flags })
    .replace(/</g, "\\u003c");
  /* markers are assembled at runtime so this source does not itself contain
     them - the builder replaces every literal occurrence in the template. */
  var mT = "__TPL" + "_B64__", mD = "__DATA" + "_JSON__";
  var inner = tpl.replace(mT, function () { return b64; })
                 .replace(mD, function () { return data; });
  return '<!doctype html><html lang="en"><head><meta charset="utf-8">' +
    '<meta name="viewport" content="width=device-width,initial-scale=1"></head><body>' +
    inner + "</body></html>";
}
function doSave() {
  var btn = document.getElementById("bsave");
  if (!ART) { toast("Saving is not available in this view. Use Copy open comments instead."); return; }
  btn.disabled = true; btn.textContent = "Saving…";
  var merged = mergePending(), mergedE = mergeEdits(), mergedF = mergeFlags();
  var doc;
  try { doc = buildDoc(merged, mergedE, mergedF); }
  catch (e) { btn.disabled = false; btn.textContent = "Save to the page"; toast("Could not build the new version: " + e.message); return; }
  try { sessionStorage.setItem(VIEW_KEY, JSON.stringify({ y: window.scrollY })); } catch (e) {}
  ART.publish(doc).then(function () {
    PEND = {}; savePend(); PEDIT = {}; saveEdits(); PFLAG = {}; saveFlags();
    toast("Saved. Reloading to the new version…");
  }).catch(function (err) {
    var code = (err && err.code) || "upstream_error";
    btn.disabled = false; btn.textContent = "Save to the page";
    if (code === "conflict") { toast("Someone else published first. Your comments are kept here; the page is reloading."); return; }
    if (code === "not_writer" || code === "not_granted" || code === "not_declared" ||
        code === "capability_disabled" || code === "capability_removed" || code === "consent_required") {
      READONLY = true; showWarn("This view can read the board but not save to it. Your comments stay in this browser — use <b>Copy open comments</b> to get them out.");
      updateBar(); return;
    }
    if (code === "too_large") { toast("The page is too large to save. Ask Claude to rebuild it."); return; }
    if (code === "rate_limited") { toast("Saving too often. Wait a moment and try again."); return; }
    toast("Save failed (" + code + "). Your comments are still here — use Copy open comments.");
  });
}
function showWarn(html) {
  var w = document.getElementById("warn");
  if (w) w.innerHTML = '<div class="warnbar">' + html + "</div>";
}

/* ---------------------------- boot ---------------------------- */
render();
wireFilters();
updateBar();
apply();

function openInput(el, id, f, cur, kind) {
  var inp = document.createElement("input");
  inp.type = kind === "date" ? "date" : "text";
  inp.className = "efinp";
  inp.value = cur || "";
  if (kind === "text") inp.placeholder = "$0,000";
  var prev = el.innerHTML;
  el.innerHTML = ""; el.appendChild(inp); inp.focus();
  var done = false;
  function close(commit) {
    if (done) return; done = true;
    var v = (inp.value || "").trim();
    if (kind === "text" && v && v.charAt(0) !== "$") v = "$" + v;
    el.innerHTML = prev;
    if (commit && v !== cur) setEdit(id, f, v); else updateBar();
  }
  inp.addEventListener("change", function () { close(true); });
  inp.addEventListener("blur", function () { close(true); });
  inp.addEventListener("keydown", function (ev) {
    if (ev.key === "Enter") { ev.preventDefault(); close(true); }
    if (ev.key === "Escape") { ev.stopPropagation(); done = true; el.innerHTML = prev; updateBar(); }
  });
  inp.addEventListener("click", function (ev) { ev.stopPropagation(); });
}
function openPicker(el) {
  if (el.querySelector("select") || el.querySelector("input")) return;
  var id = el.dataset.ef, f = el.dataset.f, r = rowById(id);
  var cur = shown(r, f);
  var kind = FIELD_TYPE[f];
  if (kind) { openInput(el, id, f, cur, kind); return; }
  var list = (META.opts && META.opts[f]) || [];
  var sel = document.createElement("select");
  sel.className = "efsel";
  var vals = list.slice();
  if (cur && vals.indexOf(cur) < 0) vals.unshift(cur);
  if (f === "community" || f === "owner_short") vals.unshift("");
  vals.forEach(function (v) {
    var o = document.createElement("option");
    o.value = v; o.textContent = v || "(blank)";
    if (v === cur) o.selected = true;
    sel.appendChild(o);
  });
  var prev = el.innerHTML;
  el.innerHTML = ""; el.appendChild(sel); sel.focus();
  var done = false;
  function close(commit) {
    if (done) return; done = true;
    var v = sel.value;
    el.innerHTML = prev;
    if (commit && v !== cur) setEdit(id, f, v); else updateBar();
  }
  sel.addEventListener("change", function () { close(true); });
  sel.addEventListener("blur", function () { close(false); });
  sel.addEventListener("keydown", function (ev2) {
    if (ev2.key === "Escape") { ev2.stopPropagation(); close(false); }
  });
  sel.addEventListener("click", function (ev2) { ev2.stopPropagation(); });
}
document.addEventListener("change", function (ev) {
  var cb = ev.target.closest("input[data-fl]");
  if (cb) setFlag(cb.dataset.fl, cb.dataset.k, cb.checked);
});
document.addEventListener("click", function (ev) {
  if (ev.target.closest(".fl")) { ev.stopPropagation(); return; }
  var ef = ev.target.closest(".ef");
  if (ef && !ev.target.closest("#mask")) { ev.stopPropagation(); openPicker(ef); return; }
  var cb = ev.target.closest(".cbtn");
  if (cb) { ev.stopPropagation(); openModal(cb.dataset.c); return; }
  var id = ev.target.closest(".rid");
  if (id && !ev.target.closest(".mhead")) { copy(id.textContent.trim()); flash(id, "copied"); return; }
  if (id) { copy(id.textContent.trim()); return; }
  var cq = ev.target.closest(".cpq");
  if (cq) { copy(cq.dataset.q); flash(cq, "copied"); }
});
document.addEventListener("keydown", function (ev) {
  if (ev.key === "Escape") { if (document.getElementById("mask")) closeModal(); }
});
window.addEventListener("beforeunload", function (ev) {
  if (pendCount()) { ev.preventDefault(); ev.returnValue = ""; }
});
try {
  var v = JSON.parse(sessionStorage.getItem(VIEW_KEY) || "null");
  if (v && typeof v.y === "number") { window.scrollTo(0, v.y); sessionStorage.removeItem(VIEW_KEY); }
} catch (e) {}

if (window.claude && typeof window.claude.use === "function") {
  window.claude.use("artifact").then(function (a) {
    ART = a || null;
    if (!ART) { READONLY = true; showWarn("Saving is not available in this view, so comments stay in this browser only. <b>Copy open comments</b> still works."); }
    updateBar();
  }).catch(function () { READONLY = true; updateBar(); });
} else {
  READONLY = true;
  showWarn("This copy of the board is running outside claude.ai, so it cannot save. Comments stay in this browser.");
}
