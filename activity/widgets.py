import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (QWidget, QLabel, QHBoxLayout,
                             QApplication,
                             QPushButton,
                             QVBoxLayout,
                             QListWidget, QListWidgetItem,
                             QInputDialog)
from PyQt6.QtGui import QPalette, QColor, QPixmap, QIcon, QPainter
from loguru import logger


# окно для черчения
class PaintWin(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.h = 200
 
        cnv = QPixmap()
        cnv.fill(QColor('white'))
        
        self.lbl = QLabel()
        self.lbl.setPixmap(cnv)

        box = QVBoxLayout()   
        box.addWidget(self.lbl)

        self.setLayout(box)       

        self.resize(600, 600)
    
    def mouseMoveEvent(self, e):
        # координаты мышки
        x = e.pos().x()
        y = e.pos().y()
        logger.debug(f"{x}::{y}")

        canvas = self.lbl.pixmap()
        canvas.fill(QColor('white'))
        painter = QPainter(canvas)
        painter.begin(self)

        # горизонтальная линия
        painter.drawLine(0, y, int(x/2-20), y) 
        painter.drawLine(int(x/2+20), y, x, y)

        # вертикальная линия
        painter.drawLine(x, self.h, x, int(y+(self.h-y)/2+10))
        painter.drawLine(x, int(y+(self.h-y)/2-10), x, y)

        # размеры ()
        painter.drawText(x-10, int(y+(self.h-y)/2+6), str(self.h - e.pos().y()))
        painter.drawText(int(x/2-8), y+5, str(e.pos().x()))

        painter.end()
        self.lbl.setPixmap(canvas)

# меню окна с разметкой стен
class MenuWallWin(QWidget):
    def __init__(self) -> None:
        super().__init__()
        btn = QPushButton()
        btn.setIcon(QIcon('res/drawable/socket.png'))
        btn.setIconSize(QSize(20,20))
        btn.setFixedSize(30, 30)
        btn.
        
        text = QLabel("розетка одинарная")

        S1box = QHBoxLayout()
        S1box.addWidget(btn)
        S1box.addWidget(text)
        
        vbox = QVBoxLayout()
        vbox.addLayout(S1box)
    def 

        vbox.addStretch(1)


        self.setLayout(vbox)
        self.setFixedWidth(200)

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

# вкладка с проектами и кнопкой добавления
class ProjectWin(QWidget):
    def __init__(self) -> None:
        super().__init__()
        vbox_layout = QVBoxLayout(self)
        
        btn_create_prjct = QPushButton('Новый проект')
        btn_create_prjct.clicked.connect(self.createPrjct)
        

        self.circle_wid = QListWidget()
        for i in range(1, 100):
            QListWidgetItem(f"Project {i}", self.circle_wid)
        self.circle_wid.itemClicked.connect(self.openPrjct)


        
        vbox_layout.addWidget(btn_create_prjct)
        vbox_layout.addWidget(self.circle_wid)

        

       # self.setFixedHeight(400)
       # self.show()

    def createPrjct(self):
        name, done1 = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        logger.debug(f"Create: {name}")

    def openPrjct(self, item: QListWidgetItem):
        logger.debug(f"Open: {item.text()}")


class DrawWin():
    pass

# класс электрооборудование(розетки, вкл, настенные светильники и т.д.)
class ElectricalEquipment():

    def __init__(self) -> None:
        
        self.h = 200
        self.left_x = 50
        self.right_y = None

# виджет розетка
class PowerSocket(QWidget, ElectricalEquipment):

    def __init__(self) -> None:
        super().__init__()
        pic = QPixmap("res/drawable/socket.png")
        lbl = QLabel(self)
        lbl.setPixmap(pic)
        lbl.setFixedSize(20,20)
        self.show()


class Test(QWidget):
    def __init__(self) -> None:
        super().__init__()        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainActivite = PaintWin()   
    mainActivite.show() 
    sys.exit(app.exec())
