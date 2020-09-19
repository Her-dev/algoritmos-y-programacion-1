def cuenta_palabras(cadena):
	"""Dada una cadena, devuelve un diccionario con la cantidad de 
	apariciones de cada palabra"""
	diccionario = {}

	for palabra in cadena.split(" "):
		diccionario[palabra] = diccionario.get(palabra, 0)
		diccionario[palabra] += 1

	return diccionario

def cuenta_caracteres(cadena):
	"""Dada una cadena, devuelve un diccionario con la cantidad de 
	apariciones de cada caracter"""
	diccionario = {}

	for e in cadena:
		diccionario[e] = diccionario.get(e, 0)
		diccionario[e] += 1

	return diccionario

import random 

def cuenta_suma_2_dados(tiradas):
	"""Dada una cantidad de tiradas de dos dados, cuenta cuantas veces
	salió la suma de ambos y la pone en un diccionario"""
	diccionario = {}

	for tir in range(tiradas):
		suma = random.randrange(1,7) + random.randrange(1,7)

		diccionario[suma] = diccionario.get(suma, 0)
		diccionario[suma] += 1

	return diccionario




