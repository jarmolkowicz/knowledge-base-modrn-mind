# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Render manually authored close-reading decisions for groups 0--4. No inference engine."""
from pathlib import Path
import json

ROOT = Path.cwd()
BASE = ROOT / 'raw/practitioner-practices-development/extraction'
manifest = json.loads((BASE / 'manifest.json').read_text(encoding='utf-8-sig'))
items = {s['id']: s for s in manifest['sources'] if s['group_index'] <= 4}
reviews = {}
cards = {}

def review(i, decision, role, locators, basis, reported, proposed, limits, related, note, practitioner):
    reviews[i] = dict(id=i, group_index=items[i]['group_index'], decision=decision, role=role,
        locators=locators, basis=basis, reported_outcomes=reported, proposed_outcomes=proposed,
        limits=limits, related_entries=related, review_note=note, practitioner=practitioner)

def card(i, stem, title, use, steps, origin, evidence, research, untested, limits, notice, related, supports=()):
    cards[stem] = dict(id=i, title=title, use=use, steps=steps, origin=origin, evidence=evidence,
        research=research, untested=untested, limits=limits, notice=notice, related=related, supports=list(supports))

review(22,'retain','origin',['L23–39, Ideas 1–3'], 'Author-proposed work-design heuristics with an anecdote about a professor obtaining datasets.',
    ['No evaluation of these three interventions reported.'], ['Direct tool use toward meaningful progress and the limiting step.'],
    ['The cited 164,000-worker study was not independently checked here. Paper counts and completed-project counts can distort quality; faster bottleneck work may expose a different bottleneck.'],
    ['effort-investment-review','memmert-effort-management-2025'],
    'Retain scoreboard/bottleneck procedure, not the opening causal productivity claim. Separate protected focus blocks into the attention group.',
    'Ask the person to choose value and quality criteria; do not let AI choose the goal or equate more papers with better research.')
review(263,'merge','support',['L97–141, five rules','L147–174, goal and weekly-audit prompts'],
    'Ruben Hassid describes a company gameplan and supplies prompts; promotional newsletter with informal observations.',
    ['Reports conversations with people who feel busier and more exhausted; no assessed outcomes of the proposed gameplan.'],
    ['Choose work with a clear purpose and set stopping boundaries.'],
    ['The three-for-one task deletion ratio and 8pm cutoff are arbitrary examples. Disagreeing with an AI audit is not evidence that it works. AI should not force one goal or decide what matters. Claims of addiction and Harvard confirmation are not established by this article.'],
    ['effort-investment-review'], 'Merge problem-before-prompt and output-necessity ideas into Newport; last-prompt boundary supports stopping card. Exclude coercive goal-selection prompt.',
    'Retain human goal choice and context-sensitive stopping time; allow several legitimate obligations.')
review(64,'merge','support',['L10–36, uses','L38–50, five non-use cases'],
    'Ethan Mollick offers explicitly contextual experience-based advice with research links.',
    ['Gives examples of AI-generated alternatives; no test of the whole decision checklist.'],
    ['Choose assistance according to learning purpose, checkability and acceptable failure.'],
    ['Tool capability examples are dated 2024. Broad statements about when effort is the point are judgment calls, not a universal ban on learning support. Linked studies not all verified.'],
    ['cognitive-offloading','think-first'], 'Merge decision criteria and learning-purpose boundary; no separate 20-item practice card.',
    'Support access and task completion where these are the goal; retain the specific reasoning someone intends to practise.')
review(408,'retain','origin',['L111–145, Three questions before you trust an AI agent'],
    'Sam Illingworth proposes three governance questions, illustrated with secondary accounts of failures.',
    ['No outcome data for the questions.'], ['Keep consequences, reversibility and human responsibility visible.'],
    ['Game theory does not require human feelings, so the claim that the game collapses without felt stakes is too broad. Mechanical descriptions can also oversimplify what a system does. Cases and amounts not independently verified here.'],
    ['cognitive-offloading'], 'Retain cost-bearer and recovery checks; revise the language check into a factual permissions/action description rather than a forced slogan about pattern matching.',
    'Require a real owner, recovery route and authorization boundary; asking questions alone cannot provide these controls.')
review(416,'merge','support',['L28–36, Step by step','L56–72, Ilia Karelin account','L82–88, reflection'],
    'Ilia Karelin contributes a prompt and personal coding/SQL reflection, hosted by Sam Illingworth.',
    ['Karelin reports recognizing reduced opportunities to form and test hypotheses; explicitly notes Claude cannot know time spent before prompting.'],
    ['Identify a thinking step to retain in a real task.'],
    ['AI cannot diagnose lost skill from chats. The account does not measure skill decline or causal effects. The prompt presupposes a loss.'],
    ['cognitive-offloading','six-pattern-diagnostic'], 'Merge with protected-task choice; base review on the person’s own task trace before consulting AI.',
    'Name an observable skipped step, not a personal deficit. Keep accommodation tools and irrelevant friction separate.')
review(464,'merge','support',['L15–45, correction and arithmetic','L113–139, accessibility and five actions'],
    'Sam Illingworth combines environmental commentary and five proposed actions.',
    ['Reports correcting an earlier public note after reader feedback; no evaluated behavioral outcomes.'],
    ['Check whether output serves anyone; ask procurers for environmental evidence.'],
    ['Internal arithmetic error: 1–2 trillion litres/year divided by 365 and 5.4 million litres/training yields about 507–1,015 trainings/day, not hundreds of thousands. Model size or price is not a verified environmental ranking. Policy and per-query figures require separate verification.'],
    ['effort-investment-review'], 'Retain output-necessity support only in this allocation. Environmental procurement is a separate evidence task; no environmental saving estimate enters the draft.',
    'Preserve the explicit accessibility caveat. A useful access aid is not waste simply because its benefit is personal.')
review(523,'retain','origin',['L24, Timo Mason credit','L36–56, Step-by-step','L76–110, contributor example','L130–136, reflection'],
    'Timo Mason’s first-person prompt experiment plus a one-week practice proposed with Sam Illingworth.',
    ['Different stated business purposes elicited different suggested protected tasks; connection with people recurred.'],
    ['Make a personal non-delegation choice visible and enact it.'],
    ['Model answers are suggestions, not evidence of the person’s values or future skill atrophy. No assessment of retained skill or improved relationships. Never-automate language is too absolute for accommodations and changing circumstances.'],
    ['cognitive-offloading','think-first'], 'Retain one chosen task and written reason, with revisable boundaries and explicit human purpose before AI input.',
    'Make the commitment manageable; a protected reasoning step can be smaller than a whole task.')
review(52,'defer','deferred',['L11–26, A Deliberate Morning'],
    'Cal Newport’s personal account of preparing 21 graduate computation lectures over a semester.',
    ['Reports better tolerance of concentration and perceived transfer to research.'],
    ['Practise difficult material without distraction.'],
    ['No independent measurement or comparison. Three hours of strain is not a general learning prescription. Snapshot has no publication date and links to spring 2012; 2026 in workbench name is a catalog fallback.'],
    ['bjork-desirable-difficulties-2011'], 'Defer a separate practice: general concentration account adds limited AI-specific procedure beyond protected attention and assessed practice.',
    'Do not prescribe long uninterrupted sessions to every learner; difficulty requires prerequisites and can become unproductive.')
review(521,'retain','origin',['L26–44, Step-by-step','L52–64, personal example','L72–80, reflection'],
    'Sam Illingworth offers a stopping exercise and a first-person poetry/climate example.',
    ['Reports a changed understanding while considering one question outdoors after closing the chat.'],
    ['End the generation loop and leave time for independent reflection.'],
    ['Anecdote does not establish an incubation benefit. Walking, touch and body attention are optional; no clinical claim. AI’s selected thought may frame reflection too narrowly.'],
    ['effort-investment-review'], 'Retain deliberate ending and one held question; make human selection explicit.',
    'Allow a seated or screen-based accessible pause and continuation of assistive technology.')
