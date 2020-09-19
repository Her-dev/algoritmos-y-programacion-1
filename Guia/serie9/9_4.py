def palabra_mas_larga(texto):
	"""Dado un texto y para cada caracter presente en el texto 
	devuelve la cadena más larga en la que se encuentra ese caracter"""
	diccionario = {}
	palabras = texto.split(" ")
	print(palabras)

	for e in texto:
		if e == " ":
			continue

		if e in diccionario:
			continue
		
		apariciones = set()
		
		for pal in palabras:
			if e in pal:
				apariciones.add(pal)

		diccionario[e] = max(apariciones, key=len)

	return diccionario

print(palabra_mas_larga("Dado un texto y para cada caracter presente en el texto devuelve la cadena más larga en la que se encuentra ese caracte"))


