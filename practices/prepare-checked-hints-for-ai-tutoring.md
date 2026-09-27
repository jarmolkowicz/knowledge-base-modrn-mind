---
status: emerging
area:
- preservation
sources:
- 'Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Marimane, R. (2025).
  Generative AI without guardrails can harm learning: Evidence from high school mathematics.
  Proceedings of the National Academy of Sciences, 122(26), e2422633122.'
source_entries:
- bastani-guardrails-math-rct-2025
intended_outcomes:
- independent-capability
- understanding
---

# Prepare checked hints for AI tutoring

## Use When

An educator is preparing AI-supported practice on material already introduced, and can supply correct solutions and feedback. This is a bounded adaptation of a studied mathematics-tutoring package.

## Try It

1. Prepare each problem, one or more correct solutions, common mistakes and helpful feedback.
2. Configure the tutor to use that material and offer hints without directly giving away the answer.
3. Have learners attempt the problems; review correct solutions after practice.
4. Check learning on similar problems without the tutor. Keep this result separate from assisted practice scores.

[Inference] Applying the package outside the studied classroom is an adaptation. Inspect sample tutor responses before use and arrange educator correction of bad feedback. These checking arrangements are editorial; teacher-provided answers do not guarantee error-free output.

## Origin

Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Marimane, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. Proceedings of the National Academy of Sciences, 122(26), e2422633122.

Main paper PDF p.2, Experimental Design and footnotes; p.3, study procedure; p.4, Table 1 and results. Based on the main-paper description, not the full supplementary implementation. Title is editorial.

[Retained original](<../raw/bastani-guardrails-math-rct-2025/source.md>). 

## Evidence and Rationale

**Basis:** Randomized classroom study of nearly 1,000 students in a Turkish high school, with four sessions. GPT Tutor combined hint-oriented instructions with teacher-prepared problem-specific material.

**Observed or reported:** Assisted practice scores improved. GPT Base users subsequently scored worse than control on same-session unaided exams; GPT Tutor users had no statistically detectable exam difference from control. The study did not isolate the effect of each tutor feature.

**Intended:** independent-capability, understanding. These are curator-assigned intended benefits, not demonstrated effects.

**Untested:** The effectiveness of this exact routine in its proposed AI-use setting, including durable independent capability, better judgment and calibrated confidence. Immediate output quality, felt competence and later unaided performance are distinct outcomes.

## Limits

This is not an exact implementation recipe or a claim that a hint-only prompt prevents harm. No equivalence test or durable transfer benefit is established. Preparing checked material takes educator work.

## What to Notice

[Inference] What can the learner explain or solve on the separate unaided task, rather than only with hints available?

## Related

- [[ask-about-the-gap-then-do-the-task]]
- [[explain-it-back-before-the-correction]]

## Sources

- [[bastani-guardrails-math-rct-2025]] — origin of the research, recommendation or framework; exact editorial additions identified above.
