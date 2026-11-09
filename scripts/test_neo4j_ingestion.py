#!/usr/bin/env python3
"""
test_neo4j_ingestion.py

Companion to Article 5: Protegé vs. GraphDB vs. Neo4j.

Loads the neo4j/schema.cypher and neo4j/seed.cypher files into a
local Neo4j instance, then runs the Q1 competency query and prints
the result. Demonstrates that the property-graph answer matches the
SPARQL answer from Article 1 -- and that the :TradedEquity
classification is ABSENT unless computed at the application layer.

Prerequisites:
    pip install neo4j
    A running Neo4j 5+ instance (e.g. via Docker):
        docker run -d --name neo4j-article5 \
          -p 7474:7474 -p 7687:7687 \
          -e NEO4J_AUTH=neo4j/testpassword \
          neo4j:5

Usage:
    python scripts/test_neo4j_ingestion.py
    # or override connection settings:
    NEO4J_URI=bolt://localhost:7687 \
    NEO4J_USER=neo4j \
    NEO4J_PASSWORD=testpassword \
    python scripts/test_neo4j_ingestion.py
"""

import os
import sys
from pathlib import Path

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable, AuthError

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "testpassword")

REPO_ROOT = Path(__file__).resolve().parent.parent
NEO4J_DIR = REPO_ROOT / "neo4j"

SCHEMA_FILE = NEO4J_DIR / "schema.cypher"
SEED_FILE = NEO4J_DIR / "seed.cypher"


def run_cypher_file(driver, path: Path) -> None:
    """Execute every statement in a .cypher file.

    Statements are separated by ';'. Lines beginning with '//' are
    comments and are stripped. This is intentionally simple -- it is
    not a full Cypher parser, but it is enough for the scripted
    files in this repo.
    """
    text = path.read_text(encoding="utf-8")
    # Strip line comments
    lines = [
        line for line in text.splitlines()
        if not line.strip().startswith("//")
    ]
    cleaned = "\n".join(lines)
    statements = [s.strip() for s in cleaned.split(";") if s.strip()]

    with driver.session() as session:
        for stmt in statements:
            session.run(stmt)
    print(f"  executed {len(statements)} statement(s) from {path.name}")


def q1_traded_on_nasdaq(driver):
    """The same competency question as Article 1 / SPARQL Q1."""
    cypher = """
    MATCH (e:Equity)-[:TRADED_ON]->(m:Market {name: "NASDAQ"})
    MATCH (e)-[:ISSUED_BY]->(i:Issuer)
    RETURN e.name AS equity, i.name AS issuer
    ORDER BY equity
    """
    with driver.session() as session:
        result = session.run(cypher)
        return [(r["equity"], r["issuer"]) for r in result]


def traded_equity_label_count(driver):
    """Count nodes explicitly labelled :TradedEquity.

    In Neo4j this will be 0 because no reasoner inferred the label.
    In GraphDB, the OWL axiom :TradedEquity ≡ :Equity ⊓
    (tradedOn some :Market) would have produced the same entities
    via inference -- which is the whole point of the comparison.
    """
    with driver.session() as session:
        result = session.run("MATCH (e:TradedEquity) RETURN count(e) AS n")
        return result.single()["n"]


def main() -> int:
    print(f"Connecting to Neo4j at {NEO4J_URI} ...")
    try:
        driver = GraphDatabase.driver(
            NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD)
        )
        driver.verify_connectivity()
    except AuthError as exc:
        print(f"Auth failed: {exc}")
        print("Check NEO4J_USER / NEO4J_PASSWORD.")
        return 2
    except ServiceUnavailable as exc:
        print(f"Could not reach Neo4j: {exc}")
        print("Is the container running? See the Docker command in the docstring.")
        return 3

    try:
        print("\n[1/3] Applying schema constraints ...")
        run_cypher_file(driver, SCHEMA_FILE)

        print("\n[2/3] Loading seed data ...")
        run_cypher_file(driver, SEED_FILE)

        print("\n[3/3] Running Q1 (equities on NASDAQ + issuers) ...")
        rows = q1_traded_on_nasdaq(driver)
        if not rows:
            print("  (no rows -- seed may not have loaded)")
        for equity, issuer in rows:
            print(f"  {equity}  |  {issuer}")

        n = traded_equity_label_count(driver)
        print(
            f"\nNodes explicitly labelled :TradedEquity = {n}"
            "\n  -> Neo4j emits a 'label does not exist' warning above."
            "\n     That warning is the point: no reasoner created the label."
            "\n     GraphDB infers it from the OWL axiom; Neo4j does not."
        )
        print(
            "\nCompare with Article 1's SPARQL result: the answer to Q1 "
            "matches, but the inferred :TradedEquity classification "
            "is absent in the property graph."
        )
        return 0
    finally:
        driver.close()


if __name__ == "__main__":
    sys.exit(main())
