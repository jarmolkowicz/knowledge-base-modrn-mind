"""Index summaries must retain full claims around author and comparison abbreviations."""
import importlib.util
from pathlib import Path
import sys
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location('index_sentences', SCRIPTS / 'build-index.py')
index = importlib.util.module_from_spec(spec)
spec.loader.exec_module(index)


class IndexSentenceTests(unittest.TestCase):
    def test_real_publication_abbreviations(self):
        for sentence in (
            'Cheng et al. report higher endorsement.',
            'Being evaluated by an AI system (vs. a person) changed ratings.',
            'J. D. Teeny studied U.S. participants.',
            'Methods differ, e.g. in task design.',
            '**The effect was uncertain.**',
        ):
            with self.subTest(sentence=sentence):
                body = '## Key Insight\n\n' + sentence + ' A second sentence.\n\nMore detail.'
                self.assertEqual(index._extract_oneliner(body, ['Key Insight']), sentence)

    def test_paragraph_boundary_and_table_safety(self):
        body = '## Overview\n\nA | B comparison without a final full stop\n\nSeparate paragraph.'
        self.assertEqual(index._extract_oneliner(body, ['Overview']),
                         'A \\| B comparison without a final full stop')


if __name__ == '__main__':
    unittest.main()
