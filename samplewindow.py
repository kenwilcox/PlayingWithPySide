#!python3.4

import sys
from PySide.QtGui import QApplication, QWidget, QIcon

class SampleWindow(QWidget):
    """ Our main window class
    """

    #Constructor function
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Icon Sample")
        self.setGeometry(300, 300, 200, 150)
        # self.setMinimumHeight(100)
        # self.setMinimumWidth(250)
        # self.setMaximumHeight(200)
        # self.setMaximumWidth(800)
    
    def setIcon(self):
        appIcon = QIcon('pyside_logo.png')
        self.setWindowIcon(appIcon)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        myWindow = SampleWindow()
        myWindow.setIcon()
        myWindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])

