def cuenta_coincidencias(lista,elemento):
	"""recibe una lista desordenada y un elemento, Busqua todos los 
	elementos coincidan con el pasado por parámetro y devuelva la 
	cantidad de coincidencias encontradas."""
	coincidencias = 0

	for e in lista:
		if e == elemento:
			coincidencias += 1

	return coincidencias

def busca_primera_coincidencia(lista,elemento):
	"""recibe una lista desordenada y un elemento y
	busca la primera coincidencia del elemento en la lista y devuelva su posición."""
	for i, e in enumerate(lista):
		if e == elemento:
			return i

def devuelve_coincidencias(lista,elemento):
	"""busqua todos los elementos que coincidan con el pasado por 
	parámetro y devuelva una lista con las posiciones."""
	l_coincidencias = []

	for i, e in enumerate(lista):
		if e == elemento:
			l_coincidencias.append(i)

	return l_coincidencias

print(devuelve_coincidencias([1,2,3,4,2,4,3,2,6,7,8,2],2))

