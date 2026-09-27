"""Run the repository validator and additional checks on this supplementary batch."""
from pathlib import Path
import hashlib
import json
import re
import sys
from dataclasses import asdict
import yaml

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'tooling/scripts'))
from validate_drafts import validate

manifest=json.loads((OUT/'manifest.json').read_text(encoding='utf-8'))
before=json.loads((OUT/'canonical-before.json').read_text(encoding='utf-8'))
coverage=json.loads((OUT/'source-coverage.json').read_text(encoding='utf-8'))
labels={Path(r['path']).stem if r['kind']=='new_practice' else 'update:'+Path(r['path']).stem for r in manifest}
selected=[]
other=[]
for source in sorted({r['source'] for r in manifest}):
    for f in validate(ROOT/'raw'/source):
        item=asdict(f)|{'workbench':source}
        (selected if f.entry in labels else other).append(item)
failures=[]
outcomes={r['id'] for r in json.loads((ROOT/'tooling/practice-outcomes.json').read_text(encoding='utf-8'))['categories']}
for row in manifest:
    p=ROOT/row['path']
    body=p.read_text(encoding='utf-8')
    if hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:
        failures.append('Draft hash changed: '+row['path'])
    for match in re.finditer(r'\]\((?:<([^>]+)>|([^\s)]+))\)',body):
        target=match[1] or match[2]
        if not re.match(r'https?://',target) and not (p.parent/target.split('#')[0]).exists():
            failures.append('Broken Markdown link: '+row['path']+' -> '+target)
    if row['kind']=='new_practice':
        fm=yaml.safe_load(body.split('---',2)[1])
        for s in fm['source_entries']:
            if not (ROOT/'sources'/f'{s}.md').exists(): failures.append('Unknown source '+s)
        if not 1<=len(fm['intended_outcomes'])<=3 or not set(fm['intended_outcomes'])<=outcomes:
            failures.append('Invalid intended outcomes: '+row['path'])
        for heading in ('Use When','Try It','Origin','Evidence and Rationale','Limits','What to Notice','Related'):
            if '\n## '+heading+'\n' not in body: failures.append('Missing '+heading+': '+row['path'])
for path,digest in before.items():
    if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=digest: failures.append('Canonical changed: '+path)
for row in coverage:
    if hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest()!=row['sha256']:
        failures.append('Original changed: '+row['path'])
required={f'N{i:02}' for i in range(1,11)}|{f'E{i:02}' for i in range(1,9)}
resolved={i for r in manifest for i in r['ids']}
if not required<=resolved: failures.append('Unresolved families '+str(required-resolved))
report=dict(new_practice_drafts=sum(r['kind']=='new_practice' for r in manifest), update_proposals=sum(r['kind']=='update_proposal' for r in manifest),original_sources_checked=len(coverage),families_accounted_for=len(required),selected_draft_findings=selected,other_workbench_findings=other,additional_failures=failures,canonical_files_unchanged=len(before) if not any('Canonical changed' in f for f in failures) else False)
(OUT/'validation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=False))
sys.exit(1 if selected or failures else 0)
