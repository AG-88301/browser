import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtWebEngineWidgets import *


class IncogWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(IncogWindow, self).__init__(*args, **kwargs)

        incog = False
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.setCentralWidget(self.tabs)

        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.tabs.currentChanged.connect(self.current_tab_changed)

        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)

        reload_btn = QAction(
            QIcon(os.path.join('v3/icons', 'cil-reload.png')), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        navtb.addAction(reload_btn)
        reload_btn.triggered.connect(
            lambda: self.tabs.currentWidget().reload())

        home_btn = QAction(
            QIcon(os.path.join('v3/icons', 'cil-home.png')), "Home", self)
        home_btn.setStatusTip("Go Home")
        navtb.addAction(home_btn)
        home_btn.triggered.connect(self.navigate_home)

        navtb.addSeparator()

        new_tab_btn = QAction(
            QIcon(os.path.join('v3/icons', 'cil-library-add.png')), "New Tab", self)
        new_tab_btn.setStatusTip("New Tab")
        navtb.addAction(new_tab_btn)
        new_tab_btn.triggered.connect(lambda _: self.add_new_tab())

        navtb.addSeparator()

        self.httpsicon = QLabel()
        self.httpsicon.setPixmap(
            QPixmap(os.path.join('v3/icons', 'cil-lock-unlocked.png')))
        navtb.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.mousePressEvent = lambda _: self.urlbar.selectAll()
        self.urlbar.mouseDoubleClickEvent = lambda _: self.urlbar.deselect()
        navtb.addWidget(self.urlbar)
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        stop_btn = QAction(
            QIcon(os.path.join('v3/icons', 'cil-media-stop.png')), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        navtb.addAction(stop_btn)
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())

        incognito_btn = QAction(
            QIcon(os.path.join('v3/icons', 'cil-user-filled.png')), "Incognito On/Off", self)
        incognito_btn.setStatusTip("Turn on or off Incognito")
        navtb.addAction(incognito_btn)
        incognito_btn.triggered.connect(lambda _: self.incog_open())

        self.setWindowTitle("Adwaya's Browser")
        self.setWindowIcon(
            QIcon(os.path.join('v3/icons', 'cil-screen-desktop.png')))

        self.setStyleSheet("""QWidget{
            background-color: rgb(48, 48, 48);
            color: rgb(255, 255, 255);
        }
        QTabWidget::pane{
            border-top: 2px solid rgb(90, 90, 90);
            position: absolute;
            top: -0.5em;
            color: rgb(255, 255, 255);
            padding: 5px;
        }
        QTabWidget::tab-bar{
            alignment: left;
        }
        QLabel, QToolButton, QTabBar::tab{
            background: rgb(90, 90, 90);
            border: 2px solid rgb(90, 90, 90);
            border-radius: 10px;
            min-width: 8ex;
            padding: 5px;
            margin-right: 2px;
            color: rgb(255, 255, 255);
        }
        QLabel:hover, QToolButton::hover, QTabBar::tab:selected, QTabBar::tab:hover{
            background: rgb(49, 49, 49);
            border: 2px solid rgb(0, 36, 36);
            background-color: rgb(0, 36, 36);
        }
        QLineEdit{
            border: 2px solid rgb(0, 36, 36);
            border-radius: 10px;
            padding: 5px;
            background-color: rgb(0, 36, 36);
            color: rgb(255, 255, 255);
        }
        QLineEdit {
            border: 2px solid rgb(0, 36, 36);
            border-radius: 10px;
            padding: 5px;
            background-color: rgb(0, 36, 36);
            color: rgb(255, 255, 255);
        }
        QLineEdit:hover{
            border: 2px solid rgb(0, 66, 124);
        }
        QLineEdit:focus{
            border: 2px solid rgb(0, 136, 255);
            color: rgb(200, 200, 200);
        }
        QPushButton{
            background: rgb(49, 49, 49);
            border: 2px solid rgb(0, 36, 36);
            background-color: rgb(0, 36, 36);
            padding: 5px;
            border-radius: 10px;
        }
        """)

        self.add_new_tab(QUrl('http://www.google.com'), 'Homepage')

        self.showMaximized()

    def add_new_tab(self, qurl=None, label="Blank"):

        with open('v3/built-ins/incog.html', 'r') as f:
            html = f.read()

        browser = QWebEngineView()
        browser = WebView(off_the_record=True)
        browser.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        browser.page().fullScreenRequested.connect(lambda request: request.accept())

        browser.setHtml(html)

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(
            lambda qurl, browser=browser: self.update_urlbar(qurl, browser))
        browser.loadFinished.connect(
            lambda _, i=i, browser=browser: self.tabs.setTabText(i, browser.page().title()))

    def tab_open_doubleclick(self, i):
        if i == -1:
            self.add_new_tab()

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)

    def update_urlbar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            return
        if q.scheme() == 'https':
            self.httpsicon.setPixmap(
                QPixmap(os.path.join('v3/icons', 'cil-lock-locked.png')))
        else:
            self.httpsicon.setPixmap(
                QPixmap(os.path.join('v3/icons', 'cil-lock-unlocked.png')))
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def current_tab_changed(self):
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())

        self.update_title(self.tabs.currentWidget())

    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            return
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("%s - Adwaya's Browser" % title)

    def navigate_to_url(self):
        url = self.urlbar.text()
        q = QUrl(url)
        if url.endswith('.com') or url.endswith('.org') or url[-3] == '.':
            if q.scheme() == "":
                q.setScheme("http")
        else:
            url = "https://www.google.com/search?q=" + url
            q = QUrl(url)

        self.tabs.currentWidget().setUrl(q)

    def navigate_home(self):
        with open('built-ins/homepage.html', 'r') as f:
            html = f.read()

        self.tabs.currentWidget().setHtml(html)


class WebView(QWebEngineView):
    def __init__(self, off_the_record=False, parent=None):
        super().__init__(parent)
        profile = (
            QWebEngineProfile()
            if off_the_record
            else QWebEngineProfile.defaultProfile()
        )
        page = QWebEnginePage(profile)
        self.setPage(page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Adwaya's Browser")

    window = IncogWindow()
    app.exec_()
