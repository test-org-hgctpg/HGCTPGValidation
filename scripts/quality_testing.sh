#!/bin/bash
# Testing checks in GitHub

# Stops the script at the first failing command
set -e

echo "Starting quality testing stage ..."

# Try to list a non existing script
#ls ./my_script.sh
echo "Quality testing script finished!"
