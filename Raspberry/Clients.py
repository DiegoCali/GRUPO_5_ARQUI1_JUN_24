import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin_arr = [29, 31, 33, 35] # 1, 2, 4, 8

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