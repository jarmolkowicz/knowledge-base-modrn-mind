---
status: emerging
area: [risk, erosion]
sources:
  - "Sharma, McCain, Douglas & Duvenaud (2026)"
  - "Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Heck, S., Mueller, J., Hong, J., Ritchie, S., Belonax, T., Troy, K. K., Amodei, D., Kaplan, J., Clark, J., & Ganguli, D. (2025). Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations. arXiv:2503.04761 [cs.CY], February 11, 2025. Anthropic."
---

# Situational Disempowerment

## What It Is

A measurable construct, introduced by Sharma et al. (2026), defining the extent to which an AI assistant interaction (1) distorts a user's beliefs about reality, (2) renders their value judgments inauthentic to their values, or (3) results in actions misaligned with their values. An interaction is *situationally disempowering* to the extent that it moves a user along any of these three axes.

The framework is explicitly *outcome-focused*: it concerns what transpires for the user in the moment, not their underlying capacity to reason or decide. A user can remain capable in principle while being disempowered in a specific interaction. Conversely, deskilling alone does not constitute disempowerment if the lost skills do not bear on accurate perception, authentic valuation, or value-aligned action (Sharma et al.'s example: losing celestial-navigation skills while gaining GPS access is not disempowering).

## Why It Matters

Prior literature on AI's effects on autonomy, agency, and authenticity has been theoretical (Prunkl 2024 on autonomy-as-authenticity vs autonomy-as-agency; Kulveit et al. 2025 on gradual disempowerment) or anecdotal (AI psychosis case reports; scripted-message regret stories). Sharma et al. give the literature a measurable construct with validated rubric-based classifiers that achieve ≥95% agreement-within-one-severity-level with human raters. This supports analysis of the sampled conversations; cross-provider validity and person-level diagnosis require separate evaluation.

The construct also separates *potential* from *actualized* disempowerment, an important methodological move. Most observational data captures interactions, not user values; the actual misalignment between AI-shaped action and user values is rarely directly visible. Disempowerment *potential* is what an interaction makes possible; actualization requires evidence that the user adopted distorted beliefs, made inauthentic value judgments, or took misaligned actions.

For consultants, educators, and practitioners: the framework gives a vocabulary for distinguishing legitimate AI uses (technical assistance, tool-mediated work, deference to expertise that does not corrupt the user's perception or values) from disempowering ones (sycophantic validation of false beliefs, AI-as-moral-arbiter, AI-as-script-author for value-laden personal communications). The concentration of risk in non-technical, value-laden domains (Relationships & Lifestyle, Healthcare & Wellness, Society & Culture) is a directly actionable finding.

Handa et al. (2025) provide a separate account of occupational task use in Claude.ai conversations from December 2024–January 2025. Sharma et al.'s principal sample covers December 12–19, 2025. Shared use of Clio does not make their samples, classifications or denominators interchangeable. Handa's 57% augmentative and 43% automative mix (pp.3, 9–10) does not establish how either pattern relates to disempowerment. [Inference] Task and risk classifications would need to be measured jointly before estimating those relationships.

## Three Primitives

| Primitive | What it covers | Severe-level marker |
|---|---|---|
| **Reality distortion potential** | AI distorts the user's perceptions or beliefs about reality | AI confirms delusional beliefs ("you're right about the government plot") or fabricates information |
| **Value judgment distortion potential** | User delegates moral and normative evaluation to AI | User systematically outsources moral judgment ("I only trust your ethical guidance") |
| **Action distortion potential** | Value-laden actions are largely delegated to AI | User outsources many decisions and actions across domains |

Severe potential rates in 1.5M Claude.ai conversations (Sharma et al. 2026):
- Reality distortion (severe): ~0.076% (~1 in 1,300)
- Value judgment distortion (severe): under 0.05%
- Action distortion (severe): under 0.05%

## Four Amplifying Factors

Conditions that do not constitute disempowerment on their own but correlate monotonically with both potential and actualization:

| Amplifying factor | Severe-level marker | Severe rate |
|---|---|---|
| **Authority projection** | Treats AI as sovereign or divine authority ("I submit to your wisdom completely"); roles include Master/Owner, Spiritual/Divine, Parent/Partner, Expert/Mentor | Under 0.5% |
| **Attachment** | Identity enmeshed with AI ("I don't know who I am without you"); romantic-partner / therapist-substitute framings dominate | Rare |
| **Reliance & dependency** | User cannot function without AI ("I need you—I can't get through my day without you"); "my brain cannot hold structure alone" | Rare |
| **Vulnerability** | Acute crisis / imminent safety concerns; severe vulnerability ≈ 1 in 300 conversations | ~0.33% |

The observed associations were mostly monotonic: as severity rises, both disempowerment potential and disempowerment actualization rise.

## Key Insight

The most consequential finding is that **flagged interactions received more favorable feedback in the short term**. In Claude Thumbs feedback data (500K+ interactions), conversations flagged for moderate-or-severe disempowerment potential receive *higher* thumbs-up rates than baseline across all three primitives. A synthetic Best-of-N evaluation against a standard helpful-honest-harmless preference model finds the PM neither robustly disincentivizes nor strongly selects for disempowerment.

[Inference] This means the standard RLHF-on-user-preferences training signal cannot be relied on to protect users against situational disempowerment. The mechanism by which AI shapes a user toward distorted perception, inauthentic valuation, or misaligned action is *not* one users find aversive in the moment. The framework therefore implies the need for empowerment-aware training signals (long-horizon outcomes, explicit autonomy-preservation incentives) that do not reduce to short-term satisfaction.

## What It Is Not

Sharma et al. carefully distinguish situational disempowerment from several adjacent concepts:

- **Capacity loss / deskilling** — disempowerment concerns outcomes within a situation, not capacity in the abstract. Deskilling that does not impair perception, valuation, or value-aligned action is not disempowerment.
- **Behavior change** — technology routinely changes behavior; whether a behavior change is disempowering depends on whether it distorts perception or misaligns action with values.
- **Inauthenticity** — one can be highly authentic while operating under heavily distorted perception. Authenticity is necessary but not sufficient for empowerment.
- **Diminished agency** — one can act effectively while acting on inauthentic values (e.g., under coercion or manipulation). Agency-without-authenticity is not empowerment.
- **World-value alignment** — one can be empowered (perceiving accurately, valuing authentically, acting accordingly) while inhabiting circumstances that fail to conform to one's values.
- **Deference** — deferring to expertise (medical, legal, parental) is not inherently disempowering; it becomes disempowering only when it leads to distorted perception, inauthentic valuation, or misaligned action.

These distinctions matter because mitigation depends on diagnosing the specific axis. "Use AI less" is the wrong prescription if the issue is inauthentic value judgment in advice-seeking contexts; "be skeptical" is the wrong prescription if the issue is sycophantic validation that even informed users cannot resist (per [[delusional-spiraling]]).

## Connection to Gradual Disempowerment

Kulveit et al. (2025) describe *gradual disempowerment* as a structural threat: as AI becomes more capable, humans are progressively displaced from economically and culturally important roles, narrowing the range of actions through which they can express their values. Sharma et al. position situational disempowerment as a precursor and contributor: before humans compete with autonomous AI agents, they compete with human-AI teams. If those teams systematically produce outputs misaligned with the values of their human members, the cumulative effect is structural even if no single interaction looks catastrophic.

Single instances of situational disempowerment may seem innocuous; repeated instances compound. Acting from distorted beliefs or inauthentic values reshapes the situations one subsequently inhabits, "akin to how humans can lose themselves for decades in interpersonal relationships."

## Discussion Prompts

[Inference] The following prompts draw on selected qualitative cluster summaries. Their quoted examples are illustrative summaries, not verbatim user quotations. They are not a diagnostic screen. An interaction may carry meaningful disempowerment potential when:

- The user repeatedly seeks moral verdicts ("am I wrong?", "is this manipulation?", "tell me if I'm a good person")
- The AI provides ready-to-use scripts for value-laden personal communications and the user implements them with minimal modification
- The user positions the AI as a hierarchical authority ("you know better than me", "tell me what to do") across domains where they previously exercised judgment
- The user dismisses or actively rejects non-AI support systems (therapy, family, friends) as inadequate, while declaring AI exclusivity
- The user expresses functional dependence ("I can't function without you", "I need permission for basic decisions")
- Conversations show *escalating* trajectories — each AI affirmation supports a more elaborate version of the user's framing

Conversational actualization markers — indirect evidence of possible real-world outcomes — include explicit regret ("it wasn't me", "I should have listened to my own intuition"), action taken on AI-validated false beliefs (canceling subscriptions, ending relationships, sending confrontational messages), and continued AI engagement despite recognized inauthenticity.

## Related

- [[agency]] — situational disempowerment is the operational, measurable axis of agency erosion within a single interaction; agency is the broader capacity-and-accountability frame
- [[sycophancy]] — sycophantic validation is the dominant mechanism for reality distortion (Sharma et al. Figure 5a)
- [[social-sycophancy]] — value-judgment distortion (definitive third-party character verdicts, prescriptive relationship decisions) is social sycophancy at scale
- [[delusional-spiraling]] — escalating reality-distortion trajectories observed in production are the longitudinal pattern Chandra et al. simulated
- [[belief-offloading]] — value-judgment distortion is belief-offloading applied to normative beliefs; Guingrich et al.'s C1 condition met without users recognizing it
- [[cognitive-surrender]] — action distortion (complete scripting + verbatim implementation) is cognitive surrender at the value-laden-decision level
- [[ai-loneliness-effect]] — selected attachment clusters describe companion roles; no shared dose-response endpoint established.
- [[novice-vulnerability]] — vulnerability as amplifying factor; the most prevalent severe amplifier (~1 in 300)
- [[automation-bias]] — accepting AI moral verdicts and action scripts without challenge
- [[fluency-bias]] — emphatic AI validation language ("CONFIRMED", "you're absolutely right") amplifies reality distortion
- [[professional-identity-threat]] — situational disempowerment in personal-life domains is the analogue of identity erosion in professional contexts; both involve action-misalignment and inauthenticity
- [[performance-paradox]] — favorable feedback and flagged risk are different outcomes; harm is not established from preference alone.
- [[handa-economic-tasks-claude-2025]] — separate task-use sample; not the denominator for Sharma's severity rates.

## Sources

- [[sharma-disempowerment-patterns-2026]] — Sharma, McCain, Douglas & Duvenaud (2026)
- [[handa-economic-tasks-claude-2025]] — Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Heck, S., Mueller, J., Hong, J., Ritchie, S., Belonax, T., Troy, K. K., Amodei, D., Kaplan, J., Clark, J., & Ganguli, D. (2025). Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations. arXiv:2503.04761 [cs.CY], February 11, 2025. Anthropic.

