./run_synthea -p 10000  --exporter.baseDirectory="./output_ucsf/" California  "San Francisco" -d "./src/main/resources/modules/"
python3 /knacc2_local/jclavin/hie-synthetic-data/ConvertUCSFEncounters.py
