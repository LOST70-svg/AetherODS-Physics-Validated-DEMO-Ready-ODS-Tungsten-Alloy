#!/bin/bash
# Run FISPACT-II activation calculation for DP-ODS

if [ $# -lt 2 ]; then
  echo "Usage: $0 <input_file> <output_file>"
  exit 1
fi

INPUT=$1
OUTPUT=$2

# Check for FISPACT installation
if ! command -v fispact &> /dev/null; then
  echo "Error: FISPACT-II not found in PATH."
  exit 1
fi

echo "Running FISPACT-II with input $INPUT ..."
fispact -i $INPUT -o $OUTPUT -v DP_ODS

echo "Done. Results written to $OUTPUT"
