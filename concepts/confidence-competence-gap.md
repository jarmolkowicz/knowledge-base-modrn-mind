---
status: solid
area: [erosion]
sources:
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

A discrepancy between confidence and demonstrated performance or understanding. AI assistance can change either side of this relationship; confident assisted output is not proof of independent competence.

## Why It Matters

Confidence, assisted performance and retained skill need separate assessment. A confidence gap can occur without skill erosion, and a short-term study cannot establish lasting decline.

Shaw & Nave (2026) provide direct experimental evidence of this gap in real-time. AI access inflated confidence by ~12 percentage points (Study 1: 77.0% AI-assisted vs 65.3% brain-only, Hedges' g = 0.54), despite approximately half of AI outputs being deliberately wrong. Critically, no statistically significant confidence decline was detected as faulty trials increased (p=.202). Per-item confidence in Study 3 was higher on AI-assisted trials (82.2%) than brain-only trials (77.5%), and did not vary between AI-accurate and AI-faulty trials. People felt equally confident whether AI helped or hurt them.

He et al. (2023) demonstrate a specific instance of the confidence-competence gap: the Dunning-Kruger Effect in AI-assisted decision making. In their study (N = 249), participants who overestimated their own competence (bottom performance quartile with inflated self-assessment) under-relied on AI — dismissing accurate AI predictions because they overrated their own ability. This shows the gap operates in both directions: AI can inflate confidence (Shaw & Nave, 2026), but pre-existing overconfidence was associated with under-reliance on accurate advice.

Fernandes et al. (2026) model metacognitive self-assessment in two logical-reasoning studies (Study 1 N=246; Study 2 N=452 randomized with monetary incentives). AI use improved task performance by about three points out of 20, while AI users overestimated their performance by about four points. These are different comparisons, not quantities to subtract. A Bayesian model separated bias (*b_k*) from noise (*σ_k*). In Study 1, the AI group's σ median was 1.01 (95% HDI [0.84, 1.19]), versus 1.78 for an external no-AI sample. The model showed a flatter relationship between skill and overestimation; it does not mean every person became equally overconfident. Study 2 replicated the bias finding, with weaker evidence for the σ pattern.

Fernandes et al. also report a counterintuitive moderation finding: higher self-rated AI literacy correlated with *lower* metacognitive accuracy (overall SNAIL × overestimation: *r* = .21 in Study 1, *r* = .20 in Study 2; both *p* < .01). The Technical Understanding subscale (familiarity with prompting, parameters, API workflows) carried the strongest effect, while Critical Appraisal and Practical Application subscales correlated with higher mean confidence without improving discrimination (AUC). The authors interpret this through the illusion of explanatory depth (Fisher & Oppenheimer, 2021): procedural fluency provides a misleading sense of ability. This challenges the assumption that AI-literacy training is uniformly protective against the gap. Study 2 showed no calibration improvement relative to Study 1 despite an accuracy bonus. That cross-study comparison does not isolate incentives or rule out effort as a contributing factor.

Lee et al. (2025) surveyed 319 knowledge workers about 936 GenAI-use examples. Higher confidence in AI was associated with less reported critical thinking (β=−.69, p<.001); self-confidence was associated with more (β=.26, p=.026). These are self-reported associations, not measured expertise or evidence that either type of confidence caused a change in ability. The survey does not validate the mechanisms proposed in the laboratory studies.

Leonardi & Leavell (2026) extend the confidence-competence gap to the organizational level through the concept of [[artificial-certainty]]. In their comparative ethnography, non-expert stakeholders who encountered AI-generated simulations believed they fully understood complex urban planning dynamics — "knowing enough to be dangerous." The gap was not between a user's confidence and their ability to use AI, but between stakeholders' confidence in understanding complex systems and their actual domain expertise. When process experts amplified AI capabilities (enhancement mode), stakeholders mistook detailed representations for reality and questioned whether expert guidance was necessary at all.

Messeri and Crockett (2024), in a Perspective, propose that illusions of understanding could affect scientific knowledge production. [Inference] Comparing this with [[artificial-certainty]] and individual confidence gaps connects different levels of analysis; the papers do not jointly test a shared causal mechanism.

Reich & Teeny (2026) found higher creative self-confidence after exposure to content labeled as AI-generated rather than human-generated (N=6,801 across 11 experiments). They report evidence consistent with downward social comparison, with weaker effects in fact-based domains. In Study 3, blinded raters found no difference in the funniness of participants' captions despite higher self-ratings in the AI-labeled condition. This bounds the confidence–performance discrepancy to that task; it does not establish general creative skill loss.

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
   Shaw & Nave (2026) report a related confidence result: AI doesn't just produce correct outputs that get misattributed — it produces *confident, fluent* outputs that inflate the user's sense of certainty regardless of accuracy. The confidence boost is not contingent on outcomes. This means the gap can widen even in a single session, not just over time.
2. User attributes success to own understanding
3. Delayed/absent feedback provides no correction signal
4. Confidence stays high while competence declines
5. Gap widens invisibly until tested

Confidence alone does not establish retained skill. An unaided assessment can test capability; the cited studies do not establish that degradation is always unnoticed until assistance is removed.

Han et al. (2025) found positive associations between reported AI use, self-efficacy and willingness to take risks in a three-wave employee survey (N=442). Learning goal orientation moderated the model, but a nonsignificant indirect association at low orientation does not establish shallow confidence or absence of genuine capability. Actual risk-taking, unaided skill and attribution of success were not measured. The study therefore does not demonstrate a confidence–competence gap.

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
- [[agency]] - Han's self-efficacy and willingness measures do not establish actual agency or competence
- [[sycophancy]] - sycophantic AI widens the gap by validating misconceptions and inflating confidence
- [[lee-critical-thinking-survey-2025]] - confidence in AI and self-confidence have different associations with reported critical thinking; causality was not tested
- [[illusion-of-explanatory-depth]] - a related discrepancy between felt and demonstrated understanding
- [[scientific-monoculture]] - a proposed community-level risk, not an established consequence of individual miscalibration

## Sources

- [[tankelevitch-metacognitive-demands-2023]] — Tankelevitch et al. (2024)
- [[shaw-cognitive-surrender-2026]] — Shaw & Nave (2026)
- [[he-illusion-competence-2023]] — He, Kuiper, & Gadiraju (2023)
- [[leonardi-artificial-certainty-2026]] — Leonardi & Leavell (2026)
- [[reich-artificial-confidence-2026]] — Reich & Teeny (2026)
- [[keshky-illusory-competence-2026]] — Keshky (2026)
- [[han-trust-self-efficacy-2025]] — Han, Z., Song, G., Zhang, Y., & Li, B. (2025)
- [[fernandes-metacognition-2025]] — Fernandes et al. (2026)
- [[lee-critical-thinking-survey-2025]] — Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers. CHI '25.
- [[messeri-crockett-illusions-understanding-2024]] — Messeri, L. & Crockett, M. J. (2024). Artificial intelligence and illusions of understanding in scientific research. Nature, 627, 49–58.
