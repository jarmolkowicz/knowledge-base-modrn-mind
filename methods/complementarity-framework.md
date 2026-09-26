---
status: speculative
area:
- preservation
- risk
sources:
  - "Vaccaro, M., Almaatouq, A. & Malone, T. (2024). When combinations of humans and AI are useful: a systematic review and meta-analysis. Nature Human Behaviour, 8, 2293–2303. https://doi.org/10.1038/s41562-024-02024-1"
  - "Dell'Acqua, F., Ayoubi, C., Lifshitz, H., Sadun, R., Mollick, E., Mollick, L., Han, Y., Goldman, J., Nair, H., Taub, S., & Lakhani, K. R. (2026). The Cybernetic Teammate: A Field Experiment on Generative AI and Teamwork. Organization Science, Articles in Advance. https://doi.org/10.1287/orsc.2025.20702"
  - "Liu, C. (2026). The Organizational Behavior of Agentic AI: Context, Boundaries, and Collective Intelligence in Human-Agent Workflows. arXiv:2606.30986v1."
  - "Ali, I., Nguyen, K., Ali, A. M., & Cui, T. (2025). Human–AI collaboration in knowledge ecosystems: A multidisciplinary review, integrative framework and future directions. Journal of Knowledge Management. https://doi.org/10.1108/JKM-03-2025-0431"
  - "Schmutz, J. B., Outland, N., Kerstan, S., Georganta, E., & Ulfert, A.-S. (2024). AI-teaming: Redefining collaboration in the digital era. Current Opinion in Psychology, 58, 101837. https://doi.org/10.1016/j.copsyc.2024.101837"
---

# Complementarity Framework

## Overview

A provisional design synthesis organizing human–AI collaboration around reasoning, memory, attention and coordination. Its five principles are suggestions for designing and evaluating a workflow, not a validated recipe for outperforming humans or AI alone.

## Author

[Unverified source] Earlier versions attributed this framework to Gonzalez, Donahue, Goldstein, Heidari, Jalali, Schelble, Singh and Woolley (2026), in PNAS Nexus. The local audit found no matching original or source entry. That attribution remains unverified; do not cite it as a confirmed publication. The linked studies below support specific observations, not authorship or validation of the complete framework.

## Core Idea

Human–AI combinations do not automatically beat the better of the human-only and AI-only baselines. Vaccaro et al. (2024) found substantial variation across tasks and relative ability. [Inference] Deliberate role design and explicit accountability are proposals to test, not proven necessary or sufficient conditions for synergy.

## Key Components

- **Reasoning**: AI clarifies goals, surfaces assumptions, flags misalignments, generates alternative hypotheses. Humans provide contextual judgment, ethical authority, and accountability. [Inference] Compare active checking with other interaction designs; superiority is not established here.
- **Memory**: AI serves as institutional memory — storing, retrieving, cross-referencing, and tracking expertise ("who knows what"). Humans contribute tacit, experiential, and embodied knowledge and validate AI-retrieved information. Together they form a transactive memory system.
- **Attention**: AI provides always-on scanning, anomaly detection, prioritization, and misinformation filtering. Humans contribute contextual interpretation, novelty detection, and judgment about when to redirect focus. Over-reliance on AI monitoring risks human disengagement.
- **Meta-Coordination and Governance**: Humans design team architecture — escalation paths, decision rights, division of labor. AI upholds procedural reliability through monitoring and workflow coordination. Human judgment guides adaptation; AI may help with consistency, but its contribution must be evaluated.

### Five Proposed Design Principles

1. **Define Goals and Constraints** — Encode multi-objective goals and ethical guardrails explicitly. Align AI optimization with human-defined values and boundaries.
2. **Build Knowledge Infrastructure** — Integrate AI into workflows with provenance tracking, audit trails, and expertise mapping. Maintain human control through intuitive interfaces.
3. **Orchestrate Attention and Interrogation** — Design interaction so AI elevates signal over noise and humans interrogate and direct reasoning. Establish escalation and disagreement protocols.
4. **Partition Roles** — Deliberately assign responsibilities based on complementary strengths. Give humans the steering wheel at critical junctures. Maintain traceability of human vs. AI contributions.
5. **Train and Evaluate Continuously** — Build shared training environments and simulations. Evaluate process quality (goal alignment, workload balance, error recovery), not just outcome accuracy. Use after-action reviews to refine both AI models and human protocols.

### Factors Shaping Complementarity

- **Team composition and size** — Dell'Acqua et al. (2026) randomized P&G workers to individual/team and AI/no-AI conditions. The authors interpret the average-quality pattern as diminishing returns from adding a second collaborator; the study did not follow teams through sequential expansion. Team+AI was approximately three times as likely to produce a top-decile solution as individuals without AI. This comparison is not evidence of synergy against AI alone, which was not tested.
- **Trust calibration** — Vaccaro et al. (2024) found no statistically significant performance moderation by AI explanations or confidence displays; this is not proof that either feature never helps, nor a direct test of trust calibration. Dell'Acqua et al. (2026) found lower best-idea selection rates with AI (approximately 37% versus 50%), even though selected outputs remained higher quality. The authors propose affirmation as one possible explanation; neither that mechanism nor a protective effect of deliberate friction was isolated.
- **User expertise** — Evaluate relevant task ability rather than assuming that a professional title predicts collaboration benefit.
- **Task characteristics** — Vaccaro et al. (2024) found negative synergy for decision tasks (g=−.27). The estimate for creation tasks was positive but not significantly different from zero (g=.19; 95% CI −.09 to .48; p=.180); the difference between task categories was significant. Relative ability also mattered: combined systems did better when humans were the stronger party. These findings do not establish a general rule that complex or strategic tasks favor a particular configuration.

