#!/usr/bin/env python3
# Made By Thicc-Juice
# What The Git!

from PyQt5 import QtCore, QtGui, QtWidgets
from level_selector import LevelWindow

class Ui_MainWindow(object):
    def switch_to_level_selector_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = LevelWindow()
        self.ui.setupUI(self.window)
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
        self.playButton.setGeometry(QtCore.QRect(300, 310, 171, 41))
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
        self.playButton.clicked.connect(self.switch_to_level_selector_window) #switch windows
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 30, 321, 241))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo_octocat.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.playButton.setText(_translate("MainWindow", "Play"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
