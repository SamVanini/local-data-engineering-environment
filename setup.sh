#!/bin/bash

# Check if python is installed
# The command is used to check if Python is installed and available in the system's environment without displaying any output.
# Standard output and error are redirected to null

echo "Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "Python 3.9 or higher required."
    exit 1
fi

python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.9"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "Python version $python_version is less than required version $required_version"
    exit 1
fi

echo "Python detected"

# Create python local environment
echo "Creating local virtual environment..."
python3 -m venv env

# Activate local pyton env
echo "Activating local virtual environment..."
source env/bin/activate

# Install and upgrade pip
echo "Installing and upgrading pip"
pip install --upgrade pip

# Install packages contained in requi#ents.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Create output dir
echo Creating output directory...
mkdir -p output

# Create env file if not available
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cat > .env << EOF
# Environment variables for local data engineering environment
PIPELINE_NAME=local_data
DATASET_NAME=my_data
DATA_DIR=./data
OUTPUT_DIR=./output

# Jupyter configuration
JUPYTER_ENABLE_LAB=yes
JUPYTER_TOKEN=your_token_here
EOF
    echo ".env file created"
fi