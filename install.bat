@echo off
echo ===============================
echo FolderTree.Parser - Installation
echo ===============================

python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo [!] Python not found
    echo Please install Python 3.9+ and add it to PATH
    pause
    exit /b
)

echo [OK] Python found
pip install -r requirements.txt

echo.
echo [OK] Installation completed
pause
