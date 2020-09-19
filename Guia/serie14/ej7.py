from colas_pilas import Cola

def tail(ruta, n):
	"""Devuelve los últimos n lineas de un archivo"""
	cola = Cola()

	with open(ruta) as archivo:
		for i in range(n): 
			linea = archivo.readline().rstrip("\n")
			if not linea:
				break
			cola.encolar(linea)

		#Ya tengo mi "slicing window" llena

		for linea in archivo:
			cola.encolar(linea.rstrip("\n"))
			cola.desencolar()
			

		while not cola.esta_vacia():
			print(cola.desencolar())

tail("lutata", 5)

