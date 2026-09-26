---
status: solid
area: [erosion, risk]
type: paper
sources:
  - "Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. Human Factors."
---

# Parasuraman & Riley (1997) — Humans and Automation

## Citation

Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors*, 39(2), 230-253.

**DOI:** [10.1518/001872097778543886](https://doi.org/10.1518/001872097778543886)

## Type

Paper (theoretical and empirical review; foundational human factors literature)

## Key Insight

Parasuraman and Riley introduce the **four-part taxonomy of human-automation interaction** that has shaped automation research for nearly three decades:

- **Use** — the voluntary activation or disengagement of automation by the operator. Influenced by trust, mental workload, perceived risk, and individual differences. Hard to predict.
- **Misuse** — *overreliance*. Excessive trust leads operators to "rely uncritically on automation without recognizing its limitations" and to fail at monitoring it. Drives both omission errors (failing to act because the AI didn't flag something) and commission errors (following an inappropriate AI directive).
- **Disuse** — *underreliance*. Mistrust — usually from false-alarm-prone alerts — leads operators to ignore, disable, or override automation that could help. The Conrail train operators tape-recording over speed-violation buzzers is the canonical example.
- **Abuse** — *inappropriate design or deployment*. Designers and managers automating "without due regard for the consequences for human performance," producing systems where the operator's role becomes a by-product of what was left unautomated.

The conceptual move that makes this taxonomy load-bearing for the AI era is the **vicious circle** the authors trace among the four modes: abuse (bad design) creates conditions for misuse (overreliance) and disuse (mistrust); when operators err under those conditions, designers and managers respond with *more* high-level automation; the cycle continues. The framework is therefore not just a classification — it's a feedback model of how human-automation systems decay over time when each mode is treated as someone else's problem.

The 1997 evidence is drawn primarily from aviation (autopilots, Flight Management Systems, GPWS), ground transportation (railroad alerts, automotive collision warning), and process control. The mechanisms it names — **automation bias** (heuristic over-reliance on AI cues at the expense of disconfirming evidence), **complacency** (degraded monitoring under stable autonomy), and **trust calibration** — translate directly to AI-assisted knowledge work, even though the original substrate was hardware control loops.

For human thinking with AI: this is the foundational literature for understanding why simply *adding* AI to a workflow without redesigning the human's role tends to fail in predictable ways. The KB's [[automation-bias]], [[novice-vulnerability]], trust-calibration-adjacent entries, and [[performance-paradox]] all rest on mechanisms first named here.

## Key Passages

> "Misuse refers to overreliance on automation, which can result in failures of monitoring or decision biases. ... Disuse, or the neglect or underutilization of automation, is commonly caused by alarms that activate falsely. ... Automation abuse, or the automation of functions by designers and implementation by managers without due regard for the consequences for human performance, tends to define the operator's roles as by-products of the automation."
> — Parasuraman & Riley, [p.1, abstract]

> "Excessive trust can lead operators to rely uncritically on automation without recognizing its limitations or fail to monitor the automation's behavior. Inadequate monitoring of automated systems has been implicated in several aviation incidents — for instance, the crash of Eastern Flight 401 in the Florida Everglades. The crew failed to notice the disengagement of the autopilot and did not monitor their altitude while they were busy diagnosing a possible problem with the landing gear."
> — Parasuraman & Riley, [p.5]

> "Mosier and Skitka (1996) also pointed out that reliance on the decisions of automation can make humans less attentive to contradictory sources of evidence. ... pilots tended to use automated cues as a heuristic replacement for information seeking. They found that pilots tended not to use disconfirming evidence available from cockpit displays when there was a conflict between expected and actual automation performance. Automation bias error rates were also found to be similar for student and professional pilot samples, indicating that expertise does not guarantee immunity from this bias."
> — Parasuraman & Riley, [pp.5–6]

> "Mosier et al. (1994) found that 77% of ASRS [Aviation Safety Reporting System] incidents in which overreliance on automation was suspected involved a probable failure in monitoring."
> — Parasuraman & Riley, [p.6]

> "If the base rate is low, as it often is for many real events, then the posterior probability of a true alarm — the probability that given an alarm, a hazardous condition exists — can be low even for sensitive warning systems. ... Many human operators tend to ignore and turn off alarms — they have cried wolf once too often."
> — Parasuraman & Riley, [pp.8–9]

> "One cannot remove human error from the system simply by removing the human operator. Indeed, one might think of automation as a means of substituting the designer for the operator. To the extent that a system is made less vulnerable to operator error through the introduction of automation, it is made more vulnerable to designer error."
> — Parasuraman & Riley, [pp.9–10]

> "In general, abuse of automation can lead to problems with costs that can reduce or even nullify the economic or other benefits that automation can provide. Moreover, automation abuse can lead to misuse and disuse of automation by operators. If this results in managers' implementing additional high-level automation, further disuse or misuse by operators may follow, and so on, in a vicious circle."
> — Parasuraman & Riley, [p.10]

## Relevance

The conceptual scaffolding for almost everything in the KB about over-trust and under-trust of AI systems originates here. Three load-bearing contributions:

- **Names automation bias as a measurable phenomenon, not a metaphor.** The 77% monitoring-failure rate in ASRS overreliance incidents (Mosier et al. 1994, cited at p.6) and the empirical demonstration that expertise *doesn't* protect against the bias (student vs. professional pilot equivalence) ground the construct in evidence. KB entries like [[automation-bias]], [[fluency-bias]], and [[performance-paradox]] cite back to this lineage even when they don't cite this paper directly.
- **Frames trust as miscalibration, not a binary.** The paper insists that trust is multidimensional — varying with reliability, observed failures, base rates, and individual disposition — and that both overtrust (misuse) and undertrust (disuse) are failures of *calibration*, not failures of "trusting AI" per se. This is exactly what the KB's [[calibration]] method operationalizes for AI use, and what [[scan]] navigates per task.
- **Identifies the abuse → misuse/disuse cascade.** Most contemporary AI-erosion arguments focus on user behavior. Parasuraman and Riley's structural insight is that user behavior is downstream of design and management choices, and that responding to user errors with *more* automation creates a feedback loop. This anticipates the [[upskilling-deskilling-paradox]] mechanism by 25 years.

## Supports

- [[automation-bias]] — foundational evidence, including the disconfirming-evidence-blindness mechanism
- [[cognitive-offloading]] — overreliance as the offloading mode that fails monitoring
- [[novice-vulnerability]] — but with an important nuance: this paper shows expertise doesn't protect, contra a naive reading of novice-vulnerability
- [[performance-paradox]] — the monitoring failure that hides until the automation hits a case it can't handle
- [[calibration]] — trust calibration as the operational response to all four modes
- [[scan]] — task-zone classification builds on the use-decision factors named here
- [[upskilling-deskilling-paradox]] — the abuse→misuse cascade is the structural mechanism
- [[goddard-automation-bias-2012]] — direct empirical follow-up in clinical decision support
- [[hohenstein-crumple-zone-2020]] - a different attribution pattern: AI absorbs some blame otherwise assigned to a human communicator
- [[bauer-discontinuing-ml-2022]] — disuse in modern ML deployment
- [[jagged-frontier]] — modern restatement of the automation-bias mechanism

## Contradicts / Extends

- Anticipates [[dellacqua-jagged-frontier-2023]] — Dell'Acqua's "jagged frontier" is the modern restatement of the automation-bias point: when AI is right, overreliance is fine; when AI is wrong, the human's failure to monitor is catastrophic, and the line between right and wrong shifts unpredictably.
- Aligns with [[shaw-cognitive-surrender-2026]] — Shaw and Nave's Study 1 finding that 79.8% of AI-engaged faulty trials involved acceptance of the faulty answer is the contemporary measurement of what Parasuraman and Riley named overreliance/automation-bias from accident-investigation evidence.
- The taxonomy itself benefits from a contemporary extension. AI knowledge work introduces a fifth mode the original paper couldn't anticipate — the case where the *output* of automation looks fluent and confident regardless of whether the underlying process succeeded ([[fluency-bias]], [[coherence-trap]]). In hardware control loops, an autopilot's failure mode is usually visible as anomalous behavior; in LLM output, failure modes can be undetectable from surface form.

## Open Questions

- The 1997 evidence base is hardware-centric (aviation, rail, process control). The four-mode taxonomy translates to AI knowledge work only by analogy — what would it mean to measure misuse/disuse/abuse in a knowledge-work setting where the "automation" produces text rather than vehicle trajectories?
- The vicious-circle prediction (abuse → misuse/disuse → more abuse) is strongly suggested but not empirically tested as a longitudinal cycle. Modern AI deployment (e.g., in healthcare, customer service, or coding) offers natural experiments — does the cycle close on the timescales the authors imply?
- The paper assumes operator override authority as the default ("usually but not always the operator is given override authority"). Many contemporary AI systems are deployed under conditions where override is friction-laden or deprecated by management policy. How does the taxonomy shift when override authority is genuinely absent?
- Automation bias is shown to be expertise-resistant in 1997 aviation studies. Does this generalize to AI knowledge work, or do contemporary studies (e.g., [[bo-sycophancy-novices-2026]]) suggest the bias is *more* damaging for novices? The reconciliation is probably that expertise protects against *some* errors but not against the specific structural pull of automation bias — but this needs explicit testing.
