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
        self.init_Button()
        self.init_Lable()
        
        
    def init_Window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


    def init_Button(self):
        # Init Button 1
        but01 = QPushButton(self)
        but01.setText('Left Button')
        but01.setFlat(True)
        but01.move(100, 200)
        but01.clicked.connect(self.but01_clicked)

        # Init Button 2
        but02 = QPushButton(self)
        but02.setText('Right Button')
        but02.resize(100, 32)
#       but02.setMenu()
        but02.move(360, 200)
        but02.clicked.connect(self.but02_clicked)


    def init_Lable(self):
        lable = QLabel(self)
        lable.setText('Hello World...!')
        lable.setAlignment(Qt.AlignCenter)
#        lable.move(260, 100)


    @pyqtSlot()
    def but01_clicked(self):
        print('Left Button')
    
    def but02_clicked(self):
        print('Right Button')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()               # Create an App class object
    ex.show()                # Show ex object
    sys.exit(app.exec_())
