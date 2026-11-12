#!/bin/bash
# Testing checks in GitHub

# Stops the script at the first failing command
set -e

echo "Starting install ref stage ..."

# Try to list a non existing script
ls -lrt
echo "Install ref script finished!"
