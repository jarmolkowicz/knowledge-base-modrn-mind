# Practice source screening — results

2026-09-26. **881 items accounted for; 15 sources selected for closer review.** A first-pass screen of the full inventory, not full reading of every source. No practices approved or integrated.

Start with the [annotated shortlist](shortlist.md). Every item remains in the [complete register](screening-register.md), with a decision, reason and reading coverage. Original sources remain where they were.

## Findings

The clearest candidates describe a specific action and show someone using it: feedback without rewriting, retaining a disputed creative choice, testing AI on realistic tasks, inspecting actual errors, or answering practice questions before seeing explanations. Proposed exercises are also useful leads; their promised benefits need separate assessment.

The shortlist includes Hogue, Mollick, Newport, Gridley, Husain/Shankar, Duke, Illingworth's book and creative contributors, the HBR team-practice article, and explicitly flagged candidates. Contributor accounts are attributed to those people, not automatically to newsletter hosts.

Trust should attach to a particular account or claim. An author can supply a useful procedure and unsupported benefit claims. Commercial language alone does not disqualify a source; professional status alone does not establish effectiveness. This screen establishes no improvements in unaided thinking, learning or judgment.

## Coverage

| Final queue | Items | Meaning |
|---|---:|---|
| Selected for closer review | 15 | 7 extraction leads, 6 flagged leads, 1 transfer source, 1 counterexample |
| Further priority leads | 239 | Plausible AI-related practice passages; detailed assessment needed |
| Transfer leads | 161 | Human reasoning, craft, learning or team routines; AI adaptation needs justification |
| Context | 184 | Lower immediate priority in inspected material; not whole-source rejection |
| Discovery | 47 | Pointers, compilations, teasers or original-source leads |
| Access holds | 198 | 151 restricted previews, 43 show notes, 2 near-empty files, 2 incomplete guides |
| Provenance holds | 23 | Conflicting titles/guests or copies requiring reconciliation |
| Repeated transcript bodies | 12 | Identical normalized bodies; not independent evidence |
| Internal material | 2 | Author-owned input, not independent external support |
| **Total** | **881** | Includes duplicates; not 881 independent sources |

Most available article/transcript bodies received an opening, a cue-ranked passage and headings where present. Some packets are very short. They support a provisional reading queue, not reliable exclusion or a representative map of practices. Long interviews may contain relevant material elsewhere; sponsor text can produce misleading cue matches.

The 194 previously known access gaps received metadata/access screening, not full-content assessment. Further reading found four more access problems. Older downloads may also be incomplete; unverified access remains marked.

Both books received a section-level screen and expanded reading of selected sections, not cover-to-cover reading. All six pages of the local PDF were extracted and inspected. Selected articles and transcript passages received expanded reading; each shortlist entry states its coverage.

A purposive lower-priority check revisited nine articles across Grant, Newport, Hassid and Ramonov (IDs 0, 9, 15, 26, 48, 264, 285, 365, 366). It caught two missing promised procedures and a video-only teaser. This was not a random audit and cannot estimate a miss rate. No source was rejected on content.

Automated cues supplied navigation; decisions came from inspected passages. Practitioner credentials were not comprehensively verified. Research cited by practitioners was not systematically re-reviewed. The shortlist records each account's basis and limits, not an overall author trust score.

## Issues before extraction

**Attribution:** Some podcast titles conflict with metadata/body identity. ID541's title names Nilan Peiris while metadata/body identify Alexander Embiricos. Check originals before attributing practices. The automated [provenance audit](provenance-audit.json) includes false positives when a title merely omits the guest's name; its flags are not verdicts.

**Duplicates:** Twelve transcript bodies are identical after whitespace normalization. These overlap the earlier 31 duplicate candidates; do not add the counts. Shared URLs with different bodies still need comparison. No originals removed or merged.

**Completeness:** IDs279 and 336 contain almost no text. IDs264 and 285 stop before promised instructions. Previews and show notes remain discovery leads, not substitutes for missing accounts.

**Claims:** The memory-check example is a useful counterexample: asking a model to question itself did not prevent an invented source. External checking mattered. Other candidates confuse challenge with truth, fluency with authorship, or assisted output with lasting learning. Preserve these limits in critique.

**PDF bibliography:** Its local export lacks a byline. Authors and publication date were checked against the [NOVA university record](https://novaresearch.unl.pt/en/publications/design-ai-systems-that-actually-strengthen-human-reasoning-strate/). Details are in the shortlist. Six local printed pages versus ten catalog pages may reflect formatting; page count alone did not establish missing text.

## Next use

Use the 15 sources as a starting reading batch, with the 400 other priority/transfer leads still visible. This is no fixed cap or claim that the shortlist contains the collection's best sources.

Extract source-faithful candidates through the existing per-source workflow, reusing book workbenches. Separate what the practitioner did, what they report happened, what research supports, and any proposed adaptation. Record decisions before canonical integration. The separate practices collection still needs workflow/indexing support before publication.

Keep the outcome taxonomy open. During close reading, record outcomes each source actually names and how they were assessed. Distinguish assisted output, unaided capability, subjective confidence and calibration. Compare apparent gaps against the wider queue and access holds before adopting categories.

[Inference] The shortlist is richer in writing, knowledge work and software/product settings than other practices. Accessibility-related leads in the wider collection and culturally varied settings need deliberate follow-up. Repeated Illingworth material is one publication network, not independent confirmation. This screen cannot establish field coverage.

## Audit trail

- [Register data](screening-register.json): decisions, original navigation, paths and hashes.
- [Shortlist data](shortlist.json): attribution, basis, limits, contribution, locators and coverage.
- `inspection-packets/`, `book-inspection-packets.json`, `expanded-*.json`: saved reading passages.
- `content-decisions.tsv`, `podcast-decisions.json`: first-pass judgments; publication script applies documented expanded-reading and duplicate overrides.
- [PDF text](pdf-screening-text.md) and [extraction metadata](pdf-screening-metadata.json).

Validation: all 881 IDs have one final disposition; all 881 source hashes matched the saved records/extraction hash. This checks inventory consistency, not source-claim accuracy.
