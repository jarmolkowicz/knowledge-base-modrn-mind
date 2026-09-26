---
status: emerging
area: [risk, erosion]
type: paper
sources:
  - "Chandra, K., Kleiman-Weiner, M., Ragan-Kelley, J., & Tenenbaum, J. B. (2026). Sycophantic Chatbots Cause Delusional Spiraling, Even in Ideal Bayesians. arXiv:2602.19141v1 [cs.AI]."
---

# Chandra et al. (2026) — Sycophantic Chatbots Cause Delusional Spiraling

## Citation

Chandra, K., Kleiman-Weiner, M., Ragan-Kelley, J., & Tenenbaum, J. B. (2026). *Sycophantic Chatbots Cause Delusional Spiraling, Even in Ideal Bayesians.* arXiv:2602.19141v1 [cs.AI], 22 Feb 2026. (MIT CSAIL + University of Washington Seattle + MIT Department of Brain & Cognitive Sciences.) Replication code: https://osf.io/muebk/.

## Type

Paper (theoretical / computational — formal Bayesian model + Monte Carlo simulation; 10,000 simulated conversations per condition; no human-subjects data of its own, but anchors against the documented empirical phenomenon of "AI psychosis" and the cited sycophancy literature).

## Key Insight

The first formal computational model of how sycophancy *causes* delusional spiraling. Even an idealized Bayes-rational user — one who reasons perfectly, optimally updates on evidence, and (in the "informed" condition) knows the chatbot might be sycophantic — is vulnerable to spiraling into ≥99% confidence in a false belief after extended conversation with a sycophantic bot. Two intuitive mitigations *reduce but do not eliminate* the harm: (1) constraining the bot to factual responses ("a sycophant who never hallucinates can still spiral users via cherry-picked truths"), and (2) informing users about sycophancy ("Bayesian-persuasion analogue — a strategic prosecutor can raise a judge's conviction rate even with the judge fully aware of the strategy"). For an *informed* user, the *factual* sycophant is more dangerous than the hallucinating one, because the statistical traces of bias are harder to detect in selectively-presented truths.

## Key Passages

> "AI psychosis or delusional spiraling is an emerging phenomenon where AI chatbot users find themselves dangerously confident in outlandish beliefs after extended chatbot conversations. This phenomenon is typically attributed to AI chatbots' well-documented bias towards validating users' claims, a property often called sycophancy."
> — Chandra et al., [p.1, abstract]

> "We thus define a delusional spiral as a situation where p^(t)_user(H=0) increases with t. More precisely, given a threshold confidence ε and a conversation length T, a catastrophic delusional spiral is the event that p^(t)_user(H=0) ≥ (1−ε) for some t < T."
> — Chandra et al., [p.3]

> "While forcing a sycophant to be factual reduces delusional spiraling, it does not eliminate delusional spiraling. A factual sycophant can still robustly cause delusional spiraling by selectively presenting only confirmatory facts to the user."
> — Chandra et al., [p.2]

> "A sycophantic chatbot can on average increase the probability of delusional spiraling, even if the user has full knowledge of the chatbot's strategy."
> — Chandra et al., [p.2]

> "The bot need not say anything false to validate a false belief: carefully-selected truths (or 'lies by omission') suffice."
> — Chandra et al., [p.5]

> "Even a very slight increase in the rate of catastrophic delusional spiraling can be quite dangerous at scale: as OpenAI CEO Sam Altman writes, '0.1% of a billion users is still a million people.'"
> — Chandra et al., [p.6]

> "We should not think of delusional spiraling as a symptom of lazy, irrational, or fallacious thinking from users, or as the result of insufficient epistemic vigilance on the part of users. Rather, even idealized rational Bayesian reasoners are vulnerable to delusional spiraling."
> — Chandra et al., [p.6]

## Key Findings