review(589,'retain','origin',['00:04:40–00:06:49, L69–79'],
    'Chip Huyen answers the host’s question about building AI products, drawing on practitioner experience.',
    ['Reports discussions where optimal technical choices offered little improvement and switching would be costly. No measured attention outcome.'],
    ['Spend investigation effort where a technology choice can change the result.'],
    ['Estimated gain and switching cost are uncertain. Some monitoring is required for maintenance, accessibility or obligations even without an immediate feature gain.'],
    ['effort-investment-review'], 'Retain the two concrete questions and the option to defer a technology decision.',
    'Give a deferred choice a revisit trigger; this is not permission to ignore required updates.')
review(616,'counterexample','counterexample',['00:48:07–00:50:41, L504–529; email account at 00:49:09'],
    'Edwin Chen’s first-person account embedded in discussion of model incentives.',
    ['Reports spending 30 minutes across 30 email versions on a message he later judged unimportant.'],
    ['Use as failure evidence for deciding when enough is enough.'],
    ['One recollection; no measured counterfactual time or proof of a company’s objective function. Asking AI to tell the user to stop also delegates the value judgment.'],
    ['effort-investment-review'], 'Counterexample supporting stopping, not a new prompt recommendation.',
    'The person defines sufficient quality and importance; do not outsource the stopping rule to a reassuring model.')
review(668,'retain','origin',['00:15:40–00:30:03, L147–235; highlight at 00:20:54; reflection at 00:23:14'],
    'Jake Knapp and John Zeratsky explain their Make Time framework with personal use examples; Knapp credits Zeratsky with the highlight.',
    ['Both describe recurring experimentation rather than perfect adherence; host reports finding a daily highlight useful.'],
    ['Protect a chosen meaningful period and learn which attention tactics fit.'],
    ['This is a non-AI routine; adapting it to AI distraction is an inference. Suggested 60–90 minutes is not a validated minimum. Autonomy over calendars varies.'],
    ['effort-investment-review'], 'Retain a clearly labeled transfer practice, including joy and relationships rather than only productive output.',
    'Pick a feasible block and revisit without treating missed days as failure.')
review(735,'defer','deferred',['01:01:48–01:09:45, L449–507; audit at 01:04:10'],
    'Matt Mochary describes a coaching energy audit and reports use with Brex founders; credits Diana Chapman for four zones.',
    ['Reports that founders redistributed internal/external meetings; host describes a simpler personal energy review.'],
    ['Notice draining work and redesign, stop or redistribute it.'],
    ['Clip title/date and full-interview body do not align; description links another full episode. Subjective recalled energy is not skill, importance or objective productivity. 80% green and nine-in-ten claims are not validated targets.'],
    ['effort-investment-review'], 'Defer separate AI transfer card: useful general audit but provenance and added contribution require resolution.',
    'Workload cannot always be delegated; do not transfer unwanted work without considering another person’s workload and consent.')
review(739,'counterexample','counterexample',['01:15:00–01:19:14, L423–448; reverse-zip example at 01:18:13'],
    'Mayur Kamat describes AI uses at companies and criticizes expanding short messages only to compress them again.',
    ['Illustrative communication pattern; no evaluated intervention.'],
    ['Question unnecessary generation and reader burden.'],
    ['Longer text can add necessary context or accessibility. Company productivity claims are rough self-reports, not evidence for this communication heuristic.'],
    ['effort-investment-review'], 'Keep as counterexample to output volume, supporting goal-first and stopping cards.',
    'Compare the information the reader needs, not word count alone.')
review(66,'retain','origin',['L18–34, learning qualifications','L36–61, own ideas and own draft first','L67–85, collective-thinking context'],
    'Ethan Mollick combines research commentary with his stated writing routine.',
    ['Reports fully drafting posts before requesting reader/editor feedback, then sometimes choosing generated alternatives.'],
    ['Preserve an independent initial direction before AI suggestions.'],
    ['His own routine is not a randomized intervention. Study summaries do not prove a universal sequence effect; blanket brain-safety and laziness claims excluded. Related creativity metrics differ from durable creative capability.'],
    ['think-first','bjork-desirable-difficulties-2011','cognitive-offloading'], 'Retain independent seeds/draft, then purposeful comparison, with timing and format adapted to task.',
    'No fixed solo duration or requirement to struggle beyond useful prerequisites; keep necessary access aids.')
review(414,'retain','origin',['L53–74, Tina Austin critique','L80–128, revised exercise and limits','L132–148, classroom procedure'],
    'Joint public exchange between Sam Illingworth and Tina Austin, ending with a proposed classroom design.',
    ['Documents correction of an earlier study claim and a revised exercise; no student outcome data for this exercise.'],
    ['Keep initial position, opposing argument construction and explanation of revision with the learner.'],
    ['The 22 interviews discussed cannot demonstrate durable trait change. Divergent outputs can arise from prompts, context and sampling, not necessarily user identity. Forty-minute timing is proposed, not optimized. Excessive questioning can exhaust learners.'],
    ['think-first','bjork-desirable-difficulties-2011'], 'Retain the September procedure rather than the earlier AI-generates-both-sides version; explicit attribution to both authors.',
    'Record the baseline by speech, drawing or typing; give novices source material and teacher support.')
review(879,'merge','support',['EPUB [ch.6 — xhtml/xhtml-0-5.xhtml], Introduction, source.md L23','EPUB [ch.21 — xhtml/xhtml-0-20.xhtml], Conclusion: What Lasts, source.md L98, One thing to try this week'],
    'Sam Illingworth’s book introduction and conclusion; scoped book reading, not cover-to-cover.',
    ['Conclusion proposes two sentences before prompting and counting occasions when no prompt was needed. No trial data for this procedure.'],
    ['Articulate one’s answer and uncertainty before asking AI.'],
    ['Two sentences is a convenient proposed format, not a validated dose. Book-wide research claims and current technology anecdotes not verified by this scoped reading.'],
    ['think-first'], 'Merge concise two-sentence variant into independent-first card; preserve existing book metadata and audit trail.',
    'Allow spoken/drawn notes and uncertainty; an initial position need not be confident or correct.')
review(880,'retain','origin',['Printed chapter 7, Reclaiming Agency; EPUB [ch.25 — xhtml/xhtml-0-24.xhtml], source.md L113; Sequence Matters and Protect the Baseline'],
    'John Nosta’s philosophical/practitioner synthesis, with secondary research interpretation.',
    ['Proposes periodic unaided performance checks and deliberate practice without assistance; no evaluation of the proposed routine.'],
    ['Track a specific capability separately from assisted output.'],
    ['Underlying clinical study not independently verified locally. Do not turn a reported performance drop into proven skill atrophy. The MIT crossover is not proof of the precise outline-first intervention claimed. No validated alternation ratio or interval.'],
    ['strategic-alternation','think-first','nosta-ai-rebound-2025','nosta-borrowed-mind-2026'],
    'Retain conditional baseline-check draft; existing source remains integrated, with update proposal only. This adds no new empirical confirmation.',
    'Practise safely; retain accommodations and avoid removing safeguards in live high-stakes work.')
review(459,'retain','origin',['L18, Rebecca J Hogue credit','L32–42, exercise','L62–80, comparison of rough/polished passages'],
    'Rebecca J Hogue’s personal writing experiment, hosted by Sam Illingworth.',
    ['Reports more useful focus after limiting feedback to five areas; rejects some advice as contrary to style; perceives improvement in later drafts.'],
    ['Use criticism to perform one’s own revision.'],
    ['No independent assessment of improved writing or transfer. Five areas/200 words are examples, not established optimum. Data-training settings do not settle every confidentiality or authorship question.'],
    ['think-first','cognitive-offloading'], 'Retain clear feedback-without-replacement procedure and human rejection examples.',
    'Describe the intended effect and let the author decline a suggestion; use a small shareable excerpt.')
