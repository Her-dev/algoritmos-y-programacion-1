def devuelve_mayor(numeros):
	"""Dada una lista no ordenada de números, devuelve el mayor"""
	mayor = numeros[0]

	for i, e in enumerate(numeros):

		if e > mayor:
			mayor = e

	return mayor

def duevuelve_mayor_y_posicion(numeros):
	"""Dada una lista no ordenada de números, devuelve el mayor y su posicion"""	
	mayor = (numeros[0],0)

	for i, e in enumerate(numeros):

		if e > mayor[0]:
			mayor = (e, i)

	return mayor


