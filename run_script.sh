#!/bin/bash
source /home/one-user/ime-ai/.venv/bin/activate
python /home/one-user/ime-ai/server_config.py
exec "$SHELL"