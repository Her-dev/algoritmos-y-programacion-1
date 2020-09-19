def ordenado(tupla):
	"""Dada una tupla de elementos, devuelve True si está ordenada de mayor a menor"""

	for i in range(1,len(tupla) - 1):
		if tupla[i] < tupla[i - 1]:
			return False

	return True

