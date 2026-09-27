# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Render manually reviewed intended-outcome mappings for all 78 practice drafts.

These are editorial navigation judgments, not keyword classifications or efficacy
scores. Historical extraction results stay intact; consolidation is a later layer.
"""
import json
from collections import Counter
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'raw/practitioner-practices-development/extraction'
DEFINITIONS={
'understanding':('Understanding','core','Explain a relationship, mechanism or limit and apply it to a case.','Not recognition of fluent prose or an AI rating.'),
'independent-capability':('Independent capability','core','Perform a chosen skill under explicitly reduced-assistance conditions, including later use.','An immediate attempt is practice or assessment, not evidence of durable transfer. Keep accommodations.'),
'judgment':('Better-founded judgment','core','Choose using relevant evidence, alternatives and consequences.','A checked artifact, consensus or successful outcome alone does not establish improved judgment.'),
'calibration':('Calibration','core','Bring confidence and reliance into closer relation with available evidence and actual performance.','Doubt, felt reassurance and numerical confidence ratings alone are not calibration.'),
'authorship-agency':('Authorship and agency','core','Form purposes, criteria and substantive contributions one can explain, revise or refuse.','Formal approval, imitation of a voice or a disclosure log alone is insufficient.'),
'creative-development':('Creative development','core','Develop, select and reshape possibilities for an intended creative purpose.','More suggestions or polished imitation is not improved creativity; range and selection should be observed separately.'),
'attention':('Directed attention','core','Spend attention deliberately on chosen work and stop or redirect when appropriate.','Screen time, discomfort and task throughput alone are not the outcome.'),
'shared-understanding':('Shared understanding','core','Communicate or reconcile meaning so actual people understand the relevant ideas and differences.','Simulated audience reactions, persuasion and consensus do not establish shared understanding.'),
'accountability':('Accountability and informed participation','enabling','Make authority, contributions, data use and unresolved responsibilities inspectable to those affected.','Documentation or named ownership alone does not show agency, fairness or compliance.'),
'work-quality':('Quality of the immediate work','enabling','Make a specific output, process or check more accurate, useful or fit for its purpose.','Better assisted work does not by itself show stronger thinking or retained capability.'),
}

# Manually assigned after reading the card's actions, rationale and limits.
ROWS='''request-criticism-without-rewriting|authorship-agency|work-quality|The writer judges criticism and makes the revisions instead of accepting replacement prose.
turn-creative-disagreement-into-your-own-checklist|independent-capability|creative-development|The reusable checklist is applied without reopening the assistant; later craft improvement remains untested.
test-ai-on-the-work-it-will-do|calibration|work-quality|Repeated representative tests can inform warranted reliance on this tool for this task.
inspect-real-errors-before-automating-evaluation|work-quality|calibration|Human error inspection and held-out judgments ground evaluation; this primarily improves checking rather than training a person.
rehearse-a-bounded-reasoning-case|independent-capability|understanding|The person chooses and explains an answer before feedback in a checked practice case.
choose-the-result-before-the-tool|authorship-agency|attention|The person defines worthwhile work and chooses assistance for the actual limiting step.
develop-parallel-creative-routes|creative-development|authorship-agency|Keeping routes separate exposes alternative framings before a team combines or chooses them.
save-your-own-starting-point|authorship-agency|judgment|A revisable initial contribution makes later changes and their reasons inspectable.
collect-independent-views-before-discussion|judgment|shared-understanding|Independent submissions preserve differences that can inform a collective decision.
turn-a-premortem-into-actions|judgment|accountability|Possible failures are translated into chosen actions and stopping criteria, not just a risk list.
answer-questions-about-your-belief|judgment|authorship-agency|The person examines premises and checks factual reasons before changing a belief.
preserve-an-ai-claim-before-challenging-it|accountability|judgment|An incident record preserves what was actually claimed so later explanations can be checked.
check-correctness-and-completeness|work-quality|judgment|Separate inspections target false or unsupported claims and important omissions in a particular answer.
carry-one-question-offline|attention|authorship-agency|Ending the generation loop creates room for a person to pursue or leave an unresolved thought.
check-a-capability-without-the-assistant|independent-capability|calibration|Comparable reduced-assistance attempts expose what the person can currently do and what help is needed.
review-ai-code-against-independent-checks|work-quality|understanding|Independent expected behavior and inspection test the code; capability preservation is not directly measured.
keep-one-thinking-step|authorship-agency|independent-capability|The person chooses and performs a valued contribution; a retained step is an opportunity for practice, not proof of skill.
define-the-delegation-before-the-agent-starts|accountability|authorship-agency|The brief makes authority, completion criteria, checkpoints and return of control explicit.
choose-the-human-part-of-the-work|authorship-agency|independent-capability|The same retained-contribution choice is already covered by keep-one-thinking-step; preserve this source as a variant.
teach-a-simulated-learner|understanding|independent-capability|Explaining and applying a framework requires the person to generate an account rather than read another explanation.
test-and-share-a-team-ai-workflow|work-quality|shared-understanding|Testing and sharing failure conditions makes the workflow usable by others; retained capability needs a separate check.
count-the-cost-of-review-before-delegating|judgment|accountability|A full-work comparison informs the choice to delegate instead of equating generation speed with useful savings.
use-a-prototype-to-brief-a-developer|shared-understanding|work-quality|A concrete but explicitly incomplete prototype helps the person and developer discuss intended behavior and unknowns.
curate-context-and-clarify-before-drafting|work-quality|authorship-agency|Relevant context and corrected assumptions improve the immediate brief; no independent learning outcome is built in.
choose-an-argument-before-drafting|authorship-agency|creative-development|The writer compares possible arguments and decides what the available archive can support before drafting.
articulate-your-writing-preferences|authorship-agency|creative-development|Concrete examples make the person's editing criteria expressible and revisable, rather than delegating identity to a profile.
reset-a-drifting-conversation|work-quality|attention|A corrected brief addresses a failed interaction; a fresh conversation alone does not improve the user's thinking.
record-a-workflow-before-turning-it-into-instructions|understanding|accountability|Explaining actual steps and exceptions makes tacit work inspectable before a generated procedure hardens it.
keep-a-document-and-question-tracker|accountability|judgment|The record separates document statements, unanswered questions and confirmations from accountable people.
settle-the-strategy-before-requesting-a-draft|authorship-agency|judgment|An accountable professional chooses the substantive approach before generated wording makes it appear settled.
preview-and-approve-before-publishing|work-quality|accountability|Inspection of the actual artifact catches errors before release; approval alone is not intellectual agency.
answer-ai-questions-with-real-evidence|judgment|calibration|Missing facts are sought in records and with people rather than replaced by model confidence.
name-consequences-before-delegating|accountability|judgment|The person examines who bears consequences and whether authority and recovery mechanisms are real.
keep-your-sensory-association-in-the-work|authorship-agency|creative-development|The user decides whether a generated scene preserves their intended expression; the model does not validate perception.
ask-children-about-ai-before-setting-rules|accountability|shared-understanding|Listening lets affected children inform a rule while adults retain their responsibilities.
map-a-return-path|judgment|calibration|Concrete and verified return constraints make a choice more assessable than generic reassurance.
build-the-opposing-case-yourself|independent-capability|judgment|The learner constructs the argument themselves after receiving an objection, leaving reasoning work with the learner.
make-ai-disclosure-reciprocal|accountability|authorship-agency|Specific reciprocal disclosure makes contributions and responsibility inspectable without promising trust gains.
diagnose-your-draft-before-feedback|calibration|understanding|Comparing a prior diagnosis with checked feedback exposes discrepancies in self-assessment.
use-fictional-questions-for-your-own-reflection|authorship-agency|understanding|The person writes their own response to an interpretation; emotional resonance cannot certify a truth about them.
ask-for-an-explanation-in-a-specific-case|understanding|calibration|Case application and follow-up expose what the learner can explain beyond polished description.
check-missing-perspectives|judgment|shared-understanding|Outside evidence determines whether an apparent omission matters and warrants changing the answer.
ask-before-workplace-data-disclosure|accountability|judgment|Documented answers about collection and use inform a person's disclosure decision.
define-the-decision-before-research|judgment|attention|Research is tied to a consequential question and evidence that could change the choice.
record-human-interventions|accountability||A contemporaneous record makes corrections and context-dependent human work visible.
ask-how-to-find-out-before-asking-ai|independent-capability|understanding|The child participates in choosing and pursuing an inquiry route before receiving an answer.
use-a-creative-constraint-and-respond|creative-development|authorship-agency|The person uses an explicitly fictional provocation to make something rather than treating generated associations as knowledge.
ask-about-the-gap-then-do-the-task|independent-capability|understanding|Explanations address a gap while the person still performs and checks the learning task.
explain-it-back-before-the-correction|understanding|calibration|An unaided explanation reveals gaps before feedback; later transfer is a separate observation.
test-one-creative-change|creative-development|authorship-agency|A bounded human revision is compared with the original rather than accepting AI's interpretation of hidden intent.
keep-a-writing-process-record|accountability|authorship-agency|The record reconstructs contributions and choices without claiming conclusive proof of authorship.
ask-contextual-human-advisers|judgment|shared-understanding|People with domain and personal context supply reasons and surprises for the person's decision.
expand-agent-authority-one-tested-step-at-a-time|accountability|calibration|Observed performance informs a bounded expansion, reduction or retention of authority.
check-what-each-person-thinks-was-decided|shared-understanding|accountability|Comparing participants' accounts reveals disagreement before owners and actions are recorded.
set-creative-criteria-before-generating|creative-development|authorship-agency|The person defines a brief and compares candidates against criteria chosen before attractive options appear.
write-a-proposal-to-test-the-idea|understanding|judgment|Constructing and defending a customer/problem/solution account can expose gaps or justify abandoning an idea.
match-confidence-to-evidence|calibration|judgment|The person distinguishes enthusiasm from evidence strength and selects a proportionate next check.
rehearse-with-audience-experience|shared-understanding|independent-capability|A knowledgeable colleague helps expose gaps in what the speaker can explain to this audience.
ask-what-an-update-would-change|attention|judgment|A decision and revisit trigger determine whether investigating an update deserves attention now.
seek-contrary-customer-evidence|judgment|calibration|Actual customer material is used to test a preferred strategy rather than confirm it.
build-the-model-to-understand-it|understanding|judgment|Constructing relationships and revising assumptions against results develops an explainable account of the system.
let-the-child-write-the-story|independent-capability|authorship-agency|The child performs the chosen writing work while using image support; the account shows participation, not demonstrated learning.
protect-a-daily-highlight|attention|authorship-agency|The person allocates feasible time to a chosen activity and reviews what enabled that attention.
name-your-own-visual-reactions|creative-development|understanding|Comparing visible features makes personal creative judgments more specific without universalizing them.
choose-from-an-ai-generated-creative-pool|creative-development|authorship-agency|The person selects components and retains creative development instead of equating generation with authorship.
review-quality-through-a-real-journey|work-quality|shared-understanding|Actual use and discussion of qualitative criteria reveal friction; improvements in the team's judgment remain a further claim.
argue-the-other-side-before-deciding|shared-understanding|judgment|Participants explain and check each other's reasons before a named decision maker resolves the choice.
keep-a-decision-and-outcome-log|calibration|judgment|Preserved prior reasoning can be compared with results, including right predictions reached for wrong reasons.
outline-the-argument-before-slides|shared-understanding|authorship-agency|The person shapes the sequence of claims before formatting makes a presentation feel complete.
answer-example-relevance|shared-understanding|independent-capability|A direct answer, example and relevance statement are practiced for a real listener rather than judged by fluency alone.
record-lived-moments|creative-development|authorship-agency|Brief dated observations supply personally sourced material while separating current events from older memories.
speak-your-thoughts-before-summarizing|authorship-agency|attention|The person articulates concerns and checks the AI summary against their own priorities.
listen-before-shaping-the-message|shared-understanding|judgment|Actual audience input changes the message and the requested action before presentation polish.
review-survey-questions-for-decisions|work-quality|judgment|Question revision aims at interpretable responses; a better survey does not itself establish better reasoning by its author.
practice-choosing-decisive-questions|independent-capability|judgment|Low-stakes practice links each selected question to the later choices its answer changes.
return-to-real-user-accounts|judgment|attention|Real user accounts inform whether an attractive AI possibility deserves a change of priorities.
explain-the-algorithm-you-own|understanding|accountability|A product owner explains objectives and inputs with implementers before exercising responsibility.
accordion-speaking-rehearsal|shared-understanding|independent-capability|Compressing and expanding a talk clarifies its essential meaning while the person repeatedly performs the delivery.'''

MERGES={'choose-the-human-part-of-the-work':'keep-one-thinking-step'}
HOLDS={'define-the-delegation-before-the-agent-starts':'Existing Mollick source entry has a pending correction; approve the focused update before relying on that canonical entry.',
       'count-the-cost-of-review-before-delegating':'Existing Mollick source entry has a pending correction; remove unsupported comparison and validation claims before reuse.'}
QUALIFIED={'inspect-real-errors-before-automating-evaluation','curate-context-and-clarify-before-drafting','reset-a-drifting-conversation','review-ai-code-against-independent-checks','preview-and-approve-before-publishing','test-and-share-a-team-ai-workflow','review-survey-questions-for-decisions','review-quality-through-a-real-journey','use-fictional-questions-for-your-own-reflection','keep-your-sensory-association-in-the-work','let-the-child-write-the-story','record-human-interventions'}

def main():
    if (BASE.parent/'integration/completed.json').exists():
        raise SystemExit('Historical review already integrated. Update the working outcome vocabulary and guide instead of overwriting this snapshot.')
    old=json.loads((BASE/'close-review-results.json').read_text(encoding='utf-8'))
    cards={Path(c['path']).stem:c for c in old['cards']}
    mapping=[]
    for line in ROWS.splitlines():
        slug,primary,second,rationale=line.split('|');c=cards[slug]
        text=(ROOT/c['path']).read_text(encoding='utf-8-sig')
        notice=re.search(r'## What to Notice\s+(.+?)(?=\n## |\Z)',text,re.S)
        mapping.append(dict(slug=slug,path=c['path'],title=c['title'],source_ids=c['source_ids'],primary_outcome=primary,secondary_outcomes=second.split(',') if second else [],rationale=rationale,observable_check=notice.group(1).strip() if notice else '',fit='qualified' if slug in QUALIFIED else 'clear',fit_note='This is an intended benefit. The source does not directly evaluate this complete routine.',consolidation='merge_variant' if slug in MERGES else 'retain',merge_into=MERGES.get(slug),integration_status='hold_for_source_correction' if slug in HOLDS else ('retained_variant' if slug in MERGES else 'awaiting_editorial_decision'),integration_note=HOLDS.get(slug,'')))
    assert len(mapping)==len(cards)==78 and {r['slug'] for r in mapping}==set(cards)
    for variant,target in MERGES.items():
        retained=next(r for r in mapping if r['slug']==target)
        retained['source_ids']=sorted(set(retained['source_ids']+cards[variant]['source_ids']))
    assert all(r['primary_outcome'] in DEFINITIONS and all(s in DEFINITIONS for s in r['secondary_outcomes']) for r in mapping)
    active=[r for r in mapping if r['consolidation']=='retain']
    counts=Counter(r['primary_outcome'] for r in active)
    out={'date':'2026-09-27','status':'proposed-v1','scope':'all 78 original practice drafts, manually mapped; 77 proposed standalone cards','categories':[dict(id=k,title=d[0],role=d[1],definition=d[2],boundary=d[3]) for k,d in DEFINITIONS.items()],'primary_counts_after_consolidation':dict(counts),'mappings':mapping,'integration_approved':False}
    (BASE/'outcome-review.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    lines=['# Intended outcomes — proposal v1','','2026-09-27. Reviewed against all 78 drafts. **77 proposed standalone practices; one retained as a source variant.** These labels describe intended benefits, not demonstrated effects.','',
    '## What changed from the first list','','Keep eight outcomes concerning people and their thinking, plus two enabling outcomes: accountability and immediate work quality. “Grounding in people and experience” is usually a way to work, so it becomes a procedural feature rather than an outcome label. Shared understanding covers actual communication and reconciliation. Immediate work quality is explicit so coding checks and workflow repairs are not mislabeled as stronger judgment.','',
    'Authorship/agency remains distinct from documented accountability. Understanding remains distinct from later independent capability. Calibration concerns the fit between confidence/reliance and evidence, not simply skepticism. Creative range and selection remain separate observations within creative development.','',
    '| Outcome | Role | Meaning | Primary cards |','|---|---|---|---:|']
    for k,d in DEFINITIONS.items():lines.append(f'| {d[0]} | {d[1]} | {d[2]} {d[3]} | {counts[k]} |')
    lines+=['','## Use the labels carefully','','Assign one primary intended outcome and at most two secondary ones. Record the task, human contribution, AI role and evidence basis separately. A direct card for an enabling outcome is useful, but must not claim retained capability unless separately assessed. A card can be a worthwhile hypothesis without evidence of effectiveness.','',
    'All observations below are curator proposals or retained draft observations, not validated measures. Primary assignments are editorial choices that can change with the user’s goal. “Qualified” marks fit needing a particularly clear boundary; it is not an evidence score.','',
    '## Complete mapping','','| Practice | Primary | Secondary | Judgment |','|---|---|---|---|']
    for r in mapping:
        path=Path(r['path']).relative_to('raw')
        url='../../'+path.as_posix()
        lines.append(f'| [{r["title"]}](<{url}>) | {DEFINITIONS[r["primary_outcome"]][0]} | '+', '.join(DEFINITIONS[x][0] for x in r['secondary_outcomes'])+f' | {r["rationale"]}'+(' Merge as variant.' if r['consolidation']=='merge_variant' else '')+' |')
    lines+=['','## Remaining uncertainties','','No direct test of this entire taxonomy or most complete routines. The pool remains concentrated in writing, education, software and product work. The 92 screened variants remain available to challenge category boundaries later; they are not silently excluded.','',
    'The full mapping with proposed observations and integration holds is in [outcome-review.json](outcome-review.json). Consolidation and concrete draft revisions are recorded separately.']
    (BASE/'outcome-review.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({'mapped':len(mapping),'standalone':len(active),'counts':counts,'source_correction_holds':len(HOLDS)},indent=2))

if __name__=='__main__':main()
