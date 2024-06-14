import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin_arr = [35, 36, 37, 38]  # 1, 2, 4, 8

for pin in pin_arr:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

binary_nums = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1]
]


# Parameter num is a integer
def convert_bin(num):
    binary = []
    if num < 10:
        binary = binary_nums[num]
    else:
        binary = binary_nums[9]
    return binary


# Parameter binary is an array of 1s and 0s
def convert_num(binary):
    num = -1
    i = 0
    for bin in binary_nums:
        if bin == binary:
            num = i
        i = i + 1
    return num


def show_binary(num):
    clean_display()
    binary = convert_bin(num)
    i = 0
    for j in range(0, 4):
        if binary[j] == 1:
            GPIO.output(pin_arr[j], GPIO.HIGH)


def clean_display():
    for pin in pin_arr:
        GPIO.output(pin, GPIO.LOW)

#esto es para la logica de ver si entra o sale un cliente
A = False # primer sensor, este debe de ir en la entrada
B = False # segundo sensor, este debe de ir adentro

def enter_exit_client(entrada):
    global A, B
    if entrada == "B":
        B = not B
        if A:
            A = False
            B = False
            return 1 #esto indica que entro un cliente
    elif entrada == "A":
        A = not A
        if B:
            A = False
            B = False
            return -1 #esto indica que salio un cliente
    return 0 #esto indica que no paso nada