review(460,'retain','origin',['L61–84, Illingworth poem editing','L194–208, Joshua Sherman songwriting and checklist','L86–192, other contributor accounts for context'],
    'Multi-contributor practice collection co-edited by Alyssa Fu Ward; specific first-person accounts from Illingworth and Joshua Sherman.',
    ['Illingworth accepted two critiques and kept another image. Sherman describes revisions he authored, rejecting AI advice, and a personal checklist applied without AI.'],
    ['Convert creative disagreement into reusable human craft criteria.'],
    ['Selected self-reports, not independent quality assessment or representative sample. Contributor practices differ: some do use generated material; no universal AI-never-writes claim. Legal borrowing claims not adopted.'],
    ['think-first','cognitive-offloading'], 'Merge criticism examples into Hogue card; retain Sherman’s reusable craft checklist as a distinct downstream routine.',
    'Credit each contributor separately. A checklist expresses a creator’s choices, not universal rules of art.')
review(449,'counterexample','counterexample',['L23–39, poll and correction','L95–111, attrition interpretation','L115–164, four literary tests'],
    'Sam Illingworth’s informal reader poll and a framework drawn from comments by Pawel Jozefiak, leroy heszler, Stephen Hall and Mia Kiraki.',
    ['Reports roughly 57% voting accuracy and a factual copying error; poll participation declines across excerpts.'],
    ['Promotes evaluation of text rather than AI-authorship detection.'],
    ['No linked participant-level evidence shows attrition caused by attention decay. Omissions, felt necessity and moral risk cannot detect absence of thought. Clear comprehensive text can reflect substantial thinking.'],
    ['think-first'], 'Downgrade from a candidate reading practice to critique support. Do not publish the four tests as a diagnostic of thought or human authorship.',
    'The author’s useful shift toward evaluation does not validate his particular criteria. Ground criticism in purpose, claims and evidence instead.')
review(480,'merge','support',['L20–45, sharing and reflecting','L51–58, rosemary-and-bleach example'],
    'Sam Illingworth’s personal memory-response example and proposed reflective exercise.',
    ['Describes finding the model’s generic interpretation unfaithful to his memory’s significance.'],
    ['Notice where a model’s reading diverges from the author’s intended meaning.'],
    ['Neither human recall nor model response establishes factual memory accuracy. No therapeutic, general comprehension or capability measure. Sharing intimate memories is unnecessary.'],
    ['cognitive-offloading'], 'Merge as an optional intended-meaning check in author-led critique; no separate memory prompt card.',
    'Use a non-sensitive or fictional passage and evaluate textual fit, not private emotional truth.')
review(516,'counterexample','counterexample',['L33–65, method and interpretive caveat','L69–133, findings and positive case','L145–177, AI role and limitations','L181–203, extrapolation'],
    'Sam Illingworth reports an open exploratory exercise: one model, ten poems, thirty outputs and one human coder.',
    ['Reports competent formal analysis, a reading that changed his view of one poem, and differences from his personal associations.'],
    ['Examines limits of AI as a critical reader.'],
    ['Published/unpublished status does not establish training-data membership. Authorial intention is not the sole valid interpretation. One coder, unpiloted prompts and text variants limit the study. Poetry disagreements do not establish clinical or universal comprehension failures. Repository not independently audited.'],
    ['think-first'], 'Use as a bounded counterexample to treating AI critique as final authority. No separate diagnostic practice.',
    'Allow useful disagreement with the author; prefer specific textual reasons over claims that only one reader knows the meaning.')
review(801,'merge','support',['18:15–20:42, L154–167; process at 19:20'],
    'Seth Godin explains how he used Claude while writing his book; direct first-person interview account.',
    ['Reports finding missing list items, unsupported claims and voice mismatches while writing the words himself.'],
    ['Use an additional reader to find omissions and unsupported argument.'],
    ['No independently assessed improvement. Perceived kindness or humility is not reliability. Suggested missing items need factual checks.'],
    ['think-first'], 'Merge into Hogue critique card as a substantive variant, with distinct attribution.',
    'Ask for locations and explanations; the author decides whether something is missing and checks evidence.')
review(514,'retain','origin',['L27–75, study interpretation','L109–151, three exercises and audit question'],
    'Sam Illingworth proposes workplace exercises from Shen and Tamkin’s exploratory coding interaction patterns.',
    ['No outcomes for the proposed workplace exercises. Cited study compares AI access and describes small behavior clusters.'],
    ['Ask conceptual questions then perform a task; investigate generated work before accepting it.'],
    ['Strategies were not randomized. Local research entry gives low-cluster mean around 39%, not learned nothing. Durable skill atrophy, universal learning loss and transfer beyond coding are not established. Model explanations are generated rationales, not records of internal decisions.'],
    ['shen-skill-formation-2026','six-pattern-diagnostic','bjork-desirable-difficulties-2011','fernandes-metacognition-2025'],
    'Retain question-first exercise, distinguish variants and add a real attempt instead of relying on Could I do it? self-report. Reject moral framing that needing AI means avoiding learning.',
    'Separate learning goal from assisted task completion. Keep access aids, external answers and human instruction available.')
review(422,'retain','origin',['L31–107, study accounts','L111–145, four-move protocol'],
    'Sam Illingworth proposes diagnosis-before-feedback and reconstruction, drawing on three studies not independently reviewed in this allocation.',
    ['No evaluation of the complete four-move protocol. Reports trial and correlational findings from other sources.'],
    ['Compare one’s own diagnosis with feedback, then reconstruct reasoning.'],
    ['Model disagreement is not a cure for sycophancy. Broad conceptual questions are not always superior to procedural ones. Cited new studies need original-source review before their effect claims are reused.'],
    ['think-first','bjork-desirable-difficulties-2011','fernandes-metacognition-2025'], 'Retain diagnosis and reconstruction as proposed practice. Do not claim this exact protocol was tested in the cited trial.',
    'Teacher support is needed where learners cannot diagnose their work; allow oral/drawn reconstruction and errors as information.')
review(698,'retain','origin',['00:21:31–00:26:40, L171–196; teach-back at 00:25:55'],
    'Julie Zhuo describes personal AI study and a workplace example involving learning analysis context.',
    ['Reports explaining a concept back in an analogy and receiving critique; no delayed retention or independent correctness assessment.'],
    ['Expose gaps in a learner’s explanation.'],
    ['Friendly feedback can obscure disagreement or error. Learning preferences are not validated learning styles. AI being a better teacher than humans is not established by this account.'],
    ['fernandes-metacognition-2025','bjork-desirable-difficulties-2011'], 'Retain learner-first teach-back with independent checks; merge overlapping generation-comprehension variant from Illingworth.',
    'Learner explains in their own form before seeing the correction; leave unresolved points unresolved until checked.')
review(658,'retain','origin',['01:21:17–01:30:33, L771–874; Aristotle details at 01:26:46–01:29:49'],
    'Hilary Gridley describes a GPT she built to generate LSAT-style reasoning questions in product-management contexts.',
    ['Shows the intended scenario/multiple-choice/feedback loop and says practice can be more frequent; no learning measurement.'],
    ['Get more opportunities to reason about familiar work situations.'],
    ['Generated answer keys can be wrong; product decisions are not always deductive with one right answer. More reps and subjective confidence do not establish transfer or calibration. Engineering estimates need actual system context.'],
    ['fernandes-metacognition-2025','bjork-desirable-difficulties-2011'], 'Retain bounded reasoning rehearsal; do not infer validated judgment training from custom GPT availability.',
    'Use fact-bounded exercises and checked explanations; do not let simulated correctness settle a real product decision.')
review(77,'retain','origin',['L18–40, pilot context and goal-play','L46–60, broader prompt/tool context'],
    'Ethan Mollick describes educational prompts developed with collaborators and a fictional Hamlet demonstration.',
    ['Reports piloting similar experiences and explicitly calls for effectiveness studies. In goal-play the student applies a framework to guide a fictional character.'],
    ['Practise applying a known framework by helping a simulated learner.'],
    ['Complete reusable prompt resides in linked material not this snapshot; draft is a labeled adaptation of the described activity. Role-play is not an authentic person, literary interpretation or measured transfer.'],
    ['bjork-desirable-difficulties-2011','cognitive-offloading'], 'Retain the student-does-the-explaining structure; avoid claiming to reproduce an unseen prompt verbatim.',
    'Instructor checks the scenario against the learning goal; simulation facts and feedback require review.')
