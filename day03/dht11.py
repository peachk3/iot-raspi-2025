# pip install adafruit-circuitpython-dht
# sudo apt install libgpiod2

# import RPi.GPIO as GPIO
import time
import adafruit_dht
import board
import mysql.connector

#dhtPin = 2

# adafruit-dht라이브러리가 GPIO를 자동으로 관리함
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(dhtPin, GPIO.IN)

# DHT11 센서를 GPIO 2번 핀에 연결
dht = adafruit_dht.DHT11(board.D2)

# DB 연결
conn = mysql.connector.connect(
    host="localhost",
    user="test",          # 만든 사용자
    password="12345",       # 해당 사용자 비밀번호
    database="test_db"
)
cursor = conn.cursor()

try:
	while True:
		try:
			# 센서에서 온도와 습로 값으로 읽어옴
			temperature = dht.temperature
			humidity = dht.humidity
			
			if temperature is not None and humidity is not None:
				print(f"Temp: {temperature}°C")
				print(f"Humi: {humidity}%")
				print("-"*20)

                # DB에 데이터 삽입
				sql = "INSERT INTO tempHumData (temp, humid) VALUES (%s, %s)"
				val = (temperature, humidity)
				cursor.execute(sql, val)
				conn.commit()

			else:
				print("데이터 읽기 실패")

		except RuntimeError as error:
			print(f"센서 읽기 오류 :{error.args[0]}")
	
		time.sleep(2)

except KeyboardInterrupt:
	print("\n프로그램 종료")

finally:
	dht.exit()
