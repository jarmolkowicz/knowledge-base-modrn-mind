---
status: emerging
area: [risk]
type: paper
sources:
  - "Cheong, I., Guo, A., Lee, M., Liao, Z., Kadoma, K., Go, D., Chang, J. C., Henderson, P., Naaman, M., & Zhang, A. X. (2025). Penalizing Transparency? How AI Disclosure and Author Demographics Shape Human and AI Judgments About Writing. arXiv:2507.01418v1."
---

# Cheong et al. (2025) — Penalizing Transparency

## Citation

Cheong, I., Guo, A., Lee, M., Liao, Z., Kadoma, K., Go, D., Chang, J. C., Henderson, P., Naaman, M., & Zhang, A. X. (2025). Penalizing Transparency? How AI Disclosure and Author Demographics Shape Human and AI Judgments About Writing. *arXiv:2507.01418v1* (CHIWORK 2025 Workshop on Generative AI Disclosure).

**URL:** [arXiv preprint](https://arxiv.org/abs/2507.01418)

## Type

Paper (pre-registered factorial experiment, n=1,970 human raters + 2,520 LLM evaluations)

## Key Insight

A 2×3×3 factorial design (AI disclosure × race × gender) shows that **disclosing AI assistance produces a measurable penalty in writing-quality judgments — among both human and LLM evaluators**. The disclosure penalty is modest in absolute terms (less than 0.15 points on a 7-point scale, p<0.05) but consistent.

A second finding is **"vanishing alignment"** in LLM raters: GPT-4o-mini and Qwen2.5-7B-Instruct each showed fairness-oriented preferences in the control condition (GPT favored Black authors, +0.137 vs. Asian; Qwen favored women, +0.133 vs. men, both p<0.001), but those preferences **disappeared when AI assistance was disclosed**. The same identical article, judged by the same model, gets a different demographic-fairness adjustment depending on whether it carries an "AI was used" label.

The authors interpret the interaction as a possible limit on the stability of fairness-related behavior. The experiment does not identify a training mechanism or test hiring, exam grading or performance reviews.

For human thinking with AI: this is an erosion-of-fairness mechanism, not a [[capacity-erosion|capacity erosion]] mechanism. In this article-rating task, demographic interactions appeared among model raters but were not detected among human raters. The same transparency norm has different equity consequences depending on who's reading.

## Key Passages

> "We find that both human and LLM raters consistently penalize disclosed AI use. However, only LLM raters exhibit demographic interaction effects: they favor articles attributed to women or Black authors when no disclosure is present. But these advantages disappear when AI assistance is revealed."
> — Cheong et al., [p.1] (abstract)

> "Both models presented statistically significant AI disclosure penalty (-0.112 points, p = 0.002 for GPT-4o-mini and -0.133 points, p = 0.026 for Qwen2.5-7B-Instruct). However, unlike humans, the AI models demonstrated distinct demographic preferences in the control condition."
> — Cheong et al., [p.3]

> "Both favored groups — Black authors and women — are historically marginalized. These preferences may reflect an alignment-driven over-correction, in which models trained with human feedback disproportionately reward underrepresented identities. However, when AI disclosure is present, these fairness-oriented preferences vanish. We term this dynamic a form of 'vanishing alignment,' where the social and ethical calibration of model behavior becomes fragile under changing contextual cues."
> — Cheong et al., [p.4]

> "Beneath these questions lies a desire to calibrate judgments to discern the boundary between human insight and synthetic fluency."
> — Cheong et al., [p.1]

> "If reader perceptions about AI disclosure are filtered through gendered, racialized, or other socio-epistemic cues, then the burden of openness becomes asymmetrical. … the groups historically under-resourced and under-represented face the greatest risk of stigmatization for using AI."
> — Cheong et al., [p.2]

## Methodology

- 1,970 human raters via pre-registered between-subjects design
- 2,520 LLM ratings: 1,260 each from GPT-4o-mini and Qwen2.5-7B-Instruct
- Single human-authored news article; only the author's photo, biography, and disclosure statement varied across 18 conditions (2 disclosure × 3 races × 3 genders)
- Dependent measures: trustworthiness, comprehensiveness, writing quality, share likelihood (7-point Likert; mean = perception score)
- Manipulation checks: only 1.1% of participants correctly guessed the study purpose

## Relevance

The study quantifies a modest disclosure penalty and finds demographic interactions in two model raters evaluating one news article. It informs [[disclosure-penalty]] and [[transparency-paradox]], while leaving the mechanism open.

The authors call the changing demographic preferences "vanishing alignment." They propose an alignment-related explanation; RLHF or fairness training was not experimentally manipulated. Results do not establish a general switch that turns model fairness on or off.

## Supports

- [[disclosure-penalty]] — quantifies the effect with pre-registered N=1,970
- [[transparency-paradox]] — provides empirical grounding
- [[raj-disclosure-penalty-2026]] — converging evidence (Raj et al. follow-up work in the same space)
- [[automation-bias]] — LLMs as evaluators amplify the same dynamic Goddard documented for clinical decision support
- [[fluency-bias]] — readers calibrate against "synthetic fluency"; the disclosure cue partially counteracts the fluency-truth coupling

## Contradicts / Extends

- Extends [[raj-disclosure-penalty-2026]] with a demographic-interaction question in a different design.
- [[ai-moralization]] raises related questions about social judgments of AI use; moralization was not measured here.
- [Inference] The pattern raises questions about whether evaluators behave consistently across contextual cues. Generalization beyond these two models and this article remains untested.

## Open Questions

- The effect was tested on news articles (a genre with strong objectivity expectations). Does the disclosure penalty hold for genres where AI assistance is normalized (marketing copy, code documentation, entertainment writing)?
- "Vanishing alignment" was demonstrated for two models on demographic dimensions. What's the breadth of contextual cues that toggle alignment behaviors? (Authorship signals? Topic? Politeness markers?)
- The study cannot disentangle whether the disclosure penalty is from perceived authorship dilution, perceived effort reduction, or epistemic stigma per se. Each implies a different intervention.
