# Form implementation generated from reading ui file '.\form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(530, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        MainWindow.setStyleSheet("QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 145, 65, 221), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.95, stop:0 rgba(145, 235, 106, 255), stop:0.740113 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(78, 120, 166, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(145, 235, 106, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(170, 255, 127);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.close = QtWidgets.QPushButton(parent=self.centralwidget)
        self.close.setGeometry(QtCore.QRect(190, 470, 120, 71))
        self.close.setMinimumSize(QtCore.QSize(120, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        self.close.setFont(font)
        self.close.setStyleSheet("background-color: rgb(152, 0, 0);\n"
"border: 5px outset rgb(255, 0, 0);\n"
"border-radius: 20px;\n"
"")
        self.close.setObjectName("close")
        self.imput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.imput.setGeometry(QtCore.QRect(230, 130, 100, 80))
        self.imput.setMinimumSize(QtCore.QSize(100, 80))
        self.imput.setMaximumSize(QtCore.QSize(100, 33))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(24)
        font.setBold(True)
        self.imput.setFont(font)
        self.imput.setStyleSheet("border: 3px solid rgb(0, 0, 127);\n"
"background-color: rgb(255, 255, 255);\n"
"box-shadow: 10px 20px 30px 15px rgb(0, 0, 0, 0.5);")
        self.imput.setInputMask("")
        self.imput.setText("")
        self.imput.setMaxLength(3)
        self.imput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.imput.setObjectName("imput")
        self.name_alfa = QtWidgets.QLabel(parent=self.centralwidget)
        self.name_alfa.setGeometry(QtCore.QRect(140, 150, 83, 50))
        self.name_alfa.setMinimumSize(QtCore.QSize(50, 50))
        self.name_alfa.setMaximumSize(QtCore.QSize(150, 33))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.name_alfa.setFont(font)
        self.name_alfa.setTabletTracking(True)
        self.name_alfa.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border: 3px solid rgb(0, 127, 127);")
        self.name_alfa.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.name_alfa.setObjectName("name_alfa")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 480, 51))
        self.label_2.setMinimumSize(QtCore.QSize(480, 50))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 16pt \"Garamond\";\n"
"font: 700 italic 20pt \"Book Antiqua\";\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 220, 491, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 16pt \"Garamond\";\n"
"font: 700 italic 16pt \"Book Antiqua\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.result = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.result.setMinimumSize(QtCore.QSize(150, 80))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(24)
        font.setBold(True)
        self.result.setFont(font)
        self.result.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(0, 0, 127);")
        self.result.setText("")
        self.result.setMaxLength(100)
        self.result.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.result.setReadOnly(True)
        self.result.setObjectName("result")
        self.horizontalLayout.addWidget(self.result)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_result = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.button_result.setMinimumSize(QtCore.QSize(240, 80))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(True)
        self.button_result.setFont(font)
        self.button_result.setStyleSheet("background-color: rgb(110, 240, 169);\n"
"border: 15px outset rgb(0, 85, 0);\n"
"border: 10px inset rgb(0, 85, 0);\n"
"color: white;\n"
"background-color: qconicalgradient(cx:0.381, cy:0.455, angle:0, stop:0.0508475 rgba(13, 213, 51, 255), stop:0.16 rgba(0, 154, 22, 255), stop:0.231638 rgba(40, 140, 83, 255), stop:0.285 rgba(67, 181, 74, 255), stop:0.345 rgba(101, 219, 102, 255), stop:0.415 rgba(112, 236, 170, 255), stop:0.52 rgba(80, 190, 76, 255), stop:0.57 rgba(80, 156, 51, 255), stop:0.635 rgba(65, 142, 42, 255), stop:0.695 rgba(54, 174, 68, 255), stop:0.75 rgba(94, 202, 86, 255), stop:0.815 rgba(139, 187, 73, 255), stop:0.88 rgba(0, 156, 51, 255), stop:0.935 rgba(118, 174, 26, 255), stop:1 rgba(65, 212, 13, 255));\n"
"\n"
"")
        self.button_result.setObjectName("button_result")
        self.horizontalLayout_2.addWidget(self.button_result)
        self.clear = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.clear.setMinimumSize(QtCore.QSize(50, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        self.clear.setFont(font)
        self.clear.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"background-color: rgb(110, 240, 169);\n"
"color: white;\n"
"border: 10px outset rgb(0, 85, 0);\n"
"background-color: qconicalgradient(cx:0.381, cy:0.455, angle:0, stop:0.0508475 rgba(13, 213, 51, 255), stop:0.16 rgba(0, 154, 22, 255), stop:0.231638 rgba(40, 140, 83, 255), stop:0.285 rgba(67, 181, 74, 255), stop:0.345 rgba(101, 219, 102, 255), stop:0.415 rgba(112, 236, 170, 255), stop:0.52 rgba(80, 190, 76, 255), stop:0.57 rgba(80, 156, 51, 255), stop:0.635 rgba(65, 142, 42, 255), stop:0.695 rgba(54, 174, 68, 255), stop:0.75 rgba(94, 202, 86, 255), stop:0.815 rgba(139, 187, 73, 255), stop:0.88 rgba(0, 156, 51, 255), stop:0.935 rgba(118, 174, 26, 255), stop:1 rgba(65, 212, 13, 255));\n"
"box-shadow: 10px 20px 30px 15px rgb(0, 0, 0, 0.5);\n"
"")
        self.clear.setObjectName("clear")
        self.horizontalLayout_2.addWidget(self.clear)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clear.clicked.connect(self.imput.clear) # type: ignore
        self.clear.clicked.connect(self.result.clear) # type: ignore
        self.close.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Операции над числами"))
        self.close.setText(_translate("MainWindow", "Закрыть"))
        self.name_alfa.setText(_translate("MainWindow", "X ="))
        self.label_2.setText(_translate("MainWindow", "Введите трёхзначное число"))
        self.label.setText(_translate("MainWindow", "Результат\n"
"преобразования"))
        self.button_result.setText(_translate("MainWindow", "Результат"))
        self.clear.setText(_translate("MainWindow", "Очистить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
