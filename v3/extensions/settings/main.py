import os
import sys
import recolour
from extensions.settings.theme import main as theme_Main
import extensions.settings.restart as restart
import extensions.settings.clearBrowsing.main as cbrowse

from extensions.settings.clearBrowsing.main import clearb
from extensions.settings.restart import restart_program
from extensions.settings.theme.main import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtWebEngineWidgets import *


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        with open('v3/extensions/settings/theme/theme.txt', 'r') as f:
            self.theme = f.readline()
            if self.theme == 'dark':
                change_theme_btn = QPushButton(
                    QIcon(os.path.join('v3/icons', 'cil-paint-bucket.png')), "", self)
                change_theme_btn.resize(50, 50)
                change_theme_btn.move(50, 50)
                change_theme_btn.clicked.connect(lambda _: self.change_theme())

                cBrowsing_btn = QPushButton(
                    QIcon(os.path.join('v3/icons', 'cil-trash.png')), "", self)
                cBrowsing_btn.resize(50, 50)
                cBrowsing_btn.move(125, 50)
                cBrowsing_btn.clicked.connect(lambda _: cbrowse.clearb())
            else:
                change_theme_btn = QPushButton(
                    QIcon(recolour.convert(os.path.join('v3/icons', 'cil-paint-bucket.png'))), "", self)
                change_theme_btn.resize(50, 50)
                change_theme_btn.move(50, 50)
                change_theme_btn.clicked.connect(lambda _: self.change_theme())

                cBrowsing_btn = QPushButton(
                    QIcon(os.path.join('v3/icons', 'cil-trash.png')), "", self)
                cBrowsing_btn.resize(50, 50)
                cBrowsing_btn.move(125, 50)
                cBrowsing_btn.clicked.connect(lambda _: cbrowse.clearb())

        self.setWindowTitle("Adwaya's Browser")
        self.setWindowIcon(
            QIcon(os.path.join('v3/icons', 'cil-screen-desktop.png')))

        with open('v3/extensions/settings/theme/theme.txt', 'r') as f:
            self.theme = f.readline()
            if self.theme == 'light':
                self.setStyleSheet("""QWidget{
                background-color: rgb(255,255, 255);
                color: rgb(0, 0, 0);
                }
                QPushButton{
                    background: rgb(187, 122, 122);
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

    def change_theme(self):
        theme_Main.Change_Theme()
        restart.restart_program()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Adwaya's Browser")

    window = Window()
    app.exec_()
