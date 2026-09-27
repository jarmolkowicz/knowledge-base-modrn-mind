# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx", "beautifulsoup4", "markdownify"]
# ///
"""Refresh public Practical-inbox articles; keep prior files and a download ledger.

Run with uv run --script tooling/scripts/refresh_practical.py --since YYYY-MM-DD.
No authentication, uploads, paywall bypass, media downloads, or KB integration.
The date window is explicit. A public preview is never labelled a complete article.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import hashlib
import json
from pathlib import Path
import re
import time
import tempfile
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
import httpx
from markdownify import markdownify

ROOT = Path(__file__).resolve().parents[2]
INBOX = ROOT / "raw/inbox/Practical"
PUBLICATIONS = {
    "Adam Grant": "https://adamgrant.substack.com",
    "Ethan Mollick": "https://www.oneusefulthing.org",
    "Nate B Jones": "https://natesnewsletter.substack.com",
    "Ruben Hassid": "https://ruben.substack.com",
    "Sabrina Ramonov": "https://www.sabrina.dev",
    "Sam Illingworth": "https://theslowai.substack.com",
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_slug(value: str) -> str:
    value = re.sub(r"[^a-z0-9-]+", "-", value.lower()).strip("-")[:150]
    if not value or value in {"agents", "claude", "readme", "con", "prn", "aux", "nul"} or re.fullmatch(r'(com|lpt)[1-9]', value):
        value = "article-" + (value or "untitled")
    return value


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def new_run_dir(until: str) -> Path:
    """One immutable download ledger per invocation, including same-day reruns."""
    parent = INBOX / '_refresh'
    parent.mkdir(parents=True, exist_ok=True)
    return Path(tempfile.mkdtemp(prefix=until + '-', dir=parent))


def transcript_path(relative: str) -> Path:
    """Accept only episode-relative paths; upstream names never select local roots."""
    path = Path(relative)
    if (path.is_absolute() or '\\' in relative or ':' in relative
            or '..' in path.parts or len(path.parts) < 3
            or path.parts[0] != 'episodes' or path.name != 'transcript.md'):
        raise ValueError(f'Invalid upstream transcript path: {relative}')
    return path


def client() -> httpx.Client:
    return httpx.Client(timeout=35, follow_redirects=True,
                        headers={"User-Agent": "ModrnMind-KB-SourceRefresh/1.0"})


def get(c: httpx.Client, url: str) -> httpx.Response:
    response = c.get(url)
    # Ordinary temporary server errors only. Access denials are recorded, not bypassed.
    if response.status_code in {500, 502, 503, 504}:
        time.sleep(2)
        response = c.get(url)
    response.raise_for_status()
    return response


def as_markdown(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.select("script, style, .subscription-widget, .share-dialog, .button-wrapper"):
        tag.decompose()
    text = markdownify(str(soup), heading_style="ATX", bullets="-")
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def write_article(run_dir: Path, folder: str, post: dict, body: str,
                  original_html: str, access: str) -> dict:
    slug = safe_slug(post["slug"])
    target = INBOX / folder / f"{slug}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    fields = {
        "title": post["title"], "date": post["date"], "url": post["url"],
        "source": folder, "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "access": access, "source_type": post.get("type", "article"),
        "text_scope": post.get("text_scope", "visible_article_body; linked audio/video not transcribed"),
        "curation_status": "unreviewed",
    }
    text = "---\n" + "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in fields.items())
    text += f"\n---\n\n# {post['title']}\n\n{body}\n"
    result = dict(fields, path=str(target.relative_to(ROOT)), words=len(body.split()))
    if len(body.split()) < 60:
        result["content_warning"] = "short text; inspect for preview, link post, or media-only content"
    if target.exists():
        old = target.read_bytes()
        backup = run_dir / "previous" / folder / target.name
        if not backup.exists():
            backup.parent.mkdir(parents=True, exist_ok=True)
            backup.write_bytes(old)
        result["previous_sha256"] = digest(old)
        result["action"] = "refreshed_existing"
    else:
        result["action"] = "added"
    target.write_text(text, encoding="utf-8")
    snapshot = run_dir / "html" / folder / f"{slug}.html"
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    snapshot.write_text(original_html, encoding="utf-8")
    result["sha256"] = digest(target.read_bytes())
    return result


def substack(folder: str, base: str, since: str, until: str, run_dir: Path) -> dict:
    result = {"collection": folder, "archive": base + "/archive", "since": since,
              "until": until, "items": [], "errors": [], "archive_complete_for_window": False}
    ledger = run_dir / "collections" / f"{safe_slug(folder)}.json"
    seen = set()
    try:
        with client() as c:
            for offset in range(0, 10000, 50):
                url = f"{base}/api/v1/archive?sort=new&offset={offset}&limit=50"
                batch = get(c, url).json()
                if not isinstance(batch, list):
                    raise ValueError("archive did not return a list")
                if not batch:
                    result["archive_complete_for_window"] = True
                    break
                crossed = False
                new_ids = 0
                for item in batch:
                    key = str(item.get("id", item.get("slug")))
                    if key in seen:
                        continue
                    seen.add(key)
                    new_ids += 1
                    date = (item.get("post_date") or "")[:10]
                    if not date:
                        result["errors"].append({"slug": item.get("slug"), "error": "missing publication date"})
                        continue
                    if date < since:
                        crossed = True
                        continue
                    if date > until:
                        continue
                    post = {"slug": item["slug"], "title": item["title"], "date": date,
                            "url": item.get("canonical_url") or base + "/p/" + item["slug"],
                            "type": item.get("type", "article")}
                    try:
                        response = get(c, post["url"])
                        soup = BeautifulSoup(response.text, "html.parser")
                        content = soup.select_one("div.body.markup") or soup.select_one(".available-content .body")
                        if content is None:
                            raise ValueError("visible article body not found")
                        body = as_markdown(str(content))
                        if not body.strip():
                            raise ValueError("empty visible article body")
                        audience = item.get("audience")
                        access = "public-page" if audience == "everyone" else "public-preview-or-restricted-post"
                        entry = write_article(run_dir, folder, post, body, response.text, access)
                        entry["publisher_audience"] = audience
                        entry["post_id"] = item.get("id")
                        result["items"].append(entry)
                    except Exception as exc:
                        result["errors"].append(dict(post, error=str(exc)))
                    save_json(ledger, result)
                    if len(result["items"]) and len(result["items"]) % 20 == 0:
                        print(f"{folder}: {len(result['items'])} saved", flush=True)
                    time.sleep(0.25)
                if crossed:
                    result["archive_complete_for_window"] = True
                    break
                if new_ids == 0:
                    raise ValueError("archive pagination repeated without progress")
            else:
                raise ValueError("archive page limit reached")
    except Exception as exc:
        result["errors"].append({"error": str(exc)})
    save_json(ledger, result)
    return result


def wordpress(since: str, until: str, run_dir: Path) -> dict:
    folder = "Cal Newport"
    result = {"collection": folder, "archive": "https://calnewport.com/blog/", "since": since,
              "until": until, "items": [], "errors": [], "archive_complete_for_window": False}
    try:
        with client() as c:
            page = 1
            while True:
                url = f"https://calnewport.com/wp-json/wp/v2/posts?per_page=100&page={page}&after={since}T00:00:00&before={until}T23:59:59"
                response = get(c, url)
                for item in response.json():
                    post = {"slug": item["slug"], "title": BeautifulSoup(item["title"]["rendered"], "html.parser").get_text(),
                            "date": item["date"][:10], "url": item["link"], "type": "article"}
                    html = item["content"]["rendered"]
                    body = as_markdown(html)
                    if not body:
                        result["errors"].append(dict(post, error="empty published content"))
                        continue
                    result["items"].append(write_article(run_dir, folder, post, body, html, "public-page"))
                if page >= int(response.headers.get("X-WP-TotalPages", "1")):
                    result["archive_complete_for_window"] = True
                    break
                page += 1
    except Exception as exc:
        result["errors"].append({"error": str(exc)})
    save_json(run_dir / "collections/cal-newport.json", result)
    return result


def podcasts(run_dir: Path) -> dict:
    """Read upstream transcripts, adding changed/new copies outside the local git checkout."""
    result = {"collection": "Lenny's Podcast", "items": [], "errors": [],
              "archive_complete_for_window": False,
              "archive": "https://github.com/ChatPRD/lennys-podcast-transcripts",
              "scope": "all upstream transcript paths; unchanged local copies retained"}
    api = "https://api.github.com/repos/ChatPRD/lennys-podcast-transcripts"
    newest = ""
    try:
        with client() as c:
            commit = get(c, api + "/commits/main").json()
            sha = commit["sha"]
            result["upstream_commit"] = sha
            result["upstream_commit_date"] = commit["commit"]["committer"]["date"]
            tree = get(c, api + f"/git/trees/{sha}?recursive=1").json()
            if tree.get("truncated"):
                raise ValueError("GitHub tree truncated")
            entries = [p for p in tree["tree"] if p["path"].startswith("episodes/") and p["path"].endswith("/transcript.md")]
            result["upstream_transcripts"] = len(entries)
            for entry in entries:
                relative = transcript_path(entry["path"])
                old_path = INBOX / "Lenny's Podcast/repo" / relative
                target = INBOX / "Lenny's Podcast/refreshed" / relative.relative_to("episodes")
                current = target if target.exists() else old_path
                if current.exists():
                    data = current.read_bytes().replace(b"\r\n", b"\n")
                    sha_local = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
                    if sha_local == entry["sha"]:
                        text = data.decode("utf-8")
                        match = re.search(r"^publish_date:\s*(\d{4}-\d{2}-\d{2})", text, re.M)
                        if match:
                            newest = max(newest, match[1])
                        continue
                url = f"https://raw.githubusercontent.com/ChatPRD/lennys-podcast-transcripts/{sha}/{entry['path']}"
                text = get(c, url).text
                match = re.search(r"^publish_date:\s*(\d{4}-\d{2}-\d{2})", text, re.M)
                date = match[1] if match else None
                newest = max(newest, date or "")
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.exists() and target.read_text(encoding="utf-8") != text:
                    backup = run_dir / "previous/Lenny's Podcast" / relative
                    backup.parent.mkdir(parents=True, exist_ok=True)
                    if not backup.exists():
                        backup.write_bytes(target.read_bytes())
                target.write_text(text, encoding="utf-8")
                result["items"].append({"url": url, "path": str(target.relative_to(ROOT)), "date": date,
                                        "action": "refreshed_copy" if old_path.exists() else "added",
                                        "sha256": digest(target.read_bytes()), "access": "public-transcript-mirror"})
                save_json(run_dir / "collections/lennys-podcast.json", result)
                time.sleep(0.15)
            result["archive_complete_for_window"] = True
            result["newest_upstream_episode"] = newest
            result["coverage_caveat"] = "Completeness is relative to the GitHub mirror, not the podcast publication schedule."
    except Exception as exc:
        result["errors"].append({"error": str(exc)})
    save_json(run_dir / "collections/lennys-podcast.json", result)
    return result


def podcast_feed(since: str, until: str, run_dir: Path) -> dict:
    url = "https://api.substack.com/feed/podcast/10845.rss"
    result = {"collection": "Lenny's Podcast episode notes", "archive": url,
              "since": since, "until": until, "items": [], "errors": [],
              "archive_complete_for_window": False,
              "coverage_caveat": "Public RSS episode notes, not full interview transcripts. No audio downloaded."}
    try:
        with client() as c:
            response = get(c, url)
        (run_dir / "lennys-podcast-feed.xml").write_text(response.text, encoding="utf-8")
        entries = ET.fromstring(response.content).findall("./channel/item")
        dates = []
        for item in entries:
            date = parsedate_to_datetime(item.findtext("pubDate")).date().isoformat()
            dates.append(date)
            if not since <= date <= until:
                continue
            link = item.findtext("link")
            html = item.findtext("description") or ""
            post = {"slug": urlparse(link).path.rsplit("/", 1)[-1], "url": link,
                    "title": item.findtext("title"), "date": date, "type": "podcast_episode_notes",
                    "text_scope": "public RSS show notes; not a full transcript"}
            body = as_markdown(html)
            if not body:
                result["errors"].append(dict(post, error="empty episode description"))
                continue
            result["items"].append(write_article(run_dir, "Lenny's Podcast/episode-notes", post,
                                                 body, html, "public-feed-show-notes"))
        result["oldest_feed_episode"] = min(dates)
        result["newest_feed_episode"] = max(dates)
        result["archive_complete_for_window"] = min(dates) <= since
    except Exception as exc:
        result["errors"].append({"error": str(exc)})
    save_json(run_dir / "collections/lennys-podcast-episode-notes.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--since", required=True)
    parser.add_argument("--until", default=datetime.now(timezone.utc).date().isoformat())
    parser.add_argument("--collections", nargs="*")
    args = parser.parse_args()
    for date in [args.since, args.until]:
        datetime.strptime(date, "%Y-%m-%d")
    if args.since > args.until:
        parser.error("since must be before until")
    selected = set(args.collections or [*PUBLICATIONS, "Cal Newport", "Lenny's Podcast", "Lenny's Podcast episode notes"])
    allowed = {*PUBLICATIONS, "Cal Newport", "Lenny's Podcast", "Lenny's Podcast episode notes"}
    if selected - allowed:
        parser.error("Unknown collections: " + ", ".join(selected - allowed))
    run_dir = new_run_dir(args.until)
    manifest = {"started_at": datetime.now(timezone.utc).isoformat(), "since": args.since,
                "until": args.until, "collections": [], "scope": "public source refresh only"}
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = []
        for folder, base in PUBLICATIONS.items():
            if folder in selected:
                futures.append(pool.submit(substack, folder, base, args.since, args.until, run_dir))
        if "Cal Newport" in selected:
            futures.append(pool.submit(wordpress, args.since, args.until, run_dir))
        if "Lenny's Podcast" in selected:
            futures.append(pool.submit(podcasts, run_dir))
        if "Lenny's Podcast episode notes" in selected:
            futures.append(pool.submit(podcast_feed, args.since, args.until, run_dir))
        for future in as_completed(futures):
            result = future.result()
            manifest["collections"].append(result)
            save_json(run_dir / "manifest.json", manifest)
            print(json.dumps({"collection": result["collection"], "saved": len(result["items"]),
                              "errors": len(result["errors"]), "archive_complete": result["archive_complete_for_window"]}), flush=True)
    manifest["finished_at"] = datetime.now(timezone.utc).isoformat()
    # Only this invocation's selected collections determine its completion status.
    save_json(run_dir / "manifest.json", manifest)
    return int(any(r["errors"] or not r["archive_complete_for_window"] for r in manifest["collections"]))


if __name__ == "__main__":
    raise SystemExit(main())
