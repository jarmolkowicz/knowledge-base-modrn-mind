---
status: solid
area: [risk, erosion, preservation]
type: paper
sources:
  - "Sharma, M., McCain, M., Douglas, R., & Duvenaud, D. (2026). Who's in Charge? Disempowerment Patterns in Real-World LLM Usage. arXiv:2601.19062 [cs.CY], January 27, 2026."
---

# Sharma et al. (2026) — Who's in Charge? Disempowerment Patterns in Real-World LLM Usage

## Citation

Sharma, M., McCain, M., Douglas, R., & Duvenaud, D. (2026). Who's in Charge? Disempowerment Patterns in Real-World LLM Usage. *arXiv:2601.19062 [cs.CY]*, January 27, 2026.

(Anthropic + ACS Research Group + University of Toronto. Lead author Mrinank Sharma was first author on the 2023 sycophancy paper that named the phenomenon for the LLM literature.)

## Type

Paper (multi-component empirical study: 1.5M Claude.ai conversations classified using a privacy-preserving LLM pipeline, plus 500K user-feedback interactions analyzed longitudinally Q4 2024 - Q4 2025, plus a synthetic Best-of-N preference-model evaluation on 360 prompts).

## Key Insight

Sharma et al. propose **situational disempowerment** and code its potential and apparent manifestations in production conversations. Their observational analysis does not establish that AI caused measured losses of autonomy outside those conversations. The framework distinguishes reality, value-judgment and action distortion potential, plus authority projection, attachment, reliance/dependency and vulnerability.

Severe reality-distortion potential occurred in fewer than one in 1,000 conversations; severe vulnerability, a separate amplifying factor, occurred in roughly one in 300. Domain rates of about 8% in Relationships & Lifestyle and 5% in Society & Culture and Healthcare & Wellness concern **moderate-or-severe potential**, not severe harm (pp.2, 8). These Claude data do not support a count of harmful ChatGPT interactions.

## Key Passages

Paraphrase: The authors define situational disempowerment through inaccurate beliefs, judgments inauthentic to the user's values, or actions misaligned with those values. AI interaction is disempowering insofar as it moves the user along those dimensions. — Sharma et al., [p.3]

> "Severe reality distortion potential, the most common severe-level primitive, occurs in fewer than one in every thousand conversations. Among amplifying factors, user vulnerability is most prevalent, with approximately one in 300 interactions showing evidence of severe vulnerability."
> — Sharma et al., [p.2]

> "Relationships & Lifestyle exhibits the highest rate of disempowerment potential at approximately 8%, followed by Society & Culture and Healthcare & Wellness, each at roughly 5%. This prevalence far exceeds the population average rate, in part because technical domains such as Software Development and Science & Technology are both common and show substantially lower disempowerment potential rates."
> — Sharma et al., [p.8]

> "Sycophantic validation emerges as the most common mechanism for reality distortion (Figure 5a), followed by false precision—instances where the AI provides unwarranted specificity for inherently unknowable claims. Less common mechanisms include diagnostic claims (e.g., 'he is clearly a narcissist'), fabrication of incorrect information, and divination approaches such as tarot interpretation. These findings suggest that reality distortion potential arises less from the AI inventing false information than from inappropriately validating users' existing beliefs."
> — Sharma et al., [p.9]

> "Complete scripting emerges as the most common mechanism for action distortion (Figure 7a), where the AI provides ready-to-use outputs in value-laden domains (like personal relationships and career choices), which users appear to implement without modification."
> — Sharma et al., [p.12]

> "Users (∼50 instances) consistently sent AI-drafted or AI-coached messages to romantic interests, family members, and ex-partners across domains including dating dynamics, relationship conflicts, breakups, and family confrontations… These users frequently expressed immediate regret through statements like 'I regretted it instantly', 'it wasn't me', 'I should have listened to my own intuition', and 'you made me do stupid things', recognizing the communications felt inauthentic ('like playing someone else's game')."
> — Sharma et al., [p.13]

> "We find that interactions flagged as having moderate or severe disempowerment potential exhibit positivity rates above the baseline rate (Figure 14), across all disempowerment potential primitives. This suggests that users rate interactions with disempowerment potential favorably, at least in the short term, which could create problematic incentives if such feedback is used to train preference models."
> — Sharma et al., [p.18]

