./run_synthea -p 10000  --exporter.baseDirectory="./output_k_state/" Kansas  "Manhattan" -d "./src/main/resources/modules/"
python3 /knacc2_local/jclavin/hie-synthetic-data/ConvertKStateEncounters.py
