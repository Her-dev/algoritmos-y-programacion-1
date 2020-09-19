def campania_electoral(nombres):
	"""recibe una tupla con nombres, y para cada 
	nombre imprima el mensaje Estimado <nombre>, vote por mí."""

	for e in nombres:
		print (f"Estimado {e} vote por mí")

def campania_origen(nombre,p,n):
	"""recibe una tupla con nombres, y para cada 
	nombre imprima el mensaje Estimado <nombre>, vote por mí. Lo hace desde la
	posición p, una cantidad n"""

	for i in range(p, p + n):
		if (i) == (len(nombre)):
			break

		print(f"Estimado {nombre[i]} vote por mi")

def campania_origen_genero(nom_gen,p,n):
	"""recibe una tupla con nombres, y para cada 
	nombre imprima el mensaje Estimado <nombre>, vote por mí. Lo hace desde la
	posición p, una cantidad n. Distingue genero"""

	for i in range(p, p + n):
		if (i) == (len(nom_gen)):
			break

		if nom_gen[i][1] == "Masculino":
			print(f"Estimado {nom_gen[i][0]} vote por mi")	
		else:
			print(f"Estimada {nom_gen[i][0]} vote por mi")

campania_origen_genero((("Herman","Masculino"),("Miru","Fem"),("Fer","Masculino")),1,2)