from PyQt6 import QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from form import Ui_MainWindow
import sys

COLOR_RED = "rgb(200, 0, 0)"
COLOR_WHITE = "rgb(255, 255, 255)"


def clear():
    ui.imput.setText('')
    ui.result.clear()
    set_stylesheet(ui.result, COLOR_WHITE)


def set_stylesheet(line_edit: QtWidgets.QLineEdit, color_rgb):
    stylesheet = f"background-color: {color_rgb}; border: 3px solid rgb(0, 0, 127);"
    line_edit.setStyleSheet(stylesheet)


def calculate(integer: int):
    """
        В трехзначном числе x зачеркнули его вторую цифру.
        Когда к образованному при этом двузначному числу слева приписали вторую цифру числа x,
        а затем результат удвоили, то получили искомое число.
    """
    first_num, integer = divmod(integer, 100)
    second_num, third_num = divmod(integer, 10)
    integer = (second_num * 100 + first_num * 10 + third_num) * 2
    return str(integer)


def show_dialog():
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Информационное сообщение")
    msg_box.setText("Необходимо ввести трёхзначное число")
    msg_box.setIcon(QMessageBox.Icon.Information)
    msg_box.exec()


def validate_input(integer: int):
    if integer < 100:
        show_dialog()


def display_form():
    integer = int(ui.imput.text())
    validate_input(integer)
    ui.result.setText(calculate(integer))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

ui.imput.setValidator(QtGui.QIntValidator(100, 999))
ui.clear.clicked.connect(clear)
ui.button_result.clicked.connect(display_form)

MainWindow.show()
sys.exit(app.exec())
