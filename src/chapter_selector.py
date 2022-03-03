#!/usr/bin/env python3
# Made By Thicc-Juice
# What The Git!
import os

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer


class ui_chapter_selection_window(object):
    def __init__(self, window):
        window.setObjectName("chapter_selection_window")
        window.resize(1280, 720)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(window.sizePolicy().hasHeightForWidth())
        window.setSizePolicy(size_policy)
        window.setMaximumSize(QtCore.QSize(1280, 720))
        window.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.chapter_selection_screen_central_widget = QtWidgets.QWidget(window)
        self.chapter_selection_screen_central_widget.setObjectName("chapter_selection_screen_central_widget")
        self.chapter_selection_screen_frame = QtWidgets.QFrame(self.chapter_selection_screen_central_widget)
        self.chapter_selection_screen_frame.setGeometry(QtCore.QRect(0, 0, 1280, 720))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.chapter_selection_screen_frame.sizePolicy().hasHeightForWidth())

        self.chapter_selection_screen_frame.setSizePolicy(size_policy)
        self.chapter_selection_screen_frame.setAutoFillBackground(False)
        self.chapter_selection_screen_frame.setStyleSheet("background-color: rgb(71, 71, 71);")
        self.chapter_selection_screen_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chapter_selection_screen_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chapter_selection_screen_frame.setObjectName("chapter_selection_screen_frame")

        self.start_screen_background = QtWidgets.QLabel(self.chapter_selection_screen_frame)
        self.start_screen_background.setGeometry(QtCore.QRect(0, 0, 1280, 720))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.start_screen_background.sizePolicy().hasHeightForWidth())

        self.start_screen_background.setSizePolicy(size_policy)
        font = QtGui.QFont()

        self.start_screen_background.setFont(font)
        self.start_screen_background.setText("")
        self.start_screen_background.setPixmap(QtGui.QPixmap("images/background.png"))
        self.start_screen_background.setScaledContents(True)
        self.start_screen_background.setObjectName("start_screen_background")

        self.toggle_music_button = QtWidgets.QPushButton(self.chapter_selection_screen_frame)
        self.toggle_music_button.setGeometry(QtCore.QRect(20, 10, 120, 30))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.toggle_music_button.sizePolicy().hasHeightForWidth())

        self.toggle_music_button.setSizePolicy(size_policy)
        self.toggle_music_button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        self.toggle_music_button.setFont(font)
        self.toggle_music_button.setStyleSheet("QPushButton {\n"
                                               "    border: 1px solid #F4D782;\n"
                                               "    font-size: 14px;\n"
                                               "    color: #F4D782;\n"
                                               "    padding: 1px;\n"
                                               "    border-radius:10px;\n"
                                               "    background: none\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "    background: #F4D780;\n"
                                               "    color: black\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:pressed {\n"
                                               "    background-color: rgb(255, 210, 103);\n"
                                               "    color: black\n"
                                               "}")
        self.toggle_music_button.setObjectName("toggle_music_button")

        self.chapter_one_start_button = QtWidgets.QPushButton(self.chapter_selection_screen_frame)
        self.chapter_one_start_button.setGeometry(QtCore.QRect(470, 260, 331, 61))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.chapter_one_start_button.sizePolicy().hasHeightForWidth())
        self.chapter_one_start_button.setSizePolicy(size_policy)
        self.chapter_one_start_button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.chapter_one_start_button.setFont(font)
        self.chapter_one_start_button.setStyleSheet("QPushButton {\n"
                                                    "    border: 1px solid #F4D780;\n"
                                                    "       font: 18pt \"Montserrat\";\n"
                                                    "    color: white;\n"
                                                    "    padding: 1px;\n"
                                                    "    border-radius:20px;\n"
                                                    "    background: black\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:hover {\n"
                                                    "    background: #F4D780;\n"
                                                    "    color: black\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:pressed {\n"
                                                    "    background-color: rgb(255, 210, 103);\n"
                                                    "    color: black\n"
                                                    "}")
        self.chapter_one_start_button.setObjectName("chapter_one_start_button")

        self.chapter_two_start_button = QtWidgets.QPushButton(self.chapter_selection_screen_frame)
        self.chapter_two_start_button.setGeometry(QtCore.QRect(470, 370, 331, 61))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.chapter_two_start_button.sizePolicy().hasHeightForWidth())

        self.chapter_two_start_button.setSizePolicy(size_policy)
        self.chapter_two_start_button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.chapter_two_start_button.setFont(font)
        self.chapter_two_start_button.setStyleSheet("QPushButton {\n"
                                                    "    border: 1px solid #F4D780;\n"
                                                    "       font: 18pt \"Montserrat\";\n"
                                                    "    color: white;\n"
                                                    "    padding: 1px;\n"
                                                    "    border-radius:20px;\n"
                                                    "    background: black\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:hover {\n"
                                                    "    background: #F4D780;\n"
                                                    "    color: black\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:pressed {\n"
                                                    "    background-color: rgb(255, 210, 103);\n"
                                                    "    color: black\n"
                                                    "}")
        self.chapter_two_start_button.setObjectName("chapter_two_start_button")

        # self.chapter_three_start_button = QtWidgets.QPushButton(self.chapter_selection_screen_frame)
        # self.chapter_three_start_button.setGeometry(QtCore.QRect(470, 480, 331, 61))
        # size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # size_policy.setHorizontalStretch(0)
        # size_policy.setVerticalStretch(0)
        # size_policy.setHeightForWidth(self.chapter_three_start_button.sizePolicy().hasHeightForWidth())
        # self.chapter_three_start_button.setSizePolicy(size_policy)
        # self.chapter_three_start_button.setMinimumSize(QtCore.QSize(0, 0))
        # font = QtGui.QFont()
        # font.setFamily("Montserrat")
        # font.setPointSize(18)
        # font.setBold(False)
        # font.setItalic(False)
        # self.chapter_three_start_button.setFont(font)
        # self.chapter_three_start_button.setStyleSheet("QPushButton {\n"
        #                                               "    border: 1px solid #F4D780;\n"
        #                                               "       font: 18pt \"Montserrat\";\n"
        #                                               "    color: white;\n"
        #                                               "    padding: 1px;\n"
        #                                               "    border-radius:20px;\n"
        #                                               "    background: black\n"
        #                                               "}\n"
        #                                               "\n"
        #                                               "QPushButton:hover {\n"
        #                                               "    background: #F4D780;\n"
        #                                               "    color: black\n"
        #                                               "}\n"
        #                                               "\n"
        #                                               "QPushButton:pressed {\n"
        #                                               "    background-color: rgb(255, 210, 103);\n"
        #                                               "    color: black\n"
        #                                               "}")
        # self.chapter_three_start_button.setObjectName("chapter_three_start_button")

        self.select_chapter_label = QtWidgets.QLabel(self.chapter_selection_screen_frame)
        self.select_chapter_label.setGeometry(QtCore.QRect(450, 30, 371, 151))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(48)
        self.select_chapter_label.setFont(font)
        self.select_chapter_label.setStyleSheet("background:none;")
        self.select_chapter_label.setObjectName("select_chapter_label_2")

        window.setCentralWidget(self.chapter_selection_screen_central_widget)
        self.retranslate(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslate(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("chapter_selection_window", "MainWindow"))
        self.toggle_music_button.setText(_translate("chapter_selection_window", "Toggle Music"))
        self.chapter_two_start_button.setText(_translate("chapter_selection_window", "Chapter 2: Branching"))
        self.chapter_one_start_button.setText(_translate("chapter_selection_window", "Chapter 1: First Commit"))
        self.select_chapter_label.setText(_translate("chapter_selection_window", "Select Chapter"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    chapter_selection_window = QtWidgets.QMainWindow()
    ui = ui_chapter_selection_window(chapter_selection_window)
    chapter_selection_window.show()
    sys.exit(app.exec_())
