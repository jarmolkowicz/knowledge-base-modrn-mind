"""Read-only structural checks shared by practice drafts, lint and navigation.

These check completeness and source identity, never efficacy or claim support.
Drafts may leave source identities/outcomes empty until editorial review.
"""
import json
from pathlib import Path
import re

import yaml

from lint_checks import Finding

REQUIRED_SECTIONS = (
    'Use When', 'Try It', 'Origin', 'Evidence and Rationale',
    'Limits', 'What to Notice', 'Related',
)


def outcome_ids():
    path = Path(__file__).resolve().parents[1] / 'practice-outcomes.json'
    return {c['id'] for c in json.loads(path.read_text(encoding='utf-8'))['categories']}


def check_practice(text, label, *, source_stems=None, draft=False, outcomes=None):
    findings = []

    def flag(issue):
        findings.append(Finding('practice_schema', label, issue))

    match = re.match(r'\A---\s*\n(.*?)\n---(?:\n|$)', text, re.S)
    try:
        meta = yaml.safe_load(match[1]) if match else None
    except yaml.YAMLError:
        meta = None
    if not isinstance(meta, dict):
        flag('missing or invalid practice frontmatter mapping')
        return findings
    body = text[match.end():]
    if not re.search(r'^# \S', body, re.M):
        flag('missing practice title')
    for name in REQUIRED_SECTIONS:
        section = re.search(r'^## ' + re.escape(name) + r'[ \t]*\n(.*?)(?=^## |\Z)', body, re.M | re.S)
        if not section or not section[1].strip():
            flag(f'missing or empty section: {name}')
    valid_outcomes = outcome_ids() if outcomes is None else outcomes
    for field in ('source_entries', 'intended_outcomes'):
        values = meta.get(field, [])
        if not isinstance(values, list) or any(not isinstance(v, str) or not v.strip() for v in values):
            flag(f'{field} must be a list of nonempty strings')
            continue
        if not values and not draft:
            flag(f'{field} is required for an integrated practice')
        if len(values) != len(set(values)):
            flag(f'{field} contains duplicates')
        if field == 'intended_outcomes':
            if len(values) > 3:
                flag('intended_outcomes allows one primary and at most two secondary outcomes')
            for value in values:
                if value not in valid_outcomes:
                    flag(f'unknown intended outcome: {value}')
        elif source_stems is not None:
            for value in values:
                if value not in source_stems:
                    flag(f'source_entries target is not a source: {value}')
    return findings
