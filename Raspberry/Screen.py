import RPi.GPIO as GPIO
from lib.LCD import LCD as lcd

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# pines a utilizar para LCD 3 y 5 para I2C

lcd = lcd(2, 0x27)
# el 2 indica que se va a usar para una version de raspberry 2 en adelante
def show_text(action):
    lcd.clear()
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