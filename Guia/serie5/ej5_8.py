def ingreso_suma_promedio():
	"""Pregunt al usuario por numeros y devuelve cuantos ingreso, su suma y su promedio"""
	suma = 0
	cuantos = 0

	while True:
		n = int(input("Ingrese un número (-1 para finalizar): "))

		if n == -1:
			break

		suma += n
		cuantos += 1
		prom = suma / cuantos

	print(f"Fueron ingresados {cuantos} números, que suman {suma} y promedian {prom}")

ingreso_suma_promedio()