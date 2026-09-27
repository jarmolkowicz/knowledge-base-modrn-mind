"""Create a complete non-practice inventory and passage pointers for editorial screening.

No keyword score is a selection decision. Existing practices are comparison only.
Canonical entries are read-only; reports live in a separate raw workbench.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from kb_search import KB_ROOT, load_entries

OUT = KB_ROOT / 'raw/kb-practice-screening-2026-09-27'
PATTERN = re.compile(r'\b(practic\w*|retriev\w*|spac\w*|interleav\w*|feedback|scaffold\w*|check\w*|verif\w*|interven\w*|withhold\w*|reflect\w*|protocol|prompt\w*|compar\w*|before|after|assign\w*|review\w*|independen\w*|confiden\w*|disclos\w*|handoff|monitor\w*|explain\w*|evaluat\w*|train\w*)\b', re.I)

def main():
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    p = argparse.ArgumentParser()
    p.add_argument('--type', choices=['method','concept','source'])
    p.add_argument('--start', type=int, default=0)
    p.add_argument('--limit', type=int, default=30)
    p.add_argument('--context', type=int, default=420)
    args = p.parse_args()
    OUT.mkdir(exist_ok=True)
    entries = load_entries()
    previous = json.loads((KB_ROOT/'raw/practitioner-practices-development/integration/completed.json').read_text(encoding='utf-8-sig'))
    covered = {Path(e['destination']).stem for e in previous['entries'] if e['type']=='source'} | {'nosta-borrowed-mind-2026'}
    rows=[]
    for e in entries.values():
        if e.type=='practice':
            continue
        text=Path(e.path).read_text(encoding='utf-8-sig')
        lines=text.splitlines()
        sections=[]
        for match in re.finditer(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)',text,re.M|re.S):
            sections.append(dict(heading=match[1],line=text[:match.start()].count('\n')+1,text=match[2].strip()))
        summary=next((s['text'] for h in ('Key Insight','What It Is','Overview','Core Idea') for s in sections if s['heading']==h),'')
        candidates=[]
        for s in sections:
            if re.search(r'Citation|Related|Supports|Sources|Key Passages|Contradicts',s['heading'],re.I):
                continue
            for paragraph in re.split(r'\n\s*\n',s['text']):
                score=len(PATTERN.findall(paragraph))
                if score:
                    candidates.append(dict(section=s['heading'],line=s['line'],text=paragraph,score=score))
        candidates.sort(key=lambda x:x['score'],reverse=True)
        row=dict(stem=e.stem,title=e.title,type=e.type,status=e.status,path=Path(e.path).relative_to(KB_ROOT).as_posix(),
                 sha256=hashlib.sha256(Path(e.path).read_bytes()).hexdigest(),lines=len(lines),words=len(text.split()),
                 previous_practice_review=e.stem in covered,summary=summary,headings=[s['heading'] for s in sections],passage_pointers=candidates[:5])
        rows.append(row)
    existing_inventory=OUT/'inventory.json'
    if not existing_inventory.exists() or json.loads(existing_inventory.read_text(encoding='utf-8')).get('format_version') != 2:
        existing_inventory.write_text(json.dumps(dict(format_version=2,scope='All canonical sources, concepts and methods; practices excluded as extraction input.',entries=rows),indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
        comparison=[dict(stem=e.stem,title=e.title,path=Path(e.path).relative_to(KB_ROOT).as_posix(),sources=e.source_entries) for e in entries.values() if e.type=='practice']
        (OUT/'existing-practices.json').write_text(json.dumps(comparison,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    selected=sorted([r for r in rows if not r['previous_practice_review'] and (not args.type or r['type']==args.type)],key=lambda r:r['stem'])
    print(f'Inventory: {len(rows)} non-practice entries; {sum(r["previous_practice_review"] for r in rows)} previously reviewed sources; {len(selected)} in this packet population.')
    for i,r in enumerate(selected[args.start:args.start+args.limit],args.start):
        print(f'\n{i}. {r["stem"]} [{r["status"]}]')
        print('SUMMARY: '+re.sub(r'\s+',' ',r['summary'])[:args.context])
        if r['type']=='method':
            print('SECTIONS: '+'; '.join(r['headings']))
        if r['passage_pointers']:
            s=r['passage_pointers'][0]
            print(f'POINTER L{s["line"]} ({s["section"]}): '+re.sub(r'\s+',' ',s['text'])[:args.context])

if __name__=='__main__':
    main()
