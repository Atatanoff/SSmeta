#!/usr/bin/python
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QWidget, QApplication, QLabel, QPushButton, QGraphicsView,
                              QMainWindow,QVBoxLayout, QHBoxLayout, QGraphicsScene)
from PyQt6.QtGui import QPainter, QPen, QPixmap, QColor
from PyQt6.QtCore import Qt
import sys
from loguru import logger

from widgets import PowerSocket, MenuWallWin


class PaintWin(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()


class ExampleMainWin(QWidget):  

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Socket Pain')
        self.setGeometry(500, 300, 1000, 600)

        w_menu = MenuWallWin()
        paint_win = PaintWin()
        

        vbox_menu = QVBoxLayout()
        vbox_menu.addWidget(w_menu)

        self.vbox_paint = QVBoxLayout()
        self.vbox_paint.addWidget(paint_win)        

        hbox = QHBoxLayout()
        hbox.addLayout(vbox_menu)
        hbox.addLayout(self.vbox_paint)
 

        self.setLayout(hbox)

        



        
    


def main():
    
    app = QApplication(sys.argv)
    ex = ExampleMainWin()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()