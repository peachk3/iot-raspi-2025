import RPi.GPIO as GPIO
import time

piezoPin = 18 

Melody = [131, 146, 164, 174, 196, 220, 247, 262]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)
# 해당 핀에 440hz 출력
sound = GPIO.PWM(piezoPin, 440)

try:
	while True:
		sound.start(50)	#튜티비(50%)로 시작!
		for i in range(0, len(Melody)): 
			sound.ChangeFrequency(Melody[i])	# 주파수 변경
			time.sleep(0.7)
		sound.stop()		# PWM 중지
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
