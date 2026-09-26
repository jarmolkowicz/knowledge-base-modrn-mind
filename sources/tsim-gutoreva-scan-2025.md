---
status: emerging
area: [erosion, preservation]
type: paper
sources:
  - "Tsim, F., & Gutoreva, A. (2025). SCAN: A Decision-Making Framework for Task Assignment with Generative AI. Preprint, December 2025."
---

# Tsim & Gutoreva (2025) — SCAN Framework

## Citation

Tsim, F., & Gutoreva, A. (2025). *SCAN: A Decision-Making Framework for Task Assignment with Generative AI*. Preprint, December 22, 2025.

**Status:** Preprint, not yet publicly indexed; verified from local PDF.

## Type

Paper (framework proposal)

## Key Insight

Tsim & Gutoreva extend Vygotsky's **[[zone-of-proximal-development|Zone of Proximal Development]] (ZPD)** by adding a fourth zone: **"known to GenAI."** The intersection of the learner's three knowledge zones (known / unknown / overlapping/ZPD) with this new "known to GenAI" zone yields four task sub-zones the framework is named for:

- **S — Substitute** (unknown to learner ∩ known to AI). Learner has no task-specific knowledge. GenAI completes the task. Mode: **automation**. Highest risk of cognitive offloading and automation bias.
- **C — Complement** (known to learner ∩ known to AI). Learner has task-specific knowledge; GenAI also has general knowledge. Mode: **collaboration**. Learner supervises and monitors GenAI output; sycophancy risk lowest because the learner can challenge.
- **A — Aid** (ZPD overlap ∩ known to AI). Learner has partial knowledge; GenAI assists scaffolding. Mode: **augmentation**.
- **N — Non-negotiable** (ZPD overlap ∩ NOT known to AI). Learner has partial knowledge but the task isn't in AI's competence — needs human-only or other-human assistance.

The conceptual move: the three modes everyone discusses (automation / augmentation / collaboration) aren't separate categories but a **continuum defined by the learner's task-specific knowledge** at a given moment. As knowledge develops, the same task can shift through sub-zones — Substitute → Aid → Complement is the **upskilling trajectory**; the reverse (Complement → Aid) is the **deskilling trajectory**.

The framework also operationalizes **metacognition** as a three-component cycle (real-time evaluation, post-task reflection, learning-into-future-tasks), borrowed from Bergamaschi Ganapini et al. (2025). The cycle is what determines whether a task moves toward Complement (upskilling) or away (deskilling).

For human thinking with AI: SCAN is the first KB-aligned attempt at a *task-level* decision rule for when to use AI vs. when to keep cognition unaided. Existing KB methods like [[strategic-alternation]] and [[think-first]] gesture at the same intuition but operate at session/practice level. SCAN's contribution is a per-task four-way classification with explicit risk flags per zone.

## Key Passages

> "We propose adding a new zone called 'known to GenAI', constructing the foundation of the SCAN framework. This small addition extends the social learning aspect of ZPD by indicating where GenAI plays a role in the Human-GenAI interaction."
> — Tsim & Gutoreva, [p.4]

> "SCAN shows that achieving [human-AI] collaboration can be task dependent, and proposes that such dependency is largely attributed to whether a learner has task specific knowledge beforehand."
> — Tsim & Gutoreva, [p.10]

> "Tasks completion at the Complement are the least prone to both cognitive offloading and sycophancy, as learner's task specific knowledge, with her metacognition, mitigates them to a large extent, via monitoring, and challenging GenAI's output via counterarguments."
> — Tsim & Gutoreva, [p.5]

> "We distinguish collaboration and augmentation from automation by locus of control and epistemic responsibility rather than by tool sophistication. … Substitute is the sub-zone that tempts automation; Aid instantiates augmentation; and Complement promotes collaboration."
> — Tsim & Gutoreva, [p.5]

