"""Save supplementary distillation/critique decisions without changing integrated sources."""
from pathlib import Path
import hashlib
import json
import os

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
assert not (OUT/'integration/completed.json').exists(), 'Batch integrated; do not overwrite historical review decisions.'
manifest=json.loads((OUT/'manifest.json').read_text(encoding='utf-8'))
coverage=json.loads((OUT/'source-coverage.json').read_text(encoding='utf-8'))
validation=json.loads((OUT/'validation.json').read_text(encoding='utf-8'))
assert not validation['selected_draft_findings'] and not validation['additional_failures']

def link(path,base=OUT):
    rel=Path(os.path.relpath(ROOT/path,base)).as_posix()
    return f'[{Path(path).stem}](<{rel}>)'

critiques={
 'E01':'Retained feedback and repeated correction; rejected a universal practice dose and the claim that ordinary work cannot teach. The replication caveat limits the expertise story, not all benefits of practice.',
 'E02':'Distinguished self-assessment from appropriate reliance. The tested tutorial used manually prepared explanations; the proposal does not delegate correctness judgments to an AI critic.',
 'E03':'The three-condition comparison is editorial. Kept task comparability, infeasible baselines and non-performance constraints explicit. Unreviewed sycophancy/abstention extensions were not imported.',
 'E04':'Kept self-reported effort distinct from measured productivity or learning. Post-task review is an optional variant, with handoff costs included and no inference that more effort is better.',
 'E05':'The recipient check is proposed, not evaluated in the surveys. Removed causal interpretations of trust and competence associations; original practitioner origin stays intact.',
 'E06':'Distinguished immediate unaided quiz outcomes from long-term skill change; main-study timing from the pilot; exploratory patterns from randomized interventions. Fan is explicitly abstract-level verification, and is used only for the abstract-reported mixed result.',
 'E07':'The paper is a philosophical design argument, not a deployment trial. Kept competence and values separate; formal approval or a named owner alone is insufficient.',
 'E08':'Preserved improved individual story ratings alongside increased similarity. Did not infer that parallel teams prevent homogenization or improve retained creativity. Mascareño remains unreviewed for its stronger cross-stage interpretation.',
 'N10':'Merged into missing-perspective checks as an explicitly editorial research-method variant. Diverse human collaborators are not interchangeable with simulated personas or more model outputs.',
 'N09-method':'Replaced exact problematic sections rather than appending a caveat below contrary claims. Removed the universal less-detail rule, the causal better-decisions claim and the claim that the method prevents the phenomenon.'
}

rows=[]
lines=['# Supplementary practice review — decisions and critique','',
       'Date: 2026-09-27. Scope: the ten candidate families and eight enrichment routes from the screening. This supplements existing source ingestions; it does not restart or demote their integrated status.','',
       '**Completed:** source checks, distillation, three-lens self-critique, duplicate comparison and mechanical validation of this batch. **Not performed:** Stage 5 integration. The following are curator recommendations, not a claim of user approval.','',
       'Original reading depth is recorded in [source-coverage.json](source-coverage.json): 19 sources; one full chapter, one abstract-level check, and targeted sections of the others. The wider screening source lists are not all newly reread. Unused supporting leads remain available in the screening register.','',
       '## Per-artifact critique','']
for r in manifest:
    key=r['ids'][0]
    concern=r.get('critique') or critiques[key]
    rows.append(dict(families=r['ids'],artifact=r['path'],outcome='NEW_DRAFT' if r['kind']=='new_practice' else 'UPDATE_DRAFT',recommendation='READY_FOR_INTEGRATION_REVIEW',evidence_verdict='APPROVE_AS_BOUNDED_DRAFT',practitioner_verdict='APPROVE',adversarial_verdict='APPROVE_WITH_STATED_LIMITS',reason=r['distinction'],resolved_concerns=concern,sha256=r['sha256']))
    lines += [f"### {', '.join(r['ids'])}: {Path(r['path']).stem}",'',link(r['path']),'',
              '**Decision:** '+('New practice draft.' if r['kind']=='new_practice' else 'Focused update proposal.')+' Ready for integration review; no canonical mutation.', '',
              '**Evidence lens:** '+concern,'',
              '**Practitioner lens:** '+r['distinction'],'',
              '**Adversarial lens:** '+('The steps are usable but their intended human benefits are not established by a fluent AI response or a successful immediate artifact. Source roles and adaptations remain explicit.' if r['kind']=='new_practice' else 'Adding a research citation must not turn the original practitioner routine into a supposedly tested intervention. Preserve its origin and the added source’s narrower role.'),'',
              '**Mechanical gate:** No findings in this selected artifact; source links and retained-original links resolve.','']
lines+=['## Workbench-level validation note','',
        'The repository validator flags `niederhoffer-workslop-2026` because it scans the first page, which belongs to the 2025 article. This workbench contains two articles. The later text explicitly says “Published on HBR.org / January 16, 2026 / Reprint H090VT”; source.json records the two-article setup. This is a manually checked first-page limitation, not a reason to rename the source. The raw validator finding remains in validation.json. No new draft finding is suppressed.','',
        '## Deferred items','',
        'The four screening hold groups remain held. Additional evidence sources named under enrichment routes have not all been reread; no new claim was drawn from an unreviewed original. The Bastani supplementary prompts were not recovered or inspected: N03 is a bounded package adaptation, not an implementation replication. The Mascareño cross-stage claim and the older delegation-source hold remain unresolved.','',
        '## Integration conditions','',
        'Record the Stage 5 decision for the selected drafts. Preserve practitioner origins in all nine practice updates. Apply the modulation correction together with N09. Rebase draft-relative original links at the canonical destination, retain audit copies, then run source-link, practice-guide, index and count updates. Keep the current outcome taxonomy.','']
