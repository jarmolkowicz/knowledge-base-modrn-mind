"""Prepare an auditable editorial package; never write canonical entries.

Run refine_practice_outcomes.py first. The plan preserves all extraction drafts,
proposes one consolidation, and records exact source dependencies and file hashes.
It is not an integration decision or a source-author endorsement.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'raw/practitioner-practices-development/extraction'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if (BASE.parent / 'integration/completed.json').exists():
        raise SystemExit('This integration is complete. Preserve the reviewed plan and create a separate batch for further work.')
    extracted = json.loads((BASE / 'close-review-results.json').read_text(encoding='utf-8'))
    outcomes = json.loads((BASE / 'outcome-review.json').read_text(encoding='utf-8'))
    cards = {Path(c['path']).stem: c for c in extracted['cards']}
    sources = {s['source']['id']: s for s in extracted['sources']}
    audit_path = BASE / 'editorial-revisions.json'
    revisions = json.loads(audit_path.read_text(encoding='utf-8')) if audit_path.exists() else []

    def revise(path, transform, reason):
        path = ROOT / path
        before = path.read_text(encoding='utf-8-sig')
        after = transform(before)
        if after == before:
            return
        old_hash = digest(path)
        path.write_text(after, encoding='utf-8')
        revisions.append(dict(date='2026-09-27', path=path.relative_to(ROOT).as_posix(),
                              reason=reason, before_sha256=old_hash, after_sha256=digest(path)))

    revise(cards['check-a-capability-without-the-assistant']['path'],
           lambda t: t.replace('John Nosta. The Borrowed Mind (book). . ',
                               'Nosta, J. (2026). The Borrowed Mind: Reclaiming Human Thought in the Age of AI. ThoughtLeaderPress.'),
           'Replace incomplete citation using the existing canonical book source.')
    revise('raw/illingworth-slow-ai-2026/drafts/source.md',
           lambda t: t.replace('Sam Illingworth. Slow AI (book). . ',
                               'Illingworth, S. (2026). Slow AI: Knowing When to Use AI and When to Leave It Alone. First edition.'),
           'Replace placeholder bibliography with title/copyright metadata already recorded in source.json; no publisher inferred.')

    unrelated = {
        'speak-your-thoughts-before-summarizing': 'doshi-hauser-creativity-diversity-2024',
        'use-fictional-questions-for-your-own-reflection': 'doshi-hauser-creativity-diversity-2024',
        'test-and-share-a-team-ai-workflow': 'anderson-homogenization-2024',
        'turn-a-premortem-into-actions': 'anderson-homogenization-2024',
        'check-what-each-person-thinks-was-decided': 'anderson-homogenization-2024',
        'return-to-real-user-accounts': 'anderson-homogenization-2024',
        'collect-independent-views-before-discussion': 'anderson-homogenization-2024',
    }
    for slug, stem in unrelated.items():
        def tighten(t, stem=stem):
            t = re.sub(r'\*\*Related research:\*\*[^\n]+',
                       '**Related research:** No directly relevant evaluation of this routine was identified in this review. The practitioner account above supplies its rationale; the AI adaptation remains untested.', t)
            return re.sub(r'^- \[\[' + re.escape(stem) + r'\]\].*\n', '', t, flags=re.M)
        revise(cards[slug]['path'], tighten,
               f'Remove generic {stem} connection: its creative-ideation/output comparison does not support this routine.')

    target = cards['keep-one-thinking-step']['path']
    variant = cards['choose-the-human-part-of-the-work']['path']
    mollick = 'Ethan Mollick. I, Cyborg: Using Co-Intelligence. 2024-03-14. https://www.oneusefulthing.org/p/i-cyborg-using-co-intelligence'
    def add_variant(t):
        if '### Complementary-task variant' in t:
            return t
        t = t.replace('draft_only: true', f'  - "{mollick}"\ndraft_only: true', 1)
        marker = '\n## Evidence and Rationale'
        addition = ('\n### Complementary-task variant\n\n'
                    'Mollick describes choosing AI contributions while retaining his wording, reading the work and rejecting some criticism. '
                    '[Inference] Name the contribution you want to make yourself, give AI a complementary bounded task, then accept or reject specific suggestions. '
                    'This is another example of the same boundary-setting action, not an independently validated routine.\n\n'
                    'Source: Ethan Mollick, “I, Cyborg: Using Co-Intelligence,” 14 March 2024, '
                    '[local original](../../../mollick-076-i-cyborg-using-co-intelligence-2024/source.md), '
                    'L30 (human graphs/AI statistics), L34–36 (own wording and reading), L40–46 (selective criticism). '
                    'The original [variant draft](../../../mollick-076-i-cyborg-using-co-intelligence-2024/drafts/practices/choose-the-human-part-of-the-work.md) is retained for the audit trail.\n')
        return t.replace(marker, addition + marker, 1)
    revise(target, add_variant, 'Consolidate a matching human-retained-contribution routine, preserving Mollick attribution and the original draft.')
    def mark_variant(t):
        if '## Consolidation Status' in t:
            return t
        return t.rstrip() + ('\n\n## Consolidation Status\n\n2026-09-27: Proposed source variant of '
                '[Keep one thinking step for yourself](../../../illingworth-523-how-to-hold-on-to-what-2025/drafts/practices/keep-one-thinking-step.md). '
                'Keep this extraction draft as an audit record; do not integrate it as a second standalone practice. Integration remains pending.\n')
    revise(variant, mark_variant, 'Mark the proposed merge without deleting the source-specific extraction.')
    audit_path.write_text(json.dumps(revisions, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for workbench in sorted({Path(r['path']).parts[1] for r in revisions}):
        log = ROOT / 'raw' / workbench / 'log.md'
        content = log.read_text(encoding='utf-8-sig') if log.exists() else '# Source log\n'
        marker = '## 2026-09-27 — Practice editorial revision'
        if marker not in content:
            reasons = [r['reason'] for r in revisions if Path(r['path']).parts[1] == workbench]
            content = content.rstrip() + '\n\n' + marker + '\n\n' + '\n'.join('- ' + r for r in reasons)
            content += ('\n\nOriginals and canonical entries unchanged. Integration pending. '
                        'Before/after hashes: [editorial revision record](../practitioner-practices-development/extraction/editorial-revisions.json).\n')
            log.write_text(content, encoding='utf-8')

    # Exact reviewed identities, not fuzzy author/year matching.
    existing = {80: 'mollick-management-ai-superpower-2026', 880: 'nosta-borrowed-mind-2026'}
    planned = []
    needed = set()
    for row in outcomes['mappings']:
        if row['consolidation'] != 'retain':
            continue
        ids = list(row['source_ids'])
        if row['slug'] == 'keep-one-thinking-step':
            ids = sorted(set(ids + cards['choose-the-human-part-of-the-work']['source_ids']))
        needed.update(ids)
        path = ROOT / row['path']
        planned.append(dict(slug=row['slug'], title=row['title'], draft=row['path'],
                            proposed_destination=f'practices/{row["slug"]}.md', sha256=digest(path),
                            source_ids=ids, primary_outcome=row['primary_outcome'], secondary_outcomes=row['secondary_outcomes'],
                            status=row['integration_status'], note=row['integration_note']))
    dependencies = []
    for sid in sorted(needed):
        record = sources[sid]
        source = record['source']
        workbench = source['workbench']
        stem = existing.get(sid, Path(workbench).name)
        source_draft = f'{workbench}/drafts/source.md'
        canonical = ROOT / f'sources/{stem}.md'
        action = 'reuse_existing' if sid in existing else 'new_source'
        if sid == 80:
            action = 'correct_existing_before_reuse'
        item = dict(id=sid, title=source['title'], url=source['url'], source_entry=stem,
                    role=record['review']['role'], action=action,
                    workbench=workbench, proposed_destination=f'sources/{stem}.md',
                    source_draft=source_draft if (ROOT / source_draft).exists() else None,
                    integration_decision='pending')
        if item['source_draft']:
            item['draft_sha256'] = digest(ROOT / source_draft)
        if canonical.exists():
            item['existing_sha256'] = digest(canonical)
        if sid not in existing and canonical.exists():
            raise ValueError(f'Unreviewed source collision: {canonical}')
        assert sid in existing or item['source_draft'], (sid, 'missing source draft')
        dependencies.append(item)
    lookup = {s['id']: s['source_entry'] for s in dependencies}
    for card in planned:
        assert not (ROOT / card['proposed_destination']).exists(), card['slug']
        card['source_entries'] = [lookup[sid] for sid in card['source_ids']]
    plan = dict(date='2026-09-27', status='review_package_only', integration_approved=False,
                original_drafts=78, standalone_candidates=len(planned), retained_variants=1,
                cards=planned, source_dependencies=dependencies,
                excluded_from_this_batch='All sources without a dependency listed here remain archived, not rejected. The 92 screened variants are outside this close-review batch.',
                stage5_requirements=[
                    'Record per-source and per-practice Decision before writing canonical entries.',
                    'Apply the reviewed Mollick source correction before the two held cards are eligible.',
                    'Recheck file hashes against this manifest if any draft changes.',
                    'Write exact source_entries from this manifest; do not guess among same-author/year articles.',
                    'Resolve local Markdown links against the draft location and rebase to each canonical destination.',
                    'Remove draft-only labels from approved copies; retain drafts and revision history.',
                    'Run link validation, source-link sync, index/count generation and bundle checks after integration.'])
    (BASE / 'integration-plan.json').write_text(json.dumps(plan, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    lines = ['# Integration preparation — review package', '',
             '2026-09-27. **77 standalone candidates, one retained source variant. No integration decision recorded.**', '',
             'The [outcome review](outcome-review.md) covers all 78 original drafts. The [manifest](integration-plan.json) records proposed destinations, exact source dependencies and current hashes. It is a plan, not permission to publish.', '',
             '## Consolidation decisions', '',
             'One merge: **Choose the human part of the work** becomes an attributed variant of **Keep one thinking step for yourself**. Both ask the person to retain a substantive contribution and bound the complementary AI work. The original extraction remains beside its source.', '',
             'Other nearby cards remain separate because their triggers, human actions or checks differ:', '',
             '| Neighbors | Reason to retain separately |', '|---|---|',
             '| Initial view, strategy before analysis, argument before slides | Starting a personal view, setting decision criteria and sequencing an audience argument require different work. |',
             '| Consequences, delegation specification, gradual agent authority | Choosing whether to delegate, defining the assignment and expanding authority after observation happen at different points. |',
             '| Writing-process record, intervention record, decision/outcome log | These check contribution history, operational repair and prior reasoning against outcomes respectively. |',
             '| Human advisers, independent group views, arguing the other side | Contextual advice, preventing early convergence and accurately representing disagreement are distinct procedures. |',
             '| Audience rehearsal, answer/example/relevance, accordion rehearsal | These check audience fit, a short answer structure and flexible compression. |',
             '| Growth model, written proposal | Constructing causal relationships and defending a customer/problem/solution account expose different gaps. |', '',
             'Existing `think-first` and `effort-investment-review` methods remain in place. A flexible practitioner starting-point routine and a pre-delegation cost check are specific applications, not automatic replacements for those broader methods.', '',
             '## Revisions applied', '',
             '- Fixed incomplete book citations for *Slow AI* and *The Borrowed Mind*, using local bibliographic records.',
             '- Removed loosely related creativity research from seven cards. Their practitioner basis and untested adaptations remain explicit.',
             '- Added the attributed Mollick variant to the retained thinking-step card; marked the original draft as a proposed variant.',
             '- All changes have before/after hashes in [editorial-revisions.json](editorial-revisions.json). Original source text was not edited.', '',
             '## Holds and decisions still needed', '',
             '- Two cards await the existing Mollick management source correction: **Define the delegation before the agent starts** and **Count the cost of review before delegating**. See the [focused source correction proposal](../../mollick-080-management-as-ai-superpower-2026/drafts/source.md).',
             '- The other 75 standalone cards await an editorial integration decision; this does not mean their benefits are proven.',
             '- Source #52 remains deferred for uncertain publication year and adds no card to this batch.',
             f'- The 77 cards refer to **{len(dependencies)} source records**. Dependencies include origins, supporting accounts and counterexamples; their roles are retained in the manifest. Sources not needed by a card are not automatically integrated.', '',
             '## Stage 5 checklist', '']
    lines += [f'{i}. {x}' for i, x in enumerate(plan['stage5_requirements'], 1)]
    lines += ['', '## Every standalone candidate', '', '| Practice | Status | Source IDs |', '|---|---|---|']
    for card in planned:
        url = '../../' + Path(card['draft']).relative_to('raw').as_posix()
        lines.append(f'| [{card["title"]}](<{url}>) | {card["status"].replace("_", " ")} | '+', '.join(map(str, card['source_ids']))+' |')
    (BASE / 'integration-plan.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps(dict(standalone=len(planned), dependencies=len(dependencies), revisions=len(revisions), integrated=0)))


if __name__ == '__main__':
    main()
