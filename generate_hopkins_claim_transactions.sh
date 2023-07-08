. ./synthetic.config
cd $SYNTHEA_DIR
./run_synthea -p 10  --exporter.baseDirectory="./output_hopkins/" Maryland "Baltimore" -d "./src/main/resources/modules/"
cd $SYTHEA_RDF_DIR
python3 ConvertHopkinsClaimTransactions.py
