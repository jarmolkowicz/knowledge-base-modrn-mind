# Independent evidence review: judgment and complementarity

Date: 2026-09-26

## Scope and decision status

Read-only audit of older, pre-Julia-PARTIAL claims in `concepts/judgment.md`, `methods/complementarity-framework.md`, and `concepts/conversational-steering.md`. Read the index, relevant public source entries, and available primary extracted texts. No public entries changed. Recommendations below await a recorded decision and the applicable integration gate.

All paths below are relative to the KB root. Line numbers refer to the files as reviewed on this date.

## Corrections recommended

| Entry / line | Claim | Assessment | Primary evidence / smallest correction |
|---|---|---|---|
| `concepts/judgment.md:18,45`; `methods/complementarity-framework.md:22` | Gonzalez et al. 2026 / PNAS Nexus attribution; quoted ethical-authority and “low-agency advisor” statements | UNVERIFIED | No matching source entry, original workbench, or extracted primary text found. Author/title/quotes need the original. Mark missing source; do not present quotations as verified. Other KB mentions of Gonzalez concern a different Nature Reviews Psychology paper. |
| `concepts/judgment.md:26–34` | Duncan’s five-type taxonomy; “Each type develops through different experiences and erodes through different mechanisms…” | UNVERIFIED | No Duncan source/workbench found. Taxonomy already labelled practitioner framework, appropriately; attribution still needs original. Remove erosion sentence or label `[Speculation]`: no evidence establishes five distinct erosion mechanisms. |
| `concepts/judgment.md:47` | Leonardi & Leavell “demonstrate…AI undermines expert judgment” | OVERSTATED | Primary `raw/leonardi-artificial-certainty-2026/source.md:33,69–71,255–257` (PDF pp.2–3 and methods): comparative ethnography of two planning organizations examines expert authority, not measured loss of judgment capability. Replace opening with “In two planning organizations, Leonardi & Leavell describe how AI representations can undermine expert authority.” Keep enhancement/modulation distinction, scoped to cases. |
| `concepts/judgment.md:51` | AI “erodes the experiences” and “eliminat[es] the developmental struggle” | OVERSTATED | No cited primary evidence here establishes inevitable removal across the professions listed. Use `[Inference] AI may reduce judgment-building practice when it replaces tasks through which novices learn.` |
| `methods/complementarity-framework.md:26,30,62` | Teams only outperform with deliberate complementary design; interrogation produces best performance | UNVERIFIED / OVERSTATED | Missing Gonzalez original. Vaccaro’s primary synthesis establishes heterogeneous outcomes, not necessary/sufficient design conditions: `raw/vaccaro-human-ai-meta-analysis-2024/source.md:109–135` (PDF p.3). Change to proposed design guidance, not universal empirical rule. |
| `methods/complementarity-framework.md:46` | Nonsignificant explanation/confidence moderators → explanations insufficient for calibrated trust | OVERSTATED | Vaccaro primary `raw/vaccaro-human-ai-meta-analysis-2024/source.md:78,119` (PDF pp.2–3) reports nonsignificant performance moderators. It does not establish no benefit or directly test this universal trust-calibration conclusion. Say “The meta-analysis found no statistically significant performance moderation by explanations or confidence displays.” |
| `methods/complementarity-framework.md:46` | Absent deliberate friction, “calibrated trust drifts toward…over-acceptance” | OVERSTATED | Dell’Acqua primary `raw/dellacqua-cybernetic-teammate-2026/source.md:1515–1539,1557–1564` (PDF pp.16–17) presents affirmation, weaker internalization, and explanations as possible mechanisms. Trust drift/friction mechanism not isolated. Keep selection result; say “Authors propose affirmation as one possible explanation; not directly tested.” |
| `methods/complementarity-framework.md:48` | Vaccaro “empirically confirms” strategic-task/general complexity rules; creation tasks “showed performance gains” | OVERSTATED | Primary `raw/vaccaro-human-ai-meta-analysis-2024/source.md:131,137` (PDF p.3): creation synergy g=.19, p=.180, CI −.09 to .48; decision/creation difference significant. Does not directly establish “complex uncertain” versus “well-defined strategic” rules. Replace with measured distinction and nonsignificant creation estimate; retain relative-ability moderator. |

## Verified claims to retain

- `concepts/conversational-steering.md:21–23`: VERIFIED. Werner primary `raw/werner-conversational-ai-steering-2024/source.md:549–573,599–608,641–652` (PDF pp.16–19): N=528; .70 versus .34 choice; 38.8% not detecting; seller-interest disclosure; no neutral control. Current caveats correctly avoid individual-reversal and causal-awareness claims.
- `methods/complementarity-framework.md:45`: VERIFIED with scope. Dell’Acqua primary `raw/dellacqua-cybernetic-teammate-2026/source.md:1583–1594,1792–1801` (PDF pp.17,20) supports authors’ sequential-expansion interpretation and approximate 3× top-decile comparison against individual/no-AI. Keep as authors’ interpretation of between-condition results; not longitudinal team expansion or AI-alone synergy.
- `methods/complementarity-framework.md:46`: selection difference VERIFIED; mechanism not. Primary Dell’Acqua `raw/dellacqua-cybernetic-teammate-2026/source.md:1427–1447` (PDF p.15): approximately 50% versus 37%; AI-assisted final selected outputs still higher quality.

## Additional concrete source-entry error

`sources/dellacqua-cybernetic-teammate-2026.md`, “Performance” paragraph: p=.242 assigned to the wrong comparison. Primary Table 2, `raw/dellacqua-cybernetic-teammate-2026/source.md:1145–1153` (PDF p.11), labels this Team+AI versus Team No AI, not Team+AI versus Individual+AI. Proposed correction: change the comparison label. This source-entry correction also awaits decision.

## Coverage limits

Substantive pre-PARTIAL claims in the three assigned entries were reviewed. Original extracted papers checked for Werner, Vaccaro, Dell’Acqua, and Leonardi; these are primary research or primary research synthesis, not secondary commentary. Gonzalez and Duncan provenance remains unavailable in the inspected KB files. New PARTIAL additions were not re-reviewed. Missing originals were not resolved externally. No claim here that an unavailable original does not exist; UNVERIFIED means the local evidence could not establish the attribution or claim.
