# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml"]
# ///
"""Build a conservative local pre-screen of the entire Practical collection.

This is retrieval assistance, not a credibility assessment or an inclusion decision.
No source is rejected automatically. Keyword misses remain open for manual screening.
Full source text is scanned locally; only metadata, flags and locators are saved.
"""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml

ROOT = Path(__file__).resolve().parents[2]
INBOX = ROOT / "raw/inbox/Practical"
OUT = ROOT / "raw/practitioner-practices-development/screening"
AI = re.compile(r"\b(?:AI|LLMs?|ChatGPT|GPT[- ]?[3456]|Claude|Copilot|Gemini|artificial intelligence|language models?)\b", re.I)
ACTION = re.compile(r"\b(?:ask|prompt|instruct|compare|check|test|evaluate|question|challenge|explain|revise|draft|write|choose|decide|reflect|practi[cs]e|rehearse|simulate|verify|try)\b", re.I)
PROCEDURE = re.compile(r"(?:^\s*\d+[.)]\s|\bstep[- ]by[- ]step\b|\b(?:first|then|next|finally)\b|\b(?:prompt|exercise|routine|checklist|workflow|protocol)\b)", re.I | re.M)
HUMAN_WORK = re.compile(r"\b(?:learn\w*|think\w*|reason\w*|judg\w*|creativ\w*|decis\w*|writ\w*|skill\w*|understand\w*|design\w*|feedback|critique|ownership|agency|argument\w*|assumption\w*|research\w*|reflect\w*)\b", re.I)
PERSONAL = re.compile(r"\b(?:I|we|my team)\s+(?:use|used|ask|asked|built|created|tried|tested|found|learned|noticed|started|do|did)\b", re.I)
LIMIT = re.compile(r"\b(?:fail\w*|limit\w*|mistake\w*|wrong|doesn.t work|didn.t work|disagree\w*|reject\w*|caution\w*)\b", re.I)


def metadata(text: str) -> tuple[dict, str, int]:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        return {}, text, 0
    try:
        value = yaml.safe_load(match[1])
        return value if isinstance(value, dict) else {}, text[match.end():], match.end()
    except yaml.YAMLError:
        return {"metadata_warning": "frontmatter needs inspection"}, text, 0


def candidates() -> list[tuple[Path, str, str]]:
    result = []
    for folder in sorted(INBOX.iterdir()):
        if not folder.is_dir() or folder.name in {"_refresh", "Lenny's Podcast", "Slow AI", "The Borrowed Mind"}:
            continue
        for path in sorted(folder.glob("*.md")):
            if path.name.startswith("download") or path.name == "extracted-practices.md":
                continue
            result.append((path, folder.name, "internal_working_document" if folder.name == "Modrn Mind" else "article"))
        for path in sorted(folder.glob("*.pdf")):
            result.append((path, folder.name, "unextracted_pdf"))
    for path in sorted((INBOX / "Lenny's Podcast/repo/episodes").glob("*/transcript.md")):
        result.append((path, "Lenny's Podcast", "transcript"))
    for path in sorted((INBOX / "Lenny's Podcast/episode-notes").glob("*.md")):
        result.append((path, "Lenny's Podcast", "episode_notes"))
    for slug, collection in [("illingworth-slow-ai-2026", "Slow AI (book)"), ("nosta-borrowed-mind-2026", "The Borrowed Mind (book)")]:
        result.append((ROOT / "raw" / slug / "source.md", collection, "book"))
    return result


def scan(path: Path, collection: str, kind: str) -> dict:
    record = {"path": path.relative_to(ROOT).as_posix(), "collection": collection, "kind": kind,
              "assessment": "automated_navigation_only", "review_decision": "pending",
              "credibility": "not_assessed", "outcomes": "not_coded"}
    if kind == "unextracted_pdf":
        return dict(record, title=path.stem, route="needs_text", access="not_extracted", reason="Extract the PDF before content screening.")
    text = path.read_text(encoding="utf-8-sig")
    meta, body, offset = metadata(text)
    heading = re.search(r"^#\s+(.+)", body, re.M)
    record.update(title=str(meta.get("title") or (heading[1] if heading else collection)),
                  date=str(meta.get("date") or meta.get("publish_date") or ""),
                  url=meta.get("url") or meta.get("youtube_url") or "",
                  access=meta.get("access") or ("local_full_book" if kind == "book" else "extent_not_verified"),
                  words=len(body.split()), sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  body_sha256=hashlib.sha256(re.sub(r"\s+", " ", body).encode()).hexdigest())
    if meta.get("metadata_warning"):
        record["metadata_warning"] = meta["metadata_warning"]
    hits = []
    # Search every part of the body, including incidental practices in broad interviews.
    # Nearby words are navigation cues; co-occurrence is not proof of a useful practice.
    for hit in AI.finditer(body):
        start, end = max(0, hit.start() - 500), min(len(body), hit.end() + 850)
        window = body[start:end]
        if len(ACTION.findall(window)) >= 3 and PROCEDURE.search(window) and HUMAN_WORK.search(window):
            if not hits or start > hits[-1]["body_offset"] + 500:
                hits.append({"line": text[:offset + hit.start()].count("\n") + 1,
                             "body_offset": start,
                             "first_person_cue": bool(PERSONAL.search(window)),
                             "limits_cue": bool(LIMIT.search(window))})
    record["candidate_passage_count"] = len(hits)
    record["passage_locators"] = hits[:12]
    record["ai_mention"] = bool(AI.search(body))
    record["general_practice_cue"] = bool(PROCEDURE.search(body) and HUMAN_WORK.search(body) and ACTION.search(body))
    if kind == "internal_working_document":
        record.update(route="internal_input", reason="Keep author-owned working material separate from independent external evidence.")
    elif kind == "episode_notes":
        record.update(route="access_gap", reason="Show notes can nominate an interview, not establish its full practice details.")
    elif "preview" in record["access"] or "restricted" in record["access"]:
        record.update(route="access_gap", reason="Only public/restricted-post text captured; assess available passage and full-text need separately.")
    elif hits:
        record.update(route="practice_passage_candidate", reason="AI, action and procedure cues occur together; inspect located passages before selecting.")
    elif record["general_practice_cue"]:
        record.update(route="possible_background_or_transfer", reason="General practice cues present; relevance to AI use needs human assessment.")
    else:
        record.update(route="needs_manual_screen", reason="No strong cue combination; not a rejection or a claim that no practice exists.")
    return record


