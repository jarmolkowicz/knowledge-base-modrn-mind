---
status: solid
area: [risk, erosion, preservation]
type: paper
sources:
  - "Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers. In CHI Conference on Human Factors in Computing Systems (CHI '25), April 26–May 1, 2025, Yokohama, Japan. ACM."
---

# Lee et al. (2025) — Critical Thinking Effects of GenAI on Knowledge Workers

## Citation

Lee, H.-P., Sarkar, A., Tankelevitch, L., Drosos, I., Rintel, S., Banks, R., & Wilson, N. (2025). The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers. In *CHI Conference on Human Factors in Computing Systems (CHI '25)*, April 26–May 1, 2025, Yokohama, Japan. ACM.

**DOI:** [10.1145/3706598.3713778](https://doi.org/10.1145/3706598.3713778)

(Carnegie Mellon University + Microsoft Research Cambridge. Open-access under CC BY 4.0.)

## Type

Paper — large-scale knowledge-worker survey (N = 319; 936 first-hand task examples; mixed quantitative + qualitative analysis; CHI '25 archival).

## Key Insight

The first peer-reviewed survey to directly measure how knowledge workers enact critical thinking when using GenAI — across 936 real-world task examples from 319 workers in diverse occupations. Two findings anchor the paper. First, a confidence pair: **higher confidence in GenAI is associated with less critical thinking** (β = −0.69, p < 0.001 for perceived enaction), while **higher self-confidence is associated with more critical thinking** (β = +0.26, p = 0.026). Second, GenAI shifts the effort of critical thinking in three ways: from information *gathering* to information *verification*, from problem *solving* to AI response *integration*, and from task *execution* to task *stewardship*. The "task stewardship" framing — accountability without material production — has already entered downstream literature ([[bartos-ai-learning-meta-meta-2026]] discusses it among possible explanations for learning outcomes, not as evidence for a null result), and this source provides the workbench-level grounding the KB has been citing without anchoring.

## Key Findings

> "We surveyed 319 knowledge workers who use GenAI tools (e.g., ChatGPT, Copilot) at work at least once per week, to model how they enact critical thinking when using GenAI tools, and how GenAI affects their perceived effort of thinking critically. Analysing 936 real-world GenAI tool use examples our participants shared, we find that knowledge workers engage in critical thinking primarily to ensure the quality of their work."
> — Lee et al., [p.16, Conclusion]

> "Our results provide empirical evidence that knowledge workers' confidence in AI doing the tasks indeed negatively correlates with their enaction of critical thinking (β=-0.69, p < 0.001)."
> — Lee et al., [p.9]

> "1) a higher confidence in GenAI is associated with less critical thinking even though it is perceived as less effort to do so, and 2) a higher self-confidence is associated with more critical thinking even though it is perceived as more effort to do so."
> — Lee et al., [p.13]

> "GenAI tools shift the effort of critical thinking in three distinct ways: for Knowledge and Comprehension, the effort shifts from information gathering to information verification; for Application, effort shifts from problem-solving to AI response integration; and for Analysis, Synthesis, and Evaluation, effort shifts from task execution to task stewardship."
> — Lee et al., [p.12]

> "Unlike in human-human collaboration, in a human-AI 'collaboration', the responsibility and accountability for the work still resides with the human user despite the labour of material production being delegated to the GenAI tool, which makes stewardship strike us as a more appropriate metaphor for what the human user is doing, than teammate, collaborator, or supervisor."
> — Lee et al., [p.14]

> "While critical thinking may not be necessary for low-stakes tasks, it is risky for users to only apply critical thinking in high-stakes situations. Without regular practice in common and/or low-stakes scenarios, cognitive abilities can deteriorate over time."
> — Lee et al., [p.10]

## Survey-Level Findings (Prevalence Numbers)

The paper's survey scale gives KB-relevant prevalence figures that small-N lab studies cannot supply.

**Sample composition.** N = 319 knowledge workers (159 men, 153 women, 5 non-binary, 2 prefer-not-to-say); ages 18–55+ (44.83% in 25–34 bracket); top occupations: Computer & Mathematical (18.50%), Arts/Design/Entertainment (13.79%), Office & Administrative Support (11.91%), Business & Financial Operations (10.97%), Educational Instruction (7.21%); top countries UK, Canada, US, South Africa, Poland; ChatGPT used by 96.87% of participants, Copilot by 23.20%, Gemini by 21.63% [p.6, Table 3].

**Critical thinking enaction.** Workers self-reported enacting critical thinking on **555 of 936 examples (59.29%)** [p.6]. Distribution across task types: Creation 374 (39.96%), Information 303 (32.37%), Advice 259 (27.67%) [p.6].

**Effort reduction across Bloom's six activities** [p.11]. Percentage of examples reported as "less" or "much less" effort with GenAI vs. without:
- Knowledge (recall): **72%**
- Comprehension (organising/translating ideas): **79%**
- Application (problem-solving): **69%**
- Analysis (breaking down a problem): **72%**
- Synthesis (putting together ideas): **76%**
- Evaluation (quality checking): **55%** — the lowest, consistent with Evaluation being the activity where verification work shifts in.

**Quantitative regression coefficients (Benjamini–Hochberg-corrected p-threshold = 0.007)** [p.10, Table 4]:
- Confidence in AI → enaction of critical thinking: **β = −0.69, p < 0.001**
- Confidence in self → enaction: β = +0.26, p = 0.026
- Confidence in evaluation → enaction: β = +0.31, p = 0.046
- Tendency to reflect → enaction: β = +0.52, p < 0.001
- Trust in GenAI → effort for Evaluation: β = −0.24, p < 0.001
- Trust in GenAI → effort for Application: β = −0.17, p = 0.002
- Trust in GenAI → effort for Knowledge: β = −0.12, p = 0.029
- Confidence in self → effort for Application: β = +0.08, p = 0.029
- Confidence in self → effort for Evaluation: β = +0.10, p = 0.027

**No significant effects** for task type (Creation/Advice/Information), gender, age group, or occupation's risk-of-automation classification, on either enaction or effort.

**Qualitative codebook prevalence (counts out of 319 participants)** [pp.9–10]:
- *Motivators for critical thinking*: avoid negative outcomes (116/319), improve work quality (74/319), skill development (13/319).
- *Awareness inhibitors*: trust/reliance on GenAI (83/319), task perceived trivial/insignificant (55/319), task perceived secondary to goal (14/319).
- *Motivation inhibitors*: lack of time (44/319), critical thinking not part of job scope (11/319).
- *Ability inhibitors*: barriers to revising query/improving response (72/319), barriers to inspecting AI response due to lack of domain knowledge (58/319).
- *Effort-shift qualitative codes*: information gathering reduced (111/319), readable information presentation (87/319), need to verify (56/319), problem-solving via personalised solutions (77/319), increased effort applying responses (19/319), scaffolding complicated tasks (48/319), translating intentions into queries (45/319), automation of creation (129/319), constant steering (48/319), personalised feedback loops (40/319), evaluating AI-generated content (42/319).

## Relevance

Three load-bearing contributions:

- **Survey evidence with a defined sample.** The 936 examples from 319 workers concern reported thinking and effort, not measured prevalence of mechanisms established by Fan, Bastani, Kosmyna or Stadler. Comparing these sources requires keeping self-report, task-process and performance outcomes separate.

- **The confidence pair.** β = −0.69 (confidence in AI → less critical thinking) and β = +0.26 (confidence in self → more critical thinking) is the cleanest survey-level demonstration that *who* is confident determines whether GenAI use is engaged or surrendered. Trust-in-GenAI also flattens perceived effort across four of six Bloom activities. This is the field-scale analogue of Shaw & Nave's lab finding that AI access inflates confidence by ~12 percentage points regardless of accuracy, and of Fernandes et al.'s Bayesian decomposition showing AI use raises everyone to a uniform high baseline overestimation. Lee et al. extends both to actual workflows and shows the pattern is bidirectional: domain expertise (self-confidence) protects, AI-confidence undermines.

- **The "task stewardship" framing.** The paper's signature qualitative contribution — that knowledge workers shift "from task execution to task stewardship" for Analysis, Synthesis, and Evaluation activities — is a useful naming for what `[[metacognitive-laziness]]` and `[[performance-paradox]]` are reaching toward. Stewardship is "guide and monitor AI to produce high-quality outputs" while "responsibility and accountability for the work still resides with the human user." The Discussion of [[bartos-ai-learning-meta-meta-2026]] cites Lee et al. 2025, but does not test task stewardship as a mediator. Its adjusted average learning estimate remains positive. The framing also crisply names what `[[professional-identity-threat]]` calls "editor not creator" at a different level of analysis.

The paper's design is a survey, not an RCT — correlations are not causation, and self-reports may conflate "less general effort" with "less critical thinking effort" (limitation explicitly noted in [p.15]). But for the KB's purposes (documenting prevalence patterns and validating lab-derived mechanisms in the wild), the survey methodology is appropriate and the analysis is rigorous (random-intercepts regressions with Benjamini–Hochberg correction across 98 hypothesised predictors).

## Supports

- [[metacognitive-laziness]] - related questions about regulation; task stewardship can include active monitoring and is not itself demonstrated metacognitive withdrawal.
- [[cognitive-offloading]] — survey-level prevalence: 72–79% of examples report reduced effort for Bloom-level activities, naming offloading at scale; the paper explicitly frames trust-in-AI-as-form-of-cognitive-offloading [p.13].
- [[confidence-competence-gap]] — the confidence pair (β = −0.69 confidence-in-AI vs. β = +0.26 confidence-in-self for enacting critical thinking) is field-scale empirical support for the gap mechanism documented in Shaw & Nave 2026, Fernandes 2026, Keshky 2026 at the lab level.
- [[performance-paradox]] — Lee et al.'s effort-vs-engagement dissociation ("less effort, less critical thinking, but the same or better task completion") is the survey-level signature of the paradox.
- [[capacity-erosion]] — the paper explicitly cites Bainbridge's *Ironies of Automation* and Simkute et al.'s *Ironies of Generative AI* [p.10], framing the trust-driven inhibition of critical thinking as the mechanism by which "cognitive abilities can deteriorate over time" if critical thinking is reserved for high-stakes tasks only.
- [[fluency-bias]] — supports the perceptual-mechanism story: workers with higher trust in GenAI report less effort across four of six Bloom activities, consistent with fluent AI output triggering reduced engagement.
- [[automation-bias]] — the trust-in-AI → less-effort, less-critical-thinking pattern is the survey-level signature of automation bias in knowledge work.
- [[professional-identity-threat]] — "stewardship" framing maps onto editor-not-creator: the worker retains accountability while delegating production.
- [[novice-vulnerability]] — qualitative finding that workers under-engage when "self-doubt in their ability to perform tasks independently" leads to default acceptance of AI output (e.g., legal-letter and grammar-check examples) [p.10].
- [[think-first]] — the paper's design recommendation to support "active and critical customisation and refining of AI-generated content" [p.13] is the protocol-level expression of think-first applied to AI workflows.
- [[strategic-alternation]] — the paper's warning that "without regular practice in common and/or low-stakes scenarios, cognitive abilities can deteriorate over time" [p.10] is the empirical motivation for strategic alternation as a counter-measure.

## Contradicts / Extends

- Related to [[fan-metacognitive-laziness-2025]]: Fan studied essay revision and task processes in an experiment; Lee studied self-reported thinking in workplace examples. They motivate further comparison, not proof of a shared causal mechanism.
- Extends [[shaw-cognitive-surrender-2026]] — Shaw reports 79.8% faulty-advice acceptance in Study 1 among AI-engaged faulty trials; Lee et al. provides the workflow-level prevalence: 55–79% effort reduction across Bloom activities, 83/319 citing trust-in-AI as the inhibitor of critical thinking. Same phenomenon, different measurement scale.
- Extends [[handa-economic-tasks-claude-2025]] — Handa shows *which* tasks are performed with AI (telemetry over Claude conversations); Lee et al. shows *how* knowledge workers report engaging cognitively *during* those tasks. Complementary: the activity layer (Handa) and the cognitive-engagement layer (Lee).
- Aligns with [[lee-relying-self-efficacy-2026]] — different Lee author (Eunhee H. Lee, USC Marshall) and different study design (preregistered experiment + survey on self-efficacy/ownership/meaning). Both Lee papers identify *mode-of-AI-use as the moderator*: passive copying (Lee 2026) / high-trust uncritical use (Lee 2025) undermines, while active collaboration / self-confident engaged use preserves. Verified non-duplicate at the triage stage.

## Open Questions

- The paper's confidence-thinking association is correlational and self-report-based. The authors explicitly note self-reports may conflate "reduced effort using GenAI" with "reduced effort doing critical thinking" [p.15]. A think-aloud or task-based assessment design would help disentangle these. Cited as a future-work direction by the authors.
- Sample skews younger and more tech-skilled (Prolific platform, weekly GenAI use minimum criterion). Older or less tech-oriented professionals may show different patterns. The English-only design also leaves cross-cultural and non-English-language workflows untested.
- The "task stewardship" framing is descriptive. What is the *threshold* of stewardship effort below which critical engagement collapses? The paper observes the shift but doesn't quantify the slope. KB's `[[strategic-alternation]]` and `[[think-first]]` would benefit from operational guidance grounded in stewardship-effort levels.
- The interaction between confidence-in-self and confidence-in-AI is not tested directly (no interaction term in the regression). The paper interprets each coefficient marginally, but a worker who is confident in both — or in neither — may behave differently. Cleaner experimental work could disentangle.
- Three motivator/inhibitor categories (awareness, motivation, ability) are presented as design-implication-ready. But the paper does not test interventions; the design implications are extrapolations. Empirical validation of awareness-targeted, motivation-targeted, and ability-targeted GenAI interventions remains future work.
