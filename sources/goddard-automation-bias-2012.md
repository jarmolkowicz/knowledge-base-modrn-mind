---
status: solid
area: [erosion, risk]
type: paper
sources:
  - "Goddard, K., Roudsari, A., & Wyatt, J. C. (2012). Automation bias: A systematic review of frequency, effect mediators, and mitigators. Journal of the American Medical Informatics Association, 19(1), 121–127. doi:10.1136/amiajnl-2011-000089"
---

# Goddard, Roudsari & Wyatt (2012) — Automation Bias: A Systematic Review

## Citation

Goddard, K., Roudsari, A., & Wyatt, J. C. (2012). Automation bias: A systematic review of frequency, effect mediators, and mitigators. *Journal of the American Medical Informatics Association*, 19(1), 121–127.

**DOI:** [10.1136/amiajnl-2011-000089](https://doi.org/10.1136/amiajnl-2011-000089)

## Type

Paper (PRISMA-style systematic review of 74 studies)

## Key Insight

Automation bias (AB) — "the tendency to over-rely on automation" — is a robust, cross-domain effect, not a curiosity of any one field. Goddard et al.'s meta-analysis of healthcare clinical decision support studies (CDSS) finds that erroneous advice was **26% more likely to be followed** when delivered by a CDSS compared with no-CDSS controls (RR 1.26, 95% CI 1.11–1.44, p<0.0005). Negative consultations — cases where a user's correct unaided decision is *changed to incorrect* after consulting the system — occur in 6–11% of cases.

Three structural findings the KB inherits:

1. **AB has two failure modes.** Errors of *commission* (following incorrect automation output) and errors of *omission* (failing to act because not prompted). Both happen; commission tends to dominate when AB is the focus, omission when complacency is.
2. **Trust calibration is the dominant lever.** "Trust is possibly the strongest driving factor in over-reliance, when trust is incorrectly calibrated against system reliability." Users default toward trusting an automated aid over a human one (positivity bias toward automation).
3. **Reliability has a non-monotonic effect.** Highly-but-imperfectly reliable systems produce *more* AB than less reliable ones — at higher reliability the user stops monitoring; at lower reliability they stay alert. A cited study reports a threshold around 70% in its setting; this is not a general optimum for automated systems.

For human thinking with AI: AI-as-CDSS is the precise scenario this review describes. [Inference] Variable LLM reliability raises similar monitoring questions, but this review predates LLMs. The "negative consultation" failure mode — where AI flips a user's correct judgment to incorrect — is a measurable phenomenon, not a hypothetical.

## Key Passages

> "Automation bias (AB) — the tendency to over-rely on automation — has been studied in various academic fields… users tend to over-accept computer output 'as a heuristic replacement of vigilant information seeking and processing.'"
> — Goddard et al., [p.1] (abstract / background)

> "The risk ratio was 1.26 (95% CI 1.11 to 1.44); erroneous advice was more likely to be followed in the CDSS groups than in the control groups and when in error the CDSS increased the risk of an incorrect decision being made by 26%."
> — Goddard et al., [p.3]

> "Trust is possibly the strongest driving factor in over-reliance, when trust is incorrectly calibrated against system reliability… Dzindolet et al. demonstrated that users had a predisposition to trust, or had a 'positivity bias' toward, [an] automated aid over a human one and commit AB error."
> — Goddard et al., [p.4] (printed p.124; original has "a automated"; grammar substitution bracketed)

> "Automation complacency error rates for interruptive systems have been shown to increase if a DSS is highly (but not perfectly) reliable, leading to overtrust and complacency, and to decrease if it is less reliable… Madhavan and Wiegmann set the optimal threshold at 70% reliability before performance degrades."
> — Goddard et al., [p.4]

> "Negative consultations are the clearest measure of AB… The proportion of decisions which demonstrated this ranged from 6% to 11% of cases in prospective empirical studies."
> — Goddard et al., [p.3]

## Relevance

A pre-LLM review with three useful contributions:

- **Quantification.** AB is real and measurable: 26% higher risk of following bad advice; 6–11% rate of correct→incorrect flips. These numbers anchor what would otherwise be qualitative concerns.
- **Reliability and monitoring.** Some reviewed settings showed complacency with highly but imperfectly reliable aids. This does not establish that every reliability improvement increases bias.
- **Mitigator catalog.** The review discusses mitigators (training, user accountability, advice positioning, confidence-level signaling, info-vs-recommendation framing). Each maps to a KB-relevant counterpractice: [[calibration]] for trust calibration, [[think-first]] for accountability, and confidence-level signaling.

## Supports

- [[automation-bias]] — defining systematic-review evidence (Goddard treats this and "automation complacency" as overlapping concepts; both fall under this entry)
- [[calibration]] — trust mis-calibration is the dominant mediator
- [[capacity-erosion]] — under-monitoring raises a skill-maintenance question; long-term skill loss was not measured
- [[parasuraman-riley-automation-1997]] — Goddard cites Parasuraman as the conceptual predecessor
- [[hohenstein-crumple-zone-2020]] — extends the responsibility/attribution dimension Goddard's review only gestures at
- [[confidence-competence-gap]] — review documents conf↑ without performance↑ in less-experienced DSS users (Walsham et al.)

## Contradicts / Extends

- Extends [[parasuraman-riley-automation-1997]] — Parasuraman & Riley conceptually framed automation misuse/disuse; Goddard provides the systematic-evidence base for the misuse half of that distinction.
- Domain bridge: most pre-2012 AB research was aviation; Goddard demonstrates the same effect in healthcare CDSS, supporting the KB's assumption that AI-induced AB will generalize to professional judgment more broadly.

## Open Questions

- The review predates LLMs. Does the 26% RR hold for free-form natural-language outputs, where the "incorrect advice" isn't a discrete recommendation but embedded in a longer narrative?
- The reliability-paradox finding (~70% threshold) was for narrow CDSS. For LLMs whose effective reliability varies by query, what's the user-perceived reliability that drives complacency?
- Goddard's mitigators (training, accountability, advice positioning) have not been re-tested in the LLM era. Which still work?
