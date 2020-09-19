def pedir_entero(mensaje, minn, maxx):
	"""Dade un mensaje, un mínimo y un maximo; le pide al usuario que ingrese
	un entero entre estos valores"""
	X = f"Por favor ingrese un número entero entre {minn} y {maxx}"

	while True:
		n = input(f"{mensaje} entre {minn} y {maxx}: ")

		if n == "":
			print (X)
			continue

		#Corroboro que la cadena sea un entero positivo o negativo
		if n[0] == "-":
			if not n[1 : ].isdigit():
				print (X)
				continue
		else:
			if not n.isdigit():
				print (X)
				continue

		#Corroborar que esté entre min y max
		if not minn <= int(n) <= maxx:
			print (X)
			continue

		return n

