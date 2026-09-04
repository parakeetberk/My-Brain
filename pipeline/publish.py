#!/usr/bin/env python3
"""
publish.py -- assemble the standalone dashboard page.

Inlines styles.css, app.js, the Parakeet logo and the built data payload into a
single self-contained HTML file, ready to hand to the Artifact tool.

    python3 pipeline/publish.py [--out build/parakeet_ops_dashboard.html]

Two outputs from the same source:

  default        page content only -- <title>, <style>, pinned React UMD script
                 tags, then the app. The Artifact runtime supplies the <head>
                 and <body> skeleton, and cdnjs is on its CSP allowlist.

  --standalone   a complete .html document with React inlined from
                 dashboard/vendor/ and the font dropped. Opens by double-click
                 with no network at all, which is what a file sent by email
                 needs; the CDN version renders blank if the script is blocked.
"""
import argparse
import base64
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Chosen for the Artifact CSP: cdnjs is allowlisted for scripts, Google Fonts
# for stylesheets. Versions are pinned deliberately.
REACT = "https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js"
REACT_DOM = "https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js"
FONT = ("https://fonts.googleapis.com/css2?family=Red+Hat+Display:"
        "wght@400;500;600;700;800&display=swap")


def die(msg):
    print("[publish] ERROR: " + msg, file=sys.stderr)
    sys.exit(1)


def read(path):
    if not os.path.exists(path):
        die("missing " + path)
    with open(path, encoding="utf-8") as f:
        return f.read()


def logo_uri():
    """Base64 the brand logo so the page stays self-contained."""
    candidates = [
        os.path.join(HERE, "dashboard", "assets", "logo_with_tagline.png"),
        os.path.join(HERE, "assets", "logo_with_tagline.png"),
    ]
    for p in candidates:
        if os.path.exists(p):
            with open(p, "rb") as f:
                return "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")
    print("[publish] note: no logo found, header will run without it")
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=os.path.join(HERE, "data", "dashboard.json"))
    ap.add_argument("--out", default=None)
    ap.add_argument("--standalone", action="store_true",
                    help="emit a complete document with React inlined, for sending as a file")
    args = ap.parse_args()
    if not args.out:
        args.out = os.path.join(
            HERE, "build",
            "Parakeet_Ops_Dashboard.html" if args.standalone else "parakeet_ops_dashboard.html")

    payload = json.loads(read(args.data))
    css = read(os.path.join(HERE, "dashboard", "styles.css"))
    app = read(os.path.join(HERE, "dashboard", "app.js"))

    # The data is injected as a JS literal. `</script>` inside a string would
    # close the tag early, and U+2028/9 are raw line breaks in JS source.
    data_js = (json.dumps(payload, separators=(",", ":"))
               .replace("</", "<\\/")
               .replace(" ", "\\u2028")
               .replace(" ", "\\u2029"))

    period = "%s closed, %s live" % (payload["period"]["closed"], payload["period"]["live"])
    title = "Property Operations"

    if args.standalone:
        react_js = read(os.path.join(HERE, "dashboard", "vendor", "react.production.min.js"))
        react_dom_js = read(os.path.join(HERE, "dashboard", "vendor", "react-dom.production.min.js"))
        # A complete document, no external requests. Red Hat Display is dropped
        # rather than linked, so the brand's Calibri fallback carries it offline.
        html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} - Parakeet Communities</title>
<style>
{css}
</style>
</head>
<body>
<div id="root"><div class="loading">Loading portfolio data\u2026</div></div>
<script>
{react}
</script>
<script>
{react_dom}
</script>
<script>
window.__PK_LOGO__ = "{logo}";
window.__DASHBOARD_DATA__ = {data};
</script>
<script>
{app}
</script>
</body>
</html>
""".format(title=title, css=css, react=react_js, react_dom=react_dom_js,
           logo=logo_uri(), data=data_js, app=app)
    else:
        html = """<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{font}">
<style>
{css}
</style>
<div id="root"><div class="loading">Loading portfolio data\u2026</div></div>
<script src="{react}"></script>
<script src="{react_dom}"></script>
<script>
window.__PK_LOGO__ = "{logo}";
window.__DASHBOARD_DATA__ = {data};
</script>
<script>
{app}
</script>
""".format(title=title, font=FONT, css=css, react=REACT, react_dom=REACT_DOM,
           logo=logo_uri(), data=data_js, app=app)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(html)

    size_kb = os.path.getsize(args.out) / 1024
    print("[publish] wrote %s (%.0f KB) for %s" % (args.out, size_kb, period))
    if size_kb > 16 * 1024:
        die("page exceeds the 16MB artifact limit")

    # Cheap structural checks. A silent typo here ships a blank page.
    for needle, what in [
        ("window.__DASHBOARD_DATA__", "data payload"),
        ("id=\"root\"", "mount point"),
        ("__PK_MOUNT__", "app bootstrap"),
        ("<title>", "title"),
    ]:
        if needle not in html:
            die("assembled page is missing its %s" % what)
    if args.standalone:
        for tag in ("<!DOCTYPE html>", "<html", "</html>", "<head>", "<body>"):
            if tag.lower() not in html.lower():
                die("standalone file is missing %s" % tag)
        if "cdnjs" in html or "fonts.googleapis" in html:
            die("standalone file still references a CDN; it must open with no network")
        if "React" not in html:
            die("standalone file has no React inlined")
    else:
        for tag in ("<!DOCTYPE", "<html", "<head>", "<body>"):
            if tag.lower() in html.lower():
                die("page contains %s; the artifact runtime supplies the skeleton" % tag)
    print("[publish] structure OK%s" % (" (standalone)" if args.standalone else ""))


if __name__ == "__main__":
    main()
