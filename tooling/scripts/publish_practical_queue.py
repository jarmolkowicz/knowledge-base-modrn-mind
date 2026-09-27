# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Publish the manually assessed 400-item practice queue; no inferred judgments.

Keeps the first pass, checks exact queue coverage and source hashes, and builds
the complete reading pool plus a contribution-based navigation shortlist.
"""
import csv, hashlib, json, os, re
from collections import Counter
from pathlib import Path
from urllib.parse import quote, unquote

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'raw/practitioner-practices-development/screening'
DEST=OUT/'queue-review'

# Editorial navigation, not an outcome taxonomy. First list = starting sources;
# second list = other selected accounts, transfers and limits in this family.
GROUPS=[
 ('Choose what deserves AI assistance',[22,408,523],[64,464,263,416], 'Start with purpose, stakes and an explicit human responsibility.'),
 ('Protect attention and know when to stop',[521,589,616],[52,668,735,739], 'Adds offline thinking and opportunity-cost failure cases, not just faster output.'),
 ('Form your own answer first',[729,414],[66,879,880], 'Combines a practitioner who reversed AI-first advice with an explicit human reasoning baseline.'),
 ('Get criticism while retaining authorship',[459,801,460],[449,516,480], 'Named writers describe actual boundaries; comparisons with personal meaning expose limits of AI interpretation.'),
 ('Explain, practise and try without assistance',[514,698,658],[262,422,427,77], 'The learner must answer or explain; model feedback is not itself a learning measure.'),
 ('Check claims against records',[456,437,580],[453,328,46], 'Pairs traceable checking routines with documented prompt-only checking failures.'),
 ('Test outputs and changing frames',[75,652],[508,423,289,517,479], 'Task-specific tests and expert error review are stronger than general trust in a model.'),
 ('Keep agent work inspectable and bounded',[356,72,375],[537,84,95,105,80,89], 'Includes stopping, permission and review costs, alongside failures of opaque delegation.'),
 ('Remain involved in coding and prototyping',[402,636],[38,339,350,275], 'Pairs active review with two-human collaboration and failure examples; working software is not proof of understanding.'),
 ('Supply context and preserve expert decisions',[276,360,394],[324,361,325,76], 'Connects clarification, evidence gathering and accountable decisions in real work.'),
 ('Turn inquiry into a decision',[439,515,710],[294,270,352,413,578,663,512,387], 'Questions serve a decision; predictions and later checks help distinguish confidence from accuracy.'),
 ('Generate possibilities and make your own creative choice',[684,524,488],[286,306,409,425,430,489,490,530,605,558,741], 'Different media and perspectives offer possibilities; personal meaning and selection stay with the person.'),
 ('Preserve inquiry in family and education settings',[750,412],[474,714], 'Adds child-led inquiry and participation in rules beyond professional knowledge work.'),
 ('Learn as a team without losing independent views',[79,550,811],[277,255,542,804], 'Connects local experiments, independent contributions and return to actual user evidence.'),
 ('Look for missing and contrary evidence',[802,760],[435,491,591], 'Adds disconfirmation, survey-question quality and direct contact with people affected.'),
 ('Make responsibility and provenance visible',[421,529,819],[436,440,482], 'Covers disclosure, process records, system objectives and who can use collected information.'),
 ('Recognize false authority and misleading feedback',[363,602,486],[441,452,478,487,399,299,316], 'These are counterexamples, not recommended prompts: personal guesses and flattering feedback are not evidence.'),
 ('Keep human advisers and practise human reasoning',[533,705,803],[585,731,821,673], 'Explicit transfer sources: actual relationships, arguing a case yourself and low-stakes rehearsal.'),
 ('Protect the thinking involved in making an artifact',[568,725,737],[601,660,677,755,702], 'Explicit transfer sources: writing, first-hand experience and evaluation before automating production.'),
]

def save(path,data):
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def link(path,label,base=OUT):
    return f'[{label}]({quote(os.path.relpath(ROOT/path,base).replace(chr(92),"/"),safe="/.:#")})'

def main():
    register=json.loads((OUT/'screening-register.json').read_text(encoding='utf-8'))
    records=register['records']; assert len(records)==881
    original=json.loads((OUT/'shortlist.json').read_text(encoding='utf-8'))
    queue=json.loads((DEST/'queue.json').read_text())
    rows=list(csv.DictReader((DEST/'decisions.tsv').read_text(encoding='utf-8-sig').splitlines(),delimiter='\t'))
    assert len(rows)==400 and len({int(r['id']) for r in rows})==400
    assert {int(r['id']) for r in rows}==set(queue)
    for r in records:
        assert hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256'],r['path']
    selected={r['id'] for r in original}|{int(r['id']) for r in rows if r['decision'].startswith('select')}
    grouped=[i for _,first,others,_ in GROUPS for i in first+others]
    assert len(grouped)==len(set(grouped)), 'Repeated group ID'
    assert set(grouped)==selected, f'Group mismatch: missing {selected-set(grouped)}, extra {set(grouped)-selected}'
    firstpass=OUT/'first-pass-register.json'
    if not firstpass.exists(): save(firstpass,register)
    reviewed=[]
    for row in rows:
        i=int(row['id']); r=records[i]
        packet=json.loads((DEST/f'{i:03}.json').read_text(encoding='utf-8'))
        assert packet['id']==i and packet['sha256']==r['sha256'] and packet['passages']
        item={**row,'id':i,'path':r['path'],'title':r['title'],'collection':r['collection'],'url':r.get('url',''),'sha256':r['sha256'],'coverage':packet['coverage'],'packet':f'queue-review/{i:03}.json'}
        reviewed.append(item)
        r.setdefault('first_pass_review_decision',r['review_decision'])
        r.setdefault('first_pass_reason',r.get('review_reason',r.get('reason','')))
        r.setdefault('first_pass_screening_coverage',r.get('screening_coverage',''))
        r['review_decision']=row['decision'];r['review_reason']=row['reason'];r['queue_review']=item
        r['assessment']='queue_screening_2026-09-26'
        r['screening_coverage']=packet['coverage']
    counts=Counter(r['decision'] for r in reviewed)
    register['queue_reviewed_at']='2026-09-26'
    register['queue_review_method']='400/400 prior priority and transfer leads assessed from expanded selected original passages; not complete reading or verification. Original 15 preserved. No ingestion or integration decisions.'
    register['current_review_counts']=dict(Counter(r['review_decision'] for r in records))
    register.setdefault('first_pass_screening_counts',register.get('screening_counts',{}))
    register.setdefault('first_pass_shortlist_ids',register.get('shortlist_ids',[]))
    register['screening_counts']=register['current_review_counts']
    register['shortlist_ids']=sorted(selected)
    register['method']='Complete inventory first pass plus expanded passage screening of all 400 priority/transfer leads. Selected sources require close reading and critique; no integration approval.'
    register['queue_review_counts']=dict(counts)
    save(DEST/'results.json',{'date':'2026-09-26','scope':'fixed 400-item queue','counts':dict(counts),'records':reviewed})
    save(OUT/'screening-register.json',register)
    pool={r['id']:{**r,'origin':'initial shortlist'} for r in original}
    for r in reviewed:
        if r['decision'].startswith('select'): pool[r['id']]={**r,'origin':'queue review','focus':r['contribution']}
    for name,first,others,why in GROUPS:
        for i in first+others:
            pool[i]['group']=name;pool[i]['starting_source']=i in first
    save(OUT/'consolidated-shortlist.json',{'date':'2026-09-26','status':'screening recommendations, not approved practices','groups':[dict(name=n,starting_ids=f,additional_ids=o,rationale=w) for n,f,o,w in GROUPS],'records':list(pool.values())})
    lines=['# Consolidated practice-source shortlist','','2026-09-26. **All 400 queued leads now have a screening decision.** The original 15 are part of this larger set, not the boundary of it.','',f'**{len(pool)} sources retained for close reading:** 91 direct or flagged leads, 28 human-practice transfer sources, 20 counterexamples. Another 91 queue items are useful variants, recorded separately to avoid treating repetition as independent support.','','These are candidate sources, not 139 proven practices. Relevant sections were inspected; most long sources were not read in full. Benefits and credentials have not been systematically verified. A named account, an observable procedure and honest limits carry more weight here than prominence.','','## Where to start','','The groups below organize contributions, **not intended outcomes**. They remain provisional. Start with the named accounts, then inspect the additional sources when extracting that same practice. This prioritizes distinct contributions after screening the whole queue; it does not impose a source-count cap.','','[Every selected account, with reasons and limits](selected-source-notes.md) · [All 400 decisions](queue-review-results.md) · [Complete 881-item register](screening-register.md)','','| Contribution | Starting sources | Other selected accounts / limits | Why retain this group |','|---|---|---|---|']
    def refs(ids,brief=False):
        return (' · ' if brief else '<br>').join(f'[ID{i}' + ('' if brief else f': {pool[i]["focus"].replace("|","—")}') + f'](selected-source-notes.md#source-{i})' for i in ids)
    for n,f,o,w in GROUPS: lines.append(f'| {n} | {refs(f)} | {refs(o,True)} | {w} |')
    lines+=['','## Trust and evidence boundaries','','- Newsletter guests retain credit for their own accounts. A host is not automatically the originator. Repeated posts, book chapters and podcast appearances are not independent confirmation.','- Practitioner and vendor accounts establish that a procedure was proposed or reportedly used. They do not establish lasting gains in unaided thinking.','- Transfer sources describe human practices. Their AI adaptations are **[Inference]** and must be labeled during extraction.','- Counterexamples supply failure modes. Do not publish their prompts as recommended practices.','- Attribution/access holds stay outside this pool until resolved. A deferred item is not a whole-source rejection.','','## Next step','','Closely read and extract these contribution groups through the per-source workflow. Consolidate overlapping practices; keep source wording, practitioner actions, reported outcomes, research support and our adaptations separate. Critique claims before approval. Record outcomes from the sources before proposing an outcome taxonomy. Implement the separate practices collection in the workflow before canonical integration.','','The remaining access and provenance holds need targeted repair when they could add missing perspectives; do not describe this as exhaustive field coverage.']
    lines=[s.replace('Another 91 queue items',f'Another {counts["variant"]+counts["variant_with_flags"]} queue items') for s in lines]
    (OUT/'consolidated-shortlist.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    notes=['# Selected source notes','','Companion to the [consolidated shortlist](consolidated-shortlist.md). Every ID links to retained raw material; the locators and caveats delimit what was inspected.','']
    for name,first,others,why in GROUPS:
        notes += [f'## {name}','']
        for i in first+others:
            r=pool[i]
            notes += [f'<a id="source-{i}"></a>',f'### ID{i} — {r["title"]}','',f'**{r["decision"]}** · {"Starting source" if i in first else "Additional selected source"} · {link(r["path"],"Raw source")}', '',f'**Contribution:** {r.get("focus",r.get("contribution"))}', '']
            if r['origin']=='initial shortlist':
                notes += [f'**Attribution:** {r["author"]}',f'**Account:** {r["contribution"]}',f'**Basis:** {r["basis"]}',f'**Limits:** {r["limits"]}',f'**Locator:** {r["locator"]}']
            else: notes += [f'**Assessment, basis and limits:** {r["reason"]}',f'**Reading packet:** [ID{i}]({r["packet"]})']
            notes += [f'**Coverage:** {r["coverage"]}','']
    (OUT/'selected-source-notes.md').write_text('\n'.join(notes)+'\n',encoding='utf-8')
    report=['# Remaining practice queue — completed screening','','2026-09-26. **400/400 unresolved leads assessed; 0 left without a second-pass disposition.** This completes screening of the queue, not full-source review, access repair or practice validation.','','[Consolidated shortlist](consolidated-shortlist.md) · [Selected source notes](selected-source-notes.md)','','## Decisions','','| Route | Count |','|---|---:|']
    report += [f'| {k} | {v} |' for k,v in sorted(counts.items())]
    report += ['','`select`: specific contribution worth close reading. `select_with_flags`: same, with material limits. `select_transfer`: human practice; AI adaptation inferred. `select_counterexample`: failure case. `variant`: useful overlap, not another independent practice. `defer_*`: outside immediate scope or needing verification, not rejected. `background` and `discovery`: context or source leads. Holds: missing content or unresolved identity.','','## Coverage and limits','','The fixed queue contained 239 priority and 161 transfer leads. Expanded original paragraphs, headers and speaker context were inspected; short articles sometimes received full available-text reading. Automated cue ranking located passages; each disposition and reason was written separately. Packets record exactly what was displayed. Additional targeted reads addressed missing central procedures.','','Long transcript passages were selected, not exhaustively read. Ranking can overselect AI mentions, host questions or advertisements and miss other useful sections. Sponsor passages were excluded from judgments when recognized. Deferral means insufficient incremental value in inspected material, not proof that the source contains nothing useful. No representative miss rate or corpus-wide outcome taxonomy can be inferred.','','No new downloads in this pass. The earlier refresh and saved hashes define the snapshot. Practitioner credentials and cited research were not comprehensively rechecked. Marketing language, personal anecdotes and untested exercises remain labeled by their account-level limits.','','Three new access holds and five new provenance holds were found. The current full inventory therefore has 201 access holds and 28 provenance holds; some identity flags remain suspicions. Twelve previously identified duplicate bodies remain retained. The full inventory is still 881 records, not 881 independent sources.','','## Collections covered','','| Collection | Queue items |','|---|---:|']
    report += [f'| {k} | {v} |' for k,v in sorted(Counter(r['collection'] for r in reviewed).items())]
    report += ['', 'A targeted final recheck expanded IDs714, 758 and 775. ID775 moved from background to a useful variant after finding an explicit warning against replacing firsthand user contact with AI summaries. This purposive check cannot estimate missed practices elsewhere.', '']
    report += ['','## All decisions','','Use IDs to locate the raw source, saved passage packet and exact reason.','']
    for r in reviewed:
        i=r['id'];report += [f'### ID{i} — {r["title"]}','',f'**{r["decision"]}: {r["contribution"]}**',r['reason'],f'{link(r["path"],"Raw source")} · [Inspected passages]({r["packet"]})',f'Coverage: {r["coverage"]}','']
    (OUT/'queue-review-results.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
    full=['# Complete practice screening register','','2026-09-26. Current dispositions after the 400-item queue review. [Consolidated shortlist](consolidated-shortlist.md) · [Second-pass details](queue-review-results.md) · [First-pass snapshot](first-pass-register.json)','','| ID | Collection | Source | Current disposition |','|---:|---|---|---|']
    for r in records:
        full.append(f'| {r["screening_id"]} | {r["collection"]} | {link(r["path"],r["title"].replace("|","—"))} | {r["review_decision"]} |')
    (OUT/'screening-register.md').write_text('\n'.join(full)+'\n',encoding='utf-8')
    checked_links=0
    for name in ('consolidated-shortlist.md','selected-source-notes.md','queue-review-results.md','screening-register.md','screening-results.md'):
        content=(OUT/name).read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',content):
            if target.startswith(('https:','http:')):continue
            file,_,anchor=target.partition('#')
            path=(OUT/unquote(file)).resolve()
            assert path.exists(),(name,target)
            if anchor.startswith('source-'):
                assert f'id="{anchor}"' in path.read_text(encoding='utf-8'),(name,target)
            checked_links+=1
    print(json.dumps({'queue':len(reviewed),'selected_pool':len(pool),'groups':len(GROUPS),'starting_sources':sum(len(x[1]) for x in GROUPS),'queue_counts':dict(counts),'all_source_hashes_verified':len(records),'local_links_verified':checked_links}))

if __name__=='__main__':main()
