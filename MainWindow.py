"""
run  python2-pyuic4 -xo ui_MainWindow.py MainWindow.ui on the command line
before running the application.
"""

from PyQt4 import QtGui
from ui_MainWindow import Ui_MainWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """The only window of the application."""

    def __init__(self, config, internalConfig):
        super(MainWindow, self).__init__()

        self.config = config
        self.internalConfig = internalConfig

        self.setupUi(self)
