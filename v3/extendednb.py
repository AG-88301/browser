import os
import sys
from extensions.voiceAssistant import main as va
from extensions.incognito import incog
from extensions.media import main as media_Main
from extensions.settings import main as setting_Main
import recolour

from extensions.voiceAssistant.main import *
from extensions.settings.main import *
from extensions.media.main import *
from extensions.incognito.incog import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtWebEngineWidgets import *


class NavBarEx(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(NavBarEx, self).__init__(*args, **kwargs)

        with open('v3/extensions/settings/theme/theme.txt', 'r') as f:
            self.theme = f.readline()
            if self.theme == 'dark':
                incognito_btn = QPushButton(
                    QIcon(os.path.join('v3/icons', 'cil-user.png')), "", self)
                incognito_btn.resize(50, 50)
                incognito_btn.move(50, 50)
                incognito_btn.clicked.connect(lambda _: self.incog_open())

                media_btn = QPushButton(
                    QIcon(os.path.join('v3/icons', 'cil-movie.png')), "", self)
                media_btn.resize(50, 50)
                media_btn.move(125, 50)
                media_btn.clicked.connect(lambda _: self.media_open())

                setting_btn = QPushButton(
                    QIcon(os.path.join('v3/icons', 'cil-settings.png')), "", self)
                setting_btn.resize(50, 50)
                setting_btn.move(200, 50)
                setting_btn.clicked.connect(lambda _: self.settings_open())

                voice_btn = QPushButton(
                    QIcon(os.path.join('v3/icons', 'cil-microphone.png')), "", self)
                voice_btn.resize(50, 50)
                voice_btn.move(50, 125)
                voice_btn.clicked.connect(lambda _: self.va_open())

                self.setWindowTitle("Adwaya's Browser")
                self.setWindowIcon(
                    QIcon(os.path.join('v3/icons', 'cil-screen-desktop.png')))
            else:
                incognito_btn = QPushButton(
                    QIcon(recolour.convert(os.path.join('v3/icons', 'cil-user.png'))), "", self)
                incognito_btn.resize(50, 50)
                incognito_btn.move(50, 50)
                incognito_btn.clicked.connect(lambda _: self.incog_open())

                media_btn = QPushButton(
                    QIcon(recolour.convert(os.path.join('v3/icons', 'cil-movie.png'))), "", self)
                media_btn.resize(50, 50)
                media_btn.move(125, 50)
                media_btn.clicked.connect(lambda _: self.media_open())

                setting_btn = QPushButton(
                    QIcon(recolour.convert(os.path.join('v3/icons', 'cil-settings.png'))), "", self)
                setting_btn.resize(50, 50)
                setting_btn.move(200, 50)
                setting_btn.clicked.connect(lambda _: self.settings_open())

                voice_btn = QPushButton(
                    QIcon(recolour.convert(os.path.join('v3/icons', 'cil-microphone.png'))), "", self)
                voice_btn.resize(50, 50)
                voice_btn.move(50, 125)
                voice_btn.clicked.connect(lambda _: self.va_open())

                self.setWindowTitle("Adwaya's Browser")
                self.setWindowIcon(
                    QIcon(os.path.join('v3/icons', 'cil-screen-desktop.png')))

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
                """)

        self.setFixedWidth(300)
        self.setFixedHeight(300)
        self.show()

    def incog_open(self):
        incog.IncogWindow()

    def media_open(self):
        self.media = media_Main.Window()
        self.media.show()

    def settings_open(self):
        self.setting = setting_Main.Window()
        self.setting.show()

    def va_open(self):
        self.va = va.AssistantWindow()
        self.va.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Adwaya's Browser")

    window = NavBarEx()
    app.exec_()
