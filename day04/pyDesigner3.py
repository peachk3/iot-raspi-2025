import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

class WindowClass(QDialog):
	def __init__(self, parent = None):
		super().__init__(parent) # 부모 생성자 호출
         # Qt Designer로 제작한 UI 파일 로드해 self에 적용
		self.ui = uic.loadUi("desi2.ui", self)
		self.ui.show()

	def slot1(self):
		self.ui.label.setText("left button clicked") # 위젯

	def slot2(self):
		self.ui.label.setText("right button clicked")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	app.exec_()
