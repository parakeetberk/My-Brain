# -*- coding: utf-8 -*-
"""Assemble the rehab board into one self-contained page.

    python3 build/assemble.py

Reads src/head.html, src/body.html, build/rehab-data.json and src/app.js and writes
build/rehab-board.html. Publish that file to the artifact URL in build/README.md.

The page carries NO doctype, <html>, <head> or <body> tags: the Artifact publisher
wraps the content in its own skeleton. Adding them here produces a nested document.
"""
import io, os, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC  = os.path.join(HERE, "src")

def read(p):
    return io.open(p, encoding="utf-8").read()

def main():
    data_path = os.path.join(HERE, "rehab-data.json")
    if not os.path.exists(data_path):
        raise SystemExit("no rehab-data.json - run make_data.py first")
    data = read(data_path)
    json.loads(data)                      # fail loudly on malformed data
    data = data.replace("</", "\\u003c/")  # cannot break out of the script tag
    out = (read(os.path.join(SRC, "head.html")) + "\n"
           + read(os.path.join(SRC, "body.html")) + "\n"
           + '<script id="rehab" type="application/json">' + data + "</script>\n"
           + "<script>\n" + read(os.path.join(SRC, "app.js")) + "\n</script>\n")
    dest = os.path.join(HERE, "rehab-board.html")
    io.open(dest, "w", encoding="utf-8").write(out)
    print("wrote %s  %d bytes" % (dest, len(out)))

if __name__ == "__main__":
    main()
