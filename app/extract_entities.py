import json
import re
from ollama import chat
import rdflib

def extract_entities(text_chunk: str):
    prompt = f"""
    You are an expert financial data extractor.
    Extract the Company name, the Metric, the Value, and the TimePeriod from the text below.
    
    Return a JSON array of objects with keys: "company", "metric", "value", "time_period".
    Do not include markdown formatting or extra text.
    
    Text: "{text_chunk}"
    """
    
    response = chat(
        model='qwen2.5:3b',
        messages=[{'role': 'user', 'content': prompt}],
        format='json' 
    )
    
    try:
        data = json.loads(response.message.content)
        return data
    except json.JSONDecodeError:
        print("❌ LLM failed to output valid JSON.")
        return []

def json_to_rdf(extracted_data):
    g = rdflib.Graph()
    FIN = rdflib.Namespace("https://froilan-sia.github.io/finance-ontology-rag/ontology#")
    g.bind("fin", FIN)
    g.bind("rdfs", rdflib.RDFS)
    
    if isinstance(extracted_data, dict):
        extracted_data = [extracted_data]
        
    for item in extracted_data:
        company = item.get("company")
        metric_name = item.get("metric")
        value = item.get("value")
        time_period = item.get("time_period")
        
        if not company:
            continue
            
        clean_company = re.sub(r'[^a-zA-Z0-9]', '', company)
        company_uri = FIN[clean_company]
        
        g.add((company_uri, rdflib.RDF.type, FIN.Issuer))
        g.add((company_uri, rdflib.RDFS.label, rdflib.Literal(company)))
        
        if metric_name:
            suffix = f"{metric_name}{time_period or ''}"
            clean_metric = re.sub(r'[^a-zA-Z0-9]', '', suffix)
            metric_uri = FIN[clean_metric]
            
            display_label = f"{metric_name} ({time_period})" if time_period else metric_name
            
            g.add((metric_uri, rdflib.RDF.type, FIN.Metric))
            g.add((metric_uri, rdflib.RDFS.label, rdflib.Literal(display_label)))
            
            # Map the actual 'value' (e.g. "10 billion") to hasValue
            if value:
                g.add((metric_uri, FIN.hasValue, rdflib.Literal(value)))
            
            g.add((company_uri, FIN.reportsMetric, metric_uri))
        
    return g.serialize(format="turtle")

# ==========================================
# EXECUTION BLOCK (This was missing!)
# ==========================================
if __name__ == "__main__":
    pdf_text = "Apple Inc. reported a Q3 revenue of 10 billion."
    
    print("Extracting entities...")
    extracted = extract_entities(pdf_text)
    print("Extracted JSON:", extracted)
    
    print("\nGenerating RDF Triples...")
    turtle_output = json_to_rdf(extracted)
    
    # Save to file for CI/CD validation
    import os
    os.makedirs("data", exist_ok=True)
    with open("data/extracted_instances.ttl", "w") as f:
        f.write(turtle_output)
        
    print("✅ Saved to data/extracted_instances.ttl")
    print("\n--- Generated Turtle ---")
    print(turtle_output)
