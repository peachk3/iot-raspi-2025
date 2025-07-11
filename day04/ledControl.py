import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

class WindowClass(QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.ui = uic.loadUi("ledControl.ui", self)
		self.ui.show()

	def redBtnClick(self):
		current_text = self.ui.red_btn.text()
		self.ui.red_btn.setText("OFF" if current_text == "ON" else "ON")

	def blueBtnClick(self):
		current_text = self.ui.blue_btn.text()
		self.ui.blue_btn.setText("OFF" if current_text == "ON" else "ON")

	def greenBtnClick(self):
		current_text = self.ui.green_btn.text()
		self.ui.green_btn.setText("OFF" if current_text== "ON" else "ON")
	

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	app.exec_()

