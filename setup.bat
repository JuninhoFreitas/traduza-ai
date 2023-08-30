@REM Run as Admin
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )

@REM generate a powershell script to install ffmpeg via chocolatey

@REM install chocolatey
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " [System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

@REM install ffmpeg
choco install ffmpeg -y

@REM install python
choco install python -y

@REM install git
choco install git -y

@REM Update Env
call RefreshEnv.cmd
pip install setuptools-rust || true

@REM install subsai
pip install git+https://github.com/abdeladim-s/subsai || true

@REM install jedi
pip install jedi || true

@REM install torchaudio
pip install -q torchaudio || true

@REM install pyqt5
pip install PyQt5 || true

:: pause (if needed)
:: pause