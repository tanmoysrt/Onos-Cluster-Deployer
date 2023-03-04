#!/bin/bash

python3 -m venv venv
source ./venv/bin/activate
pip install -r requirement.txt

echo "Generating data"
python3 generate.py
echo "--Done generating---"
echo "Go to generated folder and run 'docker compose up' or 'docker-compose up'"