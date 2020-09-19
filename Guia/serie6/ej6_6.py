def solo_consonantes(cadena):
	"""Dada una cadena, devuelve una con solo sus consonantes"""
	tupla_cadena = tuple(cadena)
	lista_final = []

	for e in tupla_cadena:
		if e not in "AaEeIiOoUu":
			lista_final.append(e)

	return "".join(lista_final)

def solo_vocales(cadena):
	"""Dada una cadena, devuelve una con solo sus vocales"""
	tupla_cadena = tuple(cadena)
	lista_final = []

	for e in tupla_cadena:
		if e in "AaEeIiOoUu ":
			lista_final.append(e)

	return "".join(lista_final)

def cambia_vocales(cadena):
	"""Dada una cadena de caracteres reemplaza cada vocal por su siguiente vocal"""
	lista_cadena = list(cadena)
	vocales = ("a","e","i","o","u","a")

	for i, e in enumerate(lista_cadena):
		for j, v in enumerate(vocales): 

			if e == v:
				lista_cadena[i] = vocales[j + 1]
				break

	return "".join(lista_cadena)

def es_palindromo(cadena):
	"""Dada una cadena, indica si es un palíndromo"""
	cadena_junta = "".join(cadena.split(" "))
	if cadena_junta == cadena_junta[ : : -1]:
		return True
	return False









