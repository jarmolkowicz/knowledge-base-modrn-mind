"""KB Linter — whole-KB health check over the Modern Mind Knowledge Base.

Runs a suite of pure-Python checks over every entry, aggregates findings into
a markdown report written to `dist/lint-report.md`. No LLM calls — fast,
free, deterministic.

## Checks

- broken_wikilinks    — [[links]] pointing to entries that don't exist
- orphans             — entries with zero inbound AND zero outbound wikilinks
                        (sources excluded — they're cited via frontmatter)
- uncited_sources     — source entries not referenced by any concept/method
- missing_related     — entry A mentions entry B's full title in body but
                        doesn't [[link]] to it
- frontmatter         — missing/invalid required fields
- source_json         — per-source raw/<slug>/source.json validity (schema +
                        lifecycle artifacts present for the recorded status)
- slug_format         — sources/<slug>.md slug doesn't end in 4-digit year
- distillation_quality— source dist body too sparse, no Key Passages, or
                        frontmatter citation lacks author names
- missing_workbench   — sources/<slug>.md exists but raw/<slug>/ does not
                        (no per-source audit trail; Pass 2 re-ingestion
                        candidate)

## Usage

    uv run python tooling/scripts/linter.py                  # summary table to stdout (no file)
    uv run python tooling/scripts/linter.py --check orphans  # filter to one check
    uv run python tooling/scripts/linter.py --stdout         # full markdown report to stdout
    uv run python tooling/scripts/linter.py --json           # JSON to stdout (for programmatic use)
    uv run python tooling/scripts/linter.py --out lint.md    # write full report to a file
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict
from datetime import date
from pathlib import Path

# Allow running as a standalone script: add own directory to sys.path so
# `import kb_search` resolves even when there's no package context.
_DIR = Path(__file__).resolve().parent
if str(_DIR) not in sys.path:
    sys.path.insert(0, str(_DIR))

from kb_search import (  # noqa: E402
    KB_ROOT,
    VALID_AREAS,
    VALID_STATUSES,
    Entry,
    load_entries,
)
from lint_checks import (  # noqa: E402
    Finding,
    HAS_AUTHOR_YEAR_RE,
    SLUG_RE,
    check_frontmatter_fields,
    check_slug_against_format,
    find_alias_form_mistakes,
    find_broken_wikilinks,
    find_missing_related,
    normalize_for_match as _normalize,
)
from practice_checks import check_practice


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------


def check_broken_wikilinks(entries: dict[str, Entry]) -> list[Finding]:
    target_pool = set(entries.keys())
    findings: list[Finding] = []
    for stem, entry in entries.items():
        findings.extend(
            find_broken_wikilinks(
                entry.body,
                target_pool,
                entry_label=stem,
                file_hint=Path(entry.path).name,
            )
        )
    return findings


def check_orphans(entries: dict[str, Entry]) -> list[Finding]:
    inbound: dict[str, set[str]] = {}
    for stem, entry in entries.items():
        for link in entry.wikilinks:
            inbound.setdefault(link, set()).add(stem)

    findings: list[Finding] = []
    for stem, entry in entries.items():
        if entry.type == "source":
            continue  # sources are checked separately
        has_in = bool(inbound.get(stem))
        has_out = bool(entry.wikilinks)
        if not has_in and not has_out:
            findings.append(
                Finding(
                    check="orphans",
                    entry=stem,
                    issue="no inbound or outbound wikilinks",
                    fix="add Related section, link from a related entry, or archive",
                )
            )
    return findings


def check_uncited_sources(entries: dict[str, Entry]) -> list[Finding]:
    # Source stems follow `author-topic-year` convention. Concept/framework/
    # practice entries cite them either as [[wikilinks]] or as free-text
    # strings in the `sources:` frontmatter field (e.g. "Risko & Gilbert (2016)").
    # We match both patterns.
    wikilinked_sources: set[str] = set()
    citation_corpus_parts: list[str] = []
    for entry in entries.values():
        if entry.type == "source":
            continue
        wikilinked_sources.update(entry.wikilinks)
        for src in entry.sources:
            citation_corpus_parts.append(_normalize(src))
    citation_corpus = " \n ".join(citation_corpus_parts)

    findings: list[Finding] = []
    for stem, entry in entries.items():
        if entry.type != "source":
            continue
        if stem in wikilinked_sources:
            continue

        parts = stem.split("-")
        year_token = next(
            (p for p in reversed(parts) if p.isdigit() and len(p) == 4), None
        )
        author_token = _normalize(parts[0]) if parts else ""

        cited = False
        if year_token and author_token and len(author_token) >= 3:
            if year_token in citation_corpus and author_token in citation_corpus:
                cited = True

        if not cited:
            findings.append(
                Finding(
                    check="uncited_sources",
                    entry=stem,
                    issue="source not referenced via [[wikilink]] or sources: frontmatter",
                    fix=f"cite in a relevant entry's sources field, add [[{stem}]] wikilink, or archive",
                )
            )
    return findings


def check_missing_related(entries: dict[str, Entry]) -> list[Finding]:
    # Only match full multi-word titles to avoid false positives on short words.
    title_to_stem: dict[str, str] = {}
    for stem, entry in entries.items():
        if entry.type == "source":
            continue
        title = entry.title.strip()
        if len(title.split()) < 2:
            continue
        title_to_stem[title.lower()] = stem

    findings: list[Finding] = []
    for stem, entry in entries.items():
        findings.extend(
            find_missing_related(
                entry.body,
                set(entry.wikilinks),
                title_to_stem,
                entry_label=stem,
                self_stem=stem,
            )
        )
    return findings


def check_frontmatter(entries: dict[str, Entry]) -> list[Finding]:
    findings: list[Finding] = []
    valid_statuses = set(VALID_STATUSES)
    valid_areas = set(VALID_AREAS)
    for stem, entry in entries.items():
        findings.extend(
            check_frontmatter_fields(
                entry_label=stem,
                entry_type=entry.type,
                status=entry.status,
                area=entry.area,
                sources=entry.sources,
                valid_statuses=valid_statuses,
                valid_areas=valid_areas,
            )
        )
    return findings


VALID_SOURCE_STATUSES = {
    "cataloged", "triaged", "drafted", "critiqued", "validated",
    "integrated", "skipped", "deferred", "escalated_validation",
}
VALID_SOURCE_TYPES = {
    "paper", "book", "article", "report", "transcript", "unknown"
}
VALID_SOURCE_FORMATS = {"pdf", "docx", "epub", "pptx", "md", "txt"}
REQUIRED_SOURCE_FIELDS = {
    "slug", "original_filename", "format", "source_type",
    "hash", "extractor", "status", "ingested_at", "decisions",
}


def check_source_json(_: dict[str, Entry]) -> list[Finding]:
    """Validate every raw/<slug>/source.json against the schema and
    confirm that lifecycle artifacts match the recorded status."""
    findings: list[Finding] = []
    raw_root = KB_ROOT / "raw"
    if not raw_root.is_dir():
        return findings

    for source_json in raw_root.glob("*/source.json"):
        slug_dir = source_json.parent
        slug = slug_dir.name
        # `inbox` and the legacy `processing/papers/articles/...` aren't per-source dirs
        if slug in {"inbox", "processing", "papers", "articles", "books", "transcripts", "decks", "other"}:
            continue
        try:
            data = json.loads(source_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            findings.append(Finding(
                check="source_json",
                entry=slug,
                issue=f"source.json is invalid JSON: {e}",
                fix="repair the JSON or re-run extract.py --force",
            ))
            continue

        for field in REQUIRED_SOURCE_FIELDS:
            if field not in data:
                findings.append(Finding(
                    check="source_json",
                    entry=slug,
                    issue=f"missing required field: {field}",
                    fix="re-run extract.py --force, or hand-edit if backfilling a legacy source",
                ))

        status = data.get("status")
        if status and status not in VALID_SOURCE_STATUSES:
            findings.append(Finding(
                check="source_json",
                entry=slug,
                issue=f"invalid status: {status!r}",
                fix=f"set status to one of {sorted(VALID_SOURCE_STATUSES)}",
            ))

        st = data.get("source_type")
        if st and st not in VALID_SOURCE_TYPES:
            findings.append(Finding(
                check="source_json",
                entry=slug,
                issue=f"invalid source_type: {st!r}",
                fix=f"set source_type to one of {sorted(VALID_SOURCE_TYPES)}",
            ))

        fmt = data.get("format")
        if fmt and fmt not in VALID_SOURCE_FORMATS:
            findings.append(Finding(
                check="source_json",
                entry=slug,
                issue=f"invalid format: {fmt!r}",
                fix=f"set format to one of {sorted(VALID_SOURCE_FORMATS)}",
            ))

        # Backfilled sources skip the triage/distill/critique artifact check —
        # they were ingested before the new pipeline existed and the audit
        # trail is permanently incomplete by design. Two backfill paths:
        # - structurally_backfilled: Pass 1 mass-migration of legacy raw/<type>/
        # - workbench_backfilled: Pass 1 gap-fill of sources that lacked raw/<slug>/
        decisions = data.get("decisions") or []
        is_backfilled = any(
            (d.get("outcome") or "").startswith(("structurally_backfilled", "workbench_backfilled"))
            for d in decisions
        )
        if is_backfilled:
            required_artifacts = {"integrated": ["source.md", "log.md"]}
        else:
            required_artifacts = {
                "cataloged":             ["source.md", "log.md"],
                "triaged":               ["source.md", "log.md", "triage.md"],
                "drafted":               ["source.md", "log.md", "triage.md", "distill.md"],
                "critiqued":             ["source.md", "log.md", "triage.md", "distill.md", "critique.md"],
                "validated":             ["source.md", "log.md", "triage.md", "distill.md"],
                "escalated_validation":  ["source.md", "log.md", "triage.md", "distill.md"],
                "integrated":            ["source.md", "log.md", "triage.md", "distill.md"],
                "skipped":               ["source.md", "log.md", "triage.md"],
                "deferred":              ["source.md", "log.md", "triage.md"],
            }
        for art in required_artifacts.get(status, []):
            if not (slug_dir / art).is_file():
                findings.append(Finding(
                    check="source_json",
                    entry=slug,
                    issue=f"status={status} but {art} is missing",
                    fix=f"either re-run the corresponding stage or correct the status field",
                ))

    return findings


def check_slug_format(entries: dict[str, Entry]) -> list[Finding]:
    """Combines two slug-shape checks: kebab-case-with-year format AND
    advisory institution-prefix detection (mit-, hbr-, pnas-, etc.)."""
    findings: list[Finding] = []
    for stem, entry in entries.items():
        if entry.type != "source":
            continue
        findings.extend(check_slug_against_format(stem))
    return findings


def check_distillation_quality(entries: dict[str, Entry]) -> list[Finding]:
    findings: list[Finding] = []
    for stem, entry in entries.items():
        if entry.type != "source":
            continue
        # 1. Body length: source distillations should be substantive
        word_count = len(re.findall(r"\b\w+\b", entry.body))
        if word_count < 200:
            findings.append(Finding(
                check="distillation_quality",
                entry=stem,
                issue=f"sparse distillation: only {word_count} words in body",
                fix="re-distill via /ingest <slug> to produce a fuller source entry",
            ))
        # 2. Key Passages section presence
        if "key passages" not in entry.body.lower() and "key findings" not in entry.body.lower():
            findings.append(Finding(
                check="distillation_quality",
                entry=stem,
                issue="no 'Key Passages' or 'Key Findings' section",
                fix="re-distill via /ingest <slug> with locator-linked verbatim quotes",
            ))
        # 3. Frontmatter citation has author names (heuristic: not just journal/year)
        # HAS_AUTHOR_YEAR_RE handles Unicode-letter authors (Gašević, Müller, etc.).
        for src_str in entry.sources:
            if not HAS_AUTHOR_YEAR_RE.search(src_str):
                findings.append(Finding(
                    check="distillation_quality",
                    entry=stem,
                    issue=f"vague citation in frontmatter: {src_str!r} (no author + year)",
                    fix="rewrite citation as 'Author(s) (Year). Title. Venue.'",
                ))
                break  # one finding per entry is enough
    return findings


def check_missing_workbench(entries: dict[str, Entry]) -> list[Finding]:
    findings: list[Finding] = []
    raw_root = KB_ROOT / "raw"
    for stem, entry in entries.items():
        if entry.type != "source":
            continue
        if not (raw_root / stem).is_dir():
            findings.append(Finding(
                check="missing_workbench",
                entry=stem,
                issue=f"raw/{stem}/ does not exist",
                fix="re-ingest the source via /ingest, or hand-place the binary and run extract.py",
            ))
    return findings


def check_practices(entries: dict[str, Entry]) -> list[Finding]:
    sources = {stem for stem, entry in entries.items() if entry.type == 'source'}
    return [finding for entry in entries.values() if entry.type == 'practice'
            for finding in check_practice(Path(entry.path).read_text(encoding='utf-8'),
                                          entry.stem, source_stems=sources)]


CHECKS = {
    "practice_schema": check_practices,
    "broken_wikilinks": check_broken_wikilinks,
    "orphans": check_orphans,
    "uncited_sources": check_uncited_sources,
    "missing_related": check_missing_related,
    "frontmatter": check_frontmatter,
    "source_json": check_source_json,
    "slug_format": check_slug_format,
    "distillation_quality": check_distillation_quality,
    "missing_workbench": check_missing_workbench,
}


CHECK_DESCRIPTIONS = {
    "practice_schema": "Practice sections, exact source identities and intended outcomes",
    "broken_wikilinks": "Wikilinks pointing to entries that don't exist",
    "orphans": "Entries with no inbound or outbound wikilinks",
    "uncited_sources": "Source entries not wikilinked from any concept/method",
    "missing_related": "Entries whose body mentions another entry's title without linking",
    "frontmatter": "Missing or invalid required frontmatter fields",
    "source_json": "Per-source source.json schema and lifecycle artifact presence",
    "slug_format": "Source slugs that don't follow <author>-<keyword>-<year>",
    "distillation_quality": "Sparse, citation-incomplete, or unstructured source dists",
    "missing_workbench": "Source dists with no per-source raw/<slug>/ workbench",
}


def run_checks(names: list[str] | None, entries: dict[str, Entry]) -> list[Finding]:
    selected = names or list(CHECKS.keys())
    findings: list[Finding] = []
    for name in selected:
        check_fn = CHECKS[name]
        findings.extend(check_fn(entries))
    return findings


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def render_markdown(findings: list[Finding], total_entries: int, selected: list[str]) -> str:
    by_check: dict[str, list[Finding]] = {name: [] for name in selected}
    for f in findings:
        by_check.setdefault(f.check, []).append(f)

    lines: list[str] = []
    lines.append("# KB Lint Report")
    lines.append("")
    lines.append(f"Generated: {date.today().isoformat()}")
    lines.append(f"Entries scanned: {total_entries}")
    lines.append(f"Total findings: {len(findings)}")
    lines.append("")

    lines.append("## Summary")
    lines.append("")
    lines.append("| Check | Count | Description |")
    lines.append("|---|---:|---|")
    for name in selected:
        count = len(by_check.get(name, []))
        desc = CHECK_DESCRIPTIONS.get(name, "")
        lines.append(f"| {name} | {count} | {desc} |")
    lines.append("")

    for name in selected:
        items = by_check.get(name, [])
        lines.append(f"## {name}  ({len(items)})")
        lines.append("")
        lines.append(f"*{CHECK_DESCRIPTIONS.get(name, '')}*")
        lines.append("")
        if not items:
            lines.append("_No findings._")
            lines.append("")
            continue
        # Group by entry for denser output
        by_entry: dict[str, list[Finding]] = {}
        for f in items:
            by_entry.setdefault(f.entry, []).append(f)
        for entry_stem in sorted(by_entry.keys()):
            lines.append(f"### `{entry_stem}`")
            for f in by_entry[entry_stem]:
                lines.append(f"- **Issue:** {f.issue}")
                if f.fix:
                    lines.append(f"  - Fix: {f.fix}")
            lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="linter",
        description="Run health checks over the Modern Mind KB.",
    )
    parser.add_argument(
        "--check",
        action="append",
        choices=list(CHECKS.keys()),
        help="run only specific checks (repeatable). Default: all.",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="optional path to write the full markdown report to (default: no file written)",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="print full markdown report to stdout (default: summary table only)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit findings as JSON to stdout",
    )
    args = parser.parse_args(argv)

    entries = load_entries()
    selected = args.check or list(CHECKS.keys())
    findings = run_checks(selected, entries)

    if args.json:
        print(json.dumps([asdict(f) for f in findings], indent=2))
        return 0

    report = render_markdown(findings, total_entries=len(entries), selected=selected)

    if args.stdout:
        print(report)
    elif args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report, encoding="utf-8")
        print(f"Wrote {len(findings)} findings across {len(selected)} checks to {out_path}")
    else:
        # Default: print the summary table to stdout. No file written.
        print(f"Lint findings: {len(findings)} across {len(selected)} checks")
        print()
        by_check: dict[str, int] = {name: 0 for name in selected}
        for f in findings:
            by_check[f.check] = by_check.get(f.check, 0) + 1
        width = max(len(n) for n in selected)
        for name in selected:
            print(f"  {name:<{width}}  {by_check.get(name, 0):>4}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
