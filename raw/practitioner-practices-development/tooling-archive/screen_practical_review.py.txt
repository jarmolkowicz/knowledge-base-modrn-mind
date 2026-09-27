# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml"]
# ///
"""Local screening reader. Generates excerpts, never semantic decisions.

Review decisions are written separately by the assistant. Recorded excerpts show
exactly which parts were inspected; an excerpt screen is not a full-text review.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from screen_practical import metadata

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'raw/practitioner-practices-development/screening'
RECORDS = json.loads((OUT / 'screening-register.json').read_text(encoding='utf-8'))['records']
sys.stdout.reconfigure(encoding='utf-8')
AI = re.compile(r'\b(?:AI|ChatGPT|Claude|LLM|artificial intelligence|language model)\b', re.I)
HUMAN = re.compile(r'\b(?:think\w*|learn\w*|reflect\w*|judg\w*|creativ\w*|decis\w*|reason\w*|question\w*|assum\w*|feedback|skill\w*|agency|ownership|voice|writ\w*)\b', re.I)
ACTION = re.compile(r'\b(?:ask|try|write|compare|test|first|step|prompt|exercise|practice|yourself|we use|I use|I tried|I asked|you can|you should)\b', re.I)
AD = re.compile(r'(?:brought to you by|our sponsors|sponsor this|off your first|off your subscription|vanta.com/lenny|university.com/lenny|lennysnewsletter.com/subscribe|product called Sprig|Sprig.s precise targeting|product-analytics.*platform|get a demo|free trial|sponsoring|sponsor.*episode)', re.I)

def paragraphs(text):
    meta, body, offset = metadata(text)
    out = []
    # Split large EPUB paragraphs at sentence boundaries while retaining offsets.
    for match in re.finditer(r'[^\n]+', body):
        raw = match[0]
        if not raw.strip() or raw.lstrip().startswith(('![', '[![', '<', '---', '#')):
            continue
        chunks = list(re.finditer(r'.{1,1200}(?:\s|$)', raw)) if len(raw) > 1500 else [None]
        for chunk in chunks:
            value = chunk[0] if chunk else raw
            start = offset + match.start() + (chunk.start() if chunk else 0)
            value = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', r'\1', value)
            value = re.sub(r'\s+', ' ', value).strip()
            if len(value) < 45 or AD.search(value):
                continue
            out.append({'line': text[:start].count('\n') + 1, 'offset': start, 'text': value})
    return meta, out

def packet(i, size):
    r = RECORDS[i]
    path = ROOT / r['path']
    if path.suffix == '.pdf':
        return {'id': i, 'title': r['title'], 'path': r['path'], 'coverage': 'PDF not yet extracted', 'passages': []}
    text = path.read_text(encoding='utf-8-sig')
    meta, paras = paragraphs(text)
    headings = [m[1].strip() for m in re.finditer(r'^#{2,6}\s+(.+)$', text, re.M)]
    scored = sorted(enumerate(paras), key=lambda ip: (bool(AI.search(ip[1]['text'])) * 4 + min(len(HUMAN.findall(ip[1]['text'])), 4) + min(len(ACTION.findall(ip[1]['text'])), 4)), reverse=True)
    selected = []
    if paras:
        selected.append(dict(paras[0], text=paras[0]['text'][:size//3]))
    for index, para in scored:
        if selected and para['offset'] == selected[0]['offset']:
            continue
        selected.append(dict(para, text=para['text'][:size]))
        break
    return {'id': i, 'title': r['title'], 'collection': r['collection'], 'path': r['path'], 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'access': r['access'], 'kind': r['kind'], 'words': r.get('words'), 'headings': headings[:14], 'coverage': 'opening + one cue-ranked passage + headings; partial inspection', 'passages': selected}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('command', choices=['packet','read','inventory'])
    ap.add_argument('ids', nargs='*', type=int)
    ap.add_argument('--chars', type=int, default=480)
    ap.add_argument('--skip-gaps', action='store_true')
    args = ap.parse_args()
    if args.command == 'inventory':
        for i,r in enumerate(RECORDS):
            print(f"{i}|{r['collection']}|{r['title']}|{r['route']}")
        return
    if args.command == 'packet':
        start, end = args.ids
        saved = OUT / 'inspection-packets'
        saved.mkdir(exist_ok=True)
        for i in range(start, min(end, len(RECORDS))):
            if args.skip_gaps and RECORDS[i]['route'] == 'access_gap':
                print(f"{i}|ACCESS HOLD|{RECORDS[i]['title']}")
                continue
            p = packet(i,args.chars)
            (saved/f'{i:03}.json').write_text(json.dumps(p,ensure_ascii=False,indent=2),encoding='utf-8')
            print(f"\n{i}|{p.get('collection')}|{p['title']}|{p.get('access')}|{p.get('words')}")
            if p.get('headings'):
                print('H: '+ ' / '.join(p['headings'])[:args.chars//2])
            for para in p['passages']:
                print(f"L{para['line']}: {para['text']}")
    else:
        for i in args.ids:
            r = RECORDS[i]
            text=(ROOT/r['path']).read_text(encoding='utf-8-sig')
            print(f"\n{i}|{r['path']}|{r['title']}")
            if args.chars >= len(text):
                for n,line in enumerate(text.splitlines(),1):
                    if not line.strip() or re.search(r'!\[.*\]\(',line):continue
                    line=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',line)
                    print(f'L{n}: {line}')
            else:
                meta, paras=paragraphs(text)
                ranked=sorted(paras,key=lambda p:bool(AI.search(p['text']))*4+min(len(HUMAN.findall(p['text'])),4)+min(len(ACTION.findall(p['text'])),4),reverse=True)
                selected=[]; used=0
                for p in ranked:
                    if used+len(p['text']) > args.chars: continue
                    selected.append(p); used+=len(p['text'])
                for p in sorted(selected,key=lambda p:p['offset']): print(f"L{p['line']}: {p['text']}")
                print('[Selected passages only; not full text]')

if __name__ == '__main__':
    main()
