#Funcion para limpiar pantalla de consola
import os
def clear():
     if os.name == "nt":
          os.system("cls")
     else:
          os.system("clear")

import Carros

controlMenu = 1
clear()
while(controlMenu == 1):
		clear()
		print("|****************************|")
		print("|**|      Bienvenidos     |**|")
		print("|**|  Menu - Automoviles  |**|")
		print("|****************************|")
		print("")
		print("Seleccione una de las siguientes opciones:")
		print("1.- Registrar Auto Civil")
		print("2.- Registrar Auto Policial")
		print("3.- Registrar Auto Bombero")
		print("4.- Mostrar Automoviles")
		print("5.- Buscar Automovil")
		print("6.- Llenar tanque de Automovil")
		print("7.- Parquear Automovil")
		print("8.- Salir\n")
		
		opcion = int(input())
		if opcion == 1:
			Carros.RegistroCarrro(opcion)
		elif opcion ==2:
			Carros.RegistroCarrro(opcion)
		elif opcion == 3:
			Carros.RegistroCarrro(opcion)
		elif opcion ==4:
			Carros.MostrarCarros()
		elif opcion == 5:
			Carros.InfoCarro()
		elif opcion == 6:
			Carros.LlenarTanque()
		elif opcion == 7:
			Carros.ParquearAutomovil()
		elif opcion == 8:
			print("Ha salido del menú muchas gracias...")
			controlMenu = 2
		else:
			print("Ha salido del menú muchas gracias...")
			controlMenu = 2



