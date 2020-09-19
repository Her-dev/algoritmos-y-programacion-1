def mismas_palabras(palabras1,palabras2):
	d1 = {}
	for pal in palabras1:
		d1[pal] = d1.get(pal, 0) + 1

	d2 = {}
	for pal in palabras2:
		d2[pal] = d2.get(pal, 0) + 1

	for palabra, cantidad in d1.items():
		if palabra in d2 and cantidad == d2[palabra]:
			d2.pop(palabra)

		else:
			return False

	return len(d2) != 0

