#Es potencia 

def es_potencia(n, b):
	"""Devuelve True si n es potencia de b"""
	if n < b:
		return False

	elif n == b:
		return True

	if es_potencia(n/b, b):
		return True
	else:
		return False

print(es_potencia(8,2))
print(es_potencia(64, 4))
print(es_potencia(70, 10))
