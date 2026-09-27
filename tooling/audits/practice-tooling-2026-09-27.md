# Practice tooling audit — 2026-09-27

**Result:** the collection support is needed, but the implementation had gaps. Sixteen batch-specific scripts did not belong among maintained commands. Nine other batch scripts were already beside their audit records but remained executable. All 25 are now preserved byte-for-byte as `.py.txt` history. Reusable-tool failures below were corrected and covered by tests.

Scope: tooling, workflow and template changes introduced in `76e8aa1`, subsequent practice documentation, and the nine Python helpers in the two practice workbenches. This is a tooling audit, not another assessment of the source claims or taxonomy. No source downloads, canonical-entry edits, pack split or new integration occurred.

## Findings and actions

| Finding | Impact | Action |
|---|---|---|
| `publish_practice_root_review.py` and several raw builders overwrite drafts, critiques, metadata and logs for fixed source IDs. Some execute work on import. | A rerun could replace approved history with pending-review state. | Archived the batch scripts as text with original hashes. No new reusable publisher was invented. |
| `check_integrated_practices.py` calls source-link sync, then updates completion hashes and validation reports. Its original-copy comparisons also predate later approved updates. | A command presented as verification can change what it checks and replace its baseline. | Archived it. Use the read-only current-KB linter and citation checker. Historical validation results remain unchanged. |
| Screening, review publishing, outcome refinement and integration contain fixed IDs, counts, editorial judgments and recorded user authority. | They are not general-purpose ingest tools, even where rerun guards exist. | Removed 16 such scripts from `tooling/scripts/`; archived nine additional batch helpers in place. [Exact mapping and hashes](practice-tooling-archive-2026-09-27.json). |
| Draft validation discovered practices but only applied generic frontmatter/link checks. | A practice without Origin, Limits, or valid outcome metadata could appear structurally ready. | Added shared `practice_checks.py`; wired it into draft validation, whole-KB lint and guide generation. Canonical practices require exact source identities and one primary / at most two secondary outcomes. Drafts may leave those labels unassigned until review. |
| Guide generation checked only the first outcome; its introduction hardcoded category counts and its review link covered only the practitioner batch. | Invalid secondary labels could pass; navigation could become stale after taxonomy/research additions. | Validate every label and source target before writing; remove fixed category counts; link both integration records. |
| `kb_search.load_entries` silently overwrote duplicate stems across collections. | A practice could hide another entry in search and validation. | Fail explicitly on duplicate canonical slugs. |
| Source-link sync passed citation text as a regular-expression replacement string. | Literal backslashes could be interpreted as escapes or cause an exception. | Use a replacement callback. Also scope the librarian's sync command to approved entries. |
| Citation checker counted exact-source-link checks as resolved citation strings. | Its output overstated what was checked. | Report legacy citation matching, exact-source links and unexamined citation strings separately. Claim support and wording-to-identity correspondence remain editorial checks. |
| Refresh reused a directory named only by end date. | Same-day reruns could replace ledgers, mix different windows/selections and retain only the first backup. | Create a separate directory for every invocation; completion status covers that invocation only. This also creates the directory before a notes-only RSS run. |
| Podcast refresh compared upstream only with the original checkout. | It could repeatedly fetch an unchanged refreshed copy, or miss an upstream reversion while retaining stale refreshed text. | Compare against the effective refreshed copy first. Validate episode paths and Windows device-name slugs. |
| The retired screening inventory included repository transcripts but omitted the refresher's `refreshed/` directory. | Future refreshes could be absent from screening. | Retired this fixed-snapshot inventory instead of presenting it as reusable. No refreshed transcript files exist in the audited checkout, so this check found no current omitted transcript to recover. A future inventory must prefer refreshed versions, reconcile paths/hashes and create a new snapshot. |

## What remains needed

| Files | Decision |
|---|---|
| `kb_search.py`, `build-index.py`, `update_readme_counts.py` | Keep practice discovery, separate navigation and counts. Duplicate-slug protection added. |
| `build-bundle.sh`, `.github/workflows/build-kb-bundle.yml` | Keep practice inclusion and counts under the user's decision to leave the combined pack. Compact and full exports tested. Release workflow remains build-and-release; this audit did not run or publish a release. |
| `sync-source-links.py`, `check_citation_links.py`, `citation-aliases.json` | Keep exact source identity support. It avoids ambiguous same-author/year matching; it does not verify evidence. Existing reviewed Mollick book alias retained. |
| `validate_drafts.py`, `linter.py`, `practice_checks.py` | Keep shared draft/canonical structural checks. They do not record approval or integrate content. |
| `build-practice-guide.py`, `practice-outcomes.json` | Keep provisional outcome navigation; outcome labels remain editorial and do not establish efficacy. |
| `templates/practice.md`, `.claude/agents/librarian.md` | Keep the agreed practice structure and recorded-decision workflow; clarify scoped sync and current validation. |
| `refresh_practical.py` | Keep a standalone public-source download helper with explicit window/collection options and per-run ledgers. Not part of testing or integration. |
| Practice/citation tests | Keep existing tests and add failure-oriented regression cases. No tests use live downloads. |
| Sixteen former `tooling/scripts/` batch helpers and nine raw helpers | Historical records only. Preserved unchanged; no longer advertised as runnable tooling. See archive READMEs and manifest. |

## Verification

- Existing suite before changes: **26 passed**.
- Final suite: **41 passed**. New cases cover incomplete practices, canonical-vs-draft requirements, secondary outcome errors, non-source identities, duplicate slugs, literal citation text, truthful check counts, exact archive preservation, repeated refreshes, transcript reversions and both export modes.
- All **83 canonical practices** pass the new practice schema check; guide rebuilt successfully.
- Whole-KB lint reports one existing `missing_related` warning for `keep-one-thinking-step` mentioning “metacognitive laziness” without a `[[metacognitive-laziness]]` link. Its entry body and that check were unchanged by this audit. No canonical edit made.
- All **25 archived scripts** retain their recorded SHA-256 hashes. Historical drafts, decisions, source material and completed validation records were not rewritten.
- All **426 canonical entries** unchanged. The vocabulary and combined-pack build rules are unchanged.
- Final real-KB smoke checks passed: search/stats, all **146 explicit practice source links**, a Gentner workbench draft validation, source-sync dry runs for all practices, README counts, and idempotent index/guide rebuilds. The existing combined pack has **426 unique entry anchors** and all **83 complete practice bodies**.
- Refresh CLI loads successfully; downloads remain mocked in tests. `.gitattributes` disables line-ending conversion for historical `.py.txt` files so archive hashes survive checkout on another platform.

Commands and dependencies are in [tooling/README.md](../README.md). Refresh behavior was tested with mocked requests; current public-site selectors, endpoints and availability were not checked live. Structural tests cannot establish source credibility, routine effectiveness or editorial correctness.
