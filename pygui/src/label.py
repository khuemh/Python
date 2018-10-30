import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Window'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.init_Window()
        self.init_Lable()
        
        
    def init_Window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


    def init_Lable(self):
        lable = QLabel(self)
        lable.setText('Hello World...!')
        lable.move(260, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()               # Create an App class object
    ex.show()                # Show ex object
    sys.exit(app.exec_())
