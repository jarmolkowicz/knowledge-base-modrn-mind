---
status: solid
area: [risk, preservation]
type: paper
sources:
  - "Tankelevitch, L., Kewenig, V., Simkute, A., Scott, A. E., Sarkar, A., Sellen, A., & Rintel, S. (2024). The Metacognitive Demands and Opportunities of Generative AI. CHI '24. doi:10.1145/3613904.3642902 (also arXiv:2312.10893, December 2023)"
---

# Tankelevitch et al. (2024; 2023 preprint) — The [[metacognitive-demand|Metacognitive Demand]]s of Generative AI

## Citation

Tankelevitch, L., Kewenig, V., Simkute, A., Scott, A. E., Sarkar, A., Sellen, A., & Rintel, S. (2024). The Metacognitive Demands and Opportunities of Generative AI. *Proceedings of the CHI Conference on Human Factors in Computing Systems* (CHI '24). **Best Paper Award.**

**arXiv (preprint, Dec 2023):** [arXiv:2312.10893](https://arxiv.org/abs/2312.10893)
**DOI:** [10.1145/3613904.3642902](https://doi.org/10.1145/3613904.3642902)

## Type

Paper (theoretical / synthesis; Microsoft Research + UCL + Edinburgh)

## Key Insight

Tankelevitch et al. argue that GenAI's usability problems aren't fragmented (prompting issues + evaluation issues + workflow integration issues). They share a single underlying cause: **GenAI imposes high metacognitive demands** — demands on the user's ability to monitor and control their own thinking — that current systems offer little support for handling.

The argument is structured around **three loci** where metacognitive demand concentrates:

1. **Prompting** — requires self-awareness of task goals (what am I really trying to accomplish?), task decomposition (what sub-tasks does this break into?), and well-adjusted confidence in one's prompting strategy.
2. **Evaluating and relying on outputs** — requires well-adjusted confidence in evaluating output quality (do I actually know whether this is right?) and metacognitive flexibility (can I shift evaluation criteria as the task reveals itself?).
3. **Automation strategy** — the higher-level question of *whether and how* to integrate GenAI into a workflow at all. Requires self-awareness of GenAI's applicability to one's work, well-adjusted confidence in manual vs. AI-supported completion, and metacognitive flexibility to adapt the workflow.

The paper's organizing analogy: **working with GenAI is like managing a team**. A manager needs to formulate goals, decompose them into delegable tasks, evaluate output, and adjust plans — all of which are metacognitive operations.

The paper proposes two complementary intervention paths:

- **Improve users' metacognition** via metacognitive support strategies integrated into GenAI systems (planning prompts, self-evaluation scaffolds, self-management aids).
- **Reduce metacognitive demand** via task-appropriate explainability and customizability (offload metacognitive processing from user to system).

The metacognitive framework draws from Flavell, Nelson & Narens, and others. They use a four-cell model: metacognitive **knowledge / experiences** (sources of information about one's own cognition) crossed with **monitoring / control** (abilities to assess and guide one's cognition). The four monitoring/control abilities most relevant for GenAI: **self-awareness, well-adjusted confidence, metacognitive flexibility, task decomposition**.

For human thinking with AI: this is the load-bearing theoretical paper for the KB's intersection with metacognition. It argues that GenAI is *not* primarily a content-generation problem or a hallucination-management problem — it's a **metacognitive overload problem**. The user is being asked to do far more meta-level work (monitor, evaluate, recalibrate) than legacy tools required, with little system-side support. The KB's preservation cluster is in essence a metacognitive-support project.

## Key Passages

> "Firstly, we suggest that current GenAI systems impose multiple metacognitive demands on users; understanding these demands can help interpret and probe the identified and potentially novel usability challenges."
> — Tankelevitch et al., [pp.1–2] (introduction)

> "The metacognitive demands of working with GenAI systems parallel those of a manager delegating tasks to a team."
> — Tankelevitch et al., [p.2]

> "Current GenAI systems often require verbalized prompting, demanding self-awareness of task goals, and decomposition of tasks into sub-tasks. System outputs then need to be evaluated, requiring well-adjusted confidence in one's evaluation and prompting abilities, and metacognitive flexibility to iterate on the prompting strategy as necessary."
> — Tankelevitch et al., [p.2]

> "Alongside the local interactions with GenAI systems, the generality of GenAI poses another, higher-level metacognitive demand: the challenge of knowing whether and how to incorporate GenAI into workflows—i.e., one's 'automation strategy'."
> — Tankelevitch et al., [p.2]

> "Confidence is one's self-assessment of one's cognitive abilities and their application to tasks… A 'well-adjusted' confidence distinguishes objectively correct and incorrect performance, and accurately matches one's abilities."
> — Tankelevitch et al., [p.3]

> "These demands can be addressed in at least two complementary ways. Firstly, given that metacognitive abilities can be taught, we can improve users' metacognition via metacognitive support strategies… Secondly, we can reduce the metacognitive demand of GenAI systems by designing task-appropriate approaches to GenAI explainability and customizability."
> — Tankelevitch et al., [p.2]

## Relevance

The most KB-aligned theoretical paper to date — directly identifies metacognition as the lens for understanding why GenAI is hard to use well. Three contributions:

- **Diagnostic framework.** The three loci (prompting, evaluation, automation strategy) plus the four abilities (self-awareness, confidence calibration, flexibility, decomposition) give the KB a structured way to map specific AI-use problems to specific metacognitive failures. Many KB concepts ([[fluency-bias]], [[automation-bias]], [[confidence-competence-gap]], [[artificial-certainty]]) can be re-categorized as failure modes of well-adjusted confidence.
- **Bridge from cognitive science to interaction design.** The paper sits between the KB's metacognition cluster (rooted in Flavell 1979) and applied AI methods (rooted in [[scan]], [[think-first]], [[calibration]]). Provides the explicit theoretical scaffolding linking the two.
- **Two-direction intervention space.** "Improve user's metacognition" and "reduce system's metacognitive demand" are non-redundant levers. The KB's preservation cluster is largely the first; the design-side interventions Tankelevitch et al. propose (explainability, customizability, calibration prompts) are the second. Both can be pursued; neither is sufficient alone.

## Supports

- [[metacognition]] — applies Flavell's framework directly to GenAI
- [[flavell-metacognition-1979]] — extends Flavell's developmental framework into the GenAI domain
- [[calibration]] — well-adjusted confidence is the metacognitive ability the KB calls calibration
- [[think-first]] — task decomposition before AI delegation = think-first as a metacognitive practice
- [[scan]] — [[tsim-gutoreva-scan-2025]] operationalizes the "automation strategy" decision with an explicit framework
- [[automation-bias]] — Tankelevitch's "well-adjusted confidence in evaluation" is the inverse of automation bias
- [[fluency-bias]] — fluency overrides metacognitive monitoring; this paper's framework names exactly that
- [[confidence-competence-gap]] — Tankelevitch's confidence-calibration framework provides the mechanism
- [[artificial-certainty]] — failure mode of confidence calibration when AI outputs feel definitive

## Contradicts / Extends

- Companion to [[tsim-gutoreva-scan-2025]] — both papers address the "automation strategy" question; Tankelevitch frames it as a metacognitive demand, Tsim & Gutoreva propose the SCAN framework as a tool for managing it. Read together.
- Extends [[flavell-metacognition-1979]] — Flavell named metacognition as a developmental construct; Tankelevitch et al. show it as the central construct for GenAI usability.
- Extends [[risko-gilbert-cognitive-offloading-2016]] — Risko & Gilbert show metacognitive evaluation drives offloading decisions; Tankelevitch et al. extend the same mechanism into the GenAI context with explicit demand categories.

## Open Questions

- The paper's intervention space (improve user's metacognition + reduce system's demand) is balanced. But the *political economy* of GenAI design pushes toward reducing apparent demand at the cost of preserving genuine demand — i.e., systems become more frictionless, which hides metacognitive demands rather than supporting them. How do you build interventions that resist this gradient?
- Metacognitive ability is heterogeneously distributed in the population. Does GenAI widen the gap between high-metacognition users (who benefit) and low-metacognition users (who get harmed)? The paper acknowledges this implicitly but doesn't quantify.
- The four abilities (self-awareness, confidence calibration, flexibility, decomposition) are presented as separable. Empirically, are they? Or is one of them upstream — is decomposition the prerequisite for everything else?
