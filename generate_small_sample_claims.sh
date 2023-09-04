. ./synthetic.config
cd $SYNTHEA_DIR
./run_synthea -p 10000  --exporter.baseDirectory="./output_small_sample/" "North Carolina"  "Durham" -d "./src/main/resources/modules/"
cd $SYNTHETIC_DATA_GENERATOR_DIR
python3 ConvertSmallSampleClaims.py
cd $SYNTHEA_RDF_DIR
python3 /knacc2_local/jclavin/synthea-rdf/conversion.py
cd $DEST_PATH
for x in claim*.ttl; do
    mv -- "$x" "small_sample_${x}"
done