./run_synthea -p 10  --exporter.baseDirectory="./output_small_sample/" "North Carolina"  "Durham" -d "./src/main/resources/modules/"
python3 /knacc2_local/jclavin/hie-synthetic-data/ConvertSmallSample.py
