import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin_arr = [29, 31, 33, 35] # 1, 2, 4, 8

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
	for j in range(0,4):
		if binary[j] == 1:
			GPIO.output(pin_arr[j], GPIO.HIGH)

def clean_display():
	for pin in pin_arr:
		GPIO.output(pin, GPIO.LOW)
