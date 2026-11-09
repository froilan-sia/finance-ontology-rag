// ============================================================
// Seed data: the same Apple/NASDAQ fact from Article 1,
// modelled as a Labeled Property Graph.
// ============================================================

// Clean slate (safe for a local dev instance only)
// ============================================================
// Seed data: Apple/NASDAQ (Article 1) plus MSFT, modelled as a
// Labeled Property Graph. Each node is created exactly once; all
// relationships use MATCH to reuse existing nodes. Safe to rerun
// because of the DETACH DELETE at the top.
// ============================================================

MATCH (n) DETACH DELETE n;

// --- Apple ---
CREATE (a:Equity { ticker: "AAPL", name: "Apple Inc. Common Stock" });
CREATE (i:Issuer { name: "Apple Inc." });
CREATE (m:Market { name: "NASDAQ" });

MATCH (a:Equity {ticker: "AAPL"}), (i:Issuer {name: "Apple Inc."})
CREATE (a)-[:ISSUED_BY]->(i);

MATCH (a:Equity {ticker: "AAPL"}), (m:Market {name: "NASDAQ"})
CREATE (a)-[:TRADED_ON]->(m);

// --- Microsoft (reuses NASDAQ; creates MSFT + its issuer once) ---
CREATE (b:Equity { ticker: "MSFT", name: "Microsoft Corporation Common Stock" });
CREATE (mi:Issuer { name: "Microsoft Corporation" });

MATCH (b:Equity {ticker: "MSFT"}), (mi:Issuer {name: "Microsoft Corporation"})
CREATE (b)-[:ISSUED_BY]->(mi);

MATCH (b:Equity {ticker: "MSFT"}), (m:Market {name: "NASDAQ"})
CREATE (b)-[:TRADED_ON]->(m);
