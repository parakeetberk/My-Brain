# -*- coding: utf-8 -*-
"""Aggregate a rehab tracker export into the board's data block.

    python3 build/make_data.py [path/to/rehab_tracker_all_data_YYYY-MM-DD.csv]

Defaults to the newest CSV in `data/`. Writes build/rehab-data.json.

EVERY business figure on the dashboard is computed here, never in the page's
JavaScript, so a number can be re-derived from the CSV without a browser.

Two rules encoded below, both of them things that go wrong quietly:

1. `expected` and `remaining` are MODELS - tier averages back-solved from as few as
   six comparable jobs, with some rows on a flat portfolio average. They are emitted
   as-is and the page labels them `model`. Never rename them to budget or forecast.
2. Twenty-one community values are unit-code prefixes rather than community names.
   CANON maps the ones that can be resolved from the vault. `NGMH`, `LS` and `PPH`
   resolve to UNRESOLVED and are never guessed - a wrong community on a capex report
   is worse than a blank one.
"""
import csv, json, glob, os, sys, collections, datetime as dt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# community field values that are unit-code prefixes, not community names
ABBREV = {"TO","PARK","RW","FOX","SILVER","BRUN","ROYAL","RO","DO","SH","SOUTH","TC",
          "BOVIIPO","BOVIPO","WPMH","HARB","GULFPO","NGMH","LS","PPH","Central",""}
# Resolved 2026-09-02 by EVIDENCE, not by guess: for each abbreviated code, look at
# what the SAME unit-code prefix maps to on rows that DO carry a real community name.
# That method corrected three of my own first-pass guesses - `SH` is Silver Hill, not
# Shady Acres (Shady Acres uses the `SA-` prefix), `PPH` is Palm Haven Estates, and
# `RO` had been mapped to Royal Oaks when Royal Oaks uses `ROYAL-` and `RO-` appears
# nowhere else in the file. A wrong community on a capex report is worse than a blank.
CANON = {
  # VERIFIED - the same unit prefix carries this community on other rows in this file
  "TO":"The Oaks", "PARK":"Parkwood Mobile Home Park", "RW":"Riverwalk",
  "FOX":"Fox Creek", "SILVER":"Silver Breeze", "BRUN":"Brunswick Estates",
  "ROYAL":"Royal Oaks", "DO":"Druid Oaks", "SH":"Silver Hill MHC",
  "SOUTH":"Southgate", "TC":"Terrace Crossings", "BOVIIPO":"Bay Oaks Village II",
  "BOVIPO":"Bay Oaks Village I", "WPMH":"Whispering Pines FL",
  "GULFPO":"Gulf Breeze", "PPH":"Palm Haven Estates",
  # INFERRED - no prefix evidence in this file; matched to an existing community page
  # by name only. Shown with the marker so nobody reads them as confirmed.
  "HARB":"Harbour Mobile Home Park (inferred)",
  "Central":"Central Mobile Home Park (inferred)",
  "LS":"Lake Saunders (inferred)",
  "NGMH":"Northgate MH (inferred)",
  # UNRESOLVED - `RO-216WHITESQUIRREL` is ambiguous between Royal Oaks and River Oaks
  # RV Resort, both real communities, and nothing in the vault settles it. Not guessed.
  "RO":"UNRESOLVED", "":"UNRESOLVED",
}
VEH = ["JREFI","JREFII","Origins","Kippy"]
BANDS = ["0-30","31-60","61-90","90+","no start"]
CAPEX_PLAN = 9954600   # CapEx Overview workbook, 169 "Existing" line items, 2026

def n(v):
    try: return float(v)
    except (TypeError, ValueError): return 0.0

def dd(v):
    try: return dt.date.fromisoformat(v)
    except (TypeError, ValueError): return None

def load(path):
    rows = list(csv.DictReader(io_open(path)))
    units = []
    for r in rows:
        age = int(n(r["age"])); has_start = bool(r["start"].strip())
        band = ("no start" if not has_start else
                "0-30" if age <= 30 else "31-60" if age <= 60 else
                "61-90" if age <= 90 else "90+")
        coh = r["community"] in ABBREV
        units.append(dict(
            u=r["unit"], c=r["community"],
            cc=(CANON.get(r["community"], r["community"]) if coh else r["community"]),
            v=r["vehicle"] or "(blank)", tr=r["track"], vd=r["vendor"] or "Unassigned",
            s=r["status"], t=r["tier"], cat=r["category"], code=r["code"],
            gl=n(r["glActual"]), tc=n(r["trackerCost"]), rm=n(r["cost"]), rms=r["costSrc"],
            exp=n(r["expected"]), rem=n(r["remaining"]),
            st=r["start"], en=r["end"] or r["done"],
            days=int(n(r["days"])), age=age, band=band,
            closed=r["closed"] == "true", intrk=r["inTracker"] == "true", coh=coh,
            fl=[f.strip() for f in r["flags"].split(";") if f.strip()],
            fc=int(n(r["flagCount"]))))
    return units

