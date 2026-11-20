@echo off
title Gym Management System - Create Database and Tables (DBMS)
cls
echo ============================================================
echo   GYM MEMBERSHIP MANAGEMENT SYSTEM
echo   DBMS: Create Database, Schema Tables, and Constraints
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

echo [INFO] Running database creation script...
"%PYTHON_CMD%" execute_sql.py create

echo.
echo ============================================================
echo   Execution Complete! Press any key to exit.
echo ============================================================
pause >nul
