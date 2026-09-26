---
status: emerging
area:
- erosion
- risk
sources:
- Bastani et al. (2025)
- Yan et al. (2025)
- Singh Yadav (2026)
- Bartoš et al. (2026)
- Stadler, Bannert & Sailer (2024)
- "Wu, S., Liu, Y., Ruan, M., Chen, S., & Xie, X.-Y. (2025). Human-generative AI collaboration enhances task performance but undermines human's intrinsic motivation. Scientific Reports, 15, 15105. https://doi.org/10.1038/s41598-025-98385-2"
- "Strömberg, Lei & Wu (2026)"
---

# Performance Paradox

## What It Is

AI boosts a learner's immediate performance on a task while simultaneously diminishing the durable learning that the task was designed to produce. Output looks competent; the person behind it is not becoming more competent.

## Why It Matters

The paradox makes AI-induced erosion invisible at the point where it matters most — assessment and evaluation. Short-term metrics (test scores, task completion, output quality) all improve, masking the fact that long-term knowledge construction is being bypassed. This applies beyond education: any professional producing AI-assisted work can appear to perform at a level they cannot sustain independently.

## Key Insight

The paradox resolves an apparent contradiction in AI-and-learning research. Studies showing "positive effects" of AI on learning are often measuring scaffolded performance (the task with AI present), not durable independent capability (performance after AI is removed). Bastani et al. (2025) demonstrated this directly in a preregistered field RCT (~1,000 students, classroom-level randomization across 50 classrooms in a Turkish high school): students with vanilla GPT-4 access scored **+48% on practice problems but −17% on the unassisted exam** versus controls who never had AI. A guardrailed variant ("GPT Tutor": teacher-curated solutions in the prompt + hint-not-answer instructions) produced **+127% on practice and approximately zero effect on the exam** — guardrails essentially neutralized the harm without sacrificing the assistance. The scaffolded performance does not translate into schemas in long-term memory; the paradox is not measurement noise but a structural feature of how AI interacts with learning.

Bastani et al. (2025) [pp.4-5] add a critical compound: **students did not perceive that they had learned less.** GPT Base students reported similar self-assessed learning to controls; GPT Tutor students reported they had learned *more* despite no exam-score advantage. The dissociation is invisible from inside the learning process, which means self-correction loops fail to trigger. External assessment design carries the burden the learner cannot.

Lodge & Loble (2026) argue this is not a measurement error but a structural feature of how AI interacts with learning: AI bypasses the intrinsic cognitive load (desirable difficulties) that builds durable knowledge, while producing outputs that signal mastery.

