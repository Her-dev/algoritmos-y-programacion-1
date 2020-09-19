def nombre(nombres):
	"""Dada una lista de tuplas (nombre, apellido, inicial de segundo nombre)
	devuelve una lista de cadenas donde cada una contiene primero el 
	nombre, luego la inicial con un punto, y luego el apellido."""
	lista_final = []

	for i in range(len(nombres)):
		lista_final.append(f" {nombres[i][0]} {nombres[i][2]}. {nombres[i][1]}")

	return lista_final

print(nombre([("Herman","Obst","S"),("Eduardo","Obst","M")]))

