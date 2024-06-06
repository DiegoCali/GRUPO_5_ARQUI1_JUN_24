import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

lights = [3, 5, 7, 11, 13, 15, 16, 19, 21, 23] # Pins that will be used for lights

for light in lights:
	GPIO.setup(light, GPIO.OUT, initial=GPIO.LOW)

# First parameter is the index in the array for the light [number]
# Second parameter dictates if it is turned on or off [on]
def turn_light(number, on):
	try:
		number = int(number)
		if 0 <= number <= 9:
			if on:
				GPIO.output(lights[number], GPIO.HIGH)
			else:
				GPIO.output(lights[number], GPIO.LOW)
		else:
			print("No existe esa luz, intente con otra")
	except:
		print("No ingreso un numero valido")


