#!/bin/bash

pip install -r requirements.txt
python3 predownload.py
gunicorn -b 0.0.0.0:30001 -k uvicorn.workers.UvicornWorker -w 3 main:app