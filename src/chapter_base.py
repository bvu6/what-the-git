from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import sys
import os
from cards import DraggableCardImages


class ui_chapter_window(object):
    def __init__(self, MainChapterWindow):
        MainChapterWindow.setObjectName("MainChapterWindow")
        MainChapterWindow.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainChapterWindow.sizePolicy().hasHeightForWidth())
        MainChapterWindow.setSizePolicy(sizePolicy)
        MainChapterWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainChapterWindow.setMaximumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainChapterWindow.setFont(font)
        MainChapterWindow.setStyleSheet("")
        MainChapterWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_chapter_central_widget = QtWidgets.QWidget(MainChapterWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_chapter_central_widget.sizePolicy().hasHeightForWidth())
        self.main_chapter_central_widget.setSizePolicy(sizePolicy)
        self.main_chapter_central_widget.setMinimumSize(QtCore.QSize(1280, 720))
        self.main_chapter_central_widget.setMaximumSize(QtCore.QSize(1281, 720))
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
        self.main_view = QtWidgets.QGraphicsView(self.main_chapter_frame)
        self.main_view.setGeometry(QtCore.QRect(0, 60, 821, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_view.sizePolicy().hasHeightForWidth())
        self.main_view.setSizePolicy(sizePolicy)
        self.main_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.main_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.main_view.setObjectName("main_view")
        self.chapter_info_text_browser = QtWidgets.QTextBrowser(self.main_chapter_frame)
        self.chapter_info_text_browser.setGeometry(QtCore.QRect(830, 70, 441, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chapter_info_text_browser.sizePolicy().hasHeightForWidth())
        self.chapter_info_text_browser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        self.chapter_info_text_browser.setFont(font)
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
        self.cmd_output_scroll_area.setWidgetResizable(True)
        self.cmd_output_scroll_area.setObjectName("cmd_output_scroll_area")
        self.cmd_output_contents = QtWidgets.QWidget()
        self.cmd_output_contents.setGeometry(QtCore.QRect(0, 0, 437, 173))
        self.cmd_output_contents.setObjectName("cmd_output_contents")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.cmd_output_contents)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cmd_output_text = QtWidgets.QTextBrowser(self.cmd_output_contents)
        font = QtGui.QFont()
        self.cmd_output_text.setFont(font)
        self.cmd_output_text.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.cmd_output_text.setObjectName("cmd_output_text")
        self.horizontalLayout_4.addWidget(self.cmd_output_text)
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
        self.toggleoff_music_button = QtWidgets.QPushButton(self.main_chapter_frame)
        self.toggleoff_music_button.setGeometry(QtCore.QRect(180, 20, 120, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_music_button.sizePolicy().hasHeightForWidth())
        self.toggle_music_button.setSizePolicy(sizePolicy)
        self.toggle_music_button.setMinimumSize(QtCore.QSize(0, 0))
        self.toggleoff_music_button.setSizePolicy(sizePolicy)
        self.toggleoff_music_button.setMinimumSize(QtCore.QSize(0, 0))
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
        self.toggleoff_music_button.setFont(font)
        self.toggleoff_music_button.setStyleSheet("QPushButton {\n"
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
        self.toggleoff_music_button.setObjectName("toggle_music_button")
        # play Song
        self.player = QMediaPlayer()
        self.toggleoff_music_button.hide()
        self.toggle_music_button.clicked.connect(lambda: self.playSong())
        self.toggleoff_music_button.clicked.connect(lambda: self.stopSong())

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
        self.file_stacked_widget.setObjectName("file_stacked_widget")
        self.file_main_page = QtWidgets.QWidget()
        self.file_main_page.setObjectName("file_main_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.file_main_page)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.files_frame_2 = QtWidgets.QFrame(self.file_main_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.files_frame_2.sizePolicy().hasHeightForWidth())
        self.files_frame_2.setSizePolicy(sizePolicy)
        self.files_frame_2.setStyleSheet("background-color: rgb(0, 157, 255);border-radius: 5px")
        self.files_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.files_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.files_frame_2.setObjectName("files_frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.files_frame_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.files_horiz_layout = QtWidgets.QHBoxLayout()
        self.files_horiz_layout.setSpacing(0)
        self.files_horiz_layout.setObjectName("files_horiz_layout")
        self.file_img1 = QtWidgets.QTextBrowser(self.files_frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_img1.sizePolicy().hasHeightForWidth())
        self.file_img1.setSizePolicy(sizePolicy)
        self.file_img1.setMaximumSize(QtCore.QSize(40, 63))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.file_img1.setFont(font)
        self.file_img1.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.file_img1.setStyleSheet("")
        self.file_img1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.file_img1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.file_img1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.file_img1.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.file_img1.setObjectName("file_img1")
        self.files_horiz_layout.addWidget(self.file_img1)
        self.horizontalLayout_6.addLayout(self.files_horiz_layout)
        self.gridLayout_2.addWidget(self.files_frame_2, 0, 0, 1, 1)
        self.file_stacked_widget.addWidget(self.file_main_page)
        self.file_txt_page1 = QtWidgets.QWidget()
        self.file_txt_page1.setObjectName("file_txt_page1")
        self.gridLayout = QtWidgets.QGridLayout(self.file_txt_page1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.file_txt1_edit = QtWidgets.QPlainTextEdit(self.file_txt_page1)
        font = QtGui.QFont()
        self.file_txt1_edit.setFont(font)
        self.file_txt1_edit.setAutoFillBackground(False)
        self.file_txt1_edit.setStyleSheet("border: 1px solid white;\n"
                                          "border-radius: 5px")
        self.file_txt1_edit.setObjectName("file_txt1_edit")
        self.gridLayout.addWidget(self.file_txt1_edit, 0, 0, 1, 1)
        self.file_txt1_button = QtWidgets.QPushButton(self.file_txt_page1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_txt1_button.sizePolicy().hasHeightForWidth())
        self.file_txt1_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.file_txt1_button.setFont(font)
        self.file_txt1_button.setStyleSheet("QPushButton {\n"
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
        self.file_txt1_button.setObjectName("file_txt1_button")
        self.gridLayout.addWidget(self.file_txt1_button, 0, 1, 1, 1)
        self.file_stacked_widget.addWidget(self.file_txt_page1)
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
        font.setPointSize(13)
        font.setBold(True)
        self.task_one.setFont(font)
        self.task_one.setStyleSheet("background-color: rgb(138, 0, 1);\n"
                                    "border-radius: 5px; \n"
                                    "padding-left:5px")
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
        font.setPointSize(13)
        font.setBold(True)
        self.task_two.setFont(font)
        self.task_two.setStyleSheet("background-color: rgb(138, 0, 1);\n"
                                    "border-radius: 5px; \n"
                                    "padding-left:5px")
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
        font.setPointSize(13)
        font.setBold(True)
        self.task_three.setFont(font)
        self.task_three.setStyleSheet("background-color: rgb(138, 0, 1);\n"
                                      "border-radius: 5px; \n"
                                      "padding-left:5px")
        self.task_three.setAlignment(QtCore.Qt.AlignCenter)
        self.task_three.setObjectName("task_three")
        self.task_vert_layout.addWidget(self.task_three)
        self.frame = QtWidgets.QFrame(self.main_chapter_frame)
        self.frame.setGeometry(QtCore.QRect(0, 500, 821, 220))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 220))
        self.frame.setStyleSheet("\n"
                                 "background-color:  #F4D782;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title_label = QtWidgets.QLabel(self.main_chapter_frame)
        self.title_label.setGeometry(QtCore.QRect(830, 10, 439, 59))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("")
        self.title_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.title_label.setObjectName("title_label")
        # self.rm_card = QtWidgets.QLabel(self.main_chapter_frame)
        # self.rm_card.setGeometry(QtCore.QRect(130, 420, 145, 190))
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.rm_card.sizePolicy().hasHeightForWidth())
        # self.rm_card.setSizePolicy(sizePolicy)
        # self.rm_card.setMaximumSize(QtCore.QSize(145, 190))
        # font = QtGui.QFont()
        # self.rm_card.setFont(font)
        # self.rm_card.setText("")
        # self.rm_card.setPixmap(QtGui.QPixmap("images/cards/rm.png"))
        # self.rm_card.setScaledContents(True)
        # self.rm_card.setObjectName("rm_card")

        # self._imgList = [
        #     "images/cards/rm.png",
        #     "images/cards/rm.png",
        # ]
        #
        # for img in self._imgList:
        #     print('1')
        #     self.card =  DraggableCardImages(imgPath=img, parent=self.main_chapter_frame, wid=None)
        self.verticalWidget = QtWidgets.QWidget(self.main_chapter_frame)
        self.verticalWidget.setGeometry(QtCore.QRect(80, 210, 160, 80))
        self.verticalWidget.setStyleSheet("background-color: rgb(4, 255, 0)")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalWidget_2 = QtWidgets.QWidget(self.main_chapter_frame)
        self.verticalWidget_2.setGeometry(QtCore.QRect(290, 210, 160, 80))
        self.verticalWidget_2.setStyleSheet("background-color: rgb(4, 255, 0)")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalWidget_3 = QtWidgets.QWidget(self.main_chapter_frame)
        self.verticalWidget_3.setGeometry(QtCore.QRect(510, 210, 160, 80))
        self.verticalWidget_3.setStyleSheet("background-color: rgb(4, 255, 0)")
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalWidget_3.hide()
        self.verticalWidget_2.hide()
        self.verticalWidget.hide()

        # ^^ widget creation for dragging card
        self.createCards(3)

        MainChapterWindow.setCentralWidget(self.main_chapter_central_widget)

        self.retranslateUi(MainChapterWindow)
        self.file_stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainChapterWindow)

    def retranslateUi(self, MainChapterWindow):
        _translate = QtCore.QCoreApplication.translate
        MainChapterWindow.setWindowTitle(_translate("MainChapterWindow", "MainWindow"))
        self.chapter_info_text_browser.setHtml(_translate("MainChapterWindow",
                                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Montserrat\'; font-size:14pt;\">Drag the card or type in the command to add, commit, and push your first file!</span></p></body></html>"))
        self.cmd_output_text.setHtml(_translate("MainChapterWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'Montserrat\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Menlo\'; font-size:11pt; color:#ffffff;\">user@what-the-git repo_folder % </span></p></body></html>"))
        self.cmd_output_text.setPlaceholderText(_translate("MainChapterWindow", "user@what-the-git repo_folder %"))
        self.back_button.setText(_translate("MainChapterWindow", "Back"))
        self.toggle_music_button.setText(_translate("MainChapterWindow", "Toggle Music"))
        self.toggleoff_music_button.setText(_translate("MainChapterWindow", "Toggle Off Music"))
        self.reload_button.setText(_translate("MainChapterWindow", "Reload"))
        self.file_img1.setHtml(_translate("MainChapterWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Montserrat\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"media/txt_img.png\" width=\"35\" height=\"40\" /></p>\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; color:#ffffff;\"> a.txt</span></p></body></html>"))
        self.file_txt1_edit.setPlainText(_translate("MainChapterWindow", "hello world"))
        self.file_txt1_button.setText(_translate("MainChapterWindow", "Done"))
        self.task_one.setText(_translate("MainChapterWindow", "Add a.txt"))
        self.task_two.setText(_translate("MainChapterWindow", "Commit the change!"))
        self.task_three.setText(_translate("MainChapterWindow", "Push!"))
        self.title_label.setText(_translate("MainChapterWindow", "CH1: First Commit"))

    def createCards(self, num):
        cardList = []
        for i in range(num):
            cardList.append(DraggableCardImages("cards/rm.png", self.main_chapter_frame, None, 150 * i, i, self))

    def playSong(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        print(current_path)
        print("song Playing")
        full_file_path = os.path.join(current_path, 'music/track.mp3')
        print(full_file_path)
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
        self.toggle_music_button.hide()
        self.toggleoff_music_button.show()

    def stopSong(self):
        self.player.stop()
        self.toggleoff_music_button.hide()
        self.toggle_music_button.show()
        print("Song Stopped")

    def showCard(self, type):
        if type == 0:
            self.verticalWidget.show()
            self.task_one.setStyleSheet("background-color: rgb(4, 255, 1);\n"
                                          "border-radius: 5px; \n"
                                          "padding-left:5px")

        elif type == 1:
            self.verticalWidget_2.show()
            self.task_two.setStyleSheet("background-color: rgb(4, 255, 1);\n"
                                          "border-radius: 5px; \n"
                                          "padding-left:5px")
        elif type == 2:
            self.verticalWidget_3.show()
            self.task_three.setStyleSheet("background-color: rgb(4, 255, 1);\n"
                                          "border-radius: 5px; \n"
                                          "padding-left:5px")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainChapterWindow = QtWidgets.QMainWindow()
    ui = ui_chapter_window(MainChapterWindow)
    MainChapterWindow.show()
    sys.exit(app.exec_())
