import RPi.GPIO as GPIO
import time

buttonPin = 17

GPIO.setmode(GPIO.BCM)
# pull_up_dow=GPIO.PUD_UP 내부 풀업 풀다운 설정
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		if(GPIO.input(buttonPin) == GPIO.LOW):
			print(f"button pressed")
		else:
			print("button released")
		time.sleep(0.3)
except KeyboardInterrupt:
	GPIO.cleanup()
