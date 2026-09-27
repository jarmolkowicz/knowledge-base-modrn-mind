"""Render reviewed practice drafts and focused update proposals. Canonical files are read-only."""
from pathlib import Path
import hashlib
import json
import re
import yaml

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
DATE = '2026-09-27'

# Actual original-text coverage used for this supplementary review. Ranges are
# inclusive source.md line numbers, not a claim to have reread complete papers.
COVERAGE = {
 'bjork-desirable-difficulties-2011': [(1,258)],
 'bastani-guardrails-math-rct-2025': [(1,30),(111,238),(320,429)],
 'topaz-fabricated-citations-2026': [(46,120),(251,326)],
 'gentner-markman-analogy-1997': [(80,126)],
 'bainbridge-ironies-automation-1983': [(301,433)],
 'bankins-formosa-ai-meaningful-work-2023': [(1299,1371)],
 'callari-meaningful-work-2025': [(1351,1447)],
 'leonardi-artificial-certainty-2026': [(142,150),(814,861)],
 'messeri-crockett-illusions-understanding-2024': [(761,849)],
 'ericsson-deliberate-practice-1993': [(143,183)],
 'macnamara-maitra-deliberate-practice-replication-2019': [(796,843)],
 'he-illusion-competence-2023': [(191,209),(601,647)],
 'vaccaro-human-ai-meta-analysis-2024': [(105,138),(225,244)],
 'memmert-effort-management-2025': [(1702,1774)],
 'niederhoffer-workslop-2026': [(1,174),(238,298)],
 'shen-skill-formation-2026': [(185,247),(355,373),(643,678)],
 'fan-metacognitive-laziness-2025': [(1,75)],
 'buijsman-autonomy-design-2025': [(818,861)],
 'doshi-hauser-creativity-diversity-2024': [(111,148)],
}

