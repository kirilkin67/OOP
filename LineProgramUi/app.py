from PyQt6 import QtGui, QtWidgets
from solution import Ui_MainWindow
from math import radians, sin, tan

import sys


def clear():
    ui.alfa.setText('0')
    ui.precision.setValue(0)
    ui.result_1.clear()
    ui.result_2.clear()


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


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

ui.alfa.setValidator(QtGui.QIntValidator())
ui.clear.clicked.connect(clear)
# ui.rezult.clicked.connect(formula)

MainWindow.show()
sys.exit(app.exec())
