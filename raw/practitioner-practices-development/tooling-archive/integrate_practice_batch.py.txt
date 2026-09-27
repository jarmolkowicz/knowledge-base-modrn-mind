"""Stage 5 for the explicitly approved September 2026 practice package.

Default prepares final review copies and validates; --apply installs those exact
copies after the recorded decision. Original extraction drafts are retained.
"""
from __future__ import annotations
import argparse
from collections import Counter
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote
import yaml

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'raw/practitioner-practices-development/extraction'
RUN = ROOT / 'raw/practitioner-practices-development/integration'
sys.path.insert(0, str(Path(__file__).parent))
import kb_search
import linter
import validate_drafts

spec = importlib.util.spec_from_file_location('source_sync', Path(__file__).with_name('sync-source-links.py'))
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read(path):
    return path.read_text(encoding='utf-8-sig')

def write_json(path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def split(text):
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.S)
    assert m, 'Missing frontmatter'
    return yaml.safe_load(m[1]), text[m.end():]

def join(meta, body):
    return '---\n' + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=130) + '---\n\n' + body.strip() + '\n'

def section(body, header, replacement=None):
    pattern = r'^## ' + re.escape(header) + r'\s*\n.*?(?=^## |\Z)'
    return re.sub(pattern, '' if replacement is None else f'## {header}\n\n{replacement}\n\n', body, flags=re.M | re.S)

def rebase(text, origin, destination):
    def sub(m):
        target = m[2].strip('<>')
        if re.match(r'^[a-zA-Z]+:', target) or target.startswith('#'):
            return m[0]
        file, sep, anchor = target.partition('#')
        resolved = (origin.parent / unquote(file)).resolve()
        assert resolved.is_relative_to(ROOT.resolve()) and resolved.exists(), (origin, target)
        relative = os.path.relpath(resolved, destination.parent).replace('\\', '/')
        return f'[{m[1]}](<{relative}{sep}{anchor}>)'
    return re.sub(r'(?<!!)\[([^\]\n]+)\]\(([^)]+)\)', sub, text)

