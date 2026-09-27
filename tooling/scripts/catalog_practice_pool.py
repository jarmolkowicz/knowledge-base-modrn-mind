# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Catalog the selected practice sources, preserving existing book workbenches.

Mechanical only: no claims of reading, triage or approval. Markdown passes
through the normal extractor; PDF text reuses the verified prior extraction.
"""
import contextlib, hashlib, io, json, re, shutil, sys
from pathlib import Path
import extract

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'raw/practitioner-practices-development'
OUT=BASE/'extraction'

def main():
    pool=json.loads((BASE/'screening/consolidated-shortlist.json').read_text(encoding='utf-8'))
    reg=json.loads((BASE/'screening/screening-register.json').read_text(encoding='utf-8'))['records']
    OUT.mkdir(exist_ok=True)
    manifest=[]
    for r in pool['records']:
        i=r['id'];original=ROOT/r['path']
        assert hashlib.sha256(original.read_bytes()).hexdigest()==r['sha256']
        group=next(n for n,g in enumerate(pool['groups']) if i in g['starting_ids']+g['additional_ids'])
        if i in (879,880):
            bench=original.parent
        else:
            collection=reg[i]['collection']
            prefix={'Sam Illingworth':'illingworth',"Lenny's Podcast":'lenny','Ruben Hassid':'hassid','Sabrina Ramonov':'ramonov','Ethan Mollick':'mollick','Cal Newport':'newport','Random':'tamisier-fayard'}.get(collection,extract.slugify(collection))
            words=extract.slugify(r['title']).split('-')[:6]
            year=str(reg[i].get('date',''))[:4]
            if not re.fullmatch(r'\d{4}',year):year='2026'
            slug=f'{prefix}-{i:03}-'+ '-'.join(words)+f'-{year}'
            bench=ROOT/'raw'/slug
            if not bench.exists():
                if original.suffix.lower()=='.pdf':
                    bench.mkdir()
                    shutil.copy2(original,bench/'original.pdf')
                    shutil.copy2(BASE/'screening/pdf-screening-text.md',bench/'source.md')
                    m=dict(slug=slug,original_filename=original.name,format='pdf',source_type='article',hash=r['sha256'],extractor='reused verified screening PDF extraction',status='cataloged',decisions=[],pages=6)
                    (bench/'source.json').write_text(json.dumps(m,indent=2)+'\n',encoding='utf-8')
                    (bench/'log.md').write_text('# Source log\n\n2026-09-26 — Cataloged original PDF and reused prior six-page extraction. No content decision.\n',encoding='utf-8')
                else:
                    sys.argv=['extract.py',str(original),'--slug',slug,'--kb-root',str(ROOT)]
                    with contextlib.redirect_stdout(io.StringIO()):assert extract.main()==0
            meta=json.loads((bench/'source.json').read_text(encoding='utf-8'))
            assert meta['hash']==r['sha256'], f'Workbench collision: {bench}'
            meta['source_type']='transcript' if collection=="Lenny's Podcast" else 'article'
            meta['screening_id']=i
            meta['collected_from']=r['path']
            meta['bibliographic_metadata']={k:reg[i].get(k) for k in ('title','date','url','collection')}
            (bench/'source.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        (bench/'drafts/practices').mkdir(parents=True,exist_ok=True)
        manifest.append({**r,'group_index':group,'workbench':bench.relative_to(ROOT).as_posix(),'source_path':(bench/'source.md').relative_to(ROOT).as_posix(),'original_snapshot':r['path'],'date':reg[i].get('date',''),'collection':reg[i]['collection'],'existing_integrated':i==880})
    (OUT/'manifest.json').write_text(json.dumps({'groups':pool['groups'],'sources':manifest},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'sources':len(manifest),'groups':len(pool['groups']),'new_workbench_candidates':len(manifest)-2,'book_workbenches_reused':2}))

if __name__=='__main__':main()
