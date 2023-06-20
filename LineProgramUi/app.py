from PyQt6 import QtGui, QtWidgets
from solution import Ui_MainWindow
from math import radians, sin, tan

import sys

COLOR_RED = "rgb(200, 0, 0)"
COLOR_WHITE = "rgb(255, 255, 255)"


def clear():
    ui.alfa.setText('0')
    ui.precision.setValue(0)
    style_sheet = f"background-color: {COLOR_WHITE}; border: 3px solid rgb(0, 0, 127);"
    ui.result_1.clear()
    ui.result_1.setStyleSheet(style_sheet)
    ui.result_2.clear()
    ui.result_2.setStyleSheet(style_sheet)


def setErrorMessageResult(line_edit: QtWidgets.QLineEdit, rgb):
    font = QtGui.QFont()
    font.setPointSize(16)
    line_edit.setFont(font)
    line_edit.setStyleSheet(f"background-color: {rgb}; border: 3px solid rgb(0, 0, 127);")
    line_edit.setText("Деление на ноль.")


def calculate():
    """
    Вычисление формул
    """
    try:
        alpha = int(ui.alfa.text())
        precision = ui.precision.value()
        alpha_radians = radians(alpha)
        result_1 = (1 - 2 * sin(alpha_radians) ** 2) / (1 + sin(2 * alpha_radians))
        result_2 = (1 - tan(alpha_radians)) / (1 + tan(alpha_radians))

        ui.result_1.setText(str(round(result_1, precision)))
        ui.result_2.setText(str(round(result_2, precision)))
    except ZeroDivisionError:
        setErrorMessageResult(ui.result_1, COLOR_RED)
        setErrorMessageResult(ui.result_2, COLOR_RED)


def first_formula(alpha_radians: float, precision: int):
    try:
        result = (1 - 2 * sin(alpha_radians) ** 2) / (1 + sin(2 * alpha_radians))
        ui.result_1.setText(str(round(result, precision)))
    except ZeroDivisionError:
        setErrorMessageResult(ui.result_1, COLOR_RED)


def second_formula(alpha_radians: float, precision: int):
    try:
        result_2 = (1 - tan(alpha_radians)) / (1 + tan(alpha_radians))
        ui.result_2.setText(str(round(result_2, precision)))
    except ZeroDivisionError:
        setErrorMessageResult(ui.result_2, COLOR_RED)


def display_form():
    alpha = int(ui.alfa.text())
    alpha_radians = radians(alpha)
    precision = ui.precision.value()

    first_formula(alpha_radians, precision)
    second_formula(alpha_radians, precision)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

ui.alfa.setValidator(QtGui.QIntValidator(0, 360))
# ui.result.clicked.connect(calculate)
ui.result.clicked.connect(display_form)
ui.clear.clicked.connect(clear)

MainWindow.show()
sys.exit(app.exec())
