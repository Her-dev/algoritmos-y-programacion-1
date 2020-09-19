def es_primo(n):
	"""Dado un número n, devuelve True si es primo y False si no lo es"""
	for i in range(2,n):
		if n % i == 0:
			return False
	return True

def desc_fact_primos(n):
	"""Dado un número n, imprime su desc en factores primos"""
	while n != 1:
		for i in range(2,n+1):
			if es_primo(i) and n % i == 0:
				print (i)
				n = n//i
				break


desc_fact_primos(252)