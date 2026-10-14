# Design Decisions

A running log of the architectural and modeling decisions made in this project, with rationale and trade-offs.

---

## DD-001 — `FinancialInstrument` as the base class for tradable assets

**Decision:** `Equity`, `Bond`, and `Derivative` are subclasses of a common parent class `FinancialInstrument`.

**Rationale:** All three share the same core relationships — they are issued by a `Party`, traded on a `Market`, and identified by an ISIN. Putting those properties on the parent class avoids repeating them three times and lets queries target "any instrument" without listing all subclasses.

**Trade-off:** A generic query for `:FinancialInstrument` returns all types (equities, bonds, derivatives). If that's ever a problem, we can add more specific restrictions on each subclass.

---

## DD-002 — `TradedEquity` as a defined class, not a primitive class

**Decision:** `TradedEquity` is defined by an equivalence axiom — `Equity and (tradedOn some Market)` — rather than being a plain subclass of `Equity` that individuals are manually typed into.

**Rationale:** This is the whole point of using OWL rather than a relational schema. A primitive class only captures necessary conditions — you have to assert membership manually. A defined class captures necessary **and sufficient** conditions, so the reasoner can classify individuals automatically. When `AppleStock` is asserted as an `Equity` traded on `NASDAQ` (a `Market`), the reasoner infers it's a `TradedEquity` without anyone typing that fact.

**Trade-off:** Defined classes require the reasoner to be running to see their members. If someone opens the file without running HermiT, `TradedEquity` will appear empty in the Asserted view. This is intentional — it's how OWL works — but it means documentation needs to explain the workflow.

**Alternative considered:** A simple `rdfs:subClassOf :Equity` with manual assertions. Rejected — it wouldn't demonstrate reasoning, which is the core capability this project is testing.

---

## DD-003 — `Market` as a separate class, not a data property

**Decision:** `Market` is an OWL class with individuals like `:NASDAQ`, connected to instruments via the `:tradedOn` object property. It is not stored as a string like `hasMarketName "NASDAQ"`.

**Rationale:** Markets have their own attributes (venue type, region, operating hours) and their own relationships (listed instruments, participating brokers). Modeling `Market` as a class lets us extend it without changing the schema for instruments.

**Trade-off:** Requires entity resolution — the same market may be referred to by different names. Out of scope for v0.1.0.

---

## DD-004 — `Party` as a parent class for `Issuer`, `Broker`, `Investor`

**Decision:** `Issuer`, `Broker`, and `Investor` are all subclasses of a common `Party` class rather than three independent classes.

**Rationale:** A single entity can hold more than one role (a firm can be both a broker and an issuer). Under `Party`, the same individual can be asserted as both without needing multiple inheritance. Shared attributes like `:hasName` belong on the parent class.

**Trade-off:** Queries for "any party" return mixed results. Acceptable — this matches the reality that financial entities play multiple roles.

---

## DD-005 — Data properties vs object properties

**Decision:** Relationships between two individuals use object properties (`:issuedBy`, `:tradedOn`, `:hasAccount`, `:hasTransaction`, `:involvesInstrument`). Attributes with literal values use data properties (`:hasISIN`, `:hasName`, `:hasAmount`, `:hasCurrency`, `:hasDate`).

**Rationale:** This is the OWL-standard split. Object properties can be reasoned over — a reasoner can infer new relationships from them. Data properties carry literal values that don't participate in reasoning the same way. Keeping them separate keeps the reasoning layer clean.

**Trade-off:** Some attributes (like `:hasName`) could arguably be object properties pointing to a `Name` class. We chose data properties for simplicity. If names ever need their own metadata (source, confidence, timestamp), this decision should be revisited.

---

## DD-006 — Namespace and IRI strategy

**Decision:** The ontology uses `https://froilan-sia.github.io/finance-ontology-rag/ontology#` as its default namespace, rather than the Protégé default of `http://www.semanticweb.org/username/ontologies/...`.

**Rationale:** The default Protégé namespace is not owned by the author and changes with username and date. A GitHub Pages URL is stable, memorable, and controlled by the project owner. The URL doesn't need to resolve — it's an identifier, not a location.

**Trade-off:** If GitHub Pages is ever set up to serve the ontology file, the namespace can be upgraded to a dereferenceable URL. Until then, it's a stable identifier only.

---

## Open Questions

- Should `FinancialInstrument` be further split into `ListedInstrument` vs `UnlistedInstrument`?
- How should we handle company subsidiaries and parent relationships?
- When should a data property like `:hasISIN` be promoted to a full `:Identifier` class with its own type (ISIN, CUSIP, SEDOL)?
- Should `:hasCurrency` reference a `Currency` class instead of a string, to enable currency-pair reasoning?

---

## How to Add a New Decision

1. Copy the template: **Decision**, **Rationale**, **Trade-off**, **Alternatives considered**.
2. Add it as the next `DD-###` entry.
3. If the decision supersedes an earlier one, note that explicitly and link to the previous decision.
4. Commit with a message like: `docs: add DD-007 on entity resolution strategy`.
