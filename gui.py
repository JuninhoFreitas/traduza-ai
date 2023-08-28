import tkinter.filedialog
import tkinter as tk
from pathlib import Path
import pysubs2
from subsai import Tools


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


# create the application
myapp = App()

myapp.master.title("Traduza Ai")

# define defaults
filetypeSRT = [("Arquivos de Legenda", ".srt")]

# create all variables needed
pathToTranscription = ""
sourceLanguage = "English"
targetLanguage = "Portuguese"
translationModel = "facebook/m2m100_1.2B"
pathToExport = "./traduzido.srt"

# add button to select file
myapp.master.geometry("500x500")
myapp.master.resizable(0, 0)
myapp.master.config(bg="black")


# add button to open file dialog box to select file when clicked
def selectPathToTranscription():
    # save path to file in a variable
    global pathToTranscription
    pathToTranscription = tkinter.filedialog.askopenfilename(filetypes=filetypeSRT)
    print(pathToTranscription)


selectFileButton = tk.Button(
    myapp,
    text="Selecione o Arquivo de Transcrição",
    command=lambda: selectPathToTranscription(),
)
selectFileButton.pack()


# add OptionMenu to select source language
languageChoices = ["English", "Spanish", "Portuguese"]
variableSourceLanguage = tk.StringVar(myapp)
variableSourceLanguage.set(languageChoices[0])  # default value


def setSourceLanguage():
    # save source language in a variable
    global sourceLanguage
    sourceLanguage = variableSourceLanguage.get()
    print(sourceLanguage)


sourceLanguageMenu = tk.OptionMenu(
    myapp,
    variableSourceLanguage,
    *languageChoices,
    command=lambda x: setSourceLanguage(),
)
sourceLanguageMenu.pack()

# add OptionMenu to select target language
variableTargetLanguage = tk.StringVar(myapp)
variableTargetLanguage.set(languageChoices[2])  # default value


def setTargetLanguage():
    # save target language in a variable
    global targetLanguage
    targetLanguage = variableTargetLanguage.get()
    print(targetLanguage)


targetLanguageMenu = tk.OptionMenu(
    myapp,
    variableTargetLanguage,
    *languageChoices,
    command=lambda x: setTargetLanguage(),
)
targetLanguageMenu.pack()

# add optionMenu to select translation model
translationModelChoices = [
    "facebook/m2m100_1.2B",
    "facebook/wmt19-en-de",
    "facebook/wmt19-de-en",
]
variableTranslationModel = tk.StringVar(myapp)
variableTranslationModel.set(translationModelChoices[0])  # default value


def setTranslationModel():
    # save translation model in a variable
    global translationModel
    translationModel = variableTranslationModel.get()
    print(translationModel)


translationModelMenu = tk.OptionMenu(
    myapp,
    variableTranslationModel,
    *translationModelChoices,
    command=lambda x: setTranslationModel(),
)
translationModelMenu.pack()


# add button to select path to where shave translation
def selectPathToExport():
    # save path to file in a variable
    global pathToExport
    pathToExport = tkinter.filedialog.asksaveasfilename(filetypes=filetypeSRT)
    print(pathToExport)


selectPathToExportButton = tk.Button(
    myapp,
    text="Selecione o Local onde salvar a Tradução",
    command=lambda: selectPathToExport(),
)
selectPathToExportButton.pack()

# start the program

tk.Button(
    myapp,
    text="Show Variables",
    command=lambda: print(
        "PathToTranscription:",
        pathToTranscription,
        "\nTranslateModel:",
        translationModel,
        "\nTarget:",
        targetLanguage,
        "\nSource: ",
        sourceLanguage,
        "\n Path to Export: ",
        pathToExport,
    ),
).pack()


def translate():
    format = ".srt"
    print("Translating...")
    subs = pysubs2.load(pathToTranscription)
    Tools.available_translation_models()
    print(Tools.available_translation_languages(translationModel))
    translated_subs = Tools.translate(
        subs,
        source_language=sourceLanguage,
        target_language=targetLanguage,
        model=translationModel,
    )
    translated_subs.save(pathToExport + format)
    print(f"translated file saved to {pathToExport+format}")
    # Show a Pop up window with the translated file path
    popup = tk.Tk()
    popup.wm_title("Local do Arquivo Traduzido")
    label = tk.Label(popup, text=pathToExport + format)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


translateButton = tk.Button(myapp, text="Translate", command=lambda: translate())
translateButton.pack()

myapp.mainloop()
