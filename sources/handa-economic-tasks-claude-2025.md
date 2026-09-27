---
status: solid
area: [risk, erosion, preservation]
type: paper
sources:
  - "Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Heck, S., Mueller, J., Hong, J., Ritchie, S., Belonax, T., Troy, K. K., Amodei, D., Kaplan, J., Clark, J., & Ganguli, D. (2025). Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations. arXiv:2503.04761 [cs.CY], February 11, 2025. Anthropic."
---

# Handa et al. (2025) — Which Economic Tasks are Performed with AI?

## Citation

Handa, K., Tamkin, A., McCain, M., Huang, S., Durmus, E., Heck, S., Mueller, J., Hong, J., Ritchie, S., Belonax, T., Troy, K. K., Amodei, D., Kaplan, J., Clark, J., & Ganguli, D. (2025). *Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations.* arXiv:2503.04761 [cs.CY], February 11, 2025. Anthropic. Public dataset: https://huggingface.co/datasets/Anthropic/EconomicIndex/

## Type

Paper (large-scale observational analysis: ~4M Claude.ai Free and Pro conversations from December 2024 – January 2025, classified via Clio and mapped to U.S. Department of Labor O*NET tasks, occupations, skills, wage bands, and Job Zones).

## Key Insight

Handa et al. provide a production-data account of which economic tasks are actually being performed with AI, against which forecasts and surveys can be tested. The study reports three main patterns. First, sampled conversations map to particular tasks rather than establishing occupation-wide adoption: ~36% of occupations show AI usage in at least 25% of their tasks but only ~4% see usage across 75% of tasks — meaning current AI is integrating selectively into specific tasks without establishing occupation-wide automation. Second, usage peaks in the upper-middle wage quartile (Computer Programmers, Web Developers) and falls off at both extremes — both the lowest-wage and highest-wage occupations show low usage, suggesting non-technical-feasibility factors (regulatory barriers, organizational readiness, physical-manipulation requirements) shape adoption. Third, the augmentation/automation split is roughly 57/43 in favor of augmentative patterns (Task Iteration, Learning, Validation), with automative patterns (Directive, Feedback Loop) the minority — this describes classified patterns in the sample, not evidence for the benefits of partial automation.

## Key Passages

> "Our analysis reveals that AI usage primarily concentrates in software development and writing tasks, which together account for nearly half of all total usage. However, usage of AI extends more broadly across the economy, with ∼ 36% of occupations using AI for at least a quarter of their associated tasks. We also analyze how AI is being used for tasks, finding 57% of usage suggests augmentation of human capabilities (e.g., learning or iterating on an output) while 43% suggests automation (e.g., fulfilling a request with minimal human involvement)."
> — Handa et al., [p.1] (Abstract)

> "Only ∼ 4% of occupations exhibit AI usage for at least 75% of their tasks, suggesting the potential for deep task-level use in some roles. More broadly, ∼ 36% of occupations show usage in at least 25% of their tasks, indicating that AI has already begun to diffuse into task portfolios across a substantial portion of the workforce."
> — Handa et al., [p.2]

> "Cognitive skills like Reading Comprehension, Writing, and Critical Thinking show high presence, while physical skills (e.g., Installation, Equipment Maintenance) and managerial skills (e.g., Negotiation) show minimal presence—reflecting clear patterns of human complementarity with current AI capabilities."
> — Handa et al., [p.2]

> "We find that AI use peaks in the upper quartile of wages but drops off at both extremes of the wage spectrum. Most high-usage occupations clustered in the upper quartile correspond predominantly to software industry positions, while both very high-wage occupations (e.g., physicians) and low-wage positions (e.g., restaurant workers) demonstrate relatively low usage. This pattern likely reflects either limitations in current AI capabilities, the inherent physical manipulation requirements of these roles, or both."
> — Handa et al., [p.3]

