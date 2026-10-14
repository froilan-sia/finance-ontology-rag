# Competency Questions

These are the acceptance criteria for the finance ontology. Every class and property must trace back to at least one question.

## Core Questions

- **Q1.** Which equities trade on NASDAQ?
- **Q2.** Who issues a given financial instrument?
- **Q3.** What transactions has a given investor made?
- **Q4.** What instruments does a given account hold?
- **Q5.** What is the total value of transactions per currency?

## Traceability

| Question | Classes Required | Properties Required |
|----------|-----------------|-------------------|
| Q1 | Equity, Market | tradedOn, rdfs:label |
| Q2 | FinancialInstrument, Issuer | issuedBy |
| Q3 | Investor, Account, Transaction | hasAccount, hasTransaction |
| Q4 | Account, FinancialInstrument | hasTransaction, involvesInstrument |
| Q5 | Transaction | hasAmount, hasCurrency |
