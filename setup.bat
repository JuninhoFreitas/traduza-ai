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

@REM install rust
pip install setuptools-rust

@REM install subsai
pip install git+https://github.com/abdeladim-s/subsai

@REM install jedi
pip install jedi

@REM install torchaudio
pip install -q torchaudio

@REM pause