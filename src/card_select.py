#!/usr/bin/env python3
# Made By Thicc-Juice
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem
from PyQt5.QtCore import Qt, QPointF


class MovingCards(QGraphicsTextItem):
    # def __init__(self, x, y, r,l):
    #     super().__init__(0, 0, r, l)
    #     self.setPos(x, y)
    #     self.setBrush(Qt.blue)
    #     self.setAcceptHoverEvents(True)

    #mouse hover
    def hoverEnterEvent(self, event):
        app.instance().setOverrideCursor(Qt.OpenHandCursor)

    def hoverLeaveEvent(self, event):
        app.instance().restoreOverrideCursor()

    #mouse press
    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        origPos = event.lastScenePos()
        curPos = event.scenePos()

        orig_position = self.scenePos()

        updatedPosx = curPos.x() - origPos.x() + orig_position.x()
        updatedPosy = curPos.y() - origPos.y() + orig_position.y()
        self.setPos(QPointF(updatedPosx, updatedPosy))

    def mouseReleaseEvent(self, event):
        print('x: {0}, y: {1}'.format(self.pos().x(), self.pos().y()))

class GraphicView(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setSceneRect(0, 0, 1200, 1000)

        # self.moveObject = MovingCards(50, 50, 150, 200)
        # self.moveObject2 = MovingCards(250, 50, 150, 200)
        # self.moveObject3 = MovingCards(450, 50, 150, 200)
        # self.scene.addItem(self.moveObject)
        # self.scene.addItem(self.moveObject2)
        # self.scene.addItem(self.moveObject3)
        self.test = MovingCards()
        self.test.setPlainText("Git Add")
        self.test.setScale(5)
        self.test.setX(500)
        self.scene.addItem(self.test)
        self.test1 = MovingCards()
        self.test1.setPlainText("Git Commit")
        self.test1.setScale(5)
        self.test.setX(200)
        self.scene.addItem(self.test1)
        self.test2 = MovingCards()
        self.test2.setPlainText("Git Push")
        self.test2.setScale(5)
        self.test.setX(800)
        self.scene.addItem(self.test2)

app = QApplication(sys.argv)
view = GraphicView()
view.show()

sys.exit(app.exec_())
