def inserte_caracter_max(cadena,separador,maxim):
	"""Dada una cadena, un separador y una cantidad máxima, inserta el caracter 
	entre las letras. No insertará más del máximo"""
	mensaje_final = ""
	contador = 0

	while contador < maxim:
		mensaje_final += cadena[contador] + separador
		contador += 1

		if contador == len(cadena):
			return mensaje_final[ : -1]

	return mensaje_final + cadena[contador : ]

def espacio_caracter_max(cadena,separador,maxim):
	"""Dada una cadena, un separador y una cantidad máxima, inserta el caracter 
	entre los espacios. No insertará más del máximo"""
	cadena_final = ""
	contador = 0

	for e in cadena:

		if e == " " and contador < maxim:
			cadena_final += separador
			contador += 1
			continue

		cadena_final += e

	return cadena_final

def digito_caracter_max(cadena,caracter,maxim):
	"""Dada una cadena, reemplaza todos sus dígitos por X, 
	hasta el maximo permitido"""
	cadena_final = ""
	contador = 0

	for e in cadena:
		if e.isdigit() and contador < maxim:
			cadena_final += caracter
			contador += 1

		else:
			cadena_final += e

	return cadena_final

def caracter_cada_3_max(cadena,caracter,maxim):
	"""Dada una cadena, inserta un caracter cada 3 elementos, hasta llegar al maximo"""
	cadena_final = ""
	contador = 0
	for i, e in enumerate(cadena):
		if i % 3 == 0 and contador < maxim and i != 0:
			cadena_final += caracter
			contador += 1

		cadena_final += e
	return cadena_final

print(caracter_cada_3_max("222555666888555",".",2))









