def devuelve_primera_letra(cadena):
	"""Dada una cadena de palabras, devuelve la primera letra de cada una"""
	cadena_final = ""
	x = cadena.split()

	for i in range(len(x)):
		cadena_final += x[i][0]

	return cadena_final

def pone_mayuscula(cadena):
	"""Dada una cadena, la devuelve con la primera letra de sus palabras en mayúscula"""
	lista_palabras = cadena.split()
	cadena_final = ""
	#lista_palabras_listas = []

	#for i in range(len(lista_palabras)):
		#lista_palabras_listas.append(list(lista_palabras[i])) #ME creo una lista de listas
		#lista_palabras_listas[i][0] = lista_palabras_listas[i][0].upper()

	for i in range(len(lista_palabras)):
		mayus = lista_palabras[i][0].upper()
		cadena_final += mayus + lista_palabras[i][1 : ] + " "

	return cadena_final[ : -1]


def solo_A(cadena):
	"""dada una cadena de caracteres, devuelve Las palabras que comiencen con la letra ‘A’"""
	lista_palabras = cadena.split()
	lista_final = []

	for i in range(len(lista_palabras)):
		if lista_palabras[i][0] in "Aa":
			lista_final.append(lista_palabras[i])

	return " ".join(lista_final)

print(solo_A("Antes de ayer habia una ave muy alta"))


