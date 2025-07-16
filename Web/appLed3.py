from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

RED = 23
GREEN = 15
BLUE = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

@app.route('/')
def ledFlask():
    return "LED Color Control Web"

@app.route('/led/<color>')
def led(color):
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(BLUE, GPIO.LOW)
    
    if color == 'red':
        GPIO.output(GREEN, GPIO.HIGH)
    elif color == 'green':
        GPIO.output(RED, GPIO.HIGH)
    elif color == 'yellow':
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(RED, GPIO.HIGH)
    elif color == 'blue':
        GPIO.output(BLUE, GPIO.HIGH)
    elif color == 'purple':
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(BLUE, GPIO.HIGH)
    elif color == 'white':
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(BLUE, GPIO.HIGH)
    else:
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(BLUE, GPIO.LOW)
    return "<h1> LED " + color + "</h1>"

@app.route('/led/off')
def led_off():
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(BLUE, GPIO.LOW)
    return "<h1>LED OFF</h1>"


@app.route('/led/clean')
def gpiocleanup():
    GPIO.cleanup()
    return "<h1> GPIO CLEANUP </h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2222)