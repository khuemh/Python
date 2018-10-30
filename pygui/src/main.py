import window
import sys 
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window.App()
    sys.exit(app.exec_())
