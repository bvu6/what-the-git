#!/usr/bin/env python3
# Made By Thicc-Juice
# What The Git!

from PyQt5 import QtWidgets
from level_selector import LevelWindow
from start_screen import Ui_MainWindow
import sys


def switch_to_level_selector_window(self):
    self.window = QtWidgets.QMainWindow()
    self.ui = LevelWindow()
    self.ui.setupUI(self.window)
    self.window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    stacked_widget = QtWidgets.QStackedWidget()
    MainWindow = QtWidgets.QMainWindow()

    stacked_widget.add(start_s)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
