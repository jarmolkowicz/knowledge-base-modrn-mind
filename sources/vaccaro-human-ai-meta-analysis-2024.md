---
status: solid
area: [risk, preservation]
type: paper
sources:
  - "Vaccaro, M., Almaatouq, A. & Malone, T. (2024). When combinations of humans and AI are useful: a systematic review and meta-analysis. Nature Human Behaviour, 8, 2293–2303. https://doi.org/10.1038/s41562-024-02024-1"
---

# Vaccaro, Almaatouq & Malone (2024) — When Combinations of Humans and AI Are Useful

## Citation

Vaccaro, M., Almaatouq, A. & Malone, T. (2024). When combinations of humans and AI are useful: a systematic review and meta-analysis. *Nature Human Behaviour*, 8, 2293–2303. https://doi.org/10.1038/s41562-024-02024-1

## Type

Paper (preregistered PRISMA systematic review and three-level meta-analysis; 106 experiments from 74 papers, 370 effect sizes; MIT Center for Collective Intelligence).

## Key Insight

The widespread assumption that "human + AI is better than either alone" does not hold on average. Across 106 experiments, human-AI combinations performed *worse* than the best of human-or-AI alone (Hedges' g = −0.23) — no human-AI **synergy** on average. But against the weaker baseline of the human working alone, combinations did help (**human augmentation**, g = 0.64). Whether the combination helps or hurts depends on the task (negative decision-task synergy; positive but nonsignificant creation-task estimate) and on relative ability (gains when the human is the stronger party, losses when the AI is). Complementarity is a specific, conditional achievement, not a default of putting a human and an AI together.

## Key Passages

> "First, we found that, on average, human–AI combinations performed significantly worse than the best of humans or AI alone (Hedges' g = −0.23; 95% confidence interval, −0.39 to −0.07)."
> — Vaccaro et al. 2024, [p.1] (Abstract)

> "In other words, the human–AI systems we analysed were, on average, better than humans alone but not better than both humans alone and AI alone."
> — Vaccaro et al. 2024, [p.3] (Overall levels of human–AI synergy)

> "When the human alone outperformed the AI alone, the combined human–AI system outperformed both alone... But when the AI alone outperformed the human alone, performance losses occurred in the combined system relative to the AI alone."
> — Vaccaro et al. 2024, [p.3] (Discussion)

> "Much of the recent research in human–AI collaboration has focused on using AI systems to help humans make decisions by providing not only suggested decisions but also confidence levels or explanations. But we found that neither of these factors significantly affected the performance of human–AI systems."
> — Vaccaro et al. 2024, [p.2] (Introduction)

> "Decision tasks were associated with performance losses, and creation tasks were associated with performance gains."
> — Vaccaro et al. 2024, [p.4] (Moderating effect of task type)

## Key Findings

**Two outcomes, two baselines** [p.2]. The paper separates two success criteria:
- **Human-AI synergy** — the combination beats *both* the human alone *and* the AI alone (the demanding bar; the paper's primary outcome).
- **Human augmentation** — the combination beats the *human alone* (the weaker bar; relevant when full automation is barred for legal, ethical, safety, or value-alignment reasons).

**Main effects** [p.3]:
- Synergy: pooled g = −0.23 (t₉₂ = −2.89; P = 0.005; 95% CI −0.39 to −0.07) — a small, significant *loss*. 213 of 370 effect sizes (58%) underperformed the better of human-or-AI alone.
- Augmentation: pooled g = 0.64 (t₉₈ = 11.87; P = 0.000; 95% CI 0.53 to 0.74) — medium-to-large *gain*. 314 of 370 (85%) outperformed the human alone.

**Significant moderators**:
- *Task type* [p.4] (F₁,₁₀₄ = 7.84; P = 0.006). Decision tasks (choosing among a finite set of options; n = 344): synergy g = −0.27 (P = 0.002) — losses. Creation tasks (open-response content; n = 34): synergy g = 0.19 (P = 0.180, not significant on its own, but the decision-vs-creation difference is significant).
- *Relative performance* [p.3] (F₁,₁₀₄ = 81.79; P = 0.000). When the human outperformed the AI alone (n = 127): synergy g = 0.46 — gains. When the AI outperformed the human alone (n = 251): synergy g = −0.54 — losses. Augmentation in the AI-stronger case was still positive (g = 0.74).

**Non-significant moderators** [p.2–3]: AI explanations, AI confidence displays, participant type (expert vs. crowdworker), and division of labour did *not* significantly affect synergy or augmentation — despite explanations and confidence being a major focus of human-AI interaction research.

**Heterogeneity** [p.3]: very high (I² = 97.7% for synergy, 93.8% for augmentation) — effects vary enormously across studies, and the moderators explain only part of it.

**Robustness** [p.8]: the synergy result showed no evidence of publication bias (Egger's regression P = 0.438) and held under leave-one-out and outlier-exclusion checks. Augmentation diagnostics indicated potential publication bias (Egger's P = 0.002). The authors did not estimate a bias-corrected effect. Upward bias is possible; these tests do not establish a numerical upper bound.

## Relevance

This is the strongest cross-task empirical synthesis the KB holds on human-AI complementarity. It does four things for the KB:

1. **Anchors `[[human-ai-complementarity]]` empirically.** That concept was `status: speculative` and asserted that "meta-analyses show that human-AI teams can outperform either party alone." Vaccaro et al. is *the* meta-analysis on the question, and the finding is the reverse: synergy is the exception (42% of effect sizes), not the rule. The concept's claim needs qualifying, and this source provides the evidence to do it carefully.
2. **Supplies the named distinction behind `[[augmentation-synergy-gap]]`** — synergy vs. augmentation as two separate bars, with the empirical fact (85% augment, 42% synergize) that they routinely come apart.
3. **Gives `[[complementarity-framework]]` real empirical grounding** for two of its "factors shaping complementarity" — task characteristics and relative ability — and an empirical caution on a third (the null result for explanations/confidence speaks directly to the framework's interrogation and interface principles).
4. **Sets the scope for `[[dellacqua-jagged-frontier-2023]]` and `[[yu-radiologists-ai-2024]]`** — those are point-studies of single firms or domains; this is the population they sit inside.

The paper's voice aligns with KB voice: it frames the null result not as AI-pessimism but as a design agenda ("promising directions for designing future human–AI systems"). It is careful about its own limitations (lab not field; only studies reporting all three conditions; publication bias on the augmentation side).

## Supports

- [[human-ai-complementarity]] — the meta-analytic anchor; synergy *is* the paper's operationalization of complementarity, and the finding is that it is conditional and not the average outcome.
- [[augmentation-synergy-gap]] — primary source for the distinction; a system can clear the augmentation bar (beats the human) without clearing the synergy bar (beats the AI alone).
- [[complementarity-framework]] — empirically confirms task type and relative ability as moderators of complementarity.
- [[automation-bias]] — the paper attributes decision-task losses partly to overreliance (humans following AI suggestions without further processing).
- [[performance-paradox]] — related "looks good by the wrong metric" pattern: the augmentation baseline can make a human-AI system look successful even when AI alone would do better.
- [[jagged-frontier]] — both address task variation, but their comparisons differ: augmentation against humans alone is not synergy against the better single performer.

## Contradicts / Extends

- Complements: [[dellacqua-jagged-frontier-2023]] — the field experiment compares assisted with unassisted human performance across tasks. Vaccaro's synergy comparison also requires AI-alone performance; the two patterns are not equivalent.
- Extends: [[yu-radiologists-ai-2024]] — Yu et al. document heterogeneous AI-assistance effects within one diagnostic domain; Vaccaro et al. quantify the heterogeneity across domains (I² = 97.7%) and name two of its sources.
- Qualifies: [[handa-economic-tasks-claude-2025]] — Handa et al. map *where* AI is used; Vaccaro et al. show that usage does not imply the combination outperforms either party alone on the studied performance dimensions.
- Does not contradict any existing source. The closest tension is with the optimistic "human + AI" framing implicit in several entries; Vaccaro et al. is the corrective evidence, not a contradiction of a specific finding.

## Open Questions

- The dataset is dominated by decision tasks (n = 344) and thin on creation tasks (n = 34). The creation-task gain is suggestive but underpowered. [Inference] Whether generative-AI creation work reliably produces synergy is still open and is the paper's flagged research priority.
- Almost all studies (>95%) have the human making the final decision after seeing AI input. Synergy under other interaction designs — predetermined division of labour, AI-final with human override, dynamic allocation — is barely represented (n = 4 for division of labour) and untested at scale.
- The studies are lab experiments from 2020–2023, predating wide deployment of frontier generative models. [Inference] Whether the synergy deficit narrows with more capable models, or with practitioners who have adapted their workflows, is unanswered.
- Heterogeneity remains largely unexplained (I² = 97.7%). The significant moderators leave most of the variance uncaptured — what else governs whether a combination helps is still open.