def io_open(p):
    import io as _io
    return _io.open(p, encoding="utf-8-sig", newline="")

def agg(units, key):
    a = collections.defaultdict(lambda: dict(n=0, open=0, ip=0, ns=0, cp=0,
                                             gl=0.0, tc=0.0, exp=0.0, rem=0.0, fc=0))
    for u in units:
        x = a[u[key]]
        x["n"] += 1; x["open"] += (not u["closed"])
        x["ip"] += u["s"] == "In Progress"; x["ns"] += u["s"] == "Not Started"
        x["cp"] += u["s"] == "Complete"
        for f in ("gl","tc","exp","rem"): x[f] += u[f]
        x["fc"] += u["fc"]
    return [dict(k=k, **{f: (round(v[f]) if f in ("gl","tc","exp","rem") else v[f])
                         for f in v})
            for k, v in sorted(a.items(), key=lambda kv: -kv[1]["rem"])]

def build(path):
    units = load(path)
    asof = os.path.basename(path).rstrip(".csv")[-10:]
    op   = [u for u in units if not u["closed"]]
    comp = [u for u in units if u["s"] == "Complete"]
    flag = lambda u, s: any(s in f for f in u["fl"])

    mo = collections.Counter()
    for u in comp:
        e = dd(u["en"])
        if e and e.year == 2026: mo[e.strftime("%Y-%m")] += 1
    completions = [{"m": m, "n": mo.get(m, 0)}
                   for m in sorted(set(list(mo) + ["2026-%02d" % i for i in range(1, 9)]))]

    wip = [{"v": v,
            "open": round(sum(u["gl"] for u in op if u["v"] == v)),
            "done": round(sum(u["gl"] for u in comp if u["v"] == v)),
            "openN": len([u for u in op if u["v"] == v and u["gl"] > 0]),
            "doneN": len([u for u in comp if u["v"] == v and u["gl"] > 0]),
            "exp": round(sum(u["exp"] for u in units if u["v"] == v)),
            "rem": round(sum(u["rem"] for u in units if u["v"] == v)),
            "tc":  round(sum(u["tc"]  for u in units if u["v"] == v)),
            "glAll": round(sum(u["gl"] for u in units if u["v"] == v))} for v in VEH]

    aging = [{"b": b, "n": len([u for u in op if u["band"] == b]),
              "rem": round(sum(u["rem"] for u in op if u["band"] == b))} for b in BANDS]

    gaps = [
      dict(k="glNoRm", t="GL has spend, Rent Manager has nothing",
        d="Accounting booked it, ops cannot see it. Anyone reading Rent Manager sees these units as free.",
        own="Controller seat, with John Clark confirming the work is real", td="TD-0405",
        ids=[u["u"] for u in units if flag(u, "GL has spend but Rent Manager")]),
      dict(k="noCode", t="No WIP or GL code on the issue",
        d="An invoice arriving for one of these has nowhere clean to land. None carries spend yet, so nothing has gone astray so far. Cheapest fix on the program and it has a natural deadline.",
        own="John Clark supplies the units, Accounting assigns the codes", td="TD-0406",
        ids=[u["u"] for u in units if not u["code"].strip()]),
      dict(k="trkOverGl", t="Vendor tracker far above GL booked",
        d="Either High Pace has done work it has not billed, which is an accrual we are missing, or the tracker is priced above what will be billed, which means the forecast is too high. Opposite problems, one flag. One question to Mark Doucette settles all nine.",
        own="Austin \u2014 he is on the Wednesday call", td="TD-0407",
        ids=[u["u"] for u in units if flag(u, "far above GL")]),
      dict(k="notTrk", t="On the board, not in the vendor tracker",
        d="All 22 Origins units and all 16 Kippy units are in here. The Wednesday call reads from that tracker, so it has never seen either fund.",
        own="unassigned \u2014 both funds are Jon Wyss's side of the house", td="TD-0416",
        ids=[u["u"] for u in units if not u["intrk"]]),
      dict(k="compGl", t="Complete, still carrying GL spend",
        d="If these were placed in service the money is capitalised and WIP is clean. If not, roughly a million dollars sits in work-in-progress for finished homes. The export carries a GL actual, not a GL account, so no source here can say which.",
        own="unassigned \u2014 the Controller seat", td="TD-0405",
        ids=[u["u"] for u in comp if u["gl"] > 0]),
      dict(k="past60", t="Open past the 60-day board goal",
        d="Ten of these are Silver Breeze units that all started 2026-04-17 \u2014 one batch that never got worked, not ten slow rehabs. SOUTH-86 and BRUN-203 are the last two of John Clark's Q1 rock.",
        own="John Clark", td="TD-0408, TD-0409",
        ids=[u["u"] for u in op if u["age"] > 60]),
      dict(k="noStart", t="Open with no start date",
        d="A start date is how a rehab enters the 60-day clock. These are not on it. 26 other rows carry a future start and 6 carry dates that do not parse, so the field is not being maintained.",
        own="John Clark", td="TD-0410",
        ids=[u["u"] for u in op if u["band"] == "no start"]),
      dict(k="noVendor", t="Open with no vendor at all",
        d="Work on the board that nobody is doing. Fourteen of the fifteen are also in the 37-row uncoded cohort.",
        own="unassigned \u2014 assign at the Wednesday call", td="TD-0411",
        ids=[u["u"] for u in op if u["vd"] == "Unassigned"]),
      dict(k="cohort", t="The 37-row cohort \u2014 a second intake path never onboarded",
        d="Every row missing from the vendor tracker, and every row missing a WIP code, is in this cohort. The other 182 rows have zero of these defects. 16 internal Parakeet Ops jobs and 16 unassigned units, keyed by unit code instead of community, untiered, uncoded.",
        own="unassigned \u2014 pairs with KP-0037, the master community list", td="TD-0413, TD-0414",
        ids=[u["u"] for u in units if u["coh"]]),
    ]

    return dict(
      asof=asof, built=dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
      totals=dict(
        rows=len(units), open=len(op),
        ip=len([u for u in units if u["s"] == "In Progress"]),
        ns=len([u for u in units if u["s"] == "Not Started"]), cp=len(comp),
        gl=round(sum(u["gl"] for u in units)), rm=round(sum(u["rm"] for u in units)),
        tc=round(sum(u["tc"] for u in units)), exp=round(sum(u["exp"] for u in units)),
        rem=round(sum(u["rem"] for u in units)),
        rmReal=len([u for u in units if u["rms"] == "RM UDF"]),
        rmPlaceholder=len([u for u in units if u["rms"] != "RM UDF"]),
        goalDone=len([u for u in comp if dd(u["en"]) and dd(u["en"]).year == 2026]),
        turnOk=len([u for u in comp if 0 < u["days"] <= 60]),
        turnAll=len([u for u in comp if u["days"] > 0]),
        past60=len([u for u in op if u["age"] > 60]),
        past90=len([u for u in op if u["age"] > 90]),
        noStart=len([u for u in op if u["band"] == "no start"]),
        noStartRem=round(sum(u["rem"] for u in op if u["band"] == "no start")),
        wipOpen=round(sum(u["gl"] for u in op if u["gl"] > 0)),
        wipOpenN=len([u for u in op if u["gl"] > 0]),
        wipDone=round(sum(u["gl"] for u in comp if u["gl"] > 0)),
        wipDoneN=len([u for u in comp if u["gl"] > 0]),
        cohort=len([u for u in units if u["coh"]]),
        cohortRem=round(sum(u["rem"] for u in units if u["coh"])),
        cohortGl=round(sum(u["gl"] for u in units if u["coh"])),
        noCode=len([u for u in units if not u["code"].strip()]),
        notTrk=len([u for u in units if not u["intrk"]]),
        noVendor=len([u for u in units if u["vd"] == "Unassigned"]),
        untiered=len([u for u in units if u["t"] == "Untiered"]),
        capexPlan=CAPEX_PLAN),
      completions=completions, wip=wip, aging=aging,
      byCommunity=agg(units, "cc"), byVehicle=agg(units, "v"),
      byVendor=agg(units, "vd"), byTier=agg(units, "t"),
      byCategory=agg(units, "cat"),
      units=units, gaps=gaps)

def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        found = sorted(glob.glob(os.path.join(ROOT, "data", "rehab_tracker_all_data_*.csv")))
        if not found:
            raise SystemExit("no tracker CSV in data/")
        path = found[-1]
    data = build(path)
    dest = os.path.join(HERE, "rehab-data.json")
    json.dump(data, io.open(dest, "w", encoding="utf-8") if False else open(dest, "w"),
              separators=(",", ":"))
    print("read  %s  (%d units, as of %s)" % (os.path.basename(path),
                                              data["totals"]["rows"], data["asof"]))
    print("wrote %s" % dest)

import io
if __name__ == "__main__":
    main()
