# Project: Local Data Engineering Environment with dlt, DuckDB & Jupyter

Project taken from dataskew.io

## Project Overview

Create a complete local data engineering environment using modern open-source tools for data processing, transformation, and analytics. The environment should be self-contained, reproducible, and suitable for learning, prototyping, and personal data projects.

## Project Structure

```
local-data-engineering-environment/
├── notebooks/
│   └── data_workflow.ipynb          # Main workflow notebook
├── data/
│   └── sample.csv                   # Sample dataset
├── env/                             # Virtual environment (created)
├── output/                          # Generated outputs (created)
├── requirements.txt                 # Python dependencies
├── setup.sh                         # Linux/Mac setup script
├── setup.bat                        # Windows setup script
├── test_setup.py                    # Validation script
├── .env                             # Environment variables (optional)
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

## How to run the project

### Project Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd local-data-engineering-environment

# Run the automated setup script
./setup.sh  # Linux/Mac
# OR
setup.bat   # Windows
```

### Launch Jupyter

```bash
# Activate virtual environment
source env/bin/activate  # Linux/Mac
# OR
env\Scripts\activate.bat  # Windows

# Start Jupyter notebook
jupyter notebook
```

### Run the Workflow

Open and execute `notebooks/data_workflow.ipynb`