> "We find that 57% of interactions show augmentative patterns (e.g., back-and-forth iteration on a task) while 43% demonstrate automation-focused usage (e.g., performing the task directly). While this ratio varies across occupations, most occupations exhibited a mix of automation and augmentation across tasks, suggesting AI serves as both an efficiency tool and collaborative partner."
> — Handa et al., [p.3]

> "This distribution suggests that while AI could be touching many occupations today, deep integration across most tasks within any given occupation remains rare for now. Rather than completely automating entire job roles, present-day AI appears to be primarily used for specific tasks within occupations."
> — Handa et al., [p.7]

> "It is worth noting that the occupational classification of a conversation does not necessarily mean the user was a professional in that field. For instance, while some nutrition-related queries might come from dietitians, others likely come from individuals seeking personal dietary advice. This widespread access to AI assistance for traditionally professional tasks—even if the assistance is not perfect—could have significant implications for these fields, though analyzing such impacts lies outside the scope of this study."
> — Handa et al., [p.5]

> "Webb [2019] predicted highest AI exposure in occupations around the 90th wage percentile, while we find peak usage in mid-to-high wage occupations, with notably lower usage at both extremes of the wage distribution. This pattern suggests that factors beyond technical feasibility—such as implementation costs, regulatory barriers, and organizational readiness—may be tempering adoption in the highest-wage sectors."
> — Handa et al., [p.12]

## Key Findings

**Task and occupation concentration ([p.5–7]):**
- Computer and Mathematical occupations: 37.2% of all queries (highest category)
- Arts, Design, Entertainment, Sports, and Media: 10.3% (second; reflects writing, marketing, content generation)
- Education and business-relevant occupations also highly represented
- Lowest: Transportation and Material Moving; Healthcare Support; Farming, Fishing, Forestry — physical-labor occupations

**Depth of usage ([p.7]):**
- ~4% of occupations: AI usage in ≥75% of tasks
- ~11% of occupations: ≥50% of tasks
- ~36% of occupations: ≥25% of tasks
- Privacy threshold: tasks counted only if ≥15 conversations across ≥5 unique accounts