review(427,'retain','origin',['L22, Mahelet G Fikru credit','L30–40, exercise','L44–98, economics example and follow-up'],
    'Mahelet G Fikru reports designing questions with ChatGPT and describes related flipped-classroom practice with personal cases, coauthored with Sam Illingworth.',
    ['Shows a revised EV supply/demand question and describes asking follow-up questions on student examples; no assessed learning gain.'],
    ['Elicit an explanation of why a concept applies or fails in a concrete case.'],
    ['Personal examples and counterintuitive questions are not AI-proof. A model can invent experiences or answer the question. Difficulty alone does not establish retention, and a fluent answer is not sufficient evidence of human understanding.'],
    ['bjork-desirable-difficulties-2011','fernandes-metacognition-2025'], 'Retain teacher-checked case explanation; reject the headline claim of questions AI cannot fake.',
    'Offer a shared case for people who cannot or do not wish to disclose personal experience; use live follow-up and explicit criteria.')
review(262,'defer','deferred',['L62–84, formula explanation','L182–196, review limits','L208–228, concluding advice'],
    'Ruben Hassid gives a tool tutorial and example requests, with commercial promotion.',
    ['Shows requests to explain and trace formulas; no learner outcome or independent formula-check results.'],
    ['Understand a spreadsheet’s formulas and inputs.'],
    ['Most content concerns output production and installation. Product comparisons, prices and capabilities are time-sensitive and not verified. Explanation alone cannot establish comprehension or correct calculations.'],
    ['cognitive-offloading','fernandes-metacognition-2025'], 'Defer standalone card. Formula tracing can be an example in teach-back, but stronger sources supply the human learning check.',
    'Do not treat the model’s explanation as a workbook audit or financial validation.')

card(22,'choose-the-result-before-the-tool','Choose the result before the tool',
    'A tool makes individual tasks faster, but the important project is not moving. Newport proposes judging progress at the level of valuable work.',
    ['Name the result you are trying to produce and how you will recognize useful quality. Write this before asking AI for work.',
     'Identify the step currently limiting progress. Use an actual project example rather than assuming the slowest visible task is the bottleneck.',
     'Choose a bounded use of AI that could improve that step. If the proposed output serves no clear purpose, stop or remove the task.',
     'Compare progress on the chosen result after using the tool. Include checking, correction and recipient effort. [Inference] Keep a short before/after note; this is an editorial observation aid.'],
    'Editorial label for Cal Newport, “Avoiding Digital Productivity Traps,” 23 March 2026, Ideas 1–3, L23–39. Ruben Hassid, “Workaholic.”, 22 February 2026, L101–141, supplies the one-sentence problem and output-necessity variants. Illingworth (1 May 2026), L135, adds a use/read/remember test.',
    'Proposed heuristics and a dataset-access anecdote, not a measured intervention. Hassid reports busyness in conversations; this does not establish the cause.',
    '[[memmert-effort-management-2025]] reports professional accounts of effort moving to checking, learning and other tasks. It supports examining total work, not the efficacy of this routine. Closely overlaps [[effort-investment-review]].',
    'Whether this improves judgment, project value or workload in a particular setting. More output and less elapsed time are separate outcomes.',
    'A numerical scoreboard can reward quantity at the expense of quality. Add the quality or care requirement the number misses. Do not adopt the fixed three-task deletion ratio or let AI force a single life goal. Some work matters because it maintains access or relationships.',
    '[Inference] Did the limiting step change, or did the tool only create more material to review?', ['effort-investment-review'], [263,64,464,739])
card(408,'name-consequences-before-delegating','Name consequences before delegating',
    'You are deciding whether AI should act on something you care about, rather than only draft a suggestion.',
    ['Name who would bear the cost of a plausible serious mistake. The responsible reviewer and affected person may differ.',
     'List the actions the tool is allowed to take and which cannot be undone. Check that a backup, version or recovery route actually exists.',
     'For actions you cannot reliably reverse, choose a human approval point or keep the action manual.',
     'Describe the allowed operation in concrete terms: what it reads, changes or sends. If you do not know, find out before expanding access. This is an editorial revision of the source’s language check.'],
    'Sam Illingworth, “AI Agents Do Not Play Games. You Do.”, 4 March 2026, three questions, L111–145. Editorial label and more precise permissions wording.',
    'A proposed governance checklist illustrated with secondary failure stories. No measured outcomes for the checklist.',
    'No study of this checklist reviewed. [[cognitive-offloading]] helps distinguish delegating execution from relinquishing responsibility; it does not validate this governance routine.',
    'Whether asking these questions changes deployment choices or prevents loss.',
    'A named owner is insufficient without time, authority and controls. The source overstates its game-theory argument; subjective stakes are not required for mathematical agents. Avoid a false reassurance that reversible actions have no consequences.',
    '[Inference] Can you point to the actual approval and recovery mechanism, rather than a statement that a human is in charge?', ['cognitive-offloading'])
card(523,'keep-one-thinking-step','Keep one thinking step for yourself',
    'A recurring task is easier to delegate, but you want to retain a specific form of judgment, care or skill practice.',
    ['Choose a recent real task. Describe what you actually did and what AI did, including thinking before the chat.',
     'Name the part you value doing or need to practise. If helpful, ask AI for possible trade-offs, then reject claims it cannot know about your behavior.',
     'Choose one task or step to handle yourself this week. State why and keep the sentence visible.',
     'Do the chosen step and review whether the boundary was useful. [Inference] Revise the boundary when the purpose, support needs or task changes.'],
    'Timo Mason with Sam Illingworth, “How to Hold on to What Should Stay Human,” 13 November 2025, L36–56 and L76–110. Ilia Karelin with Illingworth, “What AI Takes When You Aren’t Looking,” 23 December 2025, L28–36 and L56–72, adds task-specific reflection. Human task tracing before AI is an editorial adaptation.',
    'Contributor self-reports and a proposed one-week commitment. Mason obtained different suggestions under different business purposes. Karelin explicitly recognizes that Claude did not know his offline effort.',
    '[[cognitive-offloading]] distinguishes task delegation from demonstrated capability loss. [[six-pattern-diagnostic]] is an unvalidated reflection aid, not a diagnosis of a person.',
    'Preservation of skill, agency or meaning over time. The ability to name a valued step does not itself measure any of these.',
    'AI cannot identify your values or diagnose atrophy from a conversation. Do not remove accommodations, require needless pain or declare whole categories forever human-only. A person may retain the judgment while using speech, translation or other support.',
    '[Inference] What did you actually choose or work out during the protected step, and was that what you intended to keep?', ['cognitive-offloading','six-pattern-diagnostic'], [416,64])
card(521,'carry-one-question-offline','Carry one question away from the chat',
    'A conversation keeps producing more material and you need to end it or make room for your own reflection.',
    ['Choose one unresolved thought worth carrying forward. The source suggests asking AI for one thought from the chat; you decide whether its suggestion fits.',
     'Close the conversation. Keep the question in a form you can access without reopening the generation loop.',
     'Pause in a setting that works for you. The author goes outside; a seated pause or shift of attention is equally available.',
     'Let your own associations develop before requesting another answer. Stop without producing an insight if none comes.'],
    'Sam Illingworth, “When AI Never Stops, Should You?”, 30 September 2025, Step-by-step L26–44 and personal example L52–64. Edwin Chen, Lenny’s Podcast, 7 December 2025, 00:49:09–00:49:59, supplies a distinct over-iteration counterexample. Editorial title.',
    'Illingworth reports an insight about poetry while sitting outside. Chen recalls 30 minutes spent refining an inconsequential email. Neither account measures the effectiveness of a stopping routine.',
    'No direct evaluation reviewed. [[effort-investment-review]] supplies an adjacent way to notice effort spent after initial production.',
    'Any effect on insight quality, attention or reduced work. A pleasant pause is not evidence of better reasoning.',
    'Walking, touch and noticing bodily feelings are optional, not requirements. Keep assistive technology. An unresolved urgent task may need handoff rather than a reflective pause. The model should not determine what matters or whether your work is good enough.',
    '[Inference] Did you stop when you intended, and did the next useful thought come from you, another person, a source, or more generation?', ['effort-investment-review'], [263,616,739])
