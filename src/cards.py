from PyQt5 import QtCore, QtGui, QtWidgets
import os

from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QFont


class DraggableCardImages(QtWidgets.QLabel):
    def __init__(self, parent=None, wid=None, x=None, type=None, chapter=None, gitStatus=None):
        super(DraggableCardImages, self).__init__()
        self.git = gitStatus
        self.cardType = ["git add", "git commit", "git push", "git branch", "git checkout \nbranch", "git checkout "
                                                                                                     "\nhead (ID)"]
        self.chapter = chapter
        self.type = type
        self.setParent(parent)
        self.ogX = 50 + x
        self.ogY = 540
        self.setStyleSheet("background-image : url(image.png); background-position: center;")
        self.setGeometry(QtCore.QRect(self.ogX, self.ogY, 111, 161))
        self.setScaledContents(True)
        self.drag_start_pos = None
        self.wid = wid
        self.setText(self.cardType[type])
        self.setFont(QFont("Montserrat", 13))
        self.setAlignment(QtCore.Qt.AlignHCenter)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.setCursor(QtCore.Qt.ClosedHandCursor)
            # This will give us the start position when a drag is triggered
            self.drag_start_pos = event.pos()
            self.raise_()
        super(DraggableCardImages, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.drag_start_pos is not None:
            # While left button is clicked the widget will move along with the mouse
            self.move(self.pos() + event.pos() - self.drag_start_pos)
        super(DraggableCardImages, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.x() > 800 or self.y() > 430:
            self.move(self.ogX, self.ogY)
        else:
            self.chapter.execute_command(self.type)
            self.move(self.ogX, self.ogY)

    def getType(self):
        print(self.cardType[self.type])
        return self.type