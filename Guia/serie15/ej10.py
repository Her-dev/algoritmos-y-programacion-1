def mas_A_E(cadena):
	e, a = _mas_A_E(cadena, 0, 0)
	
	if e > a:
		return "Hay mas E"
	else:
		return "Hay mas A"

def _mas_A_E(cadena, a, e):
	if len(cadena) == 0:
		return e, a

	if cadena[0] == "A":
		e, a = _mas_A_E(cadena[1:], a + 1, e)

	elif cadena[0] == "E":
		e, a = _mas_A_E(cadena[1:], a, e + 1)

	else:
		e, a = _mas_A_E(cadena[1:], a, e)

	return e, a

print(mas_A_E("Cadena con E y A, pero con mas E"))

