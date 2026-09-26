# Log: hermann-genai-psychology-work-2025

## 2026-04-29T20:00:00Z — cataloged
- Extractor: pypdf
- Format: pdf ({'pages': 12})
- Word count: 8982
- Heuristic source_type: article

## 2026-04-29T23:15:00Z - triaged: DEFER
- Hermann et al. (2025) - comprehensive review of GenAI psychology of work. High-priority for next session.

## 2026-04-30T10:00:00Z — workbench renamed
- From: hermann-puntoni-morewedge-2025-genai-and-the-psychology-of-work
- To: hermann-genai-psychology-work-2025
- Reason: citability; matches recent rename pattern (bartos / sharma / perry)

## 2026-04-30T10:05:00Z — triaged: INCLUDE (re-triggered from DEFER)
- *Trends in Cognitive Sciences* Opinion piece, ~9,000 words. Synthesis of GenAI-and-work psychology through SDT/BPNT.
- Relevance HIGH (Risk + Erosion + Preservation), Quality HIGH (top venue, integrative framing).
- Extractable: BPNT triad, five-strategy coping taxonomy, paradox-of-expertise. Conservative: 1 NEW concept candidate (paradox-of-expertise) + 1 NEW method candidate (identity-threat-coping); rest UPDATE.

## 2026-04-30T10:30:00Z — drafted
- drafts/source.md: substantial distillation, 8 Key Passages with [p.N] locators, integrated Supports + Contradicts/Extends + Open Questions
- drafts/concepts/paradox-of-expertise.md (NEW; status emerging): senior-level mirror of novice-vulnerability; comparison table to novice-vulnerability; explicit "What It Is Not" carve-outs from neighbouring constructs
- drafts/methods/identity-threat-coping.md (NEW method; status emerging): five-strategy taxonomy with full mapping table + diagnostic procedure + strengths/limitations
- drafts/updates/professional-identity-threat.md: BPNT three-needs decomposition + paradox-of-expertise + identity-threat-coping linkage
- drafts/updates/agency.md: algorithmic cage + decoupled accountability + surveillance as workplace-deployment autonomy threats
- drafts/updates/novice-vulnerability.md: BPNT framing + paradox-of-expertise as senior mirror
- drafts/updates/ai-self-efficacy-erosion.md: comparison-threat + deskilling-by-offloading mechanisms
- Decision: PROCEED_TO_CRITIQUE (1 NEW concept + 1 NEW method + load-bearing UPDATEs warrant Stage 4)

## 2026-04-30T11:00:00Z — critiqued: READY
- All 7 drafts pass Evidence + Practitioner + Adversarial lenses
- AI Failure Checklist clean (citations match, no statistical drift, no construct conflation, no false novelty, status appropriately set to emerging for both NEW entries)
- Minor revision: added [Inference] flag to "What To Do" diagnostic procedure in identity-threat-coping.md (procedure extends source taxonomy)
- Decision: PROCEED_TO_INTEGRATE

## 2026-04-30T11:05:00Z — validated
- validate_drafts.py: 0 findings, clean on first pass
- Status: READY for Stage 5 integrate

## 2026-04-30T11:15:00Z — integrated
- drafts/source.md → sources/hermann-genai-psychology-work-2025.md
- drafts/concepts/paradox-of-expertise.md → concepts/paradox-of-expertise.md (NEW concept, status emerging)
- drafts/methods/identity-threat-coping.md → methods/identity-threat-coping.md (NEW method, status emerging)
- UPDATEs applied to: concepts/professional-identity-threat.md, concepts/agency.md, concepts/novice-vulnerability.md, concepts/ai-self-efficacy-erosion.md
- Aux scripts: sync-source-links.py + build-index.py + update_readme_counts.py all clean
- KB counts: 64 sources / 56 concepts / 12 methods / 132 total entries
- drafts/concepts/ and drafts/methods/ subdirs removed; drafts/updates/ retained as evidence trail
- Status: integrated

## 2026-09-26 — six-group audit correction integrated

- A03/A25 propagation only: learning bias adjustment not transferable to workplace productivity; felt competence and learning measures not one established mechanism.
- Approval: Fix; Six high-priority groups only. Batch: kb-audit-corrections-2026-09-26.
- Three-lens self-review and draft gate passed. This is a scoped correction, not complete re-review of unchanged claims. Original files and prior decisions preserved.
