import sys
from PyQt6.QtWidgets import (QMainWindow,
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QPushButton,
                             QStackedLayout,
                             QApplication)
from loguru import logger

from widgets import ProjectWin



class MainWin(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()


    def initUI(self):
        cw = QWidget()
        contl = QStackedLayout()
        prjct_win = ProjectWin()            

        vboxleft = QVBoxLayout()
        vboxleft.addWidget(prjct_win)
        vboxleft.addStretch()

        vboxright = QVBoxLayout()

        hbox = QHBoxLayout()
        hbox.addLayout(vboxleft)
        hbox.addLayout(vboxright)
        hbox.setStretchFactor(vboxleft,1)
        hbox.setStretchFactor(vboxright,4)

        cw.setLayout(hbox)
        self.setCentralWidget(cw)
        self.setGeometry(50, 50, 1200, 600)
        self.setWindowTitle('Проекты Электромонтажа')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainActivite = MainWin()    
    sys.exit(app.exec())

