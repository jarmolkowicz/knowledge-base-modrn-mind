# Practitioner practices development log

## 2026-09-26 — Initial design pass

User asked how to develop the KB to include practices from credible non-paper sources, starting with `raw/inbox/Practical`.

Inspected current index, contribution guidance, method/source templates, librarian workflow, selected existing methods, inbox counts and earlier practice extractions. Checked selected original articles, a timestamped podcast passage, and primary webpages. Standard KB search failed at uv cache initialization; used index and targeted file searches.

Created three proposal documents in `drafts/`: development approach, source shortlist, and four illustrative practice cards. This is a design workbench, not a cataloged external source; no source ingestion or integration decision is claimed. No canonical entries, original inbox files, templates or workflow instructions changed.

Pending: discussion of the proposed scope and format; per-source ingestion decisions if the pilot proceeds.

## 2026-09-26 — Direction revised; sources refreshed

User agreed a separate `practices/` collection, accepted the practice format, and asked to leave the intended-outcome taxonomy open for development through source review. User renamed the blog folder to `Sam Illingworth`, added the `Slow AI` book EPUB and a `The Borrowed Mind` EPUB, and deleted prior practice extractions.

Updated the proposal, source inventory and sample links. Saved the accepted structure as `tooling/templates/practice.md`; it remains a working template until practices are supported by the ingestion and indexing tools. No canonical entries migrated and no deleted extraction files recreated.

Downloaded 299 author posts/public previews for March–September plus 43 later podcast episode notes: 306 new text files, 36 refreshed files with backups. All 342 paths and SHA-256 hashes verified. Public archive endpoints traversed through the chosen window. Of the author posts, 151 are marked restricted/preview. The podcast transcript mirror has no newer transcripts; official RSS show notes saved separately.

Cataloged the purchased Slow AI book locally, without uploading it. The newly provided Borrowed Mind EPUB is byte-identical to the existing integrated source's original; retained both user-supplied files without duplicate ingestion.

Details: [source-refresh-2026-09-26.md](source-refresh-2026-09-26.md). Next work: review refreshed sources and develop the outcome taxonomy; implement practice-folder support before integration. No automatic inclusion decisions recorded.

## 2026-09-26 — Full-collection pre-screen prepared

After discussing coverage versus depth, user suggested screening to preselect useful sources. Created a screening protocol and complete source register: 881 items, with derivative copies and download snapshots excluded. A local whole-text cue scan supplies passage pointers, not quality scores or semantic verdicts. No source automatically excluded and no outcome taxonomy applied.

Recorded five passage-screening examples (three candidates for further reading, two background/discovery items). Remaining interpretive screening is explicitly pending. Found 31 duplicate candidates, of which six have identical normalized bodies and 25 share a URL with different bodies. No original source files changed. See `screening/screening-protocol.md`.

## 2026-09-26 — Full-inventory first pass completed

User asked to handle screening. Accounted for all 881 items, with brief passage screening for available articles/transcripts, metadata-only known access holds, section-level book screening and full extraction/reading of the six-page PDF. Expanded selected sources and checked nine lower-priority articles. Actual depth and limits are explicit; this is not full reading of all sources or systematic verification of practitioner credentials.

Published 15-source annotated shortlist and complete disposition register. Recorded 198 access holds, 23 provenance holds and 12 repeated transcript bodies (overlapping earlier duplicate candidates). All sources retained; no semantic content exclusions. PDF bibliography checked against NOVA university's publication record. Each shortlist entry records attribution, basis, locators and benefit-claim limits.

Validated complete ID coverage and all 881 source hashes. Protected the reviewed register from accidental overwrite by the initial cue scanner. No canonical entries or outcome taxonomy changed; no deleted practice extractions recreated. Results: [screening-results.md](screening/screening-results.md). Next: source-faithful close reading/extraction with the wider priority/transfer queue kept open.

## 2026-09-26 — Remaining 400-item queue screened

User chose to continue the queue after reviewing the initial 15. Assessed all 239 priority and 161 transfer leads using expanded original passages and targeted follow-up. Saved per-source reading packets and 400 individually recorded decisions. This is section-level screening, not full-source reading or systematic credential/research verification.

Selected 124 additional sources: 78 direct/flagged practice leads, 27 human-practice transfer sources and 19 counterexamples. Combined with the original 15 into 139 selected sources across 19 provisional contribution groups, with 52 starting sources for close reading. Retained 92 useful variants separately. New holds: three missing-content cases and five source-identity cases, including suspicions requiring verification. Targeted final recheck upgraded ID775 from background to a variant on firsthand user contact. No outcome taxonomy adopted.

Published consolidated shortlist, detailed source notes, full queue decisions and current register. Preserved first-pass results and register snapshot; guarded the first-pass publisher against overwriting newer judgments. Original sources and canonical entries unchanged. No practices extracted or approved in this step.

