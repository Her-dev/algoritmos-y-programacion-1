def identidad(n):
	"""Imprime la matriz identidad de dimensión n"""
	for i in range(n):
		for x in range(n):
			if i != x:
				print (0, end = "")
			else:
				print (1, end = "")
		print("")


