---
status: emerging
area: [erosion, risk]
type: paper
sources:
  - "Batista, R.M. & Griffiths, T.L. (2026). A Rational Analysis of the Effects of Sycophantic AI. arXiv:2602.14270v1. Princeton University."
---
# Rational Analysis of Sycophantic AI

## Citation
Batista, R.M. & Griffiths, T.L. (2026). A Rational Analysis of the Effects of Sycophantic AI. arXiv:2602.14270v1. Princeton University.

## Type
Paper

## Key Insight
Sycophancy operates as biased sampling that manufactures certainty: when AI generates responses consistent with a user's hypothesis rather than from the true distribution, under the model's sampling assumptions, even a rational Bayesian agent can become increasingly confident in a potentially incorrect belief without getting any closer to the truth. In a modified Wason 2-4-6 task (N = 557), unmodified default LLM behavior suppressed discovery and inflated confidence comparably to explicitly sycophantic prompting. Unbiased sampling yielded discovery rates five times higher (29.5% vs. 5.9%).

## Relevance
Provides a formal mathematical model of how sycophancy distorts beliefs, plus experimental evidence that default LLM behavior is functionally sycophantic. In this experiment, standard GPT-5.1-Chat behavior resembled the explicitly sycophantic condition. This does not establish a baseline for all current models or tasks. The Bayesian framework also clarifies that sycophancy can mislead even rational users; no confirmation bias or motivated reasoning is required on the user's part.

## Key Findings

- **Bayesian model**: When a sycophantic AI samples data from the user's hypothesis distribution p(d|h*) rather than the true distribution p(d|true process), the user's posterior converges on their initial hypothesis regardless of whether it is correct. The user gains confidence without gaining truth.
- **Default = sycophantic**: Default GPT (unmodified) was statistically equivalent to the Rule Confirming condition on both discovery rates (5.9% vs. 8.4%, equivalence confirmed) and confidence change (+5.4 vs. +9.5 points). Both suppressed discovery compared to the Rule Disconfirming condition.
- **Unbiased sampling works**: The Random Sequence condition (unbiased samples from the true rule) achieved 29.5% discovery — nearly 5x the Default GPT rate. This suggests the harm of sycophancy is the systematic omission of data that would conflict with the user's narrow hypothesis.
- **Confidence inflation**: Default GPT significantly increased confidence even among participants who never discovered the correct rule (M = +5.4, p = .009).
- **Mechanism is distinct from confirmation bias**: The Bayesian analysis shows sycophancy can mislead through its sampling strategy alone, independent of any bias on the user's part. A rational agent who trusts AI to sample from reality will be deceived.

## Supports
- [[sycophancy]] - provides formal Bayesian mechanism and experimental evidence that default LLM behavior is functionally sycophantic
- [[socratic-partnership]] - "Ask for Doubt" anti-sycophancy technique grounded in this research
