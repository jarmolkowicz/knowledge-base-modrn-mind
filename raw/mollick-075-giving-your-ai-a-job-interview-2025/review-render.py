import json, re
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[2]
m=json.loads((ROOT/'raw/practitioner-practices-development/extraction/manifest.json').read_text(encoding='utf-8-sig'))
ss={s['id']:s for s in m['sources'] if 5<=s['group_index']<=9}
rr={}; cc={}
def r(id,author,decision,locators,basis,reported,proposed,limits,related,note,coverage=None):
 s=ss[id]; n=len((ROOT/s['source_path']).read_text(encoding='utf-8-sig').splitlines())
 rr[id]=dict(id=id,group_index=s['group_index'],author=author,decision=decision,coverage=coverage or f'Full available extracted article, L1–{n}. Linked images, videos and external studies not inspected.',locators=locators,basis=basis,reported_outcomes=reported,proposed_outcomes=proposed,limits=limits,related_entries=related,practice_files=[],role={'retain':'origin','merge':'support','counterexample':'counterexample','defer':'deferred'}[decision],review_note=note)
r(453,'Khaled Ahmed, guest contributor with Sam Illingworth','retain',['L28–36: correctness and completeness checks against a supplied reference','L58–78: compiler-timeline demonstration and model-flag counts'],'Proposed checklist plus a displayed model-assisted comparison.',['The author reports seven correctness issues and eight completeness gaps; the flags were not independently validated here.'],['Make unsupported claims and missing relevant material easier to inspect.'],['The reference can be wrong or incomplete.','Completeness depends on task scope; a timeline need not contain every compiler type.','Model flags and reported time savings are not independent evaluation.'],['reference-verification','automation-bias'],'Retain two checking questions; human adjudication is an explicit editorial adaptation.')
r(456,'Sam Illingworth','retain',['L31–47: ask retrieved versus inferred and request specific source','L49–59: signed-out comparison and data-origin claims','L63–70: preserve screenshot, date, question and claim; stop repeated argument','L82: origin remains unresolved'],'First-person incident account and proposed record-keeping procedure.',['The available account does not resolve the origin of the personal information.'],['Preserve an inspectable record before the model changes its account.'],['Opening is damaged and incident context is missing.','A signed-out difference does not establish access to private records.','The account suggests connected accounts explain the data but later says its origin remains unknown.','A model account of retrieval is not forensic provenance.'],['reference-verification','automation-bias'],'Retain the log, not privacy diagnosis or legal procedure.','All 90 available lines read; opening at L15 is damaged. Linked media not inspected; original incident context remains missing.')
r(437,'J Hong of Natural Intelligence, with Sam Illingworth','counterexample',['L32: hallucination-versus-human-uncertainty prompt','L42–60: dream conversation, invented document and external file search'],'Contributor first-person account.',['J Hong reports that Dream_Journal_Analysis.docx could not be found in Drive or on disk; existing journals were JSON files. The dream memory remained uncertain.'],[],['A failed file search does not prove human memory generally more reliable.','Asking why an answer could be a hallucination did not establish its truth.'],['reference-verification','automation-bias'],'Retain failure evidence for external record checks, not the failed verification prompt.')
r(46,'Cal Newport','defer',['L9–39: Quartz/CNBC framing comparison','L39: chronology claim about layoffs before ChatGPT'],'Commentary on news coverage; original articles and screenshot contents not independently checked.',[],['Read beyond headlines and question implied causality.'],['Grouping 2022 and 2023 layoffs as before ChatGPT needs chronology correction or checking.','Original reporting and screenshots are required to assess the comparison fairly.'],['reference-verification'],'No card. Revisit original reporting and dates; general verification already exists.')
r(328,'Ruben Hassid','merge',['L95: timestamps and contradictions','L136: excerpts with original links','L144–152: legal and market-research prompts'],'Proposed search prompts and uncontrolled tool preferences.',[],['Collect traceable evidence and conflicting accounts.'],['Links requested in a prompt can be invented or irrelevant.','Tool rankings and legal recipes not independently checked.','Nine versus fifteen searches is inconsistent; no validated search protocol.'],['reference-verification'],'Merge traceability into correctness/completeness; no separate prompt catalogue.','All 212 available lines read; ending points onward and may omit original final material. Linked media not inspected.')
r(580,'Camille Fournier, interviewed by Lenny Rachitsky','counterexample',['L528–577, 01:12:42–01:17:04: complete AI-corner exchange','L547–556: invented quotations, repeated fabrication, wrong paper summary'],'First-person interview examples.',['Fournier reports more fabricated quotations after challenging the assistant; occasional sentence-editing help is a separate use.'],[],['A friend’s apparently better role prompt was not tested systematically.','Whether AI wrote the discussed film trailer is explicitly unknown.'],['reference-verification','automation-bias'],'Failure evidence for checking original records; do not extract role prompting as verification.','Read L513–577, including question context and complete AI-corner exchange (01:12:42–01:17:04); other topics excluded.')
r(75,'Ethan Mollick','retain',['L28–34: limits of idiosyncratic impressions','L46: repeated GuacaDrone comparison','L62–67: repeated real-task tests with relevant expertise'],'First-person demonstrations and proposed task-specific evaluation.',['Repeated trials produced different ratings; this does not establish ground truth for business advice.'],['Choose models using work resembling the intended task.'],['Familiar tasks can have weak criteria.','Benchmark scores are not local-task success probabilities.','Prompt variation and model updates complicate comparisons.'],['dellacqua-jagged-frontier-2023','reference-verification'],'Consolidate real-task testing; sensitivity comparisons are observations, not diagnoses of model internals.')
r(652,'Hamel Husain and Shreya Shankar, interviewed by Lenny Rachitsky','retain',['L130–272: traces, human notes, upstream errors','L296–359: domain expertise and sample-size heuristic','L377–557: AI groups notes; human refines categories and checks assignments','L581–710: prioritize, use simple checks, compare judges with humans','L935–980: resource fit and human-first boundary'],'Detailed practitioner interview with customer-support evaluation examples.',['Speakers describe broken messages, unavailable tours and handoff failures in actual traces; no controlled business-impact estimate.'],['Find meaningful failures before choosing automated checks.'],['One hundred examples is a heuristic.','One expert may not represent all affected perspectives.','Overall agreement can hide rare failures; inspect false positives and false negatives.','Cited criteria-drift research not independently reviewed.'],['automation-bias','metacognitive-demand','agency'],'Retain human-first error analysis; AI can organize notes, not replace first judgments.','Read technical conversation L90–1049 (approximately 00:05:05–01:37:55), complete relevant exchanges including L700–750. Later lightning-round material excluded.')
r(289,'Ruben Hassid','counterexample',['L96–128: newsletter advice and concession','L154–156: continue toward the answer the user prefers','L199–225: expert roles and temperature'],'First-person cross-model critique demonstration.',['A model changes its recommendation after seeing another answer; no independent truth check or later newsletter outcome.'],['Improve advice through model disagreement.'],['Preferred-answer selection can amplify confirmation bias.','Agreement is not truth.','Multiple models can share errors; expert roles do not supply expertise.'],['automation-bias','reference-verification'],'Downgrade to counterexample; never recommend battling until preferred agreement.')
r(423,'Sam Illingworth','merge',['L83–109: agreement, urgency, fresh-chat and tone comparisons','L93: research intervention differs from prompt exercise'],'Proposed exercises attached to a secondary internal-model research account.',[],['Notice changes when framing changes.'],['Urgency prompting is not the internal-vector intervention in the research.','A few outputs cannot diagnose emotion patterns or reward hacking.','Underlying research and generalization to all assistants not checked.'],['automation-bias','reference-verification'],'Keep only bounded framing comparison; reject mechanistic diagnosis.')
r(479,'Sam Illingworth','merge',['L72, L128–140: weak or fabricated references','L197–211: temperature comparison','L224–258: model comparisons and learning claims'],'First-person local-model demonstrations and settings exercise.',['Author notices slow output and unusable references; no measured literacy gain.'],['Notice output changes across settings or models.'],['Small models are not necessarily more honest or interpretable.','Local execution alone does not establish whole-workflow privacy.','Installation and product behavior not checked; tutorial excluded.'],['reference-verification'],'Merge optional model/settings comparison; defer installation and internal-mechanism claims.')
r(508,'Sam Illingworth','merge',['L95–103: fresh repetitions and reasoning-mode comparison','L113–119: different-tool check and unverified-content disclosure','L129: five-run exercise'],'Proposed routines described as personally used, attached to a secondary research summary.',[],['Notice inconsistency and distinguish checked from unchecked content.'],['Two or five runs cannot establish a general variance/bias decomposition.','Same outputs do not prove reasoning mode is noise.','Different models are not independent verification; randomness does not make auditing impossible.','Underlying paper not independently checked.'],['reference-verification','automation-bias'],'Keep repetitions inside task testing; remove stronger reliability and mechanism claims.')
r(517,'Sam Illingworth','merge',['L98–104: lost practice, omissions, stakes and interests','L116–122: funding, language comparisons, detectors, citations'],'Normative literacy essay and proposed exercises.',[],['Ask questions about AI and notice differences across contexts.'],['One language comparison does not establish bias; competent readers in both languages are needed.','Detector results are not evidence of authorship.','Broad historical, medical, legal and research assertions not checked.'],['agency','reference-verification'],'Merge language variant into task testing; do not adopt its broad literacy taxonomy.')
r(72,'Ethan Mollick','merge',['L43: blocked slide task; human supplies paper and graph','L49–55: proposed visible interfaces'],'First-person demonstrations and design speculation.',['Author reports intervening in a stuck slide-editing task.'],['Make ongoing work inspectable and correctable.'],['Interface benefit not measured.','Product/security properties not independently checked.'],['metacognitive-demand','partial-automation-principle'],'Support checkpoints and recovery; no separate card.')
r(80,'Ethan Mollick','retain',['L10–18: MBA prototype class','L24–32: human time, success likelihood and AI process costs','L44: projected saving','L58–60: purpose, limits, deliverables, done and checks'],'Teaching observation and proposed delegation model.',['MBA participants made prototypes during a four-day class; no AI-native comparison group or controlled outperformance finding.'],['Include review and retry costs; define the delegated assignment.'],['Existing canonical entry adds an AI-native comparison, validation language and an inequality not shown in this article.','Projected savings are not observed results.','Benchmark win-or-tie rates are not local success probabilities.','Time alone omits responsibility, harm and retained skill.'],['mollick-management-ai-superpower-2026','bainbridge-ironies-automation-1983','partial-automation-principle','metacognitive-demand'],'Duplicate canonical source: source draft UPDATE ONLY. Two practice drafts; canonical corrections flagged, not applied.')
r(84,'Ethan Mollick','counterexample',['L24–30: table error checked; other experiments not verified','L42: spreadsheet-formula preferences','L58–70: review difficulty and provisional trust'],'First-person demonstrations and commentary.',['One table issue was checked; other analysis exceeded what author could readily verify.'],[],['Impressive output can exceed an expert’s practical review ability.','Skill-loss discussion is a concern, not an observed result.'],['metacognitive-demand','automation-bias'],'Limit on delegation: impressive output does not establish reviewability.')
r(89,'Ethan Mollick','counterexample',['L43: polished paper with weak hypothesis and causal concerns','L47: simulated RPG players','L51: repetitive fiction'],'First-person model demonstrations.',['Author describes competent-looking analysis with weak substantive choices.'],[],['Simulated players are not real playtesting.','Polish and correct calculations do not establish a worthwhile question or causal identification.'],['reference-verification','metacognitive-demand'],'Counterexample for result criteria; no simulated-user validation claim.')
r(95,'Ethan Mollick','counterexample',['L30: repeated image-download failure','L36–58: research demos and expert impressions'],'First-person tool demonstrations.',['Image task gets stuck; some research output seems useful on inspection.'],[],['Access restrictions and confusion both feature in the failure.','Expert impressions do not verify every research claim.'],['metacognitive-demand','reference-verification'],'Support bounded retry/recovery; a pre-agreed stop rule is editorial inference.')
r(105,'Ethan Mollick','counterexample',['L28: prior preparation before the timed demonstration','L38: drafts not ready for use','L54: generated text does not mean underlying work done'],'Timed personal output demonstration with prior setup.',['Several drafts generated quickly; not finished work.'],[],['Headline duration omits preparation and review.','Output volume is not validated productivity.'],['metacognitive-demand'],'Support full cost accounting; omit headline speed as a benefit.')
r(356,'Sabrina Ramonov','merge',['L63–85: goal, constraints, verification','L93 and L206: model-scored rubric','L246–276: autonomous marketing account','L351–363: turn cap'],'Goal-mode proposal and personal marketing account.',['Author reports improved click-through results; raw data and controls unavailable.'],['Set bounded outcome and checks before autonomous work.'],['A model giving itself eight out of ten is not external validation.','Adaptive marketing tests may be confounded.','Commands and permissions not independently checked.'],['automation-bias','metacognitive-demand'],'Merge goal, bounds and checks; exclude self-score and causal-uplift claims.')
r(375,'Sabrina Ramonov','retain',['L76: preview before rendering','L84–104: wrong repository detail and evidence capture','L136–178: rough edits and human final review'],'Personal content-production demonstration involving author’s product.',['Author describes correcting an inaccurate detail and inspecting imperfect edits.'],['Catch claim and presentation errors before release.'],['Agent-captured screenshots also need human checking.','Author promotes her own product.','Local rendering does not establish all data remains local.'],['reference-verification','agency'],'Retain preview/approval, not product or security claims.')
r(537,'Aishwarya Naresh Reganti and Kiriti Badam, interviewed by Lenny Rachitsky','retain',['L170–185: suggestions, drafts and actions','L347–350: support agent shut down after repeated fixes','L353–380: bounded versions and feedback'],'Practitioner interview with deployment experience and staged-process proposal.',['Speakers report stopping a support agent after patching became burdensome; no controlled success rate.'],['Expand responsibility after bounded use and error review.'],['Few edits can mean rubber-stamping.','Maximum autonomy need not be the goal.','Clinical example not evaluated and excluded.'],['partial-automation-principle','bainbridge-ironies-automation-1983','automation-bias'],'Retain staged authority, including remaining partial or rolling back.','Read complete exchanges L125–225 (00:05:14–00:25:06) and L310–388 (00:41:20–00:58:08); other topics excluded.')
r(38,'Cal Newport, reporting an anonymous engineer','counterexample',['L15–35: initial speed estimate, two crashes, hard review','L39–41: return to manual development with narrow assistance'],'Anonymous secondhand account.',['Engineer reports early speed, later crashes and narrower AI use; no logs or independent corroboration.'],[],['Cannot attribute all failures to AI or generalize savings.','Review difficulty is not quantified generally.'],['automation-bias','metacognitive-demand'],'Failure case for review requirements; not a universal argument against AI coding.')
r(275,'Ruben Hassid','counterexample',['L101, L123, L133, L217, L369: permissive approvals','L271: incremental construction','L321–325: visual review, brief, repeated-error advice'],'Promotional tool tutorial.',[],['Build prototypes with small instructions and visible feedback.'],['Blanket permission bypass is not a general practice.','Visual inspection cannot verify data handling, authorization or backend behavior.','Every-time repair claims unsupported.'],['automation-bias','agency'],'Boundary case for prototype review; exclude permissive setup and repair guarantees.')
r(339,'Ruben Hassid','retain',['L35–75: prototype communication and team use','L212–220: intent and increments','L277–289: human testing','L537–562: developer handoff and known gaps'],'Practitioner account and proposed prototype handoff.',['Author reports communicating an idea with a prototype; production readiness and comprehension not evaluated.'],['Make an idea concrete for developer discussion.'],['Folder location is not established access control.','Bypass advice and delayed security review excluded.','Working screens do not prove maintainability or safe deployment.'],['agency','automation-bias'],'Retain communication and unknowns; merge source 350’s incremental demo.')
r(350,'Sabrina Ramonov','merge',['L20–30: niece’s two-app demonstration','L62–70: one feature at a time','L122–126: fix music issue before adding more'],'Family demonstration and tutorial.',['Two app demonstrations reported; independent coding skill not tested.'],['Keep prototyping inspectable with small steps.'],['Working demos are not understanding or production quality.','Claim that learning code is obsolete unsupported.','Do not reuse exposed credentials or private details.'],['shen-skill-formation-2026','agency'],'Merge incremental tests; no separate card or learning claim.')
r(402,'Sabrina Ramonov','retain',['L42–44: plan and alternatives','L130–161: independently expected test values and edge cases','L283–298: small changes and reuse','L310–331: manual tests, review, revisions'],'Experienced developer’s proposed routine and personal practice.',['Author rarely accepts a first draft; no controlled productivity or skill result.'],['Keep expert involvement and independently check behavior.'],['Requires ability to assess code and tests.','Tests can repeat the implementation’s misconception.','Model explanations are not internal-reasoning access.'],['shen-skill-formation-2026','automation-bias','metacognitive-demand'],'Retain independent checks; optional Thawar pairing is not measured AI benefit.')
r(636,'Farhan Thawar, interviewed by Lenny Rachitsky','merge',['L187–247, 00:22:30–00:29:18: pair-programming exchange','L238: two humans accept, reject or rewrite AI suggestions'],'Advocacy based on human pair-programming experience.',['Describes Shopify pairing; no controlled AI-pair versus individual comparison.'],['Have two humans judge suggestions.'],['Company time comparisons are uncontrolled.','Timer-and-delete exercise excluded.','Two reviewers can share blind spots.'],['shen-skill-formation-2026','automation-bias'],'Merge human-reviewer variant; preserve guest attribution.','Complete relevant exchange L187–247, 00:22:30–00:29:18 read; unrelated topics excluded.')
r(76,'Ethan Mollick','retain',['L30: human graphs with AI statistics','L34–36: alternatives, own wording and reading','L40–46: selective response to fictional-reader criticism'],'Personal writing and research accounts.',['Author selectively accepts suggestions; unaided-skill effects not measured.'],['Choose which contribution stays human.'],['No universal optimal division.','Feeling control does not establish retained capability.'],['partial-automation-principle','dellacqua-jagged-frontier-2023','agency'],'Editorial procedure grounded in examples, not a tested learning intervention.')
r(276,'Ruben Hassid','retain',['L79–125: relevant context, examples and output folders','L140–179: read-only wording','L273–278: questions and plan approval','L382–394 and L452: human writing and final review'],'Proposed context-folder workflow with demonstrations.',[],['Reduce avoidable assumptions through context and questions.'],['Read-only prompts are not access controls.','More context can expose private material and add noise.','Folder structure does not prove persistent memory or instruction following.'],['agency','automation-bias'],'Retain selection and clarification; omit setup, security promises and replacement claims.')
r(324,'Ruben Hassid','retain',['L63–76: describe failure, fresh task, questions','L105–107: select context'],'Proposed conversation-repair routine.',[],['Recover a clear task definition.'],['New chat or vendor does not fix missing expertise.','Self-diagnosed failure reasons can be invented.','Resets may discard constraints.'],['agency','reference-verification'],'Retain corrected brief, not vendor-switch requirement or introspective diagnosis.')
r(325,'Ruben Hassid','retain',['L212–213: record actual work','L218–254: clarify scope, exceptions, data, quality, approvals before SOP','L264–268: personality-based hiring excluded'],'Proposed workflow-documentation routine.',[],['Make actual process explicit before writing instructions.'],['One walkthrough can omit exceptions and tacit judgment.','Recordings can expose others’ private information.','Personality-based hiring and popularity-based paper choice excluded.'],['agency','partial-automation-principle'],'Retain recording and clarification; walkthrough check is a marked adaptation.','All 294 available lines read; ends at unfinished new heading. Complete available workflow section, not complete publication.')
r(360,'AskGwyn, guest contributor hosted by Sabrina Ramonov','retain',['L23–47: organize, do not choose insurance plan','L51–61: tracker sections','L71: document-only comparison with locators or not-found','L91–99: ask accountable sources and record confirmed answers'],'Proposed healthcare-insurance administration guide.',[],['Keep documents, questions and confirmed answers separate.'],['No measured user outcome.','Coverage, deadline and drug claims not checked or extracted as advice.','Redaction does not guarantee deidentification.','An accountable source must confirm terms.'],['reference-verification','agency'],'Credit AskGwyn; retain tracker, no coverage recommendation or medical/legal claims.')
r(361,'Paula Rojas, interviewed/profiled by Sabrina Ramonov','retain',['L74–78: irreversible actions require approval','L121–129: reported time and deadline review','L245–251: human strategy, plan, draft, citation checks','L283–311: recorded work, small pilot, later failure and human parallel checks','L327: sign-off'],'Named lawyer’s first-person account in host article.',['Rojas reports shorter drafting time and checks deadlines/citations; figures and no-error report not audited.'],['Keep strategy and sign-off with accountable person.'],['Chilean legal context is not transferable legal instruction.','Experts can miss persuasive errors.','Privacy/setup claims not verified controls.','Speed does not establish better judgment or retained expertise.'],['agency','reference-verification','metacognitive-demand'],'Retain expert strategy before drafting; legal example requires qualified checking.')
r(394,'Sabrina Ramonov','retain',['L30–40: planning account and task deletion','L112: published numbers fictional','L165–182: questions, confidence request, return to SQL data','L251: ensemble terminology'],'Personal planning account and prompt.',['Author reports deleting 237 tasks; no decision-quality follow-up and example business figures explicitly fictional.'],['Use questions to locate missing evidence before priority choices.'],['Requested 95 percent model confidence is not calibrated certainty.','Several assistants are not independent experts or technical mixture-of-experts.','A shorter task list can still be a worse decision.'],['agency','reference-verification'],'Retain real-data checks and human choice; omit confidence threshold and ensemble authority.')
def c(id,stem,title,use,steps,evidence,research,limits,notice,support=()):
 p=f"{ss[id]['workbench']}/drafts/practices/{stem}.md"
 cc[p]=dict(id=id,stem=stem,title=title,use=use,steps=steps,evidence=evidence,research=research,limits=limits,notice=notice,support=list(support))
 rr[id]['practice_files'].append(p)
 for sid in support: rr[sid]['practice_files'].append(p)
