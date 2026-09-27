"""Sync the ## Sources section in concept, method and practice entries.

For each non-source entry with citations in `sources:` frontmatter,
build (or update) a `## Sources` section in the body with wikilinks
to the matching source entries. This makes citation navigation
clickable in Obsidian without changing the frontmatter schema.

When source_entries is present, use those exact source stems. This is required
for new practice integrations where several articles share an author and year.
The list can include supporting/counterexample records; their roles stay in the
entry's Origin and Evidence sections. Citation strings remain separately visible.

Legacy match logic: extract first-author surname + 4-digit year from each
citation, find the source entry whose stem starts with that surname
and ends with that year. Diacritic-insensitive.

If a citation can't be matched (ambiguous or no source entry), it's
written as plain text with a TODO marker.

Usage:
    uv run python tooling/scripts/sync-source-links.py            # update all entries
    uv run python tooling/scripts/sync-source-links.py --dry-run  # preview, no writes
    uv run python tooling/scripts/sync-source-links.py --entry scan  # single entry
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

_DIR = Path(__file__).resolve().parent
if str(_DIR) not in sys.path:
    sys.path.insert(0, str(_DIR))

from kb_search import Entry, load_entries  # noqa: E402

_ALIAS_PATH = _DIR.parent / 'citation-aliases.json'
_ALIASES = json.loads(_ALIAS_PATH.read_text(encoding='utf-8')) if _ALIAS_PATH.exists() else {}


def _normalize(s: str) -> str:
    """Lowercase + strip diacritics for robust matching."""
    return "".join(
        c for c in unicodedata.normalize("NFKD", s.lower()) if not unicodedata.combining(c)
    )


def find_source_match(citation: str, source_stems: set[str]) -> str | None:
    """Match a citation string to a source entry stem. Returns stem or None."""
    if not citation or not citation.strip():
        return None
    alias = _ALIASES.get(citation)
    if alias and alias.get('source') in source_stems and alias.get('reason') and alias.get('evidence'):
        return alias['source']

    # Extract year (prefer parenthesized; fall back to trailing 4-digit)
    year_match = re.search(r"\((\d{4})\)", citation) or re.search(r"\b(\d{4})\b", citation)
    if not year_match:
        return None
    year = year_match.group(1)

    # Extract first author surname (first word, allowing diacritics)
    first_word = re.match(r"([\w\u00C0-\u017F\u0100-\u024F]+)", citation, re.UNICODE)
    if not first_word:
        return None
    author = _normalize(first_word.group(1))
    if len(author) < 2:
        return None

    # Match: stem must start with author surname, end with year
    candidates = [
        s for s in source_stems
        if s.startswith(author + "-") and s.endswith("-" + year)
    ]

    if len(candidates) == 1:
        return candidates[0]
    if len(candidates) > 1:
        # Ambiguous — could refine by topic later, but flag for now
        return None
    return None


def build_sources_section(citations: list[str], source_stems: set[str], source_entries: list[str] | None = None) -> tuple[str, list[str]]:
    """Build the ## Sources section. Returns (section_text, unmatched_citations).

    Matched citations get wikilinks. Unmatched citations are written as plain
    text (no TODO marker in the body — that's noise). Unmatched list is
    returned for separate reporting.
    """
    lines = ["## Sources", ""]
    unmatched: list[str] = []

    if source_entries:
        for stem in dict.fromkeys(source_entries):
            if stem in source_stems:
                lines.append(f"- [[{stem}]]")
            else:
                lines.append(f"- {stem} (source entry missing)")
                unmatched.append(stem)
        if citations:
            lines.extend(["", "Recorded citations:", ""])
            lines.extend(f"- {c.strip()}" for c in citations if c.strip())
        return "\n".join(lines), unmatched

    for citation in citations:
        citation = citation.strip()
        if not citation:
            continue
        stem = find_source_match(citation, source_stems)
        if stem:
            lines.append(f"- [[{stem}]] — {citation}")
        else:
            lines.append(f"- {citation}")
            unmatched.append(citation)

    return "\n".join(lines), unmatched


SOURCES_SECTION_RE = re.compile(
    r"^##\s+Sources\s*\n.*?(?=^##\s+|\Z)",
    re.MULTILINE | re.DOTALL,
)


def sync_entry(entry: Entry, source_stems: set[str], dry_run: bool = False) -> tuple[bool, list[str]]:
    """Read entry, sync ## Sources section. Returns (changed, unmatched_citations)."""
    if not entry.sources and not entry.source_entries:
        return False, []

    text = Path(entry.path).read_text(encoding="utf-8")
    new_section, unmatched = build_sources_section(entry.sources, source_stems, entry.source_entries)
    if not new_section.strip():
        return False, unmatched

    if SOURCES_SECTION_RE.search(text):
        new_text = SOURCES_SECTION_RE.sub(lambda _: new_section + "\n\n", text, count=1)
    else:
        new_text = text.rstrip() + "\n\n" + new_section + "\n"

    if new_text == text:
        return False, unmatched

    if not dry_run:
        Path(entry.path).write_text(new_text, encoding="utf-8")
    return True, unmatched


def main(argv: list[str] | None = None) -> int:
    # Force UTF-8 on stdout/stderr so Polish names etc. don't crash on Windows cp1252.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Sync ## Sources sections from frontmatter citations.")
    parser.add_argument("--dry-run", action="store_true", help="show what would change, no writes")
    parser.add_argument("--entry", type=str, help="sync only the named entry (stem)")
    args = parser.parse_args(argv)

    entries = load_entries()
    source_stems = {stem for stem, e in entries.items() if e.type == "source"}

    targets = [
        e for e in entries.values()
        if e.type != "source" and (e.sources or e.source_entries) and (not args.entry or e.stem == args.entry)
    ]

    if args.entry and not targets:
        print(f"No entry named '{args.entry}' found (or it has no sources).", file=sys.stderr)
        return 1

    updated = 0
    all_unmatched: list[tuple[str, list[str]]] = []

    for entry in targets:
        changed, unmatched = sync_entry(entry, source_stems, dry_run=args.dry_run)
        if changed:
            updated += 1
            print(f"  {'[dry] ' if args.dry_run else ''}updated: {entry.stem}")
        if unmatched:
            all_unmatched.append((entry.stem, unmatched))

    verb = "Would update" if args.dry_run else "Updated"
    print(f"\n{verb} {updated}/{len(targets)} entries")

    if all_unmatched:
        print(f"\n{len(all_unmatched)} entries have unresolved source references:")
        for stem, citations in all_unmatched:
            print(f"  {stem}:")
            for c in citations:
                print(f"    - {c}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
