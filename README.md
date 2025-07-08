# iot-raspi-2025

## 1일차
### 기본 설정
공유기 연결 후 인터넷 창 - 192.168.0.1 접속
- 기존 PC의 ip주소 입력 및 기본 설정

### 설치
- raspberry Pi Imager (https://www.raspberrypi.com/software/) 
    > Download for Windows
- RealVNC (https://www.realvnc.com/en/connect/download/viewer/?lai_vid=8rnEvy4v2CBa3&lai_sr=0-4&lai_sl=l)
- SD Card Formatter (https://www.sdcard.org/downloads/formatter/sd-memory-card-formatter-for-windows-download/)
    > Accept
    - sd 카드 포맷용으로 사용 (라즈베리파이 오류 시 시행)

#### raspberry Pi Imager 
1. 라즈베리파이디바이스 선택(버전 확인)
2. 운영체제 선택(Raspberry pi os (64-bit))
3. 저장소 선택 (pc에 연결한 sd 카드 선택)

#### 공유기 - raspberrypi 연결
1. 유선 LAN 연결 (raspberrypi - 공유기)
2. 모니터 연결 (raspberrypi - 모니터)
3. 키보드, 마우스 연결 (raspberrypi - 키보드/마우스)
4. raspberrypi 배경화면 > 우측 상단 인터넷 아이콘 클릭 > 연결할 공유기 찾기 > 아이디/비번 넣고 연결
5. restart (후에도 연결되어 있는지 확인)
6. 네트워크 매니저 창에 raspberrypi 연결되어 있는지 확인

#### PUTTY
1. Host Name : raspberrt.local(네트워크 매니저에서 확인한 raspberrypi ip 입력)
2. Port : 22
3. Saved Sessions : raspi
3. save -> load -> open
4. 터미널에서 명령어 실행
```shell
    sudo apt update
    sudo apt upgrade -y
    sudo reboot now
```
5. 창 상단 우클릭 > Changed Sessions > restart Sessions
6. vnc 활성화
```shell
    vncserver-virtual
    sudo raspi-config 
```
7. 화면 출력 시 3. Interface Options > I3 VNC > Yes > Finish

#### RealVNC
1. 실행 후 raspberrypi 입력
2. 이름/비번 : raspi/raspi

##### 한글 설정
1. vnc뷰어에서 raspberrypi 아이콘 클릭 > raspberrypi configuration > localiziation 으로 이동
2. location - ko(korean), KR, UTF-8로 변경
3. Timezone - Asia, Seoul로 변경
4. 터미널에서 명령어 실행
```shell
    sudo apt install fonts-nanum fonts-nanum-extra   #나눔 폰트 설치
    sudo apt install fonts-unfonts-core   #폰트 등록
    sudo reboot now
    sudo raspi-config # vnc 활성화
```

#### 라즈베리파이 Shared 파일 설치
1. 터미널에서 명령어 실행
```shell
    sudo apt install samba samba-common-bin
    sudo mkdir -p /home/pi/share
    sudo nano /etc/samba/smb.conf
```
2. 편집기에서 가장 마지막 줄에 추가
```nano
    [share]
    path = /home/pi/share
    writeable = yes
    create mask = 0777
    directory mask = 0777
    public = yes
    guest ok = yes
```
3. samba restart
```shell
    sudo systemctl restart smbd
```
4. 권한 오류 발생
```shell
    sudo chmod -R 777 /home/pi/share
```
-> 모든 사용자에게 권한 부여

5. 윈도우파일탐색기 > 라즈베리파이의 ip주소 입력


#### 라즈베리 설정
- 편집기 열어서 수정
```shell
    sudo nano /etc/nanorc
```
- 주석 해제 
	- set autoindent
	- set linenumbers
	- set tabsize 4


#### 명령어
|명령어|설명|
|------|----|
|ls -al [파일명] | 자세히 보기|
|ls| 파일 목록 보기|
|ls *.[파일확장자] | 해당 파일 확장자 모두 보기|
|rm -fr [파일명/*].[확장자명] | 파일 삭제|
|cp ./[파일명1] ./[파일명2] | 파일명을 1에서 2로 복사|
|mv [파일명1] [파일명2] | 파일명 1을 2로 변경|
|pwd | 현재 위치 |
|rmdir [폴더명] | 폴더 삭제 |
. : 현재 디렉터리
.. : 상위 디렉터리