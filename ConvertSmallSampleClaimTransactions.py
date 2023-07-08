from pathlib import Path
from synthea_rdf.graph import GraphBuilder

MODEL_PATH = "/knacc2_local/jclavin/synthea-rdf/synthea_ontology/synthea_ontology.ttl"
CSV_DIR = "/knacc2_local/synthea/output_small_sample/csv"
DEST_PATH = "/knacc2_local/jclavin/hie/apps/hie/priv/data"

builder = GraphBuilder(CSV_DIR, MODEL_PATH)
builder.convertClaimTransaction()
builder.serialize(destination=Path(DEST_PATH)/"small_sample_claim_transactions.ttl")
