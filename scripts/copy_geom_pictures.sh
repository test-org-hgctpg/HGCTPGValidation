#!/bin/bash
# Usage: ./copy_geom_pictures.sh PR$CHANGE_ID

# Check if there are 2 arguments supplied to the script
if (( $# != 1 ))
then
  echo "Usage: ./copy_geom_pictures.sh PR$CHANGE_ID"
  exit 1
fi

PRCHANGE_ID=$1

pwd

while [ ! test -f "../validation_data/${PRCHANGE_ID}/geomcheck/"] 
do
    sleep 300
    echo "Waiting for Display stage."
done

# Copy the pictures and the html page from GeomCheck stage
cp -rf ./HGCTPGGeometryTools/results/test_triggergeom/plot_errors_files ../validation_data/${PRCHANGE_ID}/geomcheck/
cp ./HGCTPGGeometryTools/results/test_triggergeom/plot_errors.html ../validation_data/${PRCHANGE_ID}/geomcheck/index.html
