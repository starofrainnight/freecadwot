# -*- coding: utf-8 -*-

"""Main module."""

import sys
from qtpy.QtCore import QTimer, QCoreApplication
from qtpy.QtWidgets import QApplication
from rabird.qt.application import InitMixin


class Application(QApplication, InitMixin):
    """
    """

    def __init__(self, **kwargs):
        super().__init__(sys.argv)
