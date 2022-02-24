#!/usr/bin/env python3
# Made By Thicc-Juice
# What The Git!

from PyQt5 import QtWidgets
from chapter_selector import LevelWindow
from start_screen import UI_start_window
import sys


class MainWindow:

    def __init__(self):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = UI_start_window(self.main_window)
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.stacked_widget.addWidget(self.main_window)
        self.stacked_widget.setFixedWidth(1280)
        self.stacked_widget.setFixedHeight(720)
        self.stacked_widget.show()
        self.ui.playButton.clicked.connect(lambda: self.switch_to_level_selector())

    def switch_to_level_selector(self):
        self.stacked_widget.hide()
        self.stacked_widget.removeWidget(self.main_window)
        self.ui = LevelWindow(self.main_window)
        self.stacked_widget.addWidget(self.main_window)
        self.stacked_widget.show()

    def switch_to_level_one(self):
        self.stacked_widget.hide()
        self.stacked_widget.removeWidget(self.main_window)
        self.ui = LevelWindow(self.main_window)
        self.stacked_widget.addWidget(self.main_window)
        self.stacked_widget.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