card(589,'ask-what-an-update-would-change','Ask what an update would change',
    'You are drawn into comparing models, frameworks or AI news while trying to finish a real piece of work.',
    ['Name the decision the new information could change.',
     'Estimate how much difference the best technical choice would make compared with a good-enough existing choice. Mark what you do not know.',
     'Ask how difficult switching away from the new choice would be.',
     'Investigate further when the likely gain or required obligation warrants it; otherwise defer. [Inference] Record what failure, change in need or maintenance deadline would make you revisit.'],
    'Chip Huyen, Lenny’s Podcast, 23 October 2025, 00:04:40–00:06:49 (L69–79). Two questions from the source, plus an editorial revisit trigger.',
    'Practitioner advice drawn from discussions about AI product building; no measured reduction in distraction or improvement in technical choices.',
    'Related to [[effort-investment-review]]: effort allocated to tools is part of work, not free overhead. No validation of this heuristic reviewed.',
    'Accuracy of estimated improvement and whether deferring investigation improves the outcome.',
    'A small immediate gain can conceal a longer-term compatibility, security or accessibility need. This is a decision filter, not a rule to ignore updates. Avoid pretending an uncertain estimate is a precise calculation.',
    '[Inference] Which update actually changed a decision, and which only consumed attention?', ['effort-investment-review'])
card(668,'protect-a-daily-highlight','Protect a daily highlight',
    'Important work or a valued personal activity gets displaced by messages, feeds or ongoing AI conversations. This is an AI-context adaptation of a non-AI routine.',
    ['At the start of the day ask what you would like to call its highlight when looking back. It can be urgent work, something satisfying, joy or time with a person.',
     'Write or record the highlight somewhere visible and reserve a feasible block for it.',
     'Choose one environmental change that makes attention possible. [Inference] For AI distraction this might mean ending unrelated chats during the block.',
     'Afterward notice whether the block and tactic helped. Adjust tomorrow as an experiment rather than adding every tactic at once.'],
    'Jake Knapp and John Zeratsky, Make Time discussion on Lenny’s Podcast, 11 February 2024, 00:20:30–00:30:03. Knapp credits Zeratsky for the highlight. AI-specific application and flexible recording format are editorial adaptations.',
    'Authors and host describe personal use. They explicitly describe imperfect days, different preferences and repeated experimentation; no causal evaluation presented.',
    'No study of this AI adaptation reviewed. Complements [[effort-investment-review]] by allocating time according to the person’s chosen value.',
    'Whether it improves attention, satisfaction or progress for a specific person. These outcomes are different.',
    'The source’s 60–90-minute suggestion is not a minimum. Use a shorter or divided period when care work, disability, shift work or shared calendars require it. Not achieving a highlight is not evidence of poor discipline.',
    '[Inference] Did you spend any protected attention on the thing you chose, and what made that easier or harder?', ['effort-investment-review'])
card(66,'save-your-own-starting-point','Save your own starting point',
    'You want AI to extend or critique your ideas while keeping a visible record of what you thought before its suggestions.',
    ['Read or encounter enough of the actual material to form a tentative view. Record a sketch, outline, rough draft or a few ideas of your own.',
     'For a short decision, try the book variant: state what you currently think and what you most need to know. Uncertainty is a valid starting point.',
     'Ask AI to address a specific need: alternatives, an unclear point or an objection. Keep the original visible.',
     'Choose what to revise and explain why. Keep, change or discard suggestions; if your own first pass is sufficient, do not prompt further.'],
    'Ethan Mollick, “Against Brain Damage,” 7 July 2025, L53–61. Marty Cagan, Lenny’s Podcast, 10 March 2024, 00:49:51–00:51:47, describes reversing his AI-first advice after observing overtrust. Sam Illingworth, Slow AI (2026), Conclusion “One thing to try this week,” EPUB [ch.21], source.md L98, supplies the two-sentence variant. Editorial consolidation.',
    'Mollick reports his writing routine; Cagan reports a change in practitioner advice. Illingworth proposes counting occasions when no AI answer was needed. None tests this consolidated routine.',
    'Overlaps [[think-first]], already labeled an inference in the KB. [[bjork-desirable-difficulties-2011]] supports distinguishing generation opportunities from fluent performance, with prerequisites; it did not test this AI sequence.',
    'Reduced anchoring, greater authorship, improved creative work and retained unaided ability. These should not be inferred from simply saving an initial note.',
    'The initial view can be wrong and can itself anchor later judgment. Keep it revisable. No fixed solo-work duration, forced struggle or ban on accommodations. Novices may need source material or instruction before an independent attempt is useful.',
    '[Inference] Which change came from new evidence, which from a suggestion, and which from your own reconsideration?', ['think-first','bjork-desirable-difficulties-2011'], [879,729,880,64])
card(414,'build-the-opposing-case-yourself','Build the opposing case yourself',
    'A classroom or learning group wants students to practise reasoning rather than watch AI conduct both sides of a debate.',
    ['Give learners a shared question and suitable source material. Each records an initial position before the model responds, using speech, drawing or text.',
     'Ask AI for a strong objection to that position.',
     'The learner constructs the opposing case themselves, checking its evidence and assumptions. Do not ask AI to provide the final rebuttal and verdict.',
     'Compare several different arguments as a group. Anyone revising their position explains what moved them. The teacher can share their own initial position too.'],
    'Sam Illingworth and Tina Austin, “AI Changes the Learner. But Do We Know How?”, 10 September 2026, revised exercise L110–128 and classroom design L132–148. Editorial label; preserved contributor credit.',
    'Proposed exercise resulting from public disagreement and correction. The source supplies a 10/15/15-minute plan but no outcome data. It explicitly separates a transcript full of reasoning from the learner doing that reasoning.',
    '[[think-first]] is a related proposal. [[bjork-desirable-difficulties-2011]] cautions that difficulties become undesirable when the learner lacks prerequisites. Neither validates this classroom exercise.',
    'Durable judgment, learning transfer or improved calibration. A reason for changing one’s mind is useful process evidence, not a validated learning score.',
    'Provide scaffolding and a way to stop when the challenge becomes fatigue. Check invented evidence. Divergence between outputs does not isolate model bias or personalization without controlling context and sampling. The initial position need not be written or publicly disclosed if that creates a barrier.',
    '[Inference] Can the learner reconstruct the opposing argument and identify the evidence that matters without reading AI’s text?', ['think-first','bjork-desirable-difficulties-2011'])
card(880,'check-a-capability-without-the-assistant','Check a capability without the assistant',
    'You need to retain a specific capability even when the usual AI tool is unavailable. The goal is a bounded skill, not proving general independence from support.',
    ['Name the capability and choose a safe representative task with observable criteria.',
     'Record what you can do without the AI assistant now. Keep ordinary accommodations and the reference materials appropriate to the skill.',
     'Plan opportunities to perform that skill yourself while using AI elsewhere as useful.',
     'Repeat a comparable task later and compare correctness, reasoning and needed help. [Inference] Record task differences and ask a qualified reviewer when you cannot assess it yourself.'],
    'John Nosta, The Borrowed Mind (2026), printed Chapter 7 “Reclaiming Agency,” “Protect the Baseline”; EPUB [ch.25 — xhtml/xhtml-0-24.xhtml], source.md L113. The book proposes unaided practice and regular measurement; criteria, comparable-task cautions and recording details are editorial additions.',
    'A practice proposal in a philosophical synthesis. Nosta relies on secondary interpretations of clinical and writing studies; the local audit does not independently establish the clinical mechanism or this remedy’s effectiveness.',
    '[[strategic-alternation]] already records that no optimal schedule is established. [[nosta-ai-rebound-2025]] preserves the same clinical-verification gap. [[shen-skill-formation-2026]] concerns a learning shortfall in a specific task, not universal loss of previously acquired skill.',
    'Whether a chosen practice schedule maintains skill. A change in one task can reflect difficulty, fatigue or familiarity rather than lasting capability change.',
    'Never withdraw needed clinical, operational or access safeguards from live work to run a test. Use simulation or low-stakes practice. Do not impose a fixed solo ratio or treat ongoing assistance as personal failure.',
    '[Inference] What can you now explain or perform under the agreed conditions, and what help remains necessary?', ['strategic-alternation','nosta-ai-rebound-2025','shen-skill-formation-2026'])