**Skills ([p.7–8]):**
- Highest presence: Critical Thinking, Reading Comprehension, Programming, Writing, Active Listening (last reflects Claude's default conversational behaviors, not user intent)
- Lowest: Installation, Equipment Maintenance, Repairing, Negotiation

**Wage and barrier-to-entry ([p.8–9]):**
- Peak: upper quartile of wages (Computer Programmers, Web Developers)
- Drop-off at extremes: low-wage (waiters) and very-high-wage (anesthesiologists, gynecologists) both low
- Peak Job Zone: Zone 4 (Considerable Preparation Needed, typically bachelor's degree)
- Drop at Zone 5 (Extensive Preparation Needed, advanced degrees) — physical manipulation and regulatory barriers likely explain the highest-wage drop-off

**Augmentation vs. automation ([p.9–10]):**
- Augmentative (57%): Task Iteration, Learning, Validation
- Automative (43%): Directive (complete task delegation), Feedback Loop (environment-guided execution)
- Directive conversations dominate writing and content generation
- Feedback Loop conversations dominate coding and debugging
- Task Iteration: front-end development, professional communication
- Learning: general education, advice-seeking
- Validation (smallest): largely concentrated in language translation tasks
- [p.9] caveat: "users might edit and adjust the response they receive from Claude outside the chat window, suggesting that the true proportion of augmentative conversations may be even higher"

**Comparison with predictions ([p.12–13]):**
- Eloundou et al. (2023) predicted 80% of U.S. workers could have ≥10% of tasks affected; Handa et al. find mapped conversations for ≥10% of tasks in ~57% of occupations; this differs from a forecast about percentages of workers
- Webb (2019) predicted peak exposure at the 90th wage percentile; Handa et al. find peak usage at mid-to-high wages with falloff at both extremes
- Predicted high usage in healthcare has not yet materialized; observed higher usage in scientific applications than predicted

**Model usage patterns ([p.11]):**
- Claude 3 Opus: more usage for creative writing, educational content, academic research
- Claude 3.5 Sonnet (new): more usage for coding and software development
- Suggests model capability shifts can drive task-distribution shifts at sector scale

## Relevance

The study maps about four million Claude.ai Free and Pro conversations to occupational tasks. It provides a large descriptive sample, but neither observes whether users work in those occupations nor establishes whether outputs enter real work.

The 57% augmentation / 43% automation split concerns conversation labels. It does not measure retained skill, job loss, worker identity, beneficial task allocation or strict human–AI synergy.

[Inference] Frequently represented tasks may be useful places to investigate [[execution-commoditization]] and [[novice-vulnerability]]. The study does not establish either outcome.

## Supports

- [[partial-automation-principle]] — production-scale evidence that the partial-automation pattern is the dominant emergent practice (57% augmentative) rather than only a normative recommendation
- [[human-ai-complementarity]] — empirical anchor for the asymmetry argument: cognitive skills (Critical Thinking, Reading Comprehension, Writing) dominate AI conversations while physical/managerial skills are minimal, indicating where human complementarity actually resides at scale
- [[execution-commoditization]] — describes which task categories appear frequently in this Claude sample, not measured commoditization (software, writing, analytical work) and which currently do not (physical labor, high-barrier specialty medicine)
- [[novice-vulnerability]] — [Inference] motivates questions about junior learning in frequently represented task categories (software development at 37.2% of all queries; writing dominant in Directive/Task-Iteration patterns)
- [[professional-identity-threat]] — supplies the breadth dimension to identity-threat claims: ~36% of occupations see AI usage in ≥25% of their tasks, raising questions about which work contexts merit study; identity effects were not measured
- [[situational-disempowerment]] — methodologically aligned (same Clio family, same Anthropic team) but turned outward at the task economy; Handa's task and occupation distributions do not provide a shared denominator for Sharma et al.'s separate sample
- [[performance-paradox]] — observation that Directive (full-delegation) conversations dominate writing/content-generation tasks and that Feedback-Loop conversations dominate coding/debugging gives a population view of where the paradox is most likely to operate at scale
- [[jagged-frontier]] — usage map, not a direct capability test of the frontier: peak usage in software/writing, drop-off in physical and high-credential specialties

## Contradicts / Extends

- Extends: Eloundou et al. (2023) — empirical follow-up to their "80% of workers, ≥10% of tasks" forecast; Handa et al. find ~57% of occupations using AI for ≥10% of tasks (not directly comparable because workers and occupations are different denominators)
- Extends: Webb (2019) — peak-exposure prediction at 90th wage percentile is partially confirmed but with falloff at the extremes that Webb did not predict
- Extends: [[sharma-disempowerment-patterns-2026]] — methodologically parallel (Clio at production scale) but addresses the distinct question of task economics rather than disempowerment patterns; together they form the production-data layer of the KB

## Open Questions

- The 57/43 augmentation/automation split derives from conversation-level classification; the paper acknowledges users may iterate outside the chat window, which would inflate the true augmentation share. Unobserved editing could change the split; the classification is not a validated measure of all downstream work.
- Sample is Claude.ai Free and Pro only — excludes Team, Enterprise, and API customers, which likely have different task profiles. Generalization to "all AI usage" is bounded.
- Conversation classification cannot disambiguate whether the user was a professional in the mapped occupation or a layperson; the paper flags this explicitly. The "what people use AI for" finding is conflated with "what tasks AI is asked to do."
- The paper does not measure whether AI outputs are incorporated into work product (no workflow context). Usage patterns ≠ adoption-into-work patterns.
- Cross-provider generalization is unknown; ChatGPT, Gemini, Copilot, and others likely show different distributions.
- The paper does not itself assess whether observed usage patterns are *good* for users — that is the question Sharma et al. (2026) take up at the same Clio-pipeline level.
