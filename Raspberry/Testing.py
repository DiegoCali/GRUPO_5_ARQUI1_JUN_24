import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(40, GPIO.OUT, initial=GPIO.HIGH)

    