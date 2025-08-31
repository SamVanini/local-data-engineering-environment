@ECHO OFF
REM Check if python is installed
REM The command is used to check if Python is installed and available in the system's environment without displaying any output.
REM Standard output and error are redirected to null

ECHO Checking Python version...
python --version >nul 2>&1

REM EXIT /b 1 terminates the current batch script or subroutine without closing the parent command prompt session
if ERRORLEVEL 1 (
    ECHO Python 3.9 or higher required.
    PAUSE
    EXIT /b 1
)

ECHO Python detected

REM Create python local environment
ECHO Creating local virtual environment...
python -m venv env

REM Activate local pyton env
ECHO Activating local virtual environment...
CALL env\Scripts\activate.bat

REM Install and upgrade pip
ECHO Installing and upgrading pip
python -m pip install --upgrade pip

REM Install packages contained in requirements.txt
ECHO Installing dependencies...
pip install -r requirements.txt

REM Create output dir
ECHO Creating output directory...
IF NOT EXIST output MKDIR output

REM Create env file if not available
IF NOT EXIST .env (
    ECHO Creating .env file...
    (
        ECHO # Environment variables for local data engineering environment
        ECHO PIPELINE_NAME=local_data
        ECHO DATASET_NAME=my_data
        ECHO DATA_DIR=./data
        ECHO OUTPUT_DIR=./output
        ECHO.
        ECHO # Jupyter configuration
        ECHO JUPYTER_ENABLE_LAB=yes
        ECHO JUPYTER_TOKEN=your_token_here
    ) > .env
    ECHO .env file created
)

PAUSE