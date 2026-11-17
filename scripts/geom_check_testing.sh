#!/bin/bash
# Testing checks in GitHub

# Stops the script at the first failing command
set -e

echo "Starting install stage ..."

# Try to list a non existing script
ls ./my_script.sh
echo "Install script finished!"
