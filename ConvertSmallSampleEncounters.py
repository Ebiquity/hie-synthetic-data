from pathlib import Path
from synthea_rdf.graph import GraphBuilder
from configparser import ConfigParser
configure = ConfigParser()
configure.read('synthetic.config')

MODEL_PATH = configure.get('default', 'MODEL_PATH')
CSV_DIR = configure.get('default', 'CSV_DIR_SMALL_SAMPLE')
DEST_PATH = configure.get('default', 'DEST_PATH')

builder = GraphBuilder(CSV_DIR, MODEL_PATH)
builder.convertEncounter()
builder.serialize(destination=Path(DEST_PATH)/"small_sample_encounters.ttl")
