@echo off
setlocal EnableDelayedExpansion
title Vietnam Adventure Publisher - Project Verification

color 0A

echo.
echo ===============================================================
echo          Vietnam Adventure Publisher
echo                 Project Verification
echo ===============================================================
echo.

REM -----------------------------------------------------------------
REM Project Root
REM -----------------------------------------------------------------

cd /d "%~dp0"

echo [INFO] Project Root:
echo        %CD%
echo.

REM -----------------------------------------------------------------
REM Python
REM -----------------------------------------------------------------

echo [CHECK] Python Installation...

python --version >nul 2>&1

if errorlevel 1 (
    color 0C
    echo.
    echo [FAILED] Python is not installed or not in PATH.
    goto END
)

python --version

echo.

REM -----------------------------------------------------------------
REM Virtual Environment
REM -----------------------------------------------------------------

echo [CHECK] Virtual Environment...

if defined VIRTUAL_ENV (
    echo [PASS] Active
    echo        %VIRTUAL_ENV%
) else (
    echo [WARNING] No virtual environment detected.
)

echo.

REM -----------------------------------------------------------------
REM Required Packages
REM -----------------------------------------------------------------

echo [CHECK] Required Packages...

python -c "import docx" >nul 2>&1

if errorlevel 1 (
    color 0C
    echo [FAILED] python-docx is NOT installed.
    echo.
    echo Install using:
    echo     pip install python-docx
    goto END
)

echo [PASS] python-docx

python -c "import lxml" >nul 2>&1

if errorlevel 1 (
    echo [WARNING] lxml not installed.
) else (
    echo [PASS] lxml
)

echo.

REM -----------------------------------------------------------------
REM Handbook
REM -----------------------------------------------------------------

echo [CHECK] Handbook...

set HANDBOOK=handbook\source\Vietnam Adventure 2026 Handbook.docx

if exist "%HANDBOOK%" (
    echo [PASS] Found
    echo        %HANDBOOK%
) else (
    color 0C
    echo [FAILED] Handbook not found.
    goto END
)

echo.

REM -----------------------------------------------------------------
REM Required Files
REM -----------------------------------------------------------------

echo [CHECK] Required Modules...

set FILECOUNT=0

call :CHECKFILE vap\main.py
call :CHECKFILE vap\models\chapter.py
call :CHECKFILE vap\models\handbook.py
call :CHECKFILE vap\models\document.py
call :CHECKFILE vap\models\paragraph.py
call :CHECKFILE vap\models\table.py
call :CHECKFILE vap\models\image.py
call :CHECKFILE vap\reader\document_reader.py
call :CHECKFILE vap\parser\chapter_detector.py
call :CHECKFILE vap\parser\component_detector.py

echo.
echo Modules Verified: %FILECOUNT%
echo.

REM -----------------------------------------------------------------
REM Tree
REM -----------------------------------------------------------------

echo ===============================================================
echo Project Structure
echo ===============================================================

tree vap /f

echo.

REM -----------------------------------------------------------------
REM Run
REM -----------------------------------------------------------------

echo ===============================================================
echo Launching Application...
echo ===============================================================
echo.

python -m vap.main

goto END

REM ================================================================
REM Functions
REM ================================================================

:CHECKFILE

if exist "%~1" (
    echo [PASS] %~1
    set /a FILECOUNT+=1
) else (
    color 0E
    echo [MISSING] %~1
)

exit /b

:END

echo.
echo ===============================================================
echo Verification Finished
echo ===============================================================
echo.

pause