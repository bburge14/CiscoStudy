@echo off
REM ===================================================================
REM  CertWize launcher (Windows)
REM  Double-click this file to start the study platform in your browser.
REM  Right-click -> Send to -> Desktop (create shortcut) for a desktop icon.
REM ===================================================================
setlocal
title CertWize
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

echo Preparing CertWize...
REM (Re)generate the question bank from the authored source (quietly).
%PY% tools\build_content.py >nul 2>&1

REM Install runtime dependencies on first run (harmless if already present).
%PY% -m pip install -q -r requirements.txt

REM Skip Streamlit's first-run "Email:" onboarding prompt (seed empty credentials).
if not exist "%USERPROFILE%\.streamlit" mkdir "%USERPROFILE%\.streamlit"
if not exist "%USERPROFILE%\.streamlit\credentials.toml" (
  >"%USERPROFILE%\.streamlit\credentials.toml" echo [general]
  >>"%USERPROFILE%\.streamlit\credentials.toml" echo email = ""
)

echo.
echo Starting CertWize at http://localhost:8501
echo (A browser tab should open automatically. Press Ctrl+C here to stop.)
echo.
%PY% -m streamlit run Home.py %*

echo.
echo CertWize has stopped.
pause
endlocal
