/* Parakeet Communities — Property Operations Dashboard
 *
 * Plain-JS React (createElement, no JSX, no build step) so the same file runs
 * from the repo during development and inlined into a standalone artifact.
 * Reads window.__DASHBOARD_DATA__, produced by pipeline/build.py.
 */
(function () {
  "use strict";

  var h = React.createElement;
  var useState = React.useState;
  var useMemo = React.useMemo;

  var GREEN = "#4ABA81";
  var NAVY = "#2F4E65";
  var YELLOW = "#FFCC3B";
  var RED = "#F16262";

  // ------------------------------------------------------------ formatting ---

  function money(v, opts) {
    if (v == null) return "—";
    var compact = opts && opts.compact;
    var n = Number(v);
    if (compact) {
      var abs = Math.abs(n);
      if (abs >= 1e6) return "$" + (n / 1e6).toFixed(2) + "M";
      if (abs >= 1e3) return "$" + Math.round(n / 1e3) + "K";
      return "$" + Math.round(n).toLocaleString("en-US");
    }
    return "$" + Math.round(n).toLocaleString("en-US");
  }

  function pct(v, places) {
    if (v == null) return "—";
    return Number(v).toFixed(places == null ? 1 : places) + "%";
  }

  function count(v) {
    if (v == null) return "—";
    return Math.round(Number(v)).toLocaleString("en-US");
  }

  var MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

  function monthLabel(ym) {
    if (!ym) return "";
    var p = String(ym).split("-");
    return MONTH_NAMES[parseInt(p[1], 10) - 1] + " " + p[0];
  }

  function monthShort(ym) {
    if (!ym) return "";
    var p = String(ym).split("-");
    return MONTH_NAMES[parseInt(p[1], 10) - 1] + " " + p[0].slice(2);
  }

  /* Higher-is-better metrics (occupancy, collections) go red below `red`.
     Lower-is-better metrics (AR share) invert. */
  function band(value, th, invert) {
    if (value == null) return "";
    if (invert) return value > th.red ? "critical" : value > th.yellow ? "watch" : "good";
    return value < th.red ? "critical" : value < th.yellow ? "watch" : "good";
  }

  function bandColor(b) {
    return b === "critical" ? RED : b === "watch" ? YELLOW : GREEN;
  }

  function Delta(props) {
    var curr = props.curr, prev = props.prev;
    if (curr == null || prev == null) return h("div", { className: "ksub" }, props.fallback || " ");
    var d = curr - prev;
    var cls = Math.abs(d) < 0.05 ? "flat" : (props.invert ? (d > 0 ? "down" : "up") : (d > 0 ? "up" : "down"));
    var arrow = Math.abs(d) < 0.05 ? "→" : d > 0 ? "▲" : "▼";
    var body = props.money
      ? money(Math.abs(d), { compact: true })
      : Math.abs(d).toFixed(1) + (props.unit || "");
    return h("div", { className: "kdelta " + cls },
      h("span", null, arrow), h("span", null, body),
      h("span", { style: { color: "var(--text-muted)", fontWeight: 500 } }, props.suffix || "vs prior month"));
  }

  // ---------------------------------------------------------------- charts ---

  /* Charts are drawn in real pixels, not arbitrary user units.
     An earlier version used a fixed 100-unit viewBox scaled to the container,
     which stretched every label horizontally and blew type up to 35px in a
     full-width panel. Measuring the container and setting viewBox to its pixel
     size keeps type, padding and stroke weight at their stated sizes in any
     panel width. */
  function useWidth(fallback) {
    var st = useState(fallback || 720);
    var w = st[0], setW = st[1];
    var ref = React.useRef(null);
    React.useEffect(function () {
      var el = ref.current;
      if (!el) return;
      function measure() {
        var next = el.clientWidth;
        if (next && Math.abs(next - w) > 2) setW(next);
      }
      measure();
      if (typeof ResizeObserver === "undefined") {
        window.addEventListener("resize", measure);
        return function () { window.removeEventListener("resize", measure); };
      }
      var ro = new ResizeObserver(measure);
      ro.observe(el);
      return function () { ro.disconnect(); };
    }, [w]);
    return [ref, w];
  }

  /* Round a span to a 1/2/5 x 10^n step so ticks land on numbers a person
     would actually say. */
  function niceStep(span, target) {
    var raw = span / (target || 2);
    if (!(raw > 0)) return 1;
    var mag = Math.pow(10, Math.floor(Math.log(raw) / Math.LN10));
    var norm = raw / mag;
    var step = norm <= 1 ? 1 : norm <= 2 ? 2 : norm <= 5 ? 5 : 10;
    return step * mag;
  }

  function niceTicks(min, max, target) {
    var step = niceStep(max - min, target);
    var lo = Math.floor(min / step) * step;
    var out = [];
    for (var v = lo; v <= max + step * 0.001; v += step) {
      if (v >= min - step * 0.001) out.push(Math.abs(v) < step * 1e-9 ? 0 : v);
    }
    return out.length >= 2 ? out : [min, max];
  }

  var FS_AXIS = 11, FS_VAL = 13;

  function LineChart(props) {
    var mw = useWidth(700);
    var ref = mw[0], W = mw[1];
    var series = props.series || [];
    var H = props.height || 230;
    var padL = 52, padR = 16, padT = 22, padB = 28;

    if (series.length < 2) {
      return h("div", { ref: ref, className: "loading" }, "Not enough history to chart yet.");
    }

    var lines = props.lines;
    var vals = [];
    var scaleFrom = series.filter(function (p) { return !p.partial; });
    if (!scaleFrom.length) scaleFrom = series;
    scaleFrom.forEach(function (p) {
      lines.forEach(function (l) { if (p[l.key] != null) vals.push(p[l.key]); });
    });
    if (props.zeroBase) vals.push(0);
    var min = Math.min.apply(null, vals);
    var max = Math.max.apply(null, vals);
    if (min === max) { min -= 1; max += 1; }
    var head = (max - min) * 0.15;
    max += head;
    min = props.zeroBase ? Math.min(0, min) : min - head;

    var innerW = Math.max(60, W - padL - padR);
    var x = function (i) { return padL + (i / (series.length - 1)) * innerW; };
    var y = function (v) {
      var t = padT + (1 - (v - min) / (max - min)) * (H - padT - padB);
      return Math.max(padT - 2, Math.min(H - padB, t));
    };

    var ticks = niceTicks(min, max, props.tickCount || 3);
    var fmtTick = props.fmtTick || function (v) { return Math.round(v); };
    var fmtPoint = props.fmtPoint || fmtTick;

    var kids = [];

    ticks.forEach(function (t, i) {
      kids.push(h("line", { key: "g" + i, className: "grid-line", x1: padL, x2: W - padR, y1: y(t), y2: y(t) }));
      kids.push(h("text", {
        key: "gt" + i, x: padL - 8, y: y(t) + FS_AXIS * 0.35, textAnchor: "end",
        style: { fontSize: FS_AXIS + "px" }
      }, fmtTick(t)));
    });

    lines.forEach(function (l, li) {
      var pts = [], liveHop = null;
      series.forEach(function (p, i) {
        if (p[l.key] == null) return;
        if (p.partial) {
          if (pts.length) liveHop = [pts[pts.length - 1], [x(i), y(p[l.key])], p[l.key]];
        } else {
          pts.push([x(i), y(p[l.key])]);
        }
      });
      if (!pts.length) return;

      if (l.area && pts.length > 1) {
        var base = y(props.zeroBase ? Math.max(0, min) : min);
        kids.push(h("path", {
          key: "a" + li,
          d: "M" + pts[0][0] + "," + base +
             pts.map(function (q) { return "L" + q[0] + "," + q[1]; }).join("") +
             "L" + pts[pts.length - 1][0] + "," + base + "Z",
          fill: l.color, fillOpacity: 0.11, stroke: "none"
        }));
      }

      if (pts.length > 1) {
        kids.push(h("path", {
          key: "l" + li,
          d: "M" + pts.map(function (q) { return q[0] + "," + q[1]; }).join("L"),
          fill: "none", stroke: l.color, strokeWidth: 2,
          strokeLinejoin: "round", strokeLinecap: "round"
        }));
      }

      if (liveHop) {
        kids.push(h("path", {
          key: "lh" + li,
          d: "M" + liveHop[0][0] + "," + liveHop[0][1] + "L" + liveHop[1][0] + "," + liveHop[1][1],
          fill: "none", stroke: l.color, strokeWidth: 2, strokeDasharray: "4 3",
          strokeLinecap: "round", opacity: 0.8
        }));
        kids.push(h("circle", {
          key: "lhc" + li, cx: liveHop[1][0], cy: liveHop[1][1], r: 3.4,
          fill: "var(--ground)", stroke: l.color, strokeWidth: 1.8
        }));
        if (li === 0) {
          kids.push(h("text", {
            key: "lhl", x: liveHop[1][0] - 6,
            y: Math.min(H - padB - 4, liveHop[1][1] + FS_VAL + 2),
            textAnchor: "end", style: { fontSize: FS_VAL + "px", fontWeight: 700 },
            fill: l.color
          }, (props.fmtPoint || props.fmtTick || String)(liveHop[2])));
        }
      }

      // Emphasize the final closed reading: the figure the headline quotes.
      var last = pts[pts.length - 1];
      kids.push(h("circle", { key: "e" + li, cx: last[0], cy: last[1], r: 3.2, fill: l.color }));
      if (li === 0) {
        var lastVal = null;
        for (var i = series.length - 1; i >= 0; i--) {
          if (!series[i].partial && series[i][l.key] != null) { lastVal = series[i][l.key]; break; }
        }
        if (lastVal != null) {
          kids.push(h("text", {
            key: "el",
            x: Math.min(last[0] - 7, W - padR),
            y: Math.max(padT - 4, last[1] - 11),
            className: "val-label", textAnchor: "end",
            style: { fontSize: FS_VAL + "px" }
          }, fmtPoint(lastVal)));
        }
      }
    });

    kids.push(h("line", { key: "ax", className: "axis-line", x1: padL, x2: W - padR, y1: H - padB, y2: H - padB }));

    var idxs = [0, Math.floor((series.length - 1) / 2), series.length - 1]
      .filter(function (v, i, a) { return a.indexOf(v) === i; });
    idxs.forEach(function (i) {
      kids.push(h("text", {
        key: "xl" + i, x: x(i), y: H - padB + FS_AXIS + 6,
        textAnchor: i === 0 ? "start" : i === series.length - 1 ? "end" : "middle",
        style: { fontSize: FS_AXIS + "px" }
      }, monthShort(series[i].month) + (series[i].partial ? " ○" : "")));
    });

    return h("div", { ref: ref, style: { width: "100%" } },
      h("svg", {
        className: "chart", viewBox: "0 0 " + W + " " + H,
        width: W, height: H, role: "img",
        "aria-label": props.ariaLabel || "trend chart"
      }, kids));
  }

  /* Stacked aging bars. One scale across every month, so stack heights compare. */
  function StackedBars(props) {
    var mw = useWidth(1000);
    var ref = mw[0], W = mw[1];
    var series = props.series || [];
    var H = props.height || 250;
    var padL = 58, padR = 16, padT = 30, padB = 28;

    if (!series.length) return h("div", { ref: ref, className: "loading" }, "No data.");

    var keys = props.keys;
    var closedTotals = series.filter(function (p) { return !p.partial; }).map(function (p) {
      return keys.reduce(function (s, k) { return s + (p[k.key] || 0); }, 0);
    });
    if (!closedTotals.length) {
      closedTotals = series.map(function (p) {
        return keys.reduce(function (s, k) { return s + (p[k.key] || 0); }, 0);
      });
    }
    var max = Math.max.apply(null, closedTotals) * 1.12 || 1;

    var innerW = Math.max(60, W - padL - padR);
    var band = innerW / series.length;
    var bw = Math.min(band * 0.62, 26);
    var y = function (v) { return padT + (1 - v / max) * (H - padT - padB); };

    var kids = [];
    niceTicks(0, max, 3).forEach(function (t, i) {
      kids.push(h("line", { key: "g" + i, className: "grid-line", x1: padL, x2: W - padR, y1: y(t), y2: y(t) }));
      kids.push(h("text", {
        key: "gt" + i, x: padL - 8, y: y(t) + FS_AXIS * 0.35, textAnchor: "end",
        style: { fontSize: FS_AXIS + "px" }
      }, t >= 1e6 ? "$" + (t / 1e6).toFixed(1) + "M" : "$" + Math.round(t / 1000) + "K"));
    });

    series.forEach(function (p, i) {
      var cx = padL + band * i + band / 2;
      var acc = 0;
      keys.forEach(function (k, ki) {
        var v = p[k.key] || 0;
        if (v <= 0) return;
        var y0 = Math.max(padT, y(acc + v)), y1 = Math.max(padT, y(acc));
        kids.push(h("rect", {
          key: "b" + i + "_" + ki, x: cx - bw / 2, y: y0, width: bw,
          height: Math.max(0.6, y1 - y0), fill: k.color,
          fillOpacity: p.partial ? 0.4 : 1,
          stroke: p.partial ? k.color : "none", strokeWidth: p.partial ? 1 : 0
        }));
        acc += v;
      });
    });

    // Cap marker and true total for a live stack that exceeds the closed scale.
    series.forEach(function (p, i) {
      if (!p.partial) return;
      var total = keys.reduce(function (a, k) { return a + (p[k.key] || 0); }, 0);
      if (!total) return;
      var cx = padL + band * i + band / 2;
      var over = total > max;
      if (over) {
        for (var z = 0; z < 2; z++) {
          kids.push(h("line", {
            key: "brk" + z, x1: cx - bw / 2 - 2, x2: cx + bw / 2 + 2,
            y1: padT + 3 + z * 4, y2: padT - 1 + z * 4,
            stroke: "var(--ground)", strokeWidth: 2.4
          }));
        }
      }
      kids.push(h("text", {
        key: "plbl", x: cx, y: Math.max(9, padT - 6), textAnchor: "middle",
        style: { fontSize: FS_VAL + "px", fontWeight: 700 }, fill: "var(--text)"
      }, (total >= 1e6 ? "$" + (total / 1e6).toFixed(2) + "M"
                       : "$" + Math.round(total / 1000) + "K") + (over ? " ↑" : "")));
    });

    kids.push(h("line", { key: "ax", className: "axis-line", x1: padL, x2: W - padR, y1: H - padB, y2: H - padB }));

    // Label as many months as fit without collisions.
    var step = Math.max(1, Math.ceil((FS_AXIS * 3.4) / band));
    series.forEach(function (p, i) {
      if (i % step !== 0 && i !== series.length - 1) return;
      kids.push(h("text", {
        key: "xl" + i, x: padL + band * i + band / 2, y: H - padB + FS_AXIS + 6,
        textAnchor: "middle", style: { fontSize: FS_AXIS + "px" }
      }, monthShort(p.month) + (p.partial ? " ○" : "")));
    });

    return h("div", { ref: ref, style: { width: "100%" } },
      h("svg", {
        className: "chart", viewBox: "0 0 " + W + " " + H,
        width: W, height: H, role: "img",
        "aria-label": props.ariaLabel || "stacked bar chart"
      }, kids));
  }

  function BarList(props) {
    var rows = props.rows || [];
    if (!rows.length) return h("div", { className: "loading" }, "Nothing to show.");
    var max = props.max || Math.max.apply(null, rows.map(function (r) { return Math.abs(r.value); })) || 1;
    return h("div", { className: "barlist" }, rows.map(function (r, i) {
      return h("div", { className: "barrow", key: r.label + i },
        h("div", { className: "bname", title: r.title || r.label },
          r.onClick
            ? h("button", { className: "linkish", onClick: r.onClick, title: r.title }, r.label)
            : r.label),
        h("div", { className: "btrack" },
          h("div", {
            className: "bfill",
            style: {
              width: Math.max(1.5, (Math.abs(r.value) / max) * 100) + "%",
              background: r.color || GREEN
            }
          })),
        h("div", { className: "bval" }, r.display));
    }));
  }

  function closedOnly(series) {
    return (series || []).filter(function (p) { return !p.partial; });
  }

  /* Period accessors. `mode` is "closed" or "live"; Financials always reads
     closed because the general ledger has not posted for the open month. */
  function pv(c, mode) { return (c && c[mode]) || {}; }

  /* Group the visible communities under their investment vehicle, pairing each
     with the pre-computed vehicle totals from the build so a collapsed row is
     still a real weighted figure and not an average of averages. */
  function groupByVehicle(d, rows, mode) {
    var byName = {};
    rows.forEach(function (c) {
      (byName[c.vehicle || "Unassigned"] = byName[c.vehicle || "Unassigned"] || []).push(c);
    });
    var pre = {};
    (d.vehicles || []).forEach(function (v) { pre[v.vehicle] = v; });
    return Object.keys(byName).map(function (k) {
      var members = byName[k];
      var full = pre[k];
      // When a filter has narrowed the set, recompute rather than showing the
      // vehicle's untouched totals next to a partial list of its communities.
      var partial = !full || members.length !== (full.names || []).length;
      var totals;
      if (partial) {
        var s_ = function (f) {
          return members.reduce(function (a, c) { return a + (pv(c, mode)[f] || 0); }, 0);
        };
        var units = s_("units"), charged = s_("charged"), arTot = s_("ar_total");
        var rev = members.reduce(function (a, c) { return a + (c.closed.revenue || 0); }, 0);
        var noi = members.reduce(function (a, c) { return a + (c.closed.noi || 0); }, 0);
        totals = {
          units: units, occupied: s_("occupied"),
          occupancy: units ? s_("occupied") / units * 100 : 0,
          charged: charged, paid: s_("paid"), outstanding: s_("outstanding"),
          collection_pct: charged ? s_("paid") / charged * 100 : 0,
          ar_total: arTot, ar_0_30: s_("ar_0_30"), ar_31_60: s_("ar_31_60"),
          ar_61_90: s_("ar_61_90"), ar_90_plus: s_("ar_90_plus"),
          ar_past_due_30plus: s_("ar_past_due_30plus"),
          ar_accounts: s_("ar_accounts"),
          ar_per_unit: units ? arTot / units : 0,
          move_ins: s_("move_ins"), move_outs: s_("move_outs"),
          revenue: rev, noi: noi, noi_margin: rev ? noi / rev * 100 : 0
        };
      } else {
        totals = full[mode];
      }
      return { key: k, label: k, rows: members, totals: totals };
    }).sort(function (a, b) { return b.totals.units - a.totals.units; });
  }

  function PeriodToggle(props) {
    var d = props.data, mode = props.mode;
    var lp = d.period;
    return h("div", { className: "period-toggle no-print", role: "group",
                      "aria-label": "Reporting period" },
      [["closed", "Closed", monthLabel(lp.closed), "month end"],
       ["live", "Live", monthLabel(lp.live), "through day " + lp.live_day]
      ].map(function (o) {
        var active = mode === o[0];
        return h("button", {
          key: o[0], className: "pbtn" + (active ? " active" : ""),
          "aria-pressed": active ? "true" : "false",
          onClick: function () { props.onChange(o[0]); }
        },
          h("span", { className: "pbtn-kind" }, o[1]),
          h("span", { className: "pbtn-month" }, o[2]),
          h("span", { className: "pbtn-note" }, o[3]));
      }));
  }

  // ----------------------------------------------------------- table pieces ---

  function SortableTable(props) {
    var cols = props.cols;
    var rows = props.rows;
    var initial = props.initialSort || { key: cols[0].key, dir: 1 };
    var s = useState(initial);
    var sort = s[0], setSort = s[1];

    var sorted = useMemo(function () {
      var col = cols.filter(function (c) { return c.key === sort.key; })[0] || cols[0];
      var out = rows.slice();
      out.sort(function (a, b) {
        var av = col.sortValue ? col.sortValue(a) : a[col.key];
        var bv = col.sortValue ? col.sortValue(b) : b[col.key];
        if (av == null) av = col.numeric ? -Infinity : "";
        if (bv == null) bv = col.numeric ? -Infinity : "";
        if (typeof av === "string") return sort.dir * av.localeCompare(bv);
        return sort.dir * (av - bv);
      });
      return out;
    }, [rows, sort.key, sort.dir, cols]);

    function toggle(key) {
      var col = cols.filter(function (c) { return c.key === key; })[0];
      setSort(function (prev) {
        if (prev.key === key) return { key: key, dir: -prev.dir };
        return { key: key, dir: col && col.numeric ? -1 : 1 };
      });
    }

    return h("div", { className: "table-scroll" },
      h("table", { className: "data" },
        h("thead", null, h("tr", null, cols.map(function (c) {
          return h("th", {
            key: c.key, onClick: function () { toggle(c.key); },
            title: c.title || ("Sort by " + c.label), scope: "col",
            "aria-sort": sort.key === c.key ? (sort.dir === 1 ? "ascending" : "descending") : "none"
          }, c.label, sort.key === c.key
            ? h("span", { className: "arrow" }, sort.dir === 1 ? " ▲" : " ▼")
            : null);
        }))),
        h("tbody", null, sorted.map(function (r, i) {
          return h("tr", { key: r.name || i }, cols.map(function (c) {
            return h("td", {
              key: c.key,
              className: (c.numeric ? "num " : "") + (c.key === cols[0].key ? "name" : "")
            }, c.render ? c.render(r) : r[c.key]);
          }));
        })),
        props.footer ? h("tfoot", null, h("tr", null, props.footer.map(function (f, i) {
          return h("td", { key: i }, f);
        }))) : null));
  }

  function Chip(props) {
    return h("span", { className: "chip " + props.band }, props.children);
  }

  // --------------------------------------------------------------- drill-in ---

  function Modal(props) {
    React.useEffect(function () {
      function onKey(e) { if (e.key === "Escape") props.onClose(); }
      document.addEventListener("keydown", onKey);
      var prev = document.body.style.overflow;
      document.body.style.overflow = "hidden";
      return function () {
        document.removeEventListener("keydown", onKey);
        document.body.style.overflow = prev;
      };
    }, [props.onClose]);

    return h("div", {
      className: "modal-scrim",
      onClick: function (e) { if (e.target === e.currentTarget) props.onClose(); }
    }, h("div", { className: "modal", role: "dialog", "aria-modal": "true",
                  "aria-label": props.title },
      h("div", { className: "modal-head" },
        h("div", null,
          h("h3", null, props.title),
          props.subtitle ? h("div", { className: "msub" }, props.subtitle) : null),
        h("button", { className: "modal-close", onClick: props.onClose,
                      "aria-label": "Close" }, "×")),
      props.stats ? h("div", { className: "modal-stats" }, props.stats.map(function (st, i) {
        return h("div", { className: "modal-stat", key: i },
          h("div", { className: "slabel" }, st.label),
          h("div", { className: "svalue", style: st.color ? { color: st.color } : null }, st.value),
          st.note ? h("div", { className: "snote" }, st.note) : null);
      })) : null,
      h("div", { className: "modal-body" }, props.children)));
  }

  function Stat(label, value, note, color) {
    return { label: label, value: value, note: note, color: color };
  }

  /* One community, four views: its rent roll, why its lots are empty, who owes
     money, and how its P&L reads against budget. */
  function CommunityDrill(props) {
    var c = props.community, d = props.data, mode = props.mode;
    var st = useState(props.view || "rentroll");
    var view = st[0], setView = st[1];
    var v = pv(c, mode), th = d.thresholds;
    var e = c.expenses || {}, ey = c.expenses_ytd || {};

    var VIEWS = [
      { id: "rentroll", label: "Rent roll (" + (c.rent_roll || []).length + ")" },
      { id: "vacancy", label: "Vacant (" + (c.vacancy_detail || []).length + ")" },
      { id: "accounts", label: "Accounts owing (" + (c.ar_accounts || []).length + ")" },
      { id: "pl", label: "P&L vs budget" }
    ];

    var body;
    if (view === "rentroll") {
      var rr = c.rent_roll || [];
      body = rr.length
        ? h("div", null,
          h("div", { className: "panel-head" },
            h("h2", null, "Rent roll"),
            h("div", { className: "note" },
              "Closed " + monthLabel(d.period.closed) +
              " · a full month billed and collected, which the open month is not yet")),
          h(SortableTable, {
            cols: [
              { key: "unit", label: "Unit", render: function (r) {
                  return h("span", null, r.unit, " ",
                    r.vacant ? h("span", { className: "tag" }, "vacant") : null); } },
              { key: "type", label: "Type" },
              { key: "rent", label: "Rent", numeric: true, render: function (r) { return money(r.rent); } },
              { key: "misc", label: "Misc", numeric: true, render: function (r) { return money(r.misc); } },
              { key: "charged", label: "Charged", numeric: true, render: function (r) { return money(r.charged); } },
              { key: "paid", label: "Paid", numeric: true, render: function (r) { return money(r.paid); } },
              { key: "balance", label: "Balance", numeric: true, render: function (r) {
                  return r.balance
                    ? h("span", { className: "down" }, money(r.balance))
                    : h("span", { style: { color: "var(--text-muted)" } }, "—"); } },
              { key: "deposit", label: "Deposit", numeric: true, render: function (r) { return money(r.deposit); } },
              { key: "move_in", label: "Moved in", render: function (r) { return r.move_in || "—"; } }
            ],
            rows: rr, initialSort: { key: "unit", dir: 1 },
            footer: ["Total " + rr.length + " units", "",
              money(rr.reduce(function (a, r) { return a + r.rent; }, 0)),
              money(rr.reduce(function (a, r) { return a + r.misc; }, 0)),
              money(rr.reduce(function (a, r) { return a + r.charged; }, 0)),
              money(rr.reduce(function (a, r) { return a + r.paid; }, 0)),
              money(rr.reduce(function (a, r) { return a + r.balance; }, 0)),
              money(rr.reduce(function (a, r) { return a + r.deposit; }, 0)), ""]
          }))
        : h("div", { className: "loading" },
            "No Rent Manager unit detail for this community. See the data notes.");
    } else if (view === "vacancy") {
      var vd = c.vacancy_detail || [];
      var counted = (c.vacancy_by_reason || []).reduce(function (a, r) { return a + r.units; }, 0);
      body = vd.length
        ? h("div", null,
            h("div", { className: "panel-body" },
              h(ReasonBar, { rows: c.vacancy_by_reason || [], meta: d.reason_meta }),
              h("div", { className: "note",
                         style: { marginTop: "12px", fontSize: "12px", color: "var(--text-muted)" } },
                "The bar counts " + count(counted) + " vacant on a unit-day basis. The list below " +
                "names " + count(vd.length) + " units with no active lease today. Different " +
                "measures, so they do not tie.")),
            h(SortableTable, {
              cols: [
                { key: "unit", label: "Unit" },
                { key: "type", label: "Unit type" },
                { key: "reason", label: "Why it is empty", render: function (r) {
                    var m = (d.reason_meta || {})[r.reason] || {};
                    return h("span", {
                      className: "chip " + (m.actionable === false ? "critical" : "watch")
                    }, m.label || r.reason); } },
                { key: "rent_lost", label: "Rent lost", numeric: true,
                  render: function (r) { return money(r.rent_lost); } }
              ],
              rows: vd, initialSort: { key: "rent_lost", dir: -1 },
              footer: [vd.length + " vacant", "", "",
                money(vd.reduce(function (a, r) { return a + r.rent_lost; }, 0))]
            }))
        : h("div", { className: "loading" }, "Nothing vacant, or no unit detail available.");
    } else if (view === "accounts") {
      var aa = c.ar_accounts || [];
      body = aa.length
        ? h(SortableTable, {
            cols: [
              { key: "unit", label: "Unit" },
              { key: "account", label: "Account", render: function (r) { return "#" + r.account; } },
              { key: "segment", label: "Standing", render: function (r) {
                  return h("span", {
                    className: "chip " + (r.segment === "legal" ? "critical"
                      : r.segment === "payment_plan" ? "good" : "watch")
                  }, SEG_LABEL[r.segment] || r.segment); } },
              { key: "b0_30", label: "0–30", numeric: true, render: function (r) { return money(r.b0_30); } },
              { key: "b31_60", label: "31–60", numeric: true, render: function (r) { return money(r.b31_60); } },
              { key: "b61_90", label: "61–90", numeric: true, render: function (r) { return money(r.b61_90); } },
              { key: "b90p", label: "90+", numeric: true, render: function (r) {
                  return r.b90p
                    ? h("span", { className: "down" }, money(r.b90p))
                    : h("span", { style: { color: "var(--text-muted)" } }, "—"); } },
              { key: "total", label: "Total owed", numeric: true, render: function (r) { return money(r.total); } },
              { key: "charges", label: "What it is" }
            ],
            rows: aa, initialSort: { key: "past_due_30plus", dir: -1 },
            footer: [aa.length + " accounts", "", "",
              money(aa.reduce(function (a, r) { return a + r.b0_30; }, 0)),
              money(aa.reduce(function (a, r) { return a + r.b31_60; }, 0)),
              money(aa.reduce(function (a, r) { return a + r.b61_90; }, 0)),
              money(aa.reduce(function (a, r) { return a + r.b90p; }, 0)),
              money(aa.reduce(function (a, r) { return a + r.total; }, 0)), ""]
          })
        : h("div", { className: "loading" }, "No outstanding accounts, or no unit detail available.");
    } else {
      body = h(PLTable, { community: c, data: d });
    }

    return h(Modal, {
      title: c.name,
      subtitle: [c.short_name, c.vehicle, c.kind, c.state,
                 count(v.units) + " lots"].filter(Boolean).join("  ·  "),
      onClose: props.onClose,
      stats: [
        Stat("Occupancy", pct(v.occupancy), count(v.occupied) + " of " + count(v.units),
             bandColor(band(v.occupancy, th.occupancy))),
        Stat("Past due 30+", money(v.ar_past_due_30plus, { compact: true }),
             count(v.ar_accounts) + " accounts", RED),
        Stat("Total AR", money(v.ar_total, { compact: true }),
             money(v.ar_per_unit) + " per lot"),
        Stat(mode === "live" ? "Collected MTD" : "Collections",
             v.charged ? pct(v.collection_pct) : "—",
             money(v.paid, { compact: true }) + " of " + money(v.charged, { compact: true })),
        Stat("NOI", money(c.closed.noi, { compact: true }),
             "closed " + monthLabel(d.period.closed),
             c.closed.noi_budget && c.closed.noi < c.closed.noi_budget ? RED : GREEN),
        Stat("Utility recapture",
             e.utility_recapture_pct == null ? "—" : pct(e.utility_recapture_pct, 0),
             money(e.utility_reimbursements) + " of " + money(e.utilities),
             e.utility_recapture_pct != null && e.utility_recapture_pct < 80 ? YELLOW : GREEN)
      ]
    },
      h("div", { className: "modal-tabs", role: "tablist" }, VIEWS.map(function (t) {
        return h("button", {
          key: t.id, className: "tab", role: "tab",
          "aria-selected": view === t.id ? "true" : "false",
          onClick: function () { setView(t.id); }
        }, t.label);
      })),
      body);
  }

  /* Line-item P&L. Budgets exist for revenue, total opex, R&M, utilities and
     NOI; the rest show actuals with a dash for variance rather than a fake
     target. Month and year to date sit side by side because a single month
     this early tells you very little on its own. */
  function PLTable(props) {
    var c = props.community, d = props.data;
    var e = c.expenses || {}, y = c.expenses_ytd || {}, cl = c.closed || {};
    var lm = (c.live || {});

    var LINES = [
      { g: "Revenue", label: "Lot and rental income", k: "lot_rent_rental" },
      { g: "Revenue", label: "Utility reimbursements", k: "utility_reimbursements" },
      { g: "Revenue", label: "Ancillary fees", k: "ancillary_fees" },
      { g: "Revenue", label: "Total operating revenue", k: null,
        actual: cl.revenue, ytd: cl.ytd_revenue,
        budget: cl.revenue_budget, budget_ytd: cl.ytd_revenue_budget, total: true },
      { g: "Controllable expense", label: "Repairs and maintenance", k: "repairs_maintenance",
        budget: e.repairs_maintenance_budget, budget_ytd: y.repairs_maintenance_budget },
      { g: "Controllable expense", label: "Payroll and management", k: "payroll_management" },
      { g: "Controllable expense", label: "Legal and professional", k: "legal_professional" },
      { g: "Controllable expense", label: "Other controllable", k: "other_controllable" },
      { g: "Controllable expense", label: "Total controllable", k: "controllable", total: true },
      { g: "Non-controllable expense", label: "Utilities", k: "utilities",
        budget: e.utilities_budget, budget_ytd: y.utilities_budget },
      { g: "Non-controllable expense", label: "Property taxes", k: "taxes" },
      { g: "Non-controllable expense", label: "Insurance", k: "insurance" },
      { g: "Non-controllable expense", label: "Total non-controllable", k: "non_controllable", total: true },
      { g: "Bottom line", label: "Total operating expense", k: "opex",
        budget: cl.opex_budget, total: true },
      { g: "Bottom line", label: "Net operating income", k: null,
        actual: cl.noi, ytd: cl.ytd_noi,
        budget: cl.noi_budget, budget_ytd: cl.ytd_noi_budget, total: true },
      { g: "Below the line", label: "Capital expenditure", k: "capex" },
      { g: "Below the line", label: "Debt service", k: "debt_service" },
      { g: "Below the line", label: "Non-operating income", k: "non_operating_income" }
    ];

    function variance(actual, budget, isExpense) {
      if (!budget) return h("span", { style: { color: "var(--text-muted)" } }, "—");
      var diff = (actual || 0) - budget;
      // Over budget is bad for an expense line and good for a revenue line.
      var good = isExpense ? diff <= 0 : diff >= 0;
      return h("span", { className: good ? "up" : "down" },
        (diff >= 0 ? "+" : "−") + money(Math.abs(diff)));
    }

    var rows = [];
    var lastG = null;
    LINES.forEach(function (L, i) {
      if (L.g !== lastG) {
        rows.push(h("tr", { className: "group-row", key: "g" + i },
          h("td", { colSpan: 6 }, h("span", { className: "gname" }, L.g))));
        lastG = L.g;
      }
      var actual = L.k ? (e[L.k] || 0) : (L.actual || 0);
      var ytd = L.k ? (y[L.k] || 0) : (L.ytd || 0);
      var isExpense = L.g.indexOf("expense") >= 0 || L.label === "Total operating expense";
      rows.push(h("tr", { key: "l" + i, className: "child-row" },
        h("td", { style: L.total ? { fontWeight: 700 } : null }, L.label),
        h("td", { className: "num", style: L.total ? { fontWeight: 700 } : null }, money(actual)),
        h("td", { className: "num" }, L.budget ? money(L.budget) : "—"),
        h("td", { className: "num" }, variance(actual, L.budget, isExpense)),
        h("td", { className: "num", style: L.total ? { fontWeight: 700 } : null }, money(ytd)),
        h("td", { className: "num" }, L.budget_ytd
          ? variance(ytd, L.budget_ytd, isExpense)
          : h("span", { style: { color: "var(--text-muted)" } }, "—"))));
    });

    return h("div", null,
      h("div", { className: "panel-head" },
        h("h2", null, "Revenue and expense against budget"),
        h("div", { className: "note" },
          "Closed " + monthLabel(d.period.closed) + " and year to date through the same month")),
      h("div", { className: "table-scroll" },
        h("table", { className: "data" },
          h("thead", null, h("tr", null,
            h("th", { style: { cursor: "default" } }, "Line"),
            h("th", { style: { cursor: "default" } }, monthLabel(d.period.closed)),
            h("th", { style: { cursor: "default" } }, "Budget"),
            h("th", { style: { cursor: "default" } }, "Variance"),
            h("th", { style: { cursor: "default" } }, "YTD"),
            h("th", { style: { cursor: "default" } }, "YTD variance"))),
          h("tbody", null, rows))),
      lm.charged ? h("div", { className: "panel-body" },
        h("div", { className: "note", style: { fontSize: "12px", color: "var(--text-muted)" } },
          "Open " + monthLabel(d.period.live) + " through day " + d.period.live_day + ": " +
          money(lm.charged) + " billed, " + money(lm.paid) + " collected, " +
          money(lm.outstanding) + " still out. The ledger does not post revenue and expense " +
          "intra-month, so the lines above stay on the closed month.")) : null);
  }

  /* Vacancy composition as one stacked bar. A list of unit types answers "what
     types", but the question is "how much of my vacancy can I actually lease",
     and proportion carries that far better than rows of numbers. */
  /* Aging reads as a ramp: fresh is fine, old is money burning. */
  var AGE_COLORS = {
    "0-30 days": "#4ABA81", "31-60 days": "#A8D5BD", "61-90 days": "#FFCC3B",
    "91-180 days": "#F1A462", "181-365 days": "#F16262", "Over a year": "#B23B3B",
    "Unknown": "#C7D3DA"
  };
  var AGE_ORDER = ['0-30 days','31-60 days','61-90 days','91-180 days','181-365 days','Over a year','Unknown'];

  /* The home lifecycle, ordered the way a home actually moves through it. */
  var STATUS_ORDER = ["Ordered", "Delivered", "Needs Rehab", "For Sale",
                      "Rent to Own Agreement", "Lease Option (LOP)", "Rental",
                      "In Use", "Eviction Filed", "To Be Demoed", "TBD", "Unknown"];
  var STATUS_COLORS = {
    "Ordered": "#C7D3DA", "Delivered": "#8FA3B2", "Needs Rehab": "#FFCC3B",
    "For Sale": "#4ABA81", "Rent to Own Agreement": "#2F4E65",
    "Lease Option (LOP)": "#5C7C93", "Rental": "#A8D5BD", "In Use": "#A8D5BD",
    "Eviction Filed": "#F16262", "To Be Demoed": "#B23B3B", "TBD": "#E0E6EA",
    "Unknown": "#E0E6EA"
  };

  var SEG_LABEL = {
    legal: "With legal", payment_plan: "On a payment plan",
    former: "Former resident", unclassified: "Not classified"
  };
  var SEG_COLORS = {
    legal: "#F16262", payment_plan: "#4ABA81",
    former: "#8FA3B2", unclassified: "#C7D3DA"
  };

  /* One proportional bar plus a legend. Used for vacancy reasons, vacancy
     aging, home status and AR segments: same shape, different dimension. */
  function BandBar(props) {
    var rows = (props.rows || []).filter(function (r) { return r.n > 0; });
    if (!rows.length) return h("div", { className: "loading" }, props.empty || "Nothing to show.");
    var total = rows.reduce(function (a, r) { return a + r.n; }, 0);
    return h("div", null,
      h("div", { className: "reasonbar", role: "img", "aria-label": props.label },
        rows.map(function (r) {
          return h("span", {
            key: r.key,
            style: { width: (r.n / total * 100) + "%", background: r.color },
            title: r.label + ": " + count(r.n) + (r.money ? " (" + money(r.money) + ")" : "")
          });
        })),
      h("div", { className: "reason-legend" }, rows.map(function (r) {
        return h("div", { className: "rl", key: r.key },
          h("span", { className: "swatch", style: { background: r.color } }),
          h("span", null,
            h("span", { className: "rl-n" }, count(r.n)), " ", r.label,
            h("span", { className: "rl-sub" },
              "  " + pct(r.n / total * 100, 0) +
              (r.money ? "  ·  " + money(r.money, { compact: true }) : ""))));
      })),
      props.note ? h("div", { className: "note",
                              style: { marginTop: "10px", fontSize: "12px",
                                       color: "var(--text-muted)" } }, props.note) : null);
  }

  function agingRows(list) {
    var by = {}, lost = {};
    (list || []).forEach(function (r) {
      by[r.band] = (by[r.band] || 0) + r.units;
      lost[r.band] = (lost[r.band] || 0) + (r.rent_lost || 0);
    });
    return AGE_ORDER.filter(function (b) { return by[b]; }).map(function (b) {
      return { key: b, label: b, n: by[b], money: lost[b], color: AGE_COLORS[b] };
    });
  }

  function statusRows(list) {
    var by = {};
    (list || []).forEach(function (r) { by[r.status] = (by[r.status] || 0) + r.homes; });
    var known = STATUS_ORDER.filter(function (k) { return by[k]; });
    Object.keys(by).forEach(function (k) { if (known.indexOf(k) === -1) known.push(k); });
    return known.map(function (k) {
      return { key: k, label: k, n: by[k], color: STATUS_COLORS[k] || "#8FA3B2" };
    });
  }

  var REASON_COLORS = {
    home_available: GREEN,
    in_rehab: YELLOW,
    pending_setup: NAVY,
    rv_seasonal: "#8FA3B2",
    vacant_lot: "#A8D5BD",
    not_leasable: RED,
    non_revenue: "#C7D3DA"
  };

  function ReasonBar(props) {
    var rows = (props.rows || []).filter(function (r) { return r.units > 0; });
    if (!rows.length) return h("div", { className: "loading" }, "Nothing vacant.");
    var total = rows.reduce(function (a, r) { return a + r.units; }, 0);
    var lost = rows.reduce(function (a, r) { return a + (r.rent_lost || 0); }, 0);
    return h("div", null,
      h("div", { className: "reasonbar", role: "img",
                 "aria-label": "Vacant units by reason" },
        rows.map(function (r) {
          return h("span", {
            key: r.reason,
            style: { width: (r.units / total * 100) + "%",
                     background: REASON_COLORS[r.reason] || "#8FA3B2" },
            title: r.label + ": " + r.units + " units"
          });
        })),
      h("div", { className: "reason-legend" }, rows.map(function (r) {
        return h("div", { className: "rl", key: r.reason },
          h("span", { className: "swatch",
                      style: { background: REASON_COLORS[r.reason] || "#8FA3B2" } }),
          h("span", null,
            h("span", { className: "rl-n" }, count(r.units)), " ", r.label,
            h("span", { className: "rl-sub" },
              "  " + pct(r.units / total * 100, 0) +
              (r.rent_lost ? "  ·  " + money(r.rent_lost, { compact: true }) + " rent lost" : ""))));
      })),
      h("div", { className: "note", style: { marginTop: "10px", fontSize: "12px",
                                             color: "var(--text-muted)" } },
        count(total) + " vacant units" + (lost ? ", " + money(lost) + " of rent not being billed" : "")));
  }

  /* A table that opens at vehicle level. Each vehicle row carries its own
     weighted totals, so collapsing loses no information. */
  function GroupedTable(props) {
    var cols = props.cols;
    var groups = props.groups;          // [{key, label, count, totals, rows}]
    var es = useState({});
    var expanded = es[0], setExpanded = es[1];
    var ss = useState(props.initialSort || { key: cols[0].key, dir: 1 });
    var sort = ss[0], setSort = ss[1];

    function toggleGroup(k) {
      setExpanded(function (prev) {
        var next = Object.assign({}, prev);
        if (next[k]) { delete next[k]; } else { next[k] = true; }
        return next;
      });
    }

    function toggleSort(key) {
      var col = cols.filter(function (c) { return c.key === key; })[0];
      setSort(function (prev) {
        if (prev.key === key) return { key: key, dir: -prev.dir };
        return { key: key, dir: col && col.numeric ? -1 : 1 };
      });
    }

    function sortRows(rows) {
      var col = cols.filter(function (c) { return c.key === sort.key; })[0] || cols[0];
      var out = rows.slice();
      out.sort(function (a, b) {
        var av = col.sortValue ? col.sortValue(a) : a[col.key];
        var bv = col.sortValue ? col.sortValue(b) : b[col.key];
        if (av == null) av = col.numeric ? -Infinity : "";
        if (bv == null) bv = col.numeric ? -Infinity : "";
        if (typeof av === "string") return sort.dir * av.localeCompare(bv);
        return sort.dir * (av - bv);
      });
      return out;
    }

    var allOpen = groups.length > 0 && groups.every(function (g) { return expanded[g.key]; });

    var body = [];
    groups.forEach(function (g) {
      var open = !!expanded[g.key];
      body.push(h("tr", {
        key: "g-" + g.key, className: "group-row",
        onClick: function () { toggleGroup(g.key); }
      }, cols.map(function (c, ci) {
        if (ci === 0) {
          return h("td", { key: c.key },
            h("span", { className: "twisty" }, open ? "▾" : "▸"),
            h("span", { className: "gname" }, g.label),
            h("span", { className: "gcount" },
              g.rows.length + (g.rows.length === 1 ? " community" : " communities")));
        }
        return h("td", { key: c.key, className: c.numeric ? "num" : "" },
          c.group ? c.group(g.totals, g) : "");
      })));
      if (open) {
        sortRows(g.rows).forEach(function (r, ri) {
          body.push(h("tr", { key: "r-" + g.key + "-" + ri, className: "child-row" },
            cols.map(function (c) {
              return h("td", {
                key: c.key,
                className: (c.numeric ? "num " : "") + (c.key === cols[0].key ? "name" : "")
              }, c.render ? c.render(r) : r[c.key]);
            })));
        });
      }
    });

    return h("div", null,
      h("div", { className: "panel-head" },
        h("h2", null, props.title),
        h("div", { className: "group-controls no-print" },
          h("span", null, props.note),
          h("button", {
            className: "minibtn",
            onClick: function () {
              setExpanded(allOpen ? {} : groups.reduce(function (a, g) {
                a[g.key] = true; return a;
              }, {}));
            }
          }, allOpen ? "Collapse all" : "Expand all"))),
      h("div", { className: "table-scroll" },
        h("table", { className: "data" },
          h("thead", null, h("tr", null, cols.map(function (c) {
            return h("th", {
              key: c.key, onClick: function () { toggleSort(c.key); },
              title: c.title || ("Sort communities by " + c.label), scope: "col",
              "aria-sort": sort.key === c.key
                ? (sort.dir === 1 ? "ascending" : "descending") : "none"
            }, c.label, sort.key === c.key
              ? h("span", { className: "arrow" }, sort.dir === 1 ? " ▲" : " ▼")
              : null);
          }))),
          h("tbody", null, body),
          props.footer ? h("tfoot", null, h("tr", null, props.footer.map(function (f, i) {
            return h("td", { key: i }, f);
          }))) : null)));
  }

  // ------------------------------------------------------------------- tabs ---

  function Kpi(props) {
    return h("div", { className: "kpi" },
      h("div", { className: "klabel" }, props.label),
      h("div", { className: "kvalue", style: props.color ? { color: props.color } : null }, props.value),
      props.sub ? h("div", { className: "ksub" }, props.sub) : null,
      props.children || null);
  }

  function Panel(props) {
    return h("section", { className: "panel" },
      h("div", { className: "panel-head" },
        h("h2", null, props.title),
        props.note ? h("div", { className: "note" }, props.note) : null),
      h("div", { className: "panel-body" + (props.flush ? " flush" : "") }, props.children));
  }

  function OverviewTab(d, filtered, mode, ctx) {
    var p = d.portfolio[mode], t = d.trends, th = d.thresholds;
    // Where the pain is: worst occupancy and biggest 90+ balances.
    var zeroCount = d.communities.filter(function (c) {
      return pv(c, mode).units >= 20 && pv(c, mode).occupancy === 0;
    }).length;
    var worstOcc = d.communities.slice()
      .filter(function (c) { return pv(c, mode).units >= 20 && pv(c, mode).occupancy > 0; })
      .sort(function (a, b) { return pv(a, mode).occupancy - pv(b, mode).occupancy; }).slice(0, 8)
      .map(function (c) {
        var o = pv(c, mode).occupancy;
        return { label: c.name, value: o, display: pct(o),
                 color: bandColor(band(o, th.occupancy)) };
      });

    var worstAr = d.communities.slice()
      .sort(function (a, b) { return pv(b, mode).ar_90_plus - pv(a, mode).ar_90_plus; }).slice(0, 8)
      .map(function (c) {
        var v = pv(c, mode).ar_90_plus;
        return { label: c.name, value: v, display: money(v, { compact: true }),
                 color: v > 100000 ? RED : v > 40000 ? YELLOW : GREEN };
      });

    return h("div", null,
      h("div", { className: "grid-2" },
        h(Panel, {
          title: "Portfolio occupancy",
          note: "Weighted by unit-days · ○ is the open month"
        }, h(LineChart, {
          series: t.occupancy, zeroBase: false, height: 230,
          lines: [{ key: "occupancy", color: GREEN, area: true }],
          fmtTick: function (v) { return v.toFixed(0) + "%"; },
          fmtPoint: function (v) { return v.toFixed(1) + "%"; },
          ariaLabel: "Portfolio occupancy by month"
        })),
        h(Panel, {
          title: "Collections rate",
          note: "Payments ÷ charges · ○ open month collects all month"
        }, h(LineChart, {
          series: t.collections, zeroBase: false, height: 230,
          lines: [{ key: "collection_pct", color: NAVY, area: true }],
          fmtTick: function (v) { return v.toFixed(0) + "%"; },
          fmtPoint: function (v) { return v.toFixed(1) + "%"; },
          ariaLabel: "Collection rate by month"
        }))),

      h(Panel, {
        title: "Receivables by age",
        note: "○ open month carries fresh billing · the 90+ band is the one that compounds"
      },
        h(StackedBars, {
          series: t.ar, height: 250,
          keys: [
            { key: "b0_30", color: GREEN, label: "0–30 days" },
            { key: "b31_60", color: NAVY, label: "31–60 days" },
            { key: "b61_90", color: YELLOW, label: "61–90 days" },
            { key: "b90p", color: RED, label: "90+ days" }
          ],
          ariaLabel: "Aged receivables by bucket and month"
        }),
        h("div", { className: "legend" },
          h("span", null, h("i", { style: { background: GREEN } }), "0–30"),
          h("span", null, h("i", { style: { background: NAVY } }), "31–60"),
          h("span", null, h("i", { style: { background: YELLOW } }), "61–90"),
          h("span", null, h("i", { style: { background: RED } }), "90+"),
          h("span", null, "○ open month, still collecting"))),

      h("div", { className: "grid-2" },
        h(Panel, {
          title: "Lowest occupancy",
          note: zeroCount
            ? "20+ lot communities · " + zeroCount + " reporting exactly 0% held back, see data notes"
            : "20+ lot communities"
        }, h(BarList, { rows: worstOcc, max: 100 })),
        h(Panel, { title: "Largest 90+ balances", note: "As of " + monthLabel(d.period[mode === "live" ? "live" : "closed"]) },
          h(BarList, { rows: worstAr }))));
  }

  function CommunitiesTab(d, filtered, mode, ctx) {
    var th = d.thresholds;
    var V = function (c) { return pv(c, mode); };
    var live = mode === "live";

    var cols = [
      { key: "name", label: "Community", render: function (r) {
          return h("span", null,
            h("button", {
              className: "linkish",
              onClick: function () { ctx.open(r); },
              title: "Open " + r.name
            }, r.name), " ",
            h("span", { className: "tag" }, r.kind)); },
        group: null },
      { key: "units", label: "Lots", numeric: true,
        sortValue: function (r) { return V(r).units; },
        render: function (r) { return count(V(r).units); },
        group: function (t) { return count(t.units); } },
      { key: "occupancy", label: "Occupancy", numeric: true,
        sortValue: function (r) { return V(r).occupancy; },
        render: function (r) {
          return h(Chip, { band: band(V(r).occupancy, th.occupancy) }, pct(V(r).occupancy)); },
        group: function (t) {
          return h(Chip, { band: band(t.occupancy, th.occupancy) }, pct(t.occupancy)); } },
      { key: "occupancy_rentable", label: "Occ (rentable)", numeric: true,
        title: "Occupancy with unusable and demo lots out of the denominator",
        render: function (r) { return pct(r.occupancy_rentable); },
        group: function () { return ""; } },
      { key: "collection_pct", label: live ? "Collected MTD" : "Collections", numeric: true,
        sortValue: function (r) { return V(r).collection_pct; },
        render: function (r) {
          return V(r).charged
            ? h(Chip, { band: band(V(r).collection_pct, live ? { red: -1, yellow: -1 } : th.collections) },
                pct(V(r).collection_pct))
            : "—"; },
        group: function (t) {
          return t.charged
            ? h(Chip, { band: band(t.collection_pct, live ? { red: -1, yellow: -1 } : th.collections) },
                pct(t.collection_pct))
            : "—"; } },
      { key: "ar_total", label: "AR", numeric: true,
        sortValue: function (r) { return V(r).ar_total; },
        render: function (r) { return money(V(r).ar_total, { compact: true }); },
        group: function (t) { return money(t.ar_total, { compact: true }); } },
      { key: "ar_past_due_30plus", label: "Past due 30+", numeric: true,
        title: "Everything outside the 0–30 bucket: money that is genuinely late",
        sortValue: function (r) { return V(r).ar_past_due_30plus; },
        render: function (r) { return money(V(r).ar_past_due_30plus, { compact: true }); },
        group: function (t) { return money(t.ar_past_due_30plus, { compact: true }); } },
      { key: "ar_90_plus", label: "90+", numeric: true,
        sortValue: function (r) { return V(r).ar_90_plus; },
        render: function (r) { return money(V(r).ar_90_plus, { compact: true }); },
        group: function (t) { return money(t.ar_90_plus, { compact: true }); } },
      { key: "ar_per_unit", label: "AR / lot", numeric: true,
        sortValue: function (r) { return V(r).ar_per_unit; },
        render: function (r) { return money(V(r).ar_per_unit); },
        group: function (t) { return money(t.ar_per_unit); } },
      { key: "noi", label: "NOI", numeric: true,
        title: "Always the closed month; the ledger does not post intra-month",
        sortValue: function (r) { return r.closed.noi; },
        render: function (r) { return money(r.closed.noi, { compact: true }); },
        group: function (t) { return money(t.noi, { compact: true }); } },
      { key: "noi_margin", label: "NOI margin", numeric: true,
        title: "Closed month. Only shown where revenue clears $5K",
        sortValue: function (r) { return r.closed.noi_margin; },
        render: function (r) {
          return r.closed.revenue >= 5000
            ? h(Chip, { band: band(r.closed.noi_margin, th.noi_margin) }, pct(r.closed.noi_margin, 0))
            : "—"; },
        group: function (t) {
          return t.revenue
            ? h(Chip, { band: band(t.noi_margin, th.noi_margin) }, pct(t.noi_margin, 0))
            : "—"; } },
      { key: "move_ins", label: "In / Out", numeric: true,
        sortValue: function (r) { return V(r).move_ins - V(r).move_outs; },
        render: function (r) { return V(r).move_ins + " / " + V(r).move_outs; },
        group: function (t) { return t.move_ins + " / " + t.move_outs; } }
    ];

    var groups = groupByVehicle(d, filtered, mode);
    var sum = function (k) { return filtered.reduce(function (s, c) { return s + (V(c)[k] || 0); }, 0); };
    var units = sum("units");
    var charged = sum("charged"), paid = sum("paid");
    var arTot = sum("ar_total");
    var noi = filtered.reduce(function (s, c) { return s + (c.closed.noi || 0); }, 0);
    var rev = filtered.reduce(function (s, c) { return s + (c.closed.revenue || 0); }, 0);

    return h("section", { className: "panel" },
      h(GroupedTable, {
        title: groups.length + (groups.length === 1 ? " vehicle" : " vehicles") +
               ", " + filtered.length + " communities",
        note: (live ? "Live through day " + d.period.live_day : "Closed " + monthLabel(d.period.closed)) +
              " · NOI always closed · click a vehicle to expand, a name to drill in",
        cols: cols, groups: groups,
        initialSort: { key: "occupancy", dir: 1 },
        footer: [
          "Portfolio", count(units), pct(units ? sum("occupied") / units * 100 : 0), "—",
          charged ? pct(paid / charged * 100) : "—",
          money(arTot, { compact: true }),
          money(sum("ar_past_due_30plus"), { compact: true }),
          money(sum("ar_90_plus"), { compact: true }),
          units ? money(arTot / units) : "—",
          money(noi, { compact: true }),
          rev ? pct(noi / rev * 100, 0) : "—",
          sum("move_ins") + " / " + sum("move_outs")
        ]
      }));
  }
  function OccupancyTab(d, filtered, mode, ctx) {
    var th = d.thresholds;
    var V = function (c) { return pv(c, mode); };
    var mh = filtered.filter(function (c) { return c.kind === "MH"; });
    var rv = filtered.filter(function (c) { return c.kind === "RV"; });
    var periodLabel = monthLabel(d.period[mode === "live" ? "live" : "closed"]);

    function wavg(rows) {
      var u = rows.reduce(function (a, c) { return a + V(c).units; }, 0);
      return u ? rows.reduce(function (a, c) { return a + V(c).occupancy * V(c).units; }, 0) / u : 0;
    }
    function lots(rows) { return rows.reduce(function (a, c) { return a + V(c).units; }, 0); }

    // Vacancy reasons for the filtered set, so the tiles agree with the filters.
    var reasonTotals = {};
    filtered.forEach(function (c) {
      (c.vacancy_by_reason || []).forEach(function (r) {
        var t = reasonTotals[r.reason] || (reasonTotals[r.reason] = {
          reason: r.reason, label: r.label, actionable: r.actionable, units: 0, rent_lost: 0
        });
        t.units += r.units;
        t.rent_lost += r.rent_lost || 0;
      });
    });
    var reasons = Object.keys(reasonTotals).map(function (k) { return reasonTotals[k]; })
      .sort(function (a, b) { return b.units - a.units; });
    function reasonUnits(k) { return (reasonTotals[k] || {}).units || 0; }
    function reasonLost(k) { return (reasonTotals[k] || {}).rent_lost || 0; }

    var byPark = {};
    filtered.forEach(function (c) {
      var p = byPark[c.park] || (byPark[c.park] = { park: c.park, units: 0, occupied: 0, members: [] });
      p.units += V(c).units;
      p.occupied += V(c).occupied;
      p.members.push(c);
    });
    var parks = Object.keys(byPark).map(function (k) { return byPark[k]; })
      .filter(function (p) { return p.units >= 20; })
      .map(function (p) {
        var o = p.units ? p.occupied / p.units * 100 : 0;
        return { label: p.park, value: o, display: pct(o),
                 color: bandColor(band(o, th.occupancy)),
                 onClick: function () { ctx.open(p.members[0], "rentroll"); },
                 title: "Open the rent roll for " + p.members[0].name };
      }).sort(function (a, b) { return a.value - b.value; });

    return h("div", null,
      h("div", { className: "grid-3" },
        h(Panel, { title: "MH occupancy", note: count(mh.length) + " communities · " + periodLabel },
          h("div", { className: "bignum" }, pct(wavg(mh))),
          h("div", { className: "ksub" }, count(lots(mh)) + " lots")),
        h(Panel, { title: "RV occupancy", note: count(rv.length) + " communities · " + periodLabel },
          h("div", { className: "bignum" }, pct(wavg(rv))),
          h("div", { className: "ksub" }, count(lots(rv)) + " lots")),
        h(Panel, { title: "Move-ins vs move-outs", note: periodLabel },
          h("div", { className: "bignum" }, (function () {
            var net = filtered.reduce(function (a, c) { return a + V(c).move_ins - V(c).move_outs; }, 0);
            return (net > 0 ? "+" : "") + net;
          })()),
          h("div", { className: "ksub" },
            filtered.reduce(function (a, c) { return a + V(c).move_ins; }, 0) + " in, " +
            filtered.reduce(function (a, c) { return a + V(c).move_outs; }, 0) + " out"))),

      // What is actually behind the vacancy, which is the difference between a
      // leasing problem and a capital or setup backlog.
      h("div", { className: "grid-3" },
        h(Panel, { title: "Homes available", note: "Park-owned, ready to sell or rent" },
          h("div", { className: "bignum", style: { color: GREEN } }, count(reasonUnits("home_available"))),
          h("div", { className: "ksub" }, money(reasonLost("home_available")) + " of rent not billed")),
        h(Panel, { title: "In rehab", note: "Cannot be leased until the work is done" },
          h("div", { className: "bignum", style: { color: YELLOW } }, count(reasonUnits("in_rehab"))),
          h("div", { className: "ksub" }, money(reasonLost("in_rehab")) + " of rent not billed")),
        h(Panel, { title: "Pending home setup", note: "Lot sold or committed, home not set" },
          h("div", { className: "bignum", style: { color: NAVY } }, count(reasonUnits("pending_setup"))),
          h("div", { className: "ksub" }, money(reasonLost("pending_setup")) + " of rent not billed"))),

      h(Panel, {
        title: "Vacancy by reason",
        note: "Unit-day weighted from the warehouse · click through on the Vacancy tab for units"
      }, h(ReasonBar, { rows: reasons, meta: d.reason_meta })),

      h(Panel, {
        title: "How long has it been sitting",
        note: "Days since the unit's last move-out"
      }, h(BandBar, {
        rows: agingRows([].concat.apply([], filtered.map(function (c) { return c.vacancy_aging || []; }))),
        label: "Vacant units by how long they have been empty",
        note: (function () {
          var rs = agingRows([].concat.apply([], filtered.map(function (c) { return c.vacancy_aging || []; })));
          var old_ = rs.filter(function (r) {
            return ["91-180 days", "181-365 days", "Over a year"].indexOf(r.key) >= 0;
          });
          var n = old_.reduce(function (a, r) { return a + r.n; }, 0);
          var m = old_.reduce(function (a, r) { return a + (r.money || 0); }, 0);
          var unk = rs.filter(function (r) { return r.key === "Unknown"; })[0];
          return (n ? count(n) + " units have been empty more than 90 days, " +
                      money(m) + " of rent a month. " : "") +
                 (unk ? count(unk.n) + " have no move-out on record and show as Unknown." : "");
        })()
      })),

      h(Panel, {
        title: "Move-ins and move-outs by community",
        note: periodLabel + " · net is the change in occupied lots",
        flush: true
      }, h(SortableTable, {
        cols: [
          { key: "name", label: "Community", render: function (r) {
              return h("span", null,
                h("button", { className: "linkish", onClick: function () { ctx.open(r.community); } },
                  r.name), " ", h("span", { className: "tag" }, r.vehicle)); } },
          { key: "units", label: "Lots", numeric: true, render: function (r) { return count(r.units); } },
          { key: "occupancy", label: "Occupancy", numeric: true,
            render: function (r) {
              return h(Chip, { band: band(r.occupancy, th.occupancy) }, pct(r.occupancy)); } },
          { key: "ins", label: "Move-ins", numeric: true, render: function (r) { return r.ins || "—"; } },
          { key: "outs", label: "Move-outs", numeric: true, render: function (r) { return r.outs || "—"; } },
          { key: "net", label: "Net", numeric: true, render: function (r) {
              if (!r.net) return h("span", { style: { color: "var(--text-muted)" } }, "0");
              return h("span", { className: r.net > 0 ? "up" : "down" },
                (r.net > 0 ? "+" : "") + r.net); } }
        ],
        rows: filtered.map(function (c) {
          var v = V(c);
          return { name: c.name, community: c, vehicle: c.vehicle, units: v.units,
                   occupancy: v.occupancy, ins: v.move_ins, outs: v.move_outs,
                   net: (v.move_ins || 0) - (v.move_outs || 0) };
        }),
        initialSort: { key: "net", dir: 1 },
        footer: ["Portfolio",
          count(filtered.reduce(function (a, c) { return a + V(c).units; }, 0)),
          pct((function () {
            var u = filtered.reduce(function (a, c) { return a + V(c).units; }, 0);
            return u ? filtered.reduce(function (a, c) { return a + V(c).occupied; }, 0) / u * 100 : 0;
          })()),
          filtered.reduce(function (a, c) { return a + V(c).move_ins; }, 0),
          filtered.reduce(function (a, c) { return a + V(c).move_outs; }, 0),
          (function () {
            var n = filtered.reduce(function (a, c) { return a + V(c).move_ins - V(c).move_outs; }, 0);
            return (n > 0 ? "+" : "") + n;
          })()]
      })),

      h(Panel, { title: "Move-in / move-out history", note: "Net resident movement · ○ open month" },
        h(LineChart, {
          series: d.trends.moves, zeroBase: true, height: 230,
          lines: [{ key: "ins", color: GREEN }, { key: "outs", color: RED }],
          fmtTick: function (v) { return Math.round(v); },
          ariaLabel: "Move-ins and move-outs by month"
        }),
        h("div", { className: "legend" },
          h("span", null, h("i", { style: { background: GREEN } }), "Move-ins"),
          h("span", null, h("i", { style: { background: RED } }), "Move-outs"),
          h("span", null, "○ open month, partial"))),

      h(Panel, {
        title: "Occupancy by park",
        note: "20+ lot parks · " + periodLabel + " · click a park for its rent roll"
      }, h(BarList, { rows: parks, max: 100 })));
  }
  function CollectionsTab(d, filtered, mode, ctx) {
    var th = d.thresholds;
    var V = function (c) { return pv(c, mode); };
    var live = mode === "live";
    var rateBand = live ? { red: -1, yellow: -1 } : th.collections;

    var cols = [
      { key: "name", label: "Community", render: function (r) {
          return h("button", {
            className: "linkish",
            onClick: function () { ctx.open(r, "accounts"); },
            title: "Show accounts owing at " + r.name
          }, r.name); } },
      { key: "charged", label: "Charged", numeric: true,
        sortValue: function (r) { return V(r).charged; },
        render: function (r) { return money(V(r).charged); },
        group: function (t) { return money(t.charged); } },
      { key: "paid", label: "Collected", numeric: true,
        sortValue: function (r) { return V(r).paid; },
        render: function (r) { return money(V(r).paid); },
        group: function (t) { return money(t.paid); } },
      { key: "outstanding", label: "Still out", numeric: true,
        title: "Charged minus collected for this period",
        sortValue: function (r) { return V(r).outstanding; },
        render: function (r) { return money(V(r).outstanding); },
        group: function (t) { return money(t.outstanding); } },
      { key: "collection_pct", label: live ? "Rate MTD" : "Rate", numeric: true,
        sortValue: function (r) { return V(r).collection_pct; },
        render: function (r) {
          return V(r).charged
            ? h(Chip, { band: band(V(r).collection_pct, rateBand) }, pct(V(r).collection_pct))
            : "—"; },
        group: function (t) {
          return t.charged
            ? h(Chip, { band: band(t.collection_pct, rateBand) }, pct(t.collection_pct))
            : "—"; } },
      { key: "ar_0_30", label: "0–30", numeric: true,
        sortValue: function (r) { return V(r).ar_0_30; },
        render: function (r) { return money(V(r).ar_0_30); },
        group: function (t) { return money(t.ar_0_30); } },
      { key: "ar_31_60", label: "31–60", numeric: true,
        sortValue: function (r) { return V(r).ar_31_60; },
        render: function (r) { return money(V(r).ar_31_60); },
        group: function (t) { return money(t.ar_31_60); } },
      { key: "ar_61_90", label: "61–90", numeric: true,
        sortValue: function (r) { return V(r).ar_61_90; },
        render: function (r) { return money(V(r).ar_61_90); },
        group: function (t) { return money(t.ar_61_90); } },
      { key: "ar_90_plus", label: "90+", numeric: true,
        sortValue: function (r) { return V(r).ar_90_plus; },
        render: function (r) { return money(V(r).ar_90_plus); },
        group: function (t) { return money(t.ar_90_plus); } },
      { key: "ar_past_due_30plus", label: "Past due 30+", numeric: true,
        title: "Everything outside 0–30: money that is genuinely late",
        sortValue: function (r) { return V(r).ar_past_due_30plus; },
        render: function (r) {
          var x = V(r).ar_past_due_30plus;
          return h("span", { className: x > 40000 ? "down" : "" }, money(x)); },
        group: function (t) {
          return h("span", { className: t.ar_past_due_30plus > 100000 ? "down" : "" },
            money(t.ar_past_due_30plus)); } },
      { key: "ar_total", label: "Total AR", numeric: true,
        sortValue: function (r) { return V(r).ar_total; },
        render: function (r) { return money(V(r).ar_total); },
        group: function (t) { return money(t.ar_total); } },
      { key: "ar_accounts", label: "Accounts", numeric: true,
        sortValue: function (r) { return V(r).ar_accounts; },
        render: function (r) { return count(V(r).ar_accounts); },
        group: function (t) { return count(t.ar_accounts); } }
    ];

    var groups = groupByVehicle(d, filtered, mode);
    var sum = function (k) { return filtered.reduce(function (s, c) { return s + (V(c)[k] || 0); }, 0); };
    var charged = sum("charged"), paid = sum("paid");

    var segRows = (function () {
      var by = {}, amt = {};
      filtered.forEach(function (c) {
        (c.ar_segments || []).forEach(function (g) {
          by[g.segment] = (by[g.segment] || 0) + g.accounts;
          amt[g.segment] = (amt[g.segment] || 0) + g.past_due_30plus;
        });
      });
      return ["legal", "payment_plan", "former", "unclassified"]
        .filter(function (k) { return by[k]; })
        .map(function (k) {
          return { key: k, label: SEG_LABEL[k], n: by[k], money: amt[k], color: SEG_COLORS[k] };
        });
    })();

    return h("div", null,
      h(Panel, {
        title: "What is behind the balances",
        note: "Accounts owing, by where the balance already sits · amounts are past due 30+"
      }, h(BandBar, {
        rows: segRows, label: "Accounts owing by work bucket",
        note: "Rent Manager holds no eviction flag on the receivable, so this is built " +
              "from court fees posted and payment plan charges. In eviction, uncollectible " +
              "and former resident cannot be split properly without the eviction tracker " +
              "as a source, which is why most of this reads as not classified."
      })),

      h("section", { className: "panel" },
      h(GroupedTable, {
        title: "Aging by vehicle",
        note: (live
          ? "Live through " + monthLabel(d.period.live) + " day " + d.period.live_day +
            " · rent billed on the 1st is late after the " + d.period.grace_day + "th"
          : "Closed " + monthLabel(d.period.closed)) +
          " · click a community for the accounts owing",
        cols: cols, groups: groups,
        initialSort: { key: "ar_past_due_30plus", dir: -1 },
        footer: [
          "Portfolio", money(charged), money(paid), money(sum("outstanding")),
          charged ? pct(paid / charged * 100) : "—",
          money(sum("ar_0_30")), money(sum("ar_31_60")),
          money(sum("ar_61_90")), money(sum("ar_90_plus")),
          money(sum("ar_past_due_30plus")),
          money(sum("ar_total")), count(sum("ar_accounts"))
        ]
      })));
  }
  function VacancyTab(d, filtered, mode, ctx) {
    // Unit-type composition across the filtered set. The reason bar answers
    // "can I lease this"; the type table answers "what is it".
    var byType = {};
    filtered.forEach(function (c) {
      (c.vacancy_composition || []).forEach(function (v) {
        var t = byType[v.type] || (byType[v.type] = {
          type: v.type, group: v.group, bucket: v.bucket, units: 0, vacant: 0
        });
        t.units += v.units;
        t.vacant += v.vacant;
      });
    });
    var typeRows = Object.keys(byType).map(function (k) { return byType[k]; })
      .sort(function (a, b) { return b.vacant - a.vacant || b.units - a.units; });

    var reasonTotals = {};
    filtered.forEach(function (c) {
      (c.vacancy_by_reason || []).forEach(function (r) {
        var t = reasonTotals[r.reason] || (reasonTotals[r.reason] = {
          reason: r.reason, label: r.label, actionable: r.actionable, units: 0, rent_lost: 0
        });
        t.units += r.units;
        t.rent_lost += r.rent_lost || 0;
      });
    });
    var reasons = Object.keys(reasonTotals).map(function (k) { return reasonTotals[k]; })
      .sort(function (a, b) { return b.units - a.units; });

    var BUCKET_LABEL = {
      rentable: "Leasable now",
      rentable_impaired: "Needs work first",
      not_rentable: "Not leasable"
    };

    // Vacancy by community, so a park with a real backlog is visible without
    // opening all 66.
    var commRows = filtered.map(function (c) {
      var vd = c.vacancy_detail || [];
      var byR = {};
      vd.forEach(function (x) { byR[x.reason] = (byR[x.reason] || 0) + 1; });
      return {
        name: c.name, community: c, vehicle: c.vehicle,
        units: pv(c, mode).units,
        vacant: (c.vacancy_by_reason || []).reduce(function (a, r) { return a + r.units; }, 0),
        named: vd.length,
        vac_pct: pv(c, mode).units
          ? (c.vacancy_by_reason || []).reduce(function (a, r) { return a + r.units; }, 0)
            / pv(c, mode).units * 100 : 0,
        over90: (c.vacancy_aging || []).filter(function (a) {
          return ["91-180 days", "181-365 days", "Over a year"].indexOf(a.band) >= 0;
        }).reduce(function (a, x) { return a + x.units; }, 0),
        over365: (c.vacancy_aging || []).filter(function (a) { return a.band === "Over a year"; })
          .reduce(function (a, x) { return a + x.units; }, 0),
        home_available: byR.home_available || 0,
        in_rehab: byR.in_rehab || 0,
        pending_setup: byR.pending_setup || 0,
        rv_seasonal: byR.rv_seasonal || 0,
        vacant_lot: byR.vacant_lot || 0,
        not_leasable: byR.not_leasable || 0,
        rent_lost: vd.reduce(function (a, x) { return a + x.rent_lost; }, 0)
      };
    }).filter(function (r) { return r.vacant > 0 || r.named > 0; });

    var sumR = function (k) { return commRows.reduce(function (a, r) { return a + r[k]; }, 0); };

    return h("div", null,
      h(Panel, {
        title: "Where the vacancy actually is",
        note: "Proportion of vacant units by reason · unit-day weighted"
      }, h(ReasonBar, { rows: reasons, meta: d.reason_meta })),

      h("div", { className: "grid-2" },
        h(Panel, {
          title: "Vacancy aging",
          note: "Days since the unit's last move-out"
        }, h(BandBar, {
          rows: agingRows([].concat.apply([], filtered.map(function (c) { return c.vacancy_aging || []; }))),
          label: "Vacant units by age"
        })),
        h(Panel, {
          title: "Home pipeline",
          note: "Park-owned homes by Rent Manager asset status"
        }, h(BandBar, {
          rows: statusRows([].concat.apply([], filtered.map(function (c) { return c.home_status || []; }))),
          label: "Homes by status",
          note: "Rent Manager tracks Ordered through Rental. There is no separate " +
                "Ready to Market or punch stage, so those would need a new status or a " +
                "user-defined field before they can be reported."
        }))),

      h(Panel, {
        title: "Vacancy by community",
        note: "Click a community to see each vacant unit and why",
        flush: true
      }, h(SortableTable, {
        cols: [
          { key: "name", label: "Community", render: function (r) {
              return h("span", null,
                h("button", {
                  className: "linkish",
                  onClick: function () { ctx.open(r.community, "vacancy"); },
                  title: "Vacant units at " + r.name
                }, r.name), " ",
                h("span", { className: "tag" }, r.vehicle)); } },
          { key: "units", label: "Lots", numeric: true, render: function (r) { return count(r.units); } },
          { key: "vacant", label: "Vacant", numeric: true, render: function (r) { return count(r.vacant); } },
          { key: "vac_pct", label: "Vacant %", numeric: true,
            render: function (r) { return pct(r.vac_pct, 0); } },
          { key: "named", label: "Units listed", numeric: true,
            title: "How many of those the Rent Manager unit list can name today",
            render: function (r) {
              return r.named
                ? h("span", { style: r.named < r.vacant ? { color: "var(--text-muted)" } : null },
                    count(r.named))
                : h("span", { style: { color: "var(--text-muted)" } }, "—"); } },
          { key: "over90", label: "Empty 90+ days", numeric: true,
            title: "Vacant more than 90 days, where a move-out date is on record",
            render: function (r) {
              return r.over90
                ? h("span", { className: r.over90 >= 10 ? "down" : "" }, count(r.over90))
                : h("span", { style: { color: "var(--text-muted)" } }, "—"); } },
          { key: "home_available", label: "Homes avail", numeric: true,
            render: function (r) { return r.home_available || "—"; } },
          { key: "in_rehab", label: "In rehab", numeric: true,
            render: function (r) { return r.in_rehab || "—"; } },
          { key: "pending_setup", label: "Pending setup", numeric: true,
            render: function (r) { return r.pending_setup || "—"; } },
          { key: "rv_seasonal", label: "RV site", numeric: true,
            render: function (r) { return r.rv_seasonal || "—"; } },
          { key: "vacant_lot", label: "Ready lot", numeric: true,
            render: function (r) { return r.vacant_lot || "—"; } },
          { key: "not_leasable", label: "Not leasable", numeric: true,
            render: function (r) { return r.not_leasable || "—"; } },
          { key: "rent_lost", label: "Rent lost", numeric: true,
            render: function (r) { return money(r.rent_lost); } }
        ],
        rows: commRows, initialSort: { key: "vacant", dir: -1 },
        footer: [
          commRows.length + " communities with vacancy",
          count(sumR("units")), count(sumR("vacant")),
          sumR("units") ? pct(sumR("vacant") / sumR("units") * 100, 0) : "—",
          count(sumR("named")),
          count(sumR("over90")),
          count(sumR("home_available")), count(sumR("in_rehab")),
          count(sumR("pending_setup")), count(sumR("rv_seasonal")),
          count(sumR("vacant_lot")), count(sumR("not_leasable")),
          money(sumR("rent_lost"))
        ]
      })),

      h(Panel, {
        title: "Vacancy composition by unit type",
        note: "Every unit type in the portfolio and how much of it sits empty",
        flush: true
      }, h(SortableTable, {
        cols: [
          { key: "type", label: "Unit type" },
          { key: "group", label: "Class" },
          { key: "bucket", label: "Standing", render: function (r) {
              return h("span", {
                className: "chip " + (r.bucket === "rentable" ? "good"
                  : r.bucket === "rentable_impaired" ? "watch" : "critical")
              }, BUCKET_LABEL[r.bucket] || r.bucket); } },
          { key: "units", label: "Lots", numeric: true, render: function (r) { return count(r.units); } },
          { key: "vacant", label: "Vacant", numeric: true, render: function (r) { return count(r.vacant); } },
          { key: "fill", label: "Filled", numeric: true,
            sortValue: function (r) { return r.units ? (r.units - r.vacant) / r.units : 0; },
            render: function (r) { return r.units ? pct((r.units - r.vacant) / r.units * 100, 0) : "—"; } }
        ],
        rows: typeRows, initialSort: { key: "vacant", dir: -1 }
      })));
  }
  function FinancialsTab(d, filtered, mode, ctx) {
    var th = d.thresholds;
    // Always the closed month. The general ledger does not post intra-month, so
    // an open-month revenue or NOI figure would read as a collapse to zero.
    var V = function (c) { return c.closed; };
    var E = function (c) { return c.expenses || {}; };

    var sum = function (k) { return filtered.reduce(function (a, c) { return a + (V(c)[k] || 0); }, 0); };
    var sumE = function (k) { return filtered.reduce(function (a, c) { return a + (E(c)[k] || 0); }, 0); };
    var rev = sum("revenue"), noi = sum("noi");
    var revB = sum("revenue_budget"), noiB = sum("noi_budget");
    var opex = sum("opex");
    var ctrl = sumE("controllable"), nonCtrl = sumE("non_controllable");
    var util = sumE("utilities"), utilInc = sumE("utility_reimbursements");
    var recapture = util ? utilInc / util * 100 : null;
    var target = 80;

    var cols = [
      { key: "name", label: "Community", render: function (r) {
          return h("button", {
            className: "linkish",
            onClick: function () { ctx.open(r, "pl"); },
            title: "Line-item P&L for " + r.name
          }, r.name); } },
      { key: "revenue", label: "Revenue", numeric: true,
        sortValue: function (r) { return V(r).revenue; },
        render: function (r) { return money(V(r).revenue); },
        group: function (t) { return money(t.revenue); } },
      { key: "controllable", label: "Controllable", numeric: true,
        title: "Total operating expense less utilities, taxes and insurance",
        sortValue: function (r) { return E(r).controllable; },
        render: function (r) { return money(E(r).controllable); },
        group: function (t) { return money(t.controllable); } },
      { key: "repairs_maintenance", label: "R&M", numeric: true,
        sortValue: function (r) { return E(r).repairs_maintenance; },
        render: function (r) { return money(E(r).repairs_maintenance); },
        group: function () { return ""; } },
      { key: "non_controllable", label: "Non-controllable", numeric: true,
        title: "Utilities, property taxes and insurance",
        sortValue: function (r) { return E(r).non_controllable; },
        render: function (r) { return money(E(r).non_controllable); },
        group: function (t) { return money(t.non_controllable); } },
      { key: "utility_recapture_pct", label: "Utility recapture", numeric: true,
        title: "Utility income billed back over utility expense",
        sortValue: function (r) { return E(r).utility_recapture_pct == null ? -1 : E(r).utility_recapture_pct; },
        render: function (r) {
          var v = E(r).utility_recapture_pct;
          return v == null ? "—"
            : h(Chip, { band: v >= target ? "good" : v >= 50 ? "watch" : "critical" }, pct(v, 0)); },
        group: function (t) {
          return t.utility_recapture_pct == null ? "—"
            : h(Chip, { band: t.utility_recapture_pct >= target ? "good"
                        : t.utility_recapture_pct >= 50 ? "watch" : "critical" },
                pct(t.utility_recapture_pct, 0)); } },
      { key: "noi", label: "NOI", numeric: true,
        sortValue: function (r) { return V(r).noi; },
        render: function (r) { return money(V(r).noi); },
        group: function (t) { return money(t.noi); } },
      { key: "noi_var", label: "NOI vs budget", numeric: true,
        sortValue: function (r) { return V(r).noi_budget ? V(r).noi - V(r).noi_budget : 0; },
        render: function (r) {
          if (!V(r).noi_budget) return "—";
          var v = V(r).noi - V(r).noi_budget;
          return h("span", { className: v >= 0 ? "up" : "down" },
            (v >= 0 ? "+" : "−") + money(Math.abs(v))); },
        group: function (t) {
          if (!t.noi_budget) return "—";
          var v = t.noi - t.noi_budget;
          return h("span", { className: v >= 0 ? "up" : "down" },
            (v >= 0 ? "+" : "−") + money(Math.abs(v))); } },
      { key: "noi_margin", label: "Margin", numeric: true,
        sortValue: function (r) { return V(r).noi_margin; },
        render: function (r) {
          return V(r).revenue >= 5000
            ? h(Chip, { band: band(V(r).noi_margin, th.noi_margin) }, pct(V(r).noi_margin, 0)) : "—"; },
        group: function (t) {
          return t.revenue
            ? h(Chip, { band: band(t.noi_margin, th.noi_margin) }, pct(t.noi_margin, 0)) : "—"; } },
      { key: "ytd_noi", label: "YTD NOI", numeric: true,
        sortValue: function (r) { return V(r).ytd_noi; },
        render: function (r) { return money(V(r).ytd_noi); },
        group: function () { return ""; } }
    ];

    var groups = groupByVehicle(d, filtered, mode);

    return h("div", null,
      h("div", { className: "grid-2" },
        h(Panel, {
          title: "Controllable against non-controllable",
          note: "Closed " + monthLabel(d.period.closed) + " · " + money(opex) + " of operating expense"
        },
          h("div", { className: "split-bar" },
            h("span", { style: { width: (opex ? ctrl / opex * 100 : 50) + "%", background: GREEN },
                        title: "Controllable " + money(ctrl) },
              opex && ctrl / opex > 0.16 ? pct(ctrl / opex * 100, 0) : ""),
            h("span", { style: { width: (opex ? nonCtrl / opex * 100 : 50) + "%", background: NAVY },
                        title: "Non-controllable " + money(nonCtrl) },
              opex && nonCtrl / opex > 0.16 ? pct(nonCtrl / opex * 100, 0) : "")),
          h("div", { className: "reason-legend" },
            h("div", { className: "rl" },
              h("span", { className: "swatch", style: { background: GREEN } }),
              h("span", null, h("span", { className: "rl-n" }, money(ctrl)), " controllable",
                h("span", { className: "rl-sub" }, "  R&M " + money(sumE("repairs_maintenance")) +
                  " · payroll " + money(sumE("payroll_management")) +
                  " · legal " + money(sumE("legal_professional")) +
                  " · other " + money(sumE("other_controllable"))))),
            h("div", { className: "rl" },
              h("span", { className: "swatch", style: { background: NAVY } }),
              h("span", null, h("span", { className: "rl-n" }, money(nonCtrl)), " non-controllable",
                h("span", { className: "rl-sub" }, "  utilities " + money(util) +
                  " · taxes " + money(sumE("taxes")) +
                  " · insurance " + money(sumE("insurance"))))))),

        h(Panel, {
          title: "Utility recapture",
          note: "Billed back against spend · target " + target + "%"
        },
          h("div", { className: "bignum",
                     style: { color: recapture == null ? "var(--text-muted)"
                              : recapture >= target ? GREEN : recapture >= 50 ? YELLOW : RED } },
            recapture == null ? "—" : pct(recapture, 0)),
          h("div", { className: "ksub" },
            money(utilInc) + " recovered of " + money(util) + " spent"),
          h("div", { className: "split-bar", style: { marginTop: "12px" } },
            h("span", { style: { width: Math.min(100, recapture || 0) + "%", background: GREEN },
                        title: "Recovered " + money(utilInc) }, ""),
            h("span", { style: { width: Math.max(0, 100 - Math.min(100, recapture || 0)) + "%",
                                 background: RED }, title: "Absorbed " + money(util - utilInc) }, "")),
          h("div", { className: "reason-legend" },
            h("div", { className: "rl" },
              h("span", { className: "swatch", style: { background: RED } }),
              h("span", null,
                h("span", { className: "rl-n" }, money(util - utilInc)),
                " absorbed by the portfolio each month",
                h("span", { className: "rl-sub" },
                  "  a metering and pricing question, not a controllable expense"))),
            (function () {
              var recov = filtered.filter(function (c) {
                return (c.utilities_service || {}).recoverable;
              });
              var rs = recov.reduce(function (a, c) { return a + (E(c).utilities || 0); }, 0);
              var ri = recov.reduce(function (a, c) { return a + (E(c).utility_reimbursements || 0); }, 0);
              return h("div", { className: "rl" },
                h("span", { className: "swatch", style: { background: GREEN } }),
                h("span", null,
                  h("span", { className: "rl-n" }, rs ? pct(ri / rs * 100, 0) : "—"),
                  " across the " + recov.length + " communities that bill residents",
                  h("span", { className: "rl-sub" },
                    "  " + (filtered.length - recov.length) + " pay their own utilities, so they " +
                    "have nothing to recover")));
            })()))),

      h(Panel, {
        title: "Why recapture is where it is",
        note: "A community that pays its own utilities has nothing to bill back, so a low rate there is the design and not a failure",
        flush: true
      }, h(SortableTable, {
        cols: [
          { key: "name", label: "Community", render: function (r) {
              return h("button", { className: "linkish",
                                   onClick: function () { ctx.open(r.community, "pl"); } }, r.name); } },
          { key: "recoverable", label: "Billable back", numeric: false,
            title: "Whether any of water, sewer or trash is paid by the resident",
            sortValue: function (r) { return r.recoverable ? 1 : 0; },
            render: function (r) {
              return h("span", { className: "chip " + (r.recoverable ? "good" : "watch") },
                r.recoverable ? "Yes" : "Community pays"); } },
          { key: "water", label: "Water", render: function (r) {
              return r.u.water_service + (r.u.water_paid_by ? " · " + r.u.water_paid_by : ""); } },
          { key: "sewer", label: "Sewer", render: function (r) {
              return r.u.sewer_service + (r.u.sewer_paid_by ? " · " + r.u.sewer_paid_by : ""); } },
          { key: "trash", label: "Trash", render: function (r) { return r.u.trash_paid_by || "—"; } },
          { key: "spend", label: "Utility spend", numeric: true,
            render: function (r) { return money(r.spend); } },
          { key: "recovered", label: "Billed back", numeric: true,
            render: function (r) { return money(r.recovered); } },
          { key: "rate", label: "Recapture", numeric: true,
            sortValue: function (r) { return r.rate == null ? -1 : r.rate; },
            render: function (r) {
              if (r.rate == null) return "—";
              // Only band a community that is supposed to be recovering.
              if (!r.recoverable) {
                return h("span", { style: { color: "var(--text-muted)" } }, pct(r.rate, 0));
              }
              return h(Chip, { band: r.rate >= target ? "good" : r.rate >= 50 ? "watch" : "critical" },
                pct(r.rate, 0)); } },
          { key: "net", label: "Absorbed", numeric: true,
            title: "Utility income minus utility spend",
            render: function (r) {
              return h("span", { className: r.net < 0 ? "down" : "up" }, money(r.net)); } }
        ],
        rows: filtered.map(function (c) {
          var e = E(c), u = c.utilities_service || {};
          return { name: c.name, community: c, u: u, recoverable: !!u.recoverable,
                   spend: e.utilities || 0, recovered: e.utility_reimbursements || 0,
                   rate: e.utility_recapture_pct, net: e.utility_net || 0 };
        }).filter(function (r) { return r.spend || r.recovered; }),
        initialSort: { key: "net", dir: 1 }
      })),

      h("div", { className: "grid-2" },
        h(Panel, { title: "Revenue against budget",
                   note: d.period.budget_from
                     ? "Actual versus plan · budget loaded from " + monthLabel(d.period.budget_from)
                     : "Actual versus plan, by closed month" },
          h(LineChart, {
            series: closedOnly(d.trends.financials), zeroBase: false, height: 230,
            lines: [{ key: "revenue", color: GREEN, area: true },
                    { key: "revenue_budget", color: NAVY }],
            fmtTick: function (v) { return "$" + (v / 1e6).toFixed(1) + "M"; },
            fmtPoint: function (v) { return "$" + (v / 1e6).toFixed(2) + "M"; },
            ariaLabel: "Revenue versus budget by month"
          }),
          h("div", { className: "legend" },
            h("span", null, h("i", { style: { background: GREEN } }), "Actual"),
            h("span", null, h("i", { style: { background: NAVY } }), "Budget"))),
        h(Panel, { title: "NOI against budget",
                   note: "Excludes debt service, CapEx and depreciation" +
                     (d.period.budget_from ? " · budget from " + monthLabel(d.period.budget_from) : "") },
          h(LineChart, {
            series: closedOnly(d.trends.financials), zeroBase: false, height: 230,
            lines: [{ key: "noi", color: GREEN, area: true },
                    { key: "noi_budget", color: NAVY }],
            fmtTick: function (v) { return "$" + (v / 1e6).toFixed(1) + "M"; },
            fmtPoint: function (v) { return "$" + (v / 1e6).toFixed(2) + "M"; },
            ariaLabel: "NOI versus budget by month"
          }),
          h("div", { className: "legend" },
            h("span", null, h("i", { style: { background: GREEN } }), "Actual"),
            h("span", null, h("i", { style: { background: NAVY } }), "Budget")))),

      h("section", { className: "panel" },
        h(GroupedTable, {
          title: "P&L by vehicle",
          note: "Closed " + monthLabel(d.period.closed) +
                " · click a community for its line items, month and year to date",
          cols: cols, groups: groups,
          initialSort: { key: "noi", dir: -1 },
          footer: [
            "Portfolio", money(rev), money(ctrl), money(sumE("repairs_maintenance")),
            money(nonCtrl), recapture == null ? "—" : pct(recapture, 0),
            money(noi),
            noiB ? ((noi - noiB >= 0 ? "+" : "−") + money(Math.abs(noi - noiB))) : "—",
            rev ? pct(noi / rev * 100, 0) : "—",
            money(sum("ytd_noi"))
          ]
        })));
  }
  function Exceptions(props) {
    var st = useState(false);
    var open = st[0], setOpen = st[1];
    var flags = props.flags || [];
    if (!flags.length) return null;
    var warns = flags.filter(function (f) { return f.severity === "warn"; }).length;
    var infos = flags.length - warns;

    return h("div", { className: "exceptions no-print" },
      h("button", {
        className: "exceptions-head", onClick: function () { setOpen(!open); },
        "aria-expanded": open ? "true" : "false"
      },
        h("span", { className: "caret" }, open ? "▼" : "▶"),
        h("strong", null, "Data notes"),
        warns ? h("span", { className: "pill-count warn" }, warns + " needs a look") : null,
        infos ? h("span", { className: "pill-count info" }, infos + " for context") : null,
        h("span", { className: "spacer" }),
        h("span", { style: { color: "var(--text-muted)", fontSize: "11.5px" } },
          open ? "Hide" : "Read before acting on these numbers")),
      open ? h("div", { className: "exception-list" }, flags.map(function (f, i) {
        return h("div", { className: "exception " + f.severity, key: i },
          h("div", { className: "stripe" }),
          h("div", { className: "body" },
            h("div", { className: "etitle" }, f.title),
            h("div", { className: "edetail" }, f.detail)));
      })) : null);
  }

  // -------------------------------------------------------------------- app ---

  var TABS = [
    { id: "overview", label: "Overview", render: OverviewTab },
    { id: "communities", label: "Communities", render: CommunitiesTab },
    { id: "occupancy", label: "Occupancy", render: OccupancyTab },
    { id: "collections", label: "Collections & AR", render: CollectionsTab },
    { id: "vacancy", label: "Vacancy", render: VacancyTab },
    { id: "financials", label: "Financials", render: FinancialsTab }
  ];

  function App(props) {
    var d = props.data;
    var ts = useState("overview");
    var tab = ts[0], setTab = ts[1];
    // Default to Live: past the grace day the open month is the actionable
    // view, and it is what someone opening this mid-month wants to see.
    var ms = useState(d.period.live_day >= d.period.grace_day ? "live" : "closed");
    var mode = ms[0], setMode = ms[1];
    var fs = useState({ kind: "all", search: "", size: "all", vehicle: "all" });
    var filters = fs[0], setFilters = fs[1];
    // The open drill-in: which community, and which of its views.
    var ds = useState(null);
    var drill = ds[0], setDrill = ds[1];
    var ctx = {
      open: function (community, view) { setDrill({ community: community, view: view || "rentroll" }); },
      close: function () { setDrill(null); }
    };

    var filtered = useMemo(function () {
      return d.communities.filter(function (c) {
        if (filters.kind !== "all" && c.kind !== filters.kind) return false;
        if (filters.vehicle !== "all" && (c.vehicle || "Unassigned") !== filters.vehicle) return false;
        var u = pv(c, mode).units || 0;
        if (filters.size === "large" && u < 100) return false;
        if (filters.size === "small" && u >= 100) return false;
        if (filters.search) {
          var q = filters.search.toLowerCase();
          if (c.name.toLowerCase().indexOf(q) === -1 &&
              String(c.park).toLowerCase().indexOf(q) === -1 &&
              String(c.short_name).toLowerCase().indexOf(q) === -1) return false;
        }
        return true;
      });
    }, [d.communities, filters.kind, filters.search, filters.size, filters.vehicle, mode]);

    var p = d.portfolio[mode], th = d.thresholds;
    var closedP = d.portfolio.closed;
    var live = mode === "live";
    var active = TABS.filter(function (t) { return t.id === tab; })[0];
    var showFilters = tab !== "overview";

    var kinds = {};
    d.communities.forEach(function (c) { kinds[c.kind] = 1; });
    // Vehicles ordered biggest first, matching how the tables group them.
    var vehicleOpts = (d.vehicles || []).map(function (v) { return v.vehicle; });
    if (!vehicleOpts.length) {
      var seen = {};
      d.communities.forEach(function (c) { seen[c.vehicle || "Unassigned"] = 1; });
      vehicleOpts = Object.keys(seen).sort();
    }

    return h("div", { className: "wrap" },
      h("header", { className: "masthead" },
        h("div", { className: "brand" },
          window.__PK_LOGO__
            ? h("img", { src: window.__PK_LOGO__, alt: "Parakeet Communities" })
            : null,
          window.__PK_LOGO__ ? h("div", { className: "rule" }) : null,
          h("div", null,
            h("h1", null, "Property Operations"),
            h("div", { className: "sub" },
              p.communities + " reportable communities · " + count(p.total_units) +
              " lots · " + monthLabel(d.period[live ? "live" : "closed"]) +
              (live ? " through day " + d.period.live_day : " closed")))),
        h(PeriodToggle, { data: d, mode: mode, onChange: setMode })),

      h(Exceptions, { flags: d.flags }),

      h("div", { className: "kpis" },
        h(Kpi, {
          label: "Occupancy",
          value: pct(p.occupancy),
          color: bandColor(band(p.occupancy, th.occupancy)),
          sub: count(p.total_occupied) + " of " + count(p.total_units) + " lots"
        }, h(Delta, { curr: p.occupancy, prev: p.occupancy_prev, unit: "pt",
                      suffix: live ? "vs " + monthLabel(d.period.closed) : "vs prior month" })),

        live
          ? h(Kpi, {
              label: "Billed, still out",
              value: money(p.outstanding, { compact: true }),
              color: YELLOW,
              sub: money(p.paid, { compact: true }) + " of " + money(p.charged, { compact: true }) +
                   " collected · day " + d.period.live_day + " of " + d.period.days_in_live
            }, h("div", { className: "kdelta flat" },
                h("span", { style: { fontWeight: 500, color: "var(--text-muted)" } },
                  pct(p.collection_pct) + " month to date")))
          : h(Kpi, {
              label: "Collections",
              value: pct(p.collection_pct),
              color: bandColor(band(p.collection_pct, th.collections)),
              sub: money(p.paid, { compact: true }) + " of " + money(p.charged, { compact: true })
            }, h("div", { className: "kdelta flat" },
                h("span", { style: { fontWeight: 500, color: "var(--text-muted)" } },
                  pct(p.collection_ttm) + " trailing 12-month"))),

        h(Kpi, {
          label: "Past due 30+",
          value: money(p.ar_past_due_30plus, { compact: true }),
          color: RED,
          sub: "everything outside the 0–30 bucket"
        }, h(Delta, { curr: p.ar_past_due_30plus, prev: closedP.ar_past_due_30plus, money: true,
                      invert: true,
                      suffix: live ? "vs " + monthLabel(d.period.closed) + " close" : "vs prior month",
                      fallback: " " })),

        h(Kpi, {
          label: "90+ days",
          value: money(p.ar_90_plus, { compact: true }),
          color: bandColor(band(p.ar_over90_share, th.over90_share, true)),
          sub: pct(p.ar_over90_share, 0) + " of " + money(p.ar_total, { compact: true }) + " total AR"
        }),

        h(Kpi, {
          label: "NOI",
          value: money(closedP.noi, { compact: true }),
          color: closedP.noi_budget && closedP.noi < closedP.noi_budget ? RED : GREEN,
          sub: closedP.noi_budget
            ? (closedP.noi >= closedP.noi_budget ? "ahead of " : "behind ") +
              money(closedP.noi_budget, { compact: true }) + " budget"
            : "no budget loaded"
        }, h("div", { className: "kdelta flat" },
            h("span", { style: { fontWeight: 500, color: "var(--text-muted)" } },
              pct(closedP.noi_margin, 0) + " margin · closed " + monthLabel(d.period.closed)))),

        h(Kpi, {
          label: "Vacant, not leasable",
          value: count(p.not_rentable_units + p.impaired_units),
          color: YELLOW,
          sub: count(p.impaired_units) + " need rehab · " + count(p.not_rentable_units) +
               " demo or unusable"
        })),

      h("div", { className: "tabs", role: "tablist" }, TABS.map(function (t) {
        return h("button", {
          key: t.id, className: "tab", role: "tab", id: "tab-" + t.id,
          "aria-selected": tab === t.id ? "true" : "false",
          onClick: function () { setTab(t.id); }
        }, t.label);
      })),

      showFilters ? h("div", { className: "controls no-print" },
        h("div", { className: "field" },
          h("label", { htmlFor: "f-search" }, "Find"),
          h("input", {
            id: "f-search", type: "search", placeholder: "Community, park or code",
            value: filters.search,
            onChange: function (e) {
              var v = e.target.value;
              setFilters(function (f) { return Object.assign({}, f, { search: v }); });
            }
          })),
        h("div", { className: "field" },
          h("label", { htmlFor: "f-vehicle" }, "Vehicle"),
          h("select", {
            id: "f-vehicle", value: filters.vehicle,
            onChange: function (e) {
              var v = e.target.value;
              setFilters(function (f) { return Object.assign({}, f, { vehicle: v }); });
            }
          }, [h("option", { key: "all", value: "all" }, "All vehicles")].concat(
            vehicleOpts.map(function (k) {
              return h("option", { key: k, value: k }, k);
            })))),
        h("div", { className: "field" },
          h("label", { htmlFor: "f-kind" }, "Type"),
          h("select", {
            id: "f-kind", value: filters.kind,
            onChange: function (e) {
              var v = e.target.value;
              setFilters(function (f) { return Object.assign({}, f, { kind: v }); });
            }
          }, [h("option", { key: "all", value: "all" }, "All types")].concat(
            Object.keys(kinds).sort().map(function (k) {
              return h("option", { key: k, value: k }, k);
            })))),
        h("div", { className: "field" },
          h("label", { htmlFor: "f-size" }, "Size"),
          h("select", {
            id: "f-size", value: filters.size,
            onChange: function (e) {
              var v = e.target.value;
              setFilters(function (f) { return Object.assign({}, f, { size: v }); });
            }
          },
            h("option", { value: "all" }, "All sizes"),
            h("option", { value: "large" }, "100+ lots"),
            h("option", { value: "small" }, "Under 100 lots"))),
        h("div", { className: "spacer" }),
        h("div", { className: "count-note" },
          filtered.length === d.communities.length
            ? "Showing all " + d.communities.length + " communities"
            : "Showing " + filtered.length + " of " + d.communities.length)) : null,

      h("div", { role: "tabpanel", "aria-labelledby": "tab-" + tab },
        active.render(d, filtered, mode, ctx)),

      drill ? h(CommunityDrill, {
        community: drill.community, data: d, mode: mode,
        view: drill.view, onClose: ctx.close
      }) : null,

      h("footer", { className: "foot" },
        h("div", null, "Source: ", d.source, " · built ",
          new Date(d.generated_at).toLocaleString("en-US", {
            dateStyle: "medium", timeStyle: "short"
          })),
        h("div", null, "Parakeet Communities · internal · schema v" + d.schema_version)));
  }

  // ------------------------------------------------------------------- boot ---

  function mount(data) {
    var root = document.getElementById("root");
    if (!data || !data.communities) {
      root.innerHTML = '<div class="errorbox">Dashboard data missing or malformed.</div>';
      return;
    }
    ReactDOM.createRoot(root).render(h(App, { data: data }));
  }

  window.__PK_MOUNT__ = mount;

  if (window.__DASHBOARD_DATA__) {
    mount(window.__DASHBOARD_DATA__);
  }
})();
