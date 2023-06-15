import sys
from random import choice

from PyQt6 import QtWidgets

from testForm import Ui_Dialog

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
try:
    with open('test1.txt', encoding='utf-8') as file:
        vopros = [i for i in file.read().replace("\n\n", '\n').split("*****") if i]


    numbers = list(range(len(vopros)))
    nomer = 0
    rezulatat = 0
    otvet = 0


    def cansel():
        ui.asc1.setCheckable(False)
        ui.asc2.setCheckable(False)
        ui.asc3.setCheckable(False)
        ui.asc1.setCheckable(True)
        ui.asc2.setCheckable(True)
        ui.asc3.setCheckable(True)


    def voprosN():
        cansel()
        global numbers, nomer, otvet
        try:
            n = choice(numbers)
            numbers.remove(n)
            vopros1 = vopros[n].split('\n')
            i = 0
            nomer += 1
            ui.number.setText(f'{nomer} из {len(vopros)}')
            if not vopros1[0]: i = 1
            ui.vopros.setText(vopros1[0 + i][3:])
            ui.asc1.setText(vopros1[-4][2:])
            ui.asc2.setText(vopros1[-3][2:])
            ui.asc3.setText(vopros1[-2][2:])
            otvet = 1 if "+" in vopros1[1 + i] else 2 if "+" in vopros1[2 + i] else 3
        except:
            rezult()


    def asc(variant):
        global rezulatat
        if otvet == variant:
            rezulatat += 1


    def new():
        global numbers, nomer, rezulatat, otvet
        numbers = list(range(len(vopros)))
        nomer = 0
        rezulatat = 0
        otvet = 0
        ui.rezult_2.setVisible(False)
        ui.asc1.setEnabled(True)
        ui.asc2.setEnabled(True)
        ui.asc3.setEnabled(True)
        ui.next.setEnabled(True)
        voprosN()


    def rezult():
        ui.vopros.setText(f'Тест закончился у вас {rezulatat} ')
        ui.asc1.setEnabled(False)
        ui.asc2.setEnabled(False)
        ui.asc3.setEnabled(False)
        ui.next.setEnabled(False)
        ui.rezult_2.setVisible(True)


    ui.rezult_2.setVisible(False)
    voprosN()
    ui.rezult_2.clicked.connect(new)
    ui.next.clicked.connect(voprosN)
    ui.asc1.clicked.connect(lambda: asc(1))
    ui.asc2.clicked.connect(lambda: asc(2))
    ui.asc3.clicked.connect(lambda: asc(3))
    ui.rezult.clicked.connect(rezult)
except:
    ui.vopros.setText('нет файла')
    ui.asc1.setVisible(False)
    ui.asc2.setVisible(False)
    ui.asc3.setVisible(False)
    ui.next.setVisible(False)
    ui.rezult_2.setVisible(False)
    ui.number.setVisible(False)
Dialog.show()
sys.exit(app.exec())
