./run_synthea -p 1000  --exporter.baseDirectory="./output_duke/" "North Carolina"  "Durham" -d "./src/main/resources/modules/"
python3 /knacc2_local/jclavin/hie-synthetic-data/ConvertDukeEncounters.py