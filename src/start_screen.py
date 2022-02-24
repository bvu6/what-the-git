#!/usr/bin/env python3
# Made By Thicc-Juice
# What The Git!
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class UI_start_window(object):
    def __init__(self, start_window_obj):
        start_window_obj.setObjectName("start_window")
        start_window_obj.resize(1280, 720)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(start_window_obj.sizePolicy().hasHeightForWidth())

        start_window_obj.setSizePolicy(size_policy)
        start_window_obj.setFocusPolicy(QtCore.Qt.ClickFocus)
        start_window_obj.setLayoutDirection(QtCore.Qt.LeftToRight)
        start_window_obj.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.start_screen_central_widget = QtWidgets.QWidget(start_window_obj)
        self.start_screen_central_widget.setObjectName("start_screen_central_widget")
        self.start_screen_frame = QtWidgets.QFrame(self.start_screen_central_widget)
        self.start_screen_frame.setGeometry(QtCore.QRect(0, 0, 1280, 720))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.start_screen_frame.sizePolicy().hasHeightForWidth())

        self.start_screen_frame.setSizePolicy(size_policy)
        self.start_screen_frame.setAutoFillBackground(False)
        self.start_screen_frame.setStyleSheet("background-color: rgb(71, 71, 71);")
        self.start_screen_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.start_screen_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.start_screen_frame.setObjectName("start_screen_frame")

        self.start_screen_background = QtWidgets.QLabel(self.start_screen_frame)
        self.start_screen_background.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.start_screen_background.setText("")
        self.start_screen_background.setPixmap(
            QtGui.QPixmap("images/background.png"))
        self.start_screen_background.setScaledContents(True)
        self.start_screen_background.setObjectName("start_screen_background")

        self.playButton = QtWidgets.QPushButton(self.start_screen_frame)
        self.playButton.setGeometry(QtCore.QRect(520, 560, 221, 41))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())

        self.playButton.setSizePolicy(size_policy)
        self.playButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("QPushButton {\n"
                                      "    border: 1px solid #F4D782;\n"
                                      "    font-size: 20px;\n"
                                      "    color: #F4D782;\n"
                                      "    padding: 1px;\n"
                                      "    border-radius:20px;\n"
                                      "    background:none\n"
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
        self.playButton.setObjectName("playButton")

        self.game_logo = QtWidgets.QLabel(self.start_screen_frame)
        self.game_logo.setGeometry(QtCore.QRect(440, 100, 391, 381))
        self.game_logo.setStyleSheet("background:none")
        self.game_logo.setText("")
        self.game_logo.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.game_logo.setScaledContents(True)
        self.game_logo.setObjectName("game_logo")

        start_window_obj.setCentralWidget(self.start_screen_central_widget)
        self.retranslate(start_window_obj)
        QtCore.QMetaObject.connectSlotsByName(start_window_obj)

    def retranslate(self, start_window_obj_retrans):
        _translate = QtCore.QCoreApplication.translate
        start_window_obj_retrans.setWindowTitle(_translate("start_window", "What The Git!"))
        self.playButton.setText(_translate("start_window", "Start"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    start_screen_ui = UI_start_window(main_window)
    main_window.show()
    sys.exit(app.exec_())
