# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Mon Jan 20 14:01:52 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(234, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 221, 541))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushAcquire = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushAcquire.setObjectName(_fromUtf8("pushAcquire"))
        self.gridLayout.addWidget(self.pushAcquire, 0, 1, 1, 1)
        self.spinAverages = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinAverages.setProperty("value", 20)
        self.spinAverages.setObjectName(_fromUtf8("spinAverages"))
        self.gridLayout.addWidget(self.spinAverages, 1, 0, 1, 1)
        self.doubleSpinIndexStart = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinIndexStart.setObjectName(_fromUtf8("doubleSpinIndexStart"))
        self.gridLayout.addWidget(self.doubleSpinIndexStart, 1, 1, 1, 1)
        self.doubleSpinIndexStep = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinIndexStep.setProperty("value", 1.0)
        self.doubleSpinIndexStep.setObjectName(_fromUtf8("doubleSpinIndexStep"))
        self.gridLayout.addWidget(self.doubleSpinIndexStep, 2, 1, 1, 1)
        self.spinCurrentIndex = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinCurrentIndex.setObjectName(_fromUtf8("spinCurrentIndex"))
        self.gridLayout.addWidget(self.spinCurrentIndex, 3, 1, 1, 1)
        self.comboLJInput = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboLJInput.setObjectName(_fromUtf8("comboLJInput"))
        self.gridLayout.addWidget(self.comboLJInput, 0, 0, 1, 1)
        self.tableData = QtGui.QTableWidget(self.gridLayoutWidget)
        self.tableData.setRowCount(1)
        self.tableData.setColumnCount(2)
        self.tableData.setObjectName(_fromUtf8("tableData"))
        item = QtGui.QTableWidgetItem()
        self.tableData.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableData.setItem(0, 1, item)
        self.gridLayout.addWidget(self.tableData, 4, 0, 1, 2)
        self.pushReset = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushReset.setObjectName(_fromUtf8("pushReset"))
        self.gridLayout.addWidget(self.pushReset, 2, 0, 1, 1)
        self.pushCopy = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushCopy.setObjectName(_fromUtf8("pushCopy"))
        self.gridLayout.addWidget(self.pushCopy, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 234, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Manual DAQ", None))
        self.pushAcquire.setToolTip(_translate("MainWindow", "Acquire data. Shortcut: Shift+Return", None))
        self.pushAcquire.setText(_translate("MainWindow", "Acquire", None))
        self.pushAcquire.setShortcut(_translate("MainWindow", "Shift+Return", None))
        self.spinAverages.setToolTip(_translate("MainWindow", "Number of averages to take when acquiring", None))
        self.doubleSpinIndexStart.setToolTip(_translate("MainWindow", "Start value of the index column when acquiring data", None))
        self.doubleSpinIndexStep.setToolTip(_translate("MainWindow", "Step value of the index column when acquiring data", None))
        self.spinCurrentIndex.setToolTip(_translate("MainWindow", "Current row to put data into", None))
        self.comboLJInput.setToolTip(_translate("MainWindow", "Select which LabJack input to use to acquire the data", None))
        __sortingEnabled = self.tableData.isSortingEnabled()
        self.tableData.setSortingEnabled(False)
        item = self.tableData.item(0, 0)
        item.setText(_translate("MainWindow", "Index", None))
        item = self.tableData.item(0, 1)
        item.setText(_translate("MainWindow", "Value", None))
        self.tableData.setSortingEnabled(__sortingEnabled)
        self.pushReset.setToolTip(_translate("MainWindow", "Reset the data and set the current index to zero", None))
        self.pushReset.setText(_translate("MainWindow", "Reset", None))
        self.pushCopy.setToolTip(_translate("MainWindow", "Copy all data to clipboard. Shortcut Ctrl+Shift+C", None))
        self.pushCopy.setText(_translate("MainWindow", "Copy", None))
        self.pushCopy.setShortcut(_translate("MainWindow", "Ctrl+Shift+C", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

