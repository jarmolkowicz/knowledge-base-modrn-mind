---
status: speculative
area:
- preservation
- risk
sources:
  - "Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Heck, S., Mueller, J., Hong, J., Ritchie, S., Belonax, T., Troy, K. K., Amodei, D., Kaplan, J., Clark, J., & Ganguli, D. (2025). Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations. arXiv:2503.04761 [cs.CY], February 11, 2025. Anthropic."
  - "Vaccaro, M., Almaatouq, A. & Malone, T. (2024). When combinations of humans and AI are useful: a systematic review and meta-analysis. Nature Human Behaviour, 8, 2293–2303. https://doi.org/10.1038/s41562-024-02024-1"
  - "Yu, F., Moehring, A., Banerjee, O., Salz, T., Agarwal, N., & Rajpurkar, P. (2024). Heterogeneity and predictors of the effects of AI assistance on radiologists. Nature Medicine, 30, 837–849. https://doi.org/10.1038/s41591-024-02850-w"
  - "Dell'Acqua, F., Ayoubi, C., Lifshitz, H., Sadun, R., Mollick, E., Mollick, L., Han, Y., Goldman, J., Nair, H., Taub, S., & Lakhani, K. R. (2026). The Cybernetic Teammate: A Field Experiment on Generative AI and Teamwork. Organization Science, Articles in Advance. https://doi.org/10.1287/orsc.2025.20702"
---

# Human-AI Complementarity

## What It Is

The condition under which a human-AI team outperforms either humans alone or AI alone on a given task. Not a default outcome of combining human and AI effort, but a specific achievement that requires deliberate design, trust calibration, and well-defined role partitioning.

## Why It Matters

The assumption that "human + AI = better" is widespread but empirically unsupported as a general claim. The largest meta-analysis to date (Vaccaro et al. 2024; 106 experiments) found that, on average, human-AI combinations performed *worse* than the best of human-or-AI alone — genuine synergy occurred in a minority of cases and only under specific conditions. Poorly designed interaction or overreliance on AI can produce worse outcomes than either working independently. This means complementarity is a design problem, not an inevitability.

## Key Insight

[Inference] Complementarity may arise when people and AI make different errors and can correct one another. This must be evaluated on the intended task; general descriptions of human judgment and AI speed do not establish which pairing will improve outcomes.

