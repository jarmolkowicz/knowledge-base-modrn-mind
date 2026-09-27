---
status: solid
area: [erosion, preservation, risk]
type: paper
sources:
  - "Lee, E. H., Yin, Y., Jia, N., & Wakslak, C. J. (2026). Relying on AI at work reduces self-efficacy, ownership, and meaning while active collaboration mitigates the effects. Scientific Reports."
---

# Lee et al. (2026) — Relying on AI Reduces Self-Efficacy, Ownership, and Meaning

## Citation

Lee, E. H., Yin, Y., Jia, N., & Wakslak, C. J. (2026). Relying on AI at work reduces self-efficacy, ownership, and meaning while active collaboration mitigates the effects. *Scientific Reports*.

**DOI:** [10.1038/s41598-026-42312-6](https://doi.org/10.1038/s41598-026-42312-6)

(USC Marshall + Penn State Smeal. CC BY-NC-ND.)

## Type

Paper (preregistered experiment N=269 + complementary real-world survey N=270; three-condition between-subjects + within-subjects post-AI manual work)

## Key Insight

Lee et al. show that **the mode of AI use affected immediate psychological outcomes in the tested writing task**. The question prior research has focused on — does AI help or hurt productivity? — misses the more consequential question: how does the way AI is integrated into work shape the worker's psychological relationship to their labor?

Three conditions in the experimental study:
- **No AI** — control, manual writing
- **Passive AI use** — copying AI-generated content
- **Active collaboration** — human-generated draft followed by AI refinement

Three outcomes measured: **self-efficacy** (confidence in completing work without AI), **ownership** (feeling the output is one's own), **meaningfulness** (perceived meaning of the work).

Findings:
1. **Passive AI use undermined all three outcomes.** Self-efficacy, ownership, and meaning all dropped relative to no-AI controls.
2. **Effects persisted into post-AI manual work.** Even after participants stopped using AI, declines in efficacy and meaning carried over — the harm wasn't confined to the AI-using moment.
3. **Active collaboration showed no detected deficit in these psychological outcomes.** The draft-then-refine condition produced efficacy, ownership, and meaning without statistically detected differences from the no-AI arm; this does not establish equivalence.
4. **Enjoyment reversal.** Passive AI use initially produced higher enjoyment and satisfaction, but those benefits reversed once participants returned to manual work — showing an immediate reversal, without measuring durable psychological resources.

The N=270 follow-up survey reported related associations across non-writing tasks; it was not an experimental replication.

The study distinguishes passive copying from active collaboration and reports different immediate psychological outcomes. This does not establish a universal rule about harm. Bastani's mathematics experiment compares different assistance designs and measures different outcomes; the two do not establish the same mechanism.

The experiment provides evidence that **different uses can change immediate self-efficacy, ownership and meaning**. It connects [[ai-self-efficacy-erosion]] (the named phenomenon) to specific behavioral patterns (passive copying), and points toward operational guidance ("draft first, then refine with AI" rather than "ask AI, then copy").

## Key Passages

> "Passive use undermined self-efficacy, ownership, and meaningfulness, with declines in efficacy and meaning persisting even when participants returned to manual work. In contrast, collaborative AI use preserved psychological connection to the task, producing outcomes comparable to independent work."
> — Lee et al., [p.2, abstract]

> "Although passive use initially boosted enjoyment and satisfaction, these benefits reversed once participants resumed manual work."
> — Lee et al., [p.2, abstract]

> "The psychological consequences of AI use hinge on how it is integrated into human workflows, underscoring that strategies promoting active, collaborative use may help capture AI's productivity benefits while preserving human workers' agency, competence, and connection to their work."
> — Lee et al., [p.2, abstract]

> "The key issue may not be whether AI is used, but how it is used."
> — Lee et al., [p.2]

## Relevance

Three contributions:

- **Operationalizes the mode-of-use distinction.** Passive copying vs. active collaboration is a measurable behavioral distinction with documented psychological consequences. Practitioners can act on this — "draft first, then refine" is a concrete protocol.
- **Documents three distinct outcomes with one design.** Self-efficacy, ownership, meaning are conceptually related but empirically dissociable. Lee et al. show all three move together under passive use — without isolating a single common mechanism.
- **The post-AI carry-over effect.** Some self-reported differences remained in the immediate subsequent manual task. Comparison with [[liu-persistence-2026]] requires keeping outcomes and time horizons separate.

## Supports

- [[ai-self-efficacy-erosion]] — primary empirical anchor for the concept
- [[nikolova-robots-meaning-2024]] — Nikolova found meaning loss under robotic automation; Lee extends to AI knowledge work
- [[execution-commoditization]] — passive copying treats execution as commodity; active collaboration preserves the engagement
- [[mascanero-proximal-collaboration-2026]] — both papers find that *how* humans engage with AI determines the outcome; Mascareño at innovation-stage level, Lee at psychological-outcome level
- [[liu-persistence-2026]] — fast-onset, post-AI persistence
- [[strategic-alternation]] — protocol implication: draft first, refine with AI
- [[think-first]] — operational counter-measure
- [[performance-paradox]] — passive use boosts enjoyment temporarily, masks underlying decline
- [[bastani-guardrails-math-rct-2025]] — both papers find structured use mitigates harm of unstructured use
- [[novice-vulnerability]] — [Speculation] novice vulnerability requires a direct subgroup test

## Contradicts / Extends

- Extends [[passalacqua-less-ai-2024]] — Passalacqua showed partial automation outperforms full automation on engagement; Lee adds the psychological-outcome layer (efficacy/ownership/meaning), raising related psychological questions without establishing a shared identity mechanism.
- Relates to [[strategic-alternation]], but does not test or validate an AI-on/AI-off schedule.

## Open Questions

- The "active collaboration" condition (draft-then-refine) is one specific operationalization. What about other variants — outline-then-AI-fills-in, AI-suggests-then-human-rewrites, joint iterative editing?
- Long-term persistence of effects: passive use carried over to immediate post-AI manual work. Does it consolidate over weeks/months into trait-level changes in self-concept?
- Domain dependence: replicated across writing + non-writing in the survey. Are there domains where passive use is psychologically benign (e.g., tasks the worker doesn't identify with)?
- Self-perception of mode: do users *know* they're in passive vs. active mode? If not, the protective recommendation requires user-facing scaffolding to enforce the active mode.
