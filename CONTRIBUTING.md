# Contributing

This is a curated public KB on "human thinking with AI." Contributions welcome.

## Suggest via issue

The quickest way to contribute — no git knowledge needed. [Open an issue](https://github.com/jarmolkowicz/modrn-mind-knowledge-base/issues) to:

- Suggest a source or paper
- Flag an error or misinterpretation
- Propose a new concept or method

## Submit a PR

Collaborators with write access push a branch directly. External contributors fork the repo and PR upstream.

For entry structure, see `tooling/templates/`. The templates define the schema, the section layout, and what each entry type (concept, method, practice, source) is for.

Practices belong in a separate `practices/` collection. Draft them in the originating source’s `raw/<slug>/drafts/practices/`; use `tooling/templates/practice.md`. Give a recognizable situation, concrete steps, attribution and locators, reported outcomes, limits and a useful observation to make. A practitioner proposal or first-person account can justify a carefully bounded candidate; label it honestly rather than presenting it as evaluated effectiveness. Explicitly label adaptations and distinguish assisted output, unaided capability and confidence. Canonical entries require a recorded integration decision through the librarian pipeline.

## What's a good fit

- Research papers with clear implications for human thinking with AI
- Methods or frameworks from domain experts
- Practitioner observations grounded in evidence
- Corrections or clarifications to existing entries

## What's not a fit

- Opinion without evidence
- Content outside the "human thinking with AI" domain (e.g., general AI capabilities, AI safety alignment)
- Duplicates of existing concepts — check `index.md` first

## Going deeper

If you have write access and use Claude Code, ingestion is driven by a single slash command: `/ingest <path>` (HITL) or `/ingest <path> --auto`. The librarian agent at `.claude/agents/librarian.md` walks the source through five stages — catalog, triage, distill, self-critique, integrate — keeping the full audit trail in `raw/<slug>/`. See `CLAUDE.md` for the operating model.
