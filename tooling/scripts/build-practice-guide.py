"""Build practice-guide.md from integrated practices and the outcome vocabulary."""
import json
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[2]

def main():
    taxonomy = json.loads((ROOT / 'tooling/practice-outcomes.json').read_text(encoding='utf-8'))
    groups = {c['id']: [] for c in taxonomy['categories']}
    groups['unassigned'] = []
    for path in sorted((ROOT / 'practices').glob('*.md')):
        text = path.read_text(encoding='utf-8')
        fm = re.match(r'^---\s*\n(.*?)\n---', text, re.S)
        meta = yaml.safe_load(fm[1]) if fm else {}
        title = re.search(r'^# (.+)$', text, re.M)[1]
        trigger = re.search(r'^## Use When\s+(.+?)(?=\n\n|\n## |\Z)', text, re.M | re.S)
        outcomes = meta.get('intended_outcomes', [])
        group = outcomes[0] if outcomes else 'unassigned'
        if group not in groups:
            raise ValueError(f'Unknown intended outcome in {path.name}: {group}')
        groups[group].append((path.stem, title, re.sub(r'\s+', ' ', trigger[1]).strip() if trigger else 'See entry.'))
    total = sum(map(len, groups.values()))
    lines = ['# Practices by intended outcome', '',
             f'**{total} integrated practices.** Choose a situation or outcome, then open the practice for steps, source accounts, limits and things to observe.', '',
             'These routines come from practitioner accounts, research, proposed exercises and documented examples. Inclusion is not proof of effectiveness or a blanket endorsement of an author. Research-based adaptations, AI adaptations and curator observations are labeled. Each entry distinguishes intended benefits from reported results.', '',
             'The outcome vocabulary is provisional. Eight categories concern human thinking and participation; two support them through accountability or immediate work quality. Better assisted output does not by itself show improved judgment, retained skill or well-calibrated confidence.', '',
             '| Intended outcome | Type | Practices |', '|---|---|---:|']
    for category in taxonomy['categories']:
        lines.append(f'| [{category["title"]}](#{category["id"]}) | {category["role"]} | {len(groups[category["id"]])} |')
    for category in taxonomy['categories'] + [dict(id='unassigned', title='Outcome not yet assigned', definition='', boundary='')]:
        rows = groups[category['id']]
        if not rows:
            continue
        lines += ['', f'<a id="{category["id"]}"></a>', '', f'## {category["title"]}', '', category['definition'], '', category['boundary'], '',
                  '| Practice | Use when |', '|---|---|']
        for stem,title,trigger in rows:
            title, trigger = title.replace('|', '\\|'), trigger.replace('|', '\\|')
            lines.append(f'| [{title}](practices/{stem}.md) | {trigger} |')
    lines += ['', 'For source selection, reading coverage, excluded items and integration history, see the [review record](raw/practitioner-practices-development/extraction/README.md).']
    (ROOT / 'practice-guide.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'Wrote practice-guide.md: {total} practices')

if __name__ == '__main__':
    main()
