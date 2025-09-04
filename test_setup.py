# TODO: add documentation

import os
import importlib

def test_imports():
    required_imports = [
        'dlt',
        'duckdb',
        'pandas',
        'numpy',
        'jupyter',
        'dotenv',
        'matplotlib',
        'seaborn'
    ]

    missing_imports = []

    for i in required_imports:
        try:
            importlib.import_module(i)
            print(f"Package {i} imported correctly")
        except ImportError as e:
            missing_imports.append(i)
            print(f"Failed to import package {i}: {e}")

    if missing_imports:
        print(f"Packages not imported: {' ,'.join(missing_imports)}")
        return False
    else:
        print(f"Required packages successfully imported")
        return True

def test_dlt_pipeline_creation():
    try:
        import dlt

        pipeline = dlt.pipeline(
            pipeline_name="test_pipeline",
            destination="duckdb",
            dataset_name="test_data"
        )

        print(f"Pipeline {pipeline.pipeline_name} created")
        print(f"Destination: {pipeline.destination}")
        print(f"Dataset name: {pipeline.dataset_name}")

        return True
    except Exception as e:
        print(f"dlt pipeline creation failed: {e}")
        return False

def test_duckdb_connection():
    try:
        import duckdb
        # No option passed as parameter --> in memory execution
        connection = duckdb.connect()
        result = connection.execute("SELECT 1 AS test_value").fetchdf()

        if result.iloc[0]['test_value'] == 1:
            print(f"duckdb basic query executed successfully")
        else:
            print(f"duckdb basic query failed")
            return False
        
        connection.close()

        return True
    except Exception as e:
        print(f"duckbd test failed: {e}")
        return False

def test_folders_structure():
    required_files = [
        'requirements.txt',
        'data/sample.csv',
        'notebooks/data_workflow.ipynb'
    ]

    required_folders = [
        'notebooks',
        'output'
    ]

    errors = False

    for file in required_files:
        if os.path.exists(file):
            print(f"File {file} found")
        else:
            print(f"File {file} not found")
            errors = True

    for folder in required_folders:
        if os.path.exists(folder):
            print(f"Folder {folder} found")
        else:
            print(f"Folder {folder} not found")
            errors = True

    return errors == False

def test_loading_sample_data():
    try:
        import pandas as pd

        df = pd.read_csv('data/sample.csv')

        print(f"Sample data loaded: {len(df)} records found")
        print(f"Columns: {list(df.columns)}")

        if len(df) > 0 and len(df.columns) >= 6:
            print("Everything seems ok")
            return True
        else:
            print("Data frame size or columns number is off")
            return False
    except Exception as e:
        print(f"Loading sample data failed: {e}")
        return False

def main():
    tests = [
        ("Packages import", test_imports),
        ("dlt Pipeline", test_dlt_pipeline_creation),
        ("DuckDB Connection", test_duckdb_connection),
        ("Folder structure", test_folders_structure),
        ("Sample data", test_loading_sample_data)
    ]

    results = []

    for test_name, function in tests:
        try:
            result = function()
            results.append((test_name, result))
        except Exception:
            results.append((test_name, False))

    passed = sum(True in result for result in results)
    total = len(results)

    for test_name, outcome in results:
        status = "Pass" if outcome else "Fail"
        print(f"{test_name}: {status}")

    if passed == total:
        print("All tests passed! Environment ready to use")
        return 0
    else:
        print(f"{total - passed} test(s) failed. Check environment setup")
        return 1

main()