. ./synthetic.config
cd $SYNTHEA_DIR
./run_synthea -p 10000  --exporter.baseDirectory="./output_univ_md/" Maryland "Baltimore" -d "./src/main/resources/modules/"
cd $SYNTHETIC_DATA_GENERATOR_DIR
python3 ConvertUnivMdEncounters.py
cd $SYNTHEA_RDF_DIR
python3 /knacc2_local/jclavin/synthea-rdf/conversion.py
cd $DEST_PATH
for x in encounter*.ttl; do
    mv -- "$x" "univ_md_to_hopkins_${x}"
done