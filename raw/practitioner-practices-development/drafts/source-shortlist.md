# Practitioner source shortlist

Date: 2026-09-26  
State: historical collection/refresh inventory. Current results: [screening report](../screening/screening-results.md) and [annotated shortlist](../screening/shortlist.md). This is not an author ranking or ingestion decision.

## Current decisions and refresh

- Separate `practices/` collection agreed. Entry format accepted. Outcome taxonomy remains open and will be developed through source review.
- `Sam Illingworth/` contains his blog/newsletter articles. `Slow AI/` contains the purchased book. These are distinct sources by the same author.
- Earlier practice-extraction files were deleted by the user. Fresh review must use originals, not those summaries.
- Public author archives refreshed for 2026-03-01 through 2026-09-26. Lenny's official episode notes cover the gap after 2026-01-11. See [refresh report](../source-refresh-2026-09-26.md) for counts and access limits.
- The previous sample cards demonstrate the accepted format; they do not determine the review batch or outcome taxonomy.

## Start here

| Source | Why inspect it | First item and limits |
|---|---|---|
| **Sam Illingworth's blog, including named guest contributors** | The inspected pieces show writing and teaching practices, examples, and human choices. Sam Illingworth has relevant university experience in pedagogy; credit the actual contributor for each routine. | Earlier Hogue and Sherman examples remain useful format illustrations. Review newer material before choosing the pilot. |
| **Slow AI — Sam Illingworth's book** | A full book source that may organize practices differently from individual blog posts. | Purchased EPUB extracted to `raw/illingworth-slow-ai-2026/`. Cataloged only; content assessment and practice extraction pending. |
| **Ethan Mollick / One Useful Thing** | Relevant research and teaching, with concrete AI experiments. His academic publications and newsletter recommendations need separate evidence labels. | “Giving your AI a Job Interview”: repeated tests on realistic work, expert assessment, comparison. Overlaps with [[calibration]]. |
| **Selected Lenny's Podcast guests** | Named practitioners explain actual work. A channel's reputation does not validate every guest or claim. | Hilary Gridley, 2025-06-15, 01:26:46–01:28:29: product-context reasoning exercises. Describes a tool and process; no measured transfer result in this passage. |

Primary background checks: [Illingworth's university profile](https://www.napier.ac.uk/people/sam-illingworth), [Mollick's Wharton profile](https://mgmt.wharton.upenn.edu/profile/emollick/). Checked 2026-09-26. Profiles establish relevant roles, not intervention effectiveness. Hogue's [original guest post](https://theslowai.substack.com/p/how-can-writers-use-ai-ethically) identifies her contribution and describes her writing experience. Gridley's role is taken from the dated episode, not asserted as her current job.

## Selectively inspect next

| Collection | Use it for | Check before inclusion |
|---|---|---|
| **Cal Newport** | Craft, attention, deliberate learning, and boundaries around delegation | Distinguish a concrete routine from commentary. Review the refreshed originals. The previously inspected “Think Inside the Box” article is primarily an argument. |
| **John Nosta / The Borrowed Mind** | Candidate routines concerning agency and maintaining capability | The newly supplied EPUB is SHA-256-identical to the stored original in `raw/nosta-borrowed-mind-2026/`, which is already integrated. Reuse that source for a fresh practice review rather than duplicating ingestion. |
| **Nate B Jones** | Possible routines concerning rejection, evaluation, intent, and human access to shared information | Most refreshed posts expose public previews. Do not reconstruct paywalled instructions or treat article statistics as checked research. Trace important claims to their original evidence. |
| **Ruben Hassid** | Concrete context-building, critique and workflow examples | Separate usable actions from promotion and tool claims. Check attribution and supporting studies; agreement between two models is not independent factual verification. |
| **Sabrina Ramonov** | Possible building and experimentation examples | New public posts downloaded; substantive review pending. Evaluate particular demonstrations for the KB's purpose; no author-level credibility verdict made. |
| **Adam Grant** | Potential supporting material on disagreement, learning and human connection | Refreshed originals available. AI adaptations of general advice must be explicitly labelled as adaptations. |
| **Modrn Mind** | The user's existing framework and workflow as separate inputs to the review | Local working material, not independent confirmation of a practitioner claim. Preserve its authorship and distinguish it from external sources. |
| **Random** | One collected PDF | Retained locally; not reassessed during the article refresh. |

These priorities concern fit to this pilot, not a judgment of the authors as people. Commercial interests were not systematically checked; that remains part of per-item triage.

## Two useful additions outside the collected folders

- **Simon Willison:** [“Here's how I use LLMs to help me write code”](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) (2025-03-11). Describes personal use, links to working examples, requires testing, and distinguishes exploration from production work. Promising for exploration with retained responsibility. Broader learning benefits remain first-person claims; transfer beyond software would be an editorial adaptation.
- **Hamel Husain:** [“Your AI Product Needs Evals”](https://hamel.dev/blog/posts/evals/) (2024-03-29). A worked application case with human review and comparison of model judgments to human judgments. Promising for turning expert judgment into explicit evaluation criteria. It evaluates AI systems; it does not demonstrate improvement in the human evaluator's thinking.

Both primary articles checked online on 2026-09-26. They are candidates for later ingestion, not newly integrated sources.

## Inbox inventory

Counts below are current top-level Markdown files in each author folder, not reviewed or eligible-source counts. Lenny's counts identify transcript files and new episode notes explicitly. Download snapshots and backups under `_refresh/` are excluded.

| Folder | Markdown files |
|---|---:|
| Adam Grant | 18 |
| Cal Newport | 46 |
| Ethan Mollick | 43 |
| Lenny's Podcast | 303 existing transcripts; 43 new episode notes |
| Modrn Mind | 2 |
| Nate B Jones | 146 |
| Random | 0; one PDF |
| Ruben Hassid | 94 |
| Sabrina Ramonov | 56 |
| Sam Illingworth | 127 |
| Slow AI | Purchased EPUB; extraction in its source workbench |
| The Borrowed Mind | 2 Markdown files plus duplicate EPUB |

The deleted extraction files are not inputs to the next review. Do not count similar newsletter retellings as independent confirmations.

Local originals for the format examples are linked in [sample-practices.md](sample-practices.md). Prior versions of refreshed articles are retained in `_refresh/2026-09-26/previous/`. Record future assessment decisions in source workbenches.
