#!/usr/bin/env python3
# Made By Thicc-Juice
# What The Git!

import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from level_selector import LevelWindow


class Start_Window(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = LevelWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 596)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(300, 220, 171, 41))
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
        self.playButton.clicked.connect(self.openWindow)
        self.settingButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingButton.setGeometry(QtCore.QRect(300, 300, 171, 41))
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
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(230, 80, 331, 61))
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

        self.retranslateUI(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUI(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.settingButton.setText(_translate("MainWindow", "Settings"))
        self.title.setText(_translate("MainWindow", "What the Git!"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Start_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())