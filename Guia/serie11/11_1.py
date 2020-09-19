def head(ruta, n):
	"""Dado un archivo, imprime por pantalla sus primeras N líneas"""
	with open(ruta) as archivo:
		cont = 0
		while cont < n:
			linea = archivo.readline().rstrip("\n")
			print (linea)
			cont += 1

head("peliculas", 5)

def head1(ruta, n):
	"""Dado un archivo, imprime por pantalla sus primeras N líneas"""
	with open(ruta) as archivo:
		cont = 0
		for linea in archivo: #Esta forma de iterar nos asegura de no pasarnos
			if cont >= n:
				break
			linea = linea.rstrip("\n")
			print (linea)
			cont += 1

head1("peliculas", 5)