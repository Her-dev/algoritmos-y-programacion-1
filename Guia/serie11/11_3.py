def cuenta_archivos(ruta):
	"""Dado un archivo, devuelve cuantas lines, palabras y caracteres tiene"""
	lineas = 0
	palabras = 0
	caracteres = 0

	with open(ruta) as archivo:
		for linea in archivo:
			caracteres += len(linea)
			palabras += len(linea.rstrip("\n").split(" "))
			lineas += 1

	return lineas, palabras, caracteres

print(cuenta_archivos("peliculas"))