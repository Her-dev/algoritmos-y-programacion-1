def devuelve_diccionario(lista):
	"""Recibe una lista de tuplas y devuelve un diccionario cuyas claves son
	el primer elemento de estas y sus valores, los segundos"""
	diccionario = {}

	for primera, segunda in lista:

		diccionario[primera] = diccionario.get(primera, []) #Me busca el valor de la clave y lo devuelve. si no lo encuentra crea una lista.
		diccionario[primera].append(segunda) 

	return diccionario

print(devuelve_diccionario([ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),
          ('Buenos', 'días') ]))

def devuelve_diccionario_no_repite(lista):
	"""Recibe una lista de tuplas y devuelve un diccionario cuyas claves son
	el primer elemento de estas y sus valores, los segundos"""
	diccionario = {}

	for primera, segunda in lista:

		diccionario[primera] = diccionario.get(primera, set()) #Me busca el valor de la clave y lo devuelve. si no lo encuentra crea un SET
		diccionario[primera].add(segunda) 

	return devuelve_diccionario_no_repite		

