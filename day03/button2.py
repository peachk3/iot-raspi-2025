# 1초 이내 연속으로 누르는 수만큼 LED 색 변환하기
# 수정 필요!!!
import RPi.GPIO as GPIO
import time

RED = 14
GREEN = 15
BLUE = 18
buttonPin = 17

GPIO.setmode(GPIO.BCM)
# 내부 풀업 저항 설정 (버튼이 눌리지 않았을 때 HIGH, 눌렸을 때 LOW)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

press_count = 0  # 눌린 횟수
last_button_state = GPIO.HIGH  # 이전 버튼 상태 저장
current_button_state = GPIO.HIGH  # 현재 버튼 상태 저장
last_press_time = 0
TIMEOUT = 1.0 # 1초 내에 연속으로 눌러야 함!

def turn_off_all_leds():
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(BLUE, GPIO.LOW)


try:
    while True:
        current_button_state = GPIO.input(buttonPin)
        current_time = time.time()
        
        # 버튼이 눌린 순간 감지 (HIGH -> LOW 변화)
        if last_button_state == GPIO.HIGH and current_button_state == GPIO.LOW:
            # 이전 누름으로부터 시간 경과 확인
            if current_time - last_press_time > TIMEOUT:
                press_count = 0
            
                print(f"button pressed: {press_count}")

                # 1번 눌렀을 때는 LED 모두 끄기
                if press_count == 1:
                    GPIO.output(GREEN, GPIO.LOW)
                    GPIO.output(RED, GPIO.LOW)
                    GPIO.output(BLUE, GPIO.LOW)
                    print("LED OFF")
                elif press_count == 2:
                    GPIO.output(GREEN, GPIO.HIGH)
                    GPIO.output(RED, GPIO.LOW)
                    GPIO.output(BLUE, GPIO.LOW)
                    print("RED ON")
                elif press_count == 3:
                    GPIO.output(RED, GPIO.HIGH)
                    GPIO.output(GREEN, GPIO.LOW)
                    GPIO.output(BLUE, GPIO.LOW)
                    print("GREEN ON")
                elif press_count == 4:
                    GPIO.output(BLUE, GPIO.HIGH)
                    GPIO.output(RED, GPIO.LOW)
                    GPIO.output(GREEN, GPIO.LOW)
                    print("BLUE ON")
                elif press_count >= 5:
                    press_count = 0
                    print("count reset. LED OFF")
                    GPIO.output(GREEN, GPIO.LOW)
                    GPIO.output(RED, GPIO.LOW)
                    GPIO.output(BLUE, GPIO.LOW)
        # 버튼이 떼어진 순간 감지 (LOW -> HIGH 변화)
        elif last_button_state == GPIO.LOW and current_button_state == GPIO.HIGH:
            print("button released")
        
        last_button_state = current_button_state
        time.sleep(0.05)  # 디바운싱을 위해 더 짧은 딜레이 사용

except KeyboardInterrupt:
    GPIO.cleanup()
