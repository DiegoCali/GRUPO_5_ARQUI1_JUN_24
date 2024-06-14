from rpi_lcd import LCD
from signal import signal, SIGTERM, SIGHUP, pause

lcd = LCD()

def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

try:
    lcd.text("Prueba...", 1)
    lcd.text("... 1, 2, 3", 2)

    pause()
except KeyboardInterrupt:
    pass 
finally:
    lcd.clear()