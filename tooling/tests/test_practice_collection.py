"""Check practice discovery, navigation and bundles without changing the KB."""
import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import kb_search
import validate_drafts


def module(name):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), SCRIPTS / f'{name}.py')
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


index = module('build-index')
counts = module('update_readme_counts')
sync = module('sync-source-links')
CARD = '''---
status: emerging
area: [preservation]
sources: ["Sam Author (2026). Test."]
source_entries: [author-specific-article-2026]
---
# Inspect a claim

## Use When

A claim needs independent checking.

## Try It

1. Inspect the original.

## Evidence and Rationale

Untested routine; practitioner account only.

## Limits

This does not establish retained skill.
'''


class PracticeCollectionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='kb-practice-test-')
        self.root = Path(self.tmp.name)
        for directory in ('concepts', 'methods', 'practices', 'sources'):
            (self.root / directory).mkdir()
        self.card = self.root / 'practices/inspect-a-claim.md'
        self.card.write_text(CARD, encoding='utf-8')

    def tearDown(self):
        self.tmp.cleanup()

    def test_search_loads_canonical_practices_only(self):
        hidden = self.root / 'raw/source/drafts/practices'
        hidden.mkdir(parents=True)
        (hidden / 'unapproved.md').write_text(CARD, encoding='utf-8')
        directories = {kind: self.root / directory.name for kind, directory in kb_search.ENTRY_DIRS.items()}
        with patch.object(kb_search, 'ENTRY_DIRS', directories), patch.object(kb_search, '_CACHE', None):
            entries = kb_search.load_entries(refresh=True)
            self.assertEqual(set(entries), {'inspect-a-claim'})
            self.assertEqual(entries['inspect-a-claim'].type, 'practice')
            self.assertEqual(entries['inspect-a-claim'].source_entries, ['author-specific-article-2026'])
            self.assertEqual(kb_search.search('independent checking', types=['practice'])[0].stem, 'inspect-a-claim')

    def test_index_displays_trigger_and_separate_collection(self):
        entry = kb_search._parse_file(self.card, 'practice')
        with patch.object(index, 'KB_ROOT', self.root), patch.object(index, 'load_entries', return_value={entry.stem: entry}):
            result = index.build_index()
        self.assertIn('## Practices (1)', result)
        self.assertIn('A claim needs independent checking.', result)
        self.assertIn('(practices/inspect-a-claim.md)', result)

    def test_readme_counts_include_practice_and_total(self):
        with patch.object(counts, 'KB_ROOT', self.root):
            values = counts.count_entries()
        self.assertEqual(values['practices'], 1)
        result, _ = counts.patch_text('`practices/` — 0 source-grounded routines; scannable catalog of all 0 entries', values)
        self.assertIn('— 1 source-grounded routines', result)
        self.assertIn('all 1 entries', result)

    def test_validator_discovers_practice_drafts(self):
        workbench = self.root / 'raw/author-test-2026'
        folder = workbench / 'drafts/practices'
        folder.mkdir(parents=True)
        (folder / self.card.name).write_text(CARD, encoding='utf-8')
        entries = validate_drafts.load_draft_entries(workbench)
        self.assertEqual(entries['inspect-a-claim'].type, 'practice')

    def test_explicit_source_identity_overrides_ambiguous_author_year(self):
        available = {'author-specific-article-2026', 'author-other-article-2026'}
        result, unresolved = sync.build_sources_section(['Author (2026). Test.'], available,
                                                        ['author-specific-article-2026'])
        self.assertEqual(unresolved, [])
        self.assertIn('[[author-specific-article-2026]]', result)
        self.assertNotIn('[[author-other-article-2026]]', result)

    def test_missing_explicit_source_is_reported_without_guessing(self):
        result, unresolved = sync.build_sources_section(['Author (2026). Test.'],
                                                        {'author-other-article-2026'}, ['author-missing-2026'])
        self.assertEqual(unresolved, ['author-missing-2026'])
        self.assertNotIn('[[author-other-article-2026]]', result)

    def test_reviewed_legacy_book_identity_survives_new_same_year_articles(self):
        available = {'mollick-cointelligence-2024', 'mollick-076-i-cyborg-using-co-intelligence-2024'}
        result, unresolved = sync.build_sources_section(['Mollick (2024)'], available)
        self.assertEqual(unresolved, [])
        self.assertIn('[[mollick-cointelligence-2024]]', result)

    def test_bundle_preserves_practice_limits_and_allows_empty_collection(self):
        bash = shutil.which('bash') or (r'C:\Program Files\Git\bin\bash.exe' if Path(r'C:\Program Files\Git\bin\bash.exe').exists() else None)
        if not bash:
            self.skipTest('Bash is unavailable')
        # Keep the fixture isolated. The optional README count helper is absent.
        script = self.root / 'build-bundle.sh'
        script.write_text((SCRIPTS / 'build-bundle.sh').read_text(encoding='utf-8'), encoding='utf-8', newline='\n')
        for populated in (True, False):
            if not populated:
                self.card.unlink()  # Exact fixture file inside this temporary directory.
            result = subprocess.run([bash, 'build-bundle.sh'], cwd=self.root, capture_output=True, text=True, timeout=30)
            self.assertEqual(result.returncode, 0, result.stderr)
            bundle = (self.root / 'dist/modern-mind-kb.md').read_text(encoding='utf-8')
            self.assertIn('## Practices', bundle)
            if populated:
                self.assertIn('This does not establish retained skill.', bundle)
                self.assertIn('Untested routine; practitioner account only.', bundle)
                self.assertNotIn('source_entries:', bundle)
                self.assertIn('(1 entries,', result.stdout)
            else:
                self.assertIn('(0 entries,', result.stdout)


if __name__ == '__main__':
    unittest.main()
