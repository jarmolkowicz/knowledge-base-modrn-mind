---
status: emerging
area:
- preservation
sources:
- Sabrina Ramonov. The ULTIMATE AI Coding Guide. 2025-07-05. https://www.sabrina.dev/p/ultimate-ai-coding-guide-claude-code
- Farhan Thawar, interviewed by Lenny Rachitsky. How Shopify builds a high-intensity culture | Farhan Thawar (VP and Head of Eng). 2024-12-19.
  https://www.youtube.com/watch?v=C_lhMOjG7PE
- Cal Newport, reporting an anonymous engineer. On AI Coding and Its Discontents. 2026-08-10. https://calnewport.com/on-ai-coding-and-its-discontents/
source_entries:
- newport-038-on-ai-coding-and-its-discontents-2026
- ramonov-402-the-ultimate-ai-coding-guide-2025
- lenny-636-how-shopify-builds-a-high-intensity-2024
intended_outcomes:
- work-quality
- understanding
---

# Review AI code against independent checks

Title is editorial, not a validated named method.

## Use When

You can assess the code and expected behavior, or work with someone who can.

## Try It

1. Review the plan and alternatives; keep changes inspectable.
2. Write or review expected results and edge cases independently of the generated implementation. Ask AI to help implement and test.
3. Inspect actual changes, run checks and manually exercise important behavior. Revise or reject failures.
4. Optional, from Farhan Thawar: another person reviews AI suggestions with you; jointly accept, rewrite or discard them.

## Origin

Sabrina Ramonov. The ULTIMATE AI Coding Guide. 2025-07-05. https://www.sabrina.dev/p/ultimate-ai-coding-guide-claude-code

Locators in `raw/ramonov-402-the-ultimate-ai-coding-guide-2025/source.md`: L42–44: plan and alternatives; L130–161: independently expected test values and edge cases; L283–298: small changes and reuse; L310–331: manual tests, review, revisions.

Farhan Thawar, interviewed by Lenny Rachitsky. How Shopify builds a high-intensity culture | Farhan Thawar (VP and Head of Eng). 2024-12-19. https://www.youtube.com/watch?v=C_lhMOjG7PE

Locators in `raw/lenny-636-how-shopify-builds-a-high-intensity-2024/source.md`: L187–247, 00:22:30–00:29:18: pair-programming exchange; L238: two humans accept, reject or rewrite AI suggestions.

Cal Newport, reporting an anonymous engineer. On AI Coding and Its Discontents. 2026-08-10. https://calnewport.com/on-ai-coding-and-its-discontents/

Locators in `raw/newport-038-on-ai-coding-and-its-discontents-2026/source.md`: L15–35: initial speed estimate, two crashes, hard review; L39–41: return to manual development with narrow assistance.

Source passages are paraphrased. Steps arrange the cited guidance; editorial additions are marked [Inference]. Support and failure cases are not independent validation.

## Evidence and Rationale

**Basis:** Experienced developer’s proposed routine and personal practice.

**Observed or reported:** Ramonov describes expert review and frequent revision. Thawar advocates two humans judging suggestions. Newport supplies an anonymous failure account. No controlled productivity gain is established.

**Related research:** [[shen-skill-formation-2026]] concerns immediate skill formation under specific assistance patterns. Correct software, felt understanding and unaided ability remain distinct.

**Untested:** No direct evaluation of this complete routine was found in the reviewed material. Output quality, later unaided capability, felt competence and calibrated confidence are separate; successful assisted completion does not establish all four.

## Limits

Generated tests can encode the same mistake as generated code; two humans can share blind spots. Expertise is required. This is not a security or production-readiness guarantee; explanations do not expose internal reasoning.

## What to Notice

[Inference] Curator-proposed observation, not a validated measure: Could you explain the expected behavior and find an error without consulting the same model?

## Related

- [[shen-skill-formation-2026]] — related local entry inspected; see rationale and limits above.
- [[automation-bias]] — related local entry inspected; see rationale and limits above.
- [[metacognitive-demand]] — related local entry inspected; see rationale and limits above.

## Intended outcomes

[Inference] Primary: work-quality. Secondary: understanding. These are intended benefits, not demonstrated effects.

## Source roles

- [[newport-038-on-ai-coding-and-its-discontents-2026]] — counterexample.
- [[ramonov-402-the-ultimate-ai-coding-guide-2025]] — origin.
- [[lenny-636-how-shopify-builds-a-high-intensity-2024]] — support.

## Sources

- [[newport-038-on-ai-coding-and-its-discontents-2026]]
- [[ramonov-402-the-ultimate-ai-coding-guide-2025]]
- [[lenny-636-how-shopify-builds-a-high-intensity-2024]]

Recorded citations:

- Sabrina Ramonov. The ULTIMATE AI Coding Guide. 2025-07-05. https://www.sabrina.dev/p/ultimate-ai-coding-guide-claude-code
- Farhan Thawar, interviewed by Lenny Rachitsky. How Shopify builds a high-intensity culture | Farhan Thawar (VP and Head of Eng). 2024-12-19. https://www.youtube.com/watch?v=C_lhMOjG7PE
- Cal Newport, reporting an anonymous engineer. On AI Coding and Its Discontents. 2026-08-10. https://calnewport.com/on-ai-coding-and-its-discontents/

