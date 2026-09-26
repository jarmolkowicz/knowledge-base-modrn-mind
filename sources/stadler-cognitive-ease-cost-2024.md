---
status: solid
area: [erosion, risk, preservation]
type: paper
sources:
  - "Stadler, M., Bannert, M., & Sailer, M. (2024). Cognitive ease at a cost: LLMs reduce mental effort but compromise depth in student scientific inquiry. Computers in Human Behavior, 160, 108386. https://doi.org/10.1016/j.chb.2024.108386"
---

# Stadler, Bannert & Sailer (2024) — Cognitive Ease at a Cost

## Citation

Stadler, M., Bannert, M., & Sailer, M. (2024). Cognitive ease at a cost: LLMs reduce mental effort but compromise depth in student scientific inquiry. *Computers in Human Behavior*, 160, 108386.

**DOI:** [10.1016/j.chb.2024.108386](https://doi.org/10.1016/j.chb.2024.108386)
**License:** CC BY 4.0 (open access)
**OSF:** [osf.io/jpxyt](https://osf.io/jpxyt) (instructions, scales)

## Type

Paper (between-subjects RCT, N=91 university students; ANCOVA controlling for prior knowledge; mediation analysis on the LLM → justification-quality pathway through germane cognitive load).

## Key Insight

In a randomized comparison, 91 university students researched sunscreen nanoparticles for 20 minutes using ChatGPT-3.5 or Google, then wrote a recommendation with justifications without notes. LLM users reported lower extraneous, intrinsic and germane cognitive load (η² = 0.09, 0.15 and 0.27) and included fewer relevant arguments in their recommendations (1.20 vs. 1.87; F = 11.18, p = .001, η² = 0.11).

An exploratory mediation analysis found a significant indirect path through self-reported germane cognitive load (β = 0.15, p = .020) and a nonsignificant direct path (β = 0.19, p = .095). The authors call this full mediation. Randomizing the research tool does not randomize the mediator: these results do not establish that load caused the difference, identify schema construction directly, or show that increased effort would improve learning.

The study measured same-session justification quality, not delayed retention, lasting skill loss, processing fluency or metacognitive monitoring. Recommendation categories did not differ significantly in their distribution (χ² = 1.78, p = .411); this is not proof of equivalence or of unchanged information exposure.

## Key Passages

> "Results indicated that students using LLMs experienced significantly lower cognitive load. However, despite this reduction, these students demonstrated lower-quality reasoning and argumentation in their final recommendations compared to those who used traditional search engines."
> — Stadler et al., [p.1, abstract]

> "The strongest difference was found for GCL, the smallest for ECL."
> — Stadler et al., [p.5]

> "We found a significant indirect effect (β = 0.15; p = 0.020) and no significant direct effect (β = 0.19; p = 0.095) indicating a full mediation of the effect of the different research conditions on the quality of the arguments and reasoning presented through GCL."
> — Stadler et al., [p.5]

> "Contrary to H3, students using LLMs did not show less variation in their recommendations than students using traditional search engines (χ²(2) = 1.78; p = 0.411). In fact, the distribution of recommendations was similar for the two groups."
> — Stadler et al., [p.5]

> "While LLMs can reduce the cognitive load, which is theoretically beneficial for learning, the nature of the content delivered and the interaction required to engage with that content also play crucial roles. The ease of obtaining answers from LLMs does not necessarily translate to deeper learning or better-quality outcomes."
> — Stadler et al., [p.5]

> "Specifically, the results point towards the importance of inferring cognitive processes (e.g., reorganizing, reflecting; Chi & Wylie, 2014) when using digital technologies that are associated with higher learning outcomes (Sailer et al., 2024). While recall of knowledge from LLMs might more closely be related to shallow learning processes, inferring knowledge from different sources might more closely be related to deep learning processes."
> — Stadler et al., [p.5]

## Relevance

- Separates ease of a research task from the quality of the justifications produced in that session.
- Provides a randomized tool comparison and an exploratory account involving self-reported cognitive load.
- Leaves durable learning and the proposed causal mechanism untested. Results from this task and interface do not establish that all LLM-assisted work reduces understanding.

## Supports

- [[fluency-bias]] — related concern about ease, but processing fluency was not measured
- [[desirable-difficulty]] — lower load coexisted with weaker justifications; more difficulty was not itself tested as an intervention
- [[cognitive-debt]] — no longitudinal measure of accumulated cost
- [[metacognitive-laziness]] — cognitive-load ratings are distinct from metacognitive behaviour
- [[performance-paradox]] — distinguishes task ease from same-session quality, not assisted performance from delayed learning
- [[cognitive-friction]] — [Inference] relevant to effort, without measuring meaning or productive friction directly
- [[cognitive-offloading]] — [Inference] one possible interpretation, not an isolated causal mechanism
- [[capacity-erosion]] — no evidence here of lasting skill erosion

## Contradicts / Extends

- [[kosmyna-cognitive-debt-2025]] uses EEG and other outcomes. This study does not establish a mediator connecting its findings to Kosmyna's.
- [[bastani-guardrails-math-rct-2025]] includes a later unaided exam; Stadler's outcome is same-session justification quality.
- [[fan-metacognitive-laziness-2025]] examines learning-process behaviour; germane-load ratings do not establish the same process.
- [[anderson-homogenization-2024]] concerns idea similarity. Stadler's nonsignificant difference in recommendation categories addresses a different outcome.

## Open Questions

- Would results persist on a delayed unaided assessment or transfer task?
- Would mediation replicate in a larger sample, and would an intervention targeting the proposed process change outcomes?
- How do prompting, interface design and model capabilities affect results? This study does not test newer systems or show that challenge prompts restore learning.
- Could repeated use change recommendation diversity even though no difference was detected in this session?
- How do confidence, ownership and measured cognitive processes relate to self-reported load?
