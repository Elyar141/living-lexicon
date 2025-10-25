@echo off
REM Elshan's Living Lexicon - Vocabulary Enrichment Tool
REM Windows batch script for easy execution

echo ========================================
echo Elshan's Living Lexicon Enrichment Tool
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if API keys are set
if "%NOTION_API_KEY%"=="" (
    echo ERROR: NOTION_API_KEY environment variable not set
    echo.
    echo Set it with:
    echo   set NOTION_API_KEY=your-notion-key-here
    echo.
    pause
    exit /b 1
)

if "%ANTHROPIC_API_KEY%"=="" (
    echo ERROR: ANTHROPIC_API_KEY environment variable not set
    echo.
    echo Set it with:
    echo   set ANTHROPIC_API_KEY=your-anthropic-key-here
    echo.
    pause
    exit /b 1
)

REM Install dependencies if needed
echo Checking dependencies...
pip install -q -r requirements.txt

REM Run the enrichment script
echo.
echo Starting enrichment...
echo.
python vocab_enricher.py

echo.
echo ========================================
echo Press any key to exit...
pause >nul