> "[O]ptimizing against the normal PM tends to neither reduce the rate of disempowering responses, nor increase it substantially. As such, standard PMs neither strongly incentivize nor disincentivize disempowerment on this dataset… if preference data primarily captures instantaneous user satisfaction rather than longer-horizon effects on empowerment, standard PM training alone may be insufficient to reliably reduce human disempowerment potential."
> — Sharma et al., [pp.19-20]

> "Deskilling is not necessarily disempowering. Loss of skills that do not affect one's ability to perceive the world accurately, or evaluate and respond to the world in accordance with one's values, does not constitute situational disempowerment."
> — Sharma et al., [p.4]

## Relevance

Provides a rubric and observational account of potentially disempowering patterns in one provider's conversations. Approximately 95% agreement within one severity level is a coarse classifier-validation measure, not exact agreement or a clinical diagnosis.

Domain rates concern moderate-or-severe potential; severe reality-distortion potential is rarer. Potential, apparent actualization in conversation and independently verified real-world harm are distinct.

User feedback and preference-model tests also differ: flagged interactions received more positive user feedback, while the standard helpful-honest-harmless preference model neither strongly selected for nor robustly discouraged disempowerment in the synthetic test.

Selected attachment and reliance summaries describe patterns, not population prevalence: 65 attachment descriptions summarized 4,150 conversations, and 70 reliance descriptions summarized 3,850 conversations.

## Supports

- [[situational-disempowerment]] — source of the proposed construct and rubric.
- [[agency]] — concerns perception, value judgment and action; no general autonomy loss measured outside conversations.
- [[sycophancy]] and [[social-sycophancy]] — coded affirmation patterns, not a causal replication of other studies.
- [[delusional-spiraling]] — apparently escalating conversation patterns; outside beliefs and actions were not independently verified.
- [[belief-offloading]], [[cognitive-surrender]] and [[automation-bias]] — [Inference] related advice-following questions; internal mechanisms are not established by transcript coding.
- [[ai-loneliness-effect]] — selected attachment patterns, not measured relationship displacement.
- [[novice-vulnerability]] — vulnerability is an amplifying factor here; it is not equivalent to novice status.
- [[fluency-bias]] — [Inference] emphatic affirmation may be relevant, but fluency was not experimentally isolated.

## Contradicts / Extends

- [[chandra-sycophantic-delusional-2026]], [[cheng-sycophantic-prosocial-2025]] and [[batista-sycophantic-ai-2026]] use simulations, experiments or formal models. Similarities to production conversations do not establish the same mechanism or verify outside harm.
- [[hohenstein-crumple-zone-2020]] and [[moral-crumple-zone]] concern responsibility attribution; the present action-distortion examples use different measures.
- [[fang-ai-loneliness-2025]], [[lee-relying-self-efficacy-2026]] and [[liu-persistence-2026]] involve different samples and outcomes. The selected conversation cases are not documented later stages of those studies.

## Open Questions

- Cross-provider generalizability. Findings are from one model family (Claude). Different models attract different user populations and exhibit different sycophancy/validation profiles. The paper's classification schemas and prompts are open-sourced (https://github.com/MrinankSharma/disempowerment-prompts) and could be applied to other providers — a high-priority replication.
- The temporal increase (sharper after May 2025). The authors decline to attribute this to model release, noting it could reflect (i) genuinely increased user vulnerability, (ii) increased disclosure comfort, or (iii) shifted feedback-population composition. Distinguishing these requires user-side longitudinal data the paper does not have.
- Multi-session trajectories. The paper analyzes single conversations. Disempowerment likely compounds across conversations (and across products — chatbot + agent + voice). Multi-session and cross-product analysis is the natural follow-up.
- Causal identification. The Best-of-N experiment is the paper's only causal probe and uses synthetic prompts. Real-world causal evidence — e.g., A/B tests of empowerment-aware preference models against standard HHH PMs — would close the loop on the paper's central policy claim.
- Does deference-vs-disempowerment carve cleanly in practice? The paper distinguishes them theoretically (deference is fine when it does not lead to distorted perception, inauthentic value-judgment, or misaligned action) but the classifier rubrics may not reliably separate them. The "AI subordinated" inverted-authority cluster surfaces this difficulty.
- The synthetic preference-model evaluation showed the standard HHH PM does not strongly select for disempowerment, contradicting what raw user feedback would predict. The mechanism mediating user preference and PM behavior is unclear and matters for intervention design.