c(453,'check-correctness-and-completeness','Check correctness and completeness separately','You have an answer, a task definition and reference material you can inspect.',['Choose the reference and state what the answer is supposed to cover.','Ask AI for two lists: claims that contradict or go beyond the reference, and relevant material missing from the answer. Require a reference location for each flag.','[Inference] Check every flag yourself against the reference. Decide which omissions matter; correct the answer and mark unresolved claims.'],'Ahmed demonstrates the split on a compiler timeline. Reported counts are model flags, not independently established errors. Hassid supplies related traceable-search prompts.','[[reference-verification]] describes the same boundary: a checking prompt is not verification until the source is inspected. This is a procedural extension, not a new tested mechanism.','A bad reference can make a faithful answer wrong. A model can invent quotations or over-report omissions. Keep “not supported here” distinct from “false.”','Which flags survive your inspection, and what did the model miss?',[328])
c(456,'preserve-an-ai-claim-before-challenging-it','Preserve an AI claim before challenging it','An assistant makes a surprising claim and starts changing its explanation.',['Save the exact question and answer, date and context before challenging it.','Ask for the specific record and whether the claim was retrieved or inferred. Label this as the model’s account, not established provenance.','Check accessible original records yourself and keep unresolved items explicit. The author proposes stopping after one correction attempt rather than arguing repeatedly.'],'Illingworth proposes an incident log; the available opening is damaged and the example’s origin remains unresolved. J Hong and Fournier report fabricated records or quotations after prompting.','[[reference-verification]] is the existing verification method. [[automation-bias]] gives a related reason to question confident explanations; neither directly tests this log routine.','A screenshot preserves words, not truth. Signed-out differences do not prove private-data access. Legal and privacy-diagnosis advice is excluded.','Can you reconstruct the original claim without relying on the model’s later version?',[437,580])
c(75,'test-ai-on-the-work-it-will-do','Test AI on the work it will do','You need to choose or assess a model for a task you can evaluate.',['Choose representative work and state what an acceptable result must do. Include checks requiring relevant expertise.','Run the task repeatedly. Keep tasks and criteria consistent when comparing models; record settings and dates.','Judge outputs against criteria and original evidence. Record errors and useful contributions; recheck after relevant model or task changes.','[Inference] Optionally vary one framing, language or setting at a time. Differences are observations, not proof of an internal mechanism.'],'Mollick recommends repeated job-like tests and demonstrates varied ratings. Illingworth proposes framing, settings and language comparisons. No optimal run count or general reliability score is established.','[[dellacqua-jagged-frontier-2023]] reports task-dependent effects in a bounded consulting experiment, not validation of this routine.','Agreement can be consistently wrong. A few changed answers cannot reveal emotion patterns or variance dominance. Do not force agreement with a preferred answer, as in Hassid’s LLM Battle example. Language comparisons need competent readers.','Which real task failures did benchmarks or a first good impression miss?',[423,479,508,517,289])
c(652,'inspect-real-errors-before-automating-evaluation','Inspect real errors before automating evaluation','An AI product has real interactions and domain expertise available for review.',['Read complete interactions and write your own failure notes before asking AI to categorize them. Look for upstream errors.','Ask AI to group the notes. A human refines categories and checks assignments, including cases that fit none.','Prioritize consequential failures. Prefer direct checks where possible; use a model judge only for a defined need.','Compare judges with held-out human judgments. Inspect false positives and false negatives, not just agreement. Keep reviewing new failures and changing criteria.'],'Husain and Shankar describe actual support traces and a concrete human-first process; no controlled business-impact estimate.','[[metacognitive-demand]] frames the continued effort of oversight. It is a related account, not direct validation of this procedure.','One hundred examples is a heuristic. One expert can miss other perspectives. Rare serious failures can disappear in aggregate scores. Categorization can reshape initial judgments.','What failure did your own reading reveal before categories and scores existed?')
c(80,'count-the-cost-of-review-before-delegating','Count the cost of review before delegating','AI looks faster, but you still need to brief, wait, inspect and repair.',['Estimate time and quality for doing the task yourself.','Include briefing, waiting, review, retries and finishing in the assisted route. Keep success likelihood uncertain without relevant local evidence.','Try a bounded case and compare finished, checked work with the baseline. [Inference] Also record responsibility and retained-skill needs that a time calculation misses.'],'Mollick proposes a cost model. His class has no AI-native control group. His separate short-output demonstration excludes setup and review; benchmark rates do not establish local success probabilities.','[[bainbridge-ironies-automation-1983]] and [[metacognitive-demand]] explain why monitoring and recovery work matter; neither establishes net savings here.','Draft-generation time is not completed-task time. Delegation may be unsuitable if results cannot be checked or doing the task is the learning objective. Canonical Mollick overstatements need correction before reuse.','How much time went to review and recovery, and could you judge the result?',[105,84])
c(80,'define-the-delegation-before-the-agent-starts','Define the delegation before the agent starts','An agent will carry out several steps or actions.',['State purpose, deliverable, acceptable result, authority limits and how the result will be checked.','Set checkpoints and what the agent should report when blocked. [Inference] Agree when to stop retries and return control.','Inspect work, supply missing evidence where appropriate, and decide whether to continue, revise or finish yourself.'],'Mollick proposes a brief and reports recovering a blocked slide task. Ramonov proposes goals, constraints and a turn cap; her self-score and marketing uplift are not independent validation.','[[partial-automation-principle]] concerns deliberate human involvement. [[metacognitive-demand]] describes the work supervision can require.','Self-scoring and polish are not success. A blocked image task and weak paper hypothesis show why activity, format and outcomes need separate checks. Textual limits are not technical permission boundaries.','Did you define an inspectable result, and did control return when it could not be met?',[72,356,89,95])
c(375,'preview-and-approve-before-publishing','Preview and approve before publishing','AI helps produce a public video, presentation or other artifact.',['Define the message and factual claims needing checks.','Request an inspectable draft or preview before final rendering or release.','Review the actual artifact: claims, captions, voice, cuts and evidence. [Inference] Open original sources rather than trusting agent-captured proof alone. Review corrections before approving release.'],'Ramonov reports correcting a repository claim and reviewing rough edits in a demonstration involving her product, not a comparative study.','[[reference-verification]] concerns factual checks; review also involves authorship and [[agency]]. Neither validates a particular product.','Final output can differ from a preview. Screenshots can be incomplete. This does not establish copyright clearance, privacy or secure local processing.','Which problem appeared only when you inspected the artifact?')
c(537,'expand-agent-authority-one-tested-step-at-a-time','Expand agent authority one tested step at a time','A team considers moving an assistant from suggestions toward actions.',['Define one bounded responsibility and the surrounding human decisions. Begin with work whose outputs can be reviewed.','Inspect actual errors and correction costs. State what evidence would justify a proposed increase in authority.','Expand one responsibility at a time, with a way to return control. [Inference] Keeping partial assistance is valid; fewer edits alone do not prove readiness.'],'Reganti and Badam describe staged development and a support agent shut down after repeated patches. This is field experience, not a controlled success estimate.','[[partial-automation-principle]] supports selected human involvement. [[bainbridge-ironies-automation-1983]] describes recovery difficulties.','Few edits can reflect disengagement. Small trials can miss rare failures. The clinical example is excluded; this is no medical deployment guidance.','What evidence changed authority, including a choice to stop or roll back?')
c(339,'use-a-prototype-to-brief-a-developer','Use a prototype to brief a developer','You want to make an idea concrete for discussion with a developer who can assess production needs.',['Describe the intended user, task and what the prototype should help communicate or discover.','Build one small feature with AI; inspect and correct it before adding another.','Handoff the prototype with what works, what is rough, intended behavior and open questions about data, login, maintenance and deployment. [Inference] Use dummy information when sensitive data is unnecessary.'],'Hassid reports prototype-to-team communication. Ramonov illustrates incremental construction with her niece. Independent skill and production safety were not measured.','[[shen-skill-formation-2026]] distinguishes completion from skill formation in a different, bounded coding study. It does not validate this prototyping routine.','Screens cannot establish backend correctness or safe data handling. Exclude permission bypass and delayed security review. The developer must investigate what the demo hides.','What became clearer, and what still needs expert investigation?',[350,275])
c(402,'review-ai-code-against-independent-checks','Review AI code against independent checks','You can assess the code and expected behavior, or work with someone who can.',['Review the plan and alternatives; keep changes inspectable.','Write or review expected results and edge cases independently of the generated implementation. Ask AI to help implement and test.','Inspect actual changes, run checks and manually exercise important behavior. Revise or reject failures.','Optional, from Farhan Thawar: another person reviews AI suggestions with you; jointly accept, rewrite or discard them.'],'Ramonov describes expert review and frequent revision. Thawar advocates two humans judging suggestions. Newport supplies an anonymous failure account. No controlled productivity gain is established.','[[shen-skill-formation-2026]] concerns immediate skill formation under specific assistance patterns. Correct software, felt understanding and unaided ability remain distinct.','Generated tests can encode the same mistake as generated code; two humans can share blind spots. Expertise is required. This is not a security or production-readiness guarantee; explanations do not expose internal reasoning.','Could you explain the expected behavior and find an error without consulting the same model?',[636,38])
c(76,'choose-the-human-part-of-the-work','Choose the human part of the work','Some parts of an assisted task matter for your judgment, voice or learning.',['[Inference] Name the contribution you want to make yourself and why it matters.','Use AI for a bounded complementary part: alternatives, critique or a technical subtask.','Accept or reject specific contributions and complete the human part yourself. Mollick describes keeping his wording, reading the work and rejecting some criticism.'],'Mollick reports active, selective use. This sequence is editorially arranged from examples, not a named protocol or measured skill-preservation intervention.','[[partial-automation-principle]] offers a related argument. [[dellacqua-jagged-frontier-2023]] concerns a consulting experiment, not this routine’s long-term learning effects.','A formal split can still leave AI setting the frame. Useful divisions depend on expertise and task. Felt ownership is not proof of capability.','Which substantive choice remained yours, and could you explain it without quoting AI?')
c(276,'curate-context-and-clarify-before-drafting','Curate context and clarify before drafting','The assistant is guessing because the task depends on local goals, examples or constraints.',['Select relevant background, project material and examples. Distinguish references from intended outputs.','Ask AI to read, identify gaps and ask questions before proposing a plan.','Answer questions, correct the plan, and review final work against the original context and purpose.'],'Hassid proposes context folders and plan approval; no measured judgment, skill or general error benefit.','[[agency]] relates to choosing context and purpose; this is an application, not a direct test.','Read-only prompts do not enforce access control. Extra personal context can expose data and add noise. Files go stale; assistants can overlook contradictions.','Which assumption did clarification expose, and did the correction survive into the artifact?')
c(324,'reset-a-drifting-conversation','Reset a drifting conversation','Repeated corrections have obscured the intended task.',['Write your own brief of the result, missing constraints and observed failure. Treat AI failure explanations as suggestions.','Start a fresh conversation with the corrected brief and necessary context; ask about unresolved gaps first.','Answer and assess against the brief. Stop if evidence or expertise is still missing.'],'Hassid proposes conversational repair; no comparison establishes that resets or changing vendors solve the task.','[[agency]] concerns task direction; [[reference-verification]] still applies after a reset.','Resets can lose constraints. Self-explanations may be invented. Repeated resets can avoid the evidence problem rather than solve it.','Did the brief correct an identifiable problem or merely produce a more agreeable answer?')
c(325,'record-a-workflow-before-turning-it-into-instructions','Record a workflow before turning it into instructions','A recurring task has tacit steps or exceptions worth documenting.',['Walk through actual work and capture notes or an appropriate recording, avoiding unnecessary confidential material.','Ask AI to clarify scope, inputs, quality, exceptions, prohibited actions, approvals and escalation before drafting instructions.','[Inference] Compare the draft with another walkthrough including an exception; correct omissions and make human decisions explicit.'],'Hassid proposes recording, questions and SOP creation. The later walkthrough check is a curator addition.','[[partial-automation-principle]] is relevant when instructions preserve necessary participation. No automation or learning outcome is tested here.','One example is not the workflow. Clean instructions can hide judgment or dignify a poor process. Personality-based hiring advice excluded.','Which exception or judgment did the first draft miss?')
c(360,'keep-a-document-and-question-tracker','Keep a document and question tracker','Several official documents need organizing before questions go to an accountable person or organization.',['Collect relevant documents and separate document facts, open questions and confirmed next steps. Supply only appropriate information.','Ask AI to compare supplied documents only, with page/section locations and explicit not-found markers.','Inspect passages yourself. Take unresolved questions to the appropriate source; record who confirmed answers and what remains unknown.'],'AskGwyn proposes this in an insurance-administration guide hosted by Ramonov; no evaluated user outcome.','[[reference-verification]] provides the related document check. Organizing uncertainty does not make AI an insurance, medical or legal authority.','Documents can be stale and locators wrong. Healthcare facts and dates are not extracted as advice. Redaction does not guarantee deidentification.','Can you distinguish a document statement, an open question and a confirmed answer?')
c(361,'settle-the-strategy-before-requesting-a-draft','Settle the strategy before requesting a draft','You are the accountable professional seeking help with an approach you can judge.',['Write the facts, objective and proposed strategy. Make the central professional choice before requesting polished text.','Ask AI for a plan within that strategy; inspect it before drafting or bounded implementation.','Check the actual draft against original material and professional requirements. Keep consequential actions and sign-off with the responsible person.'],'Paula Rojas describes this in legal work; time savings are self-reported, without audited errors, client outcomes or retained expertise.','[[metacognitive-demand]] concerns ongoing judgment effort. [[reference-verification]] applies to citations; neither establishes legality of a specific workflow.','An expert account is not legal advice. Strategy itself can be wrong. Redacted context or local folders are not verified privacy controls.','Which strategic choice did you make before polished text made it seem inevitable?')
c(394,'answer-ai-questions-with-real-evidence','Answer AI questions with real evidence','Planning sounds clear while important facts remain missing or assumed.',['State the decision and separate facts from guesses.','Ask AI what missing information could change the choice. Return to actual records or responsible people; label what cannot be established.','Review options and decide yourself. Do not use model confidence percentages or cross-model agreement as the stopping rule.'],'Ramonov describes returning to SQL data and deleting tasks. Published figures are fictional; later decision quality was not evaluated.','[[reference-verification]] distinguishes generated claims from inspected evidence; [[agency]] concerns ownership of the decision.','Questions can steer toward the wrong objective. A shorter task list and clearer story do not prove a better choice. Models are not independent business experts.','What real evidence changed the decision, and which assumption remains unresolved?')
assert set(rr)==set(ss),set(ss)-set(rr)
def bs(xs): return '\n'.join('- '+x for x in xs) if xs else '- None reported in the reviewed material.'
def citation(i):
 s=ss[i]; return f"{rr[i]['author']}. {s['title']}. {s['date'] or 'Publication date not established'}. {s['url']}"
