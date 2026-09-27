"""Report unresolved active citation strings; this does not verify claim support.

Usage: uv run python tooling/scripts/check_citation_links.py [--entry STEM ...]
       Add --drafts raw/<batch>/drafts/updates to overlay correction drafts.

Only non-source entries are checked. Explicit reviewed aliases handle publication
years that differ from historical source stems. Ambiguous matches stay unresolved.
This is read-only and separate from the source-link synchronization workflow.
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

from kb_search import KB_ROOT, _parse_file, load_entries


def normalize(value: str) -> str:
    return ''.join(c for c in unicodedata.normalize('NFKD', value.lower())
                   if c.isalnum() and not unicodedata.combining(c))


def resolve(citation: str, source_stems: set[str], aliases: dict) -> str | None:
    if citation in aliases:
        alias = aliases[citation]
        target = alias.get('source')
        if target in source_stems and alias.get('reason') and alias.get('evidence'):
            return target
        return None
    year = re.search(r'\((\d{4})\)', citation) or re.search(r'\b(\d{4})\b', citation)
    author = re.match(r"([\w'’]+)", citation)
    if not year or not author:
        return None
    name = normalize(author.group(1))
    candidates = [s for s in source_stems if normalize(s.split('-')[0]) == name
                  and s.endswith('-' + year.group(1))]
    return candidates[0] if len(candidates) == 1 else None


def check_explicit_sources(entry, source_stems: set[str]) -> list[dict]:
    """Check reviewed exact identities, without guessing from first names/year.

    This checks navigation, not whether a citation or claim is supported.
    Source roles and the review manifest document that separate editorial work.
    """
    findings = []
    for target in entry.source_entries:
        if target not in source_stems:
            findings.append({'entry': entry.stem, 'source': target, 'issue': 'explicit source entry missing'})
        elif target not in entry.wikilinks:
            findings.append({'entry': entry.stem, 'source': target, 'issue': 'identity resolved but canonical link missing'})
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--entry', action='append', default=[])
    parser.add_argument('--drafts', type=Path)
    args = parser.parse_args()
    entries = load_entries()
    sources = {s for s, e in entries.items() if e.type == 'source'}
    aliases = json.loads((KB_ROOT / 'tooling/citation-aliases.json').read_text(encoding='utf-8'))
    findings = []
    for label, alias in aliases.items():
        evidence = (KB_ROOT / alias.get('evidence', '')).resolve()
        if not evidence.is_relative_to(KB_ROOT.resolve()) or not evidence.is_file():
            findings.append({'citation': label, 'issue': 'alias evidence missing or outside KB'})
    for stem in args.entry:
        if stem not in entries or entries[stem].type == 'source':
            findings.append({'entry': stem, 'issue': 'unknown or non-citing entry'})
    checked = 0
    for stem, entry in entries.items():
        if entry.type == 'source' or (args.entry and stem not in args.entry):
            continue
        if args.drafts and (args.drafts / (stem + '.md')).is_file():
            entry = _parse_file(args.drafts / (stem + '.md'), entry.type)
        if entry.source_entries:
            checked += len(entry.sources)
            findings.extend(check_explicit_sources(entry, sources))
            continue
        for citation in entry.sources:
            checked += 1
            target = resolve(citation, sources, aliases)
            if not target:
                findings.append({'entry': stem, 'citation': citation,
                                 'issue': 'unresolved or ambiguous active citation'})
            elif target not in entry.wikilinks:
                findings.append({'entry': stem, 'citation': citation, 'source': target,
                                 'issue': 'identity resolved but canonical link missing'})
    print(json.dumps({'active_citations_checked': checked, 'findings': findings},
                     ensure_ascii=True, indent=2))
    return bool(findings)


if __name__ == '__main__':
    raise SystemExit(main())
