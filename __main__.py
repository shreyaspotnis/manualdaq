#!/usr/bin/env python

import sys
import ConfigParser
from PyQt4 import QtGui
from MainWindow import MainWindow


def main():
    config = ConfigParser.SafeConfigParser(allow_no_value=True)
    internalConfig = ConfigParser.SafeConfigParser(allow_no_value=True)
    config.read("config.ini")
    internalConfig.read("internal-config.ini")

    w = MainWindow(config, internalConfig)
    w.show()
    return app.exec_()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    sys.exit(main())
