# Finance Ontology for RAG

A governed Retrieval-Augmented Generation (RAG) system for financial data. Combines vector retrieval with a formal OWL ontology, SPARQL queries, and SHACL validation.

## Current State (v0.4.0)

| Component | Article | Status |
| :--- | :--- | :--- |
| **Ontology** (`ontology/finance-ontology.ttl`) | [Article 1](https://medium.com/@froilan.sia/why-your-rag-pipeline-needs-an-ontology-and-how-to-build-one-2b9eb952f626) | ✅ 13 classes, 6 object properties, 6 data properties |
| **Reasoner Verification** | [Article 1](https://medium.com/@froilan.sia/why-your-rag-pipeline-needs-an-ontology-and-how-to-build-one-2b9eb952f626) | ✅ HermiT and Pellet run clean |
| **Inference** | [Article 1](https://medium.com/@froilan.sia/why-your-rag-pipeline-needs-an-ontology-and-how-to-build-one-2b9eb952f626) | ✅ `AppleStock` inferred as `TradedEquity` |
| **SPARQL Queries** | [Article 1](https://medium.com/@froilan.sia/why-your-rag-pipeline-needs-an-ontology-and-how-to-build-one-2b9eb952f626) | ✅ Q1–Q3 verified in Protégé, results in `docs/screenshots/` |
| **SHACL Validation** | [Article 2](https://medium.com/@froilan.sia/automating-data-governance-cicd-knowledge-graph-0f04b5206826) | ✅ Automated via GitHub Actions (`pyshacl`) |
| **Dual-Branch RAG (Python)** | [Article 3](https://medium.com/@froilan.sia/building-the-dual-branch-rag-python-rdflib-and-chromadb-e7ec9470d362) | ✅ ChromaDB + `rdflib` + Ollama fusion layer implemented |
| **Ontology-Driven Extraction** | Article 4 | ✅ LLM entity extraction to RDF implemented |

---

## Quick Start

> **Note:** The following instructions will run the Python codebase developed in Article 3 and Article 4.

### Prerequisites
The scripts use Ollama to run a local LLM. Ensure you have Ollama installed and the required model pulled:

```bash
ollama pull qwen2.5:3b
```

### Setup & Execution

1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Seed the local vector database:**
   ```bash
   python app/setup_chroma.py
   ```

4. **Run the Dual-Branch RAG pipeline:**
   ```bash
   python app/rag_fusion.py
   ```

5. **Run the Ontology-Driven Extraction:**
   ```bash
   python app/extract_entities.py
   ```

---

## How to Verify the Inference
*(This section verifies the code from Article 1)*

1. Open `ontology/finance-ontology.ttl` in **Protégé 5**.
2. Run **Reasoner** → **HermiT** → **Start reasoner**.
3. In the class hierarchy, switch to the **Inferred** view.
4. Click `TradedEquity` — `AppleStock` should appear as a yellow-highlighted member.

---

## Data Governance (CI/CD)
*(This section verifies the code from Article 2)*

This repository uses GitHub Actions to enforce data quality. Every push to `main` triggers a `pyshacl` validation pipeline against our `financial-instrument-shape.ttl` data contracts.

[![Ontology Data Governance CI](https://github.com/froilan-sia/finance-ontology-rag/actions/workflows/validate-ontology.yml/badge.svg)](https://github.com/froilan-sia/finance-ontology-rag/actions/workflows/validate-ontology.yml)


---

## Article Series: Enterprise Ontology & RAG

This repository is built incrementally as part of an 8-part Medium series on enterprise data architecture. The code currently available reflects the progress up to Article 4.

1. **Why Your RAG Pipeline Needs an Ontology (And How to Build One)**
2. **Automating Data Governance: CI/CD for Your Knowledge Graph**
3. **Building the Dual-Branch RAG: Python, rdflib, and ChromaDB**
4. **From Tables to Triples: The "Cold Start" Problem in Enterprise Ontologies** *(Current state of repository)*
5. *Protégé vs. GraphDB vs. Neo4j: Choosing Your Ontology Tooling (Coming Soon)*
6. *Designing AI-Ready Data Foundations: The HKMA Perspective (Coming Soon)*
7. *The Competency Question Method: How to Scope an Ontology (Coming Soon)*
8. *Data-First vs. AI-First: Architecting the Future of Agentic Workflows (Coming Soon)*

---

## Related Articles

* The Definitive Guide to Becoming a Solution Data Architect
* Zero-Cost Local Multimodal RAG with ChromaDB

