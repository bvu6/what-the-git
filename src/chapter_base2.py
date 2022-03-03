#!/usr/bin/env python3
# Made By Thicc-Juice
# What The Git!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from cards import DraggableCardImages
import sys
import os

from src.git_status import git_status


class ui_chaptertwo_window(object):
    def __init__(self, window):
        self.nodedict = {}
        self.currIconLocation = "branch 2"
        self.avatarposX = 700
        self.avatarposY = 380
        self.branch1List = []
        self.branch2List = []
        self.headList = []
        self.git = git_status()
        self.valid = False
        self.lastMove = -1
        self.chapterTwo_num = 2
        self.cmd = ""
        self.card_list = []
        self.prompt = False
        self.prompt2 = False
        window.setObjectName("window")
        window.resize(1280, 720)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(window.sizePolicy().hasHeightForWidth())

        window.setSizePolicy(size_policy)
        window.setMinimumSize(QtCore.QSize(1280, 720))
        window.setMaximumSize(QtCore.QSize(1280, 720))

        font = QtGui.QFont()
        font.setPointSize(12)
        window.setFont(font)
        window.setStyleSheet("")

        window.setFont(font)
        window.setStyleSheet("")

        window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_chapter_central_widget = QtWidgets.QWidget(window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_chapter_central_widget.sizePolicy().hasHeightForWidth())
        self.main_chapter_central_widget.setSizePolicy(sizePolicy)
        self.main_chapter_central_widget.setMinimumSize(QtCore.QSize(1280, 720))
        self.main_chapter_central_widget.setMaximumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.main_chapter_central_widget.setFont(font)
        self.main_chapter_central_widget.setStyleSheet("")
        self.main_chapter_central_widget.setObjectName("main_chapter_central_widget")
        self.main_chapter_frame = QtWidgets.QFrame(self.main_chapter_central_widget)
        self.main_chapter_frame.setEnabled(True)
        self.main_chapter_frame.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_chapter_frame.sizePolicy().hasHeightForWidth())
        self.main_chapter_frame.setSizePolicy(sizePolicy)
        self.main_chapter_frame.setMinimumSize(QtCore.QSize(900, 530))
        self.main_chapter_frame.setMaximumSize(QtCore.QSize(1920, 1000))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.main_chapter_frame.setFont(font)
        self.main_chapter_frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.main_chapter_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_chapter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_chapter_frame.setObjectName("main_chapter_frame")
        self.chapter_info_text_browser = QtWidgets.QTextBrowser(self.main_chapter_frame)
        self.chapter_info_text_browser.setGeometry(QtCore.QRect(830, 70, 441, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chapter_info_text_browser.sizePolicy().hasHeightForWidth())
        self.chapter_info_text_browser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.chapter_info_text_browser.setFont(font)
        self.chapter_info_text_browser.setStyleSheet("color: white")
        self.chapter_info_text_browser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chapter_info_text_browser.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.chapter_info_text_browser.setObjectName("chapter_info_text_browser")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.main_chapter_frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(830, 500, 441, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.cmd_grid_layout = QtWidgets.QGridLayout(self.verticalLayoutWidget_2)
        self.cmd_grid_layout.setContentsMargins(0, 7, 0, 7)
        self.cmd_grid_layout.setVerticalSpacing(3)
        self.cmd_grid_layout.setObjectName("cmd_grid_layout")
        self.cmd_output_scroll_area = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmd_output_scroll_area.sizePolicy().hasHeightForWidth())
        self.cmd_output_scroll_area.setSizePolicy(sizePolicy)
        self.cmd_output_scroll_area.setMaximumSize(QtCore.QSize(439, 16777215))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.cmd_output_scroll_area.setFont(font)
        self.cmd_output_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.cmd_output_scroll_area.setWidgetResizable(True)
        self.cmd_output_scroll_area.setObjectName("cmd_output_scroll_area")
        self.cmd_output_contents = QtWidgets.QWidget()
        self.cmd_output_contents.setGeometry(QtCore.QRect(0, 0, 437, 173))
        font = QtGui.QFont()
        self.cmd_output_contents.setFont(font)
        self.cmd_output_contents.setObjectName("cmd_output_contents")
        self.cmd_output_content_hlayout = QtWidgets.QHBoxLayout(self.cmd_output_contents)
        self.cmd_output_content_hlayout.setContentsMargins(0, 0, 0, 0)
        self.cmd_output_content_hlayout.setSpacing(0)
        self.cmd_output_content_hlayout.setObjectName("cmd_output_content_hlayout")
        self.cmd_output_text = QtWidgets.QTextBrowser(self.cmd_output_contents)
        self.cmd_output_text.setMaximumSize(QtCore.QSize(437, 16777215))
        font = QtGui.QFont()
        self.cmd_output_text.setFont(font)
        self.cmd_output_text.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.cmd_output_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.cmd_output_text.setPlaceholderText("")
        self.cmd_output_text.setObjectName("cmd_output_text")
        self.cmd_output_content_hlayout.addWidget(self.cmd_output_text)
        self.cmd_output_scroll_area.setWidget(self.cmd_output_contents)
        self.cmd_grid_layout.addWidget(self.cmd_output_scroll_area, 0, 0, 1, 1)
        self.cmd_user_input_box = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmd_user_input_box.sizePolicy().hasHeightForWidth())
        self.cmd_user_input_box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cmd_user_input_box.setFont(font)
        self.cmd_user_input_box.setStyleSheet("border: 1px solid red;\n"
                                              "border-color: rgb(0, 155, 255);\n"
                                              "border-radius: 5px; \n"
                                              "background-color: rgb(30, 30, 30);\n"
                                              "color: rgb(255,255,255);\n"
                                              "padding-left:5px;\n"
                                              "padding-right:5px")
        self.cmd_user_input_box.setText("")
        self.cmd_user_input_box.setDragEnabled(False)
        self.cmd_user_input_box.setPlaceholderText("")
        self.cmd_user_input_box.setObjectName("cmd_user_input_box")
        self.cmd_grid_layout.addWidget(self.cmd_user_input_box, 1, 0, 1, 1)
        self.cmd_grid_layout.setRowStretch(0, 12)
        self.cmd_grid_layout.setRowStretch(1, 2)
        self.back_button = QtWidgets.QPushButton(self.main_chapter_frame)
        self.back_button.setGeometry(QtCore.QRect(10, 20, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("QPushButton {\n"
                                       "    border: 1px solid #F4D782;\n"
                                       "    font-size: 14px;\n"
                                       "    color: #F4D782;\n"
                                       "    padding: 1px;\n"
                                       "    border-radius:10px\n"
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
        self.back_button.setObjectName("back_button")
        self.toggle_music_button = QtWidgets.QPushButton(self.main_chapter_frame)
        self.toggle_music_button.setGeometry(QtCore.QRect(180, 20, 120, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_music_button.sizePolicy().hasHeightForWidth())
        self.toggle_music_button.setSizePolicy(sizePolicy)
        self.toggle_music_button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.toggle_music_button.setFont(font)
        self.toggle_music_button.setStyleSheet("QPushButton {\n"
                                               "    border: 1px solid #F4D782;\n"
                                               "    font-size: 14px;\n"
                                               "    color: #F4D782;\n"
                                               "    padding: 1px;\n"
                                               "    border-radius:10px\n"
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
        self.reload_button = QtWidgets.QPushButton(self.main_chapter_frame)
        self.reload_button.setGeometry(QtCore.QRect(90, 20, 80, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reload_button.sizePolicy().hasHeightForWidth())
        self.reload_button.setSizePolicy(sizePolicy)
        self.reload_button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.reload_button.setFont(font)
        self.reload_button.setStyleSheet("QPushButton {\n"
                                         "    border: 1px solid #F4D782;\n"
                                         "    font-size: 14px;\n"
                                         "    color: #F4D782;\n"
                                         "    padding: 1px;\n"
                                         "    border-radius:10px\n"
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
        self.reload_button.setObjectName("reload_button")
        self.file_stacked_widget = QtWidgets.QStackedWidget(self.main_chapter_frame)
        self.file_stacked_widget.setGeometry(QtCore.QRect(830, 410, 441, 91))
        font = QtGui.QFont()
        self.file_stacked_widget.setFont(font)
        self.file_stacked_widget.setObjectName("file_stacked_widget")
        self.file_main_page = QtWidgets.QWidget()
        font = QtGui.QFont()
        self.file_main_page.setFont(font)
        self.file_main_page.setObjectName("file_main_page")
        self.file_main_grid_layout = QtWidgets.QGridLayout(self.file_main_page)
        self.file_main_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.file_main_grid_layout.setObjectName("file_main_grid_layout")
        self.files_main_frame = QtWidgets.QFrame(self.file_main_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.files_main_frame.sizePolicy().hasHeightForWidth())
        self.files_main_frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        self.files_main_frame.setFont(font)
        self.files_main_frame.setStyleSheet("background-color: rgb(0, 157, 255);border-radius: 5px")
        self.files_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.files_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.files_main_frame.setObjectName("files_main_frame")
        self.file_main_frame_horiz_layout = QtWidgets.QHBoxLayout(self.files_main_frame)
        self.file_main_frame_horiz_layout.setContentsMargins(0, 0, 0, 0)
        self.file_main_frame_horiz_layout.setObjectName("file_main_frame_horiz_layout")
        self.file_img1 = QtWidgets.QTextBrowser(self.files_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_img1.sizePolicy().hasHeightForWidth())
        self.file_img1.setSizePolicy(sizePolicy)
        self.file_img1.setMinimumSize(QtCore.QSize(40, 63))
        self.file_img1.setMaximumSize(QtCore.QSize(40, 63))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.file_img1.setFont(font)
        self.file_img1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.file_img1.setMouseTracking(True)
        self.file_img1.setStyleSheet("")
        self.file_img1.setLineWidth(0)
        self.file_img1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.file_img1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.file_img1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.file_img1.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.file_img1.setAcceptRichText(False)
        self.file_img1.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.file_img1.setObjectName("file_img1")
        self.file_main_frame_horiz_layout.addWidget(self.file_img1)
        self.file_main_grid_layout.addWidget(self.files_main_frame, 0, 0, 1, 1)
        self.file_stacked_widget.addWidget(self.file_main_page)
        self.file1_edit_widget = QtWidgets.QWidget()
        font = QtGui.QFont()
        self.file1_edit_widget.setFont(font)
        self.file1_edit_widget.setObjectName("file1_edit_widget")
        self.file1_edit_grid_layout = QtWidgets.QGridLayout(self.file1_edit_widget)
        self.file1_edit_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.file1_edit_grid_layout.setObjectName("file1_edit_grid_layout")

        self.file1_save_button = QtWidgets.QPushButton(self.file1_edit_widget)
        size_policy.setHeightForWidth(self.file1_save_button.sizePolicy().hasHeightForWidth())
        self.file1_save_button.setSizePolicy(size_policy)
        self.file1_save_button.setMaximumSize(QtCore.QSize(60, 85))
        self.file1_save_button.setFont(font)
        self.file1_save_button.setStyleSheet("QPushButton {\n"
                                             "    border: 1px solid #F4D782;\n"
                                             "    font-size: 14px;\n"
                                             "    color: #F4D782;\n"
                                             "    padding: 10px;\n"
                                             "    border-radius:10px\n"
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
        self.file1_save_button.setObjectName("file1_done_button")
        self.file1_edit_grid_layout.addWidget(self.file1_save_button, 0, 1, 1, 1)

        self.drag_label = QtWidgets.QLabel(self.main_chapter_frame)
        self.drag_label.setGeometry(QtCore.QRect(600, 8, 300, 61))
        font.setPointSize(20)
        self.drag_label.setFont(font)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.drag_label.sizePolicy().hasHeightForWidth())
        self.drag_label.setStyleSheet("font: 24pt \"Montserrat\"; color: gray")
        self.drag_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.drag_label.move(60, 100)
        self.drag_label.setObjectName("drag_label")


        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)


        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        self.file1_qplaintextedit = QtWidgets.QPlainTextEdit(self.file1_edit_widget)
        self.file1_qplaintextedit.setMaximumSize(QtCore.QSize(16777215, 85))
        font = QtGui.QFont()
        self.file1_qplaintextedit.setFont(font)
        self.file1_qplaintextedit.setAutoFillBackground(False)
        self.file1_qplaintextedit.setStyleSheet("border: 1px solid white;\n"
                                                "border-radius: 5px;\n"
                                                "color: white")
        self.file1_qplaintextedit.setObjectName("file1_qplaintextedit")
        self.file1_edit_grid_layout.addWidget(self.file1_qplaintextedit, 0, 0, 1, 1)
        self.file_stacked_widget.addWidget(self.file1_edit_widget)
        self.layoutWidget = QtWidgets.QWidget(self.main_chapter_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(830, 280, 441, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.task_vert_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.task_vert_layout.setContentsMargins(0, 7, 0, 7)
        self.task_vert_layout.setSpacing(6)
        self.task_vert_layout.setObjectName("task_vert_layout")
        self.task_one = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_one.sizePolicy().hasHeightForWidth())
        self.task_one.setSizePolicy(sizePolicy)
        self.task_one.setMinimumSize(QtCore.QSize(0, 20))
        self.task_one.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.task_one.setFont(font)
        self.task_one.setStyleSheet("background-color: rgb(138, 0, 1);\n"
                                    "border-radius: 5px; \n"
                                    "padding-left:5px;\n"
                                    "color: white;\n"
                                    "font: 13pt \"Montserrat\";")
        self.task_one.setAlignment(QtCore.Qt.AlignCenter)
        self.task_one.setObjectName("task_one")
        self.task_vert_layout.addWidget(self.task_one)
        self.task_two = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_two.sizePolicy().hasHeightForWidth())
        self.task_two.setSizePolicy(sizePolicy)
        self.task_two.setMinimumSize(QtCore.QSize(0, 20))
        self.task_two.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.task_two.setFont(font)
        self.task_two.setStyleSheet("background-color: rgb(138, 0, 1);\n"
                                    "border-radius: 5px; \n"
                                    "padding-left:5px;\n"
                                    "color: white;\n"
                                    "font: 13pt \"Montserrat\";")
        self.task_two.setAlignment(QtCore.Qt.AlignCenter)
        self.task_two.setObjectName("task_two")
        self.task_vert_layout.addWidget(self.task_two)
        self.task_three = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_three.sizePolicy().hasHeightForWidth())
        self.task_three.setSizePolicy(sizePolicy)
        self.task_three.setMinimumSize(QtCore.QSize(0, 20))
        self.task_three.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.task_three.setFont(font)
        self.task_three.setStyleSheet("background-color: rgb(138, 0, 1);\n"
                                      "border-radius: 5px; \n"
                                      "padding-left:5px;\n"
                                      "color: white;\n"
                                      "font: 13pt \"Montserrat\";")
        self.task_three.setAlignment(QtCore.Qt.AlignCenter)
        self.task_three.setObjectName("task_three")
        self.task_vert_layout.addWidget(self.task_three)
        self.title_label = QtWidgets.QLabel(self.main_chapter_frame)
        self.title_label.setGeometry(QtCore.QRect(830, 8, 439, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: white")
        self.title_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.title_label.setObjectName("title_label")
        self.head_state_widget = QtWidgets.QWidget(self.main_chapter_frame)
        self.head_state_widget.setGeometry(QtCore.QRect(80, 280, 71, 71))
        font = QtGui.QFont()
        self.head_state_widget.setFont(font)
        self.head_state_widget.setStyleSheet("background-color:rgb(174, 61, 255)")
        self.head_state_widget.setObjectName("head_state_widget")
        self.head_state_vert_layout = QtWidgets.QVBoxLayout(self.head_state_widget)
        self.head_state_vert_layout.setContentsMargins(0, 7, 0, 0)
        self.head_state_vert_layout.setObjectName("head_state_vert_layout")
        self.head_label = QtWidgets.QTextBrowser(self.head_state_widget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.head_label.setFont(font)
        self.head_label.setStyleSheet("border: 0px")
        self.head_label.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.head_label.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.head_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.head_label.setObjectName("head_label")
        self.head_state_vert_layout.addWidget(self.head_label)
        self.commit_state_widget = QtWidgets.QWidget(self.main_chapter_frame)
        self.commit_state_widget.setGeometry(QtCore.QRect(240, 280, 81, 71))
        font = QtGui.QFont()
        self.commit_state_widget.setFont(font)
        self.commit_state_widget.setStyleSheet("background-color:rgb(174, 61, 255)")
        self.commit_state_widget.setObjectName("commit_state_widget")
        self.commit_state_widget_layout = QtWidgets.QVBoxLayout(self.commit_state_widget)
        self.commit_state_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.commit_state_widget_layout.setObjectName("commit_state_widget_layout")
        self.first_commit_label = QtWidgets.QTextBrowser(self.commit_state_widget)
        font = QtGui.QFont()
        self.first_commit_label.setFont(font)
        self.first_commit_label.setStyleSheet("border: 0px")
        self.first_commit_label.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.first_commit_label.setObjectName("first_commit_label")
        self.commit_state_widget_layout.addWidget(self.first_commit_label)
        self.commit_state_widget_3 = QtWidgets.QWidget(self.main_chapter_frame)
        self.commit_state_widget_3.setGeometry(QtCore.QRect(390, 280, 81, 71))
        font = QtGui.QFont()
        self.commit_state_widget_3.setFont(font)
        self.commit_state_widget_3.setStyleSheet("background-color:rgb(174, 61, 255)")
        self.commit_state_widget_3.setObjectName("commit_state_widget_3")
        self.commit_state_widget_layout_3 = QtWidgets.QVBoxLayout(self.commit_state_widget_3)
        self.commit_state_widget_layout_3.setContentsMargins(0, 0, 0, 0)
        self.commit_state_widget_layout_3.setObjectName("commit_state_widget_layout_3")
        self.first_commit_label_3 = QtWidgets.QTextBrowser(self.commit_state_widget_3)
        font = QtGui.QFont()
        self.first_commit_label_3.setFont(font)
        self.first_commit_label_3.setStyleSheet("border: 0px")
        self.first_commit_label_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.first_commit_label_3.setObjectName("first_commit_label_3")

        self.commit_state_widget_layout_3.addWidget(self.first_commit_label_3)
        self.commit_state_widget_4 = QtWidgets.QWidget(self.main_chapter_frame)
        self.commit_state_widget_4.setGeometry(QtCore.QRect(540, 280, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.commit_state_widget_4.setFont(font)
        self.commit_state_widget_4.setStyleSheet("background-color:rgb(174, 61, 255)")
        self.commit_state_widget_4.setObjectName("commit_state_widget_4")
        self.commit_state_widget_layout_4 = QtWidgets.QVBoxLayout(self.commit_state_widget_4)
        self.commit_state_widget_layout_4.setContentsMargins(0, 0, 0, 0)
        self.commit_state_widget_layout_4.setObjectName("commit_state_widget_layout_4")
        self.first_commit_label_4 = QtWidgets.QTextBrowser(self.commit_state_widget_4)
        font = QtGui.QFont()
        self.first_commit_label_4.setFont(font)
        self.first_commit_label_4.setStyleSheet("border: 0px")
        self.first_commit_label_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.first_commit_label_4.setObjectName("first_commit_label_4")
        self.commit_state_widget_layout_4.addWidget(self.first_commit_label_4)
        self.commit_state_widget_5 = QtWidgets.QWidget(self.main_chapter_frame)
        self.commit_state_widget_5.setGeometry(QtCore.QRect(390, 420, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.commit_state_widget_5.setFont(font)
        self.commit_state_widget_5.setStyleSheet("background-color:rgb(174, 61, 255)")
        self.commit_state_widget_5.setObjectName("commit_state_widget_5")
        self.commit_state_widget_layout_5 = QtWidgets.QVBoxLayout(self.commit_state_widget_5)
        self.commit_state_widget_layout_5.setContentsMargins(0, 0, 0, 0)
        self.commit_state_widget_layout_5.setObjectName("commit_state_widget_layout_5")
        self.first_commit_label_5 = QtWidgets.QTextBrowser(self.commit_state_widget_5)
        font = QtGui.QFont()
        self.first_commit_label_5.setFont(font)
        self.first_commit_label_5.setStyleSheet("border: 0px")
        self.first_commit_label_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.first_commit_label_5.setObjectName("first_commit_label_5")
        self.commit_state_widget_layout_5.addWidget(self.first_commit_label_5)
        self.commit_state_widget_6 = QtWidgets.QWidget(self.main_chapter_frame)
        self.commit_state_widget_6.setGeometry(QtCore.QRect(540, 420, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.commit_state_widget_6.setFont(font)
        self.commit_state_widget_6.setStyleSheet("background-color:rgb(174, 61, 255)")
        self.commit_state_widget_6.setObjectName("commit_state_widget_6")
        self.commit_state_widget_layout_6 = QtWidgets.QVBoxLayout(self.commit_state_widget_6)
        self.commit_state_widget_layout_6.setContentsMargins(0, 0, 0, 0)
        self.commit_state_widget_layout_6.setObjectName("commit_state_widget_layout_6")
        self.first_commit_label_6 = QtWidgets.QTextBrowser(self.commit_state_widget_6)
        font = QtGui.QFont()
        self.first_commit_label_6.setFont(font)
        self.first_commit_label_6.setStyleSheet("border: 0px")
        self.first_commit_label_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_6.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.first_commit_label_6.setObjectName("first_commit_label_6")
        self.commit_state_widget_layout_6.addWidget(self.first_commit_label_6)
        self.commit_state_widget_7 = QtWidgets.QWidget(self.main_chapter_frame)
        self.commit_state_widget_7.setGeometry(QtCore.QRect(680, 420, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.commit_state_widget_7.setFont(font)
        self.commit_state_widget_7.setStyleSheet("background-color:rgb(174, 61, 255)")
        self.commit_state_widget_7.setObjectName("commit_state_widget_7")
        self.commit_state_widget_layout_7 = QtWidgets.QVBoxLayout(self.commit_state_widget_7)
        self.commit_state_widget_layout_7.setContentsMargins(0, 0, 0, 0)
        self.commit_state_widget_layout_7.setObjectName("commit_state_widget_layout_7")
        self.first_commit_label_7 = QtWidgets.QTextBrowser(self.commit_state_widget_7)
        font = QtGui.QFont()
        self.first_commit_label_7.setFont(font)
        self.first_commit_label_7.setStyleSheet("border: 0px")
        self.first_commit_label_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_7.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.first_commit_label_7.setObjectName("first_commit_label_7")
        self.commit_state_widget_layout_7.addWidget(self.first_commit_label_7)
        self.commit_state_widget_8 = QtWidgets.QWidget(self.main_chapter_frame)
        self.commit_state_widget_8.setGeometry(QtCore.QRect(540, 130, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.commit_state_widget_8.setFont(font)
        self.commit_state_widget_8.setStyleSheet("background-color:rgb(174, 61, 255)")
        self.commit_state_widget_8.setObjectName("commit_state_widget_8")
        self.commit_state_widget_layout_8 = QtWidgets.QVBoxLayout(self.commit_state_widget_8)
        self.commit_state_widget_layout_8.setContentsMargins(0, 0, 0, 0)
        self.commit_state_widget_layout_8.setObjectName("commit_state_widget_layout_8")
        self.first_commit_label_8 = QtWidgets.QTextBrowser(self.commit_state_widget_8)
        font = QtGui.QFont()
        self.first_commit_label_8.setFont(font)
        self.first_commit_label_8.setStyleSheet("border: 0px")
        self.first_commit_label_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_8.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_8.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.first_commit_label_8.setObjectName("first_commit_label_8")
        self.commit_state_widget_layout_8.addWidget(self.first_commit_label_8)
        self.commit_state_widget_9 = QtWidgets.QWidget(self.main_chapter_frame)
        self.commit_state_widget_9.setGeometry(QtCore.QRect(390, 130, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.commit_state_widget_9.setFont(font)
        self.commit_state_widget_9.setStyleSheet("background-color:rgb(174, 61, 255)")
        self.commit_state_widget_9.setObjectName("commit_state_widget_9")
        self.commit_state_widget_layout_9 = QtWidgets.QVBoxLayout(self.commit_state_widget_9)
        self.commit_state_widget_layout_9.setContentsMargins(0, 0, 0, 0)
        self.commit_state_widget_layout_9.setObjectName("commit_state_widget_layout_9")
        self.first_commit_label_9 = QtWidgets.QTextBrowser(self.commit_state_widget_9)
        font = QtGui.QFont()
        self.first_commit_label_9.setFont(font)
        self.first_commit_label_9.setStyleSheet("border: 0px")
        self.first_commit_label_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_9.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_9.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.first_commit_label_9.setObjectName("first_commit_label_9")
        self.commit_state_widget_layout_9.addWidget(self.first_commit_label_9)
        self.commit_state_widget_10 = QtWidgets.QWidget(self.main_chapter_frame)
        self.commit_state_widget_10.setGeometry(QtCore.QRect(680, 130, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.commit_state_widget_10.setFont(font)
        self.commit_state_widget_10.setStyleSheet("background-color:rgb(174, 61, 255)")
        self.commit_state_widget_10.setObjectName("commit_state_widget_10")
        self.commit_state_widget_layout_10 = QtWidgets.QVBoxLayout(self.commit_state_widget_10)
        self.commit_state_widget_layout_10.setContentsMargins(0, 0, 0, 0)
        self.commit_state_widget_layout_10.setObjectName("commit_state_widget_layout_10")
        self.first_commit_label_10 = QtWidgets.QTextBrowser(self.commit_state_widget_10)
        font = QtGui.QFont()
        self.first_commit_label_10.setFont(font)
        self.first_commit_label_10.setStyleSheet("border: 0px")
        self.first_commit_label_10.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_10.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.first_commit_label_10.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.first_commit_label_10.setObjectName("first_commit_label_10")
        self.commit_state_widget_layout_10.addWidget(self.first_commit_label_10)
        self.humanIcon = QtWidgets.QLabel(self.main_chapter_frame)
        self.humanIcon.setGeometry(QtCore.QRect(700, 380, 47, 31))
        self.humanIcon.setText("")
        self.humanIcon.setPixmap(QtGui.QPixmap("iconhuman.png"))
        self.humanIcon.setScaledContents(True)
        self.humanIcon.setObjectName("humanIcon")
        self.Line1 = QtWidgets.QLabel(self.main_chapter_frame)
        self.Line1.setGeometry(QtCore.QRect(150, 310, 91, 5))
        self.Line1.setStyleSheet("background-color: rgb(85, 0, 255)")
        self.Line1.setText("")
        self.Line1.setObjectName("Line1")
        self.line3 = QtWidgets.QLabel(self.main_chapter_frame)
        self.line3.setGeometry(QtCore.QRect(320, 310, 71, 5))
        self.line3.setStyleSheet("background-color: rgb(85, 0, 255)")
        self.line3.setText("")
        self.line3.setObjectName("line3")
        self.line5 = QtWidgets.QLabel(self.main_chapter_frame)
        self.line5.setGeometry(QtCore.QRect(470, 310, 71, 5))
        self.line5.setStyleSheet("background-color: rgb(85, 0, 255)")
        self.line5.setText("")
        self.line5.setObjectName("line5")
        self.line4 = QtWidgets.QLabel(self.main_chapter_frame)
        self.line4.setGeometry(QtCore.QRect(430, 350, 5, 71))
        self.line4.setStyleSheet("background-color: rgb(85, 0, 255)")
        self.line4.setText("")
        self.line4.setObjectName("line4")
        self.line6 = QtWidgets.QLabel(self.main_chapter_frame)
        self.line6.setGeometry(QtCore.QRect(470, 450, 71, 5))
        self.line6.setStyleSheet("background-color: rgb(85, 0, 255)")
        self.line6.setText("")
        self.line6.setObjectName("line6")
        self.line7 = QtWidgets.QLabel(self.main_chapter_frame)
        self.line7.setGeometry(QtCore.QRect(620, 450, 60, 5))
        self.line7.setStyleSheet("background-color: rgb(85, 0, 255)")
        self.line7.setText("")
        self.line7.setObjectName("line7")
        self.line8 = QtWidgets.QLabel(self.main_chapter_frame)
        self.line8.setGeometry(QtCore.QRect(430, 200, 5, 73))
        self.line8.setStyleSheet("background-color: rgb(85, 0, 255)")
        self.line8.setText("")
        self.line8.setObjectName("line8")
        self.line10 = QtWidgets.QLabel(self.main_chapter_frame)
        self.line10.setGeometry(QtCore.QRect(470, 160, 71, 5))
        self.line10.setStyleSheet("background-color: rgb(85, 0, 255)")
        self.line10.setText("")
        self.line10.setObjectName("line10")
        self.Line2 = QtWidgets.QLabel(self.main_chapter_frame)
        self.Line2.setGeometry(QtCore.QRect(620, 160, 65, 5))
        self.Line2.setStyleSheet("background-color: rgb(85, 0, 255)")
        self.Line2.setText("")
        self.Line2.setObjectName("Line2")
        self.chapter_info_text_browser.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.back_button.raise_()
        self.toggle_music_button.raise_()
        self.reload_button.raise_()
        self.file_stacked_widget.raise_()
        self.layoutWidget.raise_()
        self.title_label.raise_()
        self.commit_state_widget.raise_()
        self.head_state_widget.raise_()
        self.commit_state_widget_3.raise_()
        self.commit_state_widget_4.raise_()
        self.commit_state_widget_5.raise_()
        self.commit_state_widget_6.raise_()
        self.commit_state_widget_7.raise_()
        self.commit_state_widget_8.raise_()
        self.commit_state_widget_9.raise_()
        self.commit_state_widget_10.raise_()
        self.humanIcon.raise_()
        self.Line1.raise_()
        self.line3.raise_()
        self.line5.raise_()
        self.line4.raise_()
        self.line6.raise_()
        self.line7.raise_()
        self.line8.raise_()
        self.line10.raise_()
        self.Line2.raise_()
        self.drag_label.raise_()

        self.card_holder_frame = QtWidgets.QFrame(self.main_chapter_frame)
        self.card_holder_frame.setGeometry(QtCore.QRect(0, 500, 821, 220))
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.card_holder_frame.sizePolicy().hasHeightForWidth())

        self.card_holder_frame.setSizePolicy(size_policy)
        self.card_holder_frame.setMaximumSize(QtCore.QSize(16777215, 220))
        self.card_holder_frame.setStyleSheet("\nbackground-color:  #F4D782;")
        self.card_holder_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card_holder_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.card_holder_frame.setObjectName("frame")

        self.create_cards(3)
        self.cmd_output_text.setStyleSheet("background-color: rgb(30, 30, 30); font: 11pt \"Menlo\"; color: "
                                           "white")
        self.file_img1.mousePressEvent = lambda a: self.file_stacked_widget.setCurrentIndex(
            self.file_stacked_widget.currentIndex() + 1)
       # self.file1_save_button.clicked.connect(lambda: self.save_file(1))
        self.cmd_user_input_box.returnPressed.connect(lambda: self.execute_command(-1))

        window.setCentralWidget(self.main_chapter_central_widget)

        self.nodedict["5"] = self.head_state_widget #h
        self.nodedict["10"] = self.commit_state_widget #Hc1
        self.nodedict["20"] = self.commit_state_widget_3 #hC2
        self.nodedict["30"] = self.commit_state_widget_4 #HC3
        self.nodedict["21"] = self.commit_state_widget_9 #b1c1
        self.nodedict["22"] = self.commit_state_widget_8 #b1c2
        self.nodedict["23"] = self.commit_state_widget_10 #b1c3
        self.nodedict["24"] = self.commit_state_widget_5  #b2c1
        self.nodedict["25"] = self.commit_state_widget_6   #b2c2
        self.nodedict["26"] = self.commit_state_widget_7  #b2c3

        self.branch1List.append("21")
        self.branch1List.append("22")
        self.branch1List.append("23")
        self.branch2List.append("24")
        self.branch2List.append("25")
        self.branch1List.append("26")

        self.headList.append("5")
        self.headList.append("10")
        self.headList.append("20")
        self.headList.append("30")
        print(self.headList[0])



        self.retranslateUi(window)
        self.file_stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, MainChapterWindow):
        _translate = QtCore.QCoreApplication.translate
        MainChapterWindow.setWindowTitle(_translate("MainChapterWindow", "MainWindow"))
        self.chapter_info_text_browser.setHtml(_translate("MainChapterWindow",
                                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:\'Montserrat\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Drag the card or type in the command to checkout a different commit! </span></p>\n"
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Git Checkout: Switches Branch or restore working tree files</span></p>\n"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Git Branch: List out all Branch</span></p>\n"
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">In order to get to a Branch, you need to use Git checkout (branchname)</span></p>\n"
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">In order to get to a Commit, you need the Head ID of the commit and use the the function Git checkout (ID)</span></p>\n"
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.cmd_output_text.setHtml(_translate("MainChapterWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo\'; font-size:11pt; color:#ffffff;\">user@what-the-git repo_folder % </span></p></body></html>"))
        self.back_button.setText(_translate("MainChapterWindow", "Back"))
        self.toggle_music_button.setText(_translate("MainChapterWindow", "Toggle Music"))
        self.reload_button.setText(_translate("MainChapterWindow", "Reload"))
        self.file_img1.setHtml(_translate("MainChapterWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"media/txt_img.png\" width=\"35\" height=\"40\" /></p>\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:13pt; color:#ffffff;\"> a.txt</span></p></body></html>"))
        self.file1_qplaintextedit.setPlainText(_translate("MainChapterWindow", "hello world"))
        self.file1_save_button.setText(_translate("window", "Save"))
        self.task_one.setText(_translate("MainChapterWindow", "Check current Branch"))
        self.task_two.setText(_translate("MainChapterWindow", "Get to Branch 1 Using Git Checkout"))
        self.task_three.setText(_translate("MainChapterWindow", "Get to Branch 1 Commit 3"))
        self.title_label.setText(_translate("MainChapterWindow", "CH2: Checkout"))
        self.drag_label.setText(_translate("window", "DRAG CARDS HERE"))
        self.head_label.setHtml(_translate("MainChapterWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Montserrat\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:13pt; font-weight:496; color:#ffffff;\">ID(5)</span></p>\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; font-weight:496; color:#ffffff;\">HEAD</span></p></body></html>"))
        self.first_commit_label.setHtml(_translate("MainChapterWindow",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:13pt; font-weight:496; color:#ffffff;\">ID(10)</span></p>\n"
                                                   "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:13pt; font-weight:496; color:#ffffff;\">First</span></p>\n"
                                                   "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:13pt; font-weight:496; color:#ffffff;\">Commit!</span></p></body></html>"))
        self.first_commit_label_3.setHtml(_translate("MainChapterWindow",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:13pt; font-weight:496; color:#ffffff;\">ID(20)</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:13pt; font-weight:496; color:#ffffff;\">Second</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:13pt; font-weight:496; color:#ffffff;\">Commit!</span></p></body></html>"))
        self.first_commit_label_4.setHtml(_translate("MainChapterWindow",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:13pt; font-weight:496; color:#ffffff;\">ID(30)</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:13pt; font-weight:496; color:#ffffff;\">Third</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:13pt; font-weight:496; color:#ffffff;\">Commit!</span></p></body></html>"))
        self.first_commit_label_5.setHtml(_translate("MainChapterWindow",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Branch 2 ID(24)</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">First</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Commit!</span></p></body></html>"))
        self.first_commit_label_6.setHtml(_translate("MainChapterWindow",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Branch 2 ID(25)</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Second</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Commit!</span></p></body></html>"))
        self.first_commit_label_7.setHtml(_translate("MainChapterWindow",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Branch 2 ID(26)</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Third</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Commit!</span></p></body></html>"))
        self.first_commit_label_8.setHtml(_translate("MainChapterWindow",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Branch 1 ID(21)</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Second</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Commit!</span></p></body></html>"))
        self.first_commit_label_9.setHtml(_translate("MainChapterWindow",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Branch 1 ID(22)</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">First</span></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Commit!</span></p></body></html>"))
        self.first_commit_label_10.setHtml(_translate("MainChapterWindow",
                                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                      "p, li { white-space: pre-wrap; }\n"
                                                      "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Branch 1 ID(23)</span></p>\n"
                                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Third</span></p>\n"
                                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:10pt; font-weight:496; color:#ffffff;\">Commit!</span></p></body></html>"))

    def execute_command(self, type):
        self.cmd = self.cmd_user_input_box.text()
        self.cmd_user_input_box.clear()
        if self.cmd == "git branch" and not self.prompt or type == 3:
            self.valid = self.git.check_move(3)
            self.showCard(3, self.valid)
        elif self.cmd == "git checkout branch" and not self.prompt or type == 4:
            self.valid = self.git.check_move(4)
            if self.valid:
                self.add_cmd_text("git commit \nuser@what-the-git repo_folder % Which branch\n")
                self.hideCards()
                self.prompt = True
                self.cmd = None
        elif self.prompt and (self.cmd == "main" or self.cmd == "Main" or self.cmd == "1" or self.cmd == "2"):
            self.add_cmd_text("user@what-the-git repo_folder % " + self.cmd)
            self.prompt = False
            self.showCard(4, self.valid)
        elif self.cmd == "git checkout head" and not self.prompt or type == 5:
            self.valid = self.git.check_move(5)
            if self.valid:
                self.add_cmd_text("git commit \nuser@what-the-git repo_folder % Enter the head ID\n")
                self.hideCards()
                self.prompt2 = True
                self.cmd = None
        elif self.prompt2:
            print("hello")
            flag = False
            print(self.cmd in self.headList)
            print(self.currIconLocation)
            if self.cmd in self.headList and self.currIconLocation == "main":
                print(self.cmd)
                flag = True
            elif self.cmd in self.branch1List and self.currIconLocation == "branch 1":
                flag = True
            elif self.cmd in self.branch2List and self.currIconLocation == "branch 2":
                flag = True
            if flag:
                self.add_cmd_text("user@what-the-git repo_folder % " + self.cmd)
                self.prompt2 = False
                self.showCard(5, self.valid)
        else:
            print("Invalid move")
    # print(self.cmd)


    # def save_file(self, file_num):
    #     file = os.listdir(f'wtg/CH{self.chapterTwo_num}')[file_num - 1]
    #     with open(f'wtg/CH{self.chapterTwo_num}/{file}', 'w') as f:
    #         if file_num == 1:
    #             f.write(self.file1_qplaintextedit.toPlainText())
    #
    #     self.file_stacked_widget.setCurrentIndex(self.file_stacked_widget.currentIndex() - 1)

    def create_cards(self, num):
        self.card_list = []
        for i in range(num, num+num, 1):
            self.card_list.append(DraggableCardImages(self.main_chapter_frame, None, 100 + (150 * (i-3)), i, self))

    def showCard(self, card_type, valid):

        if valid:
            if card_type == 3:
                self.add_cmd_text("\nuser@what-the-git repo_folder % Git Branch \nmain \nbranch 1 \nbranch 2")
                self.add_cmd_text("\nCurrent Branch: " + self.currIconLocation)
                print("Current Branch:", self.currIconLocation)
                self.task_one.setStyleSheet("background-color: rgb(32, 167, 21);;\n"
                                            "border-radius: 5px; \n"
                                            "padding-left:5px")

            elif card_type == 4:
                # self.add_cmd_text("\nuser@what-the-git repo_folder % " + self.cmd)
                if self.cmd == "1":
                    self.add_cmd_text("\nuser@what-the-git repo_folder % Git Checkout Branch 1 \nSwitching to branch 1")
                    self.humanIcon.move(self.nodedict["21"].pos())
                    self.currIconLocation = "branch 1"
                    self.task_two.setStyleSheet("background-color: rgb(32, 167, 21);;\n"
                                                "border-radius: 5px; \n"
                                                "padding-left:5px")
                elif self.cmd == "2":
                    self.humanIcon.move(self.nodedict["24"].pos())
                    self.add_cmd_text("\nuser@what-the-git repo_folder % Git Checkout Branch 2 \nSwitching to branch 2")
                    self.currIconLocation = "branch 2"

                elif self.cmd == "main" or self.cmd == "Main":
                    self.humanIcon.move(self.nodedict["5"].pos())
                    self.add_cmd_text("\nuser@what-the-git repo_folder % Git Checkout Main \nSwitching to Main")
                    self.currIconLocation = "main"
                self.unhideCard()
            elif card_type == 5:
                print("\nuser@what-the-git repo_folder % git checkout main" + self.cmd)
                self.add_cmd_text("\nuser@what-the-git repo_folder % Git Checkout " + self.cmd)
                self.add_cmd_text("\n" + self.cmd + "\n you are in 'detached HEAD' state. You can look around, make experimental changes \n and commit them, and you can discard any commits you make in this state without impacting any branches by performing another checkout.")
                self.add_cmd_text("\n user@what-the-git repo_folder " + self.cmd + "% ")
                self.humanIcon.move(self.nodedict[self.cmd].pos())
                if self.cmd == "23":
                    self.task_three.setStyleSheet("background-color: rgb(32, 167, 21);;\n"
                                                "border-radius: 5px; \n"
                                                "padding-left:5px")
                self.unhideCard()

    def hideCards(self):
        for i in self.card_list:
            i.hide()

    def unhideCard(self):
        for i in self.card_list:
            i.show()


    def add_cmd_text(self, txt):
        self.cmd_output_text.setText(self.cmd_output_text.toPlainText() + txt)
        self.cmd_output_text.moveCursor(QtGui.QTextCursor.End)

    def validCheck(self, card_type):
        if self.lastMove == card_type - 1:
            self.lastMove = card_type
            return True
        elif card_type == 3 or card_type == 4:
            return True
        else:
            print("Invalid move")
            return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = ui_chaptertwo_window(main_window)
    main_window.show()
    sys.exit(app.exec_())
