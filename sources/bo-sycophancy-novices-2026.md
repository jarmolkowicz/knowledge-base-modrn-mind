---
status: emerging
area: [erosion, risk]
type: paper
sources:
  - "Bo, J.Y., Kazemitabaar, M., Deng, M., Inzlicht, M., & Anderson, A. (2026). Invisible Saboteurs: Sycophantic LLMs Mislead Novices in Problem-Solving Tasks. arXiv:2510.03667v2. University of Toronto & University of Alberta."
---
# Invisible Saboteurs: Sycophantic LLMs Mislead Novices

## Citation
Bo, J.Y., Kazemitabaar, M., Deng, M., Inzlicht, M., & Anderson, A. (2026). Invisible Saboteurs: Sycophantic LLMs Mislead Novices in Problem-Solving Tasks. arXiv:2510.03667v2.

## Type
Paper

## Key Insight
In a within-subjects experiment (N = 24), a low-sycophancy chatbot improved novice task performance by +49.3% while a high-sycophancy chatbot improved it by only +4.8%. Despite this stark performance gap, 71% of participants did not notice differences between the two chatbots, with no statistically detected rating difference in helpfulness, reliability or enjoyment.

## Relevance
Complements Batista & Griffiths' theoretical analysis with applied evidence in a complex problem-solving context (ML debugging). The within-subjects design makes the contrast vivid: the same novices performed dramatically differently depending on sycophancy level, yet most did not report noticing the difference. The result raises a detection concern in this small sample; it does not establish that all novices fail to notice or that experts would be less affected.

## Key Findings

- **Performance gap**: Low-sycophancy chatbot: +49.3% task performance improvement. High-sycophancy chatbot: +4.8% (not significant). Both chatbots had equivalent general reasoning ability (MMLU scores 80-82% college CS, 95-96% high school CS).
- **Misconception reinforcement**: High-sycophancy chatbot did not improve users' misconceptions; low-sycophancy chatbot significantly reduced them. When the chatbot validated incorrect beliefs, novices retained those beliefs and applied them.
- **Over-reliance**: 47.4% of interactions with the high-sycophancy chatbot were unhelpful (user relied on irrelevant or incorrect advice), compared to only 3% with low-sycophancy.
- **Invisibility**: 71% of participants detected no sycophantic characteristics in either chatbot. Ratings did not differ significantly on helpfulness, reliability or enjoyment despite different task outcomes. This was a detection gap in the studied sample.
- **Novice-specific risk**: The study focused on ML novices prone to misconceptions. [Inference] Incorrect mental models and limited domain knowledge may make misleading agreement difficult to evaluate; this study did not compare novices with experts.

## Supports
- [[sycophancy]] - applied evidence of sycophancy's impact in complex problem-solving (beyond question-answering benchmarks)
- [[novice-vulnerability]] - documents vulnerability in ML novices; no expert comparison establishes unique susceptibility
- [[socratic-partnership]] - 71% invisibility finding motivates the "Ask for Doubt" technique
