# Form implementation generated from reading ui file 'solution.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(550, 500))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(78, 120, 166, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 491, 100))
        self.label.setMinimumSize(QtCore.QSize(490, 100))
        self.label.setStyleSheet("border: 3px solid rgb(0, 0, 255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image.jpg"))
        self.label.setObjectName("label")
        self.close = QtWidgets.QPushButton(parent=self.centralwidget)
        self.close.setGeometry(QtCore.QRect(280, 400, 230, 50))
        self.close.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        self.close.setFont(font)
        self.close.setStyleSheet("background-color: rgb(152, 0, 0);\n"
"\n"
"border: 5px outset rgb(255, 0, 0);\n"
"border-radius:20px\n"
"")
        self.close.setObjectName("close")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 330, 481, 52))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.result = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.result.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        self.result.setFont(font)
        self.result.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"background-color: rgb(110, 240, 169);\n"
"border: 5px outset rgb(0, 85, 0);\n"
"border-radius:20px\n"
"")
        self.result.setObjectName("result")
        self.horizontalLayout_3.addWidget(self.result)
        self.clear = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.clear.setMinimumSize(QtCore.QSize(230, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        self.clear.setFont(font)
        self.clear.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"background-color: rgb(110, 240, 169);\n"
"border: 5px outset rgb(0, 85, 0);\n"
"border-radius:20px\n"
"")
        self.clear.setObjectName("clear")
        self.horizontalLayout_3.addWidget(self.clear)
        self.alfa = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.alfa.setGeometry(QtCore.QRect(180, 220, 100, 33))
        self.alfa.setMinimumSize(QtCore.QSize(100, 33))
        self.alfa.setMaximumSize(QtCore.QSize(100, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.alfa.setFont(font)
        self.alfa.setStyleSheet("border: 3px solid rgb(0, 0, 127);")
        self.alfa.setInputMask("")
        self.alfa.setMaxLength(3)
        self.alfa.setObjectName("alfa")
        self.name_precision = QtWidgets.QLabel(parent=self.centralwidget)
        self.name_precision.setGeometry(QtCore.QRect(30, 270, 150, 33))
        self.name_precision.setMinimumSize(QtCore.QSize(150, 33))
        self.name_precision.setMaximumSize(QtCore.QSize(150, 33))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.name_precision.setFont(font)
        self.name_precision.setStyleSheet("background-color: rgb(127, 254, 188);\n"
"border: 3px solid rgb(0,254, 255);")
        self.name_precision.setObjectName("name_precision")
        self.name_alfa = QtWidgets.QLabel(parent=self.centralwidget)
        self.name_alfa.setGeometry(QtCore.QRect(30, 220, 150, 33))
        self.name_alfa.setMinimumSize(QtCore.QSize(150, 33))
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
        self.name_alfa.setObjectName("name_alfa")
        self.precision = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.precision.setGeometry(QtCore.QRect(180, 270, 100, 33))
        self.precision.setMinimumSize(QtCore.QSize(100, 33))
        self.precision.setMaximumSize(QtCore.QSize(100, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.precision.setFont(font)
        self.precision.setStyleSheet("border: 3px solid rgb(0, 0, 127);")
        self.precision.setMaximum(10)
        self.precision.setObjectName("precision")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 160, 491, 38))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.result_1 = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.result_1.setMinimumSize(QtCore.QSize(220, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.result_1.setFont(font)
        self.result_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(0, 0, 127);")
        self.result_1.setText("")
        self.result_1.setMaxLength(20)
        self.result_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.result_1.setReadOnly(True)
        self.result_1.setObjectName("result_1")
        self.horizontalLayout.addWidget(self.result_1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.result_2 = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.result_2.setMinimumSize(QtCore.QSize(220, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.result_2.setFont(font)
        self.result_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.result_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(0, 0, 127);")
        self.result_2.setInputMask("")
        self.result_2.setText("")
        self.result_2.setMaxLength(20)
        self.result_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.result_2.setReadOnly(True)
        self.result_2.setObjectName("result_2")
        self.horizontalLayout.addWidget(self.result_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clear.clicked.connect(self.precision.clear) # type: ignore
        self.clear.clicked.connect(self.alfa.clear) # type: ignore
        self.clear.clicked.connect(self.result_2.clear) # type: ignore
        self.close.clicked.connect(MainWindow.close) # type: ignore
        self.clear.clicked.connect(self.result_1.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Решение линейного урвнения"))
        self.close.setText(_translate("MainWindow", "Закрыть"))
        self.result.setText(_translate("MainWindow", "Результат"))
        self.clear.setText(_translate("MainWindow", "Очистить"))
        self.alfa.setText(_translate("MainWindow", "0"))
        self.name_precision.setText(_translate("MainWindow", "Точность"))
        self.name_alfa.setText(_translate("MainWindow", "ALFA, градусы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
