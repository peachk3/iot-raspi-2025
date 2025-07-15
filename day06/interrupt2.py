import RPi.GPIO as GPIO
import time

BLUE = 14
swPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led_state = False

def ledcallback(channel):
	global led_state

	led_state = not led_state

	if led_state:
		GPIO.output(BLUE, GPIO.HIGH)
		print("BLUE ON")
	else:
		GPIO.output(BLUE, GPIO.LOW)
		print("BLUE OFF")
    
# 이벤트 감지 설정 
GPIO.add_event_detect(swPin, GPIO.FALLING, callback=ledcallback)

try:
	GPIO.output(BLUE, GPIO.LOW)
	while True:
		time.sleep(1)
		
except KeyboardInterrupt:
	GPIO.output(BLUE, GPIO.LOW)
	GPIO.cleanup()
    
