// ============================================================
// Seed data: the same Apple/NASDAQ fact from Article 1,
// modelled as a Labeled Property Graph.
// ============================================================

// Clean slate (safe for a local dev instance only)
MATCH (n) DETACH DELETE n;

// Nodes
CREATE (a:Equity {
    ticker: "AAPL",
    name: "Apple Inc. Common Stock"
});

CREATE (i:Issuer {
    name: "Apple Inc."
});

CREATE (m:Market {
    name: "NASDAQ"
});

// Relationships (edges with a type, no properties in this case)
MATCH (a:Equity {ticker: "AAPL"}), (i:Issuer {name: "Apple Inc."})
CREATE (a)-[:ISSUED_BY]->(i);

MATCH (a:Equity {ticker: "AAPL"}), (m:Market {name: "NASDAQ"})
CREATE (a)-[:TRADED_ON]->(m);

// Optional: a second instrument so queries have more than one row to
// reason about. Comment out if you want the minimal example.
CREATE (b:Equity {
    ticker: "MSFT",
    name: "Microsoft Corporation Common Stock"
});
CREATE (mi:Issuer { name: "Microsoft Corporation" });
CREATE (nm:Market { name: "NASDAQ" });
MATCH (b:Equity {ticker: "MSFT"}), (mi:Issuer {name: "Microsoft Corporation"})
CREATE (b)-[:ISSUED_BY]->(mi);
MATCH (b:Equity {ticker: "MSFT"}), (nm:Market {name: "NASDAQ"})
CREATE (b)-[:TRADED_ON]->(nm);
