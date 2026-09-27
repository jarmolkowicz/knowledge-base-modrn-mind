# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Show expanded original-source sections for the fixed unresolved 400-item queue.

No semantic decisions are automated. A source packet preserves headings, relevant
section/turn context and locators. Assistant writes decisions separately.
"""
import argparse, hashlib, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'raw/practitioner-practices-development/screening'
DEST=OUT/'queue-review'
sys.stdout.reconfigure(encoding='utf-8')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('start',type=int)
    ap.add_argument('end',type=int)
    ap.add_argument('--chars',type=int,default=3800)
    args=ap.parse_args()
    records=json.loads((OUT/'screening-register.json').read_text(encoding='utf-8'))['records']
    DEST.mkdir(exist_ok=True)
    qp=DEST/'queue.json'
    if not qp.exists():
        queue=[r['screening_id'] for r in records if r['review_decision'] in ('priority_review','transfer_review')]
        assert len(queue)==400
        qp.write_text(json.dumps(queue),encoding='utf-8')
    queue=json.loads(qp.read_text())
    for pos in range(args.start,min(args.end,len(queue))):
        i=queue[pos];r=records[i];text=(ROOT/r['path']).read_text(encoding='utf-8-sig')
        assert hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256']
        lines=text.splitlines();heads=[f'L{n+1} {x}' for n,x in enumerate(lines) if x.startswith(('## ','### ','#### '))]
        clean=[]
        for n,line in enumerate(lines):
            if not line.strip() or '![' in line: continue
            line=re.sub(r'!?\[([^\]]*)\]\([^)]*\)',r'\1',line)
            clean.append((n+1,line))
        # Full available text when short. For longer texts show an expanded section
        # around the earlier inspected anchor, plus action-bearing paragraphs from
        # other parts. Selection is visible and not treated as complete reading.
        body=[x for x in clean if x[0]>8]
        budget=args.chars; chosen=set()
        if sum(len(x[1]) for x in body)<=budget:
            chosen={n for n,_ in body};coverage='all available text, excluding linked images/media'
        else:
            packet=json.loads((OUT/'inspection-packets'/f'{i:03}.json').read_text(encoding='utf-8'))
            anchor=packet['passages'][-1]['line'] if packet['passages'] else 10
            blocks=[]; in_steps=False; speaker=''
            for n,line in body:
                if line.startswith('#'):
                    in_steps=bool(re.search(r'step.by.step|the prompt|how to|protocol|tests to|questions to|things to',line,re.I))
                if re.search(r'\(\d\d:\d\d:\d\d\)',line):
                    if re.search(r'[A-Za-z]',line): speaker=line
                    continue
                if len(line)<35:continue
                if re.search(r'sponsor|brought to you|free trial|vanta.com|get a demo',line,re.I):continue
                score=len(re.findall(r'\b(?:first|then|ask|write|try|before|after|compare|question|test|example|practice|feedback|we use|I use|decide|step)\b',line,re.I))
                if 'Transcript' in ' '.join(heads):
                    if 'Lenny' in speaker: score-=30
                    if len(line)<180: score-=15
                    if re.search(r'\b(?:AI|ChatGPT|Claude|LLM|Copilot)\b',line): score+=12
                if in_steps:score+=20
                if line.startswith('`'):score+=15
                blocks.append((score,n,line))
            target=min(blocks,key=lambda x:abs(x[1]-anchor)) if blocks else None
            order=([target] if target and 'Transcript' not in ' '.join(heads) else [])+sorted(blocks,reverse=True)
            used=0
            for _,n,line in order:
                if n in chosen:continue
                if 'Transcript' in ' '.join(heads) and len(line)<180: continue
                if used+len(line)>budget:
                    continue
                chosen.add(n);used+=len(line)
                # Include nearest preceding speaker/question/header context.
                for k,v in reversed(body):
                    if k<n and (re.search(r'\(\d\d:\d\d:\d\d\)',v) or v.startswith('#')):
                        chosen.add(k);break
            coverage='expanded selected original paragraphs with speaker/header context; not full source'
        selected=[{'line':n,'text':s} for n,s in body if n in chosen]
        p=dict(queue_position=pos,id=i,path=r['path'],sha256=r['sha256'],title=r['title'],coverage=coverage,headings=heads,passages=selected)
        (DEST/f'{i:03}.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
        print(f"\n[{pos}] ID{i} {r['title']} ({r.get('words')} words)\n{coverage}")
        if heads:print('HEADINGS: '+' / '.join(heads)[:650])
        for x in selected:print(f"L{x['line']} {x['text']}")

if __name__=='__main__':main()
