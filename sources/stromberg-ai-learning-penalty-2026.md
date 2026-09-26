---
status: emerging
area: [erosion, risk, preservation]
type: paper
sources:
  - "Strömberg, Lei & Wu (2026)"
---

# Strömberg et al. (2026) — Homework Gains and Exam Losses

## Citation

Strömberg, D., Lei, V., & Wu, Y. (2026, June). *The Generative AI Learning Penalty: Evidence from Chinese Secondary Education*. Working paper; supplied PDF, no journal or DOI shown.

## Type

Paper — observational administrative panel with staggered-adoption difference-in-differences analysis.

## Key Insight

In one Chinese county, adoption of general-purpose AI was followed by better and faster homework but worse closed-book exam performance. The pattern is consistent with outsourcing learning tasks; it does not establish that all AI tutoring harms learning or that imposing longer homework time fixes it.

## Evidence

- 26,811 students in grades 7–12 at nine schools, covering roughly 90% of the county's secondary students. A June 2025 survey retrospectively dated first AI use, linked to up to three school years of exams and homework. The authors describe a 30-month panel; observed history varies by grade (PDF pp.1, 5–7).
- Main estimator: Callaway–Sant’Anna staggered difference-in-differences, comparing adopters with never-adopters, with errors clustered by 524 classes. A causal interpretation requires parallel counterfactual trends and no confounding changes accompanying adoption. Similar pretrends and alternative specifications support, but cannot prove, those assumptions (pp.7–14).
- Fully developed estimates at 6–10 months: homework scores +18% of the baseline mean; completion time about −19 minutes (64→45); monthly exam scores −20%. Average effects across all post-adoption periods were smaller: +11% homework and −13% monthly exams (p.11).
- Entrance-exam average treatment effects were about −7% in the DID approach. Estimates for students exposed for at least two years were −24% for Zhongkao and −18% for Gaokao. Identification is weaker: only one or two entrance observations are available, and the DID comparison uses a prior regular exam as baseline (pp.14–16).
- “Outsourcing” is inferred from completion times below 50 minutes; “full outsourcing” below 45. Shares were 58% and 34% overall, rising to 81% and 50% after more than five months of AI use. These are proxy-defined groups, not observed copying or chat transcripts (pp.17–19).
- Students with comparable homework time had similar exam scores whether or not they used AI. This post-adoption relationship is explicitly noncausal. Larger losses were reported for younger students, boys and higher initial achievers, with differences across subjects (pp.19–22).

## Key Passages

> "The relationship between homework completion time and exam scores should not be interpreted as causal."
> — Strömberg et al., PDF p.19

> "Better homework performance may coexist with weaker learning, and the divergence may not become visible until closed-book exams or high-stakes assessments."
> — Strömberg et al., PDF p.20

## Relevance

Extends [[performance-paradox]] over months and cumulative exams in ordinary schools. The unit of concern is retained learning, not the assisted homework score. [Inference] Track independent assessments alongside homework quality when evaluating educational AI.

## Supports

- [[performance-paradox]] — assisted output and later unaided performance diverge.
- [[cognitive-offloading]] — behavior consistent with outsourcing practice, with mechanism not experimentally isolated.
- [[capacity-erosion]] — longer exposure is associated with larger cumulative learning deficits; general cognitive decline was not measured.

## Contradicts / Extends

- Extends [[bastani-guardrails-math-rct-2025]] across subjects and longer follow-up, with weaker causal identification than randomized access.
- Qualifies [[novice-vulnerability]]: younger students showed larger losses, but so did higher prior achievers; vulnerability is not a simple low-skill gradient.

## Limitations

Self-selected adoption, retrospectively reported onset, one county, changing AI tools and incomplete histories for younger cohorts. Platform access-to-submission time is a proxy for effort, not a direct measure. No randomized tutoring-versus-outsourcing comparison. The 1.4-SD monthly estimate uses the compressed variance of scores averaged across subjects; it must not be compared directly with subject-level effect sizes (p.4). Percentages refer to the baseline mean, not percentage-point exam grades.

## Open Questions

- Can direct usage records distinguish tutoring from copying?
- Do the exceptionally large estimates reproduce in other settings and independent data?
- What intervention improves learning? The authors explicitly caution that mandated time alone may not work (p.20).
- County-exam coverage is described as grades 7/9 on p.6 and 9/12 on p.13. Clarify before using that robustness subgroup as a precise factual claim.
