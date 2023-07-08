. ./synthetic.config
cd $SYNTHEA_DIR
./run_synthea -p 10  --exporter.baseDirectory="./output_small_sample/" "North Carolina"  "Durham" -d "./src/main/resources/modules/"
cd $SYTHEA_RDF_DIR
python3 ConvertSmallSampleClaimTransactions.py
