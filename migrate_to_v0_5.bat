@echo off
title Vietnam Adventure Publisher - Milestone 0.5 Migration

echo.
echo ============================================================
echo   Vietnam Adventure Publisher
echo   Milestone 0.5 Project Structure Migration
echo ============================================================
echo.

REM Change to the script directory
cd /d "%~dp0"

echo Creating folders...
if not exist "vap\reader" mkdir "vap\reader"
if not exist "vap\publisher" mkdir "vap\publisher"

echo.

echo Creating __init__.py files...
type nul > "vap\reader\__init__.py"

echo.

echo Creating model files...
if not exist "vap\models\document.py" type nul > "vap\models\document.py"
if not exist "vap\models\paragraph.py" type nul > "vap\models\paragraph.py"
if not exist "vap\models\table.py" type nul > "vap\models\table.py"
if not exist "vap\models\image.py" type nul > "vap\models\image.py"

echo.

echo Creating reader files...
if not exist "vap\reader\document_reader.py" type nul > "vap\reader\document_reader.py"

echo.

echo Creating parser files...
if not exist "vap\parser\component_detector.py" type nul > "vap\parser\component_detector.py"

echo.

echo Creating publisher files...
if not exist "vap\publisher\publisher.py" type nul > "vap\publisher\publisher.py"

echo.
echo ============================================================
echo Migration Complete!
echo ============================================================
echo.

echo New Structure:
echo.
tree vap /f

echo.
pause