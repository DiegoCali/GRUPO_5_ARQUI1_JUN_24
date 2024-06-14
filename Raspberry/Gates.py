import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def put_angle(angle):
    if angle < 0 or angle > 180:
        return False
    starts = 4
    ends = 12.5
    ratio = (ends - starts)/100
    percentage = angle * ratio
    return starts + percentage

def open_gates():
	GPIO.setup(32, GPIO.OUT)
	p = GPIO.PWM(32, 50)
	p.start(0)
	p.ChangeDutyCycle(3)
	sleep(0.25)
	p.stop()

def close_gates():
	GPIO.setup(32, GPIO.OUT)
	p = GPIO.PWM(32, 50)
	p.start(0)
	p.ChangeDutyCycle(12)
	sleep(0.25)
	p.stop()   
