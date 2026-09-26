---
status: solid
area: [erosion, risk, preservation]
type: paper
sources:
  - "Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Marimane, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. Proceedings of the National Academy of Sciences, 122(26), e2422633122."
---

# Bastani et al. (2025) — GenAI Without Guardrails Can Harm Learning

## Citation

Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Marimane, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *Proceedings of the National Academy of Sciences*, 122(26), e2422633122.

**DOI:** [10.1073/pnas.2422633122](https://doi.org/10.1073/pnas.2422633122)

**Preregistered:** [aspredicted.org/4DL_Q3J](https://aspredicted.org/4DL_Q3J)

## Type

Paper (preregistered field RCT; ~1,000 students across 50 classrooms in a large Turkish high school, Fall 2023-24; classroom-level randomization across three arms, four sessions covering ~15% of math curriculum)

## Key Insight

In a preregistered classroom experiment, GPT Base improved assisted practice scores but reduced subsequent unaided exam scores relative to control. GPT Tutor produced larger assisted gains and no statistically detectable exam penalty or advantage.

The study involved roughly 1,000 students in about 50 classes at one Turkish high school. Each of four 90-minute sessions included instruction, practice and an immediate unaided exam. These are short-term learning outcomes, not a delayed test of durable skill loss.

| Arm | Assisted practice vs. control | Same-session unaided exam vs. control |
|---|---|---|
| GPT Base | +48% relative (p<.01) | -17% relative (p<.05) |
| GPT Tutor | +127% relative (p<.01) | -0.004 on the 0-1 score scale (SE .013); not significant |

Tutor's -0.004 coefficient is -0.4 percentage points, not a relative -0.4% change. The control exam mean was 0.321. A nonsignificant contrast does not establish statistical equivalence or prove absence of harm.

GPT Tutor combined instructions to give hints rather than answers with teacher-provided correct solutions, common mistakes and feedback. The trial tested this package; it did not separately establish that both components were necessary.

Interaction analysis and error-rate comparisons support the authors' interpretation that using GPT Base as a crutch contributed to the exam deficit. This is not a separately randomized test isolating a single mediator. Self-reported learning did not track the exam pattern: GPT Base students rated learning similarly to controls, while GPT Tutor students rated it higher without a corresponding exam advantage. This cautions against relying on self-report alone, not against every learner's ability to self-correct.

## Key Passages

> "Without guardrails, students attempt to use GPT-4 as a 'crutch' during practice problem sessions, and subsequently perform worse on their own. Thus, decision-makers must be cautious about design choices underlying generative AI deployments to preserve skill learning and long-term productivity."
> — Bastani et al., [p.1, abstract]

> "On the exam, students in the GPT Base arm perform statistically significantly worse than students in the control arm by 17%; this negative effect is essentially eradicated in the GPT Tutor arm, though we still do not observe a positive effect."
> — Bastani et al., [p.2]

> "An analysis of student interactions shows that students often use GPT Base as a 'crutch' by asking for and copying solutions, but they use GPT Tutor in more substantive ways like asking for help or independently attempting answers. Finally, we find evidence that students do not perceive any reduction in their learning or subsequent performance as a consequence of copying solutions, suggesting they are not aware of how generative AI can impede their learning."
> — Bastani et al., [p.2]

> "These results demonstrate an inherent tradeoff in access to generative AI tools: While these tools can substantially improve human performance when access is available, they can also degrade human learning (particularly when appropriate safeguards are absent), which may have a long-term impact on human performance."
> — Bastani et al., [p.4]

> "Both GPT Base and GPT Tutor reduced grade dispersion in the assisted practice sessions, matching prior findings that generative AI assistance reduces the 'skill gap' by providing the largest benefits for the weakest students. However, we find no significant effect on HHI for the unassisted exam — i.e., the reduction in the skill gap does not persist when access to AI is removed."
> — Bastani et al., [p.4]

> "Our findings suggest that the second explanation (i.e., students using GPT Base as a crutch) is the main mechanism by which GPT Base impedes student learning."
> — Bastani et al., [p.5]

## Relevance

- Distinguishes assisted practice performance from same-session unaided performance.
- Provides a tested example of combined tutor design, not a universal guardrail guarantee.
- Shows that reported learning and assessed learning can diverge.
- [Inference] Unaided assessment may help evaluate an AI-supported learning design. This study did not test [[strategic-alternation]] or [[think-first]] as interventions.

## Supports

- [[performance-paradox]] - a specific assisted-unaided dissociation
- [[metacognitive-laziness]] - related interpretation, not replication of Fan's measures
- [[novice-vulnerability]] - evidence from high-school mathematics, not all novice tasks
- [[cognitive-offloading]] - solution copying is one observed interaction pattern
- [[confidence-competence-gap]] - self-reported learning did not track assessed outcomes
- [[capacity-erosion]] - raises longer-term questions; does not demonstrate durable loss
- [[desirable-difficulty]] - related learning theory, not proof that all difficulty is useful
- [[fluency-bias]] - not directly measured as a mediator here
- [[automation-bias]] - an analogy discussed in the paper, not an identical experimental mechanism

## Contradicts / Extends

- [[fan-metacognitive-laziness-2025]] found better essay revision without a statistically significant learning difference. Bastani found a negative unaided exam contrast for GPT Base; these are related but distinct results.
- [[kosmyna-cognitive-debt-2025]] examines writing and neural measures. It should not be treated as an independent measurement of the same mechanism without a direct test.
- [[bjork-desirable-difficulties-2011]] provides a distinction between performance and learning, not a guarantee that removing difficulty harms learning.
- [[parasuraman-riley-automation-1997]] supplies historical automation analogies, not proof of identical mechanisms.
- [[leveling-effect]]: assisted grade dispersion fell, but no significant corresponding exam dispersion effect was detected. This qualifies extrapolation from [[dellacqua-jagged-frontier-2023]] to retained learning.

## Open Questions

- Do these same-session differences persist, diminish or grow over longer periods?
- Which Tutor components account for its results, and in which tasks?
- Can a design improve unaided learning beyond control, rather than merely show no detected deficit?
- Do adult professional tasks show comparable effects?
- Can behavioral measures clarify the relationship between perceived and assessed learning?
