---
status: emerging
area: ["risk","preservation"]
type: paper
sources:
  - "El, B., Su, S., Pappu, A., Yin, P., Heng, J., Heng, E., Wang, R., Haupt, A., & Zou, J. (2026). Position: AI development should prioritize cognitive security. Preprint, April 26, 2026. https://www.cstf.dev/icml_position_cstf-2.pdf"
---

# El et al. (2026) — Measuring AI Influence Without Treating All Persuasion as Harm

## Citation

El, B., Su, S., Pappu, A., Yin, P., Heng, J., Heng, E., Wang, R., Haupt, A., & Zou, J. (2026). Position: AI development should prioritize cognitive security. Preprint, April 26, 2026. https://www.cstf.dev/icml_position_cstf-2.pdf

Supplied 18-page preprint dated April 26, 2026. A [workshop version](https://openreview.net/pdf?id=5pShDP8LSm) exists; this draft follows the supplied version and does not merge versions.

Audit: [ingestion record](../raw/el-cognitive-security-2026/log.md).

## Type

Position paper and research agenda; synthesizes other studies and proposes measures, without a new intervention dataset.

## Key Insight

A change in choice is not enough to describe AI influence. The authors propose separately measuring its size, persistence, self-reinforcing use and users' awareness of the influence.

## Key Findings

- Cognitive security is defined around hazardous influence on cognitive processes. The boundary depends on contextual legal and normative judgments, not persuasion alone (pp.1–2).
- Conversion concerns immediate change; persistence its duration; dependence self-reinforcing elevated engagement; provenance awareness of when and how AI shaped beliefs (pp.7–8).
- Defensive aims should support independent evaluation rather than replace an attacker's preferred belief with a defender's (p.6).
- Proposed simulations are for hypothesis development, followed by human validation. Neither metrics nor defenses are established as a validated package (pp.8–9).
- The authors acknowledge mixed causal evidence, often modest durable changes, research costs and dual-use risks (pp.8–9).

## Key Passages

> "the goal is not to substitute the defender’s preferred beliefs for the attacker’s, but to restore the individual’s ability to evaluate information and form judgments."
> — El et al. (2026) — Measuring AI Influence Without Treating All Persuasion as Harm, PDF p.6

> "User awareness of when and how generative AI shapes their beliefs."
> — El et al. (2026) — Measuring AI Influence Without Treating All Persuasion as Harm, PDF p.8

## Relevance

Adds measurement boundaries to [[conversational-steering]]. No new cognitive-security concept or method is proposed for this PARTIAL batch.

## Supports

- [[conversational-steering]] — distinguish choice shifts from persistence and awareness.
- [[agency]] — independent evaluation differs from moving people toward a preferred belief.
- [[belief-offloading]] — tracks awareness of delegated influence without assuming all delegation is harmful.

## Contradicts / Extends

Extends the questions raised by [[werner-conversational-ai-steering-2024]]; it does not add another estimate of steering prevalence or an established protective intervention.

## Limitations

Normative and conceptual framework, not a validated measurement instrument. Baseline beliefs need not be true or desirable; restored autonomy cannot simply be assumed from return to baseline. Engagement intensity alone does not diagnose harmful dependence.

## Open Questions

- Which measures distinguish informed preference change from manipulation?
- Can defenses improve independent judgment without imposing preferred beliefs?
