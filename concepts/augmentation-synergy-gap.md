---
status: emerging
area: [risk, preservation]
sources:
  - "Vaccaro, M., Almaatouq, A. & Malone, T. (2024). When combinations of humans and AI are useful: a systematic review and meta-analysis. Nature Human Behaviour, 8, 2293–2303. https://doi.org/10.1038/s41562-024-02024-1"
---

# Augmentation-Synergy Gap

## What It Is

A human-AI system can clear two very different bars. **Augmentation** means the combination outperforms the human working alone. **Synergy** means it outperforms *both* the human alone *and* the AI alone. The augmentation-synergy gap is the routine fact that systems clear the first bar without clearing the second: the AI helps the human, yet the human-AI pair still does worse than the AI would have done on its own.

## Why It Matters

Which baseline an evaluation uses silently decides whether a human-AI system looks like a success. Benchmark against the human alone and most systems pass — Vaccaro et al. (2024) found 85% of human-AI effect sizes beat the human-alone baseline. Benchmark against the better of human-or-AI alone and most systems fail — only 42% beat it; on average the combination performed *worse* than the best single party (Hedges' g = −0.23). An evaluation against humans alone can miss the AI-alone benchmark on the measured task. [Inference] That benchmark should inform design, but a higher task score alone does not settle whether removing human involvement is safe or desirable.

## Key Insight

Augmentation is necessary but not sufficient for synergy, and the two come apart often enough that "the AI helped" is not evidence that the combination is the right design. The correct baseline is not automatic — it depends on context. Where full automation is barred for legal, ethical, safety, or value-alignment reasons, augmentation is the meaningful bar: the human must stay, so "better than the human alone" is the real question. Where automation is genuinely an option, compare the combination with AI alone on the outcomes that matter. [Inference] Task allocation also requires context-specific assessment of safety, robustness, cost, learning, accountability and user values. Failure to show synergy on one measure is not an automatic instruction to remove the human. Naming the gap forces the prior question — *which baseline actually applies here?* — before a human-AI workflow is called a win. This is distinct from the [[performance-paradox]], which is about durable human competence rather than system performance: the augmentation-synergy gap can be real even when no skill is being eroded at all.

## Related

- [[human-ai-complementarity]] — synergy is complementarity achieved; the gap is the space between augmentation and that achievement
- [[complementarity-framework]] — a framework for designing toward synergy rather than settling for augmentation
- [[performance-paradox]] — a parallel "right result, wrong metric" trap, but about learning rather than system performance
- [[automation-bias]] — overreliance is one mechanism that keeps augmenting systems short of synergy
- [[jagged-frontier]] — task-dependent assistance effects; the human-alone comparison differs from the better-of-human-or-AI synergy baseline
- [[vaccaro-human-ai-meta-analysis-2024]] — meta-analytic source for the distinction and the 85%-vs-42% split

## Sources

- [[vaccaro-human-ai-meta-analysis-2024]] — Vaccaro, M., Almaatouq, A. & Malone, T. (2024). When combinations of humans and AI are useful: a systematic review and meta-analysis. Nature Human Behaviour, 8, 2293–2303. https://doi.org/10.1038/s41562-024-02024-1

