---
status: solid
area: [preservation]
sources:
  - "Passalacqua et al. (2024)"
  - "Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Heck, S., Mueller, J., Hong, J., Ritchie, S., Belonax, T., Troy, K. K., Amodei, D., Kaplan, J., Clark, J., & Ganguli, D. (2025). Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations. arXiv:2503.04761 [cs.CY], February 11, 2025. Anthropic."
  - "Bainbridge, L. (1983). Ironies of automation. Automatica, 19(6), 775–779."
---

# Partial Automation Principle

## What It Is

Partial automation leaves some tasks to people while automating others. [Inference] Its value for preserving capability depends on whether the retained tasks exercise the skills and process understanding people need, including when automation fails. Simply keeping a person involved does not establish better motivation or long-term outcomes than full automation. Bainbridge (1983) supplies design arguments about these conditions, not a universal comparison of automation levels.

## Why It Matters

[Inference] Where people remain responsible for fallback decisions, workflow design should provide the practice and understanding that responsibility requires. Bainbridge's analysis explains why nominal oversight can be inadequate. The appropriate degree of automation depends on the task; it is not settled by a general instruction to avoid full automation.

## Key Insight

Passalacqua et al. (2024) found that university students trained with AI that supported their decisions later detected errors more accurately without AI than students trained with AI that selected decisions for them. This was a short-term manufacturing quality-control task, not a test of lasting skill erosion or general cognitive decline (PDF p.12, section 5.1.2).

The training conditions also differed in AI reliability: the partial-automation system missed one of six defects, while the fully automated system was always correct. The finding therefore does not isolate decision authority from reliability and exposure to an AI error (PDF pp.9–10).

## The Chain

[Inference] Proposed pathway, not a demonstrated causal law across settings:

```
Full automation
    ↓
Reduced autonomy
    ↓
Lower self-determined motivation
    ↓
Less cognitive engagement
    ↓
Skill deficit over time
```

## Design Implication

When designing AI workflows:
- Keep humans involved in meaningful parts of the process
- Don't optimize purely for efficiency
- Preserve opportunities for practice and judgment
- Human-in-the-loop is not just for safety—it's for capability

Bainbridge (1983, pp. 777–778) adds a condition: the retained human tasks must maintain the skills and process understanding needed when automation fails. Passive monitoring alone does not do this. Where live practice is unsuitable, provide simulation matched to the required skill and practice reasoning about unfamiliar failures. These are context-dependent design recommendations, not evidence for a universal practice frequency or a blanket rule to reduce automation.

## Evidence Quality

Evidence must be interpreted by task and study design. Bainbridge supplies historical design analysis, Passalacqua examines a particular training setting, and Handa describes patterns of use. These are not interchangeable tests of long-term skill or motivation benefits across all AI workflows.

Handa et al. (2025) provide the first production-scale empirical observation that augmentative use is the dominant emergent pattern, not just the normative recommendation. In ~4M Claude.ai conversations classified into five collaboration patterns, **57% are augmentative** (Task Iteration, Learning, Validation) and **43% are automative** (Directive complete-task delegation, Feedback Loop) [p.3]. The paper's authors note that users may iterate on AI outputs outside the chat window, "suggesting that the true proportion of augmentative conversations may be even higher" [p.9] — meaning 57% is a lower bound on partial-automation behavior at scale.

The pattern is not uniform. **Directive (full-delegation) conversations concentrate in writing and content-generation tasks** (e.g., "Draft and optimize professional business email communications") and schoolwork-style tasks. **Feedback Loop conversations concentrate in coding and debugging**. **Task Iteration concentrates in front-end development and professional communication. Learning concentrates in general education and advice-seeking. Validation (smallest category) is largely confined to language translation** [p.9–10]. This gives the partial-automation principle a sharper deployment heuristic: certain task types pull users toward full delegation by default (single-shot writing requests, geometry homework), and design or workflow scaffolding may be most needed there.

Handa's observed mix of augmentative and automative conversations does not establish why users selected those patterns or whether partial automation preserved skill or motivation. It is descriptive evidence, not a test of Bainbridge's recommendations or Passalacqua's training result.

## Related

- [[strategic-alternation]] - how to implement this
- [[cognitive-debt]] - what full automation accumulates
- [[desirable-difficulty]] - why engagement matters
- [[think-first]] - practice that applies this

## Sources

- [[passalacqua-less-ai-2024]] — Passalacqua et al. (2024)
- [[handa-economic-tasks-claude-2025]] — Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Heck, S., Mueller, J., Hong, J., Ritchie, S., Belonax, T., Troy, K. K., Amodei, D., Kaplan, J., Clark, J., & Ganguli, D. (2025). Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations. arXiv:2503.04761 [cs.CY], February 11, 2025. Anthropic.
- [[bainbridge-ironies-automation-1983]] — Bainbridge, L. (1983). Ironies of automation. Automatica, 19(6), 775–779.

