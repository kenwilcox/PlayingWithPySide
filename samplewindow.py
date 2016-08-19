#!python3.4

import sys
from PySide.QtGui import QApplication, QWidget, QIcon, QLabel

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

    def setIconModes(self):
        myIcon1 = QIcon('pyside_logo.png')
        myLabel1 = QLabel('sample', self)
        pixmap1 = myIcon1.pixmap(50, 50, QIcon.Active, QIcon.On)
        myLabel1.setPixmap(pixmap1)

        myIcon2 = QIcon('pyside_logo.png')
        myLabel2 = QLabel('sample', self)
        pixmap2 = myIcon2.pixmap(50, 50, QIcon.Disabled, QIcon.Off)
        myLabel2.setPixmap(pixmap2)
        myLabel2.move(50, 0)

        myIcon3 = QIcon('pyside_logo.png')
        myLabel3 = QLabel('sample', self)
        pixmap3 = myIcon3.pixmap(50, 50, QIcon.Selected, QIcon.On)
        myLabel3.setPixmap(pixmap3)
        myLabel3.move(100, 0)


if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        myWindow = SampleWindow()
        myWindow.setIcon()
        myWindow.setIconModes()
        myWindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])

