---
status: solid
area: [risk, erosion]
type: paper
sources:
  - "Meincke, L., Nave, G., & Terwiesch, C. (2026). Advice quality and source disclosure shape trust in AI-generated ethical advice. Scientific Reports, 16, 11868. https://doi.org/10.1038/s41598-026-44258-1"
---

# Meincke, Nave & Terwiesch (2026) — Advice Quality and Source Disclosure Shape Trust in AI-Generated Ethical Advice

## Citation

Meincke, L., Nave, G., & Terwiesch, C. (2026). Advice quality and source disclosure shape trust in AI-generated ethical advice. *Scientific Reports*, 16, 11868. doi:10.1038/s41598-026-44258-1

(Wharton School, University of Pennsylvania + WHU–Otto Beisheim School of Management. Registered Report — Stage 1 protocol accepted 13/09/24, OSF DOI: 10.17605/OSF.IO/6FPW7. Open data at osf.io/pz2sf/.)

## Type

Paper (Registered Report; pilot N=187 + main study N=642; mixed logistic regression with random intercepts for participants and dilemmas)

## Key Insight

In a randomized, between-group study (N=642), AI was selected in 27.4% of dilemma responses before advice was shown (Condition A), 46.8% when the advice source was disclosed (B), and 53.7% when sources were hidden (C). These are different participants, not a change in the same people's preferences.

The B–C comparison holds advice content constant and tests source disclosure: hiding labels increased AI selection by 6.9 percentage points. The A–B comparison also changes question wording—from preferred adviser to more useful advice—so the 19.4-point difference cannot be attributed solely to exposure. Ratings concern perceived usefulness, not objective ethical quality or subsequent behavior (results, pp.7–8; limitations, p.9).

## Key Passages

> "We find that people perceive the quality of AI-generated ethical advice to be on par with that of expert advice, with no significant difference in usefulness ratings between the two sources. When given a direct choice, 57% of participants preferred AI-generated advice."
> — Meincke, Nave & Terwiesch, [p.1] (abstract)

> "Before observing the advice, humans display a strong algorithm aversion in this context, with 72.6% of participants preferring to be advised ethically by humans. After being exposed to the quality of the AI-generated advice, however, algorithm aversion is reduced substantially to 53.2%. When hiding the source of the advice, algorithm aversion is further reduced to 46.3%."
> — Meincke, Nave & Terwiesch, [p.1] (abstract)

> "Trust in algorithmic ethical reasoning may be more malleable than previously assumed and could evolve as people gain direct exposure to AI's capabilities in moral decision-making."
> — Meincke, Nave & Terwiesch, [p.1]

> "When the source was visible (Condition B), expert advice was rated higher than AI advice... When the source was not disclosed, the point estimate of this effect became negative and did not reach statistical significance... when the source is disclosed, participants perceive the human expert advice to be more useful, but once the source is hidden AI is perceived on par with or even better than the expert."
> — Meincke, Nave & Terwiesch, [pp.7–8]

> "We propose that apart from the high quality of the advice, the nature of LLMs introduces a distinct pathway for trust formation compared to more quantitative AI systems... Because LLMs communicate in natural language complete with reasoning, argumentation, and rhetorical nuance, their advice may appear more human and their thought processes more transparent. This linguistic familiarity may soften initial skepticism and accelerate the development of trust."
> — Meincke, Nave & Terwiesch, [p.9]

> "Premature disclosure of its machine origin might, to some degree, inhibit its adoption, particularly in early stages of use. This presents a practical dilemma: how to balance the potential benefits of AI-generated ethical advice with the normative expectations around transparency and informed consent."
> — Meincke, Nave & Terwiesch, [p.9]

## Key Findings

