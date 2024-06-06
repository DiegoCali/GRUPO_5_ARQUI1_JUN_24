from Lights import *

def test_lights():
	print("Ingrese el numero de luz que desea:")
	number_light = int(input())
	print("La luz que escogio fue: ", number_light)
	if number_light < 10:
		print("Desea apagarla o encenderla? [a/e]")
		turn = input()
		if turn == "a":
			print("Apagando...")
			turn_light(number_light, False)
		else:
			print("Encendiendo...")
			turn_light(number_light, True)
	else:
		print("Desea apagar o encender todas las luces? [a/e]")
		turn = input()
		if turn == "a":
			print("Apagando...")
			turn_light(number_light, False)
		else:
			print("Encendiendo...")
			turn_light(number_light, True)
	print("Desea salir? [y/n]")
	out = input()
	if out == "y":
		print("Adios!")
		return False
	return True

running = True
while running:
	running = test_lights()
