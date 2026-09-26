# PARTIAL papers — draft review

Date: 2026-09-26

**Status update:** All ten papers integrated after user approval. See the [integration report](./julia-2026-09-26-partial-integration.md). The sections below preserve the earlier draft-review record; source links now point to their public destinations.

## Result

- Ten PARTIAL papers processed through Stage 3: ten source drafts and twelve targeted update proposals across nine existing entries.
- No new concepts or methods. No public KB integration, commit or push.
- All ten triage decisions recorded as PARTIAL; workbench status is drafted. Distillation decisions remain pending.
- This is a draft evidence check, not the formal three-lens Stage 4 critique.

## Drafts

| Paper                                                                             | Source draft                                                      | Targeted updates                                                                                                                                                                                                     | Evidence boundary                                                                                         |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Cash et al. (2026) — Specific Skills Versus Basic Cognitive Abilities             | [Read](../sources/cash-ai-stupid-2026.md)                    | [capacity-erosion](./cash-ai-stupid-2026/drafts/updates/capacity-erosion.md); [cognitive-offloading](./cash-ai-stupid-2026/drafts/updates/cognitive-offloading.md)                                                   | Skill acquisition, skill decay and basic cognitive abilities kept distinct.                               |
| Baumeister et al. (2013) — Happiness and Meaningfulness                           | [Read](../sources/baumeister-happy-meaningful-life-2013.md)  | [professional-identity-threat](./baumeister-happy-meaningful-life-2013/drafts/updates/professional-identity-threat.md)                                                                                               | Happiness and meaning separated; partial correlations not causal effects.                                 |
| Wang & Zhou (2025) — AI Replacement Concerns and Burnout                          | [Read](../sources/wang-ai-awareness-burnout-2025.md)         | [professional-identity-threat](./wang-ai-awareness-burnout-2025/drafts/updates/professional-identity-threat.md); [identity-threat-coping](./wang-ai-awareness-burnout-2025/drafts/updates/identity-threat-coping.md) | Replacement concerns, not AI literacy; cross-sectional survey. Ambiguous coefficients excluded.           |
| Schmutz et al. (2024) — Coordination in Human–AI Teams                            | [Read](../sources/schmutz-ai-teaming-2024.md)                | [complementarity-framework](./schmutz-ai-teaming-2025/drafts/updates/complementarity-framework.md)                                                                                                                   | Citation corrected to 2024. Coordination evidence does not imply a universal teaming penalty.             |
| El et al. (2026) — Measuring AI Influence Without Treating All Persuasion as Harm | [Read](../sources/el-cognitive-security-2026.md)             | [conversational-steering](./el-cognitive-security-2026/drafts/updates/conversational-steering.md)                                                                                                                    | Position paper, not validated metrics or intervention evidence.                                           |
| Nisbett & Wilson (1977)                                                           | [Read](../sources/nisbett-wilson-introspection-1977.md)      | [metacognition](./nisbett-wilson-introspection-1977/drafts/updates/metacognition.md)                                                                                                                                 | Causal self-explanations distinguished from reports of experience; no blanket dismissal of introspection. |
| Salinas et al. (2026)                                                             | [Read](../sources/salinas-law-professors-ai-2026.md)         | [judgment](./salinas-law-professors-ai-2026/drafts/updates/judgment.md)                                                                                                                                              | Expert answer preference, not student learning or transfer.                                               |
| Ali et al. (2025)                                                                 | [Read](../sources/ali-human-ai-knowledge-ecosystems-2025.md) | [complementarity-framework](./ali-human-ai-knowledge-ecosystems-2025/drafts/updates/complementarity-framework.md)                                                                                                    | Framework map, not causal validation; conflicting search start dates recorded.                            |
| Jia, Ning & Liu (2025)                                                            | [Read](../sources/jia-workplace-ai-review-2025.md)           | [professional-identity-threat](./jia-workplace-ai-review-2025/drafts/updates/professional-identity-threat.md)                                                                                                        | Different AI exposures and measures preserved; review not counted as new primary evidence.                |
| Vannoy, Cadieux & Lyubomirsky (2026)                                              | [Read](../sources/vannoy-human-2-wellbeing-2026.md)          | [ai-loneliness-effect](./vannoy-human-2-wellbeing-2026/drafts/updates/ai-loneliness-effect.md)                                                                                                                       | Structured support, communication and companionship separated; primary-source qualifications retained.    |

Each workbench's distill.md records reading coverage, proposed files, evidence checks and its pending decision. Source notes retain page-located quotations, design and limitations. Where supplementary analyses or primary studies behind a review were not independently audited, that boundary is explicit.

## Cross-paper integration considerations

- Professional identity threat receives three distinct additions: Baumeister on meaning versus happiness; Wang on replacement concerns and burnout; Jia on exposure and context. Merge under the specified headings without turning them into one causal chain.
- Complementarity framework receives two additions: Schmutz on coordination; Ali on organizational conditions. Keep the shared practical implication concise and labeled as inference.
- Schmutz's actual publication year is 2024. Preserve raw/schmutz-ai-teaming-2025 as the historical audit path; the intended public stem is schmutz-ai-teaming-2024. The update currently links its workbench identity and includes an explicit instruction to reconcile both source links at integration. The mechanical year check misses this because the first page also mentions a 2025 themed issue. This manual correction remains an integration prerequisite.
- Wang's prose and extracted tables contain conflicting signs/formatting. No coefficients or mediation magnitudes are promoted. Numerical reuse requires a separate table check.
- Ali's methods say 2020–December 2024 while its discussion says 2014–2024. Do not repeat an exact start date as settled.
- Vannoy's broad review wording must not replace the narrower source-level qualifications already in the loneliness entry.

## Checks

- Draft validator: zero findings for all ten workbenches, rerun after quotation corrections.
- Twenty quoted passages matched their stated pages in the cached source text after Unicode, whitespace and line-wrap normalization. This checks extraction-level fidelity, not PDF layout.
- Public-file SHA-256 check: all 199 baseline files unchanged; no additions or removals in concepts/, methods/, sources/, index.md, README.md or root log.md.
- No tracked files found under tmp/, temp/, .tmp/, .cache/, .pytest_cache/, .ruff_cache/ or .uv-cache/. Existing ignore rules retained. No scratch files created for this pass.

## Next decision at the draft-review stage

Review the drafts, then authorize Stage 4 critique. Integration requires a later recorded approval. Formal critique should check evidence fidelity, fit with the KB and cross-paper repetition before any public changes.
