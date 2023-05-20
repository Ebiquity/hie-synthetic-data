./run_synthea -p 100000  --exporter.baseDirectory="./output_hopkins/" Maryland "Baltimore" -d "./src/main/resources/modules/"
python3 /knacc2_local/jclavin/hie-synthetic-data/ConvertHopkinsEncounters.py
