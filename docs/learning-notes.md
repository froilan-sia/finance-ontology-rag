# Learning Notes

A running log of what I'm learning as I build this project. Raw notes, not polished articles — that's what the Medium series is for.

---

## 2026-10-02 — Starting the ontology

### Decision
Start with the Protégé Pizza tutorial to learn the tool, then move to a GraphDB Academy Engineer path for theory, then build the finance ontology.

### Resources
- Protégé Pizza tutorial: `https://michaeldebellis.com/post/new-protege-pizza-tutorial`
- Protégé download: `https://protege.stanford.edu`
- GraphDB Academy: `https://academy.graphwise.ai`

### Questions
- How do I decide between `hasValue` as a data property and a `Value` class? (Deferred — started with data property.)
- When does it make sense to specialize a class into subclasses? (Deferred.)
- How do I test that the ontology answers all CQs? (Plan: write SPARQL queries for each CQ.)

- ### 10-06-2026 -- chapter 00

<img width="1742" height="966" alt="image" src="https://github.com/user-attachments/assets/23f55ace-b086-45bc-bd29-f949e31a0a90" />
- Before reading this book, my understanding is that metadata-modelling can be used to define the structural language used to build an ontology, and now why does the data modelling and ontology a separate layer in EKA framework ?
* 


### First aha
Classes are categories. Individuals are members. In Protégé, a specific company (Apple Inc.) is an individual of class `Company` — not a subclass. That distinction is different from how I thought about data models.


## - — Pizza tutorial, chapters 0–3
## - - Chapter 00 
---

# EKA (Event-Knowledge-Action) System Architecture

An **EKA system** is formally defined as a 5-tuple:

$$EKA = (K, R, \Theta, \Phi, \Gamma)$$

---

## Core Components Summary

| Symbol | Layer | Description | Standard Technologies / Standards |
| :---: | :--- | :--- | :--- |
| $K$ | **Knowledge Graph Layer** | Entities (nodes) and semantic relationships (edges) conforming to an ontology. | RDF, Property Graphs, OWL Ontologies |
| $R$ | **Reasoning & Rules Layer** | Inference rules that derive new implicit facts from explicit graph data ($K$). | OWL, SWRL, Custom Rule Engines |
| $\Theta$ | **Trigger Layer** | Conditions (semantic events, queries, or time-based triggers) that initiate execution. | SPARQL Subscriptions, Event Buses, Cron |
| $\Phi$ | **Execution Layer** | Actions (API calls, process invocations, alerts, graph updates) modifying state. | REST/GraphQL APIs, Workflows, SPARQL Update |
| $\Gamma$ | **Governance Layer** | Constraints, validation rules, and access policies ensuring semantic integrity. | SHACL, ShEx, RBAC/ABAC Policies |

---

## Detailed Definitions

* **$K$ — Knowledge Graph Layer**  
  A set of entities (nodes) and semantic relationships (edges) conforming to a domain ontology.

* **$R$ — Reasoning & Rules Layer**  
  A set of inference rules (OWL, SWRL, or custom) that derive new facts from the Knowledge Graph ($K$).

* **$\Theta$ — Trigger Layer**  
  A set of conditions (semantic events, queries, or time-based triggers) that initiate system execution.

* **$\Phi$ — Execution Layer**  
  A set of actions (API calls, process invocations, alerts, graph updates) that change the real world or update the knowledge graph.

* **$\Gamma$ — Governance Layer**  
  Constraints, validation rules (such as SHACL), and access policies that ensure system and semantic integrity.
--

To avoid confusion, it is helpful to position EKA relative to well-known frameworks.

