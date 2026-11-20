@echo off
title Gym Management System - Generate SQL Reports (DBMS)
cls
echo ============================================================
echo   GYM MEMBERSHIP MANAGEMENT SYSTEM
echo   DBMS: SQL Queries, Joins, Aggregations, and Reports
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

echo [INFO] Executing SQL queries and generating reports...
"%PYTHON_CMD%" execute_sql.py reports

echo.
echo ============================================================
echo   Execution Complete! Report saved to outputs\sql_queries_output.txt
echo ============================================================
pause >nul
