import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 정의
piezoPin = 18	# 부저
GREEN = 15		# 빨강 LED
BLUE = 14		# 파랑 LED
buttonPin = 17  # 버튼 핀

# GPIO 모드 설정 (BCM 모드)
GPIO.setmode(GPIO.BCM)

# 출력 핀 설정 
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(piezoPin, GPIO.OUT)

# 내부 풀업 저항 설정 (버튼 OFF - HIGH, ON - LOW)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# PWM 객체 생성 (부저 제어용, 초기 주파수 1000Hz)
sound = GPIO.PWM(piezoPin, 1000)

# 상태 변수 초기화
siren_on = False				# 사이렌 ON/OFF
last_button_state = GPIO.HIGH	# 이전 버튼 상태

try:
    while True:			# 무한 루프 실행
    	# 현재 버튼 상태 읽기
        current_button_state = GPIO.input(buttonPin)
        
        # 버튼 눌림 감지 (디바운싱)
        if last_button_state == GPIO.HIGH and current_button_state == GPIO.LOW:
            siren_on = not siren_on		# 사이렌 상태 토클
            time.sleep(0.3)  			# 디바운싱 딜레이 (버튼 중복 입력 방지)
            
            if siren_on:
                sound.start(50)			# PWM 시작 (듀티 사이클 50%)
                print("사이렌 ON")
            else: 
                sound.stop()			# PWM 정지
                # 모든 LED 끄기
                GPIO.output(GREEN, GPIO.LOW)
                GPIO.output(BLUE, GPIO.LOW)
                print("사이렌 OFF")

        # 현재 버튼 상태 저장
        last_button_state = current_button_state
        
        if siren_on:
            # 사이렌 패턴 1: 주파수 상승 + 빨강  LED
            # 400Hz에서 1600Hz까지 20Hz씩 증가
            for freq in range(400, 1600, 20):
            	# 사이렌 작동 중에도 버튼 체크(즉시 종료 가능)
                current_button_state = GPIO.input(buttonPin)
                if last_button_state == GPIO.HIGH and current_button_state == GPIO.LOW:
                    siren_on = False
                    time.sleep(0.3)
                    sound.stop()
                    GPIO.output(GREEN, GPIO.LOW)
                    GPIO.output(BLUE, GPIO.LOW)
                    print("사이렌 OFF")
                    break
                last_button_state = current_button_state

                # 사이렌 OFF -> 루프 종료
                if not siren_on:
                    break

                # 주파수 변경 및 빨강 LED ON
                sound.ChangeFrequency(freq)
                GPIO.output(GREEN, GPIO.HIGH)
                GPIO.output(BLUE, GPIO.LOW)
                time.sleep(0.02)
            
            # 사이렌 패턴 2: 주파수 하강 +  파란 LED
            # 1600Hz에서 400Hz까지 20Hz씩 감소
            for freq in range(1600, 400, -20):
            	# 사이렌 작동 중에도 버튼 체크
                current_button_state = GPIO.input(buttonPin)
                if last_button_state == GPIO.HIGH and current_button_state == GPIO.LOW:
                    siren_on = False
                    time.sleep(0.3)
                    sound.stop()
                    GPIO.output(GREEN, GPIO.LOW)
                    GPIO.output(BLUE, GPIO.LOW)
                    print("사이렌 OFF")
                    break
                last_button_state = current_button_state
                
				# 사이렌 OFF -> 루프 종료 
                if not siren_on:
                    break
                
                # 주파수 변경 및 파랑 LED ON    
                sound.ChangeFrequency(freq)
                GPIO.output(GREEN, GPIO.LOW)
                GPIO.output(BLUE, GPIO.HIGH)
                time.sleep(0.02)
        else:
            time.sleep(0.05)
            
except KeyboardInterrupt:
    sound.stop()
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.cleanup()
    print("\n프로그램이 종료되었습니다.")
