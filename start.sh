#!/bin/bash

poetry shell
poetry install
python3 predownload.py
gunicorn -b 0.0.0.0:30001 -k uvicorn.workers.UvicornWorker --access-logfile ./gunicorn-access.log -w 3 main:app
