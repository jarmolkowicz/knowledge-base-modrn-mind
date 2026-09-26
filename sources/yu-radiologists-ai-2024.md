---
status: solid
area: [risk, erosion]
type: paper
sources:
  - "Yu, F., Moehring, A., Banerjee, O., Salz, T., Agarwal, N., & Rajpurkar, P. (2024). Heterogeneity and predictors of the effects of AI assistance on radiologists. Nature Medicine, 30, 837–849. https://doi.org/10.1038/s41591-024-02850-w"
---

# Yu et al. (2024) — Heterogeneity and Predictors of AI Assistance on Radiologists

## Citation

Yu, F., Moehring, A., Banerjee, O., Salz, T., Agarwal, N., & Rajpurkar, P. (2024). Heterogeneity and predictors of the effects of AI assistance on radiologists. *Nature Medicine*, 30, 837–849.

**DOI:** [10.1038/s41591-024-02850-w](https://doi.org/10.1038/s41591-024-02850-w)

## Type

Paper (large-scale diagnostic study; two-design experimental, 140 radiologists, 324 patient cases, 15 chest X-ray pathologies; CheXpert DenseNet121 AI model; pre-registered companion at NBER WP 31422)

## Key Insight

Yu et al. provide the cleanest specialist-population evidence on AI assistance heterogeneity to date: same AI, same radiologists, same tasks — treatment effects span both substantial improvement and substantial degradation, ranging from −1.295 to +1.440 (IQR 0.797) on aggregated pathologies and from −8.914 to +5.563 (IQR 3.245) on the high-prevalence "abnormal" task. Crucially, no experience-based or skill-based predictor reliably identifies who benefits and who is harmed: years of experience, subspecialty in thoracic radiology, experience with AI tools, and direct unassisted-error performance all fail. The strongest predictor is *AI error itself* — radiologist performance degrades roughly linearly with AI prediction error, and AI predictions with absolute error >80 produce a treatment effect of −16.845 absolute-error points. The paper's structural implication: complementarity between expert human and AI is not a default outcome of combining the two; it must be measured per-radiologist under realistic deployment conditions before deciding who receives AI assistance.

## Key Passages

> "Surprisingly, conventional experience-based factors, such as years of experience, subspecialty and familiarity with AI tools, fail to reliably predict the impact of AI assistance. Additionally, lower-performing radiologists do not consistently benefit more from AI assistance, challenging prevailing assumptions."
> — Yu et al., [p.1] (abstract)

> "When measuring AI's treatment effect as the improvement in absolute error across all pathologies, we observed a range of treatment effects from −1.295 to 1.440 (interquartile range (IQR), 0.797). Notably, for high-prevalence pathology labels... the largest range of treatment effects extended from −8.914 to 5.563 (IQR, 3.245) for detecting whether chest X-rays are abnormal."
> — Yu et al., [p.2]

> "We found that the combined characteristics model was a poor predictor of treatment effect on all pathologies aggregated... When used individually, each of the experience-based characteristics was found to be a poor predictor of treatment effect."
> — Yu et al., [p.4]

> "AI assistance with absolute error above 80 resulted in a treatment effect of −16.845 (95% CI: −24.288 to −9.403, n = 371). ... AI predictions with negative errors, indicating underestimation of probabilities by the AI, led to better treatment effects compared to predictions with the same magnitude of positive errors, indicating overestimation of probabilities by the AI."
> — Yu et al., [p.9]

> "Surprisingly, radiologists who initially performed poorly without AI assistance did not necessarily benefit more or experience more harm from AI assistance compared to higher-performing counterparts."
> — Yu et al., [p.11] (Discussion)

> "Without reliable predictors, it is necessary to measure radiologists' response to AI assistance under realistic simulations of deployment settings before deciding whether to provide AI assistance to different radiologists."
> — Yu et al., [p.11] (Discussion)

> "AI predictions with large errors tend to lead to negative treatment effects, suggesting that radiologists struggle to consistently distinguish between accurate and inaccurate AI predictions and can be misled by inaccurate AI predictions."
> — Yu et al., [p.11] (Discussion)

## Relevance

Three load-bearing contributions to the KB:

- **Heterogeneity at expert scale.** The KB's automation-bias and complementarity literature has been built largely on lab studies, mid-skill knowledge workers, and meta-analytic synthesis. Yu et al. contribute large-N, peer-reviewed, specialist-context evidence (140 board-certified radiologists, randomized two-design study, real chest X-rays from Stanford's healthcare system) that the same AI on the same tasks produces substantively different effects across experts. This is what [[human-ai-complementarity]] needs to ground its "not a default outcome" claim in expert practice.

- **Negative finding on conventional predictors.** Years of experience, subspecialty, and AI-tool familiarity all fail to predict who benefits — and unassisted error does not either. This complicates the simple "AI levels up novices" frame underlying parts of [[novice-vulnerability]] and the "experts under-adopt" frame in [[paradox-of-expertise]]. In this specialist context, neither story holds at the individual level. The implication is uncomfortable for prescriptive frameworks: "give AI to the lower-performers first" and "experts will know whether AI helps them" are both empirically unsupported in this study.

