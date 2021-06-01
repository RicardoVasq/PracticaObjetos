listaCarros = []


#inicializamos la clase del objeto
class ClaseCarros:
	def __init__(self, _modelo, _color, _motor, _asiento, _marca, _puerta, _combustible, _placa, _estacionado ):
		self.modelo = _modelo
		self.color = _color
		self.motor = _motor
		self.asiento = _asiento
		self.marca = _marca
		self.puerta = _puerta
		self.combustible = int(_combustible)
		self.placa = _placa
		self.estacionado = _estacionado

	#Metodo de informacion sobre el objeto
	def info(self):
		print("\nAutomovil CIVIL\n")
		print("No. Placa: ", format(self.placa),"")
		print("Model del Auto: ", format(self.modelo),"")
		print("Color del Auto: ", format(self.color),"")
		print("Tipo de Motor del Auto: ", format(self.motor),"")
		print("Asientos disponibles: ", format(self.asiento),"")
		print("Marca del auto: ", format(self.marca),"")
		print("Cantidad de Puertas: ", format(self.puerta),"")
		print("Cantidad de combustible disponible: ", format(self.combustible),"lts")
		if self.estacionado == 0:
			print("El automovil no esta estacionado")
		else:
			print("El automovil no esta estacionado")

		pausa = input("\nPresione enter para continuar")

	#Metodo acelerar
	def acelerar(self):
		print("El modelo", self.modelo, "tiene un motor", self.motor, "que tiene una aceleración brutal")

	#Metodo parquear
	def parquear(self):
		print("Metodo parquear")
		if self.estacionado == 0:
			print("Desea estacionar el vehiculo Placas ", 	self.placa, ": ")
			estacionado = int(input("Digite 1 para estacionarlo:"))
			if estacionado==1:
				print("Automovil ha sido parqueado xD")
				pausa = input("\nPresione enter para continuar")
			else:
				print("El automovil no está estacionado")
				pausa = input("\nPresione enter para continuar")
		else:
			print("El automovil ya esta estacionado")
	pausa = input("\nPresione enter para continuar")

	#Metodo Gasolina
	def gasolina(self):
		print("Según el tipo de motor ", self.motor,  "la gasolina debe ser Disiel")

#Clase hijos ____
#Clase Hijos Policial
class Policial(ClaseCarros):
	def info(self):
		print("\nAutomovil Policial\n")
		print("No. Placa: ", format(self.placa),"")
		print("Model del Auto: ", format(self.modelo),"")
		print("Color del Auto: ", format(self.color),"")
		print("Tipo de Motor del Auto: ", format(self.motor),"")
		print("Asientos disponibles: ", format(self.asiento),"")
		print("Marca del auto: ", format(self.marca),"")
		print("Cantidad de Puertas: ", format(self.puerta),"")
		print("Cantidad de combustible disponible: ", format(self.combustible),"lts")
		if self.estacionado == 0:
			print("El automovil no esta estacionado")
		else:
			print("El automovil no esta estacionado")

		pausa = input("\nPresione enter para continuar")

class Bombero(ClaseCarros):
	def info(self):
		print("\nAutomovil Bombero\n")
		print("No. Placa: ", format(self.placa),"")
		print("Model del Auto: ", format(self.modelo),"")
		print("Color del Auto: ", format(self.color),"")
		print("Tipo de Motor del Auto: ", format(self.motor),"")
		print("Asientos disponibles: ", format(self.asiento),"")
		print("Marca del auto: ", format(self.marca),"")
		print("Cantidad de Puertas: ", format(self.puerta),"")
		print("Cantidad de combustible disponible: ", format(self.combustible),"lts")
		if self.estacionado == 0:
			print("El automovil no esta estacionado")
		else:
			print("El automovil no esta estacionado")

		pausa = input("\nPresione enter para continuar")
	
#Funciones
# Funcion para conocer si existen registros
def listaVacia(list):
    # verificando si hay contenido
    if len(list) == 0:
        # retorna True si no hay elementos
        return True
    # retorna Fals si hay elementos
    return False

#Funcion Registro		
def RegistroCarrro(tipo):
	print("\n")
	print("-------------------------")
	print("Ingreso de Automovil")
	placa = input("ingresa el numero de placa del Automovil: ")
	modelo = input("Ingrese el modelo del automovil: ")
	color = input("Ingrese el color del automovil: ")
	asiento = input("Ingrese la Cantidad de asientos del automovil: ")
	marca = input("Ingrese la marca del automovil: ")
	puertas = input("Ingrese la canitdad de puertas del automovil: ")
	combustible = int(input("Ingrese la canitdad de disponible de combustible: "))
	motor = input("Ingrese el modelo del motor del automovil: ")
	estacionado = 0
	pausa = input("\nPresione enter para continuar")
	if tipo==1:
		ObjCarro = ClaseCarros (modelo, color, motor, asiento, marca, puertas, combustible, placa, estacionado)
		listaCarros.append(ObjCarro)
	elif tipo == 2:
		ObjCarro = Policial (modelo, color, motor, asiento, marca, puertas, combustible, placa, estacionado)
		listaCarros.append(ObjCarro)
	elif tipo == 3:
		ObjCarro = Bombero (modelo, color, motor, asiento, marca, puertas, combustible, placa, estacionado)
		listaCarros.append(ObjCarro)

#Funcion Mostrar todos los carros registrados
def MostrarCarros():
	comprobacion = listaVacia(listaCarros)
	if comprobacion == False:
		for Carro in listaCarros:
			Carro.info()
	else:
		print("No se ha registrado ningun automovil")
		pausa = input("\nPresione enter para continuar")

#Funcion Mostrar info de un auto en especifico
def InfoCarro():
	comprobacion = listaVacia(listaCarros)
	if comprobacion == False:
		BusquedaCarro = input("Ingrese el numero de placa del Auto: ")
		for Carro in listaCarros:
			if BusquedaCarro == Carro.placa:
				Carro.info()
	else:
		print("No se ha registrado ningun automovil")
		pausa = input("\nPresione enter para continuar")

#Funcion de llenar el tanque
def LlenarTanque():
	comprobacion = listaVacia(listaCarros)
	if comprobacion == False:
		busquedaCarro = input("Ingresa el No. de Placa del auto: ")
		for Carro in listaCarros:
			if busquedaCarro == Carro.placa:
				if Carro.combustible < 30:
					print("El automovil, tiene ", Carro.combustible, "lt de combustible disponible")
					llenar = int(input("Para llenar el tanque del automovil ingrese 1 para dejarlo asi ingrese 2 "))
					if llenar == 1:
						print("Has llenado el tanque de combustible")
					Carro.combustible = 30
				else:
					print("El automovil tiene el tanque lleno")
					print(Carro.combustible)
	else:
		print("No se ha registrado ningun automovil")
		pausa = input("\nPresione enter para continuar")

#Funcion de parquear el auto xD 
def ParquearAutomovil():
	comprobacion = listaVacia(listaCarros)
	if comprobacion == False:
		BusquedaCarro = input("Ingrese el numero de placa del Auto: ")
		for Carro in listaCarros:
			if BusquedaCarro == Carro.placa:
				Carro.parquear()
	else:
		print("No se ha registrado ningun automovil")
		pausa = input("\nPresione enter para continuar")

