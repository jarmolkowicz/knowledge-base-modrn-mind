---
status: solid
area: [preservation]
type: paper
sources:
  - "Gentner, D., & Markman, A. B. (1997). Structure mapping in analogy and similarity. American Psychologist, 52(1), 45–56. doi:10.1037/0003-066X.52.1.45"
---

# Gentner & Markman (1997) — Structure Mapping in Analogy

## Citation

Gentner, D., & Markman, A. B. (1997). Structure mapping in analogy and similarity. *American Psychologist*, 52(1), 45–56.

**DOI:** [10.1037/0003-066X.52.1.45](https://doi.org/10.1037/0003-066X.52.1.45)

## Type

Paper (theoretical synthesis)

## Key Insight

Gentner and Markman argue that analogy and similarity are **the same process operating over different proportions of relational vs. attribute matches** — both involve **structural alignment and mapping** between mental representations. The slogan is "similarity is like analogy."

Three psychological constraints define the process:

1. **Structural consistency** — matching relations must have matching arguments (parallel connectivity), and each element matches at most one element in the other representation (one-to-one correspondence).
2. **Relational focus** — common *relations* drive the analogy; common *objects* don't. Kepler's planets ↔ boatman analogy holds because relations between planet and motive force mirror relations between boat and current — even though planets and boats look nothing alike.
3. **Systematicity** — the comparison process favors *connected systems* of relations (with higher-order constraining relations) over equal numbers of unconnected relations. This is what lets analogies generate inferences: once a system aligns, further statements connected to it in the base domain can be projected as candidate inferences in the target.

The classic illustration is **cross-mapping**: in `1:3 :: 3:9`, the surface-identical 3s get *separated* to preserve relational structure (the 1↔3 and 3↔9 mappings preserve the ratio). Surface similarity is overridden by relational structure when the two conflict — and this is what genuine analogy looks like.

[Inference] For AI-assisted reasoning, structural alignment is a useful question to ask of an analogy: do the relationships match, or only the objects? The paper does not assess modern LLM capabilities, compare humans with those models, or test whether using AI changes human reasoning ability.

## Key Passages

Paraphrase: The authors challenge the separation of sophisticated analogy from simple perceptual similarity, proposing shared comparison processes. [p.1]

> "Common relations are essential to analogy; common objects are not. This promoting of relations over objects makes analogy a useful cognitive device, for physical objects are normally highly salient in human processing — easy to focus on, recognize, encode, retrieve, and so on."
> — Gentner & Markman, [p.2]

> "The systematicity principle captures a tacit preference for coherence and causal predictive power in analogical processing. We are not much interested in analogies that capture a series of coincidences, even if there are a great many of them."
> — Gentner & Markman, [p.3]

Paraphrase: In cross-mapping, similar objects occupy different relational roles. For 1:3 :: 3:9, mapping the two identical 3s would break the ratio relationship. [p.3]

> "These candidate inferences are only guesses: Their factual correctness must be checked separately. … Any process capable of producing novel true inferences is also capable of generating false inferences."
> — Gentner & Markman, [p.3]

## Relevance

The theory offers a vocabulary for examining an analogy:

- **Relations versus attributes.** Analogy and similarity share alignment processes; they can differ in the proportions of relational and attribute matches.
- **Candidate inferences.** Alignment can suggest a new claim about a target situation. The claim must then be checked; structure does not guarantee truth.
- **Cross-mapping.** Identical-looking objects may occupy different roles. The familiar ratio example illustrates why matching objects solely by appearance can fail.

[Inference] These distinctions can guide questions about AI-generated analogies. Whether particular models or users succeed is a separate empirical question, not answered by the 1997 paper.

## Supports

- [[analogical-reasoning]] - primary theoretical account
- [[metacognition]] - [Inference] checking how a comparison was formed
- [[think-first]] - a possible practice application, not an intervention tested here
- [[fluency-bias]] - distinct judgment construct; fluency does not establish a valid analogy
- [[judgment]] - [Inference] examining analogies used in novel decisions

## Contradicts / Extends

- The account connects human analogy research with computational structure-mapping models; it is not a modern LLM benchmark.
- [[bjork-desirable-difficulties-2011]] concerns learning conditions. Neither source establishes that AI substitution necessarily prevents the learning benefits of constructing an analogy.

## Open Questions

- How do particular AI models and human users perform when surface resemblance conflicts with relational structure?
- Does AI-assisted reasoning improve, preserve or reduce later unaided structural alignment?
- Which prompts, examples or feedback help users check candidate inferences?

These require direct tests; the 1997 theory does not determine their answers.
