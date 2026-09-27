import json,sys
from pathlib import Path
from dataclasses import asdict
root=Path.cwd();sys.path.insert(0,str(root/'tooling/scripts'))
from validate_drafts import validate
m=json.loads((root/'raw/practitioner-practices-development/extraction/manifest.json').read_text(encoding='utf-8-sig'))
results=[]
for s in m['sources']:
 if 5<=s['group_index']<=9:
  findings=[asdict(f) for f in validate(root/s['workbench'])]
  (root/s['workbench']/'validation.json').write_text(json.dumps({'date':'2026-09-26','scope':'mechanical draft checks only; integration pending','findings':findings},indent=2),encoding='utf-8')
  results.append({'id':s['id'],'findings':findings})
print(json.dumps(results,indent=2))
