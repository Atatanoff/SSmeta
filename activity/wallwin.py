import sys
from PyQt6 import QtCore
from PyQt6.QtCore import QObject, pyqtSignal, QSize
from PyQt6.QtWidgets import (QWidget, QApplication,
                              QHBoxLayout, QVBoxLayout,
                              QLabel, QPushButton)
from PyQt6.QtGui import QPixmap, QIcon

from widgets import Color


class WallWin(QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.initUI()

    def initUI(self):
        btnsocket = QPushButton('')
        btnsocket.setIcon(QIcon('res/drawable/socket.png'))
        btnsocket.setIconSize(QSize(24,24))

        lblsocket = QLabel("Одинарная розетка")

        hbox = QHBoxLayout()
        hbox.addWidget(lblsocket)
        hbox.addWidget(btnsocket)

        
        menubox = QVBoxLayout()
        menubox.addLayout(hbox)

        mainbox = QHBoxLayout() 
        mainbox.addLayout(menubox)        

        self.setLayout(mainbox)
        # self.setGeometry(500, 300, 1000, 600)
        # self.setWindowTitle('Тестовое окно')
        # self.show()


def main():

    app = QApplication(sys.argv)
    ex = WallWin()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