card(459,'request-criticism-without-rewriting','Request criticism without rewriting',
    'You have your own draft and want a reader’s objections while retaining the writing and editorial decisions.',
    ['Choose a shareable excerpt and state the effect, audience or claim you want it to achieve.',
     'Ask for a small set of specific areas to examine, with locations and reasons, while explicitly forbidding replacement prose. Hogue uses five areas and at most 200 words as a starting example.',
     'For each comment, decide whether it identifies a real problem or would erase an intended choice. Check factual objections against sources.',
     'Revise yourself, or keep the passage and state why. Godin’s variant asks what is missing or what claims the text does not sustain.'],
    'Rebecca J Hogue with Sam Illingworth, “How Can Writers Use AI Ethically?”, 6 December 2025, L32–42 and L62–80. Seth Godin, Lenny’s Podcast, 8 December 2024, 19:20, adds omissions/unsupported-claims checks. Illingworth’s poem editing and Joshua Sherman’s songwriting appear in “How Creatives Are Actually Using AI,” 17 March 2026, L61–84 and L194–208. Editorial label; intention/location wording added for clarity.',
    'Named first-person demonstrations. Hogue reports more useful feedback with a limit and rejects advice that conflicts with her style. Illingworth describes accepting two comments and keeping another image. No independent quality or learning assessment.',
    'Complements [[think-first]]. No study reviewed establishes that this specific critique routine improves independent writing skill.',
    'Future writing quality, retained voice and independent skill. Feeling more in control is separate from evidence of better writing.',
    'Models can invent flaws, miss facts and favor conventional style. Their taste is not final authority. Use suitable data permissions; avoiding model training alone does not resolve confidentiality or authorship rules. A personal-memory response can test fit to intended meaning, not factual memory accuracy.',
    '[Inference] Which criticism did you reject, and what purpose did your own revision serve?', ['think-first','cognitive-offloading'], [460,801,480,449,516])
card(460,'turn-creative-disagreement-into-your-own-checklist','Turn creative disagreement into your own checklist',
    'Repeated feedback conversations reveal recurring choices in your writing, music or other craft, and you want something you can use without reopening AI.',
    ['Bring work you have already begun and ask for a critical reading of a specific choice.',
     'Argue with or decline comments that do not fit the work. Try revisions yourself and judge them in the medium: sing a lyric, read a line aloud, or inspect the composition.',
     'After several decisions, name the principles you actually used. AI may help summarize the discussion; you select and rewrite the rules.',
     'Apply the short checklist to another piece without AI. Change a rule when it fails the new work. The explicit revision of rules is an editorial safeguard.'],
    'Joshua Sherman (First Radio On), in Sam Illingworth and co-editor Alyssa Fu Ward’s “How Creatives Are Actually Using AI,” 17 March 2026, L194–208, especially L206. Editorial label and operational elaboration of his described practice.',
    'Sherman narrates two songwriting exchanges, rejects some feedback and describes a personal checklist that he applies without AI. He reports the decisions; no independent quality or transfer test is provided.',
    'Related to [[think-first]] in preserving human material and choice. No direct empirical evaluation of the checklist routine reviewed.',
    'Whether the checklist supports better work or lasting craft development. Applying a rule does not by itself show expertise.',
    'Keep rules provisional and personal. A model-generated summary can misstate why you chose something. Avoid turning one song’s successful choice into a formula that flattens later work. Hearing is not required; use the evaluative mode available for the craft.',
    '[Inference] Can you use, explain and sometimes reject a checklist item without consulting the conversation?', ['think-first'], [459])
card(514,'ask-about-the-gap-then-do-the-task','Ask about the gap, then do the task',
    'You are learning a task that you would otherwise hand to AI, and want the attempt itself to remain yours.',
    ['Name a small task and list what you do not understand. Illingworth proposes three questions; fewer or more may fit.',
     'Ask for explanations of those gaps rather than a finished task. Check important explanations using the course material, documentation or a knowledgeable person.',
     'Close the AI response and perform the task yourself, with the ordinary supports appropriate to the learning goal.',
     'Check the actual attempt. If stuck, identify the next gap and get suitable help. The external check and iterative return to help are editorial additions.'],
    'Sam Illingworth, “There Are Three Ways to Learn With AI. Most People Use None of Them.”, 25 March 2026, Conceptual Inquiry exercise L113–121. Editorial title.',
    'Author-proposed exercise inspired by an observed behavior cluster. No outcomes are reported for the exercise itself.',
    '[[shen-skill-formation-2026]]: AI access was randomized; the six behavior clusters were not. Higher scores in active-inquiry clusters suggest a hypothesis, not proof that this procedure preserves learning. [[bjork-desirable-difficulties-2011]] distinguishes useful learning difficulty from difficulty beyond the learner’s prerequisites.',
    'Transfer beyond the task, delayed retention and the benefit of any particular number of questions. The source’s claim that some users learned nothing is not supported by the local research account.',
    'Do not infer skill loss from needing help, or confuse independent task completion with moral worth. A generated explanation can be wrong. Some tasks appropriately remain assisted; choose which part you actually need to learn.',
    '[Inference] Compare what you predicted you could do with the actual attempt, keeping confidence and performance separate.', ['shen-skill-formation-2026','six-pattern-diagnostic','bjork-desirable-difficulties-2011'])
card(422,'diagnose-your-draft-before-feedback','Diagnose your draft before feedback',
    'You have a draft or worked solution and want feedback without handing the entire evaluation to the model.',
    ['Before requesting critique, identify two weak parts and explain why using the task’s criteria. If you cannot yet do this, ask a teacher for criteria or an example.',
     'State what you were trying to do, then ask AI to critique and point out where it disagrees with your diagnosis.',
     'Compare each disagreement with the work and its evidence. Do not assume that disagreement is more truthful than agreement.',
     'Close the response and reconstruct the reasoning, including the hardest step, in your own words, speech or drawing. [Inference] Check this reconstruction and seek help for gaps.'],
    'Sam Illingworth, “You Did Not Learn That With AI,” 5 August 2026, protocol L115–145. This card extracts moves one and three; it does not reproduce or claim validation of the complete four-move protocol.',
    'A proposed practice accompanied by secondary study accounts. The exact combination here has no reported evaluation. New studies linked by the article were not independently assessed in this allocation.',
    '[[bjork-desirable-difficulties-2011]] provides a related retrieval/generation rationale, not validation of the AI procedure. [[fernandes-metacognition-2025]] distinguishes assisted reasoning performance from self-assessment and proposes explain-back interventions without testing them.',
    'Whether self-diagnosis improves later feedback use or durable capability in this context. Reproduction is a limited observation, not a complete definition of understanding.',
    'Novices may need explicit scaffolding; a critique can be plausible and wrong. Keep source material for checking after the attempt. Do not enforce a blanket preference for broad questions when a procedural explanation is what is needed.',
    '[Inference] What changed between your diagnosis and the reconstruction, and can you point to why?', ['think-first','bjork-desirable-difficulties-2011','fernandes-metacognition-2025'])
card(698,'explain-it-back-before-the-correction','Explain it back before the correction',
    'An AI explanation feels clear, but you want to see what you can actually explain yourself.',
    ['Read or hear the explanation and then put it aside.',
     'Explain the concept back in your own terms, example or analogy. Include where you are uncertain.',
     'Ask AI to identify specific mismatches or missing steps rather than simply rate the explanation.',
     'Check important corrections against the original material or a knowledgeable person. [Inference] Try a changed example later without the assistant to examine transfer rather than immediate repetition.'],
    'Julie Zhuo, Lenny’s Podcast, 21 September 2025, 00:25:55–00:26:40, within discussion starting 00:22:04. Putting the response aside, external checking and later changed example are editorial additions. Illingworth (25 March 2026), L133–139, supplies a related generated-work comprehension variant.',
    'First-person account of interactive study. Zhuo reports finding retelling useful and observes that politely worded feedback may mean the explanation was wrong. No independent learning measure.',
    '[[fernandes-metacognition-2025]] proposes explain-back tasks but does not evaluate them. [[bjork-desirable-difficulties-2011]] supports examining retention and transfer separately from immediate fluent performance.',
    'Improved understanding or calibration from this interaction. Agreement from the same model is not an independent test.',
    'AI can affirm a misconception or invent a correction. Generated rationales are not faithful records of a model’s internal reasoning. Use an accessible response form and keep human teaching available.',
    '[Inference] Can you explain the concept on a different example, and which parts still require help?', ['fernandes-metacognition-2025','bjork-desirable-difficulties-2011'], [514])
