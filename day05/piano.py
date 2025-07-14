import RPi.GPIO as GPIO
import time
import threading
import sys
import tty
import termios

# GPIO 핀 설정 (피에조 부저가 연결된 핀)
PIEZO_PIN = 18

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIEZO_PIN, GPIO.OUT)

# PWM 객체 생성
pwm = GPIO.PWM(PIEZO_PIN, 440)  # 초기 주파수 440Hz (A4)

# 음표와 주파수 매핑 (C4부터 시작)
notes = {
    # 낮은 옥타브 (C4 ~ B4)
    'z': 261.63,  # C4 (도)
    'x': 293.66,  # D4 (레)
    'c': 329.63,  # E4 (미)
    'v': 349.23,  # F4 (파)
    'b': 392.00,  # G4 (솔)
    'n': 440.00,  # A4 (라)
    'm': 493.88,  # B4 (시)
    
    # 중간 옥타브 (C5 ~ B5)
    'a': 523.25,  # C5 (도)
    's': 587.33,  # D5 (레)
    'd': 659.25,  # E5 (미)
    'f': 698.46,  # F5 (파)
    'g': 783.99,  # G5 (솔)
    'h': 880.00,  # A5 (라)
    'j': 987.77,  # B5 (시)
    
    # 높은 옥타브 (C6 ~ B6)
    'q': 1046.50,  # C6 (도)
    'w': 1174.66,  # D6 (레)
    'e': 1318.51,  # E6 (미)
    'r': 1396.91,  # F6 (파)
    't': 1567.98,  # G6 (솔)
    'y': 1760.00,  # A6 (라)
    'u': 1975.53,  # B6 (시)
    
    # 반음 (검은 건반)
    '2': 277.18,  # C#4
    '3': 311.13,  # D#4
    '5': 369.99,  # F#4
    '6': 415.30,  # G#4
    '7': 466.16,  # A#4
    '9': 554.37,  # C#5
    '0': 622.25,  # D#5
    '=': 739.99,  # F#5
    '[': 830.61,  # G#5
    ']': 932.33,  # A#5
}

# 키보드 입력을 위한 함수
def get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char

# 음표 재생 함수
def play_note(frequency, duration=0.5):
    if frequency > 0:
        pwm.ChangeFrequency(frequency)
        pwm.start(50)  # 50% duty cycle
        time.sleep(duration)
        pwm.stop()
    else:
        time.sleep(duration)

# 지속적인 음표 재생 (키를 누르고 있는 동안)
class ContinuousNote:
    def __init__(self):
        self.playing = False
        self.current_thread = None
    
    def start_note(self, frequency):
        self.stop_note()
        self.playing = True
        pwm.ChangeFrequency(frequency)
        pwm.start(50)
    
    def stop_note(self):
        self.playing = False
        pwm.stop()

# 메인 함수
def main():
    print("🎹 라즈베리파이 피에조 피아노 🎹")
    print("=" * 50)
    print("\n키보드 레이아웃:")
    print("높은 옥타브: Q W E R T Y U")
    print("중간 옥타브: A S D F G H J")
    print("낮은 옥타브: Z X C V B N M")
    print("\n반음 (검은 건반):")
    print("2 3   5 6 7   9 0   =   [ ]")
    print("\n사용법:")
    print("- 키를 눌러서 음표 연주")
    print("- 스페이스바: 잠시 정지")
    print("- ESC 또는 Ctrl+C: 종료")
    print("=" * 50)
    
    continuous_note = ContinuousNote()
    
    try:
        while True:
            char = get_char()
            
            # ESC 키로 종료
            if ord(char) == 27:  # ESC
                break
                
            # 엔터키로 종료
            if ord(char) == 13:  # Enter
                break
                
            # 스페이스바로 정지
            if char == ' ':
                continuous_note.stop_note()
                time.sleep(0.2)
                continue
            
            # 음표 재생
            if char in notes:
                frequency = notes[char]
                print(f"♪ {char.upper()} -> {frequency:.2f}Hz")
                
                # 짧은 음표 재생
                play_note(frequency, 0.3)
            
            elif char.lower() in notes:
                frequency = notes[char.lower()]
                print(f"♪ {char.upper()} -> {frequency:.2f}Hz")
                play_note(frequency, 0.3)
            
            else:
                print(f"'{char}' 는 할당되지 않은 키입니다.")
    
    except KeyboardInterrupt:
        print("\n\n피아노 연주를 종료합니다.")
    
    finally:
        continuous_note.stop_note()
        GPIO.cleanup()
        print("GPIO 정리 완료!")

if __name__ == "__main__":
    main()
