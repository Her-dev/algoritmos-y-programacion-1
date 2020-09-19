def agenda_simplificada(cadena,agenda):
	"""busqua dentro de la lista, todas las entradas que 
	contengan en el nombre completo la cadena recibida"""
	agenda_simp = []

	for i in range(len(agenda)):
		if cadena in agenda[i][0]:
			agenda_simp.append(agenda[i])

	return agenda_simp


