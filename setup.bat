@echo off
setlocal

:: Check if python exists
where python >nul 2>&1
if %errorlevel%==0 (
    echo ✅ Python detected.
) else (
    echo ❌ Python not found. Installing Python using winget...
    winget install -e --id Python.Python.3
    if %errorlevel% neq 0 (
        echo ❌ Python installation failed. Please install Python manually.
        exit /b 1
    )
)

:: Upgrade pip (optional but recommended)
python -m pip install --upgrade pip

:: Install the package
pip install .

if %errorlevel% neq 0 (
    echo ❌ Package installation failed.
    exit /b 1
)

:: Prompt user to uninstall Python if it was temporarily installed
set /p uninstall_python="Do you want to uninstall the temporarily installed Python? (y/n): "
if /i "%uninstall_python%"=="y" (
    echo Uninstalling Python...
    winget uninstall -e --id Python.Python.3
    if %errorlevel% neq 0 (
        echo ❌ Python uninstallation failed. You may need to uninstall manually.
    ) else (
        echo ✅ Python uninstalled.
    )
) else (
    echo Keeping Python installed.
)

echo Setup complete!
pause
