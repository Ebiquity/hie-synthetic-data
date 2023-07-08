. ./synthetic.config
cd $SYNTHEA_DIR
./run_synthea -p 100  --exporter.baseDirectory="./output_small_sample/" "North Carolina"  "Durham" -d "./src/main/resources/modules/"
cd $SYTHEA_RDF_DIR
python3 ConvertSmallSampleEncounters.py
