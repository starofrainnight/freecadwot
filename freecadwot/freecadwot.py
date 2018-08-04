# -*- coding: utf-8 -*-

"""Main module."""

import sys
from qtpy.QtCore import QTimer, QCoreApplication
from qtpy.QtWidgets import QApplication
from rabird.qt.application import InitMixin
from .MainWindow import MainWindow


class Application(QApplication, InitMixin):
    """Application of FreeCAD Wiki Offline Translator
    """

    def __init__(self, **kwargs):
        super().__init__(sys.argv)

        self._mainWindow = MainWindow()
        self._mainWindow.show()
