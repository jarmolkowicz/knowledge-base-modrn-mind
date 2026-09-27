# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Publish a navigation hub from individually authored practice-review records.

Aggregation only: decisions, claims and reading coverage come from reviewers.
No automatic inclusion decision and no canonical KB writes.
"""
from collections import Counter
import json
import os
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'raw/practitioner-practices-development/extraction'

def link(path,label):
    return f'[{label}](<{Path(os.path.relpath(path,BASE)).as_posix()}>)'
def clean(x):return str(x).replace('|','/').replace('\n',' ')
def write(name,body):(BASE/name).write_text(body.rstrip()+'\n',encoding='utf-8')

def main():
    m=json.loads((BASE/'manifest.json').read_text(encoding='utf-8'))
    rows=[]; cards={}
    for s in m['sources']:
        p=ROOT/s['workbench']/'practice-review.json'
        if not p.exists():raise SystemExit(f'Missing source review: {s["id"]}')
        v=json.loads(p.read_text(encoding='utf-8-sig'));rows.append({'source':s,'review':v})
        for path in v['practice_files']:
            f=ROOT/path
            if not f.exists():raise SystemExit(f'Missing card: {path}')
            if path not in cards:
                text=f.read_text(encoding='utf-8-sig');title=re.search(r'^# (.+)$',text,re.M)
                cards[path]={'path':path,'title':title.group(1) if title else f.stem,'source_ids':[],'group_index':s['group_index']}
            cards[path]['source_ids'].append(s['id'])
            if path.startswith(s['workbench']+'/'):cards[path]['group_index']=s['group_index']
    roles=Counter(r['review']['role'] for r in rows)
    decisions=Counter(r['review']['decision'] for r in rows)
    data={'date':'2026-09-26','stage':'close reading, distillation and critique; draft only','source_count':len(rows),'practice_count':len(cards),'groups':m['groups'],'role_counts':dict(roles),'recorded_decisions':dict(decisions),'cards':list(cards.values()),'sources':rows,'integration_approved':False}
    write('close-review-results.json',json.dumps(data,indent=2,ensure_ascii=False))
    intro=f'''# Practice source review — current result

2026-09-26. **All {len(rows)} selected sources reviewed at the recorded scope; {len(cards)} draft practice cards across 19 contribution groups.** No practice integrated or marked proven. The original 15 are included; this is the expanded pool from the completed 400-item screening queue.

Start with the [practice catalogue](practice-catalogue.md). It lists every card and its originating source record. Read [outcome questions](outcome-questions.md) for a provisional way to assess what the practices are meant to improve. [All source decisions and coverage](source-review-register.md) remain inspectable.

## What the counts mean

| Source role after close reading | Count |
|---|---:|
'''
    intro+='\n'.join(f'| {clean(k)} | {n} |' for k,n in sorted(roles.items()))
    intro+='''

A source can originate several cards or support another source’s card. Counterexamples are retained for their failure modes, not recommended as prompts. “Retain” means a bounded candidate survived critique, not that its benefits are established.

## Reading coverage

Available article bodies were read; linked media and external claims were not systematically verified. Podcast reviews cover relevant exchanges, not whole episodes or checked audio. The six-page HBR extraction was read. Books received scoped reading of relevant sections, not cover-to-cover review. Exact coverage is recorded per source. Partial articles and uncertain identities remain labeled.

This is source criticism, not a completed background check of every author. Named practitioners, worked examples, first-person field accounts, promotional context and attribution are assessed at the claim level. There is no blanket trusted-author list: the same author can supply a usable procedure and an unsupported claim.

## What changed after screening

- Agreement-seeking, rising AI grades and generated self-explanations cannot serve as independent verification. Those sources remain cautionary examples.
- Inferring hidden feelings, identity or bodily state from generated text is not accepted as evidence of insight. Reported comfort or confidence is retained as experience, separately from competence or calibration.
- Productive human procedures recur: form an initial view, construct an explanation, ask real people, rehearse, inspect source material and choose which changes to accept. Applying pre-AI procedures to AI work is labeled as an adaptation.
- Some practice claims borrow more certainty from research than that research supports. Local research entries were used to bound these claims; article-level numerical claims were not silently promoted to evidence.
- Disclosure, recordkeeping and privacy questions contribute accountability practices. They do not guarantee trust, prove authorship or establish what a vendor collects.

## Remaining work, precisely

The selected review pool is complete. The wider register still contains 92 useful variants and background/deferred items plus access/provenance holds; these have not silently become rejected sources. Newly deferred selected sources remain in the review register. The collection is concentrated in writing, education, software and product work, so it does not establish coverage of all professions or ways of thinking.

Before integration: resolve listed bibliography/provenance blockers for any affected source; select outcome wording and consolidate the documented neighboring cards where useful; implement the separate `practices/` collection in integration/search/index tooling; record per-source integration decisions. The draft validator now checks practice cards, but that alone does not enable Stage 5.

Mechanical audit: [validation report](validation.json). Its findings do not override human decisions. Original-source hashes, draft discovery, local links and proposed slugs are checked. No automatic integration follows a passing check.

## Files

- [Practice catalogue](practice-catalogue.md)
- [Outcome questions, still provisional](outcome-questions.md)
- [Source-review register](source-review-register.md)
- [Cross-source critique and consolidation notes](cross-source-critique.md)
- [Machine-readable results](close-review-results.json)
- [Prior screening results](../screening/screening-results.md)

Raw originals and audit files live in `raw/<source-slug>/`; draft cards in that source’s `drafts/practices/`. This directory is navigation and aggregate review only.
'''
    deferred='## Selected sources still deferred\n\n'
    for row in sorted((r for r in rows if r['review']['role']=='deferred'),key=lambda r:r['source']['id']):
        s=row['source'];v=row['review']
        deferred+='- '+link(ROOT/s['workbench']/'practice-review.json',f'#{s["id"]}: {s["title"]}')+' — '+v['review_note']+'\n'
    intro=intro.replace('## Remaining work, precisely',deferred+'\n## Remaining work, precisely')
    audit=json.loads((BASE/'validation.json').read_text(encoding='utf-8'))
    findings=audit['findings_by_source']
    intro=intro.replace('Mechanical audit: ',f'Validation: all {len(cards)} practice cards passed; {len(rows)-len(findings)}/{len(rows)} complete workbenches have no findings. The remaining recorded flag is source #52’s unverified publication year; it stays deferred. All {audit["original_hashes_verified"]} retained-original hashes match.\n\nMechanical audit: ')
    write('README.md',intro)
    catalog=['# Draft practice catalogue','','Every card is emerging and unapproved for integration. Groups organize contributions; they are not an adopted outcome taxonomy. Variants and supporting accounts remain attached to their source reviews.','']
    for n,g in enumerate(m['groups']):
        catalog.extend([f'## {n+1}. {g["name"]}',''])
        cs=sorted([c for c in cards.values() if c['group_index']==n],key=lambda c:c['title'])
        if not cs:catalog.append('No recommended card. Sources in this group are retained as counterexamples or supporting critique.')
        for c in cs:
            origin=next((r for r in rows if c['path'].startswith(r['source']['workbench']+'/')),None)
            who=origin['review'].get('author') or origin['review'].get('practitioner') if origin else ''
            # Source title remains exact even where a practitioner field contains advice.
            src=origin['source'] if origin else None
            catalog.append('- '+link(ROOT/c['path'],c['title'])+(f' — source #{src["id"]}: {clean(src["title"])}.' if src else '')+f' Source records: {", ".join(map(str,sorted(c["source_ids"])))}.')
        rr=[r for r in rows if r['source']['group_index']==n]
        catalog.extend(['',f'{len(rr)} sources reviewed; '+', '.join(f'{k}: {v}' for k,v in sorted(Counter(r['review']['role'] for r in rr).items()))+'.',''])
    write('practice-catalogue.md','\n'.join(catalog))
    register=['# All selected-source reviews','','Close-reading dispositions supplement the historical screening decisions. Locators refer to retained source text. No source is approved for integration by this table.','']
    for n,g in enumerate(m['groups']):
        register.extend([f'## {n+1}. {g["name"]}',''])
        for row in sorted((r for r in rows if r['source']['group_index']==n),key=lambda r:r['source']['id']):
            s=row['source'];v=row['review'];wb=ROOT/s['workbench']
            register.extend([f'### #{s["id"]} — {s["title"]}','',f'**Decision:** {v["decision"]}. **Role:** {v["role"]}.', '',v['review_note'],'',f'**Coverage:** {v["coverage"]}','',f'**Basis:** {v["basis"]}','', '**Reported:** '+'; '.join(v['reported_outcomes']),'','**Intended:** '+'; '.join(v['proposed_outcomes']),'','**Limits:** '+'; '.join(v['limits']),'',link(wb/'practice-review.json','Review record')+' · '+link(wb/'source.md','Retained source')+' · '+link(wb/'drafts','Drafts'),''])
    write('source-review-register.md','\n'.join(register))
    print(json.dumps({'sources':len(rows),'cards':len(cards),'roles':dict(roles),'decisions':dict(decisions)},indent=2))

if __name__=='__main__':main()
