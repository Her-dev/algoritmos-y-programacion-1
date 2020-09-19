def dias_numero_a_string(n):
	"""Dado un numero de día (1 a 366) y asumiendo que el año arrancó un lunes, devuelva que día de la semana es"""
	for i in range(1,366,7):
		if n == i:
			return ("Lunes")
			
	
	for i in range(2,366,7):
		if n == i:
			return ("Martes")
			

	for i in range(3,366,7):
		if n == i:
			return ("Miercoles")
			

	for i in range(4,366,7):
		if n == i:
			return ("Jueves")
			

	for i in range(5,366,7):
		if n == i:
			return ("Viernes")
			

	for i in range(6,366,7):
		if n == i:
			return ("Sábado")

	for i in range(7,366,7):
		if n == i:
			return "Domingo"
			

print (dias_numero_a_string(355))
print (dias_numero_a_string(3))
print (dias_numero_a_string(9))
