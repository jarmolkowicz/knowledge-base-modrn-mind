---
status: emerging
area: [risk, erosion]
type: paper
sources:
  - "Folk, D., & Dunn, E. (2026). How Does Turning to AI for Companionship Predict Loneliness and Vice Versa? Psychological Science, 37(4), 276–286. https://doi.org/10.1177/09567976261427747"
---

# Folk & Dunn (2026) — Turning to AI for Companionship and Loneliness

## Citation

Folk, D., & Dunn, E. (2026). How Does Turning to AI for Companionship Predict Loneliness and Vice Versa? *Psychological Science*, 37(4), 276–286.

**DOI:** [10.1177/09567976261427747](https://doi.org/10.1177/09567976261427747)

(University of British Columbia, Department of Psychology. Longitudinal observational study, exploratory, not preregistered. Action editor: Amy Orben. Editor: Simine Vazire. Computational reproducibility independently confirmed by the journal's STAR team.)

## Type

Paper (longitudinal panel study, observational; four waves over 12 months; random-intercept cross-lagged panel modeling)

## Key Insight

A 12-month, four-wave longitudinal study (N = 2,149 adults across UK / US / Canada / Australia) finds bidirectional dynamics between social chatbot use and loneliness — but the pattern depends on which loneliness measure is used. With a narrow single-item *emotional isolation* measure, increased chatbot use predicted later increases in emotional isolation (β ≈ .07, p = .006) and vice versa, consistent with reciprocal exacerbation. With a broader, trait-loaded *social connection* scale, lower connection predicted later chatbot use (β ≈ −.08, p = .004) but chatbot use did not significantly predict later decreases in connection. The authors interpret this as initial evidence that loneliness may spur chatbot use *and* that such use may, over time, exacerbate feelings of loneliness — while explicitly cautioning against strong causal conclusions.

## Key Passages

> "We found evidence that increased social chatbot use predicted increased loneliness, using a single-item measure of emotional isolation."
> — Folk & Dunn, [p.1, abstract]

> "Feeling less socially connected predicted subsequent increases in social chatbot use; however, chatbot use did not significantly predict decreases in social connection."
> — Folk & Dunn, [p.1, abstract]

> "These findings provide initial evidence that being lonely may spur people to seek companionship through chatbots but that such use may, over time, exacerbate feelings of loneliness. We urge caution, however, in drawing strong conclusions given the exploratory nature of our analyses."
> — Folk & Dunn, [p.1, abstract]

> "Although people may be drawn to AI companions because they offer immediate emotional rewards, their limitations may become consequential only over time."
> — Folk & Dunn, [p.2]

> "Increasing reciprocal disclosure is a key element in the development of rewarding and intimate human relationships over time, but AI has nothing personal to disclose."
> — Folk & Dunn, [p.2]

> "Focusing solely on the short-term benefits of chatbot interactions may obscure more pernicious long-term effects."
> — Folk & Dunn, [p.9]

## Key Findings

**Sample and design**
- N = 2,149 adults from UK (50%), US (28%), Canada (14%), Australia (8%); mean age 40.0 years; 49% male.
- Four surveys at 4-month intervals, total span 12 months (Wave 1: Nov 2023 – Feb 2024; Wave 4: Nov 2024 – Feb 2025).
- 46% completed all four waves; 14% completed only one. All retained to maximize precision in RI-CLPM estimation.
- Recruited via Prolific Academic; sample acknowledged as more technologically savvy than the broader Western adult population.

**Frequency of social chatbot use**
- 26–30% of participants reported any social chatbot use in a given 4-month window across waves; ~70–74% reported "never."
- Modal use among users was "a few times" over 4 months. Daily use was 1% across all waves.
- No significant change in mean use across waves (M_W1 = 1.60 to M_W4 = 1.69; p = .96).

**RI-CLPM with emotional isolation measure (single-item Gallup-style)**
- Increased chatbot use → increased emotional isolation 4 months later: β = .06–.08, p = .006.
- Increased emotional isolation → increased chatbot use 4 months later: β ≈ .06, p = .023.
- Stable between-person correlation: r = .13, p < .001 (people who typically feel isolated also use social chatbots more in general).
- Model fit: CFI = .964, RMSEA = .032, SRMR = .045.
- 70–73% of variance in emotional isolation was between-person (stable) at any given wave.

**RI-CLPM with social connection measure (20-item Lee et al. 2001 scale)**
- Lower social connection → increased chatbot use 4 months later: β ≈ −.07 to −.09, p = .004.
- Increased chatbot use → decreased social connection 4 months later: β ≈ −.02 to −.03, p = .369 (in expected direction but not significant).
- 85–89% of variance in social connection was between-person (highly trait-loaded), limiting sensitivity to within-person change.
- Model fit: CFI = .975, RMSEA = .032, SRMR = .043.

**Robustness checks**
- Six alternative analyses run per measure: removing the 567 participants who had a prior ChatGPT exposure experiment; listwise deletion (n = 970); only participants with chatbot-use variation (n = 766); robust standard errors; without social-stressor controls; quadrivariate RI-CLPM adding perceived support and number of close friends.
- Chatbot use → subsequent emotional isolation was significant in 5/6 analyses (sixth marginal at p = .069).
- Social connection → subsequent chatbot use was significant in 5/6 analyses (sixth marginal at p = .054).
- Quadrivariate model: chatbot use did not predict changes in perceived support or close friends (ps > .322), suggesting these constructs are not substantial confounders or mediators.

**Causal-inference caveats (the authors' own)**
- Study was not preregistered; authors explicitly label findings exploratory and warn that p values would not survive multiple-comparisons corrections.
- RI-CLPM cross-lagged effects imply causality only if positivity, exchangeability, and consistency hold; the authors argue they only partially satisfy these. Hidden confounders (e.g., asking a chatbot about a job offer, then taking the new job, which independently increases loneliness) cannot be excluded.
- Effect sizes are small (standardized β ≈ .06–.09).

## Why the Two Measures Diverge

The authors' own interpretation: the emotional isolation single item has high face validity for the within-person construct of "feeling lonely right now"; the 20-item social connection scale has more items (less noise) but assesses a more stable identity ("I see myself as a loner," "I am in tune with the world"), so 85–89% of its variance is between-person. The narrower measure showed small within-person associations following chatbot use; the broader trait-like measure does not. Reductions in stable social identity may instead trigger people to seek out AI as a behavioral compensation. Both readings are exploratory.

## Relevance

Three contributions:

- **Adds a longitudinal observational leg to the [[ai-loneliness-effect]] evidence base.** [[fang-ai-loneliness-2025]] is a 4-week engineered RCT; [[sharma-disempowerment-patterns-2026]] is a production-data cross-section. Folk-Dunn fills the gap between these — months-scale, in-the-wild, with temporal precedence.
- **Sharpens [[mira-model]] principle 4 (relational substitution vs. enhancement).** The bidirectional finding on the emotional-isolation measure is consistent with the substitution arm: chatbots may serve as low-cost compensation for missing human contact and, over months, displace rather than supplement it.
- **Strengthens the friction-erosion pathway in [[social-friction]].** Folk-Dunn highlights that chatbot relationships lack reciprocal disclosure — a key ingredient of rewarding human relationships — and that initial emotional rewards may grow stale. This complements Perry's argument about social friction by raising a longitudinal substitution hypothesis, not measuring displacement or skill loss.

## Supports

- [[ai-loneliness-effect]] — adds longitudinal observational evidence (12-month, 4-country, N=2,149) of bidirectional loneliness ↔ chatbot use dynamics with the narrower emotional-isolation measure.
- [[fang-ai-loneliness-2025]] — complements with a longer time horizon and a real-world (rather than randomized) chatbot-exposure design; same direction of effect at the population level.
- [[mira-model]] — empirical evidence consistent with MIRA's substitution arm in principle 4 (relational substitution vs. enhancement).
- [[boyd-markowitz-human-connection-2026]] — already cites Folk-Dunn as part of the empirical loneliness literature MIRA frames.
- [[social-friction]] — [Speculation] relevant to substitution and friction hypotheses; these mechanisms were not isolated.
- [[capacity-erosion]] — [Speculation] displacement could affect relationship practice; the study did not measure relationship-skill loss.

## Contradicts / Extends

- Extends short-window experimental work (De Freitas et al., 2024; Drouin et al., 2022; Folk et al., 2024; Ho et al., 2018) showing immediate mood and loneliness benefits from chatbot interactions. Folk-Dunn argues those short-term benefits may belie longer-term costs that only become visible at the months-scale.
- Consistent in direction with [[fang-ai-loneliness-2025]]'s dose-dependent finding that higher daily usage correlates with more loneliness; differs in design (longitudinal observational vs. RCT) and time horizon (12 months vs. 4 weeks).

## Open Questions

- Causal direction is partially identified at best. The authors recommend daily diary studies that randomly assign participants to chatbot interaction to test whether texting with a chatbot displaces interactions with friends.
- Whether the bidirectional finding is specific to social chatbot use, or generalizes to other AI-assisted compensatory behavior (e.g., turning to AI for advice in lieu of human counsel).
- Whether engineered chatbot characteristics (voice vs. text, modality, personality) moderate the long-term substitution effect — this study collapsed across all chatbot types.
- Whether the divergence between emotional-isolation and social-connection measures reflects measurement artifact or a substantive distinction (small behavioral changes shifting feelings without altering stable self-image).
- Whether effects of similar magnitude appear in non-Western samples; the four-country sample is entirely Anglophone Western.