card(658,'rehearse-a-bounded-reasoning-case','Rehearse a bounded reasoning case',
    'You want practice following an argument in a familiar work setting before facing a real decision.',
    ['Choose the reasoning skill and a fictional, low-stakes scenario with explicit facts.',
     'Ask AI for a short LSAT-style question framed in that setting. Have a knowledgeable person check the scenario and answer key when using it for instruction. This checking step is editorial.',
     'Choose an answer and state your reasoning before revealing the feedback.',
     'Compare the explanation to the stated facts. Challenge ambiguous assumptions or a questionable key; use another checked case if needed.'],
    'Hilary Gridley, Lenny’s Podcast, 15 June 2025, Aristotle GPT discussion at 01:26:46–01:29:49 (L849–871). Editorial label and checking/reason-giving requirements extend the described multiple-choice loop.',
    'Practitioner-built tool and narrated example. Gridley describes repeated personalized practice and recognizes missing engineering context. No measured learning or workplace transfer.',
    '[[fernandes-metacognition-2025]] shows why assisted reasoning and self-assessment should be distinguished. It does not test Gridley’s tool. [[bjork-desirable-difficulties-2011]] supports appropriate challenge with prerequisites.',
    'Improved general reasoning, product judgment or engineering estimates. More questions answered and higher confidence are not sufficient evidence.',
    'Many real product decisions involve values and uncertain evidence, not one deductively correct option. Avoid learning a false key or treating made-up business facts as real. Learners can answer by speech or text; no need to match LSAT speed.',
    '[Inference] Can you identify the decisive premise and what change would alter your answer?', ['fernandes-metacognition-2025','bjork-desirable-difficulties-2011'])
card(77,'teach-a-simulated-learner','Teach a simulated learner',
    'You know a framework and want to practise applying it through explanation, rather than ask AI to explain it again.',
    ['Choose the framework and an instructor-checked fictional situation where a character needs help.',
     'Ask AI to play that character, who does not yet know the framework. Tell it to let you guide the character instead of supplying the whole lesson.',
     'Explain and apply the framework yourself through the character’s situation. Notice where you need evidence or instruction.',
     'Debrief against the actual framework and ask a teacher or reliable source to check uncertain applications. The explicit checking step is an editorial addition.'],
    'Ethan Mollick, “Innovation through prompting,” 22 April 2024, L18–40, especially the goal-play description at L28. This is a labeled adaptation of the described student-teaches-character structure, not a reproduction of the full linked prompt.',
    'The author describes a fictional Hamlet goal-setting demonstration and pilot use of related activities. He calls for further effectiveness studies; no results for this adapted routine are reported.',
    'No direct evaluation reviewed. [[cognitive-offloading]] helps distinguish the AI’s simulation work from the learner’s explanation. [[bjork-desirable-difficulties-2011]] offers an adjacent generation rationale.',
    'Transfer to teaching a real person, durable framework knowledge and whether the role-play is better than another exercise.',
    'The simulation can oversimplify literature, people and domains. A cooperative character may make weak teaching look successful. Use a safe scenario, clear learning goal and external debrief; do not treat fictional reactions as user research.',
    '[Inference] What did you have to work out yourself, and could you apply it to a different case?', ['cognitive-offloading','bjork-desirable-difficulties-2011'])
card(427,'ask-for-an-explanation-in-a-specific-case','Ask for an explanation in a specific case',
    'An educator wants to see whether learners can apply a concept, beyond recalling a polished description.',
    ['Choose a topic you can evaluate. Ask AI for a short case that requires explaining why a central idea works or fails.',
     'Inspect and revise the question yourself. Check its facts, ambiguity and whether a correct answer really needs the intended reasoning.',
     'Have learners explain one mechanism using a relevant example. Allow a provided or fictional case instead of personal disclosure.',
     'Ask follow-up questions about the assumptions and where the example fits or departs from the concept. Assess the reasoning using explicit criteria, not the prose’s polish.'],
    'Mahelet G Fikru with Sam Illingworth, “How to Test for Real Understanding When AI Makes Every Answer Sound Right,” 12 February 2026, L30–98. Fikru’s supply-and-demand example and personal-case follow-up are the basis. Shared-case alternative and explicit assessment criteria are editorial safeguards.',
    'Demonstration of question generation and revision, plus reported use of personal purchase examples in flipped classrooms. No measured learning effect or AI-resistance test.',
    '[[bjork-desirable-difficulties-2011]] qualifies the claim that difficulty necessarily helps. [[fernandes-metacognition-2025]] supports separating perceived comprehension from task performance, not the efficacy of this particular assessment.',
    'Durable understanding, transfer and whether this reveals more than another assessment form.',
    'The question is not AI-proof: a model can answer it or invent personal experiences. Use suitable assessment conditions and follow-up rather than accusations. Do not make private life disclosure a condition of showing knowledge; adapt length and response mode for access.',
    '[Inference] Can the learner explain what assumption would need to change for their conclusion to fail?', ['bjork-desirable-difficulties-2011','fernandes-metacognition-2025'])

review(729,'merge','support',['00:49:44–00:52:07, L272–288'],
    'Marty Cagan describes reversing his own AI-first product-management advice after observing people overtrust early outputs.',
    ['Reports people optimizing an AI-suggested wrong direction; recommends a human starting point then challenge or improvement. No comparative intervention results.'],
    ['Keep an initial product judgment available for comparison.'],
    ['Informal observations, not a causal trial or a measured rate of overtrust. Product-strategy comments elsewhere in the interview are outside this draft.'],
    ['think-first'], 'Merge into the independent-starting-point card, adding a practitioner reversal account rather than treating it as experimental confirmation.',
    'The first human answer can also be wrong; judge revisions using evidence rather than personal ownership alone.')

assert set(reviews) == set(items), (set(items)-set(reviews),set(reviews)-set(items))
for i,r in reviews.items():
    s=items[i]
    if i in (879,880):
        r['coverage'] = ('Read the complete introduction and conclusion plus contents; not the whole book.' if i==879 else 'Read the complete printed Chapter 7 (Reclaiming Agency), its heading/contents and existing KB entry; not the whole book.')
    elif s['collection']=="Lenny's Podcast":
        r['coverage']='Read metadata/intro and complete relevant exchanges with surrounding discussion at the locators below; not the full episode.'
    else:
        r['coverage']='Read the complete available article text in source.md, including examples, limitations and surrounding commentary. Linked pages and embedded images/video were not independently read.'
    r['practice_files']=[f"{items[c['id']]['workbench']}/drafts/practices/{stem}.md" for stem,c in cards.items() if c['id']==i or i in c['supports']]
    r['source_path']=s['source_path']
    r['reviewed_at']='2026-09-26'
    r['integration_decision']='pending'
    r['draft_only']=True

def bullets(xs): return '\n'.join('- '+x for x in xs) if xs else '- None.'
def links(xs): return '\n'.join('- [['+x+']]' for x in xs)
def citation(s):
    author={459:'Rebecca J Hogue and Sam Illingworth',460:'Sam Illingworth and named contributors; co-editor Alyssa Fu Ward',414:'Sam Illingworth and Tina Austin',416:'Ilia Karelin and Sam Illingworth',523:'Timo Mason and Sam Illingworth',427:'Mahelet G Fikru and Sam Illingworth',879:'Sam Illingworth',880:'John Nosta'}.get(s['id'],s['collection'])
    author={589:'Chip Huyen, interviewed by Lenny Rachitsky',616:'Edwin Chen, interviewed by Lenny Rachitsky',668:'Jake Knapp and John Zeratsky, interviewed by Lenny Rachitsky',735:'Matt Mochary, interviewed by Lenny Rachitsky',739:'Mayur Kamat, interviewed by Lenny Rachitsky',729:'Marty Cagan, interviewed by Lenny Rachitsky',801:'Seth Godin, interviewed by Lenny Rachitsky',698:'Julie Zhuo, interviewed by Lenny Rachitsky',658:'Hilary Gridley, interviewed by Lenny Rachitsky'}.get(s['id'],author)
    when='publication date unverified' if s['id']==52 else s.get('date','date unverified')
    return f"{author}. {s['title']}. {when}. {s.get('url','Local purchased EPUB.')}"

