#Lista dentro de otra 
def invertir_lista(lista):
	return lista[ : : -1]

def posiciones_de_lista(a, b):
	"""Dadas dos listas a y b, devuelve una lista con las posiciones donde
	se encuentra b dentro de a"""
	return invertir_lista(posiciones_de_lista_rec(a, b, 0))

def posiciones_de_lista_rec(a, b , index):
	if len(b) + index > len(a):
		return []

	for i in range(len(b)):
		if b[i] != a[index + i]:
			return posiciones_de_lista_rec(a, b, index + 1)

		return posiciones_de_lista_rec(a, b, index + 1) + [index]

print(posiciones_de_lista("Un tete a tete con Tete", "te"))