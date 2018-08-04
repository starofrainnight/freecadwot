

import os.path
from qtpy.QtWidgets import QMainWindow
from qtpy.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self, *args):
        super().__init__(*args)

        self.ui = loadUi(
            os.path.join(os.path.dirname(__file__), 'MainWindow.ui'), self)
