#!/bin/bash
virtualenv -p python3 corona-env
source corona-env/bin/activate
pip install -r requirements.txt
python corona.py
sleep 1
