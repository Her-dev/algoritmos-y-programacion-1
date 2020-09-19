def empaquetar (numeros):
	"""Recibe una lista de números y empaqueta los repetidos"""
	elemento_repetido = 0
	empaquetado = []

	for i, e in enumerate(numeros):

		if i == 0:
			elemento_repetido += 1

		elif numeros[i] == numeros[i - 1]:
			elemento_repetido += 1
				

		elif numeros[i] != numeros[i - 1]:
			empaquetado.append((numeros[i - 1], elemento_repetido))

			elemento_repetido = 1

	empaquetado.append((numeros[i], elemento_repetido))

	return empaquetado

print (empaquetar([1,2,3,4,4,4,4,5,5,5,5,6]))

