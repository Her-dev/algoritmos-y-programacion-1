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

def suma_promedia(numeros):
	"""Dada una lista de números enteros, devuelve su suma y promedio"""
	suma = 0

	for e in numeros:
		suma += e

	return (f"la suma de los elementos es {suma} y su promedio es {suma/(len(numeros))}")

def devuelve_factorial(lista):
	"""Dada una lista de enteros, devuelve otra con sus factoriales"""
	factoriales = []

	for e in lista:
		factoriales.append(factorial(e))

	return factoriales

def factorial(n):
	factorial = 1

	for i in range(1, n + 1):
		factorial *= i

	return factorial

print(devuelve_factorial((1,2,3,4,5)))





