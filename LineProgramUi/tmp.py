import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from app import UiMainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = UiMainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