NEW = [
dict(ids=['N01'], source='bjork-desirable-difficulties-2011', stem='retrieve-again-after-a-delay', title='Retrieve again after a delay', outcomes=['independent-capability','understanding'],
 use='You need to remember or use material later, and you have a reliable source or checked solution for feedback. The authors recommend spaced study and retrieval; applying them around AI use is editorial.',
 steps=['Choose a small set of questions or problems tied to what you need to learn.', 'After a delay, close the answer and attempt recall or a solution before reopening it.', 'Check against the source or a knowledgeable teacher; correct errors and ask for help where prerequisites are missing.', 'Return on another occasion and try again, rather than treating familiarity with the explanation as success.'],
 adaptation='[Inference] This sequence combines the chapter’s spacing and retrieval recommendations. AI may help prepare questions or explain a checked error; it is not the answer key. Feedback arrangements and scheduling here are editorial. No fixed interval is prescribed.',
 loc='PDF pp.4–9 (printed pp.58–63), especially spacing on p.5 and retrieval on pp.7–9.',
 basis='Research synthesis and recommendations predating generative AI; the chapter was read in full.',
 observed='The chapter reviews studies where delayed performance differed from performance during practice, and recommends distributing study and generating or retrieving answers. It does not test this AI-assisted sequence.',
 limits='Difficulty is useful only when the learner has enough support to respond. Keep needed accessibility supports. A delayed attempt on one task does not establish broad or durable capability.',
 notice='Can you retrieve the important relationship on a later occasion, and what still needs instruction?',
 related=['desirable-difficulty','check-a-capability-without-the-assistant','ask-about-the-gap-then-do-the-task'],
 distinction='Learning scheduled across occasions, rather than a one-off capability check. N02 trains a different choice: which approach a problem needs.',
 critique='Retained an explicit AI-adaptation label, removed any universal spacing schedule, and kept prerequisite support. The chapter supplies recommendations; it does not validate this combined card.'),
dict(ids=['N02'], source='bjork-desirable-difficulties-2011', stem='mix-problem-types-before-choosing-a-solution', title='Mix problem types before choosing a solution', outcomes=['independent-capability','understanding'],
 use='You can attempt several related problem types but need practice recognizing which approach fits. Begin with suitable instruction and checked examples.',
 steps=['Select related problem types that require different approaches.', 'Mix examples instead of completing every example of one type in a block.', 'For each example, choose and explain the approach before solving it or seeing the answer.', 'Check the solution and the choice of approach. Revisit similar distinctions in a later session.'],
 adaptation='[Inference] The sequence applies the authors’ interleaving recommendation. Explaining the choice and using AI to prepare candidate examples are editorial additions. A knowledgeable person must check generated examples and solutions.',
 loc='PDF pp.5–7 (printed pp.59–61): interleaved motor practice, mathematics problems and artist-style discrimination; p.4: prerequisite boundary.',
 basis='Research synthesis of interleaving and related learning conditions, not an AI-tutoring trial.',
 observed='The chapter describes delayed benefits in several tasks, including selecting among formulas and distinguishing artists. The authors discuss discrimination and memory reloading as possible explanations.',
 limits='Randomly mixing unrelated topics is not the same design. Harder immediate performance is not itself evidence of learning. The appropriate mix and amount of instruction depend on the task.',
 notice='Can you choose an approach on a new checked example without being told its category?',
 related=['desirable-difficulty','rehearse-a-bounded-reasoning-case'],
 distinction='Keep separate from single-case rehearsal: the essential action is alternating problem types and selecting the applicable approach.',
 critique='Kept separate from N01 because timing and discrimination are different actions. Removed any promise of general reasoning improvement and required checked examples.'),
dict(ids=['N03'], source='bastani-guardrails-math-rct-2025', stem='prepare-checked-hints-for-ai-tutoring', title='Prepare checked hints for AI tutoring', outcomes=['independent-capability','understanding'],
 use='An educator is preparing AI-supported practice on material already introduced, and can supply correct solutions and feedback. This is a bounded adaptation of a studied mathematics-tutoring package.',
 steps=['Prepare each problem, one or more correct solutions, common mistakes and helpful feedback.', 'Configure the tutor to use that material and offer hints without directly giving away the answer.', 'Have learners attempt the problems; review correct solutions after practice.', 'Check learning on similar problems without the tutor. Keep this result separate from assisted practice scores.'],
 adaptation='[Inference] Applying the package outside the studied classroom is an adaptation. Inspect sample tutor responses before use and arrange educator correction of bad feedback. These checking arrangements are editorial; teacher-provided answers do not guarantee error-free output.',
 loc='Main paper PDF p.2, Experimental Design and footnotes; p.3, study procedure; p.4, Table 1 and results. Main-paper text reviewed; supplementary prompts and Figure 1 image were not independently inspected.',
 basis='Randomized classroom study of nearly 1,000 students in a Turkish high school, with four sessions. GPT Tutor combined hint-oriented instructions with teacher-prepared problem-specific material.',
 observed='Assisted practice scores improved. GPT Base users subsequently scored worse than control on same-session unaided exams; GPT Tutor users had no statistically detectable exam difference from control. The study did not isolate the effect of each tutor feature.',
 limits='This is not an exact implementation recipe or a claim that a hint-only prompt prevents harm. No equivalence test or durable transfer benefit is established. Preparing checked material takes educator work.',
 notice='What can the learner explain or solve on the separate unaided task, rather than only with hints available?',
 related=['ask-about-the-gap-then-do-the-task','explain-it-back-before-the-correction'],
 distinction='Educator preparation and assessment, rather than a learner asking AI about a gap.',
 critique='Removed the implication of proven learning gains or component-level causality. The missing supplementary prompt inspection is explicit; this is a routine outline, not a reproduction of the experimental system.'),
dict(ids=['N04'], source='topaz-fabricated-citations-2026', stem='verify-reference-identity-and-claim-support', title='Verify reference identity and claim support', outcomes=['judgment','work-quality'],
 use='A consequential claim depends on a reference supplied by AI or another writer. You need to establish both that the source exists and that it supports the claim.',
 steps=['Resolve the identifier or search for the stated title. Compare title, authors and publication details with the retrieved record.', 'If they disagree, search another suitable index or publisher record; distinguish an incorrect identifier from a source you cannot locate.', 'Record unresolved references as unresolved. Do not treat absence from one database as proof of fabrication.', 'Open the located source and check the relevant passage, methods and limits against the claim being made. Correct or remove claims that the source does not support.'],
 adaptation='[Inference] This human workflow adapts the authors’ automated audit. Step 4 checks substantive support and goes beyond their bibliographic verification. AI can suggest mismatches, but its judgment cannot establish that a reference exists or supports a claim.',
 loc='PDF p.1: sequential verification and validation; p.2: database-coverage limits and publisher recommendations.',
 basis='Large bibliographic audit with a 500-reference masked validation. Relevant procedure and limitations passages read; not a trial of this manual checklist.',
 observed='The system compared metadata and checked flagged references across several databases. Reported precision was 91%; recall was not estimated. The audit excluded references without a PMID and acknowledged that some sources might exist outside the searched databases.',
 limits='Do not transfer the audit’s precision to your own checking. A real source may be weak, retracted, misinterpreted or irrelevant. Inaccessible content leaves support unverified.',
 notice='Can another reader locate the source and the passage that supports the particular claim?',
 related=['reference-verification','check-correctness-and-completeness'],
 distinction='Establishes the reference before using it as the comparison standard. The explanatory method stays in place.',
 critique='Used unresolved instead of fabricated for unsuccessful searches. Explicitly separated identity, claim support and the audit’s measured precision.'),
dict(ids=['N05'], source='gentner-markman-analogy-1997', stem='check-an-analogys-relationships-and-limits', title='Check an analogy’s relationships and limits', outcomes=['understanding','judgment'],
 use='An analogy makes an unfamiliar situation feel understandable or suggests a decision. You have enough knowledge of both situations to check the comparison.',
 steps=['Name what corresponds to what in the two situations.', 'Check whether the important relationships and roles correspond, rather than just appearances or shared words.', 'Identify where the mapping fails or depends on a different interpretation of the situation.', 'Treat conclusions projected through the analogy as hypotheses; check their factual correctness separately.'],
 adaptation='[Inference] This checklist operationalizes structure-mapping theory; it is not an author-tested teaching routine. AI may propose a mapping or challenge one, but the person checks its fit and any resulting claims.',
 loc='PDF p.3 (printed p.47): structural consistency, relational focus, systematicity, cross-mapping and separately checking candidate inferences.',
 basis='Theoretical synthesis. Targeted original passage read, not the full paper or a new AI evaluation.',
 observed='The authors describe analogy as alignment of relational structure and explicitly treat projected inferences as guesses whose factual correctness needs separate checking.',
 limits='A systematic mapping need not be true or useful. Domain knowledge and the chosen representation affect what seems to correspond. The checklist has no demonstrated effect on AI-assisted judgment.',
 notice='Which useful inference survived an independent check, and which was only an attractive resemblance?',
 related=['analogical-reasoning','build-the-opposing-case-yourself'],
 distinction='Examines the structure of a comparison, not simply a contrary argument.',
 critique='Kept all steps labelled as an editorial operationalization. Structural elegance is not treated as truth; the full theory is not claimed as reviewed.'),
dict(ids=['N06'], source='bainbridge-ironies-automation-1983', stem='rehearse-taking-over-from-automation', title='Rehearse taking over from automation', outcomes=['independent-capability','accountability'],
 use='A workflow relies on a person to detect a failure and resume control. Use a safe simulation or training environment appropriate to that workflow.',
 steps=['Choose a credible failure and define the information and time available to the person expected to respond.', 'Rehearse detecting it, understanding the current state and taking the required corrective action.', 'Check what prevented recovery: missing skill, stale context, poor signals, unavailable controls or insufficient time.', 'Improve training or the system design, then repeat an appropriate exercise. Do not designate human takeover as a fallback that the person cannot realistically perform.'],
 adaptation='[Inference] This review-and-rehearsal sequence adapts Bainbridge’s recommendations to current workflows. The source does not test a language-model deployment. Controls and responsibility checks are editorial extensions of the recovery problem.',
 loc='PDF p.3, sections 2.2 Working storage and 2.3 Long-term knowledge; extraction interleaves columns, so section labels matter.',
 basis='Historical human-factors synthesis and training recommendations, not a controlled test of this complete routine.',
 observed='Bainbridge distinguishes maintaining skills from knowing the current process state, recommends suitable practice, and notes that fast failures may require automatic responses. Simple and high-fidelity simulators serve different learning needs.',
 limits='Unknown faults cannot all be simulated. Practice cannot compensate for an impossible response deadline. Do not create a live hazardous failure for rehearsal; preserve required accommodations and professional training standards.',
 notice='Could the person detect the problem and act in the available conditions, or did the design assume impossible recovery?',
 related=['partial-automation-principle','check-a-capability-without-the-assistant','turn-a-premortem-into-actions'],
 distinction='Rehearses actual recovery conditions, beyond identifying a risk or checking a skill in isolation.',
 critique='Added the system-redesign option so this does not blame operators or prescribe universally less automation. The source’s simulator-fidelity and response-time limits remain explicit.'),
dict(ids=['N07','N08'], source='bankins-formosa-ai-meaningful-work-2023', support=['callari-meaningful-work-2025'], stem='review-the-human-work-left-after-automation', title='Review the human work left after automation', outcomes=['authorship-agency','independent-capability','accountability'],
 use='A team is changing a recurring job with AI. Include people who do that work and someone able to change the work design. Intended benefits here concern skill, discretion and contribution; this is not a general wellbeing assessment.',
 steps=['Map what people will do after the change, using a recent real task where possible.', 'Discuss which opportunities remain to use and develop skills, make decisions, complete a meaningful contribution and work with other people.', 'Ask affected workers where this description fits or misses their experience, and what support they need.', 'Agree a concrete work-design or support change, assign someone able to act on it, and review what happened.'],
 adaptation='[Inference] The sequence combines Bankins and Formosa’s work-design argument with Callari and colleagues’ recommendations for differentiated support and consultation. Using one recent task, voluntary discussion and a follow-up action is editorial. AI may help map tasks, but cannot speak for workers or settle whose interests count.',
 loc='Bankins and Formosa: PDF p.13, Practical Implications and Future Research. Callari: PDF pp.20–21, sections 5.2–5.3.',
 basis='Conceptual ethical analysis plus qualitative open-ended survey responses. Callari’s data are not in-depth interviews; the paper explicitly identifies that limitation.',
 observed='Bankins and Formosa argue that effects depend on the human work left or created. Callari and colleagues describe different orientations toward AI use and propose tailored support. Neither evaluates this combined review.',
 limits='Do not assign a maturity label or make greater AI use the target. Felt meaning does not establish retained skill or real decision authority. Worker participation needs a route to influence decisions, not merely consultation after they are fixed.',
 notice='What changed in workers’ actual task allocation, learning opportunities or decision rights following the review?',
 related=['ai-meaningful-work-design','ai-work-practice-ideal-types','keep-one-thinking-step','meaningful-work'],
 distinction='N08 is a task-based support variant inside N07, not a second card. The intervention sits at job/team level rather than a personal delegation boundary.',
 critique='Corrected interview wording to open-ended survey responses. Removed typology-as-diagnosis and the idea that adoption is a maturity ladder. Kept outcome tags limited to this KB’s intellectual-agency scope.'),
dict(ids=['N09'], source='leonardi-artificial-certainty-2026', stem='present-projections-with-assumptions-and-alternatives', title='Present projections with assumptions and alternatives', outcomes=['judgment','shared-understanding','calibration'],
 use='People are using an AI-supported model or simulation to discuss an uncertain future. Someone can explain what the model assumes and what its output does not establish.',
 steps=['State what the representation is being used to explore and what it cannot predict reliably.', 'Present important assumptions and limitations alongside the visual or projection.', 'Where the model supports it, compare scenarios or assumptions rather than presenting one image as an inevitable future.', 'Invite discussion of consequences, missing information and choices; keep the resulting decision distinct from the model output.'],
 adaptation='The authors propose scenario contrasts and narration of assumptions and limitations. [Inference] This ordered meeting routine is an editorial adaptation. Do not fabricate model-generated scenarios or numerical uncertainty ranges.',
 loc='PDF pp.6–7, research-site description; pp.26–27, representations of/for the future and practitioner implications.',
 basis='Comparative ethnography of two urban-planning organizations using the same simulation technology, plus author recommendations. Selected original sections reviewed.',
 observed='The authors describe contrasting ways of framing representations and expert authority. They explicitly note a trade-off: heavy caveats or reduced detail may dampen stakeholder interest. They propose pairing engagement with visible uncertainty.',
 limits='The study does not causally prove that this checklist improves decisions. Less detail is not always better; retaining expert authority is not itself evidence of sound judgment. AI-generated prose about uncertainty is not an uncertainty calculation.',
 notice='Can participants distinguish a model assumption, a possible scenario and an agreed decision?',
 related=['artificial-certainty','modulation-practice','match-confidence-to-evidence'],
 distinction='Focuses on collective interpretation of projections. Existing modulation-method claims require the accompanying focused wording correction.',
 critique='Replaced universal claims about reducing detail and preventing bias with the paper’s conditional recommendations. A focused correction to the parent method is drafted alongside this card.'),
]

