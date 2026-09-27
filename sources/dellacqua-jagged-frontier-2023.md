---
status: solid
area: [risk, preservation]
type: paper
sources:
  - "Dell'Acqua, F., McFowland III, E., Mollick, E., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality. Harvard Business School Working Paper 24-013."
---

# Dell'Acqua et al. (2023) — Navigating the Jagged Technological Frontier

## Citation

Dell'Acqua, F., McFowland III, E., Mollick, E., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality. *Harvard Business School Working Paper* 24-013.

**SSRN:** [papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321)

## Type

Paper (pre-registered field experiment, N=758 BCG consultants)

## Key Insight

Dell'Acqua et al. ran a field experiment with 758 Boston Consulting Group consultants (~7% of BCG's individual contributors) to measure the actual productivity and quality effects of GPT-4 on real consulting work. Three conditions: no AI, GPT-4 access, GPT-4 + prompt engineering overview. 18 realistic consulting tasks within AI's capability frontier, plus one task deliberately outside it.

Two findings define the paper:

1. **Inside AI's capability frontier:** consultants using AI completed **12.2% more tasks**, were **25.1% faster**, and produced **40%+ higher quality** outputs than controls.

2. **Outside the frontier:** consultants using AI were **19 percentage points *less likely*** to produce correct solutions than the no-AI control. AI didn't just fail to help — it actively misled consultants on tasks it couldn't reliably handle, while consultants struggled to detect that they were outside the frontier.

The capability frontier is **jagged** — uneven across tasks that look similar at the surface. There's no clean rule for "this is in vs. out." Consultants couldn't identify the boundary reliably. The metacognitive demand of distinguishing in-frontier from out-of-frontier tasks is what the paper reveals as the central knowledge-worker challenge in the AI era.

A second important finding: the **leveling effect**. Below-average performers gained +43% from AI; above-average performers gained +17%. AI compresses the performance distribution. Whether this is a good outcome depends on what's happening to the *capacity development* of below-average performers.

The paper also identifies two human-AI integration patterns:
- **Centaurs** — divide and delegate; humans do some tasks, AI does others, with clear handoffs.
- **Cyborgs** — fully integrate human and AI work; continuous back-and-forth interleaving.

For human thinking with AI: this is the empirical anchor for both the [[jagged-frontier]] concept and the [[leveling-effect]] concept. The 19pp out-of-frontier degradation is evidence of worse performance with AI on the tested out-of-frontier task — consistent with [[automation-bias]] and [[fluency-bias]] concerns, without isolating those mechanisms.

## Key Passages

> "We suggest that the capabilities of AI create a 'jagged technological frontier' where some tasks are easily done by AI, while others, though seemingly similar in difficulty level, are outside the current capability of AI."
> — Dell'Acqua et al., [p.4] (abstract)

> "For each one of a set of 18 realistic consulting tasks within the frontier of AI capabilities, consultants using AI were significantly more productive (they completed 12.2% more tasks on average, and completed tasks 25.1% more quickly), and produced significantly higher quality results (more than 40% higher quality compared to a control group)."
> — Dell'Acqua et al., [p.4]

> "For a task selected to be outside the frontier, however, consultants using AI were 19 percentage points less likely to produce correct solutions compared to those without AI."
> — Dell'Acqua et al., [p.4]

> "Consultants across the skills distribution benefited significantly from having AI augmentation, with those below the average performance threshold increasing by 43% and those above increasing by 17% compared to their own scores."
> — Dell'Acqua et al., [p.4]

> "Our analysis shows the emergence of two distinctive patterns of successful AI use by humans along a spectrum of human-AI integration. One set of consultants acted as 'Centaurs,'… dividing and delegating their solution-creation activities to the AI or to themselves. Another set of consultants acted more like 'Cyborgs,' completely integrating their task flow with the AI."
> — Dell'Acqua et al., [p.4]

## Relevance

Field-experimental evidence of task-dependent performance gains and losses. Three contributions:

- **Quantifies the jagged frontier.** Inside it, AI increased task completion, speed and rated quality; these are different measures. Outside it, AI is a 19pp accuracy hazard. Same tool, opposite effects, no clean signal of which side you're on.
- **Names the integration patterns.** Centaur vs. Cyborg gives practitioners a vocabulary for thinking about *how* to use AI, not just whether to. The paper finds both patterns can succeed; the failure mode is undifferentiated AI use without a strategy.
- **Empirical foundation for the leveling effect.** Lower performers gain more in absolute terms — looks democratizing. Long-term effects on independent capability were not measured.

## Supports

- [[jagged-frontier]] — primary source for the construct
- [[leveling-effect]] — quantified pattern (+43% vs +17%)
- [[metacognitive-demand]] — the boundary-detection problem is a metacognitive demand
- [[capacity-erosion]] — possible longer-term concern, not measured here
- [[automation-bias]] — out-of-frontier accuracy drop is consistent with overreliance; a single mediator was not isolated
- [[mollick-management-ai-superpower-2026]] — Mollick is a co-author here; his later equation extends this work

## Contradicts / Extends

- Related to [[bo-sycophancy-novices-2026]], which tests sycophancy in a different task rather than the same frontier contrast.
- Extends [[goddard-automation-bias-2012]] — Goddard documented automation bias in clinical decision support (~26% RR for following bad advice); Dell'Acqua shows the same pattern operating at 19pp accuracy degradation in consulting.

## Open Questions

- Boundary detection: the paper shows consultants couldn't identify which tasks were outside the frontier. What interventions could improve real-time boundary detection?
- The leveling effect short-term vs. long-term: gains compress in the moment, but does capacity development compress too? The paper's design can't address this — needs longitudinal follow-up.
- Centaur vs. Cyborg: the paper identifies both as successful patterns. What determines which is appropriate for which work? Not yet answered.
