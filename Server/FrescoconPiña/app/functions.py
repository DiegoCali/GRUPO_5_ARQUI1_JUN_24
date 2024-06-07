import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

lights = [3, 5, 7, 11, 13, 15, 16, 19, 21, 23]

for light in lights:
    GPIO.setup(light, GPIO.OUT, initial=GPIO.LOW)


def lights_actions(num, state):
    try:
        if state:
            GPIO.output(lights[int(num)], GPIO.HIGH)
        else:
            GPIO.output(lights[int(num)], GPIO.LOW)
    except IndexError:
        print(f"Light {num} does not exist")


def all_lights_action(state):
    for light in lights:
        if state:
            GPIO.output(light, GPIO.HIGH)
        else:
            GPIO.output(light, GPIO.LOW)