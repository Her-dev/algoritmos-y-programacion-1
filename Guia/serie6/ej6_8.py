def binario_decimal(binarios):
	"""Dada una cadena de 1 y 0, devuelve su decimal"""
	binario_reves = binarios[ : : -1]
	decimal = 0

	for i, e in enumerate(binario_reves):
		e_num = int(e)
		decimal += e_num * (2**i)

	return decimal

