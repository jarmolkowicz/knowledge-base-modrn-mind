---
status: solid
area:
- risk
- erosion
- preservation
type: paper
sources:
  - "Bartoš et al. (2026)"
---

# Bartoš et al. (2026) — Effect of AI on Learning: A Meta-Meta-Analysis

## Citation

Bartoš, F., Bujak, O. Z., Martinková, P., & Wagenmakers, E.-J. (2026). *Effect of Artificial Intelligence on Learning: A Meta-Meta-Analysis.* University of Amsterdam, Czech Academy of Sciences, Charles University. Data and code: https://osf.io/p3xah

## Type

Paper (study-level meta-meta-analysis with publication-bias-adjusted Bayesian model averaging; preregistered framework, 1,840 effect sizes from 67 meta-analyses across 41 articles).

## Key Insight

Publication-bias adjustment substantially reduced the average estimated learning benefit in this meta-meta-analysis, without establishing a null effect. Across 1,840 effect sizes drawn from 67 meta-analyses, the complete-data three-level RoBMA-PSMA model estimated SMD = 0.196 (95% credible interval [0.000, 0.323]), compared with an unadjusted estimate of 0.629. The model reported evidence for an overall effect (BF₁₀ = 13.3).

Between-study heterogeneity was large (τ = 0.869; prediction interval −1.521 to 1.908). Subgroup analyses did not identify consistently beneficial settings or substantially resolve that heterogeneity. These results limit broad claims about learning benefits; they do not identify a general harm mechanism or show that the included outcomes were merely assisted performance.

## Key Passages

> "Publication bias-adjusted analyses reveal model-averaged effects approximately one-third the magnitude of unadjusted estimates (standardized mean difference, SMD = 0.196, 95% credible interval from 0.000 to 0.323), along with wide prediction intervals spanning both large negative and positive effects (−1.521 to 1.908)."
> — Bartoš et al. (2026), abstract, [p.2]

> "In the complete data set, a three-level RoBMA-PSMA finds strong evidence for an overall effect (BF₁₀ = 13.3). The model-averaged effect size of SMD = 0.196 [0.000, 0.323] is approximately three times lower than the publication bias-unadjusted estimate of SMD = 0.629 [0.572, 0.685]."
> — Bartoš et al. (2026), Results, [pp.12-13]

> "Crucially, the model-averaged estimate is accompanied by extreme between-study heterogeneity, τ = 0.869 [0.822, 0.926] (BF heterogeneity > 1.00 × 10⁶). Consequently, the prediction interval (PI) of true study effects ranges from −1.521 to 1.908, spanning large negative and positive treatment effects."
> — Bartoš et al. (2026), Results, [p.13]

> "While the publication bias unadjusted BMA meta-analysis finds strong evidence for the presence of the effect (BF₁₀ > 10) in 41 out of 44 meta-analyses with at least 10 effect size estimates, ... the publication bias adjustment with RoBMA-PSMA does not find any meta-analysis with at least 10 effect sizes estimates and strong evidence in favor of the effect of AI/LLMs on learning."
> — Bartoš et al. (2026), Results, [pp.20-21]

> "Subgroup analyses by outcome type, educational field, educational level, and the role of AI/LLMs failed to substantially reduce this heterogeneity or identify subgroups with consistent benefits."
> — Bartoš et al. (2026), Discussion, [p.21]

> "Although our meta-meta-analysis estimates the direct effects of AI and LLM use on learning outcomes, these estimates capture only a narrow subset of the total educational impact... null or heterogeneous average effects may signal a misalignment between systemic changes and current measurement tools rather than limited educational value."
> — Bartoš et al. (2026), Discussion, [p.23]

> "While we believe it is a priori plausible that AI/LLMs may have a positive impact on learning, the current empirical evidence base is insufficiently diagnostic and does not warrant concrete recommendations for educational practice or policy."
> — Bartoš et al. (2026), Discussion, [pp.23-24]

## Relevance

- **Magnitude and uncertainty.** Bias adjustment reduced the model-averaged estimate to roughly one-third of the unadjusted estimate. This result depends on the models and available data; it is not proof that every positive study is biased.
- **Different levels of analysis.** The complete-data model retained evidence for a positive average. Separately, none of the 44 individual meta-analyses with at least ten effect sizes retained strong evidence under the specified bias-adjusted analysis. These are different results, not a contradiction.
- **Mechanisms remain open.** The discussion considers reduced engagement and offloading as possible explanations. The meta-meta-analysis does not test mediation by these processes, separate all assisted from unaided outcomes, or show which mode of use caused the observed heterogeneity.

## Supports

- [[performance-paradox]] — context for evaluating learning claims, not a direct test of assisted–unaided performance differences
- [[novice-vulnerability]] — does not directly test differences in vulnerability between novices and experts
- [[metacognitive-laziness]] — a possible explanation discussed, not an established mediator
- [[cognitive-debt]] — related hypothesis; accumulated debt is not measured
- [[leveling-effect]] — educational-level subgroups do not test whether lower-performing individuals benefit more
- [[fluency-bias]] — [Inference] polished summaries still require scrutiny of their evidence; fluency was not measured
- [[capacity-erosion]] — a wide prediction interval is not evidence of lasting skill loss
- [[cognitive-offloading]] — a candidate explanation in the discussion, not a mechanism identified by bias correction

## Contradicts / Extends

- [[bastani-guardrails-math-rct-2025]] distinguishes assisted practice from later unaided assessment in a specific classroom intervention. The umbrella does not independently validate that intervention's mechanism.
- [[fan-metacognitive-laziness-2025]] and [[kosmyna-cognitive-debt-2025]] examine different process measures. Citing them in a discussion does not demonstrate a common causal pathway.
- Challenges unqualified claims of large, general learning benefits drawn from unadjusted averages. It does not justify automatically rejecting positive findings or treating all AI use as harmful.

## Open Questions

- **Mode-of-use moderators not measured.** The umbrella could not test the moderators KB entries already emphasise — guardrails, mode of use (active vs. passive), assessment design, sequencing of unaided practice before AI assistance — because the constituent meta-analyses did not extract them. Bartoš explicitly notes this limitation [pp.7-8]: study-level moderator information was unavailable for many included meta-analyses. *The KB needs primary studies (Bastani 2025; Lee, Yin et al. 2026; Kosmyna 2025) to fill this gap; the umbrella anchors the field, but does not resolve "what works."*
- **Pre/post-ChatGPT comparison.** No substantial difference between studies published before vs. after January 2023 (publication-bias-adjusted SMDs of 0.018 [−0.007, 0.222] and 0.108 [0.000, 0.395] respectively) suggests modern LLMs have not produced a categorically different pattern from earlier AI-tutor work. [Inference] This challenges the popular "ChatGPT changed everything" narrative for learning outcomes, but the post-2023 sample is still small (518 estimates from a young literature).
- **What the umbrella cannot resolve.** Bartoš et al. note (Discussion, [pp.22-23]) that "AI/LLMs also transform education indirectly by reshaping metacognition, instructional practices, feedback processes, and assessment systems, effects that often escape detection by short-term achievement measures." The smaller positive model-averaged estimate and wide prediction interval do not settle AI's wider educational effects. The passage discusses limitations of measured outcomes; it does not change the reported average into a null effect.
- **What it would take to update the estimate.** "Extending the meta-meta-analysis with an additional effect size estimate from a hypothetical study of infinite sample size would add less than three observations worth of effective sample size" [pp.21-22]. The path to a more diagnostic estimate is not more studies but better-designed studies — preregistered, large-scale, with standardized outcome measures and registered replication reports.
