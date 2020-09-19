def busqueda_binaria_o_agrega(numeros, elemento):
	"""Dada una lista ORDENADA y un elemento, lo busca mediante busqueda binaria. Si no lo
	encuentra, lo agrega en el lugar que corresponde"""
	izq = 0
	der = len(numeros) - 1

	while izq <= der:
		med = (izq + der) // 2

		if numeros[med] == elemento:
			return med

		if numeros[med] > elemento:
			der = med - 1

		if numeros[med] < elemento:
			izq = med + 1

	numeros.insert(izq, elemento)

	return izq #PREGUNTAR

print(busqueda_binaria_o_agrega([1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17],8))




