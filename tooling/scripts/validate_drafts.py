"""Pre-integrate validation gate for the librarian's Stage 4.5.

Runs purely-mechanical checks on the contents of `raw/<slug>/drafts/` BEFORE
those drafts are moved into the KB. Catches the recurring class of mistakes
that bit us 1-3 times per pilot ingest:

- Broken wikilinks (typos, references to renamed slugs)
- Backwards alias-form `[[old|new]]` where old doesn't exist but new does
- Body mentions of existing concept titles without [[wikilinks]] to them
- Slug-year vs. citation-year mismatch (e.g. slug ends -2026 but page 1
  of source.md says "(2025)")
- Source distillation missing a `## Key Passages` or `## Key Findings` section
- Frontmatter status/area/sources sanity

Reuses helpers from `lint_checks.py` so logic is shared with `linter.py`.

Exit code: 0 if clean, 1 if findings (for CI / scripts).

## Usage

    uv run python tooling/scripts/validate_drafts.py raw/<slug>/
    uv run python tooling/scripts/validate_drafts.py raw/<slug>/ --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict
from datetime import date
from pathlib import Path

# Allow standalone-script invocation.
_DIR = Path(__file__).resolve().parent
if str(_DIR) not in sys.path:
    sys.path.insert(0, str(_DIR))

from kb_search import (  # noqa: E402
    KB_ROOT,
    VALID_AREAS,
    VALID_STATUSES,
    Entry,
    _parse_file,
    load_entries,
)
from lint_checks import (  # noqa: E402
    Finding,
    SLUG_RE,
    check_frontmatter_fields,
    extract_wikilinks,
    find_alias_form_mistakes,
    find_broken_wikilinks,
    find_missing_related,
)


CHECK_DESCRIPTIONS: dict[str, str] = {
    "broken_wikilinks": "Wikilinks pointing to entries that don't exist",
    "alias_form": "Backwards [[old|new]] where old doesn't exist as a slug",
    "missing_related": "Drafts whose body mentions another KB entry's title without linking",
    "frontmatter": "Missing or invalid required frontmatter fields",
    "slug_year_mismatch": "Slug year doesn't match year in citation/source.md first page",
    "key_passages_missing": "Source distillation lacks a Key Passages or Key Findings section",
}


# ---------------------------------------------------------------------------
# Loading drafts
# ---------------------------------------------------------------------------


def load_draft_entries(workbench_dir: Path) -> dict[str, Entry]:
    """Parse the draft files in raw/<slug>/drafts/ as Entry objects, keyed by
    a synthetic stem that represents what the slug WILL be once integrated.

    For:
      drafts/source.md          -> stem = workbench dir name (the source slug)
      drafts/concepts/*.md      -> stem = file stem (the concept slug)
      drafts/methods/*.md       -> stem = file stem (the method slug)
      drafts/updates/*.md       -> stem = file stem (the existing entry being updated)
    """
    drafts_dir = workbench_dir / "drafts"
    if not drafts_dir.is_dir():
        return {}

    out: dict[str, Entry] = {}

    # Source distillation
    source_md = drafts_dir / "source.md"
    if source_md.is_file():
        e = _parse_file(source_md, "source")
        if e is not None:
            # Override stem to be the workbench slug (source distillation will
            # land at sources/<slug>.md).
            e.stem = workbench_dir.name
            out[workbench_dir.name] = e

    # New concept drafts
    for p in sorted((drafts_dir / "concepts").glob("*.md")):
        e = _parse_file(p, "concept")
        if e is not None:
            out[p.stem] = e

    # New method drafts
    for p in sorted((drafts_dir / "methods").glob("*.md")):
        e = _parse_file(p, "method")
        if e is not None:
            out[p.stem] = e

    # Update proposals — these target an existing entry, so the stem is the
    # existing entry's slug. We treat them as drafts for wikilink checking
    # but don't add them to the "new entries" pool (they don't create new
    # slugs).
    for p in sorted((drafts_dir / "updates").glob("*.md")):
        e = _parse_file(p, "update")
        if e is not None:
            out[f"update:{p.stem}"] = e

    return out


# ---------------------------------------------------------------------------
# Draft-specific checks (the ones not covered by reused helpers)
# ---------------------------------------------------------------------------


_YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")


def has_verified_publication_year(
    workbench_dir: Path, slug_year: str, drafts: dict[str, Entry]
) -> bool:
    """Accept a reviewed proof/publication-year distinction, never a bare override.

    source.json must name a local evidence file and an exact supporting passage.
    The year must also occur in the source draft's citation. The reviewer owns
    the bibliographic judgment; this function checks the recorded evidence.
    """
    try:
        meta = json.loads((workbench_dir / "source.json").read_text(encoding="utf-8-sig"))
        record = meta.get("publication_year_verification", {})
        if not isinstance(record, dict):
            return False
        if str(record.get("year")) != slug_year or str(meta.get("year")) != slug_year:
            return False
        if not all(isinstance(record.get(k), str) and record[k].strip()
                   for k in ("reason", "reviewed_by", "verified_at", "evidence_file", "evidence_quote")):
            return False
        evidence = (KB_ROOT / record["evidence_file"]).resolve()
        if not evidence.is_relative_to(KB_ROOT.resolve()) or not evidence.is_file():
            return False
        normalize = lambda text: " ".join(text.split())
        quote = normalize(record["evidence_quote"])
        if not re.search(rf"\b{re.escape(slug_year)}\b", quote):
            return False
        if quote not in normalize(evidence.read_text(encoding="utf-8-sig")):
            return False
        source = drafts.get(workbench_dir.name)
        return source is not None and any(
            re.search(rf"\b{re.escape(slug_year)}\b", citation)
            for citation in source.sources
        )
    except (OSError, ValueError, TypeError, AttributeError):
        return False


def check_slug_year_match(workbench_dir: Path, drafts: dict[str, Entry]) -> list[Finding]:
    """Compare the year suffix in the workbench slug to years that appear on
    the first page of source.md (the original extracted text). A mismatch is
    a soft flag — papers can have multiple years (received/accepted/published),
    so we only flag when the slug-year doesn't appear at all in the first
    page's year set.
    """
    findings: list[Finding] = []
    slug = workbench_dir.name
    m = re.search(r"-(19|20)\d{2}$", slug)
    if not m:
        return findings  # slug has no trailing year; not our problem here
    slug_year = m.group(0)[1:]  # strip leading hyphen

    source_md = workbench_dir / "source.md"
    if not source_md.is_file():
        return findings  # nothing to compare against

    # Read the first page (or the first ~3000 chars if no [p.N] markers exist)
    text = source_md.read_text(encoding="utf-8", errors="replace")
    first_page_match = re.search(r"\[p\.1\](.*?)(?=\[p\.2\]|\Z)", text, re.DOTALL)
    first_page = first_page_match.group(1) if first_page_match else text[:3000]

    found_years = set(re.findall(r"\b(19|20)\d{2}\b", first_page))
    found_years = {f"{y[0:2]}{y[2:4]}" if len(y) == 4 else y for y in re.findall(r"\b(?:19|20)\d{2}\b", first_page)}

    if slug_year not in found_years and found_years:
        if has_verified_publication_year(workbench_dir, slug_year, drafts):
            return findings
        findings.append(
            Finding(
                check="slug_year_mismatch",
                entry=slug,
                issue=(
                    f"slug ends in -{slug_year} but source.md page 1 mentions years "
                    f"{sorted(found_years)} only — none of which match. "
                    f"Likely the slug year is wrong."
                ),
                fix=(
                    f"check the source's actual publication year. If correct, rename "
                    f"the workbench dir + update source.json: slug to use the right year."
                ),
            )
        )

    return findings


def check_key_passages(drafts: dict[str, Entry], workbench_slug: str) -> list[Finding]:
    """The source distillation draft (drafts/source.md → sources/<slug>.md)
    should always have a Key Passages or Key Findings section. Concept and
    method drafts don't need one."""
    findings: list[Finding] = []
    src = drafts.get(workbench_slug)
    if src is None:
        return findings  # no source distillation in drafts (e.g., SKIP source)
    body_lc = src.body.lower()
    if "key passages" not in body_lc and "key findings" not in body_lc:
        findings.append(
            Finding(
                check="key_passages_missing",
                entry=workbench_slug,
                issue="source distillation lacks a 'Key Passages' or 'Key Findings' section",
                fix="add a ## Key Passages section with locator-anchored verbatim quotes from source.md",
            )
        )
    return findings


# ---------------------------------------------------------------------------
# Main validation orchestration
# ---------------------------------------------------------------------------


def validate(workbench_dir: Path) -> list[Finding]:
    workbench_dir = workbench_dir.resolve()
    if not workbench_dir.is_dir():
        return [
            Finding(
                check="key_passages_missing",
                entry=workbench_dir.name,
                issue=f"workbench directory {workbench_dir} does not exist",
                fix="check the path",
            )
        ]

    findings: list[Finding] = []
    workbench_slug = workbench_dir.name

    # Load existing KB to use as the wikilink target pool.
    kb_entries = load_entries()
    drafts = load_draft_entries(workbench_dir)

    # Target pool = existing KB entries + slugs that THIS ingest will create.
    # Update slugs (update:foo) target the existing entry, not a new slug.
    target_pool: set[str] = set(kb_entries.keys())
    for stem in drafts:
        if stem.startswith("update:"):
            continue
        target_pool.add(stem)

    # title → stem map for missing-related, drawn from the existing KB only
    # (no point flagging mentions of NEW concepts in the draft itself).
    title_to_stem: dict[str, str] = {}
    for stem, entry in kb_entries.items():
        if entry.type == "source":
            continue
        title = entry.title.strip()
        if len(title.split()) < 2:
            continue
        title_to_stem[title.lower()] = stem

    valid_statuses = set(VALID_STATUSES)
    valid_areas = set(VALID_AREAS)

    for stem, entry in drafts.items():
        is_update = stem.startswith("update:")
        label = stem if not is_update else stem  # keep the "update:" prefix in the report

        # Wikilink resolution
        findings.extend(
            find_broken_wikilinks(
                entry.body,
                target_pool,
                entry_label=label,
                file_hint=str(Path(entry.path).relative_to(KB_ROOT)),
            )
        )
        # Alias-form sanity (catch [[old|new]] backwards mistakes)
        findings.extend(
            find_alias_form_mistakes(
                entry.body,
                target_pool,
                entry_label=label,
            )
        )
        # Body-vs-Related drift (only for non-update drafts; updates target a
        # specific entry and are deliberately scoped)
        if not is_update:
            self_stem = stem if stem in target_pool else None
            findings.extend(
                find_missing_related(
                    entry.body,
                    set(extract_wikilinks(entry.body)),
                    title_to_stem,
                    entry_label=label,
                    self_stem=self_stem,
                )
            )
        # Frontmatter — only for entries that will land in concepts/, methods/,
        # sources/. Update proposals don't need full frontmatter validation.
        if not is_update:
            entry_type = entry.type
            findings.extend(
                check_frontmatter_fields(
                    entry_label=label,
                    entry_type=entry_type,
                    status=entry.status,
                    area=entry.area,
                    sources=entry.sources,
                    valid_statuses=valid_statuses,
                    valid_areas=valid_areas,
                )
            )

    # Slug-year sanity (workbench-level, not per-draft)
    findings.extend(check_slug_year_match(workbench_dir, drafts))

    # Key Passages presence in source distillation
    findings.extend(check_key_passages(drafts, workbench_slug))

    return findings


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def render_markdown(workbench: Path, findings: list[Finding]) -> str:
    by_check: dict[str, list[Finding]] = {}
    for f in findings:
        by_check.setdefault(f.check, []).append(f)

    lines: list[str] = []
    lines.append(f"# Pre-Integrate Validation: `{workbench.name}`")
    lines.append("")
    lines.append(f"Generated: {date.today().isoformat()}")
    lines.append(f"Workbench: `{workbench}`")
    lines.append(f"Total findings: {len(findings)}")
    lines.append("")

    if not findings:
        lines.append("**Status: READY** — no findings; safe to proceed to Stage 5 integrate.")
        lines.append("")
        return "\n".join(lines)

    lines.append("**Status: BLOCKED** — fix findings in the drafts before integrate.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Check | Count | Description |")
    lines.append("|---|---:|---|")
    for name in sorted(by_check.keys()):
        desc = CHECK_DESCRIPTIONS.get(name, "")
        lines.append(f"| {name} | {len(by_check[name])} | {desc} |")
    lines.append("")

    for name in sorted(by_check.keys()):
        items = by_check[name]
        lines.append(f"## {name} ({len(items)})")
        lines.append("")
        lines.append(f"*{CHECK_DESCRIPTIONS.get(name, '')}*")
        lines.append("")
        by_entry: dict[str, list[Finding]] = {}
        for f in items:
            by_entry.setdefault(f.entry, []).append(f)
        for entry_label in sorted(by_entry.keys()):
            lines.append(f"### `{entry_label}`")
            for f in by_entry[entry_label]:
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
        prog="validate_drafts",
        description="Pre-integrate validation gate for librarian Stage 4.5.",
    )
    parser.add_argument(
        "workbench",
        type=Path,
        help="path to raw/<slug>/ workbench dir to validate",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit findings as JSON to stdout",
    )
    parser.add_argument(
        "--exit-zero",
        action="store_true",
        help="always exit 0, even if findings exist (for non-blocking advisory mode)",
    )
    args = parser.parse_args(argv)

    findings = validate(args.workbench)

    if args.json:
        print(json.dumps([asdict(f) for f in findings], indent=2))
    else:
        print(render_markdown(args.workbench, findings))

    if args.exit_zero:
        return 0
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
