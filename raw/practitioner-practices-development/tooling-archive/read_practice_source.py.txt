# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Display line-numbered retained sources. No semantic selection or decisions."""
import argparse,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
    sys.stdout.reconfigure(encoding='utf-8')
    p=argparse.ArgumentParser();p.add_argument('ids');p.add_argument('--start',type=int,default=1);p.add_argument('--end',type=int);p.add_argument('--find');p.add_argument('--context',type=int,default=4)
    a=p.parse_args();m=json.loads((ROOT/'raw/practitioner-practices-development/extraction/manifest.json').read_text(encoding='utf-8'))
    for i in map(int,a.ids.split(',')):
        r=next(x for x in m['sources'] if x['id']==i)
        lines=(ROOT/r['source_path']).read_text(encoding='utf-8-sig').splitlines()
        print(f'\n=== ID{i} {r["title"]}; {len(lines)} lines; {r["source_path"]} ===')
        chosen=set(range(a.start-1,min(a.end or len(lines),len(lines))))
        if a.find:
            found=[n for n,l in enumerate(lines) if re.search(a.find,l,re.I)]
            chosen&={k for n in found for k in range(max(0,n-a.context),min(len(lines),n+a.context+1))}
        for n in sorted(chosen):
            line=lines[n]
            if not line.strip():continue
            if line.lstrip().startswith('!['):print(f'L{n+1} [linked image; not inspected]');continue
            line=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',line)
            print(f'L{n+1} {line}')
if __name__=='__main__':main()
