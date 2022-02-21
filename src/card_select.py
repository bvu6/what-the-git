#!/usr/bin/env python3
# Made By Thicc-Juice
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem
from PyQt5.QtCore import Qt, QPointF


class MovingCards(QGraphicsRectItem):
    def __init__(self, x, y, r, l, app):
        super().__init__(0, 0, r, l)
        self.setPos(x, y)
        self.setBrush(Qt.blue)
        self.setAcceptHoverEvents(True)
        self.text = QGraphicsTextItem()
        self.text.setPos(x,y)
        self.text.setScale(2.5)
        self.app =app

    def setName(self, text):
        self.text.setPlainText(text)

    def getText(self):
        return self.text

    # mouse hover
    def hoverEnterEvent(self, event):
        self.app.instance().setOverrideCursor(Qt.OpenHandCursor)

    def hoverLeaveEvent(self, event):
        self.app.instance().restoreOverrideCursor()

    # mouse press
    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        origPos = event.lastScenePos()
        curPos = event.scenePos()

        orig_position = self.scenePos()

        updatedPosx = curPos.x() - origPos.x() + orig_position.x()
        updatedPosy = curPos.y() - origPos.y() + orig_position.y()
        self.setPos(QPointF(updatedPosx, updatedPosy))
        self.text.setPos(QPointF(updatedPosx, updatedPosy))

    def mouseReleaseEvent(self, event):
        print('x: {0}, y: {1}'.format(self.pos().x(), self.pos().y()))
        print(self.text.pos().x(), self.text.pos().y())


if __name__ == "__main__":
    pass

