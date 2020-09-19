def es_sub_cadena(cadena1, cadena2):
	"""Devuelve True si la segunda cadena es subcadena de la primera"""
	return cadena2 in cadena1

def primera_alfa(cadena1, cadena2):
	"""Devuelve la que viene antes en orden alfabético"""
	return min(cadena1, cadena2)

print(primera_alfa("gnome","kde"))
