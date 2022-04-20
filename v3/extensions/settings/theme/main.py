import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5.QtWebEngineWidgets import *


class Change_Theme:
    def __init__(self, *args, **kwargs):
        super(Change_Theme, self).__init__(*args, **kwargs)

        with open('v3/extensions/settings/theme/theme.txt', 'r') as f:
            text = f.readline()

        with open('v3/extensions/settings/theme/theme.txt', 'w') as self.f:
            if text == 'dark':
                self.f.write("light")
            elif text == 'light':
                self.f.write("dark")
            else:
                self.f.write("dark")
