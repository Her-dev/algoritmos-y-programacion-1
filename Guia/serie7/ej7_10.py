def suma_matrices(matriz1, matriz2):
	"""Recibe 2 matrices en forma de lista de listas y devuelve su suma"""
	matriz_suma = []

	for f in range(len(matriz1)):
		matriz_suma.append([])

		for c in range(len(matriz1[0])):
			matriz_suma[f].append(matriz1[f][c] + matriz2[f][c])

	return matriz_suma

def producto_matrices(matriz1, matriz2):
	"""Recibe 2 matrices en forma de lista de listas y devuelve su suma"""
	matriz_producto = []
	suma = 0

	for f1 in range(len(matriz1)): #recorro las filas de la primera matriz
		matriz_producto.append([]) #Agrego las filas de la matriz producto

		for c2 in range(len(matriz2[0])): #Recorro las columnas de la segunda matriz
			for c1 in range(len(matriz1[0])): #Recorro las columnas de la primera matriz, que son la misma cantidad que las filas de la segunda
				suma += matriz1[f1][c1] * matriz2[c1][c2]

			matriz_producto[f1].append(suma) #Va agregando los elementos a la matriz producto
			suma = 0

	return matriz_producto
