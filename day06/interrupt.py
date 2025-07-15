import  RPi.GPIO as GPIO
import time

swPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def printcallback(channel):
    print("pushed")
    

GPIO.add_event_detect(swPin, GPIO.RISING, callback=printcallback)

try:
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
