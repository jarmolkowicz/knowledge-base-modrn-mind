---
status: emerging
area: [risk, preservation]
type: paper
sources:
  - "Liu, C. (2026). The Organizational Behavior of Agentic AI: Context, Boundaries, and Collective Intelligence in Human-Agent Workflows. arXiv:2606.30986v1."
---

# Coordination Costs in Collectives of AI Agents

## Citation

Liu, C. (2026). *The Organizational Behavior of Agentic AI: Context, Boundaries, and Collective Intelligence in Human-Agent Workflows*. [arXiv:2606.30986v1](https://arxiv.org/abs/2606.30986). Version marker: 29 June 2026; manuscript dated 1 July 2026.

## Type

Theory-building preprint with synthetic simulations and a small instrumented LLM demonstration. No field study of human organizations.

## Key Insight

Giving agents titles such as manager or reviewer does not reproduce human coordination or accountability. [[contextual-transaction-cost]] names the burden of preserving usable task information as it crosses agents, memory, tools, and human review.

## Methods and Results

Study 1 generated 8,000 synthetic tasks, each evaluated under seven organizational forms: 56,000 task–form observations. Task properties included complexity, decomposition, coupling, verifiability, ambiguity, risk, and knowledge velocity. Within-task models compared a single agent with pipeline, hierarchy, committee, market, shared-memory, and adaptive forms. Collective efficiency combines quality, success, and weighted costs (pp.7–11).

Shared-memory and adaptive forms led the simulation. Its large gains—such as 89.24% greater adaptive efficiency over a single agent—are model outputs under designed assumptions, not observed organizational productivity gains. Cost is part of the outcome formula, so the cost–efficiency relationship is partly built into the metric.

Study 2 used local tasks modeled after software repair, long-document QA, legal review, and literature synthesis; these were not official benchmark splits. Table 4 reports 12 runs per form with commercial models and 8 per form with open models (80 runs total). Single-agent execution had the highest efficiency in both sets. For commercial models, shared memory raised mean quality from 92.04 to 94.06 but lowered efficiency from 81.44 to 45.11. Thus the real-model demonstration qualifies the simulation's ranking (pp.10, 13–15).

Appendices report prompt sensitivity and a learned selector trained on the simulated environment. These probe robustness within the setup; they do not supply independent field validation.

## Key Passages

> “Contextual transaction cost is the cost of making task context usable across boundaries in an agent collective.”
> — Liu, [p.6], section 3.2

> “This design does not substitute for field studies of human-agent workflows. It prepares them.”
> — Liu, [p.9]

> “The current implementation uses local executable and automatically scored tasks rather than official benchmark splits.”
> — Liu, [p.10]

## Relevance

Makes a hidden cost of delegation inspectable: repeated summaries, missing evidence, changed meanings, and the human work needed to verify the final answer. The paper suggests checking whether each extra handoff creates a benefit worth that cost.

## Supports

- [[contextual-transaction-cost]] — named theoretical mechanism with illustrative measurements.
- [[agency]] — human accountability needs explicit evidence, permissions, and review points.
- [[judgment]] — a reviewer role does not guarantee independent error detection.
- [[complementarity-framework]] — extends coordination design to the internal organization of agent systems.

## Contradicts / Extends

- Extends [[complementarity-framework]] with context-transfer costs and a warning that more agents can share the same errors.
- Distinguishes agent-only collectives from [[cybernetic-teammate]], which concerns human work with AI. The simulation is not evidence about human-team psychology.

## Limitations

Preprint, synthetic task generation, author-defined cost weights, small local model sample, and no deployment study. The supplied paper does not provide enough task-generation, weighting, or implementation detail to independently reproduce all reported results. Apparent agreement between simulation and a policy learned on that simulation is not an independent validation. Architecture rankings should not become universal rules.

## Open Questions

- Do estimated context costs predict actual human verification time and consequential errors?
- When does shared memory preserve evidence, and when does it spread an early mistake?
