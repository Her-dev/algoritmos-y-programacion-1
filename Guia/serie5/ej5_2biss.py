def es_primo(n):
	"""Dado un número n, devuelve True si es primo y False si no lo es"""
	for i in range(2,n):
		if n % i == 0:
			return False
	return True

def desc_fact_primos(n):
	"""Dado un número n, imprime su desc en factores primos"""
	primo = 2
	while n != 1:
		
		if not es_primo(primo):
			primo += 1
			continue #Lo manda a la siguiente iteración del while


		while n % primo == 0:
				print (primo)
				n = n//primo
		primo += 1

desc_fact_primos(252)