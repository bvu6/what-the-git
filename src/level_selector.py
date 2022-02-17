#!/usr/bin/env python3
# Made By Thicc-Juice

from PyQt5 import QtCore, QtGui, QtWidgets
from chapter_base import UI_MainChapterWindow
import sys


class LevelWindow(object):
    def switch_to_level_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_MainChapterWindow()
        self.ui.setupUI(self.window)
        self.window.show()

    def setupUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 591)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lvl_one_button = QtWidgets.QPushButton(self.centralwidget)
        self.lvl_one_button.setGeometry(QtCore.QRect(300, 170, 171, 41))
        self.lvl_one_button.setStyleSheet("QPushButton{\n"
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
        self.lvl_one_button.setObjectName("lvl_one_button")
        self.lvl_one_button.clicked.connect(self.switch_to_level_window)

        self.lvl_two_button = QtWidgets.QPushButton(self.centralwidget)
        self.lvl_two_button.setGeometry(QtCore.QRect(300, 230, 171, 41))
        self.lvl_two_button.setStyleSheet("QPushButton{\n"
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
        self.lvl_two_button.setObjectName("lvl_two_button")
        self.lvl_three_button = QtWidgets.QPushButton(self.centralwidget)
        self.lvl_three_button.setGeometry(QtCore.QRect(300, 290, 171, 41))
        self.lvl_three_button.setStyleSheet("QPushButton{\n"
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
        self.lvl_three_button.setObjectName("lvl_three_button")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(270, 60, 331, 61))
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
        self.lvl_one_button.setText(_translate("MainWindow", "Level 1"))
        self.lvl_two_button.setText(_translate("MainWindow", "Level 2"))
        self.lvl_three_button.setText(_translate("MainWindow", "Level 3"))
        self.title.setText(_translate("MainWindow", "Level Selector"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Level_Window = QtWidgets.QMainWindow()
    ui = LevelWindow()
    ui.setupUI(Level_Window)
    Level_Window.show()
    sys.exit(app.exec_())
