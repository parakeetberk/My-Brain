#!/usr/bin/env python3
"""Reindex an Obsidian vault from a flat lot folder to one folder per community.

    60-Communities/lots/BELL-5.md          ->  60-Communities/Belle Haven/lots/BELL-5.md
    60-Communities/Belle Haven.md          ->  60-Communities/Belle Haven/Belle Haven.md

The lot filename keeps its short-code prefix on purpose. Obsidian resolves a
bare [[BELL-5]] by filename, so every short-form link in the vault survives the
move untouched; only the long-form [[60-Communities/lots/BELL-5|Lot 5]] links
need rewriting, and this script rewrites them everywhere, not just on the
community pages.

Dry run by default. Nothing is touched without --apply.

    python3 reindex_communities.py /path/to/vault
    python3 reindex_communities.py /path/to/vault --apply
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

COMMUNITIES_DIR = "60-Communities"
LOTS_DIR = "lots"

# Roster lives next to the dashboard pipeline so the code -> community map stays
# in step with the Property Data Sheet rather than drifting in a second copy.
ROSTER = Path(__file__).resolve().parent.parent / "pipeline" / "raw" / "pds_reportable.json"


def load_roster():
    """short_name -> community name, longest code first so NGMH beats NG."""
    rows = json.loads(ROSTER.read_text())
    codes = {}
    for r in rows:
        code = (r.get("short_name") or "").strip()
        name = (r.get("community") or r.get("property_name") or "").strip()
        if code and name:
            codes[code] = name
    return dict(sorted(codes.items(), key=lambda kv: -len(kv[0])))


def split_lot(stem, codes):
    """'BELL-46A' -> ('BELL', 'Belle Haven'). None when no code matches."""
    for code, community in codes.items():
        if stem == code or stem.startswith(code + "-"):
            return code, community
    return None, None


def plan_moves(vault, codes):
    """Returns (moves, unmapped). A move is (src, dst) as absolute paths."""
    root = vault / COMMUNITIES_DIR
    moves, unmapped = [], []

    lots = root / LOTS_DIR
    if lots.is_dir():
        for src in sorted(lots.glob("*.md")):
            code, community = split_lot(src.stem, codes)
            if not community:
                unmapped.append(src)
                continue
            moves.append((src, root / community / LOTS_DIR / src.name))

    # A community hot sheet sitting beside the lots folder becomes the folder
    # note for its own directory.
    for src in sorted(root.glob("*.md")):
        if src.stem in codes.values():
            moves.append((src, root / src.stem / f"{src.stem}.md"))

    return moves, unmapped


def link_map(moves, vault):
    """Old vault-relative link target -> new one, extension stripped."""
    out = {}
    for src, dst in moves:
        old = src.relative_to(vault).as_posix()[: -len(".md")]
        new = dst.relative_to(vault).as_posix()[: -len(".md")]
        if old != new:
            out[old] = new
    return out


WIKILINK = re.compile(r"(!?\[\[)([^\]\|#\^]+)([^\]]*)(\]\])")


def rewrite(text, links):
    """Rewrite the target of every wikilink whose path we moved.

    Only the target segment is touched. Aliases, headings and block refs after
    the first | # or ^ are carried through verbatim.
    """
    n = 0

    def sub(m):
        nonlocal n
        target = m.group(2).strip()
        # Inside a markdown table the alias pipe is escaped, so the target
        # arrives as "60-Communities/lots/BELL-5\". Most links on the community
        # pages are in tables, so missing this would silently break the bulk of
        # them. Strip the backslash to match, then put it back.
        esc = ""
        if target.endswith("\\"):
            target, esc = target[:-1].rstrip(), "\\"
        if target in links:
            n += 1
            return m.group(1) + links[target] + esc + m.group(3) + m.group(4)
        return m.group(0)

    return WIKILINK.sub(sub, text), n


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("vault", type=Path, help="path to the Obsidian vault root")
    ap.add_argument("--apply", action="store_true", help="actually move files and rewrite links")
    args = ap.parse_args()

    vault = args.vault.expanduser().resolve()
    if not (vault / COMMUNITIES_DIR).is_dir():
        sys.exit(f"no {COMMUNITIES_DIR}/ under {vault} -- is that the vault root?")

    codes = load_roster()
    moves, unmapped = plan_moves(vault, codes)
    links = link_map(moves, vault)

    if not moves:
        print("nothing to move; the vault already looks reindexed")
        return

    print(f"{len(moves)} files to move, {len(links)} link targets to rewrite\n")
    for src, dst in moves[:10]:
        print(f"  {src.relative_to(vault)}  ->  {dst.relative_to(vault)}")
    if len(moves) > 10:
        print(f"  ... and {len(moves) - 10} more")

    if unmapped:
        print(f"\n{len(unmapped)} lot files carry no known community code and stay put:")
        for p in unmapped:
            print(f"  {p.relative_to(vault)}")

    # Count the rewrites before touching anything, so a dry run reports the real
    # blast radius across the whole vault rather than just the community pages.
    notes = [p for p in vault.rglob("*.md") if ".obsidian" not in p.parts and ".trash" not in p.parts]
    touched, edits = 0, 0
    for p in notes:
        new, n = rewrite(p.read_text(encoding="utf-8"), links)
        if n:
            touched += 1
            edits += n
            if args.apply:
                p.write_text(new, encoding="utf-8")

    print(f"\n{edits} links across {touched} of {len(notes)} notes")

    if not args.apply:
        print("\nDRY RUN. Nothing changed. Re-run with --apply once this looks right.")
        return

    for src, dst in moves:
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            print(f"  SKIP, target exists: {dst.relative_to(vault)}")
            continue
        # git mv where the vault is a repo, so history follows the file.
        try:
            subprocess.run(["git", "-C", str(vault), "mv", str(src), str(dst)],
                           check=True, capture_output=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            shutil.move(str(src), str(dst))

    lots = vault / COMMUNITIES_DIR / LOTS_DIR
    if lots.is_dir() and not any(lots.iterdir()):
        lots.rmdir()

    print(f"\ndone. {len(moves)} moved, {edits} links rewritten.")


if __name__ == "__main__":
    main()
