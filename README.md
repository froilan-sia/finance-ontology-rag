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
| **Ontology-Driven Extraction** | [Article 4](https://medium.com/@froilan.sia/from-tables-to-triples-cold-start-problem-ontology-9414a08abf58) | ✅ LLM entity extraction to RDF implemented |
| **Tooling Comparison (Neo4j)** | Article 5 | ✅ Schema, seed, Q1 runner verified locally |
| **Tooling Comparison (NebulaGraph)** | Article 5 | ⚠️ Illustrative nGQL only, not tested |

---

## Quick Start

> **Note:** The following instructions will run the Python codebase developed in Article 3 and Article 4.

### Setup & Execution

1. Clone the repository
   ```bash
   git clone https://github.com/froilan-sia/finance-ontology-rag.git
   cd finance-ontology-rag
   ```

2. Create and activate a virtual environment:
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

### Prerequisites
The scripts use Ollama to run a local LLM. Ensure you have Ollama installed and the required model pulled:

```bash
ollama pull qwen2.5:3b
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
## Tooling Comparison (Article 5)

Article 5 compares three graph paradigms: RDF triplestores (GraphDB),
labeled property graphs (Neo4j), and distributed property graphs
(NebulaGraph). The runnable comparison lives in [`neo4j/`](neo4j/).

| Tool | Model | This repo | Status |
|---|---|---|---|
| Protegé | OWL / RDF (design-time) | `ontology/` | ✅ Article 1 |
| GraphDB | RDF triplestore | `ontology/` (load into GraphDB) | ✅ Article 1 |
| Neo4j | Property graph | `neo4j/` | ✅ Article 5 |
| NebulaGraph | Distributed property graph | `neo4j/nebula/` | ⚠️ illustrative syntax only, not tested |

### Running the Neo4j comparison

**1. Start Neo4j 5 (Docker):**

    docker run -d --name neo4j-article5 \
      -p 7474:7474 -p 7687:7687 \
      -e NEO4J_AUTH=neo4j/testpassword \
      neo4j:5

**2. Install the driver:**

    pip install -r requirements.txt

**3. Run the comparison script:**

    python scripts/test_neo4j_ingestion.py

The script loads `neo4j/schema.cypher` and `neo4j/seed.cypher`,
runs the Q1 competency query from Article 1 in Cypher, and prints
the result alongside a count of explicitly labelled `:TradedEquity`
nodes. That count is `0` — Neo4j has no native OWL reasoner, so the
classification that GraphDB infers must be written at ingest time
or computed in the application layer. The script is the proof.

To override the default connection (`bolt://localhost:7687`,
`neo4j` / `testpassword`):

    NEO4J_URI=bolt://localhost:7687 \
    NEO4J_USER=neo4j \
    NEO4J_PASSWORD=testpassword \
    python scripts/test_neo4j_ingestion.py

### NebulaGraph

`neo4j/nebula/` contains illustrative nGQL syntax for the same data.
It has **not** been run against a live NebulaGraph cluster; treat it
as reference only. See the transparency note in Article 5.

### Files

- [`neo4j/schema.cypher`](neo4j/schema.cypher) — uniqueness, node-key,
  and property-existence constraints (Neo4j 5+)
- [`neo4j/seed.cypher`](neo4j/seed.cypher) — Apple/MSFT seed data
- [`neo4j/queries.cypher`](neo4j/queries.cypher) — Q1–Q3 in Cypher
- [`neo4j/nebula/`](neo4j/nebula/) — illustrative nGQL (not tested)
- [`scripts/test_neo4j_ingestion.py`](scripts/test_neo4j_ingestion.py) —
  loader + Q1 runner + `:TradedEquity` count
---

## Article Series: Enterprise Ontology & RAG

This repository is built incrementally as part of an 8-part Medium series on enterprise data architecture. The code currently available reflects the progress up to Article 4.

1. *[Why Your RAG Pipeline Needs an Ontology (And How to Build One)](https://medium.com/@froilan.sia/why-your-rag-pipeline-needs-an-ontology-and-how-to-build-one-2b9eb952f626)*
2. *[Automating Data Governance: CI/CD for Your Knowledge Graph](https://medium.com/@froilan.sia/automating-data-governance-cicd-knowledge-graph-0f04b5206826)*
3. *[Building the Dual-Branch RAG: Python, rdflib, and ChromaDB*](https://medium.com/@froilan.sia/building-the-dual-branch-rag-python-rdflib-and-chromadb-e7ec9470d362)*
4. *[From Tables to Triples: The "Cold Start" Problem in Enterprise Ontologies](https://medium.com/@froilan.sia/from-tables-to-triples-cold-start-problem-ontology-9414a08abf58)* 
5. *Protégé vs. GraphDB vs. Neo4j: Choosing Your Ontology Tooling (Current state of repository)*
6. *Designing AI-Ready Data Foundations: The HKMA Perspective (Coming Soon)*
7. *The Competency Question Method: How to Scope an Ontology (Coming Soon)*
8. *Data-First vs. AI-First: Architecting the Future of Agentic Workflows (Coming Soon)*
---

## Related Articles

* [The Definitive Guide to Becoming a Solution Data Architect](https://medium.com/@froilan.sia/solution-data-architect-guide-togaf-dama-iasa-003959efa4d9)
* [Zero-Cost Local Multimodal RAG with ChromaDB](https://medium.com/@froilan.sia/zero-cost-multimodal-rag-chromadb-313930800633)

