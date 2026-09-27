---
status: solid
area: [preservation, risk, erosion]
type: paper
sources:
  - "Dell'Acqua, F., Ayoubi, C., Lifshitz, H., Sadun, R., Mollick, E., Mollick, L., Han, Y., Goldman, J., Nair, H., Taub, S., & Lakhani, K. R. (2026). The Cybernetic Teammate: A Field Experiment on Generative AI and Teamwork. Organization Science, Articles in Advance. https://doi.org/10.1287/orsc.2025.20702"
---

# Dell'Acqua et al. (2026) — The Cybernetic Teammate

## Citation

Dell'Acqua, F., Ayoubi, C., Lifshitz, H., Sadun, R., Mollick, E., Mollick, L., Han, Y., Goldman, J., Nair, H., Taub, S., & Lakhani, K. R. (2026). The Cybernetic Teammate: A Field Experiment on Generative AI and Teamwork. *Organization Science*, Articles in Advance. https://doi.org/10.1287/orsc.2025.20702

**DOI:** [10.1287/orsc.2025.20702](https://doi.org/10.1287/orsc.2025.20702)

(Open access, CC BY 4.0. Harvard Business School + HBS AI Institute + ESSEC + Warwick + Wharton + Procter & Gamble. Received June 2025; accepted April 2026; published online 12 Jun 2026.)

## Type

Paper (preregistered field experiment, N=791 professionals at Procter & Gamble, 550 submitted solutions; 2×2 between-subjects design crossing team structure × AI access; blind evaluation by multiple independent raters; regression analysis of standardized quality, emotion, and process-decomposition outcomes). AI tool: GPT-4 via Microsoft Azure (a later workshop cohort used GPT-4o).

## Key Insight

A single worker with GenAI can reproduce several benefits that organizations have historically needed a *team* to obtain — not just cognitive speed, but the three classic pillars of teamwork: **performance**, **expertise integration**, and **social/emotional engagement**. In this field experiment, individuals working with AI (+0.37 SD) matched the solution quality of two-person cross-functional teams working without AI (+0.24 SD), and adding AI to a team produced no significant *further* average gain — so AI's lift came mainly from strengthening the individual, not from improving human-to-human collaboration. This reframes GenAI from a *tool* (like a spreadsheet) to a **[[cybernetic-teammate]]**: an active counterpart that partially fills roles previously reserved for human colleagues.

Two findings keep the picture honest and non-triumphalist. First, AI is a **"quality amplifier rather than a decision enhancer"** [p.17]: it raises the average quality of *generated* ideas across the whole distribution (preserving variance in rated quality and lifting the high-quality tail), but AI-assisted participants were measurably *worse* at selecting their best idea (~37% vs. ~50% for human teams), a [[human-ai-complementarity]]-relevant asymmetry the authors suggest might partly involve AI's tendency to affirm rather than push back ([[sycophancy]], [[social-friction]]). Second, the results are a plausible *lower bound* (participants were relatively inexperienced prompters using tools not built for collaboration) obtained under flash-team conditions (one virtual day, one firm, one model), so they speak to short-run task performance, not to long-run skill development, trust, or organizational reality.

## Key Passages

> "(1) AI significantly enhances performance: individuals with AI matched the performance of teams without AI, suggesting that AI can effectively replicate certain benefits of human collaboration."
> — Dell'Acqua et al. 2026, [p.2] (Abstract)

> "Overall, these results illuminate AI's primary mechanism as a collaborative partner: it functions as a quality amplifier rather than a decision enhancer. AI consistently elevates the baseline quality of creative output while also preserving the natural variance that drives breakthrough innovation."
> — Dell'Acqua et al. 2026, [p.17] (Decomposing AI's Contributions)

> "The validating nature of AI feedback may itself erode critical engagement: unlike human teammates, who naturally introduce friction and dissent, AI tends to affirm. That affirmation may feel productive in the moment while diminishing participants' evaluative judgment."
> — Dell'Acqua et al. 2026, [p.16] (Decomposing AI's Contributions)

> "This suggests AI serves not just as an information provider but as an effective boundary-spanning mechanism, helping professionals reason across traditional domain boundaries and approach problems more holistically."
> — Dell'Acqua et al. 2026, [p.19] (Discussion)

> "Contrary to fears about AI creating negative workplace experiences, we found consistently positive emotional responses to AI use, including increased excitement and enthusiasm, as well as reduced anxiety and frustration."
> — Dell'Acqua et al. 2026, [p.19] (Discussion)

