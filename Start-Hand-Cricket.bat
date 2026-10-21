@echo off
cd /d "%~dp0"
start "Hand Cricket" http://localhost:8000/handcricket.html
where py >nul 2>nul
if %errorlevel%==0 (
  py -m http.server 8000
) else (
  python -m http.server 8000
)
