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
        self.init_msgbox() 
        self.init_button()
        

    def init_Window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
        

    def init_button(self):
        button = QPushButton(self)
        button.setText('Show message')
        button.move(100, 200)
        button.clicked.connect(self.msgshow)
        self.show()
        
    
    def init_msgbox(self):
        message = QMessageBox.question(self, 'Message', 'Do you want to fuck off?', 
                                           QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, 
                                           QMessageBox.Cancel)
        if message == QMessageBox.Yes:
            print('Yes, I want')
        elif message == QMessageBox.No:
            print('No, I don\'t')
        elif message == QMessageBox.Cancel:
            print('Cancel')
        self.show()    
    

    @pyqtSlot()
    def msgshow(self):
        init_msgbox()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()               # Create an App class object
    sys.exit(app.exec_())
