# Independent evidence review — identity and loneliness

Date: 2026-09-26

## Scope and decision boundary

Independent read-only review of older claims in `concepts/professional-identity-threat.md`, `methods/identity-threat-coping.md`, and `concepts/ai-loneliness-effect.md`. Public summaries checked against local original extracted text. No public entries changed. Recommendations below await a recorded decision before correction drafts and integration.

Main risks: causal overclaims; two direct contradictions; unclear denominators. All paths below are relative to the repository root. Entry line numbers refer to the reviewed working-tree snapshot.

## Corrections needed

| Entry / line | Exact claim | Verdict | Primary evidence | Smallest correction |
|---|---|---|---|---|
| `concepts/professional-identity-threat.md:33–35` | “quantitative floor” of identity pressure; “most acute” in Job Zone 4 | **OVERSTATED** | `raw/handa-economic-tasks-claude-2025/source.md:209–214,433–470`, pp.5,12: users need not work in mapped occupation; downstream use unknown; identity not measured. | Retain occupational task percentages as usage context. Remove identity-risk prevalence and occupational ranking. |
| Same:37,79 | Hai measured “identity threat” / “the same identity-and-meaning erosion” | **OVERSTATED** | `raw/hai-dark-side-collaboration-2025/source.md:490–504`: measures collaboration, work alienation and self-reported expediency—not professional identity or skill erosion. | Call outcome **daily work alienation**; label connection to identity `[Inference]`. |
| Same:49,55,66–71 | “leads to”; “reveals the mechanism”; “causal sequence”; “eventually distorts” | **OVERSTATED** | `raw/keshky-illusory-competence-2026/source.md:81,1784,3384–3388`: researcher-developed scales and SEM; no temporal manipulation. Public source itself flags cross-sectional design. | “Cross-sectional associations fit the proposed mediation model; direction and causal mechanism remain unestablished.” |
| Same:55 | indirect effect “p = .05” | **UNVERIFIED / conflicting reporting** | Keshky English abstract line81 and results table line3388 give **.04**; Arabic abstract/discussion lines141,3686 give **.05**. β=.35 consistent. | Omit exact p, or report table p=.04 and explicitly note discrepancy. Do not silently choose. |
| Same:75 | “AI evaluation reduces self-efficacy, which triggers self-objectification”; “identity erosion follows” | **OVERSTATED** | `raw/alessandro-self-efficacy-2025/source.md:83,141,250,423–431`: recruiter condition randomized; mediators measured and modeled. Identity erosion not measured. | Retain experimental differences; describe indirect pathway as **consistent with mediation**, not established causal chain or identity erosion. |
| Same:81 | “Where digital demands are well-resourced and bounded…does not measurably erode meaning” | **OVERSTATED** | Hai raw lines476–487 define digital demands, not resource provision; lines629–631 low-demand slope nonsignificant; lines954–965 explicitly limit causal conclusions. | “Association with alienation was nonsignificant at low digital demands; this does not establish no harm or a protective intervention.” |
| Same:83,107,122 | alienation “channels into” ethical withdrawal; multiple designs anchor “BPNT-mediated identity-threat thesis” | **OVERSTATED** | Hai raw lines499–504 uses self-reported expediency; lines954–965 causal caveat. Wu measures control, motivation and boredom—not identity or the full BPNT mediation chain. | Report observational indirect association and separate experimental outcomes. Remove claims of a demonstrated shared causal mechanism. |
| Same:105,124 | sustained collaboration “did not buffer…boredom increases” | **OVERSTATED—direct contradiction** | `raw/wu-collaboration-motivation-2025/source.md:1000–1007`, p.22: Collab–Collab showed **less boredom increase** than Collab–Solo; interaction F=4.85, p=.028. | “Sustained collaboration did not prevent boredom rising, but reduced its increase relative to switching to solo work.” |
| Same:105,124 | d=.32–.51 presented as general collaboration effect | **OVERSTATED framing** | Wu raw tables/results pp.5–22: these are within-condition task changes; solo controls also changed; Study2 motivation interaction nonsignificant and Study4 boredom versus Solo–Solo nonsignificant (lines440–441,983–988). | Label effect sizes **within-person Collab–Solo changes**, not AI-versus-control effects; name inconsistent interactions. |
| Same:103 | effect “persists across industries and roles”; general automation reduces self-determination | **OVERSTATED** | `raw/nikolova-robots-meaning-2024/source.md:38,248–250`: industrial robots; meaningfulness/autonomy strongest; competence/relatedness less robust; substantial task/role heterogeneity. | “Industrial-robot exposure was linked to lower meaningfulness and autonomy; effects varied by task and role. GenAI generalization remains an inference.” |
| Same:45,91–94,112–113 | quoted common sentiment; unassisted work restores authorship/self-efficacy; practices “restore” identity | **UNVERIFIED** | No named primary source for exact quotation or restoration intervention. Hermann raw line519 says editors versus co-creators, but as a secondary synthesis, not this quotation. | Remove quotation marks/“common”; attribute theoretical framing. Mark restoration as an untested proposal, not measured benefit. |
| `methods/identity-threat-coping.md:25,49–51,66,72,93` | escapism “most maladaptive”; taxonomy “predicts which strategy is adaptive”; interventions restore autonomy/competence; novices particularly susceptible | **OVERSTATED / UNVERIFIED** | `raw/hermann-genai-psychology-work-2025/source.md:601–615,630–639,719–750`, pp.7–9: **Opinion** proposes framework; conditional costs; explicitly says responses are not black-and-white and more research needed. No GenAI strategy-comparison trial or novice moderation. | Remove universal ranking and novice claim. Use “may”; rename procedure **discussion aid**, not validated diagnosis/intervention. Existing limitations correctly acknowledge this but main text contradicts them. |
| Same:29 | Table3 “[p.7]” | **Incorrect locator** | Hermann raw line644, **p.8**. | Change to p.8. |
| `concepts/ai-loneliness-effect.md:44` | “severe-attachment” distribution; “roughly 25%” collapsed support systems | **OVERSTATED / denominator unclear** | `raw/sharma-disempowerment-patterns-2026/source.md:1412–1418,1534–1542,1592–1597`, Figures10,12: quantitative cluster descriptions from **moderate OR severe** cases; reliance=70 descriptions/3,850 conversations; attachment=65/4,150. | Name selected moderate/severe subsets and cluster-summary method. Do not imply 25% of all users or severe-only distribution. |
| Same:68 | anthropomorphizers “wrote no more warmly and disclosed no more” | **OVERSTATED—direct contradiction** | `raw/folk-heine-dunn-anthropomorphism-2025/source.md:237–238`, p.4: warmth r=.17 and disclosure r=.12, **both p<.001**; similar associations across conditions. | “Small positive associations with warmth and disclosure occurred in both conditions; these did not explain the chatbot-specific connection advantage.” |

