import chromadb
import os

def setup_db():
    print("Initializing local ChromaDB for the finance ontology...")
    
    # Creates a persistent database locally in the project folder
    client = chromadb.PersistentClient(path="./chroma_db")
    
    # We use a specific collection name for this project
    collection = client.get_or_create_collection(name="finance_docs")
    
    # Sample narrative chunks (simulating PDFs or news articles)
    documents = [
        "Apple Inc. is a leading technology company. Its common stock is actively traded on the NASDAQ exchange.",
        "NASDAQ is an American stock exchange based in New York City. Many of the world's largest tech companies are listed there.",
        "Alice is a retail investor who recently opened a brokerage account to purchase shares of major technology companies.",
        "During the Q3 earnings call, Apple's CFO noted that hardware revenue was down slightly, but services revenue hit an all-time high."
    ]
    
    ids = ["doc1", "doc2", "doc3", "doc4"]
    
    # Add to the database
    collection.add(
        documents=documents,
        ids=ids
    )
    
    print(f"✅ Successfully added {len(documents)} documents to the 'finance_docs' collection.")

if __name__ == "__main__":
    setup_db()
