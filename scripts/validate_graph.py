import sys
from pyshacl import validate
from rdflib import Graph

def validate_ontology_graph(data_file: str, shapes_file: str) -> bool:
    print(f"Loading data graph from {data_file}...")
    data_graph = Graph()
    data_graph.parse(data_file, format="turtle")

    print(f"Loading SHACL shapes from {shapes_file}...")
    shapes_graph = Graph()
    shapes_graph.parse(shapes_file, format="turtle")

    print("Running SHACL validation...")
    conforms, results_graph, results_text = validate(
        data_graph,
        shacl_graph=shapes_graph,
        inference='rdfs',
        abort_on_first=False,
        meta_shacl=False,
        advanced=True,
        js=False
    )

    if conforms:
        print("SUCCESS: Graph validation passed.")
        return True
    else:
        print("FAILURE: Graph validation failed!")
        print(results_text)
        return False

if __name__ == "__main__":
    data_path = "ontology/finance-ontology.ttl"
    shapes_path = "validation/equity_shapes.ttl"
    
    is_valid = validate_ontology_graph(data_path, shapes_path)
    if not is_valid:
        sys.exit(1) # Block pipeline on failure
