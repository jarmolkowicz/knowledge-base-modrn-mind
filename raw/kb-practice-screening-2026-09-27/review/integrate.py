"""Stage 5 for the user-approved supplementary practice batch.

Prepare destination-ready audit copies, record the decision, then integrate only
the manifest targets. Preserve original drafts, historical notes and all sources.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import os
import re
import sys
import yaml

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
OUT=HERE/'integration'
sys.path.insert(0,str(ROOT/'tooling/scripts'))
from kb_search import _parse_file, load_entries
from lint_checks import find_broken_wikilinks, find_alias_form_mistakes
import build_drafts as reviewed

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return p.read_text(encoding='utf-8-sig')
def save(p,t):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(t,encoding='utf-8')
def jsave(p,data): save(p,json.dumps(data,indent=2,ensure_ascii=False)+'\n')
def section(text,name):
    m=re.search(r'^## '+re.escape(name)+r'\n(.*?)(?=^## |\Z)',text,re.M|re.S)
    return m.group(1).strip() if m else None
def replace(text,name,content):
    pat=r'^## '+re.escape(name)+r'\n.*?(?=^## |\Z)'
    assert re.search(pat,text,re.M|re.S),name
    return re.sub(pat,lambda m:'## '+name+'\n\n'+content.strip()+'\n\n',text,count=1,flags=re.M|re.S)
def append(text,name,content):
    old=section(text,name)
    if old is None: return text.rstrip()+'\n\n## '+name+'\n\n'+content.strip()+'\n'
    return replace(text,name,old+'\n\n'+content)
def rebase(text,source,destination):
    def change(m):
        value=m[1] or m[2]
        if re.match(r'[a-zA-Z]+:',value) or value.startswith('#'): return m[0]
        path,sep,anchor=value.partition('#')
        target=(source.parent/path).resolve()
        assert target.is_relative_to(ROOT) and target.exists(),target
        relative=Path(os.path.relpath(target,destination.parent)).as_posix()
        return '](<'+relative+(sep+anchor if sep else '')+'>)'
    return re.sub(r'\]\((?:<([^>]+)>|([^\s)]+))\)',change,text)

def prepare_update(row,data):
    dest=ROOT/row['destination']
    text=read(dest)
    oldfront,body=text.split('---',2)[1:]
    fm=yaml.safe_load(oldfront)
    body=body.lstrip('\n')
    if data['id']=='N09-method':
        draft=read(ROOT/row['path'])
        specs=[('What To Do','What To Do'),('How To Do It','How To Do It'),('Why It Works','Why It Works with Rationale and Evidence Limits'),('Related','the descriptions under Related')]
        for old,heading in specs:
            pat=r'^### Replace '+re.escape(heading)+r'\n(.*?)(?=^### |^## |\Z)'
            m=re.search(pat,draft,re.M|re.S)
            assert m,heading
            body=replace(body,old,m[1])
        body=body.replace('## Why It Works\n','## Rationale and Evidence Limits\n')
        fm['source_entries']=[data['source']]
        fm['sources']=[reviewed.citation(data['source'])]
        body=append(body,'Related','- [[present-projections-with-assumptions-and-alternatives]] — concrete source-grounded routine with explicit adaptations.')
    else:
        textadd=data['text']
        # Focused additions preserve original practitioner steps and origin.
        body=append(body,data['section'],textadd)
        body=append(body,'Evidence and Rationale','### Additional research context\n\n'+data['evidence'])
        if data['id']=='N10':
            body=append(body,'Use When','[Inference] Also when an AI-supported research method leaves important questions or kinds of evidence outside its scope.')
        if data['id']=='E04':
            body=body.replace('No research claim attached to this draft. Source links below retain provenance.','The research below motivates the review variant; it does not evaluate this routine.')
            body=re.sub(r'^## Review Status\n\s*(?=## )','',body,flags=re.M)
        sources=[data['source']]+data.get('support',[])
        for s in sources:
            if s not in fm.setdefault('source_entries',[]): fm['source_entries'].append(s)
            citation=reviewed.citation(s)
            if citation not in fm['sources']: fm['sources'].append(citation)
            body=append(body,'Source roles',f'- [[{s}]] — research rationale or boundary; not the origin or direct validation of this practitioner routine.')
            if '[['+s+']]' not in (section(body,'Related') or ''):
                body=append(body,'Related',f'- [[{s}]] — bounded research context described above.')
        provenance=[]
        for s in sources:
            ranges='; '.join(f'L{a}–{b}' for a,b in reviewed.COVERAGE[s])
            detail='abstract-level check only' if s.startswith('fan-') else 'targeted original sections'
            provenance.append(f'- [[{s}]]: [retained original](<../raw/{s}/source.md>), {ranges}; {detail}.')
        body=append(body,'Evidence and Rationale','### Research review coverage\n\n'+'\n'.join(provenance))
    return '---\n'+yaml.safe_dump(fm,sort_keys=False,allow_unicode=True)+'---\n\n'+body.rstrip()+'\n'

def main():
    assert not (OUT/'completed.json').exists(),'Batch already integrated; do not replay.'
    if '--resume-written' in sys.argv:
        decision=json.loads(read(OUT/'decision.json'))
        prepared=decision['scope']
        for r in prepared:
            assert digest(ROOT/r['destination'])==r['prepared_sha256'],r['destination']
        coverage=json.loads(read(HERE/'source-coverage.json'))
        for s in coverage: assert digest(ROOT/s['path'])==s['sha256'],s['path']
        finish(prepared,coverage,decision['taxonomy_sha256'])
        return
    assert not (OUT/'decision.json').exists(),'Prepared integration already exists; inspect before resume.'
    manifest=json.loads(read(HERE/'manifest.json'))
    baseline=json.loads(read(HERE/'canonical-before.json'))
    coverage=json.loads(read(HERE/'source-coverage.json'))
    outcomes=json.loads(read(ROOT/'tooling/practice-outcomes.json'))
    taxonomy_digest=digest(ROOT/'tooling/practice-outcomes.json')
    for r in manifest:
        assert digest(ROOT/r['path'])==r['sha256'],r['path']
        dst=ROOT/r['destination']
        if r['kind']=='new_practice': assert not dst.exists(),dst
        else: assert digest(dst)==baseline[r['destination']],f'Target edited since review: {dst}'
    for s in coverage: assert digest(ROOT/s['path'])==s['sha256'],s['path']
    all_before={p.relative_to(ROOT).as_posix():digest(p) for folder in ('sources','concepts','methods','practices') for p in (ROOT/folder).glob('*.md')}
    jsave(OUT/'canonical-before.json',all_before)
    jsave(OUT/'originals-before.json',{s['path']:s['sha256'] for s in coverage})
    pool=set(load_entries())|{Path(r['destination']).stem for r in manifest}
    prepared=[]
    for r in manifest:
        dst=ROOT/r['destination']
        src=ROOT/r['path']
        if r['kind']=='new_practice':
            text=rebase(read(src),src,dst)
            text=re.sub(r'\n## Review Status\n.*\Z','\n',text,flags=re.S)
        else:
            data=next(d for d in reviewed.UPDATES if d['id']==r['ids'][0])
            text=prepare_update(r,data)
            save(OUT/'before'/r['destination'],read(dst))
        # Prepare and audit before any canonical mutation.
        staged=ROOT/'raw'/r['source']/'drafts/integration-2026-09-27'/dst.name
        assert not staged.exists(),staged
        save(staged,text)
        assert not find_broken_wikilinks(text,pool,entry_label=dst.stem),dst
        assert not find_alias_form_mistakes(text,pool,entry_label=dst.stem),dst
        for m in re.finditer(r'\]\((?:<([^>]+)>|([^\s)]+))\)',text):
            link=m[1] or m[2]
            if not re.match(r'[a-zA-Z]+:',link) and not link.startswith('#'):
                assert (dst.parent/link.split('#')[0]).exists(),(dst,link)
        prepared.append(r|{'prepared':staged.relative_to(ROOT).as_posix(),'prepared_sha256':digest(staged)})
    jsave(OUT/'decision.json',dict(stage=5,outcome='PROCEED_TO_INTEGRATE',date='2026-09-27',by='Codex librarian; user authorized continuation',authorization='User: Continue, following the completed review and stated next step to integrate reviewed changes.',scope=prepared,taxonomy_sha256=taxonomy_digest,validation='Selected draft checks passed; the historical two-article Niederhoffer first-page-year finding was manually verified in critique-and-decisions.md.'))
    for r in prepared:
        save(ROOT/r['destination'],read(ROOT/r['prepared']))
    finish(prepared,coverage,taxonomy_digest)

def finish(prepared,coverage,taxonomy_digest):
    # Run the normal source-link synchronizer only on approved targets.
    spec=importlib.util.spec_from_file_location('source_sync',ROOT/'tooling/scripts/sync-source-links.py')
    sync=importlib.util.module_from_spec(spec); spec.loader.exec_module(sync)
    entries=load_entries(refresh=True); sources={k for k,e in entries.items() if e.type=='source'}
    for r in prepared:
        _,unmatched=sync.sync_entry(entries[Path(r['destination']).stem],sources)
        assert not unmatched,(r['destination'],unmatched)
        r['canonical_sha256']=digest(ROOT/r['destination'])
    for s in coverage:
        folder=ROOT/'raw'/s['source']
        meta=folder/'source.json'
        data=json.loads(read(meta))
        data['status']='integrated'
        data.setdefault('decisions',[]).append(dict(stage='supplementary_practices_stage_5',outcome='integrated',date='2026-09-27',by='Codex librarian; user-authorized Continue',reason='Reviewed supplementary practices or research-context updates integrated. Original source status and earlier history retained.',batch='raw/kb-practice-screening-2026-09-27/review/integration/decision.json'))
        jsave(meta,data)
        addition='\n\n## 2026-09-27 — Supplementary practices integrated\n\nStage 5 completed under the user’s continuation instruction. See the batch [integration decision](../kb-practice-screening-2026-09-27/review/integration/decision.json). Original drafts and originals retained.\n'
        for name in ('log.md','practice-review-2026-09-27.md'):
            with (folder/name).open('a',encoding='utf-8') as f: f.write(addition)
    with (ROOT/'log.md').open('a',encoding='utf-8') as f:
        f.write('\n\n## 2026-09-27 — Practices from existing KB sources\n\nIntegrated eight new practices, nine focused practice updates and one modulation-method correction following source review and recorded Stage 5 decision. Taxonomy unchanged; original drafts and source material retained. Audit: [batch decision](raw/kb-practice-screening-2026-09-27/review/integration/decision.json).\n')
    jsave(OUT/'completed.json',dict(date='2026-09-27',stage=5,entries=prepared,taxonomy_sha256=taxonomy_digest,post_integration_checks='pending'))
    print(json.dumps({'integrated':len(prepared),'new_practices':8,'practice_updates':9,'method_updates':1}))

if __name__=='__main__': main()
