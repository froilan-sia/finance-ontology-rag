# Verification Log: Neo4j Ingestion

This document records the verification steps and the troubleshooting iterations for `scripts/test_neo4j_ingestion.py`, part of the **Article 5: Protégé vs. GraphDB vs. Neo4j** comparison.

## Environment
- **Neo4j Version:** 5 (Community Edition via Docker)
- **Python Version:** 3.14 (virtual environment)
- **Neo4j Python Driver:** 5.x

## The Iterations

During the initial run of the test harness, we encountered three distinct failures. These are documented here because they perfectly illustrate the architectural differences between RDF triplestores and Property Graphs discussed in Article 5.

### Run 1: The Enterprise Edition Constraint
- **Command:** `python scripts/test_neo4j_ingestion.py`
- **Result:** `Neo.DatabaseError.Schema.ConstraintCreationFailed`
- **Error Message:** `Property existence constraint requires Neo4j Enterprise Edition.`
- **Resolution:** Neo4j 5+ supports property existence constraints, but only on the Enterprise Edition. We removed the `REQUIRE ... IS NOT NULL` constraints from `neo4j/schema.cypher` to ensure the code runs on the free Community Edition Docker image, leaving only uniqueness constraints and indexes.

### Run 2: The Duplicate Market
- **Command:** `python scripts/test_neo4j_ingestion.py`
- **Result:** `Neo.ClientError.Schema.ConstraintValidationFailed`
- **Error Message:** `Node(2) already exists with label 'Market' and property 'name' = 'NASDAQ'`
- **Resolution:** The initial seed script (`seed.cypher`) created a new `NASDAQ` market node for the Microsoft block, which violated the `market_name_unique` constraint. This proves the structural integrity constraint is working. We updated the seed script to reuse the existing NASDAQ node via a `MATCH` clause instead of a second `CREATE` statement.

### Run 3: The Duplicate Issuer
- **Command:** `python scripts/test_neo4j_ingestion.py`
- **Result:** `Neo.ClientError.Schema.ConstraintValidationFailed`
- **Error Message:** `Node(9) already exists with label 'Issuer' and property 'name' = 'Microsoft Corporation'`
- **Resolution:** Similar to Run 2, the seed script inadvertently created the Microsoft issuer twice. We refactored the seed script to guarantee exactly one `CREATE` per unique node, using `MATCH` for all subsequent relationship creations.

## The Clean Pass

After resolving the data and schema conflicts, the final run executes successfully:

```text
Connecting to Neo4j at bolt://localhost:7687 ...

[1/3] Applying schema constraints ...
  executed 5 statement(s) from schema.cypher

[2/3] Loading seed data ...
  executed 10 statement(s) from seed.cypher

[3/3] Running Q1 (equities on NASDAQ + issuers) ...
  Apple Inc. Common Stock  |  Apple Inc.
  Microsoft Corporation Common Stock  |  Microsoft Corporation

Received notification from DBMS server: warn: label does not exist. The label `TradedEquity` does not exist.
Nodes explicitly labelled :TradedEquity = 0
  -> Neo4j emits a 'label does not exist' warning above.
     That warning is the point: no reasoner created the label.
     GraphDB infers it from the OWL axiom; Neo4j does not.

Compare with Article 1's SPARQL result: the answer to Q1 matches, but the inferred :TradedEquity classification is absent in the property graph.