- **AI-error dose-response.** [[automation-bias]] and [[goddard-automation-bias-2012]] give a 26% RR-of-following-bad-advice baseline. Yu et al. provide a specialist-population dose-response curve: as AI absolute error rises through five bins, radiologist treatment effect declines from +0.679 to −16.845. The direction-of-error finding (underestimation > overestimation, holding absolute error constant) sharpens the KB's understanding of which AI failure modes are most harmful.

The methodological lesson — that without split sampling, a "hallucinated association" between unassisted error and treatment effect appears [p.5] — is also a calibration warning the KB inherits implicitly: many AI-in-medicine studies that report "lower performers benefit more" may be statistical artifacts of regression to the mean.

## Supports

- [[automation-bias]] — Yu provides specialist-context, dose-response evidence: AI absolute error >80 yields treatment effect −16.845; underestimating AI predictions yield better outcomes than overestimating ones. Generalizes Goddard's 26% RR finding into a continuous error-vs-harm curve in radiology.
- [[human-ai-complementarity]] — direct empirical demonstration that complementarity is heterogeneous and individual-level: same AI, same expert population, same tasks, treatment effects span both improvement and degradation. Complementarity is not a default outcome; it must be measured.
- [[novice-vulnerability]] — counter-evidence sharpening the entry: in this specialist context, lower-performing radiologists did not consistently benefit more from AI. The "AI as leveler" claim from Bastani et al. (2025) and others does not generalize uniformly to expert populations.
- [[paradox-of-expertise]] — Yu's failure of experience-based predictors complicates the entry's "experts under-adopt because of overestimated expertise" framing. In Yu's setup all radiologists used AI when assigned; experience did not predict whether the use helped or hurt them. The paradox needs a sharper specification of which experience-related failure modes it covers.
- [[upskilling-deskilling-paradox]] — direction-of-error texture: AI predictions that underestimate probabilities lead to better treatment effects than equally-erroneous overestimating predictions. Implies the upskilling/deskilling tilt depends partly on the failure-mode profile of the AI tool, not just on user behavior.
- [[calibration]] — practical implication: trust calibration must be measured per-individual under realistic deployment conditions; experience-based heuristics for "who is well-calibrated" don't work.
- [[partial-automation-principle]] — Yu's data argue against "give AI to all radiologists" wholesale rollouts; targeted deployment based on per-radiologist measured benefit is the operational implication.
- [[leveling-effect]] — Yu provides specialist-context counter-evidence: lower-performing radiologists did not consistently benefit more from AI; the leveling effect documented in novice/student populations does not generalize uniformly to expert cohorts.

## Contradicts / Extends

- Extends [[goddard-automation-bias-2012]] — Goddard's systematic review of 74 CDSS studies established the 26% increased risk of following bad automated advice. Yu provides a continuous dose-response in a single specialist population: error magnitude scales the harm, and direction of error matters.
- Complements [[bauer-discontinuing-ml-2022]] — Bauer studies new-skill development and a post-removal gap followed by catch-up; Yu studies assisted diagnostic performance. Different designs and measures, not joint evidence of two established lasting skill-loss mechanisms.
- Complicates [[bastani-guardrails-math-rct-2025]]'s leveling story — Bastani found vanilla GPT-4 access produced large gains for weaker math students that disappeared on unassisted exam. Yu's specialist data find no consistent leveling effect at all: lower-performing radiologists did not benefit more on assisted tasks. The leveling finding may be domain- and skill-stage-specific.
- Companion to [[passalacqua-less-ai-2024]] — Passalacqua: practice with less AI builds skill better. Yu: among already-skilled experts, individual response to AI is heterogeneous and unpredictable from experience alone. Together: skill formation needs less AI; skilled use of AI needs individual measurement.

## Open Questions

- The randomization design prevented analysis of temporal trends — Yu et al. could not test whether radiologists improved at incorporating AI predictions over time. The KB's question — does deliberate practice with AI close the heterogeneity gap, or is the spread structural? — is not answered by this study.
- The AI assistance was probability-only; no explanations, no localizations, no nuanced text reports. Yu et al. flag (p.11) that explanation-rich AI may yield different patterns. The "what AI presentation reduces harm at high error rates" question is open.
- Why do experience-based predictors fail? Yu et al. speculate (p.11) about cognitive abilities, adaptability, and decision-making style as untested candidates. The negative result is robust; the mechanistic story is not.
- The sample contains only radiologists (specialist medical imaging). Generalizability to other professional populations (radiographers without specialty training, primary-care physicians using imaging AI, non-medical specialist work) is not tested.
- The "AI underestimates → better treatment effect" finding is potentially exploitable in AI design — but the paper does not test whether deliberately calibrating AI to underestimate (a Bayesian-conservative strategy) preserves the effect, or whether the effect comes from radiologists adjusting their own confidence patterns when seeing low AI probabilities.
