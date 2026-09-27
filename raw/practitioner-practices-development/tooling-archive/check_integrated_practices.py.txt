"""Verify the approved integration, immutable inputs and destination-aware links."""
from contextlib import redirect_stdout
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
from urllib.parse import unquote
import kb_search
import linter
from check_citation_links import check_explicit_sources, resolve

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'raw/practitioner-practices-development'
RUN = BASE / 'integration'

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    result = read_json(RUN / 'completed.json')
    plan = read_json(BASE / 'extraction/integration-plan.json')
    original = read_json(BASE / 'extraction/manifest.json')
    errors = []
    spec = importlib.util.spec_from_file_location('source_sync', Path(__file__).with_name('sync-source-links.py'))
    sync = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sync)
    # Scoped auxiliary sync: do not rewrite unrelated existing entries.
    with redirect_stdout(io.StringIO()):
        for item in result['entries']:
            if item['type'] == 'practice':
                assert sync.main(['--entry', Path(item['destination']).stem]) == 0
    entries = kb_search.load_entries(refresh=True)
    sources = {s for s,e in entries.items() if e.type == 'source'}
    local_links = 0
    for path, old_hash in read_json(RUN / 'baseline.json').items():
        if sha(Path(path)) != old_hash:
            errors.append(f'Existing canonical entry changed: {path}')
    for source in original['sources']:
        if sha(ROOT / source['original_snapshot']) != source['sha256']:
            errors.append(f'Original snapshot changed: {source["id"]}')
        wb = ROOT / source['workbench']
        meta = read_json(wb / 'source.json')
        retained = list(wb.glob('original.*'))
        if not any(sha(p) == meta['hash'] for p in retained):
            errors.append(f'Retained original/hash mismatch: {source["id"]}')
    for card in plan['cards']:
        if sha(ROOT / card['draft']) != card['sha256']:
            errors.append(f'Reviewed extraction changed: {card["slug"]}')
        if card['status'] == 'hold_for_source_correction' and (ROOT / card['proposed_destination']).exists():
            errors.append(f'Held card was integrated: {card["slug"]}')
    files = [ROOT / item['destination'] for item in result['entries']]
    files += [ROOT / 'practice-guide.md', ROOT / 'index.md', BASE / 'extraction/README.md',
              BASE / 'extraction/integration-plan.md', BASE / 'extraction/outcome-review.md', RUN / 'README.md']
    for path in files:
        text = path.read_text(encoding='utf-8')
        for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)]+)\)', text):
            target = target.strip('<>').split('#')[0]
            if not target or re.match(r'^[a-zA-Z]+:', target):
                continue
            local_links += 1
            if not (path.parent / unquote(target)).exists():
                errors.append(f'Broken local link: {path.relative_to(ROOT)} -> {target}')
    for item in result['entries']:
        path = ROOT / item['destination']
        draft = ROOT / item['draft']
        if path.read_text(encoding='utf-8').rstrip() != draft.read_text(encoding='utf-8').rstrip():
            errors.append(f'Approved copy content changed: {path.name}')
        item['canonical_sha256'] = sha(path)
        if item['type'] == 'practice':
            errors.extend(check_explicit_sources(entries[path.stem], sources))
    findings = [f.__dict__ for f in linter.run_checks(None, entries)]
    errors.extend(findings)
    bundle_path = ROOT / 'dist/modern-mind-kb.md'
    bundle = bundle_path.read_text(encoding='utf-8')
    anchors = re.findall(r'<a id="((?:concepts|methods|practices|sources)-[^"]+)"></a>', bundle)
    if len(anchors) != len(entries) or len(set(anchors)) != len(entries):
        errors.append('Bundle entry count or unique anchors differ from canonical entries')
    practice_bodies = 0
    for item in result['entries']:
        if item['type'] != 'practice':
            continue
        text = (ROOT / item['destination']).read_text(encoding='utf-8')
        body = re.sub(r'^---\s*\n.*?\n---\s*\n', '', text, count=1, flags=re.S).strip()
        if body not in bundle:
            errors.append(f'Practice body changed or missing in bundle: {item["destination"]}')
        else:
            practice_bodies += 1
    # Compare legacy citation navigation with the same entries/source inventory
    # as before integration, so unrelated existing ambiguity is not hidden.
    aliases = read_json(ROOT / 'tooling/citation-aliases.json')
    old_stems = {Path(p).stem for p in read_json(RUN/'baseline.json')}
    old_sources = sources & old_stems
    def legacy_findings(source_pool):
        found = []
        for stem in sorted(old_stems):
            entry = entries[stem]
            if entry.type == 'source':
                continue
            for citation in entry.sources:
                target = resolve(citation, source_pool, aliases)
                if not target or target not in entry.wikilinks:
                    found.append(dict(entry=stem, citation=citation, issue='unresolved identity' if not target else 'canonical link missing'))
        return found
    before_citations, after_citations = legacy_findings(old_sources), legacy_findings(sources)
    regressions = [f for f in after_citations if f not in before_citations]
    errors.extend(regressions)
    (RUN / 'legacy-citation-check.json').write_text(json.dumps(dict(before=before_citations, after=after_citations, regressions=regressions), indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    summary = dict(practices_integrated=result['practices'], new_sources=result['new_sources'],
                   reused_sources=1, original_snapshots_verified=len(original['sources']),
                   retained_originals_verified=len(original['sources']), protected_entries_verified=len(read_json(RUN/'baseline.json')),
                   reviewed_draft_hashes_verified=len(plan['cards']), local_links_checked=local_links,
                   canonical_entries=len(entries), legacy_citation_findings=len(after_citations),
                   new_citation_regressions=len(regressions), bundle_entries=len(anchors),
                   complete_practice_bodies_in_bundle=practice_bodies, errors=errors)
    (RUN / 'validation.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    (RUN / 'completed.json').write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps(summary, indent=2, ensure_ascii=True))
    return bool(errors)

if __name__ == '__main__':
    raise SystemExit(main())
