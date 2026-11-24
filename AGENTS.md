# AGENTS.md — Tender Watch

## Startup Marker
- Start your first reply in every new conversation with: `Tender Watch rules loaded.`

## Project
- **Tender Watch** is a planned application for monitoring French public procurement notices (*avis*) from BOAMP open data.
- Planned pipeline: daily collection of *avis* and *acheteur* data, storage, keyword + semantic search, LLM relevance scoring against a company profile, a morning alert, and Q&A with citations (hand-written RAG).
- Planned stack: Python 3.12, FastAPI, SQLAlchemy 2, Alembic, Pydantic, pytest, uv, ruff, strict mypy, PostgreSQL + pgvector, Angular.
- **Current stage:** Step 1 done (repo skeleton only; no application code or tooling configured yet).
- **Docs:** Architecture decisions will live in `docs/adr/` (created at the first ADR); personal study notes live in `docs/learning-notes.md`.

## Environment
- OS / shell: WSL2 Ubuntu 24.04, `bash` only. Never use PowerShell or `/mnt/c` paths.
- Repository path: `~/projects/tender-watch`.
- Python tooling (`uv`, `ruff`, `mypy` strict, `pytest`) is **PLANNED**, not set up yet.

## Workflow
- Read the relevant files first before proposing or changing anything.
- Present a **PLAN** and **WAIT for Ossama's "go"** before making edits.
- Stay strictly within the current step's scope.
- One branch per ticket + pull request (even solo); never commit directly to `main` (except Step 1's initial commit).
- Use **Conventional Commits** (`feat`, `fix`, `test`, `docs`, `ci`, `build`, `chore`, `refactor`); commit bodies must explain **WHY**.
- Put tests in the same commit as the feature they cover.
- Add no dependency without an immediate, concrete use.
- **Never push, never open a PR, and never merge a PR** — Ossama runs those commands himself.
- Use sub-agents only for genuinely independent tasks.

## Verification
- Verify versions, APIs, and field names against official sources and quote what you checked; never guess.
- Show **REAL command output only**; never present output from a command that did not complete.
- If a tool is missing (exit 127) or a check could not run, say so explicitly.

## Final Report
- Include every item the prompt requested.
- Include a **Deviations from spec** section (write `none` only after checking every requirement).
- End with real output of `git status` and `git diff --ignore-blank-lines --stat` showing no stray whitespace changes. Then **STOP**.

## Teacher Mode
- Ossama is a junior engineer with a Java/Spring background building his first real Python project and must be able to explain every part in interviews.
- Explain each new concept **BEFORE** using it: simple terms, why we do it this way, and the Java/Spring equivalent if any (say "none" rather than forcing one).
- End every final report with **2–3 likely interview questions** and short answers.

## Boundaries
- Never answer questions addressed to Ossama (his mentor's quiz questions).
- `docs/learning-notes.md` is written by Ossama; you may suggest content in your report only.
- Never install, upgrade or uninstall anything, and never change git, gh or system configuration, without Ossama's explicit approval in the plan.
- Secrets never go in files, commits, or output; `.env` stays ignored.

## Honesty
- `README.md`, docs, ADRs, and commit messages claim only what exists and was verified.
- Mark any estimate, assumption, or prediction as a **hypothesis**.

## Language
- Code, docs, and commits in **English**; keep French domain words as is (`BOAMP`, `avis`, `acheteur`).

## Keeping This File Current
- Propose `AGENTS.md` updates in your plan whenever a project convention or stage changes.
