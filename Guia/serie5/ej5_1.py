def promedio_notas():
	"""Pregunta al usuario notas e imprime su promedio"""
	mas_notas = "si"
	suma_notas = 0
	contador = 0

	while mas_notas == "si":

		suma_notas += int(input("Ingrese una nota: "))
		contador += 1

		print ("El promedio es: ", suma_notas / contador)

		mas_notas = input("Quiere seguir ingresando notas <si - no>: ")

promedio_notas()



