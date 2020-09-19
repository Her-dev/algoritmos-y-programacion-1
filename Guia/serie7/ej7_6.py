def menos_mayor_k(lista,k):
	"""Dada una lista de números enteros y un entero k: Devuelve tres listas,
	una con los menores, otra con los mayores y otra con los iguales a k."""
	mayores = []
	menores = []
	iguales = []

	for e in lista:
		if e < k:
			menores.append(e)
		elif e == k:
			iguales.append(e)
		else:
			mayores.append(e)

	return menores, iguales, mayores

def multiplos_k(lista,k):
	"""Dada una lista de números enteros y un entero k: Devuelve una lista con 
	los que son multiplos de k"""
	multiplos = []

	for e in lista:
		if e % k == 0:
			multiplos.append(e)

	return multiplos

