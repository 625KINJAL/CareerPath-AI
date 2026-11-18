
@echo off
cd /d "%~dp0"

echo Checking Python...
python --version
if errorlevel 1 (
    echo Python is not installed or not available in PATH.
    pause
    exit /b 1
)

if not exist "venv\Scripts\python.exe" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Installing required packages...
call venv\Scripts\python.exe -m pip install -r requirements.txt

echo Starting CareerPath AI...
call venv\Scripts\python.exe -m streamlit run app.py

pause

