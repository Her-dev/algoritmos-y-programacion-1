def cuenta_digitos(n):
	"""devuelve la cantidad de dígitos de un numero"""

	#caso base
	if n < 10:
		return 1

	n = n / 10
	digitos = cuenta_digitos(n) + 1

	return digitos

print(cuenta_digitos(126983.4))