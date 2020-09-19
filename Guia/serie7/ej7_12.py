def cuad(n):
	return n*n

def map(funcion,lista):
	"""recibe una función y una lista y devuelva la lista que resulta de aplicar 
	la función recibida a cada uno de los elementos de la lista recibida"""
	trasformada = []

	for e in lista:
		trasformada.append(funcion(e))

	return trasformada

def es_par(n):
	return n % 2 == 0

def filter(funcion,lista):
	"""recibe una función y una lista y devuelva una lista 
	con los elementos de la lista recibida para los cuales la función 
	recibida devuelve un valor verdadero."""
	filtrada = []

	for e in lista:
		if funcion(e):
			filtrada.append(e)

	return filtrada

print(filter(es_par,[1,2,3,4,5,6,7,8,9]))