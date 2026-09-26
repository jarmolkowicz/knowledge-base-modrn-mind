---
status: emerging
area: [risk, preservation]
type: paper
sources:
  - "Topaz, M., Roguin, N., Gupta, P., Zhang, Z., & Peltonen, L.-M. (2026). Fabricated citations: an audit across 2·5 million biomedical papers. The Lancet, 407, 1779–1781."
---

# Topaz et al. (2026) — Fabricated Citations in Biomedical Papers

## Citation

Topaz, M., Roguin, N., Gupta, P., Zhang, Z., & Peltonen, L.-M. (2026). Fabricated citations: an audit across 2·5 million biomedical papers. *The Lancet*, 407, 1779–1781. Correspondence, 9 May 2026.

## Type

Research correspondence reporting a large reference-integrity audit. PDF page 3 also contains an unrelated letter, excluded from this distillation.

## Key Insight

A plausible reference can survive publication while pointing to no identifiable study. The audit found a sharp rise in fabricated references, but it cannot establish whether AI caused that rise.

## Evidence

The authors scanned 2,471,758 papers in PubMed Central's Open Access subset, dated 1 January 2023–18 February 2026. They verified 97.1 million references carrying PubMed identifiers, out of 125.6 million structured references; 23% without identifiers were excluded.

Their pipeline compared claimed metadata with PubMed and Crossref records, removed parsing artefacts, used Claude 3.5 Haiku to screen discrepancies, and checked remaining candidates against PubMed, Crossref, OpenAlex, and Google Scholar. A title found under a different identifier counted as a reference error, not a fabrication.

The pipeline identified 4,046 fabricated references across 2,810 papers. A masked 500-entry assessment by three reviewers estimated 91% precision; recall was not measured. Most affected papers contained one or two fabricated references.

Two rates must remain separate:

- **Affected papers:** approximately one in 2,828 in 2023, one in 458 in 2025, and one in 277 in early 2026.
- **Fabricated references per 10,000 papers:** approximately four in 2023, 51.3 in Q4 2025, and 56.9 in early 2026. This counts references, not affected papers.

## Key Passages

> "Each reference implicitly asserts that a verifiable source exists and supports the claims being made."
> — Topaz et al., PDF p.1 / journal p.1779

> "Our system identifies the problem, not its cause."
> — Topaz et al., PDF p.2 / journal p.1780

## Relevance

A source that looks scholarly still needs verification. Publication, plausible author names, and a valid-looking identifier do not establish that the cited study exists. The authors recommend checks before peer review, integrity metadata, retrospective screening, and a distinct tracking category for fabricated references.

## Supports

- [[reference-verification]] — a tested detection workflow, with explicit limits on coverage and precision.
- [[agency]] — [Inference] taking responsibility for an AI-assisted claim requires checking its evidence.
- [[fluency-bias]] — [Inference] plausible formatting may conceal a broken reference; this audit does not experimentally test processing fluency.

## Contradicts / Extends

- Extends: [[messeri-crockett-illusions-understanding-2024]] — adds observed damage to evidence traceability, distinct from the perspective's account of perceived understanding.
- Extends: [[workslop]] — [Inference] a specific example of apparent completeness shifting verification work downstream.

## Open Questions

- How many fabrications escape the filters, or occur among references without PubMed identifiers?
- How much of the trend reflects LLM use, paper mills, indexing changes, or other causes? Timing alone cannot resolve this.
- The 2026 estimate covers only seven weeks; the sample excludes closed-access biomedical papers.
- Non-retrieval across four databases is not absolute proof of non-existence. The estimated precision implies some false positives.
- The supplied correspondence references an appendix that is absent from this three-page PDF. Case-level validation details cannot be independently checked here.
