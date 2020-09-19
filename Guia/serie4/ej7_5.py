NUMEROS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def es_primo(n):
	"""Dado un número n, devuelve True si es primo y False si no lo es"""
	for i in range(2,n):
		if n % i == 0:
			return False
	return True

def filtra_primos(numeros):
	"""Dada una lista de números enteros,
	 devuelve una lista con todos los que sean primos."""
	primos = []

	for n in NUMEROS:
		if es_primo(n):
			primos.append(n)

	return primos

print(filtra_primos(NUMEROS))