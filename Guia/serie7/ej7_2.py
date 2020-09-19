def domino_encaja(tupla1,tupla2):
	"""indique si dos fichas de dominó encajan o no"""
	for e1 in tupla1:
		for e2 in tupla2:
			if e1 == e2:
				return True
	return False

def domino_encaja1(cadena1,cadena2):
	"""indique si dos fichas de dominó encajan o no"""
	lista1 = cadena1.split("-")
	lista2 = cadena2.split("-")

	for e1 in lista1:
		for e2 in lista2:
			if e1 == e2:
				return True
	return False