> "the first teammate addition, regardless of type, delivered significant average quality gains. However, the subsequent addition yielded less significant average improvement, while increasing the likelihood of producing top-decile, breakthrough ideas."
> — Dell'Acqua et al. 2026, [p.20] (Discussion)

## Key Findings

**Design** [p.5–8]. 791 experienced R&D and commercial professionals at P&G worked a full day on *real* early-stage product-development problems from their own business units, with real stakes (top proposals presented to business-unit leaders; some entered P&G's actual innovation pipeline). Random assignment to a 2×2: (1) individual, no AI; (2) two-person team (one commercial + one R&D), no AI; (3) individual + AI; (4) two-person team + AI. 550 solutions were scored by multiple independent evaluators without time constraints under a P&G-validated protocol.

**Performance** [p.10–11, Table 2]. Over the individual-no-AI baseline (standardized quality): Team No-AI **+0.245 SD** (p<0.05; ~6.3%); Individual + AI **+0.373 SD** (p<0.01; ~9.6%); Team + AI **+0.392 SD** (p<0.01; ~10.2%). The p=.242 comparison in Table 2 is Team+AI versus Team without AI, not versus Individual+AI. The point estimates for Individual+AI and Team+AI were similar; do not attach that p-value to their comparison. Effects robust across specifications. AI also produced much longer outputs (Table 3), but length did not explain the quality gain (no length–quality relationship among non-AI participants).

**Expertise / boundary-spanning** [p.12–13]. Without AI, professionals proposed ideas aligned to their function (commercial→commercial, R&D→technical); *with AI, that distinction largely disappeared* and both produced balanced, cross-domain solutions — with no quality penalty for the added breadth (Figure 5). Non-core-job employees (unfamiliar with product development) working *alone with AI* reached performance levels comparable to teams containing a core-job expert. → [[ai-boundary-spanning]], [[leveling-effect]].

**Sociality / affect** [p.13–14, Tables 5–6]. AI use raised self-reported positive emotion (Individual+AI **+0.457 SD**, Team+AI **+0.635 SD**; both p<0.01) and lowered negative emotion (Individual+AI **−0.233 SD**, Team+AI **−0.235 SD**; both p<0.05), vs. the control. Solo workers with AI reported affect matching or exceeding teams without AI. The authors caution that reduced interpersonal friction "may not always translate into long-term creative gains and may in fact be harmful" — some constructive tension is lost.

**Generation vs. evaluation asymmetry** [p.15–17, Figure 8]. Idea quantity was capped at five across all conditions to isolate mechanism. AI raised *average generated-idea quality* (panel a) and preserved variance (panel c — preserved variance in rated quality, not a semantic-diversity test). But on *selection* (probability of choosing one's highest-quality idea), human teams without AI were best (~50%) vs. ~37% for AI conditions (panel b). Net final quality was still higher with AI because the generation boost more than offset the selection loss (panel d). Candidate mechanisms for the selection deficit: LLM sycophancy reinforcing initial confidence, weaker internalization of AI-developed ideas, and AI explanations suppressing independent human judgment. Headline framing: AI is a **quality amplifier, not a decision enhancer** [p.17].

**Extremes and marginal returns** [p.17, p.19–20, Table 9]. Team+AI was **9.2 percentage points** more likely to produce a top-decile solution than the control mean of 5.8% — roughly **3× the breakthrough rate**. As the authors' interpretation of between-condition comparisons, not an observed longitudinal expansion: read as sequential team expansion (individual → dyad → triad-with-AI), the *first* teammate (human or AI) delivered most of the average gain; the *second* addition added little on average but disproportionately lifted the right tail. An *indicative* (not causal) decomposition suggests ~40% of the solo AI gain reflects enhancement of non-collaborative work and ~60% reflects substitution for collaborative functions [p.20].

**Adoption dynamic** [p.14–15, Tables 7–8]. Participants who reported the most positive affect while using AI also reported the largest increases in expected future AI use — a possible self-reinforcing adoption cycle (correlational).

## Relevance

A field experiment relevant to [[cybernetic-teammate]] and [[ai-boundary-spanning]]. Four contributions:

1. **Reframes the unit of augmentation from task to teamwork.** The study asks whether AI can support *team functions* (performance, expertise, sociality). It supplies the empirical anchor for [[cybernetic-teammate]].
2. **Sharpens [[human-ai-complementarity]] at the process level.** The generation-vs-evaluation split ("quality amplifier, not decision enhancer") locates where human value persists — *evaluative selection* — with a measured effect size, not just an assertion. It identifies a short-run selection difference; durable human advantage was not tested.
3. **Names boundary-spanning as an AI effect.** [[ai-boundary-spanning]] — one person reasoning across functional expertise they don't personally hold — is distinct from the [[leveling-effect]] (skill-gap compression) and is measured here.
4. **Reports an affect benefit.** Offers a different context from [[wu-collaboration-motivation-2025]] and [[hai-dark-side-collaboration-2025]].

The study's limits include the selection deficit, the loss of constructive friction, novice-prompter lower-bound, flash-team artificiality, single-firm/single-model scope, and unaddressed long-term skill/trust questions. Its short-run augmentation findings do not establish that AI replaces teammates (the authors are explicit that AI "cannot fully replicate the richness of human social and emotional interaction").

## Supports

- [[cybernetic-teammate]] — the empirical anchor; AI reproducing performance/expertise/social teamwork functions for a solo worker.
- [[ai-boundary-spanning]] — measured convergence of commercial vs. technical idea distributions under AI.
- [[human-ai-complementarity]] — process-level evidence that human judgment retains value in evaluative selection while AI amplifies generation.
- [[complementarity-framework]] — field evidence for two of the framework's factors (team size / diminishing returns; the need for humans to interrogate rather than accept AI).
- [[augmentation-synergy-gap]] — marginal-teammate value is concentrated in the tail (breakthroughs), not the mean; see the caveat under Contradicts/Extends (no AI-alone arm).
- [[leveling-effect]] — non-core-job employees + AI reach expert-team performance levels.
- [[sycophancy]] / [[social-friction]] — AI's affirmation (vs. human friction/dissent) is the proposed mechanism for the selection deficit.
- [[performance-paradox]] — short-run gains alongside a flagged risk to longer-run evaluative judgment and skill.
- [[jagged-frontier]] — Dell'Acqua's own 2023 frontier concept, invoked here (theories of the "AI mind" tracking jagged capability).

## Contradicts / Extends

- Extends: [[dellacqua-jagged-frontier-2023]] — same lead author; jagged-frontier studied a single consultant's task boundary, this studies teamwork and expertise integration in a real firm.
- Extends / reconciles: [[vaccaro-human-ai-meta-analysis-2024]] — Vaccaro found human-AI *combinations* underperform the best single party on average, with a positive but nonsignificant creation-task estimate. This creation-task field study tests a different baseline. Note a design difference: Cybernetic Teammate has **no AI-alone condition**, so it does not test Vaccaro-style *synergy* (beating both human-alone and AI-alone) directly — its "AI matches teams" claim is augmentation over the human baseline, plus a within-team marginal-returns pattern.
- Tension: [[mascanero-proximal-collaboration-2026]] — Mascareño found proximal AI collaboration *hinders* idea selection and implementation; Dell'Acqua finds AI *helps* overall final quality but agrees on the specific point that AI *weakens selection* judgment. The two converge on "AI hurts evaluative selection" while differing on the net outcome.
- Tension: [[wu-collaboration-motivation-2025]] / [[hai-dark-side-collaboration-2025]] — those document motivational/affective *costs* of GenAI collaboration; this documents affective *benefits*. [Inference] The difference may be task framing (real high-stakes innovation vs. routine tasks), novelty effects, or measurement (immediate self-report vs. sustained motivation).

## Open Questions

- Do the gains hold as users become *expert* prompters, or do they compress (ceiling) or invert (over-reliance)? The authors call the current estimates a lower bound; that is an [Inference] about direction, not a measured trajectory.
- Does AI-enabled boundary-spanning build *genuine* cross-domain expertise over time, or only rent temporary access? The paper measures one-day output, not learning. → [[ai-boundary-spanning]], [[novice-vulnerability]].
- The selection deficit: is it a fixable interaction-design problem (prompt for dissent, withhold affirmation) or an intrinsic property of affirming systems? Links to [[sycophancy]] and [[cognitive-friction]].
- Does the positive-affect → future-use correlation become a self-reinforcing preference for AI over human teammates, and at what cost to team relationships and constructive friction?
- External validity beyond one CPG firm, one model (GPT-4/4o), remote flash teams, and early-stage NPD tasks is untested.
