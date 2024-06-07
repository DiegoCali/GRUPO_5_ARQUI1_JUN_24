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
	print("Que desea convertir? [b/n]")
	option = input()
	if option == "b":
		print("Ingrese el numero que desea convertir")
		bin_arr = []
		for i in range(0, 4):
			num = int(input())
			bin_arr.append(num)
		print(f"Su numero es: {convert_num(bin_arr)}")
	else:
		print("Ingrese el numero que desea convertir")
		num = int(input())
		print(f"Su numero en binario es: {convert_bin(num)}")
	print("Desea Salir? [y/n]")
	out = input()
	if out == "y":
		return False
	return True


running = True
while running:
	running = test_clients()
