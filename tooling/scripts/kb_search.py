"""KB Search — lightweight search and inspection over the Modern Mind KB.

Two uses:
1. Python API for pipeline agents (drafter, crossref, future linter) to query
   existing entries without bulk-loading the whole KB into every prompt.
2. CLI tool for interactive exploration from a terminal or Claude Code.

Naive by design: stdlib regex + PyYAML frontmatter parsing. At KB scale
(~200 entries) this is fast enough and easy to reason about. No embeddings,
no indexing, no RAG.

## CLI examples

    uv run python tooling/scripts/kb_search.py search "cognitive offloading"
    uv run python tooling/scripts/kb_search.py search "trust calibration" --type concept --status emerging
    uv run python tooling/scripts/kb_search.py list --status speculative --json
    uv run python tooling/scripts/kb_search.py similar accountability
    uv run python tooling/scripts/kb_search.py get cognitive-offloading
    uv run python tooling/scripts/kb_search.py exists fluency-bias

## Python API

    # When invoked from another script in the same directory:
    #   from kb_search import search, get, find_similar, summarize
    from kb_search import search, get, find_similar, summarize

    hits = search("automation bias", types=["concept"], limit=5)
    for e in hits:
        print(summarize(e))
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable

import yaml

# Resolve KB root from this file's location:
#   <kb_root>/tooling/scripts/kb_search.py  →  parents[2] is <kb_root>
_SELF = Path(__file__).resolve()
KB_ROOT = _SELF.parents[2]

ENTRY_DIRS: dict[str, Path] = {
    "concept": KB_ROOT / "concepts",
    "method": KB_ROOT / "methods",
    "practice": KB_ROOT / "practices",
    "source": KB_ROOT / "sources",
}

VALID_TYPES = tuple(ENTRY_DIRS.keys())
VALID_STATUSES = ("solid", "emerging", "speculative")
VALID_AREAS = ("risk", "erosion", "preservation")


@dataclass
class Entry:
    stem: str
    type: str
    path: str
    status: str | None
    area: list[str]
    sources: list[str]
    title: str
    body: str
    wikilinks: set[str] = field(default_factory=set)
    source_entries: list[str] = field(default_factory=list)

    def to_public_dict(self, include_body: bool = False) -> dict:
        d = asdict(self)
        d["wikilinks"] = sorted(self.wikilinks)
        if not include_body:
            d.pop("body", None)
        return d


_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
_WIKILINK_RE = re.compile(r"\[\[([^\]#|]+)")
_TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def _coerce_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v) for v in value]
    return [str(value)]


def _parse_file(path: Path, entry_type: str) -> Entry | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None

    fm: dict = {}
    body = text
    m = _FRONTMATTER_RE.match(text)
    if m:
        try:
            parsed = yaml.safe_load(m.group(1))
            if isinstance(parsed, dict):
                fm = parsed
        except yaml.YAMLError:
            fm = {}
        body = text[m.end():]

    title_match = _TITLE_RE.search(body)
    title = title_match.group(1).strip() if title_match else path.stem.replace("-", " ").title()

    wikilinks = {mm.group(1).strip() for mm in _WIKILINK_RE.finditer(body)}

    return Entry(
        stem=path.stem,
        type=entry_type,
        path=str(path),
        status=fm.get("status"),
        area=_coerce_list(fm.get("area")),
        sources=_coerce_list(fm.get("sources")),
        title=title,
        body=body,
        wikilinks=wikilinks,
        source_entries=_coerce_list(fm.get("source_entries")),
    )


_CACHE: dict[str, Entry] | None = None


def load_entries(refresh: bool = False) -> dict[str, Entry]:
    """Load all KB entries into a {stem: Entry} dict. Cached per process."""
    global _CACHE
    if _CACHE is not None and not refresh:
        return _CACHE

    entries: dict[str, Entry] = {}
    for etype, dir_path in ENTRY_DIRS.items():
        if not dir_path.exists():
            continue
        for f in sorted(dir_path.glob("*.md")):
            entry = _parse_file(f, etype)
            if entry:
                if entry.stem in entries:
                    raise ValueError(f'Duplicate KB slug {entry.stem}: {entries[entry.stem].path} and {entry.path}')
                entries[entry.stem] = entry
    _CACHE = entries
    return entries


def _score(entry: Entry, terms: list[str]) -> float:
    """Heuristic relevance score. Stem > title > body. Caps body count per term."""
    if not terms:
        return 1.0
    stem_lc = entry.stem.lower()
    title_lc = entry.title.lower()
    body_lc = entry.body.lower()
    score = 0.0
    for term in terms:
        t = term.lower()
        if len(t) < 2:
            continue
        if t in stem_lc:
            score += 5.0
        if t in title_lc:
            score += 3.0
        body_count = body_lc.count(t)
        if body_count:
            score += min(body_count, 10) * 0.5
    return score


def search(
    query: str,
    types: Iterable[str] | None = None,
    status: str | None = None,
    area: str | None = None,
    limit: int = 20,
) -> list[Entry]:
    """Full-text search with frontmatter filters. Returns scored, sorted entries.

    Empty query with filters acts as a list-and-filter operation.
    """
    entries = load_entries()
    terms = [t for t in re.split(r"\W+", query.strip()) if t]
    types_set = set(types) if types else None

    results: list[tuple[float, Entry]] = []
    for entry in entries.values():
        if types_set and entry.type not in types_set:
            continue
        if status and entry.status != status:
            continue
        if area and area not in entry.area:
            continue
        score = _score(entry, terms)
        if score > 0:
            results.append((score, entry))

    results.sort(key=lambda x: (-x[0], x[1].stem))
    return [e for _, e in results[:limit]]


def exists(name: str) -> bool:
    """True if an entry with this stem exists."""
    return name in load_entries()


def get(name: str) -> Entry | None:
    """Fetch full entry by stem, or None."""
    return load_entries().get(name)


def find_similar(name: str, limit: int = 10) -> list[Entry]:
    """Entries that share wikilinks (or are linked by) the given entry.

    Jaccard-ish over the union of (entry's links ∪ the entry name itself)
    — so an entry linked directly to `name` also scores high.
    """
    entries = load_entries()
    target = entries.get(name)
    if not target:
        return []

    target_set = target.wikilinks | {name}
    scored: list[tuple[float, Entry]] = []
    for stem, entry in entries.items():
        if stem == name:
            continue
        other_set = entry.wikilinks | {stem}
        shared = target_set & other_set
        if not shared:
            continue
        union = target_set | other_set
        score = len(shared) / len(union)
        scored.append((score, entry))

    scored.sort(key=lambda x: (-x[0], x[1].stem))
    return [e for _, e in scored[:limit]]


def summarize(entry: Entry, body_chars: int = 500) -> dict:
    """Compact dict for embedding in LLM prompts."""
    snippet = re.sub(r"\n{3,}", "\n\n", entry.body.strip())
    if len(snippet) > body_chars:
        snippet = snippet[:body_chars].rstrip() + "..."
    return {
        "stem": entry.stem,
        "type": entry.type,
        "title": entry.title,
        "status": entry.status,
        "area": entry.area,
        "snippet": snippet,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _print_results(results: list[Entry], as_json: bool, include_body: bool = False) -> None:
    if as_json:
        data = [e.to_public_dict(include_body=include_body) for e in results]
        print(json.dumps(data, indent=2, default=str))
        return
    if not results:
        print("(no results)", file=sys.stderr)
        return
    for e in results:
        area = ",".join(e.area) if e.area else "-"
        badge = f"[{e.type}/{e.status or '?'}]"
        print(f"{badge:<22} {e.stem}")
        print(f"   {e.title}   area={area}")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="kb_search",
        description="Search and inspect the Modern Mind Knowledge Base.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    def _add_filters(p: argparse.ArgumentParser) -> None:
        p.add_argument("--type", action="append", dest="types", choices=VALID_TYPES)
        p.add_argument("--status", choices=VALID_STATUSES)
        p.add_argument("--area", choices=VALID_AREAS)

    p_search = sub.add_parser("search", help="full-text search with filters")
    p_search.add_argument("query", nargs="+", help="search terms")
    _add_filters(p_search)
    p_search.add_argument("--limit", type=int, default=20)
    p_search.add_argument("--json", action="store_true")
    p_search.add_argument("--full", action="store_true", help="include body in JSON output")

    p_list = sub.add_parser("list", help="list all entries, optionally filtered")
    _add_filters(p_list)
    p_list.add_argument("--limit", type=int, default=10000)
    p_list.add_argument("--json", action="store_true")

    p_exists = sub.add_parser("exists", help="check if an entry exists (exits 0/1)")
    p_exists.add_argument("name")

    p_get = sub.add_parser("get", help="print full entry content")
    p_get.add_argument("name")
    p_get.add_argument("--json", action="store_true")

    p_sim = sub.add_parser("similar", help="find entries sharing wikilinks")
    p_sim.add_argument("name")
    p_sim.add_argument("--limit", type=int, default=10)
    p_sim.add_argument("--json", action="store_true")

    p_stats = sub.add_parser("stats", help="print KB counts by type and status")
    p_stats.add_argument("--json", action="store_true")

    return parser


def _cmd_stats(as_json: bool) -> None:
    entries = load_entries()
    by_type: dict[str, int] = {}
    by_status: dict[str, int] = {}
    by_area: dict[str, int] = {}
    for e in entries.values():
        by_type[e.type] = by_type.get(e.type, 0) + 1
        by_status[e.status or "unset"] = by_status.get(e.status or "unset", 0) + 1
        for a in e.area or ["unset"]:
            by_area[a] = by_area.get(a, 0) + 1
    stats = {
        "total": len(entries),
        "by_type": by_type,
        "by_status": by_status,
        "by_area": by_area,
        "kb_root": str(KB_ROOT),
    }
    if as_json:
        print(json.dumps(stats, indent=2))
        return
    print(f"Total entries: {stats['total']}    (root: {KB_ROOT})")
    for section, label in [("by_type", "Types"), ("by_status", "Status"), ("by_area", "Area")]:
        print(f"\n{label}:")
        for k, v in sorted(stats[section].items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"  {k:<14} {v}")


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.cmd == "search":
        query = " ".join(args.query)
        results = search(
            query,
            types=args.types,
            status=args.status,
            area=args.area,
            limit=args.limit,
        )
        _print_results(results, args.json, include_body=args.full)
        return 0

    if args.cmd == "list":
        results = search(
            "",
            types=args.types,
            status=args.status,
            area=args.area,
            limit=args.limit,
        )
        _print_results(results, args.json)
        return 0

    if args.cmd == "exists":
        found = exists(args.name)
        print("yes" if found else "no")
        return 0 if found else 1

    if args.cmd == "get":
        e = get(args.name)
        if not e:
            print(f"not found: {args.name}", file=sys.stderr)
            return 1
        if args.json:
            print(json.dumps(e.to_public_dict(include_body=True), indent=2, default=str))
        else:
            print(Path(e.path).read_text(encoding="utf-8"))
        return 0

    if args.cmd == "similar":
        results = find_similar(args.name, limit=args.limit)
        if not results and not exists(args.name):
            print(f"not found: {args.name}", file=sys.stderr)
            return 1
        _print_results(results, args.json)
        return 0

    if args.cmd == "stats":
        _cmd_stats(args.json)
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
