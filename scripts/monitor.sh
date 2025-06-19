#!/bin/bash
echo "Running monitor.sh script..."
cd "$(dirname "$0")"/../backend || { echo "Failed to cd to backend"; exit 1; }
echo "Current directory: $(pwd)"

# Run the Python script and capture its output
output=$(python monitor.py)

# Display the output from monitor.py
echo "$output"

echo "monitor.py finished and results saved to db.json"
