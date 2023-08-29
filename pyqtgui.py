import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from ui import Ui_MainWindow

import functools
import threading

import pysubs2
from subsai import Tools


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("main.ui", self)
        self.initUI()
        

    def initUI(self):
        self.createButtons()
        self.setWindowTitle("TraduzAi")
        self.btnOpenTranscription.clicked.connect(self.on_btnOpenTranscription_clicked)
        self.btnOpenTranslate.clicked.connect(self.on_btnOpenTranslate_clicked)
        self.btnTranslate.clicked.connect(
            functools.partial(self.on_btnTranslate_clicked)
        )
    
    # Functions
    def perform_translation(self):
        self.btnTranslate.setEnabled(False)
        self.window().setCursor(QtCore.Qt.WaitCursor)
        print("Translating...")
        subs = pysubs2.load(self.pathToTranscription)
        Tools.available_translation_models()
        print(Tools.available_translation_languages(self.comboModel.currentText()))
        translated_subs = Tools.translate(
            subs,
            source_language=self.comboOrigin.currentText(),
            target_language=self.comboTranslate.currentText(),
            model=self.comboModel.currentText(),
        )
        translated_subs.save(self.pathToTranslate)
        print(f"translated file saved to {self.pathToTranslate}")
        self.btnTranslate.setEnabled(True)
        self.window().setCursor(QtCore.Qt.ArrowCursor)
        # Show a Pop up window with the translated file path
        # Post a custom event to trigger the show_translation_popup method
        event = TranslationEvent()
        QtCore.QCoreApplication.postEvent(self, event)

    def event(self, event):
        if isinstance(event, TranslationEvent):
            self.show_translation_popup()
            return True
        return super().event(event)

    def show_translation_popup(self):
        self.popup = QMessageBox(self,title="Tradução Concluída", text="Local do Arquivo Traduzido")
        self.popup.setText(f"Arquivo salvo: {self.pathToTranslate}")
        self.popup.exec_()
    # Button Actions 

    @QtCore.pyqtSlot(name="on_btnTranslate_clicked")
    def on_btnTranslate_clicked(self):
        self.translation_thread = threading.Thread(target=self.perform_translation)
        self.translation_thread.start()

    def on_btnOpenTranslate_clicked(self):
        # open file dialog box to select file when clicked
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(
            self,
            "QFileDialog.getSaveFileName()",
            "",
            "Arquivos de Legenda (*.srt)",
            options=options,
        )
        if fileName:
            self.pathToTranslate = fileName
            print(self.pathToTranslate)
            self.inputPathToTranslate.setText(self.pathToTranslate)
            self.inputPathToTranslate.setStyleSheet(
                "background-color: #FFFFFF; color: #000000; font-size: 12px;"
            )
    
    def on_btnOpenTranscription_clicked(self):
        # Open a dialog to ask where to save a file
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            "",
            "Arquivos de Legenda (*.srt)",
            options=options,
        )
        if fileName:
            self.pathToTranscription = fileName
            print(self.pathToTranscription)
            self.inputPathToTranscript.setText(self.pathToTranscription)
            self.inputPathToTranscript.setStyleSheet(
                "background-color: #FFFFFF; color: #000000; font-size: 12px;"
            )
    # Create Buttons for the UI #TODO MOVE IT TO COMPONENTS CLASS IN ANOTHER MODULE
    def createButtons(self):
        _translate = QtCore.QCoreApplication.translate
        self.btnTranslate = QtWidgets.QPushButton(self.centralwidget)
        self.btnTranslate.setText(_translate("MainWindow", "Traduzir"))
        self.btnTranslate.setEnabled(True)
        self.btnTranslate.setGeometry(QtCore.QRect(80, 340, 171, 41))
        self.btnTranslate.setStyleSheet(
            "QPushButton#btnTranslate{\n"
            "background: #005FB8;\n"
            "border-radius: 4px;\n"
            "font-family: 'Actor';\n"
            "font-style: normal;\n"
            "font-weight: 400;\n"
            "font-size: 14px;\n"
            "line-height: 20px;\n"
            "/* identical to box height, or 143% */\n"
            "text-align: center;\n"
            "/* Light/Fill Color/Text On Accent/Primary */\n"
            "color: #FFFFFF;\n"
            "}\n"
            "QPushButton#btnTranslate:active{\n"
            "background: rgba(14, 82, 144, 1);\n"
            "border-radius: 4px;\n"
            "font-family: 'Actor';\n"
            "font-style: normal;\n"
            "font-weight: 400;\n"
            "font-size: 14px;\n"
            "line-height: 20px;\n"
            "/* identical to box height, or 143% */\n"
            "text-align: center;\n"
            "/* Light/Fill Color/Text On Accent/Primary */\n"
            "color: #FFFFFF;\n"
            "}\n"
            "\n"
            "QPushButton#btnTranslate:hover{\n"
            "background: rgba(0, 95, 184, 0.8);\n"
            "border-radius: 4px;\n"
            "font-family: 'Actor';\n"
            "font-style: normal;\n"
            "font-weight: 400;\n"
            "font-size: 14px;\n"
            "line-height: 20px;\n"
            "/* identical to box height, or 143% */\n"
            "text-align: center;\n"
            "/* Light/Fill Color/Text On Accent/Primary */\n"
            "color: #FFFFFF;\n"
            "}\n"
            ""
        )
        self.btnTranslate.setObjectName("btnTranslate")
        # Open Transcription

        self.btnOpenTranscription = QtWidgets.QPushButton(self)
        self.btnOpenTranscription.setGeometry(QtCore.QRect(236, 90, 75, 30))
        self.btnOpenTranscription.setText(_translate("MainWindow", "Selecionar"))
        font = QtGui.QFont()
        font.setFamily("Actor")
        font.setPointSize(10)
        self.btnOpenTranscription.setFont(font)
        self.btnOpenTranscription.setStyleSheet(
            "QPushButton#btnOpenTranscription{\n"
            "background-color: #FFFFFF;\n"
            "border-color: rgba(0, 0, 0, 0.0578);\n"
            "border-radius: 2px;\n"
            "border-style: solid;\n"
            "border-width: 1px;\n"
            "\n"
            "}\n"
            "\n"
            "QPushButton#btnOpenTranscription:pressed{\n"
            "background-color: #FFFFF3;\n"
            "border-color: rgba(0, 0, 0, 0.0578);\n"
            "border-radius: 2px;\n"
            "border-style: solid;\n"
            "border-width: 1px;\n"
            "}\n"
            "\n"
            "QPushButton#btnOpenTranscription:hover{\n"
            "background-color: #f6f5f4;\n"
            "border-color: rgba(0, 0, 0, 0.0578);\n"
            "border-radius: 2px;\n"
            "border-style: solid;\n"
            "border-width: 1px;\n"
            "}\n"
            "\n"
            ""
        )
        self.btnOpenTranscription.setAutoRepeatDelay(1000)
        self.btnOpenTranscription.setFlat(True)
        self.btnOpenTranscription.setObjectName("btnOpenTranscription")
        # Open Translate
        self.btnOpenTranslate = QtWidgets.QPushButton(self)
        self.btnOpenTranslate.setGeometry(QtCore.QRect(235, 150, 75, 30))
        self.btnOpenTranslate.setText(_translate("MainWindow", "Selecionar"))
        font = QtGui.QFont()
        font.setFamily("Actor")
        font.setPointSize(10)
        self.btnOpenTranslate.setFont(font)
        self.btnOpenTranslate.setStyleSheet(
            "QPushButton#btnOpenTranslate{\n"
            "background-color: #FFFFFF;\n"
            "border-color: rgba(0, 0, 0, 0.0578);\n"
            "border-radius: 2px;\n"
            "border-style: solid;\n"
            "border-width: 1px;\n"
            "\n"
            "}\n"
            "\n"
            "QPushButton#btnOpenTranslate:pressed{\n"
            "background-color: #FFFFF3;\n"
            "border-color: rgba(0, 0, 0, 0.0578);\n"
            "border-radius: 2px;\n"
            "border-style: solid;\n"
            "border-width: 1px;\n"
            "}\n"
            "\n"
            "QPushButton#btnOpenTranslate:hover{\n"
            "background-color: #f6f5f4;\n"
            "border-color: rgba(0, 0, 0, 0.0578);\n"
            "border-radius: 2px;\n"
            "border-style: solid;\n"
            "border-width: 1px;\n"
            "}\n"
            "\n"
            ""
        )
        self.btnOpenTranslate.setAutoRepeatDelay(1000)
        self.btnOpenTranslate.setFlat(True)
        self.btnOpenTranslate.setObjectName("btnOpenTranslate")

class TranslationEvent(QtCore.QEvent):
    def __init__(self):
        super().__init__(QtCore.QEvent.Type(QtCore.QEvent.User))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
