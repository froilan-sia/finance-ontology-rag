# Finance Ontology for RAG

A governed Retrieval-Augmented Generation (RAG) system for financial data. Combines vector retrieval with a formal OWL ontology, SPARQL queries, and SHACL validation.

## Current State (v0.1.0)

| Component | Status |
|-----------|--------|
| Ontology (`ontology/finance-ontology.ttl`) | ✅ 12 classes, 5 object properties, 5 data properties |
| Reasoner verification | ✅ HermiT and Pellet run clean |
| Inference | ✅ `AppleStock` inferred as `TradedEquity` |
| SPARQL queries | ⏳ Not yet written |
| SHACL validation | ⏳ Not yet written |
| RAG fusion layer | ⏳ Not yet implemented |

## How to Verify the Inference

1. Open `ontology/finance-ontology.ttl` in Protégé 5
2. Run `Reasoner → HermiT → Start reasoner`
3. In the class hierarchy, switch to **Inferred** view
4. Click `TradedEquity` — `AppleStock` should appear as a yellow-highlighted member

## Related Articles

- [The Definitive Guide to Becoming a Solution Data Architect](https://medium.com/@froilan.sia/solution-data-architect-guide-togaf-dama-iasa-003959efa4d9)
- [Zero-Cost Local Multimodal RAG with ChromaDB](https://medium.com/@froilan.sia/zero-cost-multimodal-rag-chromadb-313930800633)
