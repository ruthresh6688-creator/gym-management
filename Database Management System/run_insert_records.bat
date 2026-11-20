@echo off
title Gym Management System - Insert Sample Records (DBMS)
cls
echo ============================================================
echo   GYM MEMBERSHIP MANAGEMENT SYSTEM
echo   DBMS: Insert Sample Database Records
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

echo [INFO] Inserting sample records into database...
"%PYTHON_CMD%" execute_sql.py insert

echo.
echo ============================================================
echo   Execution Complete! Press any key to exit.
echo ============================================================
pause >nul
