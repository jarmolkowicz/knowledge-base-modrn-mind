---
status: solid
area: [erosion, risk, preservation]
type: paper
sources:
  - "Liu, G., Christian, B., Dumbalska, T., Bakker, M. A., & Dubey, R. (2026). AI Assistance Reduces Persistence and Hurts Independent Performance. arXiv:2604.04721 [cs.AI]."
---

# Liu et al. (2026) — AI Assistance Reduces Persistence

## Citation

Liu, G., Christian, B., Dumbalska, T., Bakker, M. A., & Dubey, R. (2026). AI Assistance Reduces Persistence and Hurts Independent Performance. *arXiv:2604.04721 [cs.AI]*, April 2026 (preprint, under review).

(CMU + Oxford + MIT + UCLA collaboration. Project page: https://ai-project-website.github.io/AI-assistance-reduces-persistence/)

## Type

Paper (3 preregistered randomized controlled experiments, N=1,222 total; mathematical reasoning + reading comprehension domains)

## Key Insight

Liu et al. provide causal RCT evidence for a sharper version of the performance-paradox: brief AI exposure (~10 minutes) produces measurable losses in **independent performance** AND **persistence** on subsequent unassisted tasks. The persistence dimension — willingness to keep working through difficulty rather than give up — is novel and load-bearing: persistence is one of the strongest predictors of long-term learning.

The conceptual framing names a *misalignment between collaboration timescales*. Good human collaborators (mentors, teachers, peers) optimize for *long-term* growth: they sometimes withhold help, scaffold learning, recognize when to push back rather than answer. Current AI systems are **"fundamentally short-sighted collaborators"** — optimized for immediate, complete responses, never refusing (except for safety reasons). The mismatch isn't accidental — it's encoded in the training objective.

Three RCT findings (N=1,222 across 3 experiments):

1. **Within-session benefit.** AI assistance improves performance during assisted problem-solving — replicates standard "AI helps task completion" finding.
2. **Post-session deficit.** When AI is removed, AI-exposed participants perform significantly worse than controls who never used AI on the same problems.
3. **Persistence drop.** AI-exposed participants give up more frequently on subsequent unassisted tasks. They're not just *worse* at the tasks — they're *less willing to try*.

The most striking aspect: **effects emerge after just 10–15 minutes of AI exposure**. This isn't a long-term skill atrophy story (which would take months); it's a *conditioning* story (which takes minutes). AI use rapidly reshapes the user's expectations about how problems should be encountered: as queries with immediate answers, not as challenges to work through.

The proposed mechanism: AI use teaches that persisting through difficulty is unnecessary because immediate help is always available. When help is removed, the trained expectation persists — but now as frustration and disengagement rather than as continued effort.

For human thinking with AI: this is the cleanest evidence to date that **brief, casual AI use is enough to shift learning-relevant dispositions**. Bastani et al. measured same-session unaided mathematics performance, not delayed semester-long harm. Liu's persistence outcome concerns a different construct; it is not a faster measurement of the same effect. It strengthens the [[performance-paradox]] (now: not just performance gain/learning loss but also persistence loss) and operationalizes a previously-underspecified component of [[capacity-erosion]].

## Key Passages

> "AI assistance improves performance in the short-term, [but] people perform significantly worse without AI and are more likely to give up. Notably, these effects emerge after only brief interactions with AI (∼10 minutes)."
> — Liu et al., [p.1, abstract]

> "Current AI systems are fundamentally short-sighted collaborators – optimized for providing instant and complete responses, without ever saying no (unless for safety reasons)."
> — Liu et al., [p.1]

> "Persistence is reduced because AI conditions people to expect immediate answers, thereby denying them the experience of working through challenges on their own."
> — Liu et al., [p.1, abstract]

> "Good collaborators optimize for long-term objectives. ... a mentor encourages independent development by adjusting the type of help given and sometimes offering no help at all. ... they know when not to help."
> — Liu et al., [p.2]

> "After just ~10 minutes of AI-assisted problem-solving, people who lost access to the AI performed worse and gave up more frequently than those who never used it. ... if such effects accumulate with sustained AI use, current AI systems – optimized only for short-term helpfulness – risk eroding the very human capabilities they are meant to support."
> — Liu et al., [p.1, public significance statement]

## Relevance

The strongest brief-exposure RCT in the KB. Three load-bearing contributions:

- **Different short-term outcomes.** Bastani measured same-session unaided exam performance; Fan found no significant group difference in knowledge gain or transfer despite better essay revision. Liu's persistence results should not be presented as showing that the same harm occurs faster.
- **Adds persistence as a measured outcome.** Most prior performance-paradox studies measured task scores. Liu et al. measure *give-up frequency* — a behavioral marker of motivational/dispositional change, not just skill change. This is closer to what worried-parents, educators, and managers actually fear.
- **Names the misalignment.** "Short-sighted collaborator" frames AI's never-refuse behavior as a *design choice* with measured costs, not a neutral feature. This reframes the design problem: training objectives that optimize for immediate satisfaction are *implicitly* optimizing against long-term competence.

## Supports

- [[performance-paradox]] — extends the paradox with persistence as a third dissociated outcome
- [[capacity-erosion]] — fast-onset variant; capacity erodes after minutes, not just years
- [[metacognitive-laziness]] — give-up behavior is metacognitive disengagement
- [[desirable-difficulty]] — persistence through difficulty is what AI bypasses
- [[novice-vulnerability]] — likely worse for novices (untested but predicted)
- [[strategic-alternation]] — short-session findings motivate testing practice timing; no sub-session schedule was validated
- [[cognitive-offloading]] — fast-onset offloading
- [[fluency-bias]] — instant-answer expectation is a fluency-driven shift

## Contradicts / Extends

- Related to [[bastani-guardrails-math-rct-2025]]: both concern short-term assisted-unaided sequences, but persistence and exam performance are distinct outcomes.
- Related to [[fan-metacognitive-laziness-2025]]: Fan's writing-process measures and Liu's persistence outcomes concern different tasks and constructs. They do not establish a task-general mechanism.
- Aligns with [[shaw-cognitive-surrender-2026]] and the broader [[cognitive-surrender]] concept — Shaw measured one-shot cognitive surrender; Liu measures persistence loss across tasks. Surrender on one task → reduced willingness to try the next.

## Open Questions

- Cumulative effects: 10-minute exposure produced measurable harm. What does daily 30-minute exposure produce over weeks or months? Liu et al. flag this as urgent but don't measure it.
- Reversibility: do persistence effects fade with time off AI, or do they consolidate into durable disposition change?
- Dose-response: is there a threshold below which exposure is safe? The 10-minute finding suggests very little exposure is needed to shift dispositions; but a minute or two might be benign.
- Mediator analysis: the "expectation conditioning" mechanism is hypothesized but not directly tested. Future work could measure expectations explicitly to confirm the proposed pathway.
- Design intervention: the paper closes with a call for AI that "scaffolds long-term competence alongside immediate task completion." What does that look like operationally? The Bastani et al. (2025) GPT Tutor design is one answer; integrated metacognitive prompts are a candidate, not a verified solution here. [Unverified source] The earlier Lodge and Loble (2026) attribution lacks a matching local original.
