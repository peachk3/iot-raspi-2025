import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 사용자 정의 윈도우 클래스 정의 : QWidget 상속
class MyApp(QWidget):
	def __init__(self):
		super().__init__() 	# 부모 생성자 호출시 super()
		self.initUi() 		# 사용자 정의 Ui 초기화 매서드 호출

	def initUi(self):
		# 윈도우 제목 설정
		self.setWindowTitle("My First Application")	# 윈도우 타이틀
	
		self.move(300, 300)		# 윈도우 위치
		self.resize(400, 200)	# 윈도우 크기
		self.show()				# 윈도우 표시

# 프로그램 진입점
if __name__ == "__main__":
	# QApplication 객체 생성 
	app = QApplication(sys.argv)

	# MyApp 클래스의 인스턴스 생성 (윈도우 생성)
	ex = MyApp()

	# 애플리케이션의 이벤트 루프 실행 후, 정상 종료 시 종료 코드 반환
	sys.exit(app.exec_())	
