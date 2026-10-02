# Competency Questions

Competency questions (CQs) are the requirements specification for an ontology. They define what the ontology must be able to answer. If the ontology can answer every CQ, it's fit for purpose. If it can't, the ontology is incomplete.

This file documents the CQs for the Finance Ontology for RAG.

---

## Scope

The ontology models the structure of financial documents — primarily PDFs containing text, tables, and charts. The goal is to enable semantic retrieval and reasoning that pure vector search cannot.

## Competency Questions

### CQ1 — Entity Retrieval
**"Which companies are mentioned in this document?"**

Forces: `Company` class, `Document` class, `mentionsCompany` relationship.

### CQ2 — Metric Attribution
**"What metrics does Company X report, and for what time period?"**

Forces: `Metric` class, `TimePeriod` class, `reportsMetric`, `metricForCompany`, and `forTimePeriod` relationships.

### CQ3 — Multi-Hop Relationship
**"Which companies are mentioned in the same chart as Q3 2024 revenue?"**

Forces: `Chart` class, `chartShowsMetric` relationship, and traversal across `Chart → Metric → TimePeriod` and `Chart → Metric → Company`.

### CQ4 — Value Retrieval
**"What is the value of Metric Y for Company X in Q3 2024?"**

Forces: `hasValue` data property; numeric range.

### CQ5 — Document Context
**"What other metrics are reported in the same document as Metric Y?"**

Forces: bidirectional traversal across `Document → Metric`.

### CQ6 — Comparison
**"Which companies reported revenue above 100M in Q3 2024?"**

Forces: numeric range filtering and cross-entity comparison.

---

## Testing

Each CQ will be tested as a SPARQL query. See [`queries/`](../queries/) for the implementations.

A CQ is considered answered when:

1. The query returns meaningful results against a populated graph
2. The ontology can represent the required structure without workarounds
3. The result is defensible in an interview or portfolio review

## Status

| CQ  | Status |
|-----|--------|
| CQ1 | 🔄 Drafted |
| CQ2 | 🔄 Drafted |
| CQ3 | 🔄 Drafted |
| CQ4 | ⏳ Pending |
| CQ5 | ⏳ Pending |
| CQ6 | ⏳ Pending |
