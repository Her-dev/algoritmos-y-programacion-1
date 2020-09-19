def primeros_dos_caracteres(cadena):
	"""Dada una cadena, devuelve sus dos primeros caracteres"""
	return cadena[:2]

def tres_ultimos_caracteres(cadena):
	"""Dada una cadena, devuelve sus ultimos tres caracteres"""
	return cadena[-3 : ]

def cadena_salteada(cadena):
	"""Dada una cadena, la duevuelve salteando un caracter"""
	return cadena[ : : 2]

def cadena_inversa(cadena):
	"""Dada una cadena, la devuelve al reves"""
	return cadena[ : : -1]

def cadena_espejada(cadena):
	"""Dada una cadena, devuelve el espejo"""
	return cadena[ : ] + cadena[ : : -1]

