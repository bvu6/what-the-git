from PyQt5 import QtCore, QtGui, QtWidgets
import os

from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QFont


class DraggableCardImages(QtWidgets.QLabel):
    def __init__(self, imgPath=None, parent=None, wid=None, x=None, type=None, chapter=None):
        super(DraggableCardImages, self).__init__()
        self.cardType = ["Git Add", "Git Commit", "Git Push"]
        self.chapter = chapter
        self.type = type
        self.setParent(parent)
        self.ogX = 50 + x
        self.ogY = 540
        # self.setStyleSheet("background-color: cyan")
        self.setStyleSheet(("background-image : url(image.png); background-position: center;"))
        self.setGeometry(QtCore.QRect(self.ogX, self.ogY, 111, 161))
        self.setScaledContents(True)
        self.setPixmap(QtGui.QPixmap(imgPath))
        self.drag_start_pos = None
        self.wid = wid
        self.setText(self.cardType[type])
        self.setFont(QFont("Arial", 15))
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
        # if self.x() > 800 or self.y() > 430:
        #     self.move(self.ogX, self.ogY)
        # else:
        #print("Doing", self.cardType[self.type])
        valid = self.chapter.validCheck(self.type)
        self.chapter.showCard(self.type, valid)
        self.move(self.ogX, self.ogY)

    def getType(self):
        print(self.cardType[self.type])
        return self.type

    # def mouseReleaseEvent(self, event):
    #     self.setCursor(QtCore.Qt.ArrowCursor)
    #     self.drag_start_pos = None
    #
    #     parent_layout = self.wid
    #
    #     all_images = [parent_layout.itemAt(i).widget() for i in range(parent_layout.count())]
    #
    #     # sort the list of widgets by their x position
    #     order = sorted(all_images, key=lambda i: i.pos().x())
    #
    #     # remove each item from the layout and insert the one that should go in that index.
    #     for idx, widget in enumerate(order):
    #         parent_layout.takeAt(idx)
    #         parent_layout.insertWidget(idx, widget)
    #
    #     super(DraggableCardImages, self).mouseReleaseEvent(event)

# class MainWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.horizontalLayout = QtWidgets.QHBoxLayout()
#         self.setLayout(self.horizontalLayout)
#         self._imgList = [
#             "images/cards/rm.png",
#             "images/cards/rm.png",
#         ]
#
#         for img in self._imgList:
#             print('1')
#             draggableImage = DraggableCardImages(imgPath=img, parent=self)
#             self.horizontalLayout.addWidget(draggableImage)
#
#
# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     win = MainWindow()
#     win.show()
#     sys.exit(app.exec_())
