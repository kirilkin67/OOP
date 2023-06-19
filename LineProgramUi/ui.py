from PyQt6 import QtCore, QtGui, QtWidgets
from app_1 import UiMainWindow
import sys


def formula():
    """
    Вычисление формул
    """
    from math import tan, cos, pi, sin
    x = float(ui.x.text().replace(",", "."))
    a = ui.a.value()
    t = ui.t.value()
    y = tan(x * 2 / 2 - 1) * 2 + (2 * cos(x - pi / 6)) / (0.5 + sin(a) ** 2)
    ui.rez2.setText(str(round(y, t)))


def clear():
    ui.x.setText('0')
    ui.a.setValue(0.00)
    ui.t.setValue(0)
    ui.rez2.clear()
    ui.rez1.clear()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = UiMainWindow()
ui.setupUi(MainWindow)

ui.x.setValidator(QtGui.QDoubleValidator())

ui.clear.clicked.connect(clear)

ui.rezult.clicked.connect(formula)

MainWindow.show()
sys.exit(app.exec())
