def separador(cadena,caracter):
	"""Dada una cadena y un caracter, la devuelve con el caracter entre cada elemento"""
	mensaje_final = ""
	for e in cadena:
		mensaje_final += e + caracter

	return mensaje_final[ : -1]

def espacio_caracter(cadena,caracter):
	"""Dada una cadena con espacios, inserta el caracter en ellos"""
	cadena_final = ""
	for e in cadena:
		if e == " ":
			cadena_final += caracter
			continue

		cadena_final += e

	return cadena_final

def digit_X(cadena,caracter):
	"""Dada una cadena, reemplaza todos sus dígitos por X"""
	cadena_final = ""
	for e in cadena:
		if e.isdigit():
			cadena_final += caracter

		else:
			cadena_final += e

	return cadena_final

def caracter_cada_3(cadena,caracter):
	"""Dada una cadena, inserta un caracter cada 3 elementos"""
	cadena_final = ""
	for i, e in enumerate(cadena):
		if i % 3 == 0 and i != 0:
			cadena_final += caracter

		cadena_final += e
	return cadena_final

print(caracter_cada_3("222555666333","."))













