import os
import sys
import recolour

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtWebEngineWidgets import *


class AssistantWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(AssistantWindow, self).__init__(*args, **kwargs)

        with open('v3/extensions/settings/theme/theme.txt', 'r') as f:
            self.theme = f.readline()
            if self.theme == 'dark':
                startRecording = QPushButton(
                    QIcon(os.path.join('v3/icons', 'cil-microphone.png')), "", self)
                startRecording.resize(50, 50)
                startRecording.move(50, 50)
                startRecording.clicked.connect(lambda _: self.startVoice())

                self.ListeningLabel = QLabel(self)
                self.ListeningLabel.move(125, 50)

                stopRecording = QPushButton(
                    QIcon(os.path.join('v3/icons', 'cil-media-pause.png')), "", self)
                stopRecording.resize(50, 50)
                stopRecording.move(50, 125)
                stopRecording.clicked.connect(lambda _: self.stopVoice())

                self.ReadingLabel = QLabel(self)
                self.ReadingLabel.move(125, 125)

                self.AnswerLabel = QLabel(self)
                self.AnswerLabel.move(50, 200)
            else:
                startRecording = QPushButton(
                    QIcon(recolour.convert(os.path.join('v3/icons', 'cil-microphone.png'))), "", self)
                startRecording.resize(50, 50)
                startRecording.move(50, 50)
                startRecording.clicked.connect(lambda _: self.startVoice())

                self.ListeningLabel = QLabel(self)
                self.ListeningLabel.move(125, 50)

                stopRecording = QPushButton(
                    QIcon(recolour.convert(os.path.join('v3/icons', 'cil-media-pause.png'))), "", self)
                stopRecording.resize(50, 50)
                stopRecording.move(50, 125)
                stopRecording.clicked.connect(lambda _: self.stopVoice())

                self.ReadingLabel = QLabel(self)
                self.ReadingLabel.move(125, 125)

                self.AnswerLabel = QLabel(self)
                self.AnswerLabel.move(50, 200)

        with open('v3/extensions/settings/theme/theme.txt', 'r') as f:
            self.theme = f.readline()
            if self.theme == 'light':
                self.setStyleSheet("""QWidget{
                    background-color: rgb(255, 255, 255);
                    color: rgb(0, 0, 0);
                }
                QPushButton{
                    background: rgb(49, 49, 49);
                    border: 2px solid rgb(192, 179, 152);
                    background-color: rgb(192, 179, 152);
                    padding: 5px;
                    border-radius: 10px;
                }
                QPushButton:hover{
                    background: rgb(49, 49, 49);
                    border: 2px solid rgb(192, 192, 166);
                    background-color: rgb(192, 192, 166);
                    padding: 5px;
                    border-radius: 10px;
                }
                QLabel{
                    color: rgb(0, 0, 0);
                }
                """)
            else:
                self.setStyleSheet("""QWidget{
                    background-color: rgb(48, 48, 48);
                    color: rgb(255, 255, 255);
                }
                QPushButton{
                    background: rgb(49, 49, 49);
                    border: 2px solid rgb(0, 36, 36);
                    background-color: rgb(0, 36, 36);
                    padding: 5px;
                    border-radius: 10px;
                }
                QPushButton:hover{
                    background: rgb(49, 49, 49);
                    border: 2px solid rgb(0, 50, 50);
                    background-color: rgb(0, 50, 50);
                    padding: 5px;
                    border-radius: 10px;
                }
                QLabel{
                    color: rgb(255, 255, 255);
                }
                """)

        self.setFixedWidth(618)
        self.setFixedHeight(280)
        self.show()

    def startVoice(self):
        self.ListeningLabel.setText("Listening...")
        self.ListeningLabel.setFont(QFont('Arial', 20))
        self.ListeningLabel.adjustSize()

    def stopVoice(self):
        self.ListeningLabel.setText("")
        self.ListeningLabel.setFont(QFont('Arial', 20))
        self.ListeningLabel.adjustSize()

        self.ReadingLabel.setText("You said ")
        self.ReadingLabel.setFont(QFont('Arial', 20))
        self.ReadingLabel.adjustSize()

        self.AnswerLabel.setText("Answer ")
        self.AnswerLabel.setFont(QFont('Arial', 20))
        self.AnswerLabel.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Adwaya's Browser")

    window = AssistantWindow()
    app.exec_()
