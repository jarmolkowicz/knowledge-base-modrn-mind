---
status: emerging
area: [erosion, preservation, risk]
type: paper
sources:
  - "Singh, A., Taneja, K., Guan, Z., & Ghosh, A. (2025). Protecting Human Cognition in the Age of AI. Tools for Thought workshop, CHI '25, Yokohama, Japan. arXiv:2502.12447v3 [cs.CY]."
---

# Singh et al. (2025) — Protecting Human Cognition in the Age of AI

## Citation

Singh, A., Taneja, K., Guan, Z., & Ghosh, A. (2025). Protecting Human Cognition in the Age of AI. *Tools for Thought workshop, CHI '25*, Yokohama, Japan. arXiv:2502.12447v3 [cs.CY].

(UT Austin + Georgia Tech + Hugging Face/UConn. Workshop position paper; v3 dated 29 Sep 2025.)

## Type

Paper — **non-empirical synthesis / position paper** (CHI '25 workshop). No new data; synthesizes ~76 works through two educational-psychology frameworks. Novice/student-focused.

## Key Insight

The paper's value to the KB is not new evidence — nearly every phenomenon it names the KB already holds from primary sources — but two **organizing lenses** that give a shared vocabulary for *why* cognitive offloading harms development and *how* to design against it.

1. **Bloom's-taxonomy bypass.** Learning requires climbing the cognitive-process ladder — remember → understand → apply → analyze → evaluate → create — and building metacognitive knowledge through that climb. GenAI delivers instantly synthesized factual/procedural knowledge that lets a novice *skip the middle rungs*, outsourcing exactly the operations (applying, analyzing, evaluating) whose practice builds metacognitive skill. This reframes [[cognitive-offloading]] and [[metacognitive-laziness]] as *ladder-skipping*, and explains why the harm concentrates in [[novice-vulnerability]]: novices lack the domain knowledge to prompt well or to notice what they skipped.

2. **Dewey's reflective-thinking prerequisites.** Dewey's *How We Think* names prerequisites for reflective thought — a state of doubt/perplexity, prior knowledge, active persistent consideration, suspended judgment plus tolerance for uncertainty, and connecting/evaluating ideas. GenAI disrupts each: immediate synthesized answers dissolve the productive doubt; belief-aligned, socially-desirable responses discourage engaging opposing views; confident, uncertainty-free output raises persuasiveness and suppresses suspended judgment; and coherent structure manufactures an *illusion of comprehensive understanding* over a superficial grasp ([[illusion-of-explanatory-depth]], [[coherence-trap]], [[fluency-bias]]). Section 4 then repurposes those same prerequisites as a diagnostic-and-design framework → [[reflective-inquiry-design]].

The paper is explicitly one-sided (it studies the hindering, not the augmenting, side) and preliminary; it is best used as a citable *framing* and a bridge from the KB's descriptive erosion concepts to educational design, not as evidence.

## Key Passages

> "This paper synthesizes existing literature on GenAI's effects on different aspects of human cognition. Drawing on Krathwohl's revised Bloom's Taxonomy and Dewey's conceptualization of reflective thought, we examine the mechanisms through which GenAI is affecting the development of different cognitive abilities."
> — Singh et al. 2025, [p.1] (Abstract)

> "when using LLMs in a similar scenario, they may miss opportunities to develop and practice these essential cognitive skills—particularly remembering, applying, analyzing, and, sometimes, evaluating—by outsourcing them to LLMs. This, in turn, impedes the development of metacognitive skills, which are acquired through regular practice and assessment of different cognitive processes."
> — Singh et al. 2025, [p.3] (Bloom's Revised Taxonomy)

> "the structured and coherent nature of synthesized AI responses can create an illusion of comprehensive understanding, when in reality, people may only achieve a superficial grasp of the underlying topic or concept."
> — Singh et al. 2025, [p.3] (Dewey's Theory of Reflective Thinking)

> "We propose using Dewey's prerequisites for reflective thinking as a framework for both: (i) identifying passive AI use based on unmet prerequisites of reflective thinking in human-AI interactions, and (ii) designing interventions to foster critical thinking."
> — Singh et al. 2025, [p.4] (Supporting Thinking & Learning)

> "in the early stages of learning, AI use should be minimal, primarily serving functions such as providing formative feedback. This can be implemented using guardrails in educational AI tools that facilitate a gradual increase in learner-AI interactions, ensuring that learners have the ability to exercise independent judgment when they seek AI assistance."
> — Singh et al. 2025, [p.4] (Implications for Educators and Test Designers)

## Key Findings

This is a synthesis, so "findings" are organizing claims rather than data:

- **The two-dimensional Bloom's argument** [p.3]: GenAI accelerates access to factual/procedural knowledge but "may bypass important cognitive processes that typically occur during slower, deliberate learning." The bypassed operations (remember/apply/analyze/evaluate) are the ones that build metacognitive knowledge, so their outsourcing "impedes the development of metacognitive skills."
- **Difficulty is the trigger for analytical reasoning** [p.3]: "Experiences of cognitive difficulty prompt more analytical reasoning … Overreliance on GenAI can reduce such cognitive difficulty, which can reduce the activation of deeper metacognitive processes." (The mechanism behind [[desirable-difficulty]] and [[cognitive-grit]].)
- **Novice > expert vulnerability** [p.3]: novices are more susceptible to metacognitive laziness; experts, with structured domain knowledge, can prompt effectively and use AI to offload *lower-level* tasks — but even experts risk losing the deliberate practice that sustains expertise.
- **Dewey disruption map** [p.3]: five reflective-thinking prerequisites, each undermined by a specific GenAI property (immediacy, belief-alignment/social-desirability bias, confident uncertainty-free output, shallow processing of explanations, coherent-structure illusion).
- **Design implications** [p.4]: teach and *test* critical/evaluative skills (current curricula reward the formulaic skills AI already does well); make critiquing AI outputs a learning activity; keep early-learning AI minimal via staged guardrails (productive struggle / productive failure / cognitive endurance); inject friction; use schema/knowledge-graph tools; use metacognitive prompts and AI "provocations."
- **Scope caveat** [p.4]: "Much of the current research on AI's cognitive impacts relies on short-term studies … a pressing need for long-term studies on how sustained AI use affects cognitive development, particularly for younger users."

## Relevance

Dead-center on the KB's erosion/preservation mission, but a **secondary** source. Its contribution is threefold:

1. **A vocabulary bridge.** Bloom's-ladder-bypass and Dewey-prerequisite-disruption are compact ways to explain the KB's scattered erosion concepts to educators — useful "at 7am before a client meeting" framing.
2. **The anchor for a new method.** Section 4's repurposing of Dewey's prerequisites into a diagnostic + design framework is the KB's new `[[reflective-inquiry-design]]` method.
3. **A novice-focused consolidation.** It ties the novice-vulnerability thread to concrete educational-design levers (staged guardrails, friction, metacognitive prompts) already echoed by `[[bastani-guardrails-math-rct-2025]]` and `[[passalacqua-less-ai-2024]]`.

## Supports

- [[cognitive-offloading]] — reframed as skipping the Bloom's cognitive-process ladder
- [[metacognitive-laziness]] — the paper cites Fan et al.; Bloom's ladder-skip is the proposed mechanism → [[fan-metacognitive-laziness-2025]]
- [[novice-vulnerability]] — the paper's central population; novices skip rungs they can't yet see
- [[metacognition]] — metacognitive-knowledge development is what ladder-skipping impedes
- [[desirable-difficulty]] / [[cognitive-grit]] — "cognitive difficulty prompts analytical reasoning"; GenAI removes the productive struggle
- [[cognitive-friction]] — the paper's proposed "friction in human-AI interaction" intervention
- [[illusion-of-explanatory-depth]] / [[coherence-trap]] / [[fluency-bias]] — the "illusion of comprehensive understanding" from coherent AI output
- [[reflective-inquiry-design]] — the method this source anchors
- [[think-first]] / [[socratic-partnership]] — individual-practice cousins of the paper's educator-level design levers
- [[lee-critical-thinking-survey-2025]] / [[bastani-guardrails-math-rct-2025]] / [[passalacqua-less-ai-2024]] / [[he-illusion-competence-2023]] — primary sources the paper synthesizes

## Contradicts / Extends

- Extends [[fan-metacognitive-laziness-2025]] with a proposed Bloom's-taxonomy interpretation and design response. Fan's task-process evidence does not itself validate that explanation or intervention.
- Related to [[bastani-guardrails-math-rct-2025]] and [[passalacqua-less-ai-2024]]: specific designs motivate questions about preserving learning. Bastani tested a combined Tutor package with no detectable same-session exam difference from control, not a general staged-guardrail intervention or durable protection.
- No contradictions. As a synthesis it echoes rather than challenges existing sources; its one distinctive move is the framework overlay, not a disputed empirical claim.

## Open Questions

- The Bloom's-bypass and Dewey-disruption accounts are argued, not tested. [Inference] Whether interventions built on Dewey's prerequisites actually preserve reflective thinking is an open empirical question the paper itself flags.
- The novice/expert boundary is treated as categorical; where along a learning trajectory AI should shift from "minimal" to "collaborative" is unspecified (a [[zone-of-proximal-development]] calibration question).
- The paper is one-sided by design (harm-focused). It does not weigh cases where GenAI *aids* reflective thinking (e.g., Socratic prompting), leaving the net effect underspecified.
