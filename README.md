# Tender Watch

> Veille automatisée sur les marchés publics français publiés au BOAMP : collecte quotidienne des avis, recherche par mots-clés et sémantique, notation de pertinence par LLM, alerte matinale et questions-réponses avec citations.

Tender Watch is a planned application for monitoring French public procurement notices (*avis*) published on BOAMP open data. Think of it as a job search, automated for companies looking for public contracts: each day it will collect new *avis* and their *acheteur* details, store them, support keyword and semantic search, score each notice's relevance against a company profile with an LLM, send a morning alert, and let users ask questions answered with citations from the source notices (a hand-written RAG).

Status: work in progress. Nothing is implemented yet.

## Planned stack

- **Backend:** Python 3.12, FastAPI, SQLAlchemy 2, Alembic, Pydantic
- **Database:** PostgreSQL + pgvector
- **Frontend:** Angular
- **Tooling & Quality:** uv, ruff, strict mypy, pytest

## Development

**Prerequisite:** [`uv`](https://docs.astral.sh/uv/) (Python 3.12 is pinned in `.python-version`).

Install the locked development environment:

```bash
uv sync --locked
```

Run all checks locally:

```bash
uv run ruff check
uv run ruff format --check
uv run mypy
uv run pytest
```

## License

MIT — see [LICENSE](LICENSE).
