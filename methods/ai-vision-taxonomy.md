---
status: emerging
area: [risk, preservation]
sources:
  - "Messeri, L. & Crockett, M. J. (2024). Artificial intelligence and illusions of understanding in scientific research. Nature, 627, 49–58."
---

# AI Vision Taxonomy (Oracle / Surrogate / Quant / Arbiter)

## Overview

A four-part taxonomy of how AI tools are positioned as collaborators in knowledge work, developed by Messeri & Crockett (2024) for the scientific research pipeline. Each vision identifies a distinct cognitive limit it promises to overcome, and each carries a distinct profile of epistemic risk. The diagnostic move is simple but powerful: before adopting an AI tool, name which vision it is invoking. The vision determines which illusions of understanding the use is most exposed to.

[Inference] The categories may also help frame consulting, analysis and journalism; those applications require testing.

## What It Is / How It Works

Messeri & Crockett (2024, Table 1) map the four visions to research-pipeline stages:

| Vision | Stage | Limits AI promises to overcome | What the vision is |
|---|---|---|---|
| **Oracle** | Study design / hypothesis generation | Too much literature; uneven quality; reader bias | Tools that search, evaluate, summarize literature and generate hypotheses |
| **Surrogate** | Data collection | Data are difficult, time-consuming, or expensive to obtain | Tools that generate surrogate data points (incl. synthetic human participants) |
| **Quant** | Data analysis | Data are too large or complex to curate and analyse | Tools that analyse vast and complex datasets, sometimes producing patterns inaccessible to human minds |
| **Arbiter** | Peer review / quality judgement | Too many submissions; reviewer bias; reproducibility crisis | Tools that evaluate scientific merit and predict replicability |

The visions reinforce each other. Surrogate-generated data needs Quant analysis. Quant outputs and Surrogate datasets generate more publications for Arbiters to evaluate and Oracles to summarize. All four visions converge on two promises: **productivity** (overcoming time/attention/cognitive limits) and **objectivity** (overcoming subjectivity and bias).

## Risk Profile by Vision

Each vision has a characteristic relationship to the three illusions of understanding (Messeri & Crockett 2024):

- **Oracle** loads heavily on the [[illusion-of-objectivity]] (it is described as bias-free literature evaluation) and contributes to the [[illusion-of-exploratory-breadth]] (its summaries shape which hypotheses get pursued).
- **Surrogate** loads heavily on the [[illusion-of-objectivity]] (synthetic participants are framed as representing all humanity) and on the [[illusion-of-exploratory-breadth]] (only quantifiable, AI-tractable phenomena get studied).
- **Quant** loads heavily on the [[illusion-of-explanatory-depth]] (predictive accuracy is mistaken for understanding of mechanism — the prediction–explanation fallacy).
- **Arbiter** loads heavily on the [[illusion-of-objectivity]] (AI peer review is framed as removing human subjectivity, but embeds the standpoints of its training data).

## What To Do

An untested discussion procedure, adapted from Messeri & Crockett's prescription "be clear about why you want to use AI in your research":

1. **Name the vision.** Before adopting an AI tool, ask: am I treating this as Oracle, Surrogate, Quant, or Arbiter? More than one is possible; name each.
2. **Read the risk profile.** Each vision corresponds to specific illusions of understanding. Make those risks explicit before they start operating implicitly.
3. **Check the productivity-vs-understanding trade.** The vision is appealing because it overcomes a cognitive or material limit. Is the limit one you want overcome here, or is it doing protective work (forcing you to read the literature carefully, collect data attentively, etc.)?
4. **Check the objectivity framing.** All four visions claim to remove human bias. Whose standpoints does the tool actually embed? Whose are filtered out?
5. **Identify lower-risk uses.** Routine tasks (composing emails) and tasks within your own expertise (writing code you could write yourself, given enough time) carry less epistemic risk than tasks outside your expertise.
6. **Maintain non-AI tracks.** For high-stakes work, keep at least one method running that does not depend on the same AI toolchain — for triangulation, not just corroboration.

## Why It Works

The proposed rationale is that the visions are *not* tools — they are sociotechnical framings about what AI is *for*. Naming the framing makes the embedded promise visible, and once the promise is visible the corresponding risk profile becomes legible.

Messeri & Crockett (2024, Box 2) note that "AI is not a monolith." Treating "AI use" as a single category obscures the very different epistemic risks of, say, an Oracle that summarizes literature versus a Surrogate that simulates participants. The taxonomy is designed to break that monolith into useful pieces.

## Strengths / Limitations

**Strengths:**
- Concise. Four categories, mapped to research-pipeline stages.
- Generalizable. The categories translate naturally to consulting (Oracle = research summarizer; Surrogate = synthetic personas; Quant = analyst; Arbiter = quality judge).
- Couples each vision to specific epistemic risks rather than treating "AI risk" as a single bucket.
- Makes the productivity/objectivity dual promise visible and questionable.

**Limitations:**
- The taxonomy is descriptive of current visions; AI capabilities evolve, and new visions may emerge.
- The categories overlap in practice. A single AI use often invokes more than one vision (e.g. an LLM that summarizes literature *and* writes code is Oracle + Quant).
- Does not provide a quantitative risk weighting; it is a diagnostic, not a metric.
- [Inference] The taxonomy may understate risks specific to LLMs as conversational interfaces — sycophancy, persuasion dynamics, and mode collapse are not cleanly mapped to any single vision.

## When It Applies

Use this method whenever you are deciding whether or how to adopt an AI tool in knowledge work — research, consulting, analysis, writing, decision-making — and want a fast way to name the trade-offs. It is most useful at the *adoption* stage; once a tool is embedded in a workflow, the framing tends to become invisible and the risks harder to surface.

When NOT to use this: for purely procedural AI uses (formatting, transcription) the taxonomy adds friction without insight. The visions become useful when the AI is being asked to participate in *judgement*, not just execution.

## Related

- [[scientific-monoculture]] — the system-level structure the four visions tend to cultivate when adopted uncritically.
- [[illusion-of-explanatory-depth]] — primary risk of the Quant vision.
- [[illusion-of-exploratory-breadth]] — primary risk of the Oracle and Surrogate visions.
- [[illusion-of-objectivity]] — primary risk of the Arbiter and Oracle visions; also Surrogate via the "all standpoints" framing.
- [[partial-automation-principle]] — complementary method; the AI vision taxonomy names the *role* AI plays, partial-automation names the *boundary* of that role.
- [[think-first]] — practice that pre-empts Oracle-vision risks by getting your own framing on the page before AI's.
- [[jagged-frontier]] — capability boundary; the four visions describe the framing, jagged frontier describes where the framing breaks down empirically.

## Sources

- [[messeri-crockett-illusions-understanding-2024]] — Messeri, L. & Crockett, M. J. (2024). Artificial intelligence and illusions of understanding in scientific research. Nature, 627, 49–58.

