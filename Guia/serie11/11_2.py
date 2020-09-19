def cp(ruta, nuevo_nombre):
	"""Dado un archivo, copia todo su contenido a otro(cuyo nombre hay que indicar. Dejándolo igual"""
	cargar_archivo(leer_archivo(ruta),nuevo_nombre)

def leer_archivo(ruta):
	"""Lee un archivo de, como máximo, 1000 bytes"""
	with open(ruta) as archivo:
		return archivo.read(1000)

def cargar_archivo(archivo, nuevo_nombre):
	"""Dado un archivo, lo copia en otro (cuyo nombre se debe indicar)"""
	with open(nuevo_nombre, "w") as nuevo_archivo:
		nuevo_archivo.write(archivo)

def cp1(ruta, nuevo_nombre):
	"""Dado un archivo, copia todo su contenido a otro(cuyo nombre hay que indicar. Dejándolo igual"""
	with open(ruta) as archivo:
		with open(nuevo_nombre, "w") as nuevo_archivo:
			datos = archivo.read(10)
			while datos != "":
				nuevo_archivo.write(datos)
				datos = archivo.read(10)


