from pathlib import Path
from synthea_rdf.graph import GraphBuilder
from configparser import ConfigParser
configure = ConfigParser()
configure.read('synthetic.config')

MODEL_PATH = configure.get('default', 'MODEL_PATH')
CSV_DIR = configure.get('default', 'CSV_DIR_DUKE')
DEST_PATH = configure.get('default', 'DEST_PATH')

builder = GraphBuilder(CSV_DIR, MODEL_PATH)
builder.convertClaimTransaction()
builder.serialize(destination=Path(DEST_PATH)/"duke_to_wake_claim_transactions.ttl")