Vaccaro et al. (2024) synthesized 106 experiments (370 effect sizes) measuring human-alone, AI-alone and combined performance. Combinations underperformed the better of human or AI alone on average (Hedges' g=−0.23). About 42% of effect estimates were positive against that baseline; a positive estimate is not necessarily statistically significant synergy. Subgroup estimates differed by task and relative ability: the creation-task estimate was positive but nonsignificant, and the decision-task estimate negative. When humans outperformed AI alone, estimated synergy was g=0.46; when AI outperformed humans, it was g=−0.54. These subgroup results do not establish a universal task-allocation rule or a causal effect of making either party stronger.

Handa et al. (2025) mapped roughly four million Claude.ai conversations to occupational tasks and skills. Cognitive tasks were common, physical and some managerial tasks less common; use peaked in Job Zone 4 (pp.7–9). These observations describe requests, not task quality or human–AI synergy. The study did not compare human-only, AI-only and combined performance, and conversation categories do not identify the user's profession or skill (pp.5, 12). [Inference] Usage can identify settings for outcome evaluation, but cannot show where complementarity has been achieved.

Yu et al. (2024) provide specialist-context evidence on the heterogeneity of complementarity. In a randomized two-design study of 140 board-certified radiologists across 324 chest X-ray cases and 15 pathologies, the same AI assistance (a CheXpert-based DenseNet121 model) produced treatment effects spanning both substantial improvement and substantial degradation: −1.295 to +1.440 (IQR 0.797) on aggregated pathologies, and up to −8.914 to +5.563 (IQR 3.245) on the high-prevalence "abnormal" task [p.2]. Same model, same patient population, same expert pool — yet the human-AI team outperformed the human alone for some radiologists and underperformed for others. None of the conventional predictors of who would benefit (years of experience, thoracic subspecialty, prior AI-tool experience, unassisted-error baseline) reliably identified which radiologists fell on which side of zero [p.4–5].

[Inference] This supports evaluating assistance under the intended conditions. Yu et al.'s finding pushes the implication further: complementarity is not even reliably a *population-level* design problem — it is an individual-level one. The paper's operational recommendation: "without reliable predictors, it is necessary to measure radiologists' response to AI assistance under realistic simulations of deployment settings before deciding whether to provide AI assistance to different radiologists" [p.11]. This is a stronger requirement than current AI-deployment practice typically meets — most clinical AI deployments use population-level studies to justify rollout to all clinicians in a role, not per-clinician measured benefit.

The strongest predictor Yu et al. did identify is AI error itself: more accurate AI yields better treatment effects, with a roughly linear dose-response on aggregated pathologies and a treatment effect of −16.845 when AI absolute error exceeds 80 (on a 0–100 scale) [p.9]. Direction of error matters too — AI predictions that underestimate ground-truth probabilities produce better treatment effects than equally-erroneous predictions that overestimate them. The complementarity sweet spot in this expert specialist context depends not just on task structure  but on the AI model's specific failure-mode profile: a low-error AI that tends to underestimate is more complementary than a higher-error AI that tends to overestimate, even on the same diagnostic task.

Dell'Acqua et al. (2026) distinguish idea generation from selection in a preregistered field experiment at Procter & Gamble (N=791; 550 solutions). They capped idea quantity at five per participant. AI raised average rated idea quality and preserved variance in quality; AI-assisted participants were less likely to select their highest-rated idea (about 37%, versus about 50% for human teams without AI) [p.15]. Preserved quality variance does not establish diversity in every sense. The authors describe AI as a "quality amplifier rather than a decision enhancer" [p.17] and suggest that affirming feedback may "erode critical engagement" [p.16]. That mechanism was not isolated experimentally, and the study did not measure durable evaluative skill loss. Final quality remained higher with AI because generation gains outweighed selection losses. [Inference] Assess generation and selection separately when evaluating complementarity.

## Related

- [[complementarity-framework]] - framework for designing complementarity
- [[augmentation-synergy-gap]] - the distinction between merely beating the human (augmentation) and beating both parties (synergy); complementarity is synergy achieved
- [[calibration]] - trust calibration is a prerequisite for complementarity
- [[automation-bias]] - a primary barrier to achieving complementarity
- [[judgment]] - human ethical authority remains non-delegable in complementary teams
- accountability - complementarity requires clear lines of human accountability
- [[jagged-frontier]] - the uneven capability boundary that complementarity must navigate
- [[handa-economic-tasks-claude-2025]] — task-use patterns without comparative outcome measures.
- [[vaccaro-human-ai-meta-analysis-2024]] — meta-analytic anchor: synergy is a conditional minority result (42% of effect sizes), not the average outcome; task type and relative ability predict it
- [[yu-radiologists-ai-2024]] — specialist-context evidence that complementarity is heterogeneous at the individual-expert level; same AI, same tasks, same expert pool yields treatment effects spanning improvement and degradation; AI error magnitude and direction shape the complementarity outcome
- [[dellacqua-cybernetic-teammate-2026]] — field evidence for a within-process complementarity split: AI amplifies generation, human judgment retains value in evaluative selection ("quality amplifier, not decision enhancer")
- [[cybernetic-teammate]] — the reframing this evidence anchors: AI reproducing teamwork functions asymmetrically

## Sources

- [[handa-economic-tasks-claude-2025]] — Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Heck, S., Mueller, J., Hong, J., Ritchie, S., Belonax, T., Troy, K. K., Amodei, D., Kaplan, J., Clark, J., & Ganguli, D. (2025). Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations. arXiv:2503.04761 [cs.CY], February 11, 2025. Anthropic.
- [[vaccaro-human-ai-meta-analysis-2024]] — Vaccaro, M., Almaatouq, A. & Malone, T. (2024). When combinations of humans and AI are useful: a systematic review and meta-analysis. Nature Human Behaviour, 8, 2293–2303. https://doi.org/10.1038/s41562-024-02024-1
- [[yu-radiologists-ai-2024]] — Yu, F., Moehring, A., Banerjee, O., Salz, T., Agarwal, N., & Rajpurkar, P. (2024). Heterogeneity and predictors of the effects of AI assistance on radiologists. Nature Medicine, 30, 837–849. https://doi.org/10.1038/s41591-024-02850-w
- Dell'Acqua, F., Ayoubi, C., Lifshitz, H., Sadun, R., Mollick, E., Mollick, L., Han, Y., Goldman, J., Nair, H., Taub, S., & Lakhani, K. R. (2026). The Cybernetic Teammate: A Field Experiment on Generative AI and Teamwork. Organization Science, Articles in Advance. https://doi.org/10.1287/orsc.2025.20702

