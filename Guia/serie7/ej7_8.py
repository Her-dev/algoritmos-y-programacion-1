def invierte_lista1(lista):
	"""Dada una lista, la de vuelta (una copia) y la devuelve"""
	return lista[ : : -1]

print(invierte_lista1(['Di', 'buen', 'día', 'a', 'papa']))

def invierte_lista(lista):
	"""Dada una lista, la invierte"""
	for i in range(-1, -len(lista), -1):
		lista.insert(i, lista[0]) #Va insertando el (cambiante) elemento 0 en la posición -1, -2, -3 ..
		lista.remove(lista[0])

	lista.insert(0 ,lista[-1])
	lista.pop()

	return lista

print(invierte_lista(['Di', 'buen', 'día', 'a', 'papa']))