for stem,c in cards.items():
    s=items[c['id']]
    p=ROOT/s['workbench']/'drafts/practices'/f'{stem}.md'
    p.parent.mkdir(parents=True,exist_ok=True)
    fm='---\nstatus: emerging\narea: [preservation]\nsources:\n  - '+json.dumps(citation(s),ensure_ascii=False)+'\ndraft_only: true\nintegration_decision: pending\n---\n'
    body=f"\n# {c['title']}\n\n## Use When\n\n{c['use']}\n\n## Try It\n\n"+'\n'.join(f'{n}. {step}' for n,step in enumerate(c['steps'],1))
    body+=f"\n\n## Origin\n\n{c['origin']}\n\nLocal original: [source.md](../../source.md).\n\n## Evidence and Rationale\n\n**Basis / observed or reported:** {c['evidence']}\n\n**Related research:** {c['research']}\n\n**Untested:** {c['untested']}\n\n## Limits\n\n{c['limits']}\n\n## What to Notice\n\n{c['notice']}\n\n## Related\n\n{links(c['related'])}\n"
    p.write_text(fm+body,encoding='utf-8')

for i,r in reviews.items():
    s=items[i]; wb=ROOT/s['workbench']; book=i in (879,880)
    (wb/'practice-review.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    ar=wb/'practice-review' if book else wb
    ar.mkdir(exist_ok=True)
    files=bullets(r['practice_files'])
    scope='Draft-only close reading/extraction authorized by the user’s Continue. No canonical publication. Integration decision pending.'
    tri=f"# Practice triage: {s['title']}\n\n## Source and coverage\n\n{citation(s)}\n\n{r['coverage']}\n\n{bullets(r['locators'])}\n\n## Summary and quality\n\n{r['basis']}\n\n{r['review_note']}\n\nRelevance: HIGH for the bounded practice question; quality is source-specific practitioner evidence, not an effectiveness rating. Identity/credentials are as presented in the source, not independently verified.\n\n## Existing coverage\n\n{links(r['related_entries'])}\n\nCompared with the local entries above before drafting; related mechanisms are not evidence that this exact routine works.\n\n## Recommendation and Decision\n\n- Outcome: {r['decision'].upper()} for draft development.\n- Date: 2026-09-26\n- Reason: {r['review_note']}\n- Scope: {scope}\n"
    (ar/'triage.md').write_text(tri,encoding='utf-8')
    dist=f"# Practice distillation: {s['title']}\n\n## Account basis\n\n{r['basis']}\n\n## Reported outcomes\n\n{bullets(r['reported_outcomes'])}\n\n## Proposed outcomes, not findings\n\n{bullets(r['proposed_outcomes'])}\n\n## Extraction ledger\n\n- Role: {r['role']}\n- Concepts/methods: no new canonical entries proposed in this pass.\n- Practice files (may originate in another source workbench):\n{files}\n\n## Limits\n\n{bullets(r['limits'])}\n\n## Decision\n\n- Outcome: PROCEED_TO_CRITIQUE, draft only; no integration approval.\n- Date: 2026-09-26\n- Reason: All assigned sources received close reading and a consolidation decision, including deferred and counterexample sources.\n"
    (ar/'distill.md').write_text(dist,encoding='utf-8')
    crit=f"# Practice critique: {s['title']}\n\n## Overall: FLAGS\n\nPublication remains pending. The bounded draft incorporates the qualifications below; FLAGS does not mean a new user permission gate for preparing the drafts.\n\n## Evidence lens — revised scope retained\n\n{' '.join(r['limits'])}\n\n## Practitioner lens — usable with stated bounds\n\n{r['practitioner']}\n\n## Adversarial lens — retained objections\n\n{r['review_note']} A procedure can be actionable and still fail to improve the intended outcome. The source’s credibility must be judged at the claim level; transparent self-report is not independent evaluation.\n\n## AI failure checklist\n\n- Citations: local sources/related entries inspected; external links are provenance, not verification.\n- Methods: stated reading coverage and author/contributor credit retained.\n- Statistics: no quantitative effect of the practice asserted; source numerical caveats recorded above.\n- Constructs: assisted output, unaided capability, confidence and calibration remain distinct.\n- Status: emerging drafts only.\n- Links: checked by the allocation renderer against existing KB stems.\n- Novelty: overlapping routines consolidated; legacy methods are related entries, not silently relocated.\n\n## Decision\n\n- Outcome: DRAFT_ONLY_REVIEW_COMPLETE\n- Date: 2026-09-26\n- Integration: pending\n- Reason: {scope}\n"
    (ar/'critique.md').write_text(crit,encoding='utf-8')
    source=f"---\nstatus: emerging\narea: [preservation]\ntype: {'book' if book else ('talk' if s['collection']==chr(76)+'enny\'s Podcast' else 'article')}\nsources:\n  - {json.dumps(citation(s),ensure_ascii=False)}\ndraft_only: true\n---\n\n# {s['title']}\n\n## Citation\n\n{citation(s)}\n\n## Type and account basis\n\n{r['basis']}\n\n## Key Insight\n\n{r['review_note']}\n\n## Key Findings\n\nThese are source-account summaries, not independently validated effects.\n\n{bullets(r['reported_outcomes'])}\n\n## Locators and coverage\n\n{r['coverage']}\n\n{bullets(r['locators'])}\n\n## Relevance\n\n{bullets(r['proposed_outcomes'])}\n\n## Supports / overlaps\n\n{links(r['related_entries'])}\n\n## Contradicts / Extends\n\n{r['review_note']}\n\n## Open Questions and limits\n\n{bullets(r['limits'])}\n\n## Practice drafts\n\n{files}\n\nIntegration pending; source distillation is limited to the inspected practice contribution.\n"
    dest=wb/'drafts'/'updates'/'nosta-borrowed-mind-2026-practices.md' if i==880 else wb/'drafts'/'source.md'
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(source,encoding='utf-8')
    if not book:
        meta=json.loads((wb/'source.json').read_text(encoding='utf-8-sig'))
        meta.update(status='critiqued',draft_only=True,integration_decision='pending')
        decision=dict(stage='practice-close-reading',outcome=r['decision'],at='2026-09-26',scope='draft-only; integration pending')
        if decision not in meta.setdefault('decisions',[]):
            meta['decisions'].append(decision)
        (wb/'source.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (wb/'log.md').open('a',encoding='utf-8') as f:
        f.write(f"\n## 2026-09-26 — Practice close reading\n\n{r['coverage']} Decision: {r['decision']}; role: {r['role']}. Artifacts: {'practice-review/' if book else ''}triage.md, distill.md, critique.md; practice-review.json. Draft-only extraction and critique complete; integration pending. {'Existing source.json status and prior artifacts preserved.' if book else ''}\n")

stems={p.stem for d in ['sources','concepts','methods'] for p in (ROOT/d).glob('*.md')}
missing=sorted({x for r in reviews.values() for x in r['related_entries'] if x not in stems}|{x for c in cards.values() for x in c['related'] if x not in stems})
assert not missing, missing
(BASE/'librarian-learning-results.json').write_text(json.dumps({'source_count':len(reviews),'practice_count':len(cards),'reviews':list(reviews.values()),'cards':[{**c,'stem':stem,'path':f"{items[c['id']]['workbench']}/drafts/practices/{stem}.md"} for stem,c in cards.items()]},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'reviewed':len(reviews),'practice_cards':len(cards),'missing_related':missing}))
