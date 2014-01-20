# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Mon Jan 20 15:49:26 2014
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
        MainWindow.resize(377, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 339, 541))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableData = QtGui.QTableWidget(self.gridLayoutWidget)
        self.tableData.setRowCount(1)
        self.tableData.setColumnCount(2)
        self.tableData.setObjectName(_fromUtf8("tableData"))
        item = QtGui.QTableWidgetItem()
        self.tableData.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableData.setItem(0, 1, item)
        self.gridLayout.addWidget(self.tableData, 8, 1, 1, 3)
        self.doubleSpinIndexStart = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinIndexStart.setMinimum(-1000000.0)
        self.doubleSpinIndexStart.setMaximum(1000000.0)
        self.doubleSpinIndexStart.setObjectName(_fromUtf8("doubleSpinIndexStart"))
        self.gridLayout.addWidget(self.doubleSpinIndexStart, 1, 3, 1, 1)
        self.doubleSpinIndexStep = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinIndexStep.setMinimum(-1000000.0)
        self.doubleSpinIndexStep.setMaximum(1000000.0)
        self.doubleSpinIndexStep.setProperty("value", 1.0)
        self.doubleSpinIndexStep.setObjectName(_fromUtf8("doubleSpinIndexStep"))
        self.gridLayout.addWidget(self.doubleSpinIndexStep, 2, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 7, 2, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.comboLJInput = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboLJInput.setObjectName(_fromUtf8("comboLJInput"))
        self.gridLayout.addWidget(self.comboLJInput, 7, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.pushReset = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushReset.setObjectName(_fromUtf8("pushReset"))
        self.gridLayout.addWidget(self.pushReset, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.spinCurrentIndex = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinCurrentIndex.setMaximum(10000)
        self.spinCurrentIndex.setObjectName(_fromUtf8("spinCurrentIndex"))
        self.gridLayout.addWidget(self.spinCurrentIndex, 3, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 2, 1, 1)
        self.pushAcquire = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushAcquire.setObjectName(_fromUtf8("pushAcquire"))
        self.gridLayout.addWidget(self.pushAcquire, 1, 1, 1, 1)
        self.pushCopy = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushCopy.setObjectName(_fromUtf8("pushCopy"))
        self.gridLayout.addWidget(self.pushCopy, 3, 1, 1, 1)
        self.spinAverages = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinAverages.setProperty("value", 20)
        self.spinAverages.setObjectName(_fromUtf8("spinAverages"))
        self.gridLayout.addWidget(self.spinAverages, 5, 3, 1, 1)
        self.labelValue = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.labelValue.setFont(font)
        self.labelValue.setObjectName(_fromUtf8("labelValue"))
        self.gridLayout.addWidget(self.labelValue, 0, 2, 1, 2)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 377, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Manual DAQ", None))
        __sortingEnabled = self.tableData.isSortingEnabled()
        self.tableData.setSortingEnabled(False)
        item = self.tableData.item(0, 0)
        item.setText(_translate("MainWindow", "Index", None))
        item = self.tableData.item(0, 1)
        item.setText(_translate("MainWindow", "Value", None))
        self.tableData.setSortingEnabled(__sortingEnabled)
        self.doubleSpinIndexStart.setToolTip(_translate("MainWindow", "Start value of the index column when acquiring data", None))
        self.doubleSpinIndexStep.setToolTip(_translate("MainWindow", "Step value of the index column when acquiring data", None))
        self.label_5.setText(_translate("MainWindow", "Channel", None))
        self.label.setText(_translate("MainWindow", "Start:", None))
        self.comboLJInput.setToolTip(_translate("MainWindow", "Select which LabJack input to use to acquire the data", None))
        self.label_2.setText(_translate("MainWindow", "Step:", None))
        self.pushReset.setToolTip(_translate("MainWindow", "Reset the data and set the current index to zero", None))
        self.pushReset.setText(_translate("MainWindow", "Reset", None))
        self.label_3.setText(_translate("MainWindow", "Index:", None))
        self.spinCurrentIndex.setToolTip(_translate("MainWindow", "Current row to put data into", None))
        self.label_4.setText(_translate("MainWindow", "Averages", None))
        self.pushAcquire.setToolTip(_translate("MainWindow", "Acquire data. Shortcut: Shift+Return", None))
        self.pushAcquire.setText(_translate("MainWindow", "Acquire", None))
        self.pushAcquire.setShortcut(_translate("MainWindow", "Shift+Return", None))
        self.pushCopy.setToolTip(_translate("MainWindow", "Copy all data to clipboard. Shortcut Ctrl+Shift+C", None))
        self.pushCopy.setText(_translate("MainWindow", "Copy", None))
        self.pushCopy.setShortcut(_translate("MainWindow", "Ctrl+Shift+C", None))
        self.spinAverages.setToolTip(_translate("MainWindow", "Number of averages to take when acquiring", None))
        self.labelValue.setToolTip(_translate("MainWindow", "Current value being read from labjack", None))
        self.labelValue.setText(_translate("MainWindow", "0.00", None))
        self.label_6.setText(_translate("MainWindow", "Value", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

