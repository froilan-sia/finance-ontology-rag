// ============================================================
// Neo4j Schema: constraints and indexes for the finance ontology
// Companion to Article 5: Protegé vs. GraphDB vs. Neo4j
// ============================================================

// Uniqueness and node-key constraints (Neo4j 5+)
// These enforce structural integrity at write time.
CREATE CONSTRAINT equity_ticker_unique IF NOT EXISTS
FOR (e:Equity) REQUIRE e.ticker IS UNIQUE;

CREATE CONSTRAINT issuer_name_unique IF NOT EXISTS
FOR (i:Issuer) REQUIRE i.name IS UNIQUE;

CREATE CONSTRAINT market_name_unique IF NOT EXISTS
FOR (m:Market) REQUIRE m.name IS UNIQUE;

// Property existence: every Equity must carry a ticker and a name
//CREATE CONSTRAINT equity_ticker_exists IF NOT EXISTS
//FOR (e:Equity) REQUIRE e.ticker IS NOT NULL;

//CREATE CONSTRAINT equity_name_exists IF NOT EXISTS
//FOR (e:Equity) REQUIRE e.name IS NOT NULL;

// Indexes to support the traversal patterns in our competency questions
CREATE INDEX equity_name_idx IF NOT EXISTS FOR (e:Equity) ON (e.name);
CREATE INDEX market_name_idx IF NOT EXISTS FOR (m:Market) ON (m.name);
