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

  /* Candlestick for net resident movement.
     
     Each month is one candle centred on zero: the wick runs from minus the
     gross move-outs up to plus the gross move-ins, and the body spans zero to
     the net. So the wick length is the churn it took and the body is what the
     churn actually bought. Everything reconciles by construction -- body =
     high + low -- which a candle drawn from occupied-lot counts would not,
     because occupancy is unit-day weighted and lot counts change when a
     property joins or leaves the portfolio.

     Direction is encoded three ways, never by hue alone: the body sits above or
     below the zero line, a gaining month is drawn hollow and a losing month
     filled (the standard candlestick convention), and the net is labelled
     directly on the notable months. */
  function CandleChart(props) {
    var mw = useWidth(700);
    var ref = mw[0], W = mw[1];
    var series = props.series || [];
    var H = props.height || 260;
    var padL = 48, padR = 16, padT = 26, padB = 30;

    if (!series.length) return h("div", { ref: ref, className: "loading" }, "No move history.");

    /* Scale from real resident movement only. A month where a whole community
       was loaded into Rent Manager posts its entire sitting resident base as
       move-ins -- Riverwalk booked 169 against 201 lots -- and two such months
       set the ceiling for the whole chart and flatten the rest into a line.
       Those candles are drawn off-scale with a break marker and their true net
       labelled, so nothing is hidden and the readable months stay readable. */
    var scaleFrom = series.filter(function (p) { return !p.onboarding; });
    if (!scaleFrom.length) scaleFrom = series;
    var hi = 0, lo = 0;
    scaleFrom.forEach(function (p) {
      if (p.ins > hi) hi = p.ins;
      if (-p.outs < lo) lo = -p.outs;
    });
    /* Symmetric about zero, so a bar of gains and a bar of losses the same
       length mean the same number of residents. An asymmetric scale on a
       zero-centred chart quietly flatters whichever side got less room. */
    var bound = Math.max(hi, -lo) * 1.1;
    if (!(bound > 0)) bound = 1;
    hi = bound; lo = -bound;
    var clampY = function (v) { return Math.min(hi, Math.max(lo, v)); };

    var innerW = Math.max(60, W - padL - padR);
    var bandW = innerW / series.length;
    var bw = Math.min(bandW * 0.56, 22);
    var y = function (v) { return padT + (hi - v) / (hi - lo) * (H - padT - padB); };
    var y0 = y(0);

    var kids = [];
    // Asking for 8 rather than 4: niceStep's ladder jumps 5 to 10, so a span of
    // 250 residents resolved to a step of 100 and the chart drew one gridline.
    niceTicks(lo, hi, 8).forEach(function (t, i) {
      if (t === 0) return;
      kids.push(h("line", { key: "g" + i, className: "grid-line",
                            x1: padL, x2: W - padR, y1: y(t), y2: y(t) }));
      kids.push(h("text", {
        key: "gt" + i, x: padL - 8, y: y(t) + FS_AXIS * 0.35, textAnchor: "end",
        style: { fontSize: FS_AXIS + "px" }
      }, (t > 0 ? "+" : "") + Math.round(t)));
    });

    /* Which months get a direct label: the best and worst of the months that
       are actually on scale, the newest, and every off-scale month -- an
       off-scale candle without its number is just a mystery. */
    var best = null, worst = null;
    var labelled = {};
    series.forEach(function (p, i) {
      if (p.onboarding) { labelled[i] = true; return; }
      if (best === null || p.net > series[best].net) best = i;
      if (worst === null || p.net < series[worst].net) worst = i;
    });
    if (best !== null) labelled[best] = true;
    if (worst !== null) labelled[worst] = true;
    labelled[series.length - 1] = true;

    series.forEach(function (p, i) {
      var cx = padL + bandW * i + bandW / 2;
      var up = p.net >= 0;
      var color = up ? "var(--gain)" : "var(--loss)";
      var faint = p.partial ? 0.55 : 1;

      var yIn = clampY(p.ins), yOut = clampY(-p.outs), yNet = clampY(p.net);
      var clipped = p.ins > hi || -p.outs < lo || p.net > hi || p.net < lo;

      kids.push(h("line", {
        key: "w" + i, className: "candle-wick",
        x1: cx, x2: cx, y1: y(yIn), y2: y(yOut),
        stroke: color, strokeOpacity: faint,
        strokeDasharray: p.partial ? "3 2" : null
      }));
      // Caps make the gross figures readable where a wick is short. A capped
      // end is an axis break instead, so the eye does not read it as the value.
      [[p.ins, yIn, "i"], [-p.outs, yOut, "o"]].forEach(function (cap) {
        if (!cap[0]) return;
        if (cap[0] !== cap[1]) return;
        kids.push(h("line", {
          key: "c" + cap[2] + i, x1: cx - bw * 0.28, x2: cx + bw * 0.28,
          y1: y(cap[1]), y2: y(cap[1]), stroke: color, strokeOpacity: faint, strokeWidth: 1.6
        }));
      });

      var top = Math.min(y0, y(yNet)), bot = Math.max(y0, y(yNet));
      kids.push(h("rect", {
        key: "b" + i, x: cx - bw / 2, y: top, width: bw,
        height: Math.max(2, bot - top), rx: 2,
        // Hollow up, filled down -- the candlestick convention, and the
        // encoding a red-green reader actually uses.
        fill: up ? "var(--ground)" : color,
        fillOpacity: up ? 1 : faint,
        stroke: color, strokeWidth: 1.8, strokeOpacity: faint,
        // Dashed means "do not read this as leasing": an onboarding month, or
        // one drawn off scale. Jan 25's +90 fits on the axis and is still 88
        // residents inherited with Parkwood, so the dash cannot key off
        // clipping alone.
        strokeDasharray: (p.onboarding || clipped) ? "4 2" : null
      }));

      /* Off-scale candles are marked by their dashed outline and the arrow on
         the label, not by a break glyph: the usual two slashes are drawn in the
         ground colour to erase a solid bar, and against a dashed hollow body
         they erase nothing and read as nothing. */

      if (labelled[i] && (p.net || i === series.length - 1)) {
        var above = p.net >= 0;
        kids.push(h("text", {
          key: "nl" + i, x: cx,
          y: above ? Math.max(FS_VAL, y(yIn) - 6) : y(yOut) + FS_VAL + 2,
          textAnchor: "middle",
          style: { fontSize: FS_VAL + "px", fontWeight: 700 },
          fill: p.onboarding ? "var(--text-muted)" : "var(--text)"
        }, (p.net > 0 ? "+" : "") + p.net + (clipped ? " \u2191" : "")));
      }

      kids.push(h("title", { key: "t" + i },
        monthLabel(p.month) + (p.partial ? " (open month, partial)" : "") + ": " +
        p.ins + " in, " + p.outs + " out, net " + (p.net > 0 ? "+" : "") + p.net +
        (p.onboarding
          ? " \u2014 includes " + p.onboarding_ins + " onboarding move-ins (" +
            p.onboarding_detail + "), not leasing"
          : "")));
    });

    kids.push(h("line", { key: "zero", className: "candle-zero",
                          x1: padL, x2: W - padR, y1: y0, y2: y0 }));
    kids.push(h("text", { key: "zl", x: padL - 8, y: y0 + FS_AXIS * 0.35,
                          textAnchor: "end", style: { fontSize: FS_AXIS + "px" } }, "0"));

    var step = Math.max(1, Math.ceil((FS_AXIS * 3.4) / bandW));
    series.forEach(function (p, i) {
      if (i % step !== 0 && i !== series.length - 1) return;
      kids.push(h("text", {
        key: "xl" + i, x: padL + bandW * i + bandW / 2, y: H - padB + FS_AXIS + 8,
        textAnchor: "middle", style: { fontSize: FS_AXIS + "px" }
      }, monthShort(p.month) + (p.partial ? " \u25CB" : "")));
    });

    return h("div", { ref: ref, style: { width: "100%" } },
      h("svg", {
        className: "chart", viewBox: "0 0 " + W + " " + H,
        width: W, height: H, role: "img",
        "aria-label": props.ariaLabel || "candlestick chart of net resident movement by month"
      }, kids));
  }

  /* A donut for one part-to-whole split, at most four slices.

     The house guidance is that part-to-whole belongs in a stacked bar and a
     two-slice pie belongs in a stat tile, and it is right about both. This
     exists because the question here is "what are the services", asked three
     times over -- water, sewer, trash -- and three small donuts in a row read
     as three answers to the same question in a way three stacked bars do not.
     It stays honest by never asking the reader to judge an angle: every slice
     carries its count and share in the legend beside it, and the total sits in
     the hole. A 2%-vs-3% comparison is not made here and must not be. */
  function Donut(props) {
    var rows = (props.rows || []).filter(function (r) { return r.n > 0; });
    var total = rows.reduce(function (a, r) { return a + r.n; }, 0);
    var S = props.size || 128, R = S / 2, stroke = props.stroke || 22;
    var r0 = R - stroke / 2 - 1;
    var circ = 2 * Math.PI * r0;

    var arcs = [];
    var acc = 0;
    rows.forEach(function (row, i) {
      var frac = total ? row.n / total : 0;
      // A 2px gap between neighbouring fills, per the house mark spec. Skipped
      // on a single full-circle slice, where a gap is just a nick.
      var gap = rows.length > 1 ? 2 : 0;
      var len = Math.max(0, frac * circ - gap);
      arcs.push(h("circle", {
        key: "a" + i, cx: R, cy: R, r: r0, fill: "none",
        stroke: row.color, strokeWidth: stroke,
        strokeDasharray: len + " " + (circ - len),
        strokeDashoffset: -(acc * circ) + circ / 4,
        // The dash runs clockwise from twelve o'clock.
        transform: "scale(1,-1) translate(0," + -S + ")"
      }, h("title", null, row.label + ": " + count(row.n) +
                          (row.sub ? " \u00b7 " + row.sub : ""))));
      acc += frac;
    });

    return h("div", { className: "util-donut" },
      props.title ? h("h4", null, props.title) : null,
      total
        ? h("svg", { width: S, height: S, viewBox: "0 0 " + S + " " + S,
                     role: "img", "aria-label": props.ariaLabel || props.title },
            arcs,
            h("text", { x: R, y: R + 2, textAnchor: "middle", className: "donut-center-n" },
              count(total)),
            h("text", { x: R, y: R + 16, textAnchor: "middle", className: "donut-center-l" },
              props.centerLabel || "total"))
        : h("div", { className: "loading" }, "No data."),
      h("div", { className: "reason-legend" }, rows.map(function (row) {
        return h("div", { className: "rl", key: row.key },
          h("span", { className: "swatch", style: { background: row.color } }),
          h("span", null,
            h("span", { className: "rl-n" }, count(row.n)), " ", row.label,
            h("span", { className: "rl-sub" },
              "  " + (total ? pct(row.n / total * 100, 0) : "—") +
              (row.sub ? "  \u00b7  " + row.sub : ""))));
      })));
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

  /* The hot sheet: the one screen a regional opens on a phone before a call.

     Everything here is measured, never planned. It leads with occupancy over
     core units -- occupied lots on the rent roll today -- which is NOT the
     unit-day figure the rest of the dashboard trends on. Both are shown,
     labelled, because a lot empty for half of August is half a vacancy to the
     trend and a whole empty lot to the manager standing in front of it. */
  function HotSheet(props) {
    var c = props.community, d = props.data, mode = props.mode;
    var hs = c.hot, v = pv(c, mode), th = d.thresholds;
    if (!hs) {
      return h("div", { className: "loading" },
        "No rent roll rows for this community, so there is nothing to measure.");
    }

    var muted = { color: "var(--text-muted)" };
    function row(label, value, note, color) {
      return { label: label, value: value, note: note, color: color };
    }
    function list(items, fmt) {
      return items.length ? items.map(fmt).join(" · ") : "—";
    }

    var dead = hs.core_units - hs.rentable_units;
    // Split before printing: RV and transient lots bill per night or per
    // season, so an empty recurring charge there is the billing model, not a
    // miss. Rolling them together overstates the gap roughly sixfold.
    var nb = hs.not_billing_by_type || [];
    var real = nb.filter(function (x) { return !x.transient; });
    var tran = nb.filter(function (x) { return x.transient; });
    var realN = real.reduce(function (a, x) { return a + x.units; }, 0);
    var realM = real.reduce(function (a, x) { return a + x.market; }, 0);
    var tranN = tran.reduce(function (a, x) { return a + x.units; }, 0);

    var rows = [
      // The tile above this table reads the unit-day figure for the month and
      // will not match. Say which is which here, where someone is looking at
      // both at once, rather than letting them find the gap themselves.
      row("Occupancy today", pct(hs.occupancy),
          count(hs.occupied) + " of " + count(hs.core_units) +
          " core lots on the rent roll right now · the tile above is " +
          pct(v.occupancy) + " unit-day weighted across " +
          monthLabel(d.period[mode === "live" ? "live" : "closed"]),
          bandColor(band(hs.occupancy, th.occupancy))),
      row("Occupancy, rentable", pct(hs.occupancy_rentable),
          count(hs.rentable_units) + " lots, " + count(dead) + " demo or unusable excluded"),
      row("Vacancies", count(hs.vacant),
          list(hs.vacant_by_type, function (x) { return x.units + " " + x.type; })),
      row("Lot rent, occupied",
          hs.lot_rent_avg == null ? "—" : money(hs.lot_rent_avg),
          hs.lot_rent_avg == null
            ? "no lot is billing a recurring charge"
            : money(hs.lot_rent_median) + " median across " +
              count(hs.lots_billing) + " lots billing recurring rent")
    ];

    if (realN) {
      rows.push(row("Occupied, not billing", count(realN) + (realN === 1 ? " lot" : " lots"),
        money(realM) + "/mo at market · " +
        list(real, function (x) { return x.units + " " + x.type; }), RED));
    }
    if (tranN) {
      rows.push(row("Transient or seasonal", count(tranN) + (tranN === 1 ? " lot" : " lots"),
        "billed per stay, so no recurring charge is expected · " +
        list(tran, function (x) { return x.units + " " + x.type; })));
    }

    rows.push(
      row("Loss to lease", money(hs.loss_to_lease),
          hs.loss_to_lease_per_lot == null ? null
            : money(hs.loss_to_lease_per_lot) + " per occupied lot"),
      row("Park-owned homes",
          hs.poh_total ? count(hs.poh_occupied) + " of " + count(hs.poh_total) : "—",
          hs.poh_total
            ? pct(hs.poh_pct) + " occupied · " +
              list(hs.poh_vacant_by_status, function (x) { return x.homes + " " + x.status; })
            : "no homes on the asset listing",
          hs.poh_pct != null && hs.poh_pct < 60 ? YELLOW : null),
      row(mode === "live" ? "Collected month to date" : "Collection rate",
          v.charged ? pct(v.collection_pct) : "—",
          money(v.paid) + " of " + money(v.charged) +
          (mode === "live" ? " · a partial month, not comparable to a full one" : "")),
      row("AR outstanding", money(v.ar_total),
          count(v.ar_accounts) + (v.ar_accounts === 1 ? " account · " : " accounts · ") +
          money(v.ar_past_due_30plus) +
          " past due 30+ · " + money(v.ar_90_plus) + " over 90",
          v.ar_past_due_30plus > 0 ? RED : null),
      row("NOI year to date", money(c.closed.ytd_noi),
          c.closed.ytd_noi_budget
            ? money(c.closed.ytd_noi_budget) + " budget · " +
              pct(c.closed.ytd_noi / c.closed.ytd_noi_budget * 100, 0) + " of plan"
            : "no budget loaded",
          c.closed.ytd_noi_budget && c.closed.ytd_noi < c.closed.ytd_noi_budget ? RED : GREEN),
      row("Moves", count(v.move_ins) + " in / " + count(v.move_outs) + " out",
          monthLabel(d.period[mode === "live" ? "live" : "closed"])),
      row("Acquired",
          hs.acquired_price == null ? "—" : money(hs.acquired_price, { compact: true }),
          hs.acquired_date || "date not on the Property Data Sheet")
    );

    // The PDS is hand-maintained and the asset listing is not. Where they
    // disagree, say so on the page rather than silently preferring one.
    var notes = [];
    if (hs.pds_poh && hs.poh_total && hs.pds_poh !== hs.poh_total) {
      notes.push("The Property Data Sheet says " + hs.pds_poh +
        " park-owned homes; the asset listing has " + hs.poh_total +
        " once structures are removed. The two need reconciling.");
    }
    if (realN) {
      notes.push(count(realN) + " occupied " +
        (realN === 1 ? "lot carries" : "lots carry") +
        " no recurring rent charge, worth " + money(realM) +
        " a month at market. Either a billing gap or a deliberate arrangement, " +
        "and nobody is currently looking at it.");
    }

    return h("div", null,
      h("div", { className: "panel-head" },
        h("h2", null, "Hot sheet"),
        h("div", { className: "note" },
          "Occupancy, vacancy, rent and homes are the rent roll and asset listing " +
          "as of " + new Date(d.generated_at).toLocaleDateString("en-US",
            { month: "short", day: "numeric" }) +
          ". Collections, AR and NOI are " +
          (mode === "live" ? "the open month through day " + d.period.live_day
                           : monthLabel(d.period.closed)) + ".")),
      h("div", { className: "panel-body" }, rows.map(function (r, i) {
        return h("div", { className: "hs-row", key: i },
          h("div", { className: "hs-head" },
            h("span", { className: "hs-label" }, r.label),
            h("span", { className: "hs-value", style: { color: r.color || null } },
              r.value)),
          r.note ? h("div", { className: "hs-note" }, r.note) : null);
      })),
      notes.length ? h("div", { className: "panel-body" },
        notes.map(function (n, i) {
          return h("div", { key: i, className: "note",
                            style: { fontSize: "12px", marginTop: i ? "6px" : 0 } }, n);
        })) : null);
  }

  /* One community, four views: its rent roll, why its lots are empty, who owes
     money, and how its P&L reads against budget. */
  function CommunityDrill(props) {
    var c = props.community, d = props.data, mode = props.mode;
    var st = useState(props.view || "hot");
    var view = st[0], setView = st[1];
    var v = pv(c, mode), th = d.thresholds;
    var e = c.expenses || {}, ey = c.expenses_ytd || {};

    var VIEWS = [
      { id: "hot", label: "Hot sheet" },
      { id: "rentroll", label: "Rent roll (" + (c.rent_roll || []).length + ")" },
      { id: "vacancy", label: "Vacant (" + (c.vacancy_detail || []).length + ")" },
      { id: "accounts", label: "Accounts owing (" + (c.ar_accounts || []).length + ")" },
      { id: "homes", label: "Homes (" + (c.homes || []).length + ")" },
      { id: "evictions", label: "Evictions (" +
          (c.evictions || []).filter(function (x) { return !x.closed; }).length + ")" },
      { id: "pl", label: "P&L vs budget" }
    ];

    var body;
    if (view === "hot") {
      body = h(HotSheet, { community: c, data: d, mode: mode });
    } else if (view === "rentroll") {
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
                    className: "chip " + (r.segment === "eviction" ? "critical"
                      : r.segment === "payment_plan" ? "good"
                      : r.segment === "former" ? "" : "watch"),
                    title: r.segment_label
                  }, SEG_LABEL[r.segment] || r.segment); } },
              { key: "eviction_stage", label: "Case stage",
                title: "Current stage from the eviction tracker, and days since the case opened",
                render: function (r) {
                  return r.eviction_stage
                    ? h("span", null, r.eviction_stage,
                        r.eviction_days_open != null
                          ? h("span", { className: "rl-sub" }, "  " + r.eviction_days_open + "d")
                          : null)
                    : h("span", { style: { color: "var(--text-muted)" } }, "—"); } },
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
            footer: [aa.length + " accounts", "", "", "",
              money(aa.reduce(function (a, r) { return a + r.b0_30; }, 0)),
              money(aa.reduce(function (a, r) { return a + r.b31_60; }, 0)),
              money(aa.reduce(function (a, r) { return a + r.b61_90; }, 0)),
              money(aa.reduce(function (a, r) { return a + r.b90p; }, 0)),
              money(aa.reduce(function (a, r) { return a + r.total; }, 0)), ""]
          })
        : h("div", { className: "loading" }, "No outstanding accounts, or no unit detail available.");
    } else if (view === "homes") {
      var hs = c.homes || [];
      var pipeHomes = hs.filter(function (x) { return x.stage; });
      body = hs.length
        ? h("div", null,
            h("div", { className: "panel-body" },
              h(BandBar, { rows: pipeRows(c.home_pipeline || []),
                           label: "Homes by pipeline stage",
                           empty: "Every home here is already earning." }),
              h("div", { className: "note",
                         style: { marginTop: "12px", fontSize: "12px", color: "var(--text-muted)" } },
                count(c.homes_earning || 0) + " of " + count(hs.length) + " homes are earning; " +
                count(pipeHomes.length) + " sit somewhere in the pipeline. Days held counts from " +
                "the home's in-service date, so a long-held rental is not a problem and a long-held " +
                "rehab is.")),
            h(SortableTable, {
              cols: [
                { key: "unit", label: "Unit", render: function (r) { return r.unit || "—"; } },
                { key: "tag", label: "Tag", render: function (r) { return r.tag || "—"; } },
                { key: "type", label: "Type" },
                { key: "status", label: "Asset status", render: function (r) {
                    return h("span", { className: "chip",
                                       style: { background: (STATUS_COLORS[r.status] || "#8FA3B2") + "33",
                                                color: "var(--text)" } }, r.status); } },
                { key: "stage_label", label: "Pipeline stage", render: function (r) {
                    return r.stage
                      ? h("span", { className: "chip",
                                    style: { background: PIPE_COLORS[r.stage] + "33",
                                             color: "var(--text)" } }, r.stage_label)
                      : h("span", { style: { color: "var(--text-muted)" } }, "earning"); } },
                { key: "rtm", label: "Ready to market", render: function (r) {
                    return r.rtm
                      ? h("span", { className: "chip good" }, "Yes")
                      : h("span", { style: { color: "var(--text-muted)" } }, "—"); } },
                { key: "age_days", label: "Days held", numeric: true,
                  render: function (r) { return r.age_days == null ? "—" : count(r.age_days); } },
                { key: "market_rent", label: "Market rent", numeric: true,
                  render: function (r) { return r.market_rent ? money(r.market_rent) : "—"; } },
                { key: "title", label: "Title", render: function (r) { return r.title || "—"; } }
              ],
              rows: hs, initialSort: { key: "age_days", dir: -1 }
            }))
        : h("div", { className: "loading" }, "No park-owned homes on the asset listing here.");
    } else if (view === "evictions") {
      var ev = (c.evictions || []);
      var evOpen = ev.filter(function (x) { return !x.closed; });
      body = ev.length
        ? h("div", null,
            h("div", { className: "panel-body" },
              h(BandBar, { rows: phaseRows(c.eviction_phases || []),
                           label: "Open cases by phase",
                           empty: "No open cases here." }),
              h("div", { className: "note",
                         style: { marginTop: "12px", fontSize: "12px", color: "var(--text-muted)" } },
                count(evOpen.length) + " open of " + count(ev.length) + " on record. Balances are " +
                "the tracker's own figure as of " + (((d.portfolio || {}).evictions || {}).as_of || "the last export") +
                ", so they lag the live ledger by a day.")),
            h(SortableTable, {
              cols: [
                { key: "unit", label: "Unit" },
                { key: "stage", label: "Current stage" },
                { key: "phase_label", label: "Phase", render: function (r) {
                    return h("span", { className: "chip",
                                       style: { background: PHASE_COLORS[r.phase] + "33",
                                                color: "var(--text)" } }, r.phase_label); } },
                { key: "start", label: "Opened", render: function (r) { return r.start || "—"; } },
                { key: "days_open", label: "Days open", numeric: true, render: function (r) {
                    return r.closed
                      ? h("span", { style: { color: "var(--text-muted)" } }, "closed " + r.closed)
                      : h("span", { className: (r.days_open || 0) > 120 ? "down" : "" },
                          count(r.days_open)); } },
                { key: "days_in_stage", label: "Days in stage", numeric: true, render: function (r) {
                    return r.days_in_stage == null ? "—" : count(r.days_in_stage); } },
                { key: "with_attorney", label: "With attorney", render: function (r) {
                    return r.with_attorney
                      ? h("span", { className: "chip watch" }, "Yes")
                      : h("span", { style: { color: "var(--text-muted)" } }, "—"); } },
                { key: "open_charges", label: "Owed", numeric: true,
                  render: function (r) { return r.open_charges ? money(r.open_charges) : "—"; } }
              ],
              rows: ev, initialSort: { key: "days_open", dir: -1 },
              footer: [evOpen.length + " open", "", "", "", "", "", "",
                money(evOpen.reduce(function (a, r) { return a + r.open_charges; }, 0))]
            }))
        : h("div", { className: "loading" }, "No eviction cases on record for this community.");
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

  /* Raw Rent Manager asset statuses. The pipeline funnel is built from these
     plus the Ready to Market field; this palette is what the Homes drill-in
     uses to show the underlying status behind each stage. */
  var STATUS_COLORS = {
    "Ordered": "#C7D3DA", "Delivered": "#8FA3B2", "Needs Rehab": "#FFCC3B",
    "For Sale": "#4ABA81", "Rent to Own Agreement": "#2F4E65",
    "Lease Option (LOP)": "#5C7C93", "Rental": "#A8D5BD", "In Use": "#A8D5BD",
    "Eviction Filed": "#F16262", "To Be Demoed": "#B23B3B", "TBD": "#E0E6EA",
    "Unknown": "#E0E6EA"
  };

  /* The four work buckets Natalie asked for. These come from the eviction
     tracker now, not from guessing at charge names. */
  var SEG_ORDER = ["eviction", "payment_plan", "former", "needs_action"];
  var SEG_LABEL = {
    eviction: "In eviction", payment_plan: "On a payment plan",
    former: "Former resident", needs_action: "Needs action"
  };
  var SEG_COLORS = {
    eviction: "#F16262", payment_plan: "#4ABA81",
    former: "#8FA3B2", needs_action: "#FFCC3B"
  };

  /* The eviction funnel, in the order a case actually moves through it.
     Title and resale is deliberately its own colour: it is not a resident
     eviction at all, it is recovering and reselling an abandoned home. */
  var PHASE_ORDER = ["intake", "notice", "filed", "judgment", "possession",
                     "title", "done", "other"];
  var PHASE_COLORS = {
    intake: "#C7D3DA", notice: "#FFCC3B", filed: "#F0A33B",
    judgment: "#F16262", possession: "#B23B3B", title: "#2F4E65",
    done: "#A8D5BD", other: "#8FA3B2"
  };

  /* The home pipeline: arriving on site through listed and showable. Green is
     reserved for the two stages that mean ready; red for the gap the Ready to
     Market flag exposes -- listed for sale without being ready to show. */
  var PIPE_COLORS = {
    ordered: "#C7D3DA", delivered: "#5C7C93", rehab: "#FFCC3B",
    for_sale_prep: "#F16262", rtm: "#A8D5BD", listed: "#4ABA81",
    demo: "#B23B3B", tbd: "#E0E6EA"
  };

  /* One proportional bar plus a legend. Used for vacancy reasons, vacancy
     aging, home status and AR segments: same shape, different dimension. */
  function BandBar(props) {
    var rows = (props.rows || []).filter(function (r) { return r.n > 0; });
    if (!rows.length) return h("div", { className: "loading" }, props.empty || "Nothing to show.");
    var total = rows.reduce(function (a, r) { return a + r.n; }, 0);
    var pick = props.onPick;
    return h("div", null,
      h("div", { className: "reasonbar", role: pick ? "group" : "img",
                 "aria-label": props.label },
        rows.map(function (r) {
          return h("span", {
            key: r.key, className: pick ? "pick" : null,
            role: pick ? "button" : null, tabIndex: pick ? 0 : null,
            style: { width: (r.n / total * 100) + "%", background: r.color },
            onClick: pick ? function () { pick(r); } : null,
            onKeyDown: pick ? function (e) {
              if (e.key === "Enter" || e.key === " ") { e.preventDefault(); pick(r); }
            } : null,
            title: r.label + ": " + count(r.n) + (r.money ? " (" + money(r.money) + ")" : "") +
                   (pick ? " \u00b7 click to list them" : "")
          });
        })),
      h("div", { className: "reason-legend" }, rows.map(function (r) {
        return h(pick ? "button" : "div", {
          className: "rl" + (pick ? " pick" : ""), key: r.key,
          type: pick ? "button" : null,
          onClick: pick ? function () { pick(r); } : null,
          title: pick ? "List the " + count(r.n) + " units in " + r.label : null
        },
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

  /* Roll a list of per-community pipeline or funnel rows into BandBar shape.
     Order comes from the payload, which is already in registry order, so the
     bar always reads left to right in the sequence things actually happen. */
  function orderedRows(list, order, colors, keyField, countField) {
    var by = {}, label = {}, extra = {};
    (list || []).forEach(function (r) {
      var k = r[keyField];
      by[k] = (by[k] || 0) + r[countField];
      label[k] = r.label;
      if (r.balance) extra[k] = (extra[k] || 0) + r.balance;
    });
    var keys = order.filter(function (k) { return by[k]; });
    Object.keys(by).forEach(function (k) { if (keys.indexOf(k) === -1) keys.push(k); });
    return keys.map(function (k) {
      return { key: k, label: label[k] || k, n: by[k], money: extra[k],
               color: colors[k] || "#8FA3B2" };
    });
  }

  function pipeRows(list) {
    return orderedRows(list, Object.keys(PIPE_COLORS), PIPE_COLORS, "stage", "homes");
  }

  function phaseRows(list) {
    return orderedRows(list, PHASE_ORDER, PHASE_COLORS, "phase", "cases");
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
    var pick = props.onPick;
    return h("div", null,
      h("div", { className: "reasonbar", role: pick ? "group" : "img",
                 "aria-label": "Vacant units by reason" },
        rows.map(function (r) {
          return h("span", {
            key: r.reason, className: pick ? "pick" : null,
            role: pick ? "button" : null, tabIndex: pick ? 0 : null,
            style: { width: (r.units / total * 100) + "%",
                     background: REASON_COLORS[r.reason] || "#8FA3B2" },
            onClick: pick ? function () { pick(r); } : null,
            onKeyDown: pick ? function (e) {
              if (e.key === "Enter" || e.key === " ") { e.preventDefault(); pick(r); }
            } : null,
            title: r.label + ": " + r.units + " units" +
                   (pick ? " \u00b7 click to list them" : "")
          });
        })),
      h("div", { className: "reason-legend" }, rows.map(function (r) {
        return h(pick ? "button" : "div", {
          className: "rl" + (pick ? " pick" : ""), key: r.reason,
          type: pick ? "button" : null,
          onClick: pick ? function () { pick(r); } : null,
          title: pick ? "List the units in " + r.label : null
        },
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

  /* Flatten every named vacant unit across a set of communities into one list,
     carrying the community down with it. The bars above these lists are counted
     unit-day weighted by the warehouse, while this names units with no active
     lease today -- two different measures, so a drill-in will not tie to the
     segment that opened it, and the modal says so rather than implying it will. */
  function flattenVacant(rows) {
    var out = [];
    rows.forEach(function (c) {
      (c.vacancy_detail || []).forEach(function (v) {
        out.push({
          community: c.name, vehicle: c.vehicle, comm: c,
          unit: v.unit, type: v.type, reason: v.reason,
          days_vacant: v.days_vacant, age_band: v.age_band,
          vacant_since: v.vacant_since, rent_lost: v.rent_lost
        });
      });
    });
    return out;
  }

  /* A proportional bar whose segments open a list of the units behind them.
     Owns its own selection state, so a tab function can drop it in without
     needing hooks of its own -- tab bodies are plain functions and mount and
     unmount as the user switches, which would break hook order. */
  function VacancyPicker(props) {
    var st = useState(null);
    var pick = st[0], setPick = st[1];
    var d = props.data;
    var all = props.units || [];
    var field = props.field;                 // "reason" or "age_band"
    var keyOf = props.keyOf;                 // bar row -> the value to match

    var listed = pick ? all.filter(function (u) { return u[field] === keyOf(pick); }) : [];
    var counted = pick ? (pick.units != null ? pick.units : pick.n) : 0;

    return h("div", null,
      props.children(function (row) { setPick(row); }),
      pick ? h(Modal, {
        title: pick.label,
        subtitle: count(listed.length) + " units named" +
          (counted ? " \u00b7 " + count(counted) + " counted in the bar" : "") +
          (props.scope ? " \u00b7 " + props.scope : ""),
        onClose: function () { setPick(null); }
      },
        h("div", { className: "note",
                   style: { marginBottom: "12px", fontSize: "12px", color: "var(--text-muted)" } },
          counted && listed.length !== counted
            ? "The bar counts " + count(counted) + " on a unit-day basis; this list names " +
              count(listed.length) + " units with no active lease today. Different measures, " +
              "so they do not tie."
            : "Units with no active lease today, from the Rent Manager unit list."),
        listed.length
          ? h(SortableTable, {
              cols: [
                { key: "community", label: "Community", render: function (r) {
                    return h("span", null,
                      h("button", { className: "linkish",
                                    onClick: function () { setPick(null); props.open(r.comm, "vacancy"); },
                                    title: "Open " + r.community }, r.community),
                      " ", h("span", { className: "tag" }, r.vehicle)); } },
                { key: "unit", label: "Unit" },
                { key: "type", label: "Unit type" },
                field === "reason"
                  ? { key: "age_band", label: "How long empty", render: function (r) {
                        return r.days_vacant != null
                          ? h("span", { className: (r.days_vacant > 180 ? "down" : "") },
                              count(r.days_vacant) + "d")
                          : h("span", { style: { color: "var(--text-muted)" } }, "unknown"); } }
                  : { key: "reason", label: "Why it is empty", render: function (r) {
                        var m = (d.reason_meta || {})[r.reason] || {};
                        return h("span", {
                          className: "chip " + (m.actionable === false ? "critical" : "watch")
                        }, m.label || r.reason); } },
                { key: "vacant_since", label: "Vacant since", render: function (r) {
                    return r.vacant_since ||
                      h("span", { style: { color: "var(--text-muted)" } }, "no move-out on record"); } },
                { key: "rent_lost", label: "Rent lost", numeric: true,
                  render: function (r) { return r.rent_lost ? money(r.rent_lost) : "—"; } }
              ],
              rows: listed,
              initialSort: field === "reason"
                ? { key: "days_vacant", dir: -1 }
                : { key: "rent_lost", dir: -1 },
              footer: [count(listed.length) + " units", "", "", "", "",
                money(listed.reduce(function (a, r) { return a + (r.rent_lost || 0); }, 0))]
            })
          : h("div", { className: "loading" },
              "The Rent Manager unit list cannot name any of these. See the data notes.")
      ) : null);
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

    // Every named vacant unit across the filtered set, so a click on either bar
    // has a list to open. Built once here rather than inside each picker.
    var vacantUnits = flattenVacant(filtered);
    var scopeLabel = filtered.length === d.communities.length
      ? "whole portfolio"
      : filtered.length + " of " + d.communities.length + " communities in view";

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
        note: "Unit-day weighted from the warehouse · click any band to list the units"
      }, h(VacancyPicker, {
        data: d, units: vacantUnits, field: "reason",
        keyOf: function (r) { return r.reason; },
        scope: scopeLabel, open: ctx.open
      }, function (onPick) {
        return h(ReasonBar, { rows: reasons, meta: d.reason_meta, onPick: onPick });
      })),

      h(Panel, {
        title: "How long has it been sitting",
        note: "Days since the unit's last move-out · click any band to list the units"
      }, h(VacancyPicker, {
        data: d, units: vacantUnits, field: "age_band",
        keyOf: function (r) { return r.key; },
        scope: scopeLabel, open: ctx.open
      }, function (onPick) {
        return h(BandBar, {
        rows: agingRows([].concat.apply([], filtered.map(function (c) { return c.vacancy_aging || []; }))),
        label: "Vacant units by how long they have been empty",
        onPick: onPick,
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
        });
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

      h(Panel, {
        title: "Move-in / move-out history",
        note: "One candle a month · wick is the churn, body is what it bought · ○ open month"
      },
        h(CandleChart, {
          series: d.trends.moves, height: 260,
          ariaLabel: "Net resident movement by month, as candlesticks"
        }),
        h("div", { className: "legend" },
          h("span", null,
            h("i", { style: { background: "transparent",
                              border: "2px solid var(--gain)" } }),
            "Gained residents (hollow, above zero)"),
          h("span", null, h("i", { style: { background: "var(--loss)" } }),
            "Lost residents (filled, below zero)"),
          h("span", null, "Wick top = move-ins, wick bottom = move-outs"),
          h("span", null, "⇈ off scale, onboarding load"),
          h("span", null, "○ open month, partial")),
        h("div", { className: "note", style: { marginTop: "10px", fontSize: "12px",
                                               color: "var(--text-muted)" } },
          (function () {
            var ms = d.trends.moves || [];
            var closed = ms.filter(function (m) { return !m.partial; });
            var last = closed[closed.length - 1];
            var trail = closed.slice(-13, -1);
            // Onboarding months are excluded from the trailing figure. Left in,
            // 514 residents inherited with Riverwalk and The Oaks read as a
            // year of leasing wins that never happened.
            var real = trail.filter(function (m) { return !m.onboarding; });
            var load = trail.filter(function (m) { return m.onboarding; });
            var churn = real.reduce(function (a, m) { return a + m.ins + m.outs; }, 0);
            var net = real.reduce(function (a, m) { return a + m.net; }, 0);
            return "Body spans zero to the month's net, wick from minus the move-outs to " +
              "plus the move-ins, so the two always reconcile. " +
              (last ? "Last closed month " + monthLabel(last.month) + ": " + last.ins +
                      " in, " + last.outs + " out. " : "") +
              (real.length
                ? "Over the " + real.length + " clean months before it, " + count(churn) +
                  " moves netted " + (net > 0 ? "+" : "") + net + ". "
                : "") +
              (load.length
                ? load.length + " of the last twelve months are excluded from that: " +
                  load.map(function (m) { return monthShort(m.month); }).join(", ") +
                  " carried " +
                  count(load.reduce(function (a, m) { return a + m.onboarding_ins; }, 0)) +
                  " move-ins from communities being loaded into Rent Manager, which is " +
                  "inherited occupancy, not leasing."
                : "");
          })())),

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
        group: function (t) { return count(t.ar_accounts); } },
      // Point in time, not period, so these read the same in either mode.
      { key: "evictions_open", label: "In eviction", numeric: true,
        title: "Open eviction cases from the tracker, and what those accounts owe",
        sortValue: function (r) { return V(r).evictions_open; },
        render: function (r) {
          return V(r).evictions_open
            ? h("span", { className: "linkish", onClick: function () {
                  ctx.open(r, "evictions"); } }, count(V(r).evictions_open))
            : h("span", { style: { color: "var(--text-muted)" } }, "—"); },
        group: function (t) { return count(t.evictions_open); } },
      { key: "ar_needs_action", label: "Needs action", numeric: true,
        title: "Accounts past due 30+ with no open case, no payment plan and nobody moved out",
        sortValue: function (r) { return V(r).ar_needs_action; },
        render: function (r) {
          var x = V(r).ar_needs_action;
          return x
            ? h("span", { className: x >= 10 ? "down" : "" }, count(x))
            : h("span", { style: { color: "var(--text-muted)" } }, "—"); },
        group: function (t) {
          return h("span", { className: t.ar_needs_action >= 30 ? "down" : "" },
            count(t.ar_needs_action)); } }
    ];

    var groups = groupByVehicle(d, filtered, mode);
    var sum = function (k) { return filtered.reduce(function (s, c) { return s + (V(c)[k] || 0); }, 0); };
    var charged = sum("charged"), paid = sum("paid");

    /* The bar counts accounts carrying something 30 days old, not every account
       with a balance. Rent bills on the 1st, so on day four of a month every
       occupied lot owes money and a raw count reads like a portfolio in
       crisis. */
    var seg = (function () {
      var by = {}, late = {}, amt = {};
      filtered.forEach(function (c) {
        (c.ar_segments || []).forEach(function (g) {
          by[g.segment] = (by[g.segment] || 0) + g.accounts;
          late[g.segment] = (late[g.segment] || 0) + (g.accounts_30plus || 0);
          amt[g.segment] = (amt[g.segment] || 0) + g.past_due_30plus;
        });
      });
      return {
        rows: SEG_ORDER.filter(function (k) { return late[k]; }).map(function (k) {
          return { key: k, label: SEG_LABEL[k], n: late[k], money: amt[k], color: SEG_COLORS[k] };
        }),
        allAccounts: SEG_ORDER.reduce(function (a, k) { return a + (by[k] || 0); }, 0),
        lateAccounts: SEG_ORDER.reduce(function (a, k) { return a + (late[k] || 0); }, 0),
        needsAction: late.needs_action || 0,
        needsMoney: amt.needs_action || 0
      };
    })();

    var ev = (function () {
      var open = 0, bal = 0, attorney = 0, comms = 0, longest = 0;
      var phases = [];
      filtered.forEach(function (c) {
        var o = (c.evictions || []).filter(function (x) { return !x.closed; });
        if (!o.length) return;
        comms += 1;
        open += o.length;
        o.forEach(function (x) {
          bal += x.open_charges;
          if (x.with_attorney) attorney += 1;
          if ((x.days_open || 0) > longest) longest = x.days_open;
        });
        phases = phases.concat(c.eviction_phases || []);
      });
      return { open: open, bal: bal, attorney: attorney, comms: comms,
               longest: longest, rows: phaseRows(phases) };
    })();

    return h("div", null,
      h("div", { className: "grid-2" },
        h(Panel, {
          title: "What is behind the balances",
          note: "Accounts past due 30+ days, by what is already being done about them"
        }, h(BandBar, {
          rows: seg.rows, label: "Accounts past due by work bucket",
          empty: "Nothing past due 30 days.",
          note: count(seg.lateAccounts) + " of " + count(seg.allAccounts) +
                " accounts with a balance are actually 30 days behind; the rest is this " +
                "month's rent, billed on the 1st and not late until the " +
                d.period.grace_day + "th. In eviction and case stage come from the " +
                "eviction tracker. Needs action means no open case, no payment plan and " +
                "nobody who has moved out: " + count(seg.needsAction) + " accounts, " +
                money(seg.needsMoney) + ", that somebody has to call."
        })),
        h(Panel, {
          title: "Eviction funnel",
          note: "Open cases by how far along they are"
        }, h(BandBar, {
          rows: ev.rows, label: "Open eviction cases by phase",
          empty: "No open eviction cases.",
          note: count(ev.open) + " open cases across " + count(ev.comms) + " communities, " +
                money(ev.bal) + " owed, " + count(ev.attorney) + " already with the attorney" +
                (ev.longest ? ", oldest open " + count(ev.longest) + " days" : "") +
                ". Title and resale is not a resident eviction: it is recovering and " +
                "reselling an abandoned home."
        }))),

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
          money(sum("ar_total")), count(sum("ar_accounts")),
          count(sum("evictions_open")), count(sum("ar_needs_action"))
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

    // Both bars drill the same way they do on Occupancy. Leaving one tab's
    // bands clickable and the other's inert is the kind of inconsistency that
    // makes people stop trying.
    var vacantUnits = flattenVacant(filtered);
    var scopeLabel = filtered.length === d.communities.length
      ? "whole portfolio"
      : filtered.length + " of " + d.communities.length + " communities in view";

    return h("div", null,
      h(Panel, {
        title: "Where the vacancy actually is",
        note: "Proportion of vacant units by reason · click any band to list the units"
      }, h(VacancyPicker, {
        data: d, units: vacantUnits, field: "reason",
        keyOf: function (r) { return r.reason; },
        scope: scopeLabel, open: ctx.open
      }, function (onPick) {
        return h(ReasonBar, { rows: reasons, meta: d.reason_meta, onPick: onPick });
      })),

      h("div", { className: "grid-2" },
        h(Panel, {
          title: "Vacancy aging",
          note: "Days since the last move-out · click any band to list the units"
        }, h(VacancyPicker, {
          data: d, units: vacantUnits, field: "age_band",
          keyOf: function (r) { return r.key; },
          scope: scopeLabel, open: ctx.open
        }, function (onPick) {
          return h(BandBar, {
            rows: agingRows([].concat.apply([], filtered.map(function (c) { return c.vacancy_aging || []; }))),
            label: "Vacant units by age", onPick: onPick
          });
        })),
        h(Panel, {
          title: "Ready to Market pipeline",
          note: "Where each park-owned home sits between arriving and earning"
        }, (function () {
          var pipe = [].concat.apply([], filtered.map(function (c) { return c.home_pipeline || []; }));
          var rows = pipeRows(pipe);
          var earning = filtered.reduce(function (a, c) { return a + (c.homes_earning || 0); }, 0);
          var byStage = {};
          pipe.forEach(function (r) {
            var t = byStage[r.stage] || (byStage[r.stage] = { homes: 0, rtm: 0, ages: [] });
            t.homes += r.homes; t.rtm += r.rtm;
            if (r.median_age_days != null) t.ages.push(r.median_age_days);
          });
          var ready = (byStage.rtm ? byStage.rtm.homes : 0) + (byStage.listed ? byStage.listed.homes : 0);
          var notReady = byStage.for_sale_prep ? byStage.for_sale_prep.homes : 0;
          return h("div", null,
            h(BandBar, { rows: rows, label: "Homes by pipeline stage" }),
            h("div", { className: "note", style: { marginTop: "10px", fontSize: "12px",
                                                   color: "var(--text-muted)" } },
              count(ready) + " ready to market, " + count(earning) + " already earning" +
              (notReady ? ", " + count(notReady) + " listed for sale without the Ready to " +
                          "Market flag set" : "") +
              ". Ready to Market is a user-defined field on the Asset Listing, not a status, " +
              "which is why a home can read For Sale and not-ready at once. There is no punch " +
              "stage in Rent Manager, so rehab runs straight to ready."));
        })())),

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
        title: "Ready to Market pipeline by community",
        note: "Click a community to see every home, its status and how long it has been held",
        flush: true
      }, (function () {
        var rows = filtered.map(function (c) {
          var by = {};
          (c.home_pipeline || []).forEach(function (r) { by[r.stage] = r.homes; });
          var g = function (k) { return by[k] || 0; };
          return {
            name: c.name, community: c, vehicle: c.vehicle,
            homes: (c.homes || []).length,
            earning: c.homes_earning || 0,
            ordered: g("ordered"), delivered: g("delivered"), rehab: g("rehab"),
            not_ready: g("for_sale_prep"), rtm: g("rtm") + g("listed"),
            demo: g("demo"),
            pipeline: (c.home_pipeline || []).reduce(function (a, r) { return a + r.homes; }, 0),
            oldest: (function () {
              var ages = (c.homes || []).filter(function (x) { return x.stage && x.age_days != null; })
                .map(function (x) { return x.age_days; });
              return ages.length ? Math.max.apply(null, ages) : 0;
            })()
          };
        }).filter(function (r) { return r.homes; });
        var sumH = function (k) { return rows.reduce(function (a, r) { return a + r[k]; }, 0); };
        var dash = function (n) {
          return n ? count(n) : h("span", { style: { color: "var(--text-muted)" } }, "—");
        };
        return h(SortableTable, {
          cols: [
            { key: "name", label: "Community", render: function (r) {
                return h("span", null,
                  h("button", { className: "linkish",
                                onClick: function () { ctx.open(r.community, "homes"); },
                                title: "Every home at " + r.name },
                    r.name), " ", h("span", { className: "tag" }, r.vehicle)); } },
            { key: "homes", label: "Homes", numeric: true, render: function (r) { return count(r.homes); } },
            { key: "earning", label: "Earning", numeric: true,
              title: "Rented, rent to own, lease option or otherwise in use",
              render: function (r) { return dash(r.earning); } },
            { key: "pipeline", label: "In pipeline", numeric: true,
              render: function (r) { return dash(r.pipeline); } },
            { key: "ordered", label: "Ordered", numeric: true,
              render: function (r) { return dash(r.ordered); } },
            { key: "delivered", label: "Awaiting setup", numeric: true,
              render: function (r) { return dash(r.delivered); } },
            { key: "rehab", label: "In rehab", numeric: true,
              render: function (r) { return dash(r.rehab); } },
            { key: "not_ready", label: "Listed, not ready", numeric: true,
              title: "Status says For Sale but the Ready to Market flag is not set",
              render: function (r) {
                return r.not_ready
                  ? h("span", { className: "down" }, count(r.not_ready))
                  : h("span", { style: { color: "var(--text-muted)" } }, "—"); } },
            { key: "rtm", label: "Ready to market", numeric: true,
              render: function (r) {
                return r.rtm
                  ? h("span", { className: "up" }, count(r.rtm))
                  : h("span", { style: { color: "var(--text-muted)" } }, "—"); } },
            { key: "demo", label: "To demo", numeric: true,
              render: function (r) { return dash(r.demo); } },
            { key: "oldest", label: "Longest held", numeric: true,
              title: "Days since the in-service date of the oldest home still in the pipeline",
              render: function (r) {
                return r.oldest
                  ? h("span", { className: r.oldest > 730 ? "down" : "" }, count(r.oldest) + "d")
                  : h("span", { style: { color: "var(--text-muted)" } }, "—"); } }
          ],
          rows: rows, initialSort: { key: "pipeline", dir: -1 },
          footer: [rows.length + " communities with homes", count(sumH("homes")),
            count(sumH("earning")), count(sumH("pipeline")), count(sumH("ordered")),
            count(sumH("delivered")), count(sumH("rehab")), count(sumH("not_ready")),
            count(sumH("rtm")), count(sumH("demo")), ""]
        });
      })()),

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
      /* Order set by review: the P&L is what gets opened first, the budget
         charts are the next question asked of it, and the expense composition
         and utility picture are the analysis behind both. */
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

      h("div", { className: "grid-2" },
        h(Panel, {
          title: "Operating expense ratio",
          note: "Operating expense against revenue · closed " + monthLabel(d.period.closed)
        },
          /* The headline sits above the split, mirroring the recapture panel
             next to it: one KPI percentage, then its breakdown. The ratio is
             opex over revenue -- the figure the P&L is judged on -- while the
             controllable / non-controllable shares stay labelled on the bar. */
          (function () {
            var rev = filtered.reduce(function (a, c) { return a + (c.closed.revenue || 0); }, 0);
            var ratio = rev ? opex / rev * 100 : null;
            // Below the historical 33-42% range means expenses have not fully
            // posted, not that the month was efficient. Saying so is the
            // difference between a KPI and a trap.
            var low = ratio != null && ratio < 32;
            return h("div", null,
              h("div", { className: "bignum",
                         style: { color: ratio == null ? "var(--text-muted)"
                                  : low ? YELLOW : ratio <= 42 ? GREEN : RED } },
                ratio == null ? "—" : pct(ratio, 0)),
              h("div", { className: "ksub" },
                money(opex) + " of expense against " + money(rev) + " of revenue" +
                (low ? " · below the usual 33–42%, so expenses look part-posted" : "")));
          })(),
          h("div", { className: "split-bar", style: { marginTop: "12px" } },
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
        title: "Who pays for what",
        note: "A community that pays its own utilities has nothing to bill back, so a low rate there is the design and not a failure",
        flush: true
      },
        h("div", { className: "panel-body" },
          h("div", { className: "util-donuts" },
            ["water", "sewer", "trash"].map(function (svc) {
              /* Slice by who pays, count by community, and carry each group's
                 real utility spend and recapture into the legend. Weighting the
                 slice by dollars would be the more interesting cut but would be
                 wrong: the ledger gives one utilities figure per community, not
                 one per service, so there is no honest way to split a
                 community's spend across water, sewer and trash. */
              var buckets = {};
              filtered.forEach(function (c) {
                var u = c.utilities_service || {}, e = E(c);
                var who = (u[svc + "_paid_by"] || "").trim();
                var key = !who ? "unknown"
                  : /^resident/i.test(who) ? "resident"
                  : /^communit/i.test(who) ? "community" : "mixed";
                var t = buckets[key] || (buckets[key] = { n: 0, spend: 0, recovered: 0 });
                t.n += 1;
                t.spend += e.utilities || 0;
                t.recovered += e.utility_reimbursements || 0;
              });
              var LABELS = {
                resident: "Resident pays", community: "Community pays",
                mixed: "Mixed by section", unknown: "Not recorded"
              };
              var COLORS = {
                resident: "var(--pay-resident)", mixed: "var(--pay-mixed)",
                community: "var(--pay-community)", unknown: "var(--text-muted)"
              };
              return h(Donut, {
                key: svc,
                title: svc.charAt(0).toUpperCase() + svc.slice(1),
                centerLabel: "communities",
                ariaLabel: "Who pays for " + svc + ", by community",
                rows: ["resident", "mixed", "community", "unknown"]
                  .filter(function (k) { return buckets[k]; })
                  .map(function (k) {
                    var t = buckets[k];
                    return {
                      key: k, label: LABELS[k], n: t.n, color: COLORS[k],
                      sub: t.spend
                        ? money(t.spend, { compact: true }) + " spend, " +
                          pct(t.recovered / t.spend * 100, 0) + " back"
                        : null
                    };
                  })
              });
            })),
          /* Service type is a different question -- what infrastructure is
             there -- and it has four classes on the sewer side, so it reads
             better as two bars than as two more donuts. */
          h("div", { style: { marginTop: "18px" } },
            ["water", "sewer"].map(function (svc) {
              var byType = {};
              filtered.forEach(function (c) {
                var t = ((c.utilities_service || {})[svc + "_service"] || "Not recorded").trim();
                byType[t] = (byType[t] || 0) + 1;
              });
              var keys = Object.keys(byType).sort(function (a, b) { return byType[b] - byType[a]; });
              var tot = keys.reduce(function (a, k) { return a + byType[k]; }, 0);
              var SHADES = ["var(--pay-community)", "var(--pay-resident)",
                            "var(--pay-mixed)", "#8FA3B2", "#C7D3DA"];
              return h("div", { key: svc, style: { marginBottom: "12px" } },
                h("div", { className: "rl-sub", style: { marginBottom: "4px" } },
                  svc.charAt(0).toUpperCase() + svc.slice(1) + " service"),
                h("div", { className: "split-bar" }, keys.map(function (k, i) {
                  return h("span", {
                    key: k, style: { width: (byType[k] / tot * 100) + "%", background: SHADES[i % 5] },
                    title: k + ": " + count(byType[k]) + " communities"
                  }, byType[k] / tot > 0.14 ? k + " " + byType[k] : "");
                })));
            })),
          h("div", { className: "note",
                     style: { marginTop: "6px", fontSize: "12px", color: "var(--text-muted)" } },
            (function () {
              var recov = filtered.filter(function (c) {
                return (c.utilities_service || {}).recoverable;
              });
              return count(recov.length) + " of " + count(filtered.length) +
                " communities bill at least one utility back to residents. The other " +
                count(filtered.length - recov.length) + " pay their own, so nothing there " +
                "is recoverable and a low rate is the design. Service and who-pays come " +
                "from the Property Data Sheet; spend and billed-back come from the ledger.";
            })())),
        h("details", { className: "fold" },
          h("summary", null, "Show all " + count(filtered.length) +
            " communities with spend, billed back and what is absorbed"),
          h(SortableTable, {
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
          }))));
  }
  var NOTE_EVENT = {
    opened: "Opened", changed: "Figure changed",
    reopened: "Came back", resolved: "Cleared"
  };

  function noteAge(f) {
    if (f.days_open == null) return "age unknown";
    if (f.days_open === 0) return "first seen today";
    return f.days_open + (f.days_open === 1 ? " day old" : " days old");
  }

  /* One data note, opened. The card carries the headline; everything that
     qualifies it lives here, plus what the note has said over time -- a figure
     that has moved four times since it appeared is a different problem from one
     that has sat unchanged. */
  function NoteDetail(props) {
    var f = props.note;
    return h(Modal, {
      title: f.title,
      subtitle: [
        f.resolved ? "Cleared " + f.resolved_on : (f.severity === "warn" ? "Needs a look" : "For context"),
        "first seen " + (f.first_seen || "unknown"),
        // The date is already above; this is the duration, phrased as one.
        f.days_open == null ? null
          : f.days_open === 0 ? "open today"
          : "open " + f.days_open + (f.days_open === 1 ? " day" : " days"),
        f.changes
          ? f.changes + (f.changes === 1 ? " change since" : " changes since")
          : "unchanged since it opened"
      ].filter(Boolean).join("  ·  "),
      onClose: props.onClose
    },
      h("div", { className: "note-detail" }, f.detail),
      (f.history || []).length
        ? h("div", { className: "note-history" },
            h("h4", null, "History"),
            (f.history || []).map(function (hh, i) {
              return h("div", { className: "nh-row", key: i },
                h("div", { className: "nh-when" }, hh.date),
                h("div", null,
                  h("span", {
                    className: "chip " + (hh.event === "resolved" ? "good"
                      : hh.event === "reopened" ? "critical"
                      : hh.severity === "warn" ? "watch" : "")
                  }, NOTE_EVENT[hh.event] || hh.event),
                  h("div", { className: "nh-title" }, hh.title)));
            }))
        : null);
  }

  /* Data notes as summary cards: the headline only, with the qualification and
     the history one click away.

     They used to be a stacked list of title-plus-paragraph, which read as a
     wall nobody finished. The headline is the part that decides whether you
     care; the paragraph is what you read once you do. */
  function Exceptions(props) {
    var openSt = useState(false);
    var open = openSt[0], setOpen = openSt[1];
    var sevSt = useState("all");
    var sev = sevSt[0], setSev = sevSt[1];
    var sortSt = useState("priority");
    var sort = sortSt[0], setSort = sortSt[1];
    var qSt = useState("");
    var q = qSt[0], setQ = qSt[1];
    var pickSt = useState(null);
    var pick = pickSt[0], setPick = pickSt[1];

    var all = props.flags || [];
    if (!all.length) return null;

    var live = all.filter(function (f) { return !f.resolved; });
    var warns = live.filter(function (f) { return f.severity === "warn"; }).length;
    var infos = live.length - warns;
    var cleared = all.length - live.length;

    var FILTERS = [
      { id: "all", label: "All", n: live.length },
      { id: "warn", label: "Needs a look", n: warns },
      { id: "info", label: "For context", n: infos },
      { id: "resolved", label: "Cleared", n: cleared }
    ].filter(function (x) { return x.n; });

    var SORTS = [
      { id: "priority", label: "Priority" },
      { id: "newest", label: "Newest first" },
      { id: "aging", label: "Oldest first" },
      { id: "changed", label: "Most changed" },
      { id: "az", label: "A to Z" }
    ];

    var rows = all.filter(function (f) {
      if (sev === "resolved") { if (!f.resolved) return false; }
      else if (f.resolved) return false;
      if (sev === "warn" && f.severity !== "warn") return false;
      if (sev === "info" && f.severity !== "info") return false;
      if (q) {
        var t = (f.title + " " + f.detail).toLowerCase();
        if (t.indexOf(q.toLowerCase()) === -1) return false;
      }
      return true;
    });

    // Priority is severity first, then how long it has been sitting there. A
    // warning open for three months outranks one that appeared this morning.
    var byAge = function (a, b) { return (b.days_open || 0) - (a.days_open || 0); };
    rows = rows.slice().sort(function (a, b) {
      if (sort === "priority") {
        var sa = a.severity === "warn" ? 0 : 1, sb = b.severity === "warn" ? 0 : 1;
        return sa !== sb ? sa - sb : byAge(a, b);
      }
      if (sort === "newest") return String(b.first_seen || "").localeCompare(String(a.first_seen || ""));
      if (sort === "aging") return String(a.first_seen || "").localeCompare(String(b.first_seen || ""));
      if (sort === "changed") return (b.changes || 0) - (a.changes || 0) || byAge(a, b);
      return a.title.localeCompare(b.title);
    });

    return h("div", { className: "exceptions no-print" },
      h("button", {
        className: "exceptions-head", onClick: function () { setOpen(!open); },
        "aria-expanded": open ? "true" : "false"
      },
        h("span", { className: "caret" }, open ? "▼" : "▶"),
        h("strong", null, "Data notes"),
        warns ? h("span", { className: "pill-count warn" }, warns + " needs a look") : null,
        infos ? h("span", { className: "pill-count info" }, infos + " for context") : null,
        cleared ? h("span", { className: "pill-count" }, cleared + " cleared") : null,
        h("span", { className: "spacer" }),
        h("span", { style: { color: "var(--text-muted)", fontSize: "11.5px" } },
          open ? "Hide" : "Read before acting on these numbers")),

      open ? h("div", { className: "note-shell" },
        h("div", { className: "note-controls" },
          h("div", { className: "note-chips", role: "group", "aria-label": "Filter data notes" },
            FILTERS.map(function (x) {
              return h("button", {
                key: x.id, type: "button",
                className: "note-chip" + (sev === x.id ? " on" : ""),
                "aria-pressed": sev === x.id ? "true" : "false",
                onClick: function () { setSev(x.id); }
              }, x.label, h("span", { className: "nc-n" }, x.n));
            })),
          h("span", { className: "spacer" }),
          h("label", { className: "note-sort" }, "Sort",
            h("select", {
              value: sort,
              onChange: function (e) { setSort(e.target.value); }
            }, SORTS.map(function (o) {
              return h("option", { key: o.id, value: o.id }, o.label);
            }))),
          h("input", {
            className: "note-search", type: "search", value: q,
            placeholder: "Filter by word",
            "aria-label": "Filter data notes by word",
            onChange: function (e) { setQ(e.target.value); }
          })),

        rows.length
          ? h("div", { className: "note-cards" }, rows.map(function (f) {
              return h("button", {
                key: f.id, type: "button",
                className: "note-card " + f.severity + (f.resolved ? " done" : ""),
                onClick: function () { setPick(f); },
                title: "Open the detail and history"
              },
                h("div", { className: "nc-top" },
                  h("span", { className: "nc-dot" }),
                  h("span", { className: "nc-age" },
                    f.resolved ? "cleared " + f.resolved_on : noteAge(f))),
                h("div", { className: "nc-title" }, f.title),
                h("div", { className: "nc-foot" },
                  // Only say something when there is something to say. On the
                  // ledger's first day every note would otherwise carry the
                  // same "no change" line, twenty-one times over.
                  f.changes
                    ? h("span", null, f.changes + (f.changes === 1 ? " change" : " changes"))
                    : null,
                  h("span", { className: "nc-open" }, "Details \u2192")));
            }))
          : h("div", { className: "loading" }, "No notes match that filter."),

        h("div", { className: "note-foot" },
          "Age counts from the first build that recorded a note, not from when the " +
          "underlying problem started. The ledger began " + (props.ledgerFrom || "recently") +
          ", so anything older than that reads as first seen then.")) : null,

      pick ? h(NoteDetail, { note: pick, onClose: function () { setPick(null); } }) : null);
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
      // Opening a community lands on its hot sheet. Callers that want a
      // specific view -- a vacancy band, an AR bucket -- still name one, and
      // those deep links are the reason this default sits here rather than
      // only in CommunityDrill.
      open: function (community, view) { setDrill({ community: community, view: view || "hot" }); },
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

      h(Exceptions, { flags: d.flags, ledgerFrom: d.ledger_from }),

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
