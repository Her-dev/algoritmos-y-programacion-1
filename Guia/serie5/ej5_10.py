from ej5_2 import es_primo

def primos(n):
	"""Imprime todos los numeros primos hasta uno que ingresa como parametro"""
	for i in range(n):
		if es_primo(i):
			print(f"El número {i} es primo")
