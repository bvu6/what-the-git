#!/usr/bin/env python3
# Made By Thicc-Juice
# What The Git!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainChapterWindow(object):
    def setupUi(self, MainChapterWindow):
        MainChapterWindow.setObjectName("MainChapterWindow")
        MainChapterWindow.resize(916, 692)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainChapterWindow.sizePolicy().hasHeightForWidth())
        MainChapterWindow.setSizePolicy(sizePolicy)
        MainChapterWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.main_chapter_central_widget = QtWidgets.QWidget(MainChapterWindow)
        self.main_chapter_central_widget.setObjectName("main_chapter_central_widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.main_chapter_central_widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 469, 631, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        MainChapterWindow.setCentralWidget(self.main_chapter_central_widget)
        self.menubar = QtWidgets.QMenuBar(MainChapterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 21))
        self.menubar.setObjectName("menubar")
        MainChapterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainChapterWindow)
        self.statusbar.setObjectName("statusbar")
        MainChapterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainChapterWindow)
        QtCore.QMetaObject.connectSlotsByName(MainChapterWindow)

    def retranslateUi(self, MainChapterWindow):
        _translate = QtCore.QCoreApplication.translate
        MainChapterWindow.setWindowTitle(_translate("MainChapterWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainChapterWindow = QtWidgets.QMainWindow()
    ui = Ui_MainChapterWindow()
    ui.setupUi(MainChapterWindow)
    MainChapterWindow.show()
    sys.exit(app.exec_())
