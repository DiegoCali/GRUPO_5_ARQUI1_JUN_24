import RPi.GPIO as GPIO
import threading
from Raspberry.Gates import open_gates, close_gates
from Raspberry.Lights import turn_light
from Raspberry.ConvBelt import start_motor, stop_motor
from Raspberry.Alarm import turn_on_buzzer_with_timmer
from Raspberry.Clients import show_binary
from rpi_lcd import LCD
from signal import signal, SIGTERM, SIGHUP
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.IN) #primer sensor (este irá en la entrada)
GPIO.setup(22, GPIO.IN) #segundo sensor (este irá adentro)
GPIO.setup(31, GPIO.IN) #sensor perimetral
#GPIO.setup(33, GPIO.IN) #sensor de alarma

def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

class butler:
    def __init__(self):
        self.lcd = LCD()
        self.clients = 0
        self.gate_state = 0
        self.all_lights = 0

    def light_action(self, lights, state):
        if lights == -1:
            turn_light(10, state)
            self.all_lights = state
        else:
            turn_light(lights, state)

    def gate_action(self, state):
        if state == 1:
            close_gates()
            self.gate_state = 0
        else:
            open_gates()
            self.gate_state = 1

    def belt_activate(self):
        start_motor()
        sleep(5)
        stop_motor()

    def messages(self):
        while True:
            self.lcd.text("<G5_ARQUI1>", 1)
            self.lcd.text("<VACAS_JUN_24>", 2)
            sleep(2)
            self.lcd.text(f"Clientes: {self.clients}", 1)
            self.lcd.text("Luces: Off", 2)
            sleep(2)
            self.lcd.text("Puertas: Cerradas", 1)
            self.lcd.text("Banda: Off", 2)
            sleep(2)
            self.lcd.text("Sensores: Off", 1)
            self.lcd.text("Alarma: Off", 2)
            sleep(2)

    def clients_counter(self):
        a_state = 0
        a_prev = 0
        b_state = 0
        b_prev = 0        

        while True:
            a_state = not GPIO.input(18)
            b_state = not GPIO.input(22)

            if a_state == 1 and a_prev == 0:
                if b_prev == 1:
                    self.clients = self.clients - 1   
                    b_prev = 0         
                else:
                    a_prev = 1
                print("Contador: ", self.clients)
            
            if b_state == 1 and b_prev == 0:
                if a_prev == 1:
                    self.clients = self.clients + 1
                    a_prev = 0 
                else:
                    b_prev = 1
                print("Contador: ", self.clients)
            show_binary(self.clients)
            sleep(1)
                
    def perimeter_alarm(self):
        while True:
            if GPIO.input(31):
                turn_on_buzzer_with_timmer(10)   

    def start_supervisor(self):
        th1 = threading.Thread(target=self.messages, args=())
        th2 = threading.Thread(target=self.clients_counter, args=())
        th3 = threading.Thread(target=self.perimeter_alarm, args=())
        th1.start()
        th2.start()
        th3.start()
        
    
