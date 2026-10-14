# Learning Notes

A running log of what I'm learning as I build this project. Raw notes, not
polished articles — that's what the Medium series is for.

---

## 2026-10-02 — Starting the ontology

**Decision:** Start with the Protégé Pizza tutorial to learn the tool, then
move to a GraphDB Academy Engineer path for theory, then build the finance
ontology.

**Resources:**
- Protégé Pizza tutorial: https://michaeldebellis.com/post/new-protege-pizza-tutorial
- Protégé download: https://protege.stanford.edu
- GraphDB Academy: https://academy.graphwise.ai

**Questions (deferred):**
- How do I decide between `hasValue` as a data property and a `Value` class?
  (Started with data property.)
- When does it make sense to specialize a class into subclasses?
- How do I test that the ontology answers all CQs? (Plan: write SPARQL queries
  for each CQ.)

### First aha

Classes are categories. Individuals are members. In Protégé, a specific company
(Apple Inc.) is an individual of class `Company` — not a subclass. That
distinction is different from how I thought about data models.

---

## 2026-10-06 — Chapter 00 notes

**Open question:** Before reading this book, my understanding is that
metadata-modelling can be used to define the structural language used to build
an ontology. Why does the book treat data modelling and ontology as separate
layers in the EKA framework?

*(See `docs/eka-framework.md` for the EKA model and `docs/glossary.md` for
definitions.)*

---

## 2026-10-06 — Pizza tutorial, chapters 0–3

### Chapter 00

**Aha:** A common misconception is that OWL reasoning alone makes knowledge
executable. It doesn't — you need a trigger and execution layer on top.

**Aha:** Protégé can describe structure, process, data, and organization all
within a single unified model. Unlike traditional tools that require switching
between diagramming frameworks (UML for structure, BPMN for processes),
Protégé lets you build an ontology where all business facets are represented in
one logically connected language (OWL).

**Aha:** Ontology vs. traditional data modeling:
- Traditional databases focus on storing data efficiently.
- Ontologies focus on representing meaning formally.
- Traditional databases operate under a **Closed World Assumption (CWA)**:
  if something is not stored, it is considered false.
- Ontologies operate under an **Open World Assumption (OWA)**:
  absence of knowledge does not imply falsehood — it just means the knowledge
  is not yet known.

**Aha:** LLMs are powerful, but without explicit knowledge structures they
struggle with consistency, explainability, governance, enterprise semantics,
and controlled reasoning. Poor structures lead to "beautiful garbage" from AI.
Ontology provides the semantic backbone that complements probabilistic AI.

### Chapter 01

**Topics covered:**
- Classes, subclasses, individuals
- Object properties (individual → individual)
- Data properties (individual → literal)
- Restrictions
- Reasoners and logical inference
- SWRL rules
- SPARQL queries
- SHACL validation

**Aha:** There are three types of classes in OWL:
1. **Primitive classes** — defined by necessary (but not sufficient) conditions.
2. **Defined classes** — defined by both necessary and sufficient conditions.
3. **Anonymous classes** — created by the reasoner when using class expressions.

**Aha:** OWL restrictions fall into three categories:
1. **Quantifier restrictions** — existential (`some`) and universal (`only`).
2. **Cardinality restrictions** — exact, min, max counts.
3. **hasValue restrictions** — specific required values.

**Mapping to other modeling languages:**
- UML association ≈ OWL object property
- UML attribute ≈ OWL data property
- E/R relation ≈ OWL object property
- E/R attribute ≈ OWL data property

### Confusions (open)

- When should a data property be promoted to a full `Value` class?
- How do I decide between `some` and `only` in a restriction?
- When is an anonymous class the right modeling choice vs. a named class?

---

## 2026-10-14 — Protégé 5 + finance ontology starter

**Completed:** Pizza tutorial in Protégé 5. Created starter finance ontology
at `ontology/finance-ontology.ttl`.

**Next:** Write competency questions in `docs/competency-questions.md`, then
SPARQL queries in `queries/`, then SHACL shapes in `validation/`.

**Open question:** How do I get the HermiT reasoner to infer `TradedEquity`
from the `tradedOn` relation? (Answer: use an equivalence axiom with
`owl:intersectionOf` and `owl:someValuesFrom`.)

---

<!-- Add entries as you learn. Format: date, topic, aha moments, confusions,
finance application. -->
