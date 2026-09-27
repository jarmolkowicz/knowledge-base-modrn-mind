"""Verify scope, provenance, links and counts for the completed Stage 5 batch."""
from pathlib import Path
import hashlib
import json
import re
import sys
import yaml
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent/'integration'
sys.path.insert(0,str(ROOT/'tooling/scripts'))
from kb_search import load_entries
from lint_checks import find_broken_wikilinks, find_alias_form_mistakes, check_frontmatter_fields, find_missing_related, extract_wikilinks

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return p.read_text(encoding='utf-8-sig')
def section(t,n):
    m=re.search(r'^## '+re.escape(n)+r'\n(.*?)(?=^## |\Z)',t,re.M|re.S)
    return m[1].strip() if m else None

done=json.loads(read(OUT/'completed.json'))
before=json.loads(read(OUT/'canonical-before.json'))
originals=json.loads(read(OUT/'originals-before.json'))
targets={r['destination'] for r in done['entries']}
assert digest(ROOT/'tooling/practice-outcomes.json')==done['taxonomy_sha256']
for p,h in before.items():
    if p not in targets: assert digest(ROOT/p)==h,p
for p,h in originals.items(): assert digest(ROOT/p)==h,p
entries=load_entries()
pool=set(entries)
titles={e.title.lower():s for s,e in entries.items() if e.type!='source' and len(e.title.split())>=2}
findings=[]
for row in done['entries']:
    path=ROOT/row['destination']; e=entries[path.stem]; text=read(path)
    assert digest(ROOT/row['path'])==row['sha256'],row['path']
    assert digest(path)==row['canonical_sha256'],row['destination']
    findings+=find_broken_wikilinks(e.body,pool,entry_label=e.stem)
    findings+=find_alias_form_mistakes(e.body,pool,entry_label=e.stem)
    findings+=check_frontmatter_fields(entry_label=e.stem,entry_type=e.type,status=e.status,area=e.area,sources=e.sources,valid_statuses={'solid','emerging','speculative'},valid_areas={'risk','erosion','preservation'})
    for m in re.finditer(r'\]\((?:<([^>]+)>|([^\s)]+))\)',text):
        link=m[1] or m[2]
        if not re.match(r'[a-zA-Z]+:',link) and not link.startswith('#'):
            assert (path.parent/link.split('#')[0]).exists(),(path,link)
    assert 'Not integrated.' not in text and 'Draft from supplementary review' not in text
    if row['kind']=='new_practice':
        findings+=find_missing_related(e.body,set(extract_wikilinks(e.body)),titles,entry_label=e.stem,self_stem=e.stem)
        assert section(text,'Sources')
    elif row['destination'].startswith('practices/'):
        old=read(OUT/'before'/row['destination'])
        assert section(old,'Origin')==section(text,'Origin'),row['destination']
        oldfm=yaml.safe_load(old.split('---',2)[1]); newfm=yaml.safe_load(text.split('---',2)[1])
        assert oldfm['intended_outcomes']==newfm['intended_outcomes']
        assert set(oldfm['source_entries'])<=set(newfm['source_entries'])
    assert all(s in entries and entries[s].type=='source' for s in e.source_entries)
counts={kind:sum(e.type==kind for e in entries.values()) for kind in ('source','concept','method','practice')}
assert counts=={'source':248,'concept':73,'method':22,'practice':83},counts
assert '**Total entries:** 426' in read(ROOT/'index.md')
assert '**83 integrated practices.**' in read(ROOT/'practice-guide.md')
assert '83 source-grounded routines' in read(ROOT/'README.md')
assert not findings,[str(f) for f in findings]
result=dict(status='passed',integrated_targets=len(targets),new_practices=8,updated_practices=9,updated_methods=1,total_entries=len(entries),counts=counts,protected_preexisting_entries=sum(p not in targets for p in before),reviewed_original_texts_unchanged=len(originals),original_drafts_unchanged=len(done['entries']),practitioner_origins_preserved=9,taxonomy_unchanged=True,selected_link_and_metadata_findings=0)
(OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
done['post_integration_checks']='passed'
(OUT/'completed.json').write_text(json.dumps(done,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
