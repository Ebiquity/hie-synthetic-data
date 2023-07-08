. ./synthetic.config
cd $SYNTHEA_DIR
./run_synthea -p 100000  --exporter.baseDirectory="./output_k_state/" Kansas  "Manhattan" -d "./src/main/resources/modules/"
cd $SYTHEA_RDF_DIR
python3 ConvertKStateEncounters.py
