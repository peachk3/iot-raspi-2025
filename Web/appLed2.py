from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

@app.route('/')
def ledFlask():
    return "LED Control Web"

@app.route('/led/<state>')
def led(state):
    if state == 'on':
        GPIO.output(ledPin, GPIO.HIGH)
    else:
        GPIO.output(ledPin, GPIO.LOW)

    return "LED " + state

@app.route('/led/clean')
def gpiocleanup():
    GPIO.cleanup()
    return "<h1> GPIO CLEANUP </h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1111)