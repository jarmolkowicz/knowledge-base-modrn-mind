# Practical source refresh — 2026-09-26

## Result

**342 text files saved: 306 new, 36 refreshed with prior versions retained.**

These are downloaded source texts, not reviewed practice entries. The refreshed author posts span 2026-03-01 through 2026-09-26. The existing collections generally stopped in March; this overlap also rechecks recent saved posts. Older saved articles remain available but were not all re-fetched.

| Collection | New | Refreshed | Restricted / preview | Latest downloaded date |
|---|---:|---:|---:|---|
| Adam Grant | 8 | 1 | 0 | 2026-08-29 |
| Cal Newport | 24 | 1 | 0 | 2026-09-10 |
| Ethan Mollick | 9 | 1 | 0 | 2026-09-18 |
| Nate B Jones | 104 | 20 | 123 | 2026-09-24 |
| Ruben Hassid | 23 | 4 | 16 | 2026-09-23 |
| Sabrina Ramonov | 23 | 2 | 0 | 2026-09-26 |
| Sam Illingworth | 72 | 7 | 12 | 2026-09-25 |
| Lenny's Podcast — episode notes | 43 | 0 | Not full transcripts | 2026-09-20 |
| **Total** | **306** | **36** | **151 restricted/preview posts** | |

The seven author collections account for 299 posts: 148 marked public-page and 151 marked public-preview-or-restricted-post using publisher audience metadata. Some posts accompany podcasts or videos; the downloaded article body is not a transcription of linked media. Sam's refresh includes 22 podcast posts from his archive.

## Books

- **Slow AI:** purchased EPUB copied and extracted locally to [the source workbench](../illingworth-slow-ai-2026/source.json). Readable text: [source.md](../illingworth-slow-ai-2026/source.md), about 26,556 words. Seven numbered chapters plus front/back matter; the extractor reports 26 EPUB document items. Author/year/edition checked against title and copyright text. Stage: **cataloged**, not triaged or integrated. The purchased original was not uploaded.
- **The Borrowed Mind:** the new EPUB and the stored original have the same SHA-256: `d2431fbd7bfd25a4a61aaacd7ba3e7c0ff5557e23383846c47d1586c75cb93ad`. Its [existing source workbench](../nosta-borrowed-mind-2026/source.json) already contains the extracted text and an integrated source record. No second extraction or duplicate source created. A fresh practice review can reuse that source.

## Podcast coverage

The [ChatPRD transcript mirror](https://github.com/ChatPRD/lennys-podcast-transcripts) remains at commit `be8ab89a890a833cbba2c892178f823fff178c65`, dated 2026-01-24. Its 303 transcripts match the saved local copies; the latest episode date is 2026-01-11. Local repository changes were preserved.

The [official RSS feed](https://api.substack.com/feed/podcast/10845.rss) supplies 43 later episode descriptions through 2026-09-20. Saved under `raw/inbox/Practical/Lenny's Podcast/episode-notes/`, each marked **public show notes, not a full transcript**. These notes locate newer interviews but cannot support claims about dialogue that has not been inspected. The refresh did not obtain newer full transcripts or download audio/video.

## Provenance and checks

- [Combined download ledger](../inbox/Practical/_refresh/2026-09-26/manifest.json) and per-collection ledgers record original URLs, dates, access labels, actions, word counts and SHA-256 hashes. Each collection records its own coverage window.
- The 342 saved paths are distinct; every saved file exists and matches its recorded hash. No download failures remained. No saved article body was below the 60-word inspection flag.
- Publisher archive pagination was followed back through the requested window. This verifies coverage of those public archive endpoints, not every post on every platform an author uses.
- Source HTML snapshots and previous local files are retained under `raw/inbox/Practical/_refresh/2026-09-26/`. The podcast RSS snapshot is retained there too. These inbox materials remain outside the tracked public KB.
- No authentication, paywall bypass, file upload or automatic integration occurred. Restricted posts remain incomplete evidence until their full text is legitimately available.
- `Modrn Mind/` local working documents and the PDF in `Random/` were retained. They were not treated as subscription feeds.

## Decisions carried forward

- Separate `practices/` collection agreed; migration and tooling support still pending.
- Practice format accepted and saved as [a working template](../../tooling/templates/practice.md).
- The previous outcome list is not adopted. Collect author-stated purposes, concrete actions and observed outcomes first; develop the taxonomy through comparison and discussion.
- Deleted practice extractions were not restored. New extraction has not begun.
