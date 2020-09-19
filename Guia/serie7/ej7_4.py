def prod_escalar(vector1,vector2):
	"""Dado dos vectores, devuelve su producto escalar"""
	vector = []

	if len(vector1) != len(vector2):
		print("Los vectores deben tener la misma cantidad de elementos")

	for i in range(len(vector1)):
		vector.append(vector1[i]*vector2[i])

	return sum(vector)

def son_ortogonales(vector1,vector2):
	"""Dado dos vectores, devuelve si son ortogonales"""

	if prod_escalar(vector1,vector2) == 0:
		return True
	return False

def norma(vector):
	"""Dado un vector, devuelve su norma"""
	suma = 0

	for e in vector:
		suma += e**2

	return suma**(1/2)

def son_paralelos(vector1,vector2):
	"""Dado dos vectores, devuelve si son paralelos"""
	return (norma(vector1) * norma(vector2) == prod_escalar(vector1,vector2))



