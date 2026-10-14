# EKA (Event-Knowledge-Action) System Architecture

An **EKA system** is formally defined as a 5-tuple:

$$EKA = (K, R, \Theta, \Phi, \Gamma)$$

---

## Core Components

| Symbol | Layer | Description | Standards / Technologies |
|:---:|---|---|---|
| $K$ | **Knowledge Graph Layer** | Entities (nodes) and semantic relationships (edges) conforming to an ontology. | RDF, Property Graphs, OWL |
| $R$ | **Reasoning & Rules Layer** | Inference rules that derive new implicit facts from explicit graph data ($K$). | OWL, SWRL, custom rule engines |
| $\Theta$ | **Trigger Layer** | Conditions (semantic events, queries, time-based triggers) that initiate execution. | SPARQL subscriptions, event buses, cron |
| $\Phi$ | **Execution Layer** | Actions (API calls, process invocations, alerts, graph updates) modifying state. | REST/GraphQL APIs, workflows, SPARQL Update |
| $\Gamma$ | **Governance Layer** | Constraints, validation rules, access policies ensuring semantic integrity. | SHACL, ShEx, RBAC/ABAC |

---

## Detailed Definitions

- **$K$ — Knowledge Graph Layer:** A set of entities (nodes) and semantic
  relationships (edges) conforming to a domain ontology.
- **$R$ — Reasoning & Rules Layer:** A set of inference rules (OWL, SWRL, or
  custom) that derive new facts from the Knowledge Graph ($K$).
- **$\Theta$ — Trigger Layer:** A set of conditions (semantic events, queries,
  or time-based triggers) that initiate system execution.
- **$\Phi$ — Execution Layer:** A set of actions (API calls, process
  invocations, alerts, graph updates) that change the real world or update the
  knowledge graph.
- **$\Gamma$ — Governance Layer:** Constraints, validation rules (such as
  SHACL), and access policies that ensure system and semantic integrity.

---

## EKA Relative to Other Frameworks

| Framework | Primary Focus | Relationship to EKA |
|---|---|---|
| **TOGAF (ADM)** | Enterprise architecture process | EKA can serve as a **semantic automation pillar** within all TOGAF ADM layers. |
| **Semantic Web Stack (OWL, RDF, SPARQL)** | Knowledge representation and query | EKA **extends** the stack with an explicit execution layer. |
| **Knowledge Graph (GraphDB, Stardog, Neo4j)** | Graph storage and traversal | The $K$ layer of EKA. Native RDF graphs are recommended for preserving OWL semantics. Property graphs may be used for specialized, performance-intensive queries after transformation. |
| **Rule Engines (Drools, DMN)** | Business rule execution | EKA generalizes rules into **semantic triggers + actions**. |
| **Data Fabric / Data Mesh** | Data integration and decentralization | EKA adds **executable semantics** on top of integrated data. |

---

## EKA and `finance-ontology-rag`

| EKA Layer | Where it lives in this repo |
|---|---|
| $K$ — Knowledge Graph | `ontology/finance-ontology.ttl` |
| $R$ — Reasoning | HermiT reasoner + `:TradedEquity` equivalence axiom |
| $\Theta$ — Trigger | SPARQL queries in `queries/` (invoked by the RAG pipeline) |
| $\Phi$ — Execution | RAG fusion layer (future: SPARQL Update for graph writes) |
| $\Gamma$ — Governance | `validation/*.ttl` SHACL shapes + CI workflow |
