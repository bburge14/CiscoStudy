@echo off
REM ===================================================================
REM  Run CertLab and share it on your LOCAL NETWORK so other people
REM  (on the same Wi-Fi / LAN) can use it from their own devices.
REM  Each person picks or creates their own profile in the sidebar, so
REM  everyone's progress is tracked separately on THIS machine.
REM ===================================================================
setlocal
title CertLab (shared on your network)
cd /d "%~dp0"

where py >nul 2>&1
if %errorlevel%==0 (set "PY=py") else (set "PY=python")

%PY% --version >nul 2>&1
if not %errorlevel%==0 (
  echo [ERROR] Python 3.9+ not found on PATH. Install from https://www.python.org/downloads/
  pause
  exit /b 1
)

REM Seed empty Streamlit credentials so the first-run "Email:" prompt is skipped.
if not exist "%USERPROFILE%\.streamlit" mkdir "%USERPROFILE%\.streamlit"
if not exist "%USERPROFILE%\.streamlit\credentials.toml" (
  >"%USERPROFILE%\.streamlit\credentials.toml" echo [general]
  >>"%USERPROFILE%\.streamlit\credentials.toml" echo email = ""
)

%PY% -m pip install -q -r requirements.txt

echo.
echo  Serving CertLab on 0.0.0.0:8501 (LAN). Local: http://localhost:8501
echo  Ctrl+C to stop.
echo.
%PY% -m streamlit run Home.py --server.address 0.0.0.0 --server.port 8501 --server.headless true

pause
endlocal
