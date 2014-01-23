"""
run  python2-pyuic4 -xo ui_MainWindow.py MainWindow.ui on the command line
before running the application.
"""

from PyQt4 import QtGui, QtCore, uic
import random
import labjacksingle

Ui_MainWindow, QMainWindow = uic.loadUiType("MainWindow.ui")

class MainWindow(QMainWindow, Ui_MainWindow):
    """The only window of the application."""

    def __init__(self, config, internalConfig):
        super(MainWindow, self).__init__()

        self.config = config
        self.internalConfig = internalConfig

        self.setupUi(self)

        self.ljs = labjacksingle.LabJackSingle()
        self.ljs.configure([0])
        # some additional UI setup
        self.comboLJInput.addItems(self.ljs.getAllChannels())
        self.timer = QtCore.QBasicTimer()
        self.timer.start(100, self)

        self.connectSlots()

    def connectSlots(self):
        self.pushAcquire.clicked.connect(self.handlePushAcquire)
        self.pushCopy.clicked.connect(self.handlePushCopy)
        self.pushReset.clicked.connect(self.handlePushReset)
        self.comboLJInput.currentIndexChanged.connect(self.handleLJInputChanged)

    def handlePushAcquire(self):
        nRows = self.tableData.rowCount()
        currIndex = self.spinCurrentIndex.value()
        index_value = (self.doubleSpinIndexStart.value() +
                       self.doubleSpinIndexStep.value() * currIndex)

        value = self.ljs.read(self.spinAverages.value())[0]

        index_item = QtGui.QTableWidgetItem(str(index_value))
        value_item = QtGui.QTableWidgetItem("{0:.2f}".format(value))
        self.tableData.setRowCount(nRows + 1)
        self.tableData.setItem(nRows, 0, index_item)
        self.tableData.setItem(nRows, 1, value_item)
        self.spinCurrentIndex.setValue(currIndex + 1)

    def handlePushReset(self):
        self.spinCurrentIndex.setValue(0)
        self.tableData.setRowCount(1)

    def handlePushCopy(self):
        strList = []
        for i in range(1, self.tableData.rowCount()):
            # starts from 1 to exclude title. Plotting software complains otherwise
            for j in range(self.tableData.columnCount()):
                strList.append(str(self.tableData.item(i, j).text()))
                strList.append('\t')
            strList.append('\n')
        fullString = "".join(strList)
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(fullString)

    def handleLJInputChanged(self, newInput):
        self.ljs.configureChannels([newInput])

    def timerEvent(self, e):
        value = self.ljs.read()[0]
        self.labelValue.setText("{0:.2f}".format(value))