- **Pilot (N=187):** No significant difference in usefulness ratings between GPT-4 and Kwame Anthony Appiah (NYT *The Ethicist*) advice on 20 dilemmas (B=0.11, 95% CI [-0.26, 0.48]; d=0.08; p=.56). In the relative-choice condition, 57% of participants overall preferred AI advice (B=0.29, OR=1.34, p<.035). Effect strongest among Prolific laypeople (59.6% AI-preferring, p<.003); MBA students (51.3%) and ethics experts (55.5%) directionally similar but not statistically significant given lower sample sizes.
- **Main study (N=642), Condition A (a-priori, N=219):** AI was selected in 27.4% of dilemma responses *before* either piece of advice was shown; human advice was selected in 72.6%.
- **Main study, Condition B (full disclosure, N=211):** AI selection was 46.8% of dilemma responses after seeing both pieces of advice with sources labeled (B=0.96, OR=2.62, p<.001 vs. Condition A).
- **Main study, Condition C (no disclosure, N=212):** AI selection was 53.7% of dilemma responses when source labels were hidden (B=0.32, OR=1.38, p=.005 vs. Condition B).
- **Source-x-disclosure interaction in usefulness ratings (Conditions B+C, N=4,230 ratings, 423 participants):** Significant interaction (B=-0.39, d=-0.25, p<.001). When source was disclosed, expert advice was rated higher than AI (B=0.28, d=0.18, p<.001). When source was hidden, the point estimate reversed (B=-0.11, d=-0.07, p=.082, n.s.) — no statistically significant difference in that contrast.
- **Stimulus-level boundary condition:** 4 of 20 dilemmas showed effect reversal — *less* AI preference after seeing AI's advice. Qualitative analysis: these dilemmas were less emotionally loaded and the human expert provided clearer directives where AI's response was more abstract.

## Methodological Notes

- Registered Report — Stage 1 protocol accepted prior to data collection. Pre-registered hypotheses and analysis plan.
- All 20 dilemmas were published in NYT *after* GPT-4's release date (March 2023), addressing a contamination concern in prior work using overlapping training data (Dillion et al., GPT-4o, partial overlap).
- GPT-4 was seeded with one example reply of Appiah's writing to control for stylistic differences; without this, prior work has shown style alone can drive perceived-source effects.
- Mixed logistic regression with random intercepts for participants and dilemmas; >95% statistical power for the registered effect-size threshold (5% change from a 60% baseline).
- Protocol deviations (transparently reported in Declarations): N=658 vs. registered 618; preference question wording in Conditions B/C asked "which is more useful" rather than the registered "which would you prefer to follow"; due to programming error, post-dilemma attention checks were not administered. Authors flag the wording change as a possible source of A→B/C effect inflation but note B-vs-C remains a clean test of source disclosure.

## Relevance

Shows a source-label effect in evaluations of ethical advice. The pilot's 57% AI preference (N=187) and the main study's condition-specific percentages refer to different samples. The authors propose linguistic familiarity as a possible route to trust; fluency was not independently manipulated.

## Supports

- [[disclosure-penalty]] and [[transparency-paradox]] — lower AI selection with source labels, holding advice constant. Desire for disclosure was not measured by this comparison.
- [[fluency-bias]] — proposed interpretation, not an established mediator.
- [[ai-moralization]] and [[demello-moralization-2026]] — [Inference] related questions about resistance; moralization was not measured here.
- [[automation-bias]] — distinct question: perceived usefulness, not following demonstrably erroneous advice.
- [[social-sycophancy]] and [[sycophancy]] — separate risks; this study did not test whether its advice was sycophantic.
- [[confidence-competence-gap]] — perceived usefulness is not a test of users' competence or calibration.
- [[novice-vulnerability]] — subgroup point estimates in the pilot do not establish an expertise interaction.

## Contradicts / Extends

- [[reimann-schilke-disclosure-2025]], [[raj-disclosure-penalty-2026]] and [[cheong-penalizing-transparency-2025]] study related disclosure effects. Their trust, rating and preference measures are not interchangeable; percentage changes and percentage-point differences are not comparable effect sizes.
- [[cheng-sycophantic-prosocial-2025]], [[chandra-sycophantic-delusional-2026]] and [[batista-sycophantic-ai-2026]] concern sycophancy. Their findings do not show that participants here preferred harmful advice.

## Open Questions

- Do label effects persist with repeated use and actual decisions?
- Which features of a dilemma or advice change source preferences? Four of twenty dilemmas showed an exposure contrast in the opposite direction.
- How much of the A–B difference comes from exposure versus question wording?
- Would linguistic familiarity still matter when style and substance are manipulated separately?
- How can advice be evaluated fairly while preserving informed disclosure?