Singh Yadav (2026) provides a historical grounding through the concept of the "augmentation illusion." Every wave of cognitive technology — writing systems, calculators, GPS, internet search — created the same pattern: performance capability decoupled from underlying competence. AI is the latest and most comprehensive manifestation. The book maps the illusion through four mechanisms: cognitive offloading (reduced internal investment), fluency confusion (ease of performance mistaken for understanding), attribution errors (success credited to self rather than tool), and reduced metacognitive awareness (less confrontation with one's own knowledge gaps). The historical pattern suggests the performance paradox is not unique to AI but a universal principle of cognitive augmentation — AI simply operates across more cognitive domains simultaneously than any previous technology.

Bartoš et al. (2026) provide an umbrella-level statistical anchor. Pooling 1,840 effect sizes from 67 meta-analyses on AI/LLMs and learning, they find that the publication-bias-unadjusted average effect (SMD ≈ 0.629) collapses to SMD = 0.196 [0.000, 0.323] once corrected — about one-third the published magnitude. Crucially, after RoBMA-PSMA correction, **0 out of 44 meta-analyses with at least 10 effect sizes retain strong evidence for the effect** of AI/LLMs on learning, vs. 41/44 in the unadjusted analysis [pp.20-21]. The umbrella does not contradict the performance-paradox framing; it shows that the bulk of "AI improves learning" claims in the published meta-analytic record are scaffolded-performance findings whose effects do not consolidate under bias correction. The Discussion explicitly invokes "task stewardship" (Lee et al. 2025), cognitive offloading mediation (Gerlich 2025), and reduced engagement under LLM-assisted writing (Kosmyna et al. 2025) as the mechanisms behind the non-consolidation [pp.22-23].

Stadler, Bannert & Sailer (2024) operate at a different measurement level than Bastani: rather than scaffolded-vs-unassisted performance gap, they measure the during-task cognitive load and the same-session output quality. In their CHB RCT (N=91 university students, ChatGPT-3.5 vs. Google for a 20-minute socio-scientific search task), LLM users reported lower cognitive load on every facet (ECL η² = 0.09, ICL η² = 0.15, GCL η² = 0.27 — all p < .005) and produced lower-quality justifications (1.20 vs. 1.87 relevant arguments; F = 11.18, p = .001, η² = 0.11). The full mediation through germane cognitive load (β = 0.15, p = .020 indirect; direct path n.s.) names what is bypassed when AI makes the work easy: the active schema-construction processing that translates into output quality. The performance paradox is sharpened: it is not just that scaffolded performance and durable learning dissociate over time — even *within a single session*, when AI reduces effort, the dimension of the output that depends on active processing (depth of justification, integration of arguments) drops in lockstep.

Wu et al. (2025) extend the paradox to the *post-AI* dimension that prior KB sources have not fully captured. Across four pre-registered experiments (total N = 3,562 Prolific UK), GenAI collaboration produced clear immediate-task augmentation: rater-assessed Facebook post quality improved by d = 0.23 (Study 1); LIWC-measured word count of performance reviews increased by d = 1.50 (Study 2) and welcome emails by d = 1.26 (Study 3); analytical content and prosocial/affiliation tone all rose with medium effect sizes. This is the standard "AI augments" finding the paradox sets up. But the spillover did not arrive. Three of four studies found *no* significant transfer of augmentation to subsequent unassisted tasks (Studies 2, 3, and 4 across idea quantity, novelty, usefulness, text length, analytical content, positive tone — all effect sizes |d| < 0.15, mostly non-significant). Study 4 found a small *negative* spillover on text length (Solo-Solo wrote slightly longer than Collab-Solo, d = 0.14, p = .048). Only Study 1 found positive spillover on idea quality (d = 0.29).

This is the paradox's post-AI face: the worker performs better *with* AI but does not retain that performance in subsequent unassisted work. Where Bastani et al. show the gap *during* AI use (practice +48% but exam −17%), Wu et al. show the gap *after* AI use (immediate task gains do not transfer). The two findings together describe a fuller paradox: AI's performance benefit is bounded to its presence, with neither during-AI-learning nor post-AI-skill-transfer reliably operating in the worker's favor. The mechanism Wu et al. propose — that psychological deprivation effects (motivation decline, boredom increase) overshadow GenAI's potential cognitive benefits — converges with the Stadler "germane cognitive load" mediation: when AI removes effort, the active processing that would translate into transfer doesn't happen.

Strömberg, Lei & Wu (2026) extend the [[performance-paradox]] to a 30-month administrative panel of 26,811 Chinese secondary students. Their staggered-adoption analysis estimates +18% homework scores, roughly 30% less completion time and −20% monthly exam scores at 6–10 months after adoption. Score changes are percentages of the baseline mean, not grade percentage points. AI adoption was self-selected and onset retrospectively reported, so causal interpretation depends on parallel-trends and no-confounding assumptions. The much-publicized 18–24% entrance-exam losses concern at least two years of exposure; average entrance-exam effects were nearer −7% in the DID analysis.

The study also shows why homework quality can become a misleading learning signal: among higher-scoring AI users, better homework coexisted with lower exam scores. Outsourcing was inferred from short completion times, not directly observed. Equal homework time was associated with similar exam results; this does not prove that requiring longer homework restores learning.

## The Vicious Cycle

Lodge & Loble (2026) describe how the paradox self-reinforces:

1. Learner seeks efficiency (task completion goal)
2. AI output fluency creates an [[confidence-competence-gap|illusion of competence]]
3. Illusion triggers [[metacognitive-laziness]]
4. More outsourcing follows, eroding the knowledge base
5. Weakened knowledge makes the learner more dependent and less able to judge AI output

## Related

- [[cognitive-offloading]] - the mechanism that produces the paradox
- [[desirable-difficulty]] - what gets bypassed
- [[confidence-competence-gap]] - the subjective experience of the paradox
- [[fluency-bias]] - what makes the paradox invisible
- [[metacognitive-laziness]] - what the paradox enables
- [[capacity-erosion]] - the long-term consequence
- [[novice-vulnerability]] - who is most affected; Singh Yadav's augmentation illusion is most pronounced at early Dreyfus stages
- [[desirable-difficulty]] - Singh Yadav traces a historical arc showing each cognitive technology bypassed the productive struggle that built competence
- [[bartos-ai-learning-meta-meta-2026]] - umbrella-level evidence anchor: published "AI improves learning" effects collapse ~3× under publication-bias correction, supporting the paradox at the field level
- [[stadler-cognitive-ease-cost-2024]] — within-session paradox evidence: LLM-induced drop in cognitive load fully mediates the drop in justification quality
- [[wu-collaboration-motivation-2025]] — pre-registered RCT evidence (N = 3,562) that the paradox extends post-AI: immediate-task augmentation is robust (d up to 1.50) but spillover to subsequent unassisted tasks is largely absent across three of four studies

- [[stromberg-ai-learning-penalty-2026]] — longer-term field evidence with explicit observational limits.

## Sources

- [[bastani-guardrails-math-rct-2025]] — Bastani et al. (2025)
- Yan et al. (2025)
- [[singh-yadav-competency-paradox-2026]] — Singh Yadav (2026)
- [[bartos-ai-learning-meta-meta-2026]] — Bartoš et al. (2026)
- [[stadler-cognitive-ease-cost-2024]] — Stadler, Bannert & Sailer (2024)
- [[wu-collaboration-motivation-2025]] — Wu, S., Liu, Y., Ruan, M., Chen, S., & Xie, X.-Y. (2025). Human-generative AI collaboration enhances task performance but undermines human's intrinsic motivation. Scientific Reports, 15, 15105. https://doi.org/10.1038/s41598-025-98385-2
- [[stromberg-ai-learning-penalty-2026]] — Strömberg, Lei & Wu (2026)

