#Repaso diccionarios

def arregla_juntada(disponibilidades):
	"""Recibe un diccionario cuyas claves son los nombres de amigos y sus valores los días que NO pueden juntarse
	Devuelve un diccionario con todos los días y valores qué amigo puede ese día"""
	coincidencias = {}

	for i in range(1,32):
		coincidencias[i] = []
		for amigo in disponibilidades:
			if i not in disponibilidades[amigo]:
				coincidencias[i].append(amigo)

	return coincidencias

print(arregla_juntada({"her": [1,2,3,7,9,10,15,20],"lu":[31,30,20,5,6,7,8,9,14]}))