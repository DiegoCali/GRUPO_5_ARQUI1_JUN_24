import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#el pin que se va a usar para encender el buzzer
pin = 33
GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

def turn_on_buzzer_with_timmer(time): #time in seconds
    try:
        if time.isnumeric():
            time = float(time)
        else:
            print ("El tiempo debe de ser un numero")
            return

        GPIO.output(pin, GPIO.HIGH)
        sleep(time)
        GPIO.output(pin, GPIO.LOW)
    except:
        print("No se pudo cambiar el estado del buzzer")