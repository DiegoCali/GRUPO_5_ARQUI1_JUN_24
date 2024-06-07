from Lights import *
from Clients import *

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

def test_clients():
	print("Ingrese el numero que desea mostrar")
	num = int(input())
	show_binary(num)
	print(f"Mostrando numero {num}")
	print("Desea Salir? [y/n]")
	out = input()
	if out == "y":
		return False
	return True


running = True
while running:
	running = test_clients()
