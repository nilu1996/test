@echo off

SET LogDir=C:\ProgramData\Alteryx\BackupLog\
SET TempDir=C:\Temp\
SET NetworkDir=\\ServerName\SharePath\
SET AlteryxService="C:\Program Files\Alteryx\bin\AlteryxService.exe"
SET WorkerNodeService="C:\Program Files\Alteryx\bin\WorkerNodeService.exe"
SET ZipUtil="C:\Program Files\7-Zip\7z.exe"
SET MaxServiceWait=7200

FOR /f %%a IN ('WMIC OS GET LocalDateTime ^| FIND "."') DO SET DTS=%%a
SET DateTime=%DTS:~0,4%%DTS:~4,2%%DTS:~6,2%_%DTS:~8,2%%DTS:~10,2%%DTS:~12,2%
SET /a tztemp=%DTS:~21%/60
SET tzone=UTC%tztemp%

echo %date% %time% %tzone%: Starting backup process... > %LogDir%BackupLog%datetime%.log

:: Stop Alteryx Worker Node
echo %date% %time% %tzone%: Stopping Alteryx Worker Node... >> %LogDir%BackupLog%datetime%.log
%WorkerNodeService% stop >> %LogDir%BackupLog%datetime%.log

:: Stop Alteryx Service
echo %date% %time% %tzone%: Stopping Alteryx Service... >> %LogDir%BackupLog%datetime%.log

SET COUNT=0
:StopInitState
SC query AlteryxService | FIND "STATE" | FIND "RUNNING" >> %LogDir%BackupLog%datetime%.log
IF errorlevel 0 IF NOT errorlevel 1 GOTO StopService
SC query AlteryxService | FIND "STATE" | FIND "STOPPED" >> %LogDir%BackupLog%datetime%.log
IF errorlevel 0 IF NOT errorlevel 1 GOTO StopedService
SC query AlteryxService | FIND "STATE" | FIND "PAUSED" >> %LogDir%BackupLog%datetime%.log
IF errorlevel 0 IF NOT errorlevel 1 GOTO SystemError
echo %date% %time% %tzone%: Service State is changing, waiting for service to resolve its state before making changes >> %LogDir%BackupLog%datetime%.log
SC query AlteryxService | Find "STATE"
timeout /t 1 /nobreak >NUL
SET /A COUNT=%COUNT%+1
IF "%COUNT%" == "%MaxServiceWait%" GOTO SystemError 
GOTO StopInitState

:StopService
SET COUNT=0
SC stop AlteryxService >> %LogDir%BackupLog%datetime%.log
GOTO StoppingService

:StopServiceDelay
timeout /t 1 /nobreak >NUL
SET /A COUNT=%COUNT%+1
IF "%COUNT%" == "%MaxServiceWait%" GOTO SystemError 

:StoppingService
SC query AlteryxService | FIND "STATE" | FIND "STOPPED" >> %LogDir%BackupLog%datetime%.log
IF errorlevel 1 GOTO StopServiceDelay

:StopedService

:: Backup MongoDB to local temp directory
echo %date% %time% %tzone%: Starting MongoDB Backup... >> %LogDir%BackupLog%datetime%.log
%AlteryxService% emongodump=%TempDir%ServerBackup_%datetime%\Mongo >> %LogDir%BackupLog%datetime%.log

:: Backup Config files to local temp directory
echo %date% %time% %tzone%: Backing up settings, connections, and aliases... >> %LogDir%BackupLog%datetime%.log
copy %ProgramData%\Alteryx\RuntimeSettings.xml %TempDir%ServerBackup_%datetime%\RuntimeSettings.xml >> %LogDir%BackupLog%datetime%.log
copy %ProgramData%\Alteryx\Engine\SystemAlias.xml %TempDir%ServerBackup_%datetime%\SystemAlias.xml
copy %ProgramData%\Alteryx\Engine\SystemConnections.xml %TempDir%ServerBackup_%datetime%\SystemConnections.xml
%AlteryxService% getserversecret > %TempDir%ServerBackup_%datetime%\ControllerToken.txt

:: Start Alteryx Service
echo %date% %time% %tzone%: Restarting Alteryx Service... >> %LogDir%BackupLog%datetime%.log
SET COUNT=0

:StartInitState
SC query AlteryxService | FIND "STATE" | FIND "STOPPED" >> %LogDir%BackupLog%datetime%.log
IF errorlevel 0 IF NOT errorlevel 1 GOTO StartService
SC query AlteryxService | FIND "STATE" | FIND "RUNNING" >> %LogDir%BackupLog%datetime%.log
IF errorlevel 0 IF NOT errorlevel 1 GOTO StartedService
SC query AlteryxService | FIND "STATE" | FIND "PAUSED" >> %LogDir%BackupLog%datetime%.log
IF errorlevel 0 IF NOT errorlevel 1 GOTO SystemError
echo %date% %time% %tzone%: Service State is changing, waiting for service to resolve its state before making changes >> %LogDir%BackupLog%datetime%.log
SC query AlteryxService | Find "STATE"
timeout /t 1 /nobreak >NUL
SET /A COUNT=%COUNT%+1
IF "%COUNT%" == "%MaxServiceWait%" GOTO SystemError 
GOTO StartInitState

:StartService
SET COUNT=0
SC start AlteryxService >> %LogDir%BackupLog%datetime%.log
GOTO StartingService

:StartServiceDelay
timeout /t 1 /nobreak >NUL
SET /A COUNT=%COUNT%+1
IF "%COUNT%" == "%MaxServiceWait%" GOTO SystemError 

:StartingService
SC query AlteryxService | FIND "STATE" | FIND "RUNNING" >> %LogDir%BackupLog%datetime%.log
IF errorlevel 1 GOTO StartServiceDelay

:StartedService

:: Start Alteryx Worker Node
echo %date% %time% %tzone%: Starting Alteryx Worker Node... >> %LogDir%BackupLog%datetime%.log
%WorkerNodeService% start >> %LogDir%BackupLog%datetime%.log

echo %date% %time% %tzone%: Backup process completed >> %LogDir%BackupLog%datetime%.log

