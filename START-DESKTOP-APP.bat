@echo off
title MECA DRONE - Desktop Application
color 0A

echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                🚁 MECA DRONE GCS                           ║
echo  ║            DESKTOP APPLICATION                               ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
echo  📁 Project Structure:
echo     • frontend/ - Desktop Application (Python/Tkinter)
echo     • backend/  - Rust Services (Tauri)
echo     • ai/       - AI Person Detection (Coming Soon)
echo.
echo  🚀 Launching MECA DRONE Desktop Application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo  ❌ Python not found! Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if frontend exists
if not exist "frontend\meca-drone.py" (
    echo  ❌ Desktop application not found in frontend folder!
    pause
    exit /b 1
)

echo  ✅ Python found
echo  ✅ Desktop application found
echo  🚀 Starting MECA DRONE Ground Control Station...
echo.

REM Change to frontend directory and launch
cd frontend
python meca-drone.py

echo.
echo  ✅ Desktop application closed!
echo.
echo  📋 Project Structure Ready:
echo     • Frontend: Desktop application ✅
echo     • Backend: Rust services ready 🔄
echo     • AI: Person detection pending ⏳
echo.

pause
