from random import randrange

def encontrar_numero():
	"""genera un número secreto y le pide que ingrese al usuario números indicando si es mayor o menor, hasta que lo consigue"""
	print ("Vaya ingresando números hasta encontrar el número secreto")
	num_sec = randrange(0,100)
	
	intento = int(input("Ingrese un número: "))
	while intento != num_sec:
		if intento > num_sec:
			print ("El número ingresado es mayor que el secreto")
		else:
			print ("El número ingresado es menor que el secreto")

		intento = int(input("Ingrese un número: "))

	print ("CORRECTO, EL NUMERO DE CM DE MI CHOTA")

encontrar_numero()
