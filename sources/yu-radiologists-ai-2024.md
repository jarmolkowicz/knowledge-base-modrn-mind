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

Yu et al. study variation in AI assistance effects among radiologists: same AI, same radiologists, same tasks — treatment effects span both substantial improvement and substantial degradation, ranging from −1.295 to +1.440 (IQR 0.797) on aggregated pathologies and from −8.914 to +5.563 (IQR 3.245) on the high-prevalence "abnormal" task. Crucially, no experience-based or skill-based predictor reliably identifies who benefits and who is harmed: years of experience, subspecialty in thoracic radiology, experience with AI tools, and direct unassisted-error performance all fail. A strong case-level correlate is *AI error itself* — radiologist performance degrades roughly linearly with AI prediction error, and AI predictions with absolute error >80 produce a treatment effect of −16.845 absolute-error points. The authors recommend: complementarity between expert human and AI is not a default outcome of combining the two; it must be measured per-radiologist under realistic deployment conditions before deciding who receives AI assistance.

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

Shows substantial variation in the effect of the same AI assistance across specialist readers and cases. Experience, subspecialty, AI familiarity and unassisted performance did not reliably predict individual benefit in this setup.

Larger AI errors were associated with worse assistance effects. Error magnitude itself was not randomized; the relationship should not be treated as an experimentally assigned dose. The paper also shows why shared measurement noise can create misleading associations between baseline performance and treatment effects (p.5).

## Supports

- [[automation-bias]] — inaccurate AI predictions can mislead specialists; this is a distinct design from [[goddard-automation-bias-2012]].
- [[human-ai-complementarity]] — benefit from assistance was heterogeneous; assistance gains alone do not establish synergy over both parties alone.
- [[novice-vulnerability]], [[paradox-of-expertise]] and [[leveling-effect]] — conventional expertise and baseline-performance measures did not reliably predict benefit here.
- [[upskilling-deskilling-paradox]] — adjacent question; skill development or loss was not measured.
- [[calibration]] — [Inference] supports evaluating response to a specific tool rather than relying only on experience proxies.
- [[partial-automation-principle]] — [Inference] deployment choices need evaluation; this study did not compare all partial-automation designs.

## Contradicts / Extends

- [[goddard-automation-bias-2012]] reviews different clinical decision-support evidence. Its reported risk estimate is not a universal baseline for this continuous-error analysis.
- [[bauer-discontinuing-ml-2022]] studies learning and performance after assistance removal; these are different outcomes.
- [[bastani-guardrails-math-rct-2025]] concerns students, mathematics and a different assistance design. Neither study establishes a universal rule about who gains most.
- [[passalacqua-less-ai-2024]] tests automation levels in a separate task. Together the studies motivate task-specific evaluation, not a rule that learning always requires less AI.

## Open Questions

- The randomization design prevented analysis of temporal trends — Yu et al. could not test whether radiologists improved at incorporating AI predictions over time. The question — does deliberate practice with AI close the heterogeneity gap, or is the spread structural? — is not answered by this study.
- The AI assistance was probability-only; no explanations, no localizations, no nuanced text reports. Yu et al. flag (p.11) that explanation-rich AI may yield different patterns. The "what AI presentation reduces harm at high error rates" question is open.
- Why do experience-based predictors fail? Yu et al. speculate (p.11) about cognitive abilities, adaptability, and decision-making style as untested candidates. The negative result is robust; the mechanistic story is not.
- The sample contains only radiologists (specialist medical imaging). Generalizability to other professional populations (radiographers without specialty training, primary-care physicians using imaging AI, non-medical specialist work) is not tested.
- The "AI underestimates → better treatment effect" finding is potentially exploitable in AI design — but the paper does not test whether deliberately calibrating AI to underestimate (a Bayesian-conservative strategy) preserves the effect, or whether the effect comes from radiologists adjusting their own confidence patterns when seeing low AI probabilities.
