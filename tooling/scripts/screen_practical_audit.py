# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml", "pypdf"]
# ///
"""Local extraction/provenance helpers for the screening; no automated content verdicts."""
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from screen_practical_review import ROOT, OUT, RECORDS, paragraphs
sys.stdout.reconfigure(encoding='utf-8')

def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

def audit():
    issues=[]; bodies={}
    for i,r in enumerate(RECORDS):
        if r['kind']!='transcript': continue
        text=(ROOT/r['path']).read_text(encoding='utf-8-sig')
        speakers=Counter(re.findall(r'^([^\n:]{2,70})\s+\(\d\d:\d\d:\d\d\):', text, re.M))
        speakers={k:v for k,v in speakers.items() if 'lenny' not in k.lower()}
        top=sorted(speakers,key=speakers.get,reverse=True)[:2]
        guest=text.split('guest:',1)[1].split('\n')[0].strip() if 'guest:' in text else ''
        identity=' '.join(top)
        item={'id':i,'path':r['path'],'metadata_guest':guest,'dominant_speakers':top,'url':r['url']}
        if top and norm(guest) not in norm(identity) and not any(norm(x)[:6] in norm(identity) for x in re.findall(r'[A-Za-z]{3,}',guest)) and 'Various' not in guest and guest!='Failure':
            item['issue']='metadata_guest_body_speaker_mismatch'; issues.append(item)
        if '|' in r['title'] and top and not any(norm(x)[:6] in norm(r['title']) for x in re.findall(r'[A-Za-z]{3,}',guest)):
            issues.append(dict(item,issue='title_guest_mismatch',title=r['title']))
        body=re.split(r'## Transcript\s*',text,maxsplit=1)[-1]
        digest=hashlib.sha256(re.sub(r'\s+',' ',body).strip().encode()).hexdigest()
        if digest in bodies:
            issues.append(dict(item,issue='identical_transcript_body',duplicate_of=bodies[digest]))
        else: bodies[digest]=i
    (OUT/'provenance-audit.json').write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
    for x in issues: print(json.dumps(x,ensure_ascii=False))

def books():
    packets=[]
    for i in (879,880):
        r=RECORDS[i]; text=(ROOT/r['path']).read_text(encoding='utf-8-sig')
        sections=re.split(r'(?=\[ch\.\d+[^\n]*\])',text)
        print('\nBOOK',i,r['path'])
        for section in sections:
            if not section.strip():continue
            marker=section.split('\n',1)[0]; body=section[len(marker):].strip()
            if not body: continue
            sentences=re.split(r'(?<=[.!?])\s+',body)
            steps=[s for s in sentences if re.search(r'\b(?:exercise|practice|ask yourself|before you|try this|first.*then|write down|keep a|without AI|without the|do not|don.t)\b',s,re.I)]
            p={'book_id':i,'marker':marker,'words':len(body.split()),'opening':body[:200],'closing':body[-160:],'practice_passages':[s[:500] for s in steps[:3]],'coverage':'section opening and closing plus first three practice-cue sentences; partial chapter screen'}
            packets.append(p)
            print(json.dumps(p,ensure_ascii=False))
    (OUT/'book-inspection-packets.json').write_text(json.dumps(packets,ensure_ascii=False,indent=2),encoding='utf-8')

def pdf():
    from pypdf import PdfReader
    src=ROOT/RECORDS[255]['path']; reader=PdfReader(src)
    pages=[f'[p.{i+1}]\n'+(p.extract_text() or '') for i,p in enumerate(reader.pages)]
    dest=OUT/'pdf-screening-text.md'
    dest.write_text('\n\n'.join(pages),encoding='utf-8')
    (OUT/'pdf-screening-metadata.json').write_text(json.dumps({'original':RECORDS[255]['path'],'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'pages':len(pages),'extractor':'pypdf','purpose':'screening derivative; original retained in inbox; not cataloged'},indent=2),encoding='utf-8')
    print(dest.read_text(encoding='utf-8'))

def section():
    i,chapter=int(sys.argv[2]),int(sys.argv[3])
    text=(ROOT/RECORDS[i]['path']).read_text(encoding='utf-8-sig')
    match=re.search(r'\[ch\.'+str(chapter)+r'[^\n]*\]\s*(.*?)(?=\[ch\.|\Z)',text,re.S)
    print(match[0] if match else 'NOT FOUND')

def windows():
    i=int(sys.argv[2]);pattern=sys.argv[3];width=int(sys.argv[4]) if len(sys.argv)>4 else 700
    text=(ROOT/RECORDS[i]['path']).read_text(encoding='utf-8-sig')
    print(i,RECORDS[i]['path']);last=-1;pack=[]
    for m in re.finditer(pattern,text,re.I):
        start=max(0,m.start()-width//2);end=min(len(text),m.end()+width)
        if start<=last:continue
        pack.append({'line':text[:start].count('\n')+1,'text':text[start:end]})
        last=end
        if len(pack)>=12:break
    (OUT/f'expanded-{i}.json').write_text(json.dumps(pack,ensure_ascii=False,indent=2),encoding='utf-8')
    for p in pack:print(f"L{p['line']}: {p['text']}\n")

if __name__=='__main__':
    {'audit':audit,'books':books,'pdf':pdf,'section':section,'windows':windows}[sys.argv[1]]()
