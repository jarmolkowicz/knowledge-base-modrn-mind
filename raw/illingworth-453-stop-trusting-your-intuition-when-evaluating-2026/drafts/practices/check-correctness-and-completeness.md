---
status: emerging
area: [preservation]
sources:
  - "Khaled Ahmed, guest contributor with Sam Illingworth. Stop Trusting Your Intuition When Evaluating AI. 2026-01-03. https://theslowai.substack.com/p/evaluate-ai-correctness-completeness"
  - "Ruben Hassid. Search.. 2025-10-05. https://ruben.substack.com/p/search"
---

# Check correctness and completeness separately

Draft only. Integration pending. Title is editorial, not a validated named method.

## Use When

You have an answer, a task definition and reference material you can inspect.

## Try It

1. Choose the reference and state what the answer is supposed to cover.
2. Ask AI for two lists: claims that contradict or go beyond the reference, and relevant material missing from the answer. Require a reference location for each flag.
3. [Inference] Check every flag yourself against the reference. Decide which omissions matter; correct the answer and mark unresolved claims.

## Origin

Khaled Ahmed, guest contributor with Sam Illingworth. Stop Trusting Your Intuition When Evaluating AI. 2026-01-03. https://theslowai.substack.com/p/evaluate-ai-correctness-completeness

Locators in `raw/illingworth-453-stop-trusting-your-intuition-when-evaluating-2026/source.md`: L28–36: correctness and completeness checks against a supplied reference; L58–78: compiler-timeline demonstration and model-flag counts.

Ruben Hassid. Search.. 2025-10-05. https://ruben.substack.com/p/search

Locators in `raw/hassid-328-search-2025/source.md`: L95: timestamps and contradictions; L136: excerpts with original links; L144–152: legal and market-research prompts.

Source passages are paraphrased. Steps arrange the cited guidance; editorial additions are marked [Inference]. Support and failure cases are not independent validation.

## Evidence and Rationale

**Basis:** Proposed checklist plus a displayed model-assisted comparison.

**Observed or reported:** Ahmed demonstrates the split on a compiler timeline. Reported counts are model flags, not independently established errors. Hassid supplies related traceable-search prompts.

**Related research:** [[reference-verification]] describes the same boundary: a checking prompt is not verification until the source is inspected. This is a procedural extension, not a new tested mechanism.

**Untested:** No direct evaluation of this complete routine was found in the reviewed material. Output quality, later unaided capability, felt competence and calibrated confidence are separate; successful assisted completion does not establish all four.

## Limits

A bad reference can make a faithful answer wrong. A model can invent quotations or over-report omissions. Keep “not supported here” distinct from “false.”

## What to Notice

[Inference] Curator-proposed observation, not a validated measure: Which flags survive your inspection, and what did the model miss?

## Related

- [[reference-verification]] — related local entry inspected; see rationale and limits above.
- [[automation-bias]] — related local entry inspected; see rationale and limits above.
