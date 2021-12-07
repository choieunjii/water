import RPi.GPIO as GPIO # GPIO라이브러리 임포트
import time #time 라이브러리 임포트

GPIO.setmode(GPIO.BOARD) #핀 번호 할당 방법은 커넥터 핀번호로 설정
LED = 11 #사용할 핀 번호 할당
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW) #11번 핀을 출력 핀으로 설정, 초기 출력은 로우레벨
#예외처리(try), 반복(while)
try:
    while 1 : 
        GPIO.output(LED, GPIO.HIGH) #하이레벨 출력, 불켜짐
        time.sleep(0.5) #0.5초대기
        GPIO.output(LED, GPIO.LOW) #로우레벨 출력, 불꺼짐
        time.sleep(0.5)
except KeyboardInterrupt: #키보드예외검출
    pass #아무것도안함

GPIO.cleanup() #GPIO개방