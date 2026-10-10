@echo off
cd /d "%~dp0"
echo Starting the detector. Keep this window open. Close it to stop.
start "" /b cmd /c "timeout /t 2 /nobreak >nul && start http://localhost:8000"
where python >nul 2>nul && (python -m http.server 8000) || (py -m http.server 8000)
pause
