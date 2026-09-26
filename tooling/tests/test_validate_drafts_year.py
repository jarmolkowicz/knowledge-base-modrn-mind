"""Regression checks for explicit proof/publication-year evidence records."""
import copy
import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_drafts as validator


class PublicationYearTests(unittest.TestCase):
    def setUp(self):
        self.workbench = validator.KB_ROOT / "raw" / "test-proof-2015"
        self.record = {
            "year": 2015,
            "publication_year_verification": {
                "year": 2015, "reason": "2014 proof, 2015 publication",
                "reviewed_by": "librarian", "verified_at": "2026-09-26",
                "evidence_file": "raw/test-reference/source.md",
                "evidence_quote": "Author (2015). Test title.",
            },
        }
        self.drafts = {self.workbench.name: SimpleNamespace(sources=["Author (2015). Test title."])}

    def check(self, meta=None, evidence="Author (2015).\nTest title.", drafts=None):
        meta = self.record if meta is None else meta
        def read(path, **kwargs):
            return json.dumps(meta) if path.name == "source.json" else evidence
        with patch.object(Path, "read_text", read), patch.object(Path, "is_file", return_value=True):
            return validator.has_verified_publication_year(
                self.workbench, "2015", self.drafts if drafts is None else drafts
            )

    def test_evidence_record_accepts_whitespace_normalization(self):
        self.assertTrue(self.check())

    def test_bare_year_does_not_override(self):
        self.assertFalse(self.check({"year": 2015}))

    def test_wrong_record_year_rejected(self):
        meta = copy.deepcopy(self.record)
        meta["publication_year_verification"]["year"] = 2014
        self.assertFalse(self.check(meta))

    def test_unmatched_quote_rejected(self):
        self.assertFalse(self.check(evidence="A different citation (2015)."))

    def test_missing_draft_citation_rejected(self):
        self.assertFalse(self.check(drafts={}))

    def test_missing_review_reason_rejected(self):
        meta = copy.deepcopy(self.record)
        meta["publication_year_verification"]["reason"] = ""
        self.assertFalse(self.check(meta))

    def test_path_outside_repo_rejected(self):
        meta = copy.deepcopy(self.record)
        meta["publication_year_verification"]["evidence_file"] = "../outside.md"
        self.assertFalse(self.check(meta))

    def test_malformed_record_rejected(self):
        self.assertFalse(self.check({"publication_year_verification": []}))


if __name__ == "__main__":
    unittest.main()
