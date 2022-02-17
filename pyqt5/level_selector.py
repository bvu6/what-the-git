#!/usr/bin/env python3
# Made By Thicc-Juice

from PyQt5 import QtCore, QtGui, QtWidgets


class LevelWindow(object):
    def setupUi(self, LevelWindow):
        LevelWindow.setObjectName("Level_Window")
        LevelWindow.resize(800, 591)
        LevelWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(LevelWindow)
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
        LevelWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LevelWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        LevelWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LevelWindow)
        self.statusbar.setObjectName("statusbar")
        LevelWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LevelWindow)
        QtCore.QMetaObject.connectSlotsByName(LevelWindow)

    def retranslateUi(self, LevelWindow):
        _translate = QtCore.QCoreApplication.translate
        LevelWindow.setWindowTitle(_translate("LevelWindow", "LevelWindow"))
        self.playButton.setText(_translate("LevelWindow", "Level 1"))
        self.settingButton.setText(_translate("LevelWindow", "Level 2"))
        self.settingButton_2.setText(_translate("LevelWindow", "Level 3"))
        self.title.setText(_translate("LevelWindow", "Level Selector"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Level_Window = QtWidgets.QMainWindow()
    ui = Level_Window()
    ui.setupUi(Level_Window)
    Level_Window.show()
    sys.exit(app.exec_())
