#!/bin/bash

# Create venv
python3 -m venv venv
source venv/bin/activate

# Install app
pip3 install --no-cache-dir  -e .

# Variables
export FLASK_ENV=development
export GUNICORN_RELOAD=True
export FLASK_APP=app
export API_TOKEN=token

flask run

# Remove virtualenv
deactivate
rm -rf venv
