import RPi.GPIO as GPIO # 라즈베리파이의 GPIO 핀을 제어하기 위한 라이브러리 임포트
import time # 시간 지연(sleep)을 위한 time 모듈 임포트

GPIO.setmode(GPIO.BCM) # GPIO 번호 체계를 BCM 방식으로 설정

RED = 14		# 핀 번호
GREEN = 15		# 핀 번호
BLUE = 18		# 핀 번호

# 각 핀을 출력 모드로 설정 (전기를 흘려보낼 수 있게 설정)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

# 횟수 입력 받기
num = int(input("LED를 몇 번 깜빡이시겠습니까? : "))

# 반복 실행
for i in range(num):

	# 초록 LED 켜기 (센서 에러로 RED 켜짐)
	GPIO.output(GREEN, GPIO.HIGH)	# 전압 출력 (LED ON)
	time.sleep(1) # 1초 유지
	GPIO.output(GREEN, GPIO.LOW) 	# 전압 끔 (LED OFF)
	time.sleep(1) # 1초 유지

	# 빨간 LED 켜기 (센서 에러로 GREEN 켜짐)
	GPIO.output(RED, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(RED, GPIO.LOW)
	time.sleep(1)
	
	# 파란 LED 켜기
	GPIO.output(BLUE, GPIO.HIGH)
	time.sleep(1)	
	GPIO.output(BLUE, GPIO.LOW)
	time.sleep(1)

# GPIO 핀 초기화
GPIO.cleanup()
