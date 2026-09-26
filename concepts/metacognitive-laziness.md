---
status: solid
area:
- erosion
- risk
sources:
- Fan et al. (2025)
- Wang & Lajoie (2023)
- Bastani et al. (2025)
- Bartoš et al. (2026)
- Stadler, Bannert & Sailer (2024)
- "Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers. CHI '25."
---

# Metacognitive Laziness

## What It Is

The tendency for AI's convenience to undermine learners' engagement in essential self-regulated learning processes — planning, monitoring, and revision. The learner abdicates metacognitive responsibilities to the tool, not out of inability but out of rational efficiency-seeking. Term coined by Fan et al. (2024).

## Why It Matters

Metacognitive laziness is distinct from simply lacking metacognitive skill. It describes a situation where the capacity for self-regulation exists but goes unexercised because AI makes bypassing it the path of least resistance. This means the problem is not only about training metacognition — it is about designing environments that demand its use even when AI is present.

Fan et al. (2025) provide the first RCT-grade empirical anchor. In a 4-arm randomised trial (N=117) comparing ChatGPT, human expert, writing-analytics checklist, and control, the AI group produced significantly higher essay scores than every other group (~2 points, all p<0.05) but showed no advantage on knowledge gain or knowledge transfer. Process-mining of self-regulated learning behaviour revealed the AI group's regulation was tightly entangled with ChatGPT prompts and showed *fewer* metacognitive transitions (orientation ↔ evaluation) than the human-expert group. This is performance/learning dissociation: AI users produced better outputs while learning less.

Bastani et al. (2025) replicate Fan's lab finding at field scale. In a preregistered RCT with ~1,000 high school math students in Turkey, students given vanilla GPT-4 during practice scored 17% lower than controls on a subsequent unassisted exam. Two analyses (per-problem error-rate × student performance correlation, plus engagement-message classification) jointly support **crutch behavior as the dominant harm pathway** — students treat the AI as a way to bypass the metacognitive work of struggling with problems, not just as an information source that occasionally misleads them via hallucination. Importantly, students did not perceive that they had learned less, indicating the metacognitive layer remained absent rather than triggering self-correction.

Stadler, Bannert & Sailer (2024) found lower self-reported germane cognitive load after ChatGPT-3.5 versus Google research (N=91; M = 3.14 vs. 4.79, η² = 0.27), alongside lower same-session justification quality. The mediation analysis was exploratory. Cognitive-load ratings, Fan's process measures and Bastani's interaction logs are different measures; they do not independently validate a single disengagement mechanism.

## Key Insight

Self-regulated learning (planning, monitoring, revision) itself creates cognitive load (Wang & Lajoie 2023). When AI offers a cheaper path to task completion, learners rationally choose to offload these regulatory processes along with the task itself. The result is a double offloading: both the cognitive work and the metacognitive oversight of that work get delegated to AI.

Fan et al. (2025) define metacognitive laziness as "learners' dependence on AI assistance, offloading metacognitive load and less effectively associating responsible metacognitive processes with learning tasks" — explicitly extending Risko & Gilbert's (2016) cognitive offloading from informational tasks to the metacognitive layer.

A practical implication from the same study: ChatGPT's advantage was strongest on rubric-aligned scoring. The same property that makes AI useful for criterion-driven assessment is what enables metacognitive bypass — students discovered they could optimise the rubric via the AI without exercising the underlying skills. Assessment design that decouples performance from rubric-optimisability is a structural counter-measure.

[Unverified source] No matching local original was found for the attribution below. Its claims and quoted wording are not verified and should not be cited as established evidence.

[Unverified account] Lodge & Loble (2026) note that simply adding SRL prompts failed when AI dominated the interaction (Darvishi et al. 2024); only integrated, non-optional metacognitive pauses successfully countered the effect.

Bartoš et al. (2026) position metacognitive laziness within a broader umbrella explanation for why the published meta-analytic literature on AI-and-learning fails to show robust effects once publication bias is corrected. In the Discussion [p.22], they explicitly invoke "task stewardship" (Lee et al. 2025), cognitive offloading mediation (Gerlich 2025), and reduced engagement / poorer memory encoding under LLM-assisted writing (Kosmyna et al. 2025) as the mechanisms behind the umbrella's null result. The umbrella's bias-adjusted central estimate (SMD = 0.196 [0.000, 0.323]) and extreme heterogeneity (τ = 0.869) at the field level are consistent with metacognitive laziness operating as a systematic counter-force against the surface-level performance gains that AI assistance produces during learning tasks.

Lee et al. (2025) provide field-scale survey evidence for the trust-driven mechanism behind metacognitive laziness. In a survey of 319 knowledge workers using GenAI tools at work at least weekly, a logistic regression across 936 task examples found higher confidence in GenAI strongly predicts *less* enaction of critical thinking (β = −0.69, p < 0.001), while higher confidence in oneself predicts *more* (β = +0.26, p = 0.026). At the qualitative level, 83 of 319 participants (26%) cite trust and reliance on GenAI as their primary inhibitor of critical thinking — workers form a mental model that AI is competent for "simple" tasks, then fail to evaluate output even when the task warrants it. The paper introduces the framing of *task stewardship*: for Analysis, Synthesis, and Evaluation activities, knowledge workers shift "from task execution to task stewardship" — guiding and monitoring AI to produce high-quality outputs while retaining accountability. This stewardship framing is the field-level expression of metacognitive laziness: the worker retains responsibility for output quality but offloads the active engagement that would normally produce it. These studies use different designs and outcomes; together they motivate further tests, not confirmation of a shared causal process.

## Related

- [[metacognition]] - the broader capacity that laziness erodes
- [[performance-paradox]] - metacognitive laziness is a key driver
- [[cognitive-offloading]] - laziness extends offloading to the metacognitive level
- [[fluency-bias]] - AI fluency triggers the laziness
- [[confidence-competence-gap]] - laziness widens the gap
- [[desirable-difficulty]] - SRL effort is itself a desirable difficulty being bypassed
- [[fan-metacognitive-laziness-2025]] - primary empirical source
- [[bastani-guardrails-math-rct-2025]] - field-scale replication with crutch-mechanism evidence
- [[bartos-ai-learning-meta-meta-2026]] - umbrella-level positioning: task stewardship, cognitive offloading, and metacognitive laziness cited as candidate mechanisms behind why the published "AI improves learning" effects fail to consolidate after bias correction
- [[stadler-cognitive-ease-cost-2024]] — CLT-mediator evidence: reduced germane cognitive load fully mediates LLM-induced drops in justification quality (third operationalization of metacognitive disengagement, alongside Fan's process-mining and Bastani's interaction logs)
- [[lee-critical-thinking-survey-2025]] — field-scale survey evidence (N=319, 936 examples): trust-in-GenAI → reduced critical thinking (β = −0.69, p < .001); 83/319 cite trust/reliance as the primary inhibitor; introduces the "task stewardship" framing already cited (via Bartoš 2026) by this concept

## Sources

- [[fan-metacognitive-laziness-2025]] — Fan et al. (2025)
- Wang & Lajoie (2023)
- [[bastani-guardrails-math-rct-2025]] — Bastani et al. (2025)
- [[bartos-ai-learning-meta-meta-2026]] — Bartoš et al. (2026)
- [[stadler-cognitive-ease-cost-2024]] — Stadler, Bannert & Sailer (2024)
- [[lee-critical-thinking-survey-2025]] — Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers. CHI '25.

