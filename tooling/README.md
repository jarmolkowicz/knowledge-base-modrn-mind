# KB tooling

Use `uv run python tooling/scripts/<script>.py`. Run from the KB root.
The collection includes concepts, methods, practices and source notes. Pack splitting is not implemented.

## Ongoing practice support

| Tool | Purpose | Writes |
|---|---|---|
| `kb_search.py` | Find entries; detect duplicate slugs across collections | None |
| `linter.py` | Check the current KB, including practice sections, source identities and outcome labels | Only a report when `--out` is supplied |
| `validate_drafts.py` | Check proposed practices before integration | Only a requested report |
| `check_citation_links.py` | Check citation navigation; exact source links and legacy citation matching reported separately | None |
| `sync-source-links.py` | Rebuild source navigation after an approved integration | Canonical entries; use `--entry STEM` to limit scope, `--dry-run` to preview |
| `build-practice-guide.py` | Build navigation from integrated practices and `practice-outcomes.json` | `practice-guide.md` |
| `build-index.py`, `update_readme_counts.py` | Refresh navigation and counts | Index / README |
| `build-bundle.sh` | Export the combined pack | `dist/modern-mind-kb.md`; may refresh README counts |
| `refresh_practical.py` | Download public sources into the local inbox | Inbox, separate per-run ledgers and prior-version copies |

Practice structure comes from [the template](templates/practice.md). Outcome IDs live in [the provisional vocabulary](practice-outcomes.json). Validation checks structure and navigation, not evidence quality. A passing check does not authorize integration.

Refresh has its own dependency declaration. Example:

```sh
uv run --script tooling/scripts/refresh_practical.py --since 2026-09-27 --collections "Sam Illingworth"
```

Only public pages are requested. Run this for an authorized source refresh, not as a validation check. Article/show-note dates use the requested window; podcast transcript refresh follows the complete upstream mirror, as recorded in its ledger.

## Completed batch scripts

The September screening, editorial judgments and integration helpers were one-off scripts. They are retained as `.py.txt` records beside their batches, not maintained commands. Some execute writes on import or reset review status. Do not run them against the current KB.

- [Practitioner batch archive](../raw/practitioner-practices-development/tooling-archive/README.md)
- [Research-source batch archive](../raw/kb-practice-screening-2026-09-27/tooling-archive/README.md)
- [Original locations and exact file hashes](audits/practice-tooling-archive-2026-09-27.json)
- [Audit findings and verification](audits/practice-tooling-2026-09-27.md)

For another batch, create a new workbench and follow the librarian workflow. Reconcile source identity using paths and hashes; old numeric screening IDs and author/year guesses are not reusable identifiers.

## Tests

```sh
uv run --with httpx --with beautifulsoup4 --with markdownify python -m unittest discover -s tooling/tests -v
uv run python tooling/scripts/linter.py --check practice_schema --json
```

Refresh tests use saved fixtures and mocked requests. They do not download sources or write canonical entries.
