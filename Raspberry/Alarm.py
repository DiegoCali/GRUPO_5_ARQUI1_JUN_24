import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#el pin que se va a usar para encender el buzzer
pin = 40
GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

def turn_on_buzzer_with_timmer(time): #time in second	
	GPIO.output(pin, GPIO.LOW)
	sleep(time)
	GPIO.output(pin, GPIO.HIGH)
