. ./synthetic.config
cd $SYNTHEA_DIR
./run_synthea -p 10  --exporter.baseDirectory="./output_ucsf/" California  "San Francisco" -d "./src/main/resources/modules/"
cd $SYTHEA_RDF_DIR
python3 ConvertUCSFClaimTransactions.py
