@echo off
title Gym Management - Attendance Trends and Participation Analysis
cls
echo ============================================================
echo   FOUNDATION OF DATA SCIENCE - ATTENDANCE ANALYSIS
echo ============================================================
echo.

set PYTHON_CMD=python
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
        set "PYTHON_CMD=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
    ) else if exist "C:\Program Files\Python312\python.exe" (
        set "PYTHON_CMD=C:\Program Files\Python312\python.exe"
    )
)

echo [INFO] Running Attendance Analysis script...
"%PYTHON_CMD%" attendance_analysis.py

echo.
echo ============================================================
echo   Execution Finished! Output saved to outputs\attendance_analysis_output.txt
echo   Charts generated in visualizations\ folder.
echo ============================================================
pause >nul
