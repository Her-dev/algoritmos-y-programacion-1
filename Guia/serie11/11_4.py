def grep(ruta, cadena):
	"""Dada una cadena y un archivo, imprime las lineas que la contengan"""
	with open(ruta) as archivo:
		for linea in archivo:
			if cadena in linea:
				print (linea.rstrip("\n"))

print(grep("peliculas", "Leonardo"))


