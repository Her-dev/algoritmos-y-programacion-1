def es_par (n):
	"""Dado un número, devuelve True si es par y False si no lo es"""
	return n % 2 == 0
		
def es_primo(n):
	"""Dado un número n, devuelve True si es primo y False si no lo es"""
	for i in range(2,n):
		if n % i == 0:
			return False
	return True

