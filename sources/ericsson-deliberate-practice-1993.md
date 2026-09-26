---
status: solid
area: [preservation]
type: paper
sources:
  - "Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of deliberate practice in the acquisition of expert performance. Psychological Review, 100(3), 363–406. doi:10.1037/0033-295X.100.3.363"
---

# Ericsson, Krampe & Tesch-Römer (1993) — Deliberate Practice

## Citation

Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of deliberate practice in the acquisition of expert performance. *Psychological Review*, 100(3), 363–406.

**DOI:** [10.1037/0033-295X.100.3.363](https://doi.org/10.1037/0033-295X.100.3.363)

## Type

Paper (theoretical synthesis with two original empirical studies of expert violinists)

## Key Insight

Ericsson and colleagues separate three categories of activity in any domain — **work, play, and deliberate practice** — and argue that only deliberate practice produces sustained improvement in performance. Deliberate practice is **designed** (typically by a teacher) to improve specific weaknesses; it is **effortful** and not inherently enjoyable; it requires **immediate informative feedback** and the chance to correct via repetition; and it pushes performance **at the edge of current ability**, not within the comfort zone.

The claim that accumulated hours distinguish every elite skill level is contested. [[macnamara-maitra-deliberate-practice-replication-2019]] found substantial practice differences across groups but no significant best-versus-good difference. Treat the original account as a theory supported in part, rather than a complete explanation of expertise.

The headline empirical claim — supported by violinist studies and a survey of literatures from chess to medicine to writing — is that elite performance in any well-established domain requires roughly **10 years of intense deliberate practice** (the "10-year rule," later popularized by Gladwell as the 10,000-hour rule). Crucially, the authors reject innate talent as a primary driver: "we reject any important role for innate ability." Differences among elite performers correlate with cumulative deliberate-practice hours.

For human thinking with AI: the conditions Ericsson et al. specify for deliberate practice — designed difficulty, effortful retrieval, immediate feedback on mistakes, repeated correction — are precisely the conditions AI tends to remove. AI gives the answer rather than scaffolding the struggle; it smooths over the productive failure that grows expertise. The "work" category is also relevant: in their framework, *work* (production under external pressure) does not improve performance; it relies on already-entrenched methods. AI-assisted output sits squarely in the work category.

## Key Passages

> "Individual differences, even among elite performers, are closely related to assessed amounts of deliberate practice. Many characteristics once believed to reflect innate talent are actually the result of intense practice extended for a minimum of 10 years."
> — Ericsson et al., [p.1] (abstract)

> "In contrast to play, deliberate practice is a highly structured activity, the explicit goal of which is to improve performance. Specific tasks are invented to overcome weaknesses, and performance is carefully monitored to provide cues for ways to improve it further. We claim that deliberate practice requires effort and is not inherently enjoyable. Individuals are motivated to practice because practice improves performance."
> — Ericsson et al., [p.4]

> "The costs of mistakes or failures to meet deadlines are generally great, which discourages learning and acquisition of new and possibly better methods during the time of work. For example, highly experienced users of computer software applications are found to use a small set of commands, thus avoiding the learning of a larger set of more efficient commands."
> — Ericsson et al., [p.4]

> "If only well-established domains with a large number of active individuals are considered we know of only a small number of exceptions to the general rule that individuals require 10 or more years of preparation to attain international-level performance."
> — Ericsson et al., [p.3]

> "Deliberate practice would allow for repeated experiences in which the individual can attend to the critical aspects of the situation and incrementally improve her or his performance in response to knowledge of results, feedback, or both from a teacher."
> — Ericsson et al., [p.4]

## Relevance

The foundational reference for why expertise development requires struggle, and therefore for why AI-as-shortcut undermines expertise development. Three load-bearing arguments for the KB:

- **Names the activity that builds capability.** "Deliberate practice" is the construct any KB entry on capacity preservation needs to anchor against. AI's value proposition (faster, easier, smoother) sits on the *opposite* axis from what builds expertise.
- **Distinguishes work from practice.** This is the KB's most useful borrow. Production work — what AI typically accelerates — is by definition *not* the activity that grows the worker. Mistaking work for practice (which is easy when AI makes work feel like progress) silently halts skill development.
- **Provides the mechanism.** Effortful retrieval + immediate feedback + repeated correction at the edge of ability. Each of those mechanisms maps onto a way AI substitution disrupts learning ([[fluency-bias]] removes the effort signal; [[automation-bias]] dampens correction; [[capacity-erosion]] is the long-run consequence).

The 10-year rule has been challenged in subsequent meta-analyses (Macnamara et al. 2014, the Macnamara & Maitra 2019 replication that failed to fully reproduce the original violinist effect sizes) — but the core distinction between work, play, and deliberate practice has held up and is the part most relevant to the KB.

## Supports

- [[desirable-difficulty]] — theoretical companion to Bjork's framework; Ericsson provides the activity-level theory while Bjork provides the cognitive mechanism
- [[strategic-alternation]] — design rationale for AI-off practice intervals
- [[capacity-erosion]] — what's lost when work crowds out deliberate practice
- [[think-first]] — operationalizes the "effortful retrieval" requirement at the moment AI is reached for
- [[cognitive-friction]] — the KB-side concept of productive struggle
- [[judgment-development-paradox]] — same dynamic generalized to professional judgment

## Contradicts / Extends

- Partially challenged by [[macnamara-maitra-deliberate-practice-replication-2019]]. In a preregistered replication with 39 violinists, accumulated practice alone explained 26% of performance-group variance, versus the original reported 48% using a different comparison. Less accomplished students practiced less, but the best and good groups did not differ significantly. Teacher-designed practice explained a similar amount (23%). Small samples and retrospective estimates limit both studies; the replication tests practice-hour explanations, not whether practice is unnecessary.
- Extends [[bjork-desirable-difficulties-2011]] — both papers argue for productive struggle; Bjork frames it cognitively (storage vs. retrieval strength), Ericsson frames it activity-wise (deliberate practice vs. work).

## Open Questions

- Ericsson's mechanism requires a teacher to design the practice (or, in later formulations, the practitioner themselves with sufficient self-knowledge). What's the analogue for AI-augmented work — does the AI itself become a feedback source, and if so, what makes its feedback "informative" in Ericsson's sense versus just confirmatory?
- The 10-year rule presumed humans build expertise in stable domains. If AI changes the relevant skill landscape every two years, can deliberate practice produce expertise in something that keeps moving?
- Where does the boundary sit between *desirable* practice difficulty (productive) and *undesirable* difficulty (frustration without learning)? Ericsson and Bjork both gesture at this; neither operationalizes it for the AI-augmented worker.
