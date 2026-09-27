"""Patch the entry counts in README.md to match current state of concepts/,
methods/, practices/, sources/. Idempotent — re-running with no changes is a no-op.

The README has five count strings that need to stay in sync as the KB grows:
- "<N> atomic named phenomena" (concepts)
- "<N> structured guides" (methods)
- "<N> source-grounded routines" (practices)
- "<N> curated sources" (sources)
- "all <N> entries" (total in the index.md callout)

If the README's wording changes in the future and the regex no longer matches,
the script silently no-ops on that line rather than corrupting the file.

## Usage

    uv run python tooling/scripts/update_readme_counts.py            # apply patches
    uv run python tooling/scripts/update_readme_counts.py --check    # report only, don't write
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# On Windows the default console encoding (cp1252) can't encode characters like
# the arrow in change lines ("updated concepts: 62 -> 64"), which raised
# UnicodeEncodeError mid-run and aborted the script *before* it wrote README.md.
# Force UTF-8 output and never let an unencodable glyph crash a status print.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

KB_ROOT = Path(__file__).resolve().parents[2]
README = KB_ROOT / "README.md"


def count_entries() -> dict[str, int]:
    return {
        "concepts": len(list((KB_ROOT / "concepts").glob("*.md"))),
        "methods": len(list((KB_ROOT / "methods").glob("*.md"))),
        "practices": len(list((KB_ROOT / "practices").glob("*.md"))),
        "sources": len(list((KB_ROOT / "sources").glob("*.md"))),
    }


# Each tuple: (regex_pattern_with_count_group_named, replacement_template)
# The replacement template uses {n} which we substitute. The pattern uses a
# backreference to capture surrounding text, so the line stays identical
# except for the number.
PATCHES = [
    (
        re.compile(r"(`practices/` — )(\d+)( source-grounded routines)"),
        "practices",
    ),
    (
        re.compile(r"(`concepts/` — )(\d+)( atomic named phenomena)"),
        "concepts",
    ),
    (
        re.compile(r"(`methods/` — )(\d+)( structured guides)"),
        "methods",
    ),
    (
        re.compile(r"(`sources/` — )(\d+)( curated sources)"),
        "sources",
    ),
    (
        re.compile(r"(scannable catalog of all )(\d+)( entries)"),
        "total",
    ),
]


def patch_text(text: str, counts: dict[str, int]) -> tuple[str, list[str]]:
    """Apply all patches. Returns (new_text, list_of_changes_human_readable)."""
    new_text = text
    changes: list[str] = []
    total = sum(counts.values())
    values = {**counts, "total": total}
    for pat, key in PATCHES:
        n = values[key]
        m = pat.search(new_text)
        if not m:
            # Pattern not found — README wording may have changed. No-op.
            changes.append(f"  (no-op) pattern for '{key}' not found in README")
            continue
        old_n = int(m.group(2))
        if old_n == n:
            changes.append(f"  (unchanged) {key}: {n}")
            continue
        new_text = pat.sub(rf"\g<1>{n}\g<3>", new_text, count=1)
        changes.append(f"  updated {key}: {old_n} → {n}")
    return new_text, changes


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="report changes but don't write")
    args = parser.parse_args(argv)

    if not README.is_file():
        print(f"error: {README} not found", file=sys.stderr)
        return 2

    counts = count_entries()
    text = README.read_text(encoding="utf-8")
    new_text, changes = patch_text(text, counts)

    print(f"Counts: {counts['concepts']} concepts, {counts['methods']} methods, "
          f"{counts['practices']} practices, {counts['sources']} sources, {sum(counts.values())} total")
    for c in changes:
        print(c)

    if new_text != text:
        if args.check:
            print(f"\n--check: README would change but was not written.")
            return 1
        README.write_text(new_text, encoding="utf-8")
        print(f"\nWrote {README}")
    else:
        print("\nREADME already up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
