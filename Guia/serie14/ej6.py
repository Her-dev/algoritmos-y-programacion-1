from colas_pilas import Pila

def bien_balanceados(expresion):
	"""Dada una expresion matemática, devuelve True si sus parentesis están
	bien balanceados"""
	pila = Pila()

	for e in expresion:
		if e not in ("(","[","{",")","]","}"):
			continue

		if e in ("(","[","{"):
			pila.apilar(e)

		try:

			if e == ")" and not pila.desapilar() == "(":
				return False

			elif e == "]" and not pila.desapilar() == "[":
				return False

			elif e == "}" and not pila.desapilar() == "{":
				return False

		except IndexError:
			return False

	if pila.esta_vacia():
		return True

	return False

print(bien_balanceados('1+)2(+3'))