#!/usr/bin/env python3
"""
publish.py -- assemble the standalone dashboard page.

Inlines styles.css, app.js, the Parakeet logo and the built data payload into a
single self-contained HTML file, ready to hand to the Artifact tool.

    python3 pipeline/publish.py [--out build/parakeet_ops_dashboard.html]

The artifact runtime wraps the file in its own <head>, so this writes page
content only: <title>, <style>, the pinned React UMD scripts, then the app.
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
    ap.add_argument("--out", default=os.path.join(HERE, "build", "parakeet_ops_dashboard.html"))
    args = ap.parse_args()

    payload = json.loads(read(args.data))
    css = read(os.path.join(HERE, "dashboard", "styles.css"))
    app = read(os.path.join(HERE, "dashboard", "app.js"))

    # The data is injected as a JS literal. `</script>` inside a string would
    # close the tag early, and U+2028/9 are raw line breaks in JS source.
    data_js = (json.dumps(payload, separators=(",", ":"))
               .replace("</", "<\\/")
               .replace(" ", "\\u2028")
               .replace(" ", "\\u2029"))

    period = payload["period"]["headline"]
    title = "Property Operations"

    html = """<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{font}">
<style>
{css}
</style>
<div id="root"><div class="loading">Loading portfolio data…</div></div>
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
    for tag in ("<!DOCTYPE", "<html", "<head>", "<body>"):
        if tag.lower() in html.lower():
            die("page contains %s; the artifact runtime supplies the skeleton" % tag)
    print("[publish] structure OK")


if __name__ == "__main__":
    main()
