"""
run  python2-pyuic4 -xo ui_MainWindow.py MainWindow.ui on the command line
before running the application.
"""

from PyQt4 import QtGui
from ui_MainWindow import Ui_MainWindow
import random

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """The only window of the application."""

    def __init__(self, config, internalConfig):
        super(MainWindow, self).__init__()

        self.config = config
        self.internalConfig = internalConfig

        self.setupUi(self)

        # some additional UI setup
        pass

        self.connectSlots()

    def connectSlots(self):
        self.pushAcquire.clicked.connect(self.handlePushAcquire)
        self.pushCopy.clicked.connect(self.handlePushCopy)
        self.pushReset.clicked.connect(self.handlePushReset)

    def handlePushAcquire(self):
        nRows = self.tableData.rowCount()
        currIndex = self.spinCurrentIndex.value()
        index_value = (self.doubleSpinIndexStart.value() +
                       self.doubleSpinIndexStep.value() * currIndex)

        index_item = QtGui.QTableWidgetItem(str(index_value))
        value_item = QtGui.QTableWidgetItem(str(random.random()))
        self.tableData.setRowCount(nRows + 1)
        self.tableData.setItem(nRows, 0, index_item)
        self.tableData.setItem(nRows, 1, value_item)
        self.spinCurrentIndex.setValue(currIndex + 1)


    def handlePushReset(self):
        self.spinCurrentIndex.setValue(0)
        self.tableData.setRowCount(1)

    def handlePushCopy(self):
        strList = []
        for i in range(self.tableData.rowCount()):
            for j in range(self.tableData.columnCount()):
                strList.append(str(self.tableData.item(i, j).text()))
                strList.append('\t')
            strList.append('\n')
        fullString = "".join(strList)
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(fullString)

