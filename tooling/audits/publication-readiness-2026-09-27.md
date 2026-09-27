# Publication-readiness audit — 27 September 2026

**Initial snapshot.** A later [focused evidence follow-up](focused-evidence-2026-09-27.md) reviewed all 25 deferred questions and updated 18 entries. Counts and validation below describe the initial audit; use the follow-up for current decisions and file hashes.

All 426 canonical entries inspected. Safe cleanup completed; 363 changed, 63 unchanged. Source and reporting questions remain in 25 entries. Those questions are explicit; this is not a claim that every source is publication-ready without further verification.

Baseline working tree was clean. Scope: canonical entries, four templates, citation navigation and generated indexes. No new sources; no changes to `raw/`, `private/` or agent instructions. Nothing staged, committed, pushed or published.

## Coverage

| Directory | Inspected | Changed | Unchanged | Deferred questions |
|---|---:|---:|---:|---:|
| concepts/ | 73 | 53 | 20 | 21 |
| methods/ | 22 | 15 | 7 | 2 |
| practices/ | 83 | 83 | 0 | 0 |
| sources/ | 248 | 212 | 36 | 2 |

Deferred counts overlap changed counts: safe prose and attribution fixes were applied while unresolved claims stayed bounded. Final classifications: 63 clean, 273 publication cleanup, 65 substantive evidence correction, 25 deferred verification. Some deferred entries also contain verified corrections.

## Editorial cleanup

- Removed ingestion decisions, review-pass narration, batch references, empty sections and plans for future entries.
- Consolidated repeated citations, source roles and findings; retained exact source identities, locators, unique citations and practitioner/research distinctions.
- Separated proposed benefits, reported outcomes, theoretical explanations and untested adaptations.
- Kept valid limitations, version scope, self-report boundaries and unresolved statistical details.
- Fixed index sentence splitting at author initials, “et al.” and “vs.”; retained bold text and added two regression tests.
- Templates now keep frontmatter first and explicitly separate evidence from rationale. Rebuilt index and practice guide; README counts unchanged.

## Evidence corrections

- **Learning:** Liu results are short-term; proposed persistence mechanism is not proven. Added the omitted “We posit that” qualifier to its quotation. Hische practice now describes the visual-noticing exercise rather than a separate AI word-list example.
- **Study design:** Meincke compares separate groups and dilemma responses, not within-person preference change. Nikolova uses pooled survey cross-sections and an instrument based on other sample countries, not a worker panel or neighboring-country instrument.
- **Measured outcomes:** Mascareño assesses selected ideas and implementation plans, not workplace implementation. Reich includes rated caption performance; willingness, self-confidence and ability remain distinct.
- **Disempowerment:** Sharma domain rates concern moderate-or-severe potential, not measured severe harm. User feedback and preference-model results are distinct.
- **Meta-analysis:** Vaccaro positive point estimates are not necessarily statistically significant synergy. Creation-task estimate remains nonsignificant; augmentation and synergy use different baselines.
- **Source identity and interpretation:** Corrected Gabbiadini/Durante name order while keeping the historical slug; Ericsson Study 2 concerns pianists. Cheng’s endorsement difference is relative, and repair intentions are not observed repair behavior. Georganta used human participants labeled as AI; a null triad result is not equivalence.
- **Theory and commentary:** SCAN, Singh, Messeri, Nosta and pre-AI fluency/creativity papers now distinguish proposed explanations from measured effects. Mollick’s management account has no AI-native comparison group; removed an unsupported equation and restored “I suspect” in a quotation.
- **Citation navigation:** Added 13 verified exact aliases and 19 missing source links. Never mapped the ambiguous “Nosta, Anti-Intelligence” citation to a different article.

## Deferred questions

These require an identifiable original, a separate source intake, or author clarification. No substitute citation was guessed.

