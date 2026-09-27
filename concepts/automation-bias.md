---
status: solid
area:
- erosion
sources:
- Parasuraman & Riley (1997)
- Goddard et al. (2012)
- Shaw & Nave (2026)
- Han, Z., Song, G., Zhang, Y., & Li, B. (2025)
- "Yu, F., Moehring, A., Banerjee, O., Salz, T., Agarwal, N., & Rajpurkar, P. (2024). Heterogeneity and predictors of the effects of AI assistance on radiologists. Nature Medicine, 30, 837–849. https://doi.org/10.1038/s41591-024-02850-w"
---

# Automation Bias

## What It Is

The tendency to over-trust automated systems and AI relative to your own judgment, leading to uncritical acceptance of machine-generated outputs even when they contain errors.

Shaw & Nave (2026) propose [[cognitive-surrender]] as a broader theoretical account than item-level automation errors. Their follow/override measures do not directly establish that a person has stopped deliberating altogether.

## Why It Matters

Automation bias can lead people to miss or act on incorrect recommendations. Failure to check an answer does not by itself show a lasting loss of verification ability.

No universal primary barrier to human–AI complementarity is established here. [[vaccaro-human-ai-meta-analysis-2024]] synthesizes performance comparisons without isolating one mechanism.

Yu et al. (2024) extend the team-level evidence into a specialist diagnostic context with an explicit dose-response. In a randomized two-design study of 140 board-certified radiologists across 324 chest X-ray cases and 15 pathologies, AI prediction error scaled the harm: more accurate AI yielded better radiologist treatment effects, and AI predictions with absolute error >80 (on a 0–100 probability scale) produced a treatment effect of −16.845 absolute-error points (95% CI: −24.288 to −9.403). Critically, the direction of AI error mattered too — predictions that *underestimated* ground-truth probabilities yielded better treatment effects than equally-erroneous predictions that *overestimated* them. Yu et al. interpret the underlying mechanism plainly: "radiologists struggle to consistently distinguish between accurate and inaccurate AI predictions and can be misled by inaccurate AI predictions" [p.11]. This is automation bias at expert scale: 140 specialists working in their domain, on their core task, still systematically followed AI into error.

## Key Insight

[Inference] A proposed feedback loop:
1. Trust AI → don't verify → miss errors
2. Missing errors feels like AI was right
3. Trust increases → verify less
4. Capability to verify erodes

The complete sequence, including long-term loss of verification skill, is not established by the evidence summarized here.

Shaw & Nave (2026) found 79.8% faulty-advice acceptance in Study 1 among AI-engaged faulty trials, and 73.2% across all studies. Incentives plus feedback increased all-override rates from 20.0% to 42.3% in Study 3. Failed overrides remain possible; these results do not by themselves establish a change in the location of cognitive control.

[Inference] The provisional [[complementarity-framework]] raises a design question: could confident AI errors and reduced human checking coincide? The framework does not establish this as a measured joint failure mechanism.

Vaccaro et al. (2024) did not find statistically significant performance moderation by AI explanations or confidence displays. Their meta-analysis does not establish active interrogation as the best interaction mode. [Inference] Compare checking and interface designs in the intended task rather than assuming a universal safeguard.

Han et al. (2025) found positive associations between reported AI use, self-efficacy and willingness to take risks in a three-wave employee survey (N=442). Learning goal orientation moderated the model, but a nonsignificant indirect association at low orientation does not establish shallow confidence or absence of genuine capability. Actual risk-taking, unaided skill and attribution of success were not measured. Automation bias and reliance on erroneous advice were not tested.

Yu et al. (2024) add a heterogeneity dimension to the feedback-loop description above. The same AI on the same tasks produced treatment effects ranging from −1.295 to +1.440 (IQR 0.797) on aggregated pathologies and up to −8.914 to +5.563 on individual high-prevalence tasks — meaning automation bias is not uniform across experts. Conventional predictors of who is most susceptible (years of experience, subspecialty, AI-tool familiarity, baseline diagnostic skill) all failed to identify which radiologists would be helped versus harmed. The practical implication: at the individual expert level, susceptibility to automation bias cannot be inferred from career stage or test scores; it must be measured per-radiologist under realistic deployment conditions before deciding who receives AI assistance. This finding cautions against assuming that professional experience alone predicts benefit from AI assistance.

## Related

- [[fluency-bias]] - amplifies automation bias
- [[cognitive-offloading]] - automation bias makes offloading feel safe
- [[calibration]] - the skill that counters automation bias
- [[capacity-erosion]] - a proposed long-term risk of reduced verification practice
- [[human-ai-complementarity]] - automation bias can obstruct complementarity; its relative importance depends on the setting
- [[complementarity-framework]] - proposes attention and checking routines; effectiveness is untested
- [[cognitive-surrender]] - broader phenomenon that automation bias sits within
- [[tri-system-theory]] - framework that contextualizes automation bias as one dynamic among several
- [[ai-self-efficacy-erosion]] - Han's work-tool survey and AI-evaluation experiments examine different contexts
- [[yu-radiologists-ai-2024]] — specialist dose-response evidence: AI absolute error >80 yields treatment effect of −16.845 in 140 board-certified radiologists; experience-based and skill-based predictors of automation-bias susceptibility all fail

## Sources

- [[parasuraman-riley-automation-1997]] — Parasuraman & Riley (1997)
- [[goddard-automation-bias-2012]] — Goddard et al. (2012)
- [[shaw-cognitive-surrender-2026]] — Shaw & Nave (2026)
- [[han-trust-self-efficacy-2025]] — Han, Z., Song, G., Zhang, Y., & Li, B. (2025)
- [[yu-radiologists-ai-2024]] — Yu, F., Moehring, A., Banerjee, O., Salz, T., Agarwal, N., & Rajpurkar, P. (2024). Heterogeneity and predictors of the effects of AI assistance on radiologists. Nature Medicine, 30, 837–849. https://doi.org/10.1038/s41591-024-02850-w
