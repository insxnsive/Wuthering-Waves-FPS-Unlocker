@echo off
setlocal enabledelayedexpansion

set wantedfps=120

if not exist ".\sqlite3.exe" (
    powershell.exe -NoProfile -Command "Invoke-WebRequest 'https://sqlite.org/2024/sqlite-tools-win-x64-3460000.zip' -OutFile '.\sqlite.zip'" >nul 2>&1
    powershell.exe -NoProfile -Command "Expand-Archive '.\sqlite.zip' -Force" >nul 2>&1
    copy .\sqlite\sqlite3.exe .\sqlite3.exe >nul 2>&1
    rd /s /q .\sqlite >nul 2>&1
    del /F /Q .\sqlite.zip >nul 2>&1
)

set foundinstallpath=
for %%d in (C D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
    if exist "%%d:\Wuthering Waves\Wuthering Waves Game\Client\Saved\LocalStorage\LocalStorage.db" (
        set "foundinstallpath=%%d:\Wuthering Waves\Wuthering Waves Game"
        goto foundinstall
    )
)

:noinstall
exit /b

:foundinstall
set "dbpath=%foundinstallpath%\Client\Saved\LocalStorage\LocalStorage.db"

.\sqlite3.exe "%dbpath%" "UPDATE LocalStorage SET value = (SELECT json_set(value, '$.KeyCustomFrameRate', %wantedfps%)) WHERE key LIKE 'GameQualitySetting';" >nul 2>&1

exit /b

:error
exit /b