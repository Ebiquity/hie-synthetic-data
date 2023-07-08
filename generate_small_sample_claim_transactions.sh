./run_synthea -p 1000  --exporter.baseDirectory="./output_small_sample/" "North Carolina"  "Durham" -d "./src/main/resources/modules/"
python3 /knacc2_local/jclavin/hie-synthetic-data/ConvertSmallSampleClaimTransactions.py
