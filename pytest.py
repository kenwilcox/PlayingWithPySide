#!python3.4

import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QLabel

if __name__ == '__main__':
	myApp = QApplication(sys.argv)

	try:
		appLabel = QLabel()
		appLabel.setText("Hello, World!!!\nLook at my first app using PySide")
		appLabel.setAlignment(Qt.AlignCenter)
		appLabel.setWindowTitle("My First PySide Application")
		appLabel.setGeometry(300, 300, 250, 175)

		appLabel.show()

		myApp.exec_()
		sys.exit()
	except NameError:
		print("Name Error:", sys.exc_info()[1])
		pass