Liu (2026, preprint) adds an internal-agent coordination question: what [[contextual-transaction-cost]] does each handoff create? A role label such as reviewer or manager does not guarantee independent evidence or accountability. The proposed interface between agents and human work specifies evidence identifiers, preserved uncertainty, permissions, audit traces, and human decision points.

Schmutz et al. (2024) review evidence that communication, coordination and mutual understanding can limit human–AI team performance even when the AI is capable. Some studies used simulated tasks or manipulated beliefs about an AI teammate rather than actual AI, so the findings do not establish a universal performance penalty. The review also identifies a gap in quantitatively linking shared mental models to human–AI team performance (PDF pp.2–4).

Ali et al. (2025) map organizational context alongside user expertise and AI capability: task fit, explanation quality, resources, governance and room to challenge outputs. Their review is a framework synthesis, not a joint causal test.

[Inference] Assess handoffs, information sharing, task fit and organizational support alongside joint outcomes. Compare the workflow with relevant human-only and AI-only baselines; adoption, trust and satisfaction alone do not demonstrate complementarity.

## Strengths

- Integrates insights across cognitive science, human factors, organizational behavior, AI alignment, and ethics — genuinely interdisciplinary
- Connects specific observations from linked research to provisional design questions
- Makes complementarity an outcome to test, not assume
- Maintains human ethical authority as non-negotiable
- Practical design principles are actionable for organizations
- Acknowledges that AI role varies on a spectrum from static tool to adaptive partner

## Limitations

- Evidence base is largely from laboratory studies, small-scale deployments, and prototypes — generalizability to high-stakes, long-term environments remains uncertain
- Framework is primarily descriptive and synthesizing rather than empirically tested as a unified model
- Limited attention to how complementarity dynamics change over time as humans adapt (potential skill erosion through prolonged reliance)
- Does not deeply address the developmental cost — what happens to human expertise when AI handles the tasks that traditionally built it
- Focuses on team-level design but less on individual cognitive costs of sustained human-AI collaboration
- The "teaming" framing risks anthropomorphizing AI, despite explicit disclaimers

Agent-only collectives require separate evidence from human-AI teams. In Liu's small local LLM demonstration, shared memory sometimes improved quality but single-agent execution had the highest efficiency once coordination costs were counted. The paper's synthetic simulation favored shared and adaptive forms. These different rankings argue for task-level comparison, not a universal preference for more agents. The cost metric and its weights are author-defined; field validation is still needed.

## Related

- [[human-ai-complementarity]] - the concept this framework operationalizes
- [[calibration]] - trust calibration is central to the framework
- [[automation-bias]] - a key barrier the framework addresses
- [[metacognition]] - underlies effective human oversight in the framework
- [[judgment]] - human judgment anchors the reasoning dimension
- accountability - accountability as non-delegable is a core premise
- [[scan]] - complementary framework for individual-level AI engagement calibration
- [[vaccaro-human-ai-meta-analysis-2024]] - meta-analytic evidence for the task-type and relative-ability factors; null result on AI explanations and confidence
- [[augmentation-synergy-gap]] - the framework targets synergy; the gap names what a framework that settles for mere augmentation leaves on the table
- [[dellacqua-cybernetic-teammate-2026]] — field comparison of team configurations and idea selection; affirmation is a proposed explanation
- [[cybernetic-teammate]] — the reframing (AI as counterpart, not tool) that the framework's "adaptive partner" end of the spectrum describes

- [[contextual-transaction-cost]] — transfer, reconstruction, and verification burdens inside an agent system.

## Sources

- [[vaccaro-human-ai-meta-analysis-2024]] — Vaccaro, M., Almaatouq, A. & Malone, T. (2024). When combinations of humans and AI are useful: a systematic review and meta-analysis. Nature Human Behaviour, 8, 2293–2303. https://doi.org/10.1038/s41562-024-02024-1
- [[dellacqua-cybernetic-teammate-2026]] — Dell'Acqua, F., Ayoubi, C., Lifshitz, H., Sadun, R., Mollick, E., Mollick, L., Han, Y., Goldman, J., Nair, H., Taub, S., & Lakhani, K. R. (2026). The Cybernetic Teammate: A Field Experiment on Generative AI and Teamwork. Organization Science, Articles in Advance. https://doi.org/10.1287/orsc.2025.20702
- [[liu-agentic-ai-organizational-behavior-2026]] — Liu, C. (2026). The Organizational Behavior of Agentic AI: Context, Boundaries, and Collective Intelligence in Human-Agent Workflows. arXiv:2606.30986v1.
- [[ali-human-ai-knowledge-ecosystems-2025]] — Ali, I., Nguyen, K., Ali, A. M., & Cui, T. (2025). Human–AI collaboration in knowledge ecosystems: A multidisciplinary review, integrative framework and future directions. Journal of Knowledge Management. https://doi.org/10.1108/JKM-03-2025-0431
- [[schmutz-ai-teaming-2024]] — Schmutz, J. B., Outland, N., Kerstan, S., Georganta, E., & Ulfert, A.-S. (2024). AI-teaming: Redefining collaboration in the digital era. Current Opinion in Psychology, 58, 101837. https://doi.org/10.1016/j.copsyc.2024.101837

