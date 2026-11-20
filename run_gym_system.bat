@echo off
title Gym Management System - Master Application
cls
set JAVA_CMD=java
where java >nul 2>nul
if %ERRORLEVEL% neq 0 (
    if exist "C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot\bin\java.exe" (
        set "JAVA_CMD=C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot\bin\java.exe"
    ) else if exist "C:\Program Files\Java\jdk-17\bin\java.exe" (
        set "JAVA_CMD=C:\Program Files\Java\jdk-17\bin\java.exe"
    )
)

"%JAVA_CMD%" -cp "Java Programming\bin;Java Programming\lib\*" com.gym.app.GymApp
pause >nul