UPDATES = [
dict(id='E01', source='ericsson-deliberate-practice-1993', support=['macnamara-maitra-deliberate-practice-replication-2019'], target='rehearse-a-bounded-reasoning-case', section='Try It',
 text='[Inference] Optional repeated-practice variant: choose one recurring reasoning error, use a checked case that exposes it, receive specific feedback, and retry a similar case before increasing complexity. A knowledgeable teacher or reviewer should help diagnose mistakes the learner cannot yet see.',
 evidence='Ericsson and colleagues describe tasks designed around weaknesses, informative feedback, repeated attempts and suitable prior knowledge (PDF pp.5–6). This is a rationale for the variant, not a test of AI-generated reasoning cases. Macnamara and Maitra did not replicate the claimed complete correspondence between accumulated practice and skill-group ranking (PDF pp.15–16). Do not promise an expertise threshold or treat hours alone as sufficient.',
 reason='Extend the existing checked-case loop; no distinct trigger warrants another generic rehearsal card.'),
dict(id='E02', source='he-illusion-competence-2023', target='diagnose-your-draft-before-feedback', section='What to Notice',
 text='[Inference] Where a task has a checkable answer or clear criteria, record your initial judgment and confidence, then compare them with independently checked feedback. Notice both justified increases and decreases in confidence. Do not treat an AI rating as the answer key.',
 evidence='He and colleagues tested a tutorial with performance feedback and manually prepared contrastive explanations in logical reasoning (PDF pp.6–7, 14–15). Self-assessment calibration improved, but appropriate reliance did not improve uniformly; participants who initially underestimated themselves could do worse. The writing routine here was not tested. Showing only AI failures can also encourage misplaced distrust.',
 reason='Add a feedback observation and boundary to self-diagnosis; do not introduce another generic calibration routine.'),
dict(id='E03', source='vaccaro-human-ai-meta-analysis-2024', target='test-ai-on-the-work-it-will-do', section='Try It',
 text='[Inference] Optional workflow comparison: on comparable tasks and shared evaluation criteria, compare human-only, AI-only and combined work where all three are meaningful. Keep inputs and constraints comparable, and account for repeated-task learning. Include review time and error consequences. If a condition cannot perform the task, record why rather than forcing an artificial comparison.',
 evidence='Vaccaro and colleagues distinguish improvement over human-only performance from improvement over the better of human or AI alone (PDF pp.2–3). Across the sampled experiments, the former occurred on average while the latter did not. The sample required all three conditions and does not cover every possible collaboration (p.5). This proposed local comparison is not itself a validated intervention and does not decide legal, ethical or ownership requirements.',
 reason='Strengthen the existing task-based evaluation rather than duplicate it. Other screening leads about warmth, sycophancy and abstention remain separate unreviewed extensions in this route; no new claims from them are added.'),
dict(id='E04', source='memmert-effort-management-2025', target='record-human-interventions', section='Try It',
 text='[Inference] Optional post-task review: use the intervention notes to map effort across framing, tool learning, drafting, checking and rework. Record where effort fell, rose or moved to another person. Ask what happened to saved time across the working day. Agree one change to the next task and make unfinished checking explicit at handoff.',
 evidence='Memmert and colleagues draw on 21 interviews and distinguish effort intensity, persistence and direction. Their practice implications recommend recognizing learning costs and communicating the stage and quality of shared work (PDF pp.18–19). The proposed review is an adaptation, not a measured productivity or skill-preservation intervention. More effort is not automatically better.',
 reason='A review variant adds whole-task context to the existing log; estimated avoided costs remain estimates.'),
dict(id='E05', source='niederhoffer-workslop-2026', target='test-and-share-a-team-ai-workflow', section='Try It',
 text='[Inference] Include a recipient in the workflow trial. State what they need to do next, which claims have been checked and which remain uncertain. After handoff, ask what required clarification or rework and revise the workflow accordingly.',
 evidence='Niederhoffer, Robichaux and Hancock describe effort passed to recipients in the 2025 article (PDF pp.2–3) and recommend explicit review processes in the 2026 article (pp.7–8). Their surveys and advice do not test this trial routine. Associations involving trust and felt competence do not establish causal effects of training, trust-building or an ownership mindset.',
 reason='Extend the existing team trial with recipient outcomes; preserve the original practitioner origin and label the research as rationale.'),
dict(id='E06', source='shen-skill-formation-2026', support=['bastani-guardrails-math-rct-2025','fan-metacognitive-laziness-2025'], target='keep-one-thinking-step', section='Evidence and Rationale',
 text='**Related research, not validation:** Shen and colleagues randomized experienced Python users learning an unfamiliar library; the AI group scored lower on an immediate unaided quiz, while the main-study completion-time difference was not significant (PDF pp.6–9). Higher-scoring patterns involving conceptual questions were exploratory observations, not randomized prescriptions (pp.13–14). These results motivate checking what the learner can do separately, but do not prove that retaining one chosen step prevents skill loss.',
 evidence='Bastani’s teacher-configured Tutor package produced no detectable same-session unaided exam difference from control (p.4). Fan’s abstract reports improved essay scores without significant differences in knowledge gain or transfer (pp.1–2; abstract-level check only in this pass). These are different tasks and supports, not one universal effect. None validates this card’s one-step boundary or establishes durable capability.',
 reason='Strengthen outcome boundaries and preserve mixed findings. Do not turn exploratory coding-user patterns into proven learning strategies.'),
dict(id='E07', source='buijsman-autonomy-design-2025', target='expand-agent-authority-one-tested-step-at-a-time', section='Limits',
 text='[Inference] Before expanding authority, check whether the responsible person can understand the consequential choice, inspect failures, challenge the recommendation and act on a refusal or rollback. Record who can change the task’s purpose or criteria. Formal approval alone does not establish informed control.',
 evidence='Buijsman and colleagues distinguish domain-specific competence from authenticity of values and discuss failure transparency, maintained skills and reflection (PDF pp.17–18). These are philosophical/design proposals, not a trial showing this checklist preserves autonomy. Avoid assuming that less AI involvement or more clicks necessarily gives people more control.',
 reason='Add conditions for meaningful authority to the existing staged-deployment routine. Other screening sources remain background unless separately checked.'),
dict(id='E08', source='doshi-hauser-creativity-diversity-2024', target='develop-parallel-creative-routes', section='Evidence and Rationale',
 text='**Related research, not validation:** Doshi and Hauser found that access to AI story ideas improved average evaluations of individual short stories while stories within the AI-assisted conditions became more similar to one another (PDF pp.4–5). This was an individual writing experiment, not a test of parallel teams, retained creative ability or downstream implementation.',
 evidence='[Inference] In a parallel-workflow comparison, inspect the range of resulting ideas separately from the quality of the chosen artifact. Preserve reasons for selection. Neither more options nor a better final artifact alone demonstrates that people became more creative. The Mascareño stage-comparison lead is not used here: its stronger canonical interpretation still needs a separate original-methods review.',
 reason='Add the individual-versus-collective distinction to an existing creative comparison, without claiming this team routine prevents homogenization.'),
dict(id='N10', source='messeri-crockett-illusions-understanding-2024', target='check-missing-perspectives', section='Try It',
 text='[Inference] Research-method variant: before expanding the answer, list important questions or kinds of evidence the chosen AI-supported method cannot examine. Consult a suitable independent method, source or collaborator where that omission matters. More prompts or model personas do not automatically provide independent evidence or human standpoints.',
 evidence='Messeri and Crockett propose naming the intended role of AI and working in cognitively and demographically diverse teams (PDF p.7, Looking ahead). They ask which interventions protect against illusions of understanding; they do not report an evaluation of this checklist. The question-list step is an editorial operationalization of their conceptual argument.',
 reason='Merge into an existing outside-evidence check. A separate broad method-diversity card would currently duplicate the action while implying a more developed routine than the source supplies.'),
dict(id='N09-method', source='leonardi-artificial-certainty-2026', target='modulation-practice', target_type='method', section='Evidence boundary',
 text='Replace categorical claims that modulation prevents bias or produces better decisions with: The authors describe contrasting representational practices in two planning organizations and argue that they shape perceived certainty and expert authority. This observational comparison does not isolate causal effects on decision quality. Their practitioner proposals include scenario contrasts and explicit narration of assumptions; reducing detail is not a universal rule and can dampen engagement.',
 evidence='Original PDF pp.26–27 explicitly present strategies for further exploration and describe the engagement/uncertainty trade-off. Do not equate preserved expert authority with better judgment. Keep the framework in methods; link to the separate practice only if that draft is integrated.',
 reason='Focused correction to avoid contradictory guidance beside N09; not a migration or rewrite of the framework.'),
]

