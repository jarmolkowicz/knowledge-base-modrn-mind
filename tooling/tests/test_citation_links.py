"""Identity mapping regression tests; not tests of evidential claim support."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_citation_links import resolve


class CitationLinkTests(unittest.TestCase):
    def test_single_match(self):
        self.assertEqual(resolve('Bartoš et al. (2026)', {'bartos-learning-2026'}, {}),
                         'bartos-learning-2026')

    def test_apostrophe(self):
        self.assertEqual(resolve("Dell'Acqua et al. (2023)", {'dellacqua-frontier-2023'}, {}),
                         'dellacqua-frontier-2023')

    def test_ambiguous(self):
        self.assertIsNone(resolve('Nosta (2026)', {'nosta-one-2026', 'nosta-two-2026'}, {}))

    def test_wrong_year(self):
        self.assertIsNone(resolve('Tankelevitch et al. (2024)', {'tankelevitch-demand-2023'}, {}))

    def test_reviewed_version_alias(self):
        aliases = {'Tankelevitch et al. (2024)': {
            'source': 'tankelevitch-demand-2023', 'reason': '2024 publication',
            'evidence': 'raw/tankelevitch-demand-2023/source.md'}}
        self.assertEqual(resolve('Tankelevitch et al. (2024)', {'tankelevitch-demand-2023'}, aliases),
                         'tankelevitch-demand-2023')

    def test_alias_target_absent(self):
        self.assertIsNone(resolve('Author (2024)', set(), {'Author (2024)': {
            'source': 'author-2023', 'reason': 'publication', 'evidence': 'source.md'}}))

    def test_generic_publication_not_author(self):
        self.assertIsNone(resolve('Science Advances (2024)', {'doshi-creativity-2024'}, {}))

    def test_unknown_author_not_guessed(self):
        self.assertIsNone(resolve('Yan et al. (2025)', {'fan-laziness-2025'}, {}))


if __name__ == '__main__':
    unittest.main()
