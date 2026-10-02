# Design Decisions

A running log of the architectural and modeling decisions made in this project, with rationale.

---

## DD-001: Model `Company` as a class, not a string

**Decision:** `Company` is an OWL class with individuals, not a `hasCompanyName` string property on `Document`.

**Rationale:** String matching cannot answer "Which companies are mentioned alongside Q3 revenue?" — it can only find text. A class allows graph traversal across documents, metrics, and charts. The same company mentioned in 50 documents is one node, not 50 strings.

**Trade-off:** Requires entity resolution when ingesting PDFs — the same company may appear as "Apple", "Apple Inc.", or "AAPL". Entity resolution is a later phase.

---

## DD-002: Use `metricForCompany` rather than `companyReportsMetric`

**Decision:** The relationship is defined from the `Metric` to the `Company` (`fin:metricForCompany`), not from `Company` to `Metric`.

**Rationale:** A metric belongs to exactly one company — it's an attribute of the metric. A company reports many metrics. Placing the relationship on the "many" side (Metric) avoids a reverse cardinality issue and makes queries more natural.

**Trade-off:** Query syntax feels inverted on first read — `?metric fin:metricForCompany ?company`. Acceptable.

---

## DD-003: Include `Chart` as a first-class class

**Decision:** `Chart` is its own OWL class, not just a type of `Document` content.

**Rationale:** CQ3 requires answering "which companies are mentioned in the same chart as X." Without a `Chart` class and a `chartShowsMetric` relationship, that query becomes impossible.

**Trade-off:** Extraction complexity increases — chart entities and their metric associations must be extracted from PDFs. This is the hardest part of the ingestion pipeline.

---

## DD-004: Time periods as classes, not literal strings

**Decision:** `TimePeriod` is a class with a `hasPeriodLabel` string property, not a raw string on `Metric`.

**Rationale:** Enables temporal reasoning — comparing Q3 2024 to Q3 2023, or Q1 vs Q2. A string "Q3 2024" cannot be compared without parsing. A class can carry additional attributes later (start date, end date, fiscal year).

**Trade-off:** Slightly more verbose to populate. Acceptable.

---

## Open questions

- Should `Metric` be specialized into subclasses (`RevenueMetric`, `ProfitMetric`, `MarginMetric`)? Deferred until use cases require it.
- Should `Document` be specialized into `AnnualReport`, `QuarterlyReport`, `Filing`? Same.
- How to handle company subsidiaries and parent relationships? Out of scope for v1.

