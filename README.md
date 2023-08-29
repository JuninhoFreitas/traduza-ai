<!-- Generate a README template -->
# TraduzAI
<!-- insert image and configure size -->
<img src="https://i.imgur.com/E56G5Lv.png?width=100" alt="drawing" style="height:400px;"/>

## Descrição
O TraduzAI é um projeto que visa facilitar a tradução de vídeos, utilizando a tecnologia de inteligência artificial sem depender de dezenas de linhas de código e conhecimento de programação.

Tudo isso GRATUITAMENTE.

## Sumário

* [Instalação](#instalação)
* [Como Usar](#como-usar)
* [Questões](#questões)

## Instalação

### Automática (Via Scripts)
1. Clone ou baixa o projeto
2. Rode o arquivo ```setup.bat```
3. Aceite as permissões de ADM
4. A instalação começará automaticamente.

### Manual (Via linha de comando)
 - Basta seguir todos os pontos do arquivo setup.bat, instalando somente os que você não tem.

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

* ### 1. Como eu posso transcrever um vídeo?
```bash
# !!! Primeiro executar o setup.bat para instalar todas as dependências

# simplesmente rode o comando abaixo trocando pelo nome dos arquivos que você tem
# "./videos/example.mp4" é o local onde está o seu vídeo em relação aonde está sendo executado o comando
$ subsai ./videos/example.mp4 --model openai/whisper --model-configs '{"model_type": "small"}' --format srt
```
* ### 2. Como eu posso traduzir uma legenda .srt sem usar a interface gráfica?

```python
# !!! Primeiro executar o setup.bat para instalar todas as dependências

# Para isso, será necessário editar o arquivo main.py
# Estas são as variáveis a terem seus valores substituídos:

# subtitles_file é nome do arquivo de legenda original, ex: '.commongrace.srt'
subtitles_file = './commongrace.srt'

# translation_model é nome do modelo de tradução a ser usado, ex: 'facebook/m2m100_1.2B'
translation_model = 'facebook/m2m100_1.2B'

# source_language é o idioma original da legenda, ex: 'English'
source_language = 'English'

# target_language é o idioma para o qual irá traduzir, ex: 'Portuguese'
target_language = 'Portuguese'

#
#
# Após todos os ajustes, basta executar o comando para rodar o código:
# python main.py
```

Qualquer problema ou sugestão, me chama aí em algum dos meus contatos [LinkTree](https://juninho.dev/) também pode me contatar via [Email](brizollajr@Gmail.com).