def clean_labels(body):
    for name in ('Draft Status', 'Consolidation Status', 'Draft Disposition', 'Practice drafts', 'Practice Review'):
        body = section(body, name)
    body = body.replace('Draft only. Integration pending. ', '')
    body = re.sub(r'^.*(?:Draft only[.;]|Draft-only\.|Critiqued draft only\.|Integration pending;).*(?:\n|$)', '', body, flags=re.M)
    body = body.replace('Practitioner article; draft only.', 'Practitioner article.')
    body = body.replace('Practitioner interview; draft only.', 'Practitioner interview.')
    body = body.replace(' Integration pending.', '')
    body = body.replace('This draft endorses no', 'This entry endorses no')
    return re.sub(r'\n{3,}', '\n\n', body)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    RUN.mkdir(exist_ok=True)
    if (RUN / 'completed.json').exists():
        raise SystemExit('Already integrated; use the recorded result rather than rerunning this batch.')
    plan = json.loads(read(BASE / 'integration-plan.json'))
    close = json.loads(read(BASE / 'close-review-results.json'))
    review = {s['source']['id']: s for s in close['sources']}
    cards = [c for c in plan['cards'] if c['status'] == 'awaiting_editorial_decision']
    ids = {sid for c in cards for sid in c['source_ids']}
    deps = [s for s in plan['source_dependencies'] if s['id'] in ids]
    assert len(cards) == 75 and len(deps) == 115 and 80 not in ids
    existing = kb_search.load_entries(refresh=True)
    baseline = {e.path: sha(Path(e.path)) for e in existing.values()}
    baseline_path = RUN / 'baseline.json'
    if baseline_path.exists():
        assert json.loads(read(baseline_path)) == baseline, 'Existing KB changed since preparation; inspect before continuing.'
    else:
        write_json(baseline_path, baseline)
    decision = dict(date='2026-09-27', outcome='PROCEED_TO_INTEGRATE', user_instruction='Move on',
                    context='User continued after presentation of 75 candidates awaiting approval and two source-correction holds.',
                    scope='75 unblocked practices and their 114 new source notes; reuse existing Nosta book entry. Adopt intended-outcome navigation as a provisional taxonomy. Preserve both held cards and all review history.',
                    practices=[c['slug'] for c in cards], source_ids=sorted(ids),
                    excluded=[c['slug'] for c in plan['cards'] if c['status'] != 'awaiting_editorial_decision'])
    write_json(RUN / 'decision.json', decision)
    # Stage 4.5 against the actual approved workbenches, not the deferred pool.
    prior_findings = []
    for source in deps:
        prior_findings.extend(asdict(f) for f in validate_drafts.validate(ROOT / source['workbench']))
    assert not prior_findings, prior_findings
    staged = []
    sources_available = {s for s,e in existing.items() if e.type == 'source'} | {s['source_entry'] for s in deps}
    no_research = {741:'doshi-hauser-creativity-diversity-2024',425:'doshi-hauser-creativity-diversity-2024',
                   79:'anderson-homogenization-2024',804:'anderson-homogenization-2024',542:'anderson-homogenization-2024',
                   811:'anderson-homogenization-2024',550:'anderson-homogenization-2024'}
    def stage(meta, body, origin, destination, kind, source_id=None):
        for key in ('draft_only', 'integration_decision'):
            meta.pop(key, None)
        target = ROOT / destination
        assert not target.exists() and target.stem not in existing, destination
        body = rebase(body, origin, target)
        folder = origin.parents[1] / 'integration' if kind == 'practice' else origin.parent / 'integration'
        folder.mkdir(exist_ok=True)
        path = folder / target.name
        path.write_text(join(meta, body), encoding='utf-8')
        staged.append(dict(draft=path.relative_to(ROOT).as_posix(), destination=destination,
                           sha256=sha(path), type=kind, source_id=source_id))
    for s in deps:
        if s['action'] == 'reuse_existing':
            assert sha(ROOT / s['proposed_destination']) == s['existing_sha256']
            continue
        assert s['action'] == 'new_source'
        origin = ROOT / s['source_draft']
        assert sha(origin) == s['draft_sha256'], f'Source draft changed: {origin}'
        meta, body = split(read(origin))
        r = review[s['id']]['review']
        for i,citation in enumerate(meta.get('sources', [])):
            if not linter.HAS_AUTHOR_YEAR_RE.search(citation):
                author, rest = citation.split('. ', 1)
                date = re.search(r'\b((?:19|20)\d{2})-\d{2}-\d{2}\b', rest)
                assert date, citation
                normalized = author + '. (' + date[1] + '). ' + rest
                meta['sources'][i] = normalized
                body = body.replace(citation, normalized)
        old = re.search(r'## Key Insight\s+(.+?)(?=\n## |\Z)', body, re.S)[1].strip()
        # A public source note describes the source, not the editor's merge instruction.
        statements = r['reported_outcomes'] or r['proposed_outcomes']
        assert statements, s['id']
        insight = ('The source proposes: ' + r['proposed_outcomes'][0] + ' ') if r['proposed_outcomes'] else ''
        if r['reported_outcomes']:
            insight += 'The reviewed account reports: ' + r['reported_outcomes'][0]
        body = section(body, 'Key Insight', insight)
        body = body.replace('- ' + old + '\n', '')
        if re.search(r'## Contradicts / Extends\s+' + re.escape(old), body):
            body = section(body, 'Contradicts / Extends')
        body = clean_labels(body)
        if s['id'] in no_research:
            stem = no_research[s['id']]
            body = re.sub(r'^- \[\[' + re.escape(stem) + r'\]\].*\n', '', body, flags=re.M)
            body = re.sub(r'^(?:Doshi and Hauser|Anderson and colleagues)[^\n]+\n', '', body, flags=re.M)
        # Keep the exact limited coverage and claim-level role visible after publication.
        linked = [c for c in cards if s['id'] in c['source_ids']]
        body += '\n## Use in this collection\n\n'
        body += {'origin':'Originating account for a proposed routine; this role is not evidence that the routine works.',
                 'support':'Supporting account or variant; repeated advice is not independent validation.',
                 'counterexample':'Counterexample used to identify failure conditions; the source is not endorsed as a recommended procedure.'}[s['role']] + '\n\n'
        body += '\n'.join('- [[' + c['slug'] + ']]' for c in linked) + '\n'
        if r.get('practitioner'):
            body += '\n**Application boundary [Inference]:** ' + r['practitioner'] + '\n'
        body += '\n**Review scope:** ' + r['coverage'] + '\n'
        body += '\nLocal evidence and locators: [source text](../source.md). Source findings above are paraphrases unless explicitly quoted.\n'
        if s['id'] == 879:
            body = body.replace('# Slow AI (book)', '# Slow AI: Knowing When to Use AI and When to Leave It Alone')
        stage(meta, body, origin, s['proposed_destination'], 'source', s['id'])
    for c in cards:
        origin = ROOT / c['draft']
        assert sha(origin) == c['sha256'], f'Practice draft changed: {origin}'
        meta, body = split(read(origin))
        meta['source_entries'] = c['source_entries']
        meta['intended_outcomes'] = [c['primary_outcome']] + c['secondary_outcomes']
        body = clean_labels(body)
        body += '\n## Intended outcomes\n\n[Inference] Primary: ' + c['primary_outcome'] + '. '
        if c['secondary_outcomes']:
            body += 'Secondary: ' + ', '.join(c['secondary_outcomes']) + '. '
        body += 'These are intended benefits, not demonstrated effects.\n'
        body += '\n## Source roles\n\n'
        body += '\n'.join(f'- [[{stem}]] — {review[sid]["review"]["role"]}.' for sid,stem in zip(c['source_ids'], c['source_entries'])) + '\n\n'
        sources_section, missing = sync.build_sources_section(meta['sources'], sources_available, c['source_entries'])
        assert not missing, missing
        body += sources_section + '\n'
        stage(meta, body, origin, c['proposed_destination'], 'practice')
    future = dict(existing)
    for item in staged:
        entry = kb_search._parse_file(ROOT / item['draft'], item['type'])
        future[entry.stem] = entry
    checks = ['broken_wikilinks', 'frontmatter', 'slug_format', 'distillation_quality', 'missing_related', 'uncited_sources', 'orphans']
    findings = [asdict(f) for f in linter.run_checks(checks, future) if f.entry not in existing]
    for item in staged:
        text = read(ROOT / item['draft'])
        dest = ROOT / item['destination']
        for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)]+)\)', text):
            target = target.strip('<>').split('#')[0]
            if not target or re.match(r'^[a-zA-Z]+:', target):
                continue
            if not (dest.parent / unquote(target)).exists():
                findings.append(dict(entry=dest.stem, check='local_link', issue=target))
        if re.search(r'draft.only|integration pending|integration decision pending|critique recorded', text, re.I):
            findings.append(dict(entry=dest.stem, check='draft_label', issue='Unresolved workflow wording'))
    write_json(RUN / 'prepared.json', dict(decision=decision, entries=staged, findings=findings))
    print(json.dumps(dict(prepared=len(staged), practices=len(cards), new_sources=len(staged)-len(cards), findings=findings), ensure_ascii=True, indent=2))
    if findings or not args.apply:
        return bool(findings)
    # Decision, zero-finding checks and exact copy hashes precede canonical writes.
    for s in deps:
        wb = ROOT / s['workbench']
        decision_path = wb / 'practice-review' / 'integration-decision.md' if s['id'] in (879,880) else wb / 'integration-decision.md'
        decision_path.parent.mkdir(exist_ok=True)
        decision_path.write_text('# Integration decision\n\n- Outcome: PROCEED_TO_INTEGRATE\n- Date: 2026-09-27\n- Authority: user “Move on” after review package.\n- Scope: approved practices and the source contribution listed in the batch record; held practices excluded.\n- Validation: Stage 4.5 and prepared-copy checks passed.\n\n[Batch decision](<' + os.path.relpath(RUN/'decision.json', decision_path.parent).replace('\\','/') + '>)\n', encoding='utf-8')
        critique = wb / 'critique.md'
        if s['id'] in (879,880):
            critique = wb / 'practice-review/critique.md'
        assert critique.exists(), critique
        critique.write_text(read(critique).rstrip() + '\n\n## Integration decision — 2026-09-27\n\nOutcome: PROCEED_TO_INTEGRATE. User “Move on” approved the unblocked package. The earlier draft-only decision is historical. Scope and exact files: [current decision](integration-decision.md).\n', encoding='utf-8')
        meta_path = wb / 'source.json'
        meta = json.loads(read(meta_path))
        if s['action'] != 'reuse_existing':
            meta['status'] = 'validated'
        meta.setdefault('decisions', []).append(dict(stage='practice-stage-4.5', outcome='validated', at='2026-09-27',
            authority='User: Move on', findings=0, scope='Approved unblocked batch; exact copies in integration/prepared.json'))
        write_json(meta_path, meta)
    for item in staged:
        draft, target = ROOT / item['draft'], ROOT / item['destination']
        assert sha(draft) == item['sha256'] and not target.exists()
        target.write_bytes(draft.read_bytes())
    now = datetime.now(timezone.utc).isoformat()
    for s in deps:
        wb = ROOT / s['workbench']
        meta_path = wb / 'source.json'
        meta = json.loads(read(meta_path))
        meta['status'] = 'integrated'
        meta.pop('draft_only', None)
        meta['integration_decision'] = 'PROCEED_TO_INTEGRATE'
        meta.setdefault('decisions', []).append(dict(stage='practice-stage-5', outcome='integrated', at=now,
            authority='User: Move on', source_action=s['action'], source=s['proposed_destination'],
            practices=[c['proposed_destination'] for c in cards if s['id'] in c['source_ids']],
            scope='Reviewed practice contribution only; historical source claims not revalidated.'))
        write_json(meta_path, meta)
        review_path = wb / 'practice-review.json'
        source_review = json.loads(read(review_path))
        source_review['integration_decision'] = 'PROCEED_TO_INTEGRATE'
        source_review['integrated_at'] = now
        source_review['integrated_practices'] = [c['proposed_destination'] for c in cards if s['id'] in c['source_ids']]
        source_review['historical_drafts_retained'] = True
        write_json(review_path, source_review)
        log = wb / 'log.md'
        log.write_text(read(log).rstrip() + '\n\n## 2026-09-27 — Approved practice integration\n\nUser “Move on” approved the unblocked batch. Stage 4.5 and final-copy checks passed. '
                       + ('Reused the existing canonical source without changing it.' if s['action']=='reuse_existing' else 'Integrated the scoped source note.')
                       + ' Approved practice copies are in `practices/`; original extraction drafts and evidence remain here. See [batch record](../practitioner-practices-development/integration/decision.json).\n', encoding='utf-8')
    assert all(sha(Path(path)) == old for path,old in baseline.items()), 'Pre-existing canonical content changed'
    result = dict(at=now, entries=staged, practices=len(cards), new_sources=len(staged)-len(cards),
                  reused_sources=1, held_practices=2, previous_canonical_unchanged=len(baseline))
    write_json(RUN / 'completed.json', result)
    print('Integrated approved copies; navigation rebuild and final audit still required.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
