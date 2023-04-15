./run_synthea -p 10000  --exporter.baseDirectory="./output_wake_forest/" "North Carolina" "Winston-Salem" -d "./src/main/resources/modules/"
python3 /knacc2_local/jclavin/hie-synthetic-data/ConvertWakeEncounters.py
