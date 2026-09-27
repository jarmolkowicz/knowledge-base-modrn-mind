"""Check complete practice-review coverage, immutable originals, local links and drafts.

Run through uv with PyYAML, the existing draft-validator dependency. This is a
mechanical audit, not an effectiveness judgment or integration approval.
"""
import argparse
from collections import Counter
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote
from validate_drafts import validate, load_draft_entries

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'raw/practitioner-practices-development/extraction'

def main():
    p=argparse.ArgumentParser();p.add_argument('--root-only',action='store_true');a=p.parse_args()
    manifest=json.loads((BASE/'manifest.json').read_text(encoding='utf-8'))
    # Stage 5 retained copies contain links rebased for their recorded canonical
    # destinations. Validate those links in the intended destination context.
    prepared_path=BASE.parent/'integration/prepared.json'
    prepared=json.loads(prepared_path.read_text(encoding='utf-8')) if prepared_path.exists() else {}
    link_context={str((ROOT/e['draft']).resolve()):(ROOT/e['destination']).parent for e in prepared.get('entries',[])}
    rows=[r for r in manifest['sources'] if not a.root_only or r['group_index']>=14]
    errors=[];results=[];card_paths=set();hashes=0;links=0
    for r in rows:
        wb=ROOT/r['workbench']; rp=wb/'practice-review.json'
        if not rp.exists():errors.append(f'ID{r["id"]}: missing review');continue
        v=json.loads(rp.read_text(encoding='utf-8-sig'))
        for k in ['id','group_index','decision','coverage','locators','basis','reported_outcomes','proposed_outcomes','limits','related_entries','practice_files','role','review_note']:
            if k not in v:errors.append(f'ID{r["id"]}: missing {k}')
        if v['id']!=r['id'] or v['group_index']!=r['group_index']:errors.append(f'ID{r["id"]}: identity mismatch')
        original=ROOT/r['original_snapshot']
        if hashlib.sha256(original.read_bytes()).hexdigest()!=r['sha256']:errors.append(f'ID{r["id"]}: original hash changed')
        else:hashes+=1
        for path in v['practice_files']:
            if not (ROOT/path).is_file():errors.append(f'ID{r["id"]}: missing practice {path}')
            card_paths.add(path)
        findings=[asdict(f) for f in validate(wb)]
        results.append({'id':r['id'],'workbench':r['workbench'],'findings':findings})
        files=list((wb/'drafts').rglob('*.md'))+[rp]
        for name in ['triage.md','distill.md','critique.md']:
            candidate=wb/name
            if not candidate.exists(): candidate=wb/'practice-review'/name
            if not candidate.exists():errors.append(f'ID{r["id"]}: missing {name}')
            else:files.append(candidate)
        for path in files:
            if path.suffix!='.md':continue
            text=path.read_text(encoding='utf-8-sig')
            for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)]+)\)',text):
                target=target.strip('<>').split('#')[0]
                if not target or re.match(r'^[a-zA-Z]+:',target):continue
                # These local links are unquoted relative paths, optionally URL escaped.
                target=unquote(target)
                parent=link_context.get(str(path.resolve()),path.parent)
                if not (parent/target).exists():errors.append(f'{path.relative_to(ROOT)}: broken link {target}')
                links+=1
    # All cards must be discoverable through a source review and the draft validator.
    disk_cards={p.relative_to(ROOT).as_posix() for r in rows for p in (ROOT/r['workbench']/'drafts/practices').glob('*.md')}
    for path in sorted(disk_cards-card_paths):errors.append(f'unregistered card: {path}')
    for r in rows:
        loaded=load_draft_entries(ROOT/r['workbench'])
        for path in (ROOT/r['workbench']/'drafts/practices').glob('*.md'):
            if path.stem not in loaded:errors.append(f'validator skipped {path}')
    stems=Counter(Path(p).stem for p in disk_cards)
    errors.extend(f'duplicate proposed slug: {s}' for s,n in stems.items() if n>1)
    if not a.root_only:
        for path in BASE.glob('*.md'):
            text=path.read_text(encoding='utf-8-sig')
            for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)]+)\)',text):
                target=target.strip('<>').split('#')[0]
                if not target or re.match(r'^[a-zA-Z]+:',target):continue
                if not (path.parent/unquote(target)).exists():errors.append(f'{path.relative_to(ROOT)}: broken link {target}')
                links+=1
    out={'scope':'root' if a.root_only else 'all selected sources','sources':len(rows),'reviews':len(results),'original_hashes_verified':hashes,'practice_files':len(disk_cards),'local_links_checked':links,'errors':errors,'findings_by_source':[r for r in results if r['findings']],'integration_approved':False}
    name='root-validation.json' if a.root_only else 'validation.json'
    (BASE/name).write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,ensure_ascii=False))
    return 1 if errors or out['findings_by_source'] else 0

if __name__=='__main__':raise SystemExit(main())
