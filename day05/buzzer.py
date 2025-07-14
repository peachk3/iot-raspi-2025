import RPi.GPIO as GPIO
import time

buzzerPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

try:
	GPIO.output(buzzerPin, GPIO.HIGH)
	print("Buzzer On")
	time.sleep(1)
	GPIO.output(buzzerPin, GPIO.LOW)
	print("Buzzer off")

except KeyboardInterrupt:
	print("end...")
finally:
	GPIO.cleanup()
