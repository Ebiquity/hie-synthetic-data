from pathlib import Path
from configparser import ConfigParser
import yaml

configure = ConfigParser()
configure.read('synthetic.config')

MODEL_PATH = configure.get('default', 'MODEL_PATH')
CSV_DIR = configure.get('default', 'CSV_DIR_K_STATE')
DEST_PATH = configure.get('default', 'DEST_PATH')
SYNTHEA_RDF_DIR = configure.get('default', 'SYNTHEA_RDF_DIR')

default_chunk_size = 300000
default_include_dua = False
default_include_trustscore = False
default_skip = ["allergies.csv", 
  "careplans.csv", 
  "claims_transactions.csv", 
  "conditions.csv", 
  "devices.csv", 
  "encounters.csv", 
  "imaging_studies.csv", 
  "immunizations.csv", 
  "medications.csv", 
  "observations.csv", 
  "organizations.csv", 
  "patients.csv", 
  "patient_expenses.csv", 
  "payer_transitions.csv", 
  "payers.csv", 
  "procedures.csv",
  "providers.csv",
  "supplies.csv"]
default_do_shutdown = False

config_file = SYNTHEA_RDF_DIR + "/configuration.yaml"

with open(config_file, "r") as file:
    config = yaml.safe_load(file)

config["model_path"] = MODEL_PATH
config["synthea_csv_path"] = CSV_DIR
config["output_path"] = DEST_PATH
config["chunk_size"] = default_chunk_size
config["include_dua"] = default_include_dua
config["include_trustscore"] = default_include_trustscore
config["skip"] = default_skip
config["do_shutdown"] = default_do_shutdown

with open(config_file, 'w') as file:
    try:
        yaml.safe_dump(config, file, default_flow_style=False)
    except yaml.YAMLError as exc:
        print(exc)