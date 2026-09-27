---
status: emerging
area: [preservation]
sources:
  - "Hamel Husain and Shreya Shankar, interviewed by Lenny Rachitsky. Why AI evals are the hottest new skill for product builders | Hamel Husain & Shreya Shankar. 2025-09-25. https://www.youtube.com/watch?v=BsWxPI9UM4c"
---

# Inspect real errors before automating evaluation

Draft only. Integration pending. Title is editorial, not a validated named method.

## Use When

An AI product has real interactions and domain expertise available for review.

## Try It

1. Read complete interactions and write your own failure notes before asking AI to categorize them. Look for upstream errors.
2. Ask AI to group the notes. A human refines categories and checks assignments, including cases that fit none.
3. Prioritize consequential failures. Prefer direct checks where possible; use a model judge only for a defined need.
4. Compare judges with held-out human judgments. Inspect false positives and false negatives, not just agreement. Keep reviewing new failures and changing criteria.

## Origin

Hamel Husain and Shreya Shankar, interviewed by Lenny Rachitsky. Why AI evals are the hottest new skill for product builders | Hamel Husain & Shreya Shankar. 2025-09-25. https://www.youtube.com/watch?v=BsWxPI9UM4c

Locators in `raw/lenny-652-why-ai-evals-are-the-hottest-2025/source.md`: L130–272: traces, human notes, upstream errors; L296–359: domain expertise and sample-size heuristic; L377–557: AI groups notes; human refines categories and checks assignments; L581–710: prioritize, use simple checks, compare judges with humans; L935–980: resource fit and human-first boundary.

Source passages are paraphrased. Steps arrange the cited guidance; editorial additions are marked [Inference]. Support and failure cases are not independent validation.

## Evidence and Rationale

**Basis:** Detailed practitioner interview with customer-support evaluation examples.

**Observed or reported:** Husain and Shankar describe actual support traces and a concrete human-first process; no controlled business-impact estimate.

**Related research:** [[metacognitive-demand]] frames the continued effort of oversight. It is a related account, not direct validation of this procedure.

**Untested:** No direct evaluation of this complete routine was found in the reviewed material. Output quality, later unaided capability, felt competence and calibrated confidence are separate; successful assisted completion does not establish all four.

## Limits

One hundred examples is a heuristic. One expert can miss other perspectives. Rare serious failures can disappear in aggregate scores. Categorization can reshape initial judgments.

## What to Notice

[Inference] Curator-proposed observation, not a validated measure: What failure did your own reading reveal before categories and scores existed?

## Related

- [[automation-bias]] — related local entry inspected; see rationale and limits above.
- [[metacognitive-demand]] — related local entry inspected; see rationale and limits above.
- [[agency]] — related local entry inspected; see rationale and limits above.
