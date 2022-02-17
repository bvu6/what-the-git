from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 591)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(300, 170, 171, 41))
        self.playButton.setStyleSheet("QPushButton{\n"
"    background-Color: #3250a8;\n"
"    border-radius: 10px;\n"
"    font-size: 30px;\n"
"    font: 25pt \"Georgia\";\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"    background-Color: #4b72e3;\n"
"    border-radius: 10px;\n"
"}")
        self.playButton.setObjectName("playButton")
        self.settingButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingButton.setGeometry(QtCore.QRect(300, 230, 171, 41))
        self.settingButton.setStyleSheet("QPushButton{\n"
"    background-Color: #3250a8;\n"
"    border-radius: 10px;\n"
"    font-size: 30px;\n"
"    font: 25pt \"Georgia\";\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"    background-Color: #4b72e3;\n"
"    border-radius: 10px;\n"
"}")
        self.settingButton.setObjectName("settingButton")
        self.settingButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.settingButton_2.setGeometry(QtCore.QRect(300, 290, 171, 41))
        self.settingButton_2.setStyleSheet("QPushButton{\n"
"    background-Color: #3250a8;\n"
"    border-radius: 10px;\n"
"    font-size: 30px;\n"
"    font: 25pt \"Georgia\";\n"
"}\n"
"\n"
"QPushButton:Hover{\n"
"    background-Color: #4b72e3;\n"
"    border-radius: 10px;\n"
"}")
        self.settingButton_2.setObjectName("settingButton_2")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(220, 60, 331, 61))
        self.title.setStyleSheet("font: 36pt \"Georgia\";\n"
"color: rgb(255, 255, 255);")
        self.title.setObjectName("title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.playButton.setText(_translate("MainWindow", "Level 1"))
        self.settingButton.setText(_translate("MainWindow", "Level 2"))
        self.settingButton_2.setText(_translate("MainWindow", "Level 3"))
        self.title.setText(_translate("MainWindow", "Level Selector"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
