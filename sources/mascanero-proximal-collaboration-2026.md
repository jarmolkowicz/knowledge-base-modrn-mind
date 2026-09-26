---
status: solid
area: [risk, erosion]
type: paper
sources:
  - "Mascareño, J., Wörtler, B., Przegalińska, A., & Ciechanowski, L. (2026). When proximal collaboration with AI hinders innovation: The moderating role of idea originality and reliance on AI. Computers in Human Behavior Reports, 22, 101054."
---

# Mascareño et al. (2026) — When Proximal Collaboration With AI Hinders Innovation

## Citation

Mascareño, J., Wörtler, B., Przegalińska, A., & Ciechanowski, L. (2026). When proximal collaboration with AI hinders innovation: The moderating role of idea originality and reliance on AI. *Computers in Human Behavior Reports*, 22, 101054.

**DOI:** [10.1016/j.chbr.2026.101054](https://doi.org/10.1016/j.chbr.2026.101054)

(Open access, CC BY 4.0. University of Groningen + Kozminski University + MIT Center for Collective Intelligence.)

## Type

Paper (one-factorial between-subjects experiment, N=221 employees; multiple regression with interaction tests; rater-based assessment of idea selection + idea implementation outcomes)

## Key Insight

The literature on AI's impact on innovation has overwhelmingly focused on **idea generation** — does AI help people produce more or better ideas? Mascareño et al. argue this is only the first stage of innovation; the harder downstream stages are **idea selection** (evaluating which ideas to pursue) and **idea implementation** (turning chosen ideas into action). Their experiment tests AI's effects on these neglected stages and finds a sharp inversion of the dominant narrative.

The construct they introduce: **proximal human-AI collaboration** — close, sustained interaction with AI systems during collaborative work, distinct from prior research's focus on configuration questions (who does what role). Proximity is *relational* — how tightly coupled human and AI processes are during the task — not structural.

The theoretical anchor is Distributed Cognition (Hutchins, 1995): when cognition and decision-making are spread across human and AI agents, two things change. First, **individual accountability weakens** because responsibility is shared with a non-accountable system. Second, **attentional focus on execution diminishes** because the human's role becomes one of monitoring rather than producing.

Findings (N=221 employees, between-subjects high vs. low proximity manipulation):

1. **Proximal collaboration reduced idea selection** — particularly when ideas were low in originality. High-originality ideas commanded enough attention to overcome the proximity effect; low-originality ideas got worse selection decisions when AI was tightly coupled to the process.
2. **Proximal collaboration reduced idea implementation** — but the effect weakened as reliance on AI's input increased. Counterintuitively, *more* AI reliance during implementation partially rescued the proximal-collaboration penalty: when humans deferred to AI's specific recommendations, implementation was less impaired than when they remained ambivalent.

Together these findings suggest that AI's effects on innovation are stage-specific and configuration-sensitive in ways prior research missed. The "AI helps innovation" assumption (Wilson & Daugherty 2018) is an over-generalization that conflates idea-generation benefits with downstream-stage costs. Proximal collaboration may *help* generation but *hurt* selection and implementation.

For human thinking with AI: this is the cleanest empirical case in the KB for **stage-specific cost-benefit asymmetry** in human-AI collaboration. It complements [[creativity-diversity-paradox]] (Doshi & Hauser's individual-vs-collective tradeoff in idea generation) by adding a within-individual, across-stages asymmetry. It supports the [[strategic-alternation]] argument: not all collaboration modes work equally across all task stages, and design must be stage-aware.

## Key Passages

> "Although the importance of human–AI collaboration for organizational performance is increasingly acknowledged, its relationship with innovation remains fragmented. Based on tenets of Distributed Cognition theory, we predict that proximal human–AI collaboration impairs key innovation behaviors, namely idea selection and idea implementation."
> — Mascareño et al., [p.1, abstract]

> "Drawing from the tenets of Distributed Cognition theory (Hutchins, 1995), we argue that distributing cognition and decision-making across human and AI agents can lead to weakened individual accountability (Lyons & Guznov, 2019) and diminished attentional focus on execution (Fan et al., 2017), which are important for idea selection and implementation."
> — Mascareño et al., [p.1]

> "Proximal human–AI collaboration decreased idea selection, particularly when idea originality was low. The results further showed that proximal human–AI collaboration reduced idea implementation conditional on reliance on AI, with the negative effect weakening as reliance increased."
> — Mascareño et al., [p.1, abstract]

> "Our results challenge the prevailing — yet largely untested — assumption that human–AI collaboration inherently facilitates innovation (Wilson & Daugherty, 2018). Rather than uniformly improving innovation outcomes, collaboration with AI introduces coordination dynamics that appear to undermine evaluative and implementation processes."
> — Mascareño et al., [p.7]

> "Based on our results, however, we recommend that organizations design workflows that promote interdependence to mitigate the potential downsides of proximal human–AI collaboration."
> — Mascareño et al., [p.8]

> "Organizations should prioritize developing employees' critical assessment skills during the implementation phase. Such training enables individuals to discern when to rely on AI input and when to apply their own judgment, ensuring that AI supports rather than undermines effective implementation."
> — Mascareño et al., [p.8]

## Relevance

Three load-bearing contributions:

- **Stage-specific cost asymmetry, measured.** Most KB evidence treats "AI in work" as monolithic. Mascareño et al. show that AI's effect direction *flips* across stages within a single task: helpful for generation, harmful for selection and implementation. This is empirically novel and changes the frame for [[strategic-alternation]] practice — alternation should be stage-aware, not just session-aware.
- **Names the proximity dimension.** Prior literature focused on configuration (who has which role); Mascareño et al. operationalize *closeness* of interaction as a measurable variable with downstream effects. This is a new variable for designers and practitioners to think about explicitly.
- **Distributed Cognition mechanism.** Provides a theoretical bridge between the broader cognitive-science literature on distributed cognition and the KB's existing entries on accountability/agency erosion. The mechanisms — weakened individual accountability + diminished attentional focus — connect [[agency]], [[moral-crumple-zone]], [[hohenstein-crumple-zone-2020]], and [[performance-paradox]] under one theoretical umbrella.

## Supports

- [[creativity-diversity-paradox]] — Doshi & Hauser found a generation-stage trade-off; Mascareño et al. extend to selection + implementation stages
- [[performance-paradox]] — proximity-driven implementation decline is a stage-specific manifestation of the paradox
- [[agency]] — accountability weakening under distributed cognition
- [[hohenstein-crumple-zone-2020]] - a brief interpersonal attribution experiment, not institutional evidence for the same accountability mechanism.
- [[strategic-alternation]] — implications for stage-aware alternation design
- [[judgment]] — implementation requires critical assessment that AI can crowd out
- [[novice-vulnerability]] — proximity penalty likely worse for those with weaker domain judgment (untested but predicted)
- [[human-ai-complementarity]] — Mascareño et al. argue complementarity is stage-dependent; crude proximity often defeats it

## Contradicts / Extends

- Extends [[dellacqua-jagged-frontier-2023]] — Dell'Acqua showed AI helps creativity in consultant work; Mascareño et al. show this benefit is offset by selection/implementation costs. The "frontier" is jagged in stage-space, not just task-space.
- Related to [[fan-metacognitive-laziness-2025]] and [[bastani-guardrails-math-rct-2025]]: task regulation, learning outcomes and idea implementation are distinct measures. Their findings do not establish one shared engagement-deficit mechanism.
- Modifies [[parasuraman-riley-automation-1997]]'s framework — proximal collaboration is a finer-grained variable than misuse/disuse/abuse; it operates within the "use" mode by varying the closeness of coupling.

## Open Questions

- The high vs. low proximity manipulation collapses a continuum. What does the dose-response curve look like across intermediate proximity levels (competing → supplementing → interdependent → hybrid, in Sowa et al.'s typology)?
- The reliance-on-AI moderator is intriguing: high reliance partially rescued implementation but the paper doesn't disentangle whether this is because AI's specific recommendations were good or because deference avoided indecision. Future work could vary AI quality independently of reliance.
- Field replication needed: lab manipulation may not capture the dynamic, evolving proximity of real organizational collaborations.
- The proximity construct is theoretically rich but operationally narrow here. A next study could examine how teams *choose* proximity levels organically and whether self-selected proximity differs from assigned proximity in its effects.
