#!/usr/bin/env python3
# Made By Thicc-Juice
# What The Git!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from cards import DraggableCardImages
from git_manager import git_manager
from file import file
import sys
import os


class ui_chapter_window(QMainWindow):
    def __init__(self, window):
        super(ui_chapter_window, self).__init__()
        self.current_directory = os.path.dirname(os.path.realpath(__file__))
        self.git_manager = git_manager()
        self.valid = False
        self.lastMove = -1
        self.chapter_num = 1
        self.card_list = []
        self.prompt = False
        self.command_list = []
        self.cmd_list_pos = 1
        self.file_dict = {'a.txt': file('a.txt')}

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
        window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_chapter_central_widget = QtWidgets.QWidget(window)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.main_chapter_central_widget.sizePolicy().hasHeightForWidth())

        self.main_chapter_central_widget.setSizePolicy(size_policy)
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

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.main_chapter_frame.sizePolicy().hasHeightForWidth())

        self.main_chapter_frame.setSizePolicy(size_policy)
        self.main_chapter_frame.setMinimumSize(QtCore.QSize(1280, 720))
        self.main_chapter_frame.setMaximumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setPointSize(12)

        self.main_chapter_frame.setFont(font)
        self.main_chapter_frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.main_chapter_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_chapter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_chapter_frame.setObjectName("main_chapter_frame")
        self.main_view = QtWidgets.QGraphicsView(self.main_chapter_frame)
        self.main_view.setGeometry(QtCore.QRect(10, 70, 821, 651))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.main_view.sizePolicy().hasHeightForWidth())

        self.main_view.setSizePolicy(size_policy)
        font = QtGui.QFont()
        self.main_view.setFont(font)
        self.main_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.main_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.main_view.setObjectName("main_view")

        self.chapter_info_text_browser = QtWidgets.QTextBrowser(self.main_chapter_frame)
        self.chapter_info_text_browser.setGeometry(QtCore.QRect(830, 70, 441, 211))

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.chapter_info_text_browser.sizePolicy().hasHeightForWidth())

        self.chapter_info_text_browser.setSizePolicy(size_policy)
        font = QtGui.QFont()
        self.chapter_info_text_browser.setFont(font)
        self.chapter_info_text_browser.setStyleSheet("color: white;")
        self.chapter_info_text_browser.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.chapter_info_text_browser.setObjectName("chapter_info_text_browser")

        self.cmd_input_vert_layout = QtWidgets.QWidget(self.main_chapter_frame)
        self.cmd_input_vert_layout.setGeometry(QtCore.QRect(830, 500, 441, 221))
        self.cmd_input_vert_layout.setObjectName("cmd_input_vert_layout")

        self.cmd_grid_layout = QtWidgets.QGridLayout(self.cmd_input_vert_layout)
        self.cmd_grid_layout.setContentsMargins(0, 7, 0, 7)
        self.cmd_grid_layout.setVerticalSpacing(3)
        self.cmd_grid_layout.setObjectName("cmd_grid_layout")

        self.cmd_output_scroll_area = QtWidgets.QScrollArea(self.cmd_input_vert_layout)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.cmd_output_scroll_area.sizePolicy().hasHeightForWidth())

        self.cmd_output_scroll_area.setSizePolicy(size_policy)
        self.cmd_output_scroll_area.setMaximumSize(QtCore.QSize(439, 1280))
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

        self.console = QtWidgets.QTextBrowser(self.cmd_output_contents)
        self.console.setMaximumSize(QtCore.QSize(437, 1280))
        font = QtGui.QFont()
        self.console.setFont(font)
        self.console.setStyleSheet("background-color: rgb(30, 30, 30); font: 11pt \"Menlo\"; color: white")
        self.console.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.console.setObjectName("cmd_output_text")

        self.cmd_output_content_hlayout.addWidget(self.console)
        self.cmd_output_scroll_area.setWidget(self.cmd_output_contents)
        self.cmd_grid_layout.addWidget(self.cmd_output_scroll_area, 0, 0, 1, 1)
        self.cmd_user_input_box = QtWidgets.QLineEdit(self.cmd_input_vert_layout)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.cmd_user_input_box.sizePolicy().hasHeightForWidth())

        self.cmd_user_input_box.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cmd_user_input_box.setFont(font)
        self.cmd_user_input_box.setStyleSheet("border: 1px solid red;\n"
                                              "border-color: rgb(0, 155, 255);\n"
                                              "border-radius: 5px; \n"
                                              "color: white; \n"
                                              "background-color: rgb(30, 30, 30);\n"
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

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())

        self.back_button.setSizePolicy(size_policy)
        self.back_button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
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

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.reload_button.sizePolicy().hasHeightForWidth())

        self.reload_button.setSizePolicy(size_policy)
        self.reload_button.setMinimumSize(QtCore.QSize(0, 0))

        font = QtGui.QFont()
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

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.files_main_frame.sizePolicy().hasHeightForWidth())
        self.files_main_frame.setSizePolicy(size_policy)
        self.files_main_frame.setContentsMargins(0, 0, 0, 0)

        font = QtGui.QFont()
        self.files_main_frame.setFont(font)
        self.files_main_frame.setStyleSheet("background-color: rgb(0, 157, 255);border-radius: 5px; margin:0px")
        self.files_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.files_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.files_main_frame.setObjectName("files_main_frame")

        self.file_main_frame_horiz_layout = QtWidgets.QHBoxLayout(self.files_main_frame)
        self.file_main_frame_horiz_layout.setObjectName("file_main_frame_horiz_layout")

        self.files_horiz_layout = QtWidgets.QHBoxLayout()
        self.files_horiz_layout.setSpacing(0)
        self.files_horiz_layout.setContentsMargins(0, 0, 0, 0)
        self.files_horiz_layout.setObjectName("files_horiz_layout")

        self.file_img1 = QtWidgets.QTextBrowser(self.files_main_frame)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.file_img1.sizePolicy().hasHeightForWidth())

        self.file_img1.setSizePolicy(size_policy)
        self.file_img1.setMinimumSize(QtCore.QSize(50, 100))
        self.file_img1.setMaximumSize(QtCore.QSize(50, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.file_img1.setFont(font)
        self.file_img1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.file_img1.verticalScrollBar().setValue(self.file_img1.verticalScrollBar().maximum())
        self.file_img1.setStyleSheet("")
        self.file_img1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.file_img1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.file_img1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.file_img1.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.file_img1.setObjectName("file_img1")

        self.files_horiz_layout.addWidget(self.file_img1)
        self.file_main_frame_horiz_layout.addLayout(self.files_horiz_layout)
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

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.file1_save_button.sizePolicy().hasHeightForWidth())

        self.file1_save_button.setSizePolicy(size_policy)
        self.file1_save_button.setMaximumSize(QtCore.QSize(60, 85))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
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

        self.file1_qplaintextedit = QtWidgets.QPlainTextEdit(self.file1_edit_widget)
        self.file1_qplaintextedit.setMaximumSize(QtCore.QSize(1280, 85))
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

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.task_one.sizePolicy().hasHeightForWidth())

        self.task_one.setSizePolicy(size_policy)
        self.task_one.setMinimumSize(QtCore.QSize(0, 20))
        self.task_one.setMaximumSize(QtCore.QSize(1280, 36))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)

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

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.task_two.sizePolicy().hasHeightForWidth())

        self.task_two.setSizePolicy(size_policy)
        self.task_two.setMinimumSize(QtCore.QSize(0, 20))
        self.task_two.setMaximumSize(QtCore.QSize(1280, 36))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)

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

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.task_three.sizePolicy().hasHeightForWidth())

        self.task_three.setSizePolicy(size_policy)
        self.task_three.setMinimumSize(QtCore.QSize(0, 20))
        self.task_three.setMaximumSize(QtCore.QSize(1280, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
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

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())

        self.title_label.setSizePolicy(size_policy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("font: 24pt \"Montserrat\"; color: white")
        self.title_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.title_label.setObjectName("title_label")

        self.head_state_widget = QtWidgets.QWidget(self.main_chapter_frame)
        self.head_state_widget.setGeometry(QtCore.QRect(220, 270, 71, 71))
        font = QtGui.QFont()
        self.head_state_widget.setFont(font)
        self.head_state_widget.setStyleSheet("background-color:rgb(174, 61, 255)")
        self.head_state_widget.setObjectName("head_state_widget")
        self.head_state_vert_layout = QtWidgets.QVBoxLayout(self.head_state_widget)
        self.head_state_vert_layout.setContentsMargins(0, 8, 0, 0)
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
        self.commit_state_widget.setGeometry(QtCore.QRect(400, 270, 81, 71))
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
        self.commit_connect_line = QtWidgets.QLabel(self.main_chapter_frame)
        self.commit_connect_line.setGeometry(QtCore.QRect(292, 290, 108, 31))
        font = QtGui.QFont()

        self.commit_connect_line.setFont(font)
        self.commit_connect_line.setText("")
        self.commit_connect_line.setPixmap(QtGui.QPixmap("images/arrow.png"))
        self.commit_connect_line.setScaledContents(True)
        self.commit_connect_line.setObjectName("commit_connect_line")

        self.drag_label = QtWidgets.QLabel(self.main_chapter_frame)
        self.drag_label.setGeometry(QtCore.QRect(830, 8, 439, 61))
        font.setPointSize(24)
        self.drag_label.setFont(font)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.drag_label.sizePolicy().hasHeightForWidth())
        self.drag_label.setStyleSheet("font: 24pt \"Montserrat\"; color: gray")
        self.drag_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.drag_label.move(260, 200)
        self.drag_label.setObjectName("drag_label")

        self.main_view.raise_()
        self.chapter_info_text_browser.raise_()
        self.cmd_input_vert_layout.raise_()
        self.back_button.raise_()
        self.toggle_music_button.raise_()
        self.reload_button.raise_()
        self.file_stacked_widget.raise_()
        self.layoutWidget.raise_()
        self.title_label.raise_()
        self.commit_state_widget.raise_()
        self.head_state_widget.raise_()
        self.commit_connect_line.raise_()
        self.drag_label.raise_()

        # modifier
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
        self.file_img1.mousePressEvent = lambda a: self.file_stacked_widget.setCurrentIndex(
            self.file_stacked_widget.currentIndex() + 1)
        self.file1_save_button.clicked.connect(lambda: self.save_file(list(self.file_dict.keys())[0]))

        self.cmd_user_input_box.installEventFilter(self)
        self.cmd_user_input_box.returnPressed.connect(lambda: self.execute_command(-1))

        window.setCentralWidget(self.main_chapter_central_widget)
        self.retranslate(window)
        self.file_stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(window)

        # os.system(f'cd what_the_git/CH{self.chapter_num}')

    def retranslate(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "What The Git!"))

        with open('wtg/CH1/a.txt') as f:
            self.file1_qplaintextedit.setPlainText(_translate("window", f.read()))

        self.chapter_info_text_browser.setHtml(_translate("window",
                                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                          "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta "
                                                          "charset=\"utf-8\" /><style type=\"text/css\">\n "
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:\'Montserrat\'; "
                                                          "font-size:14pt; font-weight:400; font-style:normal;\">"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                          "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                          "text-indent:0px;\"><span style=\" font-size:14pt;\">Drag "
                                                          "the card or type in the command to add, commit, "
                                                          "and push your first file!</span></p>\n "
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                          "-qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br "
                                                          "/></p>\n "
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                          "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                          "text-indent:0px;\"><span style=\" font-size:14pt;\">git "
                                                          "add: Add file contents to the index</span></p>\n "
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                          "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                          "text-indent:0px;\"><span style=\" font-size:14pt;\">git "
                                                          "commit -m &quot;comment&quot;: Record changes to the "
                                                          "repository</span></p>\n "
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                          "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                          "text-indent:0px;\"><span style=\" font-size:14pt;\">git "
                                                          "push: Update remote refs along with associated "
                                                          "object</span></p>\n "
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                                          "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                          "-qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br "
                                                          "/></p>\n "
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; "
                                                          "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                          "text-indent:0px;\"><span style=\" font-size:14pt;\">You "
                                                          "currently have an modified a.txt file that you want to "
                                                          "push. What steps should you take to push the modified file?"
                                                          "</span></p></body></html>"))
        self.console.setHtml(_translate("window",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                        "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta "
                                        "charset=\"utf-8\" /><style type=\"text/css\">\n "
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'Menlo\'; font-size:11pt; "
                                        "font-weight:400; font-style:normal;\">\n "
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                        "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                        "style=\" font-size:11pt; color:#ffffff;\">user@what-the-git "
                                        "repo_folder % </span></p></body></html>"))
        self.back_button.setText(_translate("window", "Back"))
        self.toggle_music_button.setText(_translate("window", "Toggle Music"))
        self.reload_button.setText(_translate("window", "Reload"))
        self.file_img1.setHtml(_translate("window",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                          "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta "
                                          "charset=\"utf-8\" /><style type=\"text/css\">\n "
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; "
                                          "font-size:12pt; font-weight:400; font-style:normal;\">\n "
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                          "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img "
                                          "src=\"media/txt_img.png\" width=\"35\" height=\"40\" /></p>\n "
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                          "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                                          "font-family:\'Montserrat\'; font-size:13pt; color:#ffffff;\"> "
                                          "a.txt</span></p></body></html>"))
        self.file1_save_button.setText(_translate("window", "Save"))
        self.task_one.setText(_translate("window", "Add a.txt"))
        self.task_two.setText(_translate("window", "Commit the change!"))
        self.task_three.setText(_translate("window", "Push!"))
        self.title_label.setText(_translate("window", "CH1: First Commit"))
        self.drag_label.setText(_translate("window", "DRAG CARDS HERE"))
        self.head_label.setHtml(_translate("window",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                           "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta "
                                           "charset=\"utf-8\" /><style type=\"text/css\">\n "
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Montserrat\'; font-size:12pt; "
                                           "font-weight:400; font-style:normal;\">"
                                           "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                           "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                           "text-indent:0px; font-size:13pt; font-weight:500; color:#ffffff;\"><br "
                                           "/></p>\n "
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                                           "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                           "text-indent:0px;\"><span style=\" font-size:13pt; font-weight:500; "
                                           "color:#ffffff;\">HEAD</span></p></body></html>"))
        self.first_commit_label.setHtml(_translate("window",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                   "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta "
                                                   "charset=\"utf-8\" /><style type=\"text/css\">\n "
                                                   "p, li { white-space: pre-wrap; }"
                                                   "</style></head><body style=\" font-family:\'Montserrat\'; "
                                                   "font-size:13pt; font-weight:400; font-style:normal;\">"
                                                   "<p align=\"center\" style=\"-qt-paragraph-type:empty; "
                                                   "margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                                   "margin-right:0px; -qt-block-indent:0; text-indent:0px; "
                                                   "font-weight:500; color:#ffffff;\"><br /></p>\n "
                                                   "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                                                   "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                   "text-indent:0px;\"><span style=\" font-weight:500; "
                                                   "color:#ffffff;\">First</span></p>\n "
                                                   "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                                                   "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                                   "text-indent:0px;\"><span style=\" font-weight:500; "
                                                   "color:#ffffff;\">Commit!</span></p></body></html>"))
        self.head_label.hide()
        self.first_commit_label.hide()
        self.head_state_widget.hide()
        self.commit_state_widget.hide()
        self.commit_connect_line.hide()

    def eventFilter(self, obj, event):
        if obj is self.cmd_user_input_box and event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Up and self.command_list:
                if self.cmd_list_pos > 0:
                    if not self.command_list[-1].isspace() and self.command_list[-1]:
                        self.command_list.append(self.cmd_user_input_box.text())

                    self.cmd_list_pos -= 1
                    command = self.command_list[self.cmd_list_pos]
                    self.cmd_user_input_box.setText(command)
                    self.cmd_user_input_box.setCursorPosition(-1)

            if event.key() == QtCore.Qt.Key_Down and self.command_list:
                if self.cmd_list_pos < len(self.command_list) - 1:
                    self.cmd_list_pos += 1
                    command = self.command_list[self.cmd_list_pos]
                    self.cmd_user_input_box.setText(command)
                    self.cmd_user_input_box.setCursorPosition(-1)

        return super().eventFilter(obj, event)

    # handle commands entered by the user
    def execute_command(self, type):
        cmd = self.cmd_user_input_box.text()  # get user input
        self.cmd_user_input_box.clear()  # clear text from input box

        if self.command_list and (self.command_list[-1].isspace() or not self.command_list[-1]):
            self.command_list.pop(-1)

        # append cmd only if valid
        if not cmd.isspace() and cmd:
            self.command_list.append(cmd)

        if len(self.command_list) > 1:
            self.cmd_list_pos = len(self.command_list)

        console_output = self.git_manager.handle_commands(cmd, self.file_dict)  # handle command
        self.add_text_to_console(console_output)  # show output in console

        # if self.cmd == "git add ." and not self.prompt or type == 0:
        #     self.valid = self.git.check_move(0)
        #     self.showCard(0, self.valid)
        # elif self.cmd == "git commit" and not self.prompt or type == 1:
        #     self.valid = self.git.check_move(1)
        #     if self.valid:
        #         self.add_cmd_text("git commit \nuser@what-the-git repo_folder % Enter your commit message\n")
        #         self.hide_cards()
        #         self.prompt = True
        #         self.cmd = None
        # elif self.prompt:
        #     self.add_cmd_text("user@what-the-git repo_folder % " + self.cmd)
        #     self.prompt = False
        #     self.showCard(1, self.valid)
        # elif self.cmd == "git push" and not self.prompt or type == 2:
        #     self.valid = self.git.check_move(2)
        #     self.showCard(2, self.valid)
        # else:
        #     print("Invalid move")

    def save_file(self, file_name):

        file_location = f'{self.current_directory}/wtg/CH{self.chapter_num}/{file_name}'

        with open(file_location) as f:
            file_contents = f.read()

        with open(file_location, 'w') as f:
            if file_contents != self.file1_qplaintextedit.toPlainText():
                print('replacing')
                f.write(self.file1_qplaintextedit.toPlainText())
                self.file_dict[file_name].set_file_modified_status_true()

        self.file_stacked_widget.setCurrentIndex(self.file_stacked_widget.currentIndex() - 1)

    def create_cards(self, num):
        for i in range(num):
            self.card_list.append(
                DraggableCardImages(self.main_chapter_frame, None, 100 + 200 * i, i, self, self.git_manager))

    def showCard(self, card_type, valid):
        if valid:
            if card_type == 0:
                self.head_state_widget.show()
                self.commit_connect_line.show()
                self.head_label.show()
                self.task_one.setStyleSheet("background-color: rgb(32, 167, 21);;\n"
                                            "border-radius: 5px; \n"
                                            "padding-left:5px")

                self.console.setStyleSheet("background-color: rgb(30, 30, 30); font: 11pt \"Menlo\"; color: "
                                           "white")
                self.add_text_to_console("git add .\nuser@what-the-git repo_folder % ")

            elif card_type == 1:
                self.task_two.setStyleSheet("background-color: rgb(32, 167, 21);\n"
                                            "border-radius: 5px; \n"
                                            "padding-left:5px")
                self.add_text_to_console("\nuser@what-the-git repo_folder % [main 431c953] " + self.cmd)
                self.add_text_to_console(" 1 file changed, 1 insertions(+), 0 deletions(-)\n")
                self.add_text_to_console("create mode 100644 a.txt\nuser@what-the-git repo_folder % ")
                self.show_card()

            elif card_type == 2:
                self.commit_state_widget.show()
                self.first_commit_label.show()
                self.task_three.setStyleSheet("background-color: rgb(32, 167, 21);\n"
                                              "border-radius: 5px; \n"
                                              "padding-left:5px")
                self.add_text_to_console("git push\nEnumerating objects: 4, done.\n")
                self.add_text_to_console(
                    "Counting objects: 100% (4/4), done.\nDelta compression using up to 10 threads\n")
                self.add_text_to_console("Compressing objects: 100% (2/2), done.\n")
                self.add_text_to_console("Writing objects: 100% (3/3), 287 bytes | 287.00 KiB/s, done.\n")
                self.add_text_to_console("Total 3 (delta 0), reused 0 (delta 0), pack-reused 0\n")
                self.add_text_to_console("To https://github.com/git/wtg.git\n")
                self.add_text_to_console("   197bb24..431c953  main -> main\nuser@what-the-git repo_folder % ")

    def hide_cards(self):
        for i in self.card_list:
            i.hide()

    def show_card(self):
        for i in self.card_list:
            i.show()

    def add_text_to_console(self, new_output):
        existing_output = self.console.toPlainText()
        self.console.setText(existing_output + new_output)
        self.console.moveCursor(QtGui.QTextCursor.End)

    # def validCheck(self, card_type):
    #     if self.lastMove == card_type - 1:
    #         self.lastMove = card_type
    #         return True
    #     else:
    #         print("Invalid move")
    #         return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = ui_chapter_window(main_window)
    main_window.show()
    sys.exit(app.exec_())
