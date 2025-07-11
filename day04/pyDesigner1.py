import sys
from PyQt5. QtWidgets import *		# pyqt5의 모든 위젯 클래스 import
from PyQt5 import uic				# Qt Designer에서 만든 .ui 파일 불러오기 위한 모듈

# QDialog 기반 사용자 정의 클래스
class WindowClass(QDialog):		#  Dialog 생성
	def __init__(self, parent = None):
		super().__init__(parent)	# 부모 클래스(QDialog)의 생성자 호출

		# Qt Designer로 만든 UI 파일(desi1.ui)을 로드
		# self를 두 번째 인자로 넣어주면, 로드된 위젯들이 이 클래스에 바로 바인딩됨
		self.ui = uic.loadUi("desi1.ui", self)

		self.ui.show()

	# 버튼 클릭 등의 이벤트 처리용 슬롯 함수
	def buttonSlot(self): # pass Qt Designer에서 만든 버튼의 Slot
		print("Bye Bye~~")
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	app.exec_()
