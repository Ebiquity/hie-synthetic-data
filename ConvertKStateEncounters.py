from pathlib import Path
from synthea_rdf.graph import GraphBuilder
from configparser import ConfigParser
configure = ConfigParser()
configure.read('synthetic.config')

MODEL_PATH = configure.get('default', 'MODEL_PATH')
CSV_DIR = configure.get('default', 'CSV_DIR_K_STATE')
DEST_PATH = configure.get('default', 'DEST_PATH')

builder = GraphBuilder(CSV_DIR, MODEL_PATH)
builder.convertEncounter()
builder.serialize(destination=Path(DEST_PATH)/"k_state_to_ucsf_encounters.ttl")
