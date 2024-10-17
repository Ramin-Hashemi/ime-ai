#!/bin/bash

# Activate the virtual environment
source /home/webapps/ime-ai/.venv/bin/activate

# Run the Python script
python server_config.py "$1"

# Keep the shell open
exec "$SHELL"