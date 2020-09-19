def replicar(lista, n):
	return _replicar(lista, n, [])

def _replicar(lista, n, lista_doble):
	if len(lista) == 0:
		return lista_doble

	for i in range(n):
		lista_doble.append(lista[0])

	lista_final = _replicar(lista[1:], n, lista_doble)

	return lista_final

def replicar_nice(lista, n):
	if len(lista) == 0:
		return []

	return lista[:1] * n + replicar_nice(lista[1:],n)



