---
status: solid
area: [risk, erosion, preservation]
type: paper
sources:
  - "Fernandes, D., Villa, S., Nicholls, S., Haavisto, O., Buschek, D., Schmidt, A., Kosch, T., Shen, C., & Welsch, R. (2026). AI makes you smarter but none the wiser: The disconnect between performance and metacognition. Computers in Human Behavior, 175, 108779. https://doi.org/10.1016/j.chb.2025.108779"
---

# Fernandes et al. (2026) — AI Makes You Smarter But None the Wiser

## Citation

Fernandes, D., Villa, S., Nicholls, S., Haavisto, O., Buschek, D., Schmidt, A., Kosch, T., Shen, C., & Welsch, R. (2026). AI makes you smarter but none the wiser: The disconnect between performance and metacognition. *Computers in Human Behavior*, 175, 108779. https://doi.org/10.1016/j.chb.2025.108779

## Type

Paper (peer-reviewed empirical, two studies)

## Key Insight

The studies distinguish assisted reasoning performance from self-assessment. AI users showed overestimation and a flatter modeled Dunning–Kruger pattern; higher self-rated AI literacy was associated with greater overestimation. Confidence–correctness discrimination was weak in both Study 2 groups (.62 with AI; .61 without), not demonstrably lower because of AI. The bonus comparison across studies does not isolate a causal incentive effect.

## Key Findings

**Two studies on logical-reasoning tasks (LSAT items):**

- **Study 1** (N = 246): AI-using sample compared against the Jansen et al. (2021) open no-AI dataset (N = 3,543). Quasi-experimental.
- **Study 2** (N = 452): Randomized AI vs. no-AI comparison with monetary incentives for accurate metacognition (+£0.50 ≈ 8% of compensation).

**Performance and overconfidence**

- AI augmentation works at the group level: AI-using participants outperformed Jansen et al.'s no-AI sample (M = 12.98 vs. 9.45 of 20; t(245) = 19.23, *p* < .001, *d* = 1.23).
- No human–AI synergy on average: AI-using participants performed slightly *worse* than ChatGPT-4o alone (M = 13.65) — *t*(245) = −3.66, *p* < .001, *d* = −0.23.
- AI users overestimated by ~4 points; the no-AI Jansen sample overestimated by ~2 points. Metacognitive bias was approximately *doubled* under AI use in Study 1.

**Dunning–Kruger flattening**

A Bayesian model decomposed performance estimates into bias (*b_k*) and noise (*σ_k*). For a DKE pattern to emerge, both *b > 0* and *σ > 1* must hold (the noise term is what scales miscalibration to skill).

- **AI group**: *b_AI* median = 0.45 (95% HDI [0.32, 0.60]); *σ_AI* median = 1.01 (95% HDI [0.84, 1.19]).
- **No-AI group**: *b_noAI* median = 0.23 (95% HDI [0.21, 0.25]); *σ_noAI* median = 1.78 (95% HDI [1.69, 1.88]).
- 99% of posterior samples for bias were larger in the AI group; 0% overlap of *σ* posteriors.
- Interpretation: AI augmentation flattens skill differences, so the pattern of "low performers overestimate more, high performers underestimate" disappears. Everyone overestimates roughly equally.
- Study 2 replicated the bias finding under randomization; the σ pattern weakened with the smaller sample but trended in the same direction.

**The AI-literacy paradox**

- Overall SNAIL AI-literacy score correlated *positively* with overestimation: *r* = .21, *p* < .01 (Study 1); *r* = .20, *p* < .01 (Study 2).
- The Technical Understanding (TU) subscale carried the strongest effect: prompting fluency, parameter awareness, and API-workflow familiarity were the strongest predictors of inflated self-assessment.
- Critical Appraisal (CA) and Practical Application (PA) subscales correlated with higher mean confidence but did not improve discrimination (AUC) — a "global confidence without local monitoring" pattern.
- Authors interpret this as the *[[illusion-of-explanatory-depth|illusion of explanatory depth]]* (Fisher & Oppenheimer, 2021): procedural fluency provides a misleading sense of ability.

**Metacognitive sensitivity is low for everyone**

- Mean AUC (confidence-correctness discrimination): AI group .62, no-AI group .61 — both significantly below the authors' .70 reference benchmark (AI: *t*(244) = −10.56, *p* < .001).
- Confidence ratings only weakly distinguish correct from incorrect answers regardless of AI use.

**Cross-study incentive comparison**

- Study 2's +£0.50 bonus was accompanied by no calibration improvement relative to Study 1. The authors interpret this as evidence against a simple effort explanation, but bonus versus no bonus was not randomized within Study 2.

**Observed prompting behavior**

