from PyQt4 import QtGui


class MainWindow(QtGui.QMainWindow):
    """The only window of the application."""

    def __init__(self, config, internalConfig):
        super(MainWindow, self).__init__()

        self.config = config
        self.internalConfig = internalConfig
        self.initUI()

    def initUI(self):
        """Add UI elements to the widget."""

        self.statusBar()
