#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Run the Python script
python server_config.py

# Keep the shell open
exec "$SHELL"

# Get the function name from the first argument
function_name=$1

# Check if the function name is provided
if [ -z "$function_name" ]; then
    echo "Please provide a function name to run."
    exit 1
fi

# Call the function
$function_name
