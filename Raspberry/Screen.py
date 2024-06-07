import RPi.GPIO as GPIO
from librerias.LCD import LCD as lcd

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def show_text(action):
    texts = action.split(" ")
    rowIsFull = False
    row1=""
    row2=""
    for text in texts:
        if (len(row1) + len(text) <= 15 and not rowIsFull):
            row1 += text + " "
        else:
            rowIsFull = True
            row2 += text + " "
    lcd.text(row1, 1)
    lcd.text(row2, 2)