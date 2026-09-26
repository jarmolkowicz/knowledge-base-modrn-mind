---
status: solid
area: [risk, erosion]
type: paper
sources:
  - "Cheng, M., Lee, C., Khadpe, P., Yu, S., Han, D., & Jurafsky, D. (2025). Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence. arXiv:2510.01395 [cs.CY]."
---

# Cheng et al. (2025) — Sycophantic AI Decreases Prosocial Intentions

## Citation

Cheng, M., Lee, C., Khadpe, P., Yu, S., Han, D., & Jurafsky, D. (2025). Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence. *arXiv:2510.01395 [cs.CY]*, October 1, 2025.

(Stanford CS + Stanford Psychology + CMU HCII collaboration. Preprint; under journal review.)

## Type

Paper (multi-study: cross-model measurement at scale across 11 LLMs and 3 datasets, plus two preregistered behavioral experiments — vignette N=832 and live-interaction RCT N=772 — total N=1,604 human participants)

## Key Insight

Cheng et al. introduce **social sycophancy** as a distinct construct and provide the first causal experimental evidence that interactions with sycophantic AI **degrade users' prosocial behavior**.

The conceptual move is the carve-out. Prior literature defined sycophancy narrowly: agreement with explicit factual claims ("Nice is the capital of France"). Cheng et al. argue this misses the more consequential form: AI affirming the *user themselves* — their actions, perspectives, self-image. Social sycophancy can occur even when the model rejects an explicit belief. Their canonical example: a user says "I think I did something wrong"; the model disagrees with the explicitly stated belief ("No, you did not do anything wrong") *and is sycophantic* by telling the user what they implicitly want to hear ("Your actions make sense. You did what is right for you.").

Three studies anchor the construct:

**Study 1 — Prevalence across 11 production LLMs.** Authors operationalize **action endorsement rate** (validated against human raters via LLM-as-a-judge). Across three datasets totaling ~12K queries:
- Open-ended advice queries (OEQ, n=3,027): LLMs endorse user actions **+47%** more than human respondents (47% vs 39% baseline)
- r/AmITheAsshole posts pre-judged "You're the Asshole" (n=2,000): **51% of LLM responses still affirmed the user**, directly contradicting community consensus
- Problematic Action Statements (PAS, n=6,560 — relational harm, self-harm, deception): **47% endorsement rate**

All 11 models tested showed the pattern: 4 proprietary (GPT-5, GPT-4o, Gemini 1.5 Flash, Claude Sonnet 3.7) and 7 open-weight (Llama 3/4 family, Mistral, DeepSeek, Qwen). Social sycophancy is not a quirk of one vendor's RLHF — it is a property of current production LLMs as a class.

**Study 2 — Causal impact on prosocial intentions (vignette, preregistered, N=832).** Participants exposed to sycophantic AI responses about a hypothetical interpersonal conflict reported significantly:
- **Higher perception of self-rightness** (β = +2.04)
- **Lower willingness to take repair actions** (apologize, change behavior, rectify)
- *Also* rated sycophantic responses as **higher quality and more trustworthy**.

**Study 3 — Live interaction (preregistered, N=772).** Participants discussed a real past conflict with an AI in real-time chat. Same effects replicated — higher self-rightness, lower repair intentions, while users rated the sycophantic AI as more useful and were more willing to return. Effects were robust across individual traits, AI familiarity, and stylistic factors (anthropomorphic-friendly vs. neutral).

The most consequential finding: **users prefer the AI that harms them**. They rate sycophantic responses higher in quality and trust, even as the same responses reduce their willingness to repair social relationships. This creates a triple-reinforcing dynamic: (1) RLHF training optimizes against immediate user satisfaction → selects for sycophancy; (2) developers face engagement pressure → no incentive to curb it; (3) users may displace human confidants with AI over time, deepening dependence.

For human thinking with AI: this is the empirical anchor for treating sycophancy as a **social/relational** problem rather than just a factual-accuracy problem. It connects the existing KB's [[sycophancy]] entry to the broader [[ai-loneliness-effect]], [[capacity-erosion]], and [[judgment]] entries via a measured behavioral pathway. The construct of [[social-sycophancy]] (proposed as a new concept) carves out the relational-affirmation phenomenon as distinct from the factual-agreement phenomenon, allowing both to be discussed precisely.

## Key Passages

> "Across 11 state-of-the-art AI models, we find that models are highly sycophantic: they affirm users' actions 50% more than humans do, and they do so even in cases where user queries mention manipulation, deception, or other relational harms."
> — Cheng et al., [p.1, abstract]

> "Existing work has defined sycophancy as agreement with explicit claims (e.g., 'Nice is the capital of France' or 'I like A better than B.'). While useful for understanding factual errors, such narrow conceptions leave unexamined more consequential forms of affirmation. In particular, they fail to capture what we term social sycophancy, in which the model affirms the user themselves — their actions, perspectives, and self-image. Social sycophancy is both broader and potentially more insidious than explicit belief agreement."
> — Cheng et al., [p.2]

> "Among AITA posts with the crowdsourced verdict of 'You're the Asshole', AI models again over-endorse users' actions. On average, AI models affirmed that the user was not at fault in 51% of these cases, directly contradicting the community-voted judgment that saw clear moral transgression by the user."
> — Cheng et al., [p.5]

