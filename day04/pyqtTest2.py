# event
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.initUi()

	def initUi(self):
		self.setWindowTitle("PyQt Button Test")
		self.move(300, 300)
		self.resize(400, 200)

		# QPushButton - 버튼 생성
		button = QPushButton("Click", self)		# Click이라는 이름의 버튼 생성
		button.move(20, 20)

		# 이벤트 핸들러를 connect로 연결
		button.clicked.connect(self.button_clicked)		# 버튼이 클릭되었을 때

	def button_clicked(self):
		QMessageBox.about(self, "message", "clicked")			# 메시지 띄우기
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = MyApp()
	ex.show()
	sys.exit(app.exec_())
	
