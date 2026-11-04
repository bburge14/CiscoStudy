@echo off
REM ===================================================================
REM  Build a standalone CiscoStudy.exe on THIS Windows PC.
REM  You only need this if you want to produce the exe yourself; most
REM  people can just download the prebuilt exe from GitHub Actions.
REM  Output: dist\CiscoStudy.exe  (a single, self-contained executable)
REM ===================================================================
setlocal
title Build CiscoStudy.exe
cd /d "%~dp0"

where py >nul 2>&1
if %errorlevel%==0 (set "PY=py") else (set "PY=python")

%PY% --version >nul 2>&1
if not %errorlevel%==0 (
  echo [ERROR] Python 3.9+ is required to BUILD the exe.
  echo         Get it from https://www.python.org/downloads/ ^(tick "Add to PATH"^).
  pause
  exit /b 1
)

echo Installing build dependencies ^(this can take a minute^)...
%PY% -m pip install --upgrade pip
%PY% -m pip install -r packaging\requirements-build.txt
if not %errorlevel%==0 ( echo [ERROR] Dependency install failed. & pause & exit /b 1 )

echo Generating the question bank...
%PY% tools\build_content.py

echo Building CiscoStudy.exe with PyInstaller ^(a few minutes^)...
%PY% -m PyInstaller --noconfirm --clean CiscoStudy.spec
if not %errorlevel%==0 ( echo [ERROR] Build failed - see the output above. & pause & exit /b 1 )

echo.
echo ============================================================
echo  Done!  Your standalone app is here:
echo     %cd%\dist\CiscoStudy.exe
echo  Double-click it any time - no Python needed to RUN it.
echo ============================================================
pause
endlocal