| Framework | Primary focus | Relationship to EKA |
| --- | --- | --- |
| **TOGAF - The OpenGroup Architecture Framework (ADM - Architecture Development Method)** | Enterprise architecture process | EKA can be used as a **semantic automation pillar** within all TOGAF's ADM layers. |
| **Semantic Web Stack (OWL, RDF, SPARQL - "SPARQL Protocol and RDF Query Language")** | Knowledge representation and query | EKA **extends** the stack with an explicit execution layer. |
| **Knowledge Graph (Native RDF: GraphDB, AllegroGraph, Stardog; Property Graph: Neo4j)** | Graph storage and traversal | The *K* layer of EKA. Native RDF graphs are the recommended choice for preserving OWL semantics. Property graphs may be used for specialized, performance-intensive queries after transformation. |
| **Rule engines (Drools, DMN - Decision Model and Notation)** | Business rule execution | EKA generalizes rules into **semantic triggers + actions** |
| **Data Fabric / Data Mesh** | Data integration and decentralization | EKA adds **executable semantics** on top of integrated data. |

## -- chapter 01 : 
Classes
Subclasses
Individuals
Object Properties - these connect individuals to other individuals.
Data Properties - These connect individuals to literal value.
Restrictions
Reasoners
Logical Inference
SWRL Rules
SPARQL Queries
SHACL Validation

### Aha
* A common misconception is that OWL reasoning alone makes knowledge executable.
* Protégé can describe structure, process, data, and organization all within a single unified model.
Unlike traditional tools that require you to switch between completely different diagramming frameworks (like UML for structure or BPMN for processes), Protégé allows you to build an ontology where all of these distinct business facets are represented using a single, logically connected language (OWL - Web Ontology Language).
<img width="1442" height="834" alt="image" src="https://github.com/user-attachments/assets/dc53cb74-327a-46cb-925a-0df0ac41711f" />

* Ontology vs Traditional Data Modeling - Traditional databases focus on storing data efficiently while Ontologies focus on representing meaning formally.
* Traditional databases generally operate under a Closed World Assumption (CWA): If something is not stored, it is considered false.
* Under OWA: Absence of knowledge does not imply falsehood. - It just means the knowledge that is unknown yet.
* Large Language Models (LLMs) are powerful, but without explicit knowledge structures they often struggle with:
  - Consistency
  - Explainability
  - Governance
  - Enterprise semantics
  - Controlled reasoning
  - Poor structures for LLMs norm
* Poor structures for LLMs normally lead to the "beautiful garbage" to be generated by AI.
* Ontology provides the semantic backbone that complements probabilistic AI systems.


| Term | Definition |
| :--- | :--- |
| **Ontology** | A formal, machine-readable model that defines concepts, relationships, constraints, and inference logic within a domain. |
| **OWL (Web Ontology Language)** | A W3C standard language for representing semantic knowledge in a logically rigorous, machine-interpretable form. |
| **Protégé** | An open-source semantic modeling platform and ontology editor used to build, reason over, and validate OWL ontologies. |
| **Class** | A category or type of thing in an ontology (e.g., Pizza, CheeseTopping). |
| **Individual** | A concrete instance of a class (e.g., MargheritaPizza, MozzarellaTopping). |
| **Object Property** | A relationship that connects one individual to another (e.g., hasTopping). |
| **Data Property** | A relationship that connects an individual to a literal value (e.g., hasCalories). |
| **Reasoner** | A logic engine that checks consistency, infers implicit relationships, and automatically classifies individuals based on defined axioms. |
| **Open World Assumption (OWA)** | The principle that absence of information does not imply falsity; knowledge may be incomplete. |
| **Closed World Assumption (CWA)** | The principle that anything not explicitly known is assumed false (typical of relational databases). |
| **Executable Knowledge Architecture (EKA)** | An architectural framework that transforms formal knowledge into machine-executable intelligence through a structured pipeline of diagrams, meta-models, ontologies, knowledge graphs, and executable intelligence. |
| **Semantic Inference** | The process by which a reasoner derives new knowledge from existing axioms without manual intervention. |

### Confusion





---

<!-- Add entries as you learn. Format: date, topic, aha moments, confusions, finance application. -->
