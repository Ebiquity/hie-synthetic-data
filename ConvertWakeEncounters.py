from pathlib import Path
from synthea_rdf.graph import GraphBuilder

MODEL_PATH = "/knacc2_local/jclavin/synthea-rdf/synthea_ontology/synthea_ontology.ttl"
CSV_DIR = "/knacc2_local/synthea/output_wake_forest/csv"
DEST_PATH = "/knacc2_local/jclavin/hie/apps/hie/priv/data"

builder = GraphBuilder(CSV_DIR, MODEL_PATH)
builder.convertEncounter()
builder.serialize(destination=Path(DEST_PATH)/"wake_to_duke_encounter.ttl")
