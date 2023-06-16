from PyQt6 import QtCore, QtGui, QtWidgets
from app_1 import UiMainWindow
from math import radians, sin, tan

import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = UiMainWindow
ui.setupUi(MainWindow)

ui.x.setValidator(QtGui.QDoubleValidator())


def formula():
    """
    Вычисление формул
    :return:
    """
    x = float(ui.x.text().replace(",", "."))
    a = ui.a.value()
    t = ui.t.value()
    # y = tan(x  2 / 2 - 1)  2 + (2 * cos(x - pi / 6)) / (0.5 + sin(a) ** 2)
    alpha_radians = radians(x)
    result_1 = (1 - 2 * sin(alpha_radians) ** 2) / (1 + sin(2 * alpha_radians))
    result_2 = (1 - tan(alpha_radians)) / (1 + tan(alpha_radians))

    ui.rez2.setText(str(round(result_1, t)))


def clear():
    ui.x.setText('0')
    ui.a.setValue(0.00)
    ui.t.setValue(0)
    ui.rez2.clear()
    ui.rez1.clear()


ui.clear.clicked.connect(clear)
ui.rezult.clicked.connect(formula)

MainWindow.show()
sys.exit(app.exec())
