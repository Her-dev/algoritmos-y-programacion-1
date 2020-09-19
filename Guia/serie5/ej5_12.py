def corrector_parciales(cantidad,porcentaje):
	"""Dada la cantidad de ejercicios por parcial y el porcentaje para aprobar,
	pregunta cuantos ejercicios correctos se tiene e imprime si aprobó o no"""
	while True:
		cant = int(input("Ingrese la cantidad de ejercicios bien realizados (-1 para salir): "))
		if cant == -1:
			break
		porcent = cant / cantidad

		if porcent >= porcentaje:
			print(f"El alumno tiene un {porcent} del examen bien hecho, por lo que aprobó")
		else:
			print(f"El alumno tiene un {porcent} del examen bien, por lo que reprobó")

corrector_parciales(10,0.5)