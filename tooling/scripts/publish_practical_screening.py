# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Publish recorded human/assistant screening judgments; never infer them from cues.

Snapshot-specific: IDs address the 2026-09-26 register. Refuses changed sources,
missing judgments or repeated IDs. Retains initial navigation and prior reviews.
"""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'raw/practitioner-practices-development/screening'

# Source-specific assessments from expanded reading. Recommendations, not ingestion decisions.
SELECTED = [
 (459, 'read_for_extraction', 'Rebecca J Hogue, hosted by Sam Illingworth',
  'Feedback without rewriting', 'L28-80',
  'Short writing sample; request a limited number of improvement areas; human makes the edits and can reject advice.',
  'First-person use with a before/after example and explanation of the prompt constraint.',
  'Reported learning is not measured unaided transfer. Separate the exercise from platform privacy claims.', 'Body and worked example inspected'),
 (460, 'read_for_extraction', 'Sam Illingworth; co-editor Alyssa Fu Ward; named creative contributors',
  'Creative criticism with retained authorship', 'L61-84; L194-208',
  'Illingworth keeps a disputed poetic choice. Joshua Sherman describes revising his own lyrics after debate and building a checklist he uses without AI.',
  'Named first-person accounts with concrete creative decisions; Sherman records as First Radio On.',
  'Self-reports, not independent evaluations. Other contributors use different boundaries. Do not attribute every account to the editor or treat reuse as legal clearance.', 'Main body and contribution headings inspected; images not assessed'),
 (75, 'read_for_extraction', 'Ethan Mollick',
  'Test AI on the actual job', 'L40-62',
  'Use realistic tasks, repeated attempts and expert assessment to learn where a model works for a particular job.',
  'Worked model comparisons and research examples.',
  'Model rankings age quickly. Better assisted output does not establish stronger human judgment or learning.', 'Expanded body and evaluation examples inspected'),
 (652, 'read_for_extraction', 'Hamel Husain and Shreya Shankar, interviewed by Lenny Rachitsky',
  'Build evaluation from observed errors', '00:12:36-00:31:42; 00:56:28-00:57:18',
  'Inspect real traces, have a domain expert record failures, group errors, and compare automated judgments against human labels.',
  'Detailed consulting/practitioner account using the Nurture Boss case; explicit example of missing domain knowledge.',
  'Reliability of an AI system is the immediate outcome. Human capability growth remains unmeasured. ID653 repeats this transcript body.', 'Expanded timestamped passages; not the entire interview'),
 (658, 'read_for_extraction', 'Hilary Gridley, interviewed by Lenny Rachitsky',
  'Generate practice questions in the learner\'s work context', '01:26:34-01:29:49',
  'Her Aristotle GPT generates LSAT-style reasoning questions in a product context; the learner answers before seeing an explanation.',
  'First-person description of a tool she built and uses.',
  'Answer keys need expert checking. No measured unaided transfer; business judgment is broader than solving a logic question.', 'Expanded surrounding turns; not the entire interview'),
 (22, 'read_for_extraction', 'Cal Newport',
  'Check whether AI helps the real bottleneck', 'L23-39',
  'Identify valuable work and its bottleneck; judge tools by that work and protect time for it.',
  'Explicit author proposal illustrated by a reported researcher interview.',
  'No validation of this routine. Supporting aggregate productivity claims were not independently checked.', 'Entire short body inspected'),
 (255, 'read_with_flags', 'Melchior Tamisier-Fayard, Theodoros Evgeniou, Anne-Laure Fayard',
  'Design team routines that preserve independent reasoning', 'Local PDF p3-6',
  'Compare the Prompt with Me challenge, AI-free discussion, parallel human/AI work and interfaces that expose underlying evidence.',
  'Research synthesis and named organizational cases, including AstraZeneca and With Company.',
  'Trace cases to original accounts before making causal claims. Local export has no byline; authors/date verified in NOVA catalog. Its six printed pages differ from the catalog edition\'s ten pages; this alone does not establish missing content.', 'All six extracted PDF pages inspected'),
 (879, 'read_for_extraction', 'Sam Illingworth',
  'State your thinking before the prompt', '[ch.21] Conclusion, One thing to try this week',
  'Write what you think and what you need to know before asking AI; compare what changes and notice when your own answer was enough.',
  'Explicit exercise proposed in the book.',
  'Benefits are proposed, not demonstrated. Book and newsletter are not independent corroboration. Chapter marker is the EPUB document number.', 'Section-level screen across book; conclusion read in full'),
 (550, 'read_for_transfer', 'Annie Duke, interviewed by Lenny Rachitsky',
  'Independent input and advance stopping criteria', '00:25:18-00:30:14; 00:38:02; 01:06:18-01:08:59',
  'Collect judgments and reasons independently before discussion; attach future actions to signals that would justify stopping.',
  'Explicit decision practices and examples of use, including structured forms.',
  'AI adaptation would be an inference, not a tested method established by this interview.', 'Expanded timestamped passages; not the entire interview'),
 (512, 'read_with_flags', 'Laura O\'Driscoll, hosted by Sam Illingworth',
  'Question the assumptions in a belief or draft', 'L28-36; L56-80',
  'State a belief, invite clarifying questions, and examine assumptions; contributor also checks drafts for sweeping claims before publishing.',
  'Concrete prompt plus first-person repeated use and an example question.',
  'The model cannot reliably diagnose where a belief came from. Discomfort or reduced certainty is not evidence of improved accuracy; factual premises still need external checking.', 'Full available text inspected'),
 (437, 'read_as_counterexample', 'J Hong, hosted by Sam Illingworth',
  'Check claimed memories against external records', 'L32-60',
  'A model claimed a dream and a source file existed; the contributor searched actual records. Preserve this as a failure case for prompt-only checking.',
  'First-person failure account with a named checking action.',
  'The advertised self-check prompt did not stop fabrication. No proof that a false memory was implanted; the underlying dream remains unresolved.', 'Entire available body inspected'),
 (453, 'read_with_flags', 'Khaled Ahmed, hosted by Sam Illingworth',
  'Check correctness and completeness separately', 'L22; L32; L58-78',
  'Compare generated material against a reference and ask separately about unsupported statements and missing information.',
  'Contributor\'s compiler-history worked example with reported errors and gaps.',
  'A model reviewing its own output is not independent verification. Absence from one reference need not mean falsehood. Reported error counts and speed are not validated.', 'Expanded procedure and worked example inspected'),
 (387, 'read_with_flags', 'Sabrina Ramonov',
  'Interview for context, then challenge the proposal', 'L59-103',
  'Build context through questions, then ask for counterarguments, blind spots and risks when considering an idea.',
  'Commercial practitioner tutorial with an example exchange.',
  'Promotional intelligence and savings claims are unsupported. Challenge is not truth; check factual premises and retain the decision.', 'Earlier passage check plus expanded tutorial; not every line'),
 (263, 'read_with_flags', 'Ruben Hassid',
  'Limit AI-generated busywork', 'L101-135; L159-172',
  'State the problem before prompting, set stopping boundaries, and compare activity against actual goals.',
  'Explicit proposed rules and a prioritization prompt.',
  'Fixed task ratios are heuristics. Strong psychological/research claims are unverified; an editorial placeholder reduces confidence. Arguing with the model is not a success measure.', 'Entire available body inspected'),
 (880, 'read_with_flags', 'John Nosta',
  'Preserve an unaided baseline', '[ch.25] Chapter 7, Sequence Matters; Protect the Baseline',
  'Make an initial sketch before AI and alternate assisted and unaided work to notice what the person can still do alone.',
  'Author proposals supported by interpretation of research; source is already integrated in the KB.',
  'Recheck the cited MIT and clinical studies before repeating causal deskilling claims. Reuse existing source/workbench; do not ingest the duplicate EPUB. Consider overlap with stronger existing evidence.', 'Section-level screen across book; expanded Chapter 7 reading, with a small output gap'),
]

def main():
    register = json.loads((OUT/'screening-register.json').read_text(encoding='utf-8'))
    if register.get('queue_reviewed_at'):
        raise SystemExit('Second-pass review exists. Use publish_practical_queue.py; refusing to overwrite it with first-pass judgments.')
    records = register['records']
    assert len(records) == 881, 'Wrong inventory snapshot'
    pdf_meta = json.loads((OUT/'pdf-screening-metadata.json').read_text())
    records[255]['sha256'] = pdf_meta['sha256']
    records[255]['screening_access'] = 'local PDF extracted; all six pages inspected'
    decisions = {}
    def put(i, decision, reason):
        assert i not in decisions, f'Duplicate judgment {i}'
        decisions[i] = {'decision': decision, 'reason': reason}
    with (OUT/'content-decisions.tsv').open(encoding='utf-8-sig', newline='') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            put(int(row['id']), row['decision'], row['reason'])
    for group in json.loads((OUT/'podcast-decisions.json').read_text())['groups']:
        for i in group['ids']:
            put(i, group['decision'], group['reason'])
    for i,r in enumerate(records):
        if r['route'] == 'access_gap' and i not in decisions:
            put(i, 'access_hold', 'Restricted preview or show notes: metadata/access screen only. Full relevant account needed; no negative content verdict.')
    for i in (879,880):
        put(i, 'priority_review', 'Book section screening completed; see expanded selection assessment.')
    assert set(decisions) == set(range(881)), f'Missing/extra IDs: {set(range(881)) ^ set(decisions)}'
    # Additional checks from the lower-priority sample. These override only inspected records.
    for i,note in {
        264: 'Saved guide stops before the promised second procedure. Visible app instructions are low priority; hold missing promised material.',
        285: 'Saved text ends at the introduction of the promised prompt. Visible style advice does not establish authorship or learning; hold missing procedure.',
    }.items():
        decisions[i] = {'decision':'access_hold', 'reason':note}
    decisions[366] = {'decision':'discovery', 'reason':'Entire saved text is a video teaser and promotional links; original video needed, no practice established here.'}
    decisions[794] = {'decision':'provenance_hold', 'reason':'Title names Sachin Kansal; metadata/body identify Sanchan Saxena. Verify original episode before attribution.'}
    audit = json.loads((OUT/'provenance-audit.json').read_text())
    duplicates = {x['id']: x['duplicate_of'] for x in audit if x['issue']=='identical_transcript_body'}
    shortlist=[]
    for i,decision,author,focus,locator,contribution,basis,limits,coverage in SELECTED:
        r=records[i]
        item=dict(id=i,decision=decision,author=author,focus=focus,locator=locator,
                  contribution=contribution,basis=basis,limits=limits,coverage=coverage,
                  path=r['path'],title=r['title'],url=r.get('url'),sha256=r['sha256'])
        shortlist.append(item)
        decisions[i]={'decision':decision,'reason':focus+'; '+limits}
    byid={s['id']:s for s in shortlist}
    for i,r in enumerate(records):
        assert hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256'], f'Changed source {i}'
        if 'initial_assessment' not in r:
            r['initial_assessment']={k:r.get(k) for k in ('assessment','review_decision','credibility')}
        r['screening_id']=i
        r['assessment']='first_pass_screening_2026-09-26'
        r['review_decision']=decisions[i]['decision']
        r['screening_note']=decisions[i]['reason']
        packet=OUT/'inspection-packets'/f'{i:03}.json'
        r['screening_coverage'] = (json.loads(packet.read_text(encoding='utf-8'))['coverage'] if packet.exists()
                                    else 'metadata/access screen only')
        if i in (0,9,264,366):
            r['screening_coverage']='available text inspected in lower-priority check; linked media not inspected'
        elif i in (15,26,48,285,365,539,571):
            r['screening_coverage']='expanded selected passages, not full original source'
        if i in byid:
            r['screening_coverage']=byid[i]['coverage']
            r['source_assessment']=byid[i]
        r['credibility']='source-specific provisional basis recorded' if i in byid else 'not established by brief screen'
        if i in duplicates:
            r['duplicate_transcript_body_of']=duplicates[i]
            r['decision_before_duplicate_check']=r['review_decision']
            r['review_decision']='duplicate_body'
            r['screening_note']+=f' Normalized transcript body identical to ID{duplicates[i]}; not independent evidence. Retain both originals; reconcile metadata.'
    counts=Counter(r['review_decision'] for r in records)
    register['screened_at']='2026-09-26'
    register['method']='Complete inventory first pass; mostly brief passage screening, expanded selected-source review, metadata-only access holds. No content exclusion or integration approval.'
    register['screening_counts']=dict(sorted(counts.items()))
    register['shortlist_ids']=list(byid)
    (OUT/'screening-register.json').write_text(json.dumps(register,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (OUT/'shortlist.json').write_text(json.dumps(shortlist,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    def link(r):
        return '['+r['title'].replace('|',' / ')+'](../../../'+quote(r['path'],safe='/')+')'
    lines=['# Practice source screening register','',
           'Snapshot: 2026-09-26. All 881 items accounted for; most available bodies received a brief excerpt screen, not full reading. See [results](screening-results.md) and [shortlist](shortlist.md).',
           '', 'IDs are stable only within this snapshot. Original automated routes remain in JSON, separately from the interpretive decisions. Access holds and lower-priority items remain available for later review.', '']
    last=None
    for i,r in enumerate(records):
        if r['collection']!=last:
            last=r['collection']; lines.extend(['## '+last,'','| ID | Source | Decision | Reason | Coverage |','|---|---|---|---|---|'])
        cells=[str(i),link(r),r['review_decision'],r['screening_note'].replace('|','/'),r['screening_coverage'].replace('|','/')]
        lines.append('| '+' | '.join(cells)+' |')
    (OUT/'screening-register.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    lines=['# Sources selected for closer practice review','',
           '2026-09-26. Fifteen starting points selected after the whole-collection first pass. This is a reading shortlist, not a list of proven practices or approved KB entries. The wider queue remains open.',
           '', 'Selection rests on a visible procedure/example, attributable use or proposal, inspectable passages, and a distinct contribution. Practitioner credentials were not comprehensively verified. Claims of benefit remain separate from descriptions of use.',
           '', 'Headings describe source contributions, not an adopted outcome taxonomy. Line numbers refer to the saved original Markdown; timestamps to saved transcripts; EPUB markers identify documents, not printed chapters.', '']
    for s in shortlist:
        lines.extend(['## '+s['focus'],'',f"**{s['author']}** — {link(s)}",'',
                      f"**Reading decision:** `{s['decision']}`. **Locator:** {s['locator']}.",'',
                      s['contribution'],'', '**Basis:** '+s['basis'],'', '**Limits:** '+s['limits'],'',
                      '**Read coverage:** '+s['coverage']+'.',''])
    lines.extend(['## Bibliographic repair for the PDF','',
                  'Authors, title, publication and date (20 July 2026) checked against the [NOVA university publication record](https://novaresearch.unl.pt/en/publications/design-ai-systems-that-actually-strengthen-human-reasoning-strate/), which links to the [HBR original](https://hbr.org/2026/07/design-ai-systems-that-actually-strengthen-human-reasoning). The inbox PDF remains unchanged. Full local extraction: [screening text](pdf-screening-text.md).','',
                  'Machine-readable assessments, original paths and hashes: [shortlist.json](shortlist.json). Complete queue: [register](screening-register.md).'])
    (OUT/'shortlist.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({'items':len(records),'counts':dict(counts),'shortlist':len(shortlist),'identical_transcript_bodies':len(duplicates),'hashes_verified':len(records)},indent=2))

if __name__=='__main__':
    main()
