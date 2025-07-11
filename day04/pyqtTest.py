import sys
from PyQt5.QtWidgets import *

# QApplication 객체 생성
# 이 객체는 PyQt5 GUI 어플리케이션의 시작점,
# 이벤트 루프를 관리하고 GUI 전체를 실행하는 데 필요한 리소스를 초기화
app = QApplication(sys.argv)
#label = QLabel("Hello PyQt!!")
label = QPushButton("Quit") # 버튼 객체 생성 (버튼 이름 Quit)

# 버튼을 화면에 표시
label.show()

# 이벤트 루프를 시작하여 앱이 종요될 때까지 사용자 입력 기다림
# 이 부분이 없으면 창이 바로 닫힘
app.exec()
