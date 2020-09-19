def cargar_datos(ruta):
	"""Dado un archivo, lo ingresa a un diccionario
	PRE= El archivo debe existir y debe tener formato clave,valor"""
	diccionario = {}
	with open(ruta) as archivo:
		for linea in archivo:
			clave, valor = linea.rstrip("\n").split(",")
			diccionario[clave] = diccionario.get(clave, [])
			diccionario[clave].append(valor)

	return diccionario

def guardar_datos(nuevo_nombre, diccionario):
	with open(nuevo_nombre, "w") as nuevo_archivo:
		for clave, valor in diccionario.items():
			for elemento in valor:
				nuevo_archivo.write(f"{clave},{elemento}\n")

guardar_datos("nombres2", cargar_datos("nombres"))


