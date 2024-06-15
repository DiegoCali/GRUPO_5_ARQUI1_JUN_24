import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pinLV = 8 #luz verde
pinLR = 10 #luz roja
pinM = 12 #motor
GPIO.setup(pinLV, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pinLR, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(pinM, GPIO.OUT, initial=GPIO.HIGH)

def start_motor():
    try:
        GPIO.output(pinM, GPIO.LOW)
        GPIO.output(pinLV, GPIO.HIGH)
        GPIO.output(pinLR, GPIO.LOW)
    except:
        print("No se pudo encender el motor")

def stop_motor():
    try:
        GPIO.output(pinM, GPIO.HIGH)
        GPIO.output(pinLV, GPIO.LOW)
        GPIO.output(pinLR, GPIO.HIGH)
    except:
        print("No se pudo apagar el motor")