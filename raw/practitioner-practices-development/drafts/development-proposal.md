# Developing practitioner practices in the KB

Date: 2026-09-26  
State: direction agreed; outcome taxonomy and implementation details remain open. No canonical entries migrated.

## Recommendation

Build a separate `practices/` collection, using the existing `sources/` records and ingestion process. This replaces the initial recommendation to keep practices in `methods/`. Research-derived and practitioner-derived practices belong together. Source type does not determine the destination.

Practices specify actions someone can try in a particular situation. Concepts explain phenomena; descriptive frameworks and broader methods organize an approach. During implementation, review the existing actionable methods for migration, preserve links, and update the indexing and validation tools. Do not create duplicate entries in both folders.

The central question: **What does this way of using AI let a person practise, understand, judge, or create?** Faster output can be useful, but does not by itself answer that question.

The user accepted the proposed practice format. Keep the [four worked examples](sample-practices.md) as format illustrations, not a preselected ingestion batch. Refresh the [source collection](source-shortlist.md) before extracting practices afresh.

## What is missing today

The current README already permits research and documented practice. CONTRIBUTING permits expert methods and practitioner observations. The gap is therefore partly in execution:

- The method template asks “Why It Works,” even when effectiveness has not been tested.
- The article and transcript playbooks emphasize concepts and supporting sources; actionable routines are easy to miss.
- `solid / emerging / speculative` alone does not tell readers whether they are seeing a tested intervention, a first-person account, or an editorial suggestion.
- Some existing methods turn research into stronger prescriptions than the source description warrants. For example, [[think-first]] specifies a 15–30-minute solo period; [[socratic-partnership]] contains a five-exchange rule. Those precise rules need their own provenance. Research on a related risk is not validation of a proposed routine.
- The user deleted the previous `extracted-practices.md` files so the next review starts from refreshed originals. Do not recreate or rely on those prior extractions.

## Two separate assessments

### 1. Is this source worth using for this practice?

Look for:

1. **Relevant experience:** the person does or teaches the work being described. A degree or audience size is not enough; a degree is not required.
2. **An inspectable account:** a named person, date, original article or recording, and a precise section or timestamp.
3. **Concrete process:** a task, sequence, example, and the person's decisions—not only a prompt or an opinion.
4. **Honest boundaries:** failures, rejected outputs, prerequisites, costs, or uncertainty.
5. **Interests and dependencies:** products, consulting, courses, sponsorships, and links between supposedly independent accounts. Record what is known; use “not checked” rather than “none.”

Trust is scoped to a domain and a particular contribution. Do not approve an author's entire catalogue. A useful practice may come from an otherwise promotional article; extract it only if it can stand on its own.

### 2. What supports the claimed benefit?

Record the basis in plain language:

| Basis | What it establishes | What it does not establish |
|---|---|---|
| Proposed exercise | A procedure and rationale exist | Someone used it successfully |
| First-person account or demonstration | Someone reports using it, or shows an example | Typical results, causal effects, lasting learning |
| Documented field use | Use and outcomes in a stated setting | Transfer to other people or tasks |
| Direct evaluation | Outcomes under the tested conditions | Benefits beyond the measured outcomes and setting |

Separately record **related research**, **counterevidence**, and **what is untested**. These are not rungs on a single quality ladder: a controlled study and a rich practitioner account answer different questions.

Keep existing status tags. Add the evidence distinction in the body first, without changing the schema. Practitioner entries can be useful with `emerging` status. Reserve strong benefit claims for evidence about that benefit—not the author's reputation or repeated retelling.

## A short practice entry

Use this structure for entries in `practices/`; keep the descriptive method format for frameworks. A working template is saved at `tooling/templates/practice.md`.

1. **Use when:** a recognizable situation, desired benefit, and prerequisites.
2. **Try it:** a few steps, separating the person's work from AI's contribution. Prompts optional.
3. **Origin:** who described the practice; exact source locator. Identify any editorial name, adaptation, timing, or extra step.
4. **Evidence and rationale:** observed use, direct evaluation if any, related research, and missing evidence.
5. **Limits:** failure conditions, unsuitable settings, and what to check outside AI.
6. **What to notice:** one useful observation on the work and, when relevant, a later attempt without the same assistance.
7. **Related:** existing concepts and methods, with the relationship stated.

Avoid requiring a new experiment or daily habit for every reader. An observation can be as small as recording one rejected suggestion and why it was rejected.

## Develop the outcome taxonomy through source review

The initial five-item outcome list was insufficiently developed and is not adopted. Thinking, judgment, creativity and intellectual sovereignty are the user's motivating concerns, not a closed coding scheme.

For each reviewed source, first record:

- The author's stated purpose and outcome, preserving their wording and locator.
- What the person actually does and in which situation.
- What changed, if anything, and whether that was observed, self-reported, measured or only proposed.
- An optional curator interpretation, clearly separated from the author's claim.

Then compare across different practices and domains. Group recurring outcomes, retain exceptions and overlaps, and examine where the same label means different things. Bring a proposed taxonomy back for discussion after this review. Do not assign the old five labels by default or force one outcome per practice.

Keep output quality, unaided capability, felt competence and calibration distinguishable when they occur in the evidence. These are reading safeguards, not the final outcome taxonomy. Consider accessibility and task differences; avoid treating a particular solo-first routine as universally desirable.

## Screen the full collection before selecting close reads

1. Refresh original articles and prepare the new book source. Identify previews, missing transcripts, duplicates and access limits.
2. Screen the entire collection using the [screening protocol](../screening/screening-protocol.md). Closely read the sources or sections that pass; keep borderline cases, access gaps and reasons for setting items aside visible. Collect author-stated outcomes without fixing the taxonomy first. Work in batches without limiting the scope to a small pilot.
3. Route selected originals through the librarian: catalog → triage → distill → critique → integrate. Preserve the existing recorded Decision gates. Downloading is not inclusion.
4. Search both existing methods and proposed practices for overlap. Plan migrations or variants when the human action is essentially the same.
5. Before the first practice integration, add `practices/` support to the librarian, validators, search, index and knowledge-pack tooling. Update contributor guidance and move selected existing practical entries with link checks. This implementation is still pending.

**Success:** selection is traceable across the full collection; a reader can choose and try a resulting practice, identify its source and limits, and tell which benefit is observed versus hoped for.

## Inspection limits

Reviewed the index, templates and workflow; inventoried the inbox; inspected selected original articles and transcript passages. This was not a full audit of the inbox or existing methods. The standard KB search could not start because of a local uv cache error; overlap checks used the index, filenames and selected method files. Live checks covered selected primary webpages and institutional profiles; they did not validate every author's credentials or interests.