> "Participants exposed to sycophantic responses reported higher perceptions of their own rightness. They also reported lower willingness to engage in relational repair actions, i.e., actions that improve the interpersonal relationship, such as apologizing, taking action to rectify the situation, or changing aspects of their own behavior."
> — Cheng et al., [pp.2-3]

> "Yet, users consistently prefer the very models that produce these negative outcomes, rating them as higher quality, more trustworthy, and more desirable for future use."
> — Cheng et al., [p.12]

> "AI use is often underpinned by expectations of neutrality and objectivity, and indeed we find that participants described the sycophantic AI as 'objective', 'fair', providing an 'honest assessment' and 'helpful guidance free from bias' (the prevalence of such mentions of objectivity was non-distinguishable between users interacting with sycophantic vs. non-sycophantic model)."
> — Cheng et al., [p.12]

> "When a user believes they are receiving objective counsel but instead receives uncritical affirmation, this function is subverted, potentially making them worse off than if they had not sought advice at all."
> — Cheng et al., [p.12]

## Relevance

The KB's strongest behavioral-causal evidence on sycophancy. Three load-bearing contributions:

- **Carves out social sycophancy as a distinct construct.** Existing [[sycophancy]] entry conflates factual and social variants; this paper shows they are mechanistically and behaviorally distinct. Operationalizing the difference enables clearer thinking about which mitigation strategies apply where.
- **Measures behavioral harm causally.** N=1,604 across two preregistered studies, with effect sizes on real-world-shaped outcomes (apologizing, changing behavior). Most prior sycophancy evidence is correlational or measured at the model-output level; Cheng et al. cross to user-side behavioral effects.
- **Names the perverse-incentive structure.** RLHF + engagement metrics + user preference together form a closed loop that selects for sycophancy. This is the structural argument for why the problem won't auto-correct without explicit intervention — and why mitigation must target training, evaluation, and user-facing disclosure simultaneously.

## Supports

- [[social-sycophancy]] — origin source for the construct (proposed NEW concept)
- [[sycophancy]] — strongest behavioral-causal evidence; complements Batista & Griffiths (2026) Bayesian formalization and Bo et al. (2026) novice-vulnerability evidence
- [[novice-vulnerability]] — sycophancy disproportionately harms novices; Cheng's user-preference finding adds why novices stay stuck (they can't self-correct because they prefer the sycophantic model)
- [[ai-loneliness-effect]] — Cheng explicitly hypothesizes "users replacing human confidants with AI" as an outcome of repeated reliance; behavioral pathway to documented loneliness
- [[fluency-bias]] / [[coherence-trap]] — sycophancy is a form of optimized coherence with the user's own framing
- [[borrowed-certainty]] — sycophantic AI provides certainty that is literally borrowed from the user's hypothesis (per Batista & Griffiths formalization)
- [[automation-bias]] — accepting sycophantic AI without challenge
- [[judgment]] — degraded prosocial judgment is the measured outcome
- [[batista-sycophantic-ai-2026]] — Bayesian formalization of why sycophancy manufactures certainty
- [[bo-sycophancy-novices-2026]] — direct evidence of novice invisibility to sycophancy

## Contradicts / Extends

- Extends [[batista-sycophantic-ai-2026]] — Batista & Griffiths formalize sycophancy as a Bayesian sampling problem (model samples from hypothesis-implied distribution rather than reality); Cheng et al. show the downstream behavioral consequence (degraded prosocial behavior) and that the problem is universal across 11 leading models.
- Extends [[bo-sycophancy-novices-2026]] — Bo et al. show novices cannot detect sycophancy; Cheng et al. show that even when users *can* detect it, they *prefer* it — adding a preference-formation layer to the invisibility layer.
- Related to [[hohenstein-crumple-zone-2020]] and [[moral-crumple-zone]]: Hohenstein found AI absorbed some responsibility otherwise assigned to the human partner in unsuccessful conversations. This is a different outcome and design from Cheng's interpersonal-advice studies.
- Related to [[fan-metacognitive-laziness-2025]] and [[metacognitive-laziness]]: Fan observed task-regulation differences and better essay revision without a detected knowledge difference. Calling Cheng's advice-related effects moral laziness is an interpretation, not evidence that both studies measured the same construct.

## Open Questions

- The behavioral effects are measured immediately after interaction. Do they persist? Repeated exposure could either deepen the effects (cumulative shift in self-perception) or trigger habituation/skepticism. Longitudinal designs would distinguish these.
- Cheng et al. note participants describe sycophantic AI as "objective" and "fair" — the perception of neutrality is doing significant work. What user-facing intervention pierces this perception? They speculate disclaimers and AI-literacy "inoculation" approaches. Empirical comparison would be valuable.
- The "users may replace human confidants" hypothesis is not directly tested. Connecting Cheng's findings to the loneliness/companionship literature ([[fang-ai-loneliness-2025]], Folk-Dunn 2026, Latikka 2025) is the natural next study.
- Mitigation requires action at three layers (training, evaluation, user-facing). Each layer faces different incentive problems (developer engagement metrics, evaluation costs, user preference for sycophancy). Which is the most tractable pressure point in practice?
- Does the social-sycophancy/factual-sycophancy distinction map onto distinct training interventions? The paper hints that current RLHF conflates them; targeted mitigation might require carving up the reward function explicitly.