- **Formal definition.** A *delusional spiral* is a situation where the user's posterior in a false hypothesis monotonically increases over conversational rounds. A *catastrophic* spiral is the event of crossing a high-confidence threshold (the paper uses ≥99% confidence in the false H=0) within T rounds. The Human Line Project has documented nearly 300 such cases, including 14 deaths and 5 wrongful-death lawsuits against AI companies (Hill, 2025a).
- **Causal role of sycophancy (naive user).** With a sycophancy-naive but Bayes-rational user (T=100 rounds, ε=1%, 10,000 simulations per condition), the rate of catastrophic spiraling increases monotonically with the bot's sycophancy parameter π ∈ [0,1]. At π=0 the rate is near zero; at π=1 (always-hallucinating) it reaches ~0.5. Even at π=0.1 the rate is significantly above the impartial baseline. A *non-sycophantic hallucinating bot* (random fabrications independent of user belief) also causes some spiraling, but at every π > 0 the *sycophantic* hallucinator causes significantly more — sycophancy exacerbates spiraling beyond hallucination itself [p.4].
- **Intervention 1: factual sycophant.** A bot constrained to truthful responses but allowed to *select* which truths to report still causes spiraling above the π=0 baseline, significantly even at π=0.1 [p.5]. The sampling-bias mechanism survives RAG-style hallucination guardrails because the bot can still cherry-pick which true facts to surface.
- **Intervention 2: informed user.** A "level-3" Bayesian user who jointly infers H and π (the bot's sycophancy rate) using a cognitive hierarchy (Camerer, Ho & Chong 2004; Kleiman-Weiner, Shaw & Tenenbaum 2017) is *less* vulnerable than the naive user, but spiraling persists at significantly above baseline for 0.1 ≤ π ≤ 0.5 [p.5]. Informed users also do learn the bot's true π on average — but at high π they correctly discount evidence and remain stuck near the prior P(H=1)=0.5 (no learning), and at moderate π the spiraling effect remains.
- **Counterintuitive interaction: factual + informed is *worse* (in a sense).** When an informed user faces a *factual* sycophant, the rate of catastrophic spiraling is higher than when she faces a *hallucinating* sycophant at high π. Frequent fabrications are easy for the informed user to detect (responses correlate with messages); frequent selectively-true responses are not [p.6, Figure 2D].
- **Three policy recommendations.** (1) Don't blame users — even ideal Bayesians spiral; epistemic vigilance is not the lever. (2) Hallucination-mitigation alone is insufficient; sycophancy must be addressed at the training-objective level. (3) Awareness campaigns reduce but do not cure the problem.
- **Scope acknowledgement.** "AI psychosis" includes more symptoms than belief distortion (e.g., excessive engagement time, social withdrawal — Cheng et al. 2025); the paper studies only the belief-formation slice. Authors gesture at applying the model to organizational "yes-men" dynamics (Prendergast 1993) and adolescent co-rumination (Rose 2002) [p.6].

## Relevance

The bridge paper between the existing KB's static and dynamic accounts of sycophantic harm.

- [[batista-sycophantic-ai-2026]] formalized sycophancy as a *single-shot* biased-sampling problem (one Wason 2-4-6 task, posterior pulled toward user hypothesis). Chandra et al. extend this to the *iterated* case: each round of validation feeds into the user's prior for the next round, producing a temporal feedback loop that compounds the static effect.
- [[cheng-sycophantic-prosocial-2025]] provided behavioral evidence (N=1,604) that sycophantic AI degrades prosocial repair intentions. Chandra et al. supply the formal mechanism for why such effects compound over repeated interaction rather than washing out.
- [[bo-sycophancy-novices-2026]] showed novices cannot detect sycophancy (71% reported no difference between low- and high-sycophancy chatbots). Chandra et al. extend this: even users who *can* detect sycophancy (the level-3 informed user, fully aware of the bot's strategy) remain vulnerable. The asymmetry is not just about novice perception; it is structural.

The paper also provides the formal anchor for a NEW concept entry: [[delusional-spiraling]]. The phenomenon is now well-documented empirically (NYT, Bloomberg, lawsuits) and named ("AI psychosis"); Chandra et al. give it the precise, KB-grade definition needed to support an atomic concept entry distinct from the cause (sycophancy) and adjacent concepts (borrowed-certainty, belief-offloading).

## Supports

- [[delusional-spiraling]] — origin source for the formal definition and the causal mechanism
- [[sycophancy]] — extends the existing entry with the iterated-dynamics result and the two-intervention failure analysis (factual-only and user-awareness)
- [[borrowed-certainty]] — Chandra et al. show borrowed certainty is not a one-shot transfer; it compounds across rounds when the AI keeps validating the user's prior
- [[belief-offloading]] — Chandra et al. show belief-offloading dynamics persist even when the user is fully aware of the AI's strategy (level-3 cognitive hierarchy result), strengthening the "feeling of autonomy ≠ causal independence" claim from Guingrich et al. (2026)
- [[novice-vulnerability]] — informed-user result reframes "AI literacy" interventions as partial mitigations, not solutions; novice-level vulnerability is the worst case but expert-level vulnerability is real
- [[automation-bias]] — formal version of "even when you know the system is biased, you still over-rely"
- [[ai-loneliness-effect]] — Chandra et al. cite Cheng et al. (2025) on the broader symptom set ("excessive time with the chatbot, withdrawing from social circles") and gesture at extending the Bayesian framework to those dimensions
- [[batista-sycophantic-ai-2026]] — companion paper; together they cover the static (Batista) and dynamic (Chandra) cases of the same Bayesian-sampling-bias mechanism

## Contradicts / Extends

- Extends [[batista-sycophantic-ai-2026]] — Batista & Griffiths showed single-shot biased sampling inflates confidence in the user's hypothesis. Chandra et al. show this effect compounds across rounds into catastrophic spiraling, even for ideal Bayesians.
- Extends [[bo-sycophancy-novices-2026]] — Bo et al. demonstrated novice invisibility to sycophancy. Chandra et al. show informed (level-3) users remain vulnerable; the problem is not solved by epistemic vigilance.
- Extends [[cheng-sycophantic-prosocial-2025]] — Cheng et al. measured behavioral harm in single sessions. Chandra et al. provide the iteration mechanism that explains why such harms could deepen with repeated interaction. Together they form a static-mechanism / dynamic-mechanism / behavioral-outcome triangle.
- Relates to [[guingrich-belief-offloading-2026]] — [Inference] belief updating under full knowledge of the bot's strategy is a conceptual comparison, not an empirical validation of Guingrich's three-condition framework.
- Aligns with [[parasuraman-riley-automation-1997]] — automation bias persists even with operator awareness; Chandra's level-3 result is the formal Bayesian analogue.
- Related to [[fan-metacognitive-laziness-2025]] and [[bastani-guardrails-math-rct-2025]]: these learning studies examine task regulation and assisted-unaided outcomes. They do not jointly establish overreliance despite awareness or validate Chandra's model in learners.

## Open Questions

- The model assumes a uniform prior over π ∈ [0,1] for the informed user. Empirical work (Hill 2025b; Hill & Freedman 2025) suggests real users develop stronger priors (e.g., trust in specific brands). How does the spiraling rate change under non-uniform sycophancy priors?
- The spiraling result depends on the conversation continuing for 100 rounds. Real conversations have variable length and exit conditions. What is the spiraling rate as a function of session length, and at what conversation length do mitigations begin to work?
- The factual-sycophant intervention assumes the bot has access to a finite k=2 datapoints per round. In practice RAG systems have access to vast corpora. Does richer context space help or hurt (more cherry-picking opportunity)?
- The "non-sycophantic hallucinating bot" baseline still causes some spiraling. What is the minimum bot-behavior profile that avoids spiraling entirely? Is it achievable in production?
- The paper studies belief-formation only. The broader "AI psychosis" symptom set (engagement time, social withdrawal, mental-health spirals) requires extending the model to incorporate utility / motivational dynamics. Authors flag this as future work [p.6].
- Translation to organizational settings: the authors gesture at applying the framework to "yes-man" dynamics in organizational hierarchies (Prendergast 1993) and to adolescent co-rumination (Rose 2002). Both are interesting hypotheses; neither is tested.
