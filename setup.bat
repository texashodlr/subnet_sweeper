@echo off
echo Setting up Python and dependencies...

REM Set project directory
set "PROJECT_DIR=%~dp0"

REM Extract portable Python
echo Extracting Python...
mkdir "%PROJECT_DIR%python_install"
powershell -Command "Expand-Archive -Path '%PROJECT_DIR%python\python-3.11.4-embed-amd64.zip' -DestinationPath '%PROJECT_DIR%python_install' -Force"

REM Set Python and Scripts paths
set "PYTHON_DIR=%PROJECT_DIR%python_install"
set "PYTHON=%PYTHON_DIR%\python.exe"
set "SCRIPTS_DIR=%PYTHON_DIR%\Scripts"
set "PIP=%SCRIPTS_DIR%\pip.exe"

REM Install pip
echo Installing pip...
"%PYTHON%" "%PROJECT_DIR%python\get-pip.py" --no-index

REM Install ping3
echo Installing ping3...
"%PIP%" install "%PROJECT_DIR%ping3_deps\ping3-4.0.8-py3-none-any.whl"

REM Run the script
echo Running subnet_sweep.py...
"%PYTHON%" "%PROJECT_DIR%subnet_sweep.py"

echo Done! Check concurrent_subnet_ping_results.csv for output.
pause
