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
    series.forEach(function (p) {
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
    var y = function (v) { return padT + (1 - (v - min) / (max - min)) * (H - padT - padB); };

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
      var pts = [];
      series.forEach(function (p, i) {
        if (p[l.key] != null) pts.push([x(i), y(p[l.key])]);
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

      // Emphasize the final reading: the figure the headline quotes.
      var last = pts[pts.length - 1];
      kids.push(h("circle", { key: "e" + li, cx: last[0], cy: last[1], r: 3.2, fill: l.color }));
      if (li === 0) {
        var lastVal = null;
        for (var i = series.length - 1; i >= 0; i--) {
          if (series[i][l.key] != null) { lastVal = series[i][l.key]; break; }
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
      }, monthShort(series[i].month)));
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
    var padL = 58, padR = 16, padT = 20, padB = 28;

    if (!series.length) return h("div", { ref: ref, className: "loading" }, "No data.");

    var keys = props.keys;
    var totals = series.map(function (p) {
      return keys.reduce(function (s, k) { return s + (p[k.key] || 0); }, 0);
    });
    var max = Math.max.apply(null, totals) * 1.12 || 1;

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
        var y0 = y(acc + v), y1 = y(acc);
        kids.push(h("rect", {
          key: "b" + i + "_" + ki, x: cx - bw / 2, y: y0, width: bw,
          height: Math.max(0.6, y1 - y0), fill: k.color
        }));
        acc += v;
      });
    });

    kids.push(h("line", { key: "ax", className: "axis-line", x1: padL, x2: W - padR, y1: H - padB, y2: H - padB }));

    // Label as many months as fit without collisions.
    var step = Math.max(1, Math.ceil((FS_AXIS * 3.4) / band));
    series.forEach(function (p, i) {
      if (i % step !== 0 && i !== series.length - 1) return;
      kids.push(h("text", {
        key: "xl" + i, x: padL + band * i + band / 2, y: H - padB + FS_AXIS + 6,
        textAnchor: "middle", style: { fontSize: FS_AXIS + "px" }
      }, monthShort(p.month)));
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
        h("div", { className: "bname", title: r.label }, r.label),
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

  function OverviewTab(d) {
    var p = d.portfolio, t = d.trends, th = d.thresholds;
    var closedAr = t.ar.filter(function (x) { return !x.partial; });
    var closedColl = t.collections.filter(function (x) { return !x.partial; });

    // Where the pain is: worst occupancy and biggest 90+ balances.
    var zeroCount = d.communities.filter(function (c) {
      return c.units >= 20 && c.occupancy === 0;
    }).length;
    var worstOcc = d.communities.slice()
      .filter(function (c) { return c.units >= 20 && c.occupancy > 0; })
      .sort(function (a, b) { return a.occupancy - b.occupancy; }).slice(0, 8)
      .map(function (c) {
        return { label: c.name, value: c.occupancy, display: pct(c.occupancy),
                 color: bandColor(band(c.occupancy, th.occupancy)) };
      });

    var worstAr = d.communities.slice()
      .sort(function (a, b) { return b.ar_90_plus - a.ar_90_plus; }).slice(0, 8)
      .map(function (c) {
        return { label: c.name, value: c.ar_90_plus, display: money(c.ar_90_plus, { compact: true }),
                 color: c.ar_90_plus > 100000 ? RED : c.ar_90_plus > 40000 ? YELLOW : GREEN };
      });

    return h("div", null,
      h("div", { className: "grid-2" },
        h(Panel, {
          title: "Portfolio occupancy",
          note: "Weighted by unit-days · closed months"
        }, h(LineChart, {
          series: closedOnly(t.occupancy), zeroBase: false, height: 230,
          lines: [{ key: "occupancy", color: GREEN, area: true }],
          fmtTick: function (v) { return v.toFixed(0) + "%"; },
          fmtPoint: function (v) { return v.toFixed(1) + "%"; },
          ariaLabel: "Portfolio occupancy by month"
        })),
        h(Panel, {
          title: "Collections rate",
          note: "Payments ÷ charges · closed months"
        }, h(LineChart, {
          series: closedOnly(t.collections), zeroBase: false, height: 230,
          lines: [{ key: "collection_pct", color: NAVY, area: true }],
          fmtTick: function (v) { return v.toFixed(0) + "%"; },
          fmtPoint: function (v) { return v.toFixed(1) + "%"; },
          ariaLabel: "Collection rate by month"
        }))),

      h(Panel, {
        title: "Receivables by age",
        note: "Closed months · the 90+ band is the one that compounds"
      },
        h(StackedBars, {
          series: closedOnly(t.ar), height: 250,
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
          h("span", null, h("i", { style: { background: RED } }), "90+"))),

      h("div", { className: "grid-2" },
        h(Panel, {
          title: "Lowest occupancy",
          note: zeroCount
            ? "20+ lot communities · " + zeroCount + " reporting exactly 0% held back, see data notes"
            : "20+ lot communities"
        }, h(BarList, { rows: worstOcc, max: 100 })),
        h(Panel, { title: "Largest 90+ balances", note: "As of " + monthLabel(d.period.headline) },
          h(BarList, { rows: worstAr }))));
  }

  function CommunitiesTab(d, filtered) {
    var th = d.thresholds;
    var cols = [
      { key: "name", label: "Community", render: function (r) {
          return h("span", null, r.name, " ",
            h("span", { className: "tag" }, r.kind)); } },
      { key: "units", label: "Lots", numeric: true, render: function (r) { return count(r.units); } },
      { key: "occupancy", label: "Occupancy", numeric: true, render: function (r) {
          return h(Chip, { band: band(r.occupancy, th.occupancy) }, pct(r.occupancy)); } },
      { key: "occupancy_rentable", label: "Occ (rentable)", numeric: true,
        title: "Occupancy with unusable and demo lots out of the denominator",
        render: function (r) { return pct(r.occupancy_rentable); } },
      { key: "collection_pct", label: "Collections", numeric: true,
        title: "Blank where nothing was charged, which is an absent ledger rather than a 0% rate",
        render: function (r) {
          return r.charged
            ? h(Chip, { band: band(r.collection_pct, th.collections) }, pct(r.collection_pct))
            : "—"; } },
      { key: "ar_total", label: "AR", numeric: true, render: function (r) { return money(r.ar_total, { compact: true }); } },
      { key: "ar_90_plus", label: "90+", numeric: true, render: function (r) { return money(r.ar_90_plus, { compact: true }); } },
      { key: "ar_over90_share", label: "90+ share", numeric: true, render: function (r) {
          return h(Chip, { band: band(r.ar_over90_share, th.over90_share, true) }, pct(r.ar_over90_share, 0)); } },
      { key: "ar_per_unit", label: "AR / lot", numeric: true, render: function (r) { return money(r.ar_per_unit); } },
      { key: "noi", label: "NOI", numeric: true, render: function (r) { return money(r.noi, { compact: true }); } },
      { key: "noi_margin", label: "NOI margin", numeric: true,
        title: "Only shown where monthly revenue clears $5K; below that the ratio is noise",
        render: function (r) {
          return r.revenue >= 5000
            ? h(Chip, { band: band(r.noi_margin, th.noi_margin) }, pct(r.noi_margin, 0)) : "—"; } },
      { key: "move_ins", label: "In / Out", numeric: true,
        sortValue: function (r) { return r.move_ins - r.move_outs; },
        render: function (r) { return r.move_ins + " / " + r.move_outs; } }
    ];

    var sum = function (k) { return filtered.reduce(function (s, c) { return s + (c[k] || 0); }, 0); };
    var units = sum("units");
    var occW = units ? filtered.reduce(function (s, c) { return s + c.occupancy * c.units; }, 0) / units : 0;
    var charged = sum("charged"), paid = sum("paid");
    var arTot = sum("ar_total"), ar90 = sum("ar_90_plus");
    var rev = sum("revenue"), noi = sum("noi");

    return h("div", null,
      h(Panel, {
        title: filtered.length + " communities",
        note: "Every figure as of closed " + monthLabel(d.period.headline) + " · click a heading to sort",
        flush: true
      }, h(SortableTable, {
        cols: cols, rows: filtered,
        initialSort: { key: "occupancy", dir: 1 },
        footer: [
          "Total / weighted",
          count(units),
          pct(occW),
          "—",
          charged ? pct(paid / charged * 100) : "—",
          money(arTot, { compact: true }),
          money(ar90, { compact: true }),
          arTot ? pct(ar90 / arTot * 100, 0) : "—",
          units ? money(arTot / units) : "—",
          money(noi, { compact: true }),
          rev ? pct(noi / rev * 100, 0) : "—",
          sum("move_ins") + " / " + sum("move_outs")
        ]
      })));
  }

  function OccupancyTab(d, filtered) {
    var th = d.thresholds;
    var mh = filtered.filter(function (c) { return c.kind === "MH"; });
    var rv = filtered.filter(function (c) { return c.kind === "RV"; });

    function wavg(rows) {
      var u = rows.reduce(function (s, c) { return s + c.units; }, 0);
      return u ? rows.reduce(function (s, c) { return s + c.occupancy * c.units; }, 0) / u : 0;
    }

    var byPark = {};
    filtered.forEach(function (c) {
      if (!byPark[c.park]) byPark[c.park] = { park: c.park, units: 0, occupied: 0 };
      byPark[c.park].units += c.units;
      byPark[c.park].occupied += c.occupied;
    });
    var parks = Object.keys(byPark).map(function (k) { return byPark[k]; })
      .filter(function (p) { return p.units >= 20; })
      .map(function (p) {
        var o = p.units ? p.occupied / p.units * 100 : 0;
        return { label: p.park, value: o, display: pct(o), color: bandColor(band(o, th.occupancy)) };
      }).sort(function (a, b) { return a.value - b.value; });

    return h("div", null,
      h("div", { className: "grid-3" },
        h(Panel, { title: "MH occupancy", note: count(mh.length) + " communities" },
          h("div", { className: "kvalue", style: { fontSize: "30px", fontWeight: 800 } }, pct(wavg(mh))),
          h("div", { className: "ksub" }, count(mh.reduce(function (s, c) { return s + c.units; }, 0)) + " lots")),
        h(Panel, { title: "RV occupancy", note: count(rv.length) + " communities" },
          h("div", { className: "kvalue", style: { fontSize: "30px", fontWeight: 800 } }, pct(wavg(rv))),
          h("div", { className: "ksub" }, count(rv.reduce(function (s, c) { return s + c.units; }, 0)) + " lots")),
        h(Panel, { title: "Move-ins vs move-outs", note: monthLabel(d.period.headline) },
          h("div", { className: "kvalue", style: { fontSize: "30px", fontWeight: 800 } },
            (function () {
              var net = filtered.reduce(function (s, c) { return s + c.move_ins - c.move_outs; }, 0);
              return (net > 0 ? "+" : "") + net;
            })()),
          h("div", { className: "ksub" },
            filtered.reduce(function (s, c) { return s + c.move_ins; }, 0) + " in, " +
            filtered.reduce(function (s, c) { return s + c.move_outs; }, 0) + " out"))),

      h(Panel, { title: "Move-in / move-out history", note: "Net resident movement by month" },
        h(LineChart, {
          series: closedOnly(d.trends.moves), zeroBase: true, height: 230,
          lines: [
            { key: "ins", color: GREEN },
            { key: "outs", color: RED }
          ],
          fmtTick: function (v) { return Math.round(v); },
          ariaLabel: "Move-ins and move-outs by month"
        }),
        h("div", { className: "legend" },
          h("span", null, h("i", { style: { background: GREEN } }), "Move-ins"),
          h("span", null, h("i", { style: { background: RED } }), "Move-outs"))),

      h(Panel, { title: "Occupancy by park", note: "20+ lot parks, MH and RV segments combined" },
        h(BarList, { rows: parks, max: 100 })));
  }

  function CollectionsTab(d, filtered) {
    var th = d.thresholds;
    var cols = [
      { key: "name", label: "Community" },
      { key: "charged", label: "Charged", numeric: true, render: function (r) { return money(r.charged); } },
      { key: "paid", label: "Collected", numeric: true, render: function (r) { return money(r.paid); } },
      { key: "collection_pct", label: "Rate", numeric: true, render: function (r) {
          return r.charged
            ? h(Chip, { band: band(r.collection_pct, th.collections) }, pct(r.collection_pct))
            : "—"; } },
      { key: "ar_0_30", label: "0–30", numeric: true, render: function (r) { return money(r.ar_0_30); } },
      { key: "ar_31_60", label: "31–60", numeric: true, render: function (r) { return money(r.ar_31_60); } },
      { key: "ar_61_90", label: "61–90", numeric: true, render: function (r) { return money(r.ar_61_90); } },
      { key: "ar_90_plus", label: "90+", numeric: true, render: function (r) { return money(r.ar_90_plus); } },
      { key: "ar_total", label: "Total AR", numeric: true, render: function (r) { return money(r.ar_total); } },
      { key: "ar_accounts", label: "Accounts", numeric: true, render: function (r) { return count(r.ar_accounts); } }
    ];
    var sum = function (k) { return filtered.reduce(function (s, c) { return s + (c[k] || 0); }, 0); };
    var charged = sum("charged"), paid = sum("paid");

    return h("div", null,
      h(Panel, {
        title: "Aging detail",
        note: "Closed " + monthLabel(d.period.headline) + " · the open month is excluded because rent bills on the 1st",
        flush: true
      }, h(SortableTable, {
        cols: cols, rows: filtered, initialSort: { key: "ar_90_plus", dir: -1 },
        footer: [
          "Portfolio",
          money(charged), money(paid),
          charged ? pct(paid / charged * 100) : "—",
          money(sum("ar_0_30")), money(sum("ar_31_60")),
          money(sum("ar_61_90")), money(sum("ar_90_plus")),
          money(sum("ar_total")), count(sum("ar_accounts"))
        ]
      })));
  }

  function VacancyTab(d, filtered) {
    // Roll every community's unit-type composition into one portfolio view, so
    // "vacant" separates into lots you could lease today and lots that do not
    // functionally exist yet.
    var byType = {};
    filtered.forEach(function (c) {
      (c.vacancy_composition || []).forEach(function (v) {
        if (!byType[v.type]) byType[v.type] = { type: v.type, group: v.group, bucket: v.bucket, units: 0, vacant: 0 };
        byType[v.type].units += v.units;
        byType[v.type].vacant += v.vacant;
      });
    });
    var rows = Object.keys(byType).map(function (k) { return byType[k]; })
      .sort(function (a, b) { return b.vacant - a.vacant || b.units - a.units; });

    var BUCKET_LABEL = {
      rentable: "Leasable now",
      rentable_impaired: "Needs work first",
      not_rentable: "Not leasable"
    };
    var BUCKET_COLOR = { rentable: GREEN, rentable_impaired: YELLOW, not_rentable: RED };

    var totals = { rentable: 0, rentable_impaired: 0, not_rentable: 0 };
    rows.forEach(function (r) {
      if (totals[r.bucket] == null) totals[r.bucket] = 0;
      totals[r.bucket] += r.vacant;
    });

    var cols = [
      { key: "type", label: "Unit type" },
      { key: "group", label: "Class" },
      { key: "bucket", label: "Standing", render: function (r) {
          return h("span", { className: "chip " + (r.bucket === "rentable" ? "good" : r.bucket === "rentable_impaired" ? "watch" : "critical") },
            BUCKET_LABEL[r.bucket] || r.bucket); } },
      { key: "units", label: "Lots", numeric: true, render: function (r) { return count(r.units); } },
      { key: "vacant", label: "Vacant", numeric: true, render: function (r) { return count(r.vacant); } },
      { key: "fill", label: "Filled", numeric: true,
        sortValue: function (r) { return r.units ? (r.units - r.vacant) / r.units : 0; },
        render: function (r) { return r.units ? pct((r.units - r.vacant) / r.units * 100, 0) : "—"; } }
    ];

    return h("div", null,
      h("div", { className: "grid-3" },
        Object.keys(BUCKET_LABEL).map(function (b) {
          return h(Panel, { key: b, title: BUCKET_LABEL[b], note: "Vacant lots in this standing" },
            h("div", { className: "kvalue", style: { fontSize: "30px", fontWeight: 800, color: BUCKET_COLOR[b] } },
              count(totals[b] || 0)));
        })),
      h(Panel, {
        title: "Vacancy composition",
        note: "Empty lots are not one number: some lease today, some need rehab, some are demo or unusable",
        flush: true
      }, h(SortableTable, { cols: cols, rows: rows, initialSort: { key: "vacant", dir: -1 } })));
  }

  function FinancialsTab(d, filtered) {
    var th = d.thresholds;
    var cols = [
      { key: "name", label: "Community" },
      { key: "revenue", label: "Revenue", numeric: true, render: function (r) { return money(r.revenue); } },
      { key: "revenue_budget", label: "Rev budget", numeric: true, render: function (r) { return r.revenue_budget ? money(r.revenue_budget) : "—"; } },
      { key: "rev_var", label: "Rev var", numeric: true,
        sortValue: function (r) { return r.revenue_budget ? r.revenue - r.revenue_budget : 0; },
        render: function (r) {
          if (!r.revenue_budget) return "—";
          var v = r.revenue - r.revenue_budget;
          return h("span", { className: v >= 0 ? "up" : "down" }, (v >= 0 ? "+" : "−") + money(Math.abs(v))); } },
      { key: "opex", label: "OpEx", numeric: true, render: function (r) { return money(r.opex); } },
      { key: "noi", label: "NOI", numeric: true, render: function (r) { return money(r.noi); } },
      { key: "noi_budget", label: "NOI budget", numeric: true, render: function (r) { return r.noi_budget ? money(r.noi_budget) : "—"; } },
      { key: "noi_var", label: "NOI var", numeric: true,
        sortValue: function (r) { return r.noi_budget ? r.noi - r.noi_budget : 0; },
        render: function (r) {
          if (!r.noi_budget) return "—";
          var v = r.noi - r.noi_budget;
          return h("span", { className: v >= 0 ? "up" : "down" }, (v >= 0 ? "+" : "−") + money(Math.abs(v))); } },
      { key: "noi_margin", label: "Margin", numeric: true, render: function (r) {
          return r.revenue >= 5000
            ? h(Chip, { band: band(r.noi_margin, th.noi_margin) }, pct(r.noi_margin, 0)) : "—"; } },
      { key: "ytd_noi", label: "YTD NOI", numeric: true, render: function (r) { return money(r.ytd_noi); } }
    ];
    var sum = function (k) { return filtered.reduce(function (s, c) { return s + (c[k] || 0); }, 0); };
    var rev = sum("revenue"), noi = sum("noi");
    var revB = sum("revenue_budget"), noiB = sum("noi_budget");

    return h("div", null,
      h("div", { className: "grid-2" },
        h(Panel, { title: "Revenue against budget", note: "Actual versus plan, by month" },
          h(LineChart, {
            series: closedOnly(d.trends.financials), zeroBase: false, height: 230,
            lines: [
              { key: "revenue", color: GREEN, area: true },
              { key: "revenue_budget", color: NAVY }
            ],
            fmtTick: function (v) { return "$" + (v / 1e6).toFixed(1) + "M"; },
            fmtPoint: function (v) { return "$" + (v / 1e6).toFixed(2) + "M"; },
            ariaLabel: "Revenue versus budget by month"
          }),
          h("div", { className: "legend" },
            h("span", null, h("i", { style: { background: GREEN } }), "Actual"),
            h("span", null, h("i", { style: { background: NAVY } }), "Budget"))),
        h(Panel, { title: "NOI against budget", note: "Excludes debt service, CapEx and depreciation" },
          h(LineChart, {
            series: closedOnly(d.trends.financials), zeroBase: false, height: 230,
            lines: [
              { key: "noi", color: GREEN, area: true },
              { key: "noi_budget", color: NAVY }
            ],
            fmtTick: function (v) { return "$" + (v / 1e6).toFixed(1) + "M"; },
            fmtPoint: function (v) { return "$" + (v / 1e6).toFixed(2) + "M"; },
            ariaLabel: "NOI versus budget by month"
          }),
          h("div", { className: "legend" },
            h("span", null, h("i", { style: { background: GREEN } }), "Actual"),
            h("span", null, h("i", { style: { background: NAVY } }), "Budget")))),

      h(Panel, {
        title: "Per-community P&L",
        note: "Closed " + monthLabel(d.period.headline) + " · YTD through the same month",
        flush: true
      }, h(SortableTable, {
        cols: cols, rows: filtered, initialSort: { key: "noi", dir: -1 },
        footer: [
          "Portfolio",
          money(rev), revB ? money(revB) : "—",
          revB ? ((rev - revB >= 0 ? "+" : "−") + money(Math.abs(rev - revB))) : "—",
          money(sum("opex")), money(noi), noiB ? money(noiB) : "—",
          noiB ? ((noi - noiB >= 0 ? "+" : "−") + money(Math.abs(noi - noiB))) : "—",
          rev ? pct(noi / rev * 100, 0) : "—",
          money(sum("ytd_noi"))
        ]
      })));
  }

  // -------------------------------------------------------------- exceptions ---

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
    { id: "overview", label: "Overview", render: function (d) { return OverviewTab(d); } },
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
    var fs = useState({ kind: "all", search: "", size: "all" });
    var filters = fs[0], setFilters = fs[1];

    var filtered = useMemo(function () {
      return d.communities.filter(function (c) {
        if (filters.kind !== "all" && c.kind !== filters.kind) return false;
        if (filters.size === "large" && c.units < 100) return false;
        if (filters.size === "small" && c.units >= 100) return false;
        if (filters.search) {
          var q = filters.search.toLowerCase();
          if (c.name.toLowerCase().indexOf(q) === -1 && String(c.park).toLowerCase().indexOf(q) === -1) return false;
        }
        return true;
      });
    }, [d.communities, filters.kind, filters.search, filters.size]);

    var p = d.portfolio, th = d.thresholds;
    var active = TABS.filter(function (t) { return t.id === tab; })[0];
    var showFilters = tab !== "overview";

    var kinds = {};
    d.communities.forEach(function (c) { kinds[c.kind] = 1; });

    return h("div", { className: "wrap" },
      h("header", { className: "masthead" },
        h("div", { className: "brand" },
          window.__PK_LOGO__
            ? h("img", { src: window.__PK_LOGO__, alt: "Parakeet Communities" })
            : null,
          window.__PK_LOGO__ ? h("div", { className: "rule" }) : null,
          h("div", null,
            h("h1", null, "Property Operations"),
            h("div", { className: "sub" }, p.communities + " communities · " + count(p.total_units) + " lots · FL, GA, SC"))),
        h("div", { className: "periods" },
          h("div", { className: "period" },
            h("div", { className: "plabel" }, "Reporting month"),
            h("div", { className: "pvalue" }, monthLabel(d.period.headline)),
            h("div", { className: "pnote" }, "closed · every figure below")),
          h("div", { className: "period live" },
            h("div", { className: "plabel" }, "Open month"),
            h("div", { className: "pvalue" }, monthLabel(d.period.live_partial)),
            h("div", { className: "pnote" }, "partial · see data notes")))),

      h(Exceptions, { flags: d.flags }),

      h("div", { className: "kpis" },
        h(Kpi, {
          label: "Occupancy",
          value: pct(p.occupancy),
          color: bandColor(band(p.occupancy, th.occupancy)),
          sub: count(p.total_occupied) + " of " + count(p.total_units) + " lots"
        }, h(Delta, { curr: p.occupancy, prev: p.occupancy_prev, unit: "pt" })),
        h(Kpi, {
          label: "Collections",
          value: pct(p.collection_pct),
          color: bandColor(band(p.collection_pct, th.collections)),
          sub: money(p.paid, { compact: true }) + " of " + money(p.charged, { compact: true })
        }, h("div", { className: "kdelta flat" },
          h("span", { style: { fontWeight: 500, color: "var(--text-muted)" } },
            pct(p.collection_ttm) + " trailing 12-month"))),
        h(Kpi, {
          label: "Total receivables",
          value: money(p.ar_total, { compact: true }),
          sub: count(p.ar_accounts) + " accounts · " + money(p.ar_total / (p.total_units || 1)) + " per lot"
        }, h(Delta, { curr: p.ar_total, prev: p.ar_prev, money: true, invert: true })),
        h(Kpi, {
          label: "90+ days",
          value: money(p.ar_90_plus, { compact: true }),
          color: bandColor(band(p.ar_over90_share, th.over90_share, true)),
          sub: pct(p.ar_over90_share, 0) + " of all receivables"
        }),
        h(Kpi, {
          label: "NOI",
          value: money(p.noi, { compact: true }),
          color: p.noi_budget && p.noi < p.noi_budget ? RED : GREEN,
          sub: p.noi_budget
            ? (p.noi >= p.noi_budget ? "ahead of " : "behind ") + money(p.noi_budget, { compact: true }) + " budget"
            : "no budget loaded"
        }, h("div", { className: "kdelta " + (p.noi >= (p.noi_budget || 0) ? "up" : "down") },
          h("span", { style: { fontWeight: 500, color: "var(--text-muted)" } },
            pct(p.noi_margin, 0) + " margin on " + money(p.revenue, { compact: true })))),
        h(Kpi, {
          label: "Vacant, not leasable",
          value: count(p.not_rentable_units + p.impaired_units),
          color: YELLOW,
          sub: count(p.impaired_units) + " need rehab · " + count(p.not_rentable_units) + " demo or unusable"
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
            id: "f-search", type: "search", placeholder: "Community or park",
            value: filters.search,
            onChange: function (e) {
              var v = e.target.value;
              setFilters(function (f) { return Object.assign({}, f, { search: v }); });
            }
          })),
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
        active.render(d, filtered)),

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
