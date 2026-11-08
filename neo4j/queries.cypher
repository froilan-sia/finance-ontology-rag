// ============================================================
// Competency-question queries, mirroring the SPARQL queries
// from Article 1 (Q1–Q3), expressed in Cypher.
// ============================================================

// Q1 — Which equities trade on NASDAQ, and who issues them?
// (SPARQL equivalent: Article 1, query block "Q1")
MATCH (e:Equity)-[:TRADED_ON]->(m:Market {name: "NASDAQ"})
MATCH (e)-[:ISSUED_BY]->(i:Issuer)
RETURN e.name AS equity, i.name AS issuer
ORDER BY equity;

// Q2 — Who issues a given financial instrument?
MATCH (e:Equity {ticker: "AAPL"})-[:ISSUED_BY]->(i:Issuer)
RETURN i.name AS issuer;

// Q3 — (Investor transactions): not modelled in this LPG seed.
// Included to show the shape a Cypher version would take once
// the transaction subgraph exists.
// MATCH (inv:Investor {name: "Alice"})-[:HAS_ACCOUNT]->(acc:Account)
//       -[:HAS_TRANSACTION]->(tx:Transaction)
// RETURN inv.name, acc.id, tx.amount, tx.currency
// ORDER BY tx.date DESC;

// Demonstrating the missing reasoner: this returns nothing
// unless :TradedEquity was written explicitly at ingest time.
MATCH (e:TradedEquity)
RETURN e.name AS inferred_as_traded_equity;
