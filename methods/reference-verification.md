---
status: emerging
area: [preservation, risk]
sources:
  - "Topaz, M., Roguin, N., Gupta, P., Zhang, Z., & Peltonen, L.-M. (2026). Fabricated citations: an audit across 2·5 million biomedical papers. The Lancet, 407, 1779–1781."
---

# Reference Verification

## Overview

Check whether a reference names a real publication before relying on it. Topaz et al. (2026) demonstrate an automated workflow for biomedical references; a separate human check is needed to establish whether the real publication supports the claim.

## What It Is / How It Works

The published workflow compares a reference's claimed title and other metadata with the record attached to its identifier. It removes parsing artefacts, screens remaining discrepancies, and searches multiple scholarly databases. A wrong identifier for an existing title is a reference error; a title not found in any searched database is a candidate fabrication.

## What To Do

The first four steps adapt the authors' workflow for reference checking:

1. Retrieve the record behind the supplied DOI or PubMed identifier.
2. Compare title, authors, year, and publication venue with the claimed reference.
3. Resolve mismatches across more than one registry; distinguish transcription and formatting errors from an apparently non-existent study.
4. Record unresolved references for human review before accepting them.
5. [Inference] Open the real paper and check the cited claim and page. Identifier verification alone does not validate what the paper supposedly shows.

## Why It Works

The audit covered 97.1 million references with PubMed identifiers. Its pipeline identified 4,046 fabricated references and achieved an estimated 91% precision in a masked 500-entry human assessment. It demonstrates detection at scale, not perfect verification or proof that every absent record is fabricated. See [[topaz-fabricated-citations-2026]].

## Strengths / Limitations

- Strength: catches convincing references whose metadata do not match an identifiable work.
- Limit: the audit excluded references without PubMed identifiers; recall was unknown.
- Limit: database absence can reflect incomplete coverage.
- Limit: the paper's LLM screening stage is not a substitute for registry lookup and human review.
- Limit: preventing publication of errors was recommended, not tested as an intervention.

## When It Applies

Use when curating references, preparing research summaries, or reviewing AI-assisted writing. A verified reference may still contain poor evidence or be cited misleadingly.

## Related

- [[agency]] — responsibility for the evidence behind a claim.
- [[fluency-bias]] — polished presentation does not establish validity.
- [[workslop]] — prevents unresolved evidence checks from being handed to the next reader.

## Sources

- [[topaz-fabricated-citations-2026]] — Topaz, M., Roguin, N., Gupta, P., Zhang, Z., & Peltonen, L.-M. (2026). Fabricated citations: an audit across 2·5 million biomedical papers. The Lancet, 407, 1779–1781.