def main() -> None:
    published = OUT / "screening-register.json"
    if published.exists() and json.loads(published.read_text(encoding="utf-8")).get("screened_at"):
        raise SystemExit("Reviewed snapshot exists. Create a new inventory snapshot and reconcile decisions by path/hash; do not overwrite the completed screen.")
    records = [scan(*item) for item in candidates()]
    decisions_path = OUT / "reviewed-examples.json"
    decisions = json.loads(decisions_path.read_text(encoding="utf-8")) if decisions_path.exists() else []
    by_path = {d["path"]: d for d in decisions}
    for record in records:
        decision = by_path.get(record["path"])
        if decision and decision["source_sha256"] == record.get("sha256"):
            record["review_decision"] = decision["decision"]
            record["screening_note"] = decision["reason"]
            record["reviewed_locator"] = decision["locator"]
            record["assessment"] = "passage_screened_by_assistant; not inclusion approval"
        elif decision:
            record["screening_note"] = "Earlier decision is stale: source hash changed."
    seen_hash, seen_url = {}, {}
    for record in records:
        duplicate = None
        if record.get("body_sha256") in seen_hash:
            duplicate = seen_hash[record["body_sha256"]]
        elif record.get("url") and record["url"].rstrip("/") in seen_url:
            duplicate = seen_url[record["url"].rstrip("/")]
        if duplicate:
            record["duplicate_candidate_of"] = duplicate
        if record.get("body_sha256"):
            seen_hash.setdefault(record["body_sha256"], record["path"])
        if record.get("url"):
            seen_url.setdefault(record["url"].rstrip("/"), record["path"])
    result = {"created_at": datetime.now(timezone.utc).isoformat(),
              "scope": "all current Practical source items; book derivatives represented by their canonical extracted sources",
              "exclusions": ["download scripts", "refresh backups and HTML snapshots", "podcast repository indexes and documentation", "duplicate book representations and highlights"],
              "method": "Local whole-text cue scan. Routes are provisional navigation, not semantic review or quality scores. No source excluded on content.",
              "counts": dict(Counter(r["route"] for r in records)),
              "collections": dict(Counter(r["collection"] for r in records)),
              "records": records}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "screening-register.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    reviewed = sum(r["review_decision"] != "pending" for r in records)
    lines = ["# Practical source screening register", "", f"Source items: **{len(records)}**. Whole-text navigation scan; **{reviewed}** illustrative passage-screening decisions recorded. Remaining detailed screening is pending.", "", "No outcome taxonomy applied. No source automatically rejected. Author credibility not systematically assessed.", "", "| Provisional route | Count |", "|---|---:|"]
    lines.extend(f"| {key} | {value} |" for key, value in result["counts"].items())
    for collection in result["collections"]:
        lines += ["", "## " + collection, "", "| Source | Type | Access | Navigation route | Screening decision | Candidate locations |", "|---|---|---|---|---|---|"]
        for record in records:
            if record["collection"] != collection:
                continue
            title = record["title"].replace("|", "/").replace("[", "(").replace("]", ")").replace("\n", " ")
            path = quote("../../../" + record["path"], safe="/:")
            locations = ", ".join(str(p["line"]) for p in record.get("passage_locators", [])[:4]) or "—"
            lines.append(f"| [{title}]({path}) | {record['kind']} | {record['access']} | {record['route']} | {record['review_decision']} | {locations} |")
    (OUT / "screening-register.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"items": len(records), "counts": result["counts"], "duplicate_candidates": sum('duplicate_candidate_of' in r for r in records)}, indent=2))


if __name__ == "__main__":
    main()