def metadata(stem):
    text = (ROOT/'sources'/f'{stem}.md').read_text(encoding='utf-8-sig')
    return yaml.safe_load(text.split('---',2)[1])

def citation(stem):
    return str(metadata(stem)['sources'][0])

def write_new(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_text(encoding='utf-8') != text:
            old=json.loads((OUT/'manifest.json').read_text(encoding='utf-8'))
            expected=next((r['sha256'] for r in old if r['path']==path.relative_to(ROOT).as_posix()),None)
            assert expected==hashlib.sha256(path.read_bytes()).hexdigest(), f'Refusing to overwrite changed file: {path}'
            path.write_text(text,encoding='utf-8')
    else:
        path.write_text(text, encoding='utf-8')

def render_new(d):
    sources = [d['source']] + d.get('support',[])
    fm = dict(status='emerging', area=['preservation'], sources=[citation(s) for s in sources], source_entries=sources, intended_outcomes=d['outcomes'])
    text = '---\n'+yaml.safe_dump(fm,sort_keys=False,allow_unicode=True)+'---\n\n# '+d['title']+'\n\n'
    text += '## Use When\n\n'+d['use']+'\n\n## Try It\n\n'
    text += '\n'.join(f'{i}. {s}' for i,s in enumerate(d['steps'],1))+'\n\n'+d['adaptation']+'\n\n'
    text += '## Origin\n\n'+citation(d['source'])+'\n\n'+d['loc']+' Title is editorial.\n\n'
    text += '[Retained original](../../source.md). '
    for s in d.get('support',[]):
        text += f'Support: {citation(s)} [Retained original](../../../{s}/source.md). '
    text += '\n\n## Evidence and Rationale\n\n**Basis:** '+d['basis']+'\n\n**Observed or reported:** '+d['observed']+'\n\n'
    text += '**Intended:** '+', '.join(d['outcomes'])+'. These are curator-assigned intended benefits, not demonstrated effects.\n\n'
    text += '**Untested:** The effectiveness of this exact routine in its proposed AI-use setting, including durable independent capability, better judgment and calibrated confidence. Immediate output quality, felt competence and later unaided performance are distinct outcomes.\n\n'
    text += '## Limits\n\n'+d['limits']+'\n\n## What to Notice\n\n[Inference] '+d['notice']+'\n\n## Related\n\n'
    text += '\n'.join(f'- [[{s}]]' for s in d['related'])+'\n\n## Source roles\n\n'
    text += f'- [[{d["source"]}]] — origin of the research, recommendation or framework; exact editorial additions identified above.\n'
    text += ''.join(f'- [[{s}]] — complementary support, not independent validation of this routine.\n' for s in d.get('support',[]))
    text += '\n## Review Status\n\nDraft from supplementary review on 2026-09-27. See the per-source practice review and batch decision ledger. Not integrated.\n'
    return text

def render_update(d):
    sources=[d['source']]+d.get('support',[])
    fm=dict(status='emerging',area=['preservation'],sources=[citation(s) for s in sources])
    text='---\n'+yaml.safe_dump(fm,sort_keys=False,allow_unicode=True)+'---\n\n# Update: '+d['target']+'\n\n'
    text+=f"## Target\n\n[[{d['target']}]] — focused proposal; preserve the existing origin, steps and attribution unless the change below specifies otherwise.\n\n"
    if d['id']=='N09-method':
        text+='''## Proposed replacements

### Replace What To Do

Use AI-supported representations to explore possibilities with stakeholders while making assumptions and limits visible. Preserve room for deliberation about an uncertain future.

### Replace How To Do It

[Inference] This sequence adapts the authors' observed practices and recommendations; it is not a validated protocol.

1. Choose a level of detail appropriate to the question. High-detail and immersive representations are not automatically unsuitable.
2. Explain what the representation assumes, what it leaves unresolved and what its apparent precision does not establish.
3. Where supported by the model, compare scenarios or pair visuals with explicit narration of assumptions and limitations. Do not invent numerical uncertainty ranges.
4. Invite stakeholders to discuss possibilities and consequences; distinguish their decisions from the model output. Do not use expert authority as a substitute for explaining the evidence.

### Replace Why It Works with Rationale and Evidence Limits

Leonardi and Leavell (2026) compare two planning organizations using the same simulation technology. They describe different approaches to representations, perceived certainty and expert authority. Their comparative ethnography does not isolate a causal effect of this checklist on decision quality. The authors propose scenario contrasts and narration of assumptions, while noting that reducing detail or emphasizing caveats too heavily may reduce engagement. Preserved expert authority is not itself evidence of better judgment.

### Replace the descriptions under Related

- [[artificial-certainty]] — the interpretive risk discussed by the source, not a proven preventable outcome of this method.
- [[judgment]] — decisions require evidence and deliberation beyond model output.
- [[confidence-competence-gap]] — related concern; not an identical measured mechanism.
- [[calibration]] — related rationale for communicating uncertainty, not validation of this sequence.

'''
    else:
        text+=f"## Proposed Additions\n\n### To {d['section']}\n\n{d['text']}\n\n### Evidence and limits\n\n{d['evidence']}\n\n"
    text+='## Sources and locators\n\n'
    for s in sources:
        ranges='; '.join(f'L{a}–{b}' for a,b in COVERAGE[s])
        text+=f'- [[{s}]] — {citation(s)} [Original](../../../{s}/source.md), targeted review: {ranges}. Role: research rationale or boundary, not origin or validation of the existing practitioner routine.\n'
    text+='\n## Integration instructions\n\nAdd the cited research to source_entries and sources; label its role as rationale or boundary. Preserve the original practitioner origin. Add a source link under Related where appropriate. Do not change intended outcomes solely because another study is cited.\n\n'
    text+='## Decision rationale\n\n'+d['reason']+'\n\nStatus: prepared for critique; no canonical edit authorized by this file itself.\n'
    return text

def main():
    assert not (OUT/'integration/completed.json').exists(), 'Batch integrated; do not regenerate reviewed drafts.'
    OUT.mkdir(parents=True,exist_ok=True)
    snapshot=OUT/'canonical-before.json'
    if not snapshot.exists():
        data={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for folder in ('sources','concepts','methods','practices') for p in (ROOT/folder).glob('*.md')}
        snapshot.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    manifest=[]
    for d in NEW:
        dest=ROOT/'raw'/d['source']/'drafts/practices'/f"{d['stem']}.md"
        assert not any((ROOT/f/f"{d['stem']}.md").exists() for f in ('sources','concepts','methods','practices'))
        write_new(dest,render_new(d))
        manifest.append(dict(ids=d['ids'],kind='new_practice',source=d['source'],path=dest.relative_to(ROOT).as_posix(),destination='practices/'+d['stem']+'.md',distinction=d['distinction'],critique=d['critique']))
    for d in UPDATES:
        dest=ROOT/'raw'/d['source']/'drafts/updates'/f"kb-practices-{d['target']}.md"
        write_new(dest,render_update(d))
        manifest.append(dict(ids=[d['id']],kind='update_proposal',source=d['source'],path=dest.relative_to(ROOT).as_posix(),destination=('methods' if d.get('target_type')=='method' else 'practices')+'/'+d['target']+'.md',distinction=d['reason']))
    for row in manifest:
        row['sha256']=hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest()
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    coverage=[]
    for s,ranges in COVERAGE.items():
        p=ROOT/'raw'/s/'source.md'
        lines=p.read_text(encoding='utf-8-sig').splitlines()
        assert all(1<=a<=b<=len(lines) for a,b in ranges),s
        coverage.append(dict(source=s,path=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),line_ranges=ranges,depth='full chapter' if s.startswith('bjork-') else ('abstract only' if s.startswith('fan-') else 'targeted original sections; not full paper'),citation=citation(s)))
    (OUT/'source-coverage.json').write_text(json.dumps(coverage,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(dict(new_practices=len(NEW),update_proposals=len(UPDATES),original_sources=len(coverage)),indent=2))

if __name__=='__main__':
    main()
