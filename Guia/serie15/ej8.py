

def mayor_lista(lista):
	return _mayor_lista(lista, lista[0])

def _mayor_lista(lista, maxim):
	if len(lista) == 0:
		return maxim

	if lista[0] > maxim:
		maxim = _mayor_lista(lista[1:], lista[0])

	else:
		maxim = _mayor_lista(lista[1:], maxim)

	return maxim

