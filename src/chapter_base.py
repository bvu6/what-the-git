#!/usr/bin/env python3
# Made By Bikram Chatterjee

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia


class UI_MainChapterWindow(object):
    def setupUI(self, MainChapterWindow):
        MainChapterWindow.setObjectName("MainChapterWindow")
        MainChapterWindow.resize(1164, 900)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainChapterWindow.sizePolicy().hasHeightForWidth())

        MainChapterWindow.setSizePolicy(sizePolicy)
        MainChapterWindow.setMinimumSize(QtCore.QSize(900, 530))
        MainChapterWindow.setMaximumSize(QtCore.QSize(1920, 900))

        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)

        MainChapterWindow.setFont(font)
        MainChapterWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.main_chapter_central_widget = QtWidgets.QWidget(MainChapterWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_chapter_central_widget.sizePolicy().hasHeightForWidth())

        self.main_chapter_central_widget.setSizePolicy(sizePolicy)
        self.main_chapter_central_widget.setMinimumSize(QtCore.QSize(900, 530))
        self.main_chapter_central_widget.setMaximumSize(QtCore.QSize(1920, 900))

        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)

        self.main_chapter_central_widget.setFont(font)
        self.main_chapter_central_widget.setStyleSheet("")
        self.main_chapter_central_widget.setObjectName("main_chapter_central_widget")

        self.gridLayout = QtWidgets.QGridLayout(self.main_chapter_central_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.main_chapter_frame = QtWidgets.QFrame(self.main_chapter_central_widget)
        self.main_chapter_frame.setEnabled(True)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_chapter_frame.sizePolicy().hasHeightForWidth())

        self.main_chapter_frame.setSizePolicy(sizePolicy)
        self.main_chapter_frame.setMinimumSize(QtCore.QSize(900, 530))
        self.main_chapter_frame.setMaximumSize(QtCore.QSize(1920, 1000))

        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)

        self.main_chapter_frame.setFont(font)
        self.main_chapter_frame.setStyleSheet("background-color: rgb(18, 18, 18);")
        self.main_chapter_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_chapter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_chapter_frame.setObjectName("main_chapter_frame")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.main_chapter_frame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.main_chapter_layout = QtWidgets.QGridLayout()
        self.main_chapter_layout.setHorizontalSpacing(5)
        self.main_chapter_layout.setVerticalSpacing(1)
        self.main_chapter_layout.setObjectName("main_chapter_layout")

        self.card_holder_frame = QtWidgets.QFrame(self.main_chapter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_holder_frame.sizePolicy().hasHeightForWidth())

        self.card_holder_frame.setSizePolicy(sizePolicy)
        self.card_holder_frame.setStyleSheet("background-color: rgb(27, 35, 54); \n"
                                             "margin:5px;\n"
                                             "border-radius: 5px;")
        self.card_holder_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card_holder_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card_holder_frame.setObjectName("card_holder_frame")

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.card_holder_frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.main_chapter_layout.addWidget(self.card_holder_frame, 2, 0, 1, 1)
        self.chapter_info_frame = QtWidgets.QFrame(self.main_chapter_frame)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chapter_info_frame.sizePolicy().hasHeightForWidth())

        self.chapter_info_frame.setSizePolicy(sizePolicy)
        self.chapter_info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chapter_info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chapter_info_frame.setObjectName("chapter_info_frame")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.chapter_info_frame)
        self.gridLayout_4.setContentsMargins(0, 0, 5, 0)
        self.gridLayout_4.setVerticalSpacing(4)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.chapter_info_layout = QtWidgets.QVBoxLayout()
        self.chapter_info_layout.setObjectName("chapter_info_layout")

        self.scrollArea = QtWidgets.QScrollArea(self.chapter_info_frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 422, 238))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())

        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)

        font = QtGui.QFont()
        font.setFamily("Montserrat")

        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_5.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.chapter_info_layout.addWidget(self.scrollArea)
        self.gridLayout_4.addLayout(self.chapter_info_layout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.task_one = QtWidgets.QLabel(self.chapter_info_frame)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_one.sizePolicy().hasHeightForWidth())

        self.task_one.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.task_one.setFont(font)
        self.task_one.setStyleSheet("background-color: rgb(138, 0, 1);\n"
                                    "border-radius: 5px; \n"
                                    "padding-left:5px")
        self.task_one.setObjectName("task_one")
        self.verticalLayout.addWidget(self.task_one)
        self.task_two = QtWidgets.QLabel(self.chapter_info_frame)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_two.sizePolicy().hasHeightForWidth())

        self.task_two.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.task_two.setFont(font)
        self.task_two.setStyleSheet("background-color: rgb(138, 0, 1);\n"
                                    "border-radius: 5px; \n"
                                    "padding-left:5px")
        self.task_two.setObjectName("task_two")

        self.verticalLayout.addWidget(self.task_two)
        self.task_three = QtWidgets.QLabel(self.chapter_info_frame)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_three.sizePolicy().hasHeightForWidth())
        self.task_three.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setFamily("Montserrat")

        self.task_three.setFont(font)
        self.task_three.setStyleSheet("background-color: rgb(138, 0, 1);\n"
                                      "border-radius: 5px; \n"
                                      "padding-left:5px")
        self.task_three.setObjectName("task_three")
        self.verticalLayout.addWidget(self.task_three)
        self.gridLayout_4.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.files_frame = QtWidgets.QFrame(self.chapter_info_frame)
        self.files_frame.setStyleSheet("background-color: rgb(0, 157, 255);border-radius: 5px")
        self.files_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.files_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.files_frame.setObjectName("files_frame")

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.files_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.files_layout = QtWidgets.QHBoxLayout()
        self.files_layout.setSpacing(6)
        self.files_layout.setObjectName("files_layout")
        self.file1 = QtWidgets.QTextBrowser(self.files_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file1.sizePolicy().hasHeightForWidth())

        self.file1.setSizePolicy(sizePolicy)
        self.file1.setMaximumSize(QtCore.QSize(60, 16777215))
        self.file1.setObjectName("file1")
        self.files_layout.addWidget(self.file1)
        self.horizontalLayout_5.addLayout(self.files_layout)

        self.gridLayout_4.addWidget(self.files_frame, 2, 0, 1, 1)
        self.gridLayout_4.setRowStretch(0, 5)
        self.gridLayout_4.setRowStretch(1, 2)
        self.gridLayout_4.setRowStretch(2, 2)

        self.main_chapter_layout.addWidget(self.chapter_info_frame, 1, 1, 1, 1)
        self.title_label = QtWidgets.QLabel(self.main_chapter_frame)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())

        self.title_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(24)

        self.title_label.setFont(font)
        self.title_label.setStyleSheet("align=\"center\" ")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.main_chapter_layout.addWidget(self.title_label, 0, 1, 1, 1)

        self.frame = QtWidgets.QFrame(self.main_chapter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())

        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.commit_view = QtWidgets.QGraphicsView(self.frame)
        self.commit_view.setObjectName("commit_view")

        self.gridLayout_2.addWidget(self.commit_view, 0, 0, 1, 1)
        self.main_chapter_layout.addWidget(self.frame, 1, 0, 1, 1)

        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.button_layout.setContentsMargins(10, 10, 280, 10)
        self.button_layout.setSpacing(20)
        self.button_layout.setObjectName("button_layout")

        self.back_button = QtWidgets.QPushButton(self.main_chapter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.back_button.setFont(font)
        self.back_button.setStyleSheet(
            "background-color: rgb(71, 71, 71);border-radius: 5px;padding-left:10px ;padding-right:10px ")
        self.back_button.setObjectName("back_button")
        self.button_layout.addWidget(self.back_button)
        self.reload_button = QtWidgets.QPushButton(self.main_chapter_frame)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reload_button.sizePolicy().hasHeightForWidth())

        self.reload_button.setSizePolicy(sizePolicy)
        self.reload_button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")

        self.reload_button.setFont(font)
        self.reload_button.setStyleSheet("background-color: rgb(71, 71, 71);border-radius: 5px; ")
        self.reload_button.setObjectName("reload_button")
        self.button_layout.addWidget(self.reload_button)
        self.toggle_music_button = QtWidgets.QPushButton(self.main_chapter_frame)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_music_button.sizePolicy().hasHeightForWidth())

        self.toggle_music_button.setSizePolicy(sizePolicy)
        self.toggle_music_button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.toggle_music_button.setFont(font)
        self.toggle_music_button.setStyleSheet("background-color: rgb(71, 71, 71);border-radius: 5px; ")
        self.toggle_music_button.setObjectName("toggle_music_button")
        self.button_layout.addWidget(self.toggle_music_button)
        self.button_layout.setStretch(0, 1)
        self.button_layout.setStretch(1, 2)
        self.button_layout.setStretch(2, 4)

        self.main_chapter_layout.addLayout(self.button_layout, 0, 0, 1, 1)
        self.cmd_layout = QtWidgets.QVBoxLayout()
        self.cmd_layout.setContentsMargins(-1, 5, 5, 5)
        self.cmd_layout.setSpacing(2)
        self.cmd_layout.setObjectName("cmd_layout")
        self.cmd_output_scroll_area = QtWidgets.QScrollArea(self.main_chapter_frame)
        self.cmd_output_scroll_area.setWidgetResizable(True)
        self.cmd_output_scroll_area.setObjectName("cmd_output_scroll_area")
        self.cmd_output_contents = QtWidgets.QWidget()
        self.cmd_output_contents.setGeometry(QtCore.QRect(0, 0, 425, 157))
        self.cmd_output_contents.setObjectName("cmd_output_contents")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.cmd_output_contents)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.cmd_output_text = QtWidgets.QTextBrowser(self.cmd_output_contents)
        font = QtGui.QFont()
        font.setFamily("Courier New")

        self.cmd_output_text.setFont(font)
        self.cmd_output_text.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.cmd_output_text.setObjectName("cmd_output_text")

        self.horizontalLayout_4.addWidget(self.cmd_output_text)
        self.cmd_output_scroll_area.setWidget(self.cmd_output_contents)
        self.cmd_layout.addWidget(self.cmd_output_scroll_area)
        self.cmd_user_input_box = QtWidgets.QLineEdit(self.main_chapter_frame)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmd_user_input_box.sizePolicy().hasHeightForWidth())
        self.cmd_user_input_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(12)
        self.cmd_user_input_box.setFont(font)
        self.cmd_user_input_box.setStyleSheet("border: 1px solid red;\n"
                                              "border-color: rgb(0, 155, 255);\n"
                                              "border-radius: 5px; \n"
                                              "selection-color: rgb(4, 184, 255);\n"
                                              "background-color: rgb(0, 0, 0);")
        self.cmd_user_input_box.setText("")
        self.cmd_user_input_box.setObjectName("cmd_user_input_box")
        self.cmd_layout.addWidget(self.cmd_user_input_box)
        self.cmd_layout.setStretch(0, 5)
        self.cmd_layout.setStretch(1, 1)

        self.main_chapter_layout.addLayout(self.cmd_layout, 2, 1, 1, 1)
        self.main_chapter_layout.setColumnStretch(0, 5)
        self.main_chapter_layout.setColumnStretch(1, 3)
        self.main_chapter_layout.setRowStretch(0, 1)
        self.main_chapter_layout.setRowStretch(1, 11)
        self.main_chapter_layout.setRowStretch(2, 5)
        self.gridLayout_3.addLayout(self.main_chapter_layout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.main_chapter_frame, 0, 0, 1, 1)
        MainChapterWindow.setCentralWidget(self.main_chapter_central_widget)

        self.retranslateUI(MainChapterWindow)
        QtCore.QMetaObject.connectSlotsByName(MainChapterWindow)

    def retranslateUI(self, MainChapterWindow):
        _translate = QtCore.QCoreApplication.translate
        MainChapterWindow.setWindowTitle(_translate("MainChapterWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainChapterWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                            "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta "
                                            "charset=\"utf-8\" /><style type=\"text/css\">\n "
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Montserrat\'; "
                                            "font-size:13pt; font-weight:400; font-style:normal;\">\n "
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                            "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                            "font-size:12pt;\">Drag the card or type in the command to add, commit, "
                                            "and push your first file!</span></p></body></html>"))
        self.task_one.setText(_translate("MainChapterWindow", "Add a.txt"))
        self.task_two.setText(_translate("MainChapterWindow", "Commit the change!"))
        self.task_three.setText(_translate("MainChapterWindow", "Push!"))
        self.file1.setHtml(_translate("MainChapterWindow",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                      "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" "
                                      "/><style type=\"text/css\">\n "
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; "
                                      "font-size:13pt; font-weight:400; font-style:normal;\">\n "
                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                      "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> <img src=\"\" "
                                      "width=\"30\" height=\"30\" /></p>\n "
                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                      "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   "
                                      "a.txt</p></body></html>"))
        self.title_label.setText(_translate("MainChapterWindow", "CH1: First Commit"))
        self.back_button.setText(_translate("MainChapterWindow", "Back"))
        self.reload_button.setText(_translate("MainChapterWindow", "Reload"))
        self.toggle_music_button.setText(_translate("MainChapterWindow", "Toggle Music"))
        self.cmd_output_text.setHtml(_translate("MainChapterWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta "
                                                "charset=\"utf-8\" /><style type=\"text/css\">\n "
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'Courier New\'; "
                                                "font-size:13pt; font-weight:400; font-style:normal;\">\n "
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                                "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                                "style=\" font-family:\'Menlo\'; font-size:11pt; "
                                                "color:#ffffff;\">user@what-the-git repo_folder % "
                                                "</span></p></body></html>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainChapterWindow = QtWidgets.QMainWindow()
    ui = UI_MainChapterWindow()
    ui.setupUI(MainChapterWindow)

    # Play background music
    filename = 'music/track.mp3'
    fullpath = QtCore.QDir.current().absoluteFilePath(filename)
    media = QtCore.QUrl.fromLocalFile(fullpath)
    content = QtMultimedia.QMediaContent(media)
    player = QtMultimedia.QMediaPlayer()
    player.setMedia(content)
    player.play()

    MainChapterWindow.show()
    sys.exit(app.exec_())
