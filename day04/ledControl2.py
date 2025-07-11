import RPi.GPIO as GPIO
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

GPIO.setmode(GPIO.BCM)

RED = 14
GREEN = 15
BLUE = 18

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

GPIO.output(RED, GPIO.LOW)
GPIO.output(GREEN, GPIO.LOW)
GPIO.output(BLUE, GPIO.LOW)

class WindowClass(QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.ui = uic.loadUi("ledControl.ui", self)
		self.ui.show()

		self.red_state = False
		self.green_state = False
		self.blue_state = False

	def redBtnClick(self):
		current_text = self.ui.red_btn.text()
		if current_text == "OFF": # 버튼을 눌렀을 때 현재 꺼져있는 상태라면 LED ON
			GPIO.output(GREEN, GPIO.HIGH)   # 모듈 오류로 GREEN -> RED
			self.ui.red_btn.setText("ON")
			self.red_state = True   # 버튼 상태 변경
			print("RED ON")
		else:
			GPIO.output(GREEN, GPIO.LOW)
			self.ui.red_btn.setText("OFF")
			self.ui.red_state = False
			print("RED OFF")

	def blueBtnClick(self):
		current_text = self.ui.blue_btn.text()
		if current_text == "OFF":
			GPIO.output(BLUE, GPIO.HIGH)
			self.ui.blue_btn.setText("ON")
			self.blue_state = True
			print("BLUE ON")
		else:
			GPIO.output(BLUE, GPIO.LOW)
			self.ui.blue_btn.setText("OFF")
			self.ui.blue_state = False
			print("BLUE OFF")

	def greenBtnClick(self):
		current_text = self.ui.green_btn.text()
		if current_text == "OFF":
			GPIO.output(RED, GPIO.HIGH)
			self.ui.green_btn.setText("ON")
			self.green_state = True
			print("GREEN ON")
		else:
			GPIO.output(RED, GPIO.LOW)
			self.ui.green_btn.setText("OFF")
			self.ui.green_state = False
			print("GREEN OFF")

	def allLedBtnClick(self):
		current_text = self.ui.all_led_btn.text()
		if current_text == "OFF":
			GPIO.output(GREEN, GPIO.HIGH)
			GPIO.output(RED, GPIO.HIGH)
			GPIO.output(BLUE, GPIO.HIGH)
			self.ui.all_led_btn.setText("ON")
			self.ui.green_btn.setText("ON")
			self.ui.blue_btn.setText("ON")
			self.ui.red_btn.setText("ON")
			self.green_state = True
			self.blue_state = True
			self.red_state = True
			print("전체 조명 ON")
		else:
			GPIO.output(GREEN, GPIO.LOW)
			GPIO.output(RED, GPIO.LOW)
			GPIO.output(BLUE, GPIO.LOW)
			self.ui.all_led_btn.setText("OFF")
			self.ui.green_btn.setText("OFF")
			self.ui.blue_btn.setText("OFF")
			self.ui.red_btn.setText("OFF")
			self.green_state = False
			self.blue_state = False
			self.red_state = False
			print("전체 조명 OFF")
			
	def closeEvent(self, event):
		GPIO.cleanup()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	app.exec_()
