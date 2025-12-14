#!/bin/bash

# Check if a string argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 \"string to convert\""
    echo "Example: $0 \"29. Divide Two Integers II\""
    exit 1
fi

input_string="$(echo "$*" | xargs)"

digits=$(echo "$input_string" | grep -o '^[0-9]\{1,4\}')
if [ -z "$digits" ]; then
    echo "Error: String must start with 1-4 digits"
    exit 1
fi
padded_digits=$(printf "%04d" "$digits")

# Remove the digits and the dot from the beginning
remaining_string=$(echo "$input_string" | sed "s/^[0-9]\{1,4\}\. *//" )

remaining_string=$(echo "$remaining_string" | tr '[:upper:]' '[:lower:]')
remaining_string=$(echo "$remaining_string" | sed 's/[^a-z0-9]/_/g')
remaining_string=$(echo "$remaining_string" | sed 's/_*$//')

project_root="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -z "$project_root" ]; then
    echo "Error: Not in a git repository or git not available"
    exit 1
fi

solutions_dir="$project_root/solutions"
if [ ! -d "$solutions_dir" ]; then
    echo "Error: Could not find solutions directory at $solutions_dir"
    exit 1
fi

filename="$solutions_dir/lc_${padded_digits}_${remaining_string}.py"
touch "$filename"
echo "Created file: $filename"