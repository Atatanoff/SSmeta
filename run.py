import sys
from PyQt6.QtWidgets import QApplication
from activity.mainWin import MainWin


def main():
    app = QApplication(sys.argv)
    mainActivite = MainWin()    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()