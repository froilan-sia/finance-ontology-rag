# Finance Ontology for RAG

**Vector search finds similar text. It doesn't understand what the text means.**

This repository explores how a formal ontology can give a RAG pipeline structured knowledge about financial documents — companies, metrics, time periods, and the relationships between them.

It's the companion project to my [AI & RAG Architecture Series](https://[medium.com/@froilan.sia](https://medium.com/@froilan.sia/zero-cost-multimodal-rag-chromadb-313930800633)) and extends the vector-based pipeline into semantic retrieval and reasoning.

---

## The problem

My multimodal RAG pipeline can retrieve the right chunk of a financial PDF. But when a user asks:

> "Which companies are mentioned alongside Q3 2024 revenue?"

...it has no way to distinguish between "a company that reports revenue" and "a company mentioned in the same paragraph as a revenue chart."

Vector similarity is good at finding relevant text. It's not good at representing the *structure* of what's in that text.

## What this project does

1. Defines a small finance-domain ontology (classes, properties, relationships)
2. Builds a knowledge graph from a corpus of financial PDFs
3. Extends retrieval to use both vector similarity and graph traversal
4. Documents the architecture, design decisions, and lessons learned

## Status

🚧 **In progress** — this repo is being built as part of a learning journey. See [learning notes](docs/learning-notes.md) for the running log.

| Phase | Status |
|-------|--------|
| Competency questions defined | ✅ |
| Ontology scaffold (OWL/Turtle) | ✅ |
| Protégé refinement | 🔄 |
| Knowledge graph construction | ⏳ |
| GraphRAG integration | ⏳ |
| SHACL validation | ⏳ |

## Repository structure

- `ontology/` — the OWL/Turtle ontology files
- `queries/` — SPARQL queries answering competency questions
- `validation/` — SHACL shapes for data quality
- `docs/` — design decisions and learning notes
- `examples/` — sample outputs

## The ontology at a glance

| Class | Description |
|-------|-------------|
| `Document` | A financial report, filing, or chart |
| `Company` | An organization mentioned in a document |
| `Metric` | A measurable quantity (revenue, profit, margin) |
| `TimePeriod` | A fiscal quarter or year |
| `Chart` | A visual representation in a document |

See [`ontology/`](ontology/) for the full definition.

## Related work

- [AI & RAG Architecture Series](https://medium.com/@froilan.sia) — the vector pipeline this builds on
- [m1_multimodal_rag](https://github.com/froilan-sia/m1_multimodal_rag) — the base RAG implementation
- [The Definitive Guide to Becoming a Solution Data Architect](https://medium.com/@froilan.sia/solution-data-architect-guide-togaf-dama-iasa-003959efa4d9)

## License

MIT
