letras = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y" "z")

def rot13(ruta, nuevo_nombre):
	with open(ruta) as archivo:
		with open(nuevo_nombre, "w") as nuevo_archivo:
			for linea in archivo:
				nuevo_archivo.write(transformacion(linea.lower()))

def transformacion(linea):
	lista_linea = list(linea)

	for i, e in enumerate(lista_linea):
		if e in letras:
			lista_linea[i] = letras[(letras.index(e) + 13) % 26]

	return "".join(lista_linea)

rot13("flash", "COMETE EL FLA")


