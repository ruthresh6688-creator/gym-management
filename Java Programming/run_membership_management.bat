@echo off
title Gym Management System - Membership Management Module
cls
echo ============================================================
echo   GYM MEMBERSHIP MANAGEMENT SYSTEM
echo   MEMBERSHIP MANAGEMENT MODULE
echo ============================================================
echo.

set JAVA_CMD=java
where java >nul 2>nul
if %ERRORLEVEL% neq 0 (
    if exist "C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot\bin\java.exe" (
        set "JAVA_CMD=C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot\bin\java.exe"
    ) else if exist "C:\Program Files\Java\jdk-17\bin\java.exe" (
        set "JAVA_CMD=C:\Program Files\Java\jdk-17\bin\java.exe"
    )
)

echo [INFO] Executing MembershipManagementApp...
"%JAVA_CMD%" -cp "bin;lib/*;lib/sqlite-jdbc-3.45.1.0.jar;lib/mysql-connector-j-8.3.0.jar" com.gym.app.MembershipManagementApp
echo.
pause >nul
