@echo off
REM ===================================================================
REM  CiscoStudy launcher (Windows)
REM  Double-click this file to start the study platform in your browser.
REM  Right-click -> Send to -> Desktop (create shortcut) for a desktop icon.
REM ===================================================================
setlocal
title CiscoStudy
cd /d "%~dp0"

REM Prefer the Windows "py" launcher, fall back to "python".
where py >nul 2>&1
if %errorlevel%==0 (set "PY=py") else (set "PY=python")

REM Verify Python is available.
%PY% --version >nul 2>&1
if not %errorlevel%==0 (
  echo [ERROR] Python was not found on your PATH.
  echo         Install Python 3.9+ from https://www.python.org/downloads/
  echo         and tick "Add python.exe to PATH" during setup.
  echo.
  pause
  exit /b 1
)

echo Preparing CiscoStudy...
REM (Re)generate the question bank from the authored source (quietly).
%PY% tools\build_content.py >nul 2>&1

REM Install runtime dependencies on first run (harmless if already present).
%PY% -m pip install -q -r requirements.txt

echo.
echo Starting CiscoStudy at http://localhost:8501
echo (A browser tab should open automatically. Press Ctrl+C here to stop.)
echo.
%PY% -m streamlit run app.py %*

echo.
echo CiscoStudy has stopped.
pause
endlocal
