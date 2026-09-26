---
status: solid
area: [risk, erosion]
type: paper
sources:
  - "Wu, S., Liu, Y., Ruan, M., Chen, S., & Xie, X.-Y. (2025). Human-generative AI collaboration enhances task performance but undermines human's intrinsic motivation. Scientific Reports, 15, 15105. https://doi.org/10.1038/s41598-025-98385-2"
---

# Wu et al. (2025) — GenAI Collaboration Augments Performance, Undermines Intrinsic Motivation

## Citation

Wu, S., Liu, Y., Ruan, M., Chen, S., & Xie, X.-Y. (2025). Human-generative AI collaboration enhances task performance but undermines human's intrinsic motivation. *Scientific Reports*, 15, 15105.

**DOI:** [10.1038/s41598-025-98385-2](https://doi.org/10.1038/s41598-025-98385-2)

(Wu, Liu, Ruan, Chen, Xie at the School of Management, Zhejiang University. Open access. Pre-registered.)

## Type

Paper (four pre-registered online experiments; total N = 3,562 Prolific UK; mixed-design repeated-measures ANOVAs with paired-samples t-tests; rater-based and LIWC-based assessment of immediate task quality)

## Key Insight

Wu et al. document a paired effect they call **performance augmentation + psychological deprivation**: collaboration with GenAI improves the quality of the immediate task (modest to large effect sizes across writing-heavy tasks), but the gains do *not* spill over to a subsequent unassisted task, and the transition from collaboration back to solo work measurably reduces intrinsic motivation and increases boredom (medium effect sizes, replicated across three studies). Study 4's 2 × 2 design adds the sharpening finding: the *Solo→Collab* transition produces the steepest drop in sense of control (d = 0.84) — autonomy threat is about the presence of GenAI, not just task transition.

This is the cleanest experimental causal anchor in the KB for the motivation/boredom face of psychological deprivation. It complements [[hai-dark-side-collaboration-2025]] (within-person field ESM evidence of GenAI → alienation → expediency) and [[lee-relying-self-efficacy-2026]] (passive-vs-active mode-of-use experiment) in a third design family — within-subjects task-transition with pre-registered RCT methodology.

## Key Passages

> "Our findings consistently demonstrated that collaboration with GenAI enhanced immediate task performance. However, this performance augmentation effect did not persist in subsequent tasks performed independently by humans. Importantly, transitioning from collaboration with GenAI to solo work led to an increased sense of control of human workers, and was also accompanied by significant decreases in intrinsic motivation and increases in feelings of boredom."
> — Wu et al., [p.1, abstract]

> "These results highlight the complex dual effects of human-GenAI collaboration: It enhances immediate task performance but can undermine long-term psychological experiences of human workers."
> — Wu et al., [p.1, abstract]

> "Across four studies involving various cognitively demanding tasks (i.e., text generation and creative brainstorming), our results consistently demonstrate a double-edged sword effect of human-GenAI collaboration. While GenAI enhances the quality of human-generated outputs, it fails to sustain subsequent task performance and undermines key psychological experiences, including sense of control, intrinsic motivation, and feeling of boredom."
> — Wu et al., [p.22]

> "While GenAI contributes substantially to the current task outcomes, individuals may perceive a reduction in personal agency, thereby undermining their sense of control. Furthermore, the transition from engaging, AI-assisted tasks to less stimulating, human-solo tasks may exacerbate feelings of boredom, as tasks lacking novelty and challenges are known to erode sustained motivation."
> — Wu et al., [p.22]

> "Participants who initially worked solo and later collaborated with GenAI reported a sharp decline in their sense of control (Δ = -1.01, p < .001), whereas those who worked solo throughout experienced a more modest decrease (Δ = -0.15, p < .001). The substantial drop in the Solo-Collab condition suggests that transitioning from solo work to GenAI collaboration significantly undermines perceived sense of control, more so than sustained solo work alone."
> — Wu et al., [p.19]

> "AI system designers should emphasize human agency in collaborative platforms, achieved by integrating user feedback, input, and customization, ensuring users retain a sense of control during collaborations with AI."
> — Wu et al., [p.23]

## Methodology

- **Total sample:** 3,562 Prolific UK participants across four pre-registered experiments (Approval no. 20230323).
- **Studies 1–3:** Two-condition between-subjects (Collab-Solo vs. Solo-Solo). All three studies use a Task 1 (text generation, with or without ChatGPT) → Task 2 (independent brainstorming) sequence with psychological measures (sense of control, intrinsic motivation, feelings of boredom; 7-point Likert) after each task.
  - Study 1 (N = 352): Facebook promotional post (Task 1) → Alternative Uses Test (Task 2). ChatGPT 3.5 via Qualtrics Web Service.
  - Study 2 (N = 793): Performance review report (Task 1) → product improvement brainstorm (Task 2). LIWC-based assessment of Task 1.
  - Study 3 (N = 793): Welcome email (Task 1) → product promotion brainstorm (Task 2). LIWC-based assessment of Task 1.
- **Study 4 (N = 1,624):** 2 × 2 mixed factorial — between-subjects (Collab vs. Solo) × within-subjects (Task 1 vs. Task 2) — with four conditions: Collab-Collab (N = 456), Collab-Solo (N = 345), Solo-Solo (N = 428), Solo-Collab (N = 395). Two similar text-generation tasks (Email + Facebook post from Studies 1 and 3) counterbalanced to eliminate task-type and order confounds.
- **Measures:** Sense of control (3-item, Cronbach's α ≥ 0.88). Intrinsic motivation (4-item, α ≥ 0.95 in all studies). Boredom (4-item; α = 0.41–0.51 in Study 1 — flagged by authors as low reliability and replaced with a different 4-item dynamic-state scale from Study 2 onward, α ≥ 0.87).
- **Analysis:** Independent-samples t-tests for Task 1 augmentation and Task 2 spillover; mixed-design repeated-measures ANOVAs for psychological-experience interactions; paired-samples t-tests for within-person changes. Effect sizes reported throughout (Cohen's d, partial η², ω²) with 95% CIs.
- **Manipulation checks:** Significant chi-square tests in all studies confirming participants accurately reported their condition (e.g., χ²(1) = 567.74, p < .001 in Study 2).
- **Task 1 quality assessment:** Five independent raters with TOEFL ≥ 25 / IELTS ≥ 8 in Study 1 (ICC 0.86–0.87); LIWC2015 dictionary in Studies 2–4 (word count, analytical content, prosocial/affiliation/social/positive tone).

## Key Findings

### Performance augmentation (Task 1) — confirmed

- **Study 1** (Facebook posts, rater-assessed):
  - Engaging: M_Collab = 2.89 vs. M_Solo = 2.68; t(350) = 2.22, p = .027, d = 0.25.
  - Informative: n.s. (d = 0.18, p = .087).
  - Overall quality: d = 0.23.
- **Study 2** (performance reviews, LIWC):
  - Word count: M_Collab = 289.76 vs. M_Solo = 108.51; d = 1.50.
  - Analytical content: d = 0.25; Prosocial: d = 0.46.
- **Study 3** (welcome emails, LIWC):
  - Word count: d = 1.26; Affiliation content: d = 0.49; Social orientation: d = 0.23.
- **Study 4** (text generation, LIWC, pooled across Collab conditions):
  - Word count: d = 1.10; Analytical content: d = 0.38; Positive tone: d = 0.17.

### Spillover augmentation (Task 2) — largely absent

- **Study 1**: Idea quantity n.s. (d = 0.02); idea quality d = 0.29 (only finding of positive spillover).
- **Study 2**: All three measures (quantity, novelty, usefulness) negligible (d = 0.02–0.06, all n.s.).
- **Study 3**: All three measures negligible (d = -0.07 to -0.09, all n.s.; directionally *worse* after Collab).
- **Study 4** (Collab-Solo vs. Solo-Solo Task 2): Word count d = 0.14 with Solo-Solo *longer* (p = .048); analytical content and positive tone n.s. The augmentation effect did not transfer.

### Psychological deprivation (Task 1 → Task 2 within-person)

- **Sense of control** — Collab→Solo: significant *increase* (d = 0.15–0.39 across studies). Solo→Collab (Study 4): significant *decrease* (d = 0.84, the single largest psychological effect in the paper). Solo-Solo: small decrease in Studies 2–4. Collab-Collab: stable. Interpretation: GenAI collaboration suppresses sense of control; transitioning away restores it; transitioning into AI is the most disruptive direction.
- **Intrinsic motivation** — Collab→Solo: significant *decrease* across all four studies (d = -0.32 to -0.51, medium effect). Solo→Collab (Study 4): largest decrease (d = -0.42). Solo-Solo: smaller decrease (d = -0.14 to -0.22). Interaction effects significant in Study 1 (F = 8.41, p = .004), Study 3 (F = 5.05, p = .025), and Study 4 Solo-Solo vs. Collab-Solo (F = 5.45, p = .020). All four conditions in Study 4 showed declining motivation across tasks; transitions amplified the decline.
- **Boredom** — Collab→Solo: significant *increase* across all four studies (d = 0.32–0.51, medium effect). Solo-Solo: smaller increase (d = 0.22–0.35). Solo→Collab and Collab-Collab also showed increases. Interaction in Study 4 (Collab-Solo vs. Collab-Collab) significant (F = 4.85, p = .028) — sustained collaboration mitigates boredom growth relative to Collab→Solo, but does not eliminate it.

### Synthesis

The paper documents a **transition asymmetry**: Collab→Solo restores autonomy but reduces engagement; Solo→Collab is the most autonomy-eroding direction; Collab-Collab maintains stable control but does not buffer motivation decline or boredom; Solo-Solo declines slowly across all three measures. Sustained collaboration is *not* the protective default the productivity literature implicitly assumes.

## Relevance

Three load-bearing contributions to the KB:

- **Experimental causal anchor for the motivation-erosion thesis.** The KB's risk/erosion cluster carries the meaning- and motivation-erosion finding through several methodologies: theoretical SDT review (Hermann et al. 2025), within-person field ESM (Hai et al. 2025), passive-vs-active lab experiment (Lee et al. 2026), longitudinal industrial-automation field (Nikolova et al. 2024). Wu et al. add a fourth design family — pre-registered RCT with task-transition manipulation across four task types — that converges on the same conclusion through methodologically distinct evidence. The Cohen's d ≈ 0.32–0.51 range for intrinsic-motivation decline is the cleanest experimental effect-size estimate in this cluster.
- **The transition-asymmetry finding is novel.** Study 4's Solo→Collab d = 0.84 sense-of-control drop — the single largest psychological effect in the paper — refutes the assumption that transitioning *into* AI is benign and only Collab→Solo is risky. The autonomy threat operates whenever GenAI is present, regardless of whether the worker is moving toward or away from it. This sharpens [[strategic-alternation]] (alternation between modes is not automatically protective) and adds nuance to [[lee-relying-self-efficacy-2026]]'s post-AI carry-over finding (the harm runs both directions, not only after AI use).
- **Spillover absence as a constraint on AI-as-pedagogy claims.** Three of four studies found no spillover augmentation; Study 4 even found a small *negative* spillover on text length. This is a direct empirical caution against the implicit assumption underlying many "AI as cognitive scaffold" narratives — that working with AI builds capacity that transfers to unassisted work. Wu et al. show the opposite: GenAI augments while present and tends not to leave behind durable improvements (with the partial exception of Study 1's idea-quality finding, d = 0.29). This complements the [[performance-paradox]] finding from a different angle: the paradox there is *during* AI use; Wu et al. add that the paradox does not resolve in the worker's favor *after* AI use either.

## Supports

- [[ai-self-efficacy-erosion]] — sense-of-control decline during collaboration (and sharp drop in Solo→Collab, d = 0.84) is the autonomy-frustration face of self-efficacy erosion in a within-subjects experimental design.
- [[professional-identity-threat]] — intrinsic-motivation decline and boredom increase are SDT-grounded markers of meaning erosion; Wu et al. operate within the same Basic Psychological Needs Theory frame Hermann et al. organize the literature around.
- [[agency]] — the authors' practical recommendation ("AI system designers should emphasize human agency in collaborative platforms, achieved by integrating user feedback, input, and customization, ensuring users retain a sense of control") is a direct articulation of agency-preservation. The Solo→Collab autonomy drop is empirical evidence that GenAI's default integration mode threatens the conscious-choice-about-engagement core of agency.
- [[hai-dark-side-collaboration-2025]] — sister study from a different methodological family. Hai et al. show daily within-person ESM evidence of GenAI → alienation → expediency in field service-industry work; Wu et al. show experimental causal evidence of GenAI → motivation decline + boredom increase in lab text-generation tasks. The two converge on the same psychological pathway (motivation/meaning erosion) through complementary designs.
- [[lee-relying-self-efficacy-2026]] — both papers document post-AI carry-over of psychological harm. Lee et al. show passive-AI-use erodes self-efficacy/ownership/meaning even into post-AI manual work; Wu et al. show Collab→Solo transition reduces intrinsic motivation and increases boredom. The mechanisms are complementary — Lee at the mode-of-use level, Wu at the task-transition level.
- [[mascanero-proximal-collaboration-2026]] — both find that AI's effects depend on collaboration configuration. Mascareño shows proximal collaboration impairs idea selection and implementation (downstream innovation stages); Wu shows transitions in/out of AI carry distinct psychological costs. Both refute "AI helps innovation" generalizations.
- [[performance-paradox]] — Wu et al. add the *post-AI* face: the paradox does not resolve favorably when AI is removed; the worker's psychological state is worse, not better, even though sense of control is regained. This complements Bastani et al.'s exam-vs-practice gap (during AI) with a transition-effect (after AI).
- [[singh-yadav-competency-paradox-2026]] — Wu et al.'s spillover-absence finding (3 of 4 studies; small or negative spillover) is the experimental analogue of Singh Yadav's developmental-trajectory framing of competency erosion: gains during AI use don't translate into durable independent capability.
- [[nosta-ai-rebound-2025]] — Nosta's framing of post-AI performance dropping below baseline is partially supported and partially nuanced by Wu et al.: psychological state drops on transition (motivation, boredom), but *task* performance does not robustly drop below baseline (only Study 4 word-count showed Solo-Solo > Collab-Solo by d = 0.14). Wu et al. document the *psychological* rebound more clearly than the *behavioral* one.
- [[strategic-alternation]] — the practice is partially supported (Collab→Solo restores sense of control) but partially complicated by Wu et al.: alternation is not a clean preservation strategy; both Collab→Solo and Solo→Collab transitions carry distinct psychological costs (motivation decline; autonomy loss). The protective version of alternation requires more design care than "just switch modes."
- [[hermann-genai-psychology-work-2025]] — Wu et al. supply experimental evidence within the SDT/BPNT framework Hermann et al. use to organize the field. The deprivation effect is autonomy frustration (sense of control drop) + motivation frustration (intrinsic motivation drop), both predicted by the BPNT framework.

## Contradicts / Extends

- **Extends** [[hai-dark-side-collaboration-2025]] — adds experimental causal evidence to Hai et al.'s within-person field correlation. Together the two papers triangulate the same mechanism (GenAI → motivation/meaning erosion) through ESM field methodology + pre-registered task-transition RCT methodology.
- **Extends** [[lee-relying-self-efficacy-2026]] — Lee et al. show passive AI use erodes efficacy/ownership/meaning post-AI; Wu et al. add that the *direction* of transition matters: the autonomy-threat is sharpest when transitioning *into* AI (Solo→Collab), not just after AI use. The harm is bidirectional, not unidirectional.
- **Extends** [[performance-paradox]] — adds the post-AI dimension: the paradox does not resolve in the worker's favor when AI is removed; psychological state is worse, with no durable performance carryover.
- **Tension with optimistic spillover claims.** Some AI-as-scaffolding narratives (e.g., the "AI exposure builds skills" implicit assumption in some workforce-development discourse) are not supported by Wu et al.: across four pre-registered experiments, the augmentation effect almost never spilled over to subsequent unassisted tasks, and Study 4 found a small *negative* spillover on text length. The spillover-absence pattern is robust enough to caution against assuming AI-mediated work builds latent capacity.
- **Tension with "sustained collaboration is the safe default" assumption.** Study 4's Collab-Collab condition maintained stable sense of control but did not buffer motivation decline or boredom. Sustained collaboration is not psychologically protective; it just smooths out the autonomy-erosion of the Solo→Collab transition by keeping the worker continuously suppressed at the lower control baseline.

- Qualified by [[corgnet-genai-motivation-2026|Corgnet, Fumagalli and Rezaei (2026)]]: in a preregistered creative-task experiment, human–AI participants reported greater satisfaction, interest, autonomy, competence, and relatedness than newly formed human–human pairs. The comparison was with unfamiliar collaborators, not solo work or established colleagues. Behavioral willingness to repeat the task alone did not meaningfully increase. The findings show why Wu's task-transition results should not become a claim that AI collaboration always harms motivation; the studies do not estimate the same effect.

## Open Questions

- **Long-term arc.** The paper is limited to two consecutive tasks. Whether the deprivation effect persists, attenuates, or compounds over weeks/months of repeated transitions is open — relevant for [[liu-persistence-2026]]'s persistence findings.
- **Real workplace vs. Prolific.** Authors note Prolific samples may not reflect real workplace dynamics. The intrinsic-motivation construct measured in 4-item scales after a 5-minute Qualtrics task may not generalize to weeks-long work projects with stronger contextual motivators (career goals, team relationships, performance review consequences).
- **Boredom measure reliability in Study 1.** Cronbach's α = 0.41–0.51 in Study 1 — authors flag this as low reliability and replace the scale from Study 2 onward (α ≥ 0.87). Study 1 boredom findings should be interpreted cautiously, though the pattern replicates with the better measure in Studies 2–4.
- **Curvilinear effects of intrinsic motivation.** Authors note prior work suggests moderate intrinsic motivation can carry over but extreme levels create contrasting effects; their participants' motivation was around 5/7 (high but not extreme), so they did not test curvilinear effects. Whether very high engagement during Task 1 amplifies or attenuates Task 2 deprivation is open.
- **Mode-of-use moderation.** Lee et al. (2026) show passive vs. active AI use produces different psychological outcomes. Wu et al.'s "collaboration" condition is a single mode (prompt + receive + edit ChatGPT output) and does not separately manipulate active-collaboration vs. passive-copy modes. Whether the deprivation effect concentrates in the more passive use modes is open.
- **Domain transfer.** All four tasks are text-generation or text-adjacent (writing + brainstorming). Whether the same pattern operates in code, analysis, design, or planning tasks is not directly tested — though Lee et al.'s N = 270 follow-up survey suggests it may.
- **Job-design moderation.** The paper does not test whether high-vs-low autonomy job contexts moderate the deprivation effect — Hai et al.'s digital-job-demands moderator suggests this is plausible but Wu et al. do not address it.
