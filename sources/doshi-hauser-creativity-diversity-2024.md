---
status: solid
area: [risk]
type: paper
sources:
  - "Doshi, A. R., & Hauser, O. P. (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. Science Advances, 10(28), eadn5290. doi:10.1126/sciadv.adn5290"
---

# Doshi & Hauser (2024) — Creativity-Diversity Paradox

## Citation

Doshi, A. R., & Hauser, O. P. (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. *Science Advances*, 10(28), eadn5290.

**DOI:** [10.1126/sciadv.adn5290](https://doi.org/10.1126/sciadv.adn5290)

## Type

Paper (preregistered two-phase online experiment, N=293 writers + N=600 evaluators)

## Key Insight

Doshi & Hauser's preregistered study tests whether AI-assisted writing increases or decreases creativity. Three conditions: human-only, human + 1 AI idea, human + up to 5 AI ideas. Stories evaluated by independent raters (N=600) on novelty and usefulness.

The finding is structurally important: **individual creativity rises, collective diversity falls.** The "creativity-diversity paradox":

- **Individual gains:** stories with AI access were judged 8.1% more novel (with 5 ideas) and 9.0% more useful than human-only stories. Less-creative writers gained the most (up to +26.6% on quality).
- **Collective loss:** AI-assisted stories were significantly more *similar to each other* than human-only stories. The convergence is toward a "sophisticated average" — better than the worst human stories but more uniform than the human distribution.

The authors describe a possible **social dilemma**: average output ratings improved while stories became more similar. This does not show that every writer benefited, that human skill declined, or that breakthrough novelty was suppressed.

The leveling pattern (low performers gain more) connects to [[dellacqua-jagged-frontier-2023]]'s leveling effect at consulting tasks: AI raises the floor disproportionately. Higher between-story similarity is a distinct outcome from changes in the upper range of quality or long-term creative capability.

For human thinking with AI: this is the foundational empirical anchor for the [[creativity-diversity-paradox]] concept. The KB's argument that collective and individual outcomes can diverge under AI substitution has its strongest evidence here.

## Key Passages

> "We find that access to generative AI ideas causes stories to be evaluated as more creative, better written, and more enjoyable, especially among less creative writers. However, generative AI–enabled stories are more similar to each other than stories by humans alone."
> — Doshi & Hauser, [p.1] (abstract)

> "These results point to an increase in individual creativity at the risk of losing collective novelty. This dynamic resembles a social dilemma: With generative AI, writers are individually better off, but collectively a narrower scope of novel content is produced."
> — Doshi & Hauser, [p.1]

> "Writers in the Human with five GenAI ideas condition show an increase in novelty of 8.1% (b = 0.311, P < 0.001) over writers without generative AI access."
> — Doshi & Hauser, [p.2-3]

> "Having access to up to five AI ideas increases usefulness by 9.0% (b = 0.453, P < 0.001) over those with no generative AI access."
> — Doshi & Hauser, [p.3]

## Relevance

The KB's clearest empirical demonstration that **individual benefits and collective costs of AI can diverge**. Three contributions:

- **Quantifies the divergence.** Same intervention, opposite signs at individual vs. collective level. The outcomes should be interpreted within this short-story task.
- **Suggests an anchoring explanation.** Convergence toward AI's "sophisticated average" — writers anchor on AI's starting points and produce variations of the same template. This does not establish that the same mechanism determines quality and diversity.
- **Practical/policy hook.** Decisions about AI deployment that look beneficial at the individual level may be net-negative at the population level. This is structurally hard for organizations to address because each individual user's incentives point toward AI use.

## Supports

- [[creativity-diversity-paradox]] — primary source for the construct
- [[leveling-effect]] — larger output-rating gains among initially lower-creativity writers
- [[anderson-homogenization-2024]] — converging evidence at the cognitive level (Anderson et al. show same homogenization at group rather than individual level)
- [[capacity-erosion]] — output diversity changed; loss of human creative ability was not measured
- [[runco-jaeger-creativity-2012]] — the bipartite definition of creativity (originality + effectiveness) clarifies *what* AI is enhancing (both) and *what* it's eroding (collective novelty)

## Contradicts / Extends

- Companion to [[anderson-homogenization-2024]] (Anderson, Shah & Kreminski) — same finding, different methodology (idea generation rather than story writing). Two independent studies converge.
- Extends Mollick's "leveling" observations from his own work and from [[dellacqua-jagged-frontier-2023]] — Mollick & co. saw novices gain more; Doshi & Hauser show the cost of that gain at population level.

## Open Questions

- The "sophisticated average" is the average of the LLM's training distribution. As LLMs train on AI-generated content, does the average converge further? Recursive collapse of diversity is a worried prediction; not yet measured.
- The study is short stories. Does the paradox extend to longer creative work where human revision dominates? Maybe AI is most homogenizing in the *initial* idea phase, and human revision rebuilds diversity downstream.
- Practically: can interventions (prompt diversity, randomized seeds, deliberate "go further" instructions) recover collective diversity while preserving individual gains? Operational question for designers.
