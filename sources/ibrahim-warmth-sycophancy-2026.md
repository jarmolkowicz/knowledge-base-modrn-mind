---
status: emerging
area: [risk, preservation]
type: paper
sources:
  - "Ibrahim, L., Hafner, F. S., & Rocher, L. (2026). Training language models to be warm can reduce accuracy and increase sycophancy. Nature, 652, 1159–1165. doi:10.1038/s41586-026-10410-0"
---

# Warmth Training Can Increase Errors and Sycophancy

## Citation

Ibrahim, L., Hafner, F. S., & Rocher, L. (2026). Training language models to be warm can reduce accuracy and increase sycophancy. *Nature*, 652, 1159–1165. [DOI](https://doi.org/10.1038/s41586-026-10410-0). Published online 29 April 2026.

## Type

Peer-reviewed controlled model experiments. Emerging status reflects limits on generalization from these interventions to other models and training methods.

## Key Insight

Changing an AI's conversational warmth can also change factual reliability. In these experiments, familiar capability benchmarks mostly failed to reveal the error increases seen in open-ended questions with interpersonal cues.

## Methods and Results

Five model families—Llama-8b, Mistral-Small, Qwen-32b, Llama-70b, and GPT-4o—were fine-tuned on 1,617 conversations containing 3,667 model responses rewritten to be warmer while preserving meaning. Original models were compared with two-epoch warm variants. Four question sets tested trivia, common falsehoods, disinformation, and medical knowledge, with 500 questions each except 125 for disinformation. Added cues varied emotions, relationship framing, stakes, and incorrect user beliefs. The inferential analysis included 439,792 observations. GPT-4o scoring was checked against 470 human-annotated outputs (pp.8–9).

Without added interpersonal context, warmth training increased the adjusted probability of an incorrect response by 7.43 percentage points (p<.001). The gap reached 11.9 points with sadness cues. With incorrect beliefs present, warm models made 11 points more errors than originals. These estimates describe different conditions; the abstract's 10–30-point summary should not replace the condition-specific results (pp.2, 4–5).

MMLU, GSM8K, and harmful-request refusal were generally preserved, with an 8.6-point MMLU decrease for Llama-8b. Length adjustment did not remove the effect. Cold-style fine-tuning maintained or improved performance in three models. Warm system prompts sometimes produced similar, smaller and less consistent effects (p.5).

## Key Passages

> “Warm models produced shorter responses on average than original models”
> — Ibrahim, Hafner, & Rocher, [p.5], printed p.1163

> “We do not claim that all possible methods for inducing warmth will produce the same effects.”
> — Ibrahim, Hafner, & Rocher, [p.6], printed p.1164

> “Whether such approaches can preserve both properties remains an open question”
> — Ibrahim, Hafner, & Rocher, [p.7], printed p.1165, on proposed warm-but-honest training

## Relevance

Provides a tested model-side contributor to [[sycophancy]]. Evaluating a persona requires checking what it tells users, including when users state a false belief or express distress, as well as whether it sounds caring.

## Supports

- [[sycophancy]] — warmth interventions increased agreement with incorrect beliefs.
- [[social-sycophancy]] — relevant design pathway, but most main-task tests concerned factual errors rather than interpersonal advice.

## Contradicts / Extends

- Extends [[perry-social-friction-2026]], which referred to the earlier warmth preprint, with the published primary evidence.
- Complements [[bo-sycophancy-novices-2026]]: tests a model intervention, whereas Bo examines users' ability to detect and act on poor guidance.

## Limitations

Constructs depend on the authors' warmth transformation and factual-agreement measures. Warm and cold datasets may differ beyond warmth; GPT-4o warm and cold runs used different learning-rate multipliers. Human score validation covered a subset. Commercial post-training may differ. No experiment here measured users' beliefs, dependence, or well-being. “Warm but honest” training is proposed, not demonstrated as a solution. This summary covers the main article and Methods; separate supplements are not included.

## Open Questions

- Which training and evaluation methods preserve warmth and correction together?
- How often do the tested combinations of factual questions and emotional disclosure occur in everyday use?