(OUT/'critique-and-decisions.md').write_text('\n'.join(lines),encoding='utf-8')
(OUT/'decisions.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

for s in coverage:
    source=s['source']
    folder=ROOT/'raw'/source
    related=[r for r in manifest if source==r['source'] or f'[[{source}]]' in (ROOT/r['path']).read_text(encoding='utf-8')]
    body=['# Supplementary practice review — 2026-09-27','',
          'This review adds practice drafts or evidence-update proposals to an already integrated source. Original text, original binaries, historical distillation and integration decisions are retained.','',
          '## Reading coverage','',
          f"Original: [source.md](source.md). SHA-256: `{s['sha256']}`.",'',
          'Read: '+s['depth']+'; '+', '.join(f'L{a}–{b}' for a,b in s['line_ranges'])+'.','',
          '## Distillation and critique','']
    for r in related:
        body += [f"- {', '.join(r['ids'])}: {link(r['path'],folder)} — {r['distinction']}"]
    rel=Path(os.path.relpath(OUT/'critique-and-decisions.md',folder)).as_posix()
    body += ['',f'[Batch critique and decisions](<{rel}>).','','## Decision','',
             '- Outcome: READY_FOR_INTEGRATION_REVIEW (curator recommendation).',
             '- Scope: listed supplementary drafts only; Stage 5 not performed.',
             '- Historical source status remains unchanged; this supplementary review has its own ledger.','']
    dest=folder/'practice-review-2026-09-27.md'
    assert not dest.exists(),dest
    dest.write_text('\n'.join(body),encoding='utf-8')
    log=folder/'log.md'
    with log.open('a',encoding='utf-8') as f:
        f.write('\n\n## 2026-09-27 — Supplementary practice review\n\nTargeted source review, draft/overlap decision and self-critique recorded in [practice-review-2026-09-27.md](practice-review-2026-09-27.md). Drafts ready for integration review; no canonical edit or change to historical source status.\n')

summary=['# Source review completed','',
         '2026-09-27. All ten candidate families and eight enrichment routes received a disposition.','',
         '- **8 new practice drafts.** N08 merged into N07; N10 became a variant of an existing practice.',
         '- **9 practice-update proposals.** Eight enrichment routes plus N10.',
         '- **1 method correction.** Removes unsupported causal and universal claims from modulation-practice; keeps the method in place.',
         '- **19 original sources checked.** Mostly targeted sections, not full-paper rereads. Fan: abstract-level check only; Bjork: full chapter.',
         '- **418 canonical entries unchanged.** No new practices integrated; existing count remains 75.','',
         '## New practice drafts','',
         '| Family | Draft | Evidence boundary |','|---|---|---|']
for r in manifest:
    if r['kind']=='new_practice':
        summary.append(f"| {', '.join(r['ids'])} | {link(r['path'])} | Research-based routine or explicit adaptation; intended benefits remain separate from measured outcomes. |")
summary+=['','## Update proposals','','| Route | Target | Proposal |','|---|---|---|']
for r in manifest:
    if r['kind']=='update_proposal': summary.append(f"| {', '.join(r['ids'])} | {link(r['destination'])} | {link(r['path'])} |")
summary+=['','## What changed after reading originals','',
         '- Retrieval over time and choosing among mixed problem types remain distinct routines.',
         '- Tutor instructions alone are not the studied Bastani package; educator-prepared solutions and mistake feedback matter to its description.',
         '- Callari used open-ended survey responses, not in-depth interviews. The support conversation is folded into the work-design review, without employee labels.',
         '- Leonardi and Leavell recommend balancing engagement with uncertainty. The original does not support a universal instruction to reduce detail or a causal promise of better decisions.',
         '- He’s tutorial improved self-assessment but did not improve reliance uniformly. The update does not tell everyone to trust themselves less.',
         '- Shen’s interaction patterns are exploratory; retaining one thinking step is not a tested remedy. Fan provides a different outcome pattern and is not used as evidence of universal learning harm.','',
         '## Review and next decision','',
         'Read [critique-and-decisions.md](critique-and-decisions.md) for per-draft reasoning, [source-coverage.json](source-coverage.json) for exact original-text coverage and [validation.json](validation.json) for checks. Draft hashes and destinations are in [manifest.json](manifest.json).','',
         'The next stage is integration of the reviewed drafts and focused updates. Source roles, locators and adaptation labels must survive that step. N09 should travel with its parent-method correction. The four earlier hold groups remain visible and unchanged; they are not silently rejected or integrated.','']
(OUT/'README.md').write_text('\n'.join(summary),encoding='utf-8')
print(json.dumps({'drafts':len(manifest),'source_audit_notes':len(coverage),'stage':'review_complete_no_integration'},indent=2))
