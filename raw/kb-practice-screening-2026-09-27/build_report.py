"""Render editorial screening decisions and verify local references/input hashes.

No selection is made by this script. Unassigned entries remain background leads,
not rejected sources. No canonical file is written.
"""
import hashlib
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def read(name):
    return json.loads((HERE / name).read_text(encoding='utf-8-sig'))


def dump(name, data):
    (HERE / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def main():
    inventory = read('inventory.json')['entries']
    existing = read('existing-practices.json')
    families = read('editorial-decisions.json')['families']
    by_stem = {e['stem']: e for e in inventory}
    practices = {e['stem']: e for e in existing}
    assert len(by_stem) == 343 and len(practices) == 75
    assert set(by_stem).isdisjoint(practices)
    for e in inventory:
        assert hashlib.sha256((ROOT / e['path']).read_bytes()).hexdigest() == e['sha256'], e['path']
    # Confirm the previously integrated source copies are still the same copies.
    completed = json.loads((ROOT / 'raw/practitioner-practices-development/integration/completed.json').read_text(encoding='utf-8-sig'))
    for e in completed['entries']:
        if e['type'] == 'source':
            assert hashlib.sha256((ROOT / e['destination']).read_bytes()).hexdigest() == e['canonical_sha256'], e['destination']
    for f in families:
        assert all(s in by_stem for s in f['entries']), f['id']
        assert all(s in practices for s in f['overlap']), f['id']

    # Full canonical notes explicitly inspected in addition to the bounded screen.
    full_reads = set('''acts-of-kindness-practice ai-meaningful-work-design ai-vision-taxonomy
ai-work-practice-ideal-types autonomy-preserving-ai-design bjork-desirable-difficulties-2011
bastani-guardrails-math-rct-2025 he-illusion-competence-2023 gentner-markman-analogy-1997
modulation-practice reference-verification bainbridge-ironies-automation-1983
ericsson-deliberate-practice-1993 marcoccia-willingness-dont-know-2026
liu-agentic-ai-organizational-behavior-2026 leonardi-artificial-certainty-2026 calibration
effort-investment-review workslop-prevention messeri-crockett-illusions-understanding-2024
rajaram-tsim-flipped-classroom-2026'''.split())
    register = []
    for e in inventory:
        linked = [f for f in families if e['stem'] in f['entries']]
        if e['previous_practice_review']:
            disposition = 'previous_review_carried_forward'
            depth = 'Prior practitioner close review; identity/provenance carried forward, not reread in this screen.'
            reason = 'Already fed the completed practitioner extraction; no automatic second extraction.'
        elif linked:
            disposition = '+'.join(sorted({f['route'] for f in linked}))
            depth = 'Canonical note read in full' if e['stem'] in full_reads else 'Bounded canonical summary/section/passages screen; selected follow-up passages where useful'
            reason = '; '.join(f['id'] + ': ' + f['title'] for f in linked)
        else:
            disposition = 'background_no_distinct_lead_identified'
            depth = 'Bounded canonical summary/section/passages screen'
            reason = 'No distinct procedure selected from the inspected material. Retain as context or a future lead; this is not a full-text rejection or a judgment of source quality.'
        register.append({k: e[k] for k in ('stem', 'title', 'type', 'path', 'sha256')} | dict(disposition=disposition, reading_depth=depth, reason=reason, family_ids=[f['id'] for f in linked], original_source_review_this_pass=False))
    counts = dict(Counter(e['disposition'] for e in register))
    dump('screening-register.json', {'scope': 'Canonical sources, concepts and methods; practices used only for overlap comparison.', 'counts': counts, 'entries': register})

    def link(stem):
        e = by_stem.get(stem) or practices[stem]
        return f"[{stem}](<../../{e['path']}>)"

    lines = ['# Candidate practices from the existing KB', '',
             'Screening date: 2026-09-27. **Ten candidate families, not ten approved practices.** All require checking the original source before extraction. A source, a method and a concept based on that source are one evidence trail, not independent confirmations.', '',
             'The procedure kernels below are paraphrases or explicitly marked editorial adaptations. No new practice cards or taxonomy changes are approved by this document.', '']
    for f in families:
        lines += [f"## {f['id']}. {f['title']}", '', f"**Route:** {f['route']}.", '', '**KB trail:** ' + '; '.join(link(s) for s in f['entries']) + '.', '']
        if f['route'] == 'candidate':
            for key, label in [('locator', 'Where to look'), ('kernel', 'Procedure lead'), ('basis', 'Evidence basis'), ('difference', 'Potentially distinct contribution'), ('boundary', 'Limits'), ('next', 'Before extraction')]:
                lines += [f'**{label}:** {f[key]}', '']
        else:
            lines += [f"**Action / reason:** {f['action']}", '']
        if f['overlap']:
            lines += ['**Existing practices to compare:** ' + '; '.join(link(s) for s in f['overlap']) + '.', '']
    (HERE / 'candidates.md').write_text('\n'.join(lines), encoding='utf-8')

    lines = ['# Screening register', '',
             'Every canonical non-practice entry is accounted for. Reading depth is explicit in [the machine-readable register](screening-register.json). No original paper or book was reread in this screening pass. Keyword pointers helped locate passages; they did not select candidates.', '',
             '| Entry | Type | Disposition | Candidate / route |', '|---|---|---|---|']
    for e in register:
        ids = ', '.join(e['family_ids']) or '—'
        lines.append(f"| {link(e['stem'])} | {e['type']} | {e['disposition']} | {ids} |")
    (HERE / 'screening-register.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

    route_counts = dict(Counter(f['route'] for f in families))
    summary = dict(non_practice_entries=len(inventory), type_counts=dict(Counter(e['type'] for e in inventory)), newly_screened=sum(not e['previous_practice_review'] for e in inventory), previously_reviewed=sum(e['previous_practice_review'] for e in inventory), existing_practices_comparison_only=len(existing), family_counts=route_counts, disposition_counts=counts, canonical_input_hashes_unchanged=True, previous_integrated_source_hashes_unchanged=True, all_family_and_overlap_links_resolve=True, original_source_review_this_pass=False, new_practice_cards=0)
    dump('verification.json', summary)
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