> "Upskilling proceeds by deliberately shifting, with a learner's metacognitive ability, recurrent tasks from Substitute to Aid to Complement via spaced practice and reflective comparison of human vs. AI rationales… deskilling occurs when tasks identification changes from Complement to Aid, due to a shift of user's role from production to evaluation."
> — Tsim & Gutoreva, [p.5]

## Methodology

Theoretical paper. Foundations:

- **Vygotsky's ZPD (1978):** three zones — known / ZPD / unknown to learner.
- **Flavell's Metacognition (1979):** monitoring + reflection + learning.
- **New zone:** "known to GenAI" (Tsim & Gutoreva's contribution).
- **Two application scenarios** worked out: workplace knowledge workers (already-domain-knowledgeable) and students (still accumulating).

No empirical validation in this paper; SCAN is proposed as a decision-making tool, not an empirical claim.

## Relevance

Three load-bearing contributions for the KB:

- **Operational specificity for AI use decisions.** [[strategic-alternation]] tells a practitioner *to* alternate; SCAN tells them *which task right now* fits which mode. Concretely actionable.
- **Mechanism for the [[upskilling-deskilling-paradox]].** SCAN proposes that the same task can sit in Substitute, Aid, or Complement depending on the user's evolving knowledge — which means upskilling and deskilling aren't separate phenomena but trajectories within the same framework.
- **Integration with sycophancy and cognitive offloading risk.** The framework predicts where each risk peaks (Substitute > Aid > Complement). This is a testable claim and aligns with [[batista-sycophantic-ai-2026]] and [[bo-sycophancy-novices-2026]] findings that sycophancy is most damaging when users lack ground-truth knowledge.

The "Non-negotiable" zone (ZPD ∩ not-known-to-AI) is the most underdeveloped part of the framework — it names a bucket but doesn't specify what tasks live there. This is where domain-specific judgment sits and where AI substitution most clearly shouldn't apply.

## Supports

- [[scan]] — primary source for the SCAN method
- [[strategic-alternation]] — SCAN provides task-level decision rules complementing strategic-alternation's session-level rules
- [[cognitive-offloading]] — framework predicts where offloading risk concentrates (Substitute zone)
- [[metacognition]] — operationalized as a three-component evaluation cycle
- [[upskilling-deskilling-paradox]] — explained as trajectories within the four-zone framework
- [[automation-bias]] — risk peaks in Substitute zone
- [[batista-sycophantic-ai-2026]] — sycophancy risk varies by sub-zone in a way consistent with Batista's findings
- [[think-first]] — calibration step before delegating to GenAI

## Contradicts / Extends

- Extends Mollick's three-task framework ("Just Me / Delegated / Automated") by adding the metacognitive trajectory dimension and the four-sub-zone structure rooted in ZPD.
- Extends Gonzalez et al. (2026, *Nature Reviews Psychology*) and Hemmer et al. (2025) — those papers report [[human-ai-complementarity|human-AI complementarity]] is rarely observed empirically; SCAN proposes a structural explanation (complementarity requires the Complement zone, which requires task-specific human knowledge that's often absent). Note: Gonzalez 2026 is mentioned but not a KB workbench entry (paywalled, not currently verifiable).
- Extends [[dellacqua-jagged-frontier-2023]] — the "[[jagged-frontier|jagged frontier]]" can be partly explained as the boundary where Substitute meets Non-negotiable in a domain.

## Open Questions

- The Non-negotiable zone is named but underspecified. Which tasks belong there, and what makes a task fall outside AI's competence beyond just "current model limits"?
- SCAN is theoretical; no empirical test of whether self-classified zone (which the framework requires) tracks actual cognitive offloading or sycophancy outcomes.
- The framework assumes a learner can accurately self-assess task-specific knowledge. The metacognitive overconfidence findings ([[hu-metamemory-offloading-2019]], Risko & Gilbert 2016) suggest this assumption is fragile — users may misclassify tasks as Complement when they're actually Substitute.
- How does SCAN apply to teams or organizations rather than individual learners? The framework is single-agent.