## Verified checks and bounded recommendations

- **Handa percentages** ~36% / 11% / 4%: match raw p.7, lines249–265. Problem is interpretation, not numbers.
- **Hai coefficients** .14, .30, .34, .04 and conditional indirect .06 [.010,.118]: match raw results lines610–638. Preserve as associations.
- **Alessandro sample** 571 = 128+225+218: raw lines81,203,341. Three experiments supported.
- **Wu sample 3,562; control drop Δ−1.01, d=.84**: match raw lines8,738,752. Restricted task context; not enduring identity loss.
- **Coping five categories/table mapping**: accurately follows Hermann Table3, p.8; proposed application, not validated tool.
- **Folk–Dunn longitudinal coefficients/p-values**: match raw pp.5–6, lines430–440,502–513. Current noncausal wording sound.
- **Folk2025 interaction estimates, 58% / 72%, warmth/disclosure d=.31/.60**: match raw pp.2–5, lines113–129,203–220,304–305.
- **Latikka country samples and main age/distress/loneliness statistics**: match raw pp.7,11–15. Current cross-sectional caveat sound; keep population generalization bounded by online-panel selection/attrition, acknowledged pp.17–18.
- **Perry vulnerable-group account**: accurately attributed but theoretical Perspective. Change “identifies a population-level distribution” to **“proposes that vulnerability may differ”**.

## Coverage and limits

Targeted original-text checks for Keshky, Hai, Handa, Hermann, Wu, Alessandro, Nikolova, Sharma, both Folk papers, Latikka, Fang and Perry; public summaries checked alongside originals. This is a targeted claim audit, not a complete re-ingestion of each paper.

No new web research or uploads. Keshky Arabic extraction partly disordered; English abstract and numerical table checked, not a full Arabic-methods audit. De Mello and the newly integrated Julia sources not independently re-reviewed here.

## Recommended next step — awaits decision

Approve a bounded correction pass for the ledger above. Preserve verified numerical results; distinguish measured constructs, observational associations, experimental effects and theoretical proposals. Stage correction drafts and review before public integration. Do not expand this report into unapproved edits of other source entries.
