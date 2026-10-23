# Finance Ontology for RAG

A governed Retrieval-Augmented Generation (RAG) system for financial data. Combines vector retrieval with a formal OWL ontology, SPARQL queries, and SHACL validation.

## Current State (v0.2.0)

| Component | Status |
|-----------|--------|
| Ontology (`ontology/finance-ontology.ttl`) | ✅ 12 classes, 5 object properties, 5 data properties |
| Reasoner verification | ✅ HermiT and Pellet run clean |
| Inference | ✅ `AppleStock` inferred as `TradedEquity` |
| SPARQL queries | ✅ Q1–Q3 verified in Protégé, results in `docs/screenshots/` |
| SHACL validation | ✅ Automated via GitHub Actions (`pyshacl`) |
| RAG fusion layer | ⏳ Not yet implemented |

## How to Verify the Inference

1. Open `ontology/finance-ontology.ttl` in Protégé 5
2. Run `Reasoner → HermiT → Start reasoner`
3. In the class hierarchy, switch to **Inferred** view
4. Click `TradedEquity` — `AppleStock` should appear as a yellow-highlighted member

## Data Governance (CI/CD)

This repository uses GitHub Actions to enforce data quality. Every push to `main` triggers a `pyshacl` validation pipeline against our `financial-instrument-shape.ttl` data contracts. 

[![Ontology Data Governance CI](https://github.com/froilan-sia/finance-ontology-rag/actions/workflows/validate-ontology.yml/badge.svg)](https://github.com/froilan-sia/finance-ontology-rag/actions/workflows/validate-ontology.yml)


## Article Series: Enterprise Ontology & RAG

This repository is built incrementally as part of an 8-part Medium series on enterprise data architecture.

1. [Why Your RAG Pipeline Needs an Ontology (And How to Build One)](https://medium.com/@froilan.sia/why-your-rag-pipeline-needs-an-ontology-and-how-to-build-one-2b9eb952f626)
2. [Automating Data Governance: CI/CD for Your Knowledge Graph](https://medium.com/@froilan.sia/automating-data-governance-cicd-knowledge-graph-0f04b5206826)
3. Building the Dual-Branch RAG: Python, rdflib, and ChromaDB *(Coming Soon)*
4. From Tables to Triples: The "Cold Start" Problem in Enterprise Ontologies *(Coming Soon)*
5. Protégé vs. GraphDB vs. Neo4j: Choosing Your Ontology Tooling *(Coming Soon)*
6. Designing AI-Ready Data Foundations: The HKMA Perspective *(Coming Soon)*
7. The Competency Question Method: How to Scope an Ontology *(Coming Soon)*
8. Data-First vs. AI-First: Architecting the Future of Agentic Workflows *(Coming Soon)*

## Related Articles

- [The Definitive Guide to Becoming a Solution Data Architect](https://medium.com/@froilan.sia/solution-data-architect-guide-togaf-dama-iasa-003959efa4d9)
- [Zero-Cost Local Multimodal RAG with ChromaDB](https://medium.com/@froilan.sia/zero-cost-multimodal-rag-chromadb-313930800633)
