# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 554)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(900, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rez1 = QtWidgets.QLineEdit(self.centralwidget)
        self.rez1.setGeometry(QtCore.QRect(480, 70, 389, 39))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rez1.setFont(font)
        self.rez1.setReadOnly(True)
        self.rez1.setObjectName("rez1")
        self.rez2 = QtWidgets.QLabel(self.centralwidget)
        self.rez2.setGeometry(QtCore.QRect(480, 180, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rez2.setFont(font)
        self.rez2.setText("")
        self.rez2.setObjectName("rez2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 442, 384))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("formula.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WaitCursor))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.x = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.x.setFont(font)
        self.x.setObjectName("x")
        self.horizontalLayout.addWidget(self.x)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WaitCursor))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.a = QtWidgets.QDoubleSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.a.setFont(font)
        self.a.setObjectName("a")
        self.horizontalLayout_2.addWidget(self.a)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WaitCursor))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.t = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.t.setFont(font)
        self.t.setObjectName("t")
        self.horizontalLayout_3.addWidget(self.t)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(31, 441, 441, 51))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rezult = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rezult.setFont(font)
        self.rezult.setObjectName("rezult")
        self.horizontalLayout_4.addWidget(self.rezult)
        self.clear = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.horizontalLayout_4.addWidget(self.clear)
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionuygouygli = QtGui.QAction(MainWindow)
        self.actionuygouygli.setObjectName("actionuygouygli")
        self.actionvhlikl = QtGui.QAction(MainWindow)
        self.actionvhlikl.setObjectName("actionvhlikl")
        self.action45 = QtGui.QAction(MainWindow)
        self.action45.setObjectName("action45")

        self.retranslateUi(MainWindow)
        self.clear.clicked.connect(self.t.clear) # type: ignore
        self.clear.clicked.connect(self.a.clear) # type: ignore
        self.clear.clicked.connect(self.x.clear) # type: ignore
        self.pushButton.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Формула"))
        self.label_2.setText(_translate("MainWindow", "X="))
        self.x.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Альфа ="))
        self.label_4.setText(_translate("MainWindow", "Точность="))
        self.rezult.setText(_translate("MainWindow", "Результат "))
        self.clear.setText(_translate("MainWindow", "Очистить"))
        self.pushButton.setText(_translate("MainWindow", "Закрыть "))
        self.action.setText(_translate("MainWindow", "нагммнд"))
        self.actionuygouygli.setText(_translate("MainWindow", "uygouygli"))
        self.actionvhlikl.setText(_translate("MainWindow", "vhlikl"))
        self.action45.setText(_translate("MainWindow", "45"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())