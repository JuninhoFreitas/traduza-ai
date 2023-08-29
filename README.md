<!-- Generate a README template -->
# Traduza AI

## Description
Projeto para a tradução de legendas em formato .srt

## Table of Contents

* [Instalação](#instalação)
* [Usage](#como-usar)
* [Questions](#questões)

## Instalação

### Automática (Via Scripts)
1. Clone ou baixa o projeto
2. Rode o arquivo ```setup.bat```
3. Aceite as permissões de ADM
4. A instalação começará automaticamente.

### Manual (Via linha de comando)
```bash
# 1. Instalar Chocolatey
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " [System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

# 2. Instalar FFMPEG
choco install ffmpeg -y

# 3. Instalar Python (Versão acima da 3.X.X)

choco install python -y

# 4. install git
choco install git -y

# 5. Instalar rust
pip install setuptools-rust

# 6. Instalar subsai
pip install git+https://github.com/abdeladim-s/subsai

# 7. Instalar jedi
pip install jedi

# 8. Instalar torchaudio
pip install -q torchaudio
```

## Como usar
### Via Interface(GUI)
1. Instale tudo o que é necessário
2. Rode o arquivo `run_gui.bat` (Se deseja ver os logs, inicie a partir da linha de comando)
3. Selecione o arquivo de transcrição(origem da tradução).
4. Escolha o local e nome do arquivo da tradução final.
5. Realize os demais ajustes de acordo com o que deseja
6. Clique em `Traduzir`
7. Aguarde até que o aplicativo "volte a responder" (durante esse tempo ele ficará bloqueado)

### Via código
1. Use o arquivo `main.py` e altere as variáveis para a sua maneira.
2. Rode o arquivo com o comando `python main.py`

## Questões

1. Como eu consigo transcrever um vídeo?

If you have any questions, please contact me at [GitHub Profile](https://github.com/JuninhoFreitas) or my email at [Email](brizollajr@Gmail.com).