- 46% of participants used only one prompt per question; only 8% issued more than three. Mean prompts per question: 1.15 (SD = 0.34). Across 246 participants × 20 items, this is 6,629 prompts.
- Qualitative analysis: participants treated AI as a tool (21.5%), collaborator (12.6%), or accepted outputs without inquiry (majority). Different framings did not predict performance or calibration.

**Design implications (Table 6)**

The authors recommend three classes of intervention: confidence-calibration interfaces with AI uncertainty visualization; cognitive forcing functions (Buçinca et al., 2021); and "explain-back" micro-tasks — having users restate the AI's logic in plain language before accepting an answer, targeting the [[illusion-of-explanatory-depth|illusion of explanatory depth]] directly.

## Key Passages

> "Participants overestimated their task performance by four points. Interestingly, higher AI literacy correlated with lower metacognitive accuracy, suggesting that those with more technical knowledge of AI were more confident but less precise in judging their own performance."
> — Fernandes et al., abstract, p.1

> "The classic DKE, where lower performers overestimate and higher performers underestimate their performance, disappeared with AI use, suggesting that while AI levels performance, it does not correct inflated self-assessments."
> — Fernandes et al., §6.1, p.13

> "Familiarity with AI may enhance the better-than-average effect [...] leading to the overestimation of both relative and absolute performance."
> — Fernandes et al., §6.1, p.14

> "AI assistance also shifts the noise parameter toward unity, eliminating the skill-based damping that normally curbs high-performers' miscalibration and thus flattening the DKE slope."
> — Fernandes et al., §6.1, p.14

## Relevance

This is the primary empirical anchor the KB needs for several existing concepts that previously rested on theoretical or secondary citations. It quantifies the confidence-competence gap under generative-AI use (approximately four-point overestimation; not a one-point residual after subtracting a performance gain), provides the first computational-model decomposition of metacognitive bias and noise in the KB, and reports the counterintuitive AI-literacy result. It also resolves the deferred secondary source `dolan-competence-assessment-2025` (a PsyPost summary of this paper, currently DEFER in `raw/`).

## Supports

- [[confidence-competence-gap]] — reports approximately four-point overestimation, the Bayesian bias/noise decomposition, the DKE-flattening finding, and the AI-literacy paradox
- [[metacognition]] — weak confidence–correctness discrimination in both groups; AUC does not establish AI-caused decline
- [[calibration]] — cross-study bonus comparison; reflective interventions proposed, not shown necessary or effective here
- [[fluency-bias]] — the AI-literacy paradox is framed as [[illusion-of-explanatory-depth|illusion of explanatory depth]]: technical-fluency knowledge inflates perceived ability without improving discrimination
- [[automation-bias]] — prompting and monitoring measures raise questions about reliance; a causal explanation was not isolated
- [[metacognitive-demand]] — explicitly cites Tankelevitch et al. (2024) and provides the empirical follow-up they called for

## Contradicts / Extends

- Extends: [[he-illusion-competence-2023]] — He et al. found self-assessment associated with reliance decisions; Fernandes reports a flatter modeled DKE pattern in the assisted tasks. The studies concern different outcomes and do not establish a developmental sequence over time.
- Extends: [[shaw-cognitive-surrender-2026]] — Shaw & Nave found higher per-item confidence and accuracy changes that depended on AI correctness; Fernandes adds the global self-assessment bias and the bias/noise computational decomposition.
- Extends: [[tankelevitch-metacognitive-demands-2023]] — provides the empirical investigation of metacognition in HAI that Tankelevitch et al. argued was missing.
- Extends: [[leonardi-artificial-certainty-2026]] — Leonardi documented [[artificial-certainty]] at the organizational level (non-experts feeling expert); Fernandes shows the individual-cognitive substrate (skill-leveling that compresses the DKE).
- Tension with: assumption that AI literacy is protective. Fernandes finds the *Technical Understanding* subscale of the SNAIL is the strongest predictor of overestimation — challenging interventions that focus narrowly on technical AI training without metacognitive scaffolding.

## Open Questions

- Does the AI-literacy paradox replicate with *measured* AI literacy (not just self-reported SNAIL)? Self-report could conflate familiarity with the better-than-average effect.
- Does the DKE flattening persist in domains where AI is less reliable than ChatGPT-4o was on LSAT items (68.25% accuracy)? The augmentation hypothesis predicts that with weaker AI, low performers might no longer be lifted to a uniform high baseline.
- Does naturalistic prompting (multiple prompts, ignoring AI, proactive AI) change the metacognitive picture? The forced ≥1-prompt design may produce shallower engagement than real-world use.
- How does the gap evolve over repeated interactions? The studies are cross-sectional; learning trajectories under AI remain open (Bastani et al., 2024 cited as the closest available evidence).
- Are "explain-back" micro-tasks empirically effective at closing the gap? The recommendation is grounded in adjacent HCI work (Fisher & Oppenheimer, 2021) but not yet tested in this design.