| Entry | Unresolved question |
|---|---|
| [ai-oscillation-trap](../../concepts/ai-oscillation-trap.md) | No retained original verifies named oscillation hypothesis. |
| [anchoring-bias](../../concepts/anchoring-bias.md) | Tversky & Kahneman (1974): No direct canonical source entry exists; appearance in other papers as a cited reference does not establish a direct canonical identity. |
| [anthropomorphism-of-technology](../../concepts/anthropomorphism-of-technology.md) | Epley, Waytz & Cacioppo (2007): No direct canonical source entry exists; appearance in other papers as a cited reference does not establish a direct canonical identity. Waytz, Cacioppo & Epley (2010): No direct canonical source entry exists; appearance in other papers as a cited reference does not establish a direct canonical identity. |
| [anti-intelligence](../../concepts/anti-intelligence.md) | Nosta, Anti-Intelligence (2026): Ambiguous short citation. Existing canonical is Growing Up Anti-Intelligent (developmental article); current concept uses distinct quotes not found in that retained article. Do not alias by stem resemblance. |
| [automation-bias](../../concepts/automation-bias.md) | Gonzalez attribution unresolved; do not restore its purported evidence. |
| [capacity-erosion](../../concepts/capacity-erosion.md) | Duncan, Lodge/Loble or Gonzalez originals remain absent; retain uncertainty without reconstructing citations. |
| [cognitive-offloading](../../concepts/cognitive-offloading.md) | Duncan, Lodge/Loble or Gonzalez originals remain absent; retain uncertainty without reconstructing citations. |
| [confidence-competence-gap](../../concepts/confidence-competence-gap.md) | Scispace Literature Synthesis (2025): Generic synthesis citation lacks identifiable author/title/version and direct canonical source; cannot resolve safely. |
| [desirable-difficulty](../../concepts/desirable-difficulty.md) | Duncan, Lodge/Loble or Gonzalez originals remain absent; retain uncertainty without reconstructing citations. |
| [embodied-cognition](../../concepts/embodied-cognition.md) | Foundational originals not retained; no direct-source claim can be verified. |
| [illusion-of-explanatory-depth](../../concepts/illusion-of-explanatory-depth.md) | Rozenblit, L. & Keil, F. (2002). The misunderstood limits of folk science: an illusion of explanatory depth. Cognitive Science, 26, 521–562.: No direct canonical source entry exists; appearance in other papers as a cited reference does not establish a direct canonical identity. |
| [judgment-development-paradox](../../concepts/judgment-development-paradox.md) | Duncan, Lodge/Loble or Gonzalez originals remain absent; retain uncertainty without reconstructing citations. |
| [judgment](../../concepts/judgment.md) | Duncan, Lodge/Loble or Gonzalez originals remain absent; retain uncertainty without reconstructing citations. |
| [metacognition](../../concepts/metacognition.md) | Duncan, Lodge/Loble or Gonzalez originals remain absent; retain uncertainty without reconstructing citations. |
| [metacognitive-laziness](../../concepts/metacognitive-laziness.md) | Duncan, Lodge/Loble or Gonzalez originals remain absent; retain uncertainty without reconstructing citations. |
| [novice-vulnerability](../../concepts/novice-vulnerability.md) | Duncan, Lodge/Loble or Gonzalez originals remain absent; retain uncertainty without reconstructing citations. |
| [performance-paradox](../../concepts/performance-paradox.md) | Duncan, Lodge/Loble or Gonzalez originals remain absent; retain uncertainty without reconstructing citations. |
| [social-friction](../../concepts/social-friction.md) | Eubanks, Muran & Safran (2018): No direct canonical source entry exists; appearance in other papers as a cited reference does not establish a direct canonical identity. |
| [sycophancy](../../concepts/sycophancy.md) | Malmqvist (2025): Short author-year reference; no matching canonical entry. Exact work identity and direct evidence remain unresolved. |
| [upskilling-deskilling-paradox](../../concepts/upskilling-deskilling-paradox.md) | Shukla et al. (2025): Short author-year reference; no matching canonical entry. Exact work identity and direct evidence remain unresolved. Krook (2025): Short author-year reference; no matching canonical entry. Exact work identity and direct evidence remain unresolved. |
| [zone-of-proximal-development](../../concepts/zone-of-proximal-development.md) | Vygotsky (1978): No direct canonical source entry exists; appearance in other papers as a cited reference does not establish a direct canonical identity. Wood et al. (1976): No direct canonical source entry exists; appearance in other papers as a cited reference does not establish a direct canonical identity. Van de Pol et al. (2010): No direct canonical source entry exists; appearance in other papers as a cited reference does not establish a direct canonical identity. |
| [calibration](../../methods/calibration.md) | Gonzalez framework attribution unresolved; linked research does not validate full method. |
| [complementarity-framework](../../methods/complementarity-framework.md) | Gonzalez framework attribution unresolved; linked research does not validate full method. |
| [georganta-team-trust-2024](../../sources/georganta-team-trust-2024.md) | Why does the source abstract report 828 overall when final study samples are 494 and 318 (812 combined)? Retain study-specific counts; do not silently choose one combined total. |
| [mascanero-proximal-collaboration-2026](../../sources/mascanero-proximal-collaboration-2026.md) | Methods report April–May 2023 data collection and name a GPT-4o API. Model or collection date needs author clarification; do not guess. |

