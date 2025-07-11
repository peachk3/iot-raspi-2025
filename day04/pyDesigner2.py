import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("desi1.ui")[0]

class WindowClass(QDialog, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		
	def buttonSlot(self): pass

if __name__=="__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
