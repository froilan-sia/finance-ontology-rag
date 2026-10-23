import rdflib
import chromadb
from ollama import chat

# ==========================================
# 1. SETUP CONNECTIONS
# ==========================================
print("Loading ontology...")
graph = rdflib.Graph()
graph.parse("ontology/finance-ontology.ttl", format="turtle")

print("Connecting to local ChromaDB...")
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection(name="finance_docs")

# ==========================================
# 2. THE TWO RETRIEVAL BRANCHES
# ==========================================

def query_graph_branch():
    """Deterministic retrieval using SPARQL."""
    sparql_query = """
    PREFIX : <https://froilan-sia.github.io/finance-ontology-rag/ontology#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    
    SELECT ?equity ?name ?issuer WHERE {
        ?equity a :Equity ;
                :tradedOn :NASDAQ ;
                :issuedBy ?issuer ;
                rdfs:label ?name .
    }
    """
    results = graph.query(sparql_query)
    facts = []
    for row in results:
        facts.append(f"Fact: {row.name} is an Equity issued by {row.issuer} and trades on NASDAQ.")
    return "\n".join(facts) if facts else "No graph facts found."

def query_vector_branch(user_query: str):
    """Semantic retrieval using ChromaDB."""
    results = collection.query(
        query_texts=[user_query],
        n_results=2
    )
    return "\n\n".join(results['documents'][0])

# ==========================================
# 3. THE FUSION & GENERATION LAYER
# ==========================================

def ask_dual_branch_rag(user_query: str):
    print(f"\nUser Query: {user_query}")
    print("-" * 50)
    
    graph_facts = query_graph_branch()
    vector_context = query_vector_branch(user_query)
    
    # Construct the Guardrailed Prompt
    prompt = f"""
    You are an enterprise financial AI assistant.
    
    CRITICAL INSTRUCTION: 
    - Use the [STRUCTURED GRAPH FACTS] as the absolute source of truth for entities and relationships. 
    - Use the [NARRATIVE CONTEXT] only for background color and explanation.
    
    [STRUCTURED GRAPH FACTS]
    {graph_facts}
    
    [NARRATIVE CONTEXT]
    {vector_context}
    
    User Question: {user_query}
    """
    
    print("Sending fused prompt to Ollama (qwen2.5:3b)...")
    response = chat(
        model='qwen2.5:3b',
        messages=[{'role': 'user', 'content': prompt}]
    )
    
    return response.message.content

# ==========================================
# 4. EXECUTION
# ==========================================
if __name__ == "__main__":
    question = "Tell me about Apple's stock, where it trades, and who invests in it."
    answer = ask_dual_branch_rag(question)
    
    print("\n" + "="*50)
    print("FINAL GROUNDED ANSWER:")
    print("="*50)
    print(answer)