def wr(p,t):
 q=ROOT/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(t,encoding='utf-8')
for p,d in cc.items():
 i=d['id'];a=rr[i]; ids=[i]+d['support']; links=list(dict.fromkeys(a['related_entries']+[x for j in d['support'] for x in rr[j]['related_entries']]))
 cites='\n'.join('  - '+json.dumps(citation(j),ensure_ascii=False) for j in ids)
 origin='\n\n'.join(citation(j)+'\n\nLocators in `'+ss[j]['source_path']+'`: '+'; '.join(rr[j]['locators'])+'.' for j in ids)
 steps='\n'.join(str(n)+'. '+step for n,step in enumerate(d['steps'],1))
 wr(p,f'''---
status: emerging
area: [preservation]
sources:
{cites}
---

# {d['title']}

Draft only. Integration pending. Title is editorial, not a validated named method.

## Use When

{d['use']}

## Try It

{steps}

## Origin

{origin}

Source passages are paraphrased. Steps arrange the cited guidance; editorial additions are marked [Inference]. Support and failure cases are not independent validation.

## Evidence and Rationale

**Basis:** {a['basis']}

**Observed or reported:** {d['evidence']}

**Related research:** {d['research']}

**Untested:** No direct evaluation of this complete routine was found in the reviewed material. Output quality, later unaided capability, felt competence and calibrated confidence are separate; successful assisted completion does not establish all four.

## Limits

{d['limits']}

## What to Notice

[Inference] Curator-proposed observation, not a validated measure: {d['notice']}

## Related

'''+bs(['[['+x+']] — related local entry inspected; see rationale and limits above.' for x in links])+'\n')
for i,a in rr.items():
 s=ss[i]; w=s['workbench']; paths=a['practice_files']; own=[p for p in paths if cc[p]['id']==i]
 rec={'retain':'PARTIAL','merge':'PARTIAL','counterexample':'PARTIAL','defer':'DEFER'}[a['decision']]
 if i==80:rec='PARTIAL — UPDATE ONLY; skip duplicate source creation'
 links=bs(['[['+x+']]' for x in a['related_entries']]); plist=bs(['`'+p+'`' for p in paths]) if paths else '- No practice draft retained.'
 wr(w+'/practice-review.json',json.dumps({k:v for k,v in a.items() if k!='author'},ensure_ascii=False,indent=2)+'\n')
 wr(w+'/triage.md',f'''# Triage: {s['title']}

## Source

{citation(i)}

Extracted: `{s['source_path']}`. Original snapshot: `{s['original_snapshot']}`.

## Summary and coverage

{a['basis']} {' '.join(a['reported_outcomes'])}

{a['review_note']}

{a['coverage']}

## Relevance

HIGH for human judgment, verification or accountability. Erosion is not inferred from assisted performance.

## Quality and duplication

Practitioner evidence with explicit limits; no direct evaluation of a complete routine is established. Existing entries inspected:

{links}

## Extractable Elements

No new concept or method. Practice decision: **{a['decision']}**; role: **{a['role']}**.

{plist}

## Recommendation

**{rec}**. {a['review_note']}

## Decision

- Outcome: {rec}, for draft review only.
- Date: 2026-09-26
- Reason: Continue authorizes source review and draft preparation; integration pending.
''')
 wr(w+'/distill.md',f'''# Distillation: {s['title']}

## Extraction Ledger

- Source: {'UPDATE proposal for existing mollick-management-ai-superpower-2026, not a new canonical source' if i==80 else 'NEW audit draft, not integrated'}.
- Practices: **{a['decision']}**, role **{a['role']}**; {len(own)} originating cards. Linked cards may originate elsewhere; authorship is preserved.
- Concepts/methods: none. Practices remain a separate draft type.

{plist}

## Key Findings and Locators

Paraphrases from `{s['source_path']}`:

{bs(a['locators'])}

## Reported Outcomes

{bs(a['reported_outcomes'])}

## Proposed Outcomes

{bs(a['proposed_outcomes'])}

## Limits and Excluded Claims

{bs(a['limits'])}

## Coverage

{a['coverage']}

## Decision

- Outcome: PROCEED_TO_CRITIQUE for draft review; no integration. {'Deferred source has no practice extraction.' if a['decision']=='defer' else ''}
- Date: 2026-09-26
- Reason: {a['review_note']}
''')
 wr(w+'/drafts/source.md',f'''---
status: emerging
area: [risk, preservation]
sources:
  - {json.dumps(citation(i),ensure_ascii=False)}
---

# {s['title']}

## Citation

{citation(i)}

## Type and Scope

Practitioner {'interview' if i in (652,537,580,636) else 'article'}; draft only. {'UPDATE proposal for [[mollick-management-ai-superpower-2026]]; do not create a duplicate source.' if i==80 else 'Integration pending.'}

{a['coverage']}

## Key Insight

{a['review_note']}

## Key Findings

Paraphrases from `{s['source_path']}`:

{bs(a['locators'])}

## Evidence

{a['basis']}

Reported:

{bs(a['reported_outcomes'])}

Proposed, not demonstrated effects:

{bs(a['proposed_outcomes'])}

## Supports

{links}

## Limits

{bs(a['limits'])}

Assisted output, unaided capability, felt competence and calibration remain separate. This draft endorses no medical, legal, security or product-capability claim beyond the bounded source account.

## Practice Review

Disposition: {a['decision']}; role: {a['role']}.

{plist}
''')
 blocks=[]
 for p in [w+'/drafts/source.md']+own:
  d=cc.get(p); practic=d['limits'] if d else a['review_note']; adv=d['notice'] if d else a['limits'][-1]
  blocks.append(f'''## `{p}`

### Lens 1 — Evidence: APPROVE AS BOUNDED DRAFT

{a['basis']} {' '.join(a['limits'])} Limits are recorded, not resolved by extraction. No demonstrated learning or calibrated-confidence gain is claimed.

### Lens 2 — Practitioner: APPROVE AS BOUNDED DRAFT

{practic} The draft needs the specified expertise and external checks; it offers no reliability guarantee.

### Lens 3 — Adversarial: FLAGS

The routine could make uncertain material appear authoritative. More steps can add cost without improving judgment. A useful challenge is: {adv} Reputation is not direct validation.

**Synthesis:** Keep only this bounded draft. {a['review_note']} No integration decision made.
''')
 wr(w+'/critique.md',f'''# Self-Critique: {s['title']}

## Overall: FLAGS

Evidence and applicability limits remain visible. Canonical integration is not authorized by this artifact.

## AI Failure Checklist

- [x] Citation identity and guest attribution preserved.
- [x] No experimental method invented; proposal and reported use separated.
- [x] Counts and timings labelled self-report/model flags, not effect estimates.
- [x] Output quality, unaided ability, felt competence and calibration separated.
- [x] Emerging status retained.
- [x] Related stems checked against actual local entries.
- [x] Existing overlaps acknowledged; no new concepts or methods.
- [x] Unsupported medical, legal, privacy/security and model-mechanism claims restricted or excluded.

{chr(10).join(blocks)}

## Contributions to Other Cards

{plist}

## Decision

- Outcome: pending integration review.
- Date: 2026-09-26
- Reason: review and critique completed under Continue. Canonical files unchanged. {'Deferred source has no card; revisit its evidence gaps.' if a['decision']=='defer' else 'No integration or fixed outcome taxonomy adopted.'}
''')
 meta_path=ROOT/w/'source.json'; meta=json.loads(meta_path.read_text(encoding='utf-8-sig'))
 meta.update(status='critiqued',draft_only=True,integration_decision='pending',source_type='transcript' if i in (652,537,580,636) else 'article')
 meta.setdefault('decisions',[]).append(dict(stage='practice_review',date='2026-09-26',decision=a['decision'],scope='draft_only',integration='pending'))
 meta_path.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 with (ROOT/w/'log.md').open('a',encoding='utf-8') as f:
  f.write(f'\n## 2026-09-26 — close-read, draft preparation and critique\n- Coverage: {a["coverage"]}\n- Decision: {a["decision"]}; role: {a["role"]}; originating cards: {len(own)}.\n- Triage, distillation, source draft and three-lens critique recorded.\n- Draft only; integration pending; snapshots preserved.\n')
for p in cc:
 for stem in re.findall(r'\[\[([^\]|]+)',(ROOT/p).read_text(encoding='utf-8')):
  assert any((ROOT/f/(stem+'.md')).is_file() for f in ('concepts','methods','sources','practices')),(p,stem)
print(json.dumps(dict(reviewed_sources=len(rr),practice_cards=len(cc),decisions=dict(Counter(a['decision'] for a in rr.values())),card_paths=list(cc)),indent=2))
