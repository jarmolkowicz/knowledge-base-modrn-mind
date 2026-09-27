# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
from pathlib import Path
import sys, json
from dataclasses import asdict
root=Path.cwd()
sys.path.insert(0,str(root/'tooling/scripts'))
from validate_drafts import validate
base=root/'raw/practitioner-practices-development/extraction'
m=json.loads((base/'manifest.json').read_text(encoding='utf-8-sig'))
out=[]
for s in m['sources']:
    if s['group_index']<=4:
        findings=[asdict(f) for f in validate(root/s['workbench'])]
        out.append({'id':s['id'],'workbench':s['workbench'],'findings':findings})
(base/'librarian-learning-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps([x for x in out if x['findings']],ensure_ascii=False,indent=2))
