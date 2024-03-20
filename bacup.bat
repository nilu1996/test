@echo off

:: Set variables for Log, Temp, and Alteryx Service Path
SET LogDir=C:\ProgramData\Alteryx\BackupLog\
SET TempDir=C:\Temp\
SET AlteryxService="C:\Program Files\Alteryx\bin\AlteryxService.exe"

:: Set the maximium time to wait for the service to start or stop in whole seconds. Default value is 2 hours.
SET MaxServiceWait=7200

:: Stop Worker Node Server
echo Stopping Worker Node Server (USE1NPWAPALTA02)...
psexec \\USE1NPWAPALTA02 SC stop AlteryxService
timeout /t 5 /nobreak >NUL

:: Stop Primary Server
echo Stopping Primary Server (USE1NPWAPALTD01)...
SC stop AlteryxService
timeout /t 5 /nobreak >NUL

:: Backup process on Primary Server
echo Starting backup process on Primary Server...
%AlteryxService% emongodump="DRIVE:\BACKUP_FOLDER"
echo Backup process on Primary Server completed.

:: Start Primary Server
echo Starting Primary Server (USE1NPWAPALTD01)...
SC start AlteryxService
timeout /t 5 /nobreak >NUL

:: Start Worker Node Server
echo Starting Worker Node Server (USE1NPWAPALTA02)...
psexec \\USE1NPWAPALTA02 SC start AlteryxService
timeout /t 5 /nobreak >NUL

echo Backup process completed and servers started.