Validated 400 unique queue IDs, exact queue coverage, all 139 selected sources grouped once, and all 881 source hashes. Local project uv environment remains unavailable; stdlib scripts ran through uv's no-project mode with the bundled Python runtime.

Current result: [screening-results.md](screening/screening-results.md). Next: close reading and extraction by contribution group through per-source workbenches; resolve specific access/identity gaps when needed and implement practices support before integration.

## 2026-09-26 — Selected pool reviewed and practice drafts critiqued

User asked to continue. Completed scoped close reading of all 139 selected sources across all 19 contribution groups, including supporting sources and counterexamples. Available article bodies, relevant complete transcript exchanges, six extracted HBR pages and relevant book sections were reviewed; precise coverage and limitations remain in each workbench. This was not cover-to-cover reading of every interview/book, nor systematic external credential verification.

Created 78 emerging practice cards beside their source records. Source roles: 76 origins, 33 supporting accounts, 25 counterexamples and 5 deferred. Consolidated overlaps without treating repeated advice as independent evidence. New per-source workbenches retain originals, source metadata, triage, distillation, three-lens critique, draft source notes and practice-review.json. Existing books preserve prior stages/status; supplementary practice reviews and the Nosta update proposal remain separate.

Prepared a complete practice catalogue, source-review register, cross-source critique and nine provisional outcome questions. No outcome taxonomy adopted. Drafts distinguish author proposals, reported experience, evaluated outcomes and editorial adaptations. No canonical practices or source updates integrated. Mollick #80’s existing-entry overstatements are flagged in a draft update only.

Extended draft validation to discover practices and clarified that READY is a mechanical result, not integration approval. All 78 cards pass; 138 of 139 complete workbenches have no mechanical findings. Newport #52 remains deferred with a publication-year mismatch; not suppressed. All 139 retained-original hashes match, local draft links resolve, all cards are registered and proposed slugs are unique.

Current result: [review hub](extraction/README.md). Next editorial work: review outcome wording and neighboring cards; then support practices in integration/search/index tooling and record per-source integration decisions. The wider inventory, 92 screened variants, and access/provenance holds remain available.

## 2026-09-27 — Outcome review, consolidation and integration preparation

User asked to continue to the next step. Reviewed the procedures, rationale and limits of all 78 practice drafts against the provisional outcome list. Proposed eight human outcomes and two enabling outcomes, with one primary label, secondary labels, rationale and proposed observation for every card. This is editorial mapping, not a validated taxonomy or evidence of benefits. Original sources were not all reread during this phase; prior recorded source-review coverage remains authoritative.

Proposed 77 standalone cards. Consolidated the Mollick human-contribution card as an attributed variant in the retained thinking-step card; kept the original extraction. Other close neighbors remain separate for their different triggers, actions or checks. Fixed two incomplete book citations and removed loosely related research links from seven cards. Eleven draft revisions have before/after hashes and per-source log entries.

Prepared an integration manifest for 77 cards and 122 source dependencies, with exact destinations, current hashes, source roles and pending decisions. Two cards remain held for correction of the existing Mollick management source; 75 await an editorial decision. Source #52's year issue stays deferred. Sources not referenced by this batch remain archived, not rejected.

Enabled separate practices in search, index, README counts, source navigation and bundled releases. Explicit source stems prevent same-author/year ambiguity. Fifteen tests passed, including empty/populated practice bundles and preservation of evidence limits. The source audit verified all 139 original hashes and found no broken local links; the one known source #52 date finding remains visible.

No canonical practice/source integration or blanket author approval. Current result: [outcome review](extraction/outcome-review.md) and [integration preparation](extraction/integration-plan.md). Next: editorial decision on this concrete package, then Stage 5 for approved entries and source corrections.

## 2026-09-27 — Approved unblocked collection integrated

User said “Move on” after the concrete review package. Recorded approval for 75 unblocked practices and their dependencies; the two source-correction holds remain excluded. Adopted the eight human outcomes plus two enabling outcomes as provisional navigation, not efficacy claims.

Stage 4.5 and final-copy validation passed. Integrated 75 practices and 114 scoped source notes; reused the existing Nosta book entry. Final source summaries replace internal workflow instructions with the already recorded source proposals/reports; evidence limits and reading coverage remain explicit. Kept original extraction drafts and prepared-copy hashes. Recorded per-source decisions, validation, integration and logs. The Slow AI book has root stage pointers to its scoped practice review rather than an implied whole-book review.

Built the public practice guide, refreshed index/counts to 418 entries, and synchronized exact source links for the new practices only. Twenty-six regression tests passed. Verified all 139 original snapshots, 139 retained originals, 229 protected existing entries and 77 planned extraction hashes. No broken links or new citation regressions. Forty older citation-navigation findings are separately recorded; this is not a claim that every KB citation was newly verified.

Current result: [integrated collection and verification](integration/README.md). Remaining: the two held Mollick management cards/source correction; broader variant and access/provenance queues remain available.