Other existing source limits remain in place, including Li’s extracted Table 1 values, Lips-Wiersma/Wright’s model-fit discrepancy, Marcoccia’s inconsistent reporting, Martela/Riekki’s exclusions and p-signs, Niemiec’s pagination, and preprint/version boundaries. None was silently resolved.

## Validation

| Command/check | Result |
|---|---|
| `uv run python tooling/scripts/linter.py --json` | 53 length warnings only; all are source notes under 200 words. No structural, wikilink, metadata, source-record or missing-related findings. |
| `uv run python tooling/scripts/linter.py --check practice_schema --json` | Pass: 83 practices. |
| `uv run python tooling/scripts/check_citation_links.py` | Exit 1: 13 unresolved references in 9 entries, listed above. Verified identities and canonical links repaired. |
| `uv run --with httpx --with beautifulsoup4 --with markdownify python -m unittest discover -s tooling/tests -v` | 43 tests pass, including two new index tests. |
| `uv run python tooling/scripts/build-index.py` | Pass: exactly 426 unique canonical targets. |
| `uv run python tooling/scripts/build-practice-guide.py` | Pass: 83 practices. |
| `uv run python tooling/scripts/update_readme_counts.py` | Pass: counts already correct; README unchanged. |
| Local Markdown targets; duplicate/empty sections | Pass across all 426 entries. |
| `git diff --check` | Pass. |
| Allowlist, status labels, quotation and protected-path comparison | Pass. Two quotation corrections restore omitted uncertainty qualifiers; no other blockquote loss. |

The uv cache was blocked in the default sandbox; required checks were retried with permission and completed. Checks were not weakened. Length warnings were reviewed as heuristics rather than padded away. Citation failures remain explicit evidence gaps.

Independent reviews covered reader-facing prose, evidence corrections and structure. Each was read-only; the main agent applied final fixes. The machine-readable manifest records coverage and limits, including which scopes a reviewer had previously edited.

## Diff and review groups

Before adding this report and its manifest: 372 tracked files changed (+2,277/−4,575 lines), plus one new test file. Final working set: 363 canonical entries and 12 supporting files (navigation, templates, aliases, tests and two audit records). No entry was added, deleted or renamed.

Suggested review/commit groups (nothing staged):

1. Evidence corrections and explicit unresolved-source boundaries; review source notes alongside linked concepts/methods.
2. Editorial cleanup and practice citation consolidation.
3. Templates, generator fix, regression tests, citation aliases and rebuilt navigation.
4. This audit report and the per-file manifest.

Exact paths, reasons, classifications, hashes, deferred questions and review groups: [publication audit manifest](publication-readiness-2026-09-27.json).
