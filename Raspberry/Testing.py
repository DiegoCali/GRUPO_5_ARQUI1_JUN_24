from Lights import *

while True:
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
		print("Afectando todas las luces...")
		turn_light(number_light, False)
	print("Desea salir? [y/n]")
	out = input()
	if out == "y":
		print("Adios!")
		break
