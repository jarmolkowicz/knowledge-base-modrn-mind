"""Regression tests for failures found in the practice-tooling audit."""
import hashlib
import contextlib
import io
import json
from pathlib import Path
import tempfile
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from test_practice_collection import CARD, SCRIPTS, module
import kb_search
import validate_drafts
import check_citation_links
from practice_checks import check_practice
import refresh_practical as refresh

guide = module('build-practice-guide')
sync = module('sync-source-links')
VALID = CARD.replace('source_entries:', 'intended_outcomes: [judgment]\nsource_entries:') + '''
## Origin

Author, specific article, section 2.

## What to Notice

Which claim changed after checking?

## Related

- [[author-specific-article-2026]]
'''


class PracticeAuditTests(unittest.TestCase):
    def issues(self, text, **kwargs):
        return [f.issue for f in check_practice(text, 'test', **kwargs)]

    def test_missing_sections_are_not_ready(self):
        issues = self.issues(CARD, draft=True)
        self.assertIn('missing or empty section: Origin', issues)
        self.assertIn('missing or empty section: What to Notice', issues)

    def test_canonical_requires_exact_identity_and_outcome(self):
        text = VALID.replace('source_entries: [author-specific-article-2026]', 'source_entries: []').replace('intended_outcomes: [judgment]', 'intended_outcomes: []')
        self.assertEqual(len(self.issues(text)), 2)
        self.assertEqual(self.issues(text, draft=True), [])

    def test_all_outcomes_and_source_types_checked(self):
        text = VALID.replace('[judgment]', '[judgment, typo]')
        issues = self.issues(text, source_stems={'different-source-2026'})
        self.assertIn('unknown intended outcome: typo', issues)
        self.assertIn('source_entries target is not a source: author-specific-article-2026', issues)
        self.assertTrue(self.issues(VALID.replace('[judgment]', 'judgment')))
        self.assertTrue(self.issues(VALID.replace('[judgment]', '[judgment, judgment]')))
        self.assertTrue(self.issues(VALID.replace('[judgment]', '[judgment, understanding, attention, calibration]')))

    def test_draft_gate_runs_practice_checks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            wb = root / 'raw/author-2026'
            folder = wb / 'drafts/practices'
            folder.mkdir(parents=True)
            (folder / 'test.md').write_text(CARD, encoding='utf-8')
            with patch.object(validate_drafts, 'KB_ROOT', root), patch.object(validate_drafts, 'load_entries', return_value={}):
                findings = validate_drafts.validate(wb)
            self.assertTrue(any(f.check == 'practice_schema' and 'Origin' in f.issue for f in findings))

    def test_guide_rejects_secondary_typo_without_overwriting(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in ('tooling', 'practices', 'sources'):
                (root / folder).mkdir()
            (root / 'tooling/practice-outcomes.json').write_text(json.dumps({'categories': [{'id': 'judgment'}]}))
            (root / 'sources/author-specific-article-2026.md').touch()
            (root / 'practices/test.md').write_text(VALID.replace('[judgment]', '[judgment, typo]'), encoding='utf-8')
            output = root / 'practice-guide.md'
            output.write_text('last valid guide')
            with patch.object(guide, 'ROOT', root), self.assertRaisesRegex(ValueError, 'unknown intended outcome'):
                guide.main()
            self.assertEqual(output.read_text(), 'last valid guide')

    def test_duplicate_slug_does_not_hide_an_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            directories = {kind: root / kind for kind in ('concept', 'practice')}
            for folder in directories.values():
                folder.mkdir()
                (folder / 'same-slug.md').write_text(VALID, encoding='utf-8')
            with patch.object(kb_search, 'ENTRY_DIRS', directories), patch.object(kb_search, '_CACHE', None):
                with self.assertRaisesRegex(ValueError, 'Duplicate KB slug'):
                    kb_search.load_entries(refresh=True)

    def test_sync_preserves_literal_backslashes_in_citations(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'practice.md'
            path.write_text(VALID + '\n## Sources\n\nOld.\n', encoding='utf-8')
            entry = kb_search._parse_file(path, 'practice')
            entry.sources = [r'Author (2026). Notes on C:\new\references.']
            sync.sync_entry(entry, {'author-specific-article-2026'})
            self.assertIn(entry.sources[0], path.read_text(encoding='utf-8'))

    def test_citation_report_distinguishes_links_from_citation_resolution(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'tooling').mkdir()
            (root / 'tooling/citation-aliases.json').write_text('{}')
            source = SimpleNamespace(type='source')
            practice = SimpleNamespace(type='practice', stem='test', sources=['unresolved wording'],
                                       source_entries=['author-specific-article-2026'],
                                       wikilinks={'author-specific-article-2026'})
            output = io.StringIO()
            with patch.object(check_citation_links, 'KB_ROOT', root), patch.object(check_citation_links, 'load_entries', return_value={'test': practice, 'author-specific-article-2026': source}), patch.object(sys, 'argv', ['check_citation_links.py']), contextlib.redirect_stdout(output):
                self.assertEqual(check_citation_links.main(), 0)
            report = json.loads(output.getvalue())
            self.assertEqual(report['active_citations_checked'], 0)
            self.assertEqual(report['explicit_source_links_checked'], 1)
            self.assertEqual(report['citation_strings_not_resolved_individually'], 1)

    def test_archived_scripts_preserve_original_bytes(self):
        root = SCRIPTS.parents[1]
        moves = json.loads((root / 'tooling/audits/practice-tooling-archive-2026-09-27.json').read_text(encoding='utf-8-sig'))
        for move in moves:
            self.assertFalse((root / move['From']).exists())
            archived = root / move['To']
            self.assertEqual(hashlib.sha256(archived.read_bytes()).hexdigest().upper(), move['SHA256'])


class RefreshAuditTests(unittest.TestCase):
    def test_same_day_runs_keep_separate_ledgers_and_backups(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inbox = root / 'raw/inbox/Practical'
            with patch.object(refresh, 'ROOT', root), patch.object(refresh, 'INBOX', inbox):
                first = refresh.new_run_dir('2026-09-27')
                second = refresh.new_run_dir('2026-09-27')
                self.assertNotEqual(first, second)
                refresh.save_json(first / 'manifest.json', {'old': True})
                post = dict(slug='test', title='Test', date='2026-09-27', url='https://example.org/test')
                refresh.write_article(first, 'Example', post, 'old article', '<p>old</p>', 'public-page')
                refresh.write_article(second, 'Example', post, 'new article', '<p>new</p>', 'public-page')
                self.assertEqual(json.loads((first / 'manifest.json').read_text()), {'old': True})
                self.assertIn('old article', (second / 'previous/Example/test.md').read_text())

    def test_windows_reserved_names(self):
        for name in ('CON', 'COM1', 'LPT9'):
            self.assertTrue(refresh.safe_slug(name).startswith('article-'))

    def test_upstream_path_cannot_escape_episode_folder(self):
        for path in ('episodes/../../outside/transcript.md', 'C:/episodes/a/transcript.md', 'episodes\\a\\transcript.md'):
            with self.assertRaises(ValueError):
                refresh.transcript_path(path)

    def podcast_fixture(self, remote, saved, repo):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inbox = root / 'raw/inbox/Practical'
            target = inbox / "Lenny's Podcast/refreshed/test/transcript.md"
            old = inbox / "Lenny's Podcast/repo/episodes/test/transcript.md"
            for path, content in ((target, saved), (old, repo)):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding='utf-8')
            data = remote.encode()
            blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            responses = [SimpleNamespace(json=lambda: {'sha': 'commit', 'commit': {'committer': {'date': '2026-09-27'}}}),
                         SimpleNamespace(json=lambda: {'tree': [{'path': 'episodes/test/transcript.md', 'sha': blob}]}),
                         SimpleNamespace(text=remote)]
            with patch.object(refresh, 'ROOT', root), patch.object(refresh, 'INBOX', inbox), patch.object(refresh, 'client'), patch.object(refresh, 'get', side_effect=responses) as get, patch.object(refresh.time, 'sleep'):
                run = refresh.new_run_dir('2026-09-27')
                result = refresh.podcasts(run)
            self.assertEqual(result['errors'], [])
            return get.call_count, target.read_text()

    def test_unchanged_refreshed_transcript_is_not_downloaded_again(self):
        calls, saved = self.podcast_fixture('new', 'new', 'old')
        self.assertEqual(calls, 2)
        self.assertEqual(saved, 'new')

    def test_remote_reversion_replaces_stale_refreshed_copy(self):
        calls, saved = self.podcast_fixture('old', 'new', 'old')
        self.assertEqual(calls, 3)
        self.assertEqual(saved, 'old')


if __name__ == '__main__':
    unittest.main()
