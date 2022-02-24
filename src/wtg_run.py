#!/usr/bin/env python3
# Made By Thicc-Juice
# What The Git!
import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from chapter_selector import ui_chapter_selection_window
from start_screen import ui_start_window
from chapter_base import ui_chapter_window
import sys


class MainWindow:

    def __init__(self):

        # UI
        self.main_window = QtWidgets.QMainWindow()
        self.ui = ui_start_window(self.main_window)
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.stacked_widget.addWidget(self.main_window)
        self.stacked_widget.setFixedWidth(1280)
        self.stacked_widget.setFixedHeight(720)
        self.stacked_widget.show()

        # Music
        self.music_player = QMediaPlayer()
        self.play_music = False
        self.full_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'music/track.mp3')
        self.url = QUrl.fromLocalFile(self.full_file_path)
        self.music_player.setMedia(QMediaContent(self.url))
        self.music_player.play()
        self.ui.playButton.clicked.connect(lambda: self.switch_to_chapter_selector())

    def update_stacked_widget(self):
        self.stacked_widget.hide()
        self.stacked_widget.removeWidget(self.main_window)
        self.stacked_widget.addWidget(self.main_window)
        self.stacked_widget.show()

    def switch_to_chapter_selector(self):
        self.ui = ui_chapter_selection_window(self.main_window)
        self.update_stacked_widget()
        self.ui.toggle_music_button.setCheckable(self.play_music)
        self.ui.toggle_music_button.clicked.connect(lambda: self.manage_song(self.ui.toggle_music_button))
        self.ui.chapter_one_start_button.clicked.connect(lambda: self.switch_to_level_one())

    def switch_to_level_one(self):
        self.ui = ui_chapter_window(self.main_window)
        self.update_stacked_widget()
        self.ui.toggle_music_button.setCheckable(self.play_music)
        self.ui.toggle_music_button.clicked.connect(lambda: self.manage_song(self.ui.toggle_music_button))
        self.ui.reload_button.clicked.connect(lambda: self.switch_to_level_one())
        self.ui.back_button.clicked.connect(lambda: self.switch_to_chapter_selector())

    def manage_song(self, toggle_music_button):
        toggle_music_button.setCheckable(self.play_music)
        if toggle_music_button.isChecked():
            self.play_music = False
            toggle_music_button.setCheckable(self.play_music)
            full_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'music/track.mp3')
            url = QUrl.fromLocalFile(full_file_path)
            content = QMediaContent(url)
            self.music_player.setMedia(content)
            self.music_player.play()

        else:
            self.play_music = True
            toggle_music_button.setCheckable(self.play_music)
            self.music_player.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
