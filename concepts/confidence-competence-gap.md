---
status: solid
area: [erosion]
sources:
  - "Scispace Literature Synthesis (2025)"
  - "Tankelevitch et al. (2024)"
  - "Shaw & Nave (2026)"
  - "He, Kuiper, & Gadiraju (2023)"
  - "Leonardi & Leavell (2026)"
  - "Reich & Teeny (2026)"
  - "Keshky (2026)"
  - "Han, Z., Song, G., Zhang, Y., & Li, B. (2025)"
  - "Fernandes et al. (2026)"
  - "Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers. CHI '25."
  - "Messeri, L. & Crockett, M. J. (2024). Artificial intelligence and illusions of understanding in scientific research. Nature, 627, 49–58."
---

# Confidence-Competence Gap

## What It Is

AI creates a "skill illusion"—people feel competent when they're not. The gap between confidence and actual capability widens with AI use because correct outputs get attributed to personal understanding.

## Why It Matters

This is the hidden erosion mechanism. You don't notice capability degrading because AI keeps producing good outputs. The gap only becomes visible when you try to work without AI—and by then, significant erosion may have occurred.

Shaw & Nave (2026) provide direct experimental evidence of this gap in real-time. AI access inflated confidence by ~12 percentage points (Study 1: 77.0% AI-assisted vs 65.3% brain-only, Hedges' g = 0.54), despite approximately half of AI outputs being deliberately wrong. Critically, no statistically significant confidence decline was detected as faulty trials increased (p=.202). Per-item confidence in Study 3 was higher on AI-assisted trials (82.2%) than brain-only trials (77.5%), and did not vary between AI-accurate and AI-faulty trials. People felt equally confident whether AI helped or hurt them.

He et al. (2023) demonstrate a specific instance of the confidence-competence gap: the Dunning-Kruger Effect in AI-assisted decision making. In their study (N = 249), participants who overestimated their own competence (bottom performance quartile with inflated self-assessment) under-relied on AI — dismissing accurate AI predictions because they overrated their own ability. This shows the gap operates in both directions: AI can inflate confidence (Shaw & Nave, 2026), but pre-existing overconfidence was associated with under-reliance on accurate advice.

Fernandes et al. (2026) provide the first computational-model decomposition of the gap under generative-AI use, across two large studies on logical-reasoning tasks (Study 1 N = 246; Study 2 N = 452 randomized with monetary incentives). AI use improved task performance by ~3 points (out of 20), while AI users overestimated their actual performance by ~4 points. These are different comparisons, not quantities to subtract from one another. A Bayesian model separated bias (*b_k*, uniform overestimation) from noise (*σ_k*, skill-scaled miscalibration). Under AI use, the noise parameter collapsed to ~1 (95% HDI [0.84, 1.19]) while the no-AI group's σ remained at 1.78 — meaning AI does not correct overconfidence for low performers; it raises them to a uniform high baseline so that everyone overestimates roughly equally. The classic Dunning–Kruger gradient disappears under AI, replaced by uniform overestimation across skill levels.

Fernandes et al. also report a counterintuitive moderation finding: higher self-rated AI literacy correlated with *lower* metacognitive accuracy (overall SNAIL × overestimation: *r* = .21 in Study 1, *r* = .20 in Study 2; both *p* < .01). The Technical Understanding subscale (familiarity with prompting, parameters, API workflows) carried the strongest effect, while Critical Appraisal and Practical Application subscales correlated with higher mean confidence without improving discrimination (AUC). The authors interpret this through the illusion of explanatory depth (Fisher & Oppenheimer, 2021): procedural fluency provides a misleading sense of ability. This challenges the assumption that AI-literacy training is uniformly protective against the gap. Study 2 showed no calibration improvement relative to Study 1 despite an accuracy bonus. That cross-study comparison does not isolate incentives or rule out effort as a contributing factor.

Lee et al. (2025) extend the confidence-competence gap from lab to real-world workflows. In a survey of 319 knowledge workers (936 GenAI task examples, mixed-methods, CHI '25), a random-intercepts logistic regression revealed a confidence pair: **confidence in AI predicts less enaction of critical thinking** (β = −0.69, p < 0.001), while **confidence in self predicts more** (β = +0.26, p = 0.026; confidence in evaluating AI: β = +0.31, p = 0.046). Higher overall trust in GenAI also flattens perceived effort across four of six Bloom-level cognitive activities (Knowledge β = −0.12, Application β = −0.17, Analysis β = −0.12, Evaluation β = −0.24, all p < 0.05 corrected). At the qualitative level, 83 of 319 participants cite trust and reliance on GenAI as their primary critical-thinking inhibitor. The pair sharpens the gap mechanism: it is not just that AI inflates confidence regardless of accuracy (Shaw & Nave) or that AI use produces uniform high-baseline overestimation (Fernandes); the *direction* of confidence matters. Domain expertise (confidence-in-self) protects, AI-confidence undermines — and the two operate independently in the regression. Field-level evidence converges with the lab.

Leonardi & Leavell (2026) extend the confidence-competence gap to the organizational level through the concept of [[artificial-certainty]]. In their comparative ethnography, non-expert stakeholders who encountered AI-generated simulations believed they fully understood complex urban planning dynamics — "knowing enough to be dangerous." The gap was not between a user's confidence and their ability to use AI, but between stakeholders' confidence in understanding complex systems and their actual domain expertise. When process experts amplified AI capabilities (enhancement mode), stakeholders mistook detailed representations for reality and questioned whether expert guidance was necessary at all.

Messeri & Crockett (2024) extend the confidence-competence gap to the level of an entire knowledge-production community. In their analysis of AI in scientific research, the same mechanism that inflates individual confidence (fluent, reductive, quantitative outputs feel like understood phenomena) operates at field scale: scientists who use AI Quants for prediction tasks come to believe they understand the underlying phenomena better than they do, and the resulting "prediction–explanation fallacy" propagates through citation networks. The KB cluster confidence-competence-gap → [[artificial-certainty]] → [[scientific-monoculture]] now spans three nested levels of analysis: individual (Shaw & Nave, Fernandes et al., He et al.), organizational (Leonardi & Leavell), and knowledge-production-system (Messeri & Crockett).

Reich & Teeny (2026) identify a second mechanism that widens the confidence-competence gap: **social comparison**. Beyond misattributing AI-assisted performance to personal skill, mere exposure to AI-labeled creative content inflates self-confidence through downward comparison — people perceive gen-AI as a lower social referent for creative tasks and consequently rate their own abilities higher. This operates without any AI assistance or collaboration; seeing AI output is sufficient. The effect is domain-specific: it emerges in creative domains but attenuates in fact-based domains where AI is perceived as an equal or superior referent (N = 6,801 across 11 experiments).

Keshky (2026) provides SEM-level structural evidence for the confidence-competence gap through the construct of "illusory competence inflation" (N=393, postgraduate students). The study identifies four dimensions of inflated competence beliefs during AI use:
1. **Overestimation of self-understanding** — believing one has deeper knowledge than one actually possesses
2. **Illusory self-efficacy** — attributing AI-assisted results to personal capability
3. **Resistance to feedback** — rejecting correction that contradicts inflated self-assessment
4. **Uncritical reliance on AI** — accepting AI output without verification

Keshky's cross-sectional model associated dependence with illusory competence (β=.90), potentially reflecting some scale overlap. The indirect association with intellectual identity distortion was β=.35; the reported p-value differs across sections (.04/.05). This is not an established causal or temporal mediation chain.

The study measures reported intellectual identity distortion through three dimensions: dissolution of the thinking self, retreat of knowledge ownership and disturbance of cognitive self-concept. It does not show how these develop over time or that inflated confidence causes them.

## Key Insight

[Speculation] One possible mechanism, not a verified general sequence:
1. AI produces correct outputs
1b. Shaw & Nave (2026) reveal an additional mechanism: AI doesn't just produce correct outputs that get misattributed — it produces *confident, fluent* outputs that inflate the user's sense of certainty regardless of accuracy. The confidence boost is not contingent on outcomes. This means the gap can widen even in a single session, not just over time.
2. User attributes success to own understanding
3. Delayed/absent feedback provides no correction signal
4. Confidence stays high while competence declines
5. Gap widens invisibly until tested

Confidence alone does not establish retained skill. An unaided assessment can test capability; the cited studies do not establish that degradation is always unnoticed until assistance is removed.

Han et al. (2025) provide longitudinal evidence (N=442, 3-wave) for a mechanism that widens the confidence-competence gap: AI usage boosts self-efficacy, which increases willingness to take risks. Critically, for employees with low learning goal orientation, the self-efficacy boost does not translate into genuine risk-taking through the mediated path (CI includes zero) — suggesting their confidence is externally dependent on AI rather than rooted in internalized capability. This maps to the gap mechanism: AI makes people feel more capable and more willing to act on that feeling, even when the capability is borrowed.

## Metacognitive Illusion

Traditional metacognitive tools assume direct engagement with the task. When AI does the work, you think you understand because the output is correct—but you didn't build the understanding that produced it.

## Why Detection Is Hard

- AI outputs look like your outputs
- Success reinforces the illusion
- No natural feedback loop to correct miscalibration
- Testing yourself requires deliberate effort

Keshky includes resistance to feedback as a self-report scale dimension. This does not demonstrate a self-reinforcing causal process in which the gap actively prevents correction.

## Related

- [[metacognitive-demand]] - the skill needed to close the gap
- [[calibration]] - practice for accurate self-assessment
- [[cognitive-debt]] - what accumulates in the gap
- [[fluency-bias]] - why AI outputs feel trustworthy
- [[cognitive-surrender]] - the behavioral mechanism that drives confidence inflation with AI
- [[tri-system-theory]] - framework explaining why System 3 inflates confidence
- [[ai-moralization]] - moralized opposition may masquerade as calibrated self-reliance
- [[artificial-certainty]] - organizational variant where AI gives non-experts institutional-level false confidence (Leonardi & Leavell 2026)
- [[artificial-confidence]] - social comparison mechanism contributing to the gap
- [[professional-identity-threat]] - Keshky models cross-sectional associations with intellectual identity distortion
- [[borrowed-certainty]] - illusory self-efficacy dimension maps to borrowed certainty mechanism
- [[agency]] - Han et al. (2025) show self-efficacy as mediator between AI use and behavioral risk-taking; inflated efficacy without learning orientation produces agency illusion
- [[sycophancy]] - sycophantic AI widens the gap by validating misconceptions and inflating confidence
- [[lee-critical-thinking-survey-2025]] - field-scale evidence for the directional confidence pair (confidence-in-AI undermines vs. confidence-in-self protects critical engagement)
- [[illusion-of-explanatory-depth]] - the foundational metacognitive mechanism the gap rests on; Messeri & Crockett anchor this construct in AI-assisted science
- [[scientific-monoculture]] - system-level outcome when the gap goes uncorrected at scale; the gap is the individual-level signature of the monoculture

## Sources

- Scispace Literature Synthesis (2025)
- Tankelevitch et al. (2024)
- [[shaw-cognitive-surrender-2026]] — Shaw & Nave (2026)
- [[he-illusion-competence-2023]] — He, Kuiper, & Gadiraju (2023)
- [[leonardi-artificial-certainty-2026]] — Leonardi & Leavell (2026)
- [[reich-artificial-confidence-2026]] — Reich & Teeny (2026)
- [[keshky-illusory-competence-2026]] — Keshky (2026)
- [[han-trust-self-efficacy-2025]] — Han, Z., Song, G., Zhang, Y., & Li, B. (2025)
- Fernandes et al. (2026)
- [[lee-critical-thinking-survey-2025]] — Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers. CHI '25.
- [[messeri-crockett-illusions-understanding-2024]] — Messeri, L. & Crockett, M. J. (2024). Artificial intelligence and illusions of understanding in scientific research. Nature, 627, 49